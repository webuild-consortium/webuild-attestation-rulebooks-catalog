# Attestation Rulebook for attestations of type ESG Certificate

* Author(s):
  * [Dominic Hurni, SBB]
  * [Werner Folkendt, Robert Bosch GmbH]
* Previous Authors
* Reviewer(s):
  * [Florin Coptil, Robert Bosch GmbH]

| Version | Date       | Description                                                    |
|---------|------------|----------------------------------------------------------------|
| 0.3     | 19.05.2026 | Initial draft based on the WeBuild design attestation meetings |
| 0.6     | 29.06.2026 | update layout                                                |
| 0.8     | 29.06.2026 | Review attributes and type                                      |
| 0.9     | 03.07.2026 | Updates in regard trust and revocation

* Contact:
  * [Dominic Hurni](mailto:dominic.hurni@sbb.ch) *
  * [Werner Folkendt](mailto:werner.folkendt@de.bosch.com) *

* Feedback:

## 1 Introduction

This attestation addresses the following question:

**Does this legal entity hold a valid ESG-related certificate (e.g., ISO 9001, ISO 14001, IATF 16949) and what is its certified scope?**

The ESG Certificate Attestation provides a standardized, verifiable digital representation of Environmental, Social, and Governance certificates held by a legal entity, enabling structured exchange of certification data for use in KYS, supplier onboarding, compliance verification, and regulatory audit processes.

The issuers of the certificate are:
- **(a) Accredited issuers** — certification bodies authorized to issue ESG-related certificates
  (e.g., Bureau Veritas, TÜV, DNV).
- **(b) Legal entities** — companies that own certificates that are still valid but need to present
  the data as an EAA during onboarding to their customers.

The relying parties are:
- **(1) Procurers** checking compliance and conducting supplier audits.
- **(2) Authorities** (e.g., customs) that verify ESG attestations.

This schema has been verified for use with the following certificate types, including but not
limited to: **ISO 9001, IATF 16949, DIN EN ISO 45001, DIN EN ISO 14001, DIN EN ISO 50001,
AEO**, and others. The ESG Certificate Attestation is based on the schema defined in this document.

### 1.1 Document Scope and Purpose

The ESG Certificate Attestation provides a standardized, verifiable digital representation of
Environmental, Social, and Governance certificates held by a legal entity. It enables structured
exchange of certification data for use in KYS (Know Your Supplier), supplier onboarding,
compliance verification, and regulatory audit processes.

This attestation captures the essential attributes of a physical or digital ESG certificate —
including the certificate type, registration number, validity dates, certified scope, site
information, and optional evidence attachment — in a machine-readable, selectively disclosable
format compliant with the EUDI Wallet framework.

**Design Decisions**

This ESG Certificate Attestation Rulebook is based on:
- EUDI Wallet / eIDAS 2.0 framework for digital identity and verifiable attestations
- ISO 8601 for date formatting
- International Code Designator (ICD) 0243 for BPNL (Business Partner Number Legal entity)
  as used in Catena-X
- Support for multiple legal entity identifier schemes (EUID, LEI, DUNS, EORI, VAT ID, BPNL,
  GLN, SIREN)
- CDDL representation types per [RFC 8610] for attribute encoding

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

