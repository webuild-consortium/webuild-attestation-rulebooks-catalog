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
| 1.2     | 2026-11-09 | Restored the version history. Added an informative W3C VCDM encoding, verified SD-JWT examples, the IETF Token Status List structure for `status`, corrected example identifiers, and fixes for inconsistencies introduced by the template migration. |
| 2.0     | 2026-11-09 | Data model change, vct `eu.we-build:authorizedserviceprovider:2`. One attestation now expresses exactly one mandate: a `mandate` object with the service type, the operations within it and the EU Member State whose regime it fulfils. This reflects that a company may mandate different Service Providers for different services in different jurisdictions. The Peppol-specific `peppol_id` and `peppol_ap_id` are replaced by a scheme-qualified `network_identifier` on each party, required for eInvoicing mandates. `authorization_scope` and `tax_reporting_member_state` are removed; integrity rules IR-ASP-02 to IR-ASP-04 are rewritten. No implementations of version 1 exist. |

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
machine-verifiable way, that a named **Service Provider** is mandated to perform a specific service on
the company's behalf in a specific jurisdiction, for example to send and receive invoices in the
Netherlands, or to perform tax reporting in France. The attestation is issued by the company to its
Service Provider and is presented so that a counterpart Access Point, or, in Scenario 3, a **Tax
Administration**, can verify that the Service Provider is genuinely mandated by the company it acts
for. This closes a trust gap in the 4-corner model: it makes the company→provider mandate explicit and
verifiable rather than assumed from network registration alone.

Mandates are granular in practice. A company may mandate one Service Provider for eInvoicing and
another for tax reporting, and use different providers in different Member States. Each attestation
therefore expresses **exactly one mandate**: one company, one Service Provider, one service, one
jurisdiction. A company with several mandates issues several attestations, possibly to different
Service Providers, and each can be revoked independently.

* **Real-world fact expressed:** that a named company mandates a named Service Provider to perform a
  named service, with stated operations, under the regime of a named EU Member State, for a stated
  validity period.
* **Issuers:** the authorising company, for example a Supplier (**C1**) or a Buyer (**C4**), acting as
  a legal person through its European Business Wallet (EBW).
* **Holders:** the Service Provider, for example an Access Point (**C2** or **C3**) or a tax reporting
  provider, holding the attestation in its wallet.
* **Relying parties:** the counterpart Access Point (**C3** or **C2**) for eInvoicing mandates; the
  **Tax Administration** of the mandate's jurisdiction for tax reporting mandates (Scenario 3).
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
jurisdiction of a mandate is an EU Member State, the level at which the [ViDA] Digital Reporting
Requirements and national eInvoicing obligations apply; the precise mapping of the `tax_reporting`
service to a production digital-reporting obligation is out of scope for this pilot version.
Escalation to an eIDAS-qualified EAA (QEAA) is out of scope for this version.

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

The Authorized Service Provider attestation expresses one mandate. The design models the two parties,
the **authorizing company** (the mandator, also the technical issuer) and the **authorized service
provider** (the mandatary, the holder/subject), the **mandate** itself (service, operations and
jurisdiction), and the validity period.

**Logical model (informative):**

```
AuthorizedServiceProviderAttestation
├── attestation_legal_category : "EAA"     (metadata, section 4.1)
├── authorizing_company         (the mandator, also the issuer)
│   ├── legal_name
│   ├── legal_id                (EUID, from the company's EBWOID)
│   └── network_identifier      (conditional: scheme + id, e.g. Peppol participant identifier)
├── authorized_service_provider (the mandatary, the holder/subject)
│   ├── legal_name
│   ├── legal_id                (EUID)
│   └── network_identifier      (conditional: scheme + id, e.g. Peppol Access Point seat ID)
├── mandate
│   ├── service                 (code list, see 4.4)
│   ├── operations[]            (code list, depends on service, see 4.4)
│   └── jurisdiction            (EU Member State)
├── authorization_valid_from    (date)
└── authorization_valid_until   (date; see also the exp metadata claim)
```

**Design decisions.**

* *One mandate per attestation.* Mandates change independently: a company that moves its French tax
  reporting to another provider must be able to revoke exactly that mandate. One attestation per
  mandate gives exact revocation, and a Relying Party only ever sees the mandate that concerns it.
  A company with several mandates issues several attestations, to one or several Service Providers.
* *Service and operations are separate.* The service names the domain of the mandate (`einvoicing`,
  `tax_reporting`); the operations name what the provider may do within it (`send`, `receive`,
  `report`). New services can be added to the code lists without changing the data model.
* *Jurisdiction is a Member State.* It is the EU Member State whose regime the service fulfils, not
  necessarily the Member State where the company is established. A Dutch company VAT-registered in
  France mandates its French tax reporting with jurisdiction `FR`.
* *Network identifiers are scheme-qualified.* Peppol identifiers only make sense for services
  delivered over Peppol. Each party therefore carries an optional `network_identifier` with an
  explicit scheme, and integrity rule IR-ASP-03 states when it is required. This keeps the party
  objects network-neutral.

This model refines the flat claim list in the SC5 scenario description (issuer_id, issuer_name,
subject_id, subject_name, authorization_date, expiry_date, scope, company_peppol_id, sp_peppol_ap_id)
while preserving its information content.

**Applicable legal category.** Per the SC5 working assumptions, the Authorized Service Provider
attestation is implemented as a **non-qualified EAA**. Where SC5 material refers to a "WE BUILD QEAA",
this denotes a technically interoperable, ITB-tested attestation within the pilot trust framework, not
an eIDAS-qualified EAA. The applicable Topic 12 requirements for this category are mapped in section
2.3.

**Schema artefacts.**

