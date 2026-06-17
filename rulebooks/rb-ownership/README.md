# Attestation Rulebook for attestations of type Ownership Attestation

* Author(s):
  * [Florin Coptil, Robert Bosch GmbH]
* Reviewer(s):
  * [Baumgardt Michaela, Commerzbank]
  * [Stephan-A Fuchs, Deutsche Bank]

| Version | Date       | Description                                                     |
|---------|------------|-----------------------------------------------------------------|
| 0.1     | 23.03.2026 | Initial draft based on the WeBuild design attestations meetings |
| 0.2     | 10.05.2026 | Updates for addresses and identifiers                           |
| 0.3     | 01.06.2026 | Updates of content based on meetings                            |

* Contact:
  * [Florin Coptil](mailto:florin.coptil@bosch.com)

* Feedback:

---

## 1 Introduction

This attestation addresses the following question:

**Who are the Shareholders and Economic Interest Holders of this legal entity?**

A Shareholder or Economic Interest Holder is any natural person or legal entity
that directly or indirectly holds an ownership stake in a legal entity.

### 1.1 Document scope and purpose

The Ownership Attestation records all natural and legal persons holding direct
or indirect ownership interests in a legal entity, providing comprehensive
transparency on beneficial ownership structures and economic interests. This
attestation is a critical component of both Know Your Customer (KYC) and Know
Your Supplier (KYS) processes within the EUDI Wallet ecosystem, supporting
effective risk management, regulatory compliance, and anti-money laundering
(AML) obligations.

A Shareholder or Economic Interest Holder is defined as any natural person or
legal entity that directly or indirectly holds an ownership stake in a legal
entity, based on:

- **Ownership stake** — direct or indirect share ownership, including equity
  interests, partnership shares, or equivalent economic interests, expressed as
  a percentage (0–100) or as a rule string where the exact percentage is not
  determinable
- **Ownership type** — whether the interest is held directly by the person in
  the subject entity without intermediary entities, or indirectly through one
  or more intermediate legal entities
- **Nominal value** — the nominal monetary value of the ownership interest held,
  expressed in the applicable currency, or null where nominal value is not
  applicable or not available
- **Share class** — the type of shares or interest held (ordinary, preferred,
  dual-class, or other), determining the voting and economic rights associated
  with the holding
- **Economic rights** — the specific economic entitlements attached to the
  ownership interest, comprising:
  - *Dividend rights* — the entitlement to receive a share of distributed
    profits
  - *Liquidation rights* — the entitlement to receive a share of residual
    assets upon winding up of the entity
- **Ownership threshold** — the percentage of shares or economic interest held,
  regardless of whether control thresholds are met, as required under
  AMLR / AMLD6 and applicable company law

### 1.1 Document scope and purpose

The Ownership Attestation records all natural and legal persons holding direct or indirect
ownership in a legal entity, providing comprehensive transparency on beneficial ownership
structures and economic interests. This attestation is a critical component of both Know Your
Customer (KYC) and Know Your Supplier (KYS) processes within the EUDI Wallet ecosystem,
supporting effective risk management, regulatory compliance, and anti-money laundering (AML)
obligations.

### 1.2 Document structure

This Rulebook is structured as follows:

- Chapter 2 describes the attestation attributes and metadata in an encoding-independent
  manner, including the data model.
- Chapter 3 specifies how the attestation attributes and metadata are encoded: Section 3.2
  covers SD-JWT VC-based encoding.
- Chapter 4 specifies attestation usage scenarios, Relying Party obligations, and integration
  with KYC/KYS workflows.
- Chapter 5 defines trust anchors and verification mechanisms for issuer authorization.
- Chapter 6 defines revocation mechanisms for the attestation.
- Chapter 7 provides compliance information regarding the EUBW framework, AML regulations,
  corporate governance standards, and applicable data protection laws.
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

This document uses the terminology specified in Annex 1 of the ARF.

**Additional terminology specific to this attestation:**

