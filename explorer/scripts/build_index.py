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
SITE = os.path.join(ROOT, "explorer")
OUT = os.path.join(SITE, "index.json")
PAGES = os.path.join(SITE, "rulebooks")
BRANDING = os.path.join(SITE, "branding.json")

# filled from branding.json, the rulebook pages colour their category tags
CATEGORY_COLOURS = {}

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
    # the ARF calls this one simply an EAA. The rulebooks still write
    # "non-qualified EAA", so the text matched and the label differ.
    ("EAA", r"non-qualified EAA"),
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


# ------------------------------------------------------------- rulebook pages

# The rendered pages are committed, so the renderer has to be the same one
# everywhere. Different Python-Markdown releases differ on, among other things,
# how they treat a long run of asterisks inside a table cell.
MARKDOWN_VERSION = "3.11.2"


def need_markdown():
    try:
        import markdown
    except ImportError:
        markdown = None
    if markdown is None or markdown.__version__ != MARKDOWN_VERSION:
        have = markdown.__version__ if markdown else "nothing"
        print(f"This build renders the rulebook pages with Python-Markdown "
              f"{MARKDOWN_VERSION} and found {have}.")
        print(f"    python3 -m pip install markdown=={MARKDOWN_VERSION}")
        print("It needs Python 3.11 or newer.")
        sys.exit(1)
    return markdown


def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def flatten_toc(tokens, out=None):
    """The heading tree as a flat list, which is what a sidebar needs."""
    out = [] if out is None else out
    for t in tokens:
        out.append({"id": t["id"], "name": t["name"], "level": t["level"]})
        flatten_toc(t.get("children", []), out)
    return out


def theme_block(brand):
    """branding.json drives the page, so a rebrand flows into every page."""
    theme = (brand or {}).get("theme") or {}
    names = {
        "brand": "--brand", "brandDark": "--brand-dark", "brandLight": "--brand-light",
        "accent": "--accent", "accentDark": "--accent-dark", "ink": "--ink",
        "muted": "--muted", "line": "--line", "surface": "--surface",
        "canvas": "--canvas", "radius": "--radius", "font": "--font",
        "headingFont": "--heading-font", "monoFont": "--mono-font",
        "headerGradient": "--header-gradient",
    }
    rules = [f"{css}:{theme[key]}" for key, css in names.items() if theme.get(key)]
    return ":root{" + ";".join(rules) + "}" if rules else ""


def page_description(entry):
    bits = []
    if entry["categories"]:
        bits.append(" and ".join(entry["categories"]))
    if entry["formats"]:
        bits.append("issued as " + " or ".join(entry["formats"]))
    bits.append(f"{entry['attributeCount']} attributes")
    return f"{entry['title']}. An attestation rulebook, " + ", ".join(bits) + "."


def strip_toc(text):
    """Drop the document's own table of contents.

    The page carries the chapter list beside the text, so the one written into
    the markdown is a second copy of the same thing. Nothing normative lives in
    it, only links.
    """
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if not re.match(r"^## Table of contents\s*$", line, re.I):
            continue
        for j in range(i + 1, len(lines)):
            if re.match(r"^## ", lines[j]):
                return "\n".join(lines[:i] + lines[j:])
        return "\n".join(lines[:i])
    return text


