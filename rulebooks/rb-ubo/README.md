# Attestation Rulebook for attestations of type Ultimate Beneficial Owner (UBO)

* Author(s):
  * [Florin Coptil, Robert Bosch GmbH]
* Previous Authors

* Reviewer(s):
  * [Auth Sources]
    * [ ......Bundesanzeiger, Germany ]
    * [..... KVK, Holland ]
    * [ ..., Italy ]
  * [Banks]
    * [Bastek-Margon Jenny, CommerzBank ]
    * [Baumgardt Michaela, Commerzbank ]
    * [Stephan-A Fuchs, Deutsche Bank  ]

| Version | Date       | Description                                                     |
|---------|------------|-----------------------------------------------------------------|
| 0.1     | 13.03.2026 | Initial draft based on the WeBuild design attestations mettings |
| 0.2     | 20.04.2026 | updates in regard to the comments and legislation               |
| 0.3     | 09.05.2026 | regenerate chapter 1 and 2 in regard to address topics review   |
| 0.4     | 03.06.2026 | update after meeting                                            |

* Contact:
  * [Florin Coptil](mailto:florin.coptil@bosch.com)*

* Feedback:

---

## 1 Introduction

This attestation addresses the following question:

**Who are the Ultimate Beneficial Owners (UBOs) of a legal entity, and what is the nature and extent of their ownership or control?**

A UBO is defined as any natural person who ultimately owns or controls a legal entity based on :
- Ownership threshold — direct or indirect share ownership (typically 25%+)
- Control threshold — effective control through voting rights or other mechanisms

A Controller threshold is defined as any natural person or legal entity that directly or indirectly
exercises effective control over a legal entity. A single person may exercise control through
one or more control mechanisms simultaneously. Control is assessed based on the following
mechanisms:

- Voting Rights — direct or indirect holding of voting rights above the defined threshold
  (typically 25%+)
- Board Control — ability to appoint, remove, or control board members or board decisions
- Management / Executive Roles — executive authority enabling operational or strategic control
  over the entity
- Contractual Rights — veto, consent, or other contractual rights enabling decisive influence
  over corporate actions
- Special Shares — ownership of share classes with enhanced voting rights or disproportionate
  control powers
- Power to Appoint or Remove Management — statutory or contractual authority to appoint or
  dismiss key executives or directors
- Trustee Control — discretionary control exercised through trusts, foundations, or similar
  fiduciary arrangements
- Dominant Influence — control arising from financial, operational, or commercial dependency
  relationships
- Influence via Parent or Holding Company — indirect control exercised through ownership or
  control of an intermediary entity

as required under AMLR / AMLD6 and applicable company law.


The Ultimate Beneficial Owner (UBO) Attestation provides a standardized, verifiable
representation of the natural persons who ultimately own or control a legal entity. It enables
structured and trusted exchange of beneficial ownership data between organizations for use in
KYS (Know Your Supplier), KYC (Know Your Customer), Anti-Money Laundering (AML) compliance,
supplier onboarding, and regulatory due diligence processes.

### 1.1 Document scope and purpose

The UBO Attestation captures the essential attributes of a natural person who qualifies as an
ultimate beneficial owner of a legal entity — including personal identity, nationality,
residence, and the nature and degree of their ownership or control stake — in a machine-readable,
selectively disclosable format compliant with the EUDI Wallet framework.

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

