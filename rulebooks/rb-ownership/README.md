# Attestation Rulebook for attestations of type Ownership Attestation

* Author(s):
  * [Florin Coptil, Robert Bosch GmbH]
  * [Stephan Fuchs, Deutsche Bank AG]

* Reviewer(s):
  * [Baumgardt Michaela, Commerzbank]
  * [Ricky Lamberty, Robert Bosch GmbH]
  * @TODO Florin — Add the reviewers from attestation design (meetings UseCase, Banks, TransparentRegister)

| Version | Date       | Description                                                                            |
|---------|------------|----------------------------------------------------------------------------------------|
| 0.1     | 23.03.2026 | Initial draft based on the WeBuild design attestations meetings                        |
| 0.2     | 10.05.2026 | Updates for addresses and identifiers                                                  |
| 0.4     | 01.06.2026 | Updates of content - legal arrangements                                                |
| 0.7     | 24.06.2026 | Updates of content based on the submission regulation and AMLR/RTS and BODS vocabulary |
| 0.8     | 29.06.2026 | Updates of BODS vocabulary                                                             |
| 0.9     | 03.07.2026 | Updates in regard trust and revocation                            |

* Contact:
  * [Florin Coptil](mailto:florin.coptil@bosch.com)* 

* Feedback:

## 1 Introduction

This attestation addresses the following question:

**Who are the Shareholders and Economic Interest Holders of this legal entity?**

A Shareholder or Economic Interest Holder is any natural person, legal entity, or legal
arrangement that directly or indirectly holds an ownership stake or economic interest in a
legal entity.

### 1.1 Document Scope and Purpose

The Ownership Attestation records all natural persons, legal entities, and legal arrangements
holding direct or indirect ownership interests in a legal entity, providing comprehensive
transparency on beneficial ownership structures and economic interests. This attestation is a
critical component of both Know Your Customer (KYC) and Know Your Supplier (KYS) processes
within the EUDI Wallet ecosystem, supporting effective risk management, regulatory compliance,
and anti-money laundering (AML) obligations.

**Design Decisions**

This Ownership Attestation Rulebook is based on:
- AMLR – Regulation (EU) 2024/1624 of the European Parliament and of the Council of 31 May 2024 on the prevention of the use of the financial system for the purposes of money laundering or terrorist financing.
- The EU Anti-Money Laundering Regulation (AMLR 2024/1624) as the primary regulatory driver for beneficial ownership transparency obligations
- The EUDI Wallet ecosystem and eIDAS 2 framework as the digital identity infrastructure
- The SD-JWT VC specification (draft-ietf-oauth-sd-jwt-vc-09) for verifiable credential
  encoding
- Regulatory Technical Standards (RTS) – Draft Regulatory Technical Standards under Article 28(1) of Regulation (EU) 2024/1624, specifying the requirements for identifying beneficial owners and the information to be collected for beneficial ownership determination.
- Beneficial Ownership Submission Regulation – Commission on Implementing Regulation (EU) [number] on the formats for submitting beneficial ownership information.
- Beneficial Ownership Data Standard (BODS) version 0.4

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

| Term                                               | Definition                                                                                                                                                                                              |
|----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ownership                                          | A comprehensive record of all natural and legal persons holding direct or indirect ownership or control in a legal entity, including ownership percentages and supporting evidence                      |
| Beneficial Owner / Ultimate Beneficial Owner (UBO) | A natural person who ultimately owns or controls a legal entity, either directly or indirectly (typically defined as holding ≥25% ownership or control, per AMLD requirements)                          |
| Direct Ownership                                   | Ownership interest held directly by a natural or legal person in the subject entity, without intermediary entities                                                                                      |
| Indirect Ownership                                 | Ownership interest held through one or more intermediary legal entities (e.g., Person A owns 50% of Company B, which owns 60% of Company C → Person A has 30% indirect ownership in Company C)          |
| Total Ownership                                    | The sum of direct and indirect ownership percentages across all layers of the ownership structure                                                                                                       |
| Ownership Category                                 | Classification of the type of ownership or control relationship (e.g., shareholder, controller via voting rights, trustee, partner, holder of convertible rights, person exercising dominant influence) |
| Legal Entity Identifier Chain                      | The list of all intermediate legal entities through which indirect ownership is held, enabling full traceability of ownership layers                                                                    |
| KYC                                                | Know Your Customer – due diligence process for verifying customer identity and assessing risk in financial relationships                                                                                |
| KYS                                                | Know Your Supplier – due diligence process for verifying supplier credentials, integrity, and risk exposure                                                                                             |
| PEP                                                | Politically Exposed Person – individual entrusted with prominent public functions, posing higher risk for corruption or bribery                                                                         |
| EUCC                                               | EU Company Certificate – attestation establishing the legal existence and identity of a legal entity within the EU                                                                                      |
| Evidence                                           | Supporting documentation substantiating the ownership structure (e.g., shareholder register, organizational chart, trust deed)                                                                          |
| Legal Arrangement                                  | A non-corporate structure (e.g., trust, foundation, fiduciary arrangement) used to hold assets or exercise control over a legal entity                                                                  |
| Identifier                                         | A formal reference code used to uniquely identify a legal entity (e.g., EUID, LEI, national tax or registry number)                                                                                     |

## 2 Attestation Attributes and Metadata

The Ownership Attestation is designed to provide a complete, verifiable representation of an
entity's ownership structure in a standardised digital format. This attestation supports
transparency, compliance, and risk management by enabling automated verification of beneficial
ownership across complex, multi-tiered corporate structures.

### 2.1 Introduction

The Owner model supports three distinct owner types: 
- natural persons (`Person`), 
- legal entities(`Entity`), 
- and legal arrangements (a subtype of `Entity` — e.g., trusts, foundations).

**Data Model:**

