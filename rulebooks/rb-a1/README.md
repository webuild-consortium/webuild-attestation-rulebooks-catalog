# Attestation Rulebook for attestations of type Portable Document A1 (PD A1)

* Author(s):
  * [Philipp Friedl, DRV Bund]
  * Laurent ?
* Previous Authors
*
* Reviewer(s):
  * [Florin Coptil, Robert Bosch GmbH]

| Version | Date       | Description                                                     |
|---------|------------|-----------------------------------------------------------------|
| 0.1     | 01.05.2026 | Initial draft based on the WeBuild design attestations meetings |

* Contact:
  * [Philipp Friedl - DRV Bund](mailto:philipp.friedl@drv-bund.de)

* Feedback:

---

## 1 Introduction

This attestation addresses the following question:

**Which social security legislation applies to a citizen working in a cross-border employment situation within the EU/EFTA area?**

The Portable Document A1 (PD A1) is a certificate that documents the applicable legislation
regarding social security for a citizen in a cross-border employment situation. By determining
that only one legislation applies, it supports the mobility of working citizens while protecting
their rights.

The PD A1 is issued to the citizen by the competent social security institution from the
"sending state" upon request by the employer or the self-employed person. It is used for
verification abroad in the "receiving state" (posted worker scenario).

The **Know Your Employee (KYE)** scenario (Scenario 5) is part of BU1 and will lead to MVP
and MVP+ implementations using both Natural Person Wallets and Legal Person Wallets. The
high-level scenario is:

> *"A company A in a country A would like to send one of their employees to work and provide
> a service to company B in country B."*

This scenario requires the issuance of three main credentials:
- **Employee Credentials**
- **Portable Document (PD) A1**
- **Posted Worker Notification (PWN)**

### 1.1 Document Scope and Purpose

The PD A1 Attestation provides a standardized, verifiable digital representation of the
Portable Document A1 certificate. The main legal basis is:
- **Regulation (EC) No. 883/2004** on the coordination of social security systems
  (especially Articles 11–16)
- **Regulation (EC) No. 987/2009** — implementing regulation
- National legislation regarding social security in EU/EFTA member states

In the "classic" posting situation — where a citizen works abroad for a maximum of 24 months
— the social security institution of the "sending" state issues a PD A1 which states that the
legislation of this "sending" state stays applicable (to ensure coverage and to avoid dual
contributions).

**Design Decisions**

This PD A1 Attestation Rulebook is based on:
- The legally defined content of the Portable Document A1 as issued by competent social
  security institutions
- Regulation (EC) No. 883/2004 and Regulation (EC) No. 987/2009 as the primary legal
  framework
- EESSI (Electronic Exchange of Social Security Information) code tables for employment
  type and institution identifiers
- ISO 3166-1 alpha-2 for country codes (EU/EFTA countries + UK = 32 countries)
- ISO 8601 for date formatting
- SD-JWT VC format with selective disclosure based on logical SD element groups
  (not individual field level)
- eIDAS 2.0 / EUDI Wallet framework for digital identity and verifiable attestations

**Key Design Principles:**
- The credential schema **SHALL** match the legally defined content of the portable document;
  therefore all elements are contained.
- Personal information on the "subject" **SHALL** be kept within the VC to allow use by a
  representative (e.g., employer acting on behalf of employee).
- Selective Disclosure **SHALL NOT** be possible on single-element level, but based on logical
  blocks as defined by SD element groups. For example, it is only possible to disclose a whole
  address block, not just the street without the town.
- As specific Relying Parties may — according to GDPR — not have the right to
  request/receive all data, there **SHOULD** be accreditation-based presentation policy options
  according to the modular SD-element-group design.
- A binding mode indicator (e.g., PID binding, Wallet Instance binding, no binding) **SHALL**
  be included as a technical parameter.

### 1.2 Document Structure

This Rulebook is structured as follows:

- **Chapter 2** describes the PD A1 attestation attributes and metadata in an
  encoding-independent manner, including the data model.
- **Chapter 3** specifies how the attestation attributes and metadata are encoded: Section 3.2
  covers SD-JWT VC-based encoding.
- **Chapter 4** specifies attestation usage scenarios, Relying Party obligations, and integration
  with KYE workflows.
- **Chapter 5** defines trust anchors and verification mechanisms for issuer authorization.
- **Chapter 6** defines revocation mechanisms for the attestation.
- **Chapter 7** provides compliance information regarding the EUDI framework and applicable
  data protection laws.
- **Chapter 8** provides references to applicable standards and specifications.

### 1.3 Keywords

This document uses the capitalised keywords 'SHALL', 'SHOULD' and 'MAY' as specified in
[RFC 2119], i.e. to indicate requirements, recommendations and options specified in this
document.

In addition, 'must' (non-capitalised) is used to indicate an external constraint, i.e. a
requirement that is not mandated by this document, but, for instance, by an external document.
The word 'can' indicates a capability, whereas other words, such as 'will', and 'is' or 'are'
are intended as statements of fact.

### 1.4 Terminology

*Additional terminology specific to this attestation:*

