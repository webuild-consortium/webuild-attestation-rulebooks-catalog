# Attestation Rulebook for attestations of type Authorized Service Provider

Category: non-qualified EAA

*This Rulebook is derived from the generic WE BUILD attestation rulebook template, version 1.0 with 11 chapters (itself derived from the
EUDI attestation rulebook template) and keeps the template's chapter structure. It specifies the
Authorized Service Provider attestation used in WE BUILD Use Case SC5 (eInvoicing), Scenario 2 (Service
Provider authorization) and Scenario 3 (SP authorization verifiable by a Tax Administration).*

* Author(s):
  * Rune Kjørlaug, Emning AS / OpenPeppol (SC5 co-lead)

| Version | Date       | Description                                                  |
| ------- | ---------- | ------------------------------------------------------------ |
| 0.1     | 2026-06-01 | Initial draft of the Authorized Service Provider attestation rulebook, derived from the WE BUILD Attestation Rulebook Template v1.1 and aligned with the SC5 eInvoicing scenario specification (Scenarios 2 and 3). |
| 0.6     | 2026-07-14 | Review draft for SC5 rulebook review meeting. Aligned with the WE BUILD attestation rulebooks catalog conventions: vct pattern `eu.we-build:<slug>:1`, legal category value `EAA`, EBWOID-anchored EAA trust model per rb-base, issuer and Relying Party obligations referencing the Base Verification rulebook, and Token Status List metadata. |
| 0.7     | 2026-07-15 | Added issue tracker and cleaned up author list layout        |
| 1.1     | 2026-10-02 | Restructured onto the generic WE BUILD attestation rulebook template (11 chapters). No normative content removed. |
| 1.2     | 2026-11-09 | Restored the version history dropped in the template migration. Added a W3C VCDM encoding (section 5.3, informative until the proposed vocabulary terms are published). Replaced the placeholders in section 5.1 with an informative issued SD-JWT and a Tax Administration presentation example. Allowed the elements of `authorization_scope` to be individually selectively disclosable. Aligned the `status` claim with the IETF Token Status List structure. Corrected example identifiers (EUID, Peppol ICD, Access Point seat ID) and replaced the real company name in the examples with a fictitious one. Fixed the schema artefact file names, stale section references, traceability vs. body (binding, device binding), dangling text in chapter 9, and missing references. |

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

This Rulebook defines the **Authorized Service Provider attestation**, an Electronic Attestation of
Attributes (EAA) used within WE BUILD Use Case SC5 (eInvoicing).

In plain language, the Authorized Service Provider attestation lets a **company** declare, in a
machine-verifiable way, that a named **Service Provider** (Access Point) is authorised to send and/or
receive invoices on the company's behalf. The attestation is issued by the company to its Service
Provider and is presented so that a counterpart Access Point, or, in Scenario 3, a **Tax
Administration**, can verify that the Access Point handling a given invoice is genuinely mandated by
the company it acts for. This closes a trust gap in the 4-corner model: it makes the company→provider
mandate explicit and verifiable rather than assumed from network registration alone.

* **Real-world fact expressed:** that a named company authorises a named Service Provider (Access
  Point) to act for it, for a defined set of operations (send / receive / tax reporting) and validity
  period.
* **Issuers:** the authorising company, a Supplier (**C1**) or a Buyer (**C4**), acting as a legal
  person through its European Business Wallet (EBW).
* **Holders:** the Service Provider / Access Point (**C2** or **C3**), holding the attestation in its
  wallet.
* **Relying parties:** the counterpart Access Point (**C3** or **C2**); and, in Scenario 3, a **Tax
  Administration** verifying the provider's mandate for tax-reporting purposes.
* **Use case / user journey:** SC5 Scenario 2 (Service Provider authorization), Scenario 3 (mandate
  verifiable by a Tax Administration), and Scenario 5 (Peppol enhancements).
* **Source material:** the SC5 eInvoicing scenario descriptions in the
  [SC5 repository](https://github.com/webuild-consortium/SC5/tree/main/Scenario) (`Description.md`,
  `Scenario2.md`, `Scenario3.md` and `Scenario5.md`). Actor terminology (C1–C4, EBW, EBWOID, Access
  Point) is kept aligned with those descriptions and with the Peppol Interoperability Framework.

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
(C1–C4, Access Point, SMP/SML, Peppol participant identifier, Peppol seat ID) and WE BUILD terminology
(EBW, EBWOID, WE BUILD LoTL, WE BUILD Trusted List) as defined in the SC5 scenario descriptions and the
WP4 Blueprint.

## 2 Compliance

### 2.1 Compliance statement

This Rulebook complies with the applicable requirements of Topic 12, Attestation
Rulebooks, in Annex 2 of the Architecture and Reference Framework, version 3.0.0. It
uses the terminology of Annex 1 of the ARF.

The Authorized Service Provider attestation is a **non-qualified EAA** in the sense of the
[European Digital Identity Regulation], implemented within the WE BUILD pilot trust framework rather
than the eIDAS production ecosystem (WP4 Blueprint D4.1 §1.2.1). Its normative format is SD-JWT VC
profiled by [HAIP]; a W3C VCDM encoding is additionally defined (section 5.3). It uses OpenID4VCI for
issuance and OpenID4VP for presentation per the WE BUILD Conformance Specifications (cs-01, cs-02),
and the IETF Token Status List for revocation per the WE BUILD ADR on Attestation Revocation. The
`vida:tax_report` scope and `tax_reporting_member_state` attribute are designed to align with the ViDA
Digital Reporting Requirements for Scenario 3; their precise mapping to a production digital-reporting
obligation is out of scope for this pilot version. Escalation to an eIDAS-qualified EAA (QEAA) is out
of scope for this version.

### 2.2 Regulatory basis

This attestation is not a qualified electronic attestation of attributes. The data
described in Annex V points b, c and e of Regulation (EU) 2024/1183 is addressed as
required by EW-DM-12-018 and as recommended by EW-DM-12-020 and EW-DM-12-022: issuer
identification through `iss` and the EBWOID-anchored certificate material (chapter 10), the
subject through `authorized_service_provider`, and the validity period through `iat`/`exp` together
with `authorization_valid_from`/`authorization_valid_until`. All recommendations are followed.

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
| EW-DM-12-010                               | ARB_07                   | yes     | 3, 5.3               | EUID, Peppol identifiers and ISO 3166-1 reused; VCDM reuses EBWV terms where they exist |
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
| EW-DM-12-032                               | ARB_28                   | yes     | 4.2, 7.1             | RECOMMENDED binding to the Service Provider's EBWOID through `cryptographically_bound_to` |
| EW-DM-12-034                               | ARB_30                   | yes     | 3.2, 3.3, 3.4        | Selective disclosure stated per claim                        |
| EW-DM-12-035                               | ARB_31                   | no      |                      | No Claim Selective Disclosure Metadata document is used      |
| EW-DM-12-038                               | ARB_34                   | yes     | 7.1                  | Device binding RECOMMENDED                                   |

## 3 Attestation attributes

Attributes are defined here in an encoding-independent manner (EW-DM-12-007). The
encoding of each attribute is given in chapter 5.

### 3.1 Introduction

The Authorized Service Provider attestation expresses a mandate: a company authorises a Service
Provider to act for it in eInvoicing. The design models two parties, the **authorizing company** (C1
or C4, also the technical issuer) and the **authorized service provider** (C2 or C3, the
holder/subject), together with the set of authorised operations and the validity period.

**Logical model (informative):**

