# Writing a WE BUILD attestation rulebook

This folder holds the WE BUILD attestation rulebooks. Each one is a self-contained
document describing a single attestation type: its data model, and the rules that
govern how it is issued, presented and verified.

Every rulebook in this folder follows the same template. All of them do today, so
whichever one you open is a working example.

You can read them all on the
[rulebook explorer](https://webuild-consortium.github.io/webuild-attestation-rulebooks-catalog/),
which is built from this folder automatically.

## Start here

1. Copy [`templates/webuild-rulebook-generic-template.md`](templates/webuild-rulebook-generic-template.md)
   to `rulebooks/rb-<slug>/README.md`.
2. Fill it in. Read [`templates/README.md`](templates/README.md) first: it explains the
   three markers in the template, the requirement identifiers, and the checklist to run
   through before you submit.
3. Open a pull request. Nothing else needs to be generated or committed.

If you prefer to work from a finished document, open a rulebook close to yours and
follow its shape. [`rb-taxid`](rb-taxid/README.md) is a good general reference, and
[`rb-pid`](rb-pid/README.md) shows an attestation carried in two formats.

## The eleven chapters

The template is fixed at eleven chapters, in this order. Do not renumber or rename
them. A chapter that does not apply to your attestation type stays, with a sentence
saying why.

| Chapter | Holds |
| --- | --- |
| 1 Introduction | Scope and purpose, document structure, key words, terminology |
| 2 Compliance | The compliance statement, the regulatory basis, and the traceability table |
| 3 Attestation attributes | The attributes, named independently of any encoding |
| 4 Metadata | Metadata, code lists and integrity rules |
| 5 Formats | Which formats the attestation is issued in, and the identifier each one uses |
| 6 Protocols | The issuance and presentation protocols |
| 7 Issuance | Binding, issuance policy, lifecycle, embedded disclosure policy |
| 8 Revocation | The revocation mechanism and what triggers it |
| 9 Presentation | The presentation policy, the modes, transactional data |
| 10 Trust Framework | How a Relying Party obtains a trust anchor |
| 11 References | Every standard and document cited |

Two chapters carry most of the weight and are worth extra care:

- **Chapter 2.3, the traceability table.** Every applicable requirement of Topic 12
  mapped to the section that satisfies it, using the ARF v3.0.0 identifiers with the
  legacy `ARB_xx` identifier beside each one. No blank rows.
- **Chapter 3 and chapter 5 together.** Chapter 3 names each attribute once, without
  reference to an encoding. Chapter 5 says what identifier that attribute carries in
  each format. An attestation issued in two formats has two different identifier lists
  and one attribute list.

## Folder name

Each rulebook lives in its own folder:

```
rulebooks/rb-<slug>/README.md
```

`rb-` is a constant prefix. The slug is lower case, words separated by hyphens,
matching `^rb-[a-z0-9-]+$`. Where the EUDI ARF already has a slug for the attestation,
match it. Otherwise choose a short consortium name.

Existing examples: `rb-pid`, `rb-ebwoid`, `rb-eucc`, `rb-eu-poa`, `rb-e-receipt`,
`rb-taxid`.

The folder holds one required file, `README.md`, which is the rulebook itself. Schemas
and sample data live under [`data-schemas/`](../data-schemas), not here.

## Slugs

- A slug is agreed in the pull request that introduces the rulebook. If two pull
  requests propose the same slug, reviewers pick one.
- Once merged, a slug is stable. A rename needs a pull request with a reason, because
  the published page address changes with it.

## What happens after you open a pull request

A check builds the explorer from every rulebook in this folder. It fails only if a
rulebook can no longer be read or rendered, so you are never blocked by a note about
somebody else's document. It does print what the build makes of yours, including
whether it is on the template, whether the category was recognised, and any cross
reference pointing at a heading that is not there. Those are worth reading before you
ask for review.

Once merged, your rulebook appears on the explorer within a couple of minutes, with
its own page and its own address.