| **Term**               | **Description**                                                                                                                                                                                 |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PD A1                  | Portable Document A1 — a certificate documenting the applicable social security legislation for a citizen in a cross-border employment situation within the EU/EFTA area                         |
| Posted Worker          | A citizen employed in one EU/EFTA member state ("sending state") who is temporarily sent to work in another member state ("receiving state") for a maximum of 24 months                         |
| Sending State          | The EU/EFTA member state whose social security legislation remains applicable to the posted worker during the posting period                                                                      |
| Receiving State        | The EU/EFTA member state where the posted worker temporarily performs work                                                                                                                       |
| Competent Institution  | The national social security institution of the sending state authorized to issue the PD A1 certificate                                                                                          |
| PIN                    | Personal Identification Number — currently mostly the Social Security Number of the citizen                                                                                                             |
| PWN                    | Posted Worker Notification — an administrative requirement for companies providing intra-EU cross-border services with posted workers, filed with the host EU Member State authorities            |
| Employee Credential    | A credential issued by an employer to its employees to certify that they are part of the company at a given point in time                                                                        |
| KYE                    | Know Your Employee — a due diligence scenario (Scenario 5 / BU1) enabling companies to verify employee identity and posting status in cross-border work situations                               |
| EESSI                  | Electronic Exchange of Social Security Information — the EU system for electronic exchange of social security data between member state institutions                                             |
| SD Element Group       | A logical group of attributes that are disclosed together as a unit under Selective Disclosure (SD-JWT); disclosure is at group level, not at individual field level                              |
| EAA                    | Electronic Attestation of Attributes — as defined under eIDAS 2.0                                                                                                                               |
| PuB-EAA                | Electronic Attestation of Attributes issued by or on behalf of a public sector body responsible for an authentic source — as defined under eIDAS 2.0                                            |
| QEAA                   | Qualified Electronic Attestation of Attributes — as defined under eIDAS 2.0                                                                                                                     |
| ISO 3166-1 alpha-2     | International standard defining 2-digit country codes (e.g., DE, FR, IT); used for EU/EFTA countries + UK (32 countries total)                                                                  |
| ISO 8601               | International standard for date and time representations (e.g., YYYY-MM-DD)                                                                                                                    |
| Regulation EC 883/2004 | EU Regulation on the coordination of social security systems; primary legal basis for the PD A1, especially Articles 11–16                                                                       |
| Regulation EC 987/2009 | EU Regulation laying down the procedure for implementing Regulation (EC) No 883/2004                                                                                                            |

---

## 2 Attestation Attributes and Metadata

The PD A1 Attestation is designed to provide a standardized, verifiable digital representation
of the Portable Document A1 certificate. It captures all legally required attributes of the PD A1
in a machine-readable format compliant with the EUDI Wallet framework, while enabling
selective disclosure at the SD element group level as defined in the official credential schema.

### 2.1 Introduction

**Data Model:**

```
PDA1 Credential
├── Subject [1:1] — SD Group 1–6
│ ├── pin (string) — mandatory | SD Group 1
│ ├── gender (string/codelist) — mandatory | SD Group 2
│ ├── family_name (string) — mandatory | SD Group 3
│ ├── forename (string) — mandatory | SD Group 3
│ ├── surname_at_birth (string) — optional | SD Group 3
│ ├── forename_at_birth (string) — optional | SD Group 3
│ ├── date_of_birth (date) — mandatory | SD Group 4
│ ├── nationality (code [1:n]) — mandatory | SD Group 5
│ ├── place_of_birth [1:1] — mandatory | SD Group 6
│ │ ├── town (string) — mandatory | SD Group 6
│ │ └── country_code (code, ISO 3166-1 alpha-2) — mandatory | SD Group 6
│ └── address [1:n] — mandatory | SD Group 7–8
│ ├── address_residence [0:1] — optional | SD Group 7
│ │ ├── street_nr (string) — optional | SD Group 7
│ │ ├── town (string) — mandatory | SD Group 7
│ │ ├── post_code (string) — optional | SD Group 7
│ │ └── country (code, ISO 3166-1 alpha-2) — mandatory | SD Group 7
│ └── address_stay [0:n] — optional | SD Group 8
│ ├── street_nr (string) — optional | SD Group 8
│ ├── town (string) — mandatory | SD Group 8
│ ├── post_code (string) — optional | SD Group 8
│ └── country (code, ISO 3166-1 alpha-2) — mandatory | SD Group 8
├── Member State Legislation [1:1] — Non-SD (always disclosed)
│ ├── member_state (code, ISO 3166-1 alpha-2) — mandatory
│ ├── starting_date (date) — mandatory
│ ├── ending_date (date) — mandatory
│ ├── applies_for_duration (boolean) — optional
│ ├── provisional (boolean) — optional
│ └── transitional_rules (boolean) — optional
├── Employer / Self-Employment Details [1:n] — SD Group 9–10
│ ├── employment_type (code) — mandatory | SD Group 9
│ ├── name (string) — mandatory | SD Group 9
│ ├── employer_id (string) — mandatory | SD Group 9
│ ├── id_type (code) — mandatory | SD Group 9
│ └── address [1:1] — mandatory | SD Group 10
│ ├── street_nr (string) — optional | SD Group 10
│ ├── town (string) — mandatory | SD Group 10
│ ├── post_code (string) — optional | SD Group 10
│ └── country (code, ISO 3166-1 alpha-2) — mandatory | SD Group 10
├── Place(s) of Work [1:n] — SD Group 11–12
│ ├── no_fixed_place [0:1] — optional | SD Group 11
│ │ └── country_code (code, ISO 3166-1 alpha-2) — mandatory | SD Group 11
│ └── place_of_work [0:n] — optional | SD Group 11–12
│ ├── company_name (string) — mandatory | SD Group 11
│ ├── flag_base_home (string) — optional | SD Group 11
│ ├── company_id (string) — optional | SD Group 11
│ ├── id_type (code) — optional | SD Group 11
│ ├── street_nr (string) — optional | SD Group 12
│ ├── town (string) — mandatory | SD Group 12
│ ├── postal_code (string) — optional | SD Group 12
│ └── country (code, ISO 3166-1 alpha-2) — mandatory | SD Group 12
├── Status Confirmation [1:1] — SD Group 13
│ └── status_confirmation (code) — mandatory | SD Group 13
├── Unique Document Number [1:1] — SD Group 14
│ └── document_id (string) — mandatory | SD Group 14
└── Competent Institution [1:1] — SD Group 15–16
├── institution_id (string) — mandatory | SD Group 15
├── institution_name (string) — mandatory | SD Group 15
├── country_code (code, ISO 3166-1 alpha-2) — mandatory | SD Group 15
├── fax (string) — optional | SD Group 16
├── phone (string) — optional | SD Group 16
├── email (string) — optional | SD Group 16
├── street_nr (string) — optional | SD Group 16
├── town (string) — optional | SD Group 16
├── postal_code (string) — optional | SD Group 16
└── country_code (code, ISO 3166-1 alpha-2) — optional | SD Group 16
```


**Explanation:**

