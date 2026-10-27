#!/usr/bin/env python3
"""Build the rulebook explorer index.

Walks every attestation rulebook, extracts the fields the explorer needs, and
writes explorer/index.json. Run from the repository root:

    python3 explorer/scripts/build_index.py

Use --check to verify the committed index matches the rulebooks without
rewriting it. That is what CI runs.

Everything here reads the generic template structure. Where a rulebook does not
follow it, the field is left empty and counted in the coverage report rather
than guessed at.
"""
import argparse
import difflib
import json
import os
import re
import sys
from datetime import date, timezone, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RULEBOOKS = os.path.join(ROOT, "rulebooks")
SCHEMAS = os.path.join(ROOT, "data-schemas")
OUT = os.path.join(ROOT, "explorer", "index.json")

# rb-base holds shared chapters cited by other rulebooks, not an attestation.
NOT_ATTESTATIONS = {"rb-base", "templates"}

# The six categories of the WE BUILD category model. Anything else is reported
# as unrecognised rather than silently bucketed.
CATEGORIES = [
    ("PID", r"\bPID\b"),
    ("EBWOID", r"\bEBWOID\b"),
    ("QEAA", r"\bQEAA\b"),
    ("PuB-EAA", r"\bPuB-EAA\b"),
    ("S-EAA", r"\bS-EAA\b|self-issued EAA|self-attested"),
    ("non-qualified EAA", r"non-qualified EAA"),
]

FORMAT_ROWS = {
    "mdoc": r"ISO/IEC 18013-5",
    "SD-JWT VC": r"SD-JWT VC",
    "W3C VCDM": r"W3C VCDM",
}


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def split_row(line):
    """Split a markdown table row into cells, respecting code spans."""
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    cells, buf, tick, i = [], "", False, 0
    while i < len(s):
        c = s[i]
        if c == "`":
            tick = not tick
            buf += c
        elif c == "\\" and i + 1 < len(s):
            buf += s[i:i + 2]
            i += 1
        elif c == "|" and not tick:
            cells.append(buf)
            buf = ""
        else:
            buf += c
        i += 1
    cells.append(buf)
    return [c.strip() for c in cells]


def is_separator(cells):
    return bool(cells) and all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c)


def section(text, start_pat, stop_pat):
    """Lines between two headings, the start heading excluded.

    If the stop heading is absent, the section still ends at the next heading
    of the same or a higher level. Without that bound a missing stop heading
    swallows the rest of the document, which pulled the references chapter in
    as though it were a table of attributes.
    """
    lines = text.split("\n")
    a = b = None
    level = None
    for i, l in enumerate(lines):
        if a is None:
            if re.match(start_pat, l):
                a = i + 1
                m = re.match(r"^(#+) ", l)
                level = len(m.group(1)) if m else 6
            continue
        if re.match(stop_pat, l):
            b = i
            break
        m = re.match(r"^(#+) ", l)
        if m and len(m.group(1)) <= level:
            b = i
            break
    if a is None:
        return ""
    return "\n".join(lines[a:b if b is not None else len(lines)])


def tables(block):
    """Every table in a block, as a list of {header, rows}."""
    out, lines, i = [], block.split("\n"), 0
    while i < len(lines):
        if lines[i].lstrip().startswith("|"):
            j = i
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                j += 1
            rows = [split_row(r) for r in lines[i:j]]
            if len(rows) >= 2 and is_separator(rows[1]):
                out.append({"header": rows[0], "rows": [r for r in rows[2:] if any(r)]})
            i = j
            continue
        i += 1
    return out


def dedash(s):
    """Replace em and en dashes. House style allows neither."""
    s = s.replace("\u2014", "\u2013")          # treat them alike
    s = re.sub(r"\s+\u2013\s+", ", ", s)       # spaced, reads as a clause break
    return s.replace("\u2013", "-")             # unspaced, reads as a hyphen


def clean(cell):
    """Strip markdown emphasis, code ticks and links from a cell."""
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", cell)
    s = s.replace("`", "").replace("**", "").replace("*", "")
    return dedash(re.sub(r"\s+", " ", s).strip())


def category_of(text):
    """The declared category line, split into one or more known categories."""
    m = re.search(r"^Category:\s*(.+)$", text, re.M)
    if not m:
        return [], None
    raw = m.group(1).strip()
    found = [name for name, pat in CATEGORIES if re.search(pat, raw, re.I)]
    # "non-qualified EAA" also matches inside "S-EAA ... non-qualified"; keep both,
    # the UI treats category as a set.
    return found, raw