| Format    | Identifier                                                   | Schema artefact                                       | Version | Location                                                     |
| --------- | ------------------------------------------------------------ | ----------------------------------------------------- | ------- | ------------------------------------------------------------ |
| SD-JWT VC | `eu.we-build:authorizedserviceprovider:2`                    | JSON Schema                                           | 2.0     | [`data-schemas/sd-jwt/service-provider-authorization-sd-jwt.json`](../../data-schemas/sd-jwt/service-provider-authorization-sd-jwt.json), sample [`service-provider-authorization-sd-jwt-sample.json`](../../data-schemas/sd-jwt/sample-data/service-provider-authorization-sd-jwt-sample.json) |
| W3C VCDM  | type `AuthorizedServiceProviderCredential`, context `https://w3id.org/ebwv/v0.1` | JSON-LD context (EBWV), terms proposed in section 5.3 | pending | To be published by the WP4 semantics group                   |

The schema artefact file names differ from the rulebook name because the catalog's sample-matching
workflow matches on the first five characters of the file name, which would otherwise collide with
`authorised-signatories`. The JSON Schema enforces integrity rules IR-ASP-02 and IR-ASP-03 and the
Member State code list.

The schema artefacts referenced above are normative for encoding. Where this document and a
referenced artefact disagree, the artefact prevails for encoding questions and this document prevails
for semantics, presence and disclosure rules.

Selective disclosure applies to the SD-JWT VC encoding and is stated per attribute in the tables
below (EW-DM-12-034). The W3C VCDM encoding of section 5.3 has no selective disclosure; section 5.3
states how this is handled.

### 3.2 Mandatory attributes

| Data identifier                          | Semantic reference                                           | Definition                                                   | Data type              | Selectively disclosable                  | Example value                  |
| ---------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------------------- | ---------------------------------------- | ------------------------------ |
| `authorizing_company.legal_name`         | N/A (SC5-defined)                                            | Registered legal name of the authorising company.            | string                 | MAY (with `authorizing_company`)         | `Green Flowers B.V.`           |
| `authorizing_company.legal_id`           | EUID (Directive (EU) 2017/1132, Implementing Regulation (EU) 2021/1042) | Unique legal-person identifier of the company, sourced from its EBWOID. | string                 | MAY (with `authorizing_company`)         | `NLNHR.85374628`               |
| `authorized_service_provider.legal_name` | N/A (SC5-defined)                                            | Registered legal name of the Service Provider (the holder).  | string                 | MAY (with `authorized_service_provider`) | `Brabant Access Services N.V.` |
| `authorized_service_provider.legal_id`   | EUID (Directive (EU) 2017/1132, Implementing Regulation (EU) 2021/1042) | Unique legal-person identifier of the Service Provider.      | string                 | MAY (with `authorized_service_provider`) | `BEKBOBCE.0890123456`          |
| `mandate.service`                        | N/A (code list, section 4.4)                                 | Type of service mandated.                                    | string (enum)          | MAY (with `mandate`)                     | `einvoicing`                   |
| `mandate.operations`                     | N/A (code list, section 4.4)                                 | One or more operations the Service Provider may perform within the service. | array of string (enum) | MAY (with `mandate`)                     | `["send", "receive"]`          |
| `mandate.jurisdiction`                   | ISO 3166-1 alpha-2, restricted to EU Member States (code list, section 4.4) | The EU Member State whose regime the mandated service fulfils. | string (enum)          | MAY (with `mandate`)                     | `NL`                           |
| `authorization_valid_from`               | N/A                                                          | Date from which the mandate is valid.                        | full-date (RFC 3339)   | MAY                                      | `2026-01-01`                   |

The objects `authorizing_company`, `authorized_service_provider` and `mandate` are disclosed as a
whole; their sub-claims are not individually selectively disclosable. A Relying Party that receives
`mandate` therefore always sees the service, the operations and the jurisdiction together.

### 3.3 Optional attributes

| Data identifier             | Semantic reference | Definition                                                   | Data type            | Selectively disclosable                                      | Example value     |
| --------------------------- | ------------------ | ------------------------------------------------------------ | -------------------- | ------------------------------------------------------------ | ----------------- |
| `authorization_valid_until` | N/A                | Date until which the mandate is valid (business validity, distinct from the technical `exp` metadata claim). | full-date (RFC 3339) | MAY                                                          | `2026-12-31`      |
| `authorization_reference`   | N/A                | Company-internal reference for the service agreement underlying the mandate. | string               | MUST, so that the provider can withhold the internal reference | `SLA-2026-AP-007` |

### 3.4 Conditional attributes

| Data identifier                                  | Semantic reference                  | Definition                                                   | Condition                                                    | Data type | Selectively disclosable                  | Example value                                             |
| ------------------------------------------------ | ----------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | --------- | ---------------------------------------- | --------------------------------------------------------- |
| `authorizing_company.network_identifier`         | Identifier scheme per code list 4.4 | Identifier of the company in the network used to deliver the service: an object with `scheme` and `id`. | SHALL be present with scheme `peppol-participant` when `mandate.service` is `einvoicing` (IR-ASP-03); MAY be present otherwise. | object    | MAY (with `authorizing_company`)         | `{"scheme": "peppol-participant", "id": "0106:85374628"}` |
| `authorized_service_provider.network_identifier` | Identifier scheme per code list 4.4 | Identifier of the Service Provider in the network used to deliver the service: an object with `scheme` and `id`. | SHALL be present with scheme `peppol-ap` when `mandate.service` is `einvoicing` (IR-ASP-03); MAY be present otherwise. | object    | MAY (with `authorized_service_provider`) | `{"scheme": "peppol-ap", "id": "PBE000123"}`              |

## 4 Metadata

Metadata describes the attestation rather than its subject. Metadata claims are not selectively
disclosable.

### 4.1 Mandatory metadata

| Data identifier              | Semantic reference               | Definition                                                   | Data type    | Example value                                      |
| ---------------------------- | -------------------------------- | ------------------------------------------------------------ | ------------ | -------------------------------------------------- |
| `attestation_legal_category` | EW-DM-12-015 / EW-DM-12-029      | Indicates the legal category of the attestation.             | string       | `EAA`                                              |
| `vct`                        | [SD-JWT VC]                      | Verifiable Credential Type identifier (see section 5.1).     | string       | `eu.we-build:authorizedserviceprovider:2`          |
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
| `schema_version`             | N/A                | Version of the schema artefact used.                         | string       | `2.0`                                 |
| `trust_anchor_url`           | EW-DM-12-024       | URL at which a machine-readable version of the trust anchor can be found or looked up. For this attestation the trust anchor is the EBWOID provider's entry in the WE BUILD trust list infrastructure (chapter 10). | string (URI) | *(WE BUILD TLOL entry)*               |