| Term                   | Description                                                                                                                                                                    |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ESG Certificate        | An Environmental, Social, and Governance certificate issued by an accredited certification body or self-attested by a legal entity, proving conformity with a defined standard |
| Economic Operator      | The legal entity that holds the ESG certificate and is subject to the certification                                                                                            |
| Certified Site         | A physical location (site name and address) for which the ESG certificate is valid, as defined in the certificate scope                                                        |
| Scope of Certification | The description of location (name, adresses and scope described in activities regarding products and services) covered by the certificate                                      |
| Certificate Type       | The standard or framework under which the certificate is issued (e.g., ISO 9001, IATF 16949, DIN EN ISO 14001)                                                                 |
| Certificate Version    | The version of the standard used for certification (e.g., ISO 9001:2015)                                                                                                       |
| Registration Number    | The unique identifier of the certificate as assigned by the issuing certification body                                                                                         |
| Evidence               | An optional attachment of the original certificate document in base64 format or referenced via URI                                                                             |
| BPNL                   | Business Partner Number Legal entity — a globally unique identifier used in the Catena-X ecosystem, assigned per ICD 0243                                                      |
| EUID                   | European Unique Identifier — the unique identifier assigned to legal entities registered within the EU per Directive (EU) 2017/1132                                            |
| LEI                    | Legal Entity Identifier — a 20-character alphanumeric code per ISO 17442                                                                                                       |
| EORI                   | Economic Operators Registration and Identification number — used for customs purposes within the EU                                                                            |
| GLN                    | Global Location Number — a GS1 identifier for legal entities and locations                                                                                                     |
| KYS                    | Know Your Supplier — due diligence process for verifying supplier credentials, integrity, and risk exposure                                                                    |
| EAA                    | Electronic Attestation of Attributes — as defined under eIDAS 2.0                                                                                                              |
| QEAA                   | Qualified Electronic Attestation of Attributes — as defined under eIDAS 2.0                                                                                                    |
| ISO 8601               | International standard for date and time representations (e.g., YYYY-MM-DD)                                                                                                    |
| RFC 8610               | Concise Data Definition Language (CDDL) for encoding data structures                                                                                                           |

## 2 Attestation Attributes and Metadata

The ESG Certificate Attestation is designed to provide a standardized, verifiable digital representation of ESG-related certificates held by a legal entity. It captures all essential attributes of a physical or digital ESG certificate, including the economic operator identity, certificate metadata, certified scope with site-level granularity, and optional evidence, in a machine-readable and selectively disclosable format.

### 2.1 Introduction

[Economic Operator] --- owns --- [Certificate] --- allocated to --- [Site and Scope]

**Data Model:**

```text
├─ type (tstr) — mandatory                      
├─ version (tstr) — mandatory
├─ registration_number (tstr) — mandatory 
├─ registration_initial_date (date) — mandatory  
├─ registration_expiration_date (date) — mandatory 
├─ legal_entity (M)
│   ├─ legal_person  (M)
│   │   ├─ legal_person_name (tstr) (M)
│   │   ├─ legal_form_type (tstr) (M)
│   ├─ identifier  (M)                          // At least one identifier required
│   │   ├─ euid (str) (O)                       // European Unique Identifier
│   │   ├─ lei (str) (O)                        // Legal Entity Identifier per ISO 17442
│   │   ├─ tax (str) (O)                        // National tax or registration number    
│   │   ├─ gln (str) (O)                        // Global Location Number for legal entities — GS1 identifier
│   │   ├─ duns (str) (O)                       // Data Universal Numbering System — Dun & Bradstreet identifier
│   │   ├─ eori (str) (O)                       // Economic Operators Registration and Identification number — EU customs identifier
│   │   ├─ bpnl (str) (O)                       // Business Partner Number Legal entity — Catena-X identifier per ICD 0243
│   │   ├─ siren (str) (O)                      // Système d'Identification du Répertoire des ENtreprises — French company identifier
│   ├─ address (Address) (M)           
│   │   ├─ street (tstr) (M)
│   │   ├─ house_number (tstr) (M)
│   │   ├─ locality (tstr) (M)
│   │   ├─ region (tstr) (M)
│   │   ├─ postal_code (tstr) (M)
│   │   └─ country (tstr) (M)                   // ISO 3166-1 alpha-2
├─ scope [1..n] — mandatory                     // Array of ScopeObject
│   ├─ legal_entity_name (tstr) (M)
│   ├─ legal_entity_identifier  (M)             // At least one identifier required
│   │   ├─ euid (str) (O)                       // European Unique Identifier
│   │   ├─ lei (str) (O)                        // Legal Entity Identifier per ISO 17442
│   │   ├─ tax (str) (O)                        // National tax or registration number    
│   │   ├─ gln (str) (O)                        // Global Location Number for legal entities — GS1 identifier
│   │   ├─ duns (str) (O)                       // Data Universal Numbering System — Dun & Bradstreet identifier
│   │   ├─ eori (str) (O)                       // Economic Operators Registration and Identification number — EU customs identifier
│   │   ├─ bpnl (str) (O)                       // Business Partner Number Legal entity — Catena-X identifier per ICD 0243
│   │   ├─ siren (str) (O)                      // Système d'Identification du Répertoire des ENtreprises — French company identifier
│   ├─ site_identifier (uuid) — (O)
│   ├─ site_address (Address) — (M)
│   │   ├─ street (tstr) (M)
│   │   ├─ house_number (tstr) (M)
│   │   ├─ locality (tstr) (M)
│   │   ├─ region (tstr) (M)
│   │   ├─ postal_code (tstr) (M)
│   │   └─ country (tstr) (M)                     // ISO 3166-1 alpha-2
│   ├─ scope_description (tstr) — (M)
│   └─ certified_site (boolean) — (M) 
└─ evidence (Evidence) — mandatory
    ├─ id (tstr) (M)                            // Unique identifier, URI, or URN
    ├─ type (tstr) (M)                          // Evidence type — see Section 2.8.9
    ├─ url (uri) (O)                            // URI to publicly accessible source document
    └─ data (base64) (O)                        // Base64-encoded — required if url absent
```
*Note*: M - mandatory / O - optional.

