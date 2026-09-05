# Attestation Rulebook for attestations of type Portable Document A1 (PD A1)

* Author(s):
  * [Philipp Friedl, DRV Bund]
  * [Artur Philipp, DRV Bund]
  * Laurent ?
* Previous Authors
*
* Reviewer(s):
  * [Florin Coptil, Robert Bosch GmbH]
  * [Artur Philipp, DRV Bund]

| Version | Date       | Description                                                     |
|---------|------------|-----------------------------------------------------------------|
| 0.1     | 01.05.2026 | Initial draft based on the WeBuild design attestations meetings |

* Contact:
  * [Philipp Friedl - DRV Bund](mailto:philipp.friedl@drv-bund.de)

* Feedback:

---

## 1 Introduction

This attestation addresses the following question:

**Which social security legislation applies to a citizen working in a cross-border employment situation within the EU/EFTA area (or UK)?**

The Portable Document A1 (PD A1) is a certificate that documents the applicable legislation
regarding social security for a citizen in a cross-border employment situation. By determining
that only one legislation applies, it supports the mobility of working citizens while protecting
their rights (by ensuring coverage while avoiding dual contributions).

In the most common "posting" situation, where a person works abroad for a maximum of 24 months, the PD A1 is issued by the competent social security institution from the "sending state" upon request by the employer or the self-employed person. It is then used for verification abroad in the "receiving state".

The **Know Your Employee (KYE)** scenario (Scenario 5) is part of BU1 and will lead to MVP
and MVP+ implementations using both Natural Person Wallets and Legal Person Wallets. The
high-level scenario is:

> *"A company A in a country A would like to send one of their employees to work and provide
> a service to company B in country B."*

This scenario requires the issuance of three main credentials:
- **Portable Document (PD) A1**
- **Posted Worker Notification (PWN)**
- **Employee Credential**

### 1.1 Document Scope and Purpose

The PD A1 Attestation provides a standardized, verifiable digital representation of the
Portable Document A1. The main legal basis is:
- **Regulation (EC) No. 883/2004** on the coordination of social security systems
  (especially Articles 11–16)
- **Regulation (EC) No. 987/2009** — implementing regulation
- National legislation regarding social security in EU/EFTA member states (and the United Kingdom)

**Design Decisions**

This PD A1 Attestation Rulebook is based on:
- The EU-wide legally defined content of the Portable Document A1 as issued by competent social
  security institutions
- Regulation (EC) No. 883/2004 and Regulation (EC) No. 987/2009 as the primary legal
  framework
- EESSI (Electronic Exchange of Social Security Information) code tables, e.g. for employment
  type and institution identifiers
- ISO 3166-1 alpha-2 for country codes (mostly EU/EFTA countries + UK = 32 countries)
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
| PD A1                  | Portable Document A1 — a certificate documenting the applicable social security legislation for a citizen in a cross-border employment situation within the EU/EFTA area (and UK)                         |
| Posted Worker          | A citizen employed in one EU/EFTA member state ("sending state") who is temporarily sent to work in another member state ("receiving state") for a maximum of 24 months                         |
| Sending State          | The EU/EFTA member state whose social security legislation remains applicable to the posted worker during the posting period                                                                      |
| Receiving State        | The EU/EFTA member state where the posted worker temporarily performs work                                                                                                                       |
| Competent Institution  | The national social security institution of the sending state authorized to issue the PD A1 certificate                                                                                          |
| PIN                    | Personal Identification Number — currently mostly a Social Security Number of the citizen                                                                                                             |
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

This chapter describes the PD A1 credential attributes as defined in the v1.0 PD A1 JSON schema. All field names, types, enumerations, and constraints in Sections 2.2–2.9 are derived strictly from that schema. The normative source is the schema file [`pda1-sd-jwt.json`](../../data-schemas/sd-jwt/pda1-sd-jwt.json).

### 2.1 Introduction

**Data Model (v1.0):**

```
PDA1 Credential
├── subject [1:1]
│   ├── pin (string) — mandatory | SD Group 1
│   ├── gender (enum "0"/"1"/"2") — mandatory | SD Group 2
│   ├── names [1:1] — mandatory | SD Group 3
│   │   ├── surnames (string) — mandatory | SD Group 3
│   │   ├── forenames (string) — mandatory | SD Group 3
│   │   ├── surnameAtBirth (string) — optional | SD Group 3
│   │   └── forenamesAtBirth (string) — optional | SD Group 3
│   ├── dateOfBirth (date, YYYY-MM-DD) — mandatory | SD Group 4
│   ├── nationalities (array ≥ 1, world codes, unique) — mandatory | SD Group 5
│   ├── placeOfBirth [1:1] — mandatory | SD Group 6
│   │   ├── town (string) — mandatory | SD Group 6
│   │   └── countryCode (world code) — mandatory | SD Group 6
│   └── address [1:1] — mandatory | SD Groups 7–8
│       ├── stateOfResidence[] (addressWorld) — optional | SD Group 7
│       └── stateOfStay[] (addressPDA1State) — optional | SD Group 8
│       [anyOf: at least one non-empty list required]
├── memberstateAppliedLegislation [1:1] — Non-SD (always disclosed)
│   ├── memberstate (PDA1 code) — mandatory
│   ├── startDate (date) — mandatory
│   ├── endDate (date) — mandatory
│   ├── certificateAppliesForDuranceOfStay (boolean) — optional
│   ├── determinationIsProvisional (boolean) — optional
│   └── transitionRulesApplyAccordingEG (boolean) — optional
├── employmentSituations [1:n] — SD Groups 9–10
│   └── [each item:]
│       ├── typeOfEmployment (enum "01"/"02") — mandatory | SD Group 9
│       ├── name (string) — mandatory | SD Group 9
│       ├── employerID (string) — mandatory | SD Group 9
│       ├── typeOfID (enum) — mandatory | SD Group 9
│       └── address (addressWorld) — mandatory | SD Group 10
├── placesOfWork {<PDA1 countryCode>: [placeOfWork]} [≥ 1 key] — SD Groups 11–12
│   └── [each array item:]
│       ├── companyOrVesselName (string) — mandatory | SD Group 11
│       ├── flagBaseHomeState (string) — optional | SD Group 11
│       ├── companyID (string) — optional† | SD Group 11
│       ├── typeOfID (enum) — optional† | SD Group 11
│       └── address (addressPDA1State) — mandatory | SD Group 12
│       [† companyID and typeOfID are mutually required]
│       [empty array = works in that country with no fixed address]
├── statusConfirmation [1:1] — SD Group 13
│   ├── statusConfirmationCode (enum, 12 codes) — mandatory | SD Group 13
│   └── exceptionDescription (string) — conditional‡ | SD Group 13
│       [‡ only permitted when statusConfirmationCode = "11"]
├── documentID (string) [1:1] — SD Group 14
└── competentInstitution [1:1] — SD Groups 15–16
    ├── institutionID (string) — mandatory | SD Group 15
    ├── institutionName (string) — mandatory | SD Group 15
    ├── countryCode (PDA1 code) — mandatory | SD Group 15
    ├── address (addressPDA1State) — mandatory | SD Group 16
    ├── officeFaxNumber (E.164 string) — optional | SD Group 16
    ├── officePhoneNumber (E.164 string) — optional | SD Group 16
    └── email (string) — optional | SD Group 16
```