def attributes_of(text):
    """Attribute identifiers from chapter 3, with their presence."""
    out = []
    spans = [
        ("mandatory", r"^### 3\.2 ", r"^### 3\.3 "),
        ("optional", r"^### 3\.3 ", r"^### 3\.4 "),
        ("conditional", r"^### 3\.4 ", r"^## 4 "),
    ]
    for presence, a, b in spans:
        for t in tables(section(text, a, b)):
            head = [h.lower().replace("*", "").strip() for h in t["header"]]
            try:
                idx = next(i for i, h in enumerate(head)
                           if "data identifier" in h or h in ("attribute", "name", "claim"))
            except StopIteration:
                idx = 0
            for row in t["rows"]:
                if idx >= len(row):
                    continue
                name = clean(row[idx])
                if not name or len(name) > 80 or name.lower().startswith("data identifier"):
                    continue
                if re.fullmatch(r"[:\-\s]+", name):
                    continue
                definition = ""
                for i, h in enumerate(head):
                    if "definition" in h or "description" in h:
                        if i < len(row):
                            definition = clean(row[i])
                        break
                out.append({"name": name, "presence": presence, "definition": definition[:300]})
    if not out:
        # Some rulebooks keep their attribute tables under 3.1 subsections
        # rather than 3.2 to 3.4. Fall back to the whole of chapter 3.
        for t in tables(section(text, r"^## 3 Attestation attributes", r"^## 4 ")):
            head = [h.lower().replace("*", "").strip() for h in t["header"]]
            if not any("data identifier" in h or h in ("attribute", "claim") for h in head):
                continue
            idx = next(i for i, h in enumerate(head)
                       if "data identifier" in h or h in ("attribute", "claim"))
            opt = next((i for i, h in enumerate(head)
                        if "optionality" in h or "occurrence" in h or "presence" in h), None)
            for row in t["rows"]:
                if idx >= len(row):
                    continue
                name = clean(row[idx])
                if not name or len(name) > 80 or re.fullmatch(r"[:\-\s]+", name):
                    continue
                presence = "mandatory"
                if opt is not None and opt < len(row):
                    v = clean(row[opt]).lower()
                    if v.startswith("o") or "optional" in v:
                        presence = "optional"
                    elif v.startswith("c") or "conditional" in v:
                        presence = "conditional"
                definition = ""
                for i, h in enumerate(head):
                    if "definition" in h or "description" in h:
                        if i < len(row):
                            definition = clean(row[i])
                        break
                out.append({"name": name, "presence": presence,
                            "definition": definition[:300]})

    # de-duplicate, first presence wins
    seen, uniq = set(), []
    for a in out:
        if a["name"].lower() in seen:
            continue
        seen.add(a["name"].lower())
        uniq.append(a)
    return uniq


def formats_of(text):
    block = section(text, r"^## 5 Formats", r"^### 5\.|^## 6 ")
    supported = []
    whole = section(text, r"^## 5 Formats", r"^## 6 ")
    for t in tables(block):
        head = [h.lower() for h in t["header"]]
        if not any("format" in h for h in head):
            continue
        try:
            sup = next(i for i, h in enumerate(head) if "supported" in h)
        except StopIteration:
            continue
        for row in t["rows"]:
            if sup >= len(row):
                continue
            label = clean(row[0])
            value = clean(row[sup]).lower()
            for name, pat in FORMAT_ROWS.items():
                if re.search(pat, label, re.I) and value.startswith("yes"):
                    supported.append(name)
    if not supported:
        # No formats table. Read the 5.x subsections: a format is supported
        # unless its subsection says it is out of scope or not defined.
        for name, pat in FORMAT_ROWS.items():
            m = re.search(r"^#{3,4} 5\.\d+ .*?" + pat + r".*$", whole, re.M | re.I)
            if not m:
                continue
            body = whole[m.end():]
            nxt = re.search(r"^#{2,4} ", body, re.M)
            body = body[:nxt.start()] if nxt else body
            if re.search(r"out of scope|not defined|does not define|no .{0,20}encoding",
                         body, re.I):
                continue
            if body.strip():
                supported.append(name)
    return sorted(set(supported))


