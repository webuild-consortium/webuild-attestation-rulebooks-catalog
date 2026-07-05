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
| Certified Site         | A physical location (site/address) for which the ESG certificate is valid, as defined in the certificate scope                                                                 |
| Scope of Certification | The description of the activities, products, services, or locations covered by the certificate                                                                                 |
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

The ESG Certificate Attestation is designed to provide a standardized, verifiable digital
representation of ESG-related certificates held by a legal entity. It captures all essential
attributes of a physical or digital ESG certificate, including the economic operator identity,
certificate metadata, certified scope with site-level granularity, and optional evidence, in a
machine-readable and selectively disclosable format.

### 2.1 Introduction

**Data Model:**



```

[Economic Operator] --- owns --- [Certificate] --- allocated to --- [Site and Scope]

Certificate [1]
├─ economic_operator_main_id (tstr) — mandatory
├─ economic_operator_additional_ids (Array of identifier strings) — optional [0..n]
├─ economic_operator_name (tstr) — mandatory
├─ economic_operator_address (Address) — mandatory
│ ├─ street (tstr)
│ ├─ nr (tstr)
│ ├─ postal_code (tstr)
│ └─ city (tstr)
├─ certificate_type (tstr) — mandatory
├─ certificate_version (tstr) — mandatory
├─ registration_number (tstr) — mandatory
├─ certification_start_date (date) — mandatory
├─ certification_expiration_date (date) — mandatory
├─ scope (Array of ScopeObject) [1..n] — mandatory
│ ├─ operating_legal_entity_name (tstr) — mandatory
│ ├─ legal_entity_IDs (Array of LegalEntityID) — mandatory
│ ├─ site_location_address (Address) — mandatory
│ │ ├─ street (tstr)
│ │ ├─ nr (tstr)
│ │ ├─ postal_code (tstr)
│ │ └─ city (tstr)
│ ├─ scope_description (tstr) — mandatory
│ └─ certified_site (boolean) — mandatory
└─ certificate_evidence (Evidence) — mandatory
├─ evidence_id (tstr) — mandatory
├─ evidence_type (tstr) — optional
├─ evidence_digestMultibase (tstr) — optional
└─ evidence_data (tstr, base64) — optional
```
*Note*: M - mandatory / O - optional.

**Explanation:**
- The `Certificate` object **SHALL** appear exactly once per attestation.
- `economic_operator_main_id`, `economic_operator_name`, `economic_operator_address`,
  `certificate_type`, `certificate_version`, `registration_number`,
  `certification_start_date`, `certification_expiration_date`, `scope`,
  and `certificate_evidence` are mandatory top-level attributes.
- `economic_operator_additional_ids` is optional and **MAY** contain zero or more additional
  identifier strings (e.g., LEI, EORI, BPNL).
- `scope` **SHALL** contain at least one `ScopeObject`, representing a
  certified site with its associated scope description.
- `certificate_evidence` is mandatory as an object; however, `evidence_type`,
  `evidence_digestMultibase`, and `evidence_data` within it are optional and only required
  in cases of self-attestation of a received certificate.
- `certified_site` is a boolean flag indicating whether the certificate applies to the entire
  site (`true`) or only to specific functions or areas of the site (`false`).

**Attestation Classification:**

This attestation type **MAY** be classified as:
- **"EAA"** self-issued by the legal entity as part of its disclosures.
- **"QEAA"** issued by a Qualified Trust Service Provider (QTSP) or authorized competent body that can independently attest it

**Top-Level Data Identifiers:**

| **Data Identifier**                | **Semantic Reference** | **Definition**                                                                                 | **Data type**       |
|------------------------------------|------------------------|------------------------------------------------------------------------------------------------|---------------------|
| economic_operator_main_id          | ...                    | Primary unique identifier of the economic operator holding the certificate                     | String              |
| economic_operator_additional_ids   | ...                    | Array of additional identifiers for the economic operator                                      | Array of Strings    |
| economic_operator_name             | ...                    | Legal name of the economic operator                                                            | String              |
| economic_operator_address          | ...                    | Registered address of the economic operator                                                    | Object (Address)    |
| certificate_type                   | ...                    | Type of the ESG certificate (e.g., ISO 9001, IATF 16949)                                      | String              |
| certificate_version                | ...                    | Version of the certificate standard (e.g., ISO 9001:2015)                                     | String              |
| registration_number                | ...                    | Registration number of the certificate as issued by the certification body                     | String              |
| certification_start_date           | ...                    | Valid-from date of the certificate                                                             | Date (ISO 8601)     |
| certification_expiration_date      | ...                    | Valid-until date of the certificate                                                            | Date (ISO 8601)     |
| scope                              | ...                    | Array of certified site and scope objects                                                      | Array [ScopeObject] |
| certificate_evidence               | ...                    | Evidence object containing reference or attachment of the original certificate                 | Object (Evidence)   |

