# Attestation Rulebook for attestations of type Ownership List Attestation

* Author(s): 
    * [Florin Coptil, Robert Bosch GmbH] 

* Reviewer(s):
    * [......, Deutsche Bank]

| Version | Date       | Description                                                     |
|---------|------------|-----------------------------------------------------------------|
| 0.1     | 23.03.2026 | Initial draft based on the WeBuild design attestations mettings |

* Contact:
  <a href="mailto:florin.coptil@bosch.com">Florin Coptil</a>
  
* Feedback:

## 1 Introduction

### 1.1 Document scope and purpose

The Ownership List Attestation records all natural and legal persons holding direct or indirect ownership or control in a legal entity, providing comprehensive transparency on beneficial ownership structures and economic interests. This attestation is a critical component of both Know Your Customer (KYC) and Know Your Supplier (KYS) processes within the EUDI Wallet ecosystem, supporting effective risk management, regulatory compliance, and anti-money laundering (AML) obligations.

### 1.2 Document structure

This Rulebook is structured as follows:

- Chapter 2 describes the Ownership List attestation attributes and metadata in an encoding-independent manner, including the hierarchical ownership data model.
- Chapter 3 specifies how the attestation attributes and metadata are encoded:Section 3.1: ISO/IEC 18013-5-compliant encoding (applicability assessment)
- Chapter 4 specifies attestation usage scenarios, Relying Party obligations, and integration with KYC/KYS workflows.
- Chapter 5 defines trust anchors and verification mechanisms for issuer authorization.
- Chapter 6 defines revocation mechanisms for the attestation.
- Chapter 7 provides compliance information regarding the EUBW framework, AML regulations, and applicable data protection laws.

### 1.3 Keywords

This document uses the capitalised keywords 'SHALL', 'SHOULD' and 'MAY' as
specified in [RFC 2119], i.e. to indicate requirements, recommendations and
options specified in this document.

In addition, 'must' (non-capitalised) is used to indicate an external
constraint, i.e. a requirement that is not mandated by this document, but, for
instance, by an external document. The word 'can' indicates a capability,
whereas other words, such as 'will', and 'is' or 'are' are intended as
statements of fact.

### 1.4 Terminology
This document uses the terminology specified in Annex 1 of the ARF.

**Additional terminology specific to this attestation:**

| **Term**                                          | **Definition**                                                                                                                                                                                         |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ownership List                                    | A comprehensive record of all natural and legal persons holding direct or indirect ownership or control in a legal entity, including ownership percentages and supporting evidence                     |
| Beneficial Owner / Ultimate Beneficial Owner (UBO) | A natural person who ultimately owns or controls a legal entity, either directly or indirectly (typically defined as holding ≥25% ownership or control, per AMLD requirements)                         |
| Direct Ownership                                  |Ownership interest held directly by a natural or legal person in the subject entity, without intermediary entities|
| Indirect Ownership                                | Ownership interest held through one or more intermediary legal entities (e.g., Person A owns 50% of Company B, which owns 60% of Company C → Person A has 30% indirect ownership in Company C)         |
| Total Ownership                                   | The sum of direct and indirect ownership percentages across all layers of the ownership structure                                                                                                      |
| Ownership Category                                | Classification of the type of ownership or control relationship (e.g., shareholder, controller via voting rights, trustee, partner, holder of convertible rights, person exercising dominant influence) |
| Legal Entity Identifier Chain                     | The list of all intermediate legal entities through which indirect ownership is held, enabling full traceability of ownership layers                                                                   |
| KYC                                               | Know Your Customer – due diligence process for verifying customer identity and assessing risk in financial relationships                                                                               |
| KYS                                               | Know Your Supplier – due diligence process for verifying supplier credentials, integrity, and risk exposure                                                                                            |
| PEP                                               | Politically Exposed Person – individual entrusted with prominent public functions, posing higher risk for corruption or bribery                                                                        |
| EUCC                                              | EU Company Certificate – attestation establishing the legal existence and identity of a legal entity within the EU                                                                                     |
| Evidence                                          | Supporting documentation substantiating the ownership structure calculation (e.g., shareholder register, organizational chart, trust deed)                                                             |