The Owner model follows a hierarchical structure:
```
Owner [1..n]                                    // The person or entity that holds an interest
├─ type (enum) (M)                              // "Person" | "Entity"
├─ jurisdiction (tstr) (M)                      // ISO 3166-1 alpha-2
├─ person (O, conditional on type="Person")
│   ├─ first_name (tstr) (M)
│   ├─ surname (tstr) (M)
│   └─ birth_date (date) (O)                    // ISO 8601 YYYY-MM-DD
├─ entity (O, conditional on type="Entity")
│   ├─ category (enum) (M)                      // "legal_entity" | "legal_arrangement"
│   ├─ name (tstr) (M)
│   ├─ identifier [1..n] (M)                    // At least one identifier required
│   │   ├─ euid (str) (O)                       // European Unique Identifier
│   │   ├─ lei (str) (O)                        // Legal Entity Identifier per ISO 17442
│   │   ├─ tax (str) (O)                        // National tax or registration number
│   │   └─ other (str) (O)                      // Any other applicable identifier
│   ├─ jurisdiction (tstr) (M)                  // ISO 3166-1 alpha-2
│   ├─ form (tstr) (M)                          // See Section 2.8.6
│   └─ subtype_info (object) (O)                // Mandatory when category = "legal_arrangement"
│       ├─ settlement (tstr) (M)                // Founding instrument or trust deed
│       ├─ purpose (tstr) (M)                   // Declared purpose of the arrangement
│       ├─ assets (tstr) (M)                    // Assets held within the arrangement
│       └─ reason_for_registration (tstr) (O)   // Optional reason for formal registration
├─ address (Address) (M)                        // Residential (Person) or registered (Entity)
│   ├─ street (tstr) (M)
│   ├─ house_number (tstr) (M)
│   ├─ locality (tstr) (M)
│   ├─ region (tstr) (M)
│   ├─ postal_code (tstr) (M)
│   └─ country (tstr) (M)                       // ISO 3166-1 alpha-2
├─ interests (M)                                // Details of the economic or control interest
│   ├─ type [enum] [1..n] (M)                   // Array — see Section 2.8.5
│   ├─ level (tstr) (M)                         // "direct" | "indirect" | "joint" | "unknown"
│   ├─ percentage (Decimal) (M)                 // Ownership percentage (0–100)
│   ├─ quantity (uint) (M)                      // Number of shares or units held
│   ├─ description (tstr) (O)                   // Free-text description of the interest
│   ├─ class (tstr) (O)                         // "ordinary" | "preferred" | "dual-class" | "other"
│   └─ rights [String] [1..n] (M)              // "dividend_rights" | "liquidation_rights"
├─ effective_date (date) (M)                    // ISO 8601 YYYY-MM-DD
└─ evidence [1..n] (M)                          // At least one evidence entry required
│  ├─ id (tstr) (M)                            // Unique identifier, URI, or URN
│  ├─ type (tstr) (M)                          // Evidence type — see Section 2.8.9
│  ├─ url (uri) (O)                            // URI to publicly accessible source document
│  └─ data (base64) (O)                        // Base64-encoded — required if url absent
```
*Note*: M - mandatory / O - optional.

**Explanation:**
- The attestation SHALL contain at least one `Owner` entry of `type = "Person"` to comply with
  AML requirements mandating identification of the natural persons who ultimately own or control
  the entity (Ultimate Beneficial Owners).
- The attestation MAY contain zero or more `Owner` entries of `type = "Entity"` representing
  intermediate legal entities or legal arrangements in the ownership chain.
- Each `Owner` entry SHALL include:
  - `type` (mandatory enum: `"Person"` or `"Entity"`)
  - `jurisdiction` (mandatory — ISO 3166-1 alpha-2)
  - `address` (mandatory — residential address for `Person`, registered address for `Entity`)
  - `interests` (mandatory — at least one record)
  - `effective_date` (mandatory — date when this ownership or control became effective)
  - `evidence` (mandatory — at least one piece of supporting evidence)

- For each `Owner` of `type = "Person"`:
  - The `person` object SHALL be present and the `entity` object SHALL be absent.
  - `first_name` and `surname` SHALL be present.
  - `birth_date` SHALL be present (ISO 8601 YYYY-MM-DD).
  - At least one `interests` record SHALL be present, including:
    - `type` — SHALL use values from Section 2.8.5
    - `level` — SHALL use values from Section 2.8.2
    - `percentage` — decimal value in range 0–100
    - `quantity` — non-negative integer
    - `rights` — SHALL use values from Section 2.8.3

- For each `Owner` of `type = "Entity"`:
  - The `entity` object SHALL be present and the `person` object SHALL be absent.
  - `category` SHALL be present and SHALL be one of `"legal_entity"` or `"legal_arrangement"`.
  - `name` SHALL be present (complete official registered name).
  - `identifier` SHALL contain at least one of: `euid`, `lei`, `tax`, or `other`.
  - `jurisdiction` SHALL be present (ISO 3166-1 alpha-2).
  - `form` SHALL be present and SHALL use a value from Section 2.8.6.
  - At least one `interests` record SHALL be present, including:
    - `type` — SHALL use values from Section 2.8.5
    - `level` — SHALL use values from Section 2.8.2
    - `percentage` — decimal value in range 0–100
    - `quantity` — non-negative integer
    - `rights` — SHALL use values from Section 2.8.3

- When `entity.category = "legal_arrangement"` OR `entity.form = "trust"`, the `subtype_info`
  object SHALL be present and SHALL include:
  - `settlement` — the instrument establishing the legal arrangement
  - `purpose` — the declared purpose of the arrangement
  - `assets` — description of assets held within the arrangement
  - `reason_for_registration` is OPTIONAL

- Each `Owner` entry SHALL include at least one `evidence` entry. Each evidence entry
  SHALL include:
  - `id` — unique identifier, URI, or URN of the source document
  - `type` — SHALL use values from Section 2.8.9
  - `data` — base64-encoded document — SHALL be provided if `url` is absent or not publicly
    accessible

- `interests.type` SHALL be an array allowing multiple concurrent role types to be declared for
  a single owner (e.g., a person may simultaneously hold `shareholding` and `votingRights`).
- `interests.level` SHALL use one of: `"direct"`, `"indirect"`, `"joint"`, or `"unknown"` as
  defined in Section 2.8.2.
- `interests.rights` SHALL be an array and SHALL use values from Section 2.8.3.
- `interests.class` (optional) SHALL use a value from Section 2.8.1 when applicable.
- `effective_date` SHALL follow ISO 8601 YYYY-MM-DD format and SHALL represent the date on
  which the ownership or control relationship became legally effective.

**Attestation Classification:**

This attestation type MAY be classified as:
- **`EAA`** within the EUBW Wallet ecosystem, when self-issued by the legal entity subject to
  the ownership disclosure (i.e., the entity issues an attestation about its own ownership
  structure).
- **`QEAA`** when issued by a qualified trust service provider (QTSP) or authorized competent
  body that can independently attest the ownership structure (e.g., based on official company
  register data, audited financial statements, or notarized documentation).

#### Terms primarily relevant to a `Person` Owner

These terms describe natural persons who hold ownership or economic interests in a legal entity.

**Person Ownership Role Terms**