### 4.3 Conditional metadata

The Authorized Service Provider attestation defined in this Rulebook does not contain any
conditional metadata.

### 4.4 Code lists

| Field                                    | Allowed values or vocabulary                                 | Meaning                                                      | Source                                                       | Extensible                        |
| ---------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | --------------------------------- |
| `mandate.service`                        | `einvoicing`                                                 | Exchange of electronic invoices on the company's behalf, in the 4-corner model over Peppol. | WE BUILD SC5 vocabulary                                      | Yes, see below                    |
| `mandate.service`                        | `tax_reporting`                                              | Tax reporting / digital reporting to the Tax Administration of the jurisdiction on the company's behalf (Scenario 3), aligned with the ViDA Digital Reporting Requirements. | WE BUILD SC5 vocabulary                                      | Yes, see below                    |
| `mandate.operations` for `einvoicing`    | `send`, `receive`                                            | `send`: transmit invoices as the company's sending Access Point (C2). `receive`: receive invoices as the company's receiving Access Point (C3). Both MAY be present where the same provider acts as C2 and C3. | WE BUILD SC5 vocabulary                                      | Yes, see below                    |
| `mandate.operations` for `tax_reporting` | `report`                                                     | Submit reports to the Tax Administration of the jurisdiction. | WE BUILD SC5 vocabulary                                      | Yes, see below                    |
| `mandate.jurisdiction`                   | `AT`, `BE`, `BG`, `CY`, `CZ`, `DE`, `DK`, `EE`, `ES`, `FI`, `FR`, `GR`, `HR`, `HU`, `IE`, `IT`, `LT`, `LU`, `LV`, `MT`, `NL`, `PL`, `PT`, `RO`, `SE`, `SI`, `SK` | The EU Member States, as ISO 3166-1 alpha-2 codes. Greece is `GR`; the VAT prefix `EL` is not used. | [ISO 3166-1]                                                 | Only on a change in EU membership |
| `network_identifier.scheme`              | `peppol-participant`                                         | Peppol participant identifier, `id` as `ICD:identifier` (the value part of the `iso6523-actorid-upis` scheme), e.g. `0106:85374628`. | WE BUILD SC5 vocabulary; Peppol Policy for use of Identifiers | Yes, see below                    |
| `network_identifier.scheme`              | `peppol-ap`                                                  | Peppol Access Point seat ID (CN of the Peppol AP certificate), e.g. `PBE000123`. | WE BUILD SC5 vocabulary; Peppol PKI                          | Yes, see below                    |

Additional services, operations and identifier schemes SHOULD only be introduced if defined
consistently across issuers and verifiers and registered in the WE BUILD Attestation Rulebooks
catalog. A new service SHALL state its allowed operations and the network identifier schemes it
requires, if any.

### 4.5 Integrity rules

| Rule ID     | Rule statement                                               | Why it exists                                                | Where enforced                                               | Behaviour on failure                                         |
| ----------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `IR-ASP-01` | `authorization_valid_from` SHALL NOT be later than `authorization_valid_until` (when present), and both SHALL fall within the `iat`–`exp` window. | Prevents inconsistent or unusable validity periods.          | Issuer business rules; verifier business validation.         | Issuer SHALL reject; verifier SHALL treat the attestation as invalid. |
| `IR-ASP-02` | `mandate.operations` SHALL contain only operations allowed for `mandate.service` in code list 4.4. | Keeps each mandate within its service, so that a tax reporting mandate never carries invoice send or receive rights, and vice versa. | Issuer business rules; JSON Schema; verifier business validation. | Issuer SHALL reject; verifier SHALL treat the attestation as invalid. |
| `IR-ASP-03` | When `mandate.service` is `einvoicing`, `authorizing_company.network_identifier` SHALL be present with scheme `peppol-participant`, and `authorized_service_provider.network_identifier` SHALL be present with scheme `peppol-ap`. | The counterpart Access Point can only bind the mandate to an invoice flow through the Peppol identifiers (IR-ASP-04). | Issuer business rules; JSON Schema.                          | Issuer SHALL reject; verifier SHALL treat the attestation as invalid. |
| `IR-ASP-04` | At verification time, the Relying Party SHALL bind the mandate to the transaction in hand. For `einvoicing`: the provider's `peppol-ap` identifier SHALL match the Access Point transmitting or receiving the invoice, the company's `peppol-participant` identifier SHALL match the corresponding party on the invoice, and the operation performed SHALL be in `mandate.operations`. For `tax_reporting`: `mandate.jurisdiction` SHALL be the Tax Administration's own Member State, and the company identified by `authorizing_company.legal_id` SHALL be the taxable person on whose behalf the report is submitted. | Prevents reuse of a valid mandate for an unrelated company, provider, operation or jurisdiction. | Verifier (counterpart Access Point, or Tax Administration).  | Verifier SHALL reject the transaction.                       |

## 5 Formats

| Format               | Supported         | Identifier                                                   | Specification                   | Notes                                                        |
| -------------------- | ----------------- | ------------------------------------------------------------ | ------------------------------- | ------------------------------------------------------------ |
| ISO/IEC 18013-5 mdoc | no                |                                                              | [ISO/IEC 18013-5]               | Proximity presentation is not in scope (EW-DM-12-003)        |
| SD-JWT VC            | yes               | `vct` `eu.we-build:authorizedserviceprovider:2`              | [SD-JWT VC], [HAIP]             | Normative format; SHALL follow the HAIP profile (EW-DM-12-002) |
| W3C VCDM             | yes (informative) | type `AuthorizedServiceProviderCredential`, context `https://w3id.org/ebwv/v0.1` | [W3C VCDM v2.0], [VC-JOSE-COSE] | Permitted for non-qualified EAA (EW-DM-12-001); see section 5.3 |

