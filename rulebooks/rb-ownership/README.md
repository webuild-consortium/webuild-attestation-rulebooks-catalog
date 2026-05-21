# Attestation Rulebook for attestations of type Ownership Attestation

* Author(s): 
    * [Florin Coptil, Robert Bosch GmbH] 

* Reviewer(s):
    * [Baumgardt Michaela, Commerzbank ]
    * [Stephan-A Fuchs, Deutsche Bank  ]

| Version | Date       | Description                                                     |
|---------|------------|-----------------------------------------------------------------|
| 0.1     | 23.03.2026 | Initial draft based on the WeBuild design attestations mettings |
| 0.2     | 10.05.2026 | Updates for addresses and identifiers                           |

* Contact:
  <a href="mailto:florin.coptil@bosch.com">Florin Coptil</a>
  
* Feedback:

## 1 Introduction

This attestation addresses the following question:

**Who are the Shareholders and Economic Interest Holders of this legal entity?**

A Shareholder or Economic Interest Holder is defined as any natural person or legal entity that directly or indirectly holds an ownership stake in a legal entity, based on:
- Ownership stake — direct or indirect share ownership, including equity interests, partnership shares, or equivalent economic interests
- Share class — type of shares held (ordinary, preferred, non-voting, etc.) and associated economic rights
- Ownership threshold — percentage of shares or economic interest held, regardless of whether control thresholds are met
as required under AMLR / AMLD6 and applicable company law.

### 1.1 Document scope and purpose
The Ownership Attestation records all natural and legal persons holding direct or indirect ownership in a legal entity, providing comprehensive transparency on beneficial ownership structures and economic interests. This attestation is a critical component of both Know Your Customer (KYC) and Know Your Supplier (KYS) processes within the EUDI Wallet ecosystem, supporting effective risk management, regulatory compliance, and anti-money laundering (AML) obligations.

