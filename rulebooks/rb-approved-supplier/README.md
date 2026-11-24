# Attestation Rulebook for attestations of type Approved Supplier

Category: non-qualified EAA

*This Rulebook is derived from the generic WE BUILD attestation rulebook template, version 1.0 with 11 chapters (itself derived from
the EUDI attestation rulebook template) and keeps the template's chapter structure. It specifies the
Approved Supplier attestation used in WE BUILD Use Case SC5 (eInvoicing), Scenario 1 (Supplier
pre-approval).*

* Author(s):
  * Rune Kjørlaug, Emning AS / OpenPeppol (SC5 co-lead)

| Version | Date       | Description                                                  |
| ------- | ---------- | ------------------------------------------------------------ |
| 0.1     | 2026-06-01 | Initial draft of the Approved Supplier attestation rulebook, derived from the WE BUILD Attestation Rulebook Template v1.1 and aligned with the SC5 eInvoicing scenario specification (Scenario 1). |
| 0.6     | 2026-07-14 | Review draft for SC5 rulebook review meeting. Aligned with the WE BUILD attestation rulebooks catalog conventions: vct pattern `eu.we-build:<slug>:1`, legal category value `EAA`, EBWOID-anchored EAA trust model per rb-base, issuer and Relying Party obligations referencing the Base Verification rulebook, and Token Status List metadata. |
| 0.7     | 2026-07-15 | Added issue tracker and cleaned up author list layout        |
| 1.1     | 2026-10-02 | Restructured onto the generic WE BUILD attestation rulebook template (11 chapters). No normative content removed. |
| 1.2     | 2026-11-09 | Added a W3C VCDM encoding (section 5.3, informative until the proposed vocabulary terms are published). Replaced the placeholders in section 5.1 with an informative issued SD-JWT and presentation example. Aligned the `status` claim with the IETF Token Status List structure. Corrected example identifiers (EUID and Peppol ICD). Resolved inconsistencies introduced by the template migration: traceability vs. body (binding, device binding), selective disclosure stated in the attribute tables, stale section references, dangling text in chapter 9, missing references. |

**Written against:** ARF version 3.0.0, WE BUILD template version 1.0 (generic)

**Feedback:** [GitHub issues](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/issues)

## Table of contents