A Provider SHALL offer the SD-JWT VC format. A Provider MAY additionally offer the W3C VCDM format
once section 5.3 is normative. A Relying Party in the SC5 flows SHALL accept SD-JWT VC and is not
required to accept W3C VCDM.

### 5.1 SD-JWT VC-based encoding

This attestation type SHALL be issued in the [SD-JWT VC]-compliant format and SHALL comply with the
'SD-JWT VCs' profile specified in [HAIP] (EW-DM-12-002).

**Verifiable Credential Type (`vct`):** `eu.we-build:authorizedserviceprovider:2`

*(Proposed value; subject to registration in the WE BUILD Attestation Rulebooks catalog by the WP4
semantics group, EW-DM-12-006. Version `1` is withdrawn; it was never implemented.)*

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
| `authorizing_company`             | authorizing_company         | object; `network_identifier` as object with `scheme` and `id` | Sections 3.2, 3.4              |
| `authorized_service_provider`     | authorized_service_provider | object; `network_identifier` as object with `scheme` and `id` | Sections 3.2, 3.4              |
| `mandate`                         | mandate                     | object with `service` (string), `operations` (array of string), `jurisdiction` (string) | Section 3.2; code list 4.4     |
| `authorization_valid_from`        | authorization_valid_from    | string (full-date)                                           | Section 3.2                    |
| `authorization_valid_until`       | authorization_valid_until   | string (full-date)                                           | Section 3.3                    |
| `authorization_reference`         | authorization_reference     | string                                                       | Section 3.3                    |
| `cryptographically_bound_to`      | cryptographically_bound_to  | string                                                       | Section 4.2; section 7.1       |

**Logical claim sets (informative, fictitious data, all disclosures applied).** An eInvoicing mandate,
used in the examples of sections 5.1.1 to 5.1.3:

```json
{
  "vct": "eu.we-build:authorizedserviceprovider:2",
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
      "x": "9UnMnpFkv0a1i0Ve-u4ZPRyk8oNnUetaYlSPuTUOQjk",
      "y": "3kfxbzP1OTM3gvNESyEOgqMsiG0TxZwQvzPnMTGq8PY"
    }
  },
  "authorizing_company": {
    "legal_name": "Green Flowers B.V.",
    "legal_id": "NLNHR.85374628",
    "network_identifier": {
      "scheme": "peppol-participant",
      "id": "0106:85374628"
    }
  },
  "authorized_service_provider": {
    "legal_name": "Brabant Access Services N.V.",
    "legal_id": "BEKBOBCE.0890123456",
    "network_identifier": {
      "scheme": "peppol-ap",
      "id": "PBE000123"
    }
  },
  "mandate": {
    "service": "einvoicing",
    "operations": [
      "send",
      "receive"
    ],
    "jurisdiction": "NL"
  },
  "authorization_valid_from": "2026-01-01",
  "authorization_valid_until": "2026-12-31",
  "authorization_reference": "SLA-2026-AP-007"
}
```

A second attestation from the same company, mandating a different Service Provider for tax reporting
in France (this is also the catalog sample). No network identifiers are needed for this service:

```json
{
  "vct": "eu.we-build:authorizedserviceprovider:2",
  "iss": "https://wallet.greenflowers.example/issuer",
  "iat": 1767225600,
  "exp": 1798761600,
  "nbf": 1767225600,
  "sub": "did:example:loire-reporting-services",
  "attestation_legal_category": "EAA",
  "schema_version": "2.0",
  "cryptographically_bound_to": "uri:eu.ebw.oid.1",
  "status": {
    "status_list": {
      "idx": 88,
      "uri": "https://wallet.greenflowers.example/status/authorizedserviceprovider"
    }
  },
  "cnf": {
    "jwk": {
      "kty": "EC",
      "crv": "P-256",
      "x": "...",
      "y": "..."
    }
  },
  "authorizing_company": {
    "legal_name": "Green Flowers B.V.",
    "legal_id": "NLNHR.85374628"
  },
  "authorized_service_provider": {
    "legal_name": "Loire Reporting Services SAS",
    "legal_id": "FRRCS.901234567"
  },
  "mandate": {
    "service": "tax_reporting",
    "operations": [
      "report"
    ],
    "jurisdiction": "FR"
  },
  "authorization_valid_from": "2026-01-01",
  "authorization_valid_until": "2026-12-31",
  "authorization_reference": "MANDATE-FR-2026-03"
}
```

#### 5.1.1 Issued SD-JWT (informative)

The example below is a complete issued SD-JWT for the eInvoicing mandate, signed with a throw-away
ES256 test key. All organisations, identifiers and keys are fictitious. Every attribute of chapter 3
is selectively disclosable in this example: `authorization_reference` because it MUST be, the others to
show how the Service Provider controls disclosure. A Provider MAY make fewer claims disclosable, as
permitted in sections 3.2 to 3.4. For readability the header carries a `kid`; a production attestation
SHALL carry the EBWOID-anchored certificate material in `x5c` instead (chapter 10). The example SHALL
be regenerated if the selective-disclosure structure changes.

Issued SD-JWT (issuer-signed JWT `~` disclosures `~`):

