# Attestation Rulebook for attestations of type Contact Person

Category: non-qualified EAA

* Author(s):
  * [Florin Coptil, Robert Bosch GmbH]
  * [Dominic Hurni, SBB]
* Previous Authors
  *
* Reviewer(s):
  * [Werner Folkendt, Robert Bosch GmbH]
  * [Stephan-A Fuchs, Deutsche Bank]


* Contact:
  * [Florin Coptil](mailto:florin.coptil@bosch.com)
  * [Dominic Hurni](mailto:dominic.hurni@sbb.ch) 
  
* Feedback:

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

This attestation addresses the following question:

**Who are the designated contact persons within a legal entity and what are their roles and contact details?**

The Contact Person Attestation identifies and verifies natural persons acting as designated contacts of a economic operator, enabling automated and secure exchange of trustworthy contact person data between economic operators in supply chain, procurement, and onboarding processes.

### 1.1 Document scope and purpose

Cross-company communication and data exchange is daily business in supply management. Knowing the correct and
valid contact persons for different issues (e.g., finance, product, quality, logistics) saves time and money and therefore crucial to conduct efficient business in the supplier onboarding, pre-contracting, or contracting phase.
Minimum one contact person is required for the onboarding process. The Contact Person Attestation identifies and verifies natural persons acting as designated
contacts of the corresponding economic operator, enabling automated and secure exchange of contact person data between economic operators within supply chain and procurement processes.

**Use Cases:**

*Relying Party:*
- Logistics employees have instant access to valid logistics contact person data. For example,
  in the event of a wrongly delivered battery cell, an employee contacts the responsible sales
  representative by email or phone.
- The Relying Party Wallet validates the revocation status of contact person data. Administrative employee receives a notification and takes contact with HR responsible contact person of supplier. 

*Holder:*
- An administrative employee receives a request from a procurer to provide contact persons for
  sales, production, finance, and quality for a specific product (e.g., battery cell). The
  holder company has issued Contact Person attestations for all its employees into its Company
  Wallet. The system selects the fitting employee to answer the request (e.g., a Key Account
  Manager as the battery cell sales contact person).
- The Holder is responsible for the lifecycle of the attestation content, including revocation and
  role changes. Holder is not responsible for the attestation schema. 

The added value of the Contact Person attestation for organizations is to automate the
onboarding and maintenance process of contact person data, increasing data accuracy and
enabling fast and secure business interactions. Self issued attestation can be n times reused. 

This attestation flows only between organizations where a business relationship exists. 
After mutual identification and authentication. 

**Design Decisions**

This Contact Person Attestation Rulebook is based on:
- EU Company Certificate (EUCC) / European Business Wallet (EBW) framework as the foundational
  legal identity layer for the employing organization, including identifier.  