def encodings_of(text, formats):
    """Per format attribute identifiers, read from the chapter 5 tables.

    Chapter 3 names each attribute in an encoding independent way. Chapter 5
    maps those data identifiers onto the identifier the format actually uses,
    so a rulebook carrying two formats has two different attribute lists.
    """
    whole = section(text, r"^## 5 Formats", r"^## 6 ")
    lines = whole.split("\n")
    marks = [i for i, l in enumerate(lines) if re.match(r"^### ", l)]
    out = {}

    for n, start in enumerate(marks):
        stop = marks[n + 1] if n + 1 < len(marks) else len(lines)
        heading = lines[start][4:]
        fmt = next((name for name, pat in FORMAT_ROWS.items()
                    if re.search(pat, heading, re.I)), None)
        if fmt is None or fmt not in formats:
            continue

        rows = out.setdefault(fmt, [])
        seen = {r["data"].lower() for r in rows}
        for t in tables("\n".join(lines[start + 1:stop])):
            head = [clean(h).lower() for h in t["header"]]
            if not head or "data identifier" not in head[0]:
                continue
            ident = next((i for i, h in enumerate(head)
                          if "attribute identifier" in h or "claim name" in h), None)
            if ident is None:
                continue
            enc = next((i for i, h in enumerate(head) if "encoding" in h), None)
            for row in t["rows"]:
                data = clean(row[0]) if row else ""
                if not data or re.fullmatch(r"[:\-\s]+", data):
                    continue
                if data.lower() in seen or len(data) > 80:
                    continue
                name = clean(row[ident]) if ident < len(row) else ""
                if re.fullmatch(r"[:\-\s]*", name):
                    name = ""
                value = clean(row[enc]) if enc is not None and enc < len(row) else ""
                value = re.split(r",? see ", value, 1)[0].strip(" .,")
                rows.append({"data": data, "identifier": name,
                             "encoding": value[:40]})
                seen.add(data.lower())

    return {k: v for k, v in out.items() if v}


def traceability_of(text):
    block = section(text, r"^### 2\.3 Traceability", r"^## 3 ")
    rows = []
    for t in tables(block):
        for row in t["rows"]:
            if not row or not row[0].strip().startswith("EW-DM"):
                continue
            rows.append({
                "requirement": clean(row[0]),
                "applies": clean(row[2]) if len(row) > 2 else "",
            })
    return rows


def schema_index():
    """vct -> schema file, plus every schema file keyed by basename."""
    by_vct, files = {}, {}
    for fmt in ("sd-jwt", "mdoc"):
        d = os.path.join(SCHEMAS, fmt)
        if not os.path.isdir(d):
            continue
        for fn in sorted(os.listdir(d)):
            if not fn.endswith(".json"):
                continue
            path = os.path.join(d, fn)
            try:
                doc = json.load(open(path, encoding="utf-8"))
            except Exception:
                continue
            rel = os.path.relpath(path, ROOT)
            props = doc.get("properties", {})
            files[fn] = {
                "path": rel,
                "format": fmt,
                "title": doc.get("title", ""),
                "properties": sorted(props.keys()),
            }
            const = props.get("vct", {}).get("const")
            if const:
                by_vct[const] = rel
    return by_vct, files


def match_schemas(slug, text, files):
    """Schemas belonging to a rulebook, by filename stem or by vct."""
    stem = slug[3:] if slug.startswith("rb-") else slug
    out = []
    for fn, meta in files.items():
        base = fn.rsplit(".", 1)[0]
        base = re.sub(r"-(sd-jwt|mdoc)$", "", base)
        base = re.sub(r"^ds\d+-", "", base)
        if base == stem or base.replace("-", "") == stem.replace("-", ""):
            out.append(meta)
    return out


def vct_of(text, schemas):
    """Prefer the schema's declared vct; fall back to chapter 5 only."""
    for s in schemas:
        pass  # schema vct is resolved by caller via by_vct
    block = section(text, r"^## 5 Formats", r"^## 6 ")
    m = re.search(r"`(eu\.we-build[.:][A-Za-z0-9.:_-]+|urn:eudi:[A-Za-z0-9:._-]+)`", block)
    return m.group(1) if m else ""