**Explanation:**

*   The root object of the attestation is the `Certificate` itself.
*   The `legal_entity` object is mandatory and identifies the primary organization to which the certificate was issued. It includes the legal name, legal form, at least one official `identifier`, and the primary `Address`.
*   The `scope` attribute is a mandatory array that **SHALL** contain at least one `ScopeObject`. Each `ScopeObject` defines a specific certified entity or site, its address, a description of the certified activities, and a boolean flag (`certified_site`) indicating if the entire site is covered.
*   The `evidence` object is mandatory and serves to prove the existence of the original certificate. It **SHALL** contain a unique `id` and a `type`. It **MAY** also include a `url` pointing to the document or the `data` of the document itself, encoded in base64.

**Attestation Classification:**

This attestation type **MAY** be classified as:
- **"EAA"** self-issued by the legal entity as part of its disclosures.
- **"QEAA"** issued by a Qualified Trust Service Provider (QTSP) or authorized competent body that can independently attest it.

| **Data Identifier** | **Semantic Reference** | **Definition**                                          | **Data type**        |
|:--------------------|:-----------------------|:--------------------------------------------------------|:---------------------|
| `legal_entity`      | —                      | The certified legal entity.                             | Object               |
| `scope`             | —                      | The certified scope, including sites and descriptions.  | Array of ScopeObject |
| `evidence`          | —                      | Evidence of the original certificate.                   | Object               |

### 2.2 Mandatory Attributes

**Certificate Attributes**

| **Data Identifier**            | **Semantic Reference** | **Definition**                                        | **Data type** |
|:-------------------------------|:-----------------------|:------------------------------------------------------|:--------------|
| `type`                         | —                      | Type of the certificate (e.g., ISO 9001, IATF 16949). | String        |
| `version`                      | —                      | Version of the certificate standard (e.g., "2015").   | String        |
| `registration_number`          | —                      | Registration number from the certificate document.    | String        |
| `registration_initial_date`    | —                      | Valid-from date of the certificate (ISO 8601).        | Date          |
| `registration_expiration_date` | —                      | Valid-until date of the certificate (ISO 8601).       | Date          |

**Legal_Entity Attributes**

| **Data Identifier**              | **Semantic Reference** | **Definition**                                                                           | **Data type**  |
|:---------------------------------|:-----------------------|:-----------------------------------------------------------------------------------------|:---------------|
| `legal_person`                   | —                      | An object containing the legal name and form of the entity.                              | Object         |
| `legal_person.legal_person_name` | —                      | The full legal name of the entity.                                                       | String         |
| `legal_person.legal_form_type`   | —                      | The legal form type of the entity (e.g., GmbH, AG).                                      | String         |
| `identifier`                     | —                      | An object of identifiers for the legal entity. **SHALL** contain at least one sub-field. | Object         |
| `Address`                        | —                      | The registered primary address of the legal entity.                                      | Address Object |

