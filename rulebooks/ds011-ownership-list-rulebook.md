* Template version: 1.1, 20-08-2025

# Attestation Rulebook for attestations of type Ownership List Attestation

*Provide information about the author(s) of this Rulebook in the following form:*

* Author(s): 
    * [Florin Coptil, Robert Bosch GmbH]
* Previous Authors

* Reviewer(s):
    * [......, Deutsche Bank]

*Provide versioning information about the Rulebook in the following form:*

| Version | Date       | Description                                                     |
|---------|------------|-----------------------------------------------------------------|
| 0.1     | 13.03.2026 | Initial draft based on the WeBuild design attestations mettings |

*Provide a contact email address and/or a link to an issue tracking system that can be used for
providing feedback, e.g.:*

Contact: florin.coptil@bosch.com

**Feedback:**
  *  https://example.com/tracker 

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

Data Model
```json
Ownership List
├─ OwnerNaturalPerson   [1...n]   (at least one natural person owner required)
│   ├─ OwnerAddress     [1]       (one address per natural person owner)
│   └─ OwnerStake       [1]       (one stake record per natural person owner)
├─ OwnerLegalPerson     [0...m]   (zero or more legal entity owners)
│   ├─ OwnerAddress     [1]       (one address per legal entity owner)
│   └─ OwnerStake       [1]       (one stake record per legal entity owner)
└─ Evidence             [1...n]   (at least one piece of supporting evidence required)
```

*Explanation:*
- The Ownership List SHALL contain at least one ownership interest held by a natural person (to comply with beneficial ownership transparency requirements that mandate identification of ultimate natural person beneficiaries).
- The Ownership List MAY contain zero or more ownership interests held by legal persons (intermediate entities in the ownership chain).
- Each owner (natural or legal person) SHALL have exactly one associated OwnerStake record and one OwnerAddress record.
- The Ownership List SHALL include at least one piece of Evidence (e.g., organizational chart, shareholder register) substantiating the ownership calculation. Multiple pieces of evidence MAY be included for complex structures.
- Evidence MAY be provided as:URI reference (pointing to a publicly accessible or securely shared document)
- Embedded base64-encoded document (attached directly within the attestation)

This attestation type is classified as a "EAA" within the EUBW Wallet ecosystem, as it is typically self-issued by the legal entity subject to the ownership disclosure (i.e., the entity issues an attestation about its own ownership structure). 

| **Data Identifier**              | **Definition**                                                       | **Data type** |
|----------------------------------|----------------------------------------------------------------------|---------------|
| Owner Natural Person attributes  | Identification and personal details of natural persons with ownership interests|Object |
| Owner Legal Person attributes    | Identification and legal details of legal entities with ownership interests|Object |
| Owner Stake attributes           | Quantitative ownership data (direct, indirect, total percentages) and ownership category classification| Object |
| Owner Address attributes         |Contact and residence information for owners |Object |
| Evidence attributes              | References to supporting documentation substantiating the ownership structure | Object |

### 2.2 Mandatory attributes
@TODO Florin still to confirmed with Barth the type (after matching in vocabulary document)

**OwnerNaturalPerson Attributes**

| **Data Identifier**          | **Definition**                                                                         | **Data type**                       |
|------------------------------|----------------------------------------------------------------------------------------|-------------------------------------|
| family_name                  | Last name(s) or surname(s) of the natural person who holds ownership or control        | String | 
| given_name                   | First name(s), including middle name(s) where applicable, of the natural person        | String |
| attestation_legal_category   | Indicates the legal category of this attestation (non-qualified-EAA, PuB-EAA, or QEAA) | String| 

**OwnerLegalPerson Attributes**

| **Data Identifier** | **Definition**      | **Data type** |
|---------------------|------------------------------------------------------------------------------|---------------|
| legal_entity_name   |The complete official name of the legal entity which holds ownership interests in this entity |String|
| legal_form          |The legal form of the owning legal entity (e.g., GmbH, AG, Ltd, SA, BV) | String        |
| identification      |The unique identifier of the legal entity which owns the subject entity (e.g., EUID, national tax ID, LEI) | String        |

**OwnerStake Attributes**

| **Data Identifier**        | **Definition**      | **Data type** |
|----------------------------|------------------------------------------------------------------------------|---------------|
| direct_ownership           |The percentage of direct ownership held by this owner in the subject entity| Decimal (0-100)|
| indirect_ownership         |The percentage of indirect ownership held by this owner through intermediate entities |Decimal|
| total_ownership            |The complete percentage of ownership (direct + indirect across all layers)| Decimal |
| legal_entity_identifiers   |The list of unique legal entity identifier(s) where this owner holds interests (includes direct legal entities and all indirect legal entities in the ownership chain) |Array of Strings|
| ownership_category         |Classification of the type of ownership or control relationship| String (enumeration)| 

**Evidence Attributes**

| **Data Identifier** | **Definition**      | **Data type** |
|---------------------|------------------------------------------------------------------------------|---------------|
| evidence_id         |URI reference to the evidence document (e.g., organizational chart, shareholder register) |String |
| evidence_type       |Defines the type of the object, which SHALL be "Evidence"| String|

#### 2.3 Optional attributes

**OwnerNaturalPerson Optional Attributes**