### 2.2 Mandatory Attributes

#### Certificate Top-Level Attributes

| **Data Identifier**             | **Semantic Reference** | **Definition**                                                                                                                       | **Data type**             |
|---------------------------------|------------------------|--------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| economic_operator_main_id       | —                      | Primary unique identifier created and assigned to the economic operator (e.g., EUID)                                                 | tstr                      |
| economic_operator_name          | —                      | Legal name of the economic operator holding the certificate                                                                          | tstr                      |
| economic_operator_address       | —                      | Registered address of the economic operator                                                                                          | Address object            |
| certificate_type                | —                      | Type of the certificate as defined on the document (e.g., ISO 9001, IATF 16949, DIN EN ISO 14001)                                   | tstr                      |
| certificate_version             | —                      | Version of the certificate standard as defined on the document (e.g., ISO 9001:2015)                                                | tstr                      |
| registration_number             | —                      | Registration number of the certificate as defined on the certificate document                                                        | tstr                      |
| certification_start_date        | —                      | Valid-from date as defined on the certificate (ISO 8601)                                                                             | date                      |
| certification_expiration_date   | —                      | Valid-until date as defined on the certificate; `9999-12-31` indicates no expiration (ISO 8601)                                      | date                      |
| scope                           | —                      | Array describing the affected certified legal entities with name, location, and scope; **SHALL** contain at least one entry          | Array of ScopeObject [1..n] |
| certificate_evidence            | —                      | Object containing evidence-related information for the attached certificate; required for self-attestation of a received certificate | Evidence object           |

#### Address Object Attributes

Applies to both `economic_operator_address` and `site_location_address`:

| **Data Identifier** | **Semantic Reference** | **Definition**                          | **Data type** |
|---------------------|------------------------|-----------------------------------------|---------------|
| street              | —                      | Street name of the address              | tstr          |
| nr                  | —                      | House or building number of the address | tstr          |
| postal_code         | —                      | Postal code of the address              | tstr          |
| city                | —                      | City of the address                     | tstr          |

#### ScopeObject Attributes

Each entry in the `scope` array **SHALL** contain the following attributes:

| **Data Identifier**           | **Semantic Reference** | **Definition**                                                                                      | **Data type**            |
|-------------------------------|------------------------|-----------------------------------------------------------------------------------------------------|--------------------------|
| operating_legal_entity_name   | —                      | Legal name of the site operating entity                                                             | tstr                     |
| legal_entity_IDs              | —                      | Array of legal entity identifiers for the operating entity; **SHALL** use types from Section 2.8.1 | Array of LegalEntityID   |
| site_location_address         | —                      | Physical address of the certified site                                                              | Address object           |
| scope_description             | —                      | Textual description of the certificate scope applicable to this site                                | tstr                     |
| certified_site                | —                      | Boolean value: `true` = whole site certified; `false` = partial site only                          | boolean                  |

#### Evidence Object Attributes

| **Data Identifier** | **Semantic Reference** | **Definition**                                                 | **Data type** |
|---------------------|------------------------|----------------------------------------------------------------|---------------|
| evidence_id         | —                      | Unique certificate identifier following the UUID or URI format | tstr          |

### 2.3 Optional Attributes

#### Certificate Optional Attributes

| **Data Identifier**              | **Semantic Reference** | **Definition**                                                                                                                                                  | **Data type**           |
|----------------------------------|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| economic_operator_additional_ids | —                      | Array of additional economic operator identifiers (e.g., LEI, EORI, BPNL, VAT ID). **SHALL** use types from Section 2.8.1. **MAY** contain zero or more entries | Array of Strings [0..n] |

#### Evidence Optional Attributes

