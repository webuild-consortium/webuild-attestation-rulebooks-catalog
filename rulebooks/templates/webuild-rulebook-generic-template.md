# Attestation Rulebook for attestations of type [ATTESTATION TYPE]

Category: [PID / EBWOID / QEAA / PuB-EAA / non-qualified EAA]

Generic WE BUILD template, structure agreed at the rulebook quality assurance workshop. Aligned to ARF v3.0.0 (21 July 2026) and EC attestation rulebook template v1.5 (8 July 2026).

**Markers.** FIXED means consortium-agreed text, copy verbatim and raise changes
upstream. [AUTHOR] means yours to write. TO AGREE means an open consortium decision,
leave it alone. Strip all three before submission to the EC catalogue.

- Author(s): [NAME SURNAME, AFFILIATION]
- Previous authors: [NAME SURNAME, AFFILIATION (versions)]

| Version | Date | Description |
| --- | --- | --- |
| [VERSION] | [DATE] | [DESCRIPTION OR LINK TO CHANGELOG] |

**Written against:** ARF version [ARF VERSION], WE BUILD template version [VERSION]

**Feedback:** [ISSUE TRACKER URL]

## Table of contents

- [1 Introduction](#1-introduction)
   * [1.1 Document scope and purpose](#11-document-scope-and-purpose)
   * [1.2 Document structure](#12-document-structure)
   * [1.3 Key words](#13-key-words)
   * [1.4 Terminology](#14-terminology)
- [2 Certification](#2-certification)
   * [2.1 Compliance statement](#21-compliance-statement)
   * [2.2 Regulatory basis](#22-regulatory-basis)
   * [2.3 Traceability](#23-traceability)
- [3 Attestation attributes](#3-attestation-attributes)
   * [3.1 Introduction](#31-introduction)
   * [3.2 Mandatory attributes](#32-mandatory-attributes)
   * [3.3 Optional attributes](#33-optional-attributes)
   * [3.4 Conditional attributes](#34-conditional-attributes)
- [4 Metadata](#4-metadata)
   * [4.1 Mandatory metadata](#41-mandatory-metadata)
   * [4.2 Optional metadata](#42-optional-metadata)
   * [4.3 Conditional metadata](#43-conditional-metadata)
   * [4.4 Code lists](#44-code-lists)
   * [4.5 Integrity rules](#45-integrity-rules)
- [5 Formats](#5-formats)
- [6 Protocols](#6-protocols)
   * [6.1 Issuance](#61-issuance)
   * [6.2 Presentation](#62-presentation)
- [7 Issuance](#7-issuance)
   * [7.1 Binding](#71-binding)
   * [7.2 Lifecycle management](#72-lifecycle-management)
   * [7.3 Issuance Policy](#73-issuance-policy)
   * [7.4 Embedded disclosure policy](#74-embedded-disclosure-policy)
- [8 Revocation](#8-revocation)
- [9 Presentation](#9-presentation)
   * [9.1 Relying Party policy](#91-relying-party-policy)
   * [9.2 Presentation modes](#92-presentation-modes)
   * [9.3 Transactional data](#93-transactional-data)
- [10 Trust Framework](#10-trust-framework)
- [11 References](#11-references)


## 1 Introduction

### 1.1 Document scope and purpose

[AUTHOR] Describe in plain language what this attestation expresses and what it is
for. A reader who knows nothing about the domain should understand it from this
section alone. Cover:

- the real-world fact, entitlement, role, status or capability it expresses;
- the expected issuers, holders and relying parties;
- the use case or user journey it supports;
- the attestation description or functional specification it draws on;
- any use it is not intended for.

Keep terminology aligned with the source attestation description.

### 1.2 Document structure

FIXED

> Chapter 2 states how this Rulebook complies with the applicable regulatory and
> architectural requirements. Chapter 3 specifies the attestation attributes and
> chapter 4 the metadata, both in an encoding-independent manner, each referencing
> the machine-readable schema artefacts that define their encoding. Chapter 5 lists
> the attestation formats supported. Chapter 6 lists the issuance and presentation
> protocols supported. Chapter 7 specifies issuance, including binding and lifecycle
> management. Chapter 8 specifies revocation. Chapter 9 specifies presentation.
> Chapter 10 specifies the trust framework, including how trust anchors are
> obtained. Chapter 11 lists references.
>
> Chapters 5 and 6 identify formats and protocols only. The substantive rules for
> issuance and presentation are in chapters 7 and 9 respectively, and are not
> repeated in chapters 5 and 6.

### 1.3 Key words

FIXED

> This document uses the capitalised key words 'SHALL', 'SHOULD' and 'MAY' as
> specified in [RFC 2119], to indicate requirements, recommendations and options.
> In addition, 'must' (non-capitalised) indicates an external constraint, that is, a
> requirement mandated by an external document rather than by this document. The
> word 'can' indicates a capability. Other words such as 'will', 'is' and 'are' are
> statements of fact.

### 1.4 Terminology

FIXED

> This document uses the terminology specified in Annex 1 of the ARF.

[AUTHOR] Add only terms specific to this attestation type that Annex 1 does not
define. Do not restate ARF definitions.

| Term | Definition | Source |
| --- | --- | --- |
| | | |

## 2 Certification

Written last, although it appears first. Sections 2.1 and 2.2 are largely fixed by
the legal category. Section 2.3 can only be completed once chapters 3 to 10 are
final.

### 2.1 Compliance statement

FIXED

> This Rulebook complies with the applicable requirements of Topic 12, Attestation
> Rulebooks, in Annex 2 of the Architecture and Reference Framework, version
> [ARF VERSION]. It uses the terminology of Annex 1 of the ARF.

### 2.2 Regulatory basis

Keep the block matching the legal category and delete the others.

**PID**

> This Rulebook specifies how the mandatory and optional person identification data
> defined in Tables 1 and 2 of the Annex to CIR (EU) 2024/2977, and the metadata
> defined in Table 5 of that CIR, are encoded within the EUDI Wallet ecosystem.

**QEAA**

> This attestation includes the data required by Annex V of Regulation (EU)
> 2024/1183, points a, b, c, e and h, satisfying EW-DM-12-014, EW-DM-12-016,
> EW-DM-12-019, EW-DM-12-021 and EW-DM-12-023 respectively. It is issued by a
> qualified trust service provider.

**PuB-EAA**

> This attestation includes the data required by Annex VII of Regulation (EU)
> 2024/1183, points a, b, c, e and h, satisfying EW-DM-12-014, EW-DM-12-017,
> EW-DM-12-019, EW-DM-12-021 and EW-DM-12-023 respectively. It is issued by or on
> behalf of a public sector body responsible for an authentic source.

**Non-qualified EAA**

> This attestation is not a qualified electronic attestation of attributes. The data
> described in Annex V points b, c and e of Regulation (EU) 2024/1183 is addressed as
> required by EW-DM-12-018 and as recommended by EW-DM-12-020 and EW-DM-12-022.
> Where a recommendation is not followed, the reason is stated below.

**EBWOID**

> TO AGREE. Do not assert qualified status unless the issuer is a QTSP, and do not
> cite Annex V or Annex VII by default.

### 2.3 Traceability

Every applicable requirement mapped to the section that satisfies it. Mark a
requirement not applicable only with a stated reason. No blank rows at submission.

| Requirement | Legacy ID | Applies | Satisfied in section | Note |
| --- | --- | --- | --- | --- |
| EW-DM-12-001 | ARB_01a | | | Format restriction, W3C VCDM permitted for non-qualified EAA only |
| EW-DM-12-002 | ARB_01b | | | SD-JWT VC per the HAIP profile |
| EW-DM-12-003 | ARB_02 | | | mdoc required if proximity presentation is in scope |
| EW-DM-12-005 | ARB_04 | | | Approved specifications for W3C VCDM encoding |
| EW-DM-12-006 | ARB_05 | | | Unique attestation type or vct |
| EW-DM-12-007 | ARB_06 | | | Encoding-independent attribute definitions |
| EW-DM-12-008 | ARB_06a | | | mdoc attribute identifiers and namespaces |
| EW-DM-12-009 | ARB_06b | | | SD-JWT VC claim naming |
| EW-DM-12-010 | ARB_07 | | | Reuse of catalogued attributes |
| EW-DM-12-012 | ARB_09 | | | Mandatory, optional or conditional marking |
| EW-DM-12-013 | ARB_10 | | | Domestic namespace, if defined |
| EW-DM-12-014 | ARB_11 | | | Annex V or VII point a |
| EW-DM-12-015 | ARB_12 | | | EAA indication, non-qualified only |
| EW-DM-12-016 / EW-DM-12-017 / EW-DM-12-018 | ARB_13 / ARB_14 / ARB_15 | | | Point b, by category |
| EW-DM-12-019 / EW-DM-12-020 | ARB_16 / ARB_17 | | | Point c, by category |
| EW-DM-12-021 / EW-DM-12-022 | ARB_18 / ARB_19 | | | Point e, by category |
| EW-DM-12-023 / EW-DM-12-024 | ARB_20 / ARB_21 | | | Trust anchor or certificate location, by category |
| EW-DM-12-030 | ARB_26 | | | Trust anchor publication, non-qualified EAA |
| EW-DM-12-031 | ARB_27 | | | Whether the Relying Party must also verify a PID |
| EW-DM-12-032 | ARB_28 | | | `cryptographically_bound_to`, if used |
| EW-DM-12-034 | ARB_30 | | | Selective disclosure per claim |
| EW-DM-12-035 | ARB_31 | | | Claim Selective Disclosure Metadata |
| EW-DM-12-038 | ARB_34 | | | Device binding |

## 3 Attestation attributes

Attributes are defined here in an encoding-independent manner (EW-DM-12-007). The
authoritative encoding lives in the machine-readable schema artefacts referenced in
section 3.1, not in this document. Do not paste schema fragments into the prose,
they will drift.

### 3.1 Introduction

[AUTHOR] Describe the design of the attribute set and the decisions behind it. For
complex attestations, include or reference a logical model showing the main entities,
relationships and attribute groupings.

**Schema artefacts.** FIXED table shape. One row per format supported in chapter 5.

| Format | Identifier | Schema artefact | Version | Location |
| --- | --- | --- | --- | --- |
| SD-JWT VC | `vct` value | JSON schema or Type Metadata Document | | [URL FOR SCHEMAS] |
| mdoc | doctype and namespace | CDDL or attribute definition file | | [URL FOR SCHEMAS] |
| W3C VCDM | type and context | JSON-LD context | | [URL] |

FIXED

> The schema artefacts referenced above are normative for encoding. Where this
> document and a referenced artefact disagree, the artefact prevails for encoding
> questions and this document prevails for semantics, presence and disclosure rules.
> Each artefact SHALL be versioned and immutably addressable. Versioning of the
> artefacts SHALL align on major releases.

Note on selective disclosure: for SD-JWT VC, whether a claim is selectively
disclosable is stated in the tables below, not in the schema (EW-DM-12-034). Where
a Claim Selective Disclosure Metadata document is used (EW-DM-12-035), reference it
above.

### 3.2 Mandatory attributes

Attributes that SHALL be present in every attestation of this type.

| Data identifier | Semantic reference | Definition | Data type | Selectively disclosable | Example value |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

### 3.3 Optional attributes

Attributes the Provider MAY include at its discretion.

| Data identifier | Semantic reference | Definition | Data type | Selectively disclosable | Example value |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

### 3.4 Conditional attributes

Attributes required only when a stated condition holds. State the condition
explicitly in the definition, not in a footnote.

| Data identifier | Semantic reference | Definition | Condition | Data type | Selectively disclosable | Example value |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |


## 4 Metadata

Metadata describes the attestation rather than its subject. Use the same schema
artefacts referenced in section 3.1.

### 4.1 Mandatory metadata

Includes the `category` attribute for all categories except PID.

| Category | `category` value |
| --- | --- |
| QEAA | `urn:etsi:esi:eaa:eu:qualified` |
| PuB-EAA | `urn:etsi:esi:eaa:eu:pub` |
| Non-qualified EAA | `eaa:eu:non-qualified` |
| EBWOID | TO AGREE |
| PID | not applicable, omit |

FIXED

> The `category` attribute is defined in [ETSI TS 119 472-1] and SHALL NOT be
> selectively disclosable. In the mdoc encoding it belongs to the namespace
> `org.etsi.01947201.010101`. The superseded `attestation_legal_category` attribute,
> with values QEAA, PuB-EAA and non-qualified-EAA, SHALL NOT be used.

| Data identifier | Semantic reference | Definition | Data type | Example value |
| --- | --- | --- | --- | --- |
| category | | Legal category of this attestation | string | |
| | | | | |

### 4.2 Optional metadata

Includes `cryptographically_bound_to` where section 7.1 records a cryptographic
binding (EW-DM-12-032).

| Data identifier | Semantic reference | Definition | Data type | Example value |
| --- | --- | --- | --- | --- |
| | | | | |

### 4.3 Conditional metadata

| Data identifier | Semantic reference | Definition | Condition | Data type | Example value |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

### 4.4 Code lists

Controlled vocabularies, enumerations and value sets needed to interpret attributes
consistently. Reference an external vocabulary wherever one exists rather than
defining a local list.

| Field | Allowed values or vocabulary | Meaning | Source | Extensible |
| --- | --- | --- | --- | --- |
| | | | | |

### 4.5 Integrity rules

Consistency rules not captured by the schema alone: cross-field dependencies,
temporal consistency, mutual exclusivity, conditional combinations.

| Rule ID | Rule statement | Why it exists | Where enforced | Behaviour on failure |
| --- | --- | --- | --- | --- |
| IR-01 | | | | |

## 5 Formats

Identification only. Encoding detail lives in the schema artefacts of section 3.1,
and the rules for using each format live in chapters 7 and 9.

| Format | Supported | Identifier | Specification | Notes |
| --- | --- | --- | --- | --- |
| ISO/IEC 18013-5 mdoc | yes / no | doctype `[VALUE]`, namespace `[VALUE]` | [ISO/IEC 18013-5] | Required if proximity presentation is in scope (EW-DM-12-003) |
| SD-JWT VC | yes / no | `vct` `[VALUE]` | [SD-JWT VC], [HAIP] | SHALL follow the HAIP profile (EW-DM-12-002) |
| W3C VCDM | yes / no | type `[VALUE]`, context `[URL]` | [W3C VCDM v2.0] | Permitted for non-qualified EAA only (EW-DM-12-001) |

FIXED

> A PID SHALL be issued in both the ISO/IEC 18013-5 and SD-JWT VC formats. For other
> attestation types, at least one format SHALL be marked as supported. Identifiers
> SHALL be unique to this attestation type (EW-DM-12-006).

[AUTHOR] Where more than one format is supported, state whether a Provider SHALL
offer all of them or MAY choose.

## 6 Protocols

Identification only. Substantive issuance rules are in chapter 7, presentation rules
in chapter 9.

### 6.1 Issuance

| Protocol | Supported | Profile or version | Specification | Notes |
| --- | --- | --- | --- | --- |
| OpenID4VCI | yes / no | | [OpenID4VCI], [HAIP] | |
| [OTHER] | | | | |

### 6.2 Presentation

| Protocol | Supported | Profile or version | Specification | Notes |
| --- | --- | --- | --- | --- |
| OpenID4VP, remote | yes / no | | [OpenID4VP], [HAIP] | |
| ISO/IEC 18013-5, proximity | yes / no | | [ISO/IEC 18013-5] | Requires the mdoc format |
| [OTHER] | | | | |

FIXED

> Protocols listed here are those referenced in Topic 6 of Annex 2 of the ARF. This
> Rulebook does not profile these protocols beyond what is stated in the table.

## 7 Issuance

### 7.1 Binding

FIXED table shape. Complete every row, none may be left blank.

| Field | Value | Source |
| --- | --- | --- |
| Device-bound | SHALL / SHOULD / MAY / non device-bound | EW-DM-12-038 |
| Cryptographically bound to | none / attestation type or vct value | EW-DM-12-032 |
| Relying Party must also verify a PID | yes / no / not applicable | EW-DM-12-031 |
| Binding subject | natural person / legal person / wallet unit | |

[AUTHOR] Justify any answer that departs from the category default. For QEAA and
PuB-EAA the defaults are device-bound and bound to the PID unless justified. For
EBWOID all four rows are TO AGREE.

### 7.2 Lifecycle management

[AUTHOR] Specify:

- the authentic source of the attributes, and how currency is assured;
- validity period, or the rule that determines it;
- reissuance and renewal, including cadence for short-lived attestations;
- update or correction when the underlying facts change;
- batch issuance, if used, and any limits on reuse.

**Attestation Provider obligations.** FIXED opening, then attestation-specific
additions.

> General obligations on Attestation Providers are out of scope of this Rulebook.
> They are specified in Topic 10 of Annex 2 of the ARF, in the applicable Implementing
> Regulations, and in [ETSI TS 119 471]. This Rulebook states only obligations
> specific to this attestation type.

[AUTHOR] List the attestation-specific obligations, each as a pointer to the section
that states it, for example format obligations from chapter 5, selective disclosure
rules from chapter 3, trust anchor publication from chapter 10.

### 7.3 Issuance Policy

### 7.4 Embedded disclosure policy

| Field | Value |
| --- | --- |
| Policy present | yes / no |
| Common policy applied | none / authorised relying parties only / specific root of trust |
| Encoding | pending upstream specification |

FIXED

> Embedded disclosure policies are defined in CIR (EU) 2024/2979 and in Topic 43 of
> Annex 2 of the ARF. No standardised encoding exists in ISO/IEC 18013-5, SD-JWT VC,
> OpenID4VCI or OpenID4VP at the time of writing. This Rulebook declares which policy
> applies and does not specify a local encoding.



## 8 Revocation

Keep one branch and delete the other. Consortium default: TO AGREE.

**Short-lived**

> Attestations of this type are short-lived, with a validity period of 24 hours or
> less. They are therefore not revocable and Relying Parties do not perform a
> revocation check.

**Revocable**

> Attestations of this type are revocable. Revocation status is published using
> [Attestation Status Lists / Attestation Revocation Lists], as specified in the
> relevant Technical Specification issued by the Commission. Relying Parties and
> other entities can retrieve the relevant lists at [DOMAIN OR URL]. The full
> location relevant to an individual attestation is included in that attestation.

[AUTHOR] State who may request revocation, on what grounds, and the expected time
from trigger to status list update.

## 9 Presentation

### 9.1 Relying Party policy

FIXED

> A Relying Party receiving an attestation of this type SHALL:
>
> 1. verify the signature over the attestation using a trust anchor obtained as
>    described in chapter 10;
> 2. verify that the attestation is within its validity period;
> 3. check revocation status as described in chapter 8, unless the attestation is
>    short-lived; or remaining lifetime of the attestation is below revocation time
>    threshold;
> 4. verify device binding where section 7.1 records the attestation as device-bound;
> 5. request only those attributes that are necessary for the stated purpose of the
>    transaction, and, where the trust model for this attestation requires Relying
>    Party registration, only those attributes it is registered and authorised to
>    request.

[AUTHOR] Add obligations specific to this attestation type below. Do not edit the
list above.

### 9.2 Presentation modes

[AUTHOR] State which of remote and proximity presentation are in scope, consistent
with chapters 5 and 6. If proximity is in scope, the mdoc format is required.

### 9.3 Transactional data

FIXED

> No transactional data as defined in Topic 20 of Annex 2 of the ARF is associated
> with this attestation type.

Replace only if this attestation is used for strong user authentication for
electronic payments.

## 10 Trust Framework

Of the two legal category branches below, keep the one matching this attestation and
delete the other. Trust anchor location applies in both cases.

**PID, QEAA, PuB-EAA and attestations resolved via Trusted Lists**

FIXED

> The trust anchor is obtained from a Trusted List, as described in section 6.6.3.6
> of the ARF main document. The Provider may sign the attestation with an
> intermediate signing certificate, in which case the trust anchor is used to verify
> that certificate rather than the attestation directly.
>
> For a PuB-EAA, a Relying Party Instance first verifies the Provider signature using
> the Provider certificate issued by a QTSP, then verifies that certificate using the
> corresponding trust anchor from the QTSP Trusted List. One or more extra
> certificates are therefore involved compared with a PID or QEAA.

**Non-qualified EAA**

> The trust anchor is not obtained from a Trusted List of qualified trust service
> providers. A Relying Party obtains it as follows: [CONSORTIUM DEFAULT MECHANISM,
> TO AGREE]. It then verifies that the Provider is authorised to issue this
> attestation type by [PROCEDURE].
>
> A Wallet Unit MAY verify Provider authorisation using the mechanism described in
> ISSU_34 of Topic 10 of Annex 2 of the ARF.

**Trust anchor location**

FIXED

> The attribute or metadata carrying the trust anchor location contains at least the
> URL at which a machine-readable version can be found or looked up. For a QEAA this
> location refers to the trust anchor (EW-DM-12-023). For a PuB-EAA it refers to the
> qualified certificate that signed the attestation (EW-DM-12-023). For a
> non-qualified EAA the location and its meaning are as described above
> (EW-DM-12-024, EW-DM-12-030).

Coherence check: the attribute named here SHALL be the same attribute declared in
chapter 4.

## 11 References

| Reference | Details |
| --- | --- |
| [Regulation] | Regulation (EU) 2024/1183 amending Regulation (EU) No 910/2014 |
| [CIR 2024/2977] | Commission Implementing Regulation (EU) 2024/2977, PID and EAA |
| [CIR 2024/2979] | Commission Implementing Regulation (EU) 2024/2979, integrity and core functionality |
| [ARF] | EUDI Wallet Architecture and Reference Framework, version [VERSION] |
| [ETSI TS 119 471] | Policy and security requirements for EAA service providers |
| [ETSI TS 119 472-1] | Electronic Attestation of Attributes, Part 1 |
| [ETSI TS 119 472-2] | Electronic Attestation of Attributes, Part 2 |
| [HAIP] | OpenID4VC High Assurance Interoperability Profile |
| [ISO/IEC 18013-5] | Personal identification, ISO-compliant driving licence, Part 5, 2021 |
| [OpenID4VCI] | OpenID for Verifiable Credential Issuance |
| [OpenID4VP] | OpenID for Verifiable Presentations |
| [RFC 2119] | Key words for use in RFCs to Indicate Requirement Levels |
| [SD-JWT VC] | SD-JWT-based Verifiable Credentials |
| [W3C VCDM v2.0] | Verifiable Credentials Data Model v2.0 |
