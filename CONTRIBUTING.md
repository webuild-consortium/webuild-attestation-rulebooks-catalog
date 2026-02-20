# Contributing to WE BUILD Attestation Rulebooks and Schemas

We welcome contributions that improve clarity, correctness, and coverage of rulebooks and schemas. This guide explains how to get involved.

## Getting started

1. **Fork** the repository and clone it locally.
2. Create a feature branch from `main`:
   - Branch name suggestion: `feat/<area>-<short-description>` or `fix/<area>-<short-description>`.
3. Make your changes (see sections below).
4. Validate your changes locally before opening a pull request.

## Rulebook contributions

- Edit or add Markdown files under `rulebooks/`.
- Use the [EUDI-template.md](rulebooks/EUDI-template.md) as a starting point for new rulebooks.
- Keep terminology consistent with EUDI specifications and the existing rulebooks.
- Use RFC 2119 keywords (`SHALL`, `SHOULD`, `MAY`, etc.) for normative requirements.
- Follow the standard section structure: Introduction, Document Scope, Document Structure, Keywords, Terminology, and numbered chapters.

## Schema contributions

- Update or add JSON Schema files under `data-schemas/`. Schemas are organised by format (e.g. `sd-jwt/`, `mdoc/`).
- Use the naming convention: `ds###-<name>-<format>.json` (e.g. `ds001-ebw-oid-sd-jwt.json`).
- Include at least one representative sample under the corresponding `sample-data/` folder, named `ds###-<name>-<format>-sample.json`.
- Use JSON Schema Draft-07 or later and include `$schema`, `$id`, `title`, `description`, `type`, and `version` properties.

## Validation

The repository includes a GitHub Actions workflow ([validate-schemas.yml](.github/workflows/validate-schemas.yml)) that automatically validates schemas and samples on every pull request. Before opening a PR:

1. Ensure all JSON files are well-formed.
2. Verify your sample data conforms to its schema using any JSON Schema validator (e.g. `jsonschema` for Python, `ajv` for Node.js).
3. Check that every schema has at least one matching sample in the same folder (matched by the `ds###` file prefix).

## Pull request process

1. **Open a pull request** against `main`.
2. Describe the intent and scope of your change, and reference any related issues or external specifications.
3. The CI workflow will run automatically — ensure all checks pass.
4. Be responsive to review comments and iterate as needed until approval.

## Style and conventions

- **British English** spelling is preferred.
- Use **lowercase with hyphens** for file and folder names.
- Write **clear commit messages** with context and rationale.
- Keep changes **scoped and focused** — separate unrelated updates into different PRs.
- Prefer **additive changes**; avoid breaking changes unless necessary and clearly justified.

## Licence

This project is licensed under the [Apache Licence, Version 2.0](LICENCE). By contributing, you agree that your contributions will be licensed under the same terms.