- Schema.org vocabulary for personal name attributes
- Core Public Organisation Vocabulary (CPOV) for contact point attributes
- European Business Wallet Vocabulary (https://webuild-consortium.github.io/wp4-semantics-group/ebwv//vocabulary.html)
- The Organization Ontology for role classification
- RFC 4021 for email address formatting
- ITU-T E.164 for telephone number formatting
- EAA as proof for employeeship for each employee issued by the economic operator. 

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
| Contact Person | The attestation type defined in this Rulebook, identifying a natural person designated as a contact of an economic operator for specific business functions |
| Economic Operator | A legal entity participating in commercial or procurement activities, identified per the European Business Wallet (EBW) framework |
| EUCC | EU Company Certificate – attestation establishing the legal existence and identity of a legal entity within the EU |
| EBW | European Business Wallet – the digital wallet framework for legal entities operating within the EU single market |
| Role | A designated function or responsibility assigned to a contact person within an organization (e.g., sales, finance, quality, logistics) |
| Employee Identifier | An alphanumeric identifier assigned by the employing organization to uniquely identify an employee |
| KYS | Know Your Supplier – due diligence process to onboard suppliers including verifing credentials to assure integrity and estimate risk exposure |
| Schema.org | A collaborative, community-based vocabulary for structured data markup on the internet, used here for personal name attributes |
| CPOV | Core Public Organisation Vocabulary – a standardized EU vocabulary for describing public organizations and their contact points |
| Organization Ontology | A W3C ontology for describing organizational structures, roles, and memberships |
| RFC 4021 | IETF standard for the registration of mail and MIME header fields, used here as the reference for valid email address format |
| E.164 | ITU-T international public telecommunication numbering plan, used here as the reference for valid telephone number format |
| ISO 8601 | International standard for date and time representations (e.g., YYYY-MM-DD) |

---

## 2 Compliance

### 2.1 Compliance statement

This Rulebook complies with the applicable requirements of Topic 12, Attestation
Rulebooks, in Annex 2 of the Architecture and Reference Framework, version 3.0.0. It
uses the terminology of Annex 1 of the ARF.


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

The Contact Person Attestation is designed to provide a standardized, verifiable representation
of a natural person designated as a contact of an economic operator. This attestation enables
trusted and automated exchange of contact person data between economic operators in supply chain,
procurement, and onboarding processes.

The data model for the Contact Person Attestation is structured as follows:

*Data Model:**
````
ContactPerson Attestation
├─ legal_entity (M)
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
└── contact_persons [1..n]                      // Array of ContactPerson 
│   ├─  given_name (M)
│   ├─  family_name (M)
│   ├─  role (M)
│   ├─  email (M)
│   ├─  telephone (O)
````
*Note*: M - mandatory / O - optional.

**Explanation:**

- The `legal_entity` object **SHALL** appear exactly once and contains an `identifier` object with at least one official identifier of the company.
- The `Contact_Person` object **SHALL** appear at least once and **MAY** be repeated for each designated contact. Each instance contains the person's name, role, and contact details.

**Attestation Classification:**

This attestation type is classified as:
- **"EAA"** Self-issued by the legal entity as part of its disclosures.

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| `legal_entity` | , | An object containing identifiers for the legal entity. | Object |
| `contact_persons` | , | An array of objects, each representing an individual contact person. | Array of Objects |

| **Data Identifier** | **Semantic Reference** | **Definition** | **Optionality** | **Encoding format** |
| --- | --- | --- | --- | --- |
| legal_person_id | [legalIdentifier](https://w3id.org/ebwv#legalIdentifier) | EBW Organization Identifier, Identifier of the employing legal entity according to the European Business Wallet (EBW) framework | M | tstr |
| contact_person | [org:hasMembership](https://www.w3.org/ns/org#hasMembership).[org:member](https://www.w3.org/ns/org#member) | Object representing details of an individual contact person. This can be repeated for multiple contacts. | M (at least one) | Object |

### 3.2 Mandatory attributes

**LegalPerson Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition** | **Optionality** | **Encoding format** |
| --- | --- | --- | --- | --- |
| given_name | [givenName](https://w3id.org/ebwv#givenName)<br>[givenName – Schema.org Property](https://schema.org/givenName) | Given name. In the U.S., the first name of a Person. | M | tstr |
| family_name | [familyName](https://w3id.org/ebwv#familyName)<br>[familyName – Schema.org Property](https://schema.org/familyName) | Family name. In the U.S., the last name of a Person. | M | tstr |
| role | [org:role](https://www.w3.org/ns/org#role) | Denotes a role that a Person takes in an organization (e.g., sales, finance, quality, logistics) | M | tstr |
| employee_identifier | [employee](https://w3id.org/ebwv#employee).[identifier](https://w3id.org/ebwv#identifier) | An alphanumeric identifier of the employee assigned by the organization | M | tstr |
| email | [hasEmail](https://w3id.org/ebwv#hasEmail) <br> [Core Public Organisation Vocabulary (CPOV)](https://joinup.ec.europa.eu/collection/cpov) | An electronic address through which the Contact Person can be contacted | M | tstr |
| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |  |
| --------------------- | ------------------------ | ---------------------------------------------------------------------------- | --------------- |  |
| legal_person_name | , | The complete official legal name of the legal entity | String |  |
| legal_form_type | , | The legal form of the legal entity (e.g., SA, GmbH, Ltd, BV) | String |  |

**LegalEntity Attributes**
This object is defined once per attestation.

| **Data Identifier** | **Semantic Reference** | **Definition** | **Optionality** | **Encoding format** |
| --- | --- | --- | --- | --- |
| telephone | [hasTelephone](https://w3id.org/ebwv#hasTelephone) <br> [Core Public Organisation Vocabulary (CPOV)](https://joinup.ec.europa.eu/collection/cpov) | A telephone number through which the Contact Person can be contacted | O | tstr |
| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |  |
| :-------------------- | :----------------------- | :----------------------------------------------------------------------------------------------- | :-------------- |  |
| `identifier` | , | A structured object of legal entity identifiers; at least one sub-field **SHALL** be provided. | Object |  |

**ContactPerson Attributes**
This object is defined for each person represented in the Contact Person Attestation.

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| `given_name` | [givenName – Schema.org](https://schema.org/givenName) | The given name (first name) of the contact person. | String |
| `family_name` | [familyName – Schema.org](https://schema.org/familyName) | The family name (last name) of the contact person. | String |
| `role` | [The Organization Ontology](https://www.w3.org/TR/vocab-org/) | The designated function or role of the contact person. | String |
| `email` | [Core Public Organisation Vocabulary (CPOV)](https://joinup.ec.europa.eu/collection/cpov) | The email address of the contact person. | String |

### 3.3 Optional attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| issuance_date | [cred:validFrom](https://www.w3.org/2018/credentials/#validFrom) | The date and time when the attestation was issued (ISO 8601) | DateTime |
| expiry_date | [cred:validUntil](https://www.w3.org/2018/credentials/#validUntil) | The date and time when the attestation expires (ISO 8601) | DateTime |
| issuing_entity | [cred:issuer](https://www.w3.org/2018/credentials/#issuer) | The identifier of the legal entity that issued the attestation (typically the employing organization for self-issued EAA attestations) | String |
| attestation_legal_category | [attestationLegalCategory](https://w3id.org/ebwv#attestationLegalCategory) | Indicates the legal category of this attestation ("EAA") | String |
| vct |  | A URI or other collision-resistant identifier that defines the type of the SD-JWT Verifiable Credential | String |
**LegalEntity Identifier Optional Attributes**
At least one of the following sub-fields **SHALL** be provided within the `legal_entity.identifier` object.

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| `euid` | , | European Unique Identifier per ISO 3166-1 alpha-2. | String |
| `lei` | , | Legal Entity Identifier (LEI) per ISO 17442. | String |
| `tax` | , | National tax or company registration number. | String |
| `gln` | , | Global Location Number for legal entities (GS1 identifier). | String |
| `duns` | , | Data Universal Numbering System (Dun & Bradstreet identifier). | String |
| `eori` | , | Economic Operators Registration and Identification number (EU customs). | String |
| `bpnl` | , | Business Partner Number Legal entity (Catena-X identifier). | String |
| `siren` | , | Système d'Identification du Répertoire des ENtreprises (French identifier). | String |

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| trust_anchor_url | cred:? | URL where the trust anchor for verifying this attestation can be retrieved | URI |
| schema_version | cred:? | Version of the schema used | String |
**ContactPerson Optional Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| `telephone` | [Core Public Organisation Vocabulary (CPOV)](https://joinup.ec.europa.eu/collection/cpov) | The telephone number of the contact person. | String |

### 3.4 Conditional attributes

No conditional attributes are defined for this attestation type.

## 4 Metadata

Metadata describes the attestation rather than its subject.

### 4.1 Mandatory metadata

| **Data Identifier** | **Definition** | **Data type** |
| --- | --- | --- |
| `attestation_legal_category` | Indicates the legal category of the Attestation ("EAA"). | String |
| `cnf` | Cryptographic Key Binding to prove holder possession. | Object |

*Note: Standard JWT claims (`iss`, `iat`, `exp`) are also mandatory.*

| **Register Type** | **Example Identifier Format** |
| --- | --- |
| EU Company Register | EUID (e.g., DE-HRB-123456) |
| VAT Register | VAT number (e.g., DE123456789) |
| National Company Register | Country-specific registration ID |
| Gleif Register Authorities | [GLEIF Registration Authority List](https://www.gleif.org/en/lei-data/code-lists/gleif-registration-authorities-list?cachepath=de%2Flei-data%2Fcode-lists%2Fgleif-registration-authorities-list) |

| **Data Identifier** | **Definition** | **Data type** |
| --- | --- | --- |
| `trust_anchor_url` | URL where the trust anchor for verifying this attestation can be retrieved. | URI |
| `schema_version` | Version of the schema used for this attestation. | String |

**Legal category.** This Rulebook retains the `attestation_legal_category` attribute.
Section 4.1 of the generic template replaces it with the `category` attribute of
[ETSI TS 119 472-1], whose value for this category is `eaa:eu:non-qualified`.
EW-DM-12-029, legacy ARB_25, of ARF version 3.0.0 is a SHALL that still requires
`attestation_legal_category`, so the template and the ARF disagree. The attribute is
left as written and the deviation is recorded for the rulebook quality assurance group.

### 4.2 Optional metadata


### 4.3 Conditional metadata

No conditional metadata elements are defined for this attestation type.

### 4.4 Code lists

#### 4.4.1 Role Values
The `role` attribute SHOULD use descriptive role labels aligned with organizational functions. The following non-exhaustive list is provided for guidance:

| **Example Role Value** | **Definition** |
| --- | --- |
| `sales` | Responsible for sales and commercial relationships. |
| `finance` | Responsible for financial matters, invoicing, and payments. |
| `quality` | Responsible for quality assurance and non-conformance. |
| `logistics` | Responsible for delivery, shipping, and coordination. |
| `procurement` | Responsible for purchasing and supplier management. |
| `legal` | Responsible for legal and compliance matters. |

### 4.5 Integrity rules

The following integrity rules **SHALL** be enforced:
- `Legal_Entity` **SHALL** appear exactly once and **SHALL** contain `legal_person_name`, `legal_form_type`, and at least one `identifiers`.
- The `contact_persons` array **SHALL** contain at least one entry.
- Each `contact_person` entry **SHALL** contain a non-empty `given_name`, `family_name`, `role`, and `email`.
- `email` **SHALL** be a valid email address conforming to **RFC 4021**.
- `telephone`, if provided, **SHALL** conform to **ITU-T E.164**.


## 5 Formats


### 5.1 SD-JWT VC-based encoding

The Contact Person Attestation uses the SD-JWT VC format to allow for selective disclosure of contact attributes.

**Verifiable Credential Type (`vct`):** `eu.we-build:contactperson:1`

#### 5.1.1 Attribute Encoding Table

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
| **Contact Persons** | `contact_persons` | Array | Array of contact person objects; SHALL contain at least one entry. | MUST |
| **ContactPerson Attributes** | `contact_person` | Object |  |  |
| given_name | `given_name` | String | Given name of the contact person; [givenName – Schema.org](https://schema.org/givenName). | MUST |
| family_name | `family_name` | String | Family name of the contact person; [familyName – Schema.org](https://schema.org/familyName). | MUST |
| role | `role` | String | Role of the contact person; [Organization Ontology](https://www.w3.org/TR/vocab-org/). | MUST |
| email | `email` | String | Email address; SHALL conform to RFC 4021; [CPOV](https://joinup.ec.europa.eu/collection/cpov). | MUST |
| telephone | `telephone` | String | Telephone number; SHALL conform to ITU-T E.164; optional. | MUST |
| **Metadata** |  |  |  |  |
| issuance_date | `iat` | Number (Unix timestamp) | Date and time of issuance (RFC 7519). | MUST NOT |
| expiry_date | `exp` | Number (Unix timestamp) | Date and time of expiration (RFC 7519). | MUST NOT |
| issuing_entity | `iss` | String (URI or DID) | Identifier of the issuer (RFC 7519). | MUST NOT |
| attestation_legal_category | `attestation_legal_category` | String | "EAA" or "QEAA" as defined by eIDAS 2. | MUST NOT |
| vct | `vct` | String | The verifiable credential type definition. | MUST NOT |
| cnf | `cnf` | Object | Cryptographic Key Binding. | MUST NOT |
| trust_anchor_url | `trust_anchor_url` | String (URI) | URL to the trust anchor; optional. | MAY |
| schema_version | `schema_version` | String | Version of the schema used; optional. | MAY |

#### 5.1.2 Status Claim
For SD-JWT VC-compliant Attestations, the attestation MUST include a `status` claim if the technical validity period is greater than 24 hours.

The `status` claim SHALL be a JSON object with the following members:

| **Field** | **Type** | **Value / Constraint** |
| --- | --- | --- |
| `type` | String | SHALL be `"status-list"` |
| `status_list_credential` | String (URI) | URI of the Status List Credential document |
| `status_list_index` | Integer (>= 0) | Zero-based index into the status list |
| `status_purpose` | String | SHALL be `"revocation"` |

**Example:**
```json
{
  "status": {
    "type": "status-list",
    "status_list_credential": "https://issuer.example.com/status/contactperson/2026",
    "status_list_index": 321,
    "status_purpose": "revocation"
  }
}
```

#### 5.1.3 Example Payload
Here is a non-normative example payload reflecting the new model:
```json
{
  "vct":"eu.we-build:contactperson:1",
  "iss":"did:example:webuild-company-456",
  "iat":1736935200,
  "exp":1768471200,
  "attestation_legal_category":"EAA",
  "schema_version":"1.0",
  "trust_anchor_url":"https://trust.webuildconsortium.eu/anchors/eidas-tl",

  "legal_entity": {
    "legal_person": {
      "legal_person_name": "Example GmbH",
      "legal_form_type": "GmbH"
    },
    "identifier": {
      "euid": "DE-HRB-123456",
      "lei": "5493001KJTIIGC8Y1R12",
      "tax": "DE123456789"
    }
  },

  "contact_persons":[
    {
      "given_name":"Anna",
      "family_name":"Schmidt",
      "role":"logistics",
      "email":"anna.schmidt@example.com",
      "telephone":"+4915123456789"
    },
    {
      "given_name":"Max",
      "family_name":"Mustermann",
      "role":"finance",
      "email":"max.mustermann@example.com"
    }
  ],
  
  "status":{
    "type":"status-list",
    "status_list_credential":"https://issuer.example.com/status/contactperson/2026",
    "status_list_index":321,
    "status_purpose":"revocation"
  },
  "cnf":{
    "jwk":{
      "kty":"EC",
      "crv":"P-256",
      "x":"TCAER19Zvu3OHF4j4W4vfSVoHIP1ILilDls7vCeGemc",
      "y":"ZxjiWWbZMQGHVWKVQ4hbSIirsVfuecCE6t4jT9F2HZQ"
    }
  }
}
```
Sample payloads are provided under ../data-schemas/sd-jwt/sample-data/contact-person-sd-jwt-sample.json

### 5.2 ISO/IEC 18013-5-compliant encoding

ISO/IEC 18013-5 is out of scope for this Rulebook.

### 5.3 W3C Verifiable Credentials Data Model-based encoding


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


**For EAA (Self-Issued / Standard Issuance)**:
- The issuer (i.e., the legal entity itself) issues the attestation based on the information and supporting documentation available at the time of issuance.
- The issuer is responsible for ensuring that the attested information remains accurate and must immediately revoke the attestation if any change occurs that affects the validity or accuracy of the underlying data.

The Issuer SHALL implement the base issuer obligation as defined in the Issuer Obligation specification:
https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-base/verifier-base-verification.md#41-issuer-obligations

### 7.3 Lifecycle management

The issuer sets the validity period of the attestation and reissues it when the
underlying facts change, revoking the superseded attestation as described in chapter 8.

### 7.4 Embedded disclosure policy

This attestation defines no embedded disclosure policy.

## 8 Revocation

An attestation SHALL remain valid only while its underlying information is accurate, complete, and legally effective.

#### 8.1 Revocation Mechanism
- Token Status List: The issuer must maintain an active IETF Token Status List (aligned with the Attestation Status List mechanism specified by the EU Commission).
- Credential Metadata: The metadata status_list must be populated in every issued CompanyInfo attestation, referencing the status list URI and the credential's specific index.

Authorized Authority: Only the authorized issuer (the self-issuing legal entity for EAA) may modify the status list entry.

#### 8.2 Revocation Triggers & Business Rules
- EAA Trigger (Manual Obligation): The self-issuing legal entity is under strict obligation to immediately update or revoke its EAA if its available documents, financial thresholds, or ownership structures change.

Relying Party Action: A revoked or suspended attestation must be treated as invalid for credential-validity purposes by all RPs.
The business interpretation is determined by the Relying Party's internal compliance policies.

## 9 Presentation

#### Base Verification Process
The Relying Party SHALL perform the base attestation verification process as defined in the Base Verification specification:
https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-base/verifier-base-verification.md

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

When receiving and processing an attestation, the Relying Party SHALL perform the following verification obligations.

### 9.2 Presentation modes

Remote presentation is in scope. Proximity presentation is in scope only where
chapter 5 records an mdoc encoding.

### 9.3 Transactional data

This Rulebook defines no transactional data.

## 10 Trust Framework

This chapter specifies the trust anchor mechanisms used by Relying Parties to establish trust in the issuer of an Electronic Attestation of Attributes (EAA) or a Qualified Electronic Attestation of Attributes (QEAA). The corresponding verification procedures are defined in Sections 4.2.2–4.2.4.

#### 10.1 Electronic Attestations of Attributes (EAAs)
For EAAs, trust is established through a cryptographic chain anchored in the Electronic Business Wallet Owner Identity Document (EBWOID).
The EBWOID SHALL be included in the header of every EAA. During EBWOID issuance, the EBWOID provider verifies that the public key contained in the EBWOID is owned by the Electronic Business Wallet (EBW) owner.

The Relying Party SHALL verify the EBWOID in accordance with the verification procedure defined in this Rulebook. Upon successful verification, the Relying Party obtains:
- assurance that the EBWOID was issued by an authorized provider and is not self-issued;
- the verified identity of the issuer, including its name and EUID (or another globally unique EBW owner identifier); and
- the public key authorized to verify the EAA signature.

Authorization of the issuer is subsequently determined in accordance with the Relying Party's internal policies. Such authorization MAY be based on locally maintained wallet configuration or on trusted jurisdiction- or domain-specific trust list services that identify issuers authorized for a particular type of EAA

**Trust anchor location**

The attribute or metadata carrying the trust anchor location contains at least the URL
at which a machine-readable version can be found or looked up.

## 11 References

| **Item Reference** | **Standard name/details** |
| --- | --- |
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
