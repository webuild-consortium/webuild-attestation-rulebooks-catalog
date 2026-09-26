# WE BUILD rulebook template

How to use [`webuild-rulebook-generic-template.md`](webuild-rulebook-generic-template.md),
the generic attestation rulebook template agreed at the rulebook quality assurance
workshop. Aligned to ARF v3.0.0 (21 July 2026) and EC attestation rulebook template
v1.5 (8 July 2026).

Copy the template into your rulebook folder as `README.md` and fill it in. Do not
renumber or rename its sections. Sections that do not apply to your attestation type
are retained with a short note explaining why.

## Markers

The template carries three markers. None of them belong in a finished rulebook.

| Marker | Meaning |
| --- | --- |
| FIXED | Consortium-agreed text. Copy verbatim and raise any change upstream rather than editing it in place. |
| [AUTHOR] | Yours to write. |
| TO AGREE | An open consortium decision. Leave it alone. |

Strip all three markers before submission to the EC catalogue.

## Requirement identifiers

Section 2.3 uses the ARF v3.0.0 identifiers (`EW-DM-12-xxx`) and carries the legacy
`ARB_xx` identifier alongside each one, because the Annex 2 documents on GitHub still
use the legacy form. Keep both columns.

## Pre-submission checklist

1. Section 2.3 has no blank rows.
2. Every format marked supported in chapter 5 has a schema artefact in section 3.1,
   versioned and immutably addressable.
3. No schema fragments are pasted into chapters 3 or 4.
4. Every SD-JWT VC claim in chapter 3 states whether it is selectively disclosable.
5. The `category` value matches the legal category and uses the ETSI URN form.
   `attestation_legal_category` appears nowhere.
6. Section 7.1 has no blank rows, and matches the presence or absence of
   `cryptographically_bound_to` in section 4.2.
7. The trust anchor attribute in chapter 10 is the one declared in chapter 4.
8. If revocable, chapter 8 states the retrieval location.
9. Proximity presentation in chapter 9 implies mdoc in chapter 5.
10. Every code list in 4.4 states its source and extensibility.
11. Every integrity rule in 4.5 states enforcement point and failure behaviour.
12. The ARF version and template version are in the header, version-pinned rather
    than `/latest/`.

Maintained by the WE BUILD rulebook quality assurance group.
