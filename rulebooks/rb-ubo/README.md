# Attestation Rulebook for attestations of type Ultimate Beneficial Owner (UBO)

Category: S-EAA or QEAA, selected at issuance per integrity rule IR-24 in section 4.5

* Author(s):
  * [Florin Coptil, Robert Bosch GmbH]
  * [Stephan-A Fuchs, Deutsche Bank AG]

* Reviewer(s):
  * [Baumgardt Michaela, Commerzbank]
  * [Bastek-Margo Jenny, Commerzbank]
  * [Fabrizio Notarnicola, Infocameere IT ]
  * [Ricky Lamberty, Robert Bosch GmbH]
  * [ , Bundesanzeiger - TR]

| Version | Date | Description |
| --- | --- | --- |
| 1.1 | 15.09.2026 | Restructured onto the generic WE BUILD attestation rulebook template (11 chapters). No normative content removed. |

**Written against:** ARF version 3.0.0, WE BUILD template version 1.0 (generic)

* Contact:
  * [Florin Coptil](mailto:florin.coptil@bosch.com)
  * [Stephan Fuchs](mailto:stephan-a.fuchs@db.com)  

**Feedback:** [GitHub issues](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/issues), or contact Work Package 4 in WE BUILD.

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
   * [6.1 Issuance](#61-issuance)
   * [6.2 Presentation](#62-presentation)
- [7 Issuance](#7-issuance)
   * [7.1 Binding](#71-binding)
   * [7.2 Issuance Policy](#72-issuance-policy)
   * [7.3 Lifecycle management](#73-lifecycle-management)
   * [7.4 Embedded disclosure policy](#74-embedded-disclosure-policy)
- [8 Revocation](#8-revocation)
- [9 Request, Presentation and Verification](#9-request-presentation-and-verification)
   * [9.1 Relying Party Role ( RP Instance - EUDI Wallet)](#91-relying-party-role--rp-instance---eudi-wallet)
   * [9.2 EBW Relying Party Role ( EBW Wallet - EBW Wallet)](#92-ebw-relying-party-role--ebw-wallet---ebw-wallet)
   * [9.3 Presentation modes](#93-presentation-modes)
   * [9.4 Transactional data](#94-transactional-data)
- [10 Trust Framework](#10-trust-framework)
   * [10.1 Relying Party Role ( RP Instance - EUDI Wallet)](#101-relying-party-role--rp-instance---eudi-wallet)
   * [10.2 EBW Relying Party Role ( EBW Wallet - EBW Wallet)](#102-ebw-relying-party-role--ebw-wallet---ebw-wallet)
- [11 References](#11-references)


## 1 Introduction

This attestation addresses the following question:

**Who are the Ultimate Beneficial Owners (UBOs) of a legal entity, and what is the nature
and extent of their ownership or control?**

A UBO is defined as any natural person who ultimately owns or controls a legal entity based on
AMLR Article 3(17):

- (a) they hold directly or indirectly 25% or more of the units held in the collective
  investment undertaking;
- (b) they have the ability to define or influence the investment policy of the collective
  investment undertaking;
- (c) they control the activities of the collective investment undertaking through other means

### 1.1 Document scope and purpose

The UBO Attestation captures the essential attributes of a natural person who qualifies as an
ultimate beneficial owner of a legal entity — including personal identity, nationality,
residence, and the nature and degree of their ownership or control stake — in a
machine-readable, selectively disclosable format compliant with the EUDI Wallet framework.

**Design Decisions**

This UBO Attestation Rulebook is based on:
- AMLR – Regulation (EU) 2024/1624 of the European Parliament and of the Council of 31 May 2024 on the prevention of the use of the financial system for the purposes of money laundering or terrorist financing.
- The EU Anti-Money Laundering Regulation (AMLR 2024/1624) as the primary regulatory driver for beneficial ownership transparency obligations
- The EUDI Wallet ecosystem and eIDAS 2 framework as the digital identity infrastructure
- The SD-JWT VC specification (draft-ietf-oauth-sd-jwt-vc-09) for verifiable credential
  encoding
- ICAO 9303 for travel document types and number formats
- Regulatory Technical Standards (RTS) – Draft Regulatory Technical Standards under Article 28(1) of Regulation (EU) 2024/1624, specifying the requirements for identifying beneficial owners and the information to be collected for beneficial ownership determination.
- Beneficial Ownership Submission Regulation – Commission on Implementing Regulation (EU) [number] on the formats for submitting beneficial ownership information.
- Beneficial Ownership Data Standard (BODS) version 0.4

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

*Additional terminology specific to this attestation:*

| Term | Description |
| --- | --- |
| UBO | Ultimate Beneficial Owner — a natural person who ultimately owns or controls a legal entity, as defined under AMLR 2024/1624 |
| NaturalPerson | The natural person identified as a UBO, including their personal identity attribute (first name, surname and birth date) |
| BirthPlace | The place of birth of the natural person, including locality and country |
| Citizenship | The nationality or nationalities held by the natural person |
| ResidenceAddress | The registered residential address of the natural person |
| ContactAddress | An optional alternative contact address for the natural person |
| NaturalPersonIdentifier | A government-issued identity document (e.g., passport, national ID card) used to identify the natural person |
| NaturalPersonUniqueIdentifier | An optional unique identifier issued by an authority to uniquely identify the natural person across systems |
| Justification | The object describing how and why the person qualifies as a UBO under applicable AML thresholds and control criteria |
| threshold_met | The applicable AML threshold(s) or control criteria met by the UBO — see Section 2.8.2 |
| ownership_percentage | The total direct and indirect ownership percentage held by the UBO (0–100) |
| voting_rights_percentage | The total direct and indirect voting rights percentage held by the UBO (0–100) |
| control_details | Free text description of control exercised through means other than ownership percentage |
| effective_date | The date from which the UBO status has been effective |
| source | Supporting evidence substantiating the UBO determination |
| KYC | Know Your Customer — due diligence process for verifying customer identity and assessing risk in financial relationships |
| KYS | Know Your Supplier — due diligence process for verifying supplier credentials, integrity, and risk exposure |
| AML | Anti-Money Laundering — regulatory framework requiring financial institutions and obliged entities to identify and report suspicious activity |
| AMLR | Anti-Money Laundering Regulation — EU Regulation 2024/1624 establishing harmonised AML/CFT rules across the EU |
| ISO 3166-1 | International standard defining country codes (alpha-2 and alpha-3 formats) |
| ISO 8601 | International standard for date and time representations (e.g., YYYY-MM-DD) |
| ICAO 9303 | International Civil Aviation Organization standard for travel documents, defining document types and number formats |

## 2 Compliance

This chapter states how this Rulebook complies with the Architecture and Reference
Framework and with the applicable Regulations. Sections 2.1 and 2.2 follow from the
legal category of this attestation. Section 2.3 maps each applicable requirement to
the section that satisfies it.

### 2.1 Compliance statement

This Rulebook complies with the applicable requirements of Topic 12, Attestation
Rulebooks, in Annex 2 of the Architecture and Reference Framework, version 3.0.0.
It uses the terminology of Annex 1 of the ARF.

The attributes specified in this Rulebook comply with [AMLR 2024/1624], in particular
Articles 3, 21, 25, 60 and 62, and with the applicable Regulatory Technical Standards.

### 2.2 Regulatory basis

FIXED

The regulatory basis below is the one applicable to the legal category of this
attestation.

**PID**

This Rulebook specifies how the mandatory and optional person identification data
defined in Tables 1 and 2 of the Annex to CIR (EU) 2024/2977, and the metadata
defined in Table 5 of that CIR, are encoded within the EUDI Wallet ecosystem.

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

**Non-qualified self EAA (S-EAA)** 

> This attestation is a subtype of a non-qualified electronic attestation of attributes.
> From a technical perspective, there is no difference between an EAA and an self EAA.
> The distinction lies primarily in the legal framework, particularly with regard to issuer liability.
> A self EAA is based on information owned or self-asserted by the issuer and
> is issued and used exclusively within a defined closed ecosystem
> and is intended to have no effect on third parties.
> Where Article 2(2) eIDAS applies, the service falls outside the scope of eIDAS;
> consequently, the eIDAS TSP liability regime does not apply, and
> liability is governed by applicable contractual and national law.

**EBWOID**

> TO AGREE. Do not assert qualified status unless the issuer is a QTSP, and do not
> cite Annex V or Annex VII by default.

### 2.3 Traceability

Every applicable requirement mapped to the section that satisfies it. Requirements
marked not applicable carry a stated reason. The Applies column records where a
requirement bites only in one of the two legal categories.

| Requirement | Legacy ID | Applies | Satisfied in section | Note |
| --- | --- | --- | --- | --- |
| EW-DM-12-001 | ARB_01a | yes, EAA only | 5 | W3C VCDM permitted for non-qualified EAA; no encoding defined in this version |
| EW-DM-12-002 | ARB_01b | yes | 5 | SD-JWT VC following the HAIP profile |
| EW-DM-12-003 | ARB_02 | no |  | Proximity presentation is not in scope; mdoc is out of scope per section 5.2 |
| EW-DM-12-005 | ARB_04 | no |  | No W3C VCDM encoding is defined in this version |
| EW-DM-12-006 | ARB_05 | yes | 5 | Unique `vct` for this attestation type |
| EW-DM-12-007 | ARB_06 | yes | 3 | Attributes defined independently of encoding |
| EW-DM-12-008 | ARB_06a | no |  | No mdoc encoding is defined in this version |
| EW-DM-12-009 | ARB_06b | yes | 5.1 | SD-JWT VC claim naming |
| EW-DM-12-010 | ARB_07 | yes | 3 | Attributes aligned to the AMLR and the BOS vocabulary |
| EW-DM-12-012 | ARB_09 | yes | 3, 4 | Mandatory, optional and conditional stated per attribute |
| EW-DM-12-013 | ARB_10 | no |  | No domestic namespace is defined |
| EW-DM-12-014 | ARB_11 | yes, QEAA only | 2.2, 4.1 | Annex V point a, via `attestation_legal_category` |
| EW-DM-12-015 | ARB_12 | yes, EAA only | 4.1 | EAA indication for a non-qualified EAA |
| EW-DM-12-016 / EW-DM-12-017 / EW-DM-12-018 | ARB_13 / ARB_14 / ARB_15 | yes | 2.2, 4.1 | Point b; EW-DM-12-016 in the qualified case, EW-DM-12-018 otherwise |
| EW-DM-12-019 / EW-DM-12-020 | ARB_16 / ARB_17 | yes | 2.2 | Point c, by category |
| EW-DM-12-021 / EW-DM-12-022 | ARB_18 / ARB_19 | yes | 2.2, 4.2 | Point e, by category |
| EW-DM-12-023 / EW-DM-12-024 | ARB_20 / ARB_21 | yes | 4.1, 10 | `trust_anchor_url` and the trust framework |
| EW-DM-12-029 | ARB_25 | yes | 4.1 | Legal category attribute; see the note in section 4.1 |
| EW-DM-12-030 | ARB_26 | yes, EAA only | 10 | Trust anchor publication for non-qualified EAA, via the EBWOID chain |
| EW-DM-12-031 | ARB_27 | no |  | This attestation does not require the Relying Party to verify a PID |
| EW-DM-12-032 | ARB_28 | no |  | `cryptographically_bound_to` is not used by this attestation |
| EW-DM-12-034 | ARB_30 | yes | 5.1 | Selective disclosure stated per claim |
| EW-DM-12-035 | ARB_31 | no |  | No Claim Selective Disclosure Metadata document is used |
| EW-DM-12-038 | ARB_34 | yes | 7.1 | Device binding |

*A non-qualified self EAA answers these rows as a non-qualified EAA (EW-DM-12-015, -018, -020, , -024 and -030).

## 3 Attestation attributes

The Ultimate Beneficial Owner (UBO) Attestation provides a standardized, verifiable
representation of the natural persons who ultimately own or control a legal entity. It enables
structured and trusted exchange of beneficial ownership data between organizations for use in
KYS (Know Your Supplier), KYC (Know Your Customer), Anti-Money Laundering (AML) compliance,
supplier onboarding, and regulatory due diligence processes.

Attributes are defined here in an encoding-independent manner (EW-DM-12-007). The
authoritative encoding lives in the machine-readable schema artefacts referenced in
section 3.1, not in this document. Do not paste schema fragments into the prose,
they will drift.

### 3.1 Introduction

This UBO  Attestation Rulebook is specifically designed to comply with AMLR 2024/1624:
*Article 3(17) – Definition of Beneficial Owner:*
*Article 60 – Beneficial Ownership Registers:*
*Article 62 – Beneficial Ownership Information Requirements:*

The names of attributes is based on the : Beneficial Ownership Submission Regulation – Commission on Implementing Regulation (EU) [number] on the formats for submitting beneficial ownership information.
because the company need to provided to the TR, then provided to the Bank 
and the Bank need to check it afterwards into TR.
**Data Model:*

The UBO model follows a hierarchical structure:
```
UBO [1...n]
├─ jurisdiction (tstr) (M)
├─ person (Object) (M)
│   ├─ first_name (tstr) (M)      
│   ├─ surname (tstr) (M)
│   ├─ birth_date (date) (M)      
├─ birth_place (Object) (M)
│   ├── locality (M)
│   ├── country (M)
│   └── region (O)
├─ citizenship
│   └── citizenship(s) [1..n] (M)
├─ residential_address (Object)(M)
│   ├── street (M)
│   ├── house_number (M)
│   ├── locality (M)
│   ├── region (M)
│   ├── postal_code (M)
│   └── country (M)
├─ contact_address (Object) (O)
│   ├── street (M)
│   ├── house_number (M)
│   ├── locality (M)
│   ├── region (M)
│   ├── postal_code (M)
│   └── country(s)
├─ person_identifier (Object) M
│   ├── document_type (M)
│   ├── document_number (M)
│   ├── issuing_country (M)
│   └── expiry_date (M)
├─ person_unique_identifier (Object) (O)
│   ├── identifier_unique (O)
│   └── identifier_issuing_authority (O)
├─ justification (Object) (M)                           // How this person qualifies as UBO
│   ├─ threshold_met (Array of enum) (M)       // e.g., "ownership_25_plus", "control_voting_25_plus", "control_management"
│   ├─ ownership_percentage (Decimal) (M)      // Total direct/indirect ownership percentage
│   ├─ voting_rights_percentage (Decimal) (M)  // Total direct/indirect voting rights percentage
│   └─ control_details (tstr) (O)              // Free text if control is via other means
├─ effective_date (date) (M)                   // Date when this UBO status became effective
└─ evidence [1..n] (M)                         // At least one evidence entry required
│  ├─ id (tstr) (M)                            // Unique identifier, URI, or URN
│  ├─ type (tstr) (M)                          // Evidence type — see Section 2.8.9
│  ├─ url (uri) (O)                            // URI to publicly accessible source document
│  └─ data (base64) (O)                        // Base64-encoded — required if url absent
```
*Note*: M - mandatory / O - optional.

**Explanation:**
- The attestation **MAY** contain one or more UBO entries (`[1...n]`), one per identified
  ultimate beneficial owner.
- `person`, `birth_place`, `citizenship`, `residential_address`, `person_identifier`,
  and `justification` are mandatory objects within each UBO entry.
- `contact_address` and `person_unique_identifier` are optional objects.
- `citizenship` **SHALL** contain at least one citizenship entry and **MAY** contain multiple
  entries for persons holding multiple nationalities.
- `threshold_met` **SHALL** contain at least one value from the enumerated list in
  Section 2.8.2 and **MAY** contain multiple values where multiple thresholds apply.
- `ownership_percentage` and `voting_rights_percentage` are expressed as decimal values
  between 0 and 100.
- `source` **SHALL** contain at least one entry; if `source.url` is not a publicly accessible
  URI, `source.data` (base64) **SHALL** be provided.

**Attestation Classification:**

This attestation type MAY be classified as:

- **`EAA`** self-issued by the legal entity as part of its Ultimate Beneficial Owner (UBO) disclosure obligations.
- **`QEAA`** issued by a Qualified Trust Service Provider (QTSP) or an authorized competent body (e.g., a notary, commercial register authority, or AML-supervised entity).
  body (e.g., a notary, commercial register authority or AML-supervised entity).
  Is the obligation of the QTSP to
  - verify that the calculated UBO data is fully available
  - cross-check the calculations against the TR record

**Attribute Overview:**

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data Type** |
| --- | --- | --- | --- |
| `person` | — | Personal identity attributes of the UBO | Object |
| `birth_place` | — | Place of birth of the UBO | Object |
| `citizenship` | - | Citizenship(s) held by the UBO (one or more nationalities) | Array of Strings (ISO 3166-1 alpha-2) |
| `residential_address` | — | Registered residential address of the UBO | Object |
| `contact_address` | — | Optional alternative contact address of the UBO | Object |
| `person_identifier` | — | Government-issued identity document details of the UBO | Object |
| `person_unique_identifier` | — | Optional unique identifier assigned by an authority | Object |
| `justification` | — | How and why this person qualifies as UBO under AMLR | Object |
| `source` | — | Supporting evidence for the UBO determination | Array of Objects |

The machine-readable schema artefact for this attestation is:

| Format | Identifier | Schema artefact | Version | Location |
| --- | --- | --- | --- | --- |
| SD-JWT VC | `vct` as recorded in section 5.1 | JSON schema | 0.4.0 per its `$id` | `data-schemas/sd-jwt/ubo-sd-jwt.json` |

Sample data is at `data-schemas/sd-jwt/sample-data/ubo-sd-jwt-sample.json`.

> **Two points on the artefact.** It carries no `version` member, and the version in
> its `$id` is 0.4.0 while this Rulebook is at 1.1. Those should be reconciled. The
> schema also defines `jti`, which this Rulebook does not document.

### 3.2 Mandatory attributes

Attributes that SHALL be present in every attestation of this type.

#### Person Attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data Type** |
| --- | --- | --- | --- |
| `first_name` | — | First name(s) / given name(s) of the natural person, including middle names where applicable | String |
| `surname` | — | Surname(s) / family name(s) of the natural person | String |
| `birth_date` | — | Date of birth of the natural person (ISO 8601 YYYY-MM-DD) | String (ISO 8601) |

#### BirthPlace Attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data Type** |
| --- | --- | --- | --- |
| `locality` | — | City or locality of birth | String |
| `country` | — | Country of birth (ISO 3166-1 alpha-2) | String (ISO 3166-1) |

#### Citizenship Attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data Type** |
| --- | --- | --- | --- |
| `citizenship` | — | Nationality or nationalities held by the natural person; SHALL use ISO 3166-1 alpha-2 codes; SHALL contain at least one entry | Array of Strings [1..n] |

#### ResidentialAddress Attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data Type** |
| --- | --- | --- | --- |
| `street` | — | Street name of the residential address | String |
| `house_number` | — | House or building number of the residential address | String |
| `locality` | — | City or locality of the residential address | String |
| `region` | — | Region or state of the residential address | String |
| `postal_code` | — | Postal code of the residential address | String |
| `country` | — | Country of the residential address (ISO 3166-1 alpha-2) | String (ISO 3166-1) |

#### PersonIdentifier Attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data Type** |
| --- | --- | --- | --- |
| `document_type` | — | Type of identity document — SHALL use values from Section 2.8.1 | String (Enum) |
| `document_number` | — | Number of the identity document as printed on the document | String |
| `issuing_country` | — | Country that issued the identity document (ISO 3166-1 alpha-2) | String (ISO 3166-1) |
| `expiry_date` | — | Expiry date of the identity document (ISO 8601 YYYY-MM-DD) | String (ISO 8601) |

#### Justification Attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data Type** |
| --- | --- | --- | --- |
| `threshold_met` | — | Array of applicable AML thresholds or control criteria met — SHALL use values from Section 2.8.2 — at least one value required | Array of Strings (Enum) |
| `ownership_percentage` | — | Total direct and indirect ownership percentage held (0–100) | Decimal |
| `voting_rights_percentage` | — | Total direct and indirect voting rights percentage held (0–100) | Decimal |

#### Source Attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data Type** |
| --- | --- | --- | --- |
| `id` | — | Unique identifier for the source document | String |
| `type` | — | Type of source document (e.g., `"Evidence"`, `"Register"`, `"TrustDeed"`) | String |

#### UBO Mandatory Attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data Type** |
| --- | --- | --- | --- |
| `effective_date` | — | Date when this ownership or control relationship became legally effective — ISO 8601 YYYY-MM-DD | Date |
| `evidence` | — | At least one piece of supporting evidence substantiating the declared ownership or control | Array [Object] |

### 3.3 Optional attributes

Attributes the Provider MAY include at its discretion.

#### BirthPlace Optional Attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data Type** |
| --- | --- | --- | --- |
| `region` | — | Region or state of birth — optional | String |

#### ContactAddress Attributes *(entire object is optional)*

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data Type** |
| --- | --- | --- | --- |
| `street` | — | Street name of the contact address | String |
| `house_number` | — | House or building number of the contact address | String |
| `locality` | — | City or locality of the contact address | String |
| `region` | — | Region or state of the contact address | String |
| `postal_code` | — | Postal code of the contact address | String |
| `country` | — | Country of the contact address (ISO 3166-1 alpha-2) | String (ISO 3166-1) |

#### PersonUniqueIdentifier Attributes *(entire object is optional)*

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data Type** |
| --- | --- | --- | --- |
| `identifier_unique` | — | A unique identifier assigned to the natural person by an issuing authority | String |
| `identifier_issuing_authority` | — | The authority that issued the unique identifier | String |

#### Justification Optional Attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data Type** |
| --- | --- | --- | --- |
| `control_details` | — | Free text description of control exercised through means other than ownership percentage | String |

#### Source Optional Attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data Type** |
| --- | --- | --- | --- |
| `url` | — | URI reference to the source or evidence document | URI |
| `data` | — | Base64-encoded source document — SHALL be provided if `url` is not a publicly accessible URI | String (base64) |

### 3.4 Conditional attributes

Attributes required only when a stated condition holds. State the condition
explicitly in the definition, not in a footnote.

| **Data Identifier** | **Condition** | **Definition** | **Data Type** |
| --- | --- | --- | --- |
| `source.data` | **SHALL** be provided if `source.url` is not a publicly accessible URI | Base64-encoded evidence document | String (base64) |
| `justification.control_details` | **SHALL** be provided if `threshold_met` includes `"control_other_means"` | Free text description of other means of control | String |
| `justification.ownership_percentage` | **SHOULD** be provided if `threshold_met` includes `"ownership_25_plus"` | Total ownership percentage | Decimal |
| `justification.voting_rights_percentage` | **SHOULD** be provided if `threshold_met` includes `"control_voting_25_plus"` | Total voting rights percentage | Decimal |

## 4 Metadata

Metadata describes the attestation rather than its subject.

### 4.1 Mandatory metadata

*Note*: Only the additional mandatory attributes are listed; the mandatory attributes defined by the protocol are not specified.

| **Data Identifier** | **Semantic reference**|**Definition** |**Data type**| **Example value** |                   
| --- |-----------------------------------------------------------| --- | -- |-------------------|
| attestation_legal_category | |Indicates the legal category of the Attestation | String | S-EAA , QEAA      |
| cnf | | cryptographic Key Binding                                  | String |                   |

### 4.2 Optional metadata

| **Data Identifier** | **Definition** | **Data type** |
| --- | --- | --- |
| trust_anchor_url | URL where the trust anchor for verifying this attestation can be retrieved | URI |
| schema_version | Version of the schema used for this attestation | String |

### 4.3 Conditional metadata

No conditional metadata elements are defined for this attestation type.

### 4.4 Code lists

#### 4.4.1 Document Type Codes

The `person_identifier.document_type` attribute SHALL use one of the following standardised
values, aligned with ICAO 9303:

| **Code** | **Definition** |
| --- | --- |
| `PASSPORT` | International passport as defined by ICAO 9303 |
| `NATIONAL_ID` | National identity card issued by a competent authority |
| `RESIDENCE_PERMIT` | Residence permit issued to foreign nationals |
| `DRIVING_LICENSE` | Driving licence accepted as an identity document |
| `OTHER` | Any other government-issued identity document |

#### 4.4.2 Threshold Met Codes

The `justification.threshold_met` attribute SHALL use one or more of the following
standardised values, aligned with AMLR Article 3(17):

**a) Ownership-Based Thresholds:**

| **Code** | **Definition** |
| --- | --- |
| `ownership_25_plus` | The UBO holds ≥25% of shares or ownership interests directly or indirectly in the subject entity |
| `ownership_direct` | The UBO holds ≥25% through direct shareholding without intermediary entities |
| `ownership_indirect` | The UBO holds ≥25% through one or more intermediary legal entities |

**b) Voting Rights-Based Thresholds:**

| **Code** | **Definition** |
| --- | --- |
| `control_voting_25_plus` | The UBO holds ≥25% of voting rights directly or indirectly |
| `control_voting_direct` | The UBO holds ≥25% of voting rights through direct shareholding |
| `control_voting_indirect` | The UBO holds ≥25% of voting rights through intermediary entities |

**c) Management / Other Control:**

| **Code** | **Definition** |
| --- | --- |
| `control_management` | Control exercised through appointment of senior management or the board |
| `control_veto` | Control exercised through veto rights over major corporate decisions |
| `control_contractual` | Control exercised through formal or informal contractual agreements |
| `control_family_relationships` | Control exercised through coordinated action among family members |
| `control_acting_in_concert` | Control exercised through acting in concert with other shareholders |
| `control_nominee` | Control exercised through nominee arrangements |
| `control_other_means` | Control exercised through other means not explicitly listed above |

**d) Legal Arrangement Roles** *(for trusts, foundations, and similar structures):*

| **Code** | **Definition** |
| --- | --- |
| `arrangement_settlor` | The UBO is the settlor (creator) of a trust or similar legal arrangement |
| `arrangement_trustee` | The UBO is the trustee of a trust or similar legal arrangement |
| `arrangement_beneficiary` | The UBO is a beneficiary of a trust or similar legal arrangement |
| `arrangement_protector` | The UBO is the protector of a trust or similar legal arrangement |
| `arrangement_object_of_power` | The UBO is the object of a power in a legal arrangement |
| `arrangement_default_taker` | The UBO is the default taker (residual beneficiary) of a legal arrangement |
| `arrangement_other_control` | Any other natural person exercising ultimate control over the legal arrangement |

> **Note:** Multiple `threshold_met` values MAY apply to a single UBO. For example, a UBO
> may be identified through `"ownership_25_plus"` (35% direct shareholding) AND
> `"control_voting_25_plus"` (50% voting rights via special shares) AND
> `"control_management"` (contractual right to appoint the CEO).

#### 4.4.3 Country Codes

All `country`, `issuing_country`, and `citizenship` attributes SHALL use
**ISO 3166-1 alpha-2** two-letter country codes.

For a complete list, refer to the [ISO 3166-1 standard](https://www.iso.org/iso-3166-country-codes.html).

#### 4.4.4 Date Formats

All date attributes SHALL follow the **ISO 8601 YYYY-MM-DD** format.

#### 4.4.5 Source Type Codes

The `source.type` attribute SHOULD use one of the following standardised values:

| **Code** | **Definition** |
| --- | --- |
| `ShareRegister` | Official shareholder register extract |
| `CommercialRegister` | Extract from a national commercial or company register |
| `TransparencyRegister` | Entry from an official beneficial ownership / transparency register |
| `TrustDeed` | Trust deed or instrument establishing a legal arrangement |
| `ShareholderAgreement` | Shareholders' agreement evidencing ownership structure |
| `ArticlesOfAssociation` | Articles of association defining share structure |
| `GovernanceChart` | Organisational or governance chart showing ownership structure |
| `AMLOfficerDeclaration` | Declaration by an AML-supervised officer or compliance function |
| `NotarialDeed` | Notarially certified document evidencing ownership |
| `Other` | Any other supporting evidence document |

### 4.5 Integrity rules

The following integrity rules SHALL be enforced:

| **Rule ID** | **Rule** |
| --- | --- |
| IR-01 | The `ubo` array SHALL contain at least one UBO entry |
| IR-02 | Each UBO entry SHALL contain exactly one `person`, `birth_place`, `citizenship`, `residential_address`, `person_identifier`, `justification`, and `source` |
| IR-03 | `person.first_name` SHALL be a non-empty string |
| IR-04 | `person.surname` SHALL be a non-empty string |
| IR-05 | `person.birth_date`, if present, SHALL be a valid ISO 8601 date (YYYY-MM-DD) in the past |
| IR-06 | `birth_place.locality` SHALL be a non-empty string |
| IR-07 | `birth_place.country` SHALL be a valid ISO 3166-1 alpha-2 country code |
| IR-08 | `citizenship` SHALL contain at least one valid ISO 3166-1 alpha-2 country code |
| IR-09 | All mandatory address fields (`street`, `house_number`, `locality`, `region`, `postal_code`, `country`) within `residential_address` SHALL be non-empty |
| IR-10 | `residential_address.country` SHALL be a valid ISO 3166-1 alpha-2 country code |
| IR-11 | If `contact_address` is present, all its mandatory fields SHALL be non-empty |
| IR-12 | `person_identifier.document_type` SHALL use one of the enumerated values from Section 2.8.1 |
| IR-13 | `person_identifier.document_number` SHALL be a non-empty string |
| IR-14 | `person_identifier.issuing_country` SHALL be a valid ISO 3166-1 alpha-2 country code |
| IR-15 | `person_identifier.expiry_date` SHALL be a valid ISO 8601 date (YYYY-MM-DD) |
| IR-16 | `justification.threshold_met` SHALL contain at least one value from Section 2.8.2 |
| IR-17 | `justification.ownership_percentage` and `justification.voting_rights_percentage`, SHALL each be a decimal value between 0 and 100 inclusive |
| IR-18 | `justification.control_details` SHALL be present if `threshold_met` contains `"control_other_means"` |
| IR-19 | `effective_date` SHALL be a valid ISO 8601 date (YYYY-MM-DD) in the past |
| IR-20 | `source` SHALL contain at least one entry |
| IR-21 | If `source.url` is not a publicly accessible URI, `source.data` (base64) SHALL be provided |
| IR-22 | `issuance_date` and `expiry_date` (metadata) SHALL be valid ISO 8601 DateTimes |
| IR-23 | `expiry_date` (metadata) SHALL be later than `issuance_date` |
| IR-24 | `attestation_legal_category` SHALL be one of `"EAA"` or `"QEAA"` |
| IR-25 | `vct` SHALL be `"eu.we-build:ubo:1"` |
| IR-26 | `jurisdiction` SHALL be a valid ISO 3166-1 alpha-2 country code |

## 5 Formats

| Format | Supported | Identifier | Specification | Notes |
| --- | --- | --- | --- | --- |
| ISO/IEC 18013-5 mdoc | no |  | [ISO/IEC 18013-5] | Out of scope, see section 5.2 |
| SD-JWT VC | yes | `vct` as recorded in section 5.1 | [SD-JWT VC], [HAIP] |  |
| W3C VCDM | no |  |  | Not defined in this version, see section 5.3 |

### 5.1 SD-JWT VC-based encoding

The UBO Attestation uses the SD-JWT VC format to allow for selective disclosure of UBO
attributes.

**Selective Disclosure:** Claims within each UBO entry SHALL be individually selectively
disclosable, enabling a legal entity to disclose only the attributes requested by a Relying
Party. Sensitive personal attributes such as `birth_date`, `document_number`, and address
details SHALL be individually disclosable.

The `.` notation is used to indicate the nesting of attributes.

**Verifiable Credential Type (`vct`):** `eu.we-build:ubo:1`

#### Attribute Encoding Table

| **Data Identifier** | **Attribute Identifier** | **Encoding Format** | **Reference / Notes** | **Disclosable** |
| --- | --- | --- | --- | --- |
| `ubo` | `ubo` | Array [UBO] | SHALL contain at least one UBO entry | MUST |
| `jurisdiction` | `ubo[n].jurisdiction` | String (ISO 3166-1 alpha-2) | Jurisdiction of the subject entity — SHALL be non-empty | MUST |
| **Person** |  |  |  |  |
| `first_name` | `ubo[n].person.first_name` | String | First name(s) of the natural person — SHALL be non-empty | MUST |
| `surname` | `ubo[n].person.surname` | String | Surname(s) of the natural person — SHALL be non-empty | MUST |
| `birth_date` | `ubo[n].person.birth_date` | String (ISO 8601 YYYY-MM-DD) | Date of birth — SHALL be in the past; optional | MAY |
| **BirthPlace** |  |  |  |  |
| `locality` | `ubo[n].birth_place.locality` | String | City or locality of birth — SHALL be non-empty | MUST |
| `country` | `ubo[n].birth_place.country` | String (ISO 3166-1 alpha-2) | Country of birth — SHALL be non-empty | MUST |
| `region` | `ubo[n].birth_place.region` | String | Region or state of birth — optional | MAY |
| **Citizenship** |  |  |  |  |
| `citizenship` | `ubo[n].citizenship` | Array of Strings (ISO 3166-1 alpha-2) | Citizenship(s) — SHALL contain at least one entry | MUST |
| **ResidentialAddress** |  |  |  |  |
| `street` | `ubo[n].residential_address.street` | String | Street name — SHALL be non-empty | MUST |
| `house_number` | `ubo[n].residential_address.house_number` | String | House number — SHALL be non-empty | MUST |
| `locality` | `ubo[n].residential_address.locality` | String | City or locality — SHALL be non-empty | MUST |
| `region` | `ubo[n].residential_address.region` | String | Region or state — SHALL be non-empty | MUST |
| `postal_code` | `ubo[n].residential_address.postal_code` | String | Postal code — SHALL be non-empty | MUST |
| `country` | `ubo[n].residential_address.country` | String (ISO 3166-1 alpha-2) | Country — SHALL be non-empty | MUST |
| **ContactAddress** *(optional object)* |  |  |  |  |
| `street` | `ubo[n].contact_address.street` | String | Street name of the contact address — optional | MAY |
| `house_number` | `ubo[n].contact_address.house_number` | String | House number of the contact address — optional | MAY |
| `locality` | `ubo[n].contact_address.locality` | String | Locality of the contact address — optional | MAY |
| `region` | `ubo[n].contact_address.region` | String | Region of the contact address — optional | MAY |
| `postal_code` | `ubo[n].contact_address.postal_code` | String | Postal code of the contact address — optional | MAY |
| `country` | `ubo[n].contact_address.country` | String (ISO 3166-1 alpha-2) | Country of the contact address — optional | MAY |
| **PersonIdentifier** |  |  |  |  |
| `document_type` | `ubo[n].person_identifier.document_type` | String (Enum) | SHALL use values from Section 2.8.1 | MUST |
| `document_number` | `ubo[n].person_identifier.document_number` | String | Document number as printed on the document — SHALL be non-empty | MUST |
| `issuing_country` | `ubo[n].person_identifier.issuing_country` | String (ISO 3166-1 alpha-2) | Country that issued the document — SHALL be non-empty | MUST |
| `expiry_date` | `ubo[n].person_identifier.expiry_date` | String (ISO 8601 YYYY-MM-DD) | Expiry date of the document | MUST |
| **PersonUniqueIdentifier** *(optional object)* |  |  |  |  |
| `identifier_unique` | `ubo[n].person_unique_identifier.identifier_unique` | String | Unique identifier assigned by an authority — optional | MAY |
| `identifier_issuing_authority` | `ubo[n].person_unique_identifier.identifier_issuing_authority` | String | Authority that issued the unique identifier — optional | MAY |
| **Justification** |  |  |  |  |
| `threshold_met` | `ubo[n].justification.threshold_met` | Array of Strings (Enum) | SHALL use values from Section 2.8.2 — at least one value required | MUST |
| `ownership_percentage` | `ubo[n].justification.ownership_percentage` | Decimal (0–100) | Total direct/indirect ownership percentage — optional | MAY |
| `voting_rights_percentage` | `ubo[n].justification.voting_rights_percentage` | Decimal (0–100) | Total direct/indirect voting rights percentage — optional | MAY |
| `control_details` | `ubo[n].justification.control_details` | String | Free text for other means of control — required if `threshold_met` includes `"control_other_means"` | MAY |
| **Effective Date** |  |  |  |  |
| `effective_date` | `ubo[n].effective_date` | String (ISO 8601 YYYY-MM-DD) | Date when UBO status became effective — SHALL be non-empty | MUST |
| **Source** |  |  |  |  |
| `id` | `ubo[n].source[m].id` | String | Unique source identifier — SHALL be non-empty | MUST |
| `type` | `ubo[n].source[m].type` | String | Type of source — SHOULD use values from Section 2.8.5 | MUST |
| `url` | `ubo[n].source[m].url` | URI | URI reference to source document — optional | MAY |
| `data` | `ubo[n].source[m].data` | String (base64) | Base64-encoded source — required if `url` not publicly accessible | MAY |
| **Metadata** |  |  |  |  |
| `issuance_date` | `iat` | Number (Unix timestamp) | Date and time when the attestation was issued (ISO 8601); RFC 7519 | MUST NOT |
| `expiry_date` | `exp` | Number (Unix timestamp) | Date and time when the attestation expires (ISO 8601); RFC 7519 | MUST NOT |
| `issuing_entity` | `iss` | String (URI or DID) | Identifier of the competent institution that issued the attestation; RFC 7519 | MUST NOT |
| `attestation_legal_category` | `attestation_legal_category` | String | One of "EAA" or "QEAA" as defined by eIDAS 2 | MUST NOT |
| `vct` | `vct` | String | The vct definition | MUST NOT |
| `cnf` | `cnf` | String | Cryptographic Key Binding | MUST NOT |
| `schema_version` | `schema_version` | String | Version of the schema used; optional | MAY |
| `trust_anchor_url` | `trust_anchor_url` | String (URI) | URL where the trust anchor for verifying this attestation can be retrieved; optional | MAY |

**Notes:**

- **MUST**: The claim SHALL be selectively disclosable — the holder MAY choose to disclose or
  withhold this claim when presenting the credential to a Relying Party.
- **MAY**: The claim MAY be selectively disclosable if the issuer supports it.
- **MUST NOT**: The claim SHALL NOT be selectively disclosable — it is always present in plain
  text in the JWT header/payload.
- `ubo` entries are indexed as `[n]` where `n` starts at `0`; at least one UBO entry SHALL be
  present.
- `source` entries within each UBO are indexed as `[m]` where `m` starts at `0`; at least one
  source entry SHALL be present per UBO.
- `iat`, `exp`, and `iss` follow RFC 7519 standard JWT claim naming conventions.

### 5.2 ISO/IEC 18013-5-compliant encoding

**out of scope** for this Rulebook

### 5.3 W3C Verifiable Credentials Data Model-based encoding
**out of scope** for this Rulebook

## 6 Protocols

### 6.1 Issuance

The UBO Attestation is issued using OpenID for Verifiable Credential Issuance
[OpenID4VCI], as profiled by [HAIP].

### 6.2 Presentation

The UBO Attestation is presented using OpenID for Verifiable Presentations
[OpenID4VP]. Only remote presentation is in scope, consistent with chapter 5, which
records the mdoc encoding as out of scope.

## 7 Issuance

### 7.1 Holder Key Binding at Issuance (Wallet Binding)

This is a fundamental security requirement that prevents credential theft and ensures an attestation is bound to a specific wallet. 
**What it is:** Where the attestation is device-bound (see table below), the Holder's wallet **MUST** perform a "proof-of-possession" challenge to prove it controls a specific private key. The Attestation Provider then embeds the corresponding public key into the attestation payload before signing it.
**Why it matters:** This process creates a permanent, cryptographic link between the attestation and the Holder's wallet. During presentation (as described in Chapter 9), a Relying Party can then challenge the presenting wallet to prove it still controls that same private key. This verification step makes stolen or copied attestation files useless to a thief, as they will not have the required private key.

| Field | Value | Source |
| --- | --- | --- |
| Device-bound | MAY | EW-DM-12-038 |
| Cryptographically bound to | none | EW-DM-12-032 |
| Relying Party must also verify a PID | no | EW-DM-12-031 |
| Binding subject | legal person, the entity whose beneficial owners are attested | [AMLR 2024/1624] Article 62 |

Holder binding is expressed through the `cnf` claim recorded in section 4.1, where it
is used.

### 7.2 Issuance Policy

An Issuance Policy defines the minimum rules, policies, and procedures that any compliant Attestation Provider **SHALL** follow when issuing attestations of this type. 
For transparency and to allow Relying Parties to programmatically assess their trust in the attestation, each Attestation Provider **SHALL** publish their terms and conditions, a generic Trust Services Policy, and an EAA Policy (per attestation type) in accordance with **[ETSI TS 119 471]**. These policies must be accepted by the Holder upon receipt of the attestation.
This section references key concepts from **[ETSI TS 119 471]** and **[ETSI TS 119 461]**. The most critical issuance concepts for a rulebook author to understand and specify are explained below:

#### **1. Core Issuer Obligations**

Any entity acting as an authorized Attestation Provider under this rulebook **SHALL** comply with the following general obligations:
**Issuance Basis and Timestamping:** The Provider **SHALL** issue the attestation based on information and supporting documentation that is valid and accurate at the exact moment of issuance. A timestamp of issuance (iat in SD-JWT VC) **MUST** be included in each attestation. This enables a Relying Party to not only verify the attestation's temporal validity but also to correctly validate the Attestation Provider's trust status as it was at the moment of issuance (e.g., by checking against a historical Trust List).
**Data Currency and Revocation:** The Provider is responsible for the ongoing accuracy of the attested information. The Provider **MUST** immediately revoke the attestation if any change occurs that affects the validity or accuracy of the underlying data.

#### **2. Identity and Attribute Proofing (as per ETSI TS 119 461)**

This refers to the rigor with which the Attestation Provider verifies the information before issuing the attestation. The level of trust a Relying Party can place in an attestation depends directly on the quality of this proofing process.
**Identity Proofing:** This is the process of verifying the identity of the subject. For example, for registered legal entities in a national register, this **MUST** involve verifying its active registration in the respective register.
**Attribute Proofing:** This is the process of verifying the specific claims (attributes) being attested. The Provider **MUST** verify the attributes against a designated authentic data source (as defined by the author below).

#### **3. Architectural Pattern for EAA Provider Trust**
To enable the EAA Provider to implement the basic verification steps described in Chapter 9, the following general issuer obligations apply to all EAA Providers:
* EAA Provider SHALL make the key it signs with verifiable through the trust framework of chapter 10.
* Issuer obligation differ for the different trust mechanisms

##### Attestation Chaining (Issuer Component with Access Certificate)
1.  **Provider Identity Credential:** The EAA Provider **MUST** possess an **Access Certificate** issued by a Qualified Trust Service Provider (QTSP). This certicate already contain a `signing_key` parameter holding the public key the Provider uses to sign the issued EAAs. 
2.  **Trust Chaining Mechanism:** The EAA Provider **MUST** include their access certificate in the header of every EAA they issue. This allows a Relying Party to verify the EAA signature using the public key from the embedded access certificate and then verify the access certificate itself against the eIDAS Trusted List.

###### Attestation Chaining (EBW with EBWOID) 
1.  **Provider Identity Credential:** The EAA Provider **MUST** possess their own European Business Wallet Owner Identity (EBWOID), issued by a Qualified Trust Service Provider (QTSP). To be authorized to sign and issue other EAAs, this EBWOID **MUST** contain a `signing_key` parameter holding the public key the Provider uses to sign the issued EAAs. 
2.  **Trust Chaining Mechanism:** The EAA Provider **MUST** include their own EBWOID (or a reference/chain to it) in the header of every EAA they issue. This allows a Relying Party to verify the EAA signature using the public key from the embedded EBWOID, and then verify the EBWOID itself against the eIDAS Trusted List.

##### QSEAL
[to be described]

##### to be defined according to ADR#336
[to be described]

#### **4. Batch Issuance (Protocol Optimization)**
This is a technical efficiency and privacy feature defined in the underlying OpenID4VCI protocols.
**What it is:** A technical capability allowing a Wallet to request, and an Attestation Provider to issue, multiple credentials simultaneously in a single API interaction, rather than requiring separate network connections for each credential.
**Application to this Rulebook:** For unique, long-lived business attestations, batch issuance is typically **Optional** or **Not Applicable**, as these credentials do not require multi-copy anonymity and are issued on a one-off basis.

When issuing a UBO Attestation, the Issuer SHALL comply with the following obligations.

#### UBO Determination
The legal entity SHALL determine its Ultimate Beneficial Owner(s) (UBOs) by:
- applying the ≥25% ownership threshold to the Ownership List to identify natural persons holding, directly or indirectly, at least 25% ownership;
- analysing the Control List to identify natural persons exercising ultimate control through other means, irrespective of ownership percentage; and
- applying the applicable AMLR methodologies for determining direct ownership, indirect ownership, legal arrangement roles, and other forms of control.

### 7.3 Lifecycle management

- The attestation is issued by the legal entity itself in the EAA case, or by a QTSP
  or authorised competent body in the QEAA case, as recorded in section 7.3.
- Revocation and suspension triggers are recorded in chapter 8.
- Where beneficial ownership changes, a superseding attestation is issued and the
  previous one revoked, as described in chapter 8.

### 7.4 Embedded disclosure policy

This attestation defines no embedded disclosure policy.

## 8 Revocation

An attestation SHALL remain valid only while its underlying information is accurate, complete, and legally effective.

**Revocation Mechanism**
- Token Status List: The issuer must maintain an active IETF Token Status List (aligned with the Attestation Status List mechanism specified by the EU Commission).
- Credential Metadata: The metadata status_list must be populated in every issued CompanyInfo attestation, referencing the status list URI and the credential's specific index.

# 9. Request, Presentation and Verification

FIXED 
To verify and validate a received presentation of an attestation of this type,
the following steps SHALL be performed:

1.  **Cryptographic Integrity Verification (Tamper Proof):**
    The Verifier **MUST** verify that the received attestation data has not been altered or tampered with since its issuance. The wallet shall validate the digital signature over the attestation using a trusted public key (trust anchor) obtained according to the framework detailed in Chapter 10.
2.  **Issuer Authentication and Trust Evaluation:**
    The Verifier **MUST** verify the identity and regulatory standing of the Attestation Provider. The Verifier **MUST** verify that a trust anchor (Qualified Trust Service Provider (QTSP) for EAAs or the designated national Supervisory Body for other attestation), has confirmed that the attestation issuer owned the public key corresponding to the private key used to sign the verified attestation at the time of issuance.
3.  **Temporal Validity Verification:**
    The Verifier **MUST** verify that the attestation is within its stated validity window. An attestation that has not yet taken effect or has already expired **SHOULD** be accepted, regardless of any other successful checks.
4.  **Revocation Status Verification:**
    The Verifier **MUST** verify the real-time revocation status of the received attestation as described in Chapter 8, unless:
    *   The attestation is explicitly defined as short-lived; or
    *   The remaining lifetime of the attestation is below the designated revocation time threshold.
5.  **Holder Wallet and Device Binding Verification:**
    Where the attestation is device-bound according to section 7.1, the Verifier **MUST** verify the Holder's presentation signature and the presentation's binding to achieve two critical security checks:
    *   Ensure that the presenter has not submitted a copied or replayed attestation 
    *   Validate that the presented attestation was issued to this exact presenting wallet instance.

*Primary use cases:*
- Bank KYC for Corporate Account Opening (per AMLR Articles 20-25)
- Supplier Onboarding (KYS with UBO Transparency)
- Regulatory Submission for company to Transparency Register  ( Proposed Implementing Act dated 26/11/2025)
- Regulatory Reporting for company (Transparency Register Cross-Reference)
- Ongoing Monitoring (AMLR Article 25)

## 9.1. Relying Party Role ( RP Instance - EUDI Wallet)

[AUTHOR] Add obligations specific to this attestation type below. Do not edit the
list above.

## 9.2. EBW Relying Party Role ( EBW Wallet - EBW Wallet)

Following the principle of mutual identification the verification in the **European Business Wallet (EBW)** ecosystem is designed as a mutual cryptographic process. Unlike traditional consumer wallet flows, EBW transactions must satisfy high-assurance, machine-to-machine (M2M) environments. Verification of EAAs is executed under two distinct conditions:

1.  **Relying Party Role:** When an EBW Owner receives a presented attestation from a Holder and must verify its cryptographic claims before providing a service or executing a transaction.
2.  **Holder Role:** When an EBW Holder receives an incoming Presentation Request and must verify the identity and system integrity of the requesting Relying Party before releasing confidential, non-public attestation data.

The system performs these verification steps to achieve three core business and regulatory objectives:
**Trust Augmentation:** Establishing the absolute cryptographic authenticity of exchanged data and validating the identity of the participating legal entities.
**Liability Allocation:** Fulfilling statutory due diligence to minimize operational risk and programmatically shift liability to the responsible party (Issuer or Holder).
**Data Protection:** Safeguarding highly confidential corporate data (e.g., ultimate beneficial ownership, control structures) stored in the EBW against unauthorized harvest or access.

## 9.2.1 Relying Party obligation during request
1.  **Include own identification and authorization data in presentation requests:**
      When requesting non-public and therefore confidential data, the Relying Party **SHALL** include its own **EBWOID** and **BWUA** (using the `ebwoid` and `ebw_wallet_unit` format blocks in the `verifier_info` array of the Request Object) to allow the receiving Holder to:
   *   Enforce automated consent and exchange policies based on the Verifier’s legal identity and verified platform integrity.
   *   Ensure the request originates from a valid wallet instance rather than uncertified or spoofed software.
   *   *Operational Constraint:* Requesters that do not present a valid EBWOID and BWUA **SHOULD NOT** receive confidential attestations.
2.  **Request Wallet Unit Attestations (BWUA):**
       The Relying Party **SHOULD** include a request for the Holder’s Business Wallet Unit Attestation (BWUA)  to mitigate the risk of interacting with a revoked, compromised, or modified wallet instance.
3.  **Adhere to Data Minimization (Purpose Limitation):**
       The Relying Party **SHALL** only request attributes that are strictly necessary to fulfill the stated business purpose of the transaction.
4.  **Respect Trust Model Registration:**
       Where the trust model for a requested attestation requires Relying Party registration, the RP **SHALL** only request attributes it is explicitly registered and authorized to request.

## 9.2.2. Holder and Relying Party obligation during verification

To protect the Holder and Relying Party from processing fraudulent, tampered, or stolen attestations, they  **MUST** programmatically execute the following five verification steps on all received attestations. Holder and Relying Party performing the verification steps are called Verifier within the rest of this chapter. The Verifier can perform the steps only if the EBW supports the verification steps, therefore the EBW Wallet Provider **MUST** support the following verification steps with their EBW:

### 9.2.2.1 Impact of Cryptographic Verification on Holder Liability
 The mandatory validation of incoming requests protects the Holder when operating in high-security, backend-to-backend environments:

 *   **Establishes Non-Repudiation (Defense Against Dispute):** By validating the signature of the Request Object against the public key attested inside the Relying Party's EBWOID, the Relying Party cannot later deny having initiated the transaction or requested the data. This protects the Holder from legal claims that they disclosed confidential business secrets without a valid, authorized request.
 *   **Protects Against Impersonation (Defense Against Data Breaches):** It cryptographically proves the request did not originate from a malicious actor who simply spoofed the Relying Party's public `client_id` or metadata. Because the transaction requires a signature generated by the private key securely held within the Relying Party's hardware wallet, the Holder is guaranteed they are communicating with the actual legal entity identified in the EBWOID.
 *   **Fulfills Statutory Due Diligence (Safe Harbor under GDPR):** Under data protection regulations, a corporate Holder has a legal duty to protect its confidential operational data. Executing these mandatory checks before releasing any data payload safe-harbors the Holder from charges of negligence or unauthorized data disclosure.
 ---

 ### 9.2.2.2 Impact of Cryptographic Verification on Relying Party Liability

 The execution of the mandatory cryptographic checks defined in this chapter directly determines the legal and liability posture of the Relying Party (RP). Under the European Business Wallet framework and eIDAS, performing these verifications shifts liability and protects the RP from negligence claims:

 | Verification Check | Cryptographic Fact | Impact on Relying Party Liability |
 | :--- | :--- | :--- |
 | **Integrity & Issuer Auth (Steps 1 & 2)** | Proves data has not been modified; validates the cryptographic identity of the issuer. | **Transfers Data-Accuracy Liability to Issuer.** The RP is legally protected against errors or falsehoods in the received data. Liability shifts to the Attestation Provider under eIDAS2 or their published terms. |
 | **Temporal & Revocation (Steps 3 & 4)** | Proves the credential was actively valid and unrevoked at the exact moment of the transaction. | **Protects Against Fraud Claims.** Safe-harbors the RP from claims arising from the use of credentials that were valid in the past but have since expired or been revoked. |
 | **Device Binding & Presentation Signature (Step 5)** | Proves the holder has possession of the private key associated with the credential and actively authorized this specific session. | **Protects Against Identity Theft & Establishes Safe Harbor.** Explained in detail below. |

 #### **Defense Against Identity Theft (Shifts Burden of Proof)**
 By verifying the device binding (e.g., via the Key Binding JWT, matching `nonce` and `aud`), the RP proves that the presenter has real-time, hardware-backed control over the private key associated with the credential.

 If a malicious actor steals a copy of another company's EBWOID file, they **cannot** generate a valid binding signature without access to that specific wallet's private key. By verifying this binding, the RP completely protects itself from claims of *"failing to prevent obvious credential-sharing or identity theft,"* shifting the burden of proof entirely to the claimant.

 #### **Safe Harbor for Data Access and Key Compromise**
 Under GDPR and eIDAS, if an RP discloses confidential data or executes a transaction based on a credential where device binding was fully and correctly verified, it is legally deemed to have fulfilled its due diligence. If it is later discovered that the Holder's private key was compromised at the time of the transaction, the liability shifts away from the RP to:
 *   The **Holder**, for failing to adequately secure and protect their private key/hardware device.
 *   The **Issuer**, if they were notified of the key compromise but failed to add the credential to their revocation list in a timely manner.

 #### **Eliminates Sole Negligence under eIDAS (Art 12a / 12b)**
 Under eIDAS Article 12a and 12b, a Relying Party has a duty of care to validate credentials. If an RP fails to verify the presentation signature and the corresponding trust chains, they are considered to have accepted an unauthenticated payload. In the event of a security breach or fraudulent transaction, the RP can be held **solely liable** due to technical negligence.

### 9.2 Presentation modes

Remote presentation is in scope. Proximity presentation is not in scope, consistent
with chapter 5, which records the mdoc encoding as out of scope.

### 9.3 Transactional data

This Rulebook defines no transactional data.

### 9.4 Attestation type or use case specific Relying Party Obligation 

##### 9.4.1 Cross-Reference with Ownership and Control Lists (AMLR Article 60) ###

The AMLR compliance requires independent verification of UBO calculations.

*RPs SHALL:*
- Request Ownership List and Control List in addition to UBO
- Perform Independent UBO Calculation:Apply ≥25% threshold to Ownership List → Identify natural persons with ≥25% total ownership
- Analyze Control List for natural persons exercising ultimate control (even if <25% ownership)
- Apply AMLR determination methodologies
- Cross-Check Against Presented UBO :
  - Compare UBO data: Verify that all independently calculated UBOs appear in the presented UBO
  - Compare determination methodologies: Verify consistency
  - Compare ownership stakes (if disclosed)
- Discrepancy Handling
  - If UBOs are missing from presented list → notify entity to recalculate and update
  - If extra UBOs appear in presented list (not in calculated list) → request justification or evidence
  - If discrepancies relate to Transparency Register submission → report to register authority per AMLR Article 60
  - If discrepancies cannot be resolved -> risk cases: apply enhanced due diligence or decline relationship

##### 9.4.2 UBO Identity Verification (AMLR Article 21 Procedure) ####
For each UBO in the UBO  Attestation, the RP SHALL perform identity verification following this hierarchical procedure:
@TODO Florin Specify the process (relevant in MVP+)

**Step 1: PID-Based Verification (Preferred Method)**
- Request PID Attestation from the UBO (via EUDI Wallet)
- Cross-Check PID Against UBO  :identification & other attributes
- PID Attestation verification (Section 4.2)

**Step 2: non-PID Based Verification ( e.g., mdoc for driver's license, future passport mdoc))**
- Request presentation of identity document attestation
- Cross-Check data against UBO  :identification & other attributes
- mDOC  Attestation verification (Section 4.2)

**Step 3: Identity Document Verification (PoA)**
- Request presentation of identity document attestation (PoA)
- Cross-Check data against UBO  :identification & other attributes
- POA  Attestation verification (Section 4.2)
-
**Step 4: Manual/physical verification (in-person or certified copy)**
- Manual/physical identity document verification (in-person or certified copy)

**Step 5: Unique Personal Identification Number Verification (if available)**
- Check if unique_personal_identification_number is available in UBO
- If available:Use the unique ID number for identity verification

## 10 Trust Framework

The trust anchor for this attestation is obtained as described in the branch below
that corresponds to its legal category. The trust anchor location applies in either
case.

**PID, QEAA, PuB-EAA and attestations resolved via Trusted Lists**

The trust anchor is obtained from a Trusted List, as described in section 6.6.3.6
of the ARF main document. The Provider may sign the attestation with an
intermediate signing certificate, in which case the trust anchor is used to verify
that certificate rather than the attestation directly.

**Non-qualified EAA (including S-EAA)**

## 10.1. Relying Party Role ( RP Instance - EUDI Wallet)

The trust anchor is not obtained from a Trusted List of qualified trust service
providers. It is obtained as follows: [CONSORTIUM DEFAULT MECHANISM, TO AGREE].
Authorisation of the Provider to issue this attestation type is then verified by
[PROCEDURE].

A Wallet Unit MAY verify Provider authorisation using the mechanism described in
ISSU_34 of Topic 10 of Annex 2 of the ARF.

## 10.2 EBW Relying Party Role ( EBW Wallet - EBW Wallet)

### 10.2.1 Attestation Chaining

For this category, the attestation is not issued directly by a Qualified Trust Service Provider (QTSP). Instead, trust is established through a **delegated trust model** that chains back to a qualified credential. The process for a Relying Party to establish the trust anchor is as follows:

1.  **Locating the Trust Link:** The EAA Provider **MUST** embed their own European Business Wallet Owner Identity (EBWOID) credential within the header of the issued EAA. This embedded EBWOID serves as the crucial link in the trust chain.

2.  **Verifying the Trust Link:** The Relying Party **MUST** first extract and fully verify the embedded EBWOID. Since the EBWOID is itself a QEAA, its trust anchor is found on the **EU Trusted List of Lists (TLoL)**. This verification confirms that the EAA Provider is a legitimate legal entity, as certified by a QTSP.

3.  **Establishing the EAA's Trust Anchor:** The payload of the verified EBWOID contains the EAA Provider's public signing key (the `signing_key`). This key becomes the **direct trust anchor** for the Non-qualified EAA itself.

4.  **Verifying the EAA:** The Relying Party uses this trust anchor (the `signing_key` from the EBWOID) to perform the cryptographic integrity verification of the EAA.

In this model, trust is not directly established from the TLoL to the EAA, but is delegated from the **TLoL -> QTSP -> EAA Provider's EBWOID -> EAA Provider's Signing Key -> EAA**.

Following successful cryptographic verification, the authorisation of the Provider to issue this specific type of attestation is a business-level decision for the Relying Party, based on its own internal policies and trust lists.

### 10.2.2 QSEAL
[to be described]

### 10.2.3 to be defined according to ADR#336
[to be described]

**Trust anchor location**

The attribute or metadata carrying the trust anchor location contains at least the
URL at which a machine-readable version can be found or looked up. 

**Deployment profile**

For QEAAs, trust is established through the X.509 Public Key Infrastructure (PKI) and the applicable Trust List of Licensees (TLOL).
The issuer's certificate chain, including the intermediate certificate contained in the QEAA header, SHALL be validated up to a trusted root certificate. This validation SHALL be performed using the applicable TLOL, taking into account the trust list state applicable at the time of issuance.

Successful certificate chain validation establishes that:
- the issuer's certificate was recognized within the applicable trust framework;
- the issuer's identity has been validated by the supervisory authority during inclusion in the TLOL; and
- the issuer satisfies the trust requirements applicable to QEAAs.

In addition, the Relying Party MAY apply further authorization checks based on its internal policies, such as maintaining a whitelist of accepted QEAA providers.

For EAAs, trust is established through a cryptographic chain anchored in the Electronic Business Wallet Owner Identity Document (EBWOID).
The EBWOID SHALL be included in the header of every EAA. During EBWOID issuance, the EBWOID provider verifies that the public key contained in the EBWOID is owned by the Electronic Business Wallet (EBW) owner.

The Relying Party SHALL verify the EBWOID in accordance with the verification procedure defined in this Rulebook. Upon successful verification, the Relying Party obtains:
- assurance that the EBWOID was issued by an authorized provider and is not self-issued;
- the verified identity of the issuer, including its name and EUID (or another globally unique EBW owner identifier); and
- the public key authorized to verify the EAA signature.

Authorization of the issuer is subsequently determined in accordance with the Relying Party's internal policies. Such authorization MAY be based on locally maintained wallet configuration or on trusted jurisdiction- or domain-specific trust list services that identify issuers authorized for a particular type of EAA

## 11 References

| **Item Reference** | **Standard name/details** |
| --- | --- |
| [European Digital Identity Regulation] | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework |
| [AMLR 2024/1624] | Regulation (EU) 2024/1624 of the European Parliament and of the Council on the prevention of the use of the financial system for the purposes of money laundering or terrorist financing |
| [HAIP] | Yasuda, K. et al, OpenID4VC High Assurance Interoperability Profile, OpenId Foundation, Version draft-03 |
| [IANA-JWT-Claims] | IANA JSON Web Token Claims Registry. Available: https://www.iana.org/assignments/jwt/jwt.xhtml |
| [ICAO 9303] | ICAO Doc 9303 — Machine Readable Travel Documents. Available: https://www.icao.int/publications/pages/publication.aspx?docnum=9303 |
| [ISO/IEC 18013-5] | ISO/IEC 18013-5, Personal identification — ISO-compliant driving licence - Part 5: Mobile driving licence (mDL) application, First edition, 2021-09 |
| [ISO 3166-1] | ISO 3166-1 — Codes for the representation of names of countries and their subdivisions. Available: https://www.iso.org/iso-3166-country-codes.html |
| [ISO 8601] | ISO 8601 — Date and time format. Available: https://www.iso.org/iso-8601-date-and-time-format.html |
| [OIDC] | Sakimura, N. et al., "OpenID Connect Core 1.0", OpenID Foundation. Available: https://openid.net/specs/openid-connect-core-1_0.html |
| [RFC 2119] | RFC 2119 — Key words for use in RFCs to Indicate Requirement Levels, S. Bradner, March 1997 |
| [RFC 3339] | RFC 3339 — Date and Time on the Internet: Timestamps, G. Klyne et al., July 2002 |
| [RFC 7519] | RFC 7519 — JSON Web Token (JWT), M. Jones et al., May 2015 |
| [RFC 8610] | RFC 8610 — Concise Data Definition Language (CDDL): A Notational Convention to Express Concise Binary Object Representation (CBOR) and JSON Data Structures, H. Birkholz et al., June 2019 |
| [RFC 8943] | RFC 8943 — Concise Binary Object Representation (CBOR) Tags for Date, M. Jones et al., November 2020 |
| [RFC 8949] | RFC 8949 — Concise Binary Object Representation (CBOR), C. Bormann et al., December 2020 |
| [SD-JWT VC] | SD-JWT-based Verifiable Credentials (SD-JWT VC). Available: https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/, version draft-ietf-oauth-sd-jwt-vc-09 |
| [Topic 7] | ARF Annex 2 - Topic 7 - Attestation revocation and revocation checking. Available: https://eudi.dev/3.0.0/annexes/annex-2/annex-2.02-high-level-requirements-by-topic/#a237-topic-7-attestation-revocation-and-revocation-checking |
