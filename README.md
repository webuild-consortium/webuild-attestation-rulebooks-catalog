# WE BUILD Attestation Rulebooks and Schemas

## Repository description
This repository hosts the rulebooks and data schemas used across the WE BUILD Large Scale Pilot (LSP) use cases for the European Digital Identity (EUDI) and European Business Wallet (EBW) ecosystems. It serves as a single source of truth for governance, interoperability, and compliance materials, including:

- Rulebooks that describe requirements, roles, processes, and conformance criteria for specific credentials and attestation types.
- Data schemas (e.g. SD-JWT based) that define how credential data is structured and validated.
- Sample data demonstrating expected payload shapes for implementers.

Project structure (high level):
- `rulebooks/` — Human‑readable rulebooks and regulatory references.
- `data-schemas/` — Machine‑readable schemas (e.g., JSON Schema for SD‑JWT claims), with samples under `sample-data/`.
- `sample-data/` — Additional example payloads that complement the schemas.

This repository is intended for implementers, partners, and reviewers who need to understand and validate the format and governance of credential data in EUDI Wallet and EBW contexts.

For the official production rulebooks beyond WE BUILD, see the [EUDI Wallet – Attestation Rulebooks Catalog](https://github.com/eu-digital-identity-wallet/eudi-doc-attestation-rulebooks-catalog).

## How to contribute
We welcome contributions! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on how to get started.

## Funding

![Co-funded by the European Union](https://github.com/webuild-consortium/architecture/raw/main/images/EUFunded.png)

[WE BUILD](https://www.webuildconsortium.eu/) is co-funded by the European Union. However, the views and opinions expressed are those of the author(s) only and do not necessarily reflect those of the European Union or the granting authority. Neither the European Union nor the granting authority can be held responsible.

## License

This project is licensed under the Apache Licence, Version 2.0. See the repository's [LICENCE](LICENCE) file for
details. By contributing, you agree that
your contributions will be licensed under the same terms.