```
AuthorizedServiceProviderAttestation
├── attestation_legal_category : "EAA"     (metadata, section 4.1)
├── authorizing_company        (the company, C1 or C4, also the issuer)
│   ├── legal_name
│   ├── legal_id               (EUID, from the company's EBWOID)
│   └── peppol_id              (Peppol participant identifier)
├── authorized_service_provider (the Access Point, C2 or C3, the holder/subject)
│   ├── legal_name
│   ├── legal_id               (EUID)
│   └── peppol_ap_id           (Peppol Access Point seat ID)
├── authorization_scope        (array of code list values, see 4.4)
├── authorization_valid_from   (date)
├── authorization_valid_until  (date; see also the exp metadata claim)
└── tax_reporting_member_state (conditional, see 3.4)
```

This model refines the flat claim list in the SC5 scenario description (issuer_id, issuer_name,
subject_id, subject_name, authorization_date, expiry_date, scope, company_peppol_id, sp_peppol_ap_id)
into two grouped party objects, while preserving the same information content. The authorising party
may be either the Supplier (C1, authorising its sending AP C2) or the Buyer (C4, authorising its
receiving AP C3); the model is symmetric.

**Applicable legal category.** Per the SC5 working assumptions, the Authorized Service Provider
attestation is implemented as a **non-qualified EAA**. Where SC5 material refers to a "WE BUILD QEAA",
this denotes a technically interoperable, ITB-tested attestation within the pilot trust framework, not
an eIDAS-qualified EAA. The applicable Topic 12 requirements for this category are mapped in section
2.3.

**Schema artefacts.**

| Format    | Identifier                                                   | Schema artefact                                       | Version | Location                                                     |
| --------- | ------------------------------------------------------------ | ----------------------------------------------------- | ------- | ------------------------------------------------------------ |
| SD-JWT VC | `eu.we-build:authorizedserviceprovider:1`                    | JSON Schema                                           | 1.0     | [`data-schemas/sd-jwt/service-provider-authorization-sd-jwt.json`](../../data-schemas/sd-jwt/service-provider-authorization-sd-jwt.json), sample [`service-provider-authorization-sd-jwt-sample.json`](../../data-schemas/sd-jwt/sample-data/service-provider-authorization-sd-jwt-sample.json) |
| W3C VCDM  | type `AuthorizedServiceProviderCredential`, context `https://w3id.org/ebwv/v0.1` | JSON-LD context (EBWV), terms proposed in section 5.3 | pending | To be published by the WP4 semantics group                   |

The schema artefact file names differ from the rulebook name because the catalog's sample-matching
workflow matches on the first five characters of the file name, which would otherwise collide with
`authorised-signatories`.

The schema artefacts referenced above are normative for encoding. Where this document and a
referenced artefact disagree, the artefact prevails for encoding questions and this document prevails
for semantics, presence and disclosure rules.

Selective disclosure applies to the SD-JWT VC encoding and is stated per attribute in the tables
below (EW-DM-12-034). The W3C VCDM encoding of section 5.3 has no selective disclosure; section 5.3
states how this is handled.

### 3.2 Mandatory attributes

| Data identifier                            | Semantic reference                                           | Definition                                                   | Data type              | Selectively disclosable                             | Example value                        |
| ------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------------------- | --------------------------------------------------- | ------------------------------------ |
| `authorizing_company.legal_name`           | N/A (SC5-defined)                                            | Registered legal name of the authorising company.            | string                 | MAY (with `authorizing_company`)                    | `Green Flowers B.V.`                 |
| `authorizing_company.legal_id`             | EUID (Directive (EU) 2017/1132, Implementing Regulation (EU) 2021/1042) | Unique legal-person identifier of the company, sourced from its EBWOID. | string                 | MAY (with `authorizing_company`)                    | `NLNHR.85374628`                     |
| `authorizing_company.peppol_id`            | Peppol Participant Identifier                                | Peppol participant identifier of the company, as `ICD:identifier` (the value part of the `iso6523-actorid-upis` scheme). | string                 | MAY (with `authorizing_company`)                    | `0106:85374628`                      |
| `authorized_service_provider.legal_name`   | N/A (SC5-defined)                                            | Registered legal name of the Service Provider (the holder).  | string                 | MAY (with `authorized_service_provider`)            | `Brabant Access Services N.V.`       |
| `authorized_service_provider.legal_id`     | EUID (Directive (EU) 2017/1132, Implementing Regulation (EU) 2021/1042) | Unique legal-person identifier of the Service Provider.      | string                 | MAY (with `authorized_service_provider`)            | `BEKBOBCE.0890123456`                |
| `authorized_service_provider.peppol_ap_id` | Peppol seat ID (CN of the Peppol AP certificate)             | Identifier of the Service Provider's Peppol Access Point.    | string                 | MAY (with `authorized_service_provider`)            | `PBE000123`                          |
| `authorization_scope`                      | N/A (code list, section 4.4)                                 | One or more authorised operations.                           | array of string (enum) | Elements MAY be individually disclosable, see below | `["peppol:send", "vida:tax_report"]` |
| `authorization_valid_from`                 | N/A                                                          | Date from which the authorization is valid.                  | full-date (RFC 3339)   | MAY                                                 | `2026-01-01`                         |

The party objects `authorizing_company` and `authorized_service_provider` are disclosed as a whole;
their sub-claims are not individually selectively disclosable.

An issuer MAY make each element of `authorization_scope` individually selectively disclosable. This
lets the Service Provider disclose only the operation relevant to a given Relying Party, for example
`peppol:send` to a counterpart Access Point and `vida:tax_report` to a Tax Administration, without
revealing its other mandates. The array itself is always present.

### 3.3 Optional attributes

| Data identifier             | Semantic reference | Definition                                                   | Data type            | Selectively disclosable                                      | Example value     |
| --------------------------- | ------------------ | ------------------------------------------------------------ | -------------------- | ------------------------------------------------------------ | ----------------- |
| `authorization_valid_until` | N/A                | Date until which the authorization is valid (business validity, distinct from the technical `exp` metadata claim). | full-date (RFC 3339) | MAY                                                          | `2026-12-31`      |
| `authorization_reference`   | N/A                | Company-internal reference for the service agreement underlying the mandate. | string               | MUST, so that the provider can withhold the internal reference | `SLA-2026-AP-007` |

### 3.4 Conditional attributes

| Data identifier              | Semantic reference | Definition                                                   | Condition                                                    | Data type | Selectively disclosable | Example value |
| ---------------------------- | ------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | --------- | ----------------------- | ------------- |
| `tax_reporting_member_state` | ISO 3166-1 alpha-2 | Member State for which the provider is authorised to perform tax reporting. | SHALL be present if and only if `authorization_scope` contains `vida:tax_report` (IR-ASP-02). | string    | MAY                     | `NL`          |

## 4 Metadata

Metadata describes the attestation rather than its subject. Metadata claims are not selectively
disclosable.

### 4.1 Mandatory metadata