| **Term**                   | **Reference**                                            | **Definition in Ownership Context**                                                |
|----------------------------|----------------------------------------------------------|------------------------------------------------------------------------------------|
| `registered_shareholder`   | `interests[].type: shareholding`                         | A natural person formally registered as a shareholder                              |
| `nominee_shareholder`      | `interests[].type: nomineeShareholding`                  | A person holding shares on behalf of the actual beneficial owner                   |
| `nominator`                | `interests[].type: nomineeShareholding`                  | The natural person who is the actual beneficial owner behind a nominee arrangement |
| `settlor`                  | `interests[].type: settlor`                              | A natural person who creates and transfers assets into a trust                     |
| `trustee_individual`       | `interests[].type: trustee`                              | A natural person appointed to administer a trust                                   |
| `protector`                | `interests[].type: protector`                            | A natural person appointed to oversee or protect a trust structure                 |
| `beneficiary_individual`   | `interests[].type: beneficiaryOfLegalArrangement`        | A natural person who benefits from a trust or legal arrangement                    |
| `senior_managing_official` | `interests[].type: seniorManagingOfficial`               | A natural person exercising control through a senior management position           |
| `rights_holder`            | `interests[].type: rightsGrantedByContract`              | A natural person holding economic rights granted by contract                       |

**Person Interest Detail Terms**

| **Term**             | **Reference**                     | **Definition in Ownership Context**                              |
|----------------------|-----------------------------------|------------------------------------------------------------------|
| `direct_ownership`   | `interests[].level: direct`       | The person directly holds shares or economic rights              |
| `indirect_ownership` | `interests[].level: indirect`     | The person holds ownership through one or more intermediaries    |
| `joint_ownership`    | `interests[].level: joint`        | Ownership is shared jointly with one or more persons or entities |
| `unknown_ownership`  | `interests[].level: unknown`      | Ownership structure cannot be determined                         |
| `share_percentage`   | `interests[].percentage`          | The exact percentage of ownership interest held (0–100)          |
| `share_quantity`     | `interests[].quantity`            | The number of ownership units held (where applicable)            |
| `ordinary_shares`    | `interests[].class: ordinary`     | Standard shares with equal voting and economic rights            |
| `economic_interest`  | `interests[].type: economicBeneficiary` | Economic benefit without formal share ownership             |
| `dividend_rights`    | `interests[].rights: dividend_rights`   | Right to receive dividends from the entity                  |
| `liquidation_rights` | `interests[].rights: liquidation_rights` | Right to receive proceeds upon liquidation                 |

**Person Source & Evidence Terms**

| **Term**               | **Reference**                             | **Definition in Ownership Context**                                   |
|------------------------|-------------------------------------------|-----------------------------------------------------------------------|
| `self_declaration`     | `evidence[].type: selfDeclaration`        | The person themselves declared their ownership interest               |
| `official_register`    | `evidence[].type: officialRegister`       | Ownership verified from an official shareholder or company register   |
| `verified_third_party` | `evidence[].type: thirdPartyVerification` | Ownership confirmed by a verified third party (e.g., auditor, notary) |

---

#### Terms primarily relevant to an `Entity` Owner (as `LegalEntity` or `LegalArrangement`)

These terms describe legal entities and legal arrangements that hold ownership or economic
interests in another legal entity.

**Entity Classification Terms**

| **Term**            | **Reference**                        | **Definition in Ownership Context**                             |
|---------------------|--------------------------------------|-----------------------------------------------------------------|
| `registered_entity` | `entity.category: legal_entity`      | A formally registered legal entity holding ownership            |
| `legal_entity`      | `entity.category: legal_entity`      | A general legal entity holding shares or economic rights        |
| `state_body`        | `entity.category: legal_entity`      | A government body or state-owned entity holding ownership       |
| `arrangement`       | `entity.category: legal_arrangement` | A legal arrangement (e.g., trust, foundation) holding ownership |
| `anonymous_entity`  | `entity.category: unknown`           | An entity whose identity is intentionally withheld              |
| `unknown_entity`    | `entity.category: unknown`           | An entity that cannot currently be identified                   |

**Entity Form Terms**

| **Term**                 | **Reference**                         | **Definition in Ownership Context**                          |
|--------------------------|---------------------------------------|--------------------------------------------------------------|
| `private_company`        | `entity.form: private_company`        | A privately held company holding ownership                   |
| `public_company`         | `entity.form: public_company`         | A publicly listed company holding ownership                  |
| `partnership`            | `entity.form: partnership`            | A general or limited partnership holding ownership interest  |
| `limited_partnership`    | `entity.form: limited_partnership`    | A limited partnership holding ownership interest             |
| `foundation`             | `entity.form: foundation`             | A legal foundation holding ownership or economic rights      |
| `trust`                  | `entity.form: trust`                  | A legal trust holding assets or shares for beneficiaries     |
| `cooperative`            | `entity.form: cooperative`            | A cooperative entity holding ownership interest              |
| `state_owned_enterprise` | `entity.form: state_owned_enterprise` | A state-controlled commercial entity                         |

**Legal Arrangement Specific Terms** *(only when `entity.category = "legal_arrangement"`)*

| **Term**                  | **Reference**                                  | **Definition in Ownership Context**            |
|---------------------------|------------------------------------------------|------------------------------------------------|
| `settlor_entity`          | `interests[].type: settlor`                    | A legal entity that creates and funds a trust  |
| `trustee_entity`          | `interests[].type: trustee`                    | A legal entity administering a trust           |
| `protector_entity`        | `interests[].type: protector`                  | A legal entity overseeing trust governance     |
| `beneficiary_entity`      | `interests[].type: beneficiaryOfLegalArrangement` | A legal entity benefiting from the arrangement |
| `settlement`              | `entity.subtype_info.settlement`               | Instrument establishing the legal arrangement  |
| `purpose`                 | `entity.subtype_info.purpose`                  | Purpose of the legal arrangement               |
| `assets`                  | `entity.subtype_info.assets`                   | Assets held within the arrangement             |
| `reason_for_registration` | `entity.subtype_info.reason_for_registration`  | Reason for formal registration — optional      |

**Entity Ownership Role Terms**

| **Term**              | **Reference**                                 | **Definition in Ownership Context**                             |
|-----------------------|-----------------------------------------------|-----------------------------------------------------------------|
| `holding_company`     | `interests[].type: shareholding`              | A company whose primary purpose is holding shares               |
| `parent_company`      | `interests[].type: shareholding`              | A company that controls another entity through ownership        |
| `nominee_entity`      | `interests[].type: nomineeShareholding`       | An entity holding shares on behalf of another owner             |
| `intermediate_entity` | `interests[].level: indirect`                 | An entity through which ownership is exercised indirectly       |
| `consortium_member`   | `interests[].type: rightsGrantedByContract`   | An entity participating in ownership via consortium arrangement |

**Entity Interest Detail Terms**

