# Attestation Rulebook for attestations of type Site

Category: non-qualified EAA

* **Author(s):**
  * [Dominic Hurni, SBB]
  * [Werner Folkendt, Robert Bosch GmbH]
* **Reviewer(s):**
  * [Florin Coptil, Robert Bosch GmbH]
* **Contact:**
  * [Dominic Hurni](mailto:dominic.hurni@sbb.ch) *
  * [Werner Folkendt](mailto:werner.folkendt@de.bosch.com) *
* **Sources:**
  * [Powerpoint](https://portal.webuildconsortium.eu/group/3/files/6256/collabora-online/edit/3001)
  * [Excel](https://portal.webuildconsortium.eu/group/3/files/5757/collabora-online/edit/2384)

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
   * [6.1 Issuance](#61-issuance)
   * [6.2 Presentation](#62-presentation)
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

The Site Attestation provides a standardized, verifiable digital representation of a specific
physical location (site) operated by an economic operator. It enables structured exchange of
site-level data for use in KYS (Know Your Supplier), KYC (Know Your Customer), supply chain
mapping, compliance verification, and regulatory audit processes.

The attributes listed in this attestation are required to automate cross-business processes
within supply management.

**Design Decisions**

This Site Attestation Rulebook is based on:
- European Business Wallet (EBW) framework and vocabulary v0.1 for economic operator
  identity linkage
- The Organization Ontology for site naming
- Core Location Vocabulary for address and site identifier structures
- CDDL representation types per [RFC 8610] for attribute encoding
- International Code Designator (ICD) 0243 for BPNL/BPNS identifiers as used in Catena-X
- Support for multiple site and economic operator identifier schemes (EUID, LEI, DUNS,
  EORI, VAT ID, BPNL, GLN, SIREN, BPNS, SIRET)

> **Note:** EUID is only available and mandatory for legal entities within the EU. Legal entities
> outside the EU, for which the EUCC is not available, can use the DUNS Legal Entity, LEI Legal
> Entity, or GLN Legal Entity attestation.

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

| **Term** | **Description** |
| --- | --- |
| Site | An operational business element conducted by a specific economic operator entity at a specific physical location |
| Economic Operator | A role of a European Business Wallet (EBW) owner, the legal entity that operates one or more sites |
| EBW | European Business Wallet, the digital wallet used by legal entities to hold and present verifiable attestations |
| EUCC | EU Company Certificate, attestation establishing the legal existence and identity of a legal entity within the EU |
| EUID | European Unique Identifier, the unique identifier assigned to legal entities registered within the EU per Directive (EU) 2017/1132; preferred main ID for economic operators within the EU |
| LEI | Legal Entity Identifier, a 20-character alphanumeric code per ISO 17442 |
| DUNS | Data Universal Numbering System, Dun & Bradstreet company identifier |
| EORI | Economic Operators Registration and Identification number, EU customs identifier |
| BPNL | Business Partner Number Legal entity, Catena-X identifier per ICD 0243 |
| BPNS | Business Partner Number Site, Catena-X site-level identifier per ICD 0243 |
| GLN | Global Location Number, a GS1 identifier for legal entities and locations |
| SIREN | Système d'Identification du Répertoire des ENtreprises, French company identifier |
| SIRET | Système d'Identification du Répertoire des ETablissements, French site-level identifier |
| site_main_id | A globally unique identifier created by the Economic Operator using his EBW; generated as a UUID and stable throughout the lifecycle of the site |
| KYC | Know Your Customer, due diligence process for verifying customer identity and assessing risk in financial relationships |
| KYS | Know Your Supplier, due diligence process for verifying supplier credentials, integrity, and risk exposure |
| EAA | Electronic Attestation of Attributes, as defined under eIDAS 2.0 |
| RFC 8610 | Concise Data Definition Language (CDDL) for encoding data structures |
| Core Location Vocabulary | W3C vocabulary for representing addresses and location data in a structured, interoperable format |

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

Where the attestation is issued as a qualified electronic attestation of attributes,
the trust model of chapter 10 applies in its qualified form and the legal category
recorded in section 4.1 changes accordingly.

### 2.3 Traceability

Every applicable requirement mapped to the section that satisfies it. Requirements
marked not applicable carry a stated reason.

| Requirement | Legacy ID | Applies | Satisfied in section | Note |
| --- | --- | --- | --- | --- |
| EW-DM-12-001 | ARB_01a | yes | 5 | W3C VCDM permitted for this category; no encoding defined in this version |
| EW-DM-12-002 | ARB_01b | yes | 5.1 | SD-JWT VC following the HAIP profile |
| EW-DM-12-003 | ARB_02 | no |  | Proximity presentation is not in scope; mdoc is out of scope per section 5.2 |
| EW-DM-12-005 | ARB_04 | no |  | No W3C VCDM encoding is defined in this version |
| EW-DM-12-006 | ARB_05 | yes | 5.1 | Unique vct for this attestation type |
| EW-DM-12-007 | ARB_06 | yes | 3 | Attributes defined independently of encoding |
| EW-DM-12-008 | ARB_06a | no |  | No mdoc encoding is defined in this version |
| EW-DM-12-009 | ARB_06b | yes | 5.1 | SD-JWT VC claim naming |
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
| EW-DM-12-034 | ARB_30 | yes | 5.1 | Selective disclosure stated per claim |
| EW-DM-12-035 | ARB_31 | no |  | No Claim Selective Disclosure Metadata document is used |
| EW-DM-12-038 | ARB_34 | yes | 7.1 | Device binding |

## 3 Attestation attributes

The Site Attestation provides a standardized, verifiable digital representation of a specific physical location (site) operated by an economic operator. It captures the essential attributes required to uniquely identify a site, link it to its operating economic operator, and support cross-business processes within supply chain management and compliance verification.

Attributes are defined here in an encoding-independent manner (EW-DM-12-007). The
encoding of each attribute is given in chapter 5.

### 3.1 Introduction

The data model for the Site Attestation is structured as follows:

**Data Model:**
[Economic Operator] ---operates--- [Site] [1 - 1 ]
```
├─ name (string), mandatory
├─ identifier (uuid), mandatory
├─ additional_identifiers - optional 
│   ├─ gln (str) (O)                          // Global Location Number for site 
│   ├─ duns (str) (O)                         // duns number for site 
│   ├─ bpns (str) (O)                         // Business Partner Number Site
│   ├─ siret (str) (O)                        // Système d'Identification du Répertoire des Établissements
├─ address (Address) (M)           
│   ├─ street (tstr) (M)
│   ├─ house_number (tstr) (M)
│   ├─ locality (tstr) (M)
│   ├─ region (tstr) (M)
│   ├─ postal_code (tstr) (M)
│   └─ country (tstr) (M)                       // ISO 3166-1 alpha-2
└─ additional_addresses [0..n]                  //(Array of Address) 
│   ├─ street (tstr) (M)
│   ├─ house_number (tstr) (M)
│   ├─ locality (tstr) (M)
│   ├─ region (tstr) (M)
│   ├─ postal_code (tstr) (M)
│   └─ country (tstr) (M)                       // ISO 3166-1 alpha-2
├── economic_operator (M) 
│   ├─ identifier  (M)                    
│   │   ├─ euid (str) (O)                       // European Unique Identifier
│   │   ├─ lei (str) (O)                        // Legal Entity Identifier per ISO 17442
│   │   ├─ tax (str) (O)                        // National tax or registration number    
│   │   ├─ gln (str) (O)                        // Global Location Number for legal entities, GS1 identifier
│   │   ├─ duns (str) (O)                       // Data Universal Numbering System, Dun & Bradstreet identifier
│   │   ├─ eori (str) (O)                       // Economic Operators Registration and Identification number, EU customs identifier
│   │   ├─ bpnl (str) (O)                       // Business Partner Number Legal entity, Catena-X identifier per ICD 0243
│   │   ├─ siren (str) (O)                      // Système d'Identification du Répertoire des ENtreprises, French company identifier
```
*Note*: M - mandatory / O - optional.

**Explanation:**

- The root object of the attestation is the `Site`.
- A `Site` is defined by its mandatory `name`, a unique `identifier` (UUID), and its primary `address`.
- It is optionally possible to add `additional_identifiers` (like GLN, DUNS, BPNS for the site) and a list of `additional_addresses`.
- Each `Site` attestation **SHALL** contain a mandatory `economic_operator` object, which links the site to the legal entity that operates it.
- The `economic_operator` object **SHALL** contain an `identifier` object with at least one official identifier of the legal entity (e.g., `euid`, `lei`, `bpnl`).

**Attestation Classification:**

This attestation type is classified as:
- **"EAA"** when self-issued by the economic operator operating the site.

**Top-Level Data Identifiers:**

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| parent_economic_operator_main_id | [parent](https://w3id.org/ebwv#parent).[legalIdentifier](https://w3id.org/ebwv#legalIdentifier) | Primary unique identifier of the economic operator that operates this site (preferred: EUID) | String |
| parent_economic_operator_additional_id | [parent](https://w3id.org/ebwv#parent).[identifier](https://w3id.org/ebwv#identifier) | Array of additional identifiers for the economic operator | Array of Strings |
| site_name | [schema:name](https://schema.org/name) | The name of the site | String |
| site_main_id | @id | Globally unique identifier of the site, generated by the EBW as a UUID | UUID (String) |
| site_additional_ids | [identifier](https://w3id.org/ebwv#identifier) | Array of additional site-level identifiers | Array of Strings |
| site_main_address | [hasAddress](https://w3id.org/ebwv#hasAddress) | Physical main address of the site | Object (Address) |
| site_additional_addresses | [hasAddress](https://w3id.org/ebwv#hasAddress) | Array of additional addresses associated to the site | Array of Address |

### 3.2 Mandatory attributes

**Site Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Existing Vocabularies** |
| --- | --- | --- | --- | --- |
| parent_economic_operator_main_id | [parent](https://w3id.org/ebwv#parent).[legalIdentifier](https://w3id.org/ebwv#legalIdentifier) | The Economic Operator ID containing at least one ID (preferred: EUID) | String | European Business Wallet Vocabulary v0.1 |
| site_name | [schema:name](https://schema.org/name) | The name of the site | String | The Organization Ontology |
| site_main_id | [identifier](https://w3id.org/ebwv#identifier) | A globally unique identifier created by the Economic Operator using his EBW. The identifier is an attribute of the site that will not change during the lifecycle of the site | UUID | UUID generated by the wallet via API call |
| site_main_address | [hasAddress](https://w3id.org/ebwv#hasAddress) | Physical main address of the site | Address object | Core Location Vocabulary |

**Nested Mandatory Attributes**

Applies to both `site_main_address` and entries within `site_additional_addresses`:

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| street | [thoroughfare](https://w3id.org/ebwv#thoroughfare) | Street name of the address | String |
| nr | [locatorDesignator](https://w3id.org/ebwv#locatorDesignator) | House or building number of the address | String |
| postal_code | [postCode](https://w3id.org/ebwv#postCode) | Postal code of the address | String |
| city | [postName](https://w3id.org/ebwv#postName) | City of the address | String |

### 3.3 Optional attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Existing Vocabularies** |
| --- | --- | --- | --- | --- |
| parent_economic_operator_additional_id | [identifier](https://w3id.org/ebwv#identifier) | Array of additional economic operator identifiers. **MAY** contain zero or more entries. **SHALL** use identifier types from Section 2.8.1 | Array of Strings [0..n] | European Business Wallet Vocabulary v0.1 |
| site_additional_ids | [identifier](https://w3id.org/ebwv#identifier) | Array of additional site identifiers associated to this site. **MAY** contain zero or more entries. **SHALL** use identifier types from Section 2.8.2 | Array of Strings [0..n] | Core Location Vocabulary |
| site_additional_addresses | [hasAddress](https://w3id.org/ebwv#hasAddress) | Array of additional addresses associated to the site (e.g., additional entrances or addresses of external/rented buildings used by the site). **MAY** contain zero or more entries | Array of Address [0..n] | Core Location Vocabulary |

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| `additional_identifiers` | [identifier](https://w3id.org/ebwv#identifier) | An object containing additional standardized identifiers for the site itself (e.g., BPNS, SIRET). | Object |
| `additional_addresses` | [hasAddress](https://w3id.org/ebwv#hasAddress) | An array of additional addresses associated with the site (e.g., other entrances, rented buildings). | [Address](https://w3id.org/ebwv#Address) |

**Economic Operator Identifier Optional Attributes**
At least one of the following sub-fields **SHALL** be provided within the `economic_operator.identifier` object.

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| `euid` | , | European Unique Identifier per Directive (EU) 2017/1132. | [Euid](https://w3id.org/ebwv#Euid) |
| `lei` | , | Legal Entity Identifier (LEI) per ISO 17442. | [Lei](https://w3id.org/ebwv#Lei) |
| `tax` | , | National tax or company registration number. | [Tin](https://w3id.org/ebwv#Tin) |
| `gln` | , | Global Location Number for legal entities (GS1 identifier). | [GlobalLocationNumber](https://w3id.org/ebwv#GlobalLocationNumber) |
| `duns` | , | Data Universal Numbering System (Dun & Bradstreet identifier). | [DunsNumber](https://w3id.org/ebwv#DunsNumber) |
| `eori` | , | Economic Operators Registration and Identification number (EU customs). | [Eori](https://w3id.org/ebwv#Eori) |
| `bpnl` | , | Business Partner Number Legal entity (Catena-X identifier). | String |
| `siren` | , | Système d'Identification du Répertoire des ENtreprises (French identifier). | String |

### 3.4 Conditional attributes

No conditional attributes are defined for this attestation type.

## 4 Metadata

Metadata describes the attestation rather than its subject.

### 4.1 Mandatory metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| issuance_date | [cred:validFrom](https://www.w3.org/2018/credentials/#validFrom) | The date and time when the Site Attestation was issued (ISO 8601) | DateTime |
| expiry_date | [cred:validUntil](https://www.w3.org/2018/credentials/#validUntil) | The date and time when the Site Attestation expires (ISO 8601) | DateTime |
| issuing_entity | [cred:issuer](https://www.w3.org/2018/credentials/#issuer) | The identifier of the economic operator that issued the attestation (typically the subject entity itself for self-issued EAA) | String |
| attestation_legal_category | [attestationLegalCategory](https://w3id.org/ebwv#attestationLegalCategory) | Indicates the legal category of this attestation ("EAA") | String |
| vct |  | A unique identifier (URL or URN) for the credential type, indicating which claims must be present and which can be selectively disclosed | String |

*Note: Standard JWT claims (`iss`, `iat`, `exp`) are also mandatory.*

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| trust_anchor_url | [cred:termsOfUse](https://www.w3.org/2018/credentials/#termsOfUse) | URL where the trust anchor for verifying this attestation can be retrieved | URI |
| schema_version | @context | Version of the schema used for this attestation | String |

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

#### 2.8.1 Economic Operator Identifier Type Codes
The `economic_operator.identifier` object **SHOULD** use one or more of the following standardized identifier types as keys:

| **Code** | **Definition** |
| --- | --- |
| `euid` | European Unique Identifier per Directive (EU) 2017/1132. |
| `lei` | Legal Entity Identifier per ISO 17442. |
| `tax` | National tax or company registration number. |
| `gln` | Global Location Number for legal entities (GS1 identifier). |
| `duns` | Data Universal Numbering System (Dun & Bradstreet identifier). |
| `eori` | Economic Operators Registration and Identification number (EU customs). |
| `bpnl` | Business Partner Number Legal entity (Catena-X identifier per ICD 0243). |
| `siren` | Système d'Identification du Répertoire des ENtreprises (French identifier). |

#### 2.8.2 Site Identifier Type Codes
The `additional_identifiers` object **SHOULD** use one or more of the following standardized site-level identifier types as keys:

| **Code** | **Definition** |
| --- | --- |
| `gln` | Global Location Number for physical locations (GS1 site-level identifier). |
| `duns` | DUNS site-level identifier issued by Dun & Bradstreet. |
| `bpns` | Business Partner Number Site (Catena-X site-level identifier per ICD 0243). |
| `siret` | Système d'Identification du Répertoire des ETablissements (French site-level identifier). |

### 4.5 Integrity rules

- The root `Site` object SHALL be present.
- `name`, `identifier`, `address`, and `economic_operator` SHALL be present and non-empty.
- The `identifier` for the site SHALL be a valid UUID.
- The `economic_operator.identifier` object SHALL contain at least one valid, non-empty identifier sub-field.
- All `Address` objects SHALL contain non-empty `street`, `house_number`, `locality`, `postal_code`, and `country`.

## 5 Formats

| Format | Supported | Identifier | Specification | Notes |
| --- | --- | --- | --- | --- |
| ISO/IEC 18013-5 mdoc | no |  | [ISO/IEC 18013-5] | Out of scope, see section 5.2 |
| SD-JWT VC | yes | see section 5.1 | [SD-JWT VC], [HAIP] |  |
| W3C VCDM | no |  | [W3C VCDM v2.0] | Not defined in this version, see section 5.3 |

### 5.1 SD-JWT VC-based encoding

The Site Attestation uses the SD-JWT VC format to allow for selective disclosure.

**Verifiable Credential Type (`vct`):** `eu.we-build:site:1`

##### 3.2.1 Attribute Encoding Table

| **Data Identifier** | **Attribute Identifier** | **Encoding Format** | **Reference/Notes** | **Disclosable** |
| --- | --- | --- | --- | --- |
| **Site Details** |  |  |  |  |
| name | `name` | String | The common name of the site. | MUST |
| identifier | `identifier` | String (UUID) | Unique identifier for the site. | MUST |
| **Additional Site Identifiers** | `additional_identifiers` | Object | Object containing other site IDs. | MUST |
| gln | `additional_identifiers.gln` | String | GS1 Global Location Number for the site. | MUST |
| duns | `additional_identifiers.duns` | String | Dun & Bradstreet number for the site. | MUST |
| bpns | `additional_identifiers.bpns` | String | Catena-X Business Partner Number for the site. | MUST |
| siret | `additional_identifiers.siret` | String | French SIRET number for the establishment. | MUST |
| **Main Address** | `address` | Object | The primary address of the site. | MUST |
| street | `address.street` | String | Street name of the primary address. | MUST |
| house\_number | `address.house_number` | String | House number of the primary address. | MUST |
| locality | `address.locality` | String | Locality of the primary address. | MUST |
| region | `address.region` | String | Region of the primary address. | MUST |
| postal\_code | `address.postal_code` | String | Postal code of the primary address. | MUST |
| country | `address.country` | String | Country of the primary address. | MUST |
| **Additional Addresses** | `additional_addresses` | Array | Array of additional site addresses. | MUST |
| **Economic Operator** | `economic_operator` | Object | The operating legal entity. | MUST |
| euid | `economic_operator.identifier.euid` | String | European Unique Identifier. | MUST |
| lei | `economic_operator.identifier.lei` | String | Legal Entity Identifier. | MUST |
| tax | `economic_operator.identifier.tax` | String | National tax/registration number. | MUST |
| bpnl | `economic_operator.identifier.bpnl` | String | Catena-X BPNL identifier. | MUST |
| **Metadata** |  |  |  |  |
| issuance_date | `iat` | Number | Issuance timestamp. | MUST NOT |
| expiry_date | `exp` | Number | Expiration timestamp. | MUST NOT |
| issuing_entity | `iss` | String | Identifier of the issuer. | MUST NOT |
| attestation\_legal\_category | `attestation_legal_category` | String | "EAA" | MUST NOT |
| vct | `vct` | String | Verifiable Credential Type. | MUST NOT |
| cnf | `cnf` | Object | Cryptographic Key Binding. | MUST NOT |
| trust_anchor_url | `trust_anchor_url` | String (URI) | Optional URL to the trust anchor. | MAY |
| schema_version | `schema_version` | String | Optional version of the schema. | MAY |

##### 3.2.2 Status Claim
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
    "status_list_credential": "https://issuer.example.com/status/site/2026",
    "status_list_index": 789,
    "status_purpose": "revocation"
  }
}
```
#### 3.2.3 Example Payload

The following is a non-normative example of a Site Attestation SD-JWT VC payload:

```
{
  "vct": "eu.we-build:site:1",
  "iss": "did:example:robert-bosch-gmbh",
  "iat": 1746000000,
  "exp": 1777536000,
  "attestation_legal_category": "EAA",
  "name": "Bosch Karlsruhe Manufacturing Site",
  "identifier": "urn:uuid:550e8400-e29b-41d4-a716-446655440000",
  "additional_identifiers": {
    "bpns": "BPNS0000000001XY",
    "gln": "4012345000016"
  },
  "address": {
    "street": "Auf der Breit",
    "house_number": "4",
    "locality": "Karlsruhe",
    "region": "Baden-Württemberg",
    "postal_code": "76227",
    "country": "DE"
  },
  "additional_addresses": [
    {
      "street": "Robert-Bosch-Strasse",
      "house_number": "2",
      "locality": "Karlsruhe",
      "region": "Baden-Württemberg",
      "postal_code": "76131",
      "country": "DE"
    }
  ],
  "economic_operator": {
    "identifier": {
      "euid": "DE.HRB.12345",
      "bpnl": "BPNL00000003CML1"
    }
  },
  "status": {
    "type": "status-list",
    "status_list_credential": "https://issuer.example.com/status/site/2026",
    "status_list_index": 789,
    "status_purpose": "revocation"
  },
  "cnf": {
    "jwk": {
      "kty": "EC",
      "crv": "P-256",
      "x": "TCAER19Zvu3OHF4j4W4vfSVoHIP1ILilDls7vCeGemc",
      "y": "ZxjiWWbZMQGHVWKVQ4hbSIirsVfuecCE6t4jT9F2HZQ"
    }
  }
}
```
Sample payloads are provided under  ../data-schemas/sd-jwt/sample-data/site-attestation-sd-jwt-sample.json

### 5.2 ISO/IEC 18013-5-compliant encoding

ISO/IEC 18013-5 is out of scope for this Rulebook.

### 5.3 W3C Verifiable Credentials Data Model-based encoding

@TODO, To be discussed: which stakeholders will support this format and which use cases require it.

## 6 Protocols

### 6.1 Issuance

This attestation is issued using OpenID for Verifiable Credential Issuance
[OpenID4VCI], as profiled by [HAIP].

### 6.2 Presentation

This attestation is presented using OpenID for Verifiable Presentations [OpenID4VP].
Only remote presentation is in scope, consistent with chapter 5, which records the
mdoc encoding as out of scope.

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

**For QEAA (Qualified Issuance)**:
- The issuer-either a Qualified Trust Service Provider (QTSP) or another authorized competent body-must issue and verify the attestation exclusively on the basis of authoritative sources, such as official company register data or audited financial statements.
- The issuer is also responsible for maintaining a high level of assurance throughout the attestation's validity period by continuously monitoring the underlying information. If any change affecting the accuracy or validity of the attested data is detected, the issuer must promptly revoke the attestation.

The Issuer SHALL implement the base issuer obligation as defined in the Issuer Obligation specification:
https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-base/verifier-base-verification.md#41-issuer-obligations

### 7.3 Lifecycle management

The issuer sets the validity period of the attestation and reissues it when the
underlying facts change, revoking the superseded attestation as described in chapter 8.

### 7.4 Embedded disclosure policy

This attestation defines no embedded disclosure policy.

## 8 Revocation

An attestation SHALL remain valid only while its underlying information is accurate, complete, and legally effective.

**Revocation Mechanism**
- Token Status List: The issuer must maintain an active IETF Token Status List (aligned with the Attestation Status List mechanism specified by the EU Commission).
- Credential Metadata: The metadata status_list must be populated in every issued CompanyInfo attestation, referencing the status list URI and the credential's specific index.

Authorized Authority: Only the authorized issuer (the QTSP/competent body for QEAA, or the self-issuing legal entity for EAA) may modify the status list entry.

**Revocation Triggers & Business Rules**
- QEAA Trigger (Automatic): The QTSP/competent body must actively monitor official company register data and audited financial statements. Any detected discrepancy or change in the company registry must automatically trigger revocation of the QEAA.
- EAA Trigger (Manual Obligation): The self-issuing legal entity is under strict obligation to immediately update or revoke its EAA if its available documents, financial thresholds, or ownership structures change.

Relying Party Action: A revoked or suspended attestation must be treated as invalid for credential-validity purposes by all RPs.
The business interpretation is determined by the Relying Party's internal compliance policies.

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

Obligations specific to this attestation type, carried over from the Relying Party
obligations of the previous version of this Rulebook:

When receiving and processing an attestation, the Relying Party SHALL perform the following verification obligations.

#### 4.2.1 – 4.2.8 Base Verification Process
The Relying Party SHALL perform the base attestation verification process as defined in the
Base Verification specification:
https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-base/verifier-base-verification.md#42-relying-party-obligations

#### 4.2.9 Validate Integrity Rules
Validation of integrity and policy rules will be specified in a future version of this Rulebook.

### 9.2 Presentation modes

Remote presentation is in scope. Proximity presentation is not in scope, consistent
with chapter 5, which records the mdoc encoding as out of scope.

### 9.3 Transactional data

This Rulebook defines no transactional data.

## 10 Trust Framework

The trust anchor is obtained as described in the branch below that corresponds to the
legal category under which the attestation was issued.

This chapter specifies the trust anchor mechanisms used by Relying Parties to establish trust in the issuer of an Electronic Attestation of Attributes (EAA) or a Qualified Electronic Attestation of Attributes (QEAA). The corresponding verification procedures are defined in Sections 4.2.2–4.2.4.

**Qualified Electronic Attestations of Attributes (QEAAs)**

For QEAAs, trust is established through the X.509 Public Key Infrastructure (PKI) and the applicable Trust List of Licensees (TLOL).
The issuer's certificate chain, including the intermediate certificate contained in the QEAA header, SHALL be validated up to a trusted root certificate. This validation SHALL be performed using the applicable TLOL, taking into account the trust list state applicable at the time of issuance.

Successful certificate chain validation establishes that:
- the issuer's certificate was recognized within the applicable trust framework;
- the issuer's identity has been validated by the supervisory authority during inclusion in the TLOL; and
- the issuer satisfies the trust requirements applicable to QEAAs.

In addition, the Relying Party MAY apply further authorization checks based on its internal policies, such as maintaining a whitelist of accepted QEAA providers.

**Electronic Attestations of Attributes (EAAs)**

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
| [ISO 8601] | ISO 8601, Date and time format. Available: https://www.iso.org/iso-8601-date-and-time-format.html |
| [OIDC] | Sakimura, N. et al., "OpenID Connect Core 1.0", OpenID Foundation. Available: https://openid.net/specs/openid-connect-core-1_0.html |
| [RFC 2119] | RFC 2119, Key words for use in RFCs to Indicate Requirement Levels, S. Bradner, March 1997 |
| [RFC 3339] | RFC 3339, Date and Time on the Internet: Timestamps, G. Klyne et al., July 2002 |
| [RFC 8610] | RFC 8610, Concise Data Definition Language (CDDL): A Notational Convention to Express Concise Binary Object Representation (CBOR) and JSON Data Structures, H. Birkholz et al., June 2019 |
| [RFC 8943] | RFC 8943, Concise Binary Object Representation (CBOR) Tags for Date, M. Jones et al., November 2020 |
| [RFC 8949] | RFC 8949, Concise Binary Object Representation (CBOR), C. Bormann et al., December 2020 |
| [SD-JWT VC] | SD-JWT-based Verifiable Credentials (SD-JWT VC). Available: https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/, version draft-ietf-oauth-sd-jwt-vc-09 |
| [Topic 7] | ARF Annex 2 - Topic 7 - Attestation revocation and revocation checking. Available: https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a237-topic-7-attestation-revocation-and-revocation-checking |