| **Data Identifier**        | **Semantic Reference** | **Definition**                                                                                                                                                   | **Data type**   |
|----------------------------|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| evidence_type              | —                      | Defines the type of the evidence object; **SHALL** be `"Evidence"` when present                                                                                  | tstr            |
| evidence_digestMultibase   | —                      | Content digest value for verification, used when `evidence_id` is a URI pointing to the certificate content                                                      | tstr            |
| evidence_data              | —                      | The actual certificate document encoded as a base64 string. **SHALL** be present if `evidence_id` does not contain a URI to an accessible location with the content | tstr (base64)   |

### 2.4 Conditional Attributes

| **Data Identifier**        | **Condition**                                                                                    | **Definition**                                                          | **Data type**   |
|----------------------------|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|-----------------|
| evidence_data              | **SHALL** be present if `evidence_id` does not contain a URI to an existing accessible location  | The actual certificate document as a base64-encoded string              | tstr (base64)   |
| evidence_digestMultibase   | **SHOULD** be present if `evidence_id` is a URI pointing to an external location               | Content digest for integrity verification of the referenced certificate | tstr            |

### 2.5 Mandatory Metadata

| **Data Identifier**        | **Definition**                                                                | **Data type** |
|----------------------------|-------------------------------------------------------------------------------|---------------|
| attestation_legal_category | Indicates the legal category of the AuthorisedSignatories Attestation ("EAA") | String        |
| cnf                        | Cryptographic Key Binding                                                     | String        |

*Note*: Only the additional mandatory attributes are listed; the mandatory attributes defined by the protocol are not specified.

### 2.6 Optional Metadata

### 2.7 Conditional Metadata

No conditional metadata elements are defined for this attestation type.

### 2.8 Value Lists

#### 2.8.1 Legal Entity Identifier Type Codes

The `legal_entity_IDs` and `economic_operator_additional_ids` attributes **SHALL** use one or
more of the following standardized identifier types:

| **Code**           | **Definition**                                                                                                         |
|--------------------|------------------------------------------------------------------------------------------------------------------------|
| EUID               | European Unique Identifier per Directive (EU) 2017/1132                                                                |
| LEI                | Legal Entity Identifier per ISO 17442 (20-character alphanumeric code)                                                 |
| DUNS               | Data Universal Numbering System — Dun & Bradstreet company identifier                                                  |
| EORI               | Economic Operators Registration and Identification number — EU customs identifier                                       |
| VAT_ID             | Value Added Tax identification number — national tax identifier                                                         |
| BPNL               | Business Partner Number Legal entity — Catena-X identifier per International Code Designator (ICD): 0243               |
| GLN_legal_entity   | Global Location Number for legal entities — GS1 identifier                                                             |
| SIREN              | Système d'Identification du Répertoire des ENtreprises — French company identifier                                     |

> **Note:** The BPNL follows the structure `BPN[LSA][A-Z0-9]{10}[A-Z0-9]{2}` and is assigned
> per ICD 0243 as standardized by DIN e.V. for use in the Catena-X automotive data ecosystem.

#### 2.8.2 Certificate Type Codes

The `certificate_type` attribute **SHOULD** use one of the following standardized values where
applicable. Other certificate types **MAY** be used as free-text strings:

| **Code**    | **Definition**                                          |
|-------------|---------------------------------------------------------|
| ISO9001     | Quality Management Systems                              |
| IATF16949   | Automotive Quality Management Systems                   |
| ISO14001    | Environmental Management Systems                        |
| ISO45001    | Occupational Health and Safety Management Systems       |
| ISO50001    | Energy Management Systems                               |
| AEO         | Authorised Economic Operator — EU customs certification |

#### 2.8.3 Certified Site Flag

The `certified_site` attribute **SHALL** use a boolean value with the following semantics:

| **Value** | **Definition**                                                                                                                                                             |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| true      | The certificate is valid for the entire site at the specified address                                                                                                      |
| false     | The certificate is not valid for the entire site; the address may refer to a rented building or only specific functions or departments of the site are certified            |

### 2.9 Integrity Rules

The following integrity rules **SHALL** be enforced:

- The `Certificate` object **SHALL** appear exactly once per attestation.
- `economic_operator_main_id` **SHALL** be a non-empty string.
- `economic_operator_name` **SHALL** be a non-empty string.
- `economic_operator_address` **SHALL** contain at minimum `street`, `nr`, `postal_code`,
  and `city`.
