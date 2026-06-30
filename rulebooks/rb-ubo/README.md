# Attestation Rulebook for attestations of type Ultimate Beneficial Owner (UBO)

* Author(s):
  * [Florin Coptil, Robert Bosch GmbH]
  * [Stephan-A Fuchs, Deutsche Bank  ]
    
* Previous Authors

* Reviewer(s):
  * [Auth Sources]
    * [ ......Bundesanzeiger, Germany ]
    * [..... KVK, Holland ]
    * [ ..., Italy ]
  * [Banks]
    * [Bastek-Margon Jenny, CommerzBank ]
    * [Baumgardt Michaela, Commerzbank ]
  * [Ricky Lamberty, Robert Bosch GmbH]
  * @TODO Florin — Add the reviewers from attestation design (meetings UseCase, Banks,TransparentRegister)
 

| Version | Date       | Description                                                       |
|---------|------------|-------------------------------------------------------------------|
| 0.1     | 13.03.2026 | Initial draft based on the WeBuild design attestations mettings   |
| 0.2     | 20.04.2026 | updates in regard to the comments and legislation                 |
| 0.4     | 01.06.2026 | Updates of content - legal arrangements                           |
| 0.8     | 24.06.2026 | Updates of content based on the submisson regulation and AMLR/RTS |
| 0.9     | 29.06.2026 | Updates of content based on BOS - vocabulary                      |

* Contact:
  * [Florin Coptil](mailto:florin.coptil@bosch.com)*

* Feedback:

---

## 1 Introduction

This attestation addresses the following question:

**Who are the Ultimate Beneficial Owners (UBOs) of a legal entity, and what is the nature
and extent of their ownership or control?**

A UBO is defined as any natural person who ultimately owns or controls a legal entity based on
AMLR Article 3(17):

- (a) they hold directly or indirectly 25% or more of the units held in the collective
  investment undertaking;
- (b) they have the ability to define or influence the investment policy of the collective
  investment undertaking;
- (c) they control the activities of the collective investment undertaking through other means

### 1.1 Document scope and purpose

The UBO Attestation captures the essential attributes of a natural person who qualifies as an
ultimate beneficial owner of a legal entity — including personal identity, nationality,
residence, and the nature and degree of their ownership or control stake — in a
machine-readable, selectively disclosable format compliant with the EUDI Wallet framework.

**Design Decisions**

This UBO Attestation Rulebook is based on:

- AMLR 2024/1624 for beneficial ownership definitions and requirements
- EUDI Wallet / eIDAS 2.0 framework for digital identity and verifiable attestations
- ISO 8601 for date formatting
- ISO 3166-1 for country codes
- ICAO 9303 for travel document types and number formats

### 1.2 Document structure

This Rulebook is structured as follows:

- Chapter 2 describes the UBO attestation attributes and metadata in an encoding-independent
  manner, including the data model.
- Chapter 3 specifies how the attestation attributes and metadata are encoded: Section 3.2
  covers SD-JWT VC-based encoding.
- Chapter 4 specifies attestation usage scenarios, Relying Party obligations, and integration
  with KYC/KYS and AML workflows.
- Chapter 5 defines trust anchors and verification mechanisms for issuer authorization.
- Chapter 6 defines revocation mechanisms for the attestation.
- Chapter 7 provides compliance information regarding the EUDI framework, AML regulations,
  and applicable data protection laws.
- Chapter 8 provides references to applicable standards and specifications.

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

| **Term**                      | **Description**                                                                                                                               |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| UBO                           | Ultimate Beneficial Owner — a natural person who ultimately owns or controls a legal entity, as defined under AMLR 2024/1624                  |
| NaturalPerson                 | The natural person identified as a UBO, including their personal identity attributes                                                          |
| BirthPlace                    | The place of birth of the natural person, including locality and country                                                                      |
| Citizenship                   | The nationality or nationalities held by the natural person                                                                                   |
| ResidenceAddress              | The registered residential address of the natural person                                                                                      |
| ContactAddress                | An optional alternative contact address for the natural person                                                                                |
| NaturalPersonIdentifier       | A government-issued identity document (e.g., passport, national ID card) used to identify the natural person                                  |
| NaturalPersonUniqueIdentifier | An optional unique identifier issued by an authority to uniquely identify the natural person across systems                                   |
| Justification                 | The object describing how and why the person qualifies as a UBO under applicable AML thresholds and control criteria                          |
| threshold_met                 | The applicable AML threshold(s) or control criteria met by the UBO — see Section 2.8.2                                                        |
| ownership_percentage          | The total direct and indirect ownership percentage held by the UBO (0–100)                                                                    |
| voting_rights_percentage      | The total direct and indirect voting rights percentage held by the UBO (0–100)                                                                |
| control_details               | Free text description of control exercised through means other than ownership percentage                                                      |
| effective_date                | The date from which the UBO status has been effective                                                                                         |
| source                        | Supporting evidence substantiating the UBO determination                                                                                      |
| KYC                           | Know Your Customer — due diligence process for verifying customer identity and assessing risk in financial relationships                      |
| KYS                           | Know Your Supplier — due diligence process for verifying supplier credentials, integrity, and risk exposure                                   |
| AML                           | Anti-Money Laundering — regulatory framework requiring financial institutions and obliged entities to identify and report suspicious activity |
| AMLR                          | Anti-Money Laundering Regulation — EU Regulation 2024/1624 establishing harmonised AML/CFT rules across the EU                                |
| ISO 3166-1                    | International standard defining country codes (alpha-2 and alpha-3 formats)                                                                   |
| ISO 8601                      | International standard for date and time representations (e.g., YYYY-MM-DD)                                                                   |
| ICAO 9303                     | International Civil Aviation Organization standard for travel documents, defining document types and number formats                           |

## 2 Attestation attributes and metadata

The Ultimate Beneficial Owner (UBO) Attestation provides a standardized, verifiable
representation of the natural persons who ultimately own or control a legal entity. It enables
structured and trusted exchange of beneficial ownership data between organizations for use in
KYS (Know Your Supplier), KYC (Know Your Customer), Anti-Money Laundering (AML) compliance,
supplier onboarding, and regulatory due diligence processes.

