# Versioning

This document describes how versioning is managed across the different artefact types in this repository.

## Overview

The repository contains three distinct types of artefacts, each with its own versioning mechanism:

| Artefact type | Where the version lives | Versioning cadence |
|---|---|---|
| Rulebooks | Version table inside each rulebook's `README.md` | Per-document, independent |
| JSON Schemas | `version` field inside each `.json` schema file | Per-schema, independent |
| VCTM Credentials | File path (new file per version) | Major versions only |

In addition, the repository itself is tagged at major milestone points to pin a snapshot of all artefacts to a WE BUILD deliverable.

---

## Rulebooks

Each rulebook lives under `rulebooks/<rb-name>/` and carries its own version history in a Markdown table at the top of its `README.md`, for example:

```markdown
| Version | Date       | Description          |
|---------|------------|----------------------|
| 0.9.1   | 13.02.2026 | Initial draft        |
| 1.0.0   | 22.05.2026 | Updated after review |
```

- Versions follow [Semantic Versioning](https://semver.org/) (`MAJOR.MINOR.PATCH`).
- Each rulebook is versioned independently; one rulebook reaching `1.0.0` does not require others to do the same.
- The version table is the authoritative record of changes for that rulebook.

---

## JSON Schemas

Each JSON schema file (under `data-schemas/`) contains a top-level `version` field:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "version": "1.0.0",
  ...
}
```

- Schema versions are independent of rulebook versions and evolve at their own pace.
- However, at major milestones and deliverables, schema versions **should be co-ordinated** to match the corresponding rulebook's major version number.
- Minor and patch-level changes may diverge between a schema and its associated rulebook.

---

## VCTM Credentials

Credentials in the VCTM (Verifiable Credential Type Metadata) directory are versioned by **creating a new file** and **iterating the path**, rather than editing the existing file in place. This preserves backwards compatibility for any system already referencing a specific credential path.

- New credential files should only be created for **major version changes**.
- The number of distinct credential versions should be kept to a minimum.
- Older credential files are retained in the repository to support systems that reference them.

---

## Repository Tags

The repository uses Git tags to mark major milestone versions aligned with WE BUILD deliverables.

- A tag (e.g. `v1.0`) represents a snapshot of the entire repository at a point in time.
- A tag **does not imply** that all artefacts within the repository share the same version number; individual rulebooks, schemas, and credentials may be at different versions.
- Tags are used primarily to provide a stable reference point for project deliverables.