| Term                        | Description                                                                                                                                                                          |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UBO                         | Ultimate Beneficial Owner — a natural person who ultimately owns or controls a legal entity, as defined under AMLR 2024/1624                                                         |
| NaturalPerson               | The natural person identified as a UBO, including their personal identity attributes                                                                                                 |
| BirthPlace                  | The place of birth of the natural person, including locality and country                                                                                                             |
| Citizenship                 | The nationality or nationalities held by the natural person                                                                                                                         |
| ResidenceAddress            | The registered residential address of the natural person                                                                                                                            |
| ContactAddress              | An optional alternative contact address for the natural person                                                                                                                      |
| NaturalPersonIdentifier     | A government-issued identity document (e.g., passport, national ID card) used to identify the natural person                                                                        |
| NaturalPersonUniqueIdentifier | An optional unique identifier issued by an authority to uniquely identify the natural person across systems                                                                        |
| Ownership                   | The object describing the nature and extent of the UBO's ownership or control stake in the legal entity                                                                              |
| direct_stake                | The percentage of direct ownership held by the UBO in the legal entity (0–100)                                                                                                      |
| indirect_stake              | The percentage of indirect ownership held by the UBO through intermediate entities (0–100)                                                                                          |
| direct_voting               | The percentage of direct voting rights held by the UBO in the legal entity (0–100)                                                                                                  |
| indirect_voting             | The percentage of indirect voting rights held by the UBO through intermediate entities (0–100)                                                                                      |
| qualifies                   | Boolean flag indicating whether the natural person qualifies as a real UBO (true) or does not qualify (false)                                                                       |
| qualification_reason        | The reason a natural person does not qualify as a UBO; NULL when qualifies = true                                                                                                   |
| KYC                         | Know Your Customer — due diligence process for verifying customer identity and assessing risk in financial relationships                                                              |
| KYS                         | Know Your Supplier — due diligence process for verifying supplier credentials, integrity, and risk exposure                                                                          |
| AML                         | Anti-Money Laundering — regulatory framework requiring financial institutions and obliged entities to identify and report suspicious activity                                         |
| AMLR                        | Anti-Money Laundering Regulation — EU Regulation 2024/1624 establishing harmonized AML/CFT rules across the EU                                                                      |
| ISO 3166-1                  | International standard defining country codes (alpha-2 and alpha-3 formats)                                                                                                         |
| ISO 8601                    | International standard for date and time representations (e.g., YYYY-MM-DD)                                                                                                         |
| ICAO 9303                   | International Civil Aviation Organization standard for travel documents, defining document types and number formats                                                                  |

---

## 2 Attestation attributes and metadata

The UBO Attestation is designed to provide a standardized, verifiable representation of the
natural persons who ultimately own or control a legal entity. It captures all essential
attributes required to identify a UBO, establish their nationality and residence, verify their
identity document, and describe the nature and extent of their ownership or control stake.

### 2.1 Introduction

**Data Model:**

```
UBO [1...n]
├── NaturalPerson
│   ├── first_name (M)
│   ├── surname (M)
│   └── date_of_birth (M)
├── BirthPlace
│   ├── locality (M)
│   ├── country (M)
│   └── region (O)
├── Citizenship
│   └── citizenship(s) [1..n] (M)
├── ResidenceAddress
│   ├── street (M)
│   ├── house_number (M)
│   ├── locality (M)
│   ├── region (M)
│   ├── postal_code (M)
│   └── country (M)
├── ContactAddress (optional)
│   ├── street (M)
│   ├── house_number (M)
│   ├── locality (M)
│   ├── region (M)
│   ├── postal_code (M)
│   └── country(s)
├── NaturalPersonIdentifier
│   ├── document_type (M)
│   ├── document_number (M)
│   ├── issuing_country (M)
│   └── expiry_date (M)
├── NaturalPersonUniqueIdentifier (optional)
│   ├── identifier_unique (O)
│   └── identifier_issuing_authority (O)
└── Ownership
    ├── qualifies (M)              — bool: true = real UBO identified, false = does not qualify
    ├── qualification_reason (M)   — below_threshold | no_ubo_identified | unverifiable | null (if qualifies = true)
    ├── direct_stake (M)           — % direct ownership (0–100)
    ├── indirect_stake (M)         — % indirect ownership (0–100)
    ├── direct_voting (M)          — % direct voting rights (0–100)
    ├── indirect_voting (M)        — % indirect voting rights (0–100)
    ├── determination_methodology (M)
    └── ownership_held_date (M)
```

**Explanation:**

- The attestation **MAY** contain one or more UBO entries (`[1...n]`), one per identified
  ultimate beneficial owner.
- `NaturalPerson`, `BirthPlace`, `Citizenship`, `ResidenceAddress`,
  `NaturalPersonIdentifier`, and `Ownership` are mandatory objects within each UBO entry.
- `ContactAddress` and `NaturalPersonUniqueIdentifier` are optional objects.
- `Citizenship` **SHALL** contain at least one citizenship entry and **MAY** contain multiple
  entries for persons holding multiple nationalities.
- `qualifies` is a boolean flag: `true` indicates a real UBO has been identified; `false`
  indicates the entity does not qualify under the applicable threshold or cannot be verified.
- `qualification_reason` **SHALL** be `null` when `qualifies = true`, and **SHALL** contain
  one of the defined enumerated values when `qualifies = false`.