**ScopeObject Attributes**
This object is defined for each entry in the `scope` array.

| **Data Identifier**       | **Semantic Reference** | **Definition**                                                             | **Data type**  |
|:--------------------------|:-----------------------|:---------------------------------------------------------------------------|:---------------|
| `legal_entity_name`       | —                      | Legal name of the site/operating entity.                                   | String         |
| `legal_entity_identifier` | —                      | Identifiers for the site/operating entity; **SHALL** contain at least one. | Object         |
| `site_address`            | —                      | Physical address of the certified site.                                    | Address Object |
| `scope_description`       | —                      | Textual description of the certificate scope for this site.                | String         |
| `certified_site`          | —                      | Boolean: `true` = whole site certified; `false` = partial site only.       | Boolean        |

**Evidence Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                               | **Data type** |
|:--------------------|:-----------------------|:-------------------------------------------------------------|:--------------|
| `id`                | —                      | Unique identifier for the evidence (URI or URN).             | String        |
| `type`              | —                      | The type of evidence provided (e.g., "OriginalCertificate"). | String        |


### 2.3 Optional Attributes

**Legal_Entity Identifier Optional Attributes**

| **Data Identifier**  | **Semantic Reference** | **Definition**                                         | **Data type** |
|:---------------------|:-----------------------|:-------------------------------------------------------|:--------------|
| `euid`               | ..                     | European Unique Identifier per Directive (EU) 2017/1132.                      | String        |
| `lei`                | ..                     | Legal Entity Identifier per ISO 17442.                                        | String        |
| `tax`                | ..                     | National tax or company registration number.                                  | String        |
| `gln`                | ..                     | Global Location Number for legal entities (GS1 identifier).                   | String        |
| `duns`               | ..                     | Data Universal Numbering System (Dun & Bradstreet identifier).                | String        |
| `eori`               | ..                     | Economic Operators Registration and Identification number (EU customs).       | String        |
| `bpnl`               | ..                     | Business Partner Number Legal entity (Catena-X identifier per ICD 0243).      | String        |
| `siren`              | ..                     | Système d'Identification du Répertoire des ENtreprises (French identifier).   | String        |

**ScopeObject Identifier Optional Attributes**

| **Data Identifier**   | **Semantic Reference** | **Definition**                                                                | **Data type** |
|:----------------------|:-----------------------|:------------------------------------------------------------------------------|:--------------|
| `euid`                | ..                     | European Unique Identifier per Directive (EU) 2017/1132.                      | String        |
| `lei`                 | ..                     | Legal Entity Identifier per ISO 17442.                                        | String        |
| `tax`                 | ..                     | National tax or company registration number.                                  | String        |
| `gln`                 | ..                     | Global Location Number for legal entities (GS1 identifier).                   | String        |
| `duns`                | ..                     | Data Universal Numbering System (Dun & Bradstreet identifier).                | String        |
| `eori`                | ..                     | Economic Operators Registration and Identification number (EU customs).       | String        |
| `bpnl`                | ..                     | Business Partner Number Legal entity (Catena-X identifier per ICD 0243).      | String        |
| `siren`               | ..                     | Système d'Identification du Répertoire des ENtreprises (French identifier).   | String        |
| `site_identifier`     | —                      | A unique identifier (UUID) for the certified site.                         | String (UUID)  |
 
**Evidence Optional Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                                  | **Data type**   |
|:--------------------|:-----------------------|:----------------------------------------------------------------|:----------------|
| `url`               | —                      | A URI pointing to the publicly accessible certificate document. | String (URI)    |
| `data`              | —                      | The base64-encoded certificate document.                        | String (base64) |


### 2.4 Conditional Attributes