| **Term**                                             | **Definition**                                                                                                                                                                                         |
|------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ownership                                            | A comprehensive record of all natural and legal persons holding direct or indirect ownership or control in a legal entity, including ownership percentages and supporting evidence                      |
| Beneficial Owner / Ultimate Beneficial Owner (UBO)   | A natural person who ultimately owns or controls a legal entity, either directly or indirectly (typically defined as holding ≥25% ownership or control, per AMLD requirements)                         |
| Direct Ownership                                     | Ownership interest held directly by a natural or legal person in the subject entity, without intermediary entities                                                                                      |
| Indirect Ownership                                   | Ownership interest held through one or more intermediary legal entities (e.g., Person A owns 50% of Company B, which owns 60% of Company C → Person A has 30% indirect ownership in Company C)         |
| Total Ownership                                      | The sum of direct and indirect ownership percentages across all layers of the ownership structure                                                                                                       |
| Ownership Category                                   | Classification of the type of ownership or control relationship (e.g., shareholder, controller via voting rights, trustee, partner, holder of convertible rights, person exercising dominant influence) |
| Legal Entity Identifier Chain                        | The list of all intermediate legal entities through which indirect ownership is held, enabling full traceability of ownership layers                                                                    |
| KYC                                                  | Know Your Customer – due diligence process for verifying customer identity and assessing risk in financial relationships                                                                                |
| KYS                                                  | Know Your Supplier – due diligence process for verifying supplier credentials, integrity, and risk exposure                                                                                             |
| PEP                                                  | Politically Exposed Person – individual entrusted with prominent public functions, posing higher risk for corruption or bribery                                                                         |
| EUCC                                                 | EU Company Certificate – attestation establishing the legal existence and identity of a legal entity within the EU                                                                                      |
| Evidence                                             | Supporting documentation substantiating the ownership structure calculation (e.g., shareholder register, organizational chart, trust deed)                                                              |

---

## 2 Attestation attributes and metadata

The Ownership Attestation is designed to provide a complete, verifiable representation of an
entity's ownership structure in a standardized digital format. This attestation supports
transparency, compliance, and risk management by enabling automated verification of beneficial
ownership across complex, multi-tiered corporate structures.

### 2.1 Introduction

**Data Model:**

```
Owner[1..n]
├── type(M)                    NP = natural person | LE = legal entity
├── NaturalPerson
│ ├── first_name (M)
│ ├── surname (M)
│ └── date_of_birth (M)
├── LegalPerson
│ ├── legal_name (M)
│ ├── legal_form (M)
│ └── identifier [String] (M) identifier: euid, lei, tax, ...
├── LegalArrangements
│ ├── legal_name (M) description of the legal arrangement: a sequence of characters, letters or numbers
│ └── identifier (M) identifier of the legal arrangement: a sequence of characters, letters or numbers
│ └── info ( law governing- ISO 3166-1 alpha-3)
│ ├── settlement [String] (M) 
│ ├── purpose [String] (M) 
│ ├── assets [String] (M) 
│ ├── reason for registration
├── Address
│ ├── street (M)
│ ├── house_number (M)
│ ├── locality (M)
│ ├── region (M)
│ ├── postal_code (M)
│ └── country (M)
└── Ownership[]
│ ├── legal_identifier(M) identifier of the owned entity
│ ├── type(M) direct | indirect
│ ├── stake(M)  - % (0-100) or rule string
│ ├── amount(M)  
│ │ ├── value(M)
│ │ ├── currency(M)  
│ ├── category ordinary[String] (M) - [preferred | dual-class | other]
│ ├── economic_rights[String] (M) - [dividend_rights, liquidation_rights]
│ ├── legal_arrangement (M) identifier 
│ ├── place of administration (O) (in case of different != residence )
└─ Evidence        [1...n]   (at least one piece of supporting evidence required)
```


**Explanation:**

- The `ownership` attestation SHALL contain at least one natural person who exercises ownership
  (to comply with AML requirements that mandate identification of natural persons who ultimately
  own the entity).