| **Term**               | **Reference**                                      | **Definition in Ownership Context**                |
|------------------------|----------------------------------------------------|----------------------------------------------------|
| `direct_ownership`     | `interests[].level: direct`                        | Entity directly holds ownership interest           |
| `indirect_ownership`   | `interests[].level: indirect`                      | Entity holds ownership through intermediaries      |
| `share_percentage`     | `interests[].percentage`                           | Percentage of ownership held (0–100)               |
| `share_quantity`       | `interests[].quantity`                             | Number of ownership units held                     |
| `ordinary_shares`      | `interests[].class: ordinary`                      | Standard shares with equal rights                  |
| `preferred_shares`     | `interests[].class: preferred`                     | Shares with preferential rights                    |
| `dual_class_shares`    | `interests[].class: dual-class`                    | Shares with differentiated voting rights           |
| `other_share_class`    | `interests[].class: other`                         | Any non-standard share class                       |
| `dividend_rights`      | `interests[].rights: dividend_rights`              | Right to receive dividends                         |
| `liquidation_rights`   | `interests[].rights: liquidation_rights`           | Right to receive liquidation proceeds              |
| `economic_rights_only` | `interests[].type: economicBeneficiary`            | Economic benefit without formal ownership          |
| `contractual_rights`   | `interests[].type: rightsGrantedByContract`        | Rights derived from contract rather than shares    |
| `conditional_rights`   | `interests[].type: conditionalRightsGrantedByContract` | Rights dependent on conditions being met       |

**Entity Source & Evidence Terms**

| **Term**                  | **Reference**                             | **Definition in Ownership Context**                      |
|---------------------------|-------------------------------------------|----------------------------------------------------------|
| `official_register`       | `evidence[].type: officialRegister`       | Verified from official company or shareholder register   |
| `verified_third_party`    | `evidence[].type: thirdPartyVerification` | Verified by auditor, notary, or trusted third party      |
| `self_declaration_entity` | `evidence[].type: selfDeclaration`        | Entity itself declared ownership structure               |
| `trust_deed`              | `evidence[].type: trustDeed`              | Legal document establishing trust structure              |
| `shareholder_agreement`   | `evidence[].type: shareholderAgreement`   | Agreement defining ownership structure                   |
| `articles_of_association` | `evidence[].type: articlesOfAssociation`  | Constitutional document defining ownership rights        |
| `governance_chart`        | `evidence[].type: governanceChart`        | Organizational chart showing ownership/control structure |

---

### 2.2 Mandatory Attributes

**Owner Top-Level Mandatory Attributes** *(applies to all Owner entries)*

| **Data Identifier** | **Semantic Reference** | **Definition**                                                                                  | **Data Type**  |
|---------------------|------------------------|-------------------------------------------------------------------------------------------------|----------------|
| `type`              | —                      | Discriminator field — SHALL be `"Person"` or `"Entity"`. Determines which sub-object is present | Enum (String)  |
| `jurisdiction`      | —                      | Country of legal relevance for this owner entry — ISO 3166-1 alpha-2                            | String         |
| `address`           | —                      | Address of the owner — residential for `Person`, registered for `Entity`                        | Address Object |
| `interests`         | —                      | At least one interests record describing the ownership or control relationship                   | Array [Object] |
| `effective_date`    | —                      | Date when this ownership or control relationship became legally effective — ISO 8601 YYYY-MM-DD  | Date           |
| `evidence`          | —                      | At least one piece of supporting evidence substantiating the declared ownership or control       | Array [Object] |

**Person Owner Mandatory Attributes** *(present when `type = "Person"`)*

| **Data Identifier** | **Semantic Reference** | **Definition**                                                                  | **Data Type** |
|---------------------|------------------------|---------------------------------------------------------------------------------|---------------|
| `person.first_name` | —                      | First name(s) of the natural person, including middle name(s) where applicable  | String        |
| `person.surname`    | —                      | Last name(s) or surname(s) of the natural person owner                          | String        |
| `person.birth_date` | —                      | Date of birth — ISO 8601 YYYY-MM-DD                                             | Date          |

**Entity Owner Mandatory Attributes** *(present when `type = "Entity"`)*

| **Data Identifier**   | **Semantic Reference** | **Definition**                                                                         | **Data Type** |
|-----------------------|------------------------|----------------------------------------------------------------------------------------|---------------|
| `entity.category`     | -                      | Classification — SHALL be `"legal_entity"` or `"legal_arrangement"`                    | Enum (String) |
| `entity.name`         | —                      | Complete official registered name of the entity or legal arrangement                   | String        |
| `entity.identifier`   | —                      | At least one of: `euid`, `lei`, `tax`, or `other` SHALL be present                    | Object        |
| `entity.jurisdiction` | —                      | ISO 3166-1 alpha-2 jurisdiction in which the entity is registered or legally domiciled | String        |
| `entity.form`         | —                      | Legal form of the entity — SHALL use values from Section 2.8.6                         | String        |

**Entity Identifier Fields** *(at least one SHALL be present)*

| **Data Identifier**       | **Semantic Reference** | **Definition**                                   | **Data Type** |
|---------------------------|------------------------|--------------------------------------------------|---------------|
| `entity.identifier.euid`  | —                      | European Unique Identifier — optional            | String        |
| `entity.identifier.lei`   | —                      | Legal Entity Identifier per ISO 17442 — optional | String        |
| `entity.identifier.tax`   | —                      | National tax or registration number — optional   | String        |
| `entity.identifier.other` | —                      | Any other applicable legal identifier — optional | String        |

**Legal Arrangement Additional Mandatory Attributes** *(present when `entity.category = "legal_arrangement"` or `entity.form = "trust"`)*

| **Data Identifier**              | **Semantic Reference** | **Definition**                                                                       | **Data Type** |
|----------------------------------|------------------------|--------------------------------------------------------------------------------------|---------------|
| `entity.subtype_info.settlement` | —                      | Instrument or document establishing the legal arrangement (e.g., trust deed)         | String        |
| `entity.subtype_info.purpose`    | —                      | Declared purpose of the legal arrangement                                            | String        |
| `entity.subtype_info.assets`     | —                      | Description of assets held within the legal arrangement                              | String        |

**Address Mandatory Attributes** *(applies to all Owner entries)*

| **Data Identifier**    | **Semantic Reference** | **Definition**                                                        | **Data Type** |
|------------------------|------------------------|-----------------------------------------------------------------------|---------------|
| `address.street`       | —                      | Street name of the address                                            | String        |
| `address.house_number` | —                      | House or building number                                              | String        |
| `address.locality`     | —                      | City or locality                                                      | String        |
| `address.region`       | —                      | State, province, or region                                            | String        |
| `address.postal_code`  | —                      | Postal or ZIP code                                                    | String        |
| `address.country`      | —                      | ISO 3166-1 alpha-2 country code — SHALL use values from Section 2.8.7 | String        |

