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

#### `countryCodeWorld`

ISO 3166-1 alpha-2 code covering **195 world states**: the 193 United Nations member states plus the two UN observer states Holy See (VA) and State of Palestine (PS).

#### `date`

ISO 8601 full date in `YYYY-MM-DD` format. Pattern: `^\d{4}-(?:(?:0[13578]|1[02])-(?:0[1-9]|[12]\d|3[01])|(?:0[469]|11)-(?:0[1-9]|[12]\d|30)|02-(?:0[1-9]|1\d|2[0-9]))$`.

#### `typeOfID`

Type of identifier used for an employer, self-employed entity, or company at a place of work:

| Code | Definition |
|------|-----------|
| `01` | Identification / Registration |
| `02` | Social Security |
| `03` | Fiscal |
| `98` | Unknown |

#### `statusConfirmationCode`

Confirmation of the situation on which applicable legislation is determined (12 codes):

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

#### `employmentSituation`

Details of a single employer or self-employment activity. All five fields are required. No additional properties permitted (`additionalProperties: false`).

| Data Identifier | Definition | Data type | Occurrence | SD Group |
|----------------|-----------|-----------|------------|----------|
| `typeOfEmployment` | Type of employment: `01` = Employee, `02` = Self-employed | enum | 1:1 | 9 |
| `name` | Name of the employer or self-employed entity | String | 1:1 | 9 |
| `employerID` | Identifier of the employer or self-employed entity | String | 1:1 | 9 |
| `typeOfID` | Type of the employer identifier (see `typeOfID` above) | typeOfID | 1:1 | 9 |
| `address` | Address of the employer or self-employed entity (any world country) | addressWorld | 1:1 | 10 |

#### `placeOfWork`

A fixed company address or vessel where the holder performs work. `address` and `companyOrVesselName` are required; `companyID` and `typeOfID` are co-dependent (see below). No additional properties permitted (`additionalProperties: false`).

| Data Identifier | Definition | Data type | Occurrence | SD Group |
|----------------|-----------|-----------|------------|----------|
| `companyOrVesselName` | Name of the company or vessel where work is performed | String | 1:1 | 11 |
| `flagBaseHomeState` | Flag state, base state, or home state for maritime or aviation workers | String | 0:1 | 11 |
| `companyID` | Identifier of the company at the place of work | String | 0:1† | 11 |
| `typeOfID` | Type of the company identifier (see `typeOfID` above) | typeOfID | 0:1† | 11 |
| `address` | Address of the place of work (PDA1 country) | addressPDA1State | 1:1 | 12 |

† `companyID` and `typeOfID` are co-dependent (`dependentRequired`): if either is present the other MUST also be present.

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

---

### 2.5 Employer / Self-Employment Details

`employmentSituations` is an array of `employmentSituation` objects (see §2.2). At least one item is required (`minItems: 1`). Each item's fields are listed below with their SD group annotations.

| Data Identifier | Definition | Data type | Occurrence | SD Group |
|----------------|-----------|-----------|------------|----------|
| `employmentSituations[].typeOfEmployment` | Type of employment: `01` = Employee, `02` = Self-employed | enum | 1:1 per item | 9 |
| `employmentSituations[].name` | Name of the employer or self-employed entity | String | 1:1 per item | 9 |
| `employmentSituations[].employerID` | Identifier of the employer or self-employed entity | String | 1:1 per item | 9 |
| `employmentSituations[].typeOfID` | Type of employer identifier (see §2.2) | typeOfID | 1:1 per item | 9 |
| `employmentSituations[].address.streetAndNumber` | Street name and house number of the employer | String | 0:1 per item | 10 |
| `employmentSituations[].address.town` | Town of the employer's address | String | 1:1 per item | 10 |
| `employmentSituations[].address.postcode` | Postal code of the employer's address | String | 0:1 per item | 10 |
| `employmentSituations[].address.countryCode` | Country of the employer's address (world set) | countryCodeWorld | 1:1 per item | 10 |

---

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

Confirmation of the situation on which applicable legislation is determined. No additional properties permitted (`additionalProperties: false`).

| Data Identifier | Definition | Data type | Occurrence | SD Group |
|----------------|-----------|-----------|------------|----------|
| `statusConfirmation.statusConfirmationCode` | Status confirmation code (see §2.2) | statusConfirmationCode | 1:1 | 13 |
| `statusConfirmation.exceptionDescription` | Free-text description of the exception situation | String | 0:1‡ | 13 |

‡ `exceptionDescription` is only permitted when `statusConfirmationCode` = `"11"` (Exception); it is optional even then. It MUST NOT appear when any other code is used.

---

### 2.8 Unique Document Number

`documentID` is a **top-level string** — the unique identifier of the issued PD A1 certificate.

| Data Identifier | Definition | Data type | Occurrence | SD Group |
|----------------|-----------|-----------|------------|----------|
| `documentID` | Unique identifier of the issued PD A1 certificate | String | 1:1 | 14 |

---

### 2.9 Competent Institution

The social security institution that issued this certificate. The four fields `institutionID`, `institutionName`, `countryCode`, and `address` are required. No additional properties permitted (`additionalProperties: false`).

| Data Identifier | Definition | Data type | Occurrence | SD Group |
|----------------|-----------|-----------|------------|----------|
| `competentInstitution.institutionID` | Unique identifier of the competent institution | String | 1:1 | 15 |
| `competentInstitution.institutionName` | Name of the competent institution | String | 1:1 | 15 |
| `competentInstitution.countryCode` | Country code of the competent institution (PDA1 set) | countryCodePDA1States | 1:1 | 15 |
| `competentInstitution.address.streetAndNumber` | Street name and house number of the institution | String | 0:1 | 16 |
| `competentInstitution.address.town` | Town of the institution's address | String | 1:1 | 16 |
| `competentInstitution.address.postcode` | Postal code of the institution's address | String | 0:1 | 16 |
| `competentInstitution.address.countryCode` | Country of the institution's address (PDA1 set) | countryCodePDA1States | 1:1 | 16 |
| `competentInstitution.officeFaxNumber` | Office fax number (E.164 format) | phoneNumber | 0:1 | 16 |
| `competentInstitution.officePhoneNumber` | Office phone number (E.164 format) | phoneNumber | 0:1 | 16 |
| `competentInstitution.email` | Email address of the institution | email | 0:1 | 16 |

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