- `direct_stake`, `indirect_stake`, `direct_voting`, and `indirect_voting` are expressed as
  percentage values between 0 and 100.

**Attestation Classification:**

This attestation type MAY be classified as:
- **"EAA"** when self-issued by the legal entity subject to the UBO disclosure obligation.
- **"QEAA"** when issued by a qualified trust service provider (QTSP) or authorized competent
  body (e.g., a notary, commercial register authority, or AML-supervised entity).

| **Data Identifier**   | **Semantic Reference** | **Definition**                                                              | **Data type** |
|-----------------------|------------------------|-----------------------------------------------------------------------------|---------|
| ubo_person            | ...                    | Information about the beneficial owner(s)                                   | Object  |
| ubo_birthplace        | ...                    | Information about the birth place                                           | Object  |
| ubo_citizenship       | ...                    | Citizenship(s) held by the UBO (one or more nationalities)                  | Array of Strings (ISO 3166-1 alpha-3)                                                   |
| ubo_residence_address | ...                    | Information about the residential address of the beneficial owner(s)        | Object  |
| ubo_contact_address   | ...                    | Information about the contact address of the beneficial owner(s) (optional) | Object  |
| ubo_identification    | ...                    | Information about the identification of the beneficial owner(s)             | Object  |
| ubo_ownership_info    | ...                    | Information about the stake information of the beneficial owner(s)          | Object  |

### 2.2 Mandatory attributes

#### NaturalPerson Attributes

| **Data Identifier** | **Semantic Reference** | **Definition**                                   | **Data type**          |
|---------------------|------------------------|--------------------------------------------------|------------------------|
| first_name          | —                      | First name(s) of the natural person              | String                 |
| surname             | —                      | Surname(s) / family name(s) of the natural person | String                |
| date_of_birth       | —                      | Date of birth of the natural person (ISO 8601)   | String (ISO 8601)      |

#### BirthPlace Attributes

| **Data Identifier** | **Semantic Reference** | **Definition**                                          | **Data type**          |
|---------------------|------------------------|---------------------------------------------------------|------------------------|
| locality            | —                      | City or locality of birth                               | String                 |
| country             | —                      | Country of birth (ISO 3166-1 alpha-2)                   | String (ISO 3166-1)    |

#### Citizenship Attributes

| **Data Identifier** | **Semantic Reference** | **Definition**                                                                 | **Data type**              |
|---------------------|------------------------|--------------------------------------------------------------------------------|----------------------------|
| citizenship         | —                      | Nationality or nationalities held by the natural person (ISO 3166-1 alpha-2)   | Array of Strings [1..n]    |

#### ResidenceAddress Attributes

| **Data Identifier** | **Semantic Reference** | **Definition**                                          | **Data type**          |
|---------------------|------------------------|---------------------------------------------------------|------------------------|
| street              | —                      | Street name of the residence address                    | String                 |
| house_number        | —                      | House or building number of the residence address       | String                 |
| locality            | —                      | City or locality of the residence address               | String                 |
| region              | —                      | Region or state of the residence address                | String                 |
| postal_code         | —                      | Postal code of the residence address                    | String                 |
| country             | —                      | Country of the residence address (ISO 3166-1 alpha-2)   | String (ISO 3166-1)    |

#### NaturalPersonIdentifier Attributes

| **Data Identifier** | **Semantic Reference** | **Definition**                                                                    | **Data type**          |
|---------------------|------------------------|-----------------------------------------------------------------------------------|------------------------|
| document_type       | —                      | Type of identity document (e.g., PASSPORT, NATIONAL_ID, RESIDENCE_PERMIT)        | String (Enum)          |
| document_number     | —                      | Number of the identity document as printed on the document                        | String                 |
| issuing_country     | —                      | Country that issued the identity document (ISO 3166-1 alpha-2)                    | String (ISO 3166-1)    |
| expiry_date         | —                      | Expiry date of the identity document (ISO 8601 YYYY-MM-DD)                        | String (ISO 8601)      |

#### Ownership Attributes