| **Data Identifier** | **Definition**      | **Data type** |
|---------------------|------------------------------------------------------------------------------|---------------|
| birth_date          |Day, month, and year of birth of the natural person ISO 8601 |Date (YYYY-MM-DD)|
@TODO FLORIN 
| nationality         |ISO 3166-1 alpha-2 country code representing the nationality of the natural person | String        |
| national_id_number  |National identification number (e.g., passport number, social security number, national ID number) | String        |

**OwnerLegalPerson Optional Attributes**

| **Data Identifier**                             | **Definition**                       | **Data type** |
|-------------------------------------------------|--------------------------------------|---------------|
| lei Legal Entity Identifier (LEI) per ISO 17442 | String (20 characters)               | 
| registration_number                             | National company registration number | String                 |

**OwnerAddress Optional Attributes**

| **Data Identifier** | **Definition**                                                                                                 | **Data type** |
|---------------------|----------------------------------------------------------------------------------------------------------------|---------------|
| address             | The street address where the owner currently resides or can be contacted                                       | String        |
| locality            | The city where the owner currently resides or can be contacted                                                 | String        |
| postal_code         | The postal or ZIP code of the owner's address | String        |
| region              | The state, province, or region of the owner's address |String|                                            
| country             | ISO 3166-1 alpha-3 country code where the owner currently resides or can be contacted |String| 

**Evidence Optional Attributes**

| **Data Identifier**   | **Definition**                                                                                                 | **Data type**   |
|-----------------------|----------------------------------------------------------------------------------------------------------------|-----------------|
| evidence_data         |The actual organizational structure document as a base64-encoded string (required if evidence_id does not contain a URI to an accessible location) | String (base64) |
| evidence_confirmation |Boolean confirmation that the organizational structure document is current and has been used as the basis for the ownership calculation | Boolean         |
| evidence_date         |The date when the evidence document was created or last updated ISO 8601 | Date            |

#### 2.4 Conditional attributes
No conditional attributes are defined for this attestation type. All attributes are either mandatory or optional as specified above.

#### 2.5 Mandatory metadata

| **Data Identifier**                                                                                                                                                               | **Definition**      | **Data type**                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|----------------------------------------|
| issuance_date The date and time when the attestation was issued ISO 8601                                                                                                          |DateTime|
| expiry_date The date and time when the attestation expires ISO 8601                                                                                                               |DateTime|
| issuing_entity The identifier of the legal entity that issued the attestation (typically the subject entity itself for self-issued attestations, or the QTSP identifier for QEAA) | String|

#### 2.6 Optional metadata

| **Data Identifier**                 | **Definition**                                                          | **Data type**                          |
|-------------------------------------|-------------------------------------------------------------------------|----------------------------------------|
| trust_anchor_url                    | URL where the trust anchor for verifying this attestation can be retrieved | URI|
| schema_version                      | Version of the Owner List schema used                                   |String |

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

## 3 Attestation encoding

### 3.1 ISO/IEC 18013-5-compliant encoding

Ownership List Attestations are not intended for offline, proximity-based presentation scenarios due to the complexity and data volume of ownership structures, the need for dynamic verification against sanctions/PEP databases, and the requirement for real-time revocation checks.
Therefore, ISO/IEC 18013-5 mdoc encoding is out of scope for this attestation type.

### 3.2 SD-JWT VC-based encoding

The following table maps the data identifiers defined in Chapter 2 to SD-JWT VC claim names:
@TODO Florin&Bart - when the semantic is ready

The . notation is used to indicate the nesting of attributes.

@TOOD Florin&Mike - if is possible to referer some how the main class here over URI ?
**Verifiable Credential Type (`vct`):** `urn:eubw:ownershiplist:1`

## 4 Attestation usage

### 4.1. Issuance process ###

### 4.2 Relying Party Obligations ###
When receiving and processing a OwnerShip List Attestation, a Relying Party SHALL:

@TODO Florin -> WP4 submission
The first 4 steps are basic verification - similar for all attestations:

### 4.2.1 Verify Cryptographic Integrity ###
- Validate the digital signature over the attestation using the issuer's public key
- For SD-JWT VC: Verify JWT signature and validate all disclosed claims
### 4.2.2 Validate Issuer ###

@TODO Werner
- Issuer Authentification
- Issuer Identification
- Issuer  Authorization
  - Verify that the issuer is authorized to issue Payment Terms Attestations
  - Check the issuer's credentials against the appropriate trust framework (see Chapter 5)
  - For "EAA": Confirm issuer authorization mechanisms

### 4.2.3 Holder Related check ###
- Revocation status check
  - Query the designated revocation/status mechanism (Cap 6)
  - Treat revoked or suspended attestations as invalid
  - @TODO Forin Check Handle indeterminate status according to organizational risk policy

- Check Temporal Validity ####
  - Validate issuanceDate / iat to ensure the attestation was issued in the past
  - Validate expirationDate / exp to ensure the attestation has not expired
  - Consider attestation age in relation to business risk (e.g., payment terms updated recently vs. stale data)

### 4.2.4  Holder Wallet Related check ###
#### 4.2.4.1.Device binding  ####
@TODO Werner
- avoid copy & reply
- WUA check

#### 4.2.5 Validate Integrity Rules ####
@TODO Context check

## 5 Trust anchors
@TODO Florin

## 6 Revocation
@TODO Florin

## 7 References