**Interests Mandatory Attributes** *(at least one record per Owner entry)*

| **Data Identifier**   | **Semantic Reference** | **Definition**                                                                                                            | **Data Type** |
|-----------------------|------------------------|---------------------------------------------------------------------------------------------------------------------------|---------------|
| `interests.type`      | Section 2.8.5          | Array of one or more role or interest types defining the ownership, control, or legal relationship — SHALL use values from Section 2.8.5 | Array [Enum] |
| `interests.level`     | Section 2.8.2          | How the interest is held — SHALL be one of: `"direct"`, `"indirect"`, `"joint"`, or `"unknown"`                          | Enum (String) |
| `interests.percentage`| —                      | Percentage of ownership interest held — decimal value in range 0–100                                                      | Decimal       |
| `interests.quantity`  | —                      | Number of shares or ownership units held — SHALL be a non-negative integer                                                | Integer       |
| `interests.rights`    | Section 2.8.3          | Array of economic rights associated with the interest — SHALL use values from Section 2.8.3                               | Array [Enum]  |

**Evidence Mandatory Attributes** *(at least one entry per Owner entry)*

| **Data Identifier** | **Semantic Reference** | **Definition**                                                                          | **Data Type** |
|---------------------|------------------------|-----------------------------------------------------------------------------------------|---------------|
| `evidence[n].id`    | —                      | Unique identifier, URI, or URN of the source or evidence document                       | String        |
| `evidence[n].type`  | —                      | Type of evidence document — SHALL use a value from Section 2.8.9                        | String        |

### 2.3 Optional Attributes

**Person Owner Optional Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                                  | **Data Type** |
|---------------------|------------------------|-----------------------------------------------------------------|---------------|
| `person.birth_date` | —                      | Date of birth of the natural person owner — ISO 8601 YYYY-MM-DD | Date          |

**Legal Arrangement Optional Attributes** *(when `entity.category = "legal_arrangement"`)*

| **Data Identifier**                           | **Semantic Reference** | **Definition**                                           | **Data Type** |
|-----------------------------------------------|------------------------|----------------------------------------------------------|---------------|
| `entity.subtype_info.reason_for_registration` | —                      | The reason the legal arrangement was formally registered | String        |

**Interests Optional Attributes**

| **Data Identifier**     | **Semantic Reference** | **Definition**                                                                                        | **Data Type** |
|-------------------------|------------------------|-------------------------------------------------------------------------------------------------------|---------------|
| `interests.class`       | Section 2.8.1          | Class of shares held — SHALL use values from Section 2.8.1 (`ordinary`, `preferred`, `dual-class`, `other`) | Enum (String) |
| `interests.description` | —                      | Free-text description of the nature of the ownership or control interest                              | String        |

**Evidence Optional Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                                                                   | **Data Type**   |
|---------------------|------------------------|--------------------------------------------------------------------------------------------------|-----------------|
| `evidence[n].url`   | —                      | URI reference to the publicly accessible source or evidence document                             | URI             |
| `evidence[n].data`  | —                      | Base64-encoded source document — SHALL be provided if `url` is absent or not publicly accessible | String (base64) |

### 2.4 Conditional Attributes

| **Condition**                                          | **Applicable Attributes**                                                                      | **Rule**                                                                           |
|--------------------------------------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| `type = "Person"`                                      | `person.*` block                                                                               | The `person` object SHALL be present and the `entity` object SHALL be absent       |
| `type = "Entity"`                                      | `entity.*` block                                                                               | The `entity` object SHALL be present and the `person` object SHALL be absent       |
| `entity.category = "legal_arrangement"`                | `entity.subtype_info.settlement`, `entity.subtype_info.purpose`, `entity.subtype_info.assets`  | The `subtype_info` object SHALL be present and all three fields SHALL be populated |
| `entity.form = "trust"`                                | `entity.subtype_info.settlement`, `entity.subtype_info.purpose`, `entity.subtype_info.assets`  | The `subtype_info` object SHALL be present and all three fields SHALL be populated |
| `evidence[n].url` is absent or not publicly accessible | `evidence[n].data`                                                                             | `evidence[n].data` (base64-encoded) SHALL be provided                              |

### 2.5 Mandatory Metadata

| **Data Identifier**        | **Definition**                                                                | **Data type** |
|----------------------------|-------------------------------------------------------------------------------|---------------|
| attestation_legal_category | Indicates the legal category of the AuthorisedSignatories Attestation ("EAA") | String        |
| cnf                        | cryptographic Key Binding                                                                             | String        |

*Note*: Only the additional mandatory attributes are listed; the mandatory attributes defined by the protocol are not specified.

### 2.6 Optional Metadata

| **Data Identifier** | **Definition**                                                             | **Data type** |
|---------------------|----------------------------------------------------------------------------|---------------|
| trust_anchor_url    | URL where the trust anchor for verifying this attestation can be retrieved | URI           |
| schema_version      | Version of the schema used for this attestation                            | String        |

### 2.7 Conditional Metadata

No conditional metadata elements are defined for this attestation type.

### 2.8 Value Lists

#### 2.8.1 `interests.class` Values

| **Code**     | **Definition**                                                                                   |
|--------------|--------------------------------------------------------------------------------------------------|
| `ordinary`   | Standard shares with full voting and economic rights                                             |
| `preferred`  | Shares with preferential rights (e.g., priority dividends) but potentially limited voting rights |
| `dual-class` | Share structure with multiple classes carrying different voting rights                           |
| `other`      | Any other share class not covered above                                                          |

#### 2.8.2 `interests.level` Values

| **Code**   | **Definition**                                                                       |
|------------|--------------------------------------------------------------------------------------|
| `direct`   | Ownership interest held directly in the subject entity without intermediary entities |
| `indirect` | Ownership interest held through one or more intermediary legal entities              |
| `joint`    | Ownership interest held jointly with one or more other persons or entities           |
| `unknown`  | Ownership structure cannot be determined at the time of attestation                  |

#### 2.8.3 `interests.rights` Values

| **Code**             | **Definition**                                                    |
|----------------------|-------------------------------------------------------------------|
| `dividend_rights`    | Right to receive a share of profits distributed by the entity     |
| `liquidation_rights` | Right to receive a share of assets upon dissolution of the entity |

#### 2.8.4 Ownership Controller Category Codes