| **Data Identifier**          | **Semantic Reference** | **Definition**                                                                                                        | **Data type**  |
|------------------------------|------------------------|-----------------------------------------------------------------------------------------------------------------------|----------------|
| qualifies                    | —                      | Boolean: true = real UBO identified; false = does not qualify as UBO                                                 | Boolean        |
| qualification_reason         | —                      | Reason for non-qualification; SHALL be null if qualifies = true; one of: below_threshold, no_ubo_identified, unverifiable | String (Enum) |
| direct_stake                 | —                      | Percentage of direct ownership held by the UBO in the legal entity (0–100)                                           | Decimal (0–100) |
| indirect_stake               | —                      | Percentage of indirect ownership held by the UBO through intermediate entities (0–100)                               | Decimal (0–100) |
| direct_voting                | —                      | Percentage of direct voting rights held by the UBO in the legal entity (0–100)                                       | Decimal (0–100) |
| indirect_voting              | —                      | Percentage of indirect voting rights held by the UBO through intermediate entities (0–100)                           | Decimal (0–100) |
| determination_methodology    | —                      | Description of the method used to determine the UBO and the ownership/control percentages                            | String          |
| ownership_held_date          | —                      | Date from which the ownership or control has been held (ISO 8601 YYYY-MM-DD)                                         | String (ISO 8601) |

### 2.3 Optional attributes

#### BirthPlace Optional Attributes

| **Data Identifier** | **Semantic Reference** | **Definition**                                    | **Data type** |
|---------------------|------------------------|---------------------------------------------------|---------------|
| region              | —                      | Region or state of birth; optional                | String        |

#### ContactAddress Attributes

| **Data Identifier** | **Semantic Reference** | **Definition**                                               | **Data type**       |
|---------------------|------------------------|--------------------------------------------------------------|---------------------|
| street              | —                      | Street name of the contact address                           | String              |
| house_number        | —                      | House or building number of the contact address              | String              |
| locality            | —                      | City or locality of the contact address                      | String              |
| region              | —                      | Region or state of the contact address                       | String              |
| postal_code         | —                      | Postal code of the contact address                           | String              |
| country             | —                      | Country of the contact address (ISO 3166-1 alpha-2)          | String (ISO 3166-1) |

#### NaturalPersonUniqueIdentifier Optional Attributes

| **Data Identifier**              | **Semantic Reference** | **Definition**                                                                         | **Data type** |
|----------------------------------|------------------------|----------------------------------------------------------------------------------------|---------------|
| identifier_unique                | —                      | A unique identifier assigned to the natural person by an issuing authority; optional   | String        |
| identifier_issuing_authority     | —                      | The authority that issued the unique identifier; optional                              | String        |

### 2.4 Conditional attributes

| **Data Identifier**    | **Condition**                                                                         | **Definition**                                                                                      | **Data type**  |
|------------------------|---------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|----------------|
| qualification_reason   | **SHALL** be null if `qualifies = true`; **SHALL** contain an enumerated value if `qualifies = false` | Reason why the natural person does not qualify as a UBO under the applicable threshold | String (Enum)  |

### 2.5 Mandatory metadata

| **Data Identifier**        | **Definition**                                                                                                                                                     | **Data type** |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| issuance_date              | The date and time when the attestation was issued (ISO 8601)                                                                                                       | DateTime      |
| expiry_date                | The date and time when the attestation expires (ISO 8601)                                                                                                          | DateTime      |
| issuing_entity             | The identifier of the legal entity that issued the attestation (typically the subject entity itself for self-issued attestations, or the QTSP identifier for QEAA) | String        |
| attestation_legal_category | Indicates the legal category of this attestation ("EAA" or "QEAA")                                                                                                | String        |
| vct                        | A URI or other collision-resistant identifier that defines the type of the SD-JWT Verifiable Credential                                                            | String        |

### 2.6 Optional metadata

| **Data Identifier** | **Definition**                                                             | **Data type** |
|---------------------|----------------------------------------------------------------------------|---------------|
| trust_anchor_url    | URL where the trust anchor for verifying this attestation can be retrieved | URI           |
| schema_version      | Version of the schema used                                                 | String        |

### 2.7 Conditional metadata

No conditional metadata elements are defined for this attestation type.

### 2.8 Value Lists

#### 2.8.1 Document Type Codes

The `document_type` attribute SHALL use one of the following standardized values:

| **Code**          | **Definition**                                            |
|-------------------|-----------------------------------------------------------|
| PASSPORT          | International passport as defined by ICAO 9303            |
| NATIONAL_ID       | National identity card issued by a competent authority    |
| RESIDENCE_PERMIT  | Residence permit issued to foreign nationals              |
| DRIVING_LICENSE   | Driving licence accepted as identity document             |
| OTHER             | Any other government-issued identity document             |