- `certificate_type` **SHALL** be a non-empty string.
- `certificate_version` **SHALL** be a non-empty string.
- `registration_number` **SHALL** be a non-empty string.
- `certification_start_date` **SHALL** be a valid ISO 8601 date (YYYY-MM-DD).
- `certification_expiration_date` **SHALL** be a valid ISO 8601 date (YYYY-MM-DD) or the
  sentinel value `9999-12-31` indicating no expiration.
- `certification_expiration_date` **SHALL** be equal to or later than
  `certification_start_date`, unless the value is `9999-12-31`.
- `scope` **SHALL** contain at least one `ScopeObject`.
- Each `ScopeObject` **SHALL** contain `operating_legal_entity_name`, `legal_entity_IDs`,
  `site_location_address`, `scope_description`, and `certified_site`.
- `legal_entity_IDs` within each `ScopeObject` **SHALL** contain at least one identifier entry.
- Each identifier in `legal_entity_IDs` **SHOULD** use an identifier type from Section 2.8.1.
- `certified_site` **SHALL** be a boolean value (`true` or `false`).
- `site_location_address` **SHALL** contain at minimum `street`, `nr`, `postal_code`,
  and `city`.
- `certificate_evidence` **SHALL** be present and **SHALL** contain at minimum `evidence_id`.
- `evidence_id` **SHALL** be a non-empty string following UUID or URI format.
- If `evidence_id` does not contain a resolvable URI, `evidence_data` **SHALL** be present
  and **SHALL** contain the certificate as a valid base64-encoded string.
- If `evidence_digestMultibase` is present, it **SHALL** be a non-empty string providing a
  valid content digest of the referenced certificate.
- `issuance_date` and `expiry_date` **SHALL** be valid ISO 8601 DateTimes.
- `expiry_date` **SHALL** be later than `issuance_date`.
- `issuance_date` **SHALL** be in the past.
- `attestation_legal_category` **SHALL** be one of `"EAA"` or `"QEAA"`.
- `vct` **SHALL** be a non-empty string conforming to a URL or URN format.
- If `trust_anchor_url` is present, it **SHALL** be a valid URI.
- If `schema_version` is present, it **SHALL** be a non-empty string.
- Each attribute **SHALL** appear at most once within its respective object scope.

---

## 3 Attestation Encoding

### 3.1 ISO/IEC 18013-5-Compliant Encoding

ISO/IEC 18013-5 (also called mdoc) is out of scope for this Rulebook, as offline proximity
presentation is not a current requirement for the ESG Certificate Attestation.

### 3.2 SD-JWT VC-Based Encoding

The ESG Certificate Attestation uses the SD-JWT VC format to allow for selective disclosure
of certificate attributes.

**Selective Disclosure:** Top-level claims (e.g., `economic_operator_name`, `certificate_type`,
`scope`, `certificate_evidence`) **SHALL** be individually selectively disclosable, enabling a
legal entity to disclose only the attributes requested by a Relying Party. Attributes nested
within `ScopeObject` entries **MAY** be individually selectively disclosable as per the
attribute encoding table below.

The `.` notation is used to indicate the nesting of attributes.

**Verifiable Credential Type (`vct`):** `vct: eu.we-build:esgcertificate:1`

#### 3.2.1 Attribute Encoding Table