| Data identifier              | Semantic reference               | Definition                                                   | Data type    | Example value                                      |
| ---------------------------- | -------------------------------- | ------------------------------------------------------------ | ------------ | -------------------------------------------------- |
| `attestation_legal_category` | EW-DM-12-015 / EW-DM-12-029      | Indicates the legal category of the attestation.             | string       | `EAA`                                              |
| `vct`                        | [SD-JWT VC]                      | Verifiable Credential Type identifier (see section 5.1).     | string       | `eu.we-build:authorizedserviceprovider:1`          |
| `iss`                        | [IANA-JWT-Claims]                | Issuer identifier (the authorising company's issuing system / EBW). | string (URI) | `https://wallet.greenflowers.example/issuer`       |
| `iat`                        | [IANA-JWT-Claims]                | Issuance timestamp.                                          | NumericDate  | `1767225600`                                       |
| `exp`                        | [IANA-JWT-Claims]                | Technical expiry timestamp of the attestation.               | NumericDate  | `1798761600`                                       |
| `status`                     | [SD-JWT VC], [Token Status List] | Reference to the Token Status List entry for revocation, as `status.status_list` with `idx` and `uri` (see chapter 8). | object       | `{"status_list": {"idx": 87, "uri": "https://…"}}` |
| `cnf`                        | [SD-JWT VC]                      | Holder key-binding confirmation (proof of possession by the Service Provider's wallet). | object       | *(JWK)*                                            |

**Legal category.** This Rulebook retains the `attestation_legal_category` attribute.
Section 4.1 of the generic template replaces it with the `category` attribute of
[ETSI TS 119 472-1], whose value for this category is `eaa:eu:non-qualified`.
EW-DM-12-029, legacy ARB_25, of ARF version 3.0.0 is a SHALL that still requires
`attestation_legal_category`, so the template and the ARF disagree. The attribute is
left as written and the deviation is recorded for the rulebook quality assurance group.

### 4.2 Optional metadata

| Data identifier              | Semantic reference | Definition                                                   | Data type    | Example value                         |
| ---------------------------- | ------------------ | ------------------------------------------------------------ | ------------ | ------------------------------------- |
| `cryptographically_bound_to` | EW-DM-12-032       | vct of the attestation on the same Wallet Unit to which this attestation is cryptographically bound (the Service Provider's EBWOID). RECOMMENDED, see section 7.1. | string       | `uri:eu.ebw.oid.1`                    |
| `nbf`                        | [IANA-JWT-Claims]  | Time before which the attestation SHALL NOT be accepted.     | NumericDate  | `1767225600`                          |
| `sub`                        | [IANA-JWT-Claims]  | Identifier of the subject (the authorised Service Provider). | string       | `did:example:brabant-access-services` |
| `schema_version`             | N/A                | Version of the schema artefact used.                         | string       | `1.0`                                 |
| `trust_anchor_url`           | EW-DM-12-024       | URL at which a machine-readable version of the trust anchor can be found or looked up. For this attestation the trust anchor is the EBWOID provider's entry in the WE BUILD trust list infrastructure (chapter 10). | string (URI) | *(WE BUILD TLOL entry)*               |

### 4.3 Conditional metadata

The Authorized Service Provider attestation defined in this Rulebook does not contain any
conditional metadata.

### 4.4 Code lists

| Field                 | Allowed values or vocabulary | Meaning                                                      | Source                                                       | Extensible     |
| --------------------- | ---------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | -------------- |
| `authorization_scope` | `peppol:send`                | The provider is authorised to send (transmit) invoices as the company's sending Access Point (C2). Used by C1 authorising C2. | WE BUILD SC5 vocabulary                                      | Yes, see below |
| `authorization_scope` | `peppol:receive`             | The provider is authorised to receive invoices as the company's receiving Access Point (C3). Used by C4 authorising C3. | WE BUILD SC5 vocabulary                                      | Yes, see below |
| `authorization_scope` | `vida:tax_report`            | The provider is authorised to perform tax reporting / digital reporting on the company's behalf (Scenario 3). Requires `tax_reporting_member_state` (section 3.4). | WE BUILD SC5 vocabulary; aligned with the ViDA Digital Reporting Requirements | Yes, see below |

Additional values SHOULD only be introduced if defined consistently across issuers and verifiers and
registered in the WE BUILD Attestation Rulebooks catalog.

### 4.5 Integrity rules

| Rule ID     | Rule statement                                               | Why it exists                                                | Where enforced                                               | Behaviour on failure                                         |
| ----------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `IR-ASP-01` | `authorization_valid_from` SHALL NOT be later than `authorization_valid_until` (when present), and both SHALL fall within the `iat`–`exp` window. | Prevents inconsistent or unusable validity periods.          | Issuer business rules; verifier business validation.         | Issuer SHALL reject; verifier SHALL treat the attestation as invalid. |
| `IR-ASP-02` | If `authorization_scope` contains `vida:tax_report`, then `tax_reporting_member_state` SHALL be present; otherwise it SHALL be absent. Where scope elements are individually disclosable, a holder that discloses `tax_reporting_member_state` SHALL also disclose the `vida:tax_report` element, and a verifier evaluates the rule against the disclosed elements. | Ensures tax-reporting mandates carry the jurisdiction needed by a Tax Administration relying party (Scenario 3), and that the field is not set spuriously. | Issuer; holder; verifier (Tax Administration) business validation. | Verifier SHALL treat the attestation as invalid for tax-reporting reliance. |
| `IR-ASP-03` | `authorization_scope` SHALL contain at least one value, and SHALL NOT contain both `peppol:send` and `peppol:receive` unless the same provider genuinely acts as both C2 and C3 for the company. | Keeps the mandate explicit and prevents over-broad authorizations. | Issuer business rules.                                       | Issuer SHALL reject an empty or contradictory scope.         |
| `IR-ASP-04` | At verification time, the `authorized_service_provider.peppol_ap_id` SHALL match the Access Point actually transmitting/receiving the invoice, and `authorizing_company.peppol_id` SHALL match the corresponding party on the invoice. | Binds the mandate to the specific invoice flow, preventing reuse for an unrelated company/provider pair. | Verifier (counterpart AP, or Tax Administration).            | Verifier SHALL reject.                                       |

## 5 Formats

| Format               | Supported         | Identifier                                                   | Specification                   | Notes                                                        |
| -------------------- | ----------------- | ------------------------------------------------------------ | ------------------------------- | ------------------------------------------------------------ |
| ISO/IEC 18013-5 mdoc | no                |                                                              | [ISO/IEC 18013-5]               | Proximity presentation is not in scope (EW-DM-12-003)        |
| SD-JWT VC            | yes               | `vct` `eu.we-build:authorizedserviceprovider:1`              | [SD-JWT VC], [HAIP]             | Normative format; SHALL follow the HAIP profile (EW-DM-12-002) |
| W3C VCDM             | yes (informative) | type `AuthorizedServiceProviderCredential`, context `https://w3id.org/ebwv/v0.1` | [W3C VCDM v2.0], [VC-JOSE-COSE] | Permitted for non-qualified EAA (EW-DM-12-001); see section 5.3 |

A Provider SHALL offer the SD-JWT VC format. A Provider MAY additionally offer the W3C VCDM format
once section 5.3 is normative. A Relying Party in the SC5 flows SHALL accept SD-JWT VC and is not
required to accept W3C VCDM.

### 5.1 SD-JWT VC-based encoding

This attestation type SHALL be issued in the [SD-JWT VC]-compliant format and SHALL comply with the
'SD-JWT VCs' profile specified in [HAIP] (EW-DM-12-002).

**Verifiable Credential Type (`vct`):** `eu.we-build:authorizedserviceprovider:1`

*(Proposed value; subject to registration in the WE BUILD Attestation Rulebooks catalog by the WP4
semantics group, EW-DM-12-006.)*

A Type Metadata Document SHOULD be defined for this vct per [SD-JWT VC]. Selective disclosure per
claim is stated in sections 3.2 to 3.4; all metadata claims of chapter 4 are not selectively
disclosable. The JWT header SHALL carry the issuer's EBWOID-anchored certificate material (`x5c`) as
described in chapter 10.

**Claim encoding:**

| Data identifier                   | Attribute identifier        | Encoding format                                              | Reference / notes              |
| --------------------------------- | --------------------------- | ------------------------------------------------------------ | ------------------------------ |
| `iss`, `iat`, `exp`, `nbf`, `sub` | as named                    | per [IANA-JWT-Claims]                                        | Section 4.1, 4.2               |
| `vct`                             | vct                         | string                                                       | [SD-JWT VC]                    |
| `status`                          | status                      | object, `status_list.idx` (integer) and `status_list.uri` (string) | [Token Status List]; chapter 8 |
| `cnf`                             | cnf                         | object, `jwk`                                                | [SD-JWT VC]; holder binding    |
| `attestation_legal_category`      | attestation_legal_category  | string                                                       | Section 4.1                    |
| `authorizing_company`             | authorizing_company         | object                                                       | Section 3.2                    |
| `authorized_service_provider`     | authorized_service_provider | object                                                       | Section 3.2                    |
| `authorization_scope`             | authorization_scope         | array of string; elements MAY be array-element disclosures   | Code list 4.4                  |
| `authorization_valid_from`        | authorization_valid_from    | string (full-date)                                           | Section 3.2                    |
| `authorization_valid_until`       | authorization_valid_until   | string (full-date)                                           | Section 3.3                    |
| `tax_reporting_member_state`      | tax_reporting_member_state  | string                                                       | Section 3.4                    |
| `authorization_reference`         | authorization_reference     | string                                                       | Section 3.3                    |
| `cryptographically_bound_to`      | cryptographically_bound_to  | string                                                       | Section 4.2; section 7.1       |

**Logical claim set (informative, synthetic data, all disclosures applied):**

```json
{
  "vct": "eu.we-build:authorizedserviceprovider:1",
  "iss": "https://wallet.greenflowers.example/issuer",
  "iat": 1767225600,
  "exp": 1798761600,
  "attestation_legal_category": "EAA",
  "cryptographically_bound_to": "uri:eu.ebw.oid.1",
  "status": {
    "status_list": {
      "idx": 87,
      "uri": "https://wallet.greenflowers.example/status/authorizedserviceprovider"
    }
  },
  "cnf": {
    "jwk": {
      "kty": "EC",
      "crv": "P-256",
      "x": "lS2bfVx5fDYiuCcGw2VxHN6hwMhMf9GBbulM8cDoQ3Y",
      "y": "tCaJoPMr-bAkz-yo_S_3wFoy8gcw5uz2Y58Cf4-VqlM"
    }
  },
  "authorizing_company": {
    "legal_name": "Green Flowers B.V.",
    "legal_id": "NLNHR.85374628",
    "peppol_id": "0106:85374628"
  },
  "authorized_service_provider": {
    "legal_name": "Brabant Access Services N.V.",
    "legal_id": "BEKBOBCE.0890123456",
    "peppol_ap_id": "PBE000123"
  },
  "authorization_scope": [
    "peppol:send",
    "vida:tax_report"
  ],
  "authorization_valid_from": "2026-01-01",
  "authorization_valid_until": "2026-12-31",
  "tax_reporting_member_state": "NL",
  "authorization_reference": "SLA-2026-AP-007"
}
```

#### 5.1.1 Issued SD-JWT (informative)

The example below is a complete issued SD-JWT, signed with a throw-away ES256 test key. All
organisations, identifiers and keys are fictitious. Every attribute of chapter 3 is selectively
disclosable in this example: `authorization_reference` because it MUST be, the others to show how the
Service Provider controls disclosure. Each element of `authorization_scope` is an array-element
disclosure (section 3.2). A Provider MAY make fewer claims disclosable, as permitted in sections 3.2 to
3.4. For readability the header carries a `kid`; a production attestation SHALL carry the
EBWOID-anchored certificate material in `x5c` instead (chapter 10). The example SHALL be regenerated
if the selective-disclosure structure changes.

Issued SD-JWT (issuer-signed JWT `~` disclosures `~`):

```
eyJhbGciOiJFUzI1NiIsInR5cCI6ImRjK3NkLWp3dCIsImtpZCI6ImdyZWVuZmxvd2Vycy1lYnctaXNzdWVyLXRlc3QifQ.eyJ2Y3QiOiJldS53ZS1idWlsZDphdXRob3JpemVkc2VydmljZXByb3ZpZGVyOjEiLCJpc3MiOiJodHRwczovL3dhbGxldC5ncmVlbmZsb3dlcnMuZXhhbXBsZS9pc3N1ZXIiLCJpYXQiOjE3NjcyMjU2MDAsImV4cCI6MTc5ODc2MTYwMCwiYXR0ZXN0YXRpb25fbGVnYWxfY2F0ZWdvcnkiOiJFQUEiLCJjcnlwdG9ncmFwaGljYWxseV9ib3VuZF90byI6InVyaTpldS5lYncub2lkLjEiLCJzdGF0dXMiOnsic3RhdHVzX2xpc3QiOnsiaWR4Ijo4NywidXJpIjoiaHR0cHM6Ly93YWxsZXQuZ3JlZW5mbG93ZXJzLmV4YW1wbGUvc3RhdHVzL2F1dGhvcml6ZWRzZXJ2aWNlcHJvdmlkZXIifX0sImNuZiI6eyJqd2siOnsia3R5IjoiRUMiLCJjcnYiOiJQLTI1NiIsIngiOiJsUzJiZlZ4NWZEWWl1Q2NHdzJWeEhONmh3TWhNZjlHQmJ1bE04Y0RvUTNZIiwieSI6InRDYUpvUE1yLWJBa3oteW9fU18zd0ZveThnY3c1dXoyWTU4Q2Y0LVZxbE0ifX0sImF1dGhvcml6YXRpb25fc2NvcGUiOlt7Ii4uLiI6InFKU0RnZVBWQVRjVFg5LW5LRTNyVVB0b2Rsa3M4M3BsT3p2d08xVnlKa2cifSx7Ii4uLiI6InNvQUNxSWloX3g0SXJGZ0Z2QURZXzhQbENkdWcwdkhoNXN4Zk5RZzk0R0kifV0sIl9zZCI6WyJGR0drTkVXbmZDVFE1eS11X2NpOXBWNER3MkVOOWxqdkowcmptTUJnOEFFIiwiSEdrX1hqZTZnVWRxdmNYbjVVdlNzTmZlVmNiLWs1Wm8zV01EaWRXa19pZyIsIk5MUGxfMUd0SzdfbGg5YldkUnV6SmdMQzdtWWUtU09yX2M2VmwzaGJxMW8iLCJnQUpQOXZuTzFxNFF0a2dmY3NrSm5adXNvQ3ZpY0M1aVJwcWhEb01feDQwIiwic3hMTEJrNkdpeVBCVlRkOTVBUHhfYS1rZW1UaE9YdG05c2RDU3BURFdGWSIsIncxenNka2IwQUZNdG9pRmxlYVBaWWllVEtvVkRHZUFiOEdRMWtDcndldkUiXSwiX3NkX2FsZyI6InNoYS0yNTYifQ.haYZrvuzkVZenacr5zrSZUAa-qqJpLaXSFivIn-3BWJdLZ85DHDosv0zSJOCtcxjlCPic72uzNQ6qdbCDIS6vQ~WyJZOFBwMkx3VXdDQ1NDeFYyaXNTWGxRIiwiYXV0aG9yaXppbmdfY29tcGFueSIseyJsZWdhbF9uYW1lIjoiR3JlZW4gRmxvd2VycyBCLlYuIiwibGVnYWxfaWQiOiJOTE5IUi44NTM3NDYyOCIsInBlcHBvbF9pZCI6IjAxMDY6ODUzNzQ2MjgifV0~WyI3bDZwVG1SXzE4QUJacnBEa29GT2JRIiwiYXV0aG9yaXplZF9zZXJ2aWNlX3Byb3ZpZGVyIix7ImxlZ2FsX25hbWUiOiJCcmFiYW50IEFjY2VzcyBTZXJ2aWNlcyBOLlYuIiwibGVnYWxfaWQiOiJCRUtCT0JDRS4wODkwMTIzNDU2IiwicGVwcG9sX2FwX2lkIjoiUEJFMDAwMTIzIn1d~WyJKemRpYVU4OFAyNGNPZUU4bzhhc3lRIiwiYXV0aG9yaXphdGlvbl92YWxpZF9mcm9tIiwiMjAyNi0wMS0wMSJd~WyJwVlZ4bDFVbS14UDZPRFpCVHBLWDRRIiwiYXV0aG9yaXphdGlvbl92YWxpZF91bnRpbCIsIjIwMjYtMTItMzEiXQ~WyJMMU5BU2xCbkxQeGpIWHc5THhyR1ZRIiwidGF4X3JlcG9ydGluZ19tZW1iZXJfc3RhdGUiLCJOTCJd~WyJSb1VvcHZFVzg2M0h0S0lxMHZhT2J3IiwiYXV0aG9yaXphdGlvbl9yZWZlcmVuY2UiLCJTTEEtMjAyNi1BUC0wMDciXQ~WyJPUXA4R3JZOE1MdlBEaWNqWVBLVXR3IiwicGVwcG9sOnNlbmQiXQ~WyJJZkJsd21EZHNNQTd2dmNMNFZyX2xnIiwidmlkYTp0YXhfcmVwb3J0Il0~
```

#### 5.1.2 Human-readable payload and disclosures (informative)

Header:

```json
{
  "alg": "ES256",
  "typ": "dc+sd-jwt",
  "kid": "greenflowers-ebw-issuer-test"
}
```

Issuer-signed payload:

```json
{
  "vct": "eu.we-build:authorizedserviceprovider:1",
  "iss": "https://wallet.greenflowers.example/issuer",
  "iat": 1767225600,
  "exp": 1798761600,
  "attestation_legal_category": "EAA",
  "cryptographically_bound_to": "uri:eu.ebw.oid.1",
  "status": {
    "status_list": {
      "idx": 87,
      "uri": "https://wallet.greenflowers.example/status/authorizedserviceprovider"
    }
  },
  "cnf": {
    "jwk": {
      "kty": "EC",
      "crv": "P-256",
      "x": "lS2bfVx5fDYiuCcGw2VxHN6hwMhMf9GBbulM8cDoQ3Y",
      "y": "tCaJoPMr-bAkz-yo_S_3wFoy8gcw5uz2Y58Cf4-VqlM"
    }
  },
  "authorization_scope": [
    {
      "...": "qJSDgePVATcTX9-nKE3rUPtodlks83plOzvwO1VyJkg"
    },
    {
      "...": "soACqIih_x4IrFgFvADY_8PlCdug0vHh5sxfNQg94GI"
    }
  ],
  "_sd": [
    "FGGkNEWnfCTQ5y-u_ci9pV4Dw2EN9ljvJ0rjmMBg8AE",
    "HGk_Xje6gUdqvcXn5UvSsNfeVcb-k5Zo3WMDidWk_ig",
    "NLPl_1GtK7_lh9bWdRuzJgLC7mYe-SOr_c6Vl3hbq1o",
    "gAJP9vnO1q4QtkgfcskJnZusoCvicC5iRpqhDoM_x40",
    "sxLLBk6GiyPBVTd95APx_a-kemThOXtm9sdCSpTDWFY",
    "w1zsdkb0AFMtoiFleaPZYieTKoVDGeAb8GQ1kCrwevE"
  ],
  "_sd_alg": "sha-256"
}
```

Disclosures and the digest each produces. Object-property disclosures are
`[salt, claim name, claim value]` and their digests appear in `_sd`; array-element disclosures are
`[salt, value]` and their digests appear as `{"...": digest}` entries in `authorization_scope`.

| Claim                           | Disclosure (decoded)                                         | Digest (SHA-256, base64url)                   |
| ------------------------------- | ------------------------------------------------------------ | --------------------------------------------- |
| `authorizing_company`           | `["Y8Pp2LwUwCCSCxV2isSXlQ", "authorizing_company", {"legal_name": "Green Flowers B.V.", "legal_id": "NLNHR.85374628", "peppol_id": "0106:85374628"}]` | `HGk_Xje6gUdqvcXn5UvSsNfeVcb-k5Zo3WMDidWk_ig` |
| `authorized_service_provider`   | `["7l6pTmR_18ABZrpDkoFObQ", "authorized_service_provider", {"legal_name": "Brabant Access Services N.V.", "legal_id": "BEKBOBCE.0890123456", "peppol_ap_id": "PBE000123"}]` | `FGGkNEWnfCTQ5y-u_ci9pV4Dw2EN9ljvJ0rjmMBg8AE` |
| `authorization_valid_from`      | `["JzdiaU88P24cOeE8o8asyQ", "authorization_valid_from", "2026-01-01"]` | `sxLLBk6GiyPBVTd95APx_a-kemThOXtm9sdCSpTDWFY` |
| `authorization_valid_until`     | `["pVVxl1Um-xP6ODZBTpKX4Q", "authorization_valid_until", "2026-12-31"]` | `gAJP9vnO1q4QtkgfcskJnZusoCvicC5iRpqhDoM_x40` |
| `tax_reporting_member_state`    | `["L1NASlBnLPxjHXw9LxrGVQ", "tax_reporting_member_state", "NL"]` | `w1zsdkb0AFMtoiFleaPZYieTKoVDGeAb8GQ1kCrwevE` |
| `authorization_reference`       | `["RoUopvEW863HtKIq0vaObw", "authorization_reference", "SLA-2026-AP-007"]` | `NLPl_1GtK7_lh9bWdRuzJgLC7mYe-SOr_c6Vl3hbq1o` |
| `authorization_scope[] element` | `["OQp8GrY8MLvPDicjYPKUtw", "peppol:send"]`                  | `qJSDgePVATcTX9-nKE3rUPtodlks83plOzvwO1VyJkg` |
| `authorization_scope[] element` | `["IfBlwmDdsMA7vvcL4Vr_lg", "vida:tax_report"]`              | `soACqIih_x4IrFgFvADY_8PlCdug0vHh5sxfNQg94GI` |

#### 5.1.3 Presentation to a Tax Administration (informative)

In Scenario 3 the Service Provider presents the attestation to a Tax Administration. It discloses the
two party objects, the validity, the `vida:tax_report` scope element and `tax_reporting_member_state`.
It withholds the `peppol:send` element and `authorization_reference`, and appends a Key Binding JWT
signed with the key in `cnf`, binding the presentation to the Tax Administration (`aud`), to the
request (`nonce`) and to the exact set of disclosures (`sd_hash`):

```json
{
  "iat": 1768392000,
  "aud": "https://reporting.tax-authority.example",
  "nonce": "t-9Kd2Xq4LmP",
  "sd_hash": "3voURYu629hBoyXjdUwqUmVg1SuYeL8eN0NJAgZ1l5U"
}
```

Presented SD-JWT+KB:

```
eyJhbGciOiJFUzI1NiIsInR5cCI6ImRjK3NkLWp3dCIsImtpZCI6ImdyZWVuZmxvd2Vycy1lYnctaXNzdWVyLXRlc3QifQ.eyJ2Y3QiOiJldS53ZS1idWlsZDphdXRob3JpemVkc2VydmljZXByb3ZpZGVyOjEiLCJpc3MiOiJodHRwczovL3dhbGxldC5ncmVlbmZsb3dlcnMuZXhhbXBsZS9pc3N1ZXIiLCJpYXQiOjE3NjcyMjU2MDAsImV4cCI6MTc5ODc2MTYwMCwiYXR0ZXN0YXRpb25fbGVnYWxfY2F0ZWdvcnkiOiJFQUEiLCJjcnlwdG9ncmFwaGljYWxseV9ib3VuZF90byI6InVyaTpldS5lYncub2lkLjEiLCJzdGF0dXMiOnsic3RhdHVzX2xpc3QiOnsiaWR4Ijo4NywidXJpIjoiaHR0cHM6Ly93YWxsZXQuZ3JlZW5mbG93ZXJzLmV4YW1wbGUvc3RhdHVzL2F1dGhvcml6ZWRzZXJ2aWNlcHJvdmlkZXIifX0sImNuZiI6eyJqd2siOnsia3R5IjoiRUMiLCJjcnYiOiJQLTI1NiIsIngiOiJsUzJiZlZ4NWZEWWl1Q2NHdzJWeEhONmh3TWhNZjlHQmJ1bE04Y0RvUTNZIiwieSI6InRDYUpvUE1yLWJBa3oteW9fU18zd0ZveThnY3c1dXoyWTU4Q2Y0LVZxbE0ifX0sImF1dGhvcml6YXRpb25fc2NvcGUiOlt7Ii4uLiI6InFKU0RnZVBWQVRjVFg5LW5LRTNyVVB0b2Rsa3M4M3BsT3p2d08xVnlKa2cifSx7Ii4uLiI6InNvQUNxSWloX3g0SXJGZ0Z2QURZXzhQbENkdWcwdkhoNXN4Zk5RZzk0R0kifV0sIl9zZCI6WyJGR0drTkVXbmZDVFE1eS11X2NpOXBWNER3MkVOOWxqdkowcmptTUJnOEFFIiwiSEdrX1hqZTZnVWRxdmNYbjVVdlNzTmZlVmNiLWs1Wm8zV01EaWRXa19pZyIsIk5MUGxfMUd0SzdfbGg5YldkUnV6SmdMQzdtWWUtU09yX2M2VmwzaGJxMW8iLCJnQUpQOXZuTzFxNFF0a2dmY3NrSm5adXNvQ3ZpY0M1aVJwcWhEb01feDQwIiwic3hMTEJrNkdpeVBCVlRkOTVBUHhfYS1rZW1UaE9YdG05c2RDU3BURFdGWSIsIncxenNka2IwQUZNdG9pRmxlYVBaWWllVEtvVkRHZUFiOEdRMWtDcndldkUiXSwiX3NkX2FsZyI6InNoYS0yNTYifQ.haYZrvuzkVZenacr5zrSZUAa-qqJpLaXSFivIn-3BWJdLZ85DHDosv0zSJOCtcxjlCPic72uzNQ6qdbCDIS6vQ~WyJZOFBwMkx3VXdDQ1NDeFYyaXNTWGxRIiwiYXV0aG9yaXppbmdfY29tcGFueSIseyJsZWdhbF9uYW1lIjoiR3JlZW4gRmxvd2VycyBCLlYuIiwibGVnYWxfaWQiOiJOTE5IUi44NTM3NDYyOCIsInBlcHBvbF9pZCI6IjAxMDY6ODUzNzQ2MjgifV0~WyI3bDZwVG1SXzE4QUJacnBEa29GT2JRIiwiYXV0aG9yaXplZF9zZXJ2aWNlX3Byb3ZpZGVyIix7ImxlZ2FsX25hbWUiOiJCcmFiYW50IEFjY2VzcyBTZXJ2aWNlcyBOLlYuIiwibGVnYWxfaWQiOiJCRUtCT0JDRS4wODkwMTIzNDU2IiwicGVwcG9sX2FwX2lkIjoiUEJFMDAwMTIzIn1d~WyJKemRpYVU4OFAyNGNPZUU4bzhhc3lRIiwiYXV0aG9yaXphdGlvbl92YWxpZF9mcm9tIiwiMjAyNi0wMS0wMSJd~WyJwVlZ4bDFVbS14UDZPRFpCVHBLWDRRIiwiYXV0aG9yaXphdGlvbl92YWxpZF91bnRpbCIsIjIwMjYtMTItMzEiXQ~WyJMMU5BU2xCbkxQeGpIWHc5THhyR1ZRIiwidGF4X3JlcG9ydGluZ19tZW1iZXJfc3RhdGUiLCJOTCJd~WyJJZkJsd21EZHNNQTd2dmNMNFZyX2xnIiwidmlkYTp0YXhfcmVwb3J0Il0~eyJhbGciOiJFUzI1NiIsInR5cCI6ImtiK2p3dCJ9.eyJpYXQiOjE3NjgzOTIwMDAsImF1ZCI6Imh0dHBzOi8vcmVwb3J0aW5nLnRheC1hdXRob3JpdHkuZXhhbXBsZSIsIm5vbmNlIjoidC05S2QyWHE0TG1QIiwic2RfaGFzaCI6IjN2b1VSWXU2MjloQm95WGpkVXdxVW1WZzFTdVllTDhlTjBOSkFnWjFsNVUifQ.n_WN_xCUIhWHA9bHtQztgnzpXaLPTbFtUHo12js0QoSYRRFOcHAb4EWdpNfyaJxBzg_O69RbqzAKYsTaMG078Q
```

After processing the disclosures, the Tax Administration sees:

```json
{
  "vct": "eu.we-build:authorizedserviceprovider:1",
  "iss": "https://wallet.greenflowers.example/issuer",
  "iat": 1767225600,
  "exp": 1798761600,
  "attestation_legal_category": "EAA",
  "cryptographically_bound_to": "uri:eu.ebw.oid.1",
  "status": {
    "status_list": {
      "idx": 87,
      "uri": "https://wallet.greenflowers.example/status/authorizedserviceprovider"
    }
  },
  "cnf": {
    "jwk": {
      "kty": "EC",
      "crv": "P-256",
      "x": "lS2bfVx5fDYiuCcGw2VxHN6hwMhMf9GBbulM8cDoQ3Y",
      "y": "tCaJoPMr-bAkz-yo_S_3wFoy8gcw5uz2Y58Cf4-VqlM"
    }
  },
  "authorizing_company": {
    "legal_name": "Green Flowers B.V.",
    "legal_id": "NLNHR.85374628",
    "peppol_id": "0106:85374628"
  },
  "authorized_service_provider": {
    "legal_name": "Brabant Access Services N.V.",
    "legal_id": "BEKBOBCE.0890123456",
    "peppol_ap_id": "PBE000123"
  },
  "authorization_scope": [
    "vida:tax_report"
  ],
  "authorization_valid_from": "2026-01-01",
  "authorization_valid_until": "2026-12-31",
  "tax_reporting_member_state": "NL"
}
```

A presentation to a counterpart Access Point would instead disclose the `peppol:send` element and
withhold `vida:tax_report` and `tax_reporting_member_state`.

### 5.2 ISO/IEC 18013-5-compliant encoding

The Authorized Service Provider attestation is presented in automated, online, system-to-system flows
(see chapter 9). There is no proximity or offline presentation use case (EW-DM-12-003). An ISO/IEC
18013-5 (mdoc) encoding is therefore **not specified** in this version.

### 5.3 W3C Verifiable Credentials Data Model-based encoding

**Status.** This encoding is **informative** until the vocabulary terms proposed below are published
in the European Business Wallet Vocabulary (EBWV) context by the WP4 semantics group. A Provider SHALL
NOT issue this encoding before then. SD-JWT VC (section 5.1) remains the normative format for SC5.

The Authorized Service Provider attestation is a non-qualified EAA, the only legal category permitted
to use the W3C VCDM format (EW-DM-12-001). The encoding uses [W3C VCDM v2.0] with the EBWV context, in
line with the other catalog rulebooks that define a VCDM encoding and with the Approved Supplier
rulebook.

**Modelling.** In VCDM the credential subject is the party the claims are about. The
`credentialSubject` is therefore the Service Provider, and the company's mandate is expressed as
properties of it (`authorizedBy`, `authorizationScope`, `authorizationValidFrom`,
`authorizationValidUntil`, `taxReportingMemberState`). This carries the same information as the SD-JWT
VC claim set; section 5.3.1 gives the mapping.

**Securing mechanism.** The credential SHALL be secured as a JWT according to [VC-JOSE-COSE]. The JOSE
header SHALL carry the issuer's EBWOID-anchored certificate material in `x5c`, so the trust model of
chapter 10 applies unchanged. Data Integrity proofs are not used in this version, because the EBWOID
trust model anchors the issuer key in X.509 certificate material rather than in a verification method
resolved from the `issuer` identifier.

**Selective disclosure.** This encoding provides no selective disclosure. Consequently:

* `authorization_reference`, which MUST be selectively disclosable (section 3.3), SHALL NOT be
  included;
* every scope in `authorizationScope` is always visible to every Relying Party. An issuer that does not
  want a counterpart Access Point to learn of a tax-reporting mandate SHOULD issue separate W3C VCDM
  credentials per scope, or use the SD-JWT VC encoding.

**Holder binding.** `credentialSubject.id` SHALL be a `did:jwk` derived from the holder's public key,
which takes the role of `cnf` in the SD-JWT VC encoding. The Service Provider proves possession of the
corresponding private key when presenting.

**Revocation.** `credentialStatus` SHALL use a `BitstringStatusListEntry` according to [W3C Bitstring
Status List], with `statusPurpose` `revocation`. *Open point:* the WE BUILD ADR on Attestation
Revocation mandates the IETF Token Status List; confirmation is needed that the W3C Bitstring Status
List is acceptable for the VCDM encoding, or that the Token Status List shall be used for both.

**Proposed vocabulary terms.** The following terms do not exist in EBWV and are proposed for
addition. `peppolParticipantId` and `PeppolParticipantId` are shared with the Approved Supplier
rulebook and proposed once. Existing EBWV terms (`EconomicOperator`, `legalName`, `legalIdentifier`,
`Euid`, `attestationLegalCategory`, `ElectronicAttestationOfAttributes`) are reused. The existing EBWV
term `scopeOfAuthorization` is not reused: it describes how a legal representative may sign (for
example jointly), not which operations a service provider may perform.

| Term                                  | Kind     | Definition                                                   |
| ------------------------------------- | -------- | ------------------------------------------------------------ |
| `AuthorizedServiceProviderCredential` | class    | A credential stating that an economic operator is mandated by another economic operator to act as its service provider. |
| `authorizedBy`                        | property | The economic operator (the authorising company) that has mandated the subject. |
| `authorizationScope`                  | property | An operation the subject is authorised to perform; values per code list 4.4. Repeatable. |
| `authorizationValidFrom`              | property | Date from which the authorization is valid (business validity). |
| `authorizationValidUntil`             | property | Date until which the authorization is valid (business validity). |
| `taxReportingMemberState`             | property | ISO 3166-1 alpha-2 code of the Member State for which the subject may perform tax reporting. |
| `peppolAccessPointId`                 | property | Peppol seat ID of the subject's Access Point.                |
| `peppolParticipantId`                 | property | Peppol participant identifier of an economic operator, as `ICD:identifier` (shared with the Approved Supplier rulebook). |
| `PeppolParticipantId`                 | datatype | Datatype for `peppolParticipantId` values, analogous to `Euid` (shared with the Approved Supplier rulebook). |

#### 5.3.1 Mapping of attestation attributes

| Rulebook attribute                         | SD-JWT VC claim                            | W3C VCDM property                                            |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------------------------ |
| Credential type                            | `vct`                                      | `type` includes `AuthorizedServiceProviderCredential`        |
| Legal category                             | `attestation_legal_category`               | `attestationLegalCategory`                                   |
| Issuer                                     | `iss`                                      | `issuer`                                                     |
| Technical validity                         | `iat` / `nbf`, `exp`                       | `validFrom`, `validUntil`                                    |
| Revocation                                 | `status`                                   | `credentialStatus`                                           |
| Holder binding                             | `cnf`                                      | `credentialSubject.id` (`did:jwk`)                           |
| Binding to EBWOID                          | `cryptographically_bound_to`               | not used; binding is evaluated at presentation               |
| `authorized_service_provider.legal_name`   | `authorized_service_provider.legal_name`   | `credentialSubject.legalName`                                |
| `authorized_service_provider.legal_id`     | `authorized_service_provider.legal_id`     | `credentialSubject.legalIdentifier` (`Euid`)                 |
| `authorized_service_provider.peppol_ap_id` | `authorized_service_provider.peppol_ap_id` | `credentialSubject.peppolAccessPointId`                      |
| `authorizing_company.*`                    | `authorizing_company`                      | `credentialSubject.authorizedBy` (`EconomicOperator`, with `legalName`, `legalIdentifier`, `peppolParticipantId`) |
| `authorization_scope`                      | `authorization_scope`                      | `credentialSubject.authorizationScope`                       |
| `authorization_valid_from`                 | `authorization_valid_from`                 | `credentialSubject.authorizationValidFrom`                   |
| `authorization_valid_until`                | `authorization_valid_until`                | `credentialSubject.authorizationValidUntil`                  |
| `tax_reporting_member_state`               | `tax_reporting_member_state`               | `credentialSubject.taxReportingMemberState`                  |
| `authorization_reference`                  | `authorization_reference`                  | not included (see selective disclosure above)                |

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
    "AuthorizedServiceProviderCredential"
  ],
  "id": "urn:uuid:7c2e9a41-5b3d-4f6e-8a1c-2d3e4f5a6b7c",
  "issuer": "https://wallet.greenflowers.example/issuer",
  "validFrom": "2026-01-01T00:00:00Z",
  "validUntil": "2027-01-01T00:00:00Z",
  "attestationLegalCategory": "EAA",
  "credentialStatus": {
    "id": "https://wallet.greenflowers.example/status/authorizedserviceprovider-bsl#87",
    "type": "BitstringStatusListEntry",
    "statusPurpose": "revocation",
    "statusListIndex": "87",
    "statusListCredential": "https://wallet.greenflowers.example/status/authorizedserviceprovider-bsl"
  },
  "credentialSubject": {
    "id": "did:jwk:eyJrdHkiOiJFQyIsImNydiI6IlAtMjU2IiwieCI6ImxTMmJmVng1ZkRZaXVDY0d3MlZ4SE42aHdNaE1mOUdCYnVsTThjRG9RM1kiLCJ5IjoidENhSm9QTXItYkFrei15b19TXzN3Rm95OGdjdzV1ejJZNThDZjQtVnFsTSJ9",
    "type": "EconomicOperator",
    "legalName": "Brabant Access Services N.V.",
    "legalIdentifier": {
      "@type": "Euid",
      "@value": "BEKBOBCE.0890123456"
    },
    "peppolAccessPointId": "PBE000123",
    "authorizedBy": {
      "type": "EconomicOperator",
      "legalName": "Green Flowers B.V.",
      "legalIdentifier": {
        "@type": "Euid",
        "@value": "NLNHR.85374628"
      },
      "peppolParticipantId": {
        "@type": "PeppolParticipantId",
        "@value": "0106:85374628"
      }
    },
    "authorizationScope": [
      "peppol:send",
      "vida:tax_report"
    ],
    "taxReportingMemberState": "NL",
    "authorizationValidFrom": "2026-01-01",
    "authorizationValidUntil": "2026-12-31"
  }
}
```

The credential reads: *Green Flowers B.V. has mandated Brabant Access Services N.V. to send its Peppol
invoices and to perform tax reporting in the Netherlands for 2026.* The validity in
`validFrom`/`validUntil` is the technical validity of the credential;
`authorizationValidFrom`/`authorizationValidUntil` is the business validity of the mandate, and
IR-ASP-01 applies to both pairs.

## 6 Protocols

### 6.1 Issuance

| Protocol   | Supported | Profile or version                       | Specification        | Notes                                                        |
| ---------- | --------- | ---------------------------------------- | -------------------- | ------------------------------------------------------------ |
| OpenID4VCI | yes       | WE BUILD Conformance Specification cs-01 | [OpenID4VCI], [HAIP] | Credential format `dc+sd-jwt`. A credential format identifier for the W3C VCDM encoding is not yet profiled in cs-01. |

### 6.2 Presentation

| Protocol                   | Supported | Profile or version                             | Specification       | Notes                                                        |
| -------------------------- | --------- | ---------------------------------------------- | ------------------- | ------------------------------------------------------------ |
| OpenID4VP, remote          | yes       | WE BUILD Conformance Specification cs-02, DCQL | [OpenID4VP], [HAIP] | Machine-to-machine; the Relying Party requests only the scope elements relevant to its purpose |
| ISO/IEC 18013-5, proximity | no        |                                                | [ISO/IEC 18013-5]   | Requires the mdoc format, which is not defined               |

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
(the Service Provider's wallet), evidenced by the `cnf` claim and verified through key binding at
presentation (base verification step 4.2.8).

**Binding to another attestation.** An attestation of this type SHOULD be cryptographically bound to
the Service Provider's organisational identity attestation (EBWOID) on the same Wallet Unit. Where
present, the binding metadata identifier SHALL be `cryptographically_bound_to`, its value SHALL be a
string containing the bound attestation's vct, and that value SHALL be `uri:eu.ebw.oid.1` (the EBWOID
vct defined in [rb-ebwoid]).

**PID.** A Relying Party does not request or verify a PID. Both the holder (Service Provider) and the
authorising party are legal persons; identity assurance is provided by the EBWOID binding (chapter
10), not by a natural-person PID.

### 7.2 Issuance Policy

The issuer is the authorising company (C1 or C4), a legal person self-issuing this EAA through its EBW
on the basis of a service agreement with the Service Provider. Issuance uses OpenID4VCI as profiled by
the WE BUILD Conformance Specification cs-01.

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

An Authorized Service Provider attestation SHALL remain valid only while the underlying mandate is in
effect. The attestation is **revocable** (it is not a short-lived ≤24h attestation; mandates persist
for the duration of a service agreement).

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
* **Authorized authority:** only the issuing company (the self-issuing legal entity) may modify the
  status list entry.

### 8.2 Revocation triggers and business rules

* **Issuer trigger (obligation):** the authorising company SHALL revoke the attestation without undue
  delay when it changes Service Provider, when the service agreement ends, when the authorised scope
  changes (issuing a replacement attestation), or when the provider's identity data becomes inaccurate.
* **Relying Party action:** a revoked or suspended attestation SHALL be treated as invalid; the
  counterpart AP SHALL reject exchanges relying on it, and a Tax Administration SHALL NOT accept
  reporting mandated by it. The business interpretation of a revocation (e.g. handling of exchanges
  already in flight) is determined by the Relying Party's internal policies.

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
processing an Authorized Service Provider attestation, the Relying Party (the counterpart AP, or a Tax
Administration in Scenario 3) SHALL:

* perform the base attestation verification process for EAAs as defined in the
  [rb-base, Base Verification] specification, section 4.2. This covers verification of attestation
  authenticity and issuer identity via the EBWOID chain (4.2.2–4.2.4), validity periods (4.2.5),
  revocation status (4.2.6), wallet integrity via the WUA (4.2.7), and holder key binding (4.2.8);
* where the attestation carries `cnf`, verify the Key Binding JWT, including `aud`, `nonce` and
  `sd_hash` (see the example in section 5.1.3);
* apply the integrity rules IR-ASP-01 to IR-ASP-04 defined in section 4.5, and verify that the
  requested operation is among the disclosed `authorization_scope` elements;
* as a Tax Administration (Scenario 3), additionally confirm that the `vida:tax_report` element is
  disclosed and that `tax_reporting_member_state` matches its jurisdiction.

A counterpart Access Point SHOULD request only the scope element for the operation in question
(`peppol:send` or `peppol:receive`), and a Tax Administration only `vida:tax_report` and
`tax_reporting_member_state`. Neither SHOULD request `authorization_reference`.

Where the Relying Party is itself an EBW-based system, the Mutual Identification & Consent Handshake
defined in [rb-base, Handshake] SHOULD be applied before presentation.

### 9.2 Presentation modes

Remote presentation is in scope. Proximity presentation is not in scope, as no mdoc encoding is
defined (chapter 5).

### 9.3 Transactional data

No transactional data as defined in Topic 20 of Annex 2 of the ARF is associated with this
attestation type. The attestation authorises a *mandate*, not an individual payment.

## 10 Trust Framework

This chapter specifies how a Relying Party establishes trust in the issuer of an Authorized Service
Provider attestation. The corresponding verification procedures are steps 4.2.2–4.2.4 of the Base
Verification specification.

The Authorized Service Provider attestation is an **EAA self-issued by a legal entity** (the
authorising company). Authorising companies are not, and cannot practically be, individually registered
on a Trusted List. Trust is therefore established through a cryptographic chain anchored in the
issuer's **EBWOID**, following the common WE BUILD EAA trust model:

* The issuer's EBWOID-anchored certificate material SHALL be included in the header (`x5c`) of every
  issued Authorized Service Provider attestation, in both the SD-JWT VC and the W3C VCDM encoding.
  During EBWOID issuance, the EBWOID provider verifies that the public key contained in the EBWOID is
  owned by the EBW owner.
* The Relying Party SHALL verify the EBWOID in accordance with [rb-ebwoid] and the Base Verification
  specification. The EBWOID provider's trust anchor is obtained via the WE BUILD trust list
  infrastructure (TLOL) operated under WP4.
* Upon successful verification, the Relying Party obtains: assurance that the EBWOID was issued by an
  authorised provider (and is not self-issued); the verified identity of the issuer, including its
  legal name and EUID; and the public key authorised to verify the attestation signature.
* The Relying Party SHALL then confirm that the verified issuer identity (EUID) matches
  `authorizing_company.legal_id` in the attestation payload.

Authorization of the issuer *as a mandating company* is subsequently determined in accordance with the
Relying Party's internal policies (e.g. the counterpart AP confirming the company is the Peppol
participant on the invoice; a Tax Administration confirming the company is a registered taxpayer in its
jurisdiction), optionally supported by domain-specific trust list services.

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
| [ViDA]                                 | Council Directive amending Directive 2006/112/EC as regards VAT rules for the digital age (Digital Reporting Requirements) |
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
