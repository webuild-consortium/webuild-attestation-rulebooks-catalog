# WE BUILD Attestation Rulebooks and Schemas

## Repository description
This repository hosts the rulebooks and data schemas used across the WE BUILD Large Scale Pilot (LSP) use cases for the European Digital Identity (EUDI) and European Business Wallet (EBW) ecosystems. It serves as a single source of truth for governance, interoperability, and compliance materials, including:

- Rulebooks that describe requirements, roles, processes, and conformance criteria for specific credentials and attestation types.
- Data schemas (e.g. SD-JWT based) that define how credential data is structured and validated.
- Sample data demonstrating expected payload shapes for implementers.

Project structure (high level):
- `rulebooks/` — Human-readable rulebooks and regulatory references.
- `data-schemas/` — Machine-readable schemas (e.g., JSON Schema for SD-JWT claims), with samples under `sample-data/`.
- `sample-data/` — Additional example payloads that complement the schemas.
- `explorer/` — The source of the rulebook explorer website, built and published automatically.

This repository is intended for implementers, partners, and reviewers who need to understand and validate the format and governance of credential data in EUDI Wallet and EBW contexts.

For the official production rulebooks beyond WE BUILD, see the [EUDI Wallet Attestation Rulebooks Catalog](https://github.com/eu-digital-identity-wallet/eudi-doc-attestation-rulebooks-catalog).

## Read the rulebooks

**[webuild-consortium.github.io/webuild-attestation-rulebooks-catalog](https://webuild-consortium.github.io/webuild-attestation-rulebooks-catalog/)**

The rulebook explorer lets you search every rulebook by category, by format or by
attribute, and read any of them in full, a chapter at a time. Each rulebook has its
own page and its own address, so a link to one can be shared on its own.

The site is built from this repository on every push to `main`. The catalogue is also
available as data at
[`/index.json`](https://webuild-consortium.github.io/webuild-attestation-rulebooks-catalog/index.json).

## Writing or changing a rulebook

Every rulebook follows one generic template of eleven chapters, and all of them do
today. Start at [`rulebooks/README.md`](rulebooks/README.md), which lists the chapters,
explains how to name the folder, and points at the template.

Nothing needs to be built or generated on your machine. Editing the markdown in the
GitHub editor is enough.

## How to contribute
Contributions are welcome. [`CONTRIBUTING.md`](CONTRIBUTING.md) covers how to make a
change, what the automatic checks do, and how a change gets reviewed.

## Funding

![Co-funded by the European Union](https://github.com/webuild-consortium/architecture/raw/main/images/EUFunded.png)

[WE BUILD](https://www.webuildconsortium.eu/) is co-funded by the European Union. However, the views and opinions expressed are those of the author(s) only and do not necessarily reflect those of the European Union or the granting authority. Neither the European Union nor the granting authority can be held responsible.

## License

This project is licensed under the Apache Licence, Version 2.0. See the repository's [LICENCE](LICENCE) file for
details. By contributing, you agree that
your contributions will be licensed under the same terms.