### 2.1 Introduction

**Data Model:**

```
UBO [1...n]
├─ jurisdiction (tstr) (M)
├─ person (M)
│   ├─ first_name (tstr) (M)
│   ├─ surname (tstr) (M)
│   ├─ birth_date (date) (O)  date_of_birth
├─ birth_place 
│   ├── locality (M)
│   ├── country (M)
│   └── region (O)
├─ citizenship
│   └── citizenship(s) [1..n] (M)
├─ residential_address (M)
│   ├── street (M)
│   ├── house_number (M)
│   ├── locality (M)
│   ├── region (M)
│   ├── postal_code (M)
│   └── country (M)
├─ contact_address (optional)
│   ├── street (M)
│   ├── house_number (M)
│   ├── locality (M)
│   ├── region (M)
│   ├── postal_code (M)
│   └── country(s)
├─ person_identifier
│   ├── document_type (M)
│   ├── document_number (M)
│   ├── issuing_country (M)
│   └── expiry_date (M)
├─ person_unique_identifier (optional)
│   ├── identifier_unique (O)
│   └── identifier_issuing_authority (O)
├─ justification (M)                  // How this person qualifies as UBO
│   ├─ threshold_met (Array of enum) (M)  // e.g., "ownership_25_plus", "control_voting_25_plus", "control_management"
│   ├─ ownership_percentage (Decimal) (O) // Total direct/indirect ownership percentage
│   ├─ voting_rights_percentage (Decimal) (O) // Total direct/indirect voting rights percentage
│   └─ control_details (tstr) (O)         // Free text if control is via other means
├─ effective_date (date) (M)              // Date when this UBO status became effective
└─ source [1..n] (at least one piece of supporting evidence required) // Information about the source of this statement
│   ├─ id (tstr) (M)
│   ├─ type (tstr) (M)
│   └─ url (uri) (O)
│   └─ data (base64) (O)    
```

**Explanation:**

- The attestation **MAY** contain one or more UBO entries (`[1...n]`), one per identified
  ultimate beneficial owner.
- `person`, `birth_place`, `citizenship`, `residential_address`, `person_identifier`,
  and `justification` are mandatory objects within each UBO entry.
- `contact_address` and `person_unique_identifier` are optional objects.
- `citizenship` **SHALL** contain at least one citizenship entry and **MAY** contain multiple
  entries for persons holding multiple nationalities.
- `threshold_met` **SHALL** contain at least one value from the enumerated list in
  Section 2.8.2 and **MAY** contain multiple values where multiple thresholds apply.
- `ownership_percentage` and `voting_rights_percentage` are expressed as decimal values
  between 0 and 100.
- `source` **SHALL** contain at least one entry; if `source.url` is not a publicly accessible
  URI, `source.data` (base64) **SHALL** be provided.

**Attestation Classification:**

This attestation type MAY be classified as:

- **`EAA`** when self-issued by the legal entity subject to the UBO disclosure obligation.
- **`QEAA`** when issued by a qualified trust service provider (QTSP) or authorised competent
  body (e.g., a notary, commercial register authority, or AML-supervised entity).

**Attribute Overview:**

| **Data Identifier**        | **Semantic Reference** | **Definition**                                             | **Data Type**                         |
|----------------------------|------------------------|------------------------------------------------------------|---------------------------------------|
| `person`                   | —                      | Personal identity attributes of the UBO                    | Object                                |
| `birth_place`              | —                      | Place of birth of the UBO                                  | Object                                |
| `citizenship`              | —                      | Citizenship(s) held by the UBO (one or more nationalities) | Array of Strings (ISO 3166-1 alpha-2) |
| `residential_address`      | —                      | Registered residential address of the UBO                  | Object                                |
| `contact_address`          | —                      | Optional alternative contact address of the UBO            | Object                                |
| `person_identifier`        | —                      | Government-issued identity document details of the UBO     | Object                                |
| `person_unique_identifier` | —                      | Optional unique identifier assigned by an authority        | Object                                |
| `justification`            | —                      | How and why this person qualifies as UBO under AMLR        | Object                                |
| `source`                   | —                      | Supporting evidence for the UBO determination              | Array of Objects                      |

### 2.2 Mandatory Attributes

#### Person Attributes

| **Data Identifier**  | **Semantic Reference**  | **Definition**                                                               | **Data Type**     |
|----------------------|-------------------------|------------------------------------------------------------------------------|-------------------|
| `first_name`         | —                       | First name(s) of the natural person, including middle names where applicable | String            |
| `surname`            | —                       | Surname(s) / family name(s) of the natural person                            | String            |
| `birth_date`         | —                       | Date of birth of the natural person (ISO 8601 YYYY-MM-DD)                    | String (ISO 8601) |

#### BirthPlace Attributes

| **Data Identifier**   |  **Semantic Reference** | **Definition**                        | **Data Type**       |
|-----------------------|-------------------------|---------------------------------------|---------------------|
| `locality`            | —                       | City or locality of birth             | String              |
| `country`             | —                       | Country of birth (ISO 3166-1 alpha-2) | String (ISO 3166-1) |

#### Citizenship Attributes

| **Data Identifier**   | **Semantic Reference**   | **Definition**                                                                                                                | **Data Type**           |
|-----------------------|--------------------------|-------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| `citizenship`         | —                        | Nationality or nationalities held by the natural person; SHALL use ISO 3166-1 alpha-2 codes; SHALL contain at least one entry | Array of Strings [1..n] |

#### ResidentialAddress Attributes

| **Data Identifier**  | **Semantic Reference**  | **Definition**                                          | **Data Type**       |
|----------------------|-------------------------|---------------------------------------------------------|---------------------|
| `street`             | —                       | Street name of the residential address                  | String              |
| `house_number`       | —                       | House or building number of the residential address     | String              |
| `locality`           | —                       | City or locality of the residential address             | String              |
| `region`             | —                       | Region or state of the residential address              | String              |
| `postal_code`        | —                       | Postal code of the residential address                  | String              |
| `country`            | —                       | Country of the residential address (ISO 3166-1 alpha-2) | String (ISO 3166-1) |

