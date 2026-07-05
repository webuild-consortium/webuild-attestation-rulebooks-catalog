# Attestation Rulebook for attestations of type AuthorisedSignatories Attestation

* **Author(s):**
  * [Ricky Lamberty, Robert Bosch GmbH]
  * [Florin Coptil, Robert Bosch GmbH]
  * [Stephan-A Fuchs, Deutsche Bank] 

* **Previous Authors:**

* **Reviewer(s):**
  * [....., CommerzBank]
  * [Dominic Hurni, SBB]
  * [Werner Folkendt, Robert Bosch GmbH]

| Version | Date       | Description                                                     |
|---------|------------|-----------------------------------------------------------------|
| 0.1     | 15.05.2026 | Initial draft based on the WeBuild design attestations meetings |
| 0.6     | 23.06.2026 | Review holder and bank perspective                              |
| 0.8     | 29.06.2026 | Review supplier perspective                                     |

* **Contact:**
  * [Florin Coptil](mailto:florin.coptil@bosch.com)

* **Feedback:**

## 1 Introduction

This attestation addresses the following question:

**Who is authorised to act or sign on behalf of this legal entity?**

An AuthorisedSignatories Attestation is defined as any natural person who is authorised to act
on behalf of a legal entity in financial and contractual settings with third parties. It serves
as a digital, verifiable list and consists of natural persons having representation powers.

The authority to act on behalf of a legal entity can be derived from two primary sources:
- **Statutory Power:** Authority based on a direct entry in a national public register
  (e.g., a Commercial Register).
- **Delegated Power:** Authority granted via a separate Power of Attorney (PoA) Attestation,
  which was issued by the company which issued the AuthorisedSignatories Attestation.

The AuthorisedSignatories Attestation enables a Relying Party (banks or fintechs) to confidently
confirm that a person (the Signatory) has the authority to make binding commitments
(i.e. signing a contract). This attestation is mandatory, for example, when opening a bank
account. Other use cases may require the same type of attestation.

### 1.1 Document Scope and Purpose

The AuthorisedSignatories Attestation records all natural persons who are authorised to act on
behalf of a legal entity, providing comprehensive transparency on signatory rights and
representation powers. This attestation is a critical component of both Know Your Customer (KYC)
and Know Your Supplier (KYS) processes within the EUDI Wallet ecosystem, supporting effective
risk management, regulatory compliance, and anti-money laundering (AML) obligations.

**Important distinctions:**
- An Authorised Signatory does not need to be a registered Legal Representative.
- An Authorised Signatory does not need to meet any ownership or control threshold.
- A single person **MAY** hold both statutory and delegated authority simultaneously.

> **Note:** This attestation is not a replacement for the Power of Attorney (PoA) Attestation.

**Design Decisions**

This AuthorisedSignatories Attestation Rulebook is based on:
- EU Company Certificate (EUCC) framework as the foundational legal identity layer
- Draft RTS on Customer Due Diligence under Article 28(1) of Regulation (EU) 2024/1624
- eIDAS 2.0 / EUDI Wallet framework for digital identity and verifiable attestations
- ISO 8601 for date formatting

### 1.2 Document Structure
This Rulebook is structured as follows:

- Chapter 2 describes the Contact Person attestation attributes and metadata in an encoding-independent manner, including the data model.
- Chapter 3 specifies how the attestation attributes and metadata are encoded: Section 3.2  covers SD-JWT VC-based encoding.
- Chapter 4 specifies attestation usage scenarios, Relying Party obligations, and integration  with supplier onboarding and KYS workflows.
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

---

### 1.4 Terminology

*Additional terminology specific to this attestation:*

