/* Attestation Rulebook Explorer.
   No dependencies. Reads branding.json for the theme and index.json for the data,
   both generated or edited in this repository. */
(function () {
  "use strict";

  var brand = null;
  var data = null;
  var state = { q: "", cats: new Set(), fmts: new Set(), sort: "name", page: 1, perPage: 12 };

  var $ = function (id) { return document.getElementById(id); };

  var ICON_COPY = '<svg class="ico ico-copy" viewBox="0 0 24 24" aria-hidden="true">' +
    '<rect x="9" y="9" width="11" height="11" rx="2"></rect>' +
    '<path d="M5 15V5a2 2 0 0 1 2-2h10"></path></svg>';
  var ICON_DONE = '<svg class="ico ico-done" viewBox="0 0 24 24" aria-hidden="true">' +
    '<path d="M5 13l4 4L19 7"></path></svg>';

  /* every identifier is something a reader will want to paste somewhere */
  function copyable(value, inner) {
    return '<button type="button" class="copy" data-copy="' + esc(value) +
           '" aria-label="Copy" title="Copy">' + inner + ICON_COPY + ICON_DONE + "</button>";
  }

  function copyText(value) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(value).catch(function () { copyFallback(value); });
      return;
    }
    copyFallback(value);
  }

  function copyFallback(value) {
    var ta = document.createElement("textarea");
    ta.value = value;
    ta.setAttribute("readonly", "");
    ta.style.position = "fixed";
    ta.style.opacity = "0";
    document.body.appendChild(ta);
    ta.select();
    try { document.execCommand("copy"); } catch (err) { /* nothing else to try */ }
    document.body.removeChild(ta);
  }

  /* a short explanation of a label, shown on hover and on keyboard focus */
  function help(tip) {
    if (!tip) return "";
    return '<button type="button" class="help" aria-label="What this means" data-tip="' +
           esc(tip) + '">?</button>';
  }

  function setText(id, value) {
    var el = $(id);
    if (el) el.textContent = value;
  }

  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  function highlight(text, needle) {
    var t = esc(text);
    if (!needle) return t;
    var safe = needle.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    return t.replace(new RegExp("(" + safe + ")", "ig"), "<mark>$1</mark>");
  }

  /* ---------------------------------------------------------------- theme */
  function applyBranding(b) {
    var r = document.documentElement.style;
    var t = b.theme || {};
    var map = {
      brand: "--brand", brandDark: "--brand-dark", brandLight: "--brand-light",
      accent: "--accent", accentDark: "--accent-dark", ink: "--ink",
      muted: "--muted", line: "--line", surface: "--surface",
      canvas: "--canvas", radius: "--radius", font: "--font",
      headingFont: "--heading-font", headerGradient: "--header-gradient",
      monoFont: "--mono-font"
    };
    Object.keys(map).forEach(function (k) {
      if (t[k]) r.setProperty(map[k], t[k]);
    });

    if (t.webFonts) {
      var link = document.createElement("link");
      link.rel = "stylesheet";
      link.href = t.webFonts;
      document.head.appendChild(link);
    }

    document.title = b.productName + " | " + b.name;
    setText("brandProduct", b.productName);
    setText("pageTagline", b.tagline || "");
    if (b.copyright) {
      setText("copyright", "\u00a9 Copyright " + new Date().getFullYear() + " " +
                            b.copyright + ". All Rights Reserved.");
    }
    // The masthead logo returns to the top of the explorer rather than leaving
    // for the organisation site, which the footer logo already covers.
    var bl = $("brandLink");
    if (bl) {
      bl.href = "./";
      bl.addEventListener("click", function (e) {
        e.preventDefault();
        state.q = "";
        state.cats.clear();
        state.fmts.clear();
        state.page = 1;
        $("q").value = "";
        document.querySelectorAll(".chip.is-on").forEach(function (el) {
          el.classList.remove("is-on");
        });
        render();
        window.scrollTo({ top: 0, behavior: "smooth" });
      });
    }
    if (b.repositoryUrl && $("repoLink")) $("repoLink").href = b.repositoryUrl;
    if (b.repositoryUrl && $("genRepo")) $("genRepo").href = b.repositoryUrl;
    if (b.logo && $("brandLogo")) {
      $("brandLogo").src = b.logo;
      $("brandLogo").alt = b.logoAlt || b.name;
      if (b.logoHeight) $("brandLogo").height = b.logoHeight;
    } else if ($("brandLogo")) {
      $("brandLogo").remove();
    }
    if (b.favicon && $("favicon")) $("favicon").href = b.favicon;

    if ($("footSite") && b.siteUrl) $("footSite").href = b.siteUrl;
    var fl = $("footLogo");
    if (fl) {
      if (b.footerLogo || b.logo) {
        fl.src = b.footerLogo || b.logo;
        fl.alt = b.logoAlt || b.name;
      } else { fl.remove(); }
    }
    var eu = $("footEu");
    if (eu) {
      if (b.footerEmblem) { eu.src = b.footerEmblem; }
      else { eu.remove(); }
    }
  }

  function catColour(cat) {
    var c = (brand && brand.categoryColours) || {};
    return c[cat] || "var(--brand)";
  }

  /* ----------------------------------------------------------- repo links */
  function fileUrl(path) {
    var base = (brand && brand.repositoryUrl) || "";
    return base ? base + "/blob/main/" + path : "#";
  }

  /* --------------------------------------------------------------- search */
  function matches(rb) {
    if (state.cats.size) {
      var hit = rb.categories.some(function (c) { return state.cats.has(c); });
      if (!hit) return null;
    }
    if (state.fmts.size) {
      var f = rb.formats.some(function (x) { return state.fmts.has(x); });
      if (!f) return null;
    }

    var q = state.q.trim().toLowerCase();
    if (!q) return { attrs: [] };

    var attrHits = rb.attributes.filter(function (a) {
      return a.name.toLowerCase().indexOf(q) !== -1;
    });

    var inDoc =
      rb.title.toLowerCase().indexOf(q) !== -1 ||
      rb.slug.toLowerCase().indexOf(q) !== -1 ||
      (rb.vct || "").toLowerCase().indexOf(q) !== -1 ||
      rb.categories.join(" ").toLowerCase().indexOf(q) !== -1;

    if (inDoc || attrHits.length) return { attrs: attrHits };
    return null;
  }

  /* ---------------------------------------------------------------- views */
  function card(rb, hit) {
    var cat = rb.categories[0] || "";
    var el = document.createElement("button");
    el.className = "card";
    el.type = "button";
    el.style.setProperty("--cat", catColour(cat));

    var tags = rb.categories.map(function (c) {
      return '<span class="tag cat" style="background:' + catColour(c) + '">' + esc(c) + "</span>";
    }).join("") + rb.formats.map(function (f) {
      return '<span class="tag fmt">' + esc(f) + "</span>";
    }).join("");

    var hits = "";
    if (hit && hit.attrs.length) {
      var shown = hit.attrs.slice(0, 6).map(function (a) {
        return "<code>" + highlight(a.name, state.q) + "</code>";
      }).join("");
      var more = hit.attrs.length > 6 ? " and " + (hit.attrs.length - 6) + " more" : "";
      hits = '<div class="hits"><b>' + hit.attrs.length +
             (hit.attrs.length === 1 ? " attribute" : " attributes") + "</b> match: " +
             shown + esc(more) + "</div>";
    }

    el.innerHTML =
      "<h2>" + highlight(rb.title, state.q) + "</h2>" +
      '<div class="slug">' + esc(rb.slug) + "</div>" +
      '<div class="tags">' + tags + "</div>" +
      '<div class="meta">' +
        "<span>" + rb.attributeCount + " attributes</span>" +
        (rb.schemas.length ? "<span>" + rb.schemas.length + " schema" +
          (rb.schemas.length > 1 ? "s" : "") + "</span>" : "<span>no schema</span>") +
        (rb.onTemplate ? "" : "<span>not on template</span>") +
      "</div>" +
      (rb.vct ? '<div class="vct">' + highlight(rb.vct, state.q) + "</div>" : "") +
      hits;

    el.addEventListener("click", function () { openDetail(rb); });
    return el;
  }

  /* the page behind the drawer must not scroll or bounce while it is open */
  function lockPage(on) {
    var root = document.documentElement;
    if (on) {
      var bar = window.innerWidth - root.clientWidth;
      root.style.overflow = "hidden";
      if (bar > 0) { document.body.style.paddingRight = bar + "px"; }
      return;
    }
    root.style.overflow = "";
    document.body.style.paddingRight = "";
  }

  /* the identifier an attribute carries depends on the encoding, so the table
     follows the chapter 5 mapping for whichever format is selected */
  var detailFmt = "";

  function encodingRows(rb, fmt) {
    var map = {};
    ((rb.encodings || {})[fmt] || []).forEach(function (e) {
      map[e.data.toLowerCase()] = e;
    });
    return map;
  }

  function attrTable(rb, fmt) {
    if (!rb.attributes.length) {
      return "<p>No attributes were extracted from chapter 3.</p>";
    }
    var map = fmt ? encodingRows(rb, fmt) : null;
    var rows = rb.attributes.map(function (a) {
      if (!map) {
        return "<tr><td>" + copyable(a.name, "<code>" + esc(a.name) + "</code>") +
               "</td><td>" + esc(a.presence) + "</td><td>" +
               esc(a.definition || "") + "</td></tr>";
      }
      var e = map[a.name.toLowerCase()];
      var ident = copyable(a.name, "<code>" + esc(a.name) + "</code>");
      var note = "";
      if (e && e.identifier) {
        ident = copyable(e.identifier, "<code>" + esc(e.identifier) + "</code>");
        if (e.identifier.toLowerCase() !== a.name.toLowerCase()) {
          note = '<span class="sub">' + esc(a.name) + "</span>";
        }
      } else if (e) {
        ident = '<span class="sub">not encoded in this format</span>';
      }
      return "<tr><td>" + ident + note + "</td><td>" + esc(a.presence) + "</td><td>" +
             (e && e.encoding ? "<code>" + esc(e.encoding) + "</code>" : "") +
             "</td><td>" + esc(a.definition || "") + "</td></tr>";
    }).join("");

    var head = fmt
      ? "<tr><th>Identifier</th><th>Presence</th><th>Encoding</th><th>Definition</th></tr>"
      : "<tr><th>Identifier</th><th>Presence</th><th>Definition</th></tr>";
    return '<table class="' + (fmt ? "byformat" : "plain") + '"><thead>' + head +
           "</thead><tbody>" + rows + "</tbody></table>";
  }

  function openDetail(rb) {
    var body = $("detailBody");
    var fmts = (rb.formats || []).filter(function (f) {
      return rb.encodings && rb.encodings[f];
    });
    var fmt = fmts.length ? (fmts.indexOf(detailFmt) !== -1 ? detailFmt : fmts[0]) : "";

    function block(title, inner, tip) {
      return '<section class="detail-block"><h3>' + esc(title) + help(tip) + "</h3>" +
             inner + "</section>";
    }

    var picker = "";
    if (fmts.length > 1) {
      picker = '<div class="seg" id="fmtSeg">' + fmts.map(function (f) {
        return '<button type="button" class="segbtn' + (f === fmt ? " on" : "") +
               '" data-fmt="' + esc(f) + '">' + esc(f) + "</button>";
      }).join("") + "</div>";
    } else if (fmts.length === 1) {
      picker = '<span class="fmtnote">' + esc(fmts[0]) + "</span>";
    }

    body.innerHTML =
      '<header class="detail-head">' +
        "<h2>" + esc(rb.title) + "</h2>" +
        '<div class="slug">' + esc(rb.slug) + "</div>" +
      "</header>" +
      '<div class="detail-body">' +
        (rb.categoryDeclared
          ? block("Category as declared", "<p>" + esc(rb.categoryDeclared) + "</p>",
                  "The Category line as written at the top of the rulebook, before it " +
                  "is matched to the six known categories.") : "") +
        (rb.vct
          ? block("Credential type",
                  "<p>" + copyable(rb.vct, "<code>" + esc(rb.vct) + "</code>") + "</p>",
                  "The vct value that identifies this attestation type to a wallet " +
                  "or a relying party.") : "") +
        (rb.schemas.length
          ? block("Schema artefacts", "<ul>" + rb.schemas.map(function (s) {
              return '<li><a href="' + fileUrl(s.path) + '" target="_blank" rel="noopener"><code>' +
                     esc(s.path) + "</code></a> (" + s.propertyCount + " properties)</li>";
            }).join("") + "</ul>",
            "The machine readable schema files for this attestation, kept under " +
            "data-schemas in this repository.") : "") +
        '<section class="detail-block">' +
          '<div class="blockhead"><h3>Attributes (' + rb.attributeCount + ")" +
          help("The attributes defined in chapter 3 of the rulebook. The identifier " +
               "and the encoding are the ones chapter 5 gives for the selected format.") +
          "</h3>" + picker + "</div>" +
          '<div id="attrTable">' + attrTable(rb, fmt) + "</div>" +
        "</section>" +
      "</div>";

    var seg = $("fmtSeg");
    if (seg) {
      seg.addEventListener("click", function (e) {
        var b = e.target.closest(".segbtn");
        if (!b) return;
        detailFmt = b.getAttribute("data-fmt");
        seg.querySelectorAll(".segbtn").forEach(function (x) {
          x.classList.toggle("on", x === b);
        });
        $("attrTable").innerHTML = attrTable(rb, detailFmt);
      });
    }

    var open = $("openRulebook");
    if (open) { open.href = fileUrl(rb.path); }

    lockPage(true);
    $("detail").showModal();
  }

  function byName(a, b) { return a.title.localeCompare(b.title); }

  function sorted(list) {
    var by = state.sort;
    var cmp = {
      name: byName,
      "name-desc": function (a, b) { return b.title.localeCompare(a.title); },
      attrs: function (a, b) { return b.attributeCount - a.attributeCount ||
                                      a.title.localeCompare(b.title); },
      "attrs-asc": function (a, b) { return a.attributeCount - b.attributeCount ||
                                            a.title.localeCompare(b.title); },
      category: function (a, b) {
        var ia = data.categories.indexOf(a.categories[0]);
        var ib = data.categories.indexOf(b.categories[0]);
        if (ia < 0) ia = 99;
        if (ib < 0) ib = 99;
        return ia - ib || a.title.localeCompare(b.title);
      }
    }[by] || byName;
    return list.slice().sort(cmp);
  }

  function renderPager(pages) {
    var nav = $("pager");
    if (!nav) return;
    if (pages <= 1) { nav.hidden = state.perPage === 0 ? false : true; }
    else { nav.hidden = false; }
    if (state.perPage === 0) nav.hidden = false;

    var list = $("pageList");
    list.innerHTML = "";
    if (pages > 1) {
      // first, last, and a window around the current page
      var want = {}, i;
      want[1] = want[pages] = 1;
      for (i = state.page - 1; i <= state.page + 1; i++) {
        if (i >= 1 && i <= pages) want[i] = 1;
      }
      var nums = Object.keys(want).map(Number).sort(function (a, b) { return a - b; });
      var prev = 0;
      nums.forEach(function (p) {
        if (p - prev > 1) {
          var gap = document.createElement("span");
          gap.className = "pagegap";
          gap.textContent = "\u2026";
          list.appendChild(gap);
        }
        var b = document.createElement("button");
        b.type = "button";
        b.className = "pagenum" + (p === state.page ? " is-on" : "");
        b.textContent = p;
        if (p === state.page) b.setAttribute("aria-current", "page");
        b.addEventListener("click", function () { goto(p); });
        list.appendChild(b);
        prev = p;
      });
    }
    nav.querySelectorAll(".pagebtn").forEach(function (b) {
      var step = Number(b.dataset.step);
      b.disabled = pages <= 1 ||
                   (step < 0 && state.page === 1) ||
                   (step > 0 && state.page === pages);
    });
  }

  function goto(page) {
    var grid = $("results");

    // A short last page collapses the document, so the browser clamps the
    // scroll position before the smooth scroll runs and the page appears to
    // jump twice. Hold the grid at its current height until the scroll has
    // settled, then release it.
    var held = grid.offsetHeight;
    grid.style.minHeight = held + "px";

    state.page = page;
    render();

    var target = grid.getBoundingClientRect().top + window.scrollY - 84;
    target = Math.max(0, target);

    if (Math.abs(target - window.scrollY) < 2) {
      grid.style.minHeight = "";
      return;
    }

    window.scrollTo({ top: target, behavior: "smooth" });

    // Release once the scroll stops, or after a ceiling if it is interrupted.
    var last = -1, idle = 0;
    var tick = window.setInterval(function () {
      if (Math.round(window.scrollY) === last) {
        if (++idle > 2) { window.clearInterval(tick); grid.style.minHeight = ""; }
      } else { idle = 0; }
      last = Math.round(window.scrollY);
    }, 60);
    window.setTimeout(function () {
      window.clearInterval(tick);
      grid.style.minHeight = "";
    }, 900);
  }

  function render() {
    var out = $("results");
    out.innerHTML = "";

    var shown = [];
    sorted(data.rulebooks).forEach(function (rb) {
      var hit = matches(rb);
      if (hit) shown.push({ rb: rb, hit: hit });
    });

    var n = shown.length;
    var per = state.perPage;
    var pages = per > 0 ? Math.max(1, Math.ceil(n / per)) : 1;
    if (state.page > pages) state.page = pages;

    var slice = per > 0 ? shown.slice((state.page - 1) * per, state.page * per) : shown;
    slice.forEach(function (x) { out.appendChild(card(x.rb, x.hit)); });

    $("empty").hidden = n > 0;
    var total = data.rulebooks.length;
    var label = n === total ? total + " rulebooks" : n + " of " + total + " rulebooks";
    if (per > 0 && n > per) {
      var from = (state.page - 1) * per + 1;
      var to = Math.min(state.page * per, n);
      label += ", showing " + from + " to " + to;
    }
    $("resultCount").textContent = label;

    renderPager(pages);

    var filtered = state.q || state.cats.size || state.fmts.size;
    $("reset").hidden = !filtered;
    $("clear").hidden = !state.q;
  }

  /* --------------------------------------------------------------- chrome */
  function counts(key) {
    var c = {};
    data.rulebooks.forEach(function (rb) {
      (rb[key] || []).forEach(function (v) { c[v] = (c[v] || 0) + 1; });
    });
    return c;
  }

  function buildFilters() {
    var catCounts = counts("categories");
    var catBox = $("catFilters");
    data.categories.forEach(function (cat) {
      var n = catCounts[cat] || 0;
      var b = document.createElement("button");
      b.className = "chip";
      b.type = "button";
      b.innerHTML = '<span class="dot" style="background:' + catColour(cat) + '"></span>' +
                    esc(cat) + ' <span class="n">' + n + "</span>";
      b.disabled = n === 0;
      if (n === 0) b.style.opacity = ".45";
      b.addEventListener("click", function () {
        if (state.cats.has(cat)) { state.cats.delete(cat); b.classList.remove("is-on"); }
        else { state.cats.add(cat); b.classList.add("is-on"); }
        state.page = 1;
        render();
      });
      catBox.appendChild(b);
    });

    var fmtCounts = counts("formats");
    var fmtBox = $("fmtFilters");
    Object.keys(fmtCounts).sort().forEach(function (f) {
      var b = document.createElement("button");
      b.className = "chip";
      b.type = "button";
      b.innerHTML = esc(f) + ' <span class="n">' + fmtCounts[f] + "</span>";
      b.addEventListener("click", function () {
        if (state.fmts.has(f)) { state.fmts.delete(f); b.classList.remove("is-on"); }
        else { state.fmts.add(f); b.classList.add("is-on"); }
        state.page = 1;
        render();
      });
      fmtBox.appendChild(b);
    });
  }

  function buildStats() {
    var c = data.counts;
    setText("summary",
      "\u00b7 " + c.attributes + " attributes across " + c.rulebooks +
      " rulebooks, " + c.withSchema + " with a schema");
    setText("generated", data.generated);
  }

  function wire() {
    var q = $("q");
    var timer = null;
    q.addEventListener("input", function () {
      clearTimeout(timer);
      timer = setTimeout(function () { state.q = q.value; state.page = 1; render(); }, 90);
    });
    $("clear").addEventListener("click", function () {
      q.value = ""; state.q = ""; state.page = 1; render(); q.focus();
    });
    $("reset").addEventListener("click", function () {
      q.value = "";
      state = { q: "", cats: new Set(), fmts: new Set(), sort: "name",
                page: 1, perPage: state.perPage };
      $("sort").value = "name";
      document.querySelectorAll(".chip.is-on").forEach(function (el) {
        el.classList.remove("is-on");
      });
      render();
    });
    document.querySelectorAll(".eg").forEach(function (el) {
      el.addEventListener("click", function () {
        q.value = el.dataset.q;
        state.q = el.dataset.q;
        state.page = 1;
        render();
        q.focus();
      });
    });
    $("sort").addEventListener("change", function () {
      state.sort = this.value;
      state.page = 1;
      render();
    });
    $("perPage").addEventListener("change", function () {
      state.perPage = Number(this.value);
      state.page = 1;
      render();
    });
    document.querySelectorAll(".pagebtn").forEach(function (b) {
      b.addEventListener("click", function () {
        goto(state.page + Number(b.dataset.step));
      });
    });
    $("closeDetail").addEventListener("click", function () { $("detail").close(); });
    $("detail").addEventListener("click", function (e) {
      if (e.target === $("detail")) $("detail").close();
    });
    $("detailBody").addEventListener("click", function (e) {
      var b = e.target.closest(".copy");
      if (!b) return;
      copyText(b.getAttribute("data-copy"));
      b.classList.add("done");
      window.setTimeout(function () { b.classList.remove("done"); }, 1200);
    });
    new MutationObserver(function () {
      if (!$("detail").open) lockPage(false);
    }).observe($("detail"), { attributes: true, attributeFilter: ["open"] });
  }

  /* ----------------------------------------------------------------- boot */
  Promise.all([
    fetch("branding.json").then(function (r) { return r.json(); }).catch(function () { return {}; }),
    fetch("index.json").then(function (r) {
      if (!r.ok) throw new Error("index.json not found");
      return r.json();
    })
  ]).then(function (res) {
    brand = res[0];
    data = res[1];
    applyBranding(brand);
    buildStats();
    buildFilters();
    wire();
    render();
  }).catch(function (err) {
    document.querySelector("main").innerHTML =
      '<p class="empty">The explorer could not load its index. ' +
      "Run <code>python3 explorer/scripts/build_index.py</code> from the repository root.<br>" +
      esc(err.message) + "</p>";
  });
})();
