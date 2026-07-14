# Attestation Rulebook for attestations of type Control Attestation

* Author(s):
  * [Florin Coptil, Robert Bosch GmbH]
  * [Stephan Fuchs, Deutsche Bank AG]

* Reviewer(s):
  * [Baumgardt Michaela, Commerzbank]
  * [Ricky Lamberty, Robert Bosch GmbH]
  * @TODO Florin — Add the reviewers from attestation design (meetings UseCase, Banks, TransparentRegister)

| Version | Date       | Description                                                       |
|---------|------------|-------------------------------------------------------------------|
| 0.1     | 23.03.2026 | Initial draft based on the WeBuild design attestations meetings   |
| 0.3     | 01.06.2026 | Updates of content (review ubo documents)                         |
| 0.4     | 01.06.2026 | Updates of content - legal arrangements                           |
| 0.7     | 24.06.2026 | Updates of content based on the submission regulation and AMLR/RTS|
| 0.8     | 29.06.2026 | Updates of BODS vocabulary                                        |
| 0.9     | 03.07.2026 | Updates in regard trust and revocation                            |

* Contact:
  * [Florin Coptil](mailto:florin.coptil@bosch.com)* 

* Feedback:

## 1 Introduction

This attestation addresses the following question:

**Who exercises effective control over this legal entity?**

A Controller is any natural person, legal entity, or legal arrangement that directly or  indirectly exercises effective control over a legal entity.

### 1.1 Document Scope and Purpose

The Control Attestation records all natural persons, legal entities, and legal arrangements
which have control — direct or indirect — in a legal entity, providing comprehensive
transparency on control structures. This attestation is a critical component of both Know Your
Customer (KYC) and Know Your Supplier (KYS) processes within the Wallet ecosystem, supporting
effective risk management, regulatory compliance, and anti-money laundering (AML) obligations.

**Design Decisions**

This Control Attestation Rulebook is based on:
- The EU Anti-Money Laundering Regulation (AMLR 2024/1624) as the primary regulatory driver
  for beneficial ownership and control transparency obligations
- The EUDI Wallet ecosystem and eIDAS 2 framework as the digital identity infrastructure
- The SD-JWT VC specification (draft-ietf-oauth-sd-jwt-vc-09) for verifiable credential encoding
- ISO 3166-1 alpha-2 for country and jurisdiction codes
- ISO 8601 for date formatting
- ISO 17442 for Legal Entity Identifier (LEI) codes
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

| Term                             | Definition                                                                                                                                                                                                 |
|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Control                          | A comprehensive record of all natural and legal persons who exercise direct or indirect control over a legal entity, including control percentages and the mechanisms through which control is exercised   |
| Controller                       | A natural person, legal entity, or legal arrangement that exercises control over a legal entity, either directly or indirectly                                                                             |
| Direct Control                   | Control exercised directly by a person through ownership of voting shares, board membership, or executive roles in the subject entity                                                                      |
| Indirect Control                 | Control exercised through one or more intermediary entities or contractual arrangements (e.g., control via a parent company, nominee arrangements, or proxy voting agreements)                             |
| Control Percentage               | A quantitative measure of the degree of control a person exercises, typically based on voting rights percentage, board representation percentage, or other control metrics                                 |
| Legal Arrangement                | A trust, foundation, or similar structure that may exercise control over a legal entity. Includes roles such as settlor, trustee, protector, and beneficiary                                               |
| Know Your Customer (KYC)         | Due diligence process for verifying customer identity and assessing risk in financial relationships                                                                                                        |
| Know Your Supplier (KYS)         | Due diligence process for verifying supplier credentials, integrity, and risk exposure                                                                                                                     |
| Politically Exposed Person (PEP) | Individual entrusted with prominent public functions, posing higher risk for corruption or bribery                                                                                                         |
| EU Company Certificate (EUCC)    | Attestation establishing the legal existence and identity of a legal entity within the EU                                                                                                                  |
| Evidence                         | Supporting documentation substantiating the control structure (e.g., governance chart, shareholder agreement, articles of association, trust deed)                                                         |
| Identifier                       | A formal reference code used to uniquely identify a legal entity (e.g., EUID, LEI, national tax or registry number)                                                                                        |
| Controls                         | The sub-object within each Controller entry describing how control is exercised, including the mechanism type, level, basis, and associated rights                                                         |

---

## 2 Attestation Attributes and Metadata

The Control Attestation is designed to provide a complete, verifiable representation of an
entity's control structure in a standardised digital format. This attestation supports
transparency, compliance, and risk management by enabling automated verification of effective
control across complex, multi-tiered corporate structures where control may be exercised through
diverse mechanisms beyond simple shareholding.

### 2.1 Introduction

The Controller model supports three distinct controller types: natural persons (`Person`),
legal entities (`Entity` with `category = "legal_entity"`), and legal arrangements (`Entity`
with `category = "legal_arrangement"` — e.g., trusts, foundations).

**Controller type classification:**

| Controller Type | Description                                                                                                                       |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------|
| `Person`        | A natural person exercising control. Roles include: `seniorManagingOfficial`, `boardMember`, `boardChair`, `nominee`, `nominator` |
| `Entity`        | A legal entity or legal arrangement exercising control — further categorised by `entity.category`                                 |

**Controller entity category classification** *(applicable when `type = "Entity"`)*:

