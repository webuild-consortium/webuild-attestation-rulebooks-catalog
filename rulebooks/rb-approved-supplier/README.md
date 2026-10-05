# Attestation Rulebook for attestations of type Approved Supplier

Category: non-qualified EAA

*This Rulebook is derived from the WE BUILD v1.1 Attestation Rulebook Template (itself derived from
the EUDI attestation rulebook template) and keeps the template's chapter structure. It specifies the
Approved Supplier attestation used in WE BUILD Use Case SC5 (eInvoicing), Scenario 1 (Supplier
pre-approval).*

* Author(s):
    * Rune Kjørlaug, Emning AS / OpenPeppol (SC5 co-lead)

**Feedback:**

* [WE BUILD SC5 issue tracker](https://github.com/webuild-consortium/SC5/issues)

| Version | Date | Description |
| --- | --- | --- |
| 1.1 | 2026-10-02 | Restructured onto the generic WE BUILD attestation rulebook template (11 chapters). No normative content removed. |

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
- [6 Protocols](#6-protocols)
- [7 Issuance](#7-issuance)
   * [7.1 Binding](#71-binding)
   * [7.2 Issuance Policy](#72-issuance-policy)
   * [7.3 Lifecycle management](#73-lifecycle-management)
   * [7.4 Embedded disclosure policy](#74-embedded-disclosure-policy)
- [8 Revocation](#8-revocation)
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
* **Source material:** the SC5 eInvoicing scenario specification (SC5_Introduction.md and
  SC5_Scenario1_SupplierPreApproval.md). Actor terminology (C1–C4, EBW, EBWOID, Access Point) is kept
  aligned with that specification and with the Peppol Interoperability Framework.

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
WE BUILD LoTL, WE BUILD Trusted List) as defined in the SC5 specification and the WP4 Blueprint.

## 2 Compliance

### 2.1 Compliance statement

This Rulebook complies with the applicable requirements of Topic 12, Attestation
Rulebooks, in Annex 2 of the Architecture and Reference Framework, version 3.0.0. It
uses the terminology of Annex 1 of the ARF.

This Rulebook follows the structure mandated by [Topic 12] of the ARF and the WE BUILD Attestation
Rulebook Template v1.1. The Approved Supplier attestation is a **non-qualified EAA** in the sense of
the [European Digital Identity Regulation] and is implemented within the WE BUILD pilot trust framework
rather than the eIDAS production ecosystem (WA1.1, WA1.5; WP4 Blueprint D4.1 §1.2.1). It uses the
SD-JWT VC format profiled by [HAIP], OpenID4VCI for issuance and OpenID4VP for presentation per the WE
BUILD Conformance Specifications (cs-01, cs-02), and the IETF Token Status List for revocation per the
WE BUILD ADR on Attestation Revocation. Escalation to an eIDAS-qualified EAA (QEAA), and any associated
QTSP involvement, is a post-pilot decision and out of scope for this version.

### 2.2 Regulatory basis

This attestation is not a qualified electronic attestation of attributes. The data
described in Annex V points b, c and e of Regulation (EU) 2024/1183 is addressed as
required by EW-DM-12-018 and as recommended by EW-DM-12-020 and EW-DM-12-022. Where a
recommendation is not followed, the reason is stated below.

### 2.3 Traceability

Every applicable requirement mapped to the section that satisfies it. Requirements
marked not applicable carry a stated reason.

| Requirement | Legacy ID | Applies | Satisfied in section | Note |
| --- | --- | --- | --- | --- |
| EW-DM-12-001 | ARB_01a | yes | 5 | W3C VCDM permitted for this category; no encoding defined in this version |
| EW-DM-12-002 | ARB_01b | yes | 5 | SD-JWT VC following the HAIP profile |
| EW-DM-12-003 | ARB_02 | no |  | Proximity presentation is not in scope |
| EW-DM-12-005 | ARB_04 | no |  | No W3C VCDM encoding is defined in this version |
| EW-DM-12-006 | ARB_05 | yes | 5 | Unique vct for this attestation type |
| EW-DM-12-007 | ARB_06 | yes | 3 | Attributes defined independently of encoding |
| EW-DM-12-008 | ARB_06a | no |  | No mdoc encoding is defined in this version |
| EW-DM-12-009 | ARB_06b | yes | 5 | SD-JWT VC claim naming |
| EW-DM-12-010 | ARB_07 | yes | 3 | Attributes reused from the catalogued vocabulary where one exists |
| EW-DM-12-012 | ARB_09 | yes | 3, 4 | Mandatory, optional and conditional stated per attribute |
| EW-DM-12-013 | ARB_10 | no |  | No domestic namespace is defined |
| EW-DM-12-014 | ARB_11 | no |  | Annex V and VII point a apply to QEAA and PuB-EAA |
| EW-DM-12-015 | ARB_12 | yes | 4.1 | EAA indication for a non-qualified EAA |
| EW-DM-12-016 / EW-DM-12-017 / EW-DM-12-018 | ARB_13 / ARB_14 / ARB_15 | yes | 2.2, 4.1 | Point b, EW-DM-12-018 for the non-qualified case |
| EW-DM-12-019 / EW-DM-12-020 | ARB_16 / ARB_17 | yes | 2.2 | Point c, recommendation for non-qualified EAA |
| EW-DM-12-021 / EW-DM-12-022 | ARB_18 / ARB_19 | yes | 2.2, 4.2 | Point e, recommendation for non-qualified EAA |
| EW-DM-12-023 / EW-DM-12-024 | ARB_20 / ARB_21 | yes | 4.2, 10 | Trust anchor location and the trust framework |
| EW-DM-12-029 | ARB_25 | yes | 4.1 | Legal category attribute; see the note in section 4.1 |
| EW-DM-12-030 | ARB_26 | yes | 10 | Trust anchor publication for non-qualified EAA |
| EW-DM-12-031 | ARB_27 | no |  | This attestation does not require the Relying Party to verify a PID |
| EW-DM-12-032 | ARB_28 | no |  | cryptographically_bound_to is not used by this attestation |
| EW-DM-12-034 | ARB_30 | yes | 5 | Selective disclosure stated per claim |
| EW-DM-12-035 | ARB_31 | no |  | No Claim Selective Disclosure Metadata document is used |
| EW-DM-12-038 | ARB_34 | yes | 7.1 | Device binding |

## 3 Attestation attributes

Attributes are defined here in an encoding-independent manner (EW-DM-12-007). The
encoding of each attribute is given in chapter 5.

### 3.1 Introduction


The Approved Supplier attestation expresses a single business relationship: a Buyer's approval of a
Supplier. The design models two parties, the **approving party** (the Buyer, who is also the technical
issuer) and the **approved supplier** (the Supplier, who is the holder/subject), together with the
scope and validity of the approval.

Per ARB_12 of [Topic 12], this document defines the attribute **`attestation_legal_category`**, which
for this attestation type SHALL have the value **`EAA`**.

**Logical model (informative):**

```
ApprovedSupplierAttestation
├── attestation_legal_category : "EAA"
├── approving_party            (the Buyer, C4, also the issuer)
│   ├── legal_name
│   ├── legal_id               (EUID / LPID, from the Buyer's EBWOID)
│   └── peppol_id              (Peppol participant identifier)
├── approved_supplier          (the Supplier, C1, the holder/subject)
│   ├── legal_name
│   ├── legal_id               (EUID / LPID, from the Supplier's EBWOID)
│   └── peppol_id
├── approval_scope             (code list, see 2.8)
├── approval_valid_from        (date)
└── approval_valid_until       (date; see also the exp metadata claim)
```

This model refines the flat claim list in the SC5 specification (issuer_id, issuer_name, subject_id,
subject_name, scope, approval_date, expiry_date, buyer_peppol_id, supplier_peppol_id) into two grouped
party objects, while preserving the same information content.

Subsections 2.2–2.7 define the attributes and metadata. Section 2.8 documents the scope code list and
Section 2.9 the integrity rules.

#### Chapter overview and requirements

This chapter defines all attributes and metadata that an Approved Supplier attestation may contain, in
an encoding-independent manner (ARB_06 in [Topic 12]). Each attribute is marked mandatory, optional, or
conditional in its section (ARB_09).

**Applicable legal category.** Per SC5 working assumption WA1.1, the Approved Supplier attestation is
implemented as a **non-qualified EAA** for the WE BUILD pilot. A qualification mandate (QEAA) would
require QTSP involvement and is treated as a post-pilot decision. Where the SC5 specification refers to
a "WE BUILD QEAA", this denotes a technically interoperable, ITB-tested attestation within the pilot
trust framework, not an eIDAS-qualified EAA (WA1.5). The requirements for non-qualified EAA in
[Topic 12] therefore apply:

* An attribute indicating that the attestation is an EAA SHOULD be included (ARB_12). See Section 2.1.
* One or more attributes or metadata representing identification data of the issuer SHALL be included
  (ARB_15).
* One or more attributes representing the subject SHOULD be included (ARB_17).
* Attributes or metadata representing the validity period SHOULD be defined (ARB_19).
* Attributes or metadata representing the location of the trust anchor SHOULD be defined (ARB_21); see
  Chapter 5.

### 3.2 Mandatory attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| `approving_party.legal_name` | N/A (WE BUILD SC5 domestic namespace) | Registered legal name of the Buyer that issues the approval. | string | `Les Roses d'Or SARL` |
| `approving_party.legal_id` | EUID (Regulation (EU) 2017/1132) | Unique legal-person identifier of the Buyer, sourced from the Buyer's EBWOID. | string | `FR59120680088` |
| `approving_party.peppol_id` | Peppol Participant Identifier | Peppol participant identifier of the Buyer (scheme::value). | string | `0009:FR59120680088` |
| `approved_supplier.legal_name` | N/A (WE BUILD SC5 domestic namespace) | Registered legal name of the approved Supplier (the holder). | string | `Green Flowers B.V.` |
| `approved_supplier.legal_id` | EUID (Regulation (EU) 2017/1132) | Unique legal-person identifier of the Supplier, sourced from the Supplier's EBWOID. | string | `NL853746281B01` |
| `approved_supplier.peppol_id` | Peppol Participant Identifier | Peppol participant identifier of the Supplier. | string | `0106:853746281` |
| `approval_scope` | N/A (see code list 2.8) | Scope of the approval. | string (enum) | `peppol:einvoice` |
| `approval_valid_from` | N/A | Date from which the approval is valid. | full-date (RFC 3339) | `2026-01-01` |

### 3.3 Optional attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| `approval_valid_until` | N/A | Date until which the approval is valid (business validity, distinct from the technical `exp` metadata claim). | full-date (RFC 3339) | `2026-12-31` |
| `approval_reference` | N/A | Buyer-internal reference for the underlying commercial relationship (e.g. framework agreement or contract number). | string | `PO-FRAME-2026-0042` |

### 3.4 Conditional attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| N/A | N/A | No conditional attributes are defined for this attestation type in v0.1. | N/A | N/A |

## 4 Metadata

Metadata describes the attestation rather than its subject.

### 4.1 Mandatory metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| `attestation_legal_category` | Defined in Section 2.1 | Indicates the legal category of the attestation. | string | `EAA` |
| `vct` | [SD-JWT VC] | Verifiable Credential Type identifier (see Section 3.2). | string | `eu.we-build:approvedsupplier:1` |
| `iss` | [IANA-JWT-Claims] | Issuer identifier (the Buyer's issuing system / EBW). | string (URI) | `https://wallet.lesrosesdor.example/issuer` |
| `iat` | [IANA-JWT-Claims] | Issuance timestamp. | NumericDate | `1767225600` |
| `exp` | [IANA-JWT-Claims] | Technical expiry timestamp of the attestation. | NumericDate | `1798761600` |
| `status` | [SD-JWT VC] / [Token Status List] | Reference to the Token Status List entry for revocation (see Chapter 6). | object | *(see Chapter 6)* |
| `cnf` | [SD-JWT VC] | Holder key-binding confirmation (proof of possession by the Supplier's EBW). | object | *(JWK / key reference)* |

**Legal category.** This Rulebook retains the `attestation_legal_category` attribute.
Section 4.1 of the generic template replaces it with the `category` attribute of
[ETSI TS 119 472-1], whose value for this category is `eaa:eu:non-qualified`.
EW-DM-12-029, legacy ARB_25, of ARF version 3.0.0 is a SHALL that still requires
`attestation_legal_category`, so the template and the ARF disagree. The attribute is
left as written and the deviation is recorded for the rulebook quality assurance group.

### 4.2 Optional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| `cryptographically_bound_to` | ARB_28 / [Topic 12] | vct of another attestation on the same Wallet Unit to which this attestation is cryptographically bound (the Supplier's EBWOID). RECOMMENDED, see Chapter 4. | string | `uri:eu.ebw.oid.1` |

### 4.3 Conditional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| N/A | N/A | No conditional metadata is defined in v0.1. | N/A | N/A |

### 4.4 Code lists

| **Field name** | **Allowed values** | **Meaning** | **Source / vocabulary** | **Notes / extensibility** |
| --- | --- | --- | --- | --- |
| `approval_scope` | `peppol:einvoice` | The Buyer approves the Supplier for sending Peppol BIS Billing 3.0 eInvoices. | WE BUILD SC5 domestic vocabulary | Default value for MVP. |
| `approval_scope` | `all` | The Buyer approves the Supplier for all SC5-relevant document exchange. | WE BUILD SC5 domestic vocabulary | Additional values SHOULD only be introduced if defined consistently across issuer and verifier implementations and registered in the WE BUILD Attestation Rulebooks catalog. |

### 4.5 Integrity rules

| **Rule ID** | **Rule statement** | **Why it exists** | **Where enforced** | **Verifier / issuer behavior on failure** |
| --- | --- | --- | --- | --- |
| `IR-AS-01` | `approval_valid_from` SHALL NOT be later than `approval_valid_until` (when the latter is present), and both SHALL fall within the `iat`–`exp` window. | Prevents inconsistent or unusable validity periods. | Issuer business rules; verifier business validation. | Issuer SHALL reject; verifier SHALL treat the attestation as invalid for the transaction. |
| `IR-AS-02` | The `approving_party.peppol_id` SHALL identify the same legal person as `approving_party.legal_id`; likewise for the approved supplier. | Ensures the Peppol identifier and the legal identifier refer to the same party, so verification at C2 is unambiguous. | Issuer; verifier cross-check against EBWOID. | Verifier SHALL treat the attestation as invalid. |
| `IR-AS-03` | At verification time, the `approved_supplier.peppol_id` SHALL match the C1 participant identifier on the invoice being submitted, and `approving_party.peppol_id` SHALL match the invoice's buyer participant identifier. | Binds the approval to the specific invoice flow, preventing reuse of a valid attestation for an unrelated buyer/supplier pair. | Verifier (C2) business validation. | Verifier SHALL reject the invoice submission. |


## 5 Formats


### 5.1 SD-JWT VC-based encoding

This attestation type SHALL be issued in the [SD-JWT VC]-compliant format and SHALL comply with the
'SD-JWT VCs' profile specified in [HAIP] (ARB_01b).

**Verifiable Credential Type (`vct`):** `eu.we-build:approvedsupplier:1`

*(Proposed value; subject to registration in the WE BUILD Attestation Rulebooks catalog by the WP4
semantics group, ARB_05.)*

For all claims, the table below specifies whether an Attestation Provider MUST, MAY, or MUST NOT make
the claim selectively disclosable (ARB_30). A Type Metadata Document SHOULD be defined for this vct per
Chapter 6 of [SD-JWT VC] (ARB_31).

A JSON Schema for this encoding is published in the catalog at
`data-schemas/sd-jwt/approved-supplier-sd-jwt.json`, with sample data at
`data-schemas/sd-jwt/sample-data/approved-supplier-sd-jwt-sample.json`.

**Registered / standard claims:**

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Reference/Notes** | **Disclosable** |
| --- | --- | --- | --- | --- |
| `iss` | iss | string | [IANA-JWT-Claims] | MUST NOT |
| `iat` | iat | number | [IANA-JWT-Claims] | MUST NOT |
| `exp` | exp | number | [IANA-JWT-Claims] | MUST NOT |
| `vct` | vct | string | [SD-JWT VC] | MUST NOT |
| `status` | status | object | [Token Status List]; Chapter 6 | MUST NOT |
| `cnf` | cnf | object | [SD-JWT VC]; holder binding | MUST NOT |

**Private claims specific to this attestation type:**

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Notes** | **Disclosable** |
| --- | --- | --- | --- | --- |
| `attestation_legal_category` | attestation_legal_category | string | Section 2.1 | MUST NOT |
| `approving_party` | approving_party | object | Buyer (C4) | MAY |
| `approved_supplier` | approved_supplier | object | Supplier (C1) | MAY |
| `approval_scope` | approval_scope | string | Code list 2.8 | MAY |
| `approval_valid_from` | approval_valid_from | string (full-date) |  | MAY |
| `approval_valid_until` | approval_valid_until | string (full-date) | Optional | MAY |
| `approval_reference` | approval_reference | string | Optional | MUST, issuer SHALL make selectively disclosable so the Supplier can withhold the internal reference |
| `cryptographically_bound_to` | cryptographically_bound_to | string | Section 2.6; Chapter 4 | MUST NOT |

**Illustrative JWT claim set (informative, synthetic data):**

```json
{
  "vct": "eu.we-build:approvedsupplier:1",
  "iss": "https://wallet.lesrosesdor.example/issuer",
  "iat": 1767225600,
  "exp": 1798761600,
  "attestation_legal_category": "EAA",
  "status": { "status_list": { "idx": 412, "uri": "https://status.webuild.example/sc5/approved_supplier" } },
  "cnf": { "jwk": { "kty": "EC", "crv": "P-256", "x": "...", "y": "..." } },
  "approving_party": {
    "legal_name": "Les Roses d'Or SARL",
    "legal_id": "FR59120680088",
    "peppol_id": "0009:FR59120680088"
  },
  "approved_supplier": {
    "legal_name": "Green Flowers B.V.",
    "legal_id": "NL853746281B01",
    "peppol_id": "0106:853746281"
  },
  "approval_scope": "peppol:einvoice",
  "approval_valid_from": "2026-01-01",
  "approval_valid_until": "2026-12-31"
}
```

[RULEBOOK AUTHOR TO PROVIDE AN EXAMPLE OF THE ISSUED SD-JWT IN base64 ENCODING ONCE A REFERENCE
ISSUER IS AVAILABLE]

[RULEBOOK AUTHOR TO PROVIDE A HUMAN-READABLE VERSION OF THE SD-JWT PAYLOAD WITH THE DISCLOSURES,
ONCE THE SELECTIVE-DISCLOSURE STRUCTURE IS FINALISED WITH WP4]

### 5.2 ISO/IEC 18013-5-compliant encoding

The Approved Supplier attestation is presented in automated, online, system-to-system flows between
European Business Wallets and Access Points (see Chapter 4). There is no proximity / offline
presentation use case (ARB_02). Therefore an ISO/IEC 18013-5 (mdoc) encoding is **not specified** in
this version. If a future use case requires proximity presentation, a document type and mdoc encoding
would be added here.

### 5.3 W3C Verifiable Credentials Data Model-based encoding

A W3C VCDM encoding is **not specified** for this attestation type. SD-JWT VC (Section 3.2) is the
single normative encoding for SC5, consistent with the WE BUILD Conformance Specifications. (Note that
only a non-qualified EAA may use the VCDM format, ARB_01a; this attestation is a non-qualified EAA, so
a VCDM encoding could be added in future if an interoperability need arises.)

## 6 Protocols

This attestation is issued using OpenID for Verifiable Credential Issuance
[OpenID4VCI] and presented using OpenID for Verifiable Presentations [OpenID4VP], both
as profiled by [HAIP].

## 7 Issuance

### 7.1 Binding

| Field | Value | Source |
| --- | --- | --- |
| Device-bound | MAY | EW-DM-12-038 |
| Cryptographically bound to | none | EW-DM-12-032 |
| Relying Party must also verify a PID | no | EW-DM-12-031 |
| Binding subject | legal person |  |

### 7.2 Issuance Policy

**Primary use case.** SC5 Scenario 1 (Supplier pre-approval). The Supplier (C1) holds the attestation
in its EBW and presents it, in a machine-to-machine OpenID4VP flow, to its Access Point (C2) so that
C2 can verify the Buyer's approval before transmitting an invoice into the Peppol network.

**PID verification (ARB_27).** A relying party (C2) **does not** request or verify a PID. The holder is
a legal person, not a natural person; identity assurance is provided by the EBWOID binding (see
Chapter 5), not by a PID.

**Presentation requirements.** Presentation is online and system-to-system via OpenID4VP, using DCQL
queries as profiled by the WE BUILD Conformance Specification cs-02. There is no human-in-the-loop
wallet interaction at runtime (WA1.3). No offline / proximity presentation is supported. Where the
relying party is itself an EBW-based system, the Mutual Identification & Consent Handshake defined in
[rb-base, Handshake] SHOULD be applied before presentation.

**Device binding (ARB_34).** An attestation of this type SHOULD be device-bound to the holder's Wallet
Unit (the Supplier's EBW), evidenced by the `cnf` claim and verified through key binding at
presentation (base verification step 4.2.8).

**Binding to another attestation (ARB_28).** An attestation of this type SHOULD be cryptographically
bound to the Supplier's organisational identity attestation (EBWOID) on the same Wallet Unit. Where
present, the binding metadata identifier SHALL be `cryptographically_bound_to`, its value SHALL be a
string containing the bound attestation's vct, and that value SHALL be `uri:eu.ebw.oid.1` (the EBWOID
vct defined in [rb-ebwoid]).

**Transactional data ([Topic 20]).** No payment-authentication transactional data is defined for this
attestation type. The attestation authorises a *relationship*, not an individual payment, so the
strong-user-authentication transactional-data mechanism of [Topic 20] does not apply.

The issuer is the Buyer (C4), a legal person self-issuing this EAA through its EBW after having
established the commercial relationship with the Supplier outside the wallet system (e.g. via a
procurement process). Issuance uses OpenID4VCI as profiled by the WE BUILD Conformance Specification
cs-01.

The Issuer SHALL implement the base issuer obligations defined in the Base Verification specification:
<https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-base/verifier-base-verification.md#41-issuer-obligations>

In particular, the issuer SHALL include the holder-generated public key (`cnf`) in the payload, SHALL
include its own EBWOID-anchored certificate material in the attestation header (see Chapter 5), and
SHALL populate the `status` metadata (see Chapter 6) in every issued attestation.

### 7.3 Lifecycle management

The issuer sets the validity period of the attestation and reissues it when the
underlying facts change, revoking the superseded attestation as described in chapter 8.

### 7.4 Embedded disclosure policy

This attestation defines no embedded disclosure policy.

## 8 Revocation

An Approved Supplier attestation SHALL remain valid only while the underlying commercial approval is in
effect. The attestation is **revocable** (it is not a short-lived ≤24h attestation, since approvals
typically persist for the duration of a commercial relationship).

#### 8.1 Revocation mechanism

* **Token Status List:** the issuer SHALL maintain an active IETF Token Status List ([Token Status
  List]), aligned with the Attestation Status List mechanism specified by the EU Commission and
  mandated by the WE BUILD ADR on Attestation Revocation.
* **Credential metadata:** the `status` metadata SHALL be populated in every issued attestation with:
  * `status_list_credential` (string, URI), the URI of the Status List Credential containing the
    status bitstring;
  * `status_list_index` (integer, ≥ 0), the zero-based index into the status list bitstring for this
    attestation;
  * `status_purpose` (string), SHALL be `revocation`.
* **Authorized authority:** only the issuing Buyer (the self-issuing legal entity) may modify the
  status list entry.

#### 8.2 Revocation triggers and business rules

* **Issuer trigger (obligation):** the Buyer SHALL revoke the attestation without undue delay when the
  underlying commercial relationship ends, when the approval scope no longer applies, or when the
  Supplier's identity data becomes inaccurate.
* **Relying Party action:** a revoked or suspended attestation SHALL be treated as invalid; C2 SHALL
  reject invoice submissions relying on it. The business interpretation of a revocation (e.g. grace
  handling for invoices already in flight) is determined by the Relying Party's internal policies.

## 9 Presentation

#### Base Verification Process
The Relying Party SHALL perform the base attestation verification process for EAAs as defined in the
Base Verification specification:
<https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-base/verifier-base-verification.md#42-relying-party-obligations>

This covers verification of attestation authenticity and issuer identity via the EBWOID chain
(4.2.2–4.2.4), validity periods (4.2.5), revocation status (4.2.6), wallet integrity via the WUA
(4.2.7), and holder key binding (4.2.8).

#### Validate attestation-specific integrity rules
In addition to the base verification, the Relying Party SHALL apply the integrity rules IR-AS-01 to
IR-AS-03 defined in Section 2.9. In particular (IR-AS-03), C2 SHALL match the attestation's
`approved_supplier.peppol_id` and `approving_party.peppol_id` against, respectively, the sender and
buyer participant identifiers of the invoice in flight, and SHALL reject the invoice submission on
mismatch.

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

Obligations specific to this attestation type, carried over from the previous version
of this Rulebook:

When receiving and processing an Approved Supplier attestation, the Relying Party (C2) SHALL perform
the following verification obligations.

### 9.2 Presentation modes

Remote presentation is in scope. Proximity presentation is in scope only where
chapter 5 records an mdoc encoding.

### 9.3 Transactional data

This Rulebook defines no transactional data.

## 10 Trust Framework

This chapter specifies how a Relying Party establishes trust in the issuer of an Approved Supplier
attestation. The corresponding verification procedures are steps 4.2.2–4.2.4 of the Base Verification
specification.

The Approved Supplier attestation is an **EAA self-issued by a legal entity** (the Buyer). Buyers are
not, and cannot practically be, individually registered on a Trusted List. Trust is therefore
established through a cryptographic chain anchored in the issuer's **EBWOID**, following the common
WE BUILD EAA trust model:

* The issuer's EBWOID SHALL be included in the header of every issued Approved Supplier attestation.
  During EBWOID issuance, the EBWOID provider verifies that the public key contained in the EBWOID is
  owned by the EBW owner.
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

**Trust anchor location**

The attribute or metadata carrying the trust anchor location contains at least the URL
at which a machine-readable version can be found or looked up.

## 11 References

| **Item Reference** | **Standard name/details** |
| --- | --- |
| [European Digital Identity Regulation] | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework |
| [HAIP] | OpenID4VC High Assurance Interoperability Profile, OpenID Foundation, draft-03 |
| [IANA-JWT-Claims] | IANA JSON Web Token Claims Registry. <https://www.iana.org/assignments/jwt/jwt.xhtml> |
| [RFC 2119] | Key words for use in RFCs to Indicate Requirement Levels, S. Bradner, March 1997 |
| [RFC 3339] | Date and Time on the Internet: Timestamps, G. Klyne et al., July 2002 |
| [SD-JWT VC] | SD-JWT-based Verifiable Credentials. <https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/> |
| [Token Status List] | Token Status List, IETF OAuth WG. <https://datatracker.ietf.org/doc/draft-ietf-oauth-status-list/> |
| [OpenID4VCI] | OpenID for Verifiable Credential Issuance, OpenID Foundation |
| [OpenID4VP] | OpenID for Verifiable Presentations, OpenID Foundation |
| [Topic 7] | ARF Annex 2, Topic 7, Attestation revocation and revocation checking |
| [Topic 10] | ARF Annex 2, Topic 10, Issuing a PID or attestation to a Wallet Unit |
| [Topic 12] | ARF Annex 2, Topic 12, Attestation Rulebooks |
| [Topic 20] | ARF Annex 2, Topic 20, Strong User authentication for electronic payments |
| [Peppol BIS Billing 3.0] | OpenPeppol Business Interoperability Specification, Billing 3.0 |
| [EN 16931] | European standard on the semantic data model of the core elements of an electronic invoice |
| [EWC RB001] | EWC LPID Rulebook |
| [EWC RB002] | EWC EUCC Rulebook |
| [WP4 Blueprint] | WE BUILD Deliverable D4.1 (trust infrastructure blueprint) |
| [WBCS] | WE BUILD Conformance Specifications, cs-01 (issuance) and cs-02 (presentation) |
| [WE BUILD ADR, Revocation] | WE BUILD Architecture Decision Record on Attestation Revocation |
| [rb-base, Base Verification] | WE BUILD Rulebook for common verification steps for all attestations. <https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-base/verifier-base-verification.md> |
| [rb-base, Handshake] | WE BUILD Rulebook for Mutual Identification & Consent Handshake. <https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-base/holder-authorization-handshake.md> |
| [rb-ebwoid] | WE BUILD EBWOID Rulebook. <https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-ebwoid/README.md> |
