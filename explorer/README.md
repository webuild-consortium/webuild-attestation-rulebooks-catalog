# Attestation Rulebook Explorer

A static site that lets you search the attestation rulebooks in this repository by
category, by format and by attribute. It has no server and no build dependencies.

## How it works

`scripts/build_index.py` walks every rulebook, reads the generic template structure,
and writes three things: `index.json`, one readable page per rulebook under
`rulebooks/`, and `sitemap.xml` with `robots.txt`. The home page loads the index and
does the searching in the browser.

Parsing happens once, in CI, rather than on every page load. If a rulebook stops
parsing, the build reports it rather than the visitor seeing an empty card.

The build needs Python 3.11 or newer and a pinned Python-Markdown, because the
rendered pages are committed and different releases render the same markdown
differently:

```sh
python3 -m pip install markdown==3.11.2
```

## Running it locally

From the repository root:

```sh
python3 explorer/scripts/build_index.py
python3 -m http.server 8000 --directory explorer
```

Then open <http://localhost:8000>.

## The rulebook pages

Each rulebook is rendered to its own page, `rulebooks/<slug>.html`, with the chapter
list beside the text and every table in its own scroll box. The headings are
slugified the way GitHub does it, so the cross references the authors wrote between
chapters resolve here too. Where one does not resolve, the build says so rather than
leaving a reader to find a dead link.

The rulebook text is rendered as written. The house rule against dashes applies to
this folder's own sources, not to the rulebooks themselves.

A page per rulebook is also what makes a shared link useful: each one carries its own
title, description and social card metadata, which a page built from a query string
could not.

## The social card

`assets/og.png` is the 1200 by 630 image that Slack, LinkedIn and the rest show when
someone shares a link. It is built from `scripts/og-card.html`:

```sh
python3 -m http.server 8000 --directory explorer &
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless \
  --force-device-scale-factor=1 --window-size=1200,630 \
  --screenshot=explorer/assets/og.png \
  http://localhost:8000/scripts/og-card.html
```

## Keeping the index current

Everything generated is committed so that GitHub Pages can serve it directly. CI runs

```sh
python3 explorer/scripts/build_index.py --check
```

which fails if any committed file no longer matches the rulebooks, naming the file
and showing the first differences. When a pull request changes a rulebook, rebuild
and commit in the same change.

## What the index holds

For each rulebook: slug, title, declared category, the categories recognised from it,
whether it is on the 11-chapter template, credential type, supported formats, the
attributes from chapter 3 with their presence and definition, the chapter 5 encoding
tables keyed by format, the chapter 2.3 traceability rows, and any schema artefacts
under `data-schemas/`.

Chapter 3 names each attribute independently of any encoding. Chapter 5 maps those
names onto the identifier a format actually uses, so a rulebook that supports both
SD-JWT VC and mdoc has two attribute lists. The page shows one format at a time and
falls back to the chapter 3 name where chapter 5 does not restate an attribute.

Fields that cannot be read are left empty and reported in the build output rather
than guessed at. The build currently reports `rb-approved-supplier` as not yet on the
template, which is accurate.

## Rebranding

Everything brand-specific lives in `branding.json`. To rebrand, change that file and
replace the two SVGs in `assets/`:

| Key | What it controls |
| --- | --- |
| `name`, `productName`, `tagline` | Masthead and page heading |
| `siteUrl`, `repositoryUrl` | Masthead links, and the base for file links |
| `logo`, `logoAlt`, `favicon` | Images in `assets/` |
| `footerNote` | Footer line |
| `theme` | Colours, corner radius and font, injected as CSS custom properties |
| `categoryColours` | The colour of each category chip |
| `publicUrl` | The deployed address, used for canonical links, social cards and the sitemap |

No CSS or JavaScript changes are needed. The stylesheet reads only the custom
properties that `branding.json` sets, with fallbacks if the file is missing.

## Deployment

`.github/workflows/explorer.yml` publishes the `explorer/` folder to GitHub Pages on
every push to `main`, and checks the generated files on every pull request. Pages is
enabled in the repository settings with the source set to GitHub Actions.