## 2 Attestation attributes and metadata

The Ownership List Attestation is designed to provide a complete, verifiable representation of an entity's ownership structure in a standardized digital format. This attestation supports transparency, compliance, and risk management by enabling automated verification of beneficial ownership across complex, multi-tiered corporate structures.

### 2.1 Introduction

Data Model:
````
Ownership List
├─ OwnerNaturalPerson   [1...n]   (at least one natural person owner required)
│   ├─ OwnerAddress     [1]       (one address per natural person owner)
│   └─ OwnerStake       [1]       (one stake record per natural person owner)
├─ OwnerLegalPerson     [0...m]   (zero or more legal entity owners)
│   ├─ OwnerAddress     [1]       (one address per legal entity owner)
│   └─ OwnerStake       [1]       (one stake record per legal entity owner)
└─ Evidence             [1...n]   (at least one piece of supporting evidence required)
````

*Explanation:*
- The Ownership List SHALL contain at least one ownership interest held by a natural person (to comply with beneficial ownership transparency requirements that mandate identification of ultimate natural person beneficiaries).
- The Ownership List MAY contain zero or more ownership interests held by legal persons (intermediate entities in the ownership chain).
- Each owner (natural or legal person) SHALL have exactly one associated OwnerStake record and one OwnerAddress record.
- The Ownership List SHALL include at least one piece of Evidence (e.g., organizational chart, shareholder register) substantiating the ownership calculation. Multiple pieces of evidence MAY be included for complex structures.
- Evidence MAY be provided as:URI reference (pointing to a publicly accessible or securely shared document)
- Embedded base64-encoded document (attached directly within the attestation)


| **Data Identifier**              | **Semantic Reference** | **Definition**                                                                  | **Data type** |
|----------------------------------|------------------------|---------------------------------------------------------------------------------|---------------|
| Owner Natural Person attributes  | ---                    | Identification and personal details of natural persons with ownership interests | Object                                                                                              |
| Owner Legal Person attributes    | ---                    |Identification and legal details of legal entities with ownership interests                             | Object                                                                          |
| Owner Stake attributes           | ---                    |Quantitative ownership data (direct, indirect, total percentages) and ownership category classification | Object                                                                          |
| Owner Address attributes         | ---                    |Contact and residence information for owners                                                            | Object                                                                          |
| Evidence attributes              | ---                    |References to supporting documentation substantiating the ownership structure                           | Object                                                                          |

**Attestation Classification:**

This attestation type is classified as
- **"EAA"** within the EUBW Wallet ecosystem, as it is typically self-issued by the legal entity subject to the ownership disclosure (i.e., the entity issues an attestation about its own ownership structure).

### 2.2 Mandatory attributes

**OwnerNaturalPerson Attributes**

| **Data Identifier**          | **Semantic Reference** | **Definition**                                                                       | **Data type**                       |
|------------------------------|------------------------|--------------------------------------------------------------------------------------|-------------------------------------|
| family_name                  | --                     |Last name(s) or surname(s) of the natural person who holds ownership or control        | String                                                                               | 
| given_name                   | --                     |First name(s), including middle name(s) where applicable, of the natural person        | String                                                                               |

**OwnerLegalPerson Attributes**

| **Data Identifier** | **Semantic Reference**                                                                                     | **Definition**                                                                                | **Data type** |
|---------------------|------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|---------------|
| legal_entity_name   | --| The complete official name of the legal entity which holds ownership interests in this entity | String                                              |
| legal_form          | --| The legal form of the owning legal entity (e.g., GmbH, AG, Ltd, SA, BV)                                    | String                                                                                        |
| identification      | --| The unique identifier of the legal entity which owns the subject entity (e.g., EUID, national tax ID, LEI) | String                                                                                        |

**OwnerStake Attributes**