| Entity Category    | Description                                                                                                                                                                                |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `legal_entity`     | A formally registered legal entity (e.g., holding company) exercising control. Mechanisms include: `voting_rights`, `appointment_rights`, `agreements`, `dominance`, `contractual`         |
| `legal_arrangement`| A trust, foundation, or other legal arrangement exercising control. Roles within include: `settlor`, `trustee`, `protector`, `beneficiaryOfLegalArrangement`                               |

**Data Model:**

The Controller follows a hierarchical structure:
```
Controller [1..n]                               // The person or entity exercising control
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
├─ controls (M)                                 // How control is exercised
│   ├─ type [enum] [1..n] (M)                   // See Section 2.8.3
│   ├─ level (tstr) (M)                         // "direct" | "indirect" | "joint" | "unknown"
│   ├─ basis [enum] (M)                         // e.g., "corporate_position", "contractual"
│   ├─ voting_percentage (Decimal) (O)          // Percentage of voting rights (0–100)
│   ├─ appointment_rights (tstr) (O)            // Free text details on appointment rights
│   ├─ other_details (tstr) (O)                 // Free text for other control mechanisms
│   └─ rights [String] (M)                      // "dividend_rights" | "liquidation_rights"
├─ effective_date (date) (M)                    // ISO 8601 YYYY-MM-DD
└─ evidence [1..n] (M)                          // At least one evidence entry required
├─ id (tstr) (M)                            // Unique identifier, URI, or URN
├─ type (tstr) (M)                          // Evidence type — see Section 2.8.9
├─ url (uri) (O)                            // URI to publicly accessible source document
└─ data (base64) (O)                        // Base64-encoded — required if url absent
```
*Note*: M - mandatory / O - optional.

**Explanation:**
- The attestation SHALL contain at least one `Controller` entry of `type = "Person"` to comply
  with AML requirements mandating identification of the natural persons who ultimately exercise
  control over the entity.
- The attestation MAY contain zero or more `Controller` entries of `type = "Entity"`
  representing intermediate legal entities or legal arrangements in the control chain.
- Each `Controller` entry SHALL include:
  - `type` (mandatory enum: `"Person"` or `"Entity"`)
  - `jurisdiction` (mandatory — ISO 3166-1 alpha-2)
  - `address` (mandatory — residential address for `Person`, registered address for `Entity`)
  - `controls` (mandatory — at least one record describing how control is exercised)
  - `effective_date` (mandatory — date when this control became effective)
  - `evidence` (mandatory — at least one piece of supporting evidence)

- For each `Controller` of `type = "Person"`:
  - The `person` object SHALL be present and the `entity` object SHALL be absent.
  - `first_name` and `surname` SHALL be present.
  - `birth_date` is OPTIONAL but SHOULD be included where available.
  - At least one `controls` record SHALL be present, including:
    - `type` — SHALL use values from Section 2.8.3
    - `level` — SHALL use values from Section 2.8.2
    - `basis` — SHALL use values from Section 2.8.4
    - `rights` — SHALL use values from Section 2.8.5

- For each `Controller` of `type = "Entity"`:
  - The `entity` object SHALL be present and the `person` object SHALL be absent.
  - `category` SHALL be present and SHALL be one of `"legal_entity"` or `"legal_arrangement"`.
  - `name` SHALL be present (complete official registered name).
  - `identifier` SHALL contain at least one of: `euid`, `lei`, `tax`, or `other`.
  - `jurisdiction` SHALL be present (ISO 3166-1 alpha-2).
  - `form` SHALL be present and SHALL use a value from Section 2.8.6.
  - At least one `controls` record SHALL be present.

- When `entity.category = "legal_arrangement"` OR `entity.form = "trust"`, the `subtype_info`
  object SHALL be present and SHALL include:
  - `settlement` — the instrument establishing the legal arrangement
  - `purpose` — the declared purpose of the arrangement
  - `assets` — description of assets held within the arrangement
  - `reason_for_registration` is OPTIONAL

- Each `Controller` entry SHALL include at least one `evidence` entry. Each evidence entry
  SHALL include:
  - `id` — unique identifier, URI, or URN of the source document
  - `type` — SHALL use values from Section 2.8.9
  - `data` — base64-encoded document — SHALL be provided if `url` is absent or not publicly
    accessible

- `controls.type` SHALL be an array allowing multiple concurrent control mechanism types to be
  declared for a single controller.
- `controls.level` SHALL use one of: `"direct"`, `"indirect"`, `"joint"`, or `"unknown"` as
  defined in Section 2.8.2.
- `controls.rights` SHALL be an array and SHALL use values from Section 2.8.5.
- `effective_date` SHALL follow ISO 8601 YYYY-MM-DD format.

**Attestation Classification:**

This attestation type MAY be classified as:
- **`EAA`** within the EUBW Wallet ecosystem, when self-issued by the legal entity subject to
  the control disclosure (i.e., the entity issues an attestation about its own control
  structure).
- **`QEAA`** when issued by a qualified trust service provider (QTSP) or authorized competent
  body that can independently attest the control structure (e.g., based on official company
  register data, audited financial statements, or notarized documentation).

**Terms primarily relevant to a `Person` controller:**

