# Attestation Rulebook for attestations of type Posted Worker Notification (PWN)

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

**Has a company fulfilled its legal obligation to notify the host EU Member State authorities
prior to sending workers to provide cross-border services within the EU/EFTA area?**

The Posted Worker Notification (PWN) Attestation provides a standardized, verifiable digital
representation of the Posted Worker Notification, enabling structured exchange of posting
information for use in cross-border labour compliance verification, supplier onboarding, and
regulatory audit processes by host Member State authorities, procurers, and labour inspectorates.

The PWN is an administrative requirement for companies (legal employers) that provide intra-EU
cross-border services with their employees — both EU and non-EU nationals — either to a customer
or into another group entity. The notification must be filed with the authorities of the host EU
Member State (usually on a government portal) prior to the start of the delivery of the service.

The PWN was introduced pursuant to
[EU Directive 2014/67/EU](https://eur-lex.europa.eu/eli/dir/2014/67/oj/eng) to enable EU Member
States to monitor that Posted Workers are protected by the salary and labour conditions set out
in host legislation and collective labour agreements, and therefore do not undercut local labour
force. More or less half of the EU Member States have extended the scope of the PWN also to
employers based outside the EU.

The labour law protection of posted workers is set out in the Posting of Workers Directive
(PWD), which was adopted in 1996 and revised in 2018:
[EUR-Lex - 01996L0071-20200730 - EN - EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A01996L0071-20200730)

The **Know Your Employee (KYE)** scenario (Scenario 5) is part of BU1 and will lead to MVP
and MVP+ implementations using both Natural Person Wallets and Legal Person Wallets.
The high-level scenario is:

> *"A company A in a country A would like to send one of their employees to work and provide a
> service to company B in country B."*

This scenario requires the issuance of three main credentials:
- **Employee Credentials**
- **Portable Document (PD) A1**
- **Posted Worker Notification (PWN)**

### 1.1 Document Scope and Purpose

The PWN Attestation provides a standardized, verifiable digital representation of the Posted
Worker Notification. It enables structured exchange of posting information for use in
cross-border labour compliance verification, supplier onboarding, and regulatory audit processes
by host Member State authorities, procurers, and labour inspectorates.

The PWN Attestation captures all key attributes required by national host country authorities,
including:
- Subject (posted worker) identity attributes
- Assignment-related information (home member state, start/end dates)
- Home employer details
- Host company details
- Employee job duties abroad

The attestation schema is designed to be sufficiently generic to cover national PWN requirements
across EU Member States, verified against the requirements of **Spain** and **Netherlands** as
representative examples.

**Design Decisions**

This PWN Attestation Rulebook is based on:
- EU Directive 2014/67/EU — Posted Workers Enforcement Directive
- Posting of Workers Directive (PWD) 96/71/EC as revised in 2018
- National PWN portal requirements (Spain, Netherlands as reference implementations)
- EUDI Wallet / eIDAS 2.0 framework for digital identity and verifiable attestations
- ISO 3166-1 alpha-2 for country codes
- ISO 8601 for date formatting
- SD-JWT VC format for selective disclosure

### 1.2 Document Structure

This Rulebook is structured as follows:

- **Chapter 2** describes the PWN attestation attributes and metadata in an
  encoding-independent manner, including the data model.
- **Chapter 3** specifies how the attestation attributes and metadata are encoded:
  Section 3.2 covers SD-JWT VC-based encoding.
- **Chapter 4** specifies attestation usage scenarios, Relying Party obligations, and
  integration with KYE workflows.
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

| **Term**                      | **Description**                                                                                                                                                                                          |
|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PWN                           | Posted Worker Notification — an administrative requirement for companies providing intra-EU cross-border services with posted workers, filed with the host EU Member State authorities prior to service start |
| Posted Worker                 | A citizen employed in one EU/EFTA member state ("sending state") who is temporarily sent to work in another member state ("receiving state") for a defined period                                         |
| Home Employer                 | The legal employer in the sending state that employs the posted worker and is responsible for filing the PWN                                                                                               |
| Host Company                  | The legal entity in the receiving/host member state that receives the posted worker's services                                                                                                             |
| Sending State                 | The EU/EFTA member state where the home employer is established and from which the worker is posted                                                                                                        |
| Receiving State               | The EU/EFTA member state where the posted worker temporarily performs work (host country)                                                                                                                  |
| Administrative Representative | A designated person responsible for administrative PWN filings on behalf of the employer                                                                                                                  |
| Social Representative         | A designated person responsible for social/labour matters related to the posting                                                                                                                           |
| KYE                           | Know Your Employee — a due diligence scenario (Scenario 5 / BU1) enabling companies to verify employee identity and posting status in cross-border work situations                                        |
| Employee Credential           | A credential issued by an employer to its employees certifying employment at a given point in time                                                                                                        |
| PWD                           | Posting of Workers Directive — EU Directive 96/71/EC as revised in 2018, setting out labour law protection for posted workers                                                                             |
| NACE                          | Nomenclature of Economic Activities — EU standard for classifying economic/industry sectors                                                                                                               |
| VAT ID                        | Value Added Tax identification number — national tax identifier for legal entities                                                                                                                         |
| EAA                           | Electronic Attestation of Attributes — as defined under eIDAS 2.0                                                                                                                                         |
| QEAA                          | Qualified Electronic Attestation of Attributes — as defined under eIDAS 2.0                                                                                                                               |
| ISO 3166-1 alpha-2            | International standard defining 2-digit country codes (e.g., DE, FR, ES, NL)                                                                                                                             |
| ISO 8601                      | International standard for date and time representations (e.g., YYYY-MM-DD)                                                                                                                              |

---

## 2 Attestation Attributes and Metadata

The PWN Attestation is designed to provide a standardized, verifiable digital representation of
the Posted Worker Notification. It captures all key attributes required by host Member State
authorities for compliance verification, including subject identity, assignment details, home
employer information, host company details, and employee job duties.

### 2.1 Introduction

**Data Model:**

```
PWN Credential
├── Subject [1:1] — mandatory
│ ├── pin (String) — mandatory
│ ├── family_name (String) — mandatory
│ ├── forename (String) — mandatory
│ ├── date_of_birth (date) — mandatory
│ ├── nationality (Code [1:n], ISO 3166-1 alpha-2) — mandatory
│ ├── job_title_home_country (String) — mandatory
│ ├── gender (String/Code) — optional
│ ├── surname_at_birth (String) — optional
│ ├── forename_at_birth (String) — optional
│ ├── place_of_birth [1:1] — optional
│ │ ├── town (String)
│ │ └── country_code (Code, ISO 3166-1 alpha-2)
│ └── address [1:n] — mandatory
│ ├── address_residence [0:1] — optional
│ │ ├── street_nr (String)
│ │ ├── town (String)
│ │ ├── post_code (String)
│ │ └── country_code (Code, ISO 3166-1 alpha-2)
│ └── address_stay [0:n] — optional
│ ├── street_nr (String)
│ ├── town (String)
│ ├── post_code (String)
│ └── country_code (Code, ISO 3166-1 alpha-2)
│
├── Assignment Related Information [1:1] — mandatory
│ ├── home_member_state (Code, ISO 3166-1 alpha-2) — mandatory
│ ├── starting_date (date) — mandatory
│ ├── ending_date (date) — mandatory
│ ├── applies_for_duration (boolean) — optional
│ ├── determination_provisional (boolean) — optional
│ └── transitional_rules (boolean) — optional
│
├── Details of Home Employer(s)/Self-employment [1:1] — mandatory
│ ├── company_name (String) — mandatory
│ ├── industry_sector_nace (String) — mandatory
│ ├── construction_sector (boolean) — mandatory
│ ├── vat_id (String) — mandatory
│ ├── address_line_1 (String) — mandatory
│ ├── address_line_2 (String) — optional
│ ├── postal_code (String) — mandatory
│ ├── city (String) — mandatory
│ ├── municipality (String) — optional
│ ├── state (String) — optional
│ ├── country (Code, ISO 3166-1 alpha-2) — mandatory
│ ├── phone (String) — mandatory
│ ├── email (String) — mandatory
│ ├── administrative_representative [1:1] — mandatory
│ │ ├── last_name (String)
│ │ ├── first_name (String)
│ │ ├── telephone (String)
│ │ ├── email (String)
│ │ ├── address_line_1 (String)
│ │ ├── address_line_2 (String)
│ │ ├── postal_code (String)
│ │ ├── city (String)
│ │ ├── municipality (String)
│ │ ├── state (String)
│ │ └── country (Code, ISO 3166-1 alpha-2)
│ └── social_representative [1:1] — mandatory
│ ├── last_name (String)
│ ├── first_name (String)
│ ├── telephone (String)
│ ├── email (String)
│ ├── address_line_1 (String)
│ ├── address_line_2 (String)
│ ├── postal_code (String)
│ ├── city (String)
│ ├── municipality (String)
│ ├── state (String)
│ └── country (Code, ISO 3166-1 alpha-2)
│
├── Host Company [1:1] — mandatory
│ ├── company_name (String) — mandatory
│ ├── email (String) — mandatory
│ ├── telephone (String) — mandatory
│ ├── industry_sector (String) — mandatory
│ ├── vat_id (String) — mandatory
│ ├── address_line_1 (String) — mandatory
│ ├── address_line_2 (String) — optional
│ ├── postal_code (String) — mandatory
│ ├── city (String) — mandatory
│ ├── municipality (String) — optional
│ ├── state (String) — optional
│ └── country (Code, ISO 3166-1 alpha-2) — mandatory
│
├── Employee [1:1] — mandatory
│ └── job_duties_abroad (String) — mandatory
│
├── Place(s) of Work [1:n] — mandatory
│ ├── no_fixed_place [0:1] — optional
│ │ └── country_code (Code, ISO 3166-1 alpha-2)
│ └── place_of_work [0:n] — optional
│ ├── company_name (String)
│ ├── flag_base_home (String)
│ ├── company_id (String)
│ ├── id_type (Code)
│ ├── street_nr (String)
│ ├── town (String)
│ ├── postal_code (String)
│ └── country_code (Code, ISO 3166-1 alpha-2)
│
└── Competent Institution [1:1] — mandatory
├── institution_id (String) — mandatory
├── institution_name (String) — mandatory
├── country_code (Code, ISO 3166-1 alpha-2) — mandatory
├── fax (String) — optional
├── phone (String) — optional
├── email (String) — optional
├── street_nr (String) — optional
├── town (String) — optional
├── postal_code (String) — optional
└── country_code_address (Code, ISO 3166-1 alpha-2) — optional
```


**Explanation:**

- **Section 1 (Subject)** contains personal identity attributes of the posted worker.
  `job_title_home_country` is a PWN-specific addition not present in PD A1.
- **Section 2 (Assignment Related Information)** mirrors the PD A1 member state legislation
  section, providing the home member state, assignment start and end dates.
- **Section 3 (Home Employer Details)** provides comprehensive information about the sending
  employer, including industry sector, VAT ID, address, and designated administrative and
  social representatives.
- **Section 4 (Host Company)** identifies the receiving entity in the host member state.
- **Section 5 (Employee)** captures the job duties/activities to be performed abroad.
- **Section 6 (Places of Work)** aligns with the PD A1 structure for place(s) of work.
- **Section 7 (Competent Institution)** aligns with the PD A1 competent institution section.

**Attestation Classification:**

This attestation type **MAY** be classified as:
- **"EAA"** when self-issued by the home employer filing the PWN on behalf of their posted
  worker(s).
- **"QEAA"** when issued by a competent national authority (e.g., labour inspectorate)
  confirming receipt and acceptance of the PWN.

**Top-Level Data Identifiers:**

| **Data Identifier**     | **Semantic Reference** | **Definition**                                                                          | **Data type**       |
|-------------------------|------------------------|-----------------------------------------------------------------------------------------|---------------------|
| subject                 | [postedWorker](https://w3id.org/ebwv#postedWorker) | Personal identity attributes of the posted worker                                       | Object              |
| assignment_info         | [assignment](https://w3id.org/ebwv#assignment) | Assignment-related information including home member state and posting dates             | Object              |
| home_employer           | [employer](https://w3id.org/ebwv#employer) | Details of the home employer including company info and representatives                  | Object              |
| host_company            | [hostEntity](https://w3id.org/ebwv#hostEntity) | Details of the host company in the receiving member state                                | Object              |
| employee                | [employee](https://w3id.org/ebwv#employee) | Employee-specific information including job duties abroad                                | Object              |
| places_of_work          | [placeOfWork](https://w3id.org/ebwv#placeOfWork) | Place(s) where the posted worker performs work in the host country                       | Array [PlaceOfWork] |
| competent_institution   | ...                    | Details of the competent institution associated with the PWN                             | Object              |

---

### 2.2 Mandatory Attributes

#### Section 1 — Subject Attributes

| **Data Identifier**      | **Semantic Reference** | **Definition**                                                           | **Data type**                   | **Occurrence** |
|--------------------------|------------------------|--------------------------------------------------------------------------|---------------------------------|----------------|
| pin                      | [identifier](https://w3id.org/ebwv#identifier) | Personal Identification Number / ID number of the posted worker          | String                          | 1:1            |
| family_name              | [familyName](https://w3id.org/ebwv#familyName) | Family name(s) of the posted worker in full                              | String                          | 1:1            |
| forename                 | [givenName](https://w3id.org/ebwv#givenName) | Forename(s) of the posted worker in full                                 | String                          | 1:1            |
| date_of_birth            | [dateOfBirth](https://w3id.org/ebwv#dateOfBirth) | Date of birth of the posted worker (ISO 8601)                            | Date (YYYY-MM-DD)               | 1:1            |
| nationality              | [citizenship](https://w3id.org/ebwv#citizenship) | Nationality/ies of the posted worker                                     | Code [1:n] (ISO 3166-1 alpha-2) | 1:n            |
| job_title_home_country   | [jobTitle](https://w3id.org/ebwv#jobTitle) | Job title of the posted worker in the home country (PWN-specific)        | String                          | 1:1            |

#### Section 2 — Assignment Related Information Attributes

| **Data Identifier**                 | **Semantic Reference** | **Definition**                                                                     | **Data type**             | **Occurrence** |
|-------------------------------------|------------------------|------------------------------------------------------------------------------------|---------------------------|----------------|
| assignment_info.home_member_state   | [stateOfInsurance](https://w3id.org/ebwv#stateOfInsurance) | Code of the home member state from which the worker is posted (ISO 3166-1 alpha-2) | Code (ISO 3166-1 alpha-2) | 1:1            |
| assignment_info.starting_date       | [duration](https://w3id.org/ebwv#duration) | Start date of the posting assignment (ISO 8601)                                    | Date (YYYY-MM-DD)         | 1:1            |
| assignment_info.ending_date         | [duration](https://w3id.org/ebwv#duration) | End date of the posting assignment (ISO 8601)                                      | Date (YYYY-MM-DD)         | 1:1            |

#### Section 3 — Home Employer Attributes

| **Data Identifier**                                      | **Semantic Reference** | **Definition**                                                                            | **Data type**             | **Occurrence** |
|----------------------------------------------------------|------------------------|-------------------------------------------------------------------------------------------|---------------------------|----------------|
| home_employer.company_name                               | —                      | Full commercial name of the home employer                                                 | String                    | 1:1            |
| home_employer.industry_sector_nace                       | —                      | Industry sector of the home employer (NACE classification)                                | String                    | 1:1            |
| home_employer.construction_sector                        | —                      | Indicates whether the employer operates in the construction sector (true / false)         | Boolean                   | 1:1            |
| home_employer.vat_id                                     | —                      | VAT identification number of the home employer                                            | String                    | 1:1            |
| home_employer.address_line_1                             | —                      | Primary address line of the home employer's headquarters                                  | String                    | 1:1            |
| home_employer.postal_code                                | —                      | Postal code of the home employer's headquarters                                           | String                    | 1:1            |
| home_employer.city                                       | —                      | City of the home employer's headquarters                                                  | String                    | 1:1            |
| home_employer.country                                    | —                      | Country of the home employer's headquarters (ISO 3166-1 alpha-2)                          | Code (ISO 3166-1 alpha-2) | 1:1            |
| home_employer.phone                                      | —                      | Phone number of the home employer                                                         | String                    | 1:1            |
| home_employer.email                                      | —                      | Email address of the home employer                                                        | String                    | 1:1            |
| home_employer.administrative_representative.last_name    | —                      | Last name of the administrative representative                                            | String                    | 1:1            |
| home_employer.administrative_representative.first_name   | —                      | First name of the administrative representative                                           | String                    | 1:1            |
| home_employer.administrative_representative.telephone    | —                      | Telephone number of the administrative representative                                     | String                    | 1:1            |
| home_employer.administrative_representative.email        | —                      | Email address of the administrative representative                                        | String                    | 1:1            |
| home_employer.administrative_representative.city         | —                      | City of the administrative representative's address                                       | String                    | 1:1            |
| home_employer.administrative_representative.country      | —                      | Country of the administrative representative's address (ISO 3166-1 alpha-2)               | Code (ISO 3166-1 alpha-2) | 1:1            |
| home_employer.social_representative.last_name            | —                      | Last name of the social representative                                                    | String                    | 1:1            |
| home_employer.social_representative.first_name           | —                      | First name of the social representative                                                   | String                    | 1:1            |
| home_employer.social_representative.telephone            | —                      | Telephone number of the social representative                                             | String                    | 1:1            |
| home_employer.social_representative.email                | —                      | Email address of the social representative                                                | String                    | 1:1            |
| home_employer.social_representative.city                 | —                      | City of the social representative's address                                               | String                    | 1:1            |
| home_employer.social_representative.country              | —                      | Country of the social representative's address (ISO 3166-1 alpha-2)                       | Code (ISO 3166-1 alpha-2) | 1:1            |

#### Section 4 — Host Company Attributes

| **Data Identifier**           | **Semantic Reference** | **Definition**                                                                    | **Data type**             | **Occurrence** |
|-------------------------------|------------------------|-----------------------------------------------------------------------------------|---------------------------|----------------|
| host_company.company_name     | —                      | Full commercial name of the host company                                          | String                    | 1:1            |
| host_company.email            | —                      | Email address of the host company                                                 | String                    | 1:1            |
| host_company.telephone        | —                      | Telephone number of the host company                                              | String                    | 1:1            |
| host_company.industry_sector  | —                      | Industry sector of the host company                                               | String                    | 1:1            |
| host_company.vat_id           | —                      | VAT identification number of the host company                                     | String                    | 1:1            |
| host_company.address_line_1   | —                      | Primary address line of the host company's headquarters                           | String                    | 1:1            |
| host_company.postal_code      | —                      | Postal code of the host company's headquarters                                    | String                    | 1:1            |
| host_company.city             | —                      | City of the host company's headquarters                                           | String                    | 1:1            |
| host_company.country          | —                      | Country of the host company's headquarters (ISO 3166-1 alpha-2)                   | Code (ISO 3166-1 alpha-2) | 1:1            |

#### Section 5 — Employee Attributes

| **Data Identifier**          | **Semantic Reference** | **Definition**                                                                          | **Data type** | **Occurrence** |
|------------------------------|------------------------|-----------------------------------------------------------------------------------------|---------------|----------------|
| employee.job_duties_abroad   | —                      | Description of the job duties and activities to be performed abroad by the posted worker | String        | 1:1            |

#### Section 6 — Place(s) of Work Mandatory Fields

| **Data Identifier**                   | **Semantic Reference** | **Definition**                                                | **Data type**             | **Occurrence** |
|---------------------------------------|------------------------|---------------------------------------------------------------|---------------------------|----------------|
| place_of_work.company_name            | —                      | Name of the company or vessel at the place of work            | String                    | 1:1            |
| place_of_work.town                    | —                      | Town of the place of work                                     | String                    | 1:1            |
| place_of_work.country_code            | —                      | Country of the place of work (ISO 3166-1 alpha-2)             | Code (ISO 3166-1 alpha-2) | 1:1            |
| no_fixed_place_of_work.country_code   | —                      | Country code when no fixed place of work exists               | Code (ISO 3166-1 alpha-2) | 1:1            |

#### Section 7 — Competent Institution Mandatory Attributes

| **Data Identifier**             | **Semantic Reference** | **Definition**                                                             | **Data type**             | **Occurrence** |
|---------------------------------|------------------------|----------------------------------------------------------------------------|---------------------------|----------------|
| institution.institution_id      | —                      | Identifier of the competent institution associated with the PWN            | String                    | 1:1            |
| institution.institution_name    | —                      | Name of the competent institution                                          | String                    | 1:1            |
| institution.country_code        | —                      | Country code of the competent institution (ISO 3166-1 alpha-2)             | Code (ISO 3166-1 alpha-2) | 1:1            |

### 2.3 Optional Attributes

#### Subject Optional Attributes

| **Data Identifier**              | **Semantic Reference** | **Definition**                                                                | **Data type**             | **Occurrence** |
|----------------------------------|------------------------|-------------------------------------------------------------------------------|---------------------------|----------------|
| gender                           | —                      | Gender of the posted worker (codelist tbd)                                    | String / Code             | 0:1            |
| surname_at_birth                 | —                      | Surname(s) of the posted worker at birth (if different from current)          | String                    | 0:1            |
| forename_at_birth                | —                      | Forename(s) of the posted worker at birth (if different from current)         | String                    | 0:1            |
| place_of_birth.town              | —                      | Town/locality where the posted worker was born                                | String                    | 0:1            |
| place_of_birth.country_code      | —                      | Country where the posted worker was born (ISO 3166-1 alpha-2)                 | Code (ISO 3166-1 alpha-2) | 0:1            |
| address_residence.street_nr      | —                      | Street and number of the posted worker's residence address                    | String                    | 0:1            |
| address_residence.town           | —                      | Town of the posted worker's residence address                                 | String                    | 0:1            |
| address_residence.post_code      | —                      | Postal code of the posted worker's residence address                          | String                    | 0:1            |
| address_residence.country_code   | —                      | Country code of the posted worker's residence address (ISO 3166-1 alpha-2)    | Code (ISO 3166-1 alpha-2) | 0:1            |
| address_stay.street_nr           | —                      | Street and number of the posted worker's stay address                         | String                    | 0:1            |
| address_stay.town                | —                      | Town of the posted worker's stay address                                      | String                    | 0:1            |
| address_stay.post_code           | —                      | Postal code of the posted worker's stay address                               | String                    | 0:1            |
| address_stay.country_code        | —                      | Country code of the posted worker's stay address (ISO 3166-1 alpha-2)         | Code (ISO 3166-1 alpha-2) | 0:1            |

#### Assignment Related Information Optional Attributes

| **Data Identifier**                         | **Semantic Reference** | **Definition**                                                                  | **Data type** | **Occurrence** |
|---------------------------------------------|------------------------|---------------------------------------------------------------------------------|---------------|----------------|
| assignment_info.applies_for_duration        | —                      | Indicates whether the certificate applies for the full duration of the activity | Boolean       | 0:1            |
| assignment_info.determination_provisional   | —                      | Indicates whether the determination is provisional                               | Boolean       | 0:1            |
| assignment_info.transitional_rules          | —                      | Indicates whether transitional rules apply                                       | Boolean       | 0:1            |

#### Home Employer Optional Attributes

| **Data Identifier**                                       | **Semantic Reference** | **Definition**                                                                           | **Data type**             | **Occurrence** |
|-----------------------------------------------------------|------------------------|------------------------------------------------------------------------------------------|---------------------------|----------------|
| home_employer.address_line_2                              | —                      | Secondary address line of the home employer's headquarters                               | String                    | 0:1            |
| home_employer.municipality                                | —                      | Municipality of the home employer's headquarters                                         | String                    | 0:1            |
| home_employer.state                                       | —                      | State or region of the home employer's headquarters                                      | String                    | 0:1            |
| home_employer.administrative_representative.address_line_1 | —                     | Primary address line of the administrative representative                                | String                    | 0:1            |
| home_employer.administrative_representative.address_line_2 | —                     | Secondary address line of the administrative representative                              | String                    | 0:1            |
| home_employer.administrative_representative.postal_code    | —                     | Postal code of the administrative representative's address                               | String                    | 0:1            |
| home_employer.administrative_representative.municipality   | —                     | Municipality of the administrative representative's address                              | String                    | 0:1            |
| home_employer.administrative_representative.state          | —                     | State or region of the administrative representative's address                           | String                    | 0:1            |
| home_employer.social_representative.address_line_1         | —                     | Primary address line of the social representative                                        | String                    | 0:1            |
| home_employer.social_representative.address_line_2         | —                     | Secondary address line of the social representative                                      | String                    | 0:1            |
| home_employer.social_representative.postal_code            | —                     | Postal code of the social representative's address                                       | String                    | 0:1            |
| home_employer.social_representative.municipality           | —                     | Municipality of the social representative's address                                      | String                    | 0:1            |
| home_employer.social_representative.state                  | —                     | State or region of the social representative's address                                   | String                    | 0:1            |

#### Host Company Optional Attributes

| **Data Identifier**           | **Semantic Reference** | **Definition**                                                | **Data type**             | **Occurrence** |
|-------------------------------|------------------------|---------------------------------------------------------------|---------------------------|----------------|
| host_company.address_line_2   | —                      | Secondary address line of the host company's headquarters     | String                    | 0:1            |
| host_company.address_line_3   | —                      | Tertiary address line of the host company's headquarters      | String                    | 0:1            |
| host_company.municipality     | —                      | Municipality of the host company's headquarters               | String                    | 0:1            |
| host_company.state            | —                      | State or region of the host company's headquarters            | String                    | 0:1            |
| host_company.business_reg_nr  | —                      | Business registration number of the host company             | String                    | 0:1            |

#### Place of Work Optional Attributes

| **Data Identifier**            | **Semantic Reference** | **Definition**                                                      | **Data type** | **Occurrence** |
|--------------------------------|------------------------|---------------------------------------------------------------------|---------------|----------------|
| place_of_work.flag_base_home   | —                      | Flag, base or home state of the vessel (maritime use case)          | String        | 0:1            |
| place_of_work.company_id       | —                      | Identifier of the company at the place of work                      | String        | 0:1            |
| place_of_work.id_type          | —                      | Type of company identifier (per EESSI codelist — tbd)               | Code          | 0:1            |
| place_of_work.street_nr        | —                      | Street and number of the place of work                              | String        | 0:1            |
| place_of_work.postal_code      | —                      | Postal code of the place of work                                    | String        | 0:1            |

#### Competent Institution Optional Attributes

| **Data Identifier**                | **Semantic Reference** | **Definition**                                                           | **Data type**             | **Occurrence** |
|------------------------------------|------------------------|--------------------------------------------------------------------------|---------------------------|----------------|
| institution.fax                    | —                      | Office fax number of the competent institution                           | String                    | 0:1            |
| institution.phone                  | —                      | Office phone number of the competent institution                         | String                    | 0:1            |
| institution.email                  | —                      | Email address of the competent institution                               | String                    | 0:1            |
| institution.street_nr              | —                      | Street and number of the competent institution's address                 | String                    | 0:1            |
| institution.town                   | —                      | Town of the competent institution's address                              | String                    | 0:1            |
| institution.postal_code            | —                      | Postal code of the competent institution's address                       | String                    | 0:1            |
| institution.country_code_address   | —                      | Country code of the competent institution's address (ISO 3166-1 alpha-2) | Code (ISO 3166-1 alpha-2) | 0:1            |

#### National-Specific Optional Attributes (Netherlands PWN)

| **Data Identifier**                  | **Semantic Reference** | **Definition**                                                                                | **Data type**             | **Occurrence** |
|--------------------------------------|------------------------|-----------------------------------------------------------------------------------------------|---------------------------|----------------|
| employee.a1_certificate_applied      | —                      | Indicates whether an A1 certificate of coverage has been applied for (yes/no)                 | Boolean                   | 0:1            |
| employee.a1_country_of_issuance      | —                      | Country of issuance of the A1 certificate                                                     | Code (ISO 3166-1 alpha-2) | 0:1            |
| employee.a1_country_where_applied    | —                      | Country where the A1 certificate was applied for                                              | Code (ISO 3166-1 alpha-2) | 0:1            |
| employee.third_country_national      | —                      | Indicates whether the posted worker is a third-country national                               | Boolean                   | 0:1            |
| employee.work_permit_end_date        | —                      | End date of work permit issued by the sending country (for third-country nationals)           | Date (YYYY-MM-DD)         | 0:1            |

### 2.4 Conditional Attributes

| **Data Identifier**                                   | **Condition**                                                                                           | **Definition**                                                                                  | **Data type**             |
|-------------------------------------------------------|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|---------------------------|
| home_employer.administrative_representative.country   | Country **SHALL** be `NL` when filing for the Netherlands PWN                                          | Country of the administrative representative's address; must be Netherlands for NL PWN          | Code (ISO 3166-1 alpha-2) |
| employee.a1_certificate_applied                       | **SHALL** be present when filing for the Netherlands PWN portal                                        | Indicates whether A1 has been applied for                                                       | Boolean                   |

### 2.5 Mandatory Metadata

| **Data Identifier**        | **Definition**                                                                                                                                      | **Data type** |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| issuance_date              | The date and time when the PWN Attestation was issued (ISO 8601)                                                                                    | DateTime      |
| expiry_date                | The date and time when the PWN Attestation expires (ISO 8601)                                                                                       | DateTime      |
| issuing_entity             | The identifier of the entity that issued the attestation (home employer for EAA, or competent authority for QEAA)                                   | String        |
| attestation_legal_category | Indicates the legal category of this attestation ("EAA" or "QEAA")                                                                                  | String        |
| vct                        | A unique identifier (URL or URN) for the credential type, indicating which claims must be present and which can be selectively disclosed            | String        |
| binding                    | Information on the holder binding type (e.g., PID binding, Wallet Instance binding, no binding)                                                     | String / tbd  |

### 2.6 Optional Metadata

| **Data Identifier** | **Definition**                                                             | **Data type** |
|---------------------|----------------------------------------------------------------------------|---------------|
| trust_anchor_url    | URL where the trust anchor for verifying this attestation can be retrieved | URI           |
| schema_version      | Version of the schema used for this attestation                            | String        |
| schema_id           | Schema identifier for the PWN credential schema (tbd)                      | String        |
| revocation          | Reference to revocation information for this attestation (tbd)             | String / tbd  |

### 2.7 Conditional Metadata

No conditional metadata elements are defined for this attestation type.

### 2.8 Value Lists

#### 2.8.1 Country Codes

All country code attributes **SHALL** use **ISO 3166-1 alpha-2** codes:

| **Example Code** | **Country**  |
|------------------|--------------|
| DE               | Germany      |
| FR               | France       |
| ES               | Spain        |
| NL               | Netherlands  |
| IT               | Italy        |
| PL               | Poland       |
| BE               | Belgium      |
| PT               | Portugal     |
| CH               | Switzerland  |
| NO               | Norway       |

> For the full list of applicable EU/EFTA country codes, refer to the EESSI country code
> reference list.

#### 2.8.2 Construction Sector Flag

| **Value** | **Definition**                                                         |
|-----------|------------------------------------------------------------------------|
| true      | The home employer operates in the construction sector                  |
| false     | The home employer does not operate in the construction sector          |

#### 2.8.3 Employment Type Codes (for Place of Work section)

The `id_type` attribute for company identifiers at places of work **SHALL** use one of the
following standardized values (per EESSI — tbd):

| **Code** | **Definition**             |
|----------|----------------------------|
| 01       | Identifier type 01 (tbd)   |
| 02       | Identifier type 02 (tbd)   |
| 03       | Identifier type 03 (tbd)   |
| 99       | Other / unspecified        |

#### 2.8.4 National PWN Context Codes

The PWN attestation **SHOULD** include a `host_country_context` indicator to enable
country-specific validation logic:

| **Code** | **Definition**                                                                                     |
|----------|----------------------------------------------------------------------------------------------------|
| ES       | Spain PWN — requires administrative representative, VAT ID, NACE sector                            |
| NL       | Netherlands PWN — requires A1 certificate status, legal representative, HR representative          |
| OTHER    | Generic EU PWN for member states without specific national profile defined                          |

### 2.9 Integrity Rules

The following integrity rules **SHALL** be enforced:

- The `subject` section **SHALL** be present and **SHALL** contain at minimum `pin`,
  `family_name`, `forename`, `date_of_birth`, `nationality`, and `job_title_home_country`.
- `nationality` **SHALL** be an array of one or more valid ISO 3166-1 alpha-2 country codes.
- The `assignment_info` section **SHALL** be present and **SHALL** contain
  `home_member_state`, `starting_date`, and `ending_date`.
- `assignment_info.home_member_state` **SHALL** be a valid ISO 3166-1 alpha-2 country code.
- `starting_date` and `ending_date` **SHALL** be valid ISO 8601 dates (YYYY-MM-DD).
- `ending_date` **SHALL** be equal to or later than `starting_date`.
- The `home_employer` section **SHALL** be present and **SHALL** contain `company_name`,
  `industry_sector_nace`, `construction_sector`, `vat_id`, `address_line_1`, `postal_code`,
  `city`, `country`, `phone`, `email`, `administrative_representative`, and
  `social_representative`.
- `home_employer.country` **SHALL** be a valid ISO 3166-1 alpha-2 country code.
- `home_employer.construction_sector` **SHALL** be a boolean value (`true` or `false`).
- `administrative_representative` **SHALL** contain at minimum `last_name`, `first_name`,
  `telephone`, `email`, `city`, and `country`.
- `social_representative` **SHALL** contain at minimum `last_name`, `first_name`,
  `telephone`, `email`, `city`, and `country`.
- The `host_company` section **SHALL** be present and **SHALL** contain `company_name`,
  `email`, `telephone`, `industry_sector`, `vat_id`, `address_line_1`, `postal_code`,
  `city`, and `country`.
- `host_company.country` **SHALL** be a valid ISO 3166-1 alpha-2 country code.
- The `employee` section **SHALL** be present and **SHALL** contain `job_duties_abroad`.
- `places_of_work` **SHALL** contain at least one entry (either `no_fixed_place_of_work`
  or one or more `place_of_work` entries).
- Each `place_of_work` entry **SHALL** contain `company_name`, `town`, and `country_code`.
- All country codes **SHALL** be valid ISO 3166-1 alpha-2 codes.
- `issuance_date` and `expiry_date` **SHALL** be valid ISO 8601 DateTimes.
- `expiry_date` **SHALL** be later than `issuance_date`.
- `issuance_date` **SHALL** be in the past.
- `attestation_legal_category` **SHALL** be one of `"EAA"` or `"QEAA"`.
- `vct` **SHALL** be `"PWNCredential"`.
- Each attribute **SHALL** appear at most once within its respective object scope.
- For Netherlands PWN: `administrative_representative.country` **SHALL** be `NL`.
- For Netherlands PWN: `employee.a1_certificate_applied` **SHALL** be present.

---

## 3 Attestation Encoding

### 3.1 ISO/IEC 18013-5-Compliant Encoding

ISO/IEC 18013-5 (also called mdoc) is out of scope for this Rulebook, as offline proximity
presentation is not a current requirement for the PWN attestation.

### 3.2 SD-JWT VC-Based Encoding

The PWN Attestation uses the SD-JWT VC format to allow for selective disclosure of posting and
employer attributes.

**Selective Disclosure:** Top-level claims (e.g., `subject`, `home_employer`, `host_company`,
`places_of_work`) **SHALL** be individually selectively disclosable, enabling disclosure of only
the attributes requested by a Relying Party. Attributes nested within sub-objects **MAY** be
individually selectively disclosable.

The `.` notation is used to indicate the nesting of attributes.

**Verifiable Credential Type (`vct`):** `vct: PWNCredential`

#### 3.2.1 Attribute Encoding Table

| **Data Identifier**                | **Attribute Identifier**                               | **Encoding Format**                 | **Reference / Notes**                                                        | **Disclosable** |
|------------------------------------|--------------------------------------------------------|-------------------------------------|------------------------------------------------------------------------------|-----------------|
| **Subject**                        |                                                        |                                     |                                                                              |                 |
| pin                                | subject.pin                                            | String                              | Personal Identification Number / ID number; mandatory                        | MUST            |
| family_name                        | subject.family_name                                    | String                              | Family name(s) of the posted worker in full; mandatory                       | MUST            |
| forename                           | subject.forename                                       | String                              | Forename(s) of the posted worker in full; mandatory                          | MUST            |
| gender                             | subject.gender                                         | String / Code                       | Gender of the posted worker; optional                                        | MUST            |
| surname_at_birth                   | subject.surname_at_birth                               | String                              | Surname(s) at birth; optional                                                | MUST            |
| forename_at_birth                  | subject.forename_at_birth                              | String                              | Forename(s) at birth; optional                                               | MUST            |
| date_of_birth                      | subject.date_of_birth                                  | String (ISO 8601 YYYY-MM-DD)        | Date of birth of the posted worker; mandatory                                | MUST            |
| nationality                        | subject.nationality                                    | Array of Codes (ISO 3166-1 alpha-2) | Nationality/ies of the posted worker; mandatory                              | MUST            |
| job_title_home_country             | subject.job_title_home_country                         | String                              | Job title in the home country; PWN-specific; mandatory                       | MUST            |
| place_of_birth.town                | subject.place_of_birth.town                            | String                              | Town where the posted worker was born; optional                              | MUST            |
| place_of_birth.country_code        | subject.place_of_birth.country_code                    | Code (ISO 3166-1 alpha-2)           | Country where the posted worker was born; optional                           | MUST            |
| address_residence.street_nr        | subject.address_residence.street_nr                    | String                              | Street and number of residence address; optional                             | MUST            |
| address_residence.town             | subject.address_residence.town                         | String                              | Town of residence address; optional                                          | MUST            |
| address_residence.post_code        | subject.address_residence.post_code                    | String                              | Postal code of residence address; optional                                   | MUST            |
| address_residence.country_code     | subject.address_residence.country_code                 | Code (ISO 3166-1 alpha-2)           | Country of residence address; optional                                       | MUST            |
| address_stay.street_nr             | subject.address_stay[n].street_nr                      | String                              | Street and number of stay address; optional                                  | MUST            |
| address_stay.town                  | subject.address_stay[n].town                           | String                              | Town of stay address; optional                                               | MUST            |
| address_stay.post_code             | subject.address_stay[n].post_code                      | String                              | Postal code of stay address; optional                                        | MUST            |
| address_stay.country_code          | subject.address_stay[n].country_code                   | Code (ISO 3166-1 alpha-2)           | Country of stay address; optional                                            | MUST            |
| **Assignment Related Information** |                                                        |                                     |                                                                              |                 |
| home_member_state                  | assignment_info.home_member_state                      | Code (ISO 3166-1 alpha-2)           | Home member state from which the worker is posted; mandatory                 | MUST            |
| starting_date                      | assignment_info.starting_date                          | String (ISO 8601 YYYY-MM-DD)        | Start date of the posting assignment; mandatory                              | MUST            |
| ending_date                        | assignment_info.ending_date                            | String (ISO 8601 YYYY-MM-DD)        | End date of the posting assignment; mandatory                                | MUST            |
| applies_for_duration               | assignment_info.applies_for_duration                   | Boolean                             | True if applies for full duration; optional                                  | MUST            |
| determination_provisional          | assignment_info.determination_provisional              | Boolean                             | True if determination is provisional; optional                               | MUST            |
| transitional_rules                 | assignment_info.transitional_rules                     | Boolean                             | True if transitional rules apply; optional                                   | MUST            |
| **Home Employer**                  |                                                        |                                     |                                                                              |                 |
| home_employer.company_name         | home_employer.company_name                             | String                              | Full commercial name of the home employer; mandatory                         | MUST            |
| home_employer.industry_sector_nace | home_employer.industry_sector_nace                     | String                              | Industry sector (NACE); mandatory                                            | MUST            |
| home_employer.construction_sector  | home_employer.construction_sector                      | Boolean                             | True if construction sector; mandatory                                       | MUST            |
| home_employer.vat_id               | home_employer.vat_id                                   | String                              | VAT identification number; mandatory                                         | MUST            |
| home_employer.address_line_1       | home_employer.address_line_1                           | String                              | Primary address line; mandatory                                              | MUST            |
| home_employer.address_line_2       | home_employer.address_line_2                           | String                              | Secondary address line; optional                                             | MUST            |
| home_employer.postal_code          | home_employer.postal_code                              | String                              | Postal code; mandatory                                                       | MUST            |
| home_employer.city                 | home_employer.city                                     | String                              | City; mandatory                                                              | MUST            |
| home_employer.municipality         | home_employer.municipality                             | String                              | Municipality; optional                                                       | MUST            |
| home_employer.state                | home_employer.state                                    | String                              | State or region; optional                                                    | MUST            |
| home_employer.country              | home_employer.country                                  | Code (ISO 3166-1 alpha-2)           | Country of headquarters; mandatory                                           | MUST            |
| home_employer.phone                | home_employer.phone                                    | String                              | Phone number; mandatory                                                      | MUST            |
| home_employer.email                | home_employer.email                                    | String                              | Email address; mandatory                                                     | MUST            |
| admin_rep.last_name                | home_employer.administrative_representative.last_name  | String                              | Last name of administrative representative; mandatory                        | MUST            |
| admin_rep.first_name               | home_employer.administrative_representative.first_name | String                              | First name of administrative representative; mandatory                       | MUST            |
| admin_rep.telephone                | home_employer.administrative_representative.telephone  | String                              | Telephone of administrative representative; mandatory                        | MUST            |
| admin_rep.email                    | home_employer.administrative_representative.email      | String                              | Email of administrative representative; mandatory                            | MUST            |
| admin_rep.city                     | home_employer.administrative_representative.city       | String                              | City of administrative representative; mandatory                             | MUST            |
| admin_rep.country                  | home_employer.administrative_representative.country    | Code (ISO 3166-1 alpha-2)           | Country of administrative representative; mandatory (NL for NL PWN)          | MUST            |
| social_rep.last_name               | home_employer.social_representative.last_name          | String                              | Last name of social representative; mandatory                                | MUST            |
| social_rep.first_name              | home_employer.social_representative.first_name         | String                              | First name of social representative; mandatory                               | MUST            |
| social_rep.telephone               | home_employer.social_representative.telephone          | String                              | Telephone of social representative; mandatory                                | MUST            |
| social_rep.email                   | home_employer.social_representative.email              | String                              | Email of social representative; mandatory                                    | MUST            |
| social_rep.city                    | home_employer.social_representative.city               | String                              | City of social representative; mandatory                                     | MUST            |
| social_rep.country                 | home_employer.social_representative.country            | Code (ISO 3166-1 alpha-2)           | Country of social representative; mandatory                                  | MUST            |
| **Host Company**                   |                                                        |                                     |                                                                              |                 |
| host_company.company_name          | host_company.company_name                              | String                              | Full commercial name of host company; mandatory                              | MUST            |
| host_company.email                 | host_company.email                                     | String                              | Email address of host company; mandatory                                     | MUST            |
| host_company.telephone             | host_company.telephone                                 | String                              | Telephone number of host company; mandatory                                  | MUST            |
| host_company.industry_sector       | host_company.industry_sector                           | String                              | Industry sector of host company; mandatory                                   | MUST            |
| host_company.vat_id                | host_company.vat_id                                    | String                              | VAT identification number of host company; mandatory                         | MUST            |
| host_company.address_line_1        | host_company.address_line_1                            | String                              | Primary address line of host company; mandatory                              | MUST            |
| host_company.address_line_2        | host_company.address_line_2                            | String                              | Secondary address line; optional                                             | MUST            |
| host_company.postal_code           | host_company.postal_code                               | String                              | Postal code of host company; mandatory                                       | MUST            |
| host_company.city                  | host_company.city                                      | String                              | City of host company; mandatory                                              | MUST            |
| host_company.municipality          | host_company.municipality                              | String                              | Municipality of host company; optional                                       | MUST            |
| host_company.state                 | host_company.state                                     | String                              | State or region of host company; optional                                    | MUST            |
| host_company.country               | host_company.country                                   | Code (ISO 3166-1 alpha-2)           | Country of host company; mandatory                                           | MUST            |
| host_company.business_reg_nr       | host_company.business_reg_nr                           | String                              | Business registration number; optional                                       | MUST            |
| **Employee**                       |                                                        |                                     |                                                                              |                 |
| employee.job_duties_abroad         | employee.job_duties_abroad                             | String                              | Job duties and activities to be performed abroad; mandatory                  | MUST            |
| employee.a1_certificate_applied    | employee.a1_certificate_applied                        | Boolean                             | Whether A1 has been applied for; mandatory for NL PWN                        | MUST            |
| employee.a1_country_of_issuance    | employee.a1_country_of_issuance                        | Code (ISO 3166-1 alpha-2)           | Country of A1 issuance; optional                                             | MAY             |
| employee.a1_country_where_applied  | employee.a1_country_where_applied                      | Code (ISO 3166-1 alpha-2)           | Country where A1 was applied for; optional                                   | MAY             |
| employee.third_country_national    | employee.third_country_national                        | Boolean                             | Whether employee is a third-country national; optional                       | MAY             |
| employee.work_permit_end_date      | employee.work_permit_end_date                          | String (ISO 8601 YYYY-MM-DD)        | End date of work permit issued by sending country; optional                  | MAY             |
| **Places of Work**                 |                                                        |                                     |                                                                              |                 |
| no_fixed_place.country_code        | places_of_work[n].no_fixed_place.country_code          | Code (ISO 3166-1 alpha-2)           | Country for no fixed place of work; mandatory if no_fixed_place present      | MUST            |
| place_of_work.company_name         | places_of_work[n].place_of_work.company_name           | String                              | Name of company at place of work; mandatory if place_of_work present         | MUST            |
| place_of_work.flag_base_home       | places_of_work[n].place_of_work.flag_base_home         | String                              | Flag, base or home state of vessel; optional                                 | MUST            |
| place_of_work.company_id           | places_of_work[n].place_of_work.company_id             | String                              | Company identifier at place of work; optional                                | MUST            |
| place_of_work.id_type              | places_of_work[n].place_of_work.id_type                | Code                                | Type of company identifier; optional                                         | MUST            |
| place_of_work.street_nr            | places_of_work[n].place_of_work.street_nr              | String                              | Street and number of place of work; optional                                 | MUST            |
| place_of_work.town                 | places_of_work[n].place_of_work.town                   | String                              | Town of place of work; mandatory if place_of_work present                    | MUST            |
| place_of_work.postal_code          | places_of_work[n].place_of_work.postal_code            | String                              | Postal code of place of work; optional                                       | MUST            |
| place_of_work.country_code         | places_of_work[n].place_of_work.country_code           | Code (ISO 3166-1 alpha-2)           | Country of place of work; mandatory if place_of_work present                 | MUST            |
| **Competent Institution**          |                                                        |                                     |                                                                              |                 |
| institution_id                     | institution.institution_id                             | String                              | Identifier of the competent institution; mandatory                           | MUST            |
| institution_name                   | institution.institution_name                           | String                              | Name of the competent institution; mandatory                                 | MUST            |
| institution.country_code           | institution.country_code                               | Code (ISO 3166-1 alpha-2)           | Country of the competent institution; mandatory                              | MUST            |
| institution.fax                    | institution.fax                                        | String                              | Office fax number; optional                                                  | MUST            |
| institution.phone                  | institution.phone                                      | String                              | Office phone number; optional                                                | MUST            |
| institution.email                  | institution.email                                      | String                              | Email address of institution; optional                                       | MUST            |
| institution.street_nr              | institution.street_nr                                  | String                              | Street and number of institution address; optional                           | MUST            |
| institution.town                   | institution.town                                       | String                              | Town of institution address; optional                                        | MUST            |
| institution.postal_code            | institution.postal_code                                | String                              | Postal code of institution address; optional                                 | MUST            |
| institution.country_code_address   | institution.country_code_address                       | Code (ISO 3166-1 alpha-2)           | Country of institution address; optional                                     | MUST            |
| **Metadata**                       |                                                        |                                     |                                                                              |                 |
| issuance_date                      | iat                                                    | Number (Unix timestamp)             | Date and time when the attestation was issued (ISO 8601); RFC 7519           | MUST NOT        |
| expiry_date                        | exp                                                    | Number (Unix timestamp)             | Date and time when the attestation expires (ISO 8601); RFC 7519              | MUST NOT        |
| issuing_entity                     | iss                                                    | String (URI or DID)                 | Identifier of the entity that issued the attestation; RFC 7519               | MUST NOT        |
| attestation_legal_category         | attestation_legal_category                             | String                              | One of "EAA" or "QEAA" as defined by eIDAS 2                                 | MUST NOT        |
| vct                                | vct                                                    | String                              | "PWNCredential"                                                              | MUST NOT        |
| binding                            | binding                                                | String / tbd                        | Holder binding type (e.g., PID binding, Wallet Instance binding, no binding) | MUST NOT        |
| schema_version                     | schema_version                                         | String                              | Version of the schema used; optional                                         | MAY             |
| trust_anchor_url                   | trust_anchor_url                                       | String (URI)                        | URL where the trust anchor can be retrieved; optional                        | MAY             |

**Notes:**

- **MUST**: The claim **SHALL** be selectively disclosable — the holder **MAY** choose to
  disclose or withhold this claim when presenting the credential to a Relying Party.
- **MAY**: The claim **MAY** be selectively disclosable if the issuer supports it.
- **MUST NOT**: The claim **SHALL NOT** be selectively disclosable — it is always present in
  plain text in the JWT header/payload.
- `iat`, `exp`, and `iss` follow RFC 7519 standard JWT claim naming conventions.
- Home employer blocks **SHALL** be disclosed as a whole when requested.

#### 3.2.2 Status Claim

For SD-JWT VC-compliant PWN Attestations, the attestation **MUST** include a `status` claim if
the technical validity period is greater than 24 hours.

The `status` claim **SHALL** be a JSON object with the following members:

- `type` (string): **SHALL** be `"status-list"`.
- `status_list_credential` (string, URI): The URI of the Status List Credential document.
- `status_list_index` (integer, >= 0): The zero-based index into the status list bitstring.
- `status_purpose` (string): **SHALL** be `"revocation"` for this attestation.

**Example:**

```json
{
  "status": {
 "type": "status-list",
 "status_list_credential": "https://issuer.example.com/status/pwn/2025",
 "status_list_index": 321,
 "status_purpose": "revocation"
  }
}
```
3.2.3 Example Payload

The following is a non-normative example of a PWN SD-JWT VC payload (Spain PWN):
```
{
  "vct": "PWNCredential",
  "attestation_legal_category": "EAA",
  "iss": "did:example:example-gmbh-de",
  "iat": 1746000000,
  "exp": 1777536000,
  "jti": "pwn-attestation-20260501-001",
  "binding": "PID binding",
  "subject": {
    "pin": "12345678A",
    "family_name": "Müller",
    "forename": "Hans",
    "date_of_birth": "1985-06-15",
    "nationality": ["DE"],
    "job_title_home_country": "Software Engineer",
    "address_residence": {
      "street_nr": "Hauptstrasse 5",
      "town": "Berlin",
      "post_code": "10115",
      "country_code": "DE"
    }
  },
  "assignment_info": {
    "home_member_state": "DE",
    "starting_date": "2026-06-01",
    "ending_date": "2026-12-31",
    "applies_for_duration": false,
    "determination_provisional": false,
    "transitional_rules": false
  },
  "home_employer": {
    "company_name": "Example GmbH",
    "industry_sector_nace": "J62.01",
    "construction_sector": false,
    "vat_id": "DE123456789",
    "address_line_1": "Industriestrasse 20",
    "postal_code": "60311",
    "city": "Frankfurt",
    "country": "DE",
    "phone": "+49 69 123456",
    "email": "hr@example-gmbh.de",
    "administrative_representative": {
      "last_name": "Schmidt",
      "first_name": "Anna",
      "telephone": "+49 69 123457",
      "email": "anna.schmidt@example-gmbh.de",
      "city": "Frankfurt",
      "country": "DE"
    },
    "social_representative": {
      "last_name": "Weber",
      "first_name": "Klaus",
      "telephone": "+49 69 123458",
      "email": "klaus.weber@example-gmbh.de",
      "city": "Frankfurt",
      "country": "DE"
    }
  },
  "host_company": {
    "company_name": "Client SA",
    "email": "contact@client-sa.es",
    "telephone": "+34 91 123456",
    "industry_sector": "IT Services",
    "vat_id": "ES-B12345678",
    "address_line_1": "Calle Mayor 10",
    "postal_code": "28001",
    "city": "Madrid",
    "country": "ES"
  },
  "employee": {
    "job_duties_abroad": "Software development and technical consulting for client project"
  },
  "places_of_work": [
    {
      "place_of_work": {
        "company_name": "Client SA",
        "street_nr": "Calle Mayor 10",
        "town": "Madrid",
        "postal_code": "28001",
        "country_code": "ES"
      }
    }
  ],
  "institution": {
    "institution_id": "DE-DRV-001",
    "institution_name": "Deutsche Rentenversicherung Bund",
    "country_code": "DE"
  },
  "status": {
    "type": "status-list",
    "status_list_credential": "https://example.com/status/pwn-list-1",
    "status_list_index": 321,
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

Sample payloads are provided under ../data-schemas/sd-jwt/sample-data/pwn-sd-jwt-sample.json

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
