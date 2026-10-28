# Contributing to WE BUILD Attestation Rulebooks and Schemas

Contributions that improve the clarity, correctness and coverage of the rulebooks and
schemas are welcome. This guide covers how to make a change and what happens to it.

## Making a change

Small edits are easiest in the GitHub editor: open the file, edit it, and GitHub will
offer to create a branch and a pull request for you. Nothing has to be built or
generated on your machine.

For larger work, clone the repository, branch from `main`, and open a pull request
when you are ready. Name the branch after what it does, for example
`feat/rb-taxid-revocation` or `fix/rb-pid-cross-references`. Contributors outside the
consortium can fork and open a pull request from the fork.

## Adding or changing a rulebook

**Every rulebook follows the generic template.** It is fixed at eleven chapters and
they are not renumbered or renamed. Read
[`rulebooks/README.md`](rulebooks/README.md) before you start writing. It lists the
chapters, explains how to name the folder, and tells you where to begin.

The two documents you need:

- [`rulebooks/templates/webuild-rulebook-generic-template.md`](rulebooks/templates/webuild-rulebook-generic-template.md),
  the template itself. Copy it to `rulebooks/rb-<slug>/README.md` and fill it in.
- [`rulebooks/templates/README.md`](rulebooks/templates/README.md), which explains the
  markers in the template, the requirement identifiers, and the checklist to run
  through before you submit.

While writing:

- Use RFC 2119 key words, `SHALL`, `SHOULD` and `MAY`, for anything normative, and
  lower case `must` only for a constraint imposed by some other document.
- Keep terminology consistent with the ARF and with the rulebooks already here.
- Give every attribute a definition, a presence, and a semantic reference where one
  exists.
- Strip the `FIXED`, `[AUTHOR]` and `TO AGREE` markers before you ask for review.
  None of them belong in a finished rulebook.

Every merged rulebook is published on the
[rulebook explorer](https://webuild-consortium.github.io/webuild-attestation-rulebooks-catalog/),
with its own page, built automatically from this repository.

## Adding or changing a schema

Schemas live under [`data-schemas/`](data-schemas), organised by format, currently
`sd-jwt/`, `mdoc/` and `display/`.

- Name a new schema after the rulebook slug and the format,
  for example `approved-supplier-sd-jwt.json`. Some older files still carry the
  retired `ds###` numbering; leave those names alone rather than renumbering them.
- Include at least one sample in the matching `sample-data/` folder, named after the
  schema with `-sample` appended.
- Use JSON Schema draft-07 or later, with `$schema`, `$id`, `title`, `description`,
  `type` and `version` present.
- Reference the schema from chapter 3 of the rulebook it belongs to, so a reader can
  find it from the document.

## What runs on your pull request

Two checks, both automatic:

- **Schema validation**, from
  [`validate-schemas.yml`](.github/workflows/validate-schemas.yml). It checks that
  every JSON file is well formed, that samples conform to their schema, and that each
  schema has a sample.
- **The explorer build**, from
  [`explorer.yml`](.github/workflows/explorer.yml). It reads every rulebook and renders
  every page without writing anything, and fails only if a rulebook can no longer be
  read or rendered. It prints what it makes of the rulebooks, including any that are
  off template or carry a stale cross reference. Those are reported, not enforced.

You never need to commit generated files. The explorer is built when the site
deploys.

## Review and merge

Open the pull request against `main` and describe what the change does and why,
referencing any related issue or external specification. A rulebook change should name
the authors as reviewers. Expect at least one approving review before merge, and
respond to comments rather than force pushing over them.

Keep a pull request to one subject. Separate unrelated changes.

## Style

- British English.
- Lower case with hyphens for file and folder names.
- Commit messages that say what changed and why.
- Prefer additive changes. If something has to break, say so in the pull request.

## Licence

This project is licensed under the [Apache Licence, Version 2.0](LICENCE). By
contributing, you agree that your contributions are licensed under the same terms.