**Selective Disclosure:** SD is applied at element-group level — individual fields within a group are not independently selectable. `memberstateAppliedLegislation` is Non-SD and is always fully disclosed to the Relying Party.

**Attestation Classification** *(contextual — not a schema element):* This attestation MAY be classified as **QEAA**, **PuB-EAA**, or **EAA** depending on the issuing institution's qualification status under eIDAS 2.0.

---

### 2.2 Definitions

The following shared types are defined in `$defs` of the v1.0 schema and referenced throughout Sections 2.3–2.9.

#### `gender`

ISO/IEC 5218 gender code (string enum): `"0"` = Not known / Not specified · `"1"` = Male · `"2"` = Female.

#### `addressBase`

Base postal address object:

| Data Identifier | Definition | Data type | Occurrence |
|----------------|-----------|-----------|------------|
| `streetAndNumber` | Street name and house or building number | String | 0:1 |
| `town` | Name of the city or town | String | 1:1 |
| `postcode` | Postal code (format varies by country) | String | 0:1 |

#### `addressPDA1State`

Postal address restricted to a PDA1-participating country. Extends `addressBase` with:

| Data Identifier | Definition | Data type | Occurrence |
|----------------|-----------|-----------|------------|
| `countryCode` | Country of the address (PDA1 set) | countryCodePDA1States | 1:1 |

No additional properties permitted (`unevaluatedProperties: false`).

#### `addressWorld`

Postal address for any recognized country in the world. Extends `addressBase` with:

| Data Identifier | Definition | Data type | Occurrence |
|----------------|-----------|-----------|------------|
| `countryCode` | Country of the address (world set) | countryCodeWorld | 1:1 |

No additional properties permitted (`unevaluatedProperties: false`).

#### `phoneNumber`

Phone number in E.164 international format (e.g., `+4930123456`). Pattern: `^\+[1-9]\d{1,14}$`.

#### `email`

Email address conforming to RFC 5321/5322. Pattern: `^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$`.

#### `countryCodePDA1States`

ISO 3166-1 alpha-2 code restricted to the **32 PD A1-participating states**: the 27 EU member states (AT, BE, BG, CY, CZ, DE, DK, EE, ES, FI, FR, GR, HR, HU, IE, IT, LT, LU, LV, MT, NL, PL, PT, RO, SE, SI, SK) plus Iceland (IS), Liechtenstein (LI), Norway (NO), Great Britain (GB), and Switzerland (CH).