| **Data Identifier**        | **Semantic Reference** | **Definition**                                                                                                                                                         | **Data type** |
|----------------------------|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| direct_ownership           | --                     | The percentage of direct ownership held by this owner in the subject entity                                                                                            | Decimal (0-100)                                                                                                                                                    |
| indirect_ownership         | --                     | The percentage of indirect ownership held by this owner through intermediate entities                                                                                  | Decimal                                                                     |
| total_ownership            | --                     | The complete percentage of ownership (direct + indirect across all layers)                                                                                             | Decimal                                                                     |
| legal_entity_identifiers   | --                     | The list of unique legal entity identifier(s) where this owner holds interests (includes direct legal entities and all indirect legal entities in the ownership chain) | Array of Strings                                                            |
| ownership_category         | --                     | Classification of the type of ownership or control relationship                                                                                                        | String (enumeration)                                                        | 

**Evidence Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                                                     | **Data type** |
|---------------------|------------------------|------------------------------------------------------------------------------------|---------------|
| evidence_id         | ---                    |URI reference to the evidence document (e.g., organizational chart, shareholder register) | String                                                                             |
| evidence_type       | ---                    |Defines the type of the object, which SHALL be "Evidence"                                 | String                                                                             |

#### 2.3 Optional attributes

**OwnerNaturalPerson Optional Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                                                                     | **Data type** |
|---------------------|------------------------|----------------------------------------------------------------------------------------------------|---------------|
| birth_date          | --                     | Day, month, and year of birth of the natural person ISO 8601                                       | Date (YYYY-MM-DD)                                           |
| nationality         | --                     | ISO 3166-1 alpha-2 country code representing the nationality of the natural person                 | String        |
| national_id_number  | --                     | National identification number (e.g., passport number, social security number, national ID number) | String                                                                             |

**OwnerLegalPerson Optional Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                                    | **Data type**          |
|---------------------|------------------------|-------------------------------------------------------------------|------------------------|
| lei                 | --                     | Legal Entity Identifier (LEI) per ISO 1744 | String (20 characters) | 
| registration_number | --                     | National company registration number                              | String                 |

**OwnerAddress Optional Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                                                        | **Data type** |
|---------------------|------------------------|---------------------------------------------------------------------------------------|---------------|
| address             | --                     | The street address where the owner currently resides or can be contacted              | String                                                                                                   |
| locality            | --                     | The city where the owner currently resides or can be contacted                        | String                                                                   |
| postal_code         | --                     | The postal or ZIP code of the owner's address                                         | String                                                                   |
| region              | --                     | The state, province, or region of the owner's address                                 | String                                                                   |                                            
| country             | --                     | ISO 3166-1 alpha-3 country code where the owner currently resides or can be contacted | String                                                                   | 

**Evidence Optional Attributes**

| **Data Identifier**   | **Semantic Reference** | **Definition**                                                                                                                                      | **Data type**   |
|-----------------------|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| evidence_data         | --                     |  The actual organizational structure document as a base64-encoded string (required if evidence_id does not contain a URI to an accessible location) | String (base64)                                                                                                            |
| evidence_confirmation | --                     |Boolean confirmation that the organizational structure document is current and has been used as the basis for the ownership calculation               | Boolean                                                                                                                                             |
| evidence_date         | --                     |The date when the evidence document was created or last updated ISO 8601                                                                              | Date                                                                                                                                                |

#### 2.4 Conditional attributes
No conditional attributes are defined for this attestation type. All attributes are either mandatory or optional as specified above.

#### 2.5 Mandatory metadata

| **Data Identifier**            | **Definition**                                                                                                                     | **Data type**                                                                             |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| issuance_date                  | The date and time when the attestation was issued ISO 8601                                                                         | DateTime                                                                                  |
| expiry_date                    | The date and time when the attestation expires ISO 8601                                                                            | DateTime                                                                                  |
| issuing_entity                 | The identifier of the legal entity that issued the attestation (typically the subject entity itself for self-issued attestations)  | String                                                                                    | 
| attestation_legal_category     | Indicates the legal category of this attestation ("EAA" )                                                                          | String                                                                                    |


