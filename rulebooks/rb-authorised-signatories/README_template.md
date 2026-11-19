# Attestation Rulebook for attestations of type Authorised Signatories

Category: S-EAA 

* Author(s):
  * [Ricky Lamberty, Robert Bosch GmbH]
  * [Florin Coptil, Robert Bosch GmbH]
  * [Stephan-A Fuchs, Deutsche Bank AG] 

* Reviewer(s):
  * [Dominic Hurni, SBB]
  * [Werner Folkendt, Robert Bosch GmbH]

* Contact:
  * [Florin Coptil](mailto:florin.coptil@bosch.com)
  * [Stephan Fuchs](mailto:stephan-a.fuchs@db.com)

* Feedback: [GitHub issues](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/issues)

| Version | Date | Description |
| --- | --- | --- |
| 1.1 | 2026-10-02 | Restructured onto the generic WE BUILD attestation rulebook template (11 chapters). No normative content removed. |
| 1.2 | 2026-10-13 | Migrated to the current generic WE BUILD attestation rulebook template; attestation-specific normative content preserved. |

**Written against:** ARF version 3.0.0, WE BUILD template version 1.0 (generic)

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
   * [7.1 Holder Key Binding at Issuance (Wallet Binding)](#71-holder-key-binding-at-issuance-wallet-binding)
   * [7.2 Issuance Policy](#72-issuance-policy)
   * [7.3 Lifecycle management](#73-lifecycle-management)
   * [7.4 Embedded disclosure policy](#74-embedded-disclosure-policy)
- [8 Revocation](#8-revocation)
- [9 Request, Presentation and Verification](#9-request-presentation-and-verification)
   * [9.1 Relying Party Role (RP Instance - EUDI Wallet)](#91-relying-party-role-rp-instance---eudi-wallet)
   * [9.2 EBW Relying Party Role (EBW Wallet - EBW Wallet)](#92-ebw-relying-party-role-ebw-wallet---ebw-wallet)
   * [9.3 Presentation modes](#93-presentation-modes)
   * [9.4 Transactional data](#94-transactional-data)
- [10 Trust Framework](#10-trust-framework)
   * [10.1 Relying Party Role (RP Instance - EUDI Wallet)](#101-relying-party-role-rp-instance---eudi-wallet)
   * [10.2 EBW Relying Party Role (EBW Wallet - EBW Wallet)](#102-ebw-relying-party-role-ebw-wallet---ebw-wallet)
- [11 References](#11-references)


## 1 Introduction

This attestation addresses the following question:

**Who is authorised to act (sign, transact, etc) on behalf of this legal entity?**

The authority to act on behalf of a legal entity can be derived from two primary sources:
- **Statutory Power:** Authority based on a direct entry in a national public register (e.g., a Commercial Register).
- **Delegated Power:** Authority granted via a separate Power of Attorney (PoA) Attestation, which was issued by the company which issued the AuthorisedSignatories Attestation.
  
As a digital, verifiable list of natural persons possessing representation powers, this attestation enables a Relying Party (such as banks or fintechs) to confidently confirm that a specific person (the Signatory) has the authority to make binding commitments (e.g., signing a contract) in financial and contractual settings with third parties. This attestation is mandatory, for example, when opening a corporate bank account, though other business use cases may require the same type of verification.

### 1.1 Document scope and purpose

The AuthorisedSignatories Attestation records all natural persons who are authorised to act on
behalf of a legal entity, providing comprehensive transparency on signatory rights and
representation powers. This attestation is a critical component of both Know Your Customer (KYC)
and Know Your Supplier (KYS) processes within the EUDI Wallet ecosystem, supporting effective
risk management, regulatory compliance, and anti-money laundering (AML) obligations.

**Important distinctions:**
- An Authorised Signatory does not need to be a registered Legal Representative.
- An Authorised Signatory does not need to meet any ownership or control threshold.
- A single person **MAY** hold both statutory and delegated authority simultaneously.

 **Note:** This attestation is not a replacement for the Power of Attorney (PoA) Attestation.

**Design Decisions**

This AuthorisedSignatories Attestation Rulebook is based on:
- EU Company Certificate (EUCC) framework as the foundational legal identity layer
- Draft RTS on Customer Due Diligence under Article 28(1) of Regulation (EU) 2024/1624
- eIDAS 2.0 / EUDI Wallet framework for digital identity and verifiable attestations
- ISO 8601 for date formatting
- Submission Regulation – Commission on Implementing Regulation (EU) [number] on the formats for submitting beneficial ownership information.

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

| Term | Definition | Source |
| --- | --- | --- |
| AuthorisedSignatories | AuthorisedSignatories Attestation, the attestation type defined in this Rulebook, providing a verifiable list of natural persons authorised to act on behalf of a legal entity | |
| Authorised Signatory | A natural person who is authorised to act on behalf of a legal entity in financial and contractual settings, either through statutory power or delegated power | |
| Statutory Power | Authority to act on behalf of a legal entity based on a direct entry in a national public register (e.g., Commercial Register) | |
| Delegated Power | Authority to act on behalf of a legal entity granted via a Power of Attorney (PoA) issued by the legal entity | |
| PoA | Power of Attorney, a separate attestation granting delegated authority to act on behalf of a legal entity | |
| EUCC | EU Company Certificate, attestation establishing the legal existence and identity of a legal entity within the EU | |
| EUID | European Unique Identifier, the unique identifier assigned to legal entities registered within the EU | |
| KYC | Know Your Customer, due diligence process for verifying customer identity and assessing risk in financial relationships | |
| KYS | Know Your Supplier, due diligence process for verifying supplier credentials, integrity, and risk exposure | |
| Relying Party | A bank, fintech, or other entity that relies on the AuthorisedSignatories Attestation to verify the authority of a signatory | |
| Representation Type | The nature of the power of representation, either SOLE (one signatory sufficient) or JOINT (multiple signatories required) | |
| ISO 8601 | International standard for date and time representations (e.g., YYYY-MM-DD) | |

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

*A non-qualified self EAA answers these rows as a non-qualified EAA (EW-DM-12-015, -018, -020, , -024 and -030).

## 3 Attestation attributes

Attributes are defined here in an encoding-independent manner (EW-DM-12-007). The
authoritative encoding lives in the machine-readable schema artefacts referenced in
section 3.1, not in this document. Do not paste schema fragments into the prose,
they will drift.

### 3.1 Introduction

The AuthorisedSignatories Attestation is designed to provide a standardized, verifiable
representation of all natural persons authorised to act on behalf of a legal entity. It enables
Relying Parties to comprehensively verify signatory authority in financial and contractual
settings, supporting effective KYC/KYS processes and regulatory compliance.

**Data Model:**

The AuthorisedSignatories Attestation is structured into a root object containing two distinct
sub-objects:

```
AuthorisedSignatories
├── Legal_Entity (M)
│   ├─ legal_person  (M)
│   │   ├─ legal_person_name (tstr) (M)
│   │   ├─ legal_form_type (tstr) (M)
│   ├─ identifier  (M)                          // At least one identifier required
│   │   ├─ euid (str) (O)                       // European Unique Identifier
│   │   ├─ lei (str) (O)                        // Legal Entity Identifier per ISO 17442
│   │   ├─ tax (str) (O)                        // National tax or registration number    
│   │   ├─ gln (str) (O)                        // Global Location Number for legal entities, GS1 identifier
│   │   ├─ duns (str) (O)                       // Data Universal Numbering System, Dun & Bradstreet identifier
│   │   ├─ eori (str) (O)                       // Economic Operators Registration and Identification number, EU customs identifier
│   │   ├─ bpnl (str) (O)                       // Business Partner Number Legal entity, Catena-X identifier per ICD 0243
│   │   ├─ siren (str) (O)                      // Système d'Identification du Répertoire des ENtreprises, French company identifier
└── Authorised_Person [1..n] 
    ├─ NaturalPerson          (first_name (M), surname (M), date_of_birth (M))                                 , mandatory
    ├─ BirthPlace             (locality (M), country (M), region (O))                                          , mandatory
    ├─ Citizenship            (citizenship(s) [1..n])                                                          , mandatory
    ├─ PersonRole             (role (O), representation_type (M), email(O), phone(O))                           , mandatory
    └─ Identifier             (document_type (M), document_number (M), issuing_country (M), expiry_date (M))   , optional
```
*Note*: M - mandatory / O - optional.

**Explanation:**

The `Legal_Entity` object **SHALL** appear exactly once and contains:
- `Legal_Person`, the official legal name and legal form of the entity issuing the attestation.
- `Identifier`, the EUID (mandatory) and optionally LEI and/or tax registration number.

The `Authorised_Person` object **SHALL** appear at least once and **MAY** be repeated for each authorised signatory. Each instance contains:
- `NaturalPerson`, the full legal name and date of birth of the signatory.
- `BirthPlace`, the place of birth including at minimum locality and country.
- `Citizenship`, one or more citizenships held by the signatory.
- `PersonRole`, the role within the company (optional) and the representation type (mandatory).
- `NaturalPersonIdentifier`, optional identity document details for enhanced identification.


**Schema artefacts**

| Format | Identifier | Schema artefact | Version | Location                                              |
| --- | --- | --- | --- |-------------------------------------------------------|
| SD-JWT VC | `vct` as recorded in section 5.1 | JSON schema | 0.4.0 per its `$id` | `data-schemas/sd-jwt/ubo-authorised-signatories.json` |

Sample data is at `data-schemas/sd-jwt/sample-data/ubo-sd-jwt-sample.json`.

> **Two points on the artefact.** It carries no `version` member, and the version in
> its `$id` is 0.4.0 while this Rulebook is at 1.1. Those should be reconciled. The
> schema also defines `jti`, which this Rulebook does not document.

Attributes that SHALL be present in every attestation of this type.

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| legal_person | [EconomicOperator](https://w3id.org/ebwv#EconomicOperator) | Information about the legal person | Object |
| legal_identifier | [legalIdentifier](https://w3id.org/ebwv#legalIdentifier) | Information about the legal person identifier | Object |
| natural_person | [Person](https://w3id.org/ebwv#Person) | Information about the natural person | Object |
| birth_place | [placeOfBirth](https://w3id.org/ebwv#placeOfBirth) | Information about the birth place | Object |
| citizenship | [citizenship](https://w3id.org/ebwv#citizenship) | Citizenship(s) held by the person (one or more nationalities) | Array of Strings (ISO 3166-1 alpha-3) |
| person_role | [role](https://w3id.org/ebwv#role) <br> property needs additional Domains and Ranges in EBWV | Information about the natural person role | Object |
| identification | [identifier](https://w3id.org/ebwv#identifier) <br> at the moment "identifier" is a property, but it could point to a adms:Identifier type of class; or what does "identification" actually mean in this context? | Information about the identification of the person | Object |

### 3.2 Mandatory attributes

**LegalPerson Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| legal_person_name | [legalName](https://w3id.org/ebwv#legalName) | The complete official legal name of the legal entity | String |
| legal_form_type | [legalForm](https://w3id.org/ebwv#legalForm) | The legal form of the legal entity (e.g., SA, GmbH, Ltd, BV) | String |

**NaturalPerson Attributes**

This object is defined for each person represented in the AuthorisedSignatories Attestation.

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| first_name | [firstName](https://w3id.org/ebwv#firstName) | The first names in full (including all given names and middle names) | String |
| surname | [familyName](https://w3id.org/ebwv#familyName) | The surnames in full (all family names/last names) | String |
| date_of_birth | [dateOfBirth](https://w3id.org/ebwv#dateOfBirth) | Day, month, and year of birth of the person per ISO 8601 | Date (YYYY-MM-DD) |

**BirthPlace Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| locality | [placeOfBirth](https://w3id.org/ebwv#placeOfBirth) | Locality (city or town) where the natural person was born | String |
| country | [placeOfBirth](https://w3id.org/ebwv#placeOfBirth) | Country where the natural person was born | String (ISO 3166-1 alpha-3) |

**Citizenship Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| citizenship | [citizenship](https://w3id.org/ebwv#citizenship) | The nationality or nationalities of the authorised person (one or more) | Array of Strings (ISO 3166-1 alpha-3) |

**PersonRole Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| representation_type | [scopeOfAuthorization](https://w3id.org/ebwv#scopeOfAuthorization) | The nature of the power of representation. SHALL be one of the values defined in Section 4.4.1 | String ("SOLE" or "JOINT") |

### 3.3 Optional attributes

Attributes the Provider MAY include at its discretion.

#### BirthPlace Optional Attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| euid | [identifier](https://w3id.org/ebwv#identifier) | European Unique Identifier per Directive (EU) 2017/1132. | String |
| lei | [identifier](https://w3id.org/ebwv#identifier) | Legal Entity Identifier (LEI) per ISO 17442. | String |
| tax | [identifier](https://w3id.org/ebwv#identifier) | National tax or company registration number. | String |
| gln | [identifier](https://w3id.org/ebwv#identifier) | Global Location Number for legal entities (GS1 identifier). | String |
| duns | [identifier](https://w3id.org/ebwv#identifier) | Data Universal Numbering System (Dun & Bradstreet identifier). | String |
| eori | [identifier](https://w3id.org/ebwv#identifier) | Economic Operators Registration and Identification number (EU customs). | String |
| bpnl | [identifier](https://w3id.org/ebwv#identifier) | Business Partner Number Legal entity (Catena-X identifier). | String |
| siren | [identifier](https://w3id.org/ebwv#identifier) | Système d'Identification du Répertoire des ENtreprises (French identifier). | String |

**BirthPlace Optional Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| region | [placeOfBirth](https://w3id.org/ebwv#placeOfBirth) | Optional additional detail on the region or state of birth | String |

**PersonRole Optional Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| role | [role](https://w3id.org/ebwv#role) <br> property needs additional Domains and Ranges in EBWV | The role of the authorised person within the company (e.g., CEO, CFO, Director) | String |
| email | [hasEmail](https://w3id.org/ebwv#hasEmail) | The email of the authorised person within the company (e.g., CEO, CFO, Director) | String |
| phone | [hasTelephone](https://w3id.org/ebwv#hasTelephone) | The phone of the authorised person within the company (e.g., CEO, CFO, Director) | String |

**NaturalPersonIdentifier Optional Attributes**

When present, all four fields within this object **SHALL** be provided together.

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| document_type | ... | A value defining the type of the identity document (e.g., Passport, National identity card) | String |
| document_number | ... | The number of the identity document (passport number, national ID number, etc.) | String |
| issuing_country | ... | The country that issued the identity document (ISO 3166-1 alpha-3 code) | String |
| document_expiry_date | ... | The expiration date of the identity document per ISO 8601 | Date (YYYY-MM-DD) |

### 3.4 Conditional attributes

No conditional attributes are defined for this attestation type. All attributes are either
mandatory or optional as specified above.

## 4 Metadata

Metadata describes the attestation rather than its subject.

### 4.1 Mandatory metadata

*Note*: Only the additional mandatory attributes are listed; the mandatory attributes defined by the protocol are not specified.

| **Data Identifier** | **Semantic reference**|**Definition** |**Data type**| **Example value** |                   
| --- |-----------------------------------------------------------| --- | -- |-------------------|
| attestation_legal_category | |Indicates the legal category of the Attestation | String | S-EAA       |
| cnf | | cryptographic Key Binding                                  | String |                   |

### 4.2 Optional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| trust_anchor_url | cred: | URL where the trust anchor for verifying this attestation can be retrieved | URI |
| schema_version | cred: | Version of the schema used for this attestation | String |

### 4.3 Conditional metadata

No conditional metadata elements are defined for this attestation type.

### 4.4 Code lists

#### 4.4.1 Representation Type Codes

The `representation_type` attribute **SHALL** use one of the following standardized values:

| **Code** | **Definition** |
| --- | --- |
| SOLE | A single signatory has full authority to act and sign on behalf of the legal entity independently, without requiring the co-signature of any other person |
| JOINT | Two or more signatories are required to act together to make binding commitments on behalf of the legal entity |

> **Note:** The representation type applies in the context of financial relationships
> (e.g., opening a bank account, currency account, credit line, etc.).

#### 4.4.2 Type of Identity Document Codes

The `document_type` attribute, when present, **SHALL** use one of the following standardized values:

| **Code** | **Definition** |
| --- | --- |
| Passport | International travel document issued by a national government |
| National identity card | National identity card issued by the authorised person's country of nationality |
| Driver's license | Driver's license used as an identity document where accepted by the jurisdiction |
| Residence permit | Residence permit or similar document issued by the country of residence |
| Other official identity document | Other government-issued identity document accepted for identity verification |

### 4.5 Integrity rules

The following integrity rules **SHALL** be enforced:

- The `Authorised_Person` array **SHALL** contain at least one entry in the AuthorisedSignatories Attestation.
- Each `Authorised_Person` entry **SHALL** contain `first_name`, `surname`, `date_of_birth`, `citizenship`, `birth_place_locality`, `birth_place_country`, and `representation_type`.
- `Legal_Entity` **SHALL** appear exactly once and **SHALL** contain `legal_person_name`, `legal_form_type`, and `euid`.
- `date_of_birth` **SHALL** be a valid ISO 8601 date (YYYY-MM-DD).
- `citizenship` **SHALL** be an array of one or more valid ISO 3166-1 alpha-3 country codes.
- `birth_place_country` **SHALL** be a valid ISO 3166-1 alpha-3 country code.
- `representation_type` **SHALL** be one of the values defined in Section 4.4.1 (`"SOLE"` or `"JOINT"`).
- `document_type`, when present, **SHALL** be one of the values defined in Section 4.4.2.
- `document_expiry_date`, when present, **SHALL** be a valid ISO 8601 date (YYYY-MM-DD).
- If any `NaturalPersonIdentifier` attribute is present, all four fields (`document_type`, `document_number`, `issuing_country`, `document_expiry_date`) **SHALL** be present together.
- `euid` **SHALL** be a non-empty string conforming to the format defined in Directive (EU) 2017/1132.
- `lei`, when present, **SHALL** be a 20-character string conforming to ISO 17442.
- `issuance_date` and `expiry_date` **SHALL** be valid ISO 8601 DateTimes.
- `expiry_date` **SHALL** be later than `issuance_date`.
- `issuance_date` **SHALL** be in the past.
- `category` **SHALL** be `eaa:eu:non-qualified` for the declared non-qualified EAA category.
- If `trust_anchor_url` is present, it **SHALL** be a valid URI.
- If `schema_version` is present, it **SHALL** be a non-empty string.
- Each attribute **SHALL** appear at most once within its scope (e.g., within a `Legal_Entity` or `Authorised_Person` object).
- If the technical validity period (expiry_date − issuance_date) exceeds 24 hours, the status claim SHALL be present, conforming to the structure defined in Section 5.1.2.


## 5 Formats

> This chapter identifies the formats in which this attestation is issued. The
> encoding detail lives in the schema artefacts referenced in section 3.1, and the
> rules for using each format are in chapters 7 and 9.

| Format | Supported | Identifier | Specification | Notes |
| --- | --- | --- | --- | --- |
| ISO/IEC 18013-5 mdoc | no | | [ISO/IEC 18013-5] | Proximity presentation is out of scope |
| SD-JWT VC | yes | `vct` `eu.we-build:authorisedsignatories:1` | [SD-JWT VC], [HAIP] | SHALL follow the HAIP profile |
| W3C VCDM | no | | | No encoding is defined in this version |

### 5.1 SD-JWT VC-based encoding

The AuthorisedSignatories Attestation uses the SD-JWT VC format to allow for selective  disclosure of signatory attributes.

**Selective Disclosure:** Top-level claims (e.g., `legal_entity`, `authorised_persons`) **SHALL**
be individually selectively disclosable, enabling a legal entity to disclose only the attributes
requested by a Relying Party. Attributes nested within an `Authorised_Person` object (e.g.,
`first_name`, `date_of_birth`, `representation_type`) **MAY** be individually selectively
disclosable as per the attribute encoding table below.

The `.` notation is used to indicate the nesting of attributes.

**Verifiable Credential Type (`vct`):** `eu.we-build:authorisedsignatories:1`

#### Attribute Encoding Table

| **Data Identifier** | **Attribute Identifier** | **Encoding Format** | **Reference/Notes** | **Disclosable** |
| --- | --- | --- | --- | --- |
| **Legal Entity** |  |  |  |  |
| legal_person_name | `legal_entity.legal_person.legal_person_name` | string | The complete official legal name of the company | MUST |
| legal_form_type | `legal_entity.legal_person.legal_form_type` | string | Legal form of the company (e.g., GmbH, S.A., Ltd.) | MUST |
| **Legal Entity Identifier** |  |  |  |  |
| euid | `legal_person.identifier.euid` | String | European Unique Identifier, optional sub-field | MUST |
| lei | `legal_person.identifier.lei` | String | Legal Entity Identifier per ISO 17442, optional sub-field | MUST |
| tax | `legal_person.identifier.tax` | String | National tax or registration number, optional sub-field | MUST |
| gln | `legal_person.identifier.gln` | String | Global Location Number for legal entities, optional sub-field | MUST |
| duns | `legal_person.identifier.duns` | String | Dun & Bradstreet company identifier, optional sub-field | MUST |
| eori | `legal_person.identifier.eori` | String | EU customs identifier, optional sub-field | MUST |
| bpnl | `legal_person.identifier.bpnl` | String | Catena-X BPNL identifier per ICD 0243, optional sub-field | MUST |
| siren | `legal_person.identifier.siren` | String | French company identifier (SIREN), optional sub-field | MUST |
| **Authorised Person** |  |  |  |  |
| authorised_persons | `authorised_persons` | array | Array of authorised person objects in the AuthorisedSignatories Attestation; SHALL contain at least one entry | MUST |
| **NaturalPerson** |  |  |  |  |
| first_name | `authorised_persons[n].natural_person.first_name` | string | Full first name(s) of the authorised person per Art. 2 RTS | MUST |
| surname | `authorised_persons[n].natural_person.surname` | string | Full surname(s) of the authorised person per Art. 2 RTS | MUST |
| date_of_birth | `authorised_persons[n].natural_person.date_of_birth` | string | Date of birth of the authorised person; ISO 8601 full-date format (YYYY-MM-DD) | MUST |
| **BirthPlace** |  |  |  |  |
| birth_place.locality | `authorised_persons[n].birth_place.locality` | string | Locality (city or town) where the authorised person was born | MUST |
| birth_place.country | `authorised_persons[n].birth_place.country` | string | Country where the authorised person was born, per Art. 4 RTS; ISO 3166-1 alpha-3 | MUST |
| birth_place.region | `authorised_persons[n].birth_place.region` | string | Optional region or state of birth | MAY |
| **Citizenship** |  |  |  |  |
| citizenship | `authorised_persons[n].citizenship` | array | Nationality or nationalities of the authorised person; ISO 3166-1 alpha-3 codes | MUST |
| **PersonRole** |  |  |  |  |
| person_role.representation_type | `authorised_persons[n].person_role.representation_type ` | string | The nature of the power of representation; SHALL use codes from Section 4.4.1 ("SOLE" or "JOINT") | MUST |
| person_role.role | `authorised_persons[n].person_role.role` | string | The role of the authorised person within the company (e.g., CEO, CFO); optional | MUST |
| person_role.email | `authorised_persons[n].person_role.email` | string | The role of the authorised person within the company (e.g., CEO, CFO); optional | MUST |
| person_role.phone | `authorised_persons[n].person_role.phone` | string | The role of the authorised person within the company (e.g., CEO, CFO); optional | MUST |
| **NaturalPersonIdentifier** |  |  |  |  |
| identifier.document_type | `authorised_persons[n].identifier.document_type` | string | Type of identity document; SHALL use codes from Section 4.4.2; optional | MAY |
| identifier.document_number | `authorised_persons[n].identifier.document_number` | string | The number of the identity document; optional | MAY |
| identifier.issuing_country | `authorised_persons[n].identifier.issuing_country` | string | Country that issued the identity document; ISO 3166-1 alpha-3; optional | MAY |
| identifier.document_expiry_date | `authorised_persons[n].identifier.document_expiry_date` | string | Expiration date of the identity document; ISO 8601 full-date format (YYYY-MM-DD); optional | MAY |
| **Metadata** |  |  |  |  |
| `issuance_date` | `iat` | Number (Unix timestamp) | Date and time when the attestation was issued (ISO 8601); RFC 7519                                  | MUST NOT |
| `expiry_date` | `exp` | Number (Unix timestamp) | Date and time when the attestation expires (ISO 8601); RFC 7519                                     | MUST NOT |
| `issuing_entity` | `iss` | String (URI or DID) | Identifier of the competent institution that issued the attestation; RFC 7519                       | MUST NOT |
| `attestation_legal_category` | `attestation_legal_category` | String | One of "S-EAA" as defined by eIDAS 2                                                      | MUST NOT |
| `vct` | `vct` | String | The vct definition                                                                                  | MUST NOT |
| `cnf` | `cnf` | String | Cryptographic Key Binding                                                                           | MUST NOT |
| `schema_version` | `schema_version` | String | Version of the schema used; optional                                                                | MAY |
| `trust_anchor_url` | `trust_anchor_url` | String (URI) | URL where the trust anchor for verifying this attestation can be retrieved; optional                | MAY |

**Notes:**

- **MUST**: The claim **SHALL** be selectively disclosable, the holder **MAY** choose to
  disclose or withhold this claim when presenting the credential to a Relying Party.
- **MAY**: The claim **MAY** be selectively disclosable if the issuer supports it; the holder
  can choose to disclose or withhold.
- **MUST NOT**: The claim **SHALL NOT** be selectively disclosable, it is always present in
  plain text in the JWT header/payload and cannot be withheld by the holder, as it is required
  for credential verification and trust establishment.
- `iat`, `exp`, and `iss` follow RFC 7519 standard JWT claim naming conventions.
- The `NaturalPersonIdentifier` group of attributes is marked as `MAY` disclosable as a unit
 , if any attribute within the group is disclosed, all four **SHALL** be disclosed together.

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
| [CIR 2024/2979] | Commission Implementing Regulation (EU) 2024/2979, integrity and core functionality |
| [ETSI TS 119 461] | Policy and security requirements for trust service components providing identity proofing of trust service subjects |
| [ETSI TS 119 471] | Policy and security requirements for EAA service providers |
| [ETSI TS 119 472-1] | Profiles for Electronic Attestations of Attributes; Part 1 - General requirements |
| [OpenID4VCI] | OpenID for Verifiable Credential Issuance |
| [OpenID4VP] | OpenID for Verifiable Presentations |
| [European Digital Identity Regulation] | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework |
| [HAIP] | Yasuda, K. et al, OpenID4VC High Assurance Interoperability Profile, OpenId Foundation, Version draft-03 |
| [IANA-JWT-Claims] | IANA JSON Web Token Claims Registry. Available: https://www.iana.org/assignments/jwt/jwt.xhtml |
| [ISO/IEC 18013-5] | ISO/IEC 18013-5, Personal identification, ISO-compliant driving licence - Part 5: Mobile driving licence (mDL) application, First edition, 2021-09 |
| [ISO 4217] | ISO 4217, Currency codes. Available: https://www.iso.org/iso-4217-currency-codes.html |
| [ISO 8601] | ISO 8601, Date and time format. Available: https://www.iso.org/iso-8601-date-and-time-format.html |
| [OIDC] | Sakimura, N. et al., "OpenID Connect Core 1.0", OpenID Foundation. Available: https://openid.net/specs/openid-connect-core-1_0.html |
| [RFC 2119] | RFC 2119, Key words for use in RFCs to Indicate Requirement Levels, S. Bradner, March 1997 |
| [RFC 3339] | RFC 3339, Date and Time on the Internet: Timestamps, G. Klyne et al., July 2002 |
| [RFC 8610] | RFC 8610, Concise Data Definition Language (CDDL): A Notational Convention to Express Concise Binary Object Representation (CBOR) and JSON Data Structures, H. Birkholz et al., June 2019 |
| [RFC 8943] | RFC 8943, Concise Binary Object Representation (CBOR) Tags for Date, M. Jones et al., November 2020 |
| [RFC 8949] | RFC 8949, Concise Binary Object Representation (CBOR), C. Bormann et al., December 2020 |
| [SD-JWT VC] | SD-JWT-based Verifiable Credentials (SD-JWT VC). Available: https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/, version draft-ietf-oauth-sd-jwt-vc-09 |
| [Topic 7] | ARF Annex 2 - Topic 7 - Attestation revocation and revocation checking. Available: https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a237-topic-7-attestation-revocation-and-revocation-checking |
