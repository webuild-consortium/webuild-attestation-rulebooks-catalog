# Base Attestation Rulebook for Non-qualified Electronic Attestation of Attributes

Category: Non-qualified EAA

| Version | Date | Description |
| --- | --- | --- |
| 1.0 | 2026-09-28 | First issue. Derived from the generic WE BUILD attestation rulebook template. |

**Written against:** ARF version 3.0.0, EC attestation rulebook template v1.5

**Feedback:** [GitHub issues](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/issues)

## About this Rulebook

This is a base Rulebook. It states what applies to every attestation of the
Non-qualified EAA category, so that an attestation Rulebook of this category does not repeat
it. It is not an attestation Rulebook in its own right and no attestation is issued
against it directly.

An attestation Rulebook of this category inherits this document by stating:

```
Category: Non-qualified EAA

This Rulebook inherits the Non-qualified EAA base Rulebook:
https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/templates/webuild-base-rulebook-eaa.md
```

It then states only what is specific to the attestation. In most cases that is the
attribute set in chapter 3, the metadata in chapter 4, the schema artefacts, and the
formats in chapter 5. Where a chapter below says a matter is set by the attestation
Rulebook, the attestation Rulebook SHALL state it.

Where an attestation Rulebook departs from this base, it SHALL record the deviation
and the reason in its own chapter 2. Changes to this base are raised with the WE BUILD
rulebook quality assurance group rather than made in an attestation Rulebook.

## Table of contents

