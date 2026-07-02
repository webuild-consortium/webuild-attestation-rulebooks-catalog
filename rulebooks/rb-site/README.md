# Attestation Rulebook for attestations of type Site Attestation

* **Author(s):**
  * [Dominic Hurni, SBB]
  * [Werner Folkendt, Robert Bosch GmbH]

* Previous Authors

* **Reviewer(s):**
  * [Florin Coptil, Robert Bosch GmbH]

| Version | Date       | Description                                                    |
|---------|------------|----------------------------------------------------------------|
| 0.4     | 19.05.2026 | Initial draft based on the WeBuild design attestation meetings |
| 0.6     | 29.06.2026 | Layout and identifiers update  |

* **Contact:**
  * [Dominic Hurni](mailto:dominic.hurni@sbb.ch)
  * [Werner Folkendt](mailto:werner.folkendt@de.bosch.com)

* **Sources:**
  * [Powerpoint](https://portal.webuildconsortium.eu/group/3/files/6256/collabora-online/edit/3001)
  * [Excel](https://portal.webuildconsortium.eu/group/3/files/5757/collabora-online/edit/2384)

---

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

- **Chapter 2** describes the Site Attestation attributes and metadata in an
  encoding-independent manner, including the data model.
- **Chapter 3** specifies how the attestation attributes and metadata are encoded: Section 3.2
  covers SD-JWT VC-based encoding.
- **Chapter 4** specifies attestation usage scenarios, Relying Party obligations, and integration
  with KYS/KYC workflows.
- **Chapter 5** defines trust anchors and verification mechanisms for issuer authorization.
- **Chapter 6** defines revocation mechanisms for the attestation.
- **Chapter 7** provides compliance information regarding the EUDI framework and applicable
  data protection laws.
- **Chapter 8** provides references to applicable standards and specifications.

### 1.3 Keywords

This document uses the capitalised keywords 'SHALL', 'SHOULD' and 'MAY' as specified in
[RFC 2119], i.e. to indicate requirements, recommendations and options specified in this document.

In addition, 'must' (non-capitalised) is used to indicate an external constraint, i.e. a
requirement that is not mandated by this document, but, for instance, by an external document.
The word 'can' indicates a capability, whereas other words, such as 'will', and 'is' or 'are'
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

---

## 2 Attestation Attributes and Metadata

The Site Attestation is designed to provide a standardized, verifiable digital representation of
a specific physical location (site) operated by an economic operator. It captures all essential
attributes required to identify a site, link it to its operating economic operator, and support
cross-business processes within supply chain management, compliance verification, and
regulatory reporting.

### 2.1 Introduction

**Data Model:**
[Economic Operator] ---operates--- [Site]
```
Site [1]
├─ parent_economic_operator_main_id (string) — mandatory
├─ parent_economic_operator_id[1..n] (M)            // At least one identifier required
│   ├─ euid (str) (O)                               // European Unique Identifier
│   ├─ lei (str) (O)                                // Legal Entity Identifier per ISO 17442
│   ├─ tax (str) (O)                                // National tax or registration number
│   ├─ gln (str) (O)                                // Global Location Number for legal entities — GS1 identifier
│   ├─ duns (str) (O)                               // Data Universal Numbering System — Dun & Bradstreet identifier
│   ├─ eori (str) (O)                               // Economic Operators Registration and Identification number — EU customs identifier
│   ├─ bpnl (str) (O)                               // Business Partner Number Legal entity — Catena-X identifier per ICD 0243
│   └─ siren (str) (O)                              // Système d'Identification du Répertoire des ENtreprises — French company identifier
├─ site_name (string) — mandatory
├─ site_main_id (uuid) — mandatory
├─ site_additional_ids (Array of identifier strings) — optional [0..n]
├─ site_main_address (Address) — mandatory
│   ├─ street (string)
│   ├─ nr (string)
│   ├─ postal_code (string)
│   └─ city (string)
└─ site_additional_addresses (Array of Address) — optional [0..n]
├─ street (string)
├─ nr (string)
├─ postal_code (string)
└─ city (string)
```

**Explanation:**

- The `Site` object **SHALL** appear exactly once per attestation.
- `parent_economic_operator_main_id`, `site_name`, `site_main_id`, and
  `site_main_address` are mandatory attributes.
- `parent_economic_operator_id` **MUST** contain at least one identifier. Each sub-field
  is optional (`O`), but at least one of the listed identifier fields **SHALL** be provided.
- `site_additional_ids` and `site_additional_addresses` are optional and **MAY** contain
  zero or more entries.
- `site_main_id` is a globally unique identifier (UUID) generated by the Economic Operator
  using his EBW. This identifier **SHALL NOT** change during the lifecycle of the site.
- The attestation **MUST** be linked to the economic operator by providing at least one unique
  identifier in `parent_economic_operator_id`.
- `site_additional_addresses` **MAY** represent additional entrances of the main location or
  addresses of external (e.g., rented) buildings used by the site.

**Attestation Classification:**

This attestation type **MAY** be classified as:
- **"EAA"** when self-issued by the economic operator operating the site.

**Top-Level Data Identifiers:**

| **Data Identifier**                    | **Semantic Reference** | **Definition**                                                                                     | **Data type**    |
|----------------------------------------|------------------------|----------------------------------------------------------------------------------------------------|------------------|
| parent_economic_operator_main_id       | —                      | Primary unique identifier of the economic operator that operates this site (preferred: EUID)       | String           |
| parent_economic_operator_id            | —                      | Structured object of economic operator identifiers; at least one sub-field SHALL be provided       | Object           |
| parent_economic_operator_id.euid       | —                      | European Unique Identifier                                                                         | String (O)       |
| parent_economic_operator_id.lei        | —                      | Legal Entity Identifier per ISO 17442                                                              | String (O)       |
| parent_economic_operator_id.tax        | —                      | National tax or registration number                                                                | String (O)       |
| parent_economic_operator_id.gln        | —                      | Global Location Number for legal entities — GS1 identifier                                        | String (O)       |
| parent_economic_operator_id.duns       | —                      | Data Universal Numbering System — Dun & Bradstreet identifier                                     | String (O)       |
| parent_economic_operator_id.eori       | —                      | Economic Operators Registration and Identification number — EU customs identifier                  | String (O)       |
| parent_economic_operator_id.bpnl       | —                      | Business Partner Number Legal entity — Catena-X identifier per ICD 0243                           | String (O)       |
| parent_economic_operator_id.siren      | —                      | Système d'Identification du Répertoire des ENtreprises — French company identifier                 | String (O)       |
| site_name                              | —                      | The name of the site                                                                               | String           |
| site_main_id                           | —                      | Globally unique identifier of the site, generated by the EBW as a UUID                            | UUID (String)    |
| site_additional_ids                    | —                      | Array of additional site-level identifiers                                                         | Array of Strings |
| site_main_address                      | —                      | Physical main address of the site                                                                  | Object (Address) |
| site_additional_addresses              | —                      | Array of additional addresses associated to the site                                               | Array of Address |

### 2.2 Mandatory Attributes

#### Site Top-Level Attributes

| **Data Identifier**              | **Semantic Reference** | **Definition**                                                                                                                                                                | **Data type**  | **Existing Vocabularies**                 |
|----------------------------------|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|-------------------------------------------|
| parent_economic_operator_main_id | —                      | The Economic Operator's primary identifier. Preferred: EUID for EU entities                                                                                                   | String         | European Business Wallet Vocabulary v0.1  |
| parent_economic_operator_id      | —                      | Structured object containing economic operator identifiers; **MUST** contain at least one non-empty sub-field (see Section 2.8.1 for valid identifier types)                  | Object         | European Business Wallet Vocabulary v0.1  |
| site_name                        | —                      | The name of the site                                                                                                                                                          | String         | The Organization Ontology                 |
| site_main_id                     | —                      | A globally unique identifier created by the Economic Operator using his EBW. The identifier is an attribute of the site that will not change during the lifecycle of the site | UUID           | UUID generated by the wallet via API call |
| site_main_address                | —                      | Physical main address of the site                                                                                                                                             | Address object | Core Location Vocabulary                  |

#### Economic Operator Identifier Sub-Fields (`parent_economic_operator_id`)

At least one of the following sub-fields **SHALL** be provided. All sub-fields are individually
optional (`O`):

| **Sub-Field** | **Semantic Reference** | **Definition**                                                                      | **Data type** |
|---------------|------------------------|-------------------------------------------------------------------------------------|---------------|
| euid          | —                      | European Unique Identifier per Directive (EU) 2017/1132                             | String (O)    |
| lei           | —                      | Legal Entity Identifier per ISO 17442 (20-character alphanumeric code)              | String (O)    |
| tax           | —                      | National tax or registration number                                                 | String (O)    |
| gln           | —                      | Global Location Number for legal entities — GS1 identifier                         | String (O)    |
| duns          | —                      | Data Universal Numbering System — Dun & Bradstreet company identifier               | String (O)    |
| eori          | —                      | Economic Operators Registration and Identification number — EU customs identifier   | String (O)    |
| bpnl          | —                      | Business Partner Number Legal entity — Catena-X identifier per ICD 0243            | String (O)    |
| siren         | —                      | Système d'Identification du Répertoire des ENtreprises — French company identifier  | String (O)    |

#### Address Object Attributes

Applies to both `site_main_address` and entries within `site_additional_addresses`:

| **Data Identifier** | **Semantic Reference** | **Definition**                          | **Data type** |
|---------------------|------------------------|-----------------------------------------|---------------|
| street              | —                      | Street name of the address              | String        |
| nr                  | —                      | House or building number of the address | String        |
| postal_code         | —                      | Postal code of the address              | String        |
| city                | —                      | City of the address                     | String        |

### 2.3 Optional Attributes

| **Data Identifier**       | **Semantic Reference** | **Definition**                                                                                                                                                                     | **Data type**           | **Existing Vocabularies**                |
|---------------------------|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|------------------------------------------|
| site_additional_ids       | —                      | Array of additional site identifiers associated to this site. **MAY** contain zero or more entries. **SHALL** use identifier types from Section 2.8.2                              | Array of Strings [0..n] | Core Location Vocabulary                 |
| site_additional_addresses | —                      | Array of additional addresses associated to the site (e.g., additional entrances or addresses of external/rented buildings used by the site). **MAY** contain zero or more entries | Array of Address [0..n] | Core Location Vocabulary                 |

### 2.4 Conditional Attributes

No conditional attributes are defined for this attestation type. All attributes are either
mandatory or optional as specified above.

### 2.5 Mandatory Metadata

| **Data Identifier**        | **Definition**                                                                                                                         | **Data type** |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------|---------------|
| issuance_date              | The date and time when the Site Attestation was issued (ISO 8601)                                                                      | DateTime      |
| expiry_date                | The date and time when the Site Attestation expires (ISO 8601)                                                                         | DateTime      |
| issuing_entity             | The identifier of the economic operator that issued the attestation (typically the subject entity itself for self-issued EAA)          | String        |
| attestation_legal_category | Indicates the legal category of this attestation ("EAA")                                                                               | String        |
| vct                        | A unique identifier (URL or URN) for the credential type, indicating which claims must be present and which can be selectively disclosed | String        |

### 2.6 Optional Metadata

| **Data Identifier** | **Definition**                                                             | **Data type** |
|---------------------|----------------------------------------------------------------------------|---------------|
| trust_anchor_url    | URL where the trust anchor for verifying this attestation can be retrieved | URI           |
| schema_version      | Version of the schema used for this attestation                            | String        |

### 2.7 Conditional Metadata

No conditional metadata elements are defined for this attestation type.

### 2.8 Value Lists

#### 2.8.1 Economic Operator Identifier Type Codes

The `parent_economic_operator_main_id` and `parent_economic_operator_id` sub-fields
**SHALL** use one or more of the following standardized identifier types:

| **Code** | **Definition**                                                                                                          |
|----------|-------------------------------------------------------------------------------------------------------------------------|
| EUID     | European Unique Identifier per Directive (EU) 2017/1132 — preferred identifier for EU legal entities                   |
| LEI      | Legal Entity Identifier per ISO 17442 (20-character alphanumeric code)                                                  |
| DUNS     | Data Universal Numbering System — Dun & Bradstreet company identifier                                                   |
| EORI     | Economic Operators Registration and Identification number — EU customs identifier                                        |
| TAX      | National tax or registration number — national identifier                                                                |
| BPNL     | Business Partner Number Legal entity — Catena-X identifier per International Code Designator (ICD): 0243                |
| GLN      | Global Location Number for legal entities — GS1 identifier                                                              |
| SIREN    | Système d'Identification du Répertoire des ENtreprises — French company identifier                                      |

#### 2.8.2 Site Identifier Type Codes

The `site_additional_ids` attribute **SHALL** use one or more of the following standardized
site-level identifier types:

| **Code**  | **Definition**                                                                                                          |
|-----------|-------------------------------------------------------------------------------------------------------------------------|
| DUNS_site | DUNS site-level identifier issued by Dun & Bradstreet                                                                   |
| BPNS      | Business Partner Number Site — Catena-X site-level identifier per International Code Designator (ICD): 0243             |
| GLN_site  | Global Location Number for physical locations — GS1 site-level identifier                                               |
| SIRET     | Système d'Identification du Répertoire des ETablissements — French site-level identifier (establishment number)         |

> **Notes on identifier standards:**
> - **SIRET**: see [Numéro SIRET — L'Annuaire des Entreprises](https://annuaire-entreprises.data.gouv.fr)
> - **GLN_site**: see [Global Location Number — Schema.org Property](https://schema.org/globalLocationNumber)
> - **site_main_id (UUID)**: see [Self Attested siteID — Schema.org Property](https://schema.org/propertyID)
> - **DUNS**: Dun & Bradstreet issues and maintains the DUNS Number database
> - **BPNL / BPNS**: assigned per International Code Designator (ICD): 0243 as standardized
    >   by DIN e.V. for use in the Catena-X automotive data ecosystem
> - For all other attributes within the Site Attestation, no public value lists are currently available

### 2.9 Integrity Rules

The following integrity rules **SHALL** be enforced:

- The `Site` object **SHALL** appear exactly once per attestation.
- `parent_economic_operator_main_id` **SHALL** be a non-empty string containing at least
  one valid economic operator identifier.
- `parent_economic_operator_main_id` **SHOULD** be an EUID for economic operators
  registered within the EU.
- `parent_economic_operator_id` **SHALL** contain at least one non-empty sub-field drawn
  from the identifier types listed in Section 2.8.1.
- `site_name` **SHALL** be a non-empty string.
- `site_main_id` **SHALL** be a valid UUID string.
- `site_main_id` **SHALL NOT** change during the lifecycle of the site.
- `site_main_address` **SHALL** be present and **SHALL** contain at minimum `street`, `nr`,
  `postal_code`, and `city`.
- `site_additional_ids`, when present, **SHALL** be an array of non-empty strings using
  identifier types from Section 2.8.2.
- `site_additional_addresses`, when present, **SHALL** be an array of Address objects each
  containing at minimum `street`, `nr`, `postal_code`, and `city`.
- `issuance_date` and `expiry_date` **SHALL** be valid ISO 8601 DateTimes.
- `expiry_date` **SHALL** be later than `issuance_date`.
- `issuance_date` **SHALL** be in the past.
- `attestation_legal_category` **SHALL** be `"EAA"`.
- `vct` **SHALL** be a non-empty string conforming to a URL or URN format.
- If `trust_anchor_url` is present, it **SHALL** be a valid URI.
- If `schema_version` is present, it **SHALL** be a non-empty string.
- Each attribute **SHALL** appear at most once within its respective object scope.

---

## 3 Attestation Encoding

### 3.1 ISO/IEC 18013-5-Compliant Encoding

ISO/IEC 18013-5 (also called mdoc) is out of scope for this Rulebook, as offline proximity
presentation is not a current requirement for the Site Attestation.

### 3.2 SD-JWT VC-Based Encoding

The Site Attestation uses the SD-JWT VC format to allow for selective disclosure of site
attributes.

**Selective Disclosure:** Top-level claims (e.g., `parent_economic_operator_main_id`,
`parent_economic_operator_id`, `site_name`, `site_main_id`, `site_main_address`,
`site_additional_addresses`) **SHALL** be individually selectively disclosable, enabling an
economic operator to disclose only the attributes requested by a Relying Party.

The `.` notation is used to indicate the nesting of attributes.

**Verifiable Credential Type (`vct`):** `vct: eu.we-build:site:1`

#### 3.2.1 Attribute Encoding Table

**Site**

| **Data Identifier**                          | **Attribute Identifier**                     | **Encoding Format** | **Reference / Notes**                                                                                                   | **Disclosable** |
|----------------------------------------------|----------------------------------------------|---------------------|-------------------------------------------------------------------------------------------------------------------------|-----------------|
| **Site**                                     |                                              |                     |                                                                                                                         |                 |
| parent_economic_operator_main_id             | parent_economic_operator_main_id             | String              | Primary unique identifier of the economic operator; **SHALL** be non-empty; preferred: EUID for EU entities             | MUST            |
| parent_economic_operator_id                  | parent_economic_operator_id                  | Object              | Structured identifier object; **MUST** contain at least one non-empty sub-field from Section 2.8.1                     | MUST            |
| parent_economic_operator_id.euid             | parent_economic_operator_id.euid             | String              | European Unique Identifier — optional sub-field                                                                         | MUST            |
| parent_economic_operator_id.lei              | parent_economic_operator_id.lei              | String              | Legal Entity Identifier per ISO 17442 — optional sub-field                                                              | MUST            |
| parent_economic_operator_id.tax              | parent_economic_operator_id.tax              | String              | National tax or registration number — optional sub-field                                                                | MUST            |
| parent_economic_operator_id.gln              | parent_economic_operator_id.gln              | String              | Global Location Number for legal entities — optional sub-field                                                          | MUST            |
| parent_economic_operator_id.duns             | parent_economic_operator_id.duns             | String              | Dun & Bradstreet company identifier — optional sub-field                                                                | MUST            |
| parent_economic_operator_id.eori             | parent_economic_operator_id.eori             | String              | EU customs identifier — optional sub-field                                                                              | MUST            |
| parent_economic_operator_id.bpnl             | parent_economic_operator_id.bpnl             | String              | Catena-X BPNL identifier per ICD 0243 — optional sub-field                                                             | MUST            |
| parent_economic_operator_id.siren            | parent_economic_operator_id.siren            | String              | French company identifier (SIREN) — optional sub-field                                                                  | MUST            |
| site_name                                    | site_name                                    | String              | The name of the site; **SHALL** be non-empty                                                                            | MUST            |
| site_main_id                                 | site_main_id                                 | String (UUID)       | Globally unique identifier of the site; generated by EBW as UUID; **SHALL NOT** change during the lifecycle of the site | MUST            |
| site_additional_ids                          | site_additional_ids                          | Array of Strings    | Optional additional site-level identifiers; **SHOULD** use codes from Section 2.8.2                                     | MUST            |
| **SiteMainAddress**                          |                                              |                     |                                                                                                                         |                 |
| site_main_address.street                     | site_main_address.street                     | String              | Street of the site's main address                                                                                       | MUST            |
| site_main_address.nr                         | site_main_address.nr                         | String              | House/building number of the site's main address                                                                        | MUST            |
| site_main_address.postal_code                | site_main_address.postal_code                | String              | Postal code of the site's main address                                                                                  | MUST            |
| site_main_address.city                       | site_main_address.city                       | String              | City of the site's main address                                                                                         | MUST            |
| **SiteAdditionalAddresses**                  |                                              |                     |                                                                                                                         |                 |
| site_additional_addresses                    | site_additional_addresses                    | Array of Address    | Optional array of additional addresses associated to the site (e.g., additional entrances or external/rented buildings) | MUST            |
| site_additional_addresses[n].street          | site_additional_addresses[n].street          | String              | Street of the additional address                                                                                        | MUST            |
| site_additional_addresses[n].nr              | site_additional_addresses[n].nr              | String              | House/building number of the additional address                                                                         | MUST            |
| site_additional_addresses[n].postal_code     | site_additional_addresses[n].postal_code     | String              | Postal code of the additional address                                                                                   | MUST            |
| site_additional_addresses[n].city            | site_additional_addresses[n].city            | String              | City of the additional address                                                                                          | MUST            |
| **Metadata**                                 |                                              |                     |                                                                                                                         |                 |
| attestation_legal_category                   | attestation_legal_category                   | String              | "EAA" as defined by eIDAS 2                                                                                             | MUST NOT        |

**Notes:**

- **MUST**: The claim **SHALL** be selectively disclosable — the holder **MAY** choose to
  disclose or withhold this claim when presenting the credential to a Relying Party.
- **MAY**: The claim **MAY** be selectively disclosable if the issuer supports it; the holder
  can choose to disclose or withhold.
- **MUST NOT**: The claim **SHALL NOT** be selectively disclosable — it is always present in
  plain text in the JWT header/payload and cannot be withheld by the holder, as it is required
  for credential verification and trust establishment.
- `iat`, `exp`, and `iss` follow RFC 7519 standard JWT claim naming conventions.
- `site_additional_addresses` entries are marked as `MUST` disclosable as a unit — individual
  address attributes within an array entry are not independently selectively disclosable in
  this version.
- Individual sub-fields of `parent_economic_operator_id` are selectively disclosable
  independently, allowing an economic operator to present only the identifier(s) requested
  by a Relying Party.

#### 3.2.2 Status Claim

For SD-JWT VC-compliant Site Attestations, the attestation **MUST** include a `status` claim
if the technical validity period is greater than 24 hours. This claim enables Relying Parties
to determine if a credential has been revoked via a status list mechanism, as specified in
SD-JWT VC.

The `status` claim **SHALL** be a JSON object with the following members:

- `type` (string): **SHALL** be `"status-list"`.
- `status_list_credential` (string, URI): The URI of the Status List Credential document
  that contains the status bitstring.
- `status_list_index` (integer, >= 0): The zero-based index into the status list bitstring
  that corresponds to this credential.
- `status_purpose` (string): **SHALL** be `"revocation"` for this attestation.

**Example:**

```json
{
  "status": {
    "type": "status-list",
    "status_list_credential": "https://issuer.example.com/status/site/2025",
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
  "attestation_legal_category": "EAA",
  "iss": "did:example:robert-bosch-gmbh",
  "iat": 1746000000,
  "exp": 1777536000,
  "jti": "site-attestation-20260515-001",
  "parent_economic_operator_main_id": "DE-HRB-396699",
  "parent_economic_operator_id": {
    "euid": "DE-HRB-396699",
    "lei": "529900HNOAA1KXQJUQ27",
    "duns": "330502866",
    "eori": "DE123456789",
    "bpnl": "BPNL000000000001",
    "tax": "DE811001001",
    "gln": "4012345000009",
    "siren": "542107651"
  },
  "site_name": "Bosch Karlsruhe Manufacturing Site",
  "site_main_id": "550e8400-e29b-41d4-a716-446655440000",
  "site_additional_ids": [
    "BPNS0000000001XY",
    "GLN-4012345000016"
  ],
  "site_main_address": {
    "street": "Auf der Breit",
    "nr": "4",
    "postal_code": "76227",
    "city": "Karlsruhe"
  },
  "site_additional_addresses": [
    {
      "street": "Robert-Bosch-Strasse",
      "nr": "2",
      "postal_code": "76131",
      "city": "Karlsruhe"
    }
  ],
  "status": {
    "type": "status-list",
    "status_list_credential": "https://example.com/status/site-list-1",
    "status_list_index": 789,
    "status_purpose": "revocation"
  },
  "trust_anchor_url": "https://trust.webuildconsortium.eu/anchors/eidas-tl",
  "schema_version": "0.4.0",
  "cnf": {
    "jwk": {
      "kty": "EC",
      "crv": "P-256",
      "x": "abc-123_def-456_ghi-789_jkl-012",
      "y": "mno-345_pqr-678_stu-901_vwx-234"
    }
  }
}
```
Sample payloads are provided under  ../data-schemas/sd-jwt/sample-data/site-attestation-sd-jwt-sample.json


### 3.3 W3C Verifiable Credentials Data Model-based encoding

@TODO — To be discussed: which stakeholders will support this format and which use cases require it.

## 4 Attestation usage
### 4.1. Issuance process ###

### 4.2 Relying Party Obligations
When receiving and processing an attestation, the Relying Party SHALL perform the following verification obligations.
### 4.2.1 – 4.2.8 Base Verification Process
The Relying Party SHALL perform the base attestation verification process as defined in the Base Verification specification:
https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-base/verifier-base-verification.md
### 4.2.9 Validate Integrity Rules
Validation of integrity and policy rules will be specified in a future version of this Rulebook.

## 5 Trust anchors
This chapter will be completed in a future version of this Rulebook.

## 6 Revocation
This chapter will be completed in a future version of this Rulebook.

## 7 References
This chapter will be completed in a future version of this Rulebook.

## 8 References

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