| **Data Identifier**                   | **Attribute Identifier**                      | **Encoding Format**          | **Reference / Notes**                                                                                 | **Disclosable** |
|---------------------------------------|-----------------------------------------------|------------------------------|-------------------------------------------------------------------------------------------------------|-----------------|
| economic_operator_main_id             | economic_operator_main_id                     | String                       | Primary unique identifier of the economic operator; **SHALL** be non-empty                            | MUST            |
| economic_operator_additional_ids      | economic_operator_additional_ids              | Array of Strings             | Optional additional identifiers; **SHOULD** use codes from Section 2.8.1                              | MUST            |
| economic_operator_name                | economic_operator_name                        | String                       | Legal name of the economic operator                                                                   | MUST            |
| economic_operator_address.street      | economic_operator_address.street              | String                       | Street of the economic operator's registered address                                                  | MUST            |
| economic_operator_address.nr          | economic_operator_address.nr                  | String                       | House/building number of the economic operator's registered address                                   | MUST            |
| economic_operator_address.postal_code | economic_operator_address.postal_code         | String                       | Postal code of the economic operator's registered address                                             | MUST            |
| economic_operator_address.city        | economic_operator_address.city                | String                       | City of the economic operator's registered address                                                    | MUST            |
| certificate_type                      | certificate_type                              | String                       | Type of the certificate; **SHOULD** use codes from Section 2.8.2                                      | MUST            |
| certificate_version                   | certificate_version                           | String                       | Version of the certificate standard (e.g., ISO 9001:2015)                                             | MUST            |
| registration_number                   | registration_number                           | String                       | Registration number of the certificate as issued by the certification body                            | MUST            |
| certification_start_date              | certification_start_date                      | String (ISO 8601 YYYY-MM-DD) | Valid-from date of the certificate                                                                    | MUST            |
| certification_expiration_date         | certification_expiration_date                 | String (ISO 8601 YYYY-MM-DD) | Valid-until date of the certificate; `9999-12-31` indicates no expiration                             | MUST            |
| **ScopeObject**                       |                                               |                              |                                                                                                       |                 |
| scope                                 | scope                                         | Array [ScopeObject]          | Array of certified site and scope objects; **SHALL** contain at least one entry                       | MUST            |
| operating_legal_entity_name           | scope[n].operating_legal_entity_name          | String                       | Legal name of the site operating entity                                                               | MUST            |
| legal_entity_IDs                      | scope[n].legal_entity_IDs                     | Array of Strings             | Legal entity identifiers; **SHALL** use types from Section 2.8.1                                      | MUST            |
| site_location_address_street          | scope[n].site_location_address_street         | String                       | Street of the certified site address                                                                  | MUST            |
| site_location_address_nr              | scope[n].site_location_address_nr             | String                       | House/building number of the certified site address                                                   | MUST            |
| site_location_address_postal_code     | scope[n].site_location_address_postal_code    | String                       | Postal code of the certified site address                                                             | MUST            |
| site_location_address_city            | scope[n].site_location_address_city           | String                       | City of the certified site address                                                                    | MUST            |
| scope_description                     | scope[n].scope_description                    | String                       | Textual description of the certification scope for this site                                          | MUST            |
| certified_site                        | scope[n].certified_site                       | Boolean                      | `true` = whole site certified; `false` = partial site only                                            | MUST            |
| **Evidence**                          |                                               |                              |                                                                                                       |                 |
| evidence_id                           | certificate_evidence.evidence_id              | String (UUID or URI)         | Unique identifier of the certificate evidence; **SHALL** be non-empty                                 | MUST            |
| evidence_type                         | certificate_evidence.evidence_type            | String                       | Type of the evidence object; **SHALL** be `"Evidence"` when present; optional                         | MAY             |
| evidence_digestMultibase              | certificate_evidence.evidence_digestMultibase | String                       | Content digest for integrity verification of referenced certificate; optional                         | MAY             |
| evidence_data                         | certificate_evidence.evidence_data            | String (base64)              | The actual certificate as a base64-encoded string; **SHALL** be present if `evidence_id` is not a URI | MAY             |
| **Metadata**                          |                                               |                              |                                                                                                       |                 |
| issuance_date                         | `iat`                                         | Number (Unix timestamp)      | Date and time when the attestation was issued (ISO 8601); RFC 7519                                    | MUST NOT        |
| expiry_date                           | `exp`                                         | Number (Unix timestamp)      | Date and time when the attestation expires (ISO 8601); RFC 7519                                       | MUST NOT        |
| issuing_entity                        | `iss`                                         | String (URI or DID)          | Identifier of the competent institution that issued the attestation; RFC 7519                         | MUST NOT        |
| attestation_legal_category            | `attestation_legal_category`                  | String                       | One of "EAA" or "QEAA" as defined by eIDAS 2                                                          | MUST NOT        |
| vct                                   | `vct`                                         | String                       | The vct definition                                                                                    | MUST NOT        |
| cnf                                   | `cnf`                                         | String                       | Cryptographic Key Binding                                                                             | MUST NOT        |
| trust_anchor_url                      | `trust_anchor_url`                            | String (URI)                 | URL where the trust anchor for verifying this attestation can be retrieved; optional                  | MAY             |
| schema_version                        | `schema_version`                              | String                       | Version of the schema used; optional                                                                  | MAY             |