- [1 Introduction](#1-introduction)
  * [1.1 Document scope and purpose](#11-document-scope-and-purpose)
  * [1.2 Document structure](#12-document-structure)
  * [1.3 Key words](#13-key-words)
  * [1.4 Terminology](#14-terminology)
- [2 Compliance](#2-compliance)
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
  * [5.1 SD-JWT VC-based encoding](#51-sd-jwt-vc-based-encoding)
  * [5.2 ISO/IEC 18013-5-compliant encoding](#52-isoiec-18013-5-compliant-encoding)
  * [5.3 W3C Verifiable Credentials Data Model-based encoding](#53-w3c-verifiable-credentials-data-model-based-encoding)
- [6 Protocols](#6-protocols)
  * [6.1 Issuance](#61-issuance)
  * [6.2 Presentation](#62-presentation)
- [7 Issuance](#7-issuance)
  * [7.1 Binding](#71-binding)
  * [7.2 Issuance Policy](#72-issuance-policy)
  * [7.3 Lifecycle management](#73-lifecycle-management)
  * [7.4 Embedded disclosure policy](#74-embedded-disclosure-policy)
- [8 Revocation](#8-revocation)
  * [8.1 Revocation mechanism](#81-revocation-mechanism)
  * [8.2 Revocation triggers and business rules](#82-revocation-triggers-and-business-rules)
- [9 Presentation](#9-presentation)
  * [9.1 Presentation Policy](#91-presentation-policy)
  * [9.2 Presentation modes](#92-presentation-modes)
  * [9.3 Transactional data](#93-transactional-data)
- [10 Trust Framework](#10-trust-framework)
- [11 References](#11-references)


## 1 Introduction

### 1.1 Document scope and purpose

This Rulebook defines the **Approved Supplier attestation**, an Electronic Attestation of Attributes
(EAA) used within WE BUILD Use Case SC5 (eInvoicing).

In plain language, the Approved Supplier attestation lets a **Buyer** declare, in a machine-verifiable
way, that it has an active commercial relationship with a specific **Supplier** and approves the
receipt of invoices from that Supplier. The attestation is issued by the Buyer to the Supplier and is
later presented by the Supplier (or on the Supplier's behalf) so that a Service Provider can verify,
*before* an invoice enters the Peppol network, that the sending Supplier is genuinely approved by the
Buyer it claims to invoice. This prevents unauthorised or fraudulent invoices from being transmitted
on behalf of buyers who have no relationship with the sender.

* **Real-world fact expressed:** that a named Buyer has pre-approved a named Supplier to send it
  invoices, for a defined scope and validity period.
* **Issuers:** the Buyer (Peppol corner **C4**), acting as a legal person through its European
  Business Wallet (EBW).
* **Holders:** the Supplier (Peppol corner **C1**), holding the attestation in its EBW.
* **Relying parties:** the Supplier's Access Point (Peppol corner **C2**), which verifies the
  attestation at invoice-submission time. Other access points or supervisory parties may verify it in
  MVP+ scenarios.
* **Use case / user journey:** SC5 Scenario 1 (Supplier pre-approval). The attestation is issued once
  (or periodically) and verified on each invoice submission in a machine-to-machine flow.
* **Source material:** the SC5 eInvoicing scenario descriptions in the
  [SC5 repository](https://github.com/webuild-consortium/SC5/tree/main/Scenario) (`Description.md` and
  `Scenario1.md`). Actor terminology (C1–C4, EBW, EBWOID, Access Point) is kept aligned with those
  descriptions and with the Peppol Interoperability Framework.

### 1.2 Document structure

This Rulebook follows the generic WE BUILD attestation rulebook template. Chapter 2
states how it complies with the ARF and the applicable Regulations. Chapters 3 and 4
define the attributes and metadata in an encoding-independent manner. Chapter 5 states
the formats in which this attestation is issued. Chapters 6 to 9 cover protocols,
issuance, revocation and presentation. Chapter 10 sets out the trust framework, and
chapter 11 lists references.

### 1.3 Key words

This document uses the capitalised key words 'SHALL', 'SHOULD' and 'MAY' as specified
in [RFC 2119], to indicate requirements, recommendations and options.

In addition, 'must' (non-capitalised) indicates an external constraint, a requirement
not mandated by this document but by an external document. The word 'can' indicates a
capability. Other words such as 'will', 'is' and 'are' are statements of fact.

### 1.4 Terminology

This document uses the terminology specified in Annex 1 of the ARF, supplemented by Peppol terminology
(C1–C4, Access Point, SMP/SML, Peppol participant identifier) and WE BUILD terminology (EBW, EBWOID,
WE BUILD LoTL, WE BUILD Trusted List) as defined in the SC5 scenario descriptions and the WP4 Blueprint.

## 2 Compliance

### 2.1 Compliance statement

This Rulebook complies with the applicable requirements of Topic 12, Attestation
Rulebooks, in Annex 2 of the Architecture and Reference Framework, version 3.0.0. It
uses the terminology of Annex 1 of the ARF.

The Approved Supplier attestation is a **non-qualified EAA** in the sense of the
[European Digital Identity Regulation] and is implemented within the WE BUILD pilot trust framework
rather than the eIDAS production ecosystem (WA1.1, WA1.5; WP4 Blueprint D4.1 §1.2.1). Its normative
format is SD-JWT VC profiled by [HAIP]; a W3C VCDM encoding is additionally defined (section 5.3). It
uses OpenID4VCI for issuance and OpenID4VP for presentation per the WE BUILD Conformance
Specifications (cs-01, cs-02), and the IETF Token Status List for revocation per the WE BUILD ADR on
Attestation Revocation. Escalation to an eIDAS-qualified EAA (QEAA), and any associated QTSP
involvement, is out of scope for this version.

### 2.2 Regulatory basis

This attestation is not a qualified electronic attestation of attributes. The data
described in Annex V points b, c and e of Regulation (EU) 2024/1183 is addressed as
required by EW-DM-12-018 and as recommended by EW-DM-12-020 and EW-DM-12-022: issuer
identification through `iss` and the EBWOID-anchored certificate material (chapter 10), the
subject through `approved_supplier`, and the validity period through `iat`/`exp` together with
`approval_valid_from`/`approval_valid_until`. All recommendations are followed.

### 2.3 Traceability

Every applicable requirement mapped to the section that satisfies it. Requirements
marked not applicable carry a stated reason.

| Requirement                                | Legacy ID                | Applies | Satisfied in section | Note                                                         |
| ------------------------------------------ | ------------------------ | ------- | -------------------- | ------------------------------------------------------------ |
| EW-DM-12-001                               | ARB_01a                  | yes     | 5.3                  | W3C VCDM permitted for this category, and defined in section 5.3 |
| EW-DM-12-002                               | ARB_01b                  | yes     | 5.1                  | SD-JWT VC following the HAIP profile                         |
| EW-DM-12-003                               | ARB_02                   | no      |                      | Proximity presentation is not in scope                       |
| EW-DM-12-005                               | ARB_04                   | yes     | 5.3                  | W3C VCDM v2.0 secured with VC-JOSE-COSE; informative until the proposed vocabulary terms are published |
| EW-DM-12-006                               | ARB_05                   | yes     | 5                    | Unique vct and VCDM type for this attestation type           |
| EW-DM-12-007                               | ARB_06                   | yes     | 3                    | Attributes defined independently of encoding                 |
| EW-DM-12-008                               | ARB_06a                  | no      |                      | No mdoc encoding is defined in this version                  |
| EW-DM-12-009                               | ARB_06b                  | yes     | 5.1                  | SD-JWT VC claim naming                                       |
| EW-DM-12-010                               | ARB_07                   | yes     | 3, 5.3               | EUID and Peppol identifiers reused; VCDM reuses EBWV terms where they exist |
| EW-DM-12-012                               | ARB_09                   | yes     | 3, 4                 | Mandatory, optional and conditional stated per attribute     |
| EW-DM-12-013                               | ARB_10                   | no      |                      | No mdoc domestic namespace is defined                        |
| EW-DM-12-014                               | ARB_11                   | no      |                      | Annex V and VII point a apply to QEAA and PuB-EAA            |
| EW-DM-12-015                               | ARB_12                   | yes     | 4.1                  | EAA indication for a non-qualified EAA                       |
| EW-DM-12-016 / EW-DM-12-017 / EW-DM-12-018 | ARB_13 / ARB_14 / ARB_15 | yes     | 2.2, 4.1             | Point b, EW-DM-12-018 for the non-qualified case             |
| EW-DM-12-019 / EW-DM-12-020                | ARB_16 / ARB_17          | yes     | 2.2, 3.2             | Point c, recommendation for non-qualified EAA                |
| EW-DM-12-021 / EW-DM-12-022                | ARB_18 / ARB_19          | yes     | 2.2, 3.2, 4.1        | Point e, recommendation for non-qualified EAA                |
| EW-DM-12-023 / EW-DM-12-024                | ARB_20 / ARB_21          | yes     | 4.2, 10              | Trust anchor location and the trust framework                |
| EW-DM-12-029                               | ARB_25                   | yes     | 4.1                  | Legal category attribute; see the note in section 4.1        |
| EW-DM-12-030                               | ARB_26                   | yes     | 10                   | Trust anchor publication for non-qualified EAA               |
| EW-DM-12-031                               | ARB_27                   | no      |                      | This attestation does not require the Relying Party to verify a PID |
| EW-DM-12-032                               | ARB_28                   | yes     | 4.2, 7.1             | RECOMMENDED binding to the Supplier's EBWOID through `cryptographically_bound_to` |
| EW-DM-12-034                               | ARB_30                   | yes     | 3.2, 3.3             | Selective disclosure stated per claim                        |
| EW-DM-12-035                               | ARB_31                   | no      |                      | No Claim Selective Disclosure Metadata document is used      |
| EW-DM-12-038                               | ARB_34                   | yes     | 7.1                  | Device binding RECOMMENDED                                   |

## 3 Attestation attributes

Attributes are defined here in an encoding-independent manner (EW-DM-12-007). The
encoding of each attribute is given in chapter 5.

### 3.1 Introduction

The Approved Supplier attestation expresses a single business relationship: a Buyer's approval of a
Supplier. The design models two parties, the **approving party** (the Buyer, who is also the technical
issuer) and the **approved supplier** (the Supplier, who is the holder/subject), together with the
scope and validity of the approval.

**Logical model (informative):**

```
ApprovedSupplierAttestation
├── attestation_legal_category : "EAA"     (metadata, section 4.1)
├── approving_party            (the Buyer, C4, also the issuer)
│   ├── legal_name
│   ├── legal_id               (EUID, from the Buyer's EBWOID)
│   └── peppol_id              (Peppol participant identifier)
├── approved_supplier          (the Supplier, C1, the holder/subject)
│   ├── legal_name
│   ├── legal_id               (EUID, from the Supplier's EBWOID)
│   └── peppol_id
├── approval_scope             (code list, see 4.4)
├── approval_valid_from        (date)
└── approval_valid_until       (date; see also the exp metadata claim)
```

This model refines the flat claim list in the SC5 scenario description (issuer_id, issuer_name,
subject_id, subject_name, scope, approval_date, expiry_date, buyer_peppol_id, supplier_peppol_id) into
two grouped party objects, while preserving the same information content.

**Applicable legal category.** Per SC5 working assumption WA1.1, the Approved Supplier attestation is
implemented as a **non-qualified EAA**. Where SC5 material refers to a "WE BUILD QEAA", this denotes a
technically interoperable, ITB-tested attestation within the pilot trust framework, not an
eIDAS-qualified EAA (WA1.5). The applicable Topic 12 requirements for this category are mapped in
section 2.3.

**Schema artefacts.**

| Format    | Identifier                                                   | Schema artefact                                       | Version | Location                                                     |
| --------- | ------------------------------------------------------------ | ----------------------------------------------------- | ------- | ------------------------------------------------------------ |
| SD-JWT VC | `eu.we-build:approvedsupplier:1`                             | JSON Schema                                           | 1.0     | [`data-schemas/sd-jwt/approved-supplier-sd-jwt.json`](../../data-schemas/sd-jwt/approved-supplier-sd-jwt.json), sample [`approved-supplier-sd-jwt-sample.json`](../../data-schemas/sd-jwt/sample-data/approved-supplier-sd-jwt-sample.json) |
| W3C VCDM  | type `ApprovedSupplierCredential`, context `https://w3id.org/ebwv/v0.1` | JSON-LD context (EBWV), terms proposed in section 5.3 | pending | To be published by the WP4 semantics group                   |

The schema artefacts referenced above are normative for encoding. Where this document and a
referenced artefact disagree, the artefact prevails for encoding questions and this document prevails
for semantics, presence and disclosure rules.

Selective disclosure applies to the SD-JWT VC encoding and is stated per attribute in the tables
below (EW-DM-12-034). The W3C VCDM encoding of section 5.3 has no selective disclosure; section 5.3
states how this is handled.

### 3.2 Mandatory attributes

| Data identifier                | Semantic reference                                           | Definition                                                   | Data type            | Selectively disclosable        | Example value         |
| ------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | -------------------- | ------------------------------ | --------------------- |
| `approving_party.legal_name`   | N/A (SC5-defined)                                            | Registered legal name of the Buyer that issues the approval. | string               | MAY (with `approving_party`)   | `Les Roses d'Or SARL` |
| `approving_party.legal_id`     | EUID (Directive (EU) 2017/1132, Implementing Regulation (EU) 2021/1042) | Unique legal-person identifier of the Buyer, sourced from the Buyer's EBWOID. | string               | MAY (with `approving_party`)   | `FRRCS.120680088`     |
| `approving_party.peppol_id`    | Peppol Participant Identifier                                | Peppol participant identifier of the Buyer, as `ICD:identifier` (the value part of the `iso6523-actorid-upis` scheme). | string               | MAY (with `approving_party`)   | `0002:120680088`      |
| `approved_supplier.legal_name` | N/A (SC5-defined)                                            | Registered legal name of the approved Supplier (the holder). | string               | MAY (with `approved_supplier`) | `Green Flowers B.V.`  |
| `approved_supplier.legal_id`   | EUID (Directive (EU) 2017/1132, Implementing Regulation (EU) 2021/1042) | Unique legal-person identifier of the Supplier, sourced from the Supplier's EBWOID. | string               | MAY (with `approved_supplier`) | `NLNHR.85374628`      |
| `approved_supplier.peppol_id`  | Peppol Participant Identifier                                | Peppol participant identifier of the Supplier, as `ICD:identifier`. | string               | MAY (with `approved_supplier`) | `0106:85374628`       |
| `approval_scope`               | N/A (code list, section 4.4)                                 | Scope of the approval.                                       | string (enum)        | MAY                            | `peppol:einvoice`     |
| `approval_valid_from`          | N/A                                                          | Date from which the approval is valid.                       | full-date (RFC 3339) | MAY                            | `2026-01-01`          |

The party objects `approving_party` and `approved_supplier` are disclosed as a whole; their
sub-claims are not individually selectively disclosable.

### 3.3 Optional attributes

| Data identifier        | Semantic reference | Definition                                                   | Data type            | Selectively disclosable                                      | Example value        |
| ---------------------- | ------------------ | ------------------------------------------------------------ | -------------------- | ------------------------------------------------------------ | -------------------- |
| `approval_valid_until` | N/A                | Date until which the approval is valid (business validity, distinct from the technical `exp` metadata claim). | full-date (RFC 3339) | MAY                                                          | `2026-12-31`         |
| `approval_reference`   | N/A                | Buyer-internal reference for the underlying commercial relationship (e.g. framework agreement or contract number). | string               | MUST, so that the Supplier can withhold the internal reference | `PO-FRAME-2026-0042` |

### 3.4 Conditional attributes

The Approved Supplier attestation defined in this Rulebook does not contain any
conditional attributes.

## 4 Metadata

Metadata describes the attestation rather than its subject. Metadata claims are not selectively
disclosable.

### 4.1 Mandatory metadata

| Data identifier              | Semantic reference               | Definition                                                   | Data type    | Example value                                       |
| ---------------------------- | -------------------------------- | ------------------------------------------------------------ | ------------ | --------------------------------------------------- |
| `attestation_legal_category` | EW-DM-12-015 / EW-DM-12-029      | Indicates the legal category of the attestation.             | string       | `EAA`                                               |
| `vct`                        | [SD-JWT VC]                      | Verifiable Credential Type identifier (see section 5.1).     | string       | `eu.we-build:approvedsupplier:1`                    |
| `iss`                        | [IANA-JWT-Claims]                | Issuer identifier (the Buyer's issuing system / EBW).        | string (URI) | `https://wallet.lesrosesdor.example/issuer`         |
| `iat`                        | [IANA-JWT-Claims]                | Issuance timestamp.                                          | NumericDate  | `1767225600`                                        |
| `exp`                        | [IANA-JWT-Claims]                | Technical expiry timestamp of the attestation.               | NumericDate  | `1798761600`                                        |
| `status`                     | [SD-JWT VC], [Token Status List] | Reference to the Token Status List entry for revocation, as `status.status_list` with `idx` and `uri` (see chapter 8). | object       | `{"status_list": {"idx": 412, "uri": "https://…"}}` |
| `cnf`                        | [SD-JWT VC]                      | Holder key-binding confirmation (proof of possession by the Supplier's EBW). | object       | *(JWK)*                                             |

**Legal category.** This Rulebook retains the `attestation_legal_category` attribute.
Section 4.1 of the generic template replaces it with the `category` attribute of
[ETSI TS 119 472-1], whose value for this category is `eaa:eu:non-qualified`.
EW-DM-12-029, legacy ARB_25, of ARF version 3.0.0 is a SHALL that still requires
`attestation_legal_category`, so the template and the ARF disagree. The attribute is
left as written and the deviation is recorded for the rulebook quality assurance group.

### 4.2 Optional metadata

| Data identifier              | Semantic reference | Definition                                                   | Data type    | Example value               |
| ---------------------------- | ------------------ | ------------------------------------------------------------ | ------------ | --------------------------- |
| `cryptographically_bound_to` | EW-DM-12-032       | vct of the attestation on the same Wallet Unit to which this attestation is cryptographically bound (the Supplier's EBWOID). RECOMMENDED, see section 7.1. | string       | `uri:eu.ebw.oid.1`          |
| `nbf`                        | [IANA-JWT-Claims]  | Time before which the attestation SHALL NOT be accepted.     | NumericDate  | `1767225600`                |
| `sub`                        | [IANA-JWT-Claims]  | Identifier of the subject (the approved Supplier).           | string       | `did:example:green-flowers` |
| `schema_version`             | N/A                | Version of the schema artefact used.                         | string       | `1.0`                       |
| `trust_anchor_url`           | EW-DM-12-024       | URL at which a machine-readable version of the trust anchor can be found or looked up. For this attestation the trust anchor is the EBWOID provider's entry in the WE BUILD trust list infrastructure (chapter 10). | string (URI) | *(WE BUILD TLOL entry)*     |

### 4.3 Conditional metadata

The Approved Supplier attestation defined in this Rulebook does not contain any
conditional metadata.

### 4.4 Code lists

| Field            | Allowed values or vocabulary | Meaning                                                      | Source                  | Extensible     |
| ---------------- | ---------------------------- | ------------------------------------------------------------ | ----------------------- | -------------- |
| `approval_scope` | `peppol:einvoice`            | The Buyer approves the Supplier for sending Peppol BIS Billing 3.0 eInvoices. Default value for MVP. | WE BUILD SC5 vocabulary | Yes, see below |
| `approval_scope` | `all`                        | The Buyer approves the Supplier for all SC5-relevant document exchange. | WE BUILD SC5 vocabulary | Yes, see below |

Additional values SHOULD only be introduced if defined consistently across issuer and verifier
implementations and registered in the WE BUILD Attestation Rulebooks catalog.

### 4.5 Integrity rules

| Rule ID    | Rule statement                                               | Why it exists                                                | Where enforced                                       | Behaviour on failure                                         |
| ---------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------------------------------------------------- | ------------------------------------------------------------ |
| `IR-AS-01` | `approval_valid_from` SHALL NOT be later than `approval_valid_until` (when the latter is present), and both SHALL fall within the `iat`–`exp` window. | Prevents inconsistent or unusable validity periods.          | Issuer business rules; verifier business validation. | Issuer SHALL reject; verifier SHALL treat the attestation as invalid for the transaction. |
| `IR-AS-02` | The `approving_party.peppol_id` SHALL identify the same legal person as `approving_party.legal_id`; likewise for the approved supplier. | Ensures the Peppol identifier and the legal identifier refer to the same party, so verification at C2 is unambiguous. | Issuer; verifier cross-check against EBWOID.         | Verifier SHALL treat the attestation as invalid.             |
| `IR-AS-03` | At verification time, the `approved_supplier.peppol_id` SHALL match the C1 participant identifier on the invoice being submitted, and `approving_party.peppol_id` SHALL match the invoice's buyer participant identifier. | Binds the approval to the specific invoice flow, preventing reuse of a valid attestation for an unrelated buyer/supplier pair. | Verifier (C2) business validation.                   | Verifier SHALL reject the invoice submission.                |

## 5 Formats

| Format               | Supported         | Identifier                                                   | Specification                   | Notes                                                        |
| -------------------- | ----------------- | ------------------------------------------------------------ | ------------------------------- | ------------------------------------------------------------ |
| ISO/IEC 18013-5 mdoc | no                |                                                              | [ISO/IEC 18013-5]               | Proximity presentation is not in scope (EW-DM-12-003)        |
| SD-JWT VC            | yes               | `vct` `eu.we-build:approvedsupplier:1`                       | [SD-JWT VC], [HAIP]             | Normative format; SHALL follow the HAIP profile (EW-DM-12-002) |
| W3C VCDM             | yes (informative) | type `ApprovedSupplierCredential`, context `https://w3id.org/ebwv/v0.1` | [W3C VCDM v2.0], [VC-JOSE-COSE] | Permitted for non-qualified EAA (EW-DM-12-001); see section 5.3 |

A Provider SHALL offer the SD-JWT VC format. A Provider MAY additionally offer the W3C VCDM format
once section 5.3 is normative. A Relying Party in the SC5 Peppol flow SHALL accept SD-JWT VC and is
not required to accept W3C VCDM.

### 5.1 SD-JWT VC-based encoding

This attestation type SHALL be issued in the [SD-JWT VC]-compliant format and SHALL comply with the
'SD-JWT VCs' profile specified in [HAIP] (EW-DM-12-002).

**Verifiable Credential Type (`vct`):** `eu.we-build:approvedsupplier:1`

*(Proposed value; subject to registration in the WE BUILD Attestation Rulebooks catalog by the WP4
semantics group, EW-DM-12-006.)*

A Type Metadata Document SHOULD be defined for this vct per [SD-JWT VC]. Selective disclosure per
claim is stated in sections 3.2 and 3.3; all metadata claims of chapter 4 are not selectively
disclosable. The JWT header SHALL carry the issuer's EBWOID-anchored certificate material (`x5c`) as
described in chapter 10.

**Claim encoding:**

| Data identifier                   | Attribute identifier       | Encoding format                                              | Reference / notes              |
| --------------------------------- | -------------------------- | ------------------------------------------------------------ | ------------------------------ |
| `iss`, `iat`, `exp`, `nbf`, `sub` | as named                   | per [IANA-JWT-Claims]                                        | Section 4.1, 4.2               |
| `vct`                             | vct                        | string                                                       | [SD-JWT VC]                    |
| `status`                          | status                     | object, `status_list.idx` (integer) and `status_list.uri` (string) | [Token Status List]; chapter 8 |
| `cnf`                             | cnf                        | object, `jwk`                                                | [SD-JWT VC]; holder binding    |
| `attestation_legal_category`      | attestation_legal_category | string                                                       | Section 4.1                    |
| `approving_party`                 | approving_party            | object                                                       | Section 3.2                    |
| `approved_supplier`               | approved_supplier          | object                                                       | Section 3.2                    |
| `approval_scope`                  | approval_scope             | string                                                       | Code list 4.4                  |
| `approval_valid_from`             | approval_valid_from        | string (full-date)                                           | Section 3.2                    |
| `approval_valid_until`            | approval_valid_until       | string (full-date)                                           | Section 3.3                    |
| `approval_reference`              | approval_reference         | string                                                       | Section 3.3                    |
| `cryptographically_bound_to`      | cryptographically_bound_to | string                                                       | Section 4.2; section 7.1       |

**Logical claim set (informative, synthetic data, all disclosures applied):**

```json
{
  "vct": "eu.we-build:approvedsupplier:1",
  "iss": "https://wallet.lesrosesdor.example/issuer",
  "iat": 1767225600,
  "exp": 1798761600,
  "attestation_legal_category": "EAA",
  "cryptographically_bound_to": "uri:eu.ebw.oid.1",
  "status": { "status_list": { "idx": 412, "uri": "https://wallet.lesrosesdor.example/status/approvedsupplier" } },
  "cnf": { "jwk": { "kty": "EC", "crv": "P-256", "x": "...", "y": "..." } },
  "approving_party": {
    "legal_name": "Les Roses d'Or SARL",
    "legal_id": "FRRCS.120680088",
    "peppol_id": "0002:120680088"
  },
  "approved_supplier": {
    "legal_name": "Green Flowers B.V.",
    "legal_id": "NLNHR.85374628",
    "peppol_id": "0106:85374628"
  },
  "approval_scope": "peppol:einvoice",
  "approval_valid_from": "2026-01-01",
  "approval_valid_until": "2026-12-31",
  "approval_reference": "PO-FRAME-2026-0042"
}
```

#### 5.1.1 Issued SD-JWT (informative)

The example below is a complete issued SD-JWT, signed with a throw-away ES256 test key. All
organisations, identifiers and keys are synthetic. In this example every attribute of chapter 3 is
selectively disclosable: `approval_reference` because it MUST be, and the others to show how the
Supplier controls disclosure. A Provider MAY make fewer claims disclosable, as permitted in sections
3.2 and 3.3. For readability the header carries a `kid`; a production attestation SHALL carry the
EBWOID-anchored certificate material in `x5c` instead (chapter 10). The example SHALL be regenerated
if the selective-disclosure structure changes.

Issued SD-JWT (issuer-signed JWT `~` disclosures `~`):

```
eyJhbGciOiJFUzI1NiIsInR5cCI6ImRjK3NkLWp3dCIsImtpZCI6Imxlc3Jvc2VzZG9yLWVidy1pc3N1ZXItdGVzdCJ9.eyJ2Y3QiOiJldS53ZS1idWlsZDphcHByb3ZlZHN1cHBsaWVyOjEiLCJpc3MiOiJodHRwczovL3dhbGxldC5sZXNyb3Nlc2Rvci5leGFtcGxlL2lzc3VlciIsImlhdCI6MTc2NzIyNTYwMCwiZXhwIjoxNzk4NzYxNjAwLCJhdHRlc3RhdGlvbl9sZWdhbF9jYXRlZ29yeSI6IkVBQSIsImNyeXB0b2dyYXBoaWNhbGx5X2JvdW5kX3RvIjoidXJpOmV1LmVidy5vaWQuMSIsInN0YXR1cyI6eyJzdGF0dXNfbGlzdCI6eyJpZHgiOjQxMiwidXJpIjoiaHR0cHM6Ly93YWxsZXQubGVzcm9zZXNkb3IuZXhhbXBsZS9zdGF0dXMvYXBwcm92ZWRzdXBwbGllciJ9fSwiY25mIjp7Imp3ayI6eyJrdHkiOiJFQyIsImNydiI6IlAtMjU2IiwieCI6ImV1Sk03dm91NmhjTjVNcDZiM1I5NjVNY2FiejNlZG4xWHdoQmdCcDYwMU0iLCJ5IjoieWtTR3IyRG5HTnJuYmNsOHlRLTZHbl9ZSHBqUjlNcEJpWFQ3c21nRW5TUSJ9fSwiX3NkIjpbIjh1a3BuZWFrQjVGTGo1SjNOYkctUE5UbjF1anpSLThVSnZhb2xad3lFMjAiLCJCU3lrTnI2WTFHRDJ0TTJEQmJ5dXBldUxIN0xnaGlsWHVreC1rUjZ4dnBvIiwiREFpSVpDaWVYV2R5cmtaUkwya2liTGliUGRiM1U3eWR2M0pzb0poRlpEbyIsIlBnZlB5dzlCeU80U1hydGRKeExKbHotbTJ3VzRjbGVGbnZEV25RQ0EwMGsiLCJfMkgtTmxBckFQdG1DNldyLXBDMUVZSE5wcl96YVRZZ3dEUmF1WmpydEZFIiwicUl2Z2NzdEg4QjNWeGVJUVlJLVlXTGNta3ExZ29tbHFPdkhpU29JdjFGbyJdLCJfc2RfYWxnIjoic2hhLTI1NiJ9._ppp2liZbMSCiEiwiTDZ-DIHAZLHkW_43Y90yppY3vbOZOq5yfTMZIrqGfmKsRTY70LDQkF3ATKDfo287I5HUw~WyIyTXRtNXFRZkpyNEJfdTJHcWducmZBIiwiYXBwcm92aW5nX3BhcnR5Iix7ImxlZ2FsX25hbWUiOiJMZXMgUm9zZXMgZCdPciBTQVJMIiwibGVnYWxfaWQiOiJGUlJDUy4xMjA2ODAwODgiLCJwZXBwb2xfaWQiOiIwMDAyOjEyMDY4MDA4OCJ9XQ~WyJ6X0UySDRhOUFyRmp3ODN1dzYxczdnIiwiYXBwcm92ZWRfc3VwcGxpZXIiLHsibGVnYWxfbmFtZSI6IkdyZWVuIEZsb3dlcnMgQi5WLiIsImxlZ2FsX2lkIjoiTkxOSFIuODUzNzQ2MjgiLCJwZXBwb2xfaWQiOiIwMTA2Ojg1Mzc0NjI4In1d~WyI1Ql9rNXQyMEx4RUdSU2dRS1lCSWZBIiwiYXBwcm92YWxfc2NvcGUiLCJwZXBwb2w6ZWludm9pY2UiXQ~WyJUSVJZR2JhSEV0by1Hdl9uWFZEa2FBIiwiYXBwcm92YWxfdmFsaWRfZnJvbSIsIjIwMjYtMDEtMDEiXQ~WyJ6bVAyVU05akd2b0RQWkdsWnhEVldBIiwiYXBwcm92YWxfdmFsaWRfdW50aWwiLCIyMDI2LTEyLTMxIl0~WyJSZG9zVy12TWJ3VWlqOUdmOXJxMHBBIiwiYXBwcm92YWxfcmVmZXJlbmNlIiwiUE8tRlJBTUUtMjAyNi0wMDQyIl0~
```

#### 5.1.2 Human-readable payload and disclosures (informative)

Header:

```json
{
  "alg": "ES256",
  "typ": "dc+sd-jwt",
  "kid": "lesrosesdor-ebw-issuer-test"
}
```

Issuer-signed payload:

```json
{
  "vct": "eu.we-build:approvedsupplier:1",
  "iss": "https://wallet.lesrosesdor.example/issuer",
  "iat": 1767225600,
  "exp": 1798761600,
  "attestation_legal_category": "EAA",
  "cryptographically_bound_to": "uri:eu.ebw.oid.1",
  "status": {
    "status_list": {
      "idx": 412,
      "uri": "https://wallet.lesrosesdor.example/status/approvedsupplier"
    }
  },
  "cnf": {
    "jwk": {
      "kty": "EC",
      "crv": "P-256",
      "x": "euJM7vou6hcN5Mp6b3R965Mcabz3edn1XwhBgBp601M",
      "y": "ykSGr2DnGNrnbcl8yQ-6Gn_YHpjR9MpBiXT7smgEnSQ"
    }
  },
  "_sd": [
    "8ukpneakB5FLj5J3NbG-PNTn1ujzR-8UJvaolZwyE20",
    "BSykNr6Y1GD2tM2DBbyupeuLH7LghilXukx-kR6xvpo",
    "DAiIZCieXWdyrkZRL2kibLibPdb3U7ydv3JsoJhFZDo",
    "PgfPyw9ByO4SXrtdJxLJlz-m2wW4cleFnvDWnQCA00k",
    "_2H-NlArAPtmC6Wr-pC1EYHNpr_zaTYgwDRauZjrtFE",
    "qIvgcstH8B3VxeIQYI-YWLcmkq1gomlqOvHiSoIv1Fo"
  ],
  "_sd_alg": "sha-256"
}
```

Disclosures (`[salt, claim name, claim value]`) and the digest each produces in `_sd`:

| Claim                  | Disclosure (decoded)                                         | Digest (SHA-256, base64url)                   |
| ---------------------- | ------------------------------------------------------------ | --------------------------------------------- |
| `approving_party`      | `["2Mtm5qQfJr4B_u2GqgnrfA", "approving_party", {"legal_name": "Les Roses d'Or SARL", "legal_id": "FRRCS.120680088", "peppol_id": "0002:120680088"}]` | `DAiIZCieXWdyrkZRL2kibLibPdb3U7ydv3JsoJhFZDo` |
| `approved_supplier`    | `["z_E2H4a9ArFjw83uw61s7g", "approved_supplier", {"legal_name": "Green Flowers B.V.", "legal_id": "NLNHR.85374628", "peppol_id": "0106:85374628"}]` | `BSykNr6Y1GD2tM2DBbyupeuLH7LghilXukx-kR6xvpo` |
| `approval_scope`       | `["5B_k5t20LxEGRSgQKYBIfA", "approval_scope", "peppol:einvoice"]` | `qIvgcstH8B3VxeIQYI-YWLcmkq1gomlqOvHiSoIv1Fo` |
| `approval_valid_from`  | `["TIRYGbaHEto-Gv_nXVDkaA", "approval_valid_from", "2026-01-01"]` | `PgfPyw9ByO4SXrtdJxLJlz-m2wW4cleFnvDWnQCA00k` |
| `approval_valid_until` | `["zmP2UM9jGvoDPZGlZxDVWA", "approval_valid_until", "2026-12-31"]` | `_2H-NlArAPtmC6Wr-pC1EYHNpr_zaTYgwDRauZjrtFE` |
| `approval_reference`   | `["RdosW-vMbwUij9Gf9rq0pA", "approval_reference", "PO-FRAME-2026-0042"]` | `8ukpneakB5FLj5J3NbG-PNTn1ujzR-8UJvaolZwyE20` |

#### 5.1.3 Presentation to the Access Point (informative)

When the Supplier presents the attestation to its Access Point (C2), it discloses the party objects,
scope and validity, withholds `approval_reference`, and appends a Key Binding JWT signed with the key
in `cnf`. The KB-JWT payload binds the presentation to the Access Point (`aud`), to the request
(`nonce`), and to the exact set of disclosures (`sd_hash`):

```json
{
  "iat": 1768392000,
  "aud": "https://ap.c2-provider.example",
  "nonce": "n-0S6_WzA2Mj",
  "sd_hash": "3LVf0NRMisfNvM52Qpz1jZD6f4TNytgYTiJ_rCVNhZA"
}
```

Presented SD-JWT+KB:

```
eyJhbGciOiJFUzI1NiIsInR5cCI6ImRjK3NkLWp3dCIsImtpZCI6Imxlc3Jvc2VzZG9yLWVidy1pc3N1ZXItdGVzdCJ9.eyJ2Y3QiOiJldS53ZS1idWlsZDphcHByb3ZlZHN1cHBsaWVyOjEiLCJpc3MiOiJodHRwczovL3dhbGxldC5sZXNyb3Nlc2Rvci5leGFtcGxlL2lzc3VlciIsImlhdCI6MTc2NzIyNTYwMCwiZXhwIjoxNzk4NzYxNjAwLCJhdHRlc3RhdGlvbl9sZWdhbF9jYXRlZ29yeSI6IkVBQSIsImNyeXB0b2dyYXBoaWNhbGx5X2JvdW5kX3RvIjoidXJpOmV1LmVidy5vaWQuMSIsInN0YXR1cyI6eyJzdGF0dXNfbGlzdCI6eyJpZHgiOjQxMiwidXJpIjoiaHR0cHM6Ly93YWxsZXQubGVzcm9zZXNkb3IuZXhhbXBsZS9zdGF0dXMvYXBwcm92ZWRzdXBwbGllciJ9fSwiY25mIjp7Imp3ayI6eyJrdHkiOiJFQyIsImNydiI6IlAtMjU2IiwieCI6ImV1Sk03dm91NmhjTjVNcDZiM1I5NjVNY2FiejNlZG4xWHdoQmdCcDYwMU0iLCJ5IjoieWtTR3IyRG5HTnJuYmNsOHlRLTZHbl9ZSHBqUjlNcEJpWFQ3c21nRW5TUSJ9fSwiX3NkIjpbIjh1a3BuZWFrQjVGTGo1SjNOYkctUE5UbjF1anpSLThVSnZhb2xad3lFMjAiLCJCU3lrTnI2WTFHRDJ0TTJEQmJ5dXBldUxIN0xnaGlsWHVreC1rUjZ4dnBvIiwiREFpSVpDaWVYV2R5cmtaUkwya2liTGliUGRiM1U3eWR2M0pzb0poRlpEbyIsIlBnZlB5dzlCeU80U1hydGRKeExKbHotbTJ3VzRjbGVGbnZEV25RQ0EwMGsiLCJfMkgtTmxBckFQdG1DNldyLXBDMUVZSE5wcl96YVRZZ3dEUmF1WmpydEZFIiwicUl2Z2NzdEg4QjNWeGVJUVlJLVlXTGNta3ExZ29tbHFPdkhpU29JdjFGbyJdLCJfc2RfYWxnIjoic2hhLTI1NiJ9._ppp2liZbMSCiEiwiTDZ-DIHAZLHkW_43Y90yppY3vbOZOq5yfTMZIrqGfmKsRTY70LDQkF3ATKDfo287I5HUw~WyIyTXRtNXFRZkpyNEJfdTJHcWducmZBIiwiYXBwcm92aW5nX3BhcnR5Iix7ImxlZ2FsX25hbWUiOiJMZXMgUm9zZXMgZCdPciBTQVJMIiwibGVnYWxfaWQiOiJGUlJDUy4xMjA2ODAwODgiLCJwZXBwb2xfaWQiOiIwMDAyOjEyMDY4MDA4OCJ9XQ~WyJ6X0UySDRhOUFyRmp3ODN1dzYxczdnIiwiYXBwcm92ZWRfc3VwcGxpZXIiLHsibGVnYWxfbmFtZSI6IkdyZWVuIEZsb3dlcnMgQi5WLiIsImxlZ2FsX2lkIjoiTkxOSFIuODUzNzQ2MjgiLCJwZXBwb2xfaWQiOiIwMTA2Ojg1Mzc0NjI4In1d~WyI1Ql9rNXQyMEx4RUdSU2dRS1lCSWZBIiwiYXBwcm92YWxfc2NvcGUiLCJwZXBwb2w6ZWludm9pY2UiXQ~WyJUSVJZR2JhSEV0by1Hdl9uWFZEa2FBIiwiYXBwcm92YWxfdmFsaWRfZnJvbSIsIjIwMjYtMDEtMDEiXQ~WyJ6bVAyVU05akd2b0RQWkdsWnhEVldBIiwiYXBwcm92YWxfdmFsaWRfdW50aWwiLCIyMDI2LTEyLTMxIl0~eyJhbGciOiJFUzI1NiIsInR5cCI6ImtiK2p3dCJ9.eyJpYXQiOjE3NjgzOTIwMDAsImF1ZCI6Imh0dHBzOi8vYXAuYzItcHJvdmlkZXIuZXhhbXBsZSIsIm5vbmNlIjoibi0wUzZfV3pBMk1qIiwic2RfaGFzaCI6IjNMVmYwTlJNaXNmTnZNNTJRcHoxalpENmY0VE55dGdZVGlKX3JDVk5oWkEifQ.XFfHyihUS3tV12ybAuAlJZzVtNOiag7BQH1kqOZtsaY60aAQLGlH8jdq-GZq61xNGb_4N_C9QbXUbmV5tzvMnQ
```

### 5.2 ISO/IEC 18013-5-compliant encoding

The Approved Supplier attestation is presented in automated, online, system-to-system flows between
European Business Wallets and Access Points (see chapter 9). There is no proximity or offline
presentation use case (EW-DM-12-003). Therefore an ISO/IEC 18013-5 (mdoc) encoding is **not
specified** in this version. If a future use case requires proximity presentation, a document type
and mdoc encoding would be added here.

### 5.3 W3C Verifiable Credentials Data Model-based encoding

**Status.** This encoding is **informative** until the vocabulary terms proposed below are published
in the European Business Wallet Vocabulary (EBWV) context by the WP4 semantics group. A Provider SHALL
NOT issue this encoding before then. SD-JWT VC (section 5.1) remains the normative format for SC5.

The Approved Supplier attestation is a non-qualified EAA, the only legal category permitted to use
the W3C VCDM format (EW-DM-12-001). The encoding uses [W3C VCDM v2.0] with the EBWV context, in line
with the other catalog rulebooks that define a VCDM encoding.

**Modelling.** In VCDM the credential subject is the party the claims are about. The
`credentialSubject` is therefore the approved Supplier, and the Buyer's approval is expressed as
properties of it (`approvedBy`, `approvalScope`, `approvalValidFrom`, `approvalValidUntil`). This
carries the same information as the SD-JWT VC claim set; section 5.3.1 gives the mapping.

**Securing mechanism.** The credential SHALL be secured as a JWT according to [VC-JOSE-COSE]. The JOSE
header SHALL carry the issuer's EBWOID-anchored certificate material in `x5c`, so the trust model of
chapter 10 applies unchanged. Data Integrity proofs are not used in this version, because the EBWOID
trust model anchors the issuer key in X.509 certificate material rather than in a verification method
resolved from the `issuer` identifier.

**Selective disclosure.** This encoding provides no selective disclosure. Because `approval_reference`
MUST be selectively disclosable (section 3.3), it SHALL NOT be included in the W3C VCDM encoding.
All other attributes are always disclosed.

**Holder binding.** `credentialSubject.id` SHALL be a `did:jwk` derived from the holder's public key,
which takes the role of `cnf` in the SD-JWT VC encoding. The Supplier proves possession of the
corresponding private key when presenting.

**Revocation.** `credentialStatus` SHALL use a `BitstringStatusListEntry` according to [W3C Bitstring
Status List], with `statusPurpose` `revocation`. *Open point:* the WE BUILD ADR on Attestation
Revocation mandates the IETF Token Status List; confirmation is needed that the W3C Bitstring Status
List is acceptable for the VCDM encoding, or that the Token Status List shall be used for both.

**Proposed vocabulary terms.** The following terms do not exist in EBWV and are proposed for
addition. Existing EBWV terms (`EconomicOperator`, `legalName`, `legalIdentifier`, `Euid`,
`attestationLegalCategory`, `ElectronicAttestationOfAttributes`) are reused.

| Term                         | Kind     | Definition                                                   |
| ---------------------------- | -------- | ------------------------------------------------------------ |
| `ApprovedSupplierCredential` | class    | A credential stating that an economic operator is approved as a supplier by another economic operator. |
| `approvedBy`                 | property | The economic operator (the Buyer) that has approved the subject as a supplier. |
| `approvalScope`              | property | Scope of the approval; values per code list 4.4.             |
| `approvalValidFrom`          | property | Date from which the approval is valid (business validity).   |
| `approvalValidUntil`         | property | Date until which the approval is valid (business validity).  |
| `peppolParticipantId`        | property | Peppol participant identifier of an economic operator, as `ICD:identifier`. |
| `PeppolParticipantId`        | datatype | Datatype for `peppolParticipantId` values, analogous to `Euid`. |

#### 5.3.1 Mapping of attestation attributes

| Rulebook attribute             | SD-JWT VC claim                | W3C VCDM property                                            |
| ------------------------------ | ------------------------------ | ------------------------------------------------------------ |
| Credential type                | `vct`                          | `type` includes `ApprovedSupplierCredential`                 |
| Legal category                 | `attestation_legal_category`   | `attestationLegalCategory`                                   |
| Issuer                         | `iss`                          | `issuer`                                                     |
| Technical validity             | `iat` / `nbf`, `exp`           | `validFrom`, `validUntil`                                    |
| Revocation                     | `status`                       | `credentialStatus`                                           |
| Holder binding                 | `cnf`                          | `credentialSubject.id` (`did:jwk`)                           |
| Binding to EBWOID              | `cryptographically_bound_to`   | not used; binding is evaluated at presentation               |
| `approved_supplier.legal_name` | `approved_supplier.legal_name` | `credentialSubject.legalName`                                |
| `approved_supplier.legal_id`   | `approved_supplier.legal_id`   | `credentialSubject.legalIdentifier` (`Euid`)                 |
| `approved_supplier.peppol_id`  | `approved_supplier.peppol_id`  | `credentialSubject.peppolParticipantId`                      |
| `approving_party.*`            | `approving_party`              | `credentialSubject.approvedBy` (`EconomicOperator`, same three properties) |
| `approval_scope`               | `approval_scope`               | `credentialSubject.approvalScope`                            |
| `approval_valid_from`          | `approval_valid_from`          | `credentialSubject.approvalValidFrom`                        |
| `approval_valid_until`         | `approval_valid_until`         | `credentialSubject.approvalValidUntil`                       |
| `approval_reference`           | `approval_reference`           | not included (see selective disclosure above)                |

#### 5.3.2 Illustrative example (informative, synthetic data)

Unsecured credential (the JWT claims set according to [VC-JOSE-COSE], media type `application/vc`):

```json
{
  "@context": [
    "https://www.w3.org/ns/credentials/v2",
    "https://w3id.org/ebwv/v0.1"
  ],
  "type": [
    "VerifiableCredential",
    "ElectronicAttestationOfAttributes",
    "ApprovedSupplierCredential"
  ],
  "id": "urn:uuid:3f1c2d4e-8a6b-4c7d-9e0f-1a2b3c4d5e6f",
  "issuer": "https://wallet.lesrosesdor.example/issuer",
  "validFrom": "2026-01-01T00:00:00Z",
  "validUntil": "2027-01-01T00:00:00Z",
  "attestationLegalCategory": "EAA",
  "credentialStatus": {
    "id": "https://wallet.lesrosesdor.example/status/approvedsupplier-bsl#412",
    "type": "BitstringStatusListEntry",
    "statusPurpose": "revocation",
    "statusListIndex": "412",
    "statusListCredential": "https://wallet.lesrosesdor.example/status/approvedsupplier-bsl"
  },
  "credentialSubject": {
    "id": "did:jwk:eyJrdHkiOiJFQyIsImNydiI6IlAtMjU2IiwieCI6ImV1Sk03dm91NmhjTjVNcDZiM1I5NjVNY2FiejNlZG4xWHdoQmdCcDYwMU0iLCJ5IjoieWtTR3IyRG5HTnJuYmNsOHlRLTZHbl9ZSHBqUjlNcEJpWFQ3c21nRW5TUSJ9",
    "type": "EconomicOperator",
    "legalName": "Green Flowers B.V.",
    "legalIdentifier": {
      "@type": "Euid",
      "@value": "NLNHR.85374628"
    },
    "peppolParticipantId": {
      "@type": "PeppolParticipantId",
      "@value": "0106:85374628"
    },
    "approvedBy": {
      "type": "EconomicOperator",
      "legalName": "Les Roses d'Or SARL",
      "legalIdentifier": {
        "@type": "Euid",
        "@value": "FRRCS.120680088"
      },
      "peppolParticipantId": {
        "@type": "PeppolParticipantId",
        "@value": "0002:120680088"
      }
    },
    "approvalScope": "peppol:einvoice",
    "approvalValidFrom": "2026-01-01",
    "approvalValidUntil": "2026-12-31"
  }
}
```

The credential reads: *Les Roses d'Or SARL has approved Green Flowers B.V. as a supplier of Peppol
eInvoices for 2026.* The validity in `validFrom`/`validUntil` is the technical validity of the
credential; `approvalValidFrom`/`approvalValidUntil` is the business validity of the approval, and
IR-AS-01 applies to both pairs.

## 6 Protocols

### 6.1 Issuance

| Protocol   | Supported | Profile or version                       | Specification        | Notes                                                        |
| ---------- | --------- | ---------------------------------------- | -------------------- | ------------------------------------------------------------ |
| OpenID4VCI | yes       | WE BUILD Conformance Specification cs-01 | [OpenID4VCI], [HAIP] | Credential format `dc+sd-jwt`. A credential format identifier for the W3C VCDM encoding is not yet profiled in cs-01. |

### 6.2 Presentation

| Protocol                   | Supported | Profile or version                             | Specification       | Notes                                                       |
| -------------------------- | --------- | ---------------------------------------------- | ------------------- | ----------------------------------------------------------- |
| OpenID4VP, remote          | yes       | WE BUILD Conformance Specification cs-02, DCQL | [OpenID4VP], [HAIP] | Machine-to-machine, no human in the loop at runtime (WA1.3) |
| ISO/IEC 18013-5, proximity | no        |                                                | [ISO/IEC 18013-5]   | Requires the mdoc format, which is not defined              |

Protocols listed here are those referenced in Topic 6 of Annex 2 of the ARF. This Rulebook does not
profile these protocols beyond what is stated in the tables.

## 7 Issuance

### 7.1 Binding

| Field                                | Value                       | Source       |
| ------------------------------------ | --------------------------- | ------------ |
| Device-bound                         | SHOULD                      | EW-DM-12-038 |
| Cryptographically bound to           | `uri:eu.ebw.oid.1` (SHOULD) | EW-DM-12-032 |
| Relying Party must also verify a PID | no                          | EW-DM-12-031 |
| Binding subject                      | legal person                |              |

**Device binding.** An attestation of this type SHOULD be device-bound to the holder's Wallet Unit
(the Supplier's EBW), evidenced by the `cnf` claim and verified through key binding at presentation
(base verification step 4.2.8).

**Binding to another attestation.** An attestation of this type SHOULD be cryptographically bound to
the Supplier's organisational identity attestation (EBWOID) on the same Wallet Unit. Where present,
the binding metadata identifier SHALL be `cryptographically_bound_to`, its value SHALL be a string
containing the bound attestation's vct, and that value SHALL be `uri:eu.ebw.oid.1` (the EBWOID vct
defined in [rb-ebwoid]).

**PID.** A Relying Party (C2) does not request or verify a PID. The holder is a legal person, not a
natural person; identity assurance is provided by the EBWOID binding (chapter 10), not by a PID.

### 7.2 Issuance Policy

The issuer is the Buyer (C4), a legal person self-issuing this EAA through its EBW after having
established the commercial relationship with the Supplier outside the wallet system (e.g. via a
procurement process). Issuance uses OpenID4VCI as profiled by the WE BUILD Conformance Specification
cs-01.

The Issuer SHALL implement the base issuer obligations defined in the Base Verification specification:
<https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-base/verifier-base-verification.md#41-issuer-obligations>

In particular, the issuer SHALL include the holder-generated public key (`cnf`) in the payload, SHALL
include its own EBWOID-anchored certificate material in the attestation header (see chapter 10), and
SHALL populate the `status` metadata (see chapter 8) in every issued attestation.

### 7.3 Lifecycle management

The issuer sets the validity period of the attestation and reissues it when the
underlying facts change, revoking the superseded attestation as described in chapter 8.

### 7.4 Embedded disclosure policy

This attestation defines no embedded disclosure policy.

## 8 Revocation

An Approved Supplier attestation SHALL remain valid only while the underlying commercial approval is in
effect. The attestation is **revocable** (it is not a short-lived ≤24h attestation, since approvals
typically persist for the duration of a commercial relationship).

### 8.1 Revocation mechanism

* **Token Status List:** the issuer SHALL maintain an active IETF Token Status List ([Token Status
  List]), aligned with the Attestation Status List mechanism specified by the EU Commission and
  mandated by the WE BUILD ADR on Attestation Revocation.
* **Credential metadata:** the `status` claim SHALL be populated in every issued SD-JWT VC as
  `status.status_list`, containing:
  * `idx` (integer, ≥ 0), the index of this attestation in the status list;
  * `uri` (string, URI), the URI of the Status List Token that contains the status of this
    attestation.
* **Status values:** the status `VALID` (0x00) and `INVALID` (0x01) of [Token Status List] are used.
  `INVALID` denotes revocation.
* **W3C VCDM encoding:** see section 5.3 for `credentialStatus`.
* **Authorized authority:** only the issuing Buyer (the self-issuing legal entity) may modify the
  status list entry.

### 8.2 Revocation triggers and business rules

* **Issuer trigger (obligation):** the Buyer SHALL revoke the attestation without undue delay when the
  underlying commercial relationship ends, when the approval scope no longer applies, or when the
  Supplier's identity data becomes inaccurate.
* **Relying Party action:** a revoked or suspended attestation SHALL be treated as invalid; C2 SHALL
  reject invoice submissions relying on it. The business interpretation of a revocation (e.g. grace
  handling for invoices already in flight) is determined by the Relying Party's internal policies.

## 9 Presentation

### 9.1 Presentation Policy

To verify and validate a received presentation of an attestation of this type, the
following steps SHALL be performed:

1. verify the signature over the attestation using a trust anchor obtained as
   described in chapter 10;
2. verify that the attestation is within its validity period;
3. check revocation status as described in chapter 8, unless the attestation is
   short-lived, or its remaining lifetime is below the revocation time threshold;
4. verify device binding where section 7.1 records the attestation as device-bound;
5. request only those attributes that are necessary for the stated purpose of the
   transaction, and, where the trust model for this attestation requires Relying Party
   registration, only those attributes it is registered and authorised to request.

In addition, the following obligations are specific to this attestation type. When receiving and
processing an Approved Supplier attestation, the Relying Party (C2) SHALL:

* perform the base attestation verification process for EAAs as defined in the
  [rb-base, Base Verification] specification, section 4.2. This covers verification of attestation
  authenticity and issuer identity via the EBWOID chain (4.2.2–4.2.4), validity periods (4.2.5),
  revocation status (4.2.6), wallet integrity via the WUA (4.2.7), and holder key binding (4.2.8);
* where the attestation carries `cnf`, verify the Key Binding JWT, including `aud`, `nonce` and
  `sd_hash` (see the example in section 5.1.3);
* apply the integrity rules IR-AS-01 to IR-AS-03 defined in section 4.5. In particular (IR-AS-03),
  C2 SHALL match the attestation's `approved_supplier.peppol_id` and `approving_party.peppol_id`
  against, respectively, the sender and buyer participant identifiers of the invoice in flight, and
  SHALL reject the invoice submission on mismatch;
* request `approving_party`, `approved_supplier`, `approval_scope` and `approval_valid_from`, and
  `approval_valid_until` where present. C2 SHOULD NOT request `approval_reference`, which is not
  needed for the verification purpose.

Where the Relying Party is itself an EBW-based system, the Mutual Identification & Consent Handshake
defined in [rb-base, Handshake] SHOULD be applied before presentation.

### 9.2 Presentation modes

Remote presentation is in scope. Proximity presentation is not in scope, as no mdoc encoding is
defined (chapter 5).

### 9.3 Transactional data

No transactional data as defined in Topic 20 of Annex 2 of the ARF is associated with this
attestation type. The attestation authorises a *relationship*, not an individual payment.

## 10 Trust Framework

This chapter specifies how a Relying Party establishes trust in the issuer of an Approved Supplier
attestation. The corresponding verification procedures are steps 4.2.2–4.2.4 of the Base Verification
specification.

The Approved Supplier attestation is an **EAA self-issued by a legal entity** (the Buyer). Buyers are
not, and cannot practically be, individually registered on a Trusted List. Trust is therefore
established through a cryptographic chain anchored in the issuer's **EBWOID**, following the common
WE BUILD EAA trust model:

* The issuer's EBWOID-anchored certificate material SHALL be included in the header (`x5c`) of every
  issued Approved Supplier attestation, in both the SD-JWT VC and the W3C VCDM encoding. During EBWOID
  issuance, the EBWOID provider verifies that the public key contained in the EBWOID is owned by the
  EBW owner.
* The Relying Party SHALL verify the EBWOID in accordance with [rb-ebwoid] and the Base Verification
  specification. The EBWOID provider's trust anchor is obtained via the WE BUILD trust list
  infrastructure (TLOL) operated under WP4.
* Upon successful verification, the Relying Party obtains: assurance that the EBWOID was issued by an
  authorised provider (and is not self-issued); the verified identity of the issuer, including its
  legal name and EUID; and the public key authorised to verify the attestation signature.
* The Relying Party SHALL then confirm that the verified issuer identity (EUID) matches
  `approving_party.legal_id` in the attestation payload.

Authorization of the issuer *as a Buyer* is subsequently determined in accordance with the Relying
Party's internal policies (e.g. C2 confirming that the approving party is a registered Peppol
participant it can route to), optionally supported by domain-specific trust list services.

**Trust anchor location.** The trust anchor location is the EBWOID provider's entry in the WE BUILD
trust list infrastructure. Where the optional `trust_anchor_url` metadata (section 4.2) is present, it
SHALL contain at least the URL at which a machine-readable version of that entry can be found or
looked up.

## 11 References

| **Item Reference**                     | **Standard name/details**                                    |
| -------------------------------------- | ------------------------------------------------------------ |
| [European Digital Identity Regulation] | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework |
| [ETSI TS 119 472-1]                    | ETSI TS 119 472-1, Electronic Signatures and Trust Infrastructures (ESI); Profiles for Electronic Attestation of Attributes; Part 1: General requirements |
| [HAIP]                                 | OpenID4VC High Assurance Interoperability Profile, OpenID Foundation |
| [IANA-JWT-Claims]                      | IANA JSON Web Token Claims Registry. <https://www.iana.org/assignments/jwt/jwt.xhtml> |
| [ISO/IEC 18013-5]                      | ISO/IEC 18013-5, Personal identification, ISO-compliant driving licence, Part 5: Mobile driving licence (mDL) application |
| [RFC 2119]                             | Key words for use in RFCs to Indicate Requirement Levels, S. Bradner, March 1997 |
| [RFC 3339]                             | Date and Time on the Internet: Timestamps, G. Klyne et al., July 2002 |
| [SD-JWT VC]                            | SD-JWT-based Verifiable Credentials. <https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/> |
| [Token Status List]                    | Token Status List, IETF OAuth WG. <https://datatracker.ietf.org/doc/draft-ietf-oauth-status-list/> |
| [W3C VCDM v2.0]                        | Verifiable Credentials Data Model v2.0, W3C. <https://www.w3.org/TR/vc-data-model-2.0/> |
| [VC-JOSE-COSE]                         | Securing Verifiable Credentials using JOSE and COSE, W3C. <https://www.w3.org/TR/vc-jose-cose/> |
| [W3C Bitstring Status List]            | Bitstring Status List v1.0, W3C. <https://www.w3.org/TR/vc-bitstring-status-list/> |
| [EBWV]                                 | European Business Wallet Vocabulary. <https://w3id.org/ebwv> |
| [OpenID4VCI]                           | OpenID for Verifiable Credential Issuance, OpenID Foundation |
| [OpenID4VP]                            | OpenID for Verifiable Presentations, OpenID Foundation       |
| [Topic 7]                              | ARF Annex 2, Topic 7, Attestation revocation and revocation checking |
| [Topic 10]                             | ARF Annex 2, Topic 10, Issuing a PID or attestation to a Wallet Unit |
| [Topic 12]                             | ARF Annex 2, Topic 12, Attestation Rulebooks                 |
| [Topic 20]                             | ARF Annex 2, Topic 20, Strong User authentication for electronic payments |
| [Peppol BIS Billing 3.0]               | OpenPeppol Business Interoperability Specification, Billing 3.0 |
| [EN 16931]                             | European standard on the semantic data model of the core elements of an electronic invoice |
| [EWC RB001]                            | EWC LPID Rulebook                                            |
| [EWC RB002]                            | EWC EUCC Rulebook                                            |
| [WP4 Blueprint]                        | WE BUILD Deliverable D4.1 (trust infrastructure blueprint)   |
| [WBCS]                                 | WE BUILD Conformance Specifications, cs-01 (issuance) and cs-02 (presentation) |
| [WE BUILD ADR, Revocation]             | WE BUILD Architecture Decision Record on Attestation Revocation |
| [rb-base, Base Verification]           | WE BUILD Rulebook for common verification steps for all attestations. <https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-base/verifier-base-verification.md> |
| [rb-base, Handshake]                   | WE BUILD Rulebook for Mutual Identification & Consent Handshake. <https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-base/holder-authorization-handshake.md> |
| [rb-ebwoid]                            | WE BUILD EBWOID Rulebook. <https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-ebwoid/README.md> |
