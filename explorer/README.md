# Attestation Rulebook Explorer

A static site that lets you search the attestation rulebooks in this repository by
category, by format and by attribute. It has no server and no build dependencies.

## How it works

`scripts/build_index.py` walks every rulebook, reads the generic template structure,
and writes `index.json`. The page loads that one file and does the searching in the
browser.

Parsing happens once, in CI, rather than on every page load. If a rulebook stops
parsing, the build reports it rather than the visitor seeing an empty card.

## Running it locally

From the repository root:

```sh
python3 explorer/scripts/build_index.py
python3 -m http.server 8000 --directory explorer
```

Then open <http://localhost:8000>.

## Keeping the index current

`index.json` is committed so that GitHub Pages can serve it directly. CI runs

```sh
python3 explorer/scripts/build_index.py --check
```

which fails if the committed index no longer matches the rulebooks. When a pull
request changes a rulebook, rebuild the index and commit it in the same change.

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

No CSS or JavaScript changes are needed. The stylesheet reads only the custom
properties that `branding.json` sets, with fallbacks if the file is missing.

## Deployment

`.github/workflows/explorer.yml` publishes the `explorer/` folder to GitHub Pages on
every push to `main`, and checks the index on every pull request. Pages needs to be
enabled once in the repository settings, with the source set to GitHub Actions.