| **Data Identifier** | **Condition**                                                              | **Definition**                                       | **Data type**   |
|:--------------------|:---------------------------------------------------------------------------|:-----------------------------------------------------|:----------------|
| `evidence.data`     | **SHALL** be present if `evidence.url` is not provided or is inaccessible. | The certificate document encoded as a base64 string. | String (base64) |


### 2.5 Mandatory Metadata

| **Data Identifier**          | **Definition**                                                     | **Data type** |
|:-----------------------------|:-------------------------------------------------------------------|:--------------|
| `attestation_legal_category` | Indicates the legal category of the Attestation ("EAA" or "QEAA"). | String        |
| `cnf`                        | Cryptographic Key Binding to prove holder possession.              | Object        |

*Note: Standard JWT claims (`iss`, `iat`, `exp`) are also mandatory.*


### 2.6 Optional Metadata

| **Data Identifier** | **Definition**                                                              | **Data type** |
|:--------------------|:----------------------------------------------------------------------------|:--------------|
| `trust_anchor_url`  | URL where the trust anchor for verifying this attestation can be retrieved. | URI           |
| `schema_version`    | Version of the schema used for this attestation.                            | String        |

### 2.7 Conditional metadata
No conditional metadata elements are defined for this attestation type.

### 2.8 Value Lists

#### 2.8.1 Legal Entity Identifier Type Codes
The `identifier` objects within `Legal_Entity` and `scope` **SHOULD** use one or more of the following standardized identifier types as keys:

| **Code** | **Definition**                                                              |
|:---------|:----------------------------------------------------------------------------|
| `euid`   | European Unique Identifier per Directive (EU) 2017/1132.                    |
| `lei`    | Legal Entity Identifier per ISO 17442.                                      |
| `tax`    | National tax or company registration number.                                |
| `gln`    | Global Location Number for legal entities (GS1 identifier).                 |
| `duns`   | Data Universal Numbering System (Dun & Bradstreet identifier).              |
| `eori`   | Economic Operators Registration and Identification number (EU customs).     |
| `bpnl`   | Business Partner Number Legal entity (Catena-X identifier per ICD 0243).    |
| `siren`  | Système d'Identification du Répertoire des ENtreprises (French identifier). |

#### 2.8.2 Certificate Type Codes
The `type` attribute **SHOULD** use one of the following standardized values where applicable. Other certificate types **MAY** be used as free-text strings.

| **Code**    | **Definition**                                          |
|:------------|:--------------------------------------------------------|
| `ISO9001`   | Quality Management Systems                              |
| `IATF16949` | Automotive Quality Management Systems                   |
| `ISO14001`  | Environmental Management Systems                        |
| `ISO45001`  | Occupational Health and Safety Management Systems       |
| `ISO50001`  | Energy Management Systems                               |
| `AEO`       | Authorised Economic Operator — EU customs certification |

#### 2.8.3 Evidence Type Codes
The `evidence.type` attribute **SHOULD** use one of the following values:

| **Code**              | **Definition**                                                                |
|:----------------------|:------------------------------------------------------------------------------|
| `OriginalCertificate` | The evidence is the original digital or scanned certificate document.         |
| `DigitalTwin`         | The evidence is a digital representation or twin of the physical certificate. |


### 2.9 Integrity Rules
The following integrity rules **SHALL** be enforced:
- All mandatory attributes as defined in the data model SHALL be present and non-empty.
- `registration_expiration_date` SHALL be a date later than or equal to `registration_initial_date`.
- Each `identifier` object (for `Legal_Entity` and `scope`) SHALL contain at least one non-empty identifier.
- The `scope` array SHALL contain at least one valid `ScopeObject`.
- `evidence.id` and `evidence.type` SHALL be non-empty strings.
- Either `evidence.url` or `evidence.data` SHALL be present.
- `certified_site` SHALL be a boolean value (`true` or `false`).
- All `Address` objects SHALL contain non-empty `street`, `house_number`, `locality`, `postal_code`, and `country`.


## 3 Attestation Encoding

### 3.1 ISO/IEC 18013-5-Compliant Encoding
ISO/IEC 18013-5 is out of scope for this Rulebook.