| **Term**                 | **Reference**                              | **Definition in Control Context**                                      |
|--------------------------|--------------------------------------------|------------------------------------------------------------------------|
| `seniorManagingOfficial` | `controls.type: voting_rights`             | An individual exercising control through senior management position    |
| `boardMember`            | `controls.type: board`                     | An individual on the board exercising collective or individual control |
| `boardChair`             | `controls.type: board`                     | An individual leading the board with significant control               |
| `nominee`                | `controls.type: nominee`                   | A person acting on behalf of another (indirect control mechanism)      |
| `nominator`              | `controls.type: nominee`                   | The person who actually controls through a nominee arrangement         |

**Terms primarily relevant to an `Entity` controller (as `legal_entity` or `legal_arrangement`):**

| **Term**                             | **Reference**                                 | **Definition in Control Context**                                |
|--------------------------------------|-----------------------------------------------|------------------------------------------------------------------|
| `voting_rights`                      | `controls.type: voting_rights`                | Voting rights held through shares by a person or entity          |
| `appointment_rights`                 | `controls.type: appointment_rights`           | Right to appoint board members, held by a person or entity       |
| `agreements`                         | `controls.type: agreements`                   | Control through contractual or constitutional agreements         |
| `dominance`                          | `controls.type: dominance`                    | Ability to exercise dominant influence                           |
| `contractual`                        | `controls.type: contractual`                  | Rights granted via formal or informal contract                   |
| `conditionalRightsGrantedByContract` | `controls.type: contractual`                  | Conditional contractual rights                                   |
| `controlViaCompanyRulesOrArticles`   | `controls.type: agreements`                   | Control defined by company articles                              |
| `controlByLegalFramework`            | `controls.basis: legal_framework`             | Control applied by applicable legal framework                    |
| `settlor`                            | `controls.type: agreements`                   | Person or entity creating a trust (legal arrangement)            |
| `trustee`                            | `controls.type: agreements`                   | Person or entity administering a trust (legal arrangement)       |
| `protector`                          | `controls.type: agreements`                   | Person or entity protecting trust interests                      |
| `beneficiaryOfLegalArrangement`      | `controls.type: other_means_of_control`       | Person or entity benefiting from a trust arrangement             |

### 2.2 Mandatory Attributes

**Controller Top-Level Mandatory Attributes** *(applies to all Controller entries)*

| **Data Identifier** | **Semantic Reference** | **Definition**                                                                                  | **Data Type**  |
|---------------------|------------------------|-------------------------------------------------------------------------------------------------|----------------|
| `type`              | —                      | Discriminator field — SHALL be `"Person"` or `"Entity"`. Determines which sub-object is present | Enum (String)  |
| `jurisdiction`      | —                      | Country of legal relevance for this controller entry — ISO 3166-1 alpha-2                       | String         |
| `address`           | —                      | Address of the controller — residential for `Person`, registered for `Entity`                   | Address Object |
| `controls`          | —                      | At least one controls record describing how control is exercised                                | Array [Object] |
| `effective_date`    | —                      | Date when this control relationship became legally effective — ISO 8601 YYYY-MM-DD              | Date           |
| `evidence`          | —                      | At least one piece of supporting evidence substantiating the declared control                   | Array [Object] |

**Person Controller Mandatory Attributes** *(present when `type = "Person"`)*

| **Data Identifier** | **Semantic Reference** | **Definition**                                                            | **Data Type** |
|---------------------|------------------------|---------------------------------------------------------------------------|---------------|
| `person.first_name` | —                      | First name(s) of the natural person, including middle name(s) where applicable | String   |
| `person.surname`    | —                      | Last name(s) or surname(s) of the natural person controller               | String        |

**Entity Controller Mandatory Attributes** *(present when `type = "Entity"`)*

| **Data Identifier**       | **Semantic Reference** | **Definition**                                                                         | **Data Type** |
|---------------------------|------------------------|----------------------------------------------------------------------------------------|---------------|
| `entity.category`         | —                      | Classification — SHALL be `"legal_entity"` or `"legal_arrangement"`                    | Enum (String) |
| `entity.name`             | —                      | Complete official registered name of the entity or legal arrangement                   | String        |
| `entity.identifier`       | —                      | At least one of: `euid`, `lei`, `tax`, or `other` SHALL be present                    | Object        |
| `entity.jurisdiction`     | —                      | ISO 3166-1 alpha-2 jurisdiction in which the entity is registered or legally domiciled | String        |
| `entity.form`             | —                      | Legal form of the entity — SHALL use values from Section 2.8.6                         | String        |

**Entity Identifier Fields** *(at least one SHALL be present)*

| **Data Identifier**       | **Semantic Reference** | **Definition**                                        | **Data Type** |
|---------------------------|------------------------|-------------------------------------------------------|---------------|
| `entity.identifier.euid`  | —                      | European Unique Identifier — optional                 | String        |
| `entity.identifier.lei`   | —                      | Legal Entity Identifier per ISO 17442 — optional      | String        |
| `entity.identifier.tax`   | —                      | National tax or registration number — optional        | String        |
| `entity.identifier.other` | —                      | Any other applicable legal identifier — optional      | String        |

**Legal Arrangement Additional Mandatory Attributes** *(present when `entity.category = "legal_arrangement"` or `entity.form = "trust"`)*