| **Data Identifier**        | **Semantic Reference** | **Definition**                                                                    | **Data type**          |
|----------------------------|------------------------|-----------------------------------------------------------------------------------|------------------------|
| subject                    | [person](https://w3id.org/ebwv#person) | Personal identity attributes of the citizen subject to the PD A1                 | Object                 |
| member_state_legislation   | [jurisdiction](https://w3id.org/ebwv#jurisdiction) | Details of the applicable member state legislation; always disclosed (Non-SD)     | Object                 |
| employer_details           | [employer](https://w3id.org/ebwv#employer) | Details of the employer(s) or self-employment situation                           | Array [EmployerObject] |
| places_of_work             | [placeOfWork](https://w3id.org/ebwv#placeOfWork) | Places where the posted worker performs work                                      | Array [PlaceOfWork]    |
| status_confirmation        | [statusConfirmation](https://w3id.org/ebwv#statusConfirmation) | Status confirmation code identifying the type of cross-border situation           | Object                 |
| document_id                | @id | Unique number of the issued PD A1 document                                        | Object                 |
| competent_institution      | [cred:issuer](https://w3.org/2018/credentials#issuer) | Details of the competent social security institution that issued the PD A1        | Object                 |

ISO 3166-1 alpha-2 code covering **195 world states**: the 193 United Nations member states plus the two UN observer states Holy See (VA) and State of Palestine (PS).

#### `date`

| **Data Identifier**            | **Semantic Reference** | **Definition**                                                                                          | **Data type**                   | **Occurrence** | **SD Group** |
|--------------------------------|------------------------|---------------------------------------------------------------------------------------------------------|---------------------------------|----------------|--------------|
| pin                            | [identifier](https://w3id.org/ebwv#identifier) | Personal Identification Number (currently Social Security Number) of the citizen                        | String                          | 1:1            | 1            |
| gender                         | [gender](https://w3id.org/ebwv#gender)| Gender of the citizen                                                                                   | String / Codelist (tbd)         | 1:1            | 2            |
| family_name                    | [familyName](https://w3id.org/ebwv#familyName)| Family name(s) of the citizen in full                                                                   | String                          | 1:1            | 3            |
| forename                       | [givenName](https://w3id.org/ebwv#givenName)| Forename(s) of the citizen in full                                                                      | String                          | 1:1            | 3            |
| date_of_birth                  | [dateOfBirth](https://w3id.org/ebwv#dateOfBirth)| Date of birth of the citizen (ISO 8601)                                                                 | Date (YYYY-MM-DD)               | 1:1            | 4            |
| nationality                    | [citizenship](https://w3id.org/ebwv#citizenship)| Nationality/ies of the citizen; Relying Party always requests all nationalities; user may select which  | Code [1:n] (ISO 3166-1 alpha-2) | 1:n            | 5            |
| place_of_birth.town            | [placeOfBirth](https://w3id.org/ebwv#placeOfBirth).[geographicName](https://w3id.org/ebwv#geographicName)| Town/locality where the citizen was born                                                                | String                          | 1:1            | 6            |
| place_of_birth.country_code    | [placeOfBirth](https://w3id.org/ebwv#placeOfBirth).[geographicIdentifier](https://w3id.org/ebwv#geographicIdentifier)| Country where the citizen was born (ISO 3166-1 alpha-2)                                                 | Code (ISO 3166-1 alpha-2)       | 1:1            | 6            |

#### `typeOfID`

Type of identifier used for an employer, self-employed entity, or company at a place of work:

| **Data Identifier**                 | **Semantic Reference** | **Definition**                                              | **Data type**             | **Occurrence** | **SD Group** |
|-------------------------------------|------------------------|-------------------------------------------------------------|---------------------------|----------------|--------------|
| address_residence.town              | [domicile](https://w3id.org/ebwv#domicile).[postName](https://w3id.org/ebwv#postName)| Town of the address in the state of residence               | String                    | 1:1            | 7            |
| address_residence.country_code      | [domicile](https://w3id.org/ebwv#domicile).[adminUnitL1](https://w3id.org/ebwv#adminUnitL1) | Country code of the state of residence (ISO 3166-1 alpha-2) | Code (ISO 3166-1 alpha-2) | 1:1            | 7            |

#### `statusConfirmationCode`

| **Data Identifier**         | **Semantic Reference** | **Definition**                                          | **Data type**             | **Occurrence** | **SD Group** |
|-----------------------------|------------------------|---------------------------------------------------------|---------------------------|----------------|--------------|
| address_stay.town           | [temporaryAddress](https://w3id.org/ebwv#temporaryAddress).[postName](https://w3id.org/ebwv#postName) | Town of the address in the state of stay                | String                    | 1:1            | 8            |
| address_stay.country_code   | [temporaryAddress](https://w3id.org/ebwv#temporaryAddress).[adminUnitL1](https://w3id.org/ebwv#adminUnitL1) | Country code of the state of stay (ISO 3166-1 alpha-2)  | Code (ISO 3166-1 alpha-2) | 1:1            | 8            |

| Code | Definition |
|------|-----------|
| `01` | Posted employed person |
| `02` | Employed, working in two or more States |
| `03` | Posted self-employed person |
| `04` | Self-employed, working in two or more States |
| `05` | Civil servant |
| `06` | Contract staff |
| `07` | Mariner |
| `08` | Working as an employed person and as a self-employed person in different States |
| `09` | Working as a civil servant in one State and as an employed/self-employed person in one or more other States |
| `10` | Flight or cabin crew member |
| `11` | Exception |
| `12` | Working as an employed / self-employed person in the State which legislation applies |

| **Data Identifier**                           | **Semantic Reference** | **Definition**                                                                                                | **Data type**             | **Occurrence** |
|-----------------------------------------------|------------------------|---------------------------------------------------------------------------------------------------------------|---------------------------|----------------|
| member_state_legislation.member_state         | [jurisdiction](https://w3id.org/ebwv#jurisdiction)  | Code of the member state whose legislation applies (ISO 3166-1 alpha-2; EU/EFTA + UK = 32 countries)          | Code (ISO 3166-1 alpha-2) | 1:1            |
| member_state_legislation.starting_date        | [cred:validFrom](https://w3.org/2018/credentials#validFrom) | Starting date from which the member state legislation applies (ISO 8601)                                       | Date (YYYY-MM-DD)         | 1:1            |
| member_state_legislation.ending_date          | [cred:validUntil](https://w3.org/2018/credentials#validUntil) | Ending date until which the member state legislation applies (ISO 8601)                                        | Date (YYYY-MM-DD)         | 1:1            |

Details of a single employer or self-employment activity. All five fields are required. No additional properties permitted (`additionalProperties: false`).

| **Data Identifier**             | **Semantic Reference** | **Definition**                                                                                 | **Data type**             | **Occurrence** | **SD Group** |
|---------------------------------|------------------------|------------------------------------------------------------------------------------------------|---------------------------|----------------|--------------|
| employer.employment_type        | [typeOfEmployment](https://w3id.org/ebwv#typeOfEmployment) | Type of employment: `01` = Employment, `02` = Self-Employment (EESSI codelist)                 | Code                      | 1:1            | 9            |
| employer.name                   | [legalName](https://w3id.org/ebwv#legalName) | Name of the employer or self-employed entity                                                   | String                    | 1:1            | 9            |
| employer.employer_id            | [legalIdentifier](https://w3id.org/ebwv#legalIdentifier) | Identifier of the employer                                                                     | String                    | 1:1            | 9            |
| employer.id_type                | N/A | Type of the employer identifier: `01`, `02`, `03`, `99` (see EESSI codelist — tbd)             | Code                      | 1:1            | 9            |
| employer.address.town           | [postName](https://w3id.org/ebwv#postName)  | Town of the employer's address                                                                 | String                    | 1:1            | 10           |
| employer.address.country_code   | [adminUnitL1](https://w3id.org/ebwv#adminUnitL1) | Country of the employer's address (ISO 3166-1 alpha-2)                                         | Code (ISO 3166-1 alpha-2) | 1:1            | 10           |

#### `placeOfWork`

When a specific place of work is declared:

| **Data Identifier**             | **Semantic Reference** | **Definition**                                                                            | **Data type**             | **Occurrence** | **SD Group** |
|---------------------------------|------------------------|-------------------------------------------------------------------------------------------|---------------------------|----------------|--------------|
| place_of_work.company_name      | [placeOfWork](https://w3id.org/ebwv#placeOfWork).[legalName](https://w3id.org/ebwv#legalName);[name](https://w3id.org/ebwv#name)  | Name of the company or vessel at the place of work                                        | String                    | 1:1            | 11           |
| place_of_work.town              | [placeOfWork](https://w3id.org/ebwv#placeOfWork).[postName](https://w3id.org/ebwv#postName) | Town of the place of work                                                                 | String                    | 1:1            | 12           |
| place_of_work.country_code      | [placeOfWork](https://w3id.org/ebwv#placeOfWork).[countryCode](https://w3id.org/ebwv#countryCode) | Country of the place of work (ISO 3166-1 alpha-2; EU/EFTA + UK)                           | Code (ISO 3166-1 alpha-2) | 1:1            | 12           |

When no fixed place of work exists:

| **Data Identifier**                   | **Semantic Reference** | **Definition**                                                                    | **Data type**             | **Occurrence** | **SD Group** |
|---------------------------------------|------------------------|-----------------------------------------------------------------------------------|---------------------------|----------------|--------------|
| no_fixed_place_of_work.country_code   | [noFixedPlaceOfWork](https://w3id.org/ebwv#noFixedPlaceOfWork) AND [placeOfWork](https://w3id.org/ebwv#placeOfWork).[countryCode](https://w3id.org/ebwv#countryCode)                      | Country code indicating the country where no fixed place of work exists           | Code (ISO 3166-1 alpha-2) | 1:1            | 11           |

| Data Identifier | Definition | Data type | Occurrence | SD Group |
|----------------|-----------|-----------|------------|----------|
| `companyOrVesselName` | Name of the company or vessel where work is performed | String | 1:1 | 11 |
| `flagBaseHomeState` | Flag state, base state, or home state for maritime or aviation workers | String | 0:1 | 11 |
| `companyID` | Identifier of the company at the place of work | String | 0:1† | 11 |
| `typeOfID` | Type of the company identifier (see `typeOfID` above) | typeOfID | 0:1† | 11 |
| `address` | Address of the place of work (PDA1 country) | addressPDA1State | 1:1 | 12 |

| **Data Identifier**          | **Semantic Reference** | **Definition**                                                                                                                              | **Data type** | **Occurrence** | **SD Group** |
|------------------------------|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|---------------|----------------|--------------|
| status_confirmation.status   | [statusConfirmation](https://w3id.org/ebwv#statusConfirmation) <br> presently xsd:boolean, needs to be changed to a code list (skos:Concept?)| Status confirmation code identifying the type of cross-border situation (2-digit code per PD A1 codelist; 12 options — tbd)                 | Code          | 1:1            | 13           |

---

### 2.3 Subject

Personal details of the PD A1 certificate holder. All seven top-level keys (`pin`, `gender`, `names`, `dateOfBirth`, `nationalities`, `placeOfBirth`, `address`) are required. No additional properties permitted (`additionalProperties: false`).

| Data Identifier | Definition | Data type | Occurrence | SD Group |
|----------------|-----------|-----------|------------|----------|
| `pin` | Personal Identification Number (social security number) of the holder | String | 1:1 | 1 |
| `gender` | Gender of the holder | gender | 1:1 | 2 |
| `names.surnames` | Current family name(s) of the holder | String | 1:1 | 3 |
| `names.forenames` | Current given name(s) of the holder | String | 1:1 | 3 |
| `names.surnameAtBirth` | Family name at birth, if different from current surname | String | 0:1 | 3 |
| `names.forenamesAtBirth` | Given name(s) at birth, if different from current forename(s) | String | 0:1 | 3 |
| `dateOfBirth` | Date of birth of the holder | date | 1:1 | 4 |
| `nationalities` | Nationality/ies of the holder as world-set country codes; at least one required, no duplicates | Array of countryCodeWorld (`minItems: 1`, `uniqueItems`) | 1:n | 5 |
| `placeOfBirth.town` | Town or city of birth | String | 1:1 | 6 |
| `placeOfBirth.countryCode` | Country of birth (world set) | countryCodeWorld | 1:1 | 6 |
| `address.stateOfResidence[]` | Residence address(es); each item is a complete world address | Array of addressWorld | 0:n | 7 |
| `address.stateOfStay[]` | Stay address(es); each item is a complete PDA1-country address | Array of addressPDA1State | 0:n | 8 |

The `address` object MUST satisfy `anyOf`: either `stateOfResidence` is present with `minItems: 1`, or `stateOfStay` is present with `minItems: 1` (both MAY be present simultaneously). Only `stateOfResidence` and `stateOfStay` are permitted in `address` (`additionalProperties: false`). The `names` and `placeOfBirth` sub-objects also enforce `additionalProperties: false`.

---

### 2.4 Member State Legislation

The member state whose social security legislation applies to the holder. This section is annotated `$comment: "Always disclosed"` — it is **Non-SD** and is fully disclosed to the Relying Party in every presentation. No additional properties permitted (`additionalProperties: false`).

| Data Identifier | Definition | Data type | Occurrence | SD Group |
|----------------|-----------|-----------|------------|----------|
| `memberstate` | Country code of the member state whose legislation applies | countryCodePDA1States | 1:1 | Non-SD |
| `startDate` | Start date from which the member state legislation applies | date | 1:1 | Non-SD |
| `endDate` | End date until which the member state legislation applies | date | 1:1 | Non-SD |
| `certificateAppliesForDuranceOfStay` | Indicates whether the certificate applies for the entire duration of the stay | Boolean | 0:1 | Non-SD |
| `determinationIsProvisional` | Indicates whether the determination of applicable legislation is provisional | Boolean | 0:1 | Non-SD |
| `transitionRulesApplyAccordingEG` | Indicates whether transitional rules apply according to EC Regulation No 883/2004 | Boolean | 0:1 | Non-SD |

| **Data Identifier**    | **Semantic Reference** | **Definition**                                 | **Data type** | **Occurrence** | **SD Group** |
|------------------------|------------------------|------------------------------------------------|---------------|----------------|--------------|
| document.document_id   | [identifier](https://w3id.org/ebwv#identifier) | Unique identifier of the issued PD A1 document | String        | 1:1            | 14           |

### 2.6 Places of Work

`placesOfWork` is a JSON **object** (not an array) whose property names are `countryCodePDA1States` values. At least one property must be present (`minProperties: 1`). Each property value is an **array** of `placeOfWork` objects (see §2.2). An **empty array** indicates the holder works in that country **with no fixed address**.

| Data Identifier | Definition | Data type | Occurrence | SD Group |
|----------------|-----------|-----------|------------|----------|
| `placesOfWork.<CC>` | Work-location entries for country `<CC>`; empty array = no fixed address in that country | Array of placeOfWork | 1:n countries | 11 |
| `placesOfWork.<CC>[].companyOrVesselName` | Name of the company or vessel where work is performed | String | 1:1 per item | 11 |
| `placesOfWork.<CC>[].flagBaseHomeState` | Flag state, base state, or home state (maritime or aviation workers) | String | 0:1 per item | 11 |
| `placesOfWork.<CC>[].companyID` | Identifier of the company at the place of work | String | 0:1† per item | 11 |
| `placesOfWork.<CC>[].typeOfID` | Type of the company identifier (see §2.2) | typeOfID | 0:1† per item | 11 |
| `placesOfWork.<CC>[].address.streetAndNumber` | Street name and house number of the place of work | String | 0:1 per item | 12 |
| `placesOfWork.<CC>[].address.town` | Town of the place of work | String | 1:1 per item | 12 |
| `placesOfWork.<CC>[].address.postcode` | Postal code of the place of work | String | 0:1 per item | 12 |
| `placesOfWork.<CC>[].address.countryCode` | Country of the place of work (PDA1 set) | countryCodePDA1States | 1:1 per item | 12 |

† `companyID` and `typeOfID` are co-dependent: if either is present, the other MUST also be present.

---

### 2.7 Status Confirmation

| **Data Identifier**             | **Semantic Reference** | **Definition**                                     | **Data type** | **Occurrence** | **SD Group** |
|---------------------------------|------------------------|----------------------------------------------------|---------------|----------------|--------------|
| address_residence.street_nr     | [domicile](https://w3id.org/ebwv#domicile).[thoroughfare](https://w3id.org/ebwv#thoroughfare) <br>and [locatorDesignator](https://w3id.org/ebwv#locatorDesignator) | Street and number of the residence address         | String        | 0:1            | 7            |
| address_residence.post_code     | [domicile](https://w3id.org/ebwv#domicile).[postCode](https://w3id.org/ebwv#postCode) | Postal code of the residence address               | String        | 0:1            | 7            |
| address_stay.street_nr          | [temporaryAddress](https://w3id.org/ebwv#temporaryAddress).[thoroughfare](https://w3id.org/ebwv#thoroughfare) <br>and [locatorDesignator](https://w3id.org/ebwv#locatorDesignator) | Street and number of the stay address              | String        | 0:1            | 8            |
| address_stay.post_code          | [temporaryAddress](https://w3id.org/ebwv#temporaryAddress).[postCode](https://w3id.org/ebwv#postCode) | Postal code of the stay address                    | String        | 0:1            | 8            |

| Data Identifier | Definition | Data type | Occurrence | SD Group |
|----------------|-----------|-----------|------------|----------|
| `statusConfirmation.statusConfirmationCode` | Status confirmation code (see §2.2) | statusConfirmationCode | 1:1 | 13 |
| `statusConfirmation.exceptionDescription` | Free-text description of the exception situation | String | 0:1‡ | 13 |

| **Data Identifier**                             | **Semantic Reference** | **Definition**                                                                         | **Data type** | **Occurrence** |
|-------------------------------------------------|------------------------|----------------------------------------------------------------------------------------|---------------|----------------|
| member_state_legislation.applies_for_duration   | [fullPeriodCovered](https://w3id.org/ebwv#fullPeriodCovered) <br> needs to be changed to "activityDurationCovered" | Indicates whether the certificate applies for the full duration of the activity        | Boolean       | 0:1            |
| member_state_legislation.provisional            | [provisionalDetermination](https://w3id.org/ebwv#provisionalDetermination) | Indicates whether the determination is provisional                                     | Boolean       | 0:1            |
| member_state_legislation.transitional_rules     | [transitionalRules](https://w3id.org/ebwv#transitionalRules) | Indicates whether transitional rules apply                                              | Boolean       | 0:1            |

---

| **Data Identifier**          | **Semantic Reference** | **Definition**                              | **Data type** | **Occurrence** | **SD Group** |
|------------------------------|------------------------|---------------------------------------------|---------------|----------------|--------------|
| employer.address.street_nr   | [employer](https://w3id.org/ebwv#employer).[registeredAddress](https://w3id.org/ebwv#registeredAddress).[thoroughfare](https://w3id.org/ebwv#thoroughfare) and [locatorDesignator](https://w3id.org/ebwv#locatorDesignator) | Street and number of the employer's address | String        | 0:1            | 10           |
| employer.address.post_code   | [employer](https://w3id.org/ebwv#employer).[registeredAddress](https://w3id.org/ebwv#registeredAddress).[postCode](https://w3id.org/ebwv#postCode) | Postal code of the employer's address       | String        | 0:1            | 10           |

`documentID` is a **top-level string** — the unique identifier of the issued PD A1 certificate.

| **Data Identifier**            | **Semantic Reference** | **Definition**                                                             | **Data type** | **Occurrence** | **SD Group** |
|--------------------------------|------------------------|----------------------------------------------------------------------------|---------------|----------------|--------------|
| place_of_work.flag_base_home   | [placeOfWork](https://w3id.org/ebwv#placeOfWork).[flagState](https://w3id.org/ebwv#flagState) | Flag, base or home state of the vessel (maritime use case)                 | String        | 0:1            | 11           |
| place_of_work.company_id       | [placeOfWork](https://w3id.org/ebwv#placeOfWork).[legalIdentifier](https://w3id.org/ebwv#legalIdentifier) | Identifier of the company at the place of work                             | String        | 0:1            | 11           |
| place_of_work.id_type          | —                      | Type of company identifier: `01`, `02`, `03`, `99` (EESSI codelist — tbd) | Code          | 0:1            | 11           |
| place_of_work.street_nr        | [placeOfWork](https://w3id.org/ebwv#placeOfWork).[registeredAddress](https://w3id.org/ebwv#registeredAddress).[thoroughfare](https://w3id.org/ebwv#thoroughfare) and [locationDesignator](https://w3id.org/ebwv#locationDesignator) | Street and number of the place of work                                     | String        | 0:1            | 12           |
| place_of_work.postal_code      | [placeOfWork](https://w3id.org/ebwv#placeOfWork).[registeredAddress](https://w3id.org/ebwv#registeredAddress).[postCode](https://w3id.org/ebwv#postCode) | Postal code of the place of work                                           | String        | 0:1            | 12           |

### 2.9 Competent Institution

| **Data Identifier**         | **Semantic Reference** | **Definition**                                                           | **Data type**             | **Occurrence** | **SD Group** |
|-----------------------------|------------------------|--------------------------------------------------------------------------|---------------------------|----------------|--------------|
| institution.fax             |               | Office fax number of the competent institution                           | String                    | 0:1            | 16           |
| institution.phone           | [PublicSectorBody](https://w3id.org/ebwv#PublicSectorBody).[hasTelephone](https://w3id.org/ebwv#hasTelephone)  | Office phone number of the competent institution                         | String                    | 0:1            | 16           |
| institution.email           | [PublicSectorBody](https://w3id.org/ebwv#PublicSectorBody).[hasEmail](https://w3id.org/ebwv#hasEmail) | Email address of the competent institution                               | String                    | 0:1            | 16           |
| institution.street_nr       | [PublicSectorBody](https://w3id.org/ebwv#PublicSectorBody).[registeredAddress](https://w3id.org/ebwv#registeredAddress).[thoroughfare](https://w3id.org/ebwv#thoroughfare) and [locatorDesignator](https://w3id.org/ebwv#locatorDesignator) | Street and number of the competent institution's address                 | String                    | 0:1            | 16           |
| institution.town            | [PublicSectorBody](https://w3id.org/ebwv#PublicSectorBody).[registeredAddress](https://w3id.org/ebwv#registeredAddress).[postName](https://w3id.org/ebwv#postName) | Town of the competent institution's address                              | String                    | 0:1            | 16           |
| institution.postal_code     | [PublicSectorBody](https://w3id.org/ebwv#PublicSectorBody).[registeredAddress](https://w3id.org/ebwv#registeredAddress).[postCode](https://w3id.org/ebwv#postCode) | Postal code of the competent institution's address                       | String                    | 0:1            | 16           |
| institution.country_code    | [PublicSectorBody](https://w3id.org/ebwv#PublicSectorBody).[registeredAddress](https://w3id.org/ebwv#registeredAddress).[adminUnitL1](https://w3id.org/ebwv#adminUnitL1)  | Country code of the competent institution's address (ISO 3166-1 alpha-2) | Code (ISO 3166-1 alpha-2) | 0:1            | 16           |

### 2.4 Conditional Attributes

No conditional attributes are defined for this attestation type. All attributes are either
mandatory or optional as specified above.

### 2.5 Mandatory Metadata

| **Data Identifier**          | **Semantic Reference** | **Definition**                                                                                                                                          | **Data type** |
|---------------------------|---|---------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| issuance_date              |[cred:validFrom](https://w3.org/2018/credentials#validFrom) | The date and time when the PD A1 Attestation was issued (ISO 8601)                                                                                      | DateTime      |
| expiry_date                |[cred:validUntil](https://w3.org/2018/credentials#validUntil) | The date and time when the PD A1 Attestation expires (ISO 8601); relation to business decision date tbd                                                 | DateTime      |
| issuing_entity             | [cred:issuer](https://w3.org/2018/credentials#issuer)  | The identifier of the competent social security institution that issued the attestation                                                                 | String        |
| attestation_legal_category  | [attestationLegalCategory](https://w3id.org/ebwv#attestationLegalCategory) | Indicates the legal category of this attestation ("QEAA" or "EAA")                                                                                      | String        |
| vct                       |    | A unique identifier (often a URL or URN) for the type of credential, indicating which claims must be present and which can be selectively disclosed      | String        |
| binding                    |   | Information on the holder binding type (e.g., PID binding, Wallet Instance binding, no binding)                                                         | String / tbd  |

### 2.6 Optional Metadata

| **Data Identifier** | **Semantic Reference** | **Definition**                                                             | **Data type** |
|------------------|---|----------------------------------------------------------------------------|---------------|
| trust_anchor_url  | [cred:termsOfUse](https://w3.org/2018/credentials#termsOfUse) | URL where the trust anchor for verifying this attestation can be retrieved | URI           |
| schema_version   |   | Version of the schema used for this attestation                            | String        |
| schema_id        |   | Schema identifier for the PD A1 credential schema (tbd)                   | String        |
| revocation       |   | Reference to revocation information for this attestation (tbd)            | String / tbd  |

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
| 01       | Identifier type 01 (tbd)   |
| 02       | Identifier type 02 (tbd)   |
| 03       | Identifier type 03 (tbd)   |
| 99       | Other / unspecified        |

#### 2.8.4 Status Confirmation Codes

The `status_confirmation` attribute **SHALL** use one of the following standardized 2-digit
values as defined in the PD A1 codelist (12 options — tbd):

| **Code** | **Definition**                                                                              |
|----------|---------------------------------------------------------------------------------------------|
| tbd      | 12 status confirmation codes per PD A1 specification (to be confirmed with EESSI)           |

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

### 2.10 Metadata

> **Note:** The attributes listed below are **not part of the v1.0 PD A1 attestation data schema**. They are defined at the encoding or framework layer (SD-JWT VC, eIDAS 2.0) and are subject to change as the encoding specification evolves.
>
> The separation is intentional: an application-data schema describes semantic content — field names, types, and constraints — which remains stable across encoding formats. Issuance and transport metadata, by contrast, is format- and infrastructure-specific (SD-JWT VC claim names, eIDAS 2.0 lifecycle attributes). Mixing them would couple a stable data definition to volatile infrastructure choices, and would prevent the schema from being reused across different encoding formats. Metadata attributes are therefore defined at the framework or protocol layer and referenced here for completeness only.

---

### 2.11 Integrity Rules

The following rules are derived strictly from constraints in the v1.0 PD A1 attestation data schema. Rules concerning metadata (§2.10) are marked as framework-layer.

**Top-level required properties:** All seven properties — `subject`, `memberstateAppliedLegislation`, `employmentSituations`, `placesOfWork`, `statusConfirmation`, `documentID`, `competentInstitution` — MUST be present. No additional top-level properties are permitted (`additionalProperties: false`).

**Date format:** All `date` values MUST conform to the format `YYYY-MM-DD` and match the pattern `^\d{4}-(?:(?:0[13578]|1[02])-(?:0[1-9]|[12]\d|3[01])|(?:0[469]|11)-(?:0[1-9]|[12]\d|30)|02-(?:0[1-9]|1\d|2[0-9]))$`.

**Country-code set — world (`countryCodeWorld`, 195 codes):** MUST be used for `subject.nationalities[]`, `subject.placeOfBirth.countryCode`, `subject.address.stateOfResidence[].countryCode`, and `employmentSituations[].address.countryCode`.

**Country-code set — PDA1 (`countryCodePDA1States`, 32 codes):** MUST be used for `memberstateAppliedLegislation.memberstate`, `subject.address.stateOfStay[].countryCode`, all property names (keys) of `placesOfWork`, `placesOfWork.<CC>[].address.countryCode`, `competentInstitution.countryCode`, and `competentInstitution.address.countryCode`.

**Nationalities:** `subject.nationalities` MUST contain at least one entry (`minItems: 1`) and MUST NOT contain duplicate codes (`uniqueItems: true`).

**Subject address:** `subject.address` MUST satisfy `anyOf` — either `stateOfResidence` is present with at least one item (`minItems: 1`), or `stateOfStay` is present with at least one item (`minItems: 1`); both MAY be present simultaneously. No properties other than `stateOfResidence` and `stateOfStay` are permitted in `subject.address` (`additionalProperties: false`).

**Employment situations:** `employmentSituations` MUST contain at least one item (`minItems: 1`). Each item MUST include all five required fields: `typeOfEmployment`, `name`, `employerID`, `typeOfID`, `address`. No additional properties are permitted per item (`additionalProperties: false`).

**Places of work:** `placesOfWork` MUST contain at least one country key (`minProperties: 1`). All property names MUST be valid `countryCodePDA1States` values. An empty array value is valid and means the holder works in that country with no fixed address. Each `placeOfWork` item MUST include `address` and `companyOrVesselName`. No additional properties are permitted per item (`additionalProperties: false`).

**Company ID co-dependency:** Within each `placeOfWork`, `companyID` and `typeOfID` are co-dependent (`dependentRequired`): if `companyID` is present then `typeOfID` MUST be present, and vice versa.

**Status exception:** `statusConfirmation.statusConfirmationCode` is required. `statusConfirmation.exceptionDescription` MUST NOT be present when `statusConfirmationCode` is any value other than `"11"`. It is optional even when the code is `"11"`.

**No extra properties:** The following objects enforce `additionalProperties: false` or `unevaluatedProperties: false` — no properties beyond those defined in the schema may appear in: `subject`, `subject.names`, `subject.placeOfBirth`, `subject.address`, `memberstateAppliedLegislation`, each `employmentSituation`, `addressPDA1State`, `addressWorld`, each `placeOfWork`, `statusConfirmation`, `competentInstitution`.

**Metadata integrity rules** *(framework-layer — not v1.0 schema):* `issuance_date` and `expiry_date` MUST be valid ISO 8601 DateTimes; `expiry_date` MUST be later than `issuance_date`; `attestation_legal_category` MUST be one of `"QEAA"`, `"PuB-EAA"`, or `"EAA"`; `vct` MUST be `eu.we-build.pda1.1`.

## 3 Attestation Encoding

This chapter defines how the PD A1 attestation is serialized into a concrete verifiable-attestation
format. It is important to keep two distinct layers apart:

- **Application data (semantic content).** The meaning of each attribute, its data type, and its
  allowed values or codelists are defined in **Chapter 2** and are encoding-independent. Chapter 2
  is the single source of truth for the data model.
- **Attestation encoding & envelope (metadata).** *This chapter.* It defines only how the Chapter 2
  application data is serialized into a concrete verifiable-attestation format (SD-JWT VC), together
  with the **envelope / metadata claims** that wrap the application data (issuer, validity,
  credential type, holder binding, revocation status). These claims live at the SD-JWT VC / eIDAS 2.0
  layer (see §2.10).

**This chapter does not repeat field meanings, data types, or value codelists — see Chapter 2 for
the data model.**

### 3.1 ISO/IEC 18013-5-Compliant Encoding

ISO/IEC 18013-5 (also called mdoc) is out of scope for this Rulebook, as specific aspects of offline proximity
presentation are not a current requirement for the PD A1 attestation.

### 3.2 SD-JWT VC-Based Encoding

The PD A1 attestation uses the SD-JWT VC format to allow for selective disclosure of citizen
and employment attributes based on SD element groups.

**Selective Disclosure:** Disclosure is applied at the **SD element group level**, not at the
individual field level. A Relying Party **SHALL** request disclosure of complete logical blocks
(e.g., a full address block, a full employment block); it is not possible to disclose partial
blocks (e.g., only the town from an address without the other address fields). The SD element group
membership of every application-data attribute is given by the **"SD Group" column in Chapter 2**
(§2.3–§2.9); those groupings are not restated here. In particular,
`memberstateAppliedLegislation` (§2.4) is **Non-SD** and is **always fully disclosed**.

The `.` notation is used to indicate the nesting of attributes.

**Verifiable Credential Type (`vct`):** `vct: eu.we-build.pda1.1`

#### 3.2.1 Envelope / Metadata Claims

The claims below form the SD-JWT VC **envelope** that wraps the Chapter 2 application data. They are
defined at the SD-JWT VC / eIDAS 2.0 layer and are **not part of the Chapter 2 application data**
(see §2.10). This table lists only envelope claims — application-data attributes, their data types,
and their codelists are defined in Chapter 2 and are not repeated here.

| **Claim**                    | **Encoding Format**       | **Reference / Notes**                                                                     | **Disclosable** |
|------------------------------|---------------------------|-------------------------------------------------------------------------------------------|-----------------|
| `vct`                        | String                    | Verifiable Credential Type; **SHALL** be `eu.we-build.pda1.1`                             | Non-SD          |
| `iss`                        | String (URI)              | Issuer identifier (the competent institution issuing the attestation); RFC 7519          | Non-SD          |
| `iat`                        | Number (Unix timestamp)   | Issuance time; RFC 7519                                                                   | Non-SD          |
| `exp`                        | Number (Unix timestamp)   | Expiry time; **MUST** be later than `iat`; RFC 7519                                       | Non-SD          |
| `jti`                        | String (URI)              | Unique JWT identifier for this attestation instance; RFC 7519                            | Non-SD          |
| `cnf`                        | JSON object (JWK / kid)   | Holder key-binding confirmation claim; RFC 7519                                           | Non-SD          |
| `attestation_legal_category` | String                    | eIDAS 2.0 legal category; one of `QEAA` / `PuB-EAA` / `EAA` (see §2.11)                   | Non-SD          |
| `binding`                    | String                    | Holder binding type (e.g., PID binding, Wallet Instance binding, no binding)             | Non-SD          |
| `status`                     | JSON object               | Revocation status via status list; see §3.2.2                                             | Non-SD          |
| `trust_anchor_url`           | String (URI)              | Optional. URL from which the trust anchor for verifying this attestation can be retrieved | MAY             |

**Notes:**

- These claims are defined at the SD-JWT VC / eIDAS 2.0 layer, **not** in the Chapter 2 application
  data, and describe the attestation container rather than its subject.
- Envelope claims are **always present in the envelope and are not selectively disclosable**
  (marked *Non-SD*), with the exception of `trust_anchor_url`, which is optional (`MAY`).
- `iss`, `iat`, `exp`, `jti`, and `cnf` are registered JWT claims and follow RFC 7519 naming
  conventions.
- The application-data attributes wrapped by this envelope, and their SD element group membership,
  are defined in Chapter 2 (§2.3–§2.9).

#### 3.2.2 Status Claim

PD A1 attestations are based on [SD-JWT-based Verifiable Digital Credentials (SD-JWT VC)](https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/16/). If a PD A1 attestation issued as an SD-JWT VC is meant to be valid for longer than 24 hours, the `status` claim as shown in [SD-JWT-based Verifiable Digital Credentials (SD-JWT VC)](https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/16/) and specified in [Token Status List (TSL)](https://datatracker.ietf.org/doc/draft-ietf-oauth-status-list/) MUST be used according to this rulebook. This claim enables Relying Parties to determine whether a credential has been revoked via a status list mechanism as specified in [Token Status List (TSL)](https://datatracker.ietf.org/doc/draft-ietf-oauth-status-list/).

While the [Token Status List (TSL)](https://datatracker.ietf.org/doc/draft-ietf-oauth-status-list/) specification only suggests that the status object of an SD-JWT VC (if present) SHOULD be checked, this rulebook prescribes (and therefore overrules) that the status object of an SD-JWT VC PD A1 attestation (if present) MUST always be checked by the verifying party.

The status object of a PD A1 attestation SD-JWT VC MUST contain the following members according to [Token Status List (TSL)](https://datatracker.ietf.org/doc/draft-ietf-oauth-status-list/):

```json
"status": {
    "status_list": {
      "idx": 0,
      "uri": "https://example.com/statuslists/1"
    }
  }
```

- `status`: OPTIONAL. The claim that references one or more mechanisms a relying party can use to look up status information about this credential. It's a container, and the specification allows different status mechanisms to sit inside it side by side.
- `status_list`: REQUIRED. The member identifying that the Token Status List mechanism is in use. It bundles together the two pieces of information needed to locate this credential's entry within a published status list. While the [Token Status List (TSL)](https://datatracker.ietf.org/doc/draft-ietf-oauth-status-list/) specification permits other status mechanisms to be used within the `status` claim, this rulebook prescribes that only the `status_list` mechanism MUST be used for PD A1 attestations if a status object is within the SD-JWT VC PD A1 attestation.
- `idx`: REQUIRED. The credential's assigned position in the status list. A relying party reads the bit(s) at this position to determine the credential's current status. It must be a non-negative integer.
- `uri`: REQUIRED. The address from which the Status List Token is retrieved. It must be a valid URI, and a relying party confirms it matches the `sub` claim of the fetched token before trusting the result.

For further details see [section 6.2. in Token Status List (TSL)](https://datatracker.ietf.org/doc/draft-ietf-oauth-status-list/).

The [Token Status List (TSL)](https://datatracker.ietf.org/doc/draft-ietf-oauth-status-list/) defines basic status types like `VALID`, `INVALID` and `SUSPENDED`. This rulebook limits the statuses allowed to be used for PD A1 SD-JWT VC attestations to only `VALID` and `INVALID`. Any status other than `VALID` or `INVALID` for a referenced VC is to be considered "not defined" and therefore MUST be treated as if the credential's status is `INVALID`.

### 3.2.3 Example Payload
A valid PD A1 JSON example is provided in [`pda1-sd-jwt-sample.json`](../../data-schemas/sd-jwt/sample-data/pda1-sd-jwt-sample.json).

## 4 Attestation usage

The PD A1 Attestation is a certificate that documents the applicable legislation regarding social security in a cross-border employment situation. It is mainly intended for verifying that a "posted worker" abroad is covered by the social security system of his "sending state"(home country) while temporarily working in a "receiving state". Based on an application by the "sending" employer, the PD A1 Attestation is issued by a competent social security institution of the "sending state".

**Typical usage scenarios include:**

- presentation by the posted worker to an official authority in the receiving state
- presentation by the posted worker towards an employer/contractor abroad
- presentation by the "posting" employer towards an employer/contractor abroad
- presentation by the "posting" employer (or an employer/contractor abroad) towards an official authority (abroad)
- offline or low-connectivity verification where the verifier can at least validate the credential signature, issuer, validity period, and disclosed PD A1 data without necessarily relying on an available real-time backend

**Verification contexts** include labour inspections, social security inspections, employee-to-employer/contractor, employer-to-employer interactions and administrative procedures.
A Relying Party receiving the attestation SHALL verify:
- the issuer signature;
- the SD-JWT VC type (vct);
- the issuer authorisation to issue PD A1 Attestation;
- the credential validity period;
- the credential status, where a status mechanism is present;
- holder binding, where used;
- the integrity rules defined in Section 2.9;

In EUDI Wallet related usage scenarios, the Relying Party SHOULD request and verify PID or another accepted identity credential - or compare the PD A1 subject data with other identification means - to verify that it matches the affected person. In such cases, the Relying Party SHOULD compare the relevant identity attributes with the PD A1 Attestation. The Relying Party SHALL apply data minimisation and SHALL request only the attributes required for their specific purposes.

Unlike many identity-related attestations, a PD A1 Attestation MAY legitimately be presented by different actors or wallets, i.e. EUDI or EBW, depending on the business process.

As the PD A1 Attestation is not only relevant for usage by the citizen but also by the applying employer and also in specific "transfer" scenarios, any holder binding MUST be handled in a flexible way, based on the intended usage and a decision taken during issuance:
- The attestation MAY have no specific binding at all;
- The Attestation MAY be device-bound through holder binding where supported by the EUDI Wallet and the applicable SD-JWT VC profile;
- The attestation MAY be cryptographically bound to a PID or another accepted identity attestation where the usage requires stronger identity matching. Where this binding is used, the metadata attribute cryptographically_bound_to SHOULD contain: urn:eudi:pid:1

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