| **Code**                            | **Definition**                                                                                                    |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| `directShareholder`                 | Natural or legal person holding shares directly in the subject entity                                             |
| `indirectShareholder`               | Natural or legal person holding shares through one or more intermediate entities                                  |
| `controllerViaVotingOrGovernance`   | Natural or legal person exercising control through voting rights, board representation, or governance mechanisms  |
| `trusteeBeneficiaryFiduciary`       | Natural or legal person acting as trustee or beneficiary in a trust, foundation, or similar fiduciary arrangement |
| `partnerInPartnership`              | Natural or legal person holding a partnership interest                                                            |
| `holderOfConvertibleRights`         | Natural or legal person holding convertible instruments (bonds, options, warrants) convertible into equity        |
| `personExercisingDominantInfluence` | Natural or legal person exercising dominant influence through contractual arrangements or operational control      |

#### 2.8.5 `interests.type` Values

| **Code**                             | **Applicable To** | **Definition**                                                   |
|--------------------------------------|-------------------|------------------------------------------------------------------|
| `shareholding`                       | Person, Entity    | Direct or indirect share ownership in the subject entity         |
| `nomineeShareholding`                | Person, Entity    | Shares held on behalf of the actual beneficial owner             |
| `votingRights`                       | Person, Entity    | Rights to vote at general meetings of the subject entity         |
| `appointmentOfBoard`                 | Person, Entity    | Right to appoint or remove members of the board                  |
| `otherInfluenceOrControl`            | Person, Entity    | Other significant influence or control not covered by other codes |
| `seniorManagingOfficial`             | Person            | Control exercised through a senior management position           |
| `settlor`                            | Person, Entity    | Created and transferred assets into a legal arrangement          |
| `trustee`                            | Person, Entity    | Administers a trust or legal arrangement                         |
| `protector`                          | Person, Entity    | Oversees or protects beneficiary interests in a trust            |
| `beneficiaryOfLegalArrangement`      | Person, Entity    | Receives benefit from a trust or legal arrangement               |
| `rightsGrantedByContract`            | Person, Entity    | Rights granted through contractual arrangements                  |
| `conditionalRightsGrantedByContract` | Person, Entity    | Rights contingent on specified conditions being met              |
| `economicBeneficiary`                | Person, Entity    | Economic benefit without formal share ownership                  |
| `controlViaCompanyRulesOrArticles`   | Person, Entity    | Control defined in the company rules or articles of association  |
| `controlByLegalFramework`            | Entity            | Control applied through the applicable legal framework           |

#### 2.8.6 `entity.form` Values

| **Value**                | **Definition**                                                          |
|--------------------------|-------------------------------------------------------------------------|
| `private_company`        | A privately held company                                                |
| `public_company`         | A publicly listed company                                               |
| `partnership`            | A general or limited partnership                                        |
| `limited_partnership`    | A limited partnership with defined liability                            |
| `trust`                  | A legal arrangement where assets are held by trustees for beneficiaries |
| `foundation`             | A legal arrangement established for charitable or private purposes      |
| `cooperative`            | A cooperative entity                                                    |
| `state_owned_enterprise` | A state-owned or state-controlled commercial entity                     |
| `other`                  | Other legal form not covered above                                      |

#### 2.8.7 Country Codes

`owner.jurisdiction`, `entity.jurisdiction`, and `address.country` SHALL use **ISO 3166-1 alpha-2**
two-letter country codes.

#### 2.8.8 Date Formats

All date attributes (e.g., `effective_date`, `person.birth_date`) SHALL follow the
**ISO 8601 YYYY-MM-DD** format.

#### 2.8.9 Evidence Type Values

| **Code**                 | **Applicable To** | **Definition**                                                        |
|--------------------------|-------------------|-----------------------------------------------------------------------|
| `officialRegister`       | Person, Entity    | Ownership verified from an official shareholder or company register   |
| `selfDeclaration`        | Person, Entity    | The owner themselves declared their ownership interest                |
| `thirdPartyVerification` | Person, Entity    | Ownership confirmed by a verified third party (e.g., auditor, notary) |
| `trustDeed`              | Entity            | Legal document establishing a trust structure                         |
| `shareholderAgreement`   | Person, Entity    | Agreement defining the ownership or control structure                 |
| `articlesOfAssociation`  | Entity            | Constitutional document defining ownership rights and governance      |
| `governanceChart`        | Entity            | Organizational chart showing the ownership or control structure       |

### 2.9 Integrity Rules

The following integrity rules SHALL be enforced:

| **Rule ID** | **Rule**                                                                                                                                                                             |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IR-01       | The `owner` array SHALL contain at least one entry                                                                                                                                   |
| IR-02       | At least one `Owner` entry SHALL be of `type = "Person"` to satisfy AML requirements mandating identification of natural persons who ultimately own or control the entity            |
| IR-03       | If `owner.type = "Person"`, the `person` object SHALL be present and the `entity` object SHALL be absent                                                                             |
| IR-04       | If `owner.type = "Entity"`, the `entity` object SHALL be present and the `person` object SHALL be absent                                                                             |
| IR-05       | If `entity.category = "legal_arrangement"` or `entity.form = "trust"`, the `subtype_info` object SHALL be present and `settlement`, `purpose`, and `assets` SHALL all be populated  |
| IR-06       | `entity.identifier` SHALL contain at least one of: `euid`, `lei`, `tax`, or `other`                                                                                                 |
| IR-07       | `interests.type` SHALL be an array containing at least one value from Section 2.8.5                                                                                                  |
| IR-08       | `interests.level` SHALL use one of the values defined in Section 2.8.2                                                                                                               |
| IR-09       | `interests.percentage` SHALL be a decimal value in the range 0–100                                                                                                                   |
| IR-10       | `interests.quantity` SHALL be a non-negative integer                                                                                                                                 |
| IR-11       | `interests.rights` SHALL be an array containing at least one value from Section 2.8.3                                                                                                |
| IR-12       | `interests.class`, when present, SHALL use a value from Section 2.8.1                                                                                                                |
| IR-13       | Each `Owner` entry SHALL contain at least one `evidence` entry                                                                                                                       |
| IR-14       | Each `evidence` entry SHALL contain a non-empty `id` and `type`                                                                                                                      |
| IR-15       | If `evidence[n].url` is absent or not publicly accessible, `evidence[n].data` (base64-encoded) SHALL be provided                                                                    |
| IR-16       | `evidence[n].type` SHALL use a value from Section 2.8.9                                                                                                                              |
| IR-17       | All date fields (e.g., `effective_date`, `person.birth_date`) SHALL conform to ISO 8601 YYYY-MM-DD format                                                                            |
| IR-18       | All jurisdiction and country fields (`owner.jurisdiction`, `entity.jurisdiction`, `address.country`) SHALL use ISO 3166-1 alpha-2 codes                                              |
| IR-19       | The sum of all `interests.percentage` values across all `Owner` entries for the same subject entity SHOULD NOT exceed 100%                                                           |
| IR-20       | `entity.form` SHALL use a value from Section 2.8.6                                                                                                                                   |
| IR-21       | Each `Owner` entry SHALL contain a non-empty `effective_date`                                                                                                                        |

