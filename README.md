# WEBUILD Attestation Rulebooks and Schemas

## Repository description
This repository hosts the rulebooks and data schemas used across the WE BUILD Large Scale Pilot (LSP) use cases for the European Digital Identity (EUDI) ecosystem. It serves as a single source of truth for governance, interoperability, and compliance materials, including:

- Rulebooks that describe requirements, roles, processes, and conformance criteria for specific credentials and attestation types.
- Data schemas (e.g. SD-JWT based) that define how credential data is structured and validated.
- Sample data demonstrating expected payload shapes for implementers.

Project structure (high level):
- `rulebooks/` — Human‑readable rulebooks and regulatory references.
- `data-schemas/` — Machine‑readable schemas (e.g., JSON Schema for SD‑JWT claims), with samples under `sample-data/`.
- `sample-data/` — Additional example payloads that complement the schemas.

This repository is intended for implementers, partners, and reviewers who need to understand and validate the format and governance of credential data in EUDI wallet contexts.

## Dependencies

# Dependencies and Identifier Issuance

# PID/LPID Dependency Graph

```mermaid
graph TD

%% Work Packages
WP4S["Input from WP4 Semantics"]
WP4A["Input from WP4 Architecture"]

%% Outer group
subgraph PID_LPID_Group["PID / LPID Group"]

  %% Inner PID block
  subgraph PID_Block["Issue PID"]
  end

  %% Inner LPID block
  subgraph LPID_Block["Issue LPID"]
  end

end

%% Work packages connect to the group
WP4S --> PID_LPID_Group
WP4A --> PID_LPID_Group

%% Wallets
NPW["NP Wallets"]
BW["Business Wallets"]

%% Use Cases
BU1["BU1"]
BU2["BU2"]
BU3["BU3"]
BU4["BU4"]
BU5["BU5"]
BU6["BU6"]
SC1["SC1"]
SC2["SC2"]
SC5["SC5"]
PA1["PA1"]
PA2["PA2"]
PA3["PA3"]
PA4["PA4"]

%% PID issuance
PID_Block --> NPW
PID_Block --> BU1
PID_Block --> BU2
PID_Block --> BU3
PID_Block --> BU4
PID_Block --> BU5
PID_Block --> BU6
PID_Block --> SC1
PID_Block --> SC2
PID_Block --> SC5
PID_Block --> PA1
PID_Block --> PA2
PID_Block --> PA3

%% LPID issuance
LPID_Block --> BW
LPID_Block --> BU1
LPID_Block --> BU2
LPID_Block --> BU3
LPID_Block --> BU4
LPID_Block --> BU5
LPID_Block --> SC1
LPID_Block --> SC2
LPID_Block --> SC5
LPID_Block --> PA3
LPID_Block --> PA4
```



## How to contribute
We welcome contributions that improve clarity, correctness, and coverage of rulebooks and schemas. To contribute:

1. Fork the repository and create a feature branch:
   - Branch name suggestion: `feat/<area>-<short-description>` or `fix/<area>-<short-description>`.
2. Make your changes:
   - For rulebooks: edit or add Markdown files under `rulebooks/` and keep terminology consistent with EUDI specifications.
   - For schemas: update or add JSON Schema files under `data-schemas/` and include at least one representative example under the corresponding `sample-data/` folder.
   - For samples: add minimal, realistic examples that pass schema validation.
3. Validate your changes locally (recommended):
   - Ensure JSON files are well‑formed.
   - If you introduce a schema, verify your sample(s) conform to it using any JSON Schema validator of your choice.
4. Open a Pull Request (PR):
   - Describe the intent and scope of your change and reference any related issues or external specs.
   - The repository includes a GitHub Actions workflow (`.github/workflows/validate-schemas.yml`) that will run basic checks on JSON files and schemas. Please ensure the checks pass.
5. Address review feedback:
   - Be responsive to comments and iterate as needed until approval.

### Contribution guidelines and tips
- Keep changes scoped and focused; separate unrelated updates into different PRs.
- Prefer additive changes when possible; avoid breaking changes unless necessary and clearly justified.
- Use clear commit messages and include context and rationale when updating rulebooks.
- Maintain consistency in file naming (lowercase with hyphens) and folder placement.
- British English spelling is preferred.

## License

This project is licensed under the Apache Licence, Version 2.0. See the repository's [LICENCE](LICENCE) file for
details. By contributing, you agree that
your contributions will be licensed under the same terms.