def render_page(entry, text, brand, problems):
    markdown = need_markdown()
    text = strip_toc(text)
    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "toc", "sane_lists", "attr_list"],
        extension_configs={"toc": {"permalink": False}},
    )
    body = md.convert(text)

    # the authors cross reference chapters by anchor. Report the ones that no
    # longer resolve rather than leaving a reader to find a dead link.
    ids = set(re.findall(r'id="([^"]+)"', body))
    dead = sorted(set(re.findall(r'href="#([^"]+)"', body)) - ids)
    if dead:
        problems.append(f"{entry['slug']}: {len(dead)} cross reference(s) point at "
                        f"a heading that is not there, e.g. #{dead[0]}")

    # every table gets its own scroll box, they are far wider than a phone
    body = body.replace("<table>", '<div class="tablewrap"><table>')
    body = body.replace("</table>", "</table></div>")

    chapters = [t for t in flatten_toc(md.toc_tokens) if t["level"] in (2, 3)]
    nav = "".join(
        f'<a class="lvl{t["level"]}" href="#{esc(t["id"])}">{esc(t["name"])}</a>'
        for t in chapters
    )

    site = (brand or {}).get("publicUrl", "").rstrip("/")
    name = (brand or {}).get("name", "")
    product = (brand or {}).get("productName", "")
    repo = (brand or {}).get("repositoryUrl", "")
    logo = (brand or {}).get("logo", "assets/logo.svg")
    logo_eu = (brand or {}).get("footerEmblem", "assets/logo-eu.svg")
    url = f"{site}/rulebooks/{entry['slug']}.html" if site else ""
    desc = page_description(entry)
    head_title = f"{entry['title']} rulebook"

    tags = "".join(
        f'<span class="tag cat" style="background:{CATEGORY_COLOURS.get(c, "#003399")}">'
        f"{esc(c)}</span>" for c in entry["categories"]
    ) + "".join(f'<span class="tag fmt">{esc(f)}</span>' for f in entry["formats"])

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(head_title)} | {esc(name)}</title>
<meta name="description" content="{esc(desc)}">
{f'<link rel="canonical" href="{esc(url)}">' if url else ''}
<meta property="og:type" content="article">
<meta property="og:site_name" content="{esc(name)} {esc(product)}">
<meta property="og:title" content="{esc(head_title)}">
<meta property="og:description" content="{esc(desc)}">
{f'<meta property="og:url" content="{esc(url)}">' if url else ''}
{f'<meta property="og:image" content="{esc(site)}/assets/og.png?v=2">' if site else ''}
<meta property="og:image:type" content="image/png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{esc(name)} {esc(product)}">
<meta name="twitter:card" content="summary_large_image">
{f'<meta name="twitter:image" content="{esc(site)}/assets/og.png?v=2">' if site else ''}
<meta name="theme-color" content="{esc(((brand or {}).get('theme') or {}).get('brand', '#003399'))}">
<link rel="icon" href="../{esc((brand or {}).get('favicon', 'assets/favicon.svg'))}">
<link rel="stylesheet" href="../assets/style.css">
<style>{theme_block(brand)}</style>
</head>
<body>

<header class="masthead">
  <div class="bar">
    <a class="brand" href="../index.html"><img src="../{esc(logo)}" alt="{esc((brand or {}).get('logoAlt', name))}" height="44"></a>
    <span class="brand-sep" aria-hidden="true"></span>
    <span class="brand-product">{esc(product)}</span>
    <nav class="masthead-links">
      <a class="ghlink" href="{esc(repo)}/blob/main/{esc(entry['path'])}" target="_blank" rel="noopener" title="View this rulebook on GitHub">
        <svg viewBox="0 0 16 16" width="19" height="19" aria-hidden="true"><path fill="currentColor" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82a7.4 7.4 0 0 1 2-.27c.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8Z"/></svg>
        <span>GitHub</span>
      </a>
    </nav>
  </div>
</header>

<div class="doc">
  <aside class="doc-nav">
    <a class="doc-back" href="../index.html">All rulebooks</a>
    <details class="doc-chapters" open>
      <summary>Chapters</summary>
      <nav class="doc-toc" aria-label="Chapters">{nav}</nav>
    </details>
  </aside>
  <article class="doc-body">
    <p class="doc-tags">{tags}</p>
    {body}
  </article>
</div>

<footer class="foot">
  <div class="foot-band">
    <div class="foot-inner">
      <a class="foot-logolink" href="{esc((brand or {}).get('siteUrl', '#'))}" target="_blank" rel="noopener"><img class="foot-logo" src="../{esc(logo)}" alt="{esc((brand or {}).get('logoAlt', name))}" height="56"></a>
      <img class="foot-eu" src="../{esc(logo_eu)}" alt="{esc((brand or {}).get('footerNote', ''))}" height="46">
    </div>
  </div>
  <div class="foot-base">
    <div class="foot-inner">
      <span class="copyright">&copy; Copyright {date.today().year} {esc((brand or {}).get('copyright', name))}. All Rights Reserved.</span>
      <span class="gen">Rendered from <a href="{esc(repo)}/blob/main/{esc(entry['path'])}" target="_blank" rel="noopener">the rulebook</a> in this repository.</span>
    </div>
  </div>