```
eyJhbGciOiJFUzI1NiIsInR5cCI6ImRjK3NkLWp3dCIsImtpZCI6ImdyZWVuZmxvd2Vycy1lYnctaXNzdWVyLXRlc3QifQ.eyJ2Y3QiOiJldS53ZS1idWlsZDphdXRob3JpemVkc2VydmljZXByb3ZpZGVyOjIiLCJpc3MiOiJodHRwczovL3dhbGxldC5ncmVlbmZsb3dlcnMuZXhhbXBsZS9pc3N1ZXIiLCJpYXQiOjE3NjcyMjU2MDAsImV4cCI6MTc5ODc2MTYwMCwiYXR0ZXN0YXRpb25fbGVnYWxfY2F0ZWdvcnkiOiJFQUEiLCJjcnlwdG9ncmFwaGljYWxseV9ib3VuZF90byI6InVyaTpldS5lYncub2lkLjEiLCJzdGF0dXMiOnsic3RhdHVzX2xpc3QiOnsiaWR4Ijo4NywidXJpIjoiaHR0cHM6Ly93YWxsZXQuZ3JlZW5mbG93ZXJzLmV4YW1wbGUvc3RhdHVzL2F1dGhvcml6ZWRzZXJ2aWNlcHJvdmlkZXIifX0sImNuZiI6eyJqd2siOnsia3R5IjoiRUMiLCJjcnYiOiJQLTI1NiIsIngiOiI5VW5NbnBGa3YwYTFpMFZlLXU0WlBSeWs4b05uVWV0YVlsU1B1VFVPUWprIiwieSI6IjNrZnhielAxT1RNM2d2TkVTeUVPZ3FNc2lHMFR4WndRdnpQbk1UR3E4UFkifX0sIl9zZCI6WyI5TlFqeVdZd3hfcUVoR2dkSHpnLWxDYzhRVkRNa0kxYlJJMUVES0dGSXBVIiwiRHZaa19lVmd0aGRQdHAwVlNydnYyeUtKNDA3WHlWRG81ZWpDNjRvTlA1byIsIkw0Z3hGQkJTa24tYzFKZlpVWnFQMS1JZXRUOEJ0WEdsRjF4ZEo3X0tNdWMiLCJYRTNKZVBWQmkwblNEZTBEbkNTMXBnc2FhZFp4LWd4R3hldkg5QXJEVkM0IiwiZWM3amR3cUNDaFYwSFZQMDlaVFZzaWo2Qm9NWmp1cVBoY2l0bm04QUdudyIsInY2SXQ2cTVXc293RTl2c1pRZ1hXYUhSVndvQ25TRkhBb2kyR3ROZEpSalkiXSwiX3NkX2FsZyI6InNoYS0yNTYifQ.JKDdurjNadhH495sBIs0YNhzni6NtitHT53hoJN6R_vnk-KXvBJa-5vasUM1QLsa2Lr9iakhDLXM4NVWPcJz7Q~WyJmenFRTm9jbW9GUmNpTVZobFZwS3VnIiwiYXV0aG9yaXppbmdfY29tcGFueSIseyJsZWdhbF9uYW1lIjoiR3JlZW4gRmxvd2VycyBCLlYuIiwibGVnYWxfaWQiOiJOTE5IUi44NTM3NDYyOCIsIm5ldHdvcmtfaWRlbnRpZmllciI6eyJzY2hlbWUiOiJwZXBwb2wtcGFydGljaXBhbnQiLCJpZCI6IjAxMDY6ODUzNzQ2MjgifX1d~WyJnZXkzZ0hzZlRlMktHZ0xNcGgyQUxRIiwiYXV0aG9yaXplZF9zZXJ2aWNlX3Byb3ZpZGVyIix7ImxlZ2FsX25hbWUiOiJCcmFiYW50IEFjY2VzcyBTZXJ2aWNlcyBOLlYuIiwibGVnYWxfaWQiOiJCRUtCT0JDRS4wODkwMTIzNDU2IiwibmV0d29ya19pZGVudGlmaWVyIjp7InNjaGVtZSI6InBlcHBvbC1hcCIsImlkIjoiUEJFMDAwMTIzIn19XQ~WyJIS2FjdXdlTnRBRnFudEVLRGpGaWZnIiwibWFuZGF0ZSIseyJzZXJ2aWNlIjoiZWludm9pY2luZyIsIm9wZXJhdGlvbnMiOlsic2VuZCIsInJlY2VpdmUiXSwianVyaXNkaWN0aW9uIjoiTkwifV0~WyJIVlJ0Y0FmdThNYVVoMXJqTjM3ZHZRIiwiYXV0aG9yaXphdGlvbl92YWxpZF9mcm9tIiwiMjAyNi0wMS0wMSJd~WyJTNDhYLXVpekV3YlRHN29CZngtaUh3IiwiYXV0aG9yaXphdGlvbl92YWxpZF91bnRpbCIsIjIwMjYtMTItMzEiXQ~WyJFVGRKNzk3VFZKNlRQc1h4NXVlaWRnIiwiYXV0aG9yaXphdGlvbl9yZWZlcmVuY2UiLCJTTEEtMjAyNi1BUC0wMDciXQ~
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
  "vct": "eu.we-build:authorizedserviceprovider:2",
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
      "x": "9UnMnpFkv0a1i0Ve-u4ZPRyk8oNnUetaYlSPuTUOQjk",
      "y": "3kfxbzP1OTM3gvNESyEOgqMsiG0TxZwQvzPnMTGq8PY"
    }
  },
  "_sd": [
    "9NQjyWYwx_qEhGgdHzg-lCc8QVDMkI1bRI1EDKGFIpU",
    "DvZk_eVgthdPtp0VSrvv2yKJ407XyVDo5ejC64oNP5o",
    "L4gxFBBSkn-c1JfZUZqP1-IetT8BtXGlF1xdJ7_KMuc",
    "XE3JePVBi0nSDe0DnCS1pgsaadZx-gxGxevH9ArDVC4",
    "ec7jdwqCChV0HVP09ZTVsij6BoMZjuqPhcitnm8AGnw",
    "v6It6q5WsowE9vsZQgXWaHRVwoCnSFHAoi2GtNdJRjY"
  ],
  "_sd_alg": "sha-256"
}
```

Disclosures (`[salt, claim name, claim value]`) and the digest each produces in `_sd`:

| Claim                         | Disclosure (decoded)                                         | Digest (SHA-256, base64url)                   |
| ----------------------------- | ------------------------------------------------------------ | --------------------------------------------- |
| `authorizing_company`         | `["fzqQNocmoFRciMVhlVpKug", "authorizing_company", {"legal_name": "Green Flowers B.V.", "legal_id": "NLNHR.85374628", "network_identifier": {"scheme": "peppol-participant", "id": "0106:85374628"}}]` | `L4gxFBBSkn-c1JfZUZqP1-IetT8BtXGlF1xdJ7_KMuc` |
| `authorized_service_provider` | `["gey3gHsfTe2KGgLMph2ALQ", "authorized_service_provider", {"legal_name": "Brabant Access Services N.V.", "legal_id": "BEKBOBCE.0890123456", "network_identifier": {"scheme": "peppol-ap", "id": "PBE000123"}}]` | `9NQjyWYwx_qEhGgdHzg-lCc8QVDMkI1bRI1EDKGFIpU` |
| `mandate`                     | `["HKacuweNtAFqntEKDjFifg", "mandate", {"service": "einvoicing", "operations": ["send", "receive"], "jurisdiction": "NL"}]` | `DvZk_eVgthdPtp0VSrvv2yKJ407XyVDo5ejC64oNP5o` |
| `authorization_valid_from`    | `["HVRtcAfu8MaUh1rjN37dvQ", "authorization_valid_from", "2026-01-01"]` | `v6It6q5WsowE9vsZQgXWaHRVwoCnSFHAoi2GtNdJRjY` |
| `authorization_valid_until`   | `["S48X-uizEwbTG7oBfx-iHw", "authorization_valid_until", "2026-12-31"]` | `XE3JePVBi0nSDe0DnCS1pgsaadZx-gxGxevH9ArDVC4` |
| `authorization_reference`     | `["ETdJ797TVJ6TPsXx5ueidg", "authorization_reference", "SLA-2026-AP-007"]` | `ec7jdwqCChV0HVP09ZTVsij6BoMZjuqPhcitnm8AGnw` |

#### 5.1.3 Presentation to the counterpart Access Point (informative)

The Service Provider, acting as the company's C2, presents the attestation to the receiving Access
Point (C3). It discloses the two party objects, the mandate and the validity, withholds
`authorization_reference`, and appends a Key Binding JWT signed with the key in `cnf`, binding the
presentation to C3 (`aud`), to the request (`nonce`) and to the exact set of disclosures (`sd_hash`):

```json
{
  "iat": 1768392000,
  "aud": "https://ap.c3-provider.example",
  "nonce": "q-4Rt8ZpW1Ns",
  "sd_hash": "pjBD2mUV46BWtI0TMHcOvHceXoWsq6C6AdsGKBWvDcE"
}
```

Presented SD-JWT+KB:

```
eyJhbGciOiJFUzI1NiIsInR5cCI6ImRjK3NkLWp3dCIsImtpZCI6ImdyZWVuZmxvd2Vycy1lYnctaXNzdWVyLXRlc3QifQ.eyJ2Y3QiOiJldS53ZS1idWlsZDphdXRob3JpemVkc2VydmljZXByb3ZpZGVyOjIiLCJpc3MiOiJodHRwczovL3dhbGxldC5ncmVlbmZsb3dlcnMuZXhhbXBsZS9pc3N1ZXIiLCJpYXQiOjE3NjcyMjU2MDAsImV4cCI6MTc5ODc2MTYwMCwiYXR0ZXN0YXRpb25fbGVnYWxfY2F0ZWdvcnkiOiJFQUEiLCJjcnlwdG9ncmFwaGljYWxseV9ib3VuZF90byI6InVyaTpldS5lYncub2lkLjEiLCJzdGF0dXMiOnsic3RhdHVzX2xpc3QiOnsiaWR4Ijo4NywidXJpIjoiaHR0cHM6Ly93YWxsZXQuZ3JlZW5mbG93ZXJzLmV4YW1wbGUvc3RhdHVzL2F1dGhvcml6ZWRzZXJ2aWNlcHJvdmlkZXIifX0sImNuZiI6eyJqd2siOnsia3R5IjoiRUMiLCJjcnYiOiJQLTI1NiIsIngiOiI5VW5NbnBGa3YwYTFpMFZlLXU0WlBSeWs4b05uVWV0YVlsU1B1VFVPUWprIiwieSI6IjNrZnhielAxT1RNM2d2TkVTeUVPZ3FNc2lHMFR4WndRdnpQbk1UR3E4UFkifX0sIl9zZCI6WyI5TlFqeVdZd3hfcUVoR2dkSHpnLWxDYzhRVkRNa0kxYlJJMUVES0dGSXBVIiwiRHZaa19lVmd0aGRQdHAwVlNydnYyeUtKNDA3WHlWRG81ZWpDNjRvTlA1byIsIkw0Z3hGQkJTa24tYzFKZlpVWnFQMS1JZXRUOEJ0WEdsRjF4ZEo3X0tNdWMiLCJYRTNKZVBWQmkwblNEZTBEbkNTMXBnc2FhZFp4LWd4R3hldkg5QXJEVkM0IiwiZWM3amR3cUNDaFYwSFZQMDlaVFZzaWo2Qm9NWmp1cVBoY2l0bm04QUdudyIsInY2SXQ2cTVXc293RTl2c1pRZ1hXYUhSVndvQ25TRkhBb2kyR3ROZEpSalkiXSwiX3NkX2FsZyI6InNoYS0yNTYifQ.JKDdurjNadhH495sBIs0YNhzni6NtitHT53hoJN6R_vnk-KXvBJa-5vasUM1QLsa2Lr9iakhDLXM4NVWPcJz7Q~WyJmenFRTm9jbW9GUmNpTVZobFZwS3VnIiwiYXV0aG9yaXppbmdfY29tcGFueSIseyJsZWdhbF9uYW1lIjoiR3JlZW4gRmxvd2VycyBCLlYuIiwibGVnYWxfaWQiOiJOTE5IUi44NTM3NDYyOCIsIm5ldHdvcmtfaWRlbnRpZmllciI6eyJzY2hlbWUiOiJwZXBwb2wtcGFydGljaXBhbnQiLCJpZCI6IjAxMDY6ODUzNzQ2MjgifX1d~WyJnZXkzZ0hzZlRlMktHZ0xNcGgyQUxRIiwiYXV0aG9yaXplZF9zZXJ2aWNlX3Byb3ZpZGVyIix7ImxlZ2FsX25hbWUiOiJCcmFiYW50IEFjY2VzcyBTZXJ2aWNlcyBOLlYuIiwibGVnYWxfaWQiOiJCRUtCT0JDRS4wODkwMTIzNDU2IiwibmV0d29ya19pZGVudGlmaWVyIjp7InNjaGVtZSI6InBlcHBvbC1hcCIsImlkIjoiUEJFMDAwMTIzIn19XQ~WyJIS2FjdXdlTnRBRnFudEVLRGpGaWZnIiwibWFuZGF0ZSIseyJzZXJ2aWNlIjoiZWludm9pY2luZyIsIm9wZXJhdGlvbnMiOlsic2VuZCIsInJlY2VpdmUiXSwianVyaXNkaWN0aW9uIjoiTkwifV0~WyJIVlJ0Y0FmdThNYVVoMXJqTjM3ZHZRIiwiYXV0aG9yaXphdGlvbl92YWxpZF9mcm9tIiwiMjAyNi0wMS0wMSJd~WyJTNDhYLXVpekV3YlRHN29CZngtaUh3IiwiYXV0aG9yaXphdGlvbl92YWxpZF91bnRpbCIsIjIwMjYtMTItMzEiXQ~eyJhbGciOiJFUzI1NiIsInR5cCI6ImtiK2p3dCJ9.eyJpYXQiOjE3NjgzOTIwMDAsImF1ZCI6Imh0dHBzOi8vYXAuYzMtcHJvdmlkZXIuZXhhbXBsZSIsIm5vbmNlIjoicS00UnQ4WnBXMU5zIiwic2RfaGFzaCI6InBqQkQybVVWNDZCV3RJMFRNSGNPdkhjZVhvV3NxNkM2QWRzR0tCV3ZEY0UifQ.02yV-nfL_gbHB7gmL34hVzwHmD6TD4eD5Z5scnAPsJlRaH_zvjHz-afrPfGk6AK9r2cnQkB1jrQAOBizdbDMsA
```