#### PersonIdentifier Attributes

| **Data Identifier**   | **Semantic Reference**  | **Definition**                                                  | **Data Type**       |
|-----------------------|-------------------------|-----------------------------------------------------------------|---------------------|
| `document_type`       | —                       | Type of identity document — SHALL use values from Section 2.8.1 | String (Enum)       |
| `document_number`     | —                       | Number of the identity document as printed on the document      | String              |
| `issuing_country`     | —                       | Country that issued the identity document (ISO 3166-1 alpha-2)  | String (ISO 3166-1) |
| `expiry_date`         | —                       | Expiry date of the identity document (ISO 8601 YYYY-MM-DD)      | String (ISO 8601)   |

#### Justification Attributes

| **Data Identifier**   | **Semantic Reference**   | **Definition**                                                                                                                 | **Data Type**           |
|-----------------------|--------------------------|--------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| `threshold_met`       | —                        | Array of applicable AML thresholds or control criteria met — SHALL use values from Section 2.8.2 — at least one value required | Array of Strings (Enum) |

#### Source Attributes

| **Data Identifier**  | **Semantic Reference**   | **Definition**                                                            | **Data Type**   |
|----------------------|--------------------------|---------------------------------------------------------------------------|-----------------|
| `id`                 | —                        | Unique identifier for the source document                                 | String          |
| `type`               | —                        | Type of source document (e.g., `"Evidence"`, `"Register"`, `"TrustDeed"`) | String          |

### 2.3 Optional Attributes

#### BirthPlace Optional Attributes

| **Data Identifier**  | **Semantic Reference**   | **Definition**                      | **Data Type**   |
|----------------------|--------------------------|-------------------------------------|-----------------|
| `region`             | —                        | Region or state of birth — optional | String          |

#### Person Optional Attributes

| **Data Identifier**  | **Semantic Reference**   | **Definition**                                                                              | **Data Type**     |
|----------------------|--------------------------|---------------------------------------------------------------------------------------------|-------------------|
| `birth_date`         | —                        | Date of birth (ISO 8601 YYYY-MM-DD) — recommended, may be omitted in specific jurisdictions | String (ISO 8601) |

#### ContactAddress Attributes *(entire object is optional)*

| **Data Identifier**  | **Semantic Reference**  | **Definition**                                      | **Data Type**       |
|----------------------|-------------------------|-----------------------------------------------------|---------------------|
| `street`             | —                       | Street name of the contact address                  | String              |
| `house_number`       | —                       | House or building number of the contact address     | String              |
| `locality`           | —                       | City or locality of the contact address             | String              |
| `region`             | —                       | Region or state of the contact address              | String              |
| `postal_code`        | —                       | Postal code of the contact address                  | String              |
| `country`            | —                       | Country of the contact address (ISO 3166-1 alpha-2) | String (ISO 3166-1) |

#### PersonUniqueIdentifier Attributes *(entire object is optional)*

| **Data Identifier**            | **Semantic Reference**  | **Definition**                                                             | **Data Type**  |
|--------------------------------|-------------------------|----------------------------------------------------------------------------|----------------|
| `identifier_unique`            | —                       | A unique identifier assigned to the natural person by an issuing authority | String         |
| `identifier_issuing_authority` | —                       | The authority that issued the unique identifier                            | String         |

#### Justification Optional Attributes

| **Data Identifier**        | **Semantic Reference**  | **Definition**                                                                           | **Data Type**   |
|----------------------------|-------------------------|------------------------------------------------------------------------------------------|-----------------|
| `ownership_percentage`     | —                       | Total direct and indirect ownership percentage held (0–100)                              | Decimal         |
| `voting_rights_percentage` | —                       | Total direct and indirect voting rights percentage held (0–100)                          | Decimal         |
| `control_details`          | —                       | Free text description of control exercised through means other than ownership percentage | String          |

#### Source Optional Attributes

| **Data Identifier**  | **Semantic Reference**  | **Definition**                                                                               | **Data Type**   |
|----------------------|-------------------------|----------------------------------------------------------------------------------------------|-----------------|
| `url`                | —                       | URI reference to the source or evidence document                                             | URI             |
| `data`               | —                       | Base64-encoded source document — SHALL be provided if `url` is not a publicly accessible URI | String (base64) |

### 2.4 Conditional Attributes

| **Data Identifier**                      | **Condition**                                                                 | **Definition**                                  | **Data Type**   |
|------------------------------------------|-------------------------------------------------------------------------------|-------------------------------------------------|-----------------|
| `source.data`                            | **SHALL** be provided if `source.url` is not a publicly accessible URI        | Base64-encoded evidence document                | String (base64) |
| `justification.control_details`          | **SHALL** be provided if `threshold_met` includes `"control_other_means"`     | Free text description of other means of control | String          |
| `justification.ownership_percentage`     | **SHOULD** be provided if `threshold_met` includes `"ownership_25_plus"`      | Total ownership percentage                      | Decimal         |
| `justification.voting_rights_percentage` | **SHOULD** be provided if `threshold_met` includes `"control_voting_25_plus"` | Total voting rights percentage                  | Decimal         |

### 2.5 Mandatory Metadata

| **Data Identifier**          | **Definition**                                                                     | **Data Type**  |
|------------------------------|------------------------------------------------------------------------------------|----------------|
| `attestation_legal_category` | Legal category of this attestation — SHALL be `"EAA"` or `"QEAA"`                  | String         |

### 2.6 Optional Metadata
### 2.7 Conditional Metadata

No conditional metadata elements are defined for this attestation type.

### 2.8 Value Lists

#### 2.8.1 Document Type Codes

The `person_identifier.document_type` attribute SHALL use one of the following standardised
values, aligned with ICAO 9303:

| **Code**           | **Definition**                                         |
|--------------------|--------------------------------------------------------|
| `PASSPORT`         | International passport as defined by ICAO 9303         |
| `NATIONAL_ID`      | National identity card issued by a competent authority |
| `RESIDENCE_PERMIT` | Residence permit issued to foreign nationals           |
| `DRIVING_LICENSE`  | Driving licence accepted as an identity document       |
| `OTHER`            | Any other government-issued identity document          |

#### 2.8.2 Threshold Met Codes

The `justification.threshold_met` attribute SHALL use one or more of the following
standardised values, aligned with AMLR Article 3(17):

**a) Ownership-Based Thresholds:**

| **Code**             | **Definition**                                                                                   |
|----------------------|--------------------------------------------------------------------------------------------------|
| `ownership_25_plus`  | The UBO holds ≥25% of shares or ownership interests directly or indirectly in the subject entity |
| `ownership_direct`   | The UBO holds ≥25% through direct shareholding without intermediary entities                     |
| `ownership_indirect` | The UBO holds ≥25% through one or more intermediary legal entities                               |

**b) Voting Rights-Based Thresholds:**

| **Code**                  | **Definition**                                                    |
|---------------------------|-------------------------------------------------------------------|
| `control_voting_25_plus`  | The UBO holds ≥25% of voting rights directly or indirectly        |
| `control_voting_direct`   | The UBO holds ≥25% of voting rights through direct shareholding   |
| `control_voting_indirect` | The UBO holds ≥25% of voting rights through intermediary entities |

**c) Management / Other Control:**

| **Code**                       | **Definition**                                                          |
|--------------------------------|-------------------------------------------------------------------------|
| `control_management`           | Control exercised through appointment of senior management or the board |
| `control_veto`                 | Control exercised through veto rights over major corporate decisions    |
| `control_contractual`          | Control exercised through formal or informal contractual agreements     |
| `control_family_relationships` | Control exercised through coordinated action among family members       |
| `control_acting_in_concert`    | Control exercised through acting in concert with other shareholders     |
| `control_nominee`              | Control exercised through nominee arrangements                          |
| `control_other_means`          | Control exercised through other means not explicitly listed above       |

**d) Legal Arrangement Roles** *(for trusts, foundations, and similar structures):*

| **Code**                      | **Definition**                                                                  |
|-------------------------------|---------------------------------------------------------------------------------|
| `arrangement_settlor`         | The UBO is the settlor (creator) of a trust or similar legal arrangement        |
| `arrangement_trustee`         | The UBO is the trustee of a trust or similar legal arrangement                  |
| `arrangement_beneficiary`     | The UBO is a beneficiary of a trust or similar legal arrangement                |
| `arrangement_protector`       | The UBO is the protector of a trust or similar legal arrangement                |
| `arrangement_object_of_power` | The UBO is the object of a power in a legal arrangement                         |
| `arrangement_default_taker`   | The UBO is the default taker (residual beneficiary) of a legal arrangement      |
| `arrangement_other_control`   | Any other natural person exercising ultimate control over the legal arrangement |

> **Note:** Multiple `threshold_met` values MAY apply to a single UBO. For example, a UBO
> may be identified through `"ownership_25_plus"` (35% direct shareholding) AND
> `"control_voting_25_plus"` (50% voting rights via special shares) AND
> `"control_management"` (contractual right to appoint the CEO).

#### 2.8.3 Country Codes

All `country`, `issuing_country`, and `citizenship` attributes SHALL use
**ISO 3166-1 alpha-2** two-letter country codes.