</footer>

<script>
/* the chapter list is open beside the text, and out of the way on a phone */
(function () {{
  var box = document.querySelector(".doc-chapters");
  if (box && window.matchMedia("(max-width: 860px)").matches) box.open = false;
}}());
</script>

</body>
</html>
"""


def build():
    by_vct, files = schema_index()
    entries, problems = [], []
    sources = {}

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

        sources[slug] = text
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
            "page": f"rulebooks/{slug}.html",
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
    return index, problems, sources


SOURCES = ["index.html", "branding.json", "README.md",
           "assets/app.js", "assets/style.css",
           "scripts/build_index.py", "scripts/og-card.html"]


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


def sitemap(index, brand):
    site = (brand or {}).get("publicUrl", "").rstrip("/")
    if not site:
        return ""
    day = index["generated"]
    urls = [f"{site}/"] + [f"{site}/{e['page']}" for e in index["rulebooks"]]
    rows = "".join(
        f"  <url><loc>{esc(u)}</loc><lastmod>{day}</lastmod></url>\n" for u in urls
    )
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + rows + "</urlset>\n")


def artefacts():
    """Everything the build writes, keyed by path relative to explorer/."""
    brand = {}
    if os.path.exists(BRANDING):
        brand = json.loads(read(BRANDING))
    CATEGORY_COLOURS.clear()
    CATEGORY_COLOURS.update(brand.get("categoryColours") or {})

    index, problems, sources = build()
    out = {"index.json": json.dumps(index, indent=1, ensure_ascii=False) + "\n"}

    for entry in index["rulebooks"]:
        out[entry["page"]] = render_page(entry, sources[entry["slug"]], brand, problems)

    site = (brand or {}).get("publicUrl", "").rstrip("/")
    if site:
        out["sitemap.xml"] = sitemap(index, brand)
        out["robots.txt"] = f"User-agent: *\nAllow: /\nSitemap: {site}/sitemap.xml\n"

    return index, problems, out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="fail if the committed files are out of date")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    index, problems, out = artefacts()

    dashes = dash_report()
    if dashes:
        print(f"em or en dashes found in {len(dashes)} place(s):")
        for d in dashes:
            print(f"  {d}")
        return 1

    # the generated date moves on its own, it is not a reason to fail
    def comparable(text):
        text = re.sub(r'"generated": "[^"]*"', "", text)
        return re.sub(r"<lastmod>[^<]*</lastmod>", "", text)

    if args.check:
        stale = []
        for rel, payload in sorted(out.items()):
            path = os.path.join(SITE, rel)
            if not os.path.exists(path):
                stale.append((rel, None, payload))
                continue
            if comparable(read(path)) != comparable(payload):
                stale.append((rel, read(path), payload))
        if stale:
            print(f"{len(stale)} generated file(s) out of date. "
                  "Run build_index.py and commit.")
            for rel, current, payload in stale[:5]:
                if current is None:
                    print(f"  {rel} is missing")
                    continue
                print(f"  {rel}")
                diff = difflib.unified_diff(
                    comparable(current).split("\n"), comparable(payload).split("\n"),
                    "committed", "rebuilt", n=1, lineterm="")
                for n, line in enumerate(diff):
                    if n > 14:
                        print("    ...")
                        break
                    print("    " + line[:180])
            return 1
        print(f"generated files are current: {index['counts']['rulebooks']} rulebooks, "
              f"{len(out)} files")
        return 0

    # a rulebook that goes away must not leave its page behind
    if os.path.isdir(PAGES):
        keep = {os.path.basename(rel) for rel in out if rel.startswith("rulebooks/")}
        for name in os.listdir(PAGES):
            if name.endswith(".html") and name not in keep:
                os.remove(os.path.join(PAGES, name))

    for rel, payload in out.items():
        path = os.path.join(SITE, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(payload)

    if not args.quiet:
        c = index["counts"]
        print(f"wrote {len(out)} files under {os.path.relpath(SITE, ROOT)}/")
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