C3 then applies IR-ASP-04: `PBE000123` is the Access Point transmitting the invoice, `0106:85374628`
is the sender on the invoice, and `send` is in `mandate.operations`.

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
`credentialSubject` is therefore the Service Provider. The mandate is expressed as properties of it
(`authorizedBy`, `mandateService`, `mandateOperation`, `mandateJurisdiction`,
`authorizationValidFrom`, `authorizationValidUntil`). A network identifier is a typed literal under
`networkIdentifier`, where the datatype carries the scheme (`PeppolParticipantId`,
`PeppolAccessPointId`), in the same way as `legalIdentifier` uses `Euid`. This carries the same
information as the SD-JWT VC claim set; section 5.3.1 gives the mapping.

**Securing mechanism.** The credential SHALL be secured as a JWT according to [VC-JOSE-COSE]. The JOSE
header SHALL carry the issuer's EBWOID-anchored certificate material in `x5c`, so the trust model of
chapter 10 applies unchanged. Data Integrity proofs are not used in this version, because the EBWOID
trust model anchors the issuer key in X.509 certificate material rather than in a verification method
resolved from the `issuer` identifier.

**Selective disclosure.** This encoding provides no selective disclosure. `authorization_reference`,
which MUST be selectively disclosable (section 3.3), SHALL NOT be included. Because each attestation
carries one mandate, the lack of selective disclosure does not expose a provider's other mandates.

**Holder binding.** `credentialSubject.id` SHALL be a `did:jwk` derived from the holder's public key,
which takes the role of `cnf` in the SD-JWT VC encoding. The Service Provider proves possession of the
corresponding private key when presenting.

**Revocation.** `credentialStatus` SHALL use a `BitstringStatusListEntry` according to [W3C Bitstring
Status List], with `statusPurpose` `revocation`. *Open point:* the WE BUILD ADR on Attestation
Revocation mandates the IETF Token Status List; confirmation is needed that the W3C Bitstring Status
List is acceptable for the VCDM encoding, or that the Token Status List shall be used for both.

**Proposed vocabulary terms.** The following terms do not exist in EBWV and are proposed for
addition. `PeppolParticipantId` is shared with the Approved Supplier rulebook and proposed once.
Existing EBWV terms (`EconomicOperator`, `legalName`, `legalIdentifier`, `Euid`,
`attestationLegalCategory`, `ElectronicAttestationOfAttributes`) are reused. The existing EBWV term
`scopeOfAuthorization` is not reused: it describes how a legal representative may sign (for example
jointly), not which service a provider may perform.

| Term                                  | Kind     | Definition                                                   |
| ------------------------------------- | -------- | ------------------------------------------------------------ |
| `AuthorizedServiceProviderCredential` | class    | A credential stating that an economic operator is mandated by another economic operator to perform a service on its behalf in a jurisdiction. |
| `authorizedBy`                        | property | The economic operator (the authorising company) that has mandated the subject. |
| `mandateService`                      | property | The service mandated; values per code list 4.4.              |
| `mandateOperation`                    | property | An operation the subject may perform within the service; values per code list 4.4. Repeatable. |
| `mandateJurisdiction`                 | property | ISO 3166-1 alpha-2 code of the EU Member State whose regime the service fulfils. |
| `authorizationValidFrom`              | property | Date from which the mandate is valid (business validity).    |
| `authorizationValidUntil`             | property | Date until which the mandate is valid (business validity).   |
| `networkIdentifier`                   | property | Identifier of an economic operator in the network used to deliver the service, as a typed literal whose datatype names the scheme. |
| `PeppolParticipantId`                 | datatype | Peppol participant identifier as `ICD:identifier` (shared with the Approved Supplier rulebook). |
| `PeppolAccessPointId`                 | datatype | Peppol Access Point seat ID.                                 |

#### 5.3.1 Mapping of attestation attributes