- The `ownership` attestation MAY contain zero or more legal_person entries, representing
  intermediate legal entities in the ownership chain.
- For each `natural_person` owner:
  - It SHALL include a `first_name` and `surname`.
  - It SHALL include a `date_of_birth`.
  - It SHALL include a mandatory `Address`.
  - It SHALL include at least one `Ownership` record detailing the ownership interest.
- For each `legal_person` owner:
  - It SHALL include `legal_name` and `legal_form`.
  - It SHALL include a mandatory `identifier` object (with at least one of EUID, LEI, TAX
    specified).
  - It SHALL include a mandatory `Address`.
  - It SHALL include at least one `Ownership` record detailing the ownership interest.
- The `ownership` attestation SHALL include at least one piece of evidence (e.g., governance
  chart, shareholder agreement, articles of association) substantiating the ownership
  calculation. Multiple pieces of evidence MAY be included for complex structures.

| **Data Identifier**          | **Semantic Reference** | **Definition**                                                                                          | **Data type** |
|------------------------------|------------------------|---------------------------------------------------------------------------------------------------------|---------------|
| NaturalPerson attributes     | ---                    | Identification and personal details of natural persons with ownership interests                         | Object        |
| LegalPerson attributes       | ---                    | Identification and legal details of legal entities with ownership interests                             | Object        |
| Address attributes           | ---                    | Address for natural or legal person owner                                                               | Object        |
| Ownership attributes         | ---                    | Quantitative ownership data (stake, type, amount) and ownership category classification                 | Object        |
| Evidence attributes          | ---                    | References to supporting documentation substantiating the ownership structure                           | Object        |

**Attestation Classification:**

This attestation type is classified as:
- **"EAA"** within the EUBW Wallet ecosystem, as it is typically self-issued by the legal
  entity subject to the ownership disclosure (i.e., the entity issues an attestation about its
  own ownership structure).

### 2.2 Mandatory attributes

**NaturalPerson Mandatory Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                                                  | **Data type**     |
|---------------------|------------------------|---------------------------------------------------------------------------------|-------------------|
| first_name          | --                     | First name(s), including middle name(s) where applicable, of the natural person | String            |
| surname             | --                     | Last name(s) or surname(s) of the natural person who holds ownership or control | String            |
| date_of_birth       | --                     | Day, month, and year of birth of the natural person (ISO 8601)                  | Date (YYYY-MM-DD) |

**LegalPerson Mandatory Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                                                                | **Data type** |
|---------------------|------------------------|-----------------------------------------------------------------------------------------------|---------------|
| legal_name          | --                     | The complete official name of the legal entity which holds ownership interests in this entity | String        |
| legal_form          | --                     | The legal form of the owning legal entity (e.g., GmbH, AG, Ltd, SA, BV)                      | String        |
| identifier          | --                     | At least one legal entity identifier (euid, lei, tax, or equivalent)                         | String        |

**Address Mandatory Attributes**

Applies to both NaturalPerson and LegalPerson owners:

| **Data Identifier** | **Semantic Reference** | **Definition**                                             | **Data type** |
|---------------------|------------------------|------------------------------------------------------------|---------------|
| street              | --                     | Street name of the address                                 | String        |
| house_number        | --                     | House or building number of the address                    | String        |
| locality            | --                     | City or locality of the address                            | String        |
| region              | --                     | State, province, or region of the address                  | String        |
| postal_code         | --                     | Postal or ZIP code of the address                          | String        |
| country             | --                     | ISO 3166-1 alpha-2 country code of the address             | String        |

**Ownership Mandatory Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                                                             | **Data type**         |
|---------------------|------------------------|--------------------------------------------------------------------------------------------|-----------------------|
| legal_identifier    | --                     | Identifier of the owned entity                                                             | String                |
| type                | --                     | Type of ownership: direct or indirect                                                      | String (direct/indirect) |
| stake               | --                     | Percentage of ownership (0–100) or rule string                                             | Decimal or String     |
| amount              | --                     | Nominal value and currency of the ownership stake, or null if not applicable               | String or null        |
| category            | --                     | Category of shares: ordinary, preferred, dual-class, or other                              | String (enumeration)  |
| economic_rights     | --                     | Economic rights associated with the ownership (e.g., dividend_rights, liquidation_rights)  | Array of Strings      |