For a complete list, refer to the [ISO 3166-1 standard](https://www.iso.org/iso-3166-country-codes.html).

#### 2.8.4 Date Formats

All date attributes SHALL follow the **ISO 8601 YYYY-MM-DD** format.

#### 2.8.5 Source Type Codes

The `source.type` attribute SHOULD use one of the following standardised values:

| **Code**                | **Definition**                                                      |
|-------------------------|---------------------------------------------------------------------|
| `ShareRegister`         | Official shareholder register extract                               |
| `CommercialRegister`    | Extract from a national commercial or company register              |
| `TransparencyRegister`  | Entry from an official beneficial ownership / transparency register |
| `TrustDeed`             | Trust deed or instrument establishing a legal arrangement           |
| `ShareholderAgreement`  | Shareholders' agreement evidencing ownership structure              |
| `ArticlesOfAssociation` | Articles of association defining share structure                    |
| `GovernanceChart`       | Organisational or governance chart showing ownership structure      |
| `AMLOfficerDeclaration` | Declaration by an AML-supervised officer or compliance function     |
| `NotarialDeed`          | Notarially certified document evidencing ownership                  |
| `Other`                 | Any other supporting evidence document                              |

### 2.9 Integrity Rules

The following integrity rules SHALL be enforced:

| **Rule ID**  | **Rule**                                                                                                                                                   |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IR-01        | The `ubo` array SHALL contain at least one UBO entry                                                                                                       |
| IR-02        | Each UBO entry SHALL contain exactly one `person`, `birth_place`, `citizenship`, `residential_address`, `person_identifier`, `justification`, and `source` |
| IR-03        | `person.first_name` SHALL be a non-empty string                                                                                                            |
| IR-04        | `person.surname` SHALL be a non-empty string                                                                                                               |
| IR-05        | `person.birth_date`, if present, SHALL be a valid ISO 8601 date (YYYY-MM-DD) in the past                                                                   |
| IR-06        | `birth_place.locality` SHALL be a non-empty string                                                                                                         |
| IR-07        | `birth_place.country` SHALL be a valid ISO 3166-1 alpha-2 country code                                                                                     |
| IR-08        | `citizenship` SHALL contain at least one valid ISO 3166-1 alpha-2 country code                                                                             |
| IR-09        | All mandatory address fields (`street`, `house_number`, `locality`, `region`, `postal_code`, `country`) within `residential_address` SHALL be non-empty    |
| IR-10        | `residential_address.country` SHALL be a valid ISO 3166-1 alpha-2 country code                                                                             |
| IR-11        | If `contact_address` is present, all its mandatory fields SHALL be non-empty                                                                               |
| IR-12        | `person_identifier.document_type` SHALL use one of the enumerated values from Section 2.8.1                                                                |
| IR-13        | `person_identifier.document_number` SHALL be a non-empty string                                                                                            |
| IR-14        | `person_identifier.issuing_country` SHALL be a valid ISO 3166-1 alpha-2 country code                                                                       |
| IR-15        | `person_identifier.expiry_date` SHALL be a valid ISO 8601 date (YYYY-MM-DD)                                                                                |
| IR-16        | `justification.threshold_met` SHALL contain at least one value from Section 2.8.2                                                                          |
| IR-17        | `justification.ownership_percentage` and `justification.voting_rights_percentage`, if present, SHALL each be a decimal value between 0 and 100 inclusive   |
| IR-18        | `justification.control_details` SHALL be present if `threshold_met` contains `"control_other_means"`                                                       |
| IR-19        | `effective_date` SHALL be a valid ISO 8601 date (YYYY-MM-DD) in the past                                                                                   |
| IR-20        | `source` SHALL contain at least one entry                                                                                                                  |
| IR-21        | If `source.url` is not a publicly accessible URI, `source.data` (base64) SHALL be provided                                                                 |
| IR-22        | `issuance_date` and `expiry_date` (metadata) SHALL be valid ISO 8601 DateTimes                                                                             |
| IR-23        | `expiry_date` (metadata) SHALL be later than `issuance_date`                                                                                               |
| IR-24        | `attestation_legal_category` SHALL be one of `"EAA"` or `"QEAA"`                                                                                           |
| IR-25        | `vct` SHALL be `"eu.we-build:ubo:1"`                                                                                                                       |
| IR-26        | `jurisdiction` SHALL be a valid ISO 3166-1 alpha-2 country code                                                                                            |

---

## 3 Attestation Encoding

### 3.1 ISO/IEC 18013-5-Compliant Encoding

ISO/IEC 18013-5 (mdoc) is **out of scope** for this Rulebook, as offline proximity
presentation is not a current requirement for the UBO Attestation.

### 3.2 SD-JWT VC-Based Encoding

The UBO Attestation uses the SD-JWT VC format to allow for selective disclosure of UBO
attributes.

**Selective Disclosure:** Claims within each UBO entry SHALL be individually selectively
disclosable, enabling a legal entity to disclose only the attributes requested by a Relying
Party. Sensitive personal attributes such as `birth_date`, `document_number`, and address
details SHALL be individually disclosable.

The `.` notation is used to indicate the nesting of attributes.

**Verifiable Credential Type (`vct`):** `eu.we-build:ubo:1`

#### 3.2.1 Attribute Encoding Table

| **Data Identifier**                            | **Attribute Identifier**                                       | **Encoding Format**                   | **Reference / Notes**                                                                               | **Disclosable** |
|------------------------------------------------|----------------------------------------------------------------|---------------------------------------|-----------------------------------------------------------------------------------------------------|-----------------|
| `ubo`                                          | `ubo`                                                          | Array [UBO]                           | SHALL contain at least one UBO entry                                                                | MUST            |
| `jurisdiction`                                 | `ubo[n].jurisdiction`                                          | String (ISO 3166-1 alpha-2)           | Jurisdiction of the subject entity — SHALL be non-empty                                             | MUST            |
| **Person**                                     |                                                                |                                       |                                                                                                     |                 |
| `first_name`                                   | `ubo[n].person.first_name`                                     | String                                | First name(s) of the natural person — SHALL be non-empty                                            | MUST            |
| `surname`                                      | `ubo[n].person.surname`                                        | String                                | Surname(s) of the natural person — SHALL be non-empty                                               | MUST            |
| `birth_date`                                   | `ubo[n].person.birth_date`                                     | String (ISO 8601 YYYY-MM-DD)          | Date of birth — SHALL be in the past; optional                                                      | MAY             |
| **BirthPlace**                                 |                                                                |                                       |                                                                                                     |                 |
| `locality`                                     | `ubo[n].birth_place.locality`                                  | String                                | City or locality of birth — SHALL be non-empty                                                      | MUST            |
| `country`                                      | `ubo[n].birth_place.country`                                   | String (ISO 3166-1 alpha-2)           | Country of birth — SHALL be non-empty                                                               | MUST            |
| `region`                                       | `ubo[n].birth_place.region`                                    | String                                | Region or state of birth — optional                                                                 | MAY             |
| **Citizenship**                                |                                                                |                                       |                                                                                                     |                 |
| `citizenship`                                  | `ubo[n].citizenship`                                           | Array of Strings (ISO 3166-1 alpha-2) | Citizenship(s) — SHALL contain at least one entry                                                   | MUST            |
| **ResidentialAddress**                         |                                                                |                                       |                                                                                                     |                 |
| `street`                                       | `ubo[n].residential_address.street`                            | String                                | Street name — SHALL be non-empty                                                                    | MUST            |
| `house_number`                                 | `ubo[n].residential_address.house_number`                      | String                                | House number — SHALL be non-empty                                                                   | MUST            |
| `locality`                                     | `ubo[n].residential_address.locality`                          | String                                | City or locality — SHALL be non-empty                                                               | MUST            |
| `region`                                       | `ubo[n].residential_address.region`                            | String                                | Region or state — SHALL be non-empty                                                                | MUST            |
| `postal_code`                                  | `ubo[n].residential_address.postal_code`                       | String                                | Postal code — SHALL be non-empty                                                                    | MUST            |
| `country`                                      | `ubo[n].residential_address.country`                           | String (ISO 3166-1 alpha-2)           | Country — SHALL be non-empty                                                                        | MUST            |
| **ContactAddress** *(optional object)*         |                                                                |                                       |                                                                                                     |                 |
| `street`                                       | `ubo[n].contact_address.street`                                | String                                | Street name of the contact address — optional                                                       | MAY             |
| `house_number`                                 | `ubo[n].contact_address.house_number`                          | String                                | House number of the contact address — optional                                                      | MAY             |
| `locality`                                     | `ubo[n].contact_address.locality`                              | String                                | Locality of the contact address — optional                                                          | MAY             |
| `region`                                       | `ubo[n].contact_address.region`                                | String                                | Region of the contact address — optional                                                            | MAY             |
| `postal_code`                                  | `ubo[n].contact_address.postal_code`                           | String                                | Postal code of the contact address — optional                                                       | MAY             |
| `country`                                      | `ubo[n].contact_address.country`                               | String (ISO 3166-1 alpha-2)           | Country of the contact address — optional                                                           | MAY             |
| **PersonIdentifier**                           |                                                                |                                       |                                                                                                     |                 |
| `document_type`                                | `ubo[n].person_identifier.document_type`                       | String (Enum)                         | SHALL use values from Section 2.8.1                                                                 | MUST            |
| `document_number`                              | `ubo[n].person_identifier.document_number`                     | String                                | Document number as printed on the document — SHALL be non-empty                                     | MUST            |
| `issuing_country`                              | `ubo[n].person_identifier.issuing_country`                     | String (ISO 3166-1 alpha-2)           | Country that issued the document — SHALL be non-empty                                               | MUST            |
| `expiry_date`                                  | `ubo[n].person_identifier.expiry_date`                         | String (ISO 8601 YYYY-MM-DD)          | Expiry date of the document                                                                         | MUST            |
| **PersonUniqueIdentifier** *(optional object)* |                                                                |                                       |                                                                                                     |                 |
| `identifier_unique`                            | `ubo[n].person_unique_identifier.identifier_unique`            | String                                | Unique identifier assigned by an authority — optional                                               | MAY             |
| `identifier_issuing_authority`                 | `ubo[n].person_unique_identifier.identifier_issuing_authority` | String                                | Authority that issued the unique identifier — optional                                              | MAY             |
| **Justification**                              |                                                                |                                       |                                                                                                     |                 |
| `threshold_met`                                | `ubo[n].justification.threshold_met`                           | Array of Strings (Enum)               | SHALL use values from Section 2.8.2 — at least one value required                                   | MUST            |
| `ownership_percentage`                         | `ubo[n].justification.ownership_percentage`                    | Decimal (0–100)                       | Total direct/indirect ownership percentage — optional                                               | MAY             |
| `voting_rights_percentage`                     | `ubo[n].justification.voting_rights_percentage`                | Decimal (0–100)                       | Total direct/indirect voting rights percentage — optional                                           | MAY             |
| `control_details`                              | `ubo[n].justification.control_details`                         | String                                | Free text for other means of control — required if `threshold_met` includes `"control_other_means"` | MAY             |
| **Effective Date**                             |                                                                |                                       |                                                                                                     |                 |
| `effective_date`                               | `ubo[n].effective_date`                                        | String (ISO 8601 YYYY-MM-DD)          | Date when UBO status became effective — SHALL be non-empty                                          | MUST            |
| **Source**                                     |                                                                |                                       |                                                                                                     |                 |
| `id`                                           | `ubo[n].source[m].id`                                          | String                                | Unique source identifier — SHALL be non-empty                                                       | MUST            |
| `type`                                         | `ubo[n].source[m].type`                                        | String                                | Type of source — SHOULD use values from Section 2.8.5                                               | MUST            |
| `url`                                          | `ubo[n].source[m].url`                                         | URI                                   | URI reference to source document — optional                                                         | MAY             |
| `data`                                         | `ubo[n].source[m].data`                                        | String (base64)                       | Base64-encoded source — required if `url` not publicly accessible                                   | MAY             |
| **Metadata**                                   |                                                                |                                       |                                                                                                     |                 |
| `attestation_legal_category`                   | `attestation_legal_category`                                   | String                                | SHALL be `"EAA"` or `"QEAA"`                                                                        | MUST NOT        |

**Notes:**

- **MUST**: The claim SHALL be selectively disclosable — the holder MAY choose to disclose or
  withhold this claim when presenting the credential to a Relying Party.
- **MAY**: The claim MAY be selectively disclosable if the issuer supports it.
- **MUST NOT**: The claim SHALL NOT be selectively disclosable — it is always present in plain
  text in the JWT header/payload.
- `ubo` entries are indexed as `[n]` where `n` starts at `0`; at least one UBO entry SHALL be
  present.
- `source` entries within each UBO are indexed as `[m]` where `m` starts at `0`; at least one
  source entry SHALL be present per UBO.
- `iat`, `exp`, and `iss` follow RFC 7519 standard JWT claim naming conventions.

#### 3.2.2 Status Claim

For SD-JWT VC-compliant UBO Attestations, the attestation MUST include a `status` claim if the
technical validity period is greater than 24 hours. This claim enables Relying Parties to
determine if a credential has been revoked via a status list mechanism.

The `status` claim SHALL be a JSON object with the following members:

| **Field**                | **Type**       | **Value**                                       |
|--------------------------|----------------|-------------------------------------------------|
| `type`                   | String         | SHALL be `"status-list"`                        |
| `status_list_credential` | String (URI)   | URI of the Status List Credential document      |
| `status_list_index`      | Integer (>= 0) | Zero-based index into the status list bitstring |
| `status_purpose`         | String         | SHALL be `"revocation"`                         |

Example:

```json
{
  "status": {
    "type": "status-list",
    "status_list_credential": "https://issuer.example.com/status/ubo/2025",
    "status_list_index": 101,
    "status_purpose": "revocation"
  }
}
```


#### 3.2.3 Example Payload

The following is a non-normative example of a UBO SD-JWT VC payload demonstrating a natural
person qualifying as UBO through direct shareholding and management control:

```json
{
  "vct": "eu.we-build:ubo:1",
  "iss": "https://issuer.example.com",
  "iat": 1736935200,
  "exp": 1768471200,
  "issuing_entity": "did:example:legal-entity-789",
  "attestation_legal_category": "EAA",
  "schema_version": "0.4.0",
  "trust_anchor_url": "https://trust.webuildconsortium.eu/anchors/eidas-tl",

  "ubo": [
    {
      "jurisdiction": "DE",
      "person": {
        "first_name": "Anna",
        "surname": "Müller",
        "birth_date": "1978-04-15"
      },
      "birth_place": {
        "locality": "Munich",
        "country": "DE",
        "region": "Bavaria"
      },
      "citizenship": ["DE", "AT"],
      "residential_address": {
        "street": "Hauptstraße",
        "house_number": "12",
        "locality": "Munich",
        "region": "Bavaria",
        "postal_code": "80331",
        "country": "DE"
      },
      "contact_address": {
        "street": "Marienplatz",
        "house_number": "1",
        "locality": "Munich",
        "region": "Bavaria",
        "postal_code": "80331",
        "country": "DE"
      },
      "person_identifier": {
        "document_type": "PASSPORT",
        "document_number": "C01X00T47",
        "issuing_country": "DE",
        "expiry_date": "2030-04-14"
      },
      "person_unique_identifier": {
        "identifier_unique": "DE-12345678",
        "identifier_issuing_authority": "Bundesamt für Justiz"
      },
      "justification": {
        "threshold_met": [
          "ownership_25_plus",
          "control_voting_25_plus",
          "control_management"
        ],
        "ownership_percentage": 45.0,
        "voting_rights_percentage": 45.0,
        "control_details": "Additionally controls via contractual right to appoint CEO per shareholders agreement dated 2015-03-01"
      },
      "effective_date": "2015-03-01",
      "source": [
        {
          "id": "src-ubo-001",
          "type": "ShareRegister",
          "url": "https://example.com/docs/share-register-extract-2024.pdf"
        },
        {
          "id": "src-ubo-002",
          "type": "ShareholderAgreement",
          "url": "https://example.com/docs/shareholder-agreement-2015.pdf"
        }
      ]
    },
    {
      "jurisdiction": "DE",
      "person": {
        "first_name": "Klaus",
        "surname": "Weber",
        "birth_date": "1965-11-30"
      },
      "birth_place": {
        "locality": "Hamburg",
        "country": "DE"
      },
      "citizenship": ["DE"],
      "residential_address": {
        "street": "Alsterufer",
        "house_number": "5",
        "locality": "Hamburg",
        "region": "Hamburg",
        "postal_code": "20354",
        "country": "DE"
      },
      "person_identifier": {
        "document_type": "NATIONAL_ID",
        "document_number": "L01X00T28",
        "issuing_country": "DE",
        "expiry_date": "2028-11-29"
      },
      "justification": {
        "threshold_met": [
          "ownership_indirect",
          "control_voting_indirect"
        ],
        "ownership_percentage": 30.0,
        "voting_rights_percentage": 30.0
      },
      "effective_date": "2018-07-15",
      "source": [
        {
          "id": "src-ubo-003",
          "type": "CommercialRegister",
          "url": "https://handelsregister.example.de/extract/HRB-12345"
        }
      ]
    }
  ],

  "status": {
    "type": "status-list",
    "status_list_credential": "https://issuer.example.com/status/ubo/2025",
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

Sample payloads are provided under `../data-schemas/sd-jwt/sample-data/ubo-sd-jwt-sample.json`

### 3.3 W3C Verifiable Credentials Data Model-based encoding

@TODO — To be discussed: which stakeholders will support this format and which use cases require it.

---

## 4 Attestation usage

The UBO Attestation serves the core AML/CTF compliance requirement of identifying ultimate beneficial owners across European financial and business ecosystems:

*Primary use cases:*
- Bank KYC for Corporate Account Opening (per AMLR Articles 20-25)
- Supplier Onboarding (KYS with UBO Transparency)
- Regulatory Submission for company to Transparency Register  ( Proposed Implementing Act dated 26/11/2025)
- Regulatory Reporting for company (Transparency Register Cross-Reference)
- Ongoing Monitoring (AMLR Article 25)

### 4.1. Issuance process ###

When issuing the attestation, the Issuer SHALL perform the following obligations:

**Issuance Flow:**
*Calculation and Issuance:*
- The legal entity calculates its UBO  by:Applying the ≥25% threshold to the Ownership List (identifying natural persons with ≥25% direct or indirect ownership)
- Analyzing the Control List for natural persons exercising ultimate control through other means (even if ownership <25%)
- Applying AMLR determination methodologies (direct ownership, indirect ownership, legal arrangement roles, nature of control)
- The legal entity self-issues the UBO  Attestation into its Company Wallet OR a QTSP issues the UBO  Attestation to the company's wallet (as a QEAA), certifying the UBO calculation
- Classification: "EAA" (self-issued) or "QEAA (Transparency Reqister/QTSP issued)

**Attestation**
The Issuer SHALL implement the base issuer obligation as defined in the Issuer Obligation specification:
https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-base/verifier-base-verification.md#41-issuer-obligations

### 4.2 Relying Party Obligations
When receiving and processing an attestation, the Relying Party SHALL perform the following verification obligations.
### 4.2.1 – 4.2.8 Base Verification Process
The Relying Party SHALL perform the base attestation verification process as defined in the Base Verification specification:
https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-base/verifier-base-verification.md#42-relying-party-obligations

### 4.2.9 Validate Integrity Rule
- Verify that at least one UBO is present
- Verify that all AMLR Article 62 mandatory attributes are present for each UBO
- Verify that each UBO has at least one determination_methodology

#### 4.2.10 UseCaseSpecific: Cross-Reference with Ownership and Control Lists (AMLR Article 60) ###
@TODO Florin -> review with the banks in regard of banks obligation for Discrepancy
The AMLR compliance requires independent verification of UBO calculations.

*RPs SHALL:*
- Request Ownership List and Control List in addition to UBO
- Perform Independent UBO Calculation:Apply ≥25% threshold to Ownership List → Identify natural persons with ≥25% total ownership
- Analyze Control List for natural persons exercising ultimate control (even if <25% ownership)
- Apply AMLR determination methodologies
- Cross-Check Against Presented UBO :
  - Compare UBO data: Verify that all independently calculated UBOs appear in the presented UBO
  - Compare determination methodologies: Verify consistency
  - Compare ownership stakes (if disclosed)
- Discrepancy Handling
  - If UBOs are missing from presented list → notify entity to recalculate and update
  - If extra UBOs appear in presented list (not in calculated list) → request justification or evidence
  - If discrepancies relate to Transparency Register submission → report to register authority per AMLR Article 60
  - If discrepancies cannot be resolved -> risk cases: apply enhanced due diligence or decline relationship

#### 4.2.12 UseCaseSpecific: UBO Identity Verification (AMLR Article 21 Procedure) ####
For each UBO in the UBO  Attestation, the RP SHALL perform identity verification following this hierarchical procedure:
@TODO Florin Specify the process (relevant in MVP+)

**Step 1: PID-Based Verification (Preferred Method)**
- Request PID Attestation from the UBO (via EUDI Wallet)
- Cross-Check PID Against UBO  :identification & other attributes
- PID Attestation verification (Section 4.2)

**Step 2: non-PID Based Verification ( e.g., mdoc for driver's license, future passport mdoc))**
- Request presentation of identity document attestation
- Cross-Check data against UBO  :identification & other attributes
- mDOC  Attestation verification (Section 4.2)

**Step 3: Identity Document Verification (PoA)**
- Request presentation of identity document attestation (PoA)
- Cross-Check data against UBO  :identification & other attributes
- POA  Attestation verification (Section 4.2)
-
**Step 4: Manual/physical verification (in-person or certified copy)**
- Manual/physical identity document verification (in-person or certified copy)

**Step 5: Unique Personal Identification Number Verification (if available)**
- Check if unique_personal_identification_number is available in UBO
- If available:Use the unique ID number for identity verification

## 5 Trust anchors

### 5.1 Trust Model for UBO  Attestations

### 5.2 Trust Anchor Location Metadata
UBO  Attestations SHOULD include the trust_anchor_url metadata attribute (see Section 2.6).
@Florin -> trust topic

## 6 Revocation
Details on the revocation mechanisms and processes for UBO  attestations will be completed in a future version of this Rulebook. This will cover how Relying Parties can check the revocation status of an attestation.
@Florin -> revocation  topic

## 7 References
This chapter will be completed in a future version of this Rulebook to include specific references relevant to UBO  attestations.

## 7 Compliance
This UBO  Attestation Rulebook is specifically designed to comply with AMLR 2024/1624:
*Article 3(17) – Definition of Beneficial Owner:*
*Article 60 – Beneficial Ownership Registers:*
*Article 62 – Beneficial Ownership Information Requirements:*



## 8 References

| **Item Reference**                     | **Standard name/details**                                                                                                                                                                                                                                                |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [European Digital Identity Regulation] | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework |
| [AMLR 2024/1624]                       | Regulation (EU) 2024/1624 of the European Parliament and of the Council on the prevention of the use of the financial system for the purposes of money laundering or terrorist financing                                                                                  |
| [HAIP]                                 | Yasuda, K. et al, OpenID4VC High Assurance Interoperability Profile, OpenId Foundation, Version draft-03                                                                                                                                                                 |
| [IANA-JWT-Claims]                      | IANA JSON Web Token Claims Registry. Available: https://www.iana.org/assignments/jwt/jwt.xhtml                                                                                                                                                                           |
| [ICAO 9303]                            | ICAO Doc 9303 — Machine Readable Travel Documents. Available: https://www.icao.int/publications/pages/publication.aspx?docnum=9303                                                                                                                                        |
| [ISO/IEC 18013-5]                      | ISO/IEC 18013-5, Personal identification — ISO-compliant driving licence - Part 5: Mobile driving licence (mDL) application, First edition, 2021-09                                                                                                                      |
| [ISO 3166-1]                           | ISO 3166-1 — Codes for the representation of names of countries and their subdivisions. Available: https://www.iso.org/iso-3166-country-codes.html                                                                                                                        |
| [ISO 8601]                             | ISO 8601 — Date and time format. Available: https://www.iso.org/iso-8601-date-and-time-format.html                                                                                                                                                                       |
| [OIDC]                                 | Sakimura, N. et al., "OpenID Connect Core 1.0", OpenID Foundation. Available: https://openid.net/specs/openid-connect-core-1_0.html                                                                                                                                      |
| [RFC 2119]                             | RFC 2119 — Key words for use in RFCs to Indicate Requirement Levels, S. Bradner, March 1997                                                                                                                                                                              |
| [RFC 3339]                             | RFC 3339 — Date and Time on the Internet: Timestamps, G. Klyne et al., July 2002                                                                                                                                                                                         |
| [RFC 7519]                             | RFC 7519 — JSON Web Token (JWT), M. Jones et al., May 2015                                                                                                                                                                                                               |
| [RFC 8610]                             | RFC 8610 — Concise Data Definition Language (CDDL): A Notational Convention to Express Concise Binary Object Representation (CBOR) and JSON Data Structures, H. Birkholz et al., June 2019                                                                               |
| [RFC 8943]                             | RFC 8943 — Concise Binary Object Representation (CBOR) Tags for Date, M. Jones et al., November 2020                                                                                                                                                                     |
| [RFC 8949]                             | RFC 8949 — Concise Binary Object Representation (CBOR), C. Bormann et al., December 2020                                                                                                                                                                                 |
| [SD-JWT VC]                            | SD-JWT-based Verifiable Credentials (SD-JWT VC). Available: https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/, version draft-ietf-oauth-sd-jwt-vc-09                                                                                                          |
| [Topic 7]                              | ARF Annex 2 - Topic 7 - Attestation revocation and revocation checking. Available: https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a237-topic-7-attestation-revocation-and-revocation-checking |