#### 2.8.2 Qualification Reason Codes

The `qualification_reason` attribute SHALL use one of the following standardized values when
`qualifies = false`:

| **Code**             | **Definition**                                                                                                            |
|----------------------|---------------------------------------------------------------------------------------------------------------------------|
| below_threshold      | No natural person holds ownership or voting rights above the applicable AML threshold (typically 25%)                    |
| no_ubo_identified    | No natural person could be identified as exercising ultimate control through other means                                  |
| unverifiable         | The ownership or control structure could not be sufficiently verified to identify a UBO                                   |

#### 2.8.3 Country Codes

The `country` attributes within `BirthPlace`, `ResidenceAddress`, `ContactAddress`,
`Citizenship`, and `NaturalPersonIdentifier` SHALL follow **ISO 3166-1 alpha-2** country codes.

| **Code** | **Definition** |
|----------|----------------|
| DE       | Germany        |
| FR       | France         |
| NL       | Netherlands    |
| CH       | Switzerland    |
| GB       | United Kingdom |

For a complete list, refer to the ISO 3166-1 alpha-2 standard.


### 2.8.4 Determination Methodology Codes
The determination_methodology attribute SHALL use one or more of the following standardized values, aligned with AMLR Article 3(17) and the proposed Implementing Act:

*a) Type of Ownership:*

| **Code**             | **Definition**                                                                                                                    |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Direct ownership     | The UBO holds ≥25% of shares, voting rights, or ownership interests directly in the subject entity, without intermediary entities |
| Indirect ownership   | The UBO holds ≥25% of shares, voting rights, or ownership interests indirectly through one or more intermediary legal entities    |

*b) Legal Arrangement (for trusts, foundations, and similar structures):*

| **Code**          | **Definition**                                                                                                                                                                                                                     |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Settlor           | The UBO is the settlor (creator) of a trust or similar legal arrangement                                                                                                                                                           |
| Trustee           | The UBO is the trustee of a trust or similar legal arrangement                                                                                                                                                                     |
| Beneficiary       | The UBO is a beneficiary of a trust or similar legal arrangement                                                                                                                                                                   |
| Object of a power | The UBO is the object of a power in a legal arrangement                                                                                                                                                                            |
| Default taker     | The UBO is the default taker (residual beneficiary) of a legal arrangement                                                                                                                                                         |
| Protector         | The UBO is the protector of a trust or similar legal arrangement                                                                                                                                                                   |
| Other             | person exercising ultimate control over legal arrangement Any other natural person exercising ultimate control over the legal arrangement (direct, indirect, or by other means, including through a chain of control or ownership) |

*c) Nature of Control (for control through means other than ownership percentage):*

