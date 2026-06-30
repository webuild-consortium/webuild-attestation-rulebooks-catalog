# Attestation Rulebook for attestations of type DUNS Legal Entity Attestation

* **Author(s):**
    * [Werner Folkendt, Robert Bosch GmbH]
* **Reviewer(s):**
    * [Dominic Hurni, SBB]
    * [Florin Coptil, Robert Bosch GmbH]

| Version | Date       | Description                                                  |
|---------|------------|--------------------------------------------------------------|
| 0.1     | 23.06.2026 | Initial draft based on the WeBuild design attestation meetings |
| 0.6     | 29.06.2026 | update layout                                                |

* **Contact:**
    * [Werner Folkendt](mailto:werner.folkendt@de.bosch.com)

## 1 DUNS Legal Entity Attestation

A DUNS Legal Entity Attestation provides legal entity information according to the
data provided by a legal entity to Dun & Bradstreet to obtain a DUNS number. A DUNS
number is a unique identifier issued by Dun & Bradstreet (DUNS – Data Universal
Numbering System) for three types of business entities: a) legal entities b) sites and
c) locations.

The DUNS number is a nine-digit numeric code that uniquely identifies a business
entity worldwide, providing a standardized reference for suppliers, customers, and
regulatory authorities.

In the context of supplier verification and the Know Your Supplier (KYS) process, a
DUNS number serves several critical functions. In several industry branches it is
impossible for a legal entity to do business without providing this number to business
partners.

### 1.1 Document scope and purpose

The DUNS Legal Entity Attestation is designed to provide a standardized, verifiable
representation of a legal entity's business profile as registered with Dun & Bradstreet,
including its legal identity, operational status, registration details, and industry
classification. This attestation complements the EUCC by providing additional non-core
identity attributes required for KYS, KYC, supplier onboarding, and risk assessment
processes.

### 1.2 Document structure

This Rulebook is structured as follows:

- Chapter 2 describes the DUNS attestation attributes and metadata in an encoding-independent manner, including the data model.
- Chapter 3 specifies how the attestation attributes and metadata are encoded: Section 3.2 covers SD-JWT VC-based encoding.
- Chapter 4 specifies attestation usage scenarios, Relying Party obligations, and integration with KYC/KYS workflows.
- Chapter 5 defines trust anchors and verification mechanisms for issuer authorization.
- Chapter 6 defines revocation mechanisms for the attestation.
- Chapter 7 provides compliance information regarding the EUDI framework and applicable data protection laws.

### 1.3 Keywords

This document uses the capitalised keywords `SHALL`, `SHOULD` and `MAY` as specified in
[RFC 2119], i.e. to indicate requirements, recommendations and options specified in this
document.

In addition, `must` (non-capitalised) is used to indicate an external constraint, i.e. a
requirement that is not mandated by this document, but, for instance, by an external document.
The word `can` indicates a capability, whereas other words, such as `will`, and `is` or `are`
are intended as statements of fact.

### 1.4 Terminology

*Additional terminology specific to this attestation:*

| Term         | Description                                                                                                                          |
|:-------------|:-------------------------------------------------------------------------------------------------------------------------------------|
| DUNS         | Data Universal Numbering System — a nine-digit identifier issued by Dun & Bradstreet to uniquely identify a business entity worldwide |
| EUCC         | EU Company Certificate – attestation establishing the legal existence and identity of a legal entity within the EU                   |
| NAICS        | North American Industry Classification System — a standard used to classify business establishments by industry                     |
| KYS          | Know Your Supplier — due diligence process for verifying supplier identity and assessing supply chain risk                           |
| KYC          | Know Your Customer — due diligence process for verifying customer identity                                                           |
| ISO 8601     | International standard for date and time representations (e.g., YYYY-MM-DD)                                                         |
| ISO 3166-1   | International standard for country codes (two-letter alpha-2 codes)                                                                  |
| EAA          | Electronic Attestation of Attributes as defined by eIDAS 2                                                                           |
| QEAA         | Qualified Electronic Attestation of Attributes as defined by eIDAS 2                                                                 |

---

## 2 Attestation attributes and metadata