- [1 Introduction](#1-introduction)
- [2 Compliance](#2-compliance)
- [3 Attestation attributes](#3-attestation-attributes)
- [4 Metadata](#4-metadata)
- [5 Formats](#5-formats)
- [6 Protocols](#6-protocols)
- [7 Issuance](#7-issuance)
- [8 Revocation](#8-revocation)
- [9 Presentation](#9-presentation)
- [10 Trust Framework](#10-trust-framework)
- [11 References](#11-references)

## 1 Introduction

### 1.1 Scope and purpose

This Rulebook applies to every attestation of the Non-qualified EAA category, that is, every
electronic attestation of attributes issued by an Attestation Provider that is not acting as a qualified trust service provider for this attestation within the WE BUILD
ecosystem.

The purpose and subject matter of an individual attestation are stated by its own
Rulebook.

### 1.2 Document structure

Chapter 2 states compliance and the regulatory basis of the category. Chapters 3 and 4
state what the attestation Rulebook defines for attributes and metadata, and fix the
legal category metadata. Chapter 5 states the formats available to the category.
Chapters 6 to 9 cover protocols, issuance, revocation and presentation. Chapter 10
states the trust framework. Chapter 11 lists references.

### 1.3 Key words

This document uses the capitalised key words 'SHALL', 'SHOULD' and 'MAY' as specified
in [RFC 2119], to indicate requirements, recommendations and options. In addition,
'must' (non-capitalised) indicates an external constraint, that is, a requirement
mandated by an external document rather than by this document. The word 'can'
indicates a capability. Other words such as 'will', 'is' and 'are' are statements of
fact.

### 1.4 Terminology

This document uses the terminology specified in Annex 1 of the ARF.

## 2 Compliance

### 2.1 Compliance statement

This Rulebook complies with the applicable requirements of Topic 12, Attestation
Rulebooks, in Annex 2 of the Architecture and Reference Framework, version 3.0.0. It
uses the terminology of Annex 1 of the ARF.

### 2.2 Regulatory basis

An attestation of this category is not a qualified electronic attestation of
attributes. The data described in Annex V points b, c and e of Regulation (EU)
2024/1183 is addressed as required by EW-DM-12-018 and as recommended by
EW-DM-12-020 and EW-DM-12-022. Where a recommendation is not followed, the
attestation rulebook SHALL state the reason.

### 2.3 Traceability

The table states, for each requirement of Topic 12, whether the Non-qualified EAA category
settles it. Rows marked as set by the attestation Rulebook are completed there,
together with the section that satisfies them.

| Requirement | Legacy ID | Status for this category | Note |
| --- | --- | --- | --- |
| EW-DM-12-001 | ARB_01a | applies | W3C VCDM is available to this category |
| EW-DM-12-002 | ARB_01b | set by the attestation rulebook | SD-JWT VC per the HAIP profile |
| EW-DM-12-003 | ARB_02 | set by the attestation rulebook | mdoc required if proximity presentation is in scope |
| EW-DM-12-005 | ARB_04 | set by the attestation rulebook | Approved specifications for W3C VCDM encoding |
| EW-DM-12-006 | ARB_05 | set by the attestation rulebook | Unique attestation type or vct |
| EW-DM-12-007 | ARB_06 | set by the attestation rulebook | Encoding-independent attribute definitions |
| EW-DM-12-008 | ARB_06a | set by the attestation rulebook | mdoc attribute identifiers and namespaces |
| EW-DM-12-009 | ARB_06b | set by the attestation rulebook | SD-JWT VC claim naming |
| EW-DM-12-010 | ARB_07 | set by the attestation rulebook | Reuse of catalogued attributes |
| EW-DM-12-012 | ARB_09 | set by the attestation rulebook | Mandatory, optional or conditional marking |
| EW-DM-12-013 | ARB_10 | set by the attestation rulebook | Domestic namespace, if defined |
| EW-DM-12-014 | ARB_11 | not applicable | Annex V and VII point a apply to QEAA and PuB-EAA |
| EW-DM-12-015 | ARB_12 | applies | EAA indication, satisfied by `category` in section 4.1 |
| EW-DM-12-016 / EW-DM-12-017 / EW-DM-12-018 | ARB_13 / ARB_14 / ARB_15 | EW-DM-12-018 applies | Annex V point b, non-qualified case |
| EW-DM-12-019 / EW-DM-12-020 | ARB_16 / ARB_17 | EW-DM-12-020 recommended | Annex V point c, state the reason if not followed |
| EW-DM-12-021 / EW-DM-12-022 | ARB_18 / ARB_19 | EW-DM-12-022 recommended | Annex V point e, state the reason if not followed |
| EW-DM-12-023 / EW-DM-12-024 | ARB_20 / ARB_21 | EW-DM-12-024 applies | Trust anchor location, chapter 10 |
| EW-DM-12-029 | ARB_25 | applies | Legal category attribute, section 4.1 |
| EW-DM-12-030 | ARB_26 | applies | Trust anchor publication, chapter 10 |
| EW-DM-12-031 | ARB_27 | set by the attestation rulebook | Whether the Relying Party must also verify a PID |
| EW-DM-12-032 | ARB_28 | set by the attestation rulebook | `cryptographically_bound_to`, if used |
| EW-DM-12-034 | ARB_30 | set by the attestation rulebook | Selective disclosure per claim |
| EW-DM-12-035 | ARB_31 | set by the attestation rulebook | Claim Selective Disclosure Metadata |
| EW-DM-12-038 | ARB_34 | set by the attestation rulebook | Device binding, no category default |

## 3 Attestation attributes

Attributes SHALL be defined in an encoding-independent manner (EW-DM-12-007). The
authoritative encoding lives in the machine-readable schema artefacts, not in the
prose of a Rulebook.

Each attestation Rulebook of this category SHALL state:

- the schema artefact for every format it marks as supported, versioned and immutably
  addressable, and the identifier of that artefact;
- its mandatory attributes;
- its optional attributes;
- its conditional attributes, each with the condition stated in the definition.

For SD-JWT VC, whether a claim is selectively disclosable SHALL be stated per claim in
the attestation Rulebook, not in the schema (EW-DM-12-034).

## 4 Metadata

### 4.1 Legal category metadata

Every attestation of this category SHALL carry the `category` attribute with the
following value:

| Data identifier | Definition | Data type | Value for this category |
| --- | --- | --- | --- |
| category | Legal category of the attestation | string | `eaa:eu:non-qualified` |

The `category` attribute is defined in [ETSI TS 119 472-1] and SHALL NOT be selectively
disclosable. In the mdoc encoding it belongs to the namespace
`org.etsi.01947201.010101`.

The superseded `attestation_legal_category` attribute is replaced by `category`. Note
that EW-DM-12-029, legacy ARB_25, of ARF version 3.0.0 still requires
`attestation_legal_category`. The two disagree, and the matter is open with the WE
BUILD rulebook quality assurance group. An attestation Rulebook that retains
`attestation_legal_category` SHALL record the deviation and the reason.

### 4.2 Other metadata

Metadata other than `category`, together with code lists and integrity rules, is set by
the attestation Rulebook. Code lists SHALL state their source and whether they are
extensible. Integrity rules SHALL state where they are enforced and the behaviour on
failure.

## 5 Formats

The formats available to this category:

| Format | Availability | Note |
| --- | --- | --- |
| ISO/IEC 18013-5 mdoc | MAY be used | Required if proximity presentation is in scope (EW-DM-12-003) |
| SD-JWT VC | MAY be used | SHALL follow the HAIP profile (EW-DM-12-002) |
| W3C VCDM | MAY be used | Available to this category (EW-DM-12-001). The attestation rulebook states the type and context |

Each attestation Rulebook SHALL mark at least one format as supported and SHALL state
the identifiers for it. Identifiers SHALL be unique to the attestation type
(EW-DM-12-006). Where more than one format is supported, the attestation Rulebook
SHALL state whether a Provider offers all of them or may choose.

## 6 Protocols

Attestations of this category are issued using OpenID for Verifiable Credential
Issuance [OpenID4VCI] and presented using OpenID for Verifiable Presentations
[OpenID4VP], both as profiled by [HAIP]. Proximity presentation uses ISO/IEC 18013-5
device retrieval and requires the mdoc format.

An attestation Rulebook states any profile it relies on beyond these.

## 7 Issuance

### 7.1 Binding

| Field | Value for this category | Source | Note |
| --- | --- | --- | --- |
| Device-bound | set by the attestation rulebook | EW-DM-12-038 | This category has no default |
| Cryptographically bound to | set by the attestation rulebook | EW-DM-12-032 | This category has no default |
| Relying Party must also verify a PID | set by the attestation rulebook | EW-DM-12-031 |  |
| Binding subject | set by the attestation rulebook |  |  |

Every attestation Rulebook SHALL complete each row, and SHALL justify any departure
from a value fixed by this base.

### 7.2 Issuance Policy

General obligations on Attestation Providers are out of scope of this Rulebook. They
are specified in Topic 10 of Annex 2 of the ARF, in the applicable Implementing
Regulations, and in [ETSI TS 119 471].

An attestation Rulebook states the issuance obligations specific to its attestation,
each as a pointer to the section that states it.

### 7.3 Lifecycle management

An attestation Rulebook states the validity period or the rule that determines it,
reissuance and renewal including cadence for short-lived attestations, and what happens
when the underlying facts change, including reissuance and revocation of the superseded
attestation.

Where lifecycle management is specified in an EAA Policy or in the Attestation
Provider's trust services policy, the attestation Rulebook may reference those
documents instead.

### 7.4 Embedded disclosure policy

An attestation Rulebook states which embedded disclosure policy applies, if any. The
policies available are described in Annex III of Implementing Regulation (EU) 2024/2979
and specified in [ETSI TS 119 472-3].

## 8 Revocation

An attestation Rulebook states whether attestations of its type are revocable.

Where they are short-lived, with a validity period of 24 hours or less, they are not
revocable and Relying Parties do not perform a revocation check.

Where they are revocable, revocation status is published using Attestation Status Lists
or Attestation Revocation Lists as specified in the relevant Technical Specification
issued by the Commission, and the attestation Rulebook SHALL state the location at
which the relevant lists can be retrieved. It SHALL also state who may request
revocation, the grounds specific to the attestation type in addition to any imposed by
regulation, and the expected time from trigger to status list update.

## 9 Presentation

### 9.1 Presentation Policy

To verify and validate a received presentation of an attestation of this category, the
following steps SHALL be performed:

1. verify the signature over the attestation using a trust anchor obtained as described
   in chapter 10;
2. verify that the attestation is within its validity period;
3. check revocation status as described in chapter 8, unless the attestation is
   short-lived, or its remaining lifetime is below the revocation time threshold;
4. verify device binding where section 7.1 records the attestation as device-bound;
5. request only those attributes that are necessary for the stated purpose of the
   transaction, and, where the trust model for the attestation requires Relying Party
   registration, only those attributes it is registered and authorised to request.

An attestation Rulebook adds the obligations specific to its attestation after this
list. It does not amend the list.

### 9.2 Presentation modes and transactional data

An attestation Rulebook states which of remote and proximity presentation are in scope,
consistent with the formats it supports, and states any transactional data it defines.

## 10 Trust Framework

The trust anchor SHALL NOT be obtained from a Trusted List of qualified trust
service providers. The mechanism by which it is obtained, and the procedure by
which a Relying Party verifies that the Provider is authorised to issue the
attestation type, are an open consortium decision. Until that decision is taken,
each attestation rulebook of this category SHALL state the mechanism and the
procedure it relies on in its chapter 10.

A Wallet Unit MAY verify Provider authorisation using the mechanism described in
ISSU_34 of Topic 10 of Annex 2 of the ARF.

**Trust anchor location**

The attribute or metadata carrying the trust anchor location SHALL contain at least
the URL at which a machine-readable version can be found or looked up. For this
category the location and its meaning are as stated by the attestation rulebook
(EW-DM-12-024, EW-DM-12-030).

The attribute named in the attestation Rulebook's chapter 10 SHALL be the same
attribute it declares in chapter 4.

**Deployment profile**

An attestation Rulebook states the trust anchor arrangements of the deployment it runs
in: how Provider trust anchors are distributed, how a Relying Party or Wallet Unit
looks one up, the ordered verification steps, and any consortium-specific endpoint the
deployment depends on.

## 11 References

| Reference | Details |
| --- | --- |
| [Regulation] | Regulation (EU) 2024/1183 amending Regulation (EU) No 910/2014 |
| [CIR 2024/2979] | Commission Implementing Regulation (EU) 2024/2979, integrity and core functionality |
| [CIR 2026/1731] | Commission Implementing Regulation (EU) 2026/1731, as regards applicable standards and specifications |
| [ARF] | EUDI Wallet Architecture and Reference Framework, version 3.0.0 |
| [ETSI TS 119 471] | Policy and security requirements for EAA service providers |
| [ETSI TS 119 472-1] | Profiles for Electronic Attestations of Attributes; Part 1 - General requirements |
| [ETSI TS 119 472-2] | Profiles for Electronic Attestations of Attributes; Part 2 - Profiles for EAA/PID Presentations to Relying Party |
| [ETSI TS 119 472-3] | Profiles for Electronic Attestations of Attributes; Part 3 - Profiles for issuance of EAA or PID |
| [HAIP] | OpenID4VC High Assurance Interoperability Profile |
| [ISO/IEC 18013-5] | Personal identification, ISO-compliant driving licence, Part 5, 2021 |
| [OpenID4VCI] | OpenID for Verifiable Credential Issuance |
| [OpenID4VP] | OpenID for Verifiable Presentations |
| [RFC 2119] | Key words for use in RFCs to Indicate Requirement Levels |
| [SD-JWT VC] | SD-JWT-based Verifiable Credentials |
| [W3C VCDM v2.0] | Verifiable Credentials Data Model v2.0 |