## 3 Attestation Encoding

### 3.1 ISO/IEC 18013-5-Compliant Encoding

ISO/IEC 18013-5 (mdoc) is **out of scope** for this Rulebook, as offline proximity  presentation is not a current requirement for the Control Attestation.

### 3.2 SD-JWT VC-Based Encoding

The Ownership Attestation uses the SD-JWT VC format to allow for selective disclosure of ownership structure attributes.

**Selective Disclosure:** Top-level claims (`owner`) SHALL be individually selectively
disclosable, enabling a legal entity to disclose only the attributes requested by a Relying
Party.
The `.` notation is used to indicate the nesting of attributes.

**Verifiable Credential Type (`vct`):** `eu.we-build:ownership:1`

#### 3.2.1 Attribute Encoding Table

| **Data Identifier**           | **Attribute Identifier**                               | **Encoding Format**         | **Reference / Notes**                                                                 | **Disclosable**    |
|-------------------------------|--------------------------------------------------------|-----------------------------|---------------------------------------------------------------------------------------|--------------------|
| `owner`                       | `owner`                                                | Array [Owner]               | SHALL contain at least one entry                                                      | MUST               |
| `type`                        | `owner[n].type`                                        | String                      | `"Person"` \| `"Entity"`                                                              | MUST               |
| **Person**                    |                                                        |                             |                                                                                       |                    |
| `first_name`                  | `owner[n].person.first_name`                           | String                      | SHALL be non-empty                                                                    | MUST               |
| `surname`                     | `owner[n].person.surname`                              | String                      | SHALL be non-empty                                                                    | MUST               |
| `birth_date`                  | `owner[n].person.birth_date`                           | String (ISO 8601)           | ISO 8601 YYYY-MM-DD — optional                                                        | MAY                |
| **Entity / LegalArrangement** |                                                        |                             |                                                                                       |                    |
| `category`                    | `owner[n].entity.category`                             | String                      | `"legal_entity"` \| `"legal_arrangement"`                                             | MUST               |
| `name`                        | `owner[n].entity.name`                                 | String                      | SHALL be non-empty                                                                    | MUST               |
| `euid`                        | `owner[n].entity.identifier.euid`                      | String                      | European Unique Identifier — optional; at least one identifier field SHALL be present | MAY                |
| `lei`                         | `owner[n].entity.identifier.lei`                       | String (20 chars)           | LEI per ISO 17442 — optional                                                          | MAY                |
| `tax`                         | `owner[n].entity.identifier.tax`                       | String                      | National tax or registration number — optional                                        | MAY                |
| `other`                       | `owner[n].entity.identifier.other`                     | String                      | Any other applicable identifier — optional                                            | MAY                |
| `jurisdiction`                | `owner[n].entity.jurisdiction`                         | String (ISO 3166-1 alpha-2) | SHALL be non-empty                                                                    | MUST               |
| `form`                        | `owner[n].entity.form`                                 | String                      | SHALL use values from Section 2.8.6                                                   | MUST               |
| **subtype_info**              | `owner[n].entity.subtype_info`                         | Object                      | Mandatory when `entity.category = "legal_arrangement"` or `entity.form = "trust"`     | MUST (conditional) |
| `settlement`                  | `owner[n].entity.subtype_info.settlement`              | String                      | Mandatory when `subtype_info` is present                                              | MUST (conditional) |
| `purpose`                     | `owner[n].entity.subtype_info.purpose`                 | String                      | Mandatory when `subtype_info` is present                                              | MUST (conditional) |
| `assets`                      | `owner[n].entity.subtype_info.assets`                  | String                      | Mandatory when `subtype_info` is present                                              | MUST (conditional) |
| `reason_for_registration`     | `owner[n].entity.subtype_info.reason_for_registration` | String                      | Optional                                                                              | MAY                |
| **Address**                   |                                                        |                             |                                                                                       |                    |
| `street`                      | `owner[n].address.street`                              | String                      | SHALL be non-empty                                                                    | MUST               |
| `house_number`                | `owner[n].address.house_number`                        | String                      | SHALL be non-empty                                                                    | MUST               |
| `locality`                    | `owner[n].address.locality`                            | String                      | SHALL be non-empty                                                                    | MUST               |
| `region`                      | `owner[n].address.region`                              | String                      | SHALL be non-empty                                                                    | MUST               |
| `postal_code`                 | `owner[n].address.postal_code`                         | String                      | SHALL be non-empty                                                                    | MUST               |
| `country`                     | `owner[n].address.country`                             | String (ISO 3166-1 alpha-2) | SHALL be non-empty                                                                    | MUST               |
| **Interests**                 |                                                        |                             |                                                                                       |                    |
| `type`                        | `owner[n].interests.type`                              | Array of Strings            | SHALL use values from Section 2.8.5 — at least one required                           | MUST               |
| `level`                       | `owner[n].interests.level`                             | String                      | SHALL use values from Section 2.8.2                                                   | MUST               |
| `percentage`                  | `owner[n].interests.percentage`                        | Decimal (0–100)             | SHALL be a decimal value in range 0–100                                               | MUST               |
| `quantity`                    | `owner[n].interests.quantity`                          | uint                        | Non-negative integer                                                                  | MUST               |
| `description`                 | `owner[n].interests.description`                       | String                      | Free-text description — optional                                                      | MAY                |
| `class`                       | `owner[n].interests.class`                             | String                      | SHALL use values from Section 2.8.1 — optional                                        | MAY                |
| `rights`                      | `owner[n].interests.rights`                            | Array of Strings            | SHALL use values from Section 2.8.3                                                   | MUST               |
| `effective_date`              | `owner[n].effective_date`                              | String (ISO 8601)           | Date ownership became effective — ISO 8601 YYYY-MM-DD                                 | MUST               |
| **Evidence**                  |                                                        |                             |                                                                                       |                    |
| `id`                          | `owner[n].evidence[m].id`                              | String                      | Unique identifier, URI, or URN — SHALL be non-empty                                   | MUST               |
| `type`                        | `owner[n].evidence[m].type`                            | String                      | SHALL use values from Section 2.8.9 — SHALL be non-empty                              | MUST               |
| `url`                         | `owner[n].evidence[m].url`                             | URI                         | URI reference to source document — optional                                           | MAY                |
| `data`                        | `owner[n].evidence[m].data`                            | String (base64)             | Base64-encoded source — SHALL be provided if `url` not publicly accessible            | MAY                |
| **Metadata**                  |                                                        |                             |                                                                                       |                    |
| `issuance_date`               | `iat`                                                  | Number (Unix timestamp)     | Date and time when the attestation was issued (ISO 8601); RFC 7519                    | MUST NOT           |
| `expiry_date`                 | `exp`                                                  | Number (Unix timestamp)     | Date and time when the attestation expires (ISO 8601); RFC 7519                       | MUST NOT           |
| `issuing_entity`              | `iss`                                                  | String (URI or DID)         | Identifier of the competent institution that issued the attestation; RFC 7519         | MUST NOT           |
| `attestation_legal_category`  | `attestation_legal_category`                           | String                      | One of "EAA" or "QEAA" as defined by eIDAS 2                                          | MUST NOT           |
| `vct`                         | `vct`                                                  | String                      | The vct definition                                                                    | MUST NOT           |
| `cnf`                         | `cnf`                                                  | String                      | Cryptographic Key Binding                                                             | MUST NOT           |
| `schema_version`              | `schema_version`                                       | String                      | Version of the schema used; optional                                                  | MAY                |
| `trust_anchor_url`            | `trust_anchor_url`                                     | String (URI)                | URL where the trust anchor for verifying this attestation can be retrieved; optional  | MAY                |