The DUNS Credential provides a standardized, verifiable representation of a company with
all the relevant information from a DUNS perspective, including legal entity details,
operational status, registration information, and industry classification.

### 2.1 Data Model

The attestation structure is defined as a structured object:

```
DUNS
├─ duns_number (tstr)
├─ legal_entity (DUNSLegalEntity)
│   ├─ legal_name (tstr)
│   └─ legal_form (tstr)
│   └─ registered_address (Address)
│       ├─ [street]
│       ├─ [nr]
│       ├─ [postal_code]
│       ├─ [city]
│       └─ [country]
├─ operational_status (tstr)
├─ operational_status_date (date)
├─ date_of_incorporation (date)
├─ registration (DUNSRegistration)
│   ├─ jurisdiction (tstr)
│   ├─ initial_registration_date (date)
│   ├─ last_update_date (date)
│   └─ registration_status (date)
└─ industry_Classification (DUNSIndustry Classification)
├─ primary_naics (tstr)
├─ secondary_naics (Array of strings) (0-n)
└─ naics_version (tstr)
```

**Explanation:**

- `duns_number` is the mandatory nine-digit unique identifier assigned by Dun & Bradstreet to
  the legal entity.
- `legal_entity` is a mandatory object encapsulating the legal identity of the entity,
  containing:
    - `legal_name`: the registered legal name of the entity (mandatory).
    - `legal_form`: the legal form of the entity (e.g., GmbH, AG, Ltd.) (mandatory).
    - `registered_address`: the official registered address of the entity (mandatory object),
      with all address sub-fields being optional:
        - `street`: street name of the registered address.
        - `nr`: street or building number.
        - `postal_code`: postal or ZIP code.
        - `city`: city or municipality.
        - `country`: country of the registered address (ISO 3166-1 alpha-2).
- `operational_status` is a mandatory field indicating the current operational status of the
  entity (e.g., Active, Inactive, Dissolved).
- `operational_status_date` is the mandatory date on which the operational status was last
  confirmed or changed (ISO 8601).
- `date_of_incorporation` is the mandatory date on which the legal entity was incorporated
  or formally established (ISO 8601).
- `registration` is a mandatory object providing details about the entity's formal
  registration, containing:
    - `jurisdiction`: the jurisdiction in which the entity is registered (mandatory).
    - `initial_registration_date`: the date the entity was first registered (mandatory).
    - `last_update_date`: the date the registration record was last updated (mandatory).
    - `registration_status`: the current status of the registration record (mandatory).
- `industry_classification` is a mandatory object providing the NAICS-based industry
  classification of the entity, containing:
    - `primary_naics`: the primary NAICS code representing the entity's main business
      activity (mandatory).
    - `secondary_naics`: an optional array of zero or more additional NAICS codes
      representing secondary business activities.
    - `naics_version`: the version of the NAICS standard used (mandatory).

**Attestation Classification:**

This attestation type MAY be classified as:
- **"EAA"** when self-issued by the legal entity subject to the disclosure.
- **"QEAA"** when issued by a qualified trust service provider (QTSP) or authorized
  competent body that can independently attest the company information (e.g., based on
  official Dun & Bradstreet registry data).

**VC Type:** `vct: eu.we-build:duns:1`

### 2.2 Mandatory attributes

#### 2.2.1 DUNS Top-Level Attributes

| **Data Identifier**    | **Semantic Reference** | **Definition**                                                                                       | **Optionality** | **Encoding format** |
|------------------------|------------------------|------------------------------------------------------------------------------------------------------|-----------------|---------------------|
| duns_number            | --                     | Nine-digit unique identifier assigned by Dun & Bradstreet to the legal entity                        | M               | tstr                |
| operational_status     | --                     | Current operational status of the entity (e.g., Active, Inactive, Dissolved)                        | M               | tstr                |
| operational_status_date| --                     | Date on which the operational status was last confirmed or changed (ISO 8601)                        | M               | date (ISO 8601)     |
| date_of_incorporation  | --                     | Date on which the legal entity was incorporated or formally established (ISO 8601)                   | M               | date (ISO 8601)     |

#### 2.2.2 DUNSLegalEntity Object Attributes

| **Data Identifier**                    | **Semantic Reference** | **Definition**                                                                          | **Optionality** | **Encoding format**      |
|----------------------------------------|------------------------|-----------------------------------------------------------------------------------------|-----------------|--------------------------|
| legal_entity                           | --                     | Object encapsulating the legal identity of the entity                                   | M               | Object                   |
| legal_entity.legal_name                | --                     | The registered legal name of the entity                                                 | M               | tstr                     |
| legal_entity.legal_form                | --                     | The legal form of the entity (e.g., GmbH, AG, Ltd., SRL)                               | M               | tstr                     |
| legal_entity.registered_address        | --                     | The official registered address of the entity                                           | M               | Object                   |
| legal_entity.registered_address.street | --                     | Street name of the registered address                                                   | O               | tstr                     |
| legal_entity.registered_address.nr     | --                     | Street or building number of the registered address                                     | O               | tstr                     |
| legal_entity.registered_address.postal_code | --              | Postal or ZIP code of the registered address                                            | O               | tstr                     |
| legal_entity.registered_address.city   | --                     | City or municipality of the registered address                                          | O               | tstr                     |
| legal_entity.registered_address.country| --                     | Country of the registered address                                                       | O               | tstr (ISO 3166-1 alpha-2)|

#### 2.2.3 DUNSRegistration Object Attributes

| **Data Identifier**                    | **Semantic Reference** | **Definition**                                                                          | **Optionality** | **Encoding format** |
|----------------------------------------|------------------------|-----------------------------------------------------------------------------------------|-----------------|---------------------|
| registration                           | --                     | Object providing details about the entity's formal registration                         | M               | Object              |
| registration.jurisdiction              | --                     | The jurisdiction in which the entity is registered (e.g., country or region code)      | M               | tstr                |
| registration.initial_registration_date | --                     | The date the entity was first registered (ISO 8601)                                    | M               | date (ISO 8601)     |
| registration.last_update_date          | --                     | The date the registration record was last updated (ISO 8601)                           | M               | date (ISO 8601)     |
| registration.registration_status       | --                     | The current status of the registration record (e.g., Active, Suspended, Cancelled)     | M               | tstr                |

#### 2.2.4 DUNSIndustryClassification Object Attributes

| **Data Identifier**                        | **Semantic Reference** | **Definition**                                                                              | **Optionality** | **Encoding format**  |
|--------------------------------------------|------------------------|---------------------------------------------------------------------------------------------|-----------------|----------------------|
| industry_classification                    | --                     | Object providing the NAICS-based industry classification of the entity                      | M               | Object               |
| industry_classification.primary_naics      | --                     | The primary NAICS code representing the entity's main business activity                     | M               | tstr                 |
| industry_classification.secondary_naics    | --                     | Additional NAICS codes representing secondary business activities; MAY be empty             | O               | Array of tstr (0-n)  |
| industry_classification.naics_version      | --                     | The version of the NAICS standard used (e.g., "2022", "2017")                              | M               | tstr                 |

### 2.3 Optional attributes

| **Data Identifier**                        | **Semantic Reference** | **Definition**                                                                                                         | **Optionality** | **Encoding format** |
|--------------------------------------------|------------------------|------------------------------------------------------------------------------------------------------------------------|-----------------|---------------------|
| legal_entity.registered_address.street     | --                     | Street name of the registered address. MAY be omitted if not available.                                               | O               | tstr                |
| legal_entity.registered_address.nr         | --                     | Street or building number. MAY be omitted if not available.                                                           | O               | tstr                |
| legal_entity.registered_address.postal_code| --                     | Postal or ZIP code. MAY be omitted if not available.                                                                  | O               | tstr                |
| legal_entity.registered_address.city       | --                     | City or municipality. MAY be omitted if not available.                                                                | O               | tstr                |
| legal_entity.registered_address.country    | --                     | Country of the registered address (ISO 3166-1 alpha-2). MAY be omitted if not available.                             | O               | tstr                |
| industry_classification.secondary_naics    | --                     | Array of secondary NAICS codes representing additional business activities. MAY contain zero or more values.           | O               | Array of tstr       |

### 2.4 Conditional attributes

No conditional attributes are defined for this attestation type. All attributes are either
mandatory or optional as specified above. When the `registered_address` object is present,
it MAY contain any combination of its optional sub-fields.

### 2.5 Mandatory metadata

| **Data Identifier**        | **Definition**                                                                                                                                                       | **Data type** |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| issuance_date              | The date and time when the attestation was issued (ISO 8601)                                                                                                         | DateTime      |
| expiry_date                | The date and time when the attestation expires (ISO 8601)                                                                                                            | DateTime      |
| issuing_entity             | The identifier of the legal entity that issued the attestation (typically the subject entity itself for self-issued EAA, or the QTSP identifier for QEAA)            | String        |
| attestation_legal_category | Indicates the legal category of this attestation ("EAA" or "QEAA")                                                                                                  | String        |
| vct                        | A URI or other collision-resistant identifier that defines the type of the SD-JWT Verifiable Credential                                                              | String        |

### 2.6 Optional metadata

| **Data Identifier** | **Definition**                                                             | **Data type** |
|---------------------|----------------------------------------------------------------------------|---------------|
| trust_anchor_url    | URL where the trust anchor for verifying this attestation can be retrieved | URI           |
| schema_version      | Version of the schema used                                                 | String        |

### 2.7 Conditional metadata

No conditional metadata elements are defined for this attestation type.

### 2.8 Value Lists

#### 2.8.1 Operational Status Values

The `operational_status` attribute SHOULD use one of the following standardized values:

| **Value**   | **Definition**                                                              |
|-------------|-----------------------------------------------------------------------------|
| Active      | The entity is currently operating and in good standing                      |
| Inactive    | The entity is registered but not currently operating                        |
| Dissolved   | The entity has been formally dissolved and no longer exists as a legal entity|
| Suspended   | The entity's operations have been temporarily suspended                     |
| Bankrupt    | The entity has filed for or been declared bankrupt                          |

#### 2.8.2 Registration Status Values

The `registration.registration_status` attribute SHOULD use one of the following values:

| **Value**   | **Definition**                                                              |
|-------------|-----------------------------------------------------------------------------|
| Active      | The registration record is current and valid                                |
| Suspended   | The registration has been temporarily suspended by the competent authority  |
| Cancelled   | The registration has been permanently cancelled                             |
| Pending     | The registration is awaiting confirmation or completion                     |

#### 2.8.3 NAICS Version Values

The `industry_classification.naics_version` attribute SHOULD use one of the following values:

| **Value** | **Definition**                                      |
|-----------|-----------------------------------------------------|
| 2022      | NAICS 2022 — most recent revision                   |
| 2017      | NAICS 2017                                          |
| 2012      | NAICS 2012                                          |

#### 2.8.4 Country Codes

The `legal_entity.registered_address.country` attribute SHALL use country codes as defined
by **ISO 3166-1 alpha-2** (e.g., `DE` for Germany, `FR` for France, `US` for United States).

### 2.9 Integrity Rules

The following integrity rules SHALL be enforced:

- `duns_number` SHALL be a non-empty nine-digit numeric string uniquely identifying the
  entity within the Dun & Bradstreet system.
- `legal_entity.legal_name` SHALL be a non-empty string.
- `legal_entity.legal_form` SHALL be a non-empty string.
- `legal_entity.registered_address.country`, if provided, SHALL conform to
  **ISO 3166-1 alpha-2** (two-letter country code).
- `operational_status` SHALL be a non-empty string.
- `operational_status_date` SHALL conform to **ISO 8601** date format (YYYY-MM-DD).
- `date_of_incorporation` SHALL conform to **ISO 8601** date format (YYYY-MM-DD).
- `registration.jurisdiction` SHALL be a non-empty string.
- `registration.initial_registration_date` SHALL conform to **ISO 8601** date format
  (YYYY-MM-DD).
- `registration.last_update_date` SHALL conform to **ISO 8601** date format (YYYY-MM-DD).
- `registration.last_update_date` SHALL be equal to or later than
  `registration.initial_registration_date`.
- `registration.registration_status` SHALL be a non-empty string.
- `industry_classification.primary_naics` SHALL be a non-empty string containing a valid
  NAICS code.
- `industry_classification.secondary_naics` MAY contain zero or more NAICS code strings.
- `industry_classification.naics_version` SHALL be a non-empty string identifying the
  applicable NAICS edition.
- Each attribute SHALL appear at most once in the attestation.
- The attestation SHALL be issued by an authorized issuer acting on behalf of, or with
  the consent of, the legal entity identified by the `duns_number`.

---

## 3 Attestation encoding

### 3.1 ISO/IEC 18013-5-compliant encoding

ISO/IEC 18013-5 (also called mdoc) is out of scope for this Rulebook, as offline proximity
presentation is not a current requirement for the DUNS Legal Entity attestation.

### 3.2 SD-JWT VC-based encoding

The DUNS Legal Entity attestation uses the SD-JWT VC format to allow for selective disclosure
of company attributes.

**Selective Disclosure:** All top-level claims (`duns_number`, `legal_entity`,
`operational_status`, `operational_status_date`, `date_of_incorporation`, `registration`,
`industry_classification`) SHALL be individually selectively disclosable, enabling a legal
entity to disclose only the attributes requested by a Relying Party.

The `.` notation is used to indicate the nesting of attributes.

**Verifiable Credential Type (`vct`):** `vct: eu.we-build:duns:1`

#### 3.2.1 Attribute Encoding Table

| **Data Identifier**                         | **Attribute Identifier**                              | **Encoding format**          | **Reference/Notes**                                                                          | **Disclosable** |
|---------------------------------------------|-------------------------------------------------------|------------------------------|----------------------------------------------------------------------------------------------|-----------------|
| duns_number                                 | `duns_number`                                         | String                       | Nine-digit DUNS identifier; SHALL be non-empty                                               | MUST            |
| **DUNSLegalEntity**                         | `legal_entity`                                        | Object                       | Object encapsulating the legal identity of the entity                                        | MUST            |
| legal_entity.legal_name                     | `legal_entity.legal_name`                             | String                       | Registered legal name of the entity                                                          | MUST            |
| legal_entity.legal_form                     | `legal_entity.legal_form`                             | String                       | Legal form of the entity (e.g., GmbH, AG, Ltd.)                                             | MUST            |
| legal_entity.registered_address             | `legal_entity.registered_address`                     | Object                       | Official registered address of the entity                                                    | MUST            |
| legal_entity.registered_address.street      | `legal_entity.registered_address.street`              | String                       | Street name; optional                                                                        | MUST            |
| legal_entity.registered_address.nr          | `legal_entity.registered_address.nr`                  | String                       | Street or building number; optional                                                          | MUST            |
| legal_entity.registered_address.postal_code | `legal_entity.registered_address.postal_code`         | String                       | Postal or ZIP code; optional                                                                 | MUST            |
| legal_entity.registered_address.city        | `legal_entity.registered_address.city`                | String                       | City or municipality; optional                                                               | MUST            |
| legal_entity.registered_address.country     | `legal_entity.registered_address.country`             | String (ISO 3166-1 alpha-2)  | Country of registered address; optional                                                      | MUST            |
| operational_status                          | `operational_status`                                  | String                       | Current operational status (e.g., Active, Inactive, Dissolved)                              | MUST            |
| operational_status_date                     | `operational_status_date`                             | String (ISO 8601 YYYY-MM-DD) | Date on which the operational status was last confirmed or changed                           | MUST            |
| date_of_incorporation                       | `date_of_incorporation`                               | String (ISO 8601 YYYY-MM-DD) | Date on which the legal entity was incorporated or formally established                      | MUST            |
| **DUNSRegistration**                        | `registration`                                        | Object                       | Object providing details about the entity's formal registration                              | MUST            |
| registration.jurisdiction                   | `registration.jurisdiction`                           | String                       | Jurisdiction in which the entity is registered                                               | MUST            |
| registration.initial_registration_date      | `registration.initial_registration_date`              | String (ISO 8601 YYYY-MM-DD) | Date the entity was first registered                                                         | MUST            |
| registration.last_update_date               | `registration.last_update_date`                       | String (ISO 8601 YYYY-MM-DD) | Date the registration record was last updated                                                | MUST            |
| registration.registration_status           | `registration.registration_status`                    | String                       | Current status of the registration record (e.g., Active, Suspended, Cancelled)              | MUST            |
| **DUNSIndustryClassification**              | `industry_classification`                             | Object                       | Object providing the NAICS-based industry classification of the entity                       | MUST            |
| industry_classification.primary_naics       | `industry_classification.primary_naics`               | String                       | Primary NAICS code for the entity's main business activity                                   | MUST            |
| industry_classification.secondary_naics     | `industry_classification.secondary_naics`             | Array of Strings             | Zero or more additional NAICS codes for secondary business activities; optional              | MUST            |
| industry_classification.naics_version       | `industry_classification.naics_version`               | String                       | Version of the NAICS standard used (e.g., "2022")                                           | MUST            |
| **Metadata**                                |                                                       |                              |                                                                                              |                 |
| attestation_legal_category                  | `attestation_legal_category`                          | String                       | One of `EAA` or `QEAA` as defined by eIDAS 2                                                | MUST NOT        |

**Notes:**

- **MUST**: The claim SHALL be selectively disclosable — the holder MAY choose to disclose or
  withhold this claim when presenting the credential to a Relying Party.
- **MUST NOT**: The claim SHALL NOT be selectively disclosable — it is always present in plain
  text in the JWT header/payload and cannot be withheld by the holder, as it is required for
  credential verification and trust establishment.
- `iat`, `exp`, and `iss` follow RFC 7519 standard JWT claim naming conventions.
- Individual address sub-fields within `registered_address` are independently selectively
  disclosable to allow partial disclosure of location information.

#### 3.2.2 Status Claim

For SD-JWT VC-compliant DUNS Legal Entity attestations, the attestation MUST include a
`status` claim if the technical validity period is greater than 24 hours. This claim enables
Relying Parties to determine if a credential has been revoked via a status list mechanism,
as specified in SD-JWT VC.

The `status` claim SHALL be a JSON object with the following members:

- `type` (string): SHALL be `"status-list"`.
- `status_list_credential` (string, URI): The URI of the Status List Credential document
  that contains the status bitstring.
- `status_list_index` (integer, >= 0): The zero-based index into the status list bitstring
  that corresponds to this credential.
- `status_purpose` (string): SHALL be `"revocation"` for this attestation.

Example:

```json
{
  "status": {
 "type": "status-list",
 "status_list_credential": "https://issuer.example.com/status/duns/2025",
 "status_list_index": 456,
 "status_purpose": "revocation"
  }
}
```

### 3.2.3 Example Payload

The following is a non-normative example of a CompanyInfo SD-JWT VC payload:
```
{
  "vct": "eu.we-build:duns:1",
  "iss": "https://issuer.example.com",
  "iat": 1736935200,
  "exp": 1768471200,
  "issuing_entity": "did:example:duns-issuer-001",
  "issuing_country": "DE",
  "attestation_legal_category": "EAA",
  "schema_version": "1.0",
  "trust_anchor_url": "https://trust.webuildconsortium.eu/anchors/eidas-tl",
  "duns_number": "123456789",
  "legal_entity": {
 "legal_name": "Example GmbH",
 "legal_form": "GmbH",
 "registered_address": {
   "street": "Musterstraße",
   "nr": "42",
   "postal_code": "70174",
   "city": "Stuttgart",
   "country": "DE"
 }
  },
  "operational_status": "Active",
  "operational_status_date": "2025-01-01",
  "date_of_incorporation": "2005-03-15",
  "registration": {
 "jurisdiction": "DE",
 "initial_registration_date": "2005-03-15",
 "last_update_date": "2024-12-01",
 "registration_status": "Active"
  },
  "industry_classification": {
 "primary_naics": "541512",
 "secondary_naics": ["541511", "541519"],
 "naics_version": "2022"
  },
  "status": {
 "type": "status-list",
 "status_list_credential": "https://issuer.example.com/status/duns/2025",
 "status_list_index": 456,
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

Sample payloads are provided under ../data-schemas/sd-jwt/sample-data/duns-sd-jwt-sample.json

### 3.3 W3C Verifiable Credentials Data Model-based encoding

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