def build():
    by_vct, files = schema_index()
    entries, problems = [], []

    for slug in sorted(os.listdir(RULEBOOKS)):
        d = os.path.join(RULEBOOKS, slug)
        if not os.path.isdir(d) or slug in NOT_ATTESTATIONS:
            continue
        # take the name from the directory listing. A case insensitive file
        # system would otherwise report README.md for a file named readme.md,
        # and the link to it on GitHub would not resolve.
        cand = sorted(f for f in os.listdir(d) if f.lower() == "readme.md")
        if not cand:
            problems.append(f"{slug}: no README.md")
            continue
        path = os.path.join(d, cand[0])

        text = read(path)
        title = ""
        m = re.search(r"^#\s+(.+)$", text, re.M)
        if m:
            title = re.sub(r"^Attestation Rulebook for attestations of type\s*", "", m.group(1)).strip()
            title = re.sub(r"^WE BUILD (Attestation )?Rulebook for attestations of type\s*", "", title).strip()
            title = title.strip("_* ")

        cats, raw_cat = category_of(text)
        on_template = bool(re.search(r"^## 11 References", text, re.M))
        schemas = match_schemas(slug, text, files)
        vct = ""
        for s in schemas:
            for k, v in by_vct.items():
                if v == s["path"]:
                    vct = k
                    break
            if vct:
                break
        if not vct:
            vct = vct_of(text, schemas)

        attrs = attributes_of(text)
        trace = traceability_of(text)
        fmts = formats_of(text)
        encodings = encodings_of(text, fmts)

        if not on_template:
            problems.append(f"{slug}: not on the 11-chapter template")
        if not cats:
            problems.append(f"{slug}: category not recognised ({raw_cat or 'absent'})")
        if not attrs:
            problems.append(f"{slug}: no attributes extracted from chapter 3")

        entries.append({
            "slug": slug,
            "title": title or slug,
            "path": os.path.relpath(path, ROOT),
            "categories": cats,
            "categoryDeclared": raw_cat or "",
            "onTemplate": on_template,
            "vct": vct,
            "formats": fmts,
            "encodings": encodings,
            "attributes": attrs,
            "attributeCount": len(attrs),
            "traceability": trace,
            "schemas": [{"path": s["path"], "format": s["format"],
                         "propertyCount": len(s["properties"])} for s in schemas],
            "lines": len(text.split("\n")),
        })

    # nothing reaches the index with a dash of either kind
    def scrub(node):
        if isinstance(node, str):
            return dedash(node)
        if isinstance(node, list):
            return [scrub(x) for x in node]
        if isinstance(node, dict):
            return {k: scrub(v) for k, v in node.items()}
        return node

    entries = scrub(entries)

    index = {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "repository": "webuild-consortium/webuild-attestation-rulebooks-catalog",
        "categories": [c[0] for c in CATEGORIES],
        "counts": {
            "rulebooks": len(entries),
            "onTemplate": sum(1 for e in entries if e["onTemplate"]),
            "withSchema": sum(1 for e in entries if e["schemas"]),
            "attributes": sum(e["attributeCount"] for e in entries),
        },
        "rulebooks": entries,
    }
    return index, problems


SOURCES = ["index.html", "branding.json", "README.md",
           "assets/app.js", "assets/style.css", "scripts/build_index.py"]


def dash_report():
    """Em or en dashes in the explorer's own source files."""
    bad = []
    base = os.path.join(ROOT, "explorer")
    for rel in SOURCES:
        path = os.path.join(base, rel)
        if not os.path.exists(path):
            continue
        for n, line in enumerate(read(path).split("\n"), 1):
            if "\u2014" in line or "\u2013" in line:
                bad.append(f"explorer/{rel}:{n}: {line.strip()[:80]}")
    return bad


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="fail if the committed index is out of date")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    index, problems = build()
    payload = json.dumps(index, indent=1, ensure_ascii=False) + "\n"

    dashes = dash_report()
    if dashes:
        print(f"em or en dashes found in {len(dashes)} place(s):")
        for d in dashes:
            print(f"  {d}")
        return 1

    if args.check:
        if not os.path.exists(OUT):
            print("explorer/index.json is missing. Run build_index.py.")
            return 1
        current = read(OUT)
        # ignore the generated date when comparing
        a = re.sub(r'"generated": "[^"]*"', "", current)
        b = re.sub(r'"generated": "[^"]*"', "", payload)
        if a != b:
            print("explorer/index.json is out of date. Run build_index.py and commit.")
            diff = difflib.unified_diff(a.split("\n"), b.split("\n"),
                                        "committed", "rebuilt", n=1, lineterm="")
            for n, line in enumerate(diff):
                if n > 40:
                    print("  ...")
                    break
                print("  " + line[:200])
            return 1
        print(f"index is current: {index['counts']['rulebooks']} rulebooks")
        return 0

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(payload)

    if not args.quiet:
        c = index["counts"]
        print(f"wrote {os.path.relpath(OUT, ROOT)}")
        print(f"  rulebooks     {c['rulebooks']}")
        print(f"  on template   {c['onTemplate']}")
        print(f"  with schema   {c['withSchema']}")
        print(f"  attributes    {c['attributes']}")
        by_cat = {}
        for e in index["rulebooks"]:
            for cat in (e["categories"] or ["(unrecognised)"]):
                by_cat[cat] = by_cat.get(cat, 0) + 1
        print("  by category")
        for k in index["categories"] + ["(unrecognised)"]:
            if k in by_cat:
                print(f"    {k:22} {by_cat[k]}")
        if problems:
            print(f"  notes ({len(problems)})")
            for p in problems:
                print(f"    {p}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