**Notes:**

- **MUST**: The claim **SHALL** be selectively disclosable — the holder **MAY** choose to
  disclose or withhold this claim when presenting the credential to a Relying Party.
- **MAY**: The claim **MAY** be selectively disclosable if the issuer supports it; the holder
  can choose to disclose or withhold.
- **MUST NOT**: The claim **SHALL NOT** be selectively disclosable — it is always present in
  plain text in the JWT header/payload and cannot be withheld by the holder, as it is required
  for credential verification and trust establishment.
- `iat`, `exp`, and `iss` follow RFC 7519 standard JWT claim naming conventions.
- `scope` entries are marked as `MUST` disclosable as a unit — individual scope attributes
  within an array entry are not independently selectively disclosable in this version.

#### 3.2.2 Status Claim

For SD-JWT VC-compliant Attestations, the attestation MUST include a `status` claim if  the technical validity period is greater than 24 hours. This claim enables Relying Parties to
determine if a credential has been revoked via a status list mechanism, as specified in SD-JWT VC.

The `status` claim SHALL be a JSON object with the following members:

| **Field**                | **Type**       | **Value / Constraint**                                                     |
|--------------------------|----------------|----------------------------------------------------------------------------|
| `type`                   | String         | SHALL be `"status-list"`                                                   |
| `status_list_credential` | String (URI)   | URI of the Status List Credential document containing the status bitstring |
| `status_list_index`      | Integer (>= 0) | Zero-based index into the status list bitstring for this credential        |
| `status_purpose`         | String         | SHALL be `"revocation"`                                                    |

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
### 3.2.3 Example Payload
The following is a non-normative example of an ESG Certificate Attestation SD-JWT VC payload,
based on the ISO 9001:2015 certificate illustrated in Appendix 1
```
{
  "vct": "eu.we-build:esgcertificate:1",
  "attestation_legal_category": "EAA",
  "iss": "did:example:robert-bosch-gmbh",
  "iat": 1724284800,
  "exp": 1882051200,
  "jti": "esg-cert-attestation-20240822-001",
  "economic_operator_main_id": "DE-HRB-396699",
  "economic_operator_additional_ids": [
    "BPNL000000000001",
    "DE811001001"
  ],
  "economic_operator_name": "Robert Bosch GmbH",
  "economic_operator_address": {
    "street": "Auf der Breit",
    "nr": "4",
    "postal_code": "76227",
    "city": "Karlsruhe"
  },
  "certificate_type": "ISO9001",
  "certificate_version": "ISO 9001:2015",
  "registration_number": "DE015008",
  "certification_start_date": "2024-08-22",
  "certification_expiration_date": "2027-08-22",
  "scope": [
    {
      "operating_legal_entity_name": "Robert Bosch GmbH",
      "legal_entity_IDs": ["DE-HRB-396699", "BPNL000000000001"],
      "site_location_address_street": "Auf der Breit",
      "site_location_address_nr": "4",
      "site_location_address_postal_code": "76227",
      "site_location_address_city": "Karlsruhe"
      "scope_description": "Provision, logistics and worldwide distribution of automotive
      parts, as well as development, production and distribution of products and services
      for the vehicle manufacturers and the automotive aftermarket.",
      "certified_site": true
    },
    {
      "operating_legal_entity_name": "Holger Christiansen A/S",
      "legal_entity_IDs": ["DK-CVR-12345678"],
      "site_location_address_street": "Hedelundvej",
      "site_location_address_nr": "13",
      "site_location_address_postal_code": "6705",
      "site_location_address_city": "Esbjerg"
      "scope_description": "Sales and logistics of auto mechanical and auto electrical products",
      "certified_site": false
    }
  ],
  "certificate_evidence": {
    "evidence_id": "urn:uuid:550e8400-e29b-41d4-a716-446655440000",
    "evidence_type": "Evidence",
    "evidence_digestMultibase": "zQmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco",
    "evidence_data": "JVBERi0xLjQKJcOkw7zDtsO..."
  },
  "status": {
    "type": "status-list",
    "status_list_credential": "https://example.com/status/esgcertificate-list-1",
    "status_list_index": 456,
    "status_purpose": "revocation"
  },
  "trust_anchor_url": "https://trust.webuildconsortium.eu/anchors/eidas-tl",
  "schema_version": "0.3.0",
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