| Rulebook attribute                               | SD-JWT VC claim                                  | W3C VCDM property                                            |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------------------ |
| Credential type                                  | `vct`                                            | `type` includes `AuthorizedServiceProviderCredential`        |
| Legal category                                   | `attestation_legal_category`                     | `attestationLegalCategory`                                   |
| Issuer                                           | `iss`                                            | `issuer`                                                     |
| Technical validity                               | `iat` / `nbf`, `exp`                             | `validFrom`, `validUntil`                                    |
| Revocation                                       | `status`                                         | `credentialStatus`                                           |
| Holder binding                                   | `cnf`                                            | `credentialSubject.id` (`did:jwk`)                           |
| Binding to EBWOID                                | `cryptographically_bound_to`                     | not used; binding is evaluated at presentation               |
| `authorized_service_provider.legal_name`         | `authorized_service_provider.legal_name`         | `credentialSubject.legalName`                                |
| `authorized_service_provider.legal_id`           | `authorized_service_provider.legal_id`           | `credentialSubject.legalIdentifier` (`Euid`)                 |
| `authorized_service_provider.network_identifier` | `authorized_service_provider.network_identifier` | `credentialSubject.networkIdentifier` (datatype per scheme)  |
| `authorizing_company.*`                          | `authorizing_company`                            | `credentialSubject.authorizedBy` (`EconomicOperator`, with `legalName`, `legalIdentifier`, `networkIdentifier`) |
| `mandate.service`                                | `mandate.service`                                | `credentialSubject.mandateService`                           |
| `mandate.operations`                             | `mandate.operations`                             | `credentialSubject.mandateOperation`                         |
| `mandate.jurisdiction`                           | `mandate.jurisdiction`                           | `credentialSubject.mandateJurisdiction`                      |
| `authorization_valid_from`                       | `authorization_valid_from`                       | `credentialSubject.authorizationValidFrom`                   |
| `authorization_valid_until`                      | `authorization_valid_until`                      | `credentialSubject.authorizationValidUntil`                  |
| `authorization_reference`                        | `authorization_reference`                        | not included (see selective disclosure above)                |

#### 5.3.2 Illustrative example (informative, fictitious data)

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
    "id": "did:jwk:eyJrdHkiOiJFQyIsImNydiI6IlAtMjU2IiwieCI6IjlVbk1ucEZrdjBhMWkwVmUtdTRaUFJ5azhvTm5VZXRhWWxTUHVUVU9RamsiLCJ5IjoiM2tmeGJ6UDFPVE0zZ3ZORVN5RU9ncU1zaUcwVHhad1F2elBuTVRHcThQWSJ9",
    "type": "EconomicOperator",
    "legalName": "Brabant Access Services N.V.",
    "legalIdentifier": {
      "@type": "Euid",
      "@value": "BEKBOBCE.0890123456"
    },
    "networkIdentifier": {
      "@type": "PeppolAccessPointId",
      "@value": "PBE000123"
    },
    "authorizedBy": {
      "type": "EconomicOperator",
      "legalName": "Green Flowers B.V.",
      "legalIdentifier": {
        "@type": "Euid",
        "@value": "NLNHR.85374628"
      },
      "networkIdentifier": {
        "@type": "PeppolParticipantId",
        "@value": "0106:85374628"
      }
    },
    "mandateService": "einvoicing",
    "mandateOperation": [
      "send",
      "receive"
    ],
    "mandateJurisdiction": "NL",
    "authorizationValidFrom": "2026-01-01",
    "authorizationValidUntil": "2026-12-31"
  }
}
```

The credential reads: *Green Flowers B.V. has mandated Brabant Access Services N.V. to send and
receive its Peppol invoices under the Dutch regime for 2026.* The validity in `validFrom`/`validUntil`
is the technical validity of the credential; `authorizationValidFrom`/`authorizationValidUntil` is the
business validity of the mandate, and IR-ASP-01 applies to both pairs.

## 6 Protocols

### 6.1 Issuance

| Protocol   | Supported | Profile or version                       | Specification        | Notes                                                        |
| ---------- | --------- | ---------------------------------------- | -------------------- | ------------------------------------------------------------ |
| OpenID4VCI | yes       | WE BUILD Conformance Specification cs-01 | [OpenID4VCI], [HAIP] | Credential format `dc+sd-jwt`. A credential format identifier for the W3C VCDM encoding is not yet profiled in cs-01. |

### 6.2 Presentation

| Protocol                   | Supported | Profile or version                             | Specification       | Notes                                                        |
| -------------------------- | --------- | ---------------------------------------------- | ------------------- | ------------------------------------------------------------ |
| OpenID4VP, remote          | yes       | WE BUILD Conformance Specification cs-02, DCQL | [OpenID4VP], [HAIP] | Machine-to-machine. A Relying Party SHOULD constrain its query to the service and jurisdiction it needs, so that a provider holding several mandates presents the right attestation. |
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

The issuer is the authorising company, a legal person self-issuing this EAA through its EBW on the
basis of a service agreement with the Service Provider. Issuance uses OpenID4VCI as profiled by the WE
BUILD Conformance Specification cs-01.

The issuer SHALL issue one attestation per mandate. Where a company mandates the same Service Provider
for several services or jurisdictions, it SHALL issue a separate attestation for each combination of
service and jurisdiction.

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
  delay when the mandate ends, when it moves the mandated service in that jurisdiction to another
  Service Provider, when the mandated operations change (issuing a replacement attestation), or when
  the provider's identity data becomes inaccurate. Because each attestation carries one mandate, a
  change to one mandate SHALL NOT require revoking the company's other mandates.
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
* request the two party objects, `mandate` and the validity attributes, and apply the integrity rules
  IR-ASP-01 to IR-ASP-04 defined in section 4.5. A counterpart Access Point SHALL accept only a
  mandate with service `einvoicing` and the operation in question; a Tax Administration SHALL accept
  only a mandate with service `tax_reporting` and its own Member State as jurisdiction.

Neither SHOULD request `authorization_reference`.

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
participant on the invoice; a Tax Administration confirming the company is a taxable person registered
in its Member State), optionally supported by domain-specific trust list services.

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
| [ISO 3166-1]                           | ISO 3166-1, Codes for the representation of names of countries and their subdivisions, Part 1: Country code |
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