| **Data Identifier**              | **Semantic Reference** | **Definition**                                                                            | **Data Type** |
|----------------------------------|------------------------|-------------------------------------------------------------------------------------------|---------------|
| `entity.subtype_info.settlement` | —                      | Instrument or document establishing the legal arrangement (e.g., trust deed)              | String        |
| `entity.subtype_info.purpose`    | —                      | Declared purpose of the legal arrangement                                                 | String        |
| `entity.subtype_info.assets`     | —                      | Description of assets held within the legal arrangement                                   | String        |

**Address Mandatory Attributes** *(applies to all Controller entries)*

| **Data Identifier**    | **Semantic Reference** | **Definition**                                                        | **Data Type** |
|------------------------|------------------------|-----------------------------------------------------------------------|---------------|
| `address.street`       | —                      | Street name of the address                                            | String        |
| `address.house_number` | —                      | House or building number                                              | String        |
| `address.locality`     | —                      | City or locality                                                      | String        |
| `address.region`       | —                      | State, province, or region                                            | String        |
| `address.postal_code`  | —                      | Postal or ZIP code                                                    | String        |
| `address.country`      | —                      | ISO 3166-1 alpha-2 country code — SHALL use values from Section 2.8.7 | String        |

**Controls Mandatory Attributes** *(at least one record per Controller entry)*

| **Data Identifier**  | **Semantic Reference** | **Definition**                                                                                       | **Data Type** |
|----------------------|------------------------|------------------------------------------------------------------------------------------------------|---------------|
| `controls.type`      | Section 2.8.3          | Array of one or more control mechanism types — SHALL use values from Section 2.8.3                   | Array [Enum]  |
| `controls.level`     | Section 2.8.2          | How control is held — SHALL be one of: `"direct"`, `"indirect"`, `"joint"`, or `"unknown"`           | Enum (String) |
| `controls.basis`     | Section 2.8.4          | Legal or structural basis for control — SHALL use values from Section 2.8.4                          | Enum (String) |
| `controls.rights`    | Section 2.8.5          | Array of economic rights associated with the control — SHALL use values from Section 2.8.5           | Array [Enum]  |

**Evidence Mandatory Attributes** *(at least one entry per Controller entry)*

| **Data Identifier** | **Semantic Reference** | **Definition**                                                                                                                                          | **Data Type** |
|---------------------|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| `evidence[n].id`    | —                      | Unique identifier, URI, or URN of the source or evidence document                                                                                       | String        |
| `evidence[n].type`  | —                      | Type of evidence document — SHALL use a value from Section 2.8.9 (e.g., `officialRegister`, `governanceChart`, `trustDeed`, `shareholderAgreement`) | String        |

### 2.3 Optional Attributes

**Person Controller Optional Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                                  | **Data Type** |
|---------------------|------------------------|-----------------------------------------------------------------|---------------|
| `person.birth_date` | —                      | Date of birth of the natural person controller — ISO 8601 YYYY-MM-DD | Date     |

**Legal Arrangement Optional Attributes** *(when `entity.category = "legal_arrangement"`)*

| **Data Identifier**                           | **Semantic Reference** | **Definition**                                           | **Data Type** |
|-----------------------------------------------|------------------------|----------------------------------------------------------|---------------|
| `entity.subtype_info.reason_for_registration` | —                      | The reason the legal arrangement was formally registered | String        |

**Controls Optional Attributes**

| **Data Identifier**          | **Semantic Reference** | **Definition**                                                                         | **Data Type**    |
|------------------------------|------------------------|----------------------------------------------------------------------------------------|------------------|
| `controls.voting_percentage` | —                      | Percentage of voting rights held — decimal value in range 0–100                        | Decimal          |
| `controls.appointment_rights`| —                      | Free text details on appointment rights                                                | String           |
| `controls.other_details`     | —                      | Free text for other control mechanisms not captured by structured fields               | String           |

**Evidence Optional Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                                                                   | **Data Type**   |
|---------------------|------------------------|--------------------------------------------------------------------------------------------------|-----------------|
| `evidence[n].url`   | —                      | URI reference to the publicly accessible source or evidence document                             | URI             |
| `evidence[n].data`  | —                      | Base64-encoded source document — SHALL be provided if `url` is absent or not publicly accessible | String (base64) |


### 2.4 Conditional Attributes

| **Condition**                                          | **Applicable Attributes**                                                                             | **Rule**                                                                             |
|--------------------------------------------------------|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| `type = "Person"`                                      | `person.*` block                                                                                      | The `person` object SHALL be present and the `entity` object SHALL be absent         |
| `type = "Entity"`                                      | `entity.*` block                                                                                      | The `entity` object SHALL be present and the `person` object SHALL be absent         |
| `entity.category = "legal_arrangement"`                | `entity.subtype_info.settlement`, `entity.subtype_info.purpose`, `entity.subtype_info.assets`         | The `subtype_info` object SHALL be present and all three fields SHALL be populated   |
| `entity.form = "trust"`                                | `entity.subtype_info.settlement`, `entity.subtype_info.purpose`, `entity.subtype_info.assets`         | The `subtype_info` object SHALL be present and all three fields SHALL be populated   |
| `evidence[n].url` is absent or not publicly accessible | `evidence[n].data`                                                                                    | `evidence[n].data` (base64-encoded) SHALL be provided                                |

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

---

### 2.8 Value Lists

#### 2.8.1 `controller.type` Values