### 2.6 Optional metadata

| **Data Identifier** | **Definition**                                                             | **Data type**                          |
|---------------------|----------------------------------------------------------------------------|----------------------------------------|
| trust_anchor_url    | URL where the trust anchor for verifying this attestation can be retrieved | URI|
| schema_version      | Version of the schema used                                                 |String |


#### 2.7 Conditional metadata
No conditional metadata elements are defined for this attestation type.

### 2.8 Value Lists

#### 2.8.1 Ownership Category Codes

The ownership_category attribute SHALL use one of the following standardized values:

| **Code**                                        | **Definition**      |
|-------------------------------------------------|---------------------------------------------------------------------|
| Direct shareholder                              |Natural or legal person holding shares directly in the subject entity|
| Indirect shareholder                            |Natural or legal person holding shares through one or more intermediate entities|
| Controller via voting or governance rights      |Natural or legal person exercising control through voting rights, board representation, or governance mechanisms, regardless of ownership percentage|
| Trustee / beneficiary in fiduciary arrangements |Natural or legal person acting as trustee or beneficiary in a trust, foundation, or similar fiduciary arrangement|
| Partner in partnership structures               |Natural or legal person holding a partnership interest in a partnership entity|
| Holder of convertible rights                    |Natural or legal person holding convertible instruments (e.g., convertible bonds, options, warrants) that may be converted into equity|
| Person exercising dominant influence            |Natural or legal person exercising dominant influence over the entity through contractual arrangements, operational control, or other means|

### 2.9 Integrity Rules

The following integrity rules SHALL be enforced:

- `family_name` SHALL be a non-empty string for all OwnerNaturalPerson entries.
- `given_name` SHALL be a non-empty string for all OwnerNaturalPerson entries.
- `legal_entity_name` SHALL be a non-empty string for all OwnerLegalPerson entries.
- `legal_form` SHALL be a non-empty string for all OwnerLegalPerson entries.
- `identification` SHALL be a non-empty string uniquely identifying the legal entity owner.
- `direct_ownership` SHALL be a decimal value between 0.00 and 100.00 (inclusive).
- `indirect_ownership` SHALL be a decimal value between 0.00 and 100.00 (inclusive).
- `total_ownership` SHALL be a decimal value between 0.00 and 100.00 (inclusive).
- `total_ownership` SHALL be equal to or greater than `direct_ownership`.
- `total_ownership` SHALL be equal to or greater than `indirect_ownership`.
- `legal_entity_identifiers` SHALL contain at least one non-empty string identifier.
- `ownership_category` SHALL use one of the enumerated values defined in Section 2.8.
- `evidence_id` SHALL be a non-empty URI string for all Evidence entries.
- `evidence_type` SHALL be the string `"Evidence"` for all Evidence entries.
- `birth_date`, if provided, SHALL be a valid ISO 8601 date (YYYY-MM-DD).
- `nationality`, if provided, SHALL be a valid ISO 3166-1 alpha-2 country code.
- `lei`, if provided, SHALL be a valid 20-character LEI code per ISO 17442.
- `evidence_date`, if provided, SHALL be a valid ISO 8601 date (YYYY-MM-DD).
- `evidence_confirmation`, if provided, SHALL be a boolean value.
- `country`, if provided, SHALL be a valid ISO 3166-1 alpha-3 country code.
- The Ownership List SHALL contain at least one OwnerNaturalPerson entry.
- Each attribute SHALL appear at most once within each object in the attestation.
- At least one Evidence entry SHALL be present in the attestation.

---

## 3 Attestation encoding

### 3.1 ISO/IEC 18013-5-compliant encoding

ISO/IEC 18013-5 (also called mdoc) is out of scope for this Rulebook, as offline proximity
presentation is not a current requirement for the Ownership List attestation.

### 3.2 SD-JWT VC-based encoding