- Section **1 (Subject)** contains personal identity attributes of the citizen. All mandatory
  fields **SHALL** be present. At least one address **SHALL** be provided (either residence or
  stay address).
- Section **2 (Member State Legislation)** is **Non-SD** and is always fully disclosed to the
  Relying Party, as it contains the core purpose of the PD A1 certificate.
- Section **3 (Employer/Self-Employment Details)** **SHALL** contain at least one employer
  entry. All blocks **SHALL** be presented as a whole to show a complete picture of the
  employment situation.
- Section **4 (Places of Work)** requires a "country attribute" at the top level. The Verifier
  has the ability to request only their own country (or all). The user can select only on a
  country basis.
- Section **5 (Status Confirmation)** identifies the type of cross-border situation.
- Section **6 (Unique Document Number)** provides the unique identifier of the issued PD A1.
- Section **7 (Competent Institution)** identifies the issuing social security institution.

**Selective Disclosure Design:**

Selective Disclosure is based on **SD element groups** (not individual field level):
- Disclosing a whole logical block (e.g., SD Group 7 = full residence address) is required.
- It is not possible to disclose, for example, only the town from an address block without
  the other address fields.
- Section 2 (Member State Legislation) is **always disclosed** (Non-SD).
- Section 3 (Employer Details) must always be disclosed as a whole set of blocks.

**Attestation Classification:**