| **Code**                                             | **Definition**                                                                                                                                                 |
|------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Control through ownership                            | Control exercised through ownership of shares/capital (overlaps with "Direct ownership" / "Indirect ownership" but emphasizes control aspect)                  |
| Control through voting rights                        | Control exercised through voting rights that exceed ownership percentage (e.g., special shares with enhanced voting rights)                                    |
| Control through right of appointments                | Control exercised through the right to appoint or remove directors, senior management, or other key decision-makers                                            |
| Control through veto rights                          | Control exercised through veto rights over major corporate decisions (e.g., M&A, capital increases, dissolution)                                               |
| Control through distribution of profits              | Control exercised through the right to control the distribution of profits (e.g., special dividend rights)                                                     |
| Control through formal or informal agreements        | Control exercised through formal agreements (e.g., shareholders' agreements, management agreements) or informal arrangements                                   |
| Control through relationships between family members | Control exercised through coordinated action among family members (acting in concert)                                                                          |
| Control through acting in concert                    | Control exercised through acting in concert with other shareholders or stakeholders                                                                            |
| Control through nominee arrangements                 | Control exercised through nominee shareholders, nominee directors, or other nominee arrangements where the UBO is the beneficial controller behind the nominee |

Note: Multiple determination methodologies MAY apply to a single UBO. For example, a UBO may be identified through:
"Direct ownership" (30% direct shareholding) AND
"Control through voting rights" (50% voting rights via special shares) AND
"Control through right of appointments" (contractual right to appoint CEO)

In such cases, determination_methodology SHOULD be encoded as an array containing all applicable codes._

### 2.9 Integrity Rules

The following integrity rules SHALL be enforced:

- Each UBO entry **SHALL** contain exactly one `NaturalPerson`, one `BirthPlace`, one
  `Citizenship`, one `ResidenceAddress`, one `NaturalPersonIdentifier`, and one `Ownership`
  object.
- `first_name` **SHALL** be a non-empty string.
- `surname` **SHALL** be a non-empty string.
- `date_of_birth` **SHALL** be a valid ISO 8601 date (YYYY-MM-DD) in the past.
- `BirthPlace.locality` **SHALL** be a non-empty string.
- `BirthPlace.country` **SHALL** be a valid ISO 3166-1 alpha-2 country code.
- `Citizenship` **SHALL** contain at least one non-empty ISO 3166-1 alpha-2 country code.
- All address objects (`ResidenceAddress`, `ContactAddress`) **SHALL** contain non-empty
  values for all mandatory fields (`street`, `house_number`, `locality`, `region`,
  `postal_code`, `country`).
- `ResidenceAddress.country` **SHALL** be a valid ISO 3166-1 alpha-2 country code.
- `document_type` **SHALL** use one of the enumerated values defined in Section 2.8.1.
- `document_number` **SHALL** be a non-empty string.
- `issuing_country` **SHALL** be a valid ISO 3166-1 alpha-2 country code.
- `expiry_date` in `NaturalPersonIdentifier` **SHALL** be a valid ISO 8601 date (YYYY-MM-DD).
- `qualifies` **SHALL** be a boolean value (`true` or `false`).
- `qualification_reason` **SHALL** be `null` when `qualifies = true`.
- `qualification_reason` **SHALL** be one of the enumerated values from Section 2.8.2 when
  `qualifies = false`.
- `direct_stake`, `indirect_stake`, `direct_voting`, and `indirect_voting` **SHALL** each be
  a decimal value between 0 and 100 inclusive.
- `determination_methodology` **SHALL** be a non-empty string.
- `ownership_held_date` **SHALL** be a valid ISO 8601 date (YYYY-MM-DD) in the past.
- `issuance_date` and `expiry_date` (metadata) **SHALL** be valid ISO 8601 DateTimes.
- `expiry_date` **SHALL** be later than `issuance_date`.
- `attestation_legal_category` **SHALL** be one of `"EAA"` or `"QEAA"`.
- `vct` **SHALL** be a non-empty string conforming to a URL or URN format.
- Each attribute **SHALL** appear at most once within its respective object scope.

---

## 3 Attestation encoding

### 3.1 ISO/IEC 18013-5-compliant encoding

ISO/IEC 18013-5 (also called mdoc) is out of scope for this Rulebook, as offline proximity
presentation is not a current requirement for the UBO attestation.

### 3.2 SD-JWT VC-based encoding

The UBO attestation uses the SD-JWT VC format to allow for selective disclosure of UBO
attributes.

**Selective Disclosure:** Claims within each UBO entry SHALL be individually selectively
disclosable, enabling a legal entity to disclose only the attributes requested by a Relying
Party. Sensitive personal attributes such as `date_of_birth`, `document_number`, and address
details SHALL be individually disclosable.

The `.` notation is used to indicate the nesting of attributes.

**Verifiable Credential Type (`vct`):** `vct: eu.we-build.ubo.1`

#### 3.2.1 Attribute Encoding Table

**NaturalPerson**

| **Data Identifier**               | **Attribute identifier**                                  | **Encoding format**          | **Reference/Notes**                                                               | **Disclosable** |
|-----------------------------------|-----------------------------------------------------------|------------------------------|-----------------------------------------------------------------------------------|-----------------|
| ubo                               | `ubo`                                                     | Array [UBO]                  | Array of UBO objects; **SHALL** contain at least one UBO.                         | MUST            |
| **Person**                        |                                                           |                              |                                                                                   |                 |
| first_name                        | ubo[n].natural_person.first_name                          | String                       | First name(s) of the natural person                                               | MUST            |
| surname                           | ubo[n].natural_person.surname                             | String                       | Surname(s) of the natural person                                                  | MUST            |
| date_of_birth                     | ubo[n].natural_person.date_of_birth                       | String (ISO 8601 YYYY-MM-DD) | Date of birth; SHALL be in the past                                               | MUST            |
| **BirthPlace**                    |                                                           |                              |                                                                                   |                 |
| locality                          | ubo[n].birth_place.locality                               | String                       | City or locality of birth                                                         | MUST            |
| country                           | ubo[n].birth_place.country                                | String (ISO 3166-1 alpha-2)  | Country of birth                                                                  | MUST            |
| region                            | ubo[n].birth_place.region                                 | String                       | Region or state of birth; optional                                                | MAY             |
| **Citizenship**                   |                                                           |                              |                                                                                   |                 |
| citizenship                       | ubo[n].citizenship                                        | Array of Strings             | Nationality or nationalities; ISO 3166-1 alpha-2; SHALL contain at least one      | MUST            |
| **ResidenceAddress**              |                                                           |                              |                                                                                   |                 
| street                            | ubo[n].residence_address.street                           | String                       | Street name of the residence address                                              | MUST            |
| house_number                      | ubo[n].residence_address.house_number                     | String                       | House number of the residence address                                             | MUST            |
| locality                          | ubo[n].residence_address.locality                         | String                       | City or locality of the residence address                                         | MUST            |
| region                            | ubo[n].residence_address.region                           | String                       | Region of the residence address                                                   | MUST            |
| postal_code                       | ubo[n].residence_address.postal_code                      | String                       | Postal code of the residence address                                              | MUST            |
| country                           | ubo[n].residence_address.country                          | String (ISO 3166-1 alpha-2)  | Country of the residence address                                                  | MUST            |
| **ContactAddress**                |                                                           |                              |                                                                                   |
| street                            | ubo[n].contact_address.street                             | String                       | Street name of the contact address; optional                                      | MAY             |
| house_number                      | ubo[n].contact_address.house_number                       | String                       | House number of the contact address; optional                                     | MAY             |
| locality                          | ubo[n].contact_address.locality                           | String                       | Locality of the contact address; optional                                         | MAY             |
| region                            | ubo[n].contact_address.region                             | String                       | Region of the contact address; optional                                           | MAY             |
| postal_code                       | ubo[n].contact_address.postal_code                        | String                       | Postal code of the contact address; optional                                      | MAY             |
| country                           | ubo[n].contact_address.country                            | String (ISO 3166-1 alpha-2)  | Country of the contact address; optional                                          | MAY             |
| **NaturalPersonIdentifier**       |                                                           |                              |                                                                                   |
| document_type                     | ubo[n].natural_person_identifier.document_type            | String (Enum)                | Type of identity document; SHALL use values from Section 2.8.1                    | MUST            |
| document_number                   | ubo[n].natural_person_identifier.document_number          | String                       | Document number as printed on the identity document                               | MUST            |
| issuing_country                   | ubo[n].natural_person_identifier.issuing_country          | String (ISO 3166-1 alpha-2)  | Country that issued the identity document                                         | MUST            |
| expiry_date                       | ubo[n].natural_person_identifier.expiry_date              | String (ISO 8601 YYYY-MM-DD) | Expiry date of the identity document                                              | MUST            |
| **NaturalPersonUniqueIdentifier** |                                                           |                              |                                                                                   |
| identifier_unique                 | ubo[n].natural_person_unique_identifier.identifier_unique | String                       | Unique identifier assigned by an authority; optional                              | MAY             |
| identifier_issuing_authority      | ubo[n].natural_person_unique_identifier.issuing_authority | String                       | Authority that issued the unique identifier; optional                             | MAY             |
| **Ownership**                     |                                                           |                              |                                                                                   |
| qualifies                         | ubo[n].ownership.qualifies                                | Boolean                      | true = real UBO identified; false = does not qualify                              | MUST            |
| qualification_reason              | ubo[n].ownership.qualification_reason                     | String (Enum)                | Reason for non-qualification; null if qualifies = true; values from Section 2.8.2 | MUST            |
| direct_stake                      | ubo[n].ownership.direct_stake                             | Decimal (0–100)              | Percentage of direct ownership (0–100)                                            | MUST            |
| indirect_stake                    | ubo[n].ownership.indirect_stake                           | Decimal (0–100)              | Percentage of indirect ownership (0–100)                                          | MUST            |
| direct_voting                     | ubo[n].ownership.direct_voting                            | Decimal (0–100)              | Percentage of direct voting rights (0–100)                                        | MUST            |
| indirect_voting                   | ubo[n].ownership.indirect_voting                          | Decimal (0–100)              | Percentage of indirect voting rights (0–100)                                      | MUST            |
| determination_methodology         | ubo[n].ownership.determination_methodology                | String                       | Method used to determine the UBO and the ownership/control percentages            | MUST            |
| ownership_held_date               | ubo[n].ownership.ownership_held_date                      | String (ISO 8601 YYYY-MM-DD) | Date from which the ownership or control has been held                            | MUST            |
| **Metadata**                      |                                                           |                              |                                                                                   |
| issuance_date                     | iat                                                       | Number (Unix timestamp)      | Date and time when the attestation was issued (ISO 8601); RFC 7519                | MUST NOT        |
| expiry_date                       | exp                                                       | Number (Unix timestamp)      | Date and time when the attestation expires (ISO 8601); RFC 7519                   | MUST NOT        |
| issuing_entity                    | iss                                                       | String (URI or DID)          | Identifier of the entity that issued the attestation; RFC 7519                    | MUST NOT        |
| attestation_legal_category        | attestation_legal_category                                | String                       | One of EAA or QEAA as defined by eIDAS 2                                          | MUST NOT        |
| vct                               | vct                                                       | String                       | A URI or other collision-resistant identifier for the credential type             | MUST NOT        |
| schema_version                    | schema_version                                            | String                       | Version of the schema used; optional                                              | MAY             |
| trust_anchor_url                  | trust_anchor_url                                          | String (URI)                 | URL where the trust anchor for verifying this attestation can be retrieved        | MAY             |

**Notes:**

- **MUST**: The claim SHALL be selectively disclosable — the holder MAY choose to disclose or
  withhold this claim when presenting the credential to a Relying Party.
- **MAY**: The claim MAY be selectively disclosable if the issuer supports it; the holder can
  choose to disclose or withhold.
- **MUST NOT**: The claim SHALL NOT be selectively disclosable — it is always present in plain
  text in the JWT header/payload and cannot be withheld by the holder, as it is required for
  credential verification and trust establishment.
- `iat`, `exp`, and `iss` follow RFC 7519 standard JWT claim naming conventions.
- The attestation MAY contain multiple UBO entries, each indexed as `ubo[n]`.

#### 3.2.2 Status Claim

For SD-JWT VC-compliant UBO attestations, the attestation MUST include a `status` claim if the
technical validity period is greater than 24 hours. This claim enables Relying Parties to
determine if a credential has been revoked via a status list mechanism, as specified in SD-JWT VC.

The `status` claim SHALL be a JSON object with the following members:

- `type` (string): SHALL be `"status-list"`.
- `status_list_credential` (string, URI): The URI of the Status List Credential document that
  contains the status bitstring.
- `status_list_index` (integer, >= 0): The zero-based index into the status list bitstring that
  corresponds to this credential.
- `status_purpose` (string): SHALL be `"revocation"` for this attestation.

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

The following is a non-normative example of a UBO SD-JWT VC payload:

```json
{
  "vct": "eu.we-build.ubo.1",
  "iss": "https://issuer.example.com",
  "iat": 1736935200,
  "exp": 1768471200,
  "issuing_entity": "did:example:legal-entity-789",
  "attestation_legal_category": "EAA",
  "schema_version": "0.1.0",
  "trust_anchor_url": "https://trust.webuildconsortium.eu/anchors/eidas-tl",

  "ubo": [
    {
      "natural_person": {
        "first_name": "Anna",
        "surname": "Müller",
        "date_of_birth": "1978-04-15"
      },
      "birth_place": {
        "locality": "Munich",
        "country": "DE",
        "region": "Bavaria"
      },
      "citizenship": ["DE"],
      "residence_address": {
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
      "natural_person_identifier": {
        "document_type": "PASSPORT",
        "document_number": "C01X00T47",
        "issuing_country": "DE",
        "expiry_date": "2030-04-14"
      },
      "natural_person_unique_identifier": {
        "identifier_unique": "DE-12345678",
        "identifier_issuing_authority": "Bundesamt für Justiz"
      },
      "ownership": {
        "qualifies": true,
        "qualification_reason": null,
        "direct_stake": 35.0,
        "indirect_stake": 10.0,
        "direct_voting": 35.0,
        "indirect_voting": 10.0,
        "determination_methodology": "Share register review and corporate structure analysis conducted by external AML officer",
        "ownership_held_date": "2015-03-01"
      }
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