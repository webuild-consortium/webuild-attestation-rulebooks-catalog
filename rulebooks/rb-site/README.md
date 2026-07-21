# Attestation Rulebook for attestations of type Site Attestation

* **Author(s):**
  * [Dominic Hurni, SBB]
  * [Werner Folkendt, Robert Bosch GmbH]

* **Reviewer(s):**
  * [Florin Coptil, Robert Bosch GmbH]

| Version | Date       | Description                                                    |
|---------|------------|----------------------------------------------------------------|
| 0.4     | 19.05.2026 | Initial draft based on the WeBuild design attestation meetings |
| 0.6     | 29.06.2026 | Layout and identifiers update  |
| 0.9     | 03.07.2026 | Updates in regard trust and revocation                            |

* **Contact:**
  * [Dominic Hurni](mailto:dominic.hurni@sbb.ch) *
  * [Werner Folkendt](mailto:werner.folkendt@de.bosch.com) *

* **Sources:**
  * [Powerpoint](https://portal.webuildconsortium.eu/group/3/files/6256/collabora-online/edit/3001)
  * [Excel](https://portal.webuildconsortium.eu/group/3/files/5757/collabora-online/edit/2384)

## 1 Introduction

This attestation addresses the following question:

**Where does the responsible economic operator operate his business, and what unique
identifiers are associated to a site?**

The Site Attestation provides a standardized, verifiable digital representation of a specific
physical location (site) operated by an economic operator. It enables structured exchange of
site-level data for use in KYS (Know Your Supplier), KYC (Know Your Customer), supply chain
mapping, compliance verification, and regulatory audit processes.

A site is defined as an operational business element conducted by a specific economic operator
entity at a specific physical location. An economic operator is a role of a European Business
Wallet Owner (EBW owner).

The Site Attestation is **NOT** designed to provide Economic Operator specific data such as
NACE code, tax information, nor attestations regarding the operating Economic Operator. These
data are provided by EBW owner attestations like EUCC, EBWOID, and others. The site
attestation **MUST** be linked to the economic operator by providing at least one unique
identifier associated to the Economic Operator.

Transparency in supply chain requires clarity about location and operation of an economic
operator's sites, for example to define incoterms, track products, or calculate CO2eq emissions.

Examples:
- A legal entity delivers goods to 10 other companies and operates from a hired site.
- A legal entity operates in 100 manufacturing sites and has to declare from which site the
  product is delivered.

The added value for a company to have "site" as an attestation is to automate contracting
processes in offering, delivering, creating digital product passports and reporting, customs and
other authorities.

Economic Operator attestations (like EUCC, LEI, DUNS legal entity, ...) help to answer
KYC/KYS questions like:
- Who signs the contract?
- Who bears liability?
- Corporate hierarchy?

The Site Attestation helps to answer questions like:
- Where does the work get performed?
- Which facility is in scope?
- What operational risk do we have?
- For which establishments do we need which compliance attestations? (e.g., ISO 9000, ...)

Together, they support key KYC/KYS topics:
- Multi-site suppliers
- Site-specific approvals
- Regulatory audits
- Supply-chain mapping

### 1.1 Document Scope and Purpose

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

### 1.2 Document Structure

This Rulebook is structured as follows:

- Chapter 2 describes the attestation attributes and metadata in an encoding-independent manner, including the data model.
- Chapter 3 specifies how the attestation attributes and metadata are encoded: Section 3.2 covers SD-JWT VC-based encoding.
- Chapter 4 specifies attestation usage scenarios, Relying Party obligations, and integration with KYC/KYS workflows.
- Chapter 5 defines trust anchors and verification mechanisms for issuer authorization.
- Chapter 6 defines revocation mechanisms for the attestation.
- Chapter 7 provides compliance information regarding the EUDI framework and applicable data protection laws.

### 1.3 Keywords

This document uses the capitalised keywords `SHALL`, `SHOULD` and `MAY` as specified in
[RFC 2119], i.e. to indicate requirements, recommendations and options specified in this document.

In addition, `must` (non-capitalised) is used to indicate an external constraint, i.e. a
requirement that is not mandated by this document, but, for instance, by an external document.
The word `can` indicates a capability, whereas other words, such as `will`, and `is` or `are`
are intended as statements of fact.

### 1.4 Terminology

*Additional terminology specific to this attestation:*

| **Term**                 | **Description**                                                                                                                                                                              |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Site                     | An operational business element conducted by a specific economic operator entity at a specific physical location                                                                              |
| Economic Operator        | A role of a European Business Wallet (EBW) owner — the legal entity that operates one or more sites                                                                                          |
| EBW                      | European Business Wallet — the digital wallet used by legal entities to hold and present verifiable attestations                                                                              |
| EUCC                     | EU Company Certificate — attestation establishing the legal existence and identity of a legal entity within the EU                                                                            |
| EUID                     | European Unique Identifier — the unique identifier assigned to legal entities registered within the EU per Directive (EU) 2017/1132; preferred main ID for economic operators within the EU  |
| LEI                      | Legal Entity Identifier — a 20-character alphanumeric code per ISO 17442                                                                                                                     |
| DUNS                     | Data Universal Numbering System — Dun & Bradstreet company identifier                                                                                                                        |
| EORI                     | Economic Operators Registration and Identification number — EU customs identifier                                                                                                             |
| BPNL                     | Business Partner Number Legal entity — Catena-X identifier per ICD 0243                                                                                                                      |
| BPNS                     | Business Partner Number Site — Catena-X site-level identifier per ICD 0243                                                                                                                   |
| GLN                      | Global Location Number — a GS1 identifier for legal entities and locations                                                                                                                   |
| SIREN                    | Système d'Identification du Répertoire des ENtreprises — French company identifier                                                                                                            |
| SIRET                    | Système d'Identification du Répertoire des ETablissements — French site-level identifier                                                                                                     |
| site_main_id             | A globally unique identifier created by the Economic Operator using his EBW; generated as a UUID and stable throughout the lifecycle of the site                                              |
| KYC                      | Know Your Customer — due diligence process for verifying customer identity and assessing risk in financial relationships                                                                       |
| KYS                      | Know Your Supplier — due diligence process for verifying supplier credentials, integrity, and risk exposure                                                                                   |
| EAA                      | Electronic Attestation of Attributes — as defined under eIDAS 2.0                                                                                                                            |
| RFC 8610                 | Concise Data Definition Language (CDDL) for encoding data structures                                                                                                                         |
| Core Location Vocabulary | W3C vocabulary for representing addresses and location data in a structured, interoperable format                                                                                            |

## 2 Attestation Attributes and Metadata

The Site Attestation provides a standardized, verifiable digital representation of a specific physical location (site) operated by an economic operator. It captures the essential attributes required to uniquely identify a site, link it to its operating economic operator, and support cross-business processes within supply chain management and compliance verification.

### 2.1 Introduction
The data model for the Site Attestation is structured as follows:

**Data Model:**
[Economic Operator] ---operates--- [Site] [1 - 1 ]
```
├─ name (string) — mandatory
├─ identifier (uuid) — mandatory
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
│   │   ├─ gln (str) (O)                        // Global Location Number for legal entities — GS1 identifier
│   │   ├─ duns (str) (O)                       // Data Universal Numbering System — Dun & Bradstreet identifier
│   │   ├─ eori (str) (O)                       // Economic Operators Registration and Identification number — EU customs identifier
│   │   ├─ bpnl (str) (O)                       // Business Partner Number Legal entity — Catena-X identifier per ICD 0243
│   │   ├─ siren (str) (O)                      // Système d'Identification du Répertoire des ENtreprises — French company identifier
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

| **Data Identifier** | **Semantic Reference** | **Definition**                                            | **Data type** |
|:--------------------|:-----------------------|:----------------------------------------------------------|:--------------|
| `Site`              | —                      | The root object containing all site information.          | Object        |
| `economic_operator` | —                      | An object linking the site to its operating legal entity. | Object        |

### 2.2 Mandatory Attributes

**Site Attributes**

| **Data Identifier** | **Semantic Reference**                   | **Definition**                                                             | **Data type**  |
|:--------------------|:-----------------------------------------|:---------------------------------------------------------------------------|:---------------|
| `name`              | —                                        | The common name of the site.                                               | String         |
| `identifier`        | —                                        | A globally unique identifier (UUID) for the site, generated by the wallet. | String (UUID)  |
| `address`           | Core Location Vocabulary                 | The primary physical address of the site.                                  | Address Object |
| `economic_operator` | European Business Wallet Vocabulary v0.1 | Object linking the site to its operating legal entity.                     | Object         |

**Nested Mandatory Attributes**

| **Data Identifier**            | **Semantic Reference** | **Definition**                                                                           | **Data type** |
|:-------------------------------|:-----------------------|:-----------------------------------------------------------------------------------------|:--------------|
| `address.street`               | —                      | The street name of the address.                                                          | String        |
| `address.house_number`         | —                      | The house or building number of the address.                                             | String        |
| `address.locality`             | —                      | The city or locality of the address.                                                     | String        |
| `address.region`               | —                      | The state, province, or region of the address.                                           | String        |
| `address.postal_code`          | —                      | The postal code of the address.                                                          | String        |
| `address.country`              | —                      | The country of the address (ISO 3166-1 alpha-2).                                         | String        |
| `economic_operator.identifier` | —                      | An object of identifiers for the legal entity; **SHALL** contain at least one sub-field. | Object        |

### 2.3 Optional Attributes

**Site Optional Attributes**

| **Data Identifier**      | **Semantic Reference**   | **Definition**                                                                                       | **Data type**    |
|:-------------------------|:-------------------------|:-----------------------------------------------------------------------------------------------------|:-----------------|
| `additional_identifiers` | Core Location Vocabulary | An object containing additional standardized identifiers for the site itself (e.g., BPNS, SIRET).    | Object           |
| `additional_addresses`   | Core Location Vocabulary | An array of additional addresses associated with the site (e.g., other entrances, rented buildings). | Array of Address |

**Economic Operator Identifier Optional Attributes**
At least one of the following sub-fields **SHALL** be provided within the `economic_operator.identifier` object.

| **Data Identifier** | **Semantic Reference** | **Definition**                                                              | **Data type** |
|:--------------------|:-----------------------|:----------------------------------------------------------------------------|:--------------|
| `euid`              | —                      | European Unique Identifier per Directive (EU) 2017/1132.                    | String        |
| `lei`               | —                      | Legal Entity Identifier (LEI) per ISO 17442.                                | String        |
| `tax`               | —                      | National tax or company registration number.                                | String        |
| `gln`               | —                      | Global Location Number for legal entities (GS1 identifier).                 | String        |
| `duns`              | —                      | Data Universal Numbering System (Dun & Bradstreet identifier).              | String        |
| `eori`              | —                      | Economic Operators Registration and Identification number (EU customs).     | String        |
| `bpnl`              | —                      | Business Partner Number Legal entity (Catena-X identifier).                 | String        |
| `siren`             | —                      | Système d'Identification du Répertoire des ENtreprises (French identifier). | String        |

### 2.4 Conditional Attributes
No conditional attributes are defined for this attestation type.

### 2.5 Mandatory Metadata

| **Data Identifier**          | **Definition**                                           | **Data type**  |
|:-----------------------------|:---------------------------------------------------------|:---------------|
| `attestation_legal_category` | Indicates the legal category of the Attestation ("EAA"). | String         |
| `cnf`                        | Cryptographic Key Binding to prove holder possession.    | Object         |

*Note: Standard JWT claims (`iss`, `iat`, `exp`) are also mandatory.*

### 2.6 Optional Metadata

| **Data Identifier** | **Definition**                                                              | **Data type** |
|:--------------------|:----------------------------------------------------------------------------|:--------------|
| `trust_anchor_url`  | URL where the trust anchor for verifying this attestation can be retrieved. | URI           |
| `schema_version`    | Version of the schema used for this attestation.                            | String        |

### 2.7 Conditional metadata
No conditional metadata elements are defined for this attestation type.

### 2.8 Value Lists

#### 2.8.1 Economic Operator Identifier Type Codes
The `economic_operator.identifier` object **SHOULD** use one or more of the following standardized identifier types as keys:

| **Code**   | **Definition**                                                              |
|:-----------|:----------------------------------------------------------------------------|
| `euid`     | European Unique Identifier per Directive (EU) 2017/1132.                    |
| `lei`      | Legal Entity Identifier per ISO 17442.                                      |
| `tax`      | National tax or company registration number.                                |
| `gln`      | Global Location Number for legal entities (GS1 identifier).                 |
| `duns`     | Data Universal Numbering System (Dun & Bradstreet identifier).              |
| `eori`     | Economic Operators Registration and Identification number (EU customs).     |
| `bpnl`     | Business Partner Number Legal entity (Catena-X identifier per ICD 0243).    |
| `siren`    | Système d'Identification du Répertoire des ENtreprises (French identifier). |

#### 2.8.2 Site Identifier Type Codes
The `additional_identifiers` object **SHOULD** use one or more of the following standardized site-level identifier types as keys:

| **Code**   | **Definition**                                                                            |
|:-----------|:------------------------------------------------------------------------------------------|
| `gln`      | Global Location Number for physical locations (GS1 site-level identifier).                |
| `duns`     | DUNS site-level identifier issued by Dun & Bradstreet.                                    |
| `bpns`     | Business Partner Number Site (Catena-X site-level identifier per ICD 0243).               |
| `siret`    | Système d'Identification du Répertoire des ETablissements (French site-level identifier). |

### 2.9 Integrity Rules
- The root `Site` object SHALL be present.
- `name`, `identifier`, `address`, and `economic_operator` SHALL be present and non-empty.
- The `identifier` for the site SHALL be a valid UUID.
- The `economic_operator.identifier` object SHALL contain at least one valid, non-empty identifier sub-field.
- All `Address` objects SHALL contain non-empty `street`, `house_number`, `locality`, `postal_code`, and `country`.

## 3 Attestation Encoding

### 3.1 ISO/IEC 18013-5-compliant encoding
ISO/IEC 18013-5 is out of scope for this Rulebook.

### 3.2 SD-JWT VC-based encoding
The Site Attestation uses the SD-JWT VC format to allow for selective disclosure.

**Verifiable Credential Type (`vct`):** `eu.we-build:site:1`

#### 3.2.1 Attribute Encoding Table

| **Data Identifier**             | **Attribute Identifier**            | **Encoding Format** | **Reference/Notes**                            | **Disclosable** |
|:--------------------------------|:------------------------------------|:--------------------|:-----------------------------------------------|:----------------|
| **Site Details**                |                                     |                     |                                                |                 |
| name                            | `name`                              | String              | The common name of the site.                   | MUST            |
| identifier                      | `identifier`                        | String (UUID)       | Unique identifier for the site.                | MUST            |
| **Additional Site Identifiers** | `additional_identifiers`            | Object              | Object containing other site IDs.              | MUST            |
| gln                             | `additional_identifiers.gln`        | String              | GS1 Global Location Number for the site.       | MUST            |
| duns                            | `additional_identifiers.duns`       | String              | Dun & Bradstreet number for the site.          | MUST            |
| bpns                            | `additional_identifiers.bpns`       | String              | Catena-X Business Partner Number for the site. | MUST            |
| siret                           | `additional_identifiers.siret`      | String              | French SIRET number for the establishment.     | MUST            |
| **Main Address**                | `address`                           | Object              | The primary address of the site.               | MUST            |
| street                          | `address.street`                    | String              | Street name of the primary address.            | MUST            |
| house\_number                   | `address.house_number`              | String              | House number of the primary address.           | MUST            |
| locality                        | `address.locality`                  | String              | Locality of the primary address.               | MUST            |
| region                          | `address.region`                    | String              | Region of the primary address.                 | MUST            |
| postal\_code                    | `address.postal_code`               | String              | Postal code of the primary address.            | MUST            |
| country                         | `address.country`                   | String              | Country of the primary address.                | MUST            |
| **Additional Addresses**        | `additional_addresses`              | Array               | Array of additional site addresses.            | MUST            |
| **Economic Operator**           | `economic_operator`                 | Object              | The operating legal entity.                    | MUST            |
| euid                            | `economic_operator.identifier.euid` | String              | European Unique Identifier.                    | MUST            |
| lei                             | `economic_operator.identifier.lei`  | String              | Legal Entity Identifier.                       | MUST            |
| tax                             | `economic_operator.identifier.tax`  | String              | National tax/registration number.              | MUST            |
| bpnl                            | `economic_operator.identifier.bpnl` | String              | Catena-X BPNL identifier.                      | MUST            |
| **Metadata**                    |                                     |                     |                                                |                 |
| issuance_date                   | `iat`                               | Number              | Issuance timestamp.                            | MUST NOT        |
| expiry_date                     | `exp`                               | Number              | Expiration timestamp.                          | MUST NOT        |
| issuing_entity                  | `iss`                               | String              | Identifier of the issuer.                      | MUST NOT        |
| attestation\_legal\_category    | `attestation_legal_category`        | String              | "EAA"                                          | MUST NOT        |
| vct                             | `vct`                               | String              | Verifiable Credential Type.                    | MUST NOT        |
| cnf                             | `cnf`                               | Object              | Cryptographic Key Binding.                     | MUST NOT        |
| trust_anchor_url                | `trust_anchor_url`                  | String (URI)        | Optional URL to the trust anchor.              | MAY             |
| schema_version                  | `schema_version`                    | String              | Optional version of the schema.                | MAY             |

#### 3.2.2 Status Claim
For SD-JWT VC-compliant Attestations, the attestation MUST include a `status` claim if the technical validity period is greater than 24 hours.

The `status` claim SHALL be a JSON object with the following members:

| **Field**                | **Type**       | **Value / Constraint**                     |
|:-------------------------|:---------------|:-------------------------------------------|
| `type`                   | String         | SHALL be `"status-list"`                   |
| `status_list_credential` | String (URI)   | URI of the Status List Credential document |
| `status_list_index`      | Integer (>= 0) | Zero-based index into the status list      |
| `status_purpose`         | String         | SHALL be `"revocation"`                    |

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
### 3.2.3 Example Payload

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

### 3.3 W3C Verifiable Credentials Data Model-based encoding

@TODO — To be discussed: which stakeholders will support this format and which use cases require it.

## 4 Attestation usage

### 4.1. Issuance process ###
**For EAA (Self-Issued / Standard Issuance)**:
- The issuer (i.e., the legal entity itself) issues the attestation based on the information and supporting documentation available at the time of issuance.
- The issuer is responsible for ensuring that the attested information remains accurate and must immediately revoke the attestation if any change occurs that affects the validity or accuracy of the underlying data.

**For QEAA (Qualified Issuance)**:
- The issuer—either a Qualified Trust Service Provider (QTSP) or another authorized competent body—must issue and verify the attestation exclusively on the basis of authoritative sources, such as official company register data or audited financial statements.
- The issuer is also responsible for maintaining a high level of assurance throughout the attestation's validity period by continuously monitoring the underlying information. If any change affecting the accuracy or validity of the attested data is detected, the issuer must promptly revoke the attestation.

The Issuer SHALL implement the base issuer obligation as defined in the Issuer Obligation specification:
https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-base/verifier-base-verification.md#41-issuer-obligations

### 4.2 Relying Party Obligations
When receiving and processing an attestation, the Relying Party SHALL perform the following verification obligations.

### 4.2.1 – 4.2.8 Base Verification Process
The Relying Party SHALL perform the base attestation verification process as defined in the
Base Verification specification:
https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-base/verifier-base-verification.md#42-relying-party-obligations

### 4.2.9 Validate Integrity Rules
Validation of integrity and policy rules will be specified in a future version of this Rulebook.

## 5 Trust anchors
This chapter specifies the trust anchor mechanisms used by Relying Parties to establish trust in the issuer of an Electronic Attestation of Attributes (EAA) or a Qualified Electronic Attestation of Attributes (QEAA). The corresponding verification procedures are defined in Sections 4.2.2–4.2.4.

### 5.1 Qualified Electronic Attestations of Attributes (QEAAs)

For QEAAs, trust is established through the X.509 Public Key Infrastructure (PKI) and the applicable Trust List of Licensees (TLOL).
The issuer's certificate chain, including the intermediate certificate contained in the QEAA header, SHALL be validated up to a trusted root certificate. This validation SHALL be performed using the applicable TLOL, taking into account the trust list state applicable at the time of issuance.

Successful certificate chain validation establishes that:
- the issuer's certificate was recognized within the applicable trust framework;
- the issuer's identity has been validated by the supervisory authority during inclusion in the TLOL; and
- the issuer satisfies the trust requirements applicable to QEAAs.

In addition, the Relying Party MAY apply further authorization checks based on its internal policies, such as maintaining a whitelist of accepted QEAA providers.

### 5.2 Electronic Attestations of Attributes (EAAs)

For EAAs, trust is established through a cryptographic chain anchored in the Electronic Business Wallet Owner Identity Document (EBWOID).
The EBWOID SHALL be included in the header of every EAA. During EBWOID issuance, the EBWOID provider verifies that the public key contained in the EBWOID is owned by the Electronic Business Wallet (EBW) owner.

The Relying Party SHALL verify the EBWOID in accordance with the verification procedure defined in this Rulebook. Upon successful verification, the Relying Party obtains:
- assurance that the EBWOID was issued by an authorized provider and is not self-issued;
- the verified identity of the issuer, including its name and EUID (or another globally unique EBW owner identifier); and
- the public key authorized to verify the EAA signature.

Authorization of the issuer is subsequently determined in accordance with the Relying Party's internal policies. Such authorization MAY be based on locally maintained wallet configuration or on trusted jurisdiction- or domain-specific trust list services that identify issuers authorized for a particular type of EAA

## 6 Revocation
An attestation SHALL remain valid only while its underlying information is accurate, complete, and legally effective.

### 6.1 Revocation Mechanism
- Token Status List: The issuer must maintain an active IETF Token Status List (aligned with the Attestation Status List mechanism specified by the EU Commission).
- Credential Metadata: The metadata status_list must be populated in every issued CompanyInfo attestation, referencing the status list URI and the credential's specific index.

Authorized Authority: Only the authorized issuer (the QTSP/competent body for QEAA, or the self-issuing legal entity for EAA) may modify the status list entry.

### 6.2 Revocation Triggers & Business Rules
- QEAA Trigger (Automatic): The QTSP/competent body must actively monitor official company register data and audited financial statements. Any detected discrepancy or change in the company registry must automatically trigger revocation of the QEAA.
- EAA Trigger (Manual Obligation): The self-issuing legal entity is under strict obligation to immediately update or revoke its EAA if its available documents, financial thresholds, or ownership structures change.

Relying Party Action: A revoked or suspended attestation must be treated as invalid for credential-validity purposes by all RPs.
The business interpretation is determined by the Relying Party's internal compliance policies.

## 7 References

| **Item Reference**                     | **Standard name/details**                                                                                                                                                                                                                                                                                      |
|----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [European Digital Identity Regulation] | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework                                       |
| [HAIP]                                 | Yasuda, K. et al, OpenID4VC High Assurance Interoperability Profile, OpenId Foundation, Version draft-03                                                                                                                                                                                                       |
| [IANA-JWT-Claims]                      | IANA JSON Web Token Claims Registry. Available: https://www.iana.org/assignments/jwt/jwt.xhtml                                                                                                                                                                                                                 |
| [ISO/IEC 18013-5]                      | ISO/IEC 18013-5, Personal identification — ISO-compliant driving licence - Part 5: Mobile driving licence (mDL) application, First edition, 2021-09                                                                                                                                                            |
| [ISO 8601]                             | ISO 8601 — Date and time format. Available: https://www.iso.org/iso-8601-date-and-time-format.html                                                                                                                                                                                                             |
| [OIDC]                                 | Sakimura, N. et al., "OpenID Connect Core 1.0", OpenID Foundation. Available: https://openid.net/specs/openid-connect-core-1_0.html                                                                                                                                                                            |
| [RFC 2119]                             | RFC 2119 — Key words for use in RFCs to Indicate Requirement Levels, S. Bradner, March 1997                                                                                                                                                                                                                    |
| [RFC 3339]                             | RFC 3339 — Date and Time on the Internet: Timestamps, G. Klyne et al., July 2002                                                                                                                                                                                                                               |
| [RFC 8610]                             | RFC 8610 — Concise Data Definition Language (CDDL): A Notational Convention to Express Concise Binary Object Representation (CBOR) and JSON Data Structures, H. Birkholz et al., June 2019                                                                                                                     |
| [RFC 8943]                             | RFC 8943 — Concise Binary Object Representation (CBOR) Tags for Date, M. Jones et al., November 2020                                                                                                                                                                                                           |
| [RFC 8949]                             | RFC 8949 — Concise Binary Object Representation (CBOR), C. Bormann et al., December 2020                                                                                                                                                                                                                       |
| [SD-JWT VC]                            | SD-JWT-based Verifiable Credentials (SD-JWT VC). Available: https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/, version draft-ietf-oauth-sd-jwt-vc-09                                                                                                                                                |
| [Topic 7]                              | ARF Annex 2 - Topic 7 - Attestation revocation and revocation checking. Available: https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a237-topic-7-attestation-revocation-and-revocation-checking              |