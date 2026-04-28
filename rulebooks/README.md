# Rulebook conventions

This folder contains the WE BUILD attestation rulebooks. Each rulebook is a self-contained document describing a single attestation type, its data model, and the rules that govern its issuance, presentation, and verification.

This README defines the naming and structure convention for rulebooks in this folder. It applies to all new rulebooks and to migrations of existing ones.

## 1. Folder name pattern

Each rulebook lives in its own folder under `rulebooks/`:

```
rulebooks/rb-<slug>/
```

- `rb-` is a constant prefix.
- `<slug>` is lower-case kebab-case. Where an EUDI ARF attestation slug exists (for example `pid`, `mdl`), match it. Otherwise use a short, consortium-defined name.

Regex: `^rb-[a-z0-9-]+$`

Examples:

- `rb-pid`
- `rb-mdl`
- `rb-eucc`
- `rb-eu-poa`
- `rb-ereceipt`
- `rb-organisational-mandate`

## 2. Folder contents

Each rulebook folder contains a single required file:

- `README.md`, the rulebook itself, following the rulebook template at [`rulebooks/EUDI-template.md`](EUDI-template.md).

Authors should not renumber or rename the template's sections. Sections that do not apply to a specific attestation type should be retained with a short note explaining why.

Schemas, samples, machine-readable metadata, and supporting assets are out of scope for this version of the convention. They will be addressed in a follow-up proposal once the per-folder README structure is in place across all rulebooks.

## 3. Governance

- Slugs are agreed in the pull request that introduces the rulebook. If two pull requests propose the same slug, reviewers pick one.
- Slugs are stable once merged. Renames are allowed via a pull request with a clear reason.
- This convention retires the previous `dsNNN-` numbering scheme. Gaps in the old numbering and the placement of the Hello World example alongside numbered rulebooks are resolved by switching to slugs.

## 4. Migration of existing rulebooks

Existing rulebooks move into the new structure as follows:

| Current file | New path |
|---|---|
| `rulebooks/ds001-ebw-oid-rulebook.md` | `rulebooks/rb-ebw-oid/README.md` |
| `rulebooks/ds002-pid-rulebook.md` | `rulebooks/rb-pid/README.md` |
| `rulebooks/ds004-eucc-rulebook.md` | `rulebooks/rb-eucc/README.md` |
| `rulebooks/ds005-hello-world-rulebook.md` | `rulebooks/rb-hello-world/README.md` |
| `rulebooks/ds007-eu-poa-rulebook.md` | `rulebooks/rb-eu-poa/README.md` |
| `rulebooks/rb-e-receipt.md` | `rulebooks/rb-e-receipt/README.md` |

The migration itself will be carried out in a separate pull request. Slugs in this table can be revised before the migration lands; once merged, they are stable.