| **Value** | **Definition**                                                                              |
|-----------|---------------------------------------------------------------------------------------------|
| `Person`  | The controller is a natural person (individual)                                             |
| `Entity`  | The controller is a legal entity or legal arrangement — further qualified by `entity.category` |

#### 2.8.2 `controls.level` Values

| **Code**   | **Definition**                                                                        |
|------------|---------------------------------------------------------------------------------------|
| `direct`   | Control exercised directly over the subject entity without intermediary entities      |
| `indirect` | Control exercised through one or more intermediary legal entities or arrangements     |
| `joint`    | Control exercised jointly with one or more other persons or entities                  |
| `unknown`  | Control structure cannot be determined at the time of attestation                     |

#### 2.8.3 `controls.type` Values

| **Value**                | **Definition**                                                                                                   |
|--------------------------|------------------------------------------------------------------------------------------------------------------|
| `voting_rights`          | Control through a majority of voting rights at general meetings                                                  |
| `appointment_rights`     | The right to appoint or remove a majority of the board of directors or management body                           |
| `agreements`             | Control through contractual agreements, articles of association, or other binding arrangements                   |
| `dominance`              | The ability to exercise dominant influence or control                                                            |
| `other_means_of_control` | Control exercised through means not explicitly listed, but resulting in significant influence                    |
| `board`                  | Control exercised through the right to appoint or remove members of the board of directors or supervisory board  |
| `veto`                   | Control exercised through veto rights over major corporate decisions (e.g., M&A, capital increases, dissolution) |
| `contractual`            | Control exercised through formal or informal agreements (e.g., shareholders' agreements, management agreements)  |
| `nominee`                | Control exercised through nominee shareholders, nominee directors, or other nominee arrangements                 |
| `profit_distribution`    | Control exercised through the right to control the distribution of profits                                       |

> **Note:** Multiple mechanism types MAY apply to a single controller. In such cases,
> `controls.type` SHALL be encoded as an array containing all applicable values.

#### 2.8.4 `controls.basis` Values

| **Code**              | **Definition**                                                              |
|-----------------------|-----------------------------------------------------------------------------|
| `corporate_position`  | Control derives from a formal position within the corporate governance structure (e.g., director, executive officer) |
| `shareholding`        | Control derives from ownership of shares conferring voting or governance rights |
| `contractual`         | Control derives from a contractual arrangement (e.g., shareholders' agreement, management agreement) |
| `legal_framework`     | Control derives from the applicable legal or regulatory framework            |
| `trust_arrangement`   | Control derives from a role within a trust or legal arrangement (e.g., trustee, protector) |
| `other`               | Control derives from a basis not covered by the above categories             |

#### 2.8.5 `controls.rights` Values

| **Code**             | **Definition**                                                    |
|----------------------|-------------------------------------------------------------------|
| `dividend_rights`    | Right to receive a share of profits distributed by the entity     |
| `liquidation_rights` | Right to receive a share of assets upon dissolution of the entity |

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

`controller.jurisdiction`, `entity.jurisdiction`, and `address.country` SHALL use
**ISO 3166-1 alpha-2** two-letter country codes.

#### 2.8.8 Date Formats

All date attributes (e.g., `effective_date`, `person.birth_date`) SHALL follow the
**ISO 8601 YYYY-MM-DD** format.

#### 2.8.9 Evidence Type Values

| **Code**                 | **Applicable To** | **Definition**                                                         |
|--------------------------|-------------------|------------------------------------------------------------------------|
| `officialRegister`       | Person, Entity    | Control verified from an official company or governance register       |
| `selfDeclaration`        | Person, Entity    | The controller themselves declared their control interest              |
| `thirdPartyVerification` | Person, Entity    | Control confirmed by a verified third party (e.g., auditor, notary)   |
| `trustDeed`              | Entity            | Legal document establishing a trust structure                          |
| `shareholderAgreement`   | Person, Entity    | Agreement defining the control or ownership structure                  |
| `articlesOfAssociation`  | Entity            | Constitutional document defining governance rights and control         |
| `governanceChart`        | Entity            | Organizational chart showing the control structure                     |


### 2.9 Integrity Rules

The following integrity rules SHALL be enforced during issuance and verification:

| **Rule ID** | **Rule**                                                                                                                                                            |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IR-01       | The `controller` array SHALL contain at least one entry                                                                                                             |
| IR-02       | At least one `Controller` entry SHALL be of `type = "Person"` to satisfy AML requirements mandating identification of natural persons who ultimately control the entity |
| IR-03       | If `controller.type = "Person"`, the `person` object SHALL be present and the `entity` object SHALL be absent                                                       |
| IR-04       | If `controller.type = "Entity"`, the `entity` object SHALL be present and the `person` object SHALL be absent                                                       |
| IR-05       | If `entity.category = "legal_arrangement"` or `entity.form = "trust"`, the `subtype_info` object SHALL be present and `settlement`, `purpose`, and `assets` SHALL all be populated |
| IR-06       | `entity.identifier` SHALL contain at least one of: `euid`, `lei`, `tax`, or `other`                                                                                |
| IR-07       | `controls.type` SHALL be an array containing at least one value from Section 2.8.3                                                                                  |
| IR-08       | `controls.level` SHALL use one of the values defined in Section 2.8.2                                                                                               |
| IR-09       | `controls.basis` SHALL use one of the values defined in Section 2.8.4                                                                                               |
| IR-10       | `controls.rights` SHALL be an array containing at least one value from Section 2.8.5                                                                                |
| IR-11       | `controls.voting_percentage`, when present, SHALL be a decimal value in the range 0–100                                                                             |
| IR-12       | Each `Controller` entry SHALL contain at least one `evidence` entry                                                                                                 |
| IR-13       | Each `evidence` entry SHALL contain a non-empty `id` and `type`                                                                                                     |
| IR-14       | If `evidence[n].url` is absent or not publicly accessible, `evidence[n].data` (base64-encoded) SHALL be provided                                                    |
| IR-15       | `evidence[n].type` SHALL use a value from Section 2.8.9                                                                                                             |
| IR-16       | All date fields (e.g., `effective_date`, `person.birth_date`) SHALL conform to ISO 8601 YYYY-MM-DD format                                                           |
| IR-17       | All jurisdiction and country fields (`controller.jurisdiction`, `entity.jurisdiction`, `address.country`) SHALL use ISO 3166-1 alpha-2 codes                        |
| IR-18       | `entity.form` SHALL use a value from Section 2.8.6                                                                                                                  |
| IR-19       | Each `Controller` entry SHALL contain a non-empty `effective_date`                                                                                                   |


## 3 Attestation Encoding

### 3.1 ISO/IEC 18013-5-Compliant Encoding

ISO/IEC 18013-5 (mdoc) is **out of scope** for this Rulebook, as offline proximity  presentation is not a current requirement for the Control Attestation.

### 3.2 SD-JWT VC-Based Encoding

The Control Attestation uses the SD-JWT VC format to allow for selective disclosure of control  structure attributes.

**Selective Disclosure:** Top-level claims (`controller`, `evidence`) SHALL be individually  selectively disclosable, enabling a legal entity to disclose only the attributes requested by  a Relying Party.
The `.` notation is used to indicate the nesting of attributes.

**Verifiable Credential Type (`vct`):** `eu.we-build:control:1`

#### 3.2.1 Attribute Encoding Table

| **Data Identifier**           | **Attribute Identifier**                                | **Encoding Format**          | **Reference / Notes**                                                                        | **Disclosable**    |
|-------------------------------|---------------------------------------------------------|------------------------------|----------------------------------------------------------------------------------------------|--------------------|
| `controller`                  | `controller`                                            | Array [Controller]           | SHALL contain at least one entry                                                             | MUST               |
| `type`                        | `controller[n].type`                                    | String                       | `"Person"` \| `"Entity"`                                                                     | MUST               |
| **Person**                    |                                                         |                              |                                                                                              |                    |
| `first_name`                  | `controller[n].person.first_name`                       | String                       | SHALL be non-empty                                                                           | MUST               |
| `surname`                     | `controller[n].person.surname`                          | String                       | SHALL be non-empty                                                                           | MUST               |
| `birth_date`                  | `controller[n].person.birth_date`                       | String (ISO 8601 YYYY-MM-DD) | Optional                                                                                     | MAY                |
| **Entity**                    |                                                         |                              |                                                                                              |                    |
| `category`                    | `controller[n].entity.category`                         | String                       | `"legal_entity"` \| `"legal_arrangement"`                                                    | MUST               |
| `name`                        | `controller[n].entity.name`                             | String                       | SHALL be non-empty                                                                           | MUST               |
| `euid`                        | `controller[n].entity.identifier.euid`                  | String                       | European Unique Identifier — optional; at least one identifier field SHALL be present        | MAY                |
| `lei`                         | `controller[n].entity.identifier.lei`                   | String (20 chars)            | LEI per ISO 17442 — optional                                                                 | MAY                |
| `tax`                         | `controller[n].entity.identifier.tax`                   | String                       | National tax or registration number — optional                                               | MAY                |
| `other`                       | `controller[n].entity.identifier.other`                 | String                       | Any other applicable identifier — optional                                                   | MAY                |
| `jurisdiction`                | `controller[n].entity.jurisdiction`                     | String (ISO 3166-1 alpha-2)  | SHALL be non-empty                                                                           | MUST               |
| `form`                        | `controller[n].entity.form`                             | String                       | SHALL use values from Section 2.8.6                                                          | MUST               |
| **subtype_info**              | `controller[n].entity.subtype_info`                     | Object                       | Mandatory when `entity.category = "legal_arrangement"` or `entity.form = "trust"`           | MUST (conditional) |
| `settlement`                  | `controller[n].entity.subtype_info.settlement`          | String                       | Mandatory when `subtype_info` is present                                                     | MUST (conditional) |
| `purpose`                     | `controller[n].entity.subtype_info.purpose`             | String                       | Mandatory when `subtype_info` is present                                                     | MUST (conditional) |
| `assets`                      | `controller[n].entity.subtype_info.assets`              | String                       | Mandatory when `subtype_info` is present                                                     | MUST (conditional) |
| `reason_for_registration`     | `controller[n].entity.subtype_info.reason_for_registration` | String                   | Optional                                                                                     | MAY                |
| **Address**                   |                                                         |                              |                                                                                              |                    |
| `street`                      | `controller[n].address.street`                          | String                       | SHALL be non-empty                                                                           | MUST               |
| `house_number`                | `controller[n].address.house_number`                    | String                       | SHALL be non-empty                                                                           | MUST               |
| `locality`                    | `controller[n].address.locality`                        | String                       | SHALL be non-empty                                                                           | MUST               |
| `region`                      | `controller[n].address.region`                          | String                       | SHALL be non-empty                                                                           | MUST               |
| `postal_code`                 | `controller[n].address.postal_code`                     | String                       | SHALL be non-empty                                                                           | MUST               |
| `country`                     | `controller[n].address.country`                         | String (ISO 3166-1 alpha-2)  | SHALL be non-empty                                                                           | MUST               |
| **Controls**                  |                                                         |                              |                                                                                              |                    |
| `type`                        | `controller[n].controls.type`                           | Array of Strings             | SHALL use values from Section 2.8.3 — at least one required                                  | MUST               |
| `level`                       | `controller[n].controls.level`                          | String                       | SHALL use values from Section 2.8.2                                                          | MUST               |
| `basis`                       | `controller[n].controls.basis`                          | String                       | SHALL use values from Section 2.8.4                                                          | MUST               |
| `voting_percentage`           | `controller[n].controls.voting_percentage`              | Decimal (0–100)              | Percentage of voting rights — optional                                                       | MAY                |
| `appointment_rights`          | `controller[n].controls.appointment_rights`             | String                       | Free text — optional                                                                         | MAY                |
| `other_details`               | `controller[n].controls.other_details`                  | String                       | Free text for other control mechanisms — optional                                            | MAY                |
| `rights`                      | `controller[n].controls.rights`                         | Array of Strings             | SHALL use values from Section 2.8.5                                                          | MUST               |
| `effective_date`              | `controller[n].effective_date`                          | String (ISO 8601 YYYY-MM-DD) | Date control became effective — SHALL be non-empty                                           | MUST               |
| **Evidence**                  |                                                         |                              |                                                                                              |                    |
| `id`                          | `controller[n].evidence[m].id`                          | String                       | Unique identifier, URI, or URN — SHALL be non-empty                                          | MUST               |
| `type`                        | `controller[n].evidence[m].type`                        | String                       | SHALL use values from Section 2.8.9 — SHALL be non-empty                                     | MUST               |
| `url`                         | `controller[n].evidence[m].url`                         | URI                          | URI reference to source document — optional                                                  | MAY                |
| `data`                        | `controller[n].evidence[m].data`                        | String (base64)              | Base64-encoded source — SHALL be provided if `url` not publicly accessible                   | MAY                |
| **Metadata**                 |                                                             |                              |                                                                                       |                    |
| `issuance_date`              | `iat`                                                       | Number (Unix timestamp)      | Date and time when the attestation was issued (ISO 8601); RFC 7519                    | MUST NOT           |
| `expiry_date`                | `exp`                                                       | Number (Unix timestamp)      | Date and time when the attestation expires (ISO 8601); RFC 7519                       | MUST NOT           |
| `issuing_entity`             | `iss`                                                       | String (URI or DID)          | Identifier of the competent institution that issued the attestation; RFC 7519         | MUST NOT           |
| `attestation_legal_category` | `attestation_legal_category`                                | String                       | One of "EAA" or "QEAA" as defined by eIDAS 2                                          | MUST NOT           |
| `vct`                        | `vct`                                                       | String                       | The vct definition                                                                    | MUST NOT           |
| `cnf`                        | `cnf`                                                       | String                       | Cryptographic Key Binding                                                             | MUST NOT           |
| `schema_version`             | `schema_version`                                            | String                       | Version of the schema used; optional                                                  | MAY                |
| `trust_anchor_url`           | `trust_anchor_url`                                          | String (URI)                 | URL where the trust anchor for verifying this attestation can be retrieved; optional  | MAY                |

**Notes:**

- **MUST**: The claim SHALL be selectively disclosable — the holder MAY choose to disclose or
  withhold this claim when presenting the credential to a Relying Party.
- **MUST NOT**: The claim SHALL NOT be selectively disclosable — it is always present in plain
  text in the JWT header/payload and cannot be withheld by the holder, as it is required for
  credential verification and trust establishment.
- **MUST (conditional)**: The claim SHALL be selectively disclosable and SHALL be present when
  the specified condition is met.
- `controller` entries are indexed as `[n]` where `n` starts at `0`; at least one controller
  SHALL be present, and at least one SHALL be of `type = "Person"`.
- `evidence` entries within each controller are indexed as `[m]` where `m` starts at `0`;
  at least one evidence entry SHALL be present per controller.
- `iat`, `exp`, and `iss` follow RFC 7519 standard JWT claim naming conventions.

#### 3.2.2 Status Claim

For SD-JWT VC-compliant Control Attestations, the attestation MUST include a `status` claim if
the technical validity period is greater than 24 hours. This claim enables Relying Parties to
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
    "status_list_credential": "https://issuer.example.com/status/control/2025",
    "status_list_index": 456,
    "status_purpose": "revocation"
  }
}
```
3.2.3 Example Payload

The following is a non-normative example of a Control Attestation SD-JWT VC payload
demonstrating a natural person controller, a legal entity controller, and a legal arrangement
controller:
```
{
  "vct": "eu.we-build:control:1",
  "iss": "https://issuer.example.com",
  "iat": 1736935200,
  "exp": 1768471200,
  "issuing_entity": "did:example:company-456",
  "attestation_legal_category": "EAA",
  "schema_version": "0.9.0",
  "trust_anchor_url": "https://trust.webuildconsortium.eu/anchors/eidas-tl",

  "controller": [
    {
      "type": "Person",
      "jurisdiction": "DE",
      "person": {
        "first_name": "Alice",
        "surname": "Smith",
        "birth_date": "1975-03-20"
      },
      "address": {
        "street": "Hauptstrasse",
        "house_number": "10",
        "locality": "Berlin",
        "region": "Berlin",
        "postal_code": "10115",
        "country": "DE"
      },
      "controls": {
        "type": ["voting_rights", "board"],
        "level": "direct",
        "basis": "shareholding",
        "voting_percentage": 60.0,
        "appointment_rights": "Right to appoint majority of supervisory board",
        "rights": ["dividend_rights", "liquidation_rights"]
      },
      "effective_date": "2020-01-15",
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
        "name": "HoldCo GmbH",
        "identifier": {
          "euid": "DE987654321",
          "lei": "529900T8BM49AURSDO55",
          "tax": "DE123456789"
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
      "controls": {
        "type": ["nominee", "voting_rights"],
        "level": "indirect",
        "basis": "shareholding",
        "voting_percentage": 40.0,
        "rights": ["dividend_rights"]
      },
      "effective_date": "2019-06-01",
      "evidence": [
        {
          "id": "src-002",
          "type": "governanceChart",
          "url": "https://example.com/docs/governance-chart-2024.pdf"
        }
      ]
    },
    {
      "type": "Entity",
      "jurisdiction": "LU",
      "entity": {
        "category": "legal_arrangement",
        "name": "Smith Family Trust",
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
      "controls": {
        "type": ["agreements", "other_means_of_control"],
        "level": "indirect",
        "basis": "trust_arrangement",
        "voting_percentage": null,
        "other_details": "Control exercised through trustee appointment rights over beneficiary assets",
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
    "status_list_credential": "https://issuer.example.com/status/control/2025",
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
Sample payloads are provided under `../data-schemas/sd-jwt/sample-data/control-sd-jwt-sample.json`

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

| **Item Reference**                     | **Standard name/details**                                                                                                                                                                                                                                                                         |
|----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [European Digital Identity Regulation] | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework                          |
| [AMLR 2024/1624]                       | Regulation (EU) 2024/1624 of the European Parliament and of the Council on the prevention of the use of the financial system for the purposes of money laundering or terrorist financing                                                                                                          |
| [HAIP]                                 | Yasuda, K. et al, OpenID4VC High Assurance Interoperability Profile, OpenId Foundation, Version draft-03                                                                                                                                                                                          |
| [IANA-JWT-Claims]                      | IANA JSON Web Token Claims Registry. Available: https://www.iana.org/assignments/jwt/jwt.xhtml                                                                                                                                                                                                    |
| [ICAO 9303]                            | ICAO Doc 9303 — Machine Readable Travel Documents. Available: https://www.icao.int/publications/pages/publication.aspx?docnum=9303                                                                                                                                                                |
| [ISO/IEC 18013-5]                      | ISO/IEC 18013-5, Personal identification — ISO-compliant driving licence - Part 5: Mobile driving licence (mDL) application, First edition, 2021-09                                                                                                                                               |
| [ISO 3166-1]                           | ISO 3166-1 — Codes for the representation of names of countries and their subdivisions. Available: https://www.iso.org/iso-3166-country-codes.html                                                                                                                                                |
| [ISO 8601]                             | ISO 8601 — Date and time format. Available: https://www.iso.org/iso-8601-date-and-time-format.html                                                                                                                                                                                                |
| [OIDC]                                 | Sakimura, N. et al., "OpenID Connect Core 1.0", OpenID Foundation. Available: https://openid.net/specs/openid-connect-core-1_0.html                                                                                                                                                               |
| [RFC 2119]                             | RFC 2119 — Key words for use in RFCs to Indicate Requirement Levels, S. Bradner, March 1997                                                                                                                                                                                                       |
| [RFC 3339]                             | RFC 3339 — Date and Time on the Internet: Timestamps, G. Klyne et al., July 2002                                                                                                                                                                                                                  |
| [RFC 7519]                             | RFC 7519 — JSON Web Token (JWT), M. Jones et al., May 2015                                                                                                                                                                                                                                        |
| [RFC 8610]                             | RFC 8610 — Concise Data Definition Language (CDDL): A Notational Convention to Express Concise Binary Object Representation (CBOR) and JSON Data Structures, H. Birkholz et al., June 2019                                                                                                        |
| [RFC 8943]                             | RFC 8943 — Concise Binary Object Representation (CBOR) Tags for Date, M. Jones et al., November 2020                                                                                                                                                                                              |
| [RFC 8949]                             | RFC 8949 — Concise Binary Object Representation (CBOR), C. Bormann et al., December 2020                                                                                                                                                                                                          |
| [SD-JWT VC]                            | SD-JWT-based Verifiable Credentials (SD-JWT VC). Available: https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/, version draft-ietf-oauth-sd-jwt-vc-09                                                                                                                                   |
| [Topic 7]                              | ARF Annex 2 - Topic 7 - Attestation revocation and revocation checking. Available: https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a237-topic-7-attestation-revocation-and-revocation-checking |