### 3.2 SD-JWT VC-Based Encoding
The ESG Certificate Attestation uses the SD-JWT VC format to allow for selective disclosure.

**Verifiable Credential Type (`vct`):** `eu.we-build:esgcertificate:1`

#### 3.2.1 Attribute Encoding Table

| **Data Identifier**                        | **Attribute Identifier**                      | **Encoding Format**     | **Reference / Notes**                            | **Disclosable** |
|:-------------------------------------------|:----------------------------------------------|:------------------------|:-------------------------------------------------|:----------------|
| type                                       | `type`                                        | String                  | Type of the ESG certificate.                     | MUST            |
| version                                    | `version`                                     | String                  | Version of the certificate standard.             | MUST            |
| registration_number                        | `registration_number`                         | String                  | Unique registration number.                      | MUST            |
| registration_initial_date                  | `registration_initial_date`                   | String (ISO 8601)       | Date of initial registration.                    | MUST            |
| registration_expiration_date               | `registration_expiration_date`                | String (ISO 8601)       | Date of expiration.                              | MUST            |
| **Legal Entity**                           | `legal_entity`                                | Object                  | The certified legal entity.                      | MUST            |
| legal_person_name                          | `legal_entity.legal_person.legal_person_name` | String                  | Legal name of the entity.                        | MUST            |
| legal_form_type                            | `legal_entity.legal_person.legal_form_type`   | String                  | Legal form of the entity.                        | MUST            |
| **Legal Entity**                           | `legal_entity.identifier`                     | Object                  | The legal entity identifier                      | MUST            |
| euid                                       | `legal_entity.identifier.euid`                | String                  | European Unique Identifier.                      | MUST            |
| lei                                        | `legal_entity.identifier.lei`                 | String                  | Legal Entity Identifier.                         | MUST            |
| tax                                        | `legal_entity.identifier.tax`                 | String                  | National tax/registration number.                | MUST            |
| gln                                        | `legal_entity.identifier.gln`                 | String                  | Global Location Number.                          | MUST            |
| duns                                       | `legal_entity.identifier.duns`                | String                  | Dun & Bradstreet identifier.                     | MUST            |
| eori                                       | `legal_entity.identifier.eori`                | String                  | EU customs identifier.                           | MUST            |
| bpnl                                       | `legal_entity.identifier.bpnl`                | String                  | Catena-X BPNL identifier.                        | MUST            |
| siren                                      | `legal_entity.identifier.siren`               | String                  | French SIREN identifier.                         | MUST            |
| **Address**                                | `legal_entity.address`                        | Object                  | The address of legal entity.                     | MUST            |
| street                                     | `legal_entity.address.street`                 | String                  | Street name of the main address.                 | MUST            |
| house_number                               | `legal_entity.address.house_number`           | String                  | House number of the main address.                | MUST            |
| locality                                   | `legal_entity.address.locality`               | String                  | Locality of the main address.                    | MUST            |
| region                                     | `legal_entity.address.region`                 | String                  | Region of the main address.                      | MUST            |
| postal_code                                | `legal_entity.address.postal_code`            | String                  | Postal code of the main address.                 | MUST            |
| country                                    | `legal_entity.address.country`                | String                  | Country of the main address.                     | MUST            |
| **Scope**                                  | `scope`                                       | Array [ScopeObject]     | Array of certified scope objects.                | MUST            |
| legal_entity_name (scope)                  | `scope[n].legal_entity_name`                  | String                  | Legal name of the entity in scope.               | MUST            |
| **legal_entity_identifier**                | `legal_entity_identifier`                     | Object                  | The  legal entity identifier                     | MUST            |
| euid (scope)                               | `scope[n].legal_entity_identifier.euid`       | String                  | EUID for the scoped entity.                      | MUST            |
| lei (scope)                                | `scope[n].legal_entity_identifier.lei`        | String                  | LEI for the scoped entity.                       | MUST            |
| tax (scope)                                | `scope[n].legal_entity_identifier.tax`        | String                  | Tax ID for the scoped entity.                    | MUST            |
| gln (scope)                                | `scope[n].legal_entity_identifier.gln`        | String                  | GLN for the scoped entity.                       | MUST            |
| duns (scope)                               | `scope[n].legal_entity_identifier.duns`       | String                  | DUNS for the scoped entity.                      | MUST            |
| eori (scope)                               | `scope[n].legal_entity_identifier.eori`       | String                  | EORI for the scoped entity.                      | MUST            |
| bpnl (scope)                               | `scope[n].legal_entity_identifier.bpnl`       | String                  | BPNL for the scoped entity.                      | MUST            |
| siren (scope)                              | `scope[n].legal_entity_identifier.siren`      | String                  | SIREN for the scoped entity.                     | MUST            |
| site_identifier                            | `scope[n].site_identifier`                    | String (UUID)           | Unique identifier for the site.                  | MUST            |
| street (scope)                             | `scope[n].site_address.street`                | String                  | Street of the site address.                      | MUST            |
| house_number (scope)                       | `scope[n].site_address.house_number`          | String                  | House number of the site address.                | MUST            |
| locality (scope)                           | `scope[n].site_address.locality`              | String                  | Locality of the site address.                    | MUST            |
| region (scope)                             | `scope[n].site_address.region`                | String                  | Region of the site address.                      | MUST            |
| postal_code (scope)                        | `scope[n].site_address.postal_code`           | String                  | Postal code of the site address.                 | MUST            |
| country (scope)                            | `scope[n].site_address.country`               | String                  | Country of the site address.                     | MUST            |
| scope_description                          | `scope[n].scope_description`                  | String                  | Description of the certification scope.          | MUST            |
| certified_site                             | `scope[n].certified_site`                     | Boolean                 | Flag indicating if the entire site is certified. | MUST            |
| **Evidence**                               | `evidence`                                    | Object                  | Object containing evidence details.              | MUST            |
| id                                         | `evidence.id`                                 | String                  | Unique identifier for the evidence.              | MUST            |
| type                                       | `evidence.type`                               | String                  | Type of the evidence provided.                   | MUST            |
| url                                        | `evidence.url`                                | String (URI)            | Optional URI to the evidence document.           | MAY             |
| data                                       | `evidence.data`                               | String (base64)         | Optional base64 encoded evidence data.           | MAY             |
| **Metadata**                               |                                               |                         |                                                  |                 |
| issuance_date                              | `iat`                                         | Number (Unix timestamp) | Issuance timestamp.                              | MUST NOT        |
| expiration_date                            | `exp`                                         | Number (Unix timestamp) | Expiration timestamp.                            | MUST NOT        |
| issuing_entity                             | `iss`                                         | String (URI or DID)     | Identifier of the issuer.                        | MUST NOT        |
| attestation_legal_category                 | `attestation_legal_category`                  | String                  | "EAA" or "QEAA".                                 | MUST NOT        |
| vct                                        | `vct`                                         | String                  | Verifiable Credential Type.                      | MUST NOT        |
| cnf                                        | `cnf`                                         | Object                  | Cryptographic Key Binding.                       | MUST NOT        |
| trust_anchor_url                           | `trust_anchor_url`                            | String (URI)            | Optional URL to the trust anchor.                | MAY             |
| schema_version                             | `schema_version`                              | String                  | Optional version of the schema.                  | MAY             |

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
    "status_list_credential": "https://issuer.example.com/status/esgcertificate/2025",
    "status_list_index": 456,
    "status_purpose": "revocation"
  }
}
```

#### 3.2.3 Example Payload
The following is a non-normative example of an ESG Certificate Attestation SD-JWT VC payload.
```json
{
  "vct": "eu.we-build:esgcertificate:1",
  "iss": "did:example:accredited-cert-issuer-123",
  "iat": 1724284800,
  "exp": 1882051200,
  "attestation_legal_category": "QEAA",
  "type": "ISO9001",
  "version": "2015",
  "registration_number": "DE015008",
  "registration_initial_date": "2024-08-22",
  "registration_expiration_date": "2027-08-22",
  "legal_entity": {
    "legal_person": {
      "legal_person_name": "Robert Bosch GmbH",
      "legal_form_type": "GmbH"
    },
    "identifier": {
      "euid": "DE.HRB.12345",
      "lei": "529900T8BM49AURSDO55",
      "tax": "DE811001001"
    },
    "address": {
      "street": "Robert-Bosch-Platz",
      "house_number": "1",
      "locality": "Gerlingen-Schillerhöhe",
      "region": "Baden-Württemberg",
      "postal_code": "70839",
      "country": "DE"
    }
  },
  "scope": [
    {
      "legal_entity_name": "Robert Bosch GmbH",
      "legal_entity_identifier": {
        "bpnl": "BPNL00000003CML1"
      },
      "site_identifier": "urn:uuid:f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
      "site_address": {
        "street": "Auf der Breit",
        "house_number": "4",
        "locality": "Karlsruhe",
        "region": "Baden-Württemberg",
        "postal_code": "76227",
        "country": "DE"
      },
      "scope_description": "Development, production and distribution of products and services for the automotive aftermarket.",
      "certified_site": true
    }
  ],
  "evidence": {
    "id": "urn:uuid:6e8bc430-9c3a-11d9-9669-0800200c9a66",
    "type": "OriginalCertificate",
    "url": "https://certificates.issuer.com/DE015008.pdf"
  },
  "status": {
    "type": "status-list",
    "status_list_credential": "https://issuer.example.com/status/esg/2024",
    "status_list_index": 101,
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
Sample payloads are provided under ../data-schemas/sd-jwt/sample-data/esg-certificate-sd-jwt-sample.json

### 3.3 W3C Verifiable Credentials Data Model-based encoding

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

| **Item Reference**                     | **Standard name/details**                                                                                                                                                                                                                                                                           |
|----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [European Digital Identity Regulation] | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework                            |
| [HAIP]                                 |Yasuda, K. et al, OpenID4VC High Assurance Interoperability Profile, OpenId Foundation, Version draft-03|
| [IANA-JWT-Claims]                      | IANA JSON Web Token Claims Registry. Available: https://www.iana.org/assignments/jwt/jwt.xhtml|
| [ISO/IEC 18013-5]                      | ISO/IEC 18013-5, Personal identification — ISO-compliant driving licence - Part 5: Mobile driving licence (mDL) application, First edition, 2021-09|
| [ISO 4217]                             | ISO 4217 — Currency codes. Available: https://www.iso.org/iso-4217-currency-codes.html|
| [ISO 8601]                             | ISO 8601 — Date and time format. Available: https://www.iso.org/iso-8601-date-and-time-format.html|
| [OIDC]                                 |Sakimura, N. et al., "OpenID Connect Core 1.0", OpenID Foundation. Available: https://openid.net/specs/openid-connect-core-1_0.html|
| [RFC 2119]                             | RFC 2119 — Key words for use in RFCs to Indicate Requirement Levels, S. Bradner, March 1997|
| [RFC 3339]                             |RFC 3339 — Date and Time on the Internet: Timestamps, G. Klyne et al., July 2002|
| [RFC 8610]                             |RFC 8610 — Concise Data Definition Language (CDDL): A Notational Convention to Express Concise Binary Object Representation (CBOR) and JSON Data Structures, H. Birkholz et al., June 2019|
| [RFC 8943]                             |RFC 8943 — Concise Binary Object Representation (CBOR) Tags for Date, M. Jones et al., November 2020|
| [RFC 8949]                             |RFC 8949 — Concise Binary Object Representation (CBOR), C. Bormann et al., December 2020|
| [SD-JWT VC]                            | SD-JWT-based Verifiable Credentials (SD-JWT VC). Available: https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/, version draft-ietf-oauth-sd-jwt-vc-09|
| [Topic 7]                              |ARF Annex 2 - Topic 7 - Attestation revocation and revocation checking. Available: https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a237-topic-7-attestation-revocation-and-revocation-checking|