This attestation type **MAY** be classified as:
- **"QEAA"** when issued by a competent national social security institution acting as a qualified trust service provider.
- **"PuB-EAA"** when issued by a competent national social security institution which is not a qualified trust service provider (issued by or on behalf of a public sector body responsible for an authentic source)
- **"EAA"** in specific delegation or representation scenarios (or if the national social security institution can't fulfill the requirements of a PuB-EAA issuer - under discussion).

**Top-Level Data Identifiers:**

| **Data Identifier**        | **Semantic Reference** | **Definition**                                                                    | **Data type**          |
|----------------------------|------------------------|-----------------------------------------------------------------------------------|------------------------|
| subject                    | ...                    | Personal identity attributes of the citizen subject to the PD A1                 | Object                 |
| member_state_legislation   | ...                    | Details of the applicable member state legislation; always disclosed (Non-SD)     | Object                 |
| employer_details           | ...                    | Details of the employer(s) or self-employment situation                           | Array [EmployerObject] |
| places_of_work             | ...                    | Places where the posted worker performs work                                      | Array [PlaceOfWork]    |
| status_confirmation        | ...                    | Status confirmation code identifying the type of cross-border situation           | Object                 |
| document_id                | ...                    | Unique number of the issued PD A1 document                                        | Object                 |
| competent_institution      | ...                    | Details of the competent social security institution that issued the PD A1        | Object                 |

### 2.2 Mandatory Attributes

#### Section 1 — Subject Attributes

| **Data Identifier**            | **Semantic Reference** | **Definition**                                                                                          | **Data type**                   | **Occurrence** | **SD Group** |
|--------------------------------|------------------------|---------------------------------------------------------------------------------------------------------|---------------------------------|----------------|--------------|
| pin                            | —                      | Personal Identification Number (currently Social Security Number) of the citizen                        | String                          | 1:1            | 1            |
| gender                         | —                      | Gender of the citizen                                                                                   | String / Codelist (tbd)         | 1:1            | 2            |
| family_name                    | —                      | Family name(s) of the citizen in full                                                                   | String                          | 1:1            | 3            |
| forename                       | —                      | Forename(s) of the citizen in full                                                                      | String                          | 1:1            | 3            |
| date_of_birth                  | —                      | Date of birth of the citizen (ISO 8601)                                                                 | Date (YYYY-MM-DD)               | 1:1            | 4            |
| nationality                    | —                      | Nationality/ies of the citizen; Relying Party always requests all nationalities; user may select which  | Code [1:n] (ISO 3166-1 alpha-2) | 1:n            | 5            |
| place_of_birth.town            | —                      | Town/locality where the citizen was born                                                                | String                          | 1:1            | 6            |
| place_of_birth.country_code    | —                      | Country where the citizen was born (ISO 3166-1 alpha-2)                                                 | Code (ISO 3166-1 alpha-2)       | 1:1            | 6            |

#### Address — Residence (SD Group 7)

At least one address **SHALL** be provided (residence or stay):

| **Data Identifier**                 | **Semantic Reference** | **Definition**                                              | **Data type**             | **Occurrence** | **SD Group** |
|-------------------------------------|------------------------|-------------------------------------------------------------|---------------------------|----------------|--------------|
| address_residence.town              | —                      | Town of the address in the state of residence               | String                    | 1:1            | 7            |
| address_residence.country_code      | —                      | Country code of the state of residence (ISO 3166-1 alpha-2) | Code (ISO 3166-1 alpha-2) | 1:1            | 7            |

#### Address — Stay (SD Group 8)

| **Data Identifier**         | **Semantic Reference** | **Definition**                                          | **Data type**             | **Occurrence** | **SD Group** |
|-----------------------------|------------------------|---------------------------------------------------------|---------------------------|----------------|--------------|
| address_stay.town           | —                      | Town of the address in the state of stay                | String                    | 1:1            | 8            |
| address_stay.country_code   | —                      | Country code of the state of stay (ISO 3166-1 alpha-2)  | Code (ISO 3166-1 alpha-2) | 1:1            | 8            |

#### Section 2 — Member State Legislation Attributes (Non-SD, always disclosed)

| **Data Identifier**                           | **Semantic Reference** | **Definition**                                                                                                | **Data type**             | **Occurrence** |
|-----------------------------------------------|------------------------|---------------------------------------------------------------------------------------------------------------|---------------------------|----------------|
| member_state_legislation.member_state         | —                      | Code of the member state whose legislation applies (ISO 3166-1 alpha-2; EU/EFTA + UK = 32 countries)          | Code (ISO 3166-1 alpha-2) | 1:1            |
| member_state_legislation.starting_date        | —                      | Starting date from which the member state legislation applies (ISO 8601)                                       | Date (YYYY-MM-DD)         | 1:1            |
| member_state_legislation.ending_date          | —                      | Ending date until which the member state legislation applies (ISO 8601)                                        | Date (YYYY-MM-DD)         | 1:1            |

#### Section 3 — Employer / Self-Employment Details (SD Groups 9–10)

Each employer entry **SHALL** contain the following mandatory attributes:

| **Data Identifier**             | **Semantic Reference** | **Definition**                                                                                 | **Data type**             | **Occurrence** | **SD Group** |
|---------------------------------|------------------------|------------------------------------------------------------------------------------------------|---------------------------|----------------|--------------|
| employer.employment_type        | —                      | Type of employment: `01` = Employment, `02` = Self-Employment (EESSI codelist)                 | Code                      | 1:1            | 9            |
| employer.name                   | —                      | Name of the employer or self-employed entity                                                   | String                    | 1:1            | 9            |
| employer.employer_id            | —                      | Identifier of the employer                                                                     | String                    | 1:1            | 9            |
| employer.id_type                | —                      | Type of the employer identifier: `01`, `02`, `03`, `99` (see EESSI codelist — tbd)             | Code                      | 1:1            | 9            |
| employer.address.town           | —                      | Town of the employer's address                                                                 | String                    | 1:1            | 10           |
| employer.address.country_code   | —                      | Country of the employer's address (ISO 3166-1 alpha-2)                                         | Code (ISO 3166-1 alpha-2) | 1:1            | 10           |

#### Section 4 — Places of Work (SD Groups 11–12)

When a specific place of work is declared:

| **Data Identifier**             | **Semantic Reference** | **Definition**                                                                            | **Data type**             | **Occurrence** | **SD Group** |
|---------------------------------|------------------------|-------------------------------------------------------------------------------------------|---------------------------|----------------|--------------|
| place_of_work.company_name      | —                      | Name of the company or vessel at the place of work                                        | String                    | 1:1            | 11           |
| place_of_work.town              | —                      | Town of the place of work                                                                 | String                    | 1:1            | 12           |
| place_of_work.country_code      | —                      | Country of the place of work (ISO 3166-1 alpha-2; EU/EFTA + UK)                           | Code (ISO 3166-1 alpha-2) | 1:1            | 12           |

When no fixed place of work exists:

| **Data Identifier**                   | **Semantic Reference** | **Definition**                                                                    | **Data type**             | **Occurrence** | **SD Group** |
|---------------------------------------|------------------------|-----------------------------------------------------------------------------------|---------------------------|----------------|--------------|
| no_fixed_place_of_work.country_code   | —                      | Country code indicating the country where no fixed place of work exists           | Code (ISO 3166-1 alpha-2) | 1:1            | 11           |

#### Section 5 — Status Confirmation (SD Group 13)

| **Data Identifier**          | **Semantic Reference** | **Definition**                                                                                                                              | **Data type** | **Occurrence** | **SD Group** |
|------------------------------|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|---------------|----------------|--------------|
| status_confirmation.status   | —                      | Status confirmation code identifying the type of cross-border situation (2-digit code per PD A1 codelist; 12 options — tbd)                 | Code          | 1:1            | 13           |

#### Section 6 — Unique Document Number (SD Group 14)

| **Data Identifier**    | **Semantic Reference** | **Definition**                                 | **Data type** | **Occurrence** | **SD Group** |
|------------------------|------------------------|------------------------------------------------|---------------|----------------|--------------|
| document.document_id   | —                      | Unique identifier of the issued PD A1 document | String        | 1:1            | 14           |

#### Section 7 — Competent Institution (SD Groups 15–16)

| **Data Identifier**              | **Semantic Reference** | **Definition**                                                                               | **Data type**             | **Occurrence** | **SD Group** |
|----------------------------------|------------------------|----------------------------------------------------------------------------------------------|---------------------------|----------------|--------------|
| institution.institution_id       | —                      | Identifier of the competent institution                                                      | String                    | 1:1            | 15           |
| institution.institution_name     | —                      | Name of the competent institution                                                            | String                    | 1:1            | 15           |
| institution.country_code         | —                      | Country code of the competent institution (ISO 3166-1 alpha-2; EU/EFTA + UK)                 | Code (ISO 3166-1 alpha-2) | 1:1            | 15           |

### 2.3 Optional Attributes

#### Subject Optional Attributes (SD Group 3)

| **Data Identifier** | **Semantic Reference** | **Definition**                                                 | **Data type** | **Occurrence** | **SD Group** |
|---------------------|------------------------|----------------------------------------------------------------|---------------|----------------|--------------|
| surname_at_birth    | —                      | Surname(s) of the citizen at birth (if different from current) | String        | 0:1            | 3            |
| forename_at_birth   | —                      | Forename(s) of the citizen at birth (if different from current)| String        | 0:1            | 3            |

#### Address Optional Fields

| **Data Identifier**             | **Semantic Reference** | **Definition**                                     | **Data type** | **Occurrence** | **SD Group** |
|---------------------------------|------------------------|----------------------------------------------------|---------------|----------------|--------------|
| address_residence.street_nr     | —                      | Street and number of the residence address         | String        | 0:1            | 7            |
| address_residence.post_code     | —                      | Postal code of the residence address               | String        | 0:1            | 7            |
| address_stay.street_nr          | —                      | Street and number of the stay address              | String        | 0:1            | 8            |
| address_stay.post_code          | —                      | Postal code of the stay address                    | String        | 0:1            | 8            |

#### Member State Legislation Optional Attributes (Non-SD)

| **Data Identifier**                             | **Semantic Reference** | **Definition**                                                                         | **Data type** | **Occurrence** |
|-------------------------------------------------|------------------------|----------------------------------------------------------------------------------------|---------------|----------------|
| member_state_legislation.applies_for_duration   | —                      | Indicates whether the certificate applies for the full duration of the activity        | Boolean       | 0:1            |
| member_state_legislation.provisional            | —                      | Indicates whether the determination is provisional                                     | Boolean       | 0:1            |
| member_state_legislation.transitional_rules     | —                      | Indicates whether transitional rules apply                                              | Boolean       | 0:1            |

#### Employer Address Optional Fields (SD Group 10)

| **Data Identifier**          | **Semantic Reference** | **Definition**                              | **Data type** | **Occurrence** | **SD Group** |
|------------------------------|------------------------|---------------------------------------------|---------------|----------------|--------------|
| employer.address.street_nr   | —                      | Street and number of the employer's address | String        | 0:1            | 10           |
| employer.address.post_code   | —                      | Postal code of the employer's address       | String        | 0:1            | 10           |

#### Place of Work Optional Fields (SD Groups 11–12)

| **Data Identifier**            | **Semantic Reference** | **Definition**                                                             | **Data type** | **Occurrence** | **SD Group** |
|--------------------------------|------------------------|----------------------------------------------------------------------------|---------------|----------------|--------------|
| place_of_work.flag_base_home   | —                      | Flag, base or home state of the vessel (maritime use case)                 | String        | 0:1            | 11           |
| place_of_work.company_id       | —                      | Identifier of the company at the place of work                             | String        | 0:1            | 11           |
| place_of_work.id_type          | —                      | Type of company identifier: `01`, `02`, `03`, `99` (EESSI codelist — tbd) | Code          | 0:1            | 11           |
| place_of_work.street_nr        | —                      | Street and number of the place of work                                     | String        | 0:1            | 12           |
| place_of_work.postal_code      | —                      | Postal code of the place of work                                           | String        | 0:1            | 12           |

#### Competent Institution Optional Fields (SD Group 16)

| **Data Identifier**         | **Semantic Reference** | **Definition**                                                           | **Data type**             | **Occurrence** | **SD Group** |
|-----------------------------|------------------------|--------------------------------------------------------------------------|---------------------------|----------------|--------------|
| institution.fax             | —                      | Office fax number of the competent institution                           | String                    | 0:1            | 16           |
| institution.phone           | —                      | Office phone number of the competent institution                         | String                    | 0:1            | 16           |
| institution.email           | —                      | Email address of the competent institution                               | String                    | 0:1            | 16           |
| institution.street_nr       | —                      | Street and number of the competent institution's address                 | String                    | 0:1            | 16           |
| institution.town            | —                      | Town of the competent institution's address                              | String                    | 0:1            | 16           |
| institution.postal_code     | —                      | Postal code of the competent institution's address                       | String                    | 0:1            | 16           |
| institution.country_code    | —                      | Country code of the competent institution's address (ISO 3166-1 alpha-2) | Code (ISO 3166-1 alpha-2) | 0:1            | 16           |

### 2.4 Conditional Attributes

No conditional attributes are defined for this attestation type. All attributes are either
mandatory or optional as specified above.

### 2.5 Mandatory Metadata

| **Data Identifier**          | **Definition**                                                                                                                                          | **Data type** |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| issuance_date                | The date and time when the PD A1 Attestation was issued (ISO 8601)                                                                                      | DateTime      |
| expiry_date                  | The date and time when the PD A1 Attestation expires (ISO 8601); relation to business decision date tbd                                                 | DateTime      |
| issuing_entity               | The identifier of the competent social security institution that issued the attestation                                                                 | String        |
| attestation_legal_category   | Indicates the legal category of this attestation ("QEAA" or "EAA")                                                                                      | String        |
| vct                          | A unique identifier (often a URL or URN) for the type of credential, indicating which claims must be present and which can be selectively disclosed      | String        |
| binding                      | Information on the holder binding type (e.g., PID binding, Wallet Instance binding, no binding)                                                         | String / tbd  |

### 2.6 Optional Metadata

| **Data Identifier** | **Definition**                                                             | **Data type** |
|---------------------|----------------------------------------------------------------------------|---------------|
| trust_anchor_url    | URL where the trust anchor for verifying this attestation can be retrieved | URI           |
| schema_version      | Version of the schema used for this attestation                            | String        |
| schema_id           | Schema identifier for the PD A1 credential schema (tbd)                   | String        |
| revocation          | Reference to revocation information for this attestation (tbd)            | String / tbd  |

### 2.7 Conditional Metadata

No conditional metadata elements are defined for this attestation type.

### 2.8 Value Lists

#### 2.8.1 Country Codes

All country code attributes **SHALL** use **ISO 3166-1 alpha-2** codes. For member state
legislation and places of work, the applicable country set covers all **EU/EFTA countries
+ UK (32 countries total)**:

| **Example Code** | **Country**    |
|------------------|----------------|
| DE               | Germany        |
| FR               | France         |
| IT               | Italy          |
| ES               | Spain          |
| NL               | Netherlands    |
| PL               | Poland         |
| CH               | Switzerland    |
| NO               | Norway         |
| GB               | United Kingdom |

> For the full list of applicable EU/EFTA + UK country codes, refer to the EESSI country
> code reference list.

#### 2.8.2 Employment Type Codes

The `employment_type` attribute **SHALL** use one of the following standardized values:

| **Code** | **Definition**  |
|----------|-----------------|
| 01       | Employment      |
| 02       | Self-Employment |

#### 2.8.3 Employer / Company Identifier Type Codes

The `id_type` attribute for employer and place of work identifiers **SHALL** use one of the
following standardized values (per EESSI — tbd):

| **Code** | **Definition**             |
|----------|----------------------------|
| 01       | Identification/Registration   |
| 02       | Social Security   |
| 03       | Fiscal   |
| 98       | Unknown        |

#### 2.8.4 Status Confirmation Codes

The `status_confirmation` attribute **SHALL** use one of the following standardized 2-digit
values as defined in the PD A1 codelist (12 options — tbd):

| **Code** | **Definition**                                                                              |
|----------|---------------------------------------------------------------------------------------------|
| 01       | Posted employed person           |
| 02       | Employed, working in two or more States           |
| 03       | Posted self-employed person           |
| 04       | Self-employed, working in two or more States           |
| 05       | Civil servant           |
| 06       | Contract staff           |
| 07       | Mariner           |
| 08       | Working as an employed person and as a self-employed person in different States           |
| 09       | Working as a civil servant in one State and as an employed/self-employed person in one or more other States           |
| 10       | Flight or cabin crew member      |
| 11       | Exception           |
| 12       | Working as an employed / self-employed person in the State which legislation applies           |

### 2.9 Integrity Rules

The following integrity rules **SHALL** be enforced:

- The `subject` section **SHALL** be present and **SHALL** contain at minimum `pin`,
  `gender`, `family_name`, `forename`, `date_of_birth`, `nationality`, and `place_of_birth`.
- At least one address **SHALL** be provided within the `subject` section (either
  `address_residence` or `address_stay`).
- `nationality` **SHALL** be an array of one or more valid ISO 3166-1 alpha-2 country codes.
- `place_of_birth.country_code` **SHALL** be a valid ISO 3166-1 alpha-2 country code.
- `address_residence.country_code` and `address_stay.country_code`, when present,
  **SHALL** be valid ISO 3166-1 alpha-2 country codes.
- The `member_state_legislation` section **SHALL** be present and **SHALL** contain
  `member_state`, `starting_date`, and `ending_date`.
- `member_state_legislation.member_state` **SHALL** be a valid ISO 3166-1 alpha-2 country
  code from the EU/EFTA + UK set (32 countries).
- `starting_date` and `ending_date` **SHALL** be valid ISO 8601 dates (YYYY-MM-DD).
- `ending_date` **SHALL** be equal to or later than `starting_date`.
- `employer_details` **SHALL** contain at least one employer entry.
- Each employer entry **SHALL** contain `employment_type`, `name`, `employer_id`, `id_type`,
  and a valid `address` with at minimum `town` and `country_code`.
- `employment_type` **SHALL** be one of the values defined in Section 2.8.2.
- `id_type` for employer identifiers **SHALL** be one of the values defined in Section 2.8.3.
- `places_of_work` **SHALL** contain at least one entry (either `no_fixed_place_of_work` or
  one or more `place_of_work` entries).
- Each `place_of_work` entry **SHALL** contain `company_name`, `town`, and `country_code`.
- `status_confirmation.status` **SHALL** be a valid 2-digit code from the PD A1 status
  confirmation codelist (Section 2.8.4).
- `document.document_id` **SHALL** be a non-empty string.
- The `competent_institution` section **SHALL** contain `institution_id`, `institution_name`,
  and `country_code`.
- `institution.country_code` **SHALL** be a valid ISO 3166-1 alpha-2 country code from the
  EU/EFTA + UK set.
- `date_of_birth` **SHALL** be a valid ISO 8601 date (YYYY-MM-DD).
- `issuance_date` and `expiry_date` **SHALL** be valid ISO 8601 DateTimes.
- `expiry_date` **SHALL** be later than `issuance_date`.
- `issuance_date` **SHALL** be in the past.
- `attestation_legal_category` **SHALL** be one of `"EAA"` or `"QEAA"`.
- `vct` **SHALL** be `eu.we-build.pda1.1`.
- Selective Disclosure **SHALL** be applied at SD element group level only — individual
  fields within a group **SHALL NOT** be independently selectable.
- Section 2 (Member State Legislation) **SHALL** always be fully disclosed (Non-SD).
- Each attribute **SHALL** appear at most once within its respective object scope.

---

## 3 Attestation Encoding

### 3.1 ISO/IEC 18013-5-Compliant Encoding

ISO/IEC 18013-5 (also called mdoc) is out of scope for this Rulebook, as specific aspects of offline proximity
presentation are not a current requirement for the PD A1 attestation.

### 3.2 SD-JWT VC-Based Encoding

The PD A1 attestation uses the SD-JWT VC format to allow for selective disclosure of citizen
and employment attributes based on SD element groups.

**Selective Disclosure:** Disclosure is applied at the **SD element group level**, not at the
individual field level. A Relying Party **SHALL** request disclosure of complete logical blocks
(e.g., full address block, full employer block). It is not possible to disclose partial blocks
(e.g., only the town from an address without the other address fields).

Section 2 (Member State Legislation) is **Non-SD** and is **always fully disclosed**.

The `.` notation is used to indicate the nesting of attributes.

**Verifiable Credential Type (`vct`):** `vct: eu.we-build.pda1.1`

#### 3.2.1 Attribute Encoding Table

| **Data Identifier**              | **Attribute Identifier**                       | **Encoding Format**                 | **Reference / Notes**                                                                      | **Disclosable** |
|----------------------------------|------------------------------------------------|-------------------------------------|--------------------------------------------------------------------------------------------|-----------------|
| pin                              | subject.pin                                    | String                              | Personal Identification Number (Social Security Number); mandatory                         | MUST            |
| gender                           | subject.gender                                 | String / Codelist                   | Gender of the citizen (codelist tbd); mandatory                                            | MUST            |
| family_name                      | subject.family_name                            | String                              | Family name(s) of the citizen in full; mandatory                                           | MUST            |
| forename                         | subject.forename                               | String                              | Forename(s) of the citizen in full; mandatory                                              | MUST            |
| surname_at_birth                 | subject.surname_at_birth                       | String                              | Surname(s) at birth; optional                                                              | MUST            |
| forename_at_birth                | subject.forename_at_birth                      | String                              | Forename(s) at birth; optional                                                             | MUST            |
| date_of_birth                    | subject.date_of_birth                          | String (ISO 8601 YYYY-MM-DD)        | Date of birth of the citizen; mandatory                                                    | MUST            |
| nationality                      | subject.nationality                            | Array of Codes (ISO 3166-1 alpha-2) | Nationality/ies; Verifier always requests all; user may decide which to present; mandatory | MUST            |
| place_of_birth.town              | subject.place_of_birth.town                    | String                              | Town where the citizen was born; mandatory                                                 | MUST            |
| place_of_birth.country_code      | subject.place_of_birth.country_code            | Code (ISO 3166-1 alpha-2)           | Country where the citizen was born; mandatory                                              | MUST            |
| address_residence.street_nr      | subject.address_residence.street_nr            | String                              | Street and number of residence address; optional                                           | MUST            |
| address_residence.town           | subject.address_residence.town                 | String                              | Town of residence address; mandatory if address_residence present                          | MUST            |
| address_residence.post_code      | subject.address_residence.post_code            | String                              | Postal code of residence address; optional                                                 | MUST            |
| address_residence.country_code   | subject.address_residence.country_code         | Code (ISO 3166-1 alpha-2)           | Country of residence address; mandatory if address_residence present                       | MUST            |
| address_stay.street_nr           | subject.address_stay[n].street_nr              | String                              | Street and number of stay address; optional                                                | MUST            |
| address_stay.town                | subject.address_stay[n].town                   | String                              | Town of stay address; mandatory if address_stay present                                    | MUST            |
| address_stay.post_code           | subject.address_stay[n].post_code              | String                              | Postal code of stay address; optional                                                      | MUST            |
| address_stay.country_code        | subject.address_stay[n].country_code           | Code (ISO 3166-1 alpha-2)           | Country of stay address; mandatory if address_stay present                                 | MUST            |
| **Member State Legislation***    |                                                |                                     |                                                                                            |                 |
| member_state                     | member_state_legislation.member_state          | Code (ISO 3166-1 alpha-2)           | Member state whose legislation applies; always disclosed; mandatory                        | MUST NOT        |
| starting_date                    | member_state_legislation.starting_date         | String (ISO 8601 YYYY-MM-DD)        | Starting date of applicable legislation; always disclosed; mandatory                       | MUST NOT        |
| ending_date                      | member_state_legislation.ending_date           | String (ISO 8601 YYYY-MM-DD)        | Ending date of applicable legislation; always disclosed; mandatory                         | MUST NOT        |
| applies_for_duration             | member_state_legislation.applies_for_duration  | Boolean                             | True if certificate applies for full duration of activity; optional; always disclosed      | MUST NOT        |
| provisional                      | member_state_legislation.provisional           | Boolean                             | True if determination is provisional; optional; always disclosed                           | MUST NOT        |
| transitional_rules               | member_state_legislation.transitional_rules    | Boolean                             | True if transitional rules apply; optional; always disclosed                               | MUST NOT        |
| **Employer Details***            |                                                |                                     |                                                                                            |                 |
| employer.employment_type         | employer_details[n].employment_type            | Code                                | `01` = Employment, `02` = Self-Employment; mandatory                                       | MUST            |
| employer.name                    | employer_details[n].name                       | String                              | Name of the employer; mandatory                                                            | MUST            |
| employer.employer_id             | employer_details[n].employer_id                | String                              | Identifier of the employer; mandatory                                                      | MUST            |
| employer.id_type                 | employer_details[n].id_type                    | Code                                | Type of employer identifier (01, 02, 03, 99 per EESSI); mandatory                          | MUST            |
| employer.address.street_nr       | employer_details[n].address.street_nr          | String                              | Street and number of employer address; optional                                            | MUST            |
| employer.address.town            | employer_details[n].address.town               | String                              | Town of employer address; mandatory                                                        | MUST            |
| employer.address.post_code       | employer_details[n].address.post_code          | String                              | Postal code of employer address; optional                                                  | MUST            |
| employer.address.country_code    | employer_details[n].address.country_code       | Code (ISO 3166-1 alpha-2)           | Country of employer address; mandatory                                                     | MUST            |
| **Places of Work***              |                                                |                                     |                                                                                            |                 |
| no_fixed_place.country_code      | places_of_work[n].no_fixed_place.country_code  | Code (ISO 3166-1 alpha-2)           | Country for no fixed place of work; mandatory if no_fixed_place present                    | MUST            |
| place_of_work.company_name       | places_of_work[n].place_of_work.company_name   | String                              | Name of company or vessel at place of work; mandatory if place_of_work present             | MUST            |
| place_of_work.flag_base_home     | places_of_work[n].place_of_work.flag_base_home | String                              | Flag, base or home state of vessel; optional                                               | MUST            |
| place_of_work.company_id         | places_of_work[n].place_of_work.company_id     | String                              | Company identifier at place of work; optional                                              | MUST            |
| place_of_work.id_type            | places_of_work[n].place_of_work.id_type        | Code                                | Type of company identifier (01, 02, 03, 99); optional                                      | MUST            |
| place_of_work.street_nr          | places_of_work[n].place_of_work.street_nr      | String                              | Street and number of place of work; optional                                               | MUST            |
| place_of_work.town               | places_of_work[n].place_of_work.town           | String                              | Town of place of work; mandatory if place_of_work present                                  | MUST            |
| place_of_work.postal_code        | places_of_work[n].place_of_work.postal_code    | String                              | Postal code of place of work; optional                                                     | MUST            |
| place_of_work.country_code       | places_of_work[n].place_of_work.country_code   | Code (ISO 3166-1 alpha-2)           | Country of place of work (EU/EFTA + UK); mandatory if place_of_work present                | MUST            |
| **Status Confirmation***         |                                                |                                     |                                                                                            |                 |
| status_confirmation              | status_confirmation.status                     | Code                                | 2-digit status code per PD A1 codelist (12 options — tbd); mandatory                       | MUST            |
| **Unique Document Number***      |                                                |                                     |                                                                                            |                 |
| document_id                      | document.document_id                           | String                              | Unique identifier of the issued PD A1 document; mandatory                                  | MUST            |
| **Competent Institution**        |                                                |                                     |                                                                                            |                 |
| institution_id                   | institution.institution_id                     | String                              | Identifier of the competent institution; mandatory                                         | MUST            |
| institution_name                 | institution.institution_name                   | String                              | Name of the competent institution; mandatory                                               | MUST            |
| institution.country_code         | institution.country_code                       | Code (ISO 3166-1 alpha-2)           | Country of the competent institution; mandatory                                            | MUST            |
| institution.fax                  | institution.fax                                | String                              | Office fax number; optional                                                                | MUST            |
| institution.phone                | institution.phone                              | String                              | Office phone number; optional                                                              | MUST            |
| institution.email                | institution.email                              | String                              | Email address of the institution; optional                                                 | MUST            |
| institution.street_nr            | institution.street_nr                          | String                              | Street and number of institution address; optional                                         | MUST            |
| institution.town                 | institution.town                               | String                              | Town of institution address; optional                                                      | MUST            |
| institution.postal_code          | institution.postal_code                        | String                              | Postal code of institution address; optional                                               | MUST            |
| institution.country_code_address | institution.country_code_address               | Code (ISO 3166-1 alpha-2)           | Country of institution address; optional                                                   | MUST            |
| **Metadata**                     |                                                |                                     |                                                                                            |                 |
| issuance_date                    | iat                                            | Number (Unix timestamp)             | Date and time when the attestation was issued (ISO 8601); RFC 7519                         | MUST NOT        |
| expiry_date                      | exp                                            | Number (Unix timestamp)             | Date and time when the attestation expires (ISO 8601); RFC 7519                            | MUST NOT        |
| issuing_entity                   | iss                                            | String (URI or DID)                 | Identifier of the competent institution that issued the attestation; RFC 7519              | MUST NOT        |
| attestation_legal_category       | attestation_legal_category                     | String                              | One of "EAA" or "QEAA" as defined by eIDAS 2                                               | MUST NOT        |
| vct                              | vct                                            | String                              | The vct definition                                                                         | MUST NOT        |
| binding                          | binding                                        | String / tbd                        | Holder binding type (e.g., PID binding, Wallet Instance binding, no binding)               | MUST NOT        |
| schema_version                   | schema_version                                 | String                              | Version of the schema used; optional                                                       | MAY             |
| trust_anchor_url                 | trust_anchor_url                               | String (URI)                        | URL where the trust anchor for verifying this attestation can be retrieved; optional       | MAY             |

**Notes:**

- **MUST**: The claim **SHALL** be selectively disclosable at the SD element group level — the
  holder **MAY** choose to disclose or withhold this entire SD group when presenting the
  credential to a Relying Party. Individual fields within an SD group are **not** independently
  selectable.
- **MUST NOT**: The claim **SHALL NOT** be selectively disclosable — it is always present in
  plain text in the JWT header/payload and cannot be withheld by the holder.
- **MAY**: The claim **MAY** be selectively disclosable if the issuer supports it.
- Section 2 (Member State Legislation) claims are marked `MUST NOT` as they are Non-SD
  and always fully disclosed.
- `iat`, `exp`, and `iss` follow RFC 7519 standard JWT claim naming conventions.
- All employer detail blocks **SHALL** be disclosed as a whole when requested, to provide a
  complete picture of the employment situation.

#### 3.2.2 Status Claim

For SD-JWT VC-compliant PD A1 Attestations, the attestation **MUST** include a `status` claim
if the technical validity period is greater than 24 hours. This claim enables Relying Parties
to determine if a credential has been revoked via a status list mechanism, as specified in
SD-JWT VC.

The `status` claim **SHALL** be a JSON object with the following members:

- `type` (string): **SHALL** be `"status-list"`.
- `status_list_credential` (string, URI): The URI of the Status List Credential document that
  contains the status bitstring.
- `status_list_index` (integer, >= 0): The zero-based index into the status list bitstring that
  corresponds to this credential.
- `status_purpose` (string): **SHALL** be `"revocation"` for this attestation.

**Example:**

```json
{
  "status": {
 "type": "status-list",
 "status_list_credential": "https://issuer.example.com/status/pda1/2025",
 "status_list_index": 789,
 "status_purpose": "revocation"
  }
}
```

### 3.2.3 Example Payload

The following is a non-normative example of a PD A1 SD-JWT VC payload:
```
{
  "vct": "eu.we-build.pda1.1",
  "attestation_legal_category": "QEAA",
  "iss": "did:example:social-security-institution-de",
  "iat": 1746000000,
  "exp": 1809158400,
  "jti": "pda1-attestation-20260501-001",
  "binding": "PID binding",
  "subject": {
    "pin": "12345678A",
    "gender": "M",
    "family_name": "Müller",
    "forename": "Hans",
    "date_of_birth": "1985-06-15",
    "nationality": ["DE"],
    "place_of_birth": {
      "town": "Munich",
      "country_code": "DE"
    },
    "address_residence": {
      "street_nr": "Hauptstrasse 5",
      "town": "Berlin",
      "post_code": "10115",
      "country_code": "DE"
    },
    "address_stay": [
      {
        "street_nr": "Rue de la Paix 10",
        "town": "Paris",
        "post_code": "75001",
        "country_code": "FR"
      }
    ]
  },
  "member_state_legislation": {
    "member_state": "DE",
    "starting_date": "2026-01-01",
    "ending_date": "2027-12-31",
    "applies_for_duration": false,
    "provisional": false,
    "transitional_rules": false
  },
  "employer_details": [
    {
      "employment_type": "01",
      "name": "Example GmbH",
      "employer_id": "DE123456789",
      "id_type": "01",
      "address": {
        "street_nr": "Industriestrasse 20",
        "town": "Frankfurt",
        "post_code": "60311",
        "country_code": "DE"
      }
    }
  ],
  "places_of_work": [
    {
      "place_of_work": {
        "company_name": "Client SA",
        "company_id": "FR987654321",
        "id_type": "01",
        "street_nr": "Avenue des Champs 5",
        "town": "Paris",
        "postal_code": "75008",
        "country_code": "FR"
      }
    }
  ],
  "status_confirmation": {
    "status": "01"
  },
  "document": {
    "document_id": "DE-PDA1-2026-00123456"
  },
  "institution": {
    "institution_id": "DE-DRV-001",
    "institution_name": "Deutsche Rentenversicherung Bund",
    "country_code": "DE",
    "phone": "+49 30 865 0",
    "email": "info@drv-bund.de",
    "street_nr": "Ruhrstrasse 2",
    "town": "Berlin",
    "postal_code": "10709",
    "country_code_address": "DE"
  },
  "status": {
    "type": "status-list",
    "status_list_credential": "https://example.com/status/pda1-list-1",
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
Sample payloads are provided under ../data-schemas/sd-jwt/sample-data/company-info-sd-jwt-sample.json

### 3.3 W3C Verifiable Credentials Data Model-based encoding

@TODO — To be discussed: which stakeholders will support this format and which use cases require it.

## 4 Attestation usage
### 4.1. Issuance process ###
TBD
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