The Ownership List attestation uses the SD-JWT VC format to allow for selective disclosure of
ownership structure attributes.

**Selective Disclosure:** Top-level claims (`OwnerNaturalPerson`, `OwnerLegalPerson`,
`Evidence`) SHALL be individually selectively disclosable, enabling a legal entity to disclose
only the attributes requested by a Relying Party.

The `.` notation is used to indicate the nesting of attributes.

**Verifiable Credential Type (`vct`):** `vct: eu.we-build.ownershiplist.1`

#### 3.2.1 Attribute Encoding Table

| **Data Identifier**                       | **Attribute identifier**                                  | **Encoding format**          | **Reference/Notes**                                                                                                                                     | **Disclosable** |
|-------------------------------------------|-----------------------------------------------------------|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| **OwnerNaturalPerson**                    |                                                           |                              |                                                                                                                                                         |                 |
| family_name                               | `owner_natural_person[n].family_name`                     | String                       | Last name(s) or surname(s) of the natural person who holds ownership interests                                                                          | MUST            |
| given_name                                | `owner_natural_person[n].given_name`                      | String                       | First name(s), including middle name(s) where applicable                                                                                                | MUST            |
| birth_date                                | `owner_natural_person[n].birth_date`                      | String (ISO 8601 YYYY-MM-DD) | Day, month, and year of birth of the natural person; optional                                                                                           | MUST            |
| nationality                               | `owner_natural_person[n].nationality`                     | String (ISO 3166-1 alpha-2)  | Nationality of the natural person; optional                                                                                                             | MUST            |
| national_id_number                        | `owner_natural_person[n].national_id_number`              | String                       | National identification number (e.g., passport number, social security number); optional                                                                | MUST            |
| **OwnerNaturalPerson – OwnerAddress**     |                                                           |                              |                                                                                                                                                         |                 |
| address                                   | `owner_natural_person[n].address.address`                 | String                       | Street address where the owner currently resides or can be contacted; optional                                                                          | MUST            |
| locality                                  | `owner_natural_person[n].address.locality`                | String                       | City where the owner currently resides or can be contacted; optional                                                                                    | MUST            |
| postal_code                               | `owner_natural_person[n].address.postal_code`             | String                       | Postal or ZIP code of the owner's address; optional                                                                                                     | MUST            |
| region                                    | `owner_natural_person[n].address.region`                  | String                       | State, province, or region of the owner's address; optional                                                                                             | MUST            |
| country                                   | `owner_natural_person[n].address.country`                 | String (ISO 3166-1 alpha-3)  | Country where the owner currently resides or can be contacted; optional                                                                                 | MUST            |
| **OwnerNaturalPerson – OwnerStake**       |                                                           |                              |                                                                                                                                                         |                 |
| direct_ownership                          | `owner_natural_person[n].stake.direct_ownership`          | Decimal (0–100)              | Percentage of direct ownership held by this owner in the subject entity                                                                                 | MUST            |
| indirect_ownership                        | `owner_natural_person[n].stake.indirect_ownership`        | Decimal (0–100)              | Percentage of indirect ownership held by this owner through intermediate entities                                                                       | MUST            |
| total_ownership                           | `owner_natural_person[n].stake.total_ownership`           | Decimal (0–100)              | Complete percentage of ownership (direct + indirect across all layers)                                                                                  | MUST            |
| legal_entity_identifiers                  | `owner_natural_person[n].stake.legal_entity_identifiers`  | Array of Strings             | List of unique legal entity identifiers where this owner holds interests (direct and indirect)                                                          | MUST            |
| ownership_category                        | `owner_natural_person[n].stake.ownership_category`        | String (enumeration)         | Classification of the type of ownership or control relationship                                                                                         | MUST            |
| **OwnerLegalPerson**                      |                                                           |                              |                                                                                                                                                         |                 |
| legal_entity_name                         | `owner_legal_person[m].legal_entity_name`                 | String                       | Complete official name of the legal entity which holds ownership interests                                                                              | MUST            |
| legal_form                                | `owner_legal_person[m].legal_form`                        | String                       | Legal form of the owning legal entity (e.g., GmbH, AG, Ltd, SA, BV)                                                                                     | MUST            |
| identification                            | `owner_legal_person[m].identification`                    | String                       | Unique identifier of the owning legal entity (e.g., EUID, national tax ID, LEI)                                                                         | MUST            |
| lei                                       | `owner_legal_person[m].lei`                               | String (20 characters)       | Legal Entity Identifier (LEI) per ISO 17442; optional                                                                                                   | MUST            |
| registration_number                       | `owner_legal_person[m].registration_number`               | String                       | National company registration number; optional                                                                                                          | MUST            |
| **OwnerLegalPerson – OwnerAddress**       |                                                           |                              |                                                                                                                                                         |                 |
| address                                   | `owner_legal_person[m].address.address`                   | String                       | Street address where the owning entity is registered or can be contacted; optional                                                                      | MUST            |
| locality                                  | `owner_legal_person[m].address.locality`                  | String                       | City where the owning entity is registered or can be contacted; optional                                                                                | MUST            |
| postal_code                               | `owner_legal_person[m].address.postal_code`               | String                       | Postal or ZIP code of the owning entity's address; optional                                                                                             | MUST            |
| region                                    | `owner_legal_person[m].address.region`                    | String                       | State, province, or region of the owning entity's address; optional                                                                                     | MUST            |
| country                                   | `owner_legal_person[m].address.country`                   | String (ISO 3166-1 alpha-3)  | Country where the owning entity is registered or can be contacted; optional                                                                             | MUST            |
| **OwnerLegalPerson – OwnerStake**         |                                                           |                              |                                                                                                                                                         |                 |
| direct_ownership                          | `owner_legal_person[m].stake.direct_ownership`            | Decimal (0–100)              | Percentage of direct ownership held by this legal entity owner in the subject entity                                                                    | MUST            |
| indirect_ownership                        | `owner_legal_person[m].stake.indirect_ownership`          | Decimal (0–100)              | Percentage of indirect ownership held by this legal entity owner through intermediate entities                                                          | MUST            |
| total_ownership                           | `owner_legal_person[m].stake.total_ownership`             | Decimal (0–100)              | Complete percentage of ownership (direct + indirect across all layers)                                                                                  | MUST            |
| legal_entity_identifiers                  | `owner_legal_person[m].stake.legal_entity_identifiers`    | Array of Strings             | List of unique legal entity identifiers where this owner holds interests                                                                                | MUST            |
| ownership_category                        | `owner_legal_person[m].stake.ownership_category`          | String (enumeration)         | Classification of the type of ownership or control relationship                                                                                         | MUST            |
| **Evidence**                              |                                                           |                              |                                                                                                                                                         |                 |
| evidence_id                               | `evidence[n].evidence_id`                                 | String (URI)                 | URI reference to the evidence document (e.g., organizational chart, shareholder register)                                                               | MUST            |
| evidence_type                             | `evidence[n].evidence_type`                               | String                       | Defines the type of the object, which SHALL be "Evidence"                                                                                               | MUST            |
| evidence_data                             | `evidence[n].evidence_data`                               | String (base64)              | Actual organizational structure document as a base64-encoded string; required if evidence_id does not contain a URI to an accessible location; optional | MUST            |
| evidence_confirmation                     | `evidence[n].evidence_confirmation`                       | Boolean                      | Confirmation that the organizational structure document is current and used as the basis for the ownership calculation; optional                        | MUST            |
| evidence_date                             | `evidence[n].evidence_date`                               | String (ISO 8601 YYYY-MM-DD) | Date when the evidence document was created or last updated; optional                                                                                   | MUST            |
| **Metadata**                              |                                                           |                              |                                                                                                                                                         |                 |
| issuance_date                             | `iat`                                                     | Number (Unix timestamp)      | The date and time when the attestation was issued (ISO 8601); RFC 7519 / Section 2.5                                                                    | MUST NOT        |
| expiry_date                               | `exp`                                                     | Number (Unix timestamp)      | The date and time when the attestation expires (ISO 8601); RFC 7519 / Section 2.5                                                                       | MUST NOT        |
| issuing_entity                            | `issuing_entity`                                          | String                       | Identifier of the legal entity that issued the attestation (subject entity for EAA)                                                                     | MUST NOT        |
| attestation_legal_category                | `attestation_legal_category`                              | String                       | One of `EAA` as defined by eIDAS 2                                                                                                                      | MUST NOT        |
| trust_anchor_url                          | `trust_anchor_url`                                        | String (URI)                 | URL where the trust anchor for verifying this attestation can be retrieved; optional                                                                    | MUST NOT        |
| schema_version                            | `schema_version`                                          | String                       | Version of the schema used; optional                                                                                                                    | MUST NOT        |

**Notes:**

- **MUST**: The claim SHALL be selectively disclosable — the holder MAY choose to disclose or
  withhold this claim when presenting the credential to a Relying Party.
- **MUST NOT**: The claim SHALL NOT be selectively disclosable — it is always present in plain
  text in the JWT header/payload and cannot be withheld by the holder, as it is required for
  credential verification and trust establishment.
- `OwnerNaturalPerson` entries are indexed as `[n]` where `n` starts at 0; at least one
  natural person owner SHALL be present.
- `OwnerLegalPerson` entries are indexed as `[m]` where `m` starts at 0; zero or more legal
  person owners MAY be present.
- `Evidence` entries are indexed as `[n]` where `n` starts at 0; at least one evidence entry
  SHALL be present.
- `iat`, `exp`, and `iss` follow RFC 7519 standard JWT claim naming conventions.

#### 3.2.2 Status Claim

For SD-JWT VC-compliant Ownership List attestations, the attestation MUST include a `status`
claim if the technical validity period is greater than 24 hours. This claim enables Relying
Parties to determine if a credential has been revoked via a status list mechanism, as specified
in SD-JWT VC.

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
 "status_list_credential": "https://issuer.example.com/status/ownershiplist/2025",
 "status_list_index": 456,
 "status_purpose": "revocation"
  }
}
```

3.2.3 Example Payload
The following is a non-normative example of an Ownership List SD-JWT VC payload:
```
{
  "vct": "eu.we-build.ownershiplist.1",
  "iss": "https://issuer.example.com",
  "iat": 1736935200,
  "exp": 1768471200,
  "issuing_entity": "did:example:legal-entity-123",
  "issuing_country": "DE",
  "attestation_legal_category": "EAA",
  "schema_version": "1.0",
  "trust_anchor_url": "https://trust.webuildconsortium.eu/anchors/eidas-tl",

  "owner_natural_person": [
 {
   "family_name": "Müller",
   "given_name": "Hans Peter",
   "birth_date": "1975-04-12",
   "nationality": "DE",
   "national_id_number": "L01X00T47",
   "address": {
     "address": "Hauptstraße 12",
     "locality": "Berlin",
     "postal_code": "10115",
     "region": "Berlin",
     "country": "DEU"
   },
   "stake": {
     "direct_ownership": 30.00,
     "indirect_ownership": 25.00,
     "total_ownership": 55.00,
     "legal_entity_identifiers": [
       "DE-HRB-123456",
       "DE-HRB-654321"
     ],
     "ownership_category": "Direct ownership"
   }
 }
  ],

  "owner_legal_person": [
 {
   "legal_entity_name": "Holding GmbH",
   "legal_form": "GmbH",
   "identification": "DE-HRB-654321",
   "lei": "52990079W74X20Y90210",
   "registration_number": "HRB 654321",
   "address": {
     "address": "Industrieweg 5",
     "locality": "Munich",
     "postal_code": "80331",
     "region": "Bavaria",
     "country": "DEU"
   },
   "stake": {
     "direct_ownership": 45.00,
     "indirect_ownership": 0.00,
     "total_ownership": 45.00,
     "legal_entity_identifiers": [
       "DE-HRB-123456"
     ],
     "ownership_category": "Direct ownership"
   }
 }
  ],

  "evidence": [
 {
   "evidence_id": "https://company-register.example.com/docs/shareholder-register-2024.pdf",
   "evidence_type": "Evidence",
   "evidence_confirmation": true,
   "evidence_date": "2024-12-01"
 }
  ],

  "status": {
 "type": "status-list",
 "status_list_credential": "https://issuer.example.com/status/ownershiplist/2025",
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
Sample payloads are provided under
../data-schemas/sd-jwt-vc/sample-data/ownershiplist-sd-jwt-sample.json


### 3.3 W3C Verifiable Credentials Data Model-based encoding

@TODO — To be discussed: which stakeholders will support this format and which use cases require it.

## 4 Attestation usage
### 4.1. Issuance process ###

### 4.2 Relying Party Obligations ###
When receiving and processing the attestation, a Relying Party SHALL:

### 4.2.1- 4.2.4 - Base verification process
A base verification for the attestation should be made.

#### 4.2.5 Validate Integrity Rules ####
This chapter will be completed in a future version of this Rulebook.

## 5 Trust anchors
This chapter will be completed in a future version of this Rulebook.

## 6 Revocation
This chapter will be completed in a future version of this Rulebook.

## 7 References
This chapter will be completed in a future version of this Rulebook.

## 8 References
| **Item Reference**                     | **Standard name/details**                                                                                                                                                                                                                                                                             |
|----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [European Digital Identity Regulation] | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework                              |
| [HAIP]	                                |Yasuda, K. et al, OpenID4VC High Assurance Interoperability Profile, OpenId Foundation, Version draft-03|
| [IANA-JWT-Claims]                      |	IANA JSON Web Token Claims Registry. Available: https://www.iana.org/assignments/jwt/jwt.xhtml|
| [ISO/IEC 18013-5]                      |	ISO/IEC 18013-5, Personal identification — ISO-compliant driving licence - Part 5: Mobile driving licence (mDL) application, First edition, 2021-09|
| [ISO 4217]	                            |ISO 4217 — Currency codes. Available: https://www.iso.org/iso-4217-currency-codes.html|
| [ISO 8601]	                            |ISO 8601 — Date and time format. Available: https://www.iso.org/iso-8601-date-and-time-format.html|
| [ISO 17442]                            |	ISO 17442 — Legal Entity Identifier (LEI). Available: https://www.iso.org/standard/78829.html|
| [OIDC]	                                |Sakimura, N. et al., "OpenID Connect Core 1.0", OpenID Foundation. Available: https://openid.net/specs/openid-connect-core-1_0.html|
| [RFC 2119]	                            |RFC 2119 — Key words for use in RFCs to Indicate Requirement Levels, S. Bradner, March 1997|
| [RFC 3339]	                            |RFC 3339 — Date and Time on the Internet: Timestamps, G. Klyne et al., July 2002|
| [RFC 7519]	                            |RFC 7519 — JSON Web Token (JWT), M. Jones et al., May 2015|
| [RFC 8610]	                            |RFC 8610 — Concise Data Definition Language (CDDL): A Notational Convention to Express Concise Binary Object Representation (CBOR) and JSON Data Structures, H. Birkholz et al., June 2019|
| [RFC 8943]	                            |RFC 8943 — Concise Binary Object Representation (CBOR) Tags for Date, M. Jones et al., November 2020|
| [RFC 8949]	                            |RFC 8949 — Concise Binary Object Representation (CBOR), C. Bormann et al., December 2020|
| [SD-JWT VC]	                           |SD-JWT-based Verifiable Credentials (SD-JWT VC). Available: https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/, version draft-ietf-oauth-sd-jwt-vc-09|
| [Topic 7]	                             |ARF Annex 2 - Topic 7 - Attestation revocation and revocation checking. Available: https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a237-topic-7-attestation-revocation-and-revocation-checking|