**Notes:**

- **MUST**: The claim SHALL be selectively disclosable — the holder MAY choose to disclose or
  withhold this claim when presenting the credential to a Relying Party.
- **MUST NOT**: The claim SHALL NOT be selectively disclosable — it is always present in plain
  text in the JWT header/payload and cannot be withheld by the holder, as it is required for
  credential verification and trust establishment.
- `owner` entries are indexed as `[n]` where `n` starts at `0`; at least one owner SHALL be
  present, and at least one SHALL be of `type = "Person"`.
- `evidence` entries within each owner are indexed as `[m]` where `m` starts at `0`; at least
  one evidence entry SHALL be present per owner.
- `iat`, `exp`, and `iss` follow RFC 7519 standard JWT claim naming conventions.

#### 3.2.2 Status Claim

For SD-JWT VC-compliant Ownership Attestations, the attestation MUST include a `status` claim
if the technical validity period is greater than 24 hours. This claim enables Relying Parties
to determine if a credential has been revoked via a status list mechanism.

The `status` claim SHALL be a JSON object with the following members:

| **Field**                | **Type**       | **Value**                                       |
|--------------------------|----------------|-------------------------------------------------|
| `type`                   | String         | SHALL be `"status-list"`                        |
| `status_list_credential` | String (URI)   | URI of the Status List Credential document      |
| `status_list_index`      | Integer (>= 0) | Zero-based index into the status list bitstring |
| `status_purpose`         | String         | SHALL be `"revocation"`                         |

**Example:**

```json
{
  "status": {
    "type": "status-list",
    "status_list_credential": "https://issuer.example.com/status/ownership/2025",
    "status_list_index": 456,
    "status_purpose": "revocation"
  }
}
```
#### 3.2.3 Example Payload
The following is a non-normative example of an Ownership SD-JWT VC payload demonstrating a  natural person owner, a legal entity owner, and a legal arrangement owner:
```
{
  "vct": "eu.we-build:ownership:1",
  "iss": "https://issuer.example.com",
  "iat": 1736935200,
  "exp": 1768471200,
  "issuing_entity": "did:example:legal-entity-789",
  "attestation_legal_category": "EAA",
  "schema_version": "0.8.0",
  "trust_anchor_url": "https://trust.webuildconsortium.eu/anchors/eidas-tl",

  "owner": [
    {
      "type": "Person",
      "jurisdiction": "DE",
      "person": {
        "first_name": "Anna",
        "surname": "Schmidt",
        "birth_date": "1978-04-15"
      },
      "address": {
        "street": "Hauptstraße",
        "house_number": "12",
        "locality": "Berlin",
        "region": "Berlin",
        "postal_code": "10115",
        "country": "DE"
      },
      "interests": {
        "type": ["shareholding"],
        "level": "direct",
        "percentage": 51.0,
        "quantity": 51000,
        "class": "ordinary",
        "rights": ["dividend_rights", "liquidation_rights"]
      },
      "effective_date": "2018-03-01",
      "evidence": [
        {
          "id": "src-001",
          "type": "officialRegister",
          "url": "https://example.com/docs/shareholder-register-2024.pdf"
        }
      ]
    },
    {
      "type": "Entity",
      "jurisdiction": "DE",
      "entity": {
        "category": "legal_entity",
        "name": "Holding GmbH",
        "identifier": {
          "euid": "DE-HRB-654321",
          "lei": "529900T8BM49AURSDO55",
          "tax": "DE987654321"
        },
        "jurisdiction": "DE",
        "form": "private_company"
      },
      "address": {
        "street": "Musterstraße",
        "house_number": "45",
        "locality": "Frankfurt",
        "region": "Hessen",
        "postal_code": "60311",
        "country": "DE"
      },
      "interests": {
        "type": ["shareholding", "votingRights"],
        "level": "indirect",
        "percentage": 30.0,
        "quantity": 30000,
        "class": "preferred",
        "rights": ["dividend_rights"]
      },
      "effective_date": "2019-06-15",
      "evidence": [
        {
          "id": "src-002",
          "type": "shareholderAgreement",
          "url": "https://example.com/docs/shareholder-agreement-2019.pdf"
        }
      ]
    },
    {
      "type": "Entity",
      "jurisdiction": "LU",
      "entity": {
        "category": "legal_arrangement",
        "name": "Schmidt Family Trust",
        "identifier": {
          "lei": "549300ABCDEF12345678"
        },
        "jurisdiction": "LU",
        "form": "trust",
        "subtype_info": {
          "settlement": "Settled under Luxembourg trust law on 2015-03-01",
          "purpose": "Family wealth management and succession planning",
          "assets": "Real estate, securities portfolios, and cash holdings",
          "reason_for_registration": "Registered for tax transparency under CRS"
        }
      },
      "address": {
        "street": "Rue de la Forêt",
        "house_number": "7",
        "locality": "Luxembourg",
        "region": "Luxembourg",
        "postal_code": "L-1234",
        "country": "LU"
      },
      "interests": {
        "type": ["beneficiaryOfLegalArrangement", "economicBeneficiary"],
        "level": "indirect",
        "percentage": 19.0,
        "quantity": 0,
        "rights": ["dividend_rights", "liquidation_rights"]
      },
      "effective_date": "2015-03-01",
      "evidence": [
        {
          "id": "src-003",
          "type": "trustDeed",
          "url": "https://example.com/docs/trust-deed-2015.pdf"
        }
      ]
    }
  ],

  "status": {
    "type": "status-list",
    "status_list_credential": "https://issuer.example.com/status/ownership/2025",
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
Sample payloads are provided under `../data-schemas/sd-jwt/sample-data/ownership-sd-jwt-sample.json`

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