**Evidence Mandatory Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                                                            | **Data type** |
|---------------------|------------------------|-------------------------------------------------------------------------------------------|---------------|
| evidence_id         | ---                    | URI reference to the evidence document (e.g., organizational chart, shareholder register) | String        |
| evidence_type       | ---                    | Defines the type of the object, which SHALL be "Evidence"                                 | String        |

### 2.3 Optional attributes

**LegalPersonIdentifier Optional Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                              | **Data type** |
|---------------------|------------------------|---------------------------------------------|---------------|
| euid                | --                     | EUID per ISO 3166-1 alpha-2                 | String        |
| lei                 | --                     | Legal Entity Identifier (LEI) per ISO 17442 | String        |
| tax                 | --                     | National company registration number        | String        |

**Evidence Optional Attributes**

| **Data Identifier**   | **Semantic Reference** | **Definition**                                                                                                                                     | **Data type**   |
|-----------------------|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| evidence_data         | --                     | The actual organizational structure document as a base64-encoded string (required if evidence_id does not contain a URI to an accessible location) | String (base64) |
| evidence_confirmation | --                     | Boolean confirmation that the organizational structure document is current and has been used as the basis for the ownership calculation             | Boolean         |
| evidence_date         | --                     | The date when the evidence document was created or last updated (ISO 8601)                                                                         | Date            |

### 2.4 Conditional attributes

No conditional attributes are defined for this attestation type. All attributes are either
mandatory or optional as specified above.

### 2.5 Mandatory metadata

| **Data Identifier**        | **Definition**                                                                                                                    | **Data type** |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------|---------------|
| issuance_date              | The date and time when the attestation was issued (ISO 8601)                                                                      | DateTime      |
| expiry_date                | The date and time when the attestation expires (ISO 8601)                                                                         | DateTime      |
| issuing_entity             | The identifier of the legal entity that issued the attestation (typically the subject entity itself for self-issued attestations) | String        |
| attestation_legal_category | Indicates the legal category of this attestation ("EAA")                                                                          | String        |
| vct                        | A URI or other collision-resistant identifier that defines the type of the SD-JWT Verifiable Credential                                                            | String          |

### 2.6 Optional metadata

| **Data Identifier** | **Definition**                                                             | **Data type** |
|---------------------|----------------------------------------------------------------------------|---------------|
| trust_anchor_url    | URL where the trust anchor for verifying this attestation can be retrieved | URI           |
| schema_version      | Version of the schema used                                                 | String        |

### 2.7 Conditional metadata

No conditional metadata elements are defined for this attestation type.

### 2.8 Value Lists

#### 2.8.1 Ownership Category Codes

The `category` attribute SHALL use one of the following standardized values:

| **Code**                                         | **Definition**                                                                                                                                                                    |
|--------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ordinary                                         | Standard shares with full voting and economic rights                                                                                                                              |
| preferred                                        | Shares with preferential rights (e.g., priority dividends) but potentially limited voting rights                                                                                  |
| dual-class                                       | Share structure with multiple classes carrying different voting rights                                                                                                             |
| other                                            | Any other share category not covered by the above                                                                                                                                 |

#### 2.8.2 Ownership Type Codes

The `type` attribute within Ownership SHALL use one of the following values:

| **Code**   | **Definition**                                                                                       |
|------------|------------------------------------------------------------------------------------------------------|
| direct     | Ownership interest held directly by the owner in the subject entity without intermediary entities    |
| indirect   | Ownership interest held through one or more intermediary legal entities                              |

#### 2.8.3 Economic Rights Codes

The `economic_rights` attribute SHALL use one or more of the following standardized values:

| **Code**             | **Definition**                                                          |
|----------------------|-------------------------------------------------------------------------|
| dividend_rights      | Right to receive a share of profits distributed by the entity           |
| liquidation_rights   | Right to receive a share of assets upon dissolution of the entity       |

#### 2.8.4 Ownership Controller Category Codes

The `ownership_category` attribute SHALL use one of the following standardized values:

| **Code**                                         | **Definition**                                                                                                                                                                    |
|--------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Direct shareholder                               | Natural or legal person holding shares directly in the subject entity                                                                                                             |
| Indirect shareholder                             | Natural or legal person holding shares through one or more intermediate entities                                                                                                  |
| Controller via voting or governance rights       | Natural or legal person exercising control through voting rights, board representation, or governance mechanisms, regardless of ownership percentage                               |
| Trustee / beneficiary in fiduciary arrangements  | Natural or legal person acting as trustee or beneficiary in a trust, foundation, or similar fiduciary arrangement                                                                 |
| Partner in partnership structures                | Natural or legal person holding a partnership interest in a partnership entity                                                                                                    |
| Holder of convertible rights                     | Natural or legal person holding convertible instruments (e.g., convertible bonds, options, warrants) that may be converted into equity                                            |
| Person exercising dominant influence             | Natural or legal person exercising dominant influence over the entity through contractual arrangements, operational control, or other means                                        |

### 2.9 Integrity Rules

TODO Florin

---

## 3 Attestation encoding

### 3.1 ISO/IEC 18013-5-compliant encoding

ISO/IEC 18013-5 (also called mdoc) is out of scope for this Rulebook, as offline proximity
presentation is not a current requirement for the Ownership attestation.

### 3.2 SD-JWT VC-based encoding

The Ownership attestation uses the SD-JWT VC format to allow for selective disclosure of
ownership structure attributes.

**Selective Disclosure:** Top-level claims (`owner`, `evidence`) SHALL be individually
selectively disclosable, enabling a legal entity to disclose only the attributes requested by
a Relying Party.

The `.` notation is used to indicate the nesting of attributes.

**Verifiable Credential Type (`vct`):** `vct: eu.we-build.ownership.1`

#### 3.2.1 Attribute Encoding Table

| **Data Identifier**        | **Attribute identifier**               | **Encoding format**          | **Reference/Notes**                                                                                                                                     | **Disclosable** |
|----------------------------|----------------------------------------|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| owner                      | owner                                  | Array [Owner]                | Array of owner objects; **SHALL** contain at least one owner entry                                                                                      | MUST            |
| type                       | owner[n].type                          | String                       | NP = natural person / LE = legal entity; SHALL be non-empty                                                                                             | MUST            |
| **NaturalPerson**          |                                        |                              |                                                                                                                                                         |
| first_name                 | owner[n].natural_person.first_name     | String                       | First name(s) of the natural person owner; SHALL be non-empty                                                                                           | MUST            |
| surname                    | owner[n].natural_person.surname        | String                       | Surname(s) of the natural person owner; SHALL be non-empty                                                                                              | MUST            |
| date_of_birth              | owner[n].natural_person.date_of_birth  | String (ISO 8601 YYYY-MM-DD) | Date of birth of the natural person owner; SHALL be non-empty                                                                                           | MUST            |
| **LegalPerson**            |                                        |                              |                                                                                   
| legal_name                 | owner[n].legal_person.legal_name       | String                       | Complete official name of the legal entity owner; SHALL be non-empty                                                                                    | MUST            |
| legal_form                 | owner[n].legal_person.legal_form       | String                       | Legal form of the owning legal entity (e.g., GmbH, AG, Ltd)                                                                                             | MUST            |
| identifier                 | owner[n].legal_person.identifier       | String                       | At least one legal entity identifier (euid, lei, tax, or equivalent)                                                                                    | MUST            |
| **LegalPersonIdentifier**  |                                        |                              |                                                                                                                                                         |
| euid                       | owner[n].legal_person.identifier.euid  | String                       | EUID of the controlling legal entity; optional                                                                                                          | MUST            |
| lei                        | owner[n].legal_person.identifier.lei   | String (20 characters)       | LEI code of the controlling legal entity; optional                                                                                                      | MUST            |
| tax                        | owner[n].legal_person.identifier.tax   | String                       | National company registration number; optional                                                                                                          | MUST            |
| **Address**                |                                        |                              |                                                                                                                                                         |
| street                     | owner[n].address.street                | String                       | Street name of the address; SHALL be non-empty                                                                                                          | MUST            |
| house_number               | owner[n].address.house_number          | String                       | House or building number of the address; SHALL be non-empty                                                                                             | MUST            |
| locality                   | owner[n].address.locality              | String                       | City or locality of the address; SHALL be non-empty                                                                                                     | MUST            |
| region                     | owner[n].address.region                | String                       | State, province, or region of the address; SHALL be non-empty                                                                                           | MUST            |
| postal_code                | owner[n].address.postal_code           | String                       | Postal or ZIP code of the address; SHALL be non-empty                                                                                                   | MUST            |
| country                    | owner[n].address.country               | String (ISO 3166-1 alpha-2)  | Country code of the address; SHALL be non-empty                                                                                                         | MUST            |
| **Ownership**              |                                        |                              |                                                                                                                                                         |
| legal_identifier           | owner[n].ownership[m].legal_identifier | String                       | Identifier of the owned entity; SHALL be non-empty                                                                                                      | MUST            |
| type                       | owner[n].ownership[m].type             | String                       | direct or indirect; SHALL use values from Section 2.8.2                                                                                                 | MUST            |
| stake                      | owner[n].ownership[m].stake            | Decimal or null              | Percentage of ownership (0–100) or rule string; SHALL be non-empty                                                                                      | MUST            |
| value                      | owner[n].ownership[m].amount.value     | Decimal or null              | Nominal value and currency of the ownership stake, or null if not applicable                                                                            | MUST            |
| currency                   | owner[n].ownership[m].amount.currency  | String or null               | Nominal value and currency of the ownership stake, or null if not applicable                                                                            | MUST            |
| category                   | owner[n].ownership[m].category         | String (enumeration)         | Share category: preferred, dual-class, or other; SHALL use values from Section 2.8.1                                                                    | MUST            |
| economic_rights            | owner[n].ownership[m].economic_rights  | Array of Strings             | Economic rights associated with the ownership; SHALL use values from Section 2.8.3                                                                      | MUST            |
| **Evidence**               |                                        |                              |                                                                                                                                                         |
| evidence_id                | evidence[n].evidence_id                | String (URI)                 | URI reference to the evidence document (e.g., organizational chart, shareholder register); SHALL be non-empty                                           | MUST            |
| evidence_type              | evidence[n].evidence_type              | String                       | Defines the type of the object; SHALL be "Evidence"                                                                                                     | MUST            |
| evidence_data              | evidence[n].evidence_data              | String (base64)              | Actual organizational structure document as a base64-encoded string; required if evidence_id does not contain a URI to an accessible location; optional | MUST            |
| evidence_confirmation      | evidence[n].evidence_confirmation      | Boolean                      | Confirmation that the organizational structure document is current and used as the basis for the ownership calculation; optional                        | MUST            |
| evidence_date              | evidence[n].evidence_date              | String (ISO 8601 YYYY-MM-DD) | Date when the evidence document was created or last updated; optional                                                                                   | MUST            |
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
- **MUST NOT**: The claim SHALL NOT be selectively disclosable — it is always present in plain
  text in the JWT header/payload and cannot be withheld by the holder, as it is required for
  credential verification and trust establishment.
- `owner` entries are indexed as `[n]` where `n` starts at 0; at least one owner SHALL be
  present, and at least one SHALL be a natural person.
- `ownership` entries within each owner are indexed as `[m]` where `m` starts at 0; at least
  one ownership record SHALL be present per owner.
- `evidence` entries are indexed as `[n]` where `n` starts at 0; at least one evidence entry
  SHALL be present.
- `iat`, `exp`, and `iss` follow RFC 7519 standard JWT claim naming conventions.

#### 3.2.2 Status Claim

For SD-JWT VC-compliant Ownership attestations, the attestation MUST include a `status` claim
if the technical validity period is greater than 24 hours. This claim enables Relying Parties
to determine if a credential has been revoked via a status list mechanism, as specified in
SD-JWT VC.

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
 "status_list_credential": "https://issuer.example.com/status/ownership/2025",
 "status_list_index": 456,
 "status_purpose": "revocation"
  }
}
```

3.2.3 Example Payload
The following is a non-normative example of an Ownership SD-JWT VC payload:

```
{
  "vct": "eu.we-build.ownership.1",
  "iss": "https://issuer.example.com",
  "iat": 1736935200,
  "exp": 1768471200,
  "issuing_entity": "did:example:legal-entity-789",
  "attestation_legal_category": "EAA",
  "schema_version": "1.0",

  "owner": [
    {
      "type": "NP",
      "natural_person": {
        "first_name": "Anna",
        "surname": "Schmidt",
        "date_of_birth": "1978-04-15"
      },
      "address": {
        "street": "Hauptstraße",
        "house_number": "12",
        "locality": "Berlin",
        "region": "Berlin",
        "postal_code": "10115",
        "country": "DE"
      },
      "ownership": [
        {
          "legal_identifier": "DE-HRB-123456",
          "type": "direct",
          "stake": 51.0,
          "amount": {
            "value": 510000,
            "currency": "EUR"
          },
          "category": "ordinary",
          "economic_rights": ["dividend_rights", "liquidation_rights"]
        }
      ]
    },
    {
      "type": "LE",
      "legal_person": {
        "legal_name": "Holding GmbH",
        "legal_form": "GmbH",
        "identifier": "DE-HRB-654321"
      },
      "address": {
        "street": "Industriestraße",
        "house_number": "5",
        "locality": "Munich",
        "region": "Bavaria",
        "postal_code": "80331",
        "country": "DE"
      },
      "ownership": [
        {
          "legal_identifier": "DE-HRB-123456",
          "type": "indirect",
          "stake": 49.0,
          "amount": {
            "value": 490000,
            "currency": "EUR"
          },
          "category": "preferred",
          "economic_rights": ["dividend_rights"]
        }
      ]
    }
  ],

  "evidence": [
    {
      "evidence_id": "urn:uuid:550e8400-e29b-41d4-a716-446655440000",
      "evidence_type": "Evidence",
      "evidence_confirmation": true,
      "evidence_date": "2025-01-10"
    }
  ],

  "status": {
    "type": "status-list",
    "status_list_credential": "https://issuer.example.com/status/ownership/2025",
    "status_list_index": 456,
    "status_purpose": "revocation"
  },
  "schema_version": "0.3.0",
  "trust_anchor_url": "https://trust.webuildconsortium.eu/anchors/eidas-tl"

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

@TODO — To be discussed: which stakeholders will support this format and which use cases require it.

## 4 Attestation usage
### 4.1. Issuance process ###

**Attestation**
The Issuer SHALL implement the base issuer obligation as defined in the Issuer Obligation specification:
https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-base/verifier-base-verification.md#41-issuer-obligations

### 4.2 Relying Party Obligations
When receiving and processing an attestation, the Relying Party SHALL perform the following verification obligations.
### 4.2.1 – 4.2.8 Base Verification Process
The Relying Party SHALL perform the base attestation verification process as defined in the Base Verification specification:
https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-base/verifier-base-verification.md#42-relying-party-obligations

### 4.2.9 Validate Integrity Rules
Validation of integrity and policy rules will be specified in a future version of this Rulebook.

## 5 Trust anchors
This chapter will be completed in a future version of this Rulebook.

## 6 Revocation
This chapter will be completed in a future version of this Rulebook.

## 7 References
This chapter will be completed in a future version of this Rulebook.

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