| Term                | Description                                                                                                                                                                    |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AuthorisedSignatories | AuthorisedSignatories Attestation — the attestation type defined in this Rulebook, providing a verifiable list of natural persons authorised to act on behalf of a legal entity |
| Authorised Signatory  | A natural person who is authorised to act on behalf of a legal entity in financial and contractual settings, either through statutory power or delegated power                  |
| Statutory Power       | Authority to act on behalf of a legal entity based on a direct entry in a national public register (e.g., Commercial Register)                                                  |
| Delegated Power       | Authority to act on behalf of a legal entity granted via a Power of Attorney (PoA) issued by the legal entity                                                                   |
| PoA                   | Power of Attorney — a separate attestation granting delegated authority to act on behalf of a legal entity                                                                      |
| EUCC                  | EU Company Certificate — attestation establishing the legal existence and identity of a legal entity within the EU                                                              |
| EUID                  | European Unique Identifier — the unique identifier assigned to legal entities registered within the EU                                                                          |
| KYC                   | Know Your Customer — due diligence process for verifying customer identity and assessing risk in financial relationships                                                        |
| KYS                   | Know Your Supplier — due diligence process for verifying supplier credentials, integrity, and risk exposure                                                                     |
| Relying Party         | A bank, fintech, or other entity that relies on the AuthorisedSignatories Attestation to verify the authority of a signatory                                                    |
| Representation Type   | The nature of the power of representation — either SOLE (one signatory sufficient) or JOINT (multiple signatories required)                                                     |
| ISO 8601              | International standard for date and time representations (e.g., YYYY-MM-DD)                                                                                                    |

---

## 2 Attestation Attributes and Metadata

The AuthorisedSignatories Attestation is designed to provide a standardized, verifiable
representation of all natural persons authorised to act on behalf of a legal entity. It enables
Relying Parties to comprehensively verify signatory authority in financial and contractual
settings, supporting effective KYC/KYS processes and regulatory compliance.

### 2.1 Introduction

**Data Model:**

The AuthorisedSignatories Attestation is structured into a root object containing two distinct
sub-objects:

```
AuthorisedSignatories Attestation
├── Legal_Entity [1]
│   ├─ Legal_Person    (legal_person_name (M), legal_form_type (M))                                             — mandatory
│   ├─ identifier [1..n] (M)                    // At least one identifier required
│   │   ├─ euid (str) (O)                       // European Unique Identifier
│   │   ├─ lei (str) (O)                        // Legal Entity Identifier per ISO 17442
│   │   ├─ tax (str) (O)                        // National tax or registration number                                                         — mandatory
└── Authorised_Person [1..n]
    ├─ NaturalPerson          (first_name (M), surname (M), date_of_birth (M))                                  — mandatory
    ├─ BirthPlace             (locality (M), country (M), region (O))                                           — mandatory
    ├─ Citizenship            (citizenship(s) [1..n])                                                           — mandatory
    ├─ PersonRole             (role (O), representation_type (M))                                               — mandatory
    └─ NaturalPersonIdentifier (document_type (M), document_number (M), issuing_country (M), expiry_date (M))  — optional
```
**Explanation:**

The `Legal_Entity` object **SHALL** appear exactly once and contains:
- `Legal_Person` — the official legal name and legal form of the entity issuing the attestation.
- `Identifier` — the EUID (mandatory) and optionally LEI and/or tax registration number.

The `Authorised_Person` object **SHALL** appear at least once and **MAY** be repeated for each
authorised signatory. Each instance contains:
- `NaturalPerson` — the full legal name and date of birth of the signatory.
- `BirthPlace` — the place of birth including at minimum locality and country.
- `Citizenship` — one or more citizenships held by the signatory.
- `PersonRole` — the role within the company (optional) and the representation type (mandatory).
- `NaturalPersonIdentifier` — optional identity document details for enhanced identification.

**Attestation Classification:**

This attestation type **MAY** be classified as:
- **"EAA"** when self-issued by the legal entity subject to the disclosure.

| **Data Identifier** | **Semantic Reference** | **Definition**                                                        | **Data type**                         |
|---------------------|------------------------|-----------------------------------------------------------------------|---------------------------------------|
| legal_person        | ...                    | Information about the legal person                                    | Object                                |
| legal_identifier    | ...                    | Information about the legal person identifier                         | Object                                |
| natural_person      | ...                    | Information about the natural person                                  | Object                                |
| birth_place         | ...                    | Information about the birth place                                     | Object                                |
| citizenship         | ...                    | Citizenship(s) held by the person (one or more nationalities)         | Array of Strings (ISO 3166-1 alpha-3) |
| person_role         | ...                    | Information about the natural person role                             | Object                                |
| residence_address   | ...                    | Information about the residential address of the person               | Object                                |
| identification      | ...                    | Information about the identification of the person                    | Object                                |

---

### 2.2 Mandatory Attributes

**LegalPerson Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                                             | **Data type** |
|---------------------|------------------------|----------------------------------------------------------------------------|---------------|
| legal_person_name   | —                      | The complete official legal name of the legal entity                       | String        |
| legal_form_type     | —                      | The legal form of the legal entity (e.g., SA, GmbH, Ltd, BV)              | String        |
| euid                | —                      | The European Unique Identifier of the company per Directive (EU) 2017/1132 | String        |

**NaturalPerson Attributes**

This object is defined for each person represented in the AuthorisedSignatories Attestation.

| **Data Identifier** | **Semantic Reference** | **Definition**                                                       | **Data type**     |
|---------------------|------------------------|----------------------------------------------------------------------|-------------------|
| first_name          | ...                    | The first names in full (including all given names and middle names) | String            |
| surname             | ...                    | The surnames in full (all family names/last names)                   | String            |
| date_of_birth       | ...                    | Day, month, and year of birth of the person per ISO 8601             | Date (YYYY-MM-DD) |

**BirthPlace Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                            | **Data type**               |
|---------------------|------------------------|-----------------------------------------------------------|-----------------------------|
| locality            | ...                    | Locality (city or town) where the natural person was born | String                      |
| country             | ...                    | Country where the natural person was born                 | String (ISO 3166-1 alpha-3) |

**Citizenship Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                                          | **Data type**                         |
|---------------------|------------------------|-------------------------------------------------------------------------|---------------------------------------|
| citizenship         | ...                    | The nationality or nationalities of the authorised person (one or more) | Array of Strings (ISO 3166-1 alpha-3) |

**PersonRole Attributes**

| **Data Identifier**   | **Semantic Reference** | **Definition**                                                                                      | **Data type**                  |
|-----------------------|------------------------|-----------------------------------------------------------------------------------------------------|--------------------------------|
| representation_type   | ...                    | The nature of the power of representation. SHALL be one of the values defined in Section 2.8.1      | String ("SOLE" or "JOINT")     |

---

### 2.3 Optional Attributes

**LegalPersonIdentifier Optional Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                              | **Data type**          |
|---------------------|------------------------|---------------------------------------------|------------------------|
| lei                 | —                      | Legal Entity Identifier (LEI) per ISO 17442 | String (20 characters) |
| tax                 | —                      | National company tax or registration number | String                 |

**BirthPlace Optional Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                             | **Data type** |
|---------------------|------------------------|------------------------------------------------------------|---------------|
| region              | ...                    | Optional additional detail on the region or state of birth | String        |

**PersonRole Optional Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                                                  | **Data type** |
|---------------------|------------------------|---------------------------------------------------------------------------------|---------------|
| role                | ...                    | The role of the authorised person within the company (e.g., CEO, CFO, Director) | String        |

**ResidenceAddress Optional Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                                      | **Data type** |
|---------------------|------------------------|---------------------------------------------------------------------|---------------|
| address             | —                      | The street address where the authorised person currently resides    | String        |
| locality            | —                      | The city where the authorised person currently resides              | String        |
| postal_code         | —                      | The postal or ZIP code of the authorised person's address           | String        |
| region              | —                      | The state, province, or region of the authorised person's address   | String        |
| country             | —                      | ISO 3166-1 alpha-3 country code where the authorised person resides | String        |

**NaturalPersonIdentifier Optional Attributes**

When present, all four fields within this object **SHALL** be provided together.

| **Data Identifier**    | **Semantic Reference** | **Definition**                                                                                | **Data type**     |
|------------------------|------------------------|-----------------------------------------------------------------------------------------------|-------------------|
| document_type          | ...                    | A value defining the type of the identity document (e.g., Passport, National identity card)   | String            |
| document_number        | ...                    | The number of the identity document (passport number, national ID number, etc.)               | String            |
| issuing_country        | ...                    | The country that issued the identity document (ISO 3166-1 alpha-3 code)                       | String            |
| document_expiry_date   | ...                    | The expiration date of the identity document per ISO 8601                                     | Date (YYYY-MM-DD) |

---

### 2.4 Conditional Attributes

No conditional attributes are defined for this attestation type. All attributes are either
mandatory or optional as specified above.

---

### 2.5 Mandatory Metadata

| **Data Identifier**          | **Definition**                                                                                                                                                     | **Data type** |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| attestation_legal_category   | Indicates the legal category of the AuthorisedSignatories Attestation ("EAA")                                                                                      | String        |

### 2.6 Optional Metadata

### 2.7 Conditional Metadata

### 2.8 Value Lists

#### 2.8.1 Representation Type Codes

The `representation_type` attribute **SHALL** use one of the following standardized values:

| **Code** | **Definition**                                                                                                                                          |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| SOLE     | A single signatory has full authority to act and sign on behalf of the legal entity independently, without requiring the co-signature of any other person |
| JOINT    | Two or more signatories are required to act together to make binding commitments on behalf of the legal entity                                           |

> **Note:** The representation type applies in the context of financial relationships
> (e.g., opening a bank account, currency account, credit line, etc.).

#### 2.8.2 Type of Identity Document Codes

The `document_type` attribute, when present, **SHALL** use one of the following standardized values:

| **Code**                         | **Definition**                                                                   |
|----------------------------------|----------------------------------------------------------------------------------|
| Passport                         | International travel document issued by a national government                    |
| National identity card           | National identity card issued by the authorised person's country of nationality  |
| Driver's license                 | Driver's license used as an identity document where accepted by the jurisdiction |
| Residence permit                 | Residence permit or similar document issued by the country of residence          |
| Other official identity document | Other government-issued identity document accepted for identity verification     |

---

### 2.9 Integrity Rules

The following integrity rules **SHALL** be enforced:

- The `Authorised_Person` array **SHALL** contain at least one entry in the AuthorisedSignatories Attestation.
- Each `Authorised_Person` entry **SHALL** contain `first_name`, `surname`, `date_of_birth`, `citizenship`, `birth_place_locality`, `birth_place_country`, and `representation_type`.
- `Legal_Entity` **SHALL** appear exactly once and **SHALL** contain `legal_person_name`, `legal_form_type`, and `euid`.
- `date_of_birth` **SHALL** be a valid ISO 8601 date (YYYY-MM-DD).
- `citizenship` **SHALL** be an array of one or more valid ISO 3166-1 alpha-3 country codes.
- `birth_place_country` **SHALL** be a valid ISO 3166-1 alpha-3 country code.
- `representation_type` **SHALL** be one of the values defined in Section 2.8.1 (`"SOLE"` or `"JOINT"`).
- `document_type`, when present, **SHALL** be one of the values defined in Section 2.8.2.
- `document_expiry_date`, when present, **SHALL** be a valid ISO 8601 date (YYYY-MM-DD).
- If any `NaturalPersonIdentifier` attribute is present, all four fields (`document_type`, `document_number`, `issuing_country`, `document_expiry_date`) **SHALL** be present together.
- `euid` **SHALL** be a non-empty string conforming to the format defined in Directive (EU) 2017/1132.
- `lei`, when present, **SHALL** be a 20-character string conforming to ISO 17442.
- `issuance_date` and `expiry_date` **SHALL** be valid ISO 8601 DateTimes.
- `expiry_date` **SHALL** be later than `issuance_date`.
- `issuance_date` **SHALL** be in the past.
- `attestation_legal_category` **SHALL** be `"EAA"`.
- If `trust_anchor_url` is present, it **SHALL** be a valid URI.
- If `schema_version` is present, it **SHALL** be a non-empty string.
- Each attribute **SHALL** appear at most once within its scope (e.g., within a `Legal_Entity` or `Authorised_Person` object).
- If the technical validity period (expiry_date − issuance_date) exceeds 24 hours, the status claim SHALL be present, conforming to the structure defined in Section 3.2.2.

---

## 3 Attestation Encoding

### 3.1 ISO/IEC 18013-5-Compliant Encoding

ISO/IEC 18013-5 (also called mdoc) is out of scope for this Rulebook, as offline proximity
presentation is not a current requirement for the AuthorisedSignatories Attestation.

### 3.2 SD-JWT VC-Based Encoding

The AuthorisedSignatories Attestation uses the SD-JWT VC format to allow for selective
disclosure of signatory attributes.

**Selective Disclosure:** Top-level claims (e.g., `legal_entity`, `authorised_persons`) **SHALL**
be individually selectively disclosable, enabling a legal entity to disclose only the attributes
requested by a Relying Party. Attributes nested within an `Authorised_Person` object (e.g.,
`first_name`, `date_of_birth`, `representation_type`) **MAY** be individually selectively
disclosable as per the attribute encoding table below.

The `.` notation is used to indicate the nesting of attributes.

**Verifiable Credential Type (`vct`):** `vct: eu.we-build:authorisedsignatories:1`

#### 3.2.1 Attribute Encoding Table

| **Data Identifier**               | **Attribute Identifier**                                | **Encoding Format** | **Reference/Notes**                                                                                               | **Disclosable** |
|-----------------------------------|---------------------------------------------------------|---------------------|-------------------------------------------------------------------------------------------------------------------|-----------------|
| **Legal Entity**                  |                                                         |                     |                                                                                                                   |                 |
| legal_person_name                 | legal_entity.legal_person.legal_person_name             | string              | The complete official legal name of the company                                                                   | MUST            |
| legal_form_type                   | legal_entity.legal_person.legal_form_type               | string              | Legal form of the company (e.g., GmbH, S.A., Ltd.)                                                                | MUST            |
| euid                              | legal_entity.identifier.euid                            | string              | EUID per Directive (EU) 2017/1132; mandatory                                                                      | MUST            |
| lei                               | legal_entity.identifier.lei                             | string              | LEI per ISO 17442; optional                                                                                       | MUST            |
| tax                               | legal_entity.identifier.tax                             | string              | National tax or registration number; optional                                                                     | MUST            |
| **Authorised Person**             |                                                         |                     |                                                                                                                   |                 |
| authorised_persons                | authorised_persons                                      | array               | Array of authorised person objects in the AuthorisedSignatories Attestation; SHALL contain at least one entry     | MUST            |
| **NaturalPerson**                 |                                                         |                     |                                                                                                                   |                 |
| first_name                        | authorised_persons[n].natural_person.first_name         | string              | Full first name(s) of the authorised person per Art. 2 RTS                                                        | MUST            |
| surname                           | authorised_persons[n].natural_person.surname            | string              | Full surname(s) of the authorised person per Art. 2 RTS                                                           | MUST            |
| date_of_birth                     | authorised_persons[n].natural_person.date_of_birth      | string              | Date of birth of the authorised person; ISO 8601 full-date format (YYYY-MM-DD)                                    | MUST            |
| **BirthPlace**                    |                                                         |                     |                                                                                                                   |                 |
| birth_place.locality              | authorised_persons[n].birth_place.locality              | string              | Locality (city or town) where the authorised person was born                                                      | MUST            |
| birth_place.country               | authorised_persons[n].birth_place.country               | string              | Country where the authorised person was born, per Art. 4 RTS; ISO 3166-1 alpha-3                                  | MUST            |
| birth_place.region                | authorised_persons[n].birth_place.region                | string              | Optional region or state of birth                                                                                 | MAY             |
| **Citizenship**                   |                                                         |                     |                                                                                                                   |                 |
| citizenship                       | authorised_persons[n].citizenship                       | array               | Nationality or nationalities of the authorised person; ISO 3166-1 alpha-3 codes                                   | MUST            |
| **PersonRole**                    |                                                         |                     |                                                                                                                   |                 |
| person_role.representation_type   | authorised_persons[n].person_role.representation_type   | string              | The nature of the power of representation; SHALL use codes from Section 2.8.1 ("SOLE" or "JOINT")                 | MUST            |
| person_role.role                  | authorised_persons[n].person_role.role                  | string              | The role of the authorised person within the company (e.g., CEO, CFO); optional                                   | MUST            |
| **NaturalPersonIdentifier**       |                                                         |                     |                                                                                                                   |                 |
| identifier.document_type          | authorised_persons[n].identifier.document_type          | string              | Type of identity document; SHALL use codes from Section 2.8.2; optional                                           | MAY             |
| identifier.document_number        | authorised_persons[n].identifier.document_number        | string              | The number of the identity document; optional                                                                     | MAY             |
| identifier.issuing_country        | authorised_persons[n].identifier.issuing_country        | string              | Country that issued the identity document; ISO 3166-1 alpha-3; optional                                           | MAY             |
| identifier.document_expiry_date   | authorised_persons[n].identifier.document_expiry_date   | string              | Expiration date of the identity document; ISO 8601 full-date format (YYYY-MM-DD); optional                        | MAY             |
| **Metadata**                      |                                                         |                     |                                                                                                                   |                 |
| attestation_legal_category        | attestation_legal_category                              | string              | One of "EAA" as defined by eIDAS 2                                                                                | MUST NOT        |

**Notes:**

- **MUST**: The claim **SHALL** be selectively disclosable — the holder **MAY** choose to
  disclose or withhold this claim when presenting the credential to a Relying Party.
- **MAY**: The claim **MAY** be selectively disclosable if the issuer supports it; the holder
  can choose to disclose or withhold.
- **MUST NOT**: The claim **SHALL NOT** be selectively disclosable — it is always present in
  plain text in the JWT header/payload and cannot be withheld by the holder, as it is required
  for credential verification and trust establishment.
- `iat`, `exp`, and `iss` follow RFC 7519 standard JWT claim naming conventions.
- The `NaturalPersonIdentifier` group of attributes is marked as `MAY` disclosable as a unit
  — if any attribute within the group is disclosed, all four **SHALL** be disclosed together.

#### 3.2.2 Status Claim

For SD-JWT VC-compliant AuthorisedSignatories Attestations, the attestation **MUST** include
a `status` claim if the technical validity period is greater than 24 hours. This claim enables
Relying Parties to determine if a credential has been revoked via a status list mechanism,
as specified in SD-JWT VC.

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
    "status_list_credential": "https://issuer.example.com/status/authorisedsignatories/2025",
    "status_list_index": 789,
    "status_purpose": "revocation"
  }
}
```

### 3.2.3 Example Payload
The following is a non-normative example of an AuthorisedSignatories Attestation SD-JWT VC payload:

```

{
  "vct": "eu.we-build:authorisedsignatories:1",
  "attestation_legal_category": "EAA",
  "iss": "https://example-gmbh.de",
  "iat": 1746000000,
  "exp": 1777536000,
  "jti": "asr-attestation-20260515-001",
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
  "authorised_persons": [
    {
      "natural_person": {
        "first_name": "Maria Anna",
        "surname": "Müller",
        "date_of_birth": "1982-07-14"
      },
      "birth_place": {
        "locality": "Munich",
        "country": "DEU",
        "region": "Bavaria"
      },
      "citizenship": ["DEU"],
      "person_role": {
        "representation_type": "SOLE",
        "role": "CEO"
      },
      "identifier": {
        "document_type": "Passport",
        "document_number": "C01X00T47",
        "issuing_country": "DEU",
        "document_expiry_date": "2031-03-20"
      }
    },
    {
      "natural_person": {
        "first_name": "Jean",
        "surname": "Dupont",
        "date_of_birth": "1975-11-30"
      },
      "birth_place": {
        "locality": "Paris",
        "country": "FRA"
      },
      "citizenship": ["FRA", "BEL"],
      "person_role": {
        "representation_type": "JOINT",
        "role": "CFO"
      }
    }
  ],
  "status": {
    "type": "status-list",
    "status_list_credential": "https://example.com/status/authorisedsignatories-list-1",
    "status_list_index": 789,
    "status_purpose": "revocation"
  },
  "trust_anchor_url": "https://trust.webuildconsortium.eu/anchors/eidas-tl",
  "schema_version": "0.1.0",
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
Sample payloads are provided under ../data-schemas/sd-jwt/sample-data/authorised-signatories-sd-jwt-sample.json

### 3.3 W3C Verifiable Credentials Data Model-based encoding

@TODO — To be discussed: which stakeholders will support this format and which use cases require it.

## 4 Attestation usage
### 4.1. Issuance process ###
To be specified in a future version of this Rulebook.

### 4.2 Relying Party Obligations
When receiving and processing an attestation, the Relying Party SHALL perform the following verification obligations.

### 4.2.1 – 4.2.8 Base Verification Process
The Relying Party SHALL perform the base attestation verification process as defined in the
Base Verification specification:
https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-base/verifier-base-verification.md#42-relying-party-obligations

### 4.2.9 Validate Integrity Rules
Validation of integrity and policy rules will be specified in a future version of this Rulebook.

## 5 Trust anchors
This chapter will be completed in a future version of this Rulebook.

## 6 Revocation
This chapter will be completed in a future version of this Rulebook.

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
