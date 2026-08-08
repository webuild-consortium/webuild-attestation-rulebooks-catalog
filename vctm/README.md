# VCTM — Verifiable Credential Type Metadata

## What is VCTM?

**VCTM** (Verifiable Credential Type Metadata) is a standardised format for describing the structure, display properties, and claims of a Verifiable Credential type. A VCTM definition captures everything a verifier or wallet needs to understand a credential: its type identifier (VCT URI), the claims it contains, their types and display names, selective-disclosure settings, and visual rendering hints such as background and text colours.

## Files in this folder

Each credential type in this folder consists of:

| File                      | Purpose |
|---------------------------|---------|
| `<attestation-slug>.md`   | Markdown source defining the credential (front matter + claims) |
| `<attestation-slug>.schema-meta.yaml` | Sidecar metadata (rulebook URI, LoS, binding type, trusted authorities) |

## Registry

Published credential types are listed in the **Siros Credential Type Registry**:

**[https://registry.siros.org](https://registry.siros.org)**

## Documentation

- **How to register your credential type:** [https://registry.siros.org/docs/register.html](https://registry.siros.org/docs/register.html)
- **Markdown format reference (syntax for defining claims, display names, localisation, etc.):** [https://registry.siros.org/docs/markdown-format.html](https://registry.siros.org/docs/markdown-format.html)