### 1.2 Document structure
[This Rulebook is structured as follows:
- Chapter 2 describes the attestation attributes and metadata in an encoding-independent manner, including the data model.
- Chapter 3 specifies how the attestation attributes and metadata are encoded: Section 3.2 covers SD-JWT VC-based encoding.
- Chapter 4 specifies attestation usage scenarios, Relying Party obligations, and integration with KYC/KYS workflows.
- Chapter 5 defines trust anchors and verification mechanisms for issuer authorization.
- Chapter 6 defines revocation mechanisms for the attestation.
- Chapter 7 provides compliance information regarding the EUBW framework, AML regulations, corporate governance standards, and applicable data protection laws.
- Chapter 8 provides references to applicable standards and specifications.
](https://github.com/flo0x/wp3-technology-standards/blob/main/PA3/PA3_MVP_Plus.md#assumptions--relying-party-business-wallet)
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
| Ownership                                    | A comprehensive record of all natural and legal persons holding direct or indirect ownership or control in a legal entity, including ownership percentages and supporting evidence                     |
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

The Ownership Attestation is designed to provide a complete, verifiable representation of an entity's ownership structure in a standardized digital format. This attestation supports transparency, compliance, and risk management by enabling automated verification of beneficial ownership across complex, multi-tiered corporate structures.

### 2.1 Introduction

Data Model:
````
Ownership
├─ NaturalPerson   [1...n]   (at least one natural person owner required)
│   ├─ Identifier        [1]       (the identifier of the natural person )
│   ├─ ResidenceAddress  [1]       (residence address per natural person owner)
│   ├─ ContactAddress    [0]       (contact address per natural person owner)
│   └─ Stake             [1]       (one stake record per natural person owner)
├─ LegalPerson     [0...m]   (zero or more legal entity owners)
│   ├─ Identifier        [1]       (the identifier of the legal person )
│   ├─ RegisteredAddress [1]       (registered address per legal entity owner)
│   ├─ ContactAddress    [0]       (contact address per legal entity owner)
│   └─ Stake             [1]       (one stake record per legal entity owner)
└─ Evidence        [1...n]   (at least one piece of supporting evidence required)
````

*Explanation:*
- The `ownership` attestation SHALL contain at least one natural_person who exercises ownership (to comply with AML requirements that mandate identification of natural persons who ultimately ownership the entity).
- The `ownership` attestation MAY contain zero or more legal_person entries, representing intermediate legal entities in the ownership chain.
- For each `natural_person` ownershipler:
  - It SHALL include a family_name and given_name.
  - It MAY include birth_date, nationality.
  - It MAY include an identifier object containing issuing_country and document_number.
  - It SHALL include a mandatory residence_address.
  - It MAY include an optional contact_address.
  - It SHALL include exactly one stake record detailing the ownership interest.
- For each legal_person ownershipler:
  - It SHALL include legal_entity_name, legal_form.
  - It SHALL include a mandatory legal_person_identifier object (with at least one of EUID, LEI, TAX specified).
  - It MAY include lei (as a specific field) and registration_number.
  - It SHALL include a mandatory registered_address.
  - It MAY include an optional contact_address.
  - It SHALL include exactly one stake record detailing the ownership interest.
- The `ownership` attestation SHALL include at least one piece of evidence (e.g., governance chart, shareholder agreement, articles of association) substantiating the ownership calculation. Multiple pieces of evidence MAY be included for complex structures.
  evidence MAY be provided as a URI reference (pointing to a publicly accessible or securely shared document) or as an embedded base64-encoded document (attached directly within the attestation).

| **Data Identifier**           | **Semantic Reference** | **Definition**                                                                                          | **Data type** |
|-------------------------------|------------------------|---------------------------------------------------------------------------------------------------------|---------------|
| Natural Person attributes     | ---                    | Identification and personal details of natural persons with ownership interests                         | Object                                                                                              |
| Legal Person attributes       | ---                    | Identification and legal details of legal entities with ownership interests                             | Object                                                                          |
| Stake attributes              | ---                    | Quantitative ownership data (direct, indirect, total percentages) and ownership category classification | Object                                                                          |
| Residence Address attributes  | ---                    | Residence address for natural person                                                                    | Object                                                                          |
| Registered Address attributes | ---                    | Registered address for legal person                                                                     | Object                                                                          |
| Contact Address attributes    | ---                    | Contact address for owners (natural or legal persons)                                                   | Object                                                                          |
| Evidence attributes           | ---                    | References to supporting documentation substantiating the ownership structure                           | Object                                                                          |

**Attestation Classification:**

This attestation type is classified as
- **"EAA"** within the EUBW Wallet ecosystem, as it is typically self-issued by the legal entity subject to the ownership disclosure (i.e., the entity issues an attestation about its own ownership structure).

### 2.2 Mandatory attributes

**NaturalPerson Attributes**

| **Data Identifier**  | **Semantic Reference** | **Definition**                                                                       | **Data type**   |
|----------------------|------------------------|--------------------------------------------------------------------------------------|-----------------|
| family_name          | --                     |Last name(s) or surname(s) of the natural person who holds ownership or control        | String          | 
| given_name           | --                     |First name(s), including middle name(s) where applicable, of the natural person        | String          |

**LegalPerson Attributes**

| **Data Identifier** | **Semantic Reference**                                                                                     | **Definition**                                                                                | **Data type** |
|---------------------|------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|---------------|
| legal_person_name   | --| The complete official name of the legal entity which holds ownership interests in this entity | String                                              |
| legal_form_type     | --| The legal form of the owning legal entity (e.g., GmbH, AG, Ltd, SA, BV)                                    | String                                                                                        |

**Stake Attributes**

| **Data Identifier**        | **Semantic Reference** | **Definition**                                                                                                                                                        | **Data type** |
|----------------------------|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| direct_ownership           | --                     | The percentage of direct ownership held by this owner in the subject entity                                                                                           | Decimal (0-100)                                                                                                                                                    |
| indirect_ownership         | --                     | The percentage of indirect ownership held by this owner through intermediate entities                                                                                 | Decimal                                                                     |
| total_ownership            | --                     | The complete percentage of ownership (direct + indirect across all layers)                                                                                            | Decimal                                                                     |
| legal_entity_identifiers   | --                     | The list legal entity identifier(s) where this owner holds interests (includes direct legal entities and all indirect legal entities in the ownership chain) | Array of Strings                                                            |
| ownership_category         | --                     | Classification of the type of ownership or control relationship                                                                                                       | String (enumeration)                                                        | 

**Evidence Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                                                     | **Data type** |
|---------------------|------------------------|------------------------------------------------------------------------------------|---------------|
| evidence_id         | ---                    |URI reference to the evidence document (e.g., organizational chart, shareholder register) | String                                                                             |
| evidence_type       | ---                    |Defines the type of the object, which SHALL be "Evidence"                                 | String                                                                             |

#### 2.3 Optional attributes

**NaturalPerson Optional Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                                                                     | **Data type** |
|---------------------|------------------------|----------------------------------------------------------------------------------------------------|---------------|
| birth_date          | --                     | Day, month, and year of birth of the natural person ISO 8601                                       | Date (YYYY-MM-DD)                                           |


**NaturalPersonIdentifier Optional Attributes**

| **Data Identifier**   | **Semantic Reference** | **Definition**                                                                                                                                        | **Data type**                                                    |
|-----------------------|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| document_type         | ...                    | A value defining the type of the identity document according to the nationality of the UBO (e.g., Passport, National identity card, Driver's license) | String                                                           |
| document_number       | ...                    | The number of the identity document (passport number, national ID number, driver's license number, etc.)                                              | String                                                           |
| issuing_country       | ...                    | The country that issued the identity document (ISO 3166-1 alpha-3 code)                                                                               | String                                                           |

**LegalPersonIdentifier Optional Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                             | **Data type** |
|---------------------|------------------------|--------------------------------------------|---------------|
| euid                | --                     | EUID per ISO 3166-1 alpha-2                | String        |
| lei                 | --                     | Legal Entity Identifier (LEI) per ISO 1744 | String        | 
| tax                 | --                     | National company registration number       | String        |

**ResidenceAddress Optional Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                                                        | **Data type** |
|---------------------|------------------------|---------------------------------------------------------------------------------------|---------------|
| address             | --                     | The street address where the owner currently resides             | String                                                                                                   |
| locality            | --                     | The city where the owner currently resides d                        | String                                                                   |
| postal_code         | --                     | The postal or ZIP code of the owner's address                                         | String                                                                   |
| region              | --                     | The state, province, or region of the owner's address                                 | String                                                                   |                                            
| country             | --                     | ISO 3166-1 alpha-3 country code where the owner currently resides  | String                                                                   | 

**RegisteredAddress Optional Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                                                      | **Data type** |
|---------------------|------------------------|-------------------------------------------------------------------------------------|---------------|
| address             | --                     | The street address where the legal owner currently is registered                    | String                                                                                                   |
| locality            | --                     | The city where the  legal owner currently is registered                             | String                                                                   |
| postal_code         | --                     | The postal or ZIP code of the legal owner's address                                 | String                                                                   |
| region              | --                     | The state, province, or region of the lega owner's address                          | String                                                                   |                                            
| country             | --                     | ISO 3166-1 alpha-3 country code where the legal owner currently is registered | String                                                                   | 

**ContactAddress Optional Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                                   | **Data type** |
|---------------------|------------------------|------------------------------------------------------------------|---------------|
| address             | --                     | The street address where the owner  can be contacted             | String                                                                                                   |
| locality            | --                     | The city where the owner  can be contacted                       | String                                                                   |
| postal_code         | --                     | The postal or ZIP code of the owner's address                    | String                                                                   |
| region              | --                     | The state, province, or region of the owner's address            | String                                                                   |                                            
| country             | --                     | ISO 3166-1 alpha-3 country code where the owner can be contacted | String                                                                   |

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
TODO Florin
The following integrity rules SHALL be enforced:

## 3 Attestation encoding

### 3.1 ISO/IEC 18013-5-compliant encoding

ISO/IEC 18013-5 (also called mdoc) is out of scope for this Rulebook, as offline proximity
presentation is not a current requirement for the Ownership attestation.

### 3.2 SD-JWT VC-based encoding

The Ownership attestation uses the SD-JWT VC format to allow for selective disclosure of
ownership structure attributes.

**Selective Disclosure:** Top-level claims (`OwnerNaturalPerson`, `OwnerLegalPerson`,
`Evidence`) SHALL be individually selectively disclosable, enabling a legal entity to disclose
only the attributes requested by a Relying Party.

The `.` notation is used to indicate the nesting of attributes.

**Verifiable Credential Type (`vct`):** `vct: eu.we-build.ownership.1`

#### 3.2.1 Attribute Encoding Table

| **Data Identifier**         | **Attribute identifier**                                                          | **Encoding format**          | **Reference/Notes**                                                                                                                                     | **Disclosable** |
|-----------------------------|-----------------------------------------------------------------------------------|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| ownership                   | `ownership`                                                                       | Array [Ownership]            | Array of ownership objects; **SHALL** contain at least one ownership                                                                                    | MUST            |
| **NaturalPerson**           |                                                                                   |                              |                                                                                                                                                         |                 |
| family_name                 | `ownership[n].natural_person.family_name`                                         | String                       | Last name(s) or surname(s) of the natural person who holds ownership interests                                                                          | MUST            |
| given_name                  | `ownership[n].natural_person.person.given_name`                                   | String                       | First name(s), including middle name(s) where applicable                                                                                                | MUST            |
| birth_date                  | `ownership[n].natural_person.person.birth_date`                                   | String (ISO 8601 YYYY-MM-DD) | Day, month, and year of birth of the natural person; optional                                                                                           | MUST            |
| **NaturalPersonIdentifier** |                                                                                   | Optional identification details for the natural person.                             |                                                                                                                                                         |                  |
| document_type               | `ownership[n].natural_person.identifier.document_type`                            | String                       | A value defining the type of the identity document according to the nationality of the UBO (e.g., Passport, National identity card, Driver's license)   | MUST             |
| document_number             | `ownership[n].natural_person.identifier.document_number`                          | String                       | The number of the identity document (passport number, national ID number, driver's license number, etc.)                                                | MUST             |
| issuing_country             | `ownership[n].natural_person.identifier.issuing_country`                        / | String (ISO 3166-1 alpha-3)  | The country that issued the identity document                                                                                                           | MUST             |
| **ResidenceAddress**        |                                                                                   |                              |                                                                                                                                                         |                 |
| address                     | `ownership[n].natural_person.residence_address.address`                           | String                       | Street address where the owner currently resides ; optional                                                                                             | MUST            |
| locality                    | `ownership[n].natural_person.residence_address.locality`                          | String                       | City where the owner currently resides optional                                                                                                         | MUST            |
| state                       | `ownership[n].natural_person.residence_address.state`                             | String                       | State, province, or region of the owner's address; optional                                                                                             | MUST            |
| postal_code                 | `ownership[n].natural_person.residence_address.postal_code`                       | String                       | Postal or ZIP code of the owner's address; optional                                                                                                     | MUST            |
| country                     | `ownership[n].natural_person.residence_address.country`                           | String (ISO 3166-1 alpha-3)  | Country where the owner currently resides ; optional                                                                                                    | MUST            |
| **ContactAddress**          |                                                                                   |                              |                                                                                                                                                         |                 |
| address                     | `ownership[n].natural_person.contact_address.address`                             | String                       | Street address where the owner can be contacted; optional                                                                                               | MUST            |
| locality                    | `ownership[n].natural_person.contact_address.locality`                            | String                       | City where the owner can be contacted; optional                                                                                                         | MUST            |
| state                       | `ownership[n].natural_person.contact_address.state`                               | String                       | State, province, or region of the owner's address; optional                                                                                             | MUST            |
| postal_code                 | `ownership[n].natural_person.contact_address.postal_code`                         | String                       | Postal or ZIP code of the owner's address; optional                                                                                                     | MUST            |
| country                     | `ownership[n].natural_person.contact_address.country`                             | String (ISO 3166-1 alpha-3)  | Country where the owner can be contacted; optional                                                                                                      | MUST            |
| **Stake**                   |                                                                                   |                              |                                                                                                                                                         |                 |
| direct_ownership            | `ownership[n].natural_person.stake.direct_ownership`                              | Decimal (0–100)              | Percentage of direct ownership held by this owner in the subject entity                                                                                 | MUST            |
| indirect_ownership          | `ownership[n].natural_person.stake.indirect_ownership`                            | Decimal (0–100)              | Percentage of indirect ownership held by this owner through intermediate entities                                                                       | MUST            |
| total_ownership             | `ownership[n].natural_person.stake.total_ownership`                               | Decimal (0–100)              | Complete percentage of ownership (direct + indirect across all layers)                                                                                  | MUST            |
| legal_entity_identifiers    | `ownership[n].natural_person.stake.legal_person_id`                               | Array of Strings             | List of legal entity identifiers where this owner holds interests (direct and indirect)  (EUID, LEI, DUNS)                                              | MUST            |
| ownership_category          | `ownership[n].natural_person.stake.ownership_category`                            | String (enumeration)         | Classification of the type of ownership or control relationship                                                                                         | MUST            |
| **LegalPerson**             |                                                                                   |                              |                                                                                                                                                         |                 |
| legal_entity_name           | `ownership[n].legal_person.legal_entity_name`                                     | String                       | Complete official name of the legal entity which holds ownership interests                                                                              | MUST            |
| legal_form_type             | `ownership[n].legal_person.legal_form_type`                                       | String                       | Legal form of the owning legal entity (e.g., GmbH, AG, Ltd, SA, BV)                                                                                     | MUST            |
| **LegalPersonIdentifier**   |                                                                                   |                              |                                                                                                                                                         |                  |
| euid                        | `ownership[n].legal_person.identifier.euid`                                       | String                       | Complete official name of the legal entity which exercises control                                                                                      | MUST             |
| lei                         | `ownership[n].legal_person.identifier.lei`                                        | String (20 characters)       | LEI code of the controlling legal entity; optional                                                                                                      | MUST             |
| tax                         | `ownership[n].legal_person.identifier.tax`                                        | String                       | National company registration number; optional                                                                                                          | MUST             |
| **RegisteredAddress**       |                                                                                   |                              |                                                                                                                                                         |                 |
| address                     | `ownership[n].legal_person.registered_address.address`                            | String                       | Street address where the owning entity is registered ; optional                                                                                         | MUST            |
| locality                    | `ownership[n].legal_person.registered_address.locality`                           | String                       | City where the owning entity is registered ; optional                                                                                                   | MUST            |
| postal_code                 | `ownership[n].legal_person.registered_address.postal_code`                        | String                       | Postal or ZIP code of the owning entity's address; optional                                                                                             | MUST            |
| region                      | `ownership[n].legal_person.registered_address.region`                             | String                       | State, province, or region of the owning entity's address; optional                                                                                     | MUST            |
| country                     | `ownership[n].legal_person.registered_address.country`                            | String (ISO 3166-1 alpha-3)  | Country where the owning entity is registered ; optional                                                                                                | MUST            |
| **ContactAddress**          |                                                                                   |                              |                                                                                                                                                         |                 |
| address                     | `ownership[n].legal_person.contact_address.address`                               | String                       | Street address where the owning entity can be contacted; optional                                                                                       | MUST            |
| locality                    | `ownership[n].legal_person.contact_address.locality`                              | String                       | City where the owning entity can be contacted; optional                                                                                                 | MUST            |
| postal_code                 | `ownership[n].legal_person.contact_address.postal_code`                           | String                       | Postal or ZIP code of the owning entity's address; optional                                                                                             | MUST            |
| region                      | `ownership[n].legal_person.contact_address.region`                                | String                       | State, province, or region of the owning entity's address; optional                                                                                     | MUST            |
| country                     | `ownership[n].legal_person.contact_address.country`                               | String (ISO 3166-1 alpha-3)  | Country where the owning entity can be contacted; optional                                                                                              | MUST            |
| **Stake**                   |                                                                                   |                              |                                                                                                                                                         |                 |
| direct_ownership            | `ownership[n].legal_person.stake.direct_ownership`                                | Decimal (0–100)              | Percentage of direct ownership held by this legal entity owner in the subject entity                                                                    | MUST            |
| indirect_ownership          | `ownership[n].legal_person.stake.indirect_ownership`                              | Decimal (0–100)              | Percentage of indirect ownership held by this legal entity owner through intermediate entities                                                          | MUST            |
| total_ownership             | `ownership[n].legal_person.stake.total_ownership`                                 | Decimal (0–100)              | Complete percentage of ownership (direct + indirect across all layers)                                                                                  | MUST            |
| legal_person_id             | `ownership[n].legal_person.stake.legal_person_id`                                 | Array of Strings             | List of legal entity identifiers where this owner holds interests                                                                                       | MUST            |
| ownership_category          | `ownership[n].legal_person.stake.ownership_category`                              | String (enumeration)         | Classification of the type of ownership or control relationship                                                                                         | MUST            |
| **Evidence**                |                                                                                   |                              |                                                                                                                                                         |                 |
| evidence_id                 | `evidence[n].evidence_id`                                                         | String (URI)                 | URI reference to the evidence document (e.g., organizational chart, shareholder register)                                                               | MUST            |
| evidence_type               | `evidence[n].evidence_type`                                                       | String                       | Defines the type of the object, which SHALL be "Evidence"                                                                                               | MUST            |
| evidence_data               | `evidence[n].evidence_data`                                                       | String (base64)              | Actual organizational structure document as a base64-encoded string; required if evidence_id does not contain a URI to an accessible location; optional | MUST            |
| evidence_confirmation       | `evidence[n].evidence_confirmation`                                               | Boolean                      | Confirmation that the organizational structure document is current and used as the basis for the ownership calculation; optional                        | MUST            |
| evidence_date               | `evidence[n].evidence_date`                                                       | String (ISO 8601 YYYY-MM-DD) | Date when the evidence document was created or last updated; optional                                                                                   | MUST            |
| **Metadata**                |                                                                                   |                              |                                                                                                                                                         |                 |
| issuance_date               | `iat`                                                                             | Number (Unix timestamp)      | The date and time when the attestation was issued (ISO 8601); RFC 7519 / Section 2.5                                                                    | MUST NOT        |
| expiry_date                 | `exp`                                                                             | Number (Unix timestamp)      | The date and time when the attestation expires (ISO 8601); RFC 7519 / Section 2.5                                                                       | MUST NOT        |
| issuing_entity              | `issuing_entity`                                                                  | String                       | Identifier of the legal entity that issued the attestation (subject entity for EAA)                                                                     | MUST NOT        |
| attestation_legal_category  | `attestation_legal_category`                                                      | String                       | One of `EAA` as defined by eIDAS 2                                                                                                                      | MUST NOT        |
| trust_anchor_url            | `trust_anchor_url`                                                                | String (URI)                 | URL where the trust anchor for verifying this attestation can be retrieved; optional                                                                    | MUST NOT        |
| schema_version              | `schema_version`                                                                  | String                       | Version of the schema used; optional                                                                                                                    | MUST NOT        |

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

For SD-JWT VC-compliant Ownership attestations, the attestation MUST include a `status`
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
 "status_list_credential": "https://issuer.example.com/status/ownership/2025",
 "status_list_index": 456,
 "status_purpose": "revocation"
  }
}
```

### 3.2.3 Example Payload

The following is a non-normative example of a CompanyInfo SD-JWT VC payload:
```
{
  "vct": "eu.we-build.ownership.1",
  "attestation_legal_category": "EAA",
  "issuing_entity": "did:example:legal-entity-123",
  "ownership": [
    {
      "natural_person": {
        "family_name": "Doe",
        "given_name": "John",
        "birth_date": "1980-01-15",
        "natural_person_identifier": {
          "document_type": "Passport",
          "document_number": "P12345678",
          "issuing_country": "USA"
        },
        "residence_address": {
          "address": "123 Main St",
          "locality": "Anytown",
          "postal_code": "12345",
          "region": "CA",
          "country": "USA"
        },
        "contact_address": {
          "address": "456 Oak Ave",
          "locality": "Otherville",
          "postal_code": "67890",
          "region": "NY",
          "country": "USA"
        },
        "stake": {
          "direct_ownership": 25.00,
          "indirect_ownership": 10.00,
          "total_ownership": 35.00,
          "legal_person_id": ["DE12.HRB1212","12345678901234567890"],
          "ownership_category": "Direct shareholder"
        }
      }
    },
    {
      "legal_person": {
        "legal_person_name": "Acme Holdings Inc.",
        "legal_form_type": "Corporation",
        "legal_person_identifier": {
          "lei": "98765432109876543210"
        },
        "registered_address": {
          "address": "789 Corporate Blvd",
          "locality": "Biztown",
          "postal_code": "54321",
          "region": "DE",
          "country": "DEU"
        },
        "contact_address": {
          "address": "101 Business Pkwy",
          "locality": "Metropolis",
          "postal_code": "00000",
          "region": "DE",
          "country": "DEU"
        },
        "stake": {
          "direct_ownership": 50.00,
          "indirect_ownership": 0.00,
          "total_ownership": 50.00,
          "legal_person_id": ["EUID:XYZ-456"],
          "ownership_category": "Direct shareholder"
        }
      }
    }
  ],
  "evidence": [
    {
      "evidence_id": "https://example.com/org-chart-2023.pdf",
      "evidence_type": "Evidence",
      "evidence_confirmation": true,
      "evidence_date": "2023-10-26"
    },
    {
      "evidence_id": "urn:webuild:shareholder-register-2023",
      "evidence_type": "Evidence",
      "evidence_data": "JVBERi0xLjQKJdDUxdgKOSAyIG9iago8PC9GaWx0ZXIs..."
    }
  ],
  "status": {
    "type": "status-list",
    "status_list_credential": "https://example.com/status/1",
    "status_list_index": 123,
    "status_purpose": "revocation"
  },
  "trust_anchor_url": "https://webuildconsortium.eu/trust-anchor.json",
  "schema_version": "0.1.0",
  "cnf": {
    "jwk": {
      "kty": "EC",
      "crv": "P-256",
      "x": "f83_oX1f8m5y_B7D9S9-C_0R5-Q0_u_X8P_S0_0F8_C",
      "y": "e6_z_C8D_D9S9-C_0R5-Q0_u_X8P_S0_0F8_C"
    }
  }
}
```
Sample payloads are provided under
../data-schemas/sd-jwt/sample-data/ownership-sd-jwt-sample.json

### 3.3 W3C Verifiable Credentials Data Model-based encoding

@TODO — To be discussed: which stakeholders will support this format and which use cases require it.

## 4 Attestation usage
### 4.1. Issuance process ###

### 4.2 Relying Party Obligations
When receiving and processing an attestation, the Relying Party SHALL perform the following verification obligations.
### 4.2.1 – 4.2.8 Base Verification Process
The Relying Party SHALL perform the base attestation verification process as defined in the Base Verification specification:
https://github.com/flo0x/webuild-attestations/blob/main/rulebooks/rb-base/verifier-base-verification.md#42-relying-party-obligations
### 4.2.9 Validate Integrity Rules
Validation of integrity and policy rules will be specified in a future version of this Rulebook.

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

