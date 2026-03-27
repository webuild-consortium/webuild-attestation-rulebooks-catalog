* Template version: 1.1, 20-08-2025
# Attestation Rulebook for attestations of type Control List Attestation

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
The Control List Attestation captures all natural and legal persons who exercise direct or indirect control over a legal entity, providing comprehensive visibility into decision-makers and influencers whose power may not be reflected solely through ownership percentages. This attestation complements the Ownership List (UBO List) by focusing specifically on control mechanisms—such as voting rights, board representation, management authority, contractual powers, and dominant influence—that determine who effectively steers the entity's operations, strategy, and governance.

### 1.2 Document structure
This Rulebook is structured as follows:
- Chapter 2 describes the Control List attestation attributes and metadata in an encoding-independent manner, including the hierarchical control data model.
-Chapter 3 specifies how the attestation attributes and metadata are encoded:Section 3.1: ISO/IEC 18013-5-compliant encoding (applicability assessment)
  - Section 3.2: SD-JWT VC-based encoding
- Chapter 4 specifies attestation usage scenarios, Relying Party obligations, and integration with KYC/KYS workflows.
- Chapter 5 defines trust anchors and verification mechanisms for issuer authorization.
- Chapter 6 defines revocation mechanisms for the attestation.
- Chapter 7 provides compliance information regarding the EUBW framework, AML regulations, corporate governance standards, and applicable data protection laws.

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

| **Term**                       | **Definition**                                                                                                                                                                                         |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Control List                   |A comprehensive record of all natural and legal persons who exercise direct or indirect control over a legal entity, including control percentages and the mechanisms through which control is exercised|
| Effective Control              |The power to direct or influence the management, operations, or strategic decisions of a legal entity, regardless of ownership percentage|
| Control Mechanism              |The specific means by which a person exercises control (e.g., voting rights, board seats, management roles, contractual veto rights, golden shares, trustee authority, dominant influence)|
| Controller                     |A natural or legal person who exercises control over a legal entity, either directly or indirectly|
| Direct Control                 | Control exercised directly by a person through ownership of voting shares, board membership, or executive roles in the subject entity|
| Indirect Control               |Control exercised through one or more intermediary entities or contractual arrangements (e.g., control via a parent company, nominee arrangements, or proxy voting agreements)|
| Control Percentage             | A quantitative measure of the degree of control a person exercises, typically based on voting rights percentage, board representation percentage, or other control metrics|
| Nominee Director               |A board member appointed to represent the interests of a specific shareholder or external party, who may exercise control on behalf of that party|
| KYC Know Your Customer         | due diligence process for verifying customer identity and assessing risk in financial relationships|
| KYS Know Your Supplier         | due diligence process for verifying supplier credentials, integrity, and risk exposure|
| PEP Politically Exposed Person | individual entrusted with prominent public functions, posing higher risk for corruption or bribery|
| EUCC EU Company Certificate    |attestation establishing the legal existence and identity of a legal entity within the EU|
| Evidence                       |Supporting documentation substantiating the control structure calculation (e.g., governance chart, shareholder agreement, articles of association, trust deed)|

## 2 Attestation attributes and metadata

The Control List Attestation is designed to provide a complete, verifiable representation of an entity's control structure in a standardized digital format. This attestation supports transparency, compliance, and risk management by enabling automated verification of effective control across complex, multi-tiered corporate structures where control may be exercised through diverse mechanisms beyond simple shareholding.

### 2.1 Introduction

Data Model:

The Conrol List follows a hierarchical structure:

Data Model
```json

Control List
├─ ControlNaturalPerson   [1...n]   (at least one natural person controller required)
│   ├─ ControlAddress     [1]       (one address per natural person controller)
│   └─ ControlStake       [1]       (one stake record per natural person controller)
├─ ControlLegalPerson     [0...m]   (zero or more legal entity controllers)
│   ├─ ControlAddress     [1]       (one address per legal entity controller)
│   └─ ControlStake       [1]       (one stake record per legal entity controller)
└─ Evidence               [1...n]   (at least one piece of supporting evidence required)
```

*Explanation:*
- The Control List SHALL contain at least one control interest held by a natural person (to comply with AML requirements that mandate identification of natural persons who ultimately control the entity).
- The Control List MAY contain zero or more control interests held by legal persons (intermediate entities in the control chain).
- Each controller (natural or legal person) SHALL have exactly one associated ControlStake record and one ControlAddress record.
- The Control List SHALL include at least one piece of Evidence (e.g., governance chart, shareholder agreement, articles of association) substantiating the control calculation. Multiple pieces of evidence MAY be included for complex structures.
- Evidence MAY be provided as:URI reference (pointing to a publicly accessible or securely shared document)
- Embedded base64-encoded document (attached directly within the attestation)

This attestation type is classified as a "EAA" within the EUBW Wallet ecosystem, as it is typically self-issued by the legal entity subject to the ownership disclosure (i.e., the entity issues an attestation about its own ownership structure).

| **Data Identifier**                   | **Definition**                                                       | **Data type** |
|---------------------------------------|----------------------------------------------------------------------|---------------|
| Controller Natural Person attributes  | Identification and personal details of natural persons with control interests|
| Controller Legal Person attributes    | Identification and legal details of legal entities with control interests|
| Control Stake attributes              | Quantitative control data (control percentage) and control mechanism classification|
| Controller Address attributes         |Contact and residence information for controllers|
| Evidence attributes                   | References to supporting documentation substantiating the control structure|

### 2.2 Mandatory attributes
@TODO Florin still to confirmed with Barth the type (after matching in vocabulary document)
**ControlNaturalPerson Attributes**

| **Data Identifier**        | **Definition**      | **Data type**                       |
|----------------------------|-------------------------------------------------------------------|-------------------------------------|
| family_name                |Last name(s) or surname(s) of the natural person who holds control |String|
| given_name                 | First name(s), including middle name(s) where applicable, of the natural person |String|
| attestation_legal_category |Indicates the legal category of this attestation (EAA)| String |

**ControlLegalPerson Attributes**

| **Data Identifier** | **Definition**                                                                                                | **Data type** |
|---------------------|---------------------------------------------------------------------------------------------------------------|---------------|
| legal_entity_name   |The complete official name of the legal entity which exercises control over this entity |String |
| legal_form          |The legal form of the controlling legal entity (e.g., SA, GmbH, Ltd, BV) |String |
| identification      | The unique identifier of the legal entity which controls the subject entity (e.g., EUID, national tax ID, LEI)| String|

**ControlStake Attributes**

| **Data Identifier**     | **Definition**      | **Data type**     |
|-------------------------|------------------------------------------------------------------------------|-------------------|
| effective_control       |The percentage of direct control exercised by this controller (based on voting rights, decision-making power, or other control metrics)| Decimal           |
| legal_entity_identifier | The unique legal entity identifier where the controller's interests belong (direct legal entity and all indirect legal entities through which control is exercised) | String            |
| control_mechanism       |Classification of the control mechanism(s) through which control is exercised| Array of Strings  |

**Evidence Attributes**

| **Data Identifier** | **Definition**      | **Data type** |
|---------------------|------------------------------------------------------------------------------|---------------|
| evidence_id         |URI reference to the evidence document (e.g., organizational chart, shareholder register) |String |
| evidence_type       |Defines the type of the object, which SHALL be "Evidence"| String|

#### 2.3 Optional attributes

**ControlNaturalPerson Optional Attributes**

| **Data Identifier** | **Definition**      | **Data type** |
|---------------------|------------------------------------------------------------------------------|---------------|
| birth_date          |Day, month, and year of birth of the natural person ISO 8601 |Date (YYYY-MM-DD)|
@TODO FLORIN
| nationality         |ISO 3166-1 alpha-2 country code representing the nationality of the natural person | String        |
| national_id_number  |National identification number (e.g., passport number, social security number, national ID number) | String        |

**ControlLegalPerson Optional Attributes**

| **Data Identifier**                             | **Definition**                       | **Data type** |
|-------------------------------------------------|--------------------------------------|---------------|
| lei Legal Entity Identifier (LEI) per ISO 17442 | String (20 characters)               |
| registration_number                             | National company registration number | String                 |

**ControlAddress Optional Attributes**

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
| issuing_entity_name The official name of the issuing entity                                                                                                                       |String|
| issuer_country ISO 3166-1 alpha-2 country code of the issuing entity's jurisdiction                                                                                               |String (2 characters) |

#### 2.6 Optional metadata

| **Data Identifier**                 | **Definition**                                                          | **Data type**                          |
|-------------------------------------|-------------------------------------------------------------------------|----------------------------------------|
| trust_anchor_url                    | URL where the trust anchor for verifying this attestation can be retrieved | URI|
| schema_version                      | Version of the Owner List schema used                                   |String |

#### 2.7 Conditional metadata
No conditional metadata elements are defined for this attestation type.

### 2.8 Value Lists

#### 2.8.1 Control Category Codes

The control_mechanism attribute SHALL use one or more of the following standardized values (represented as an array to accommodate multiple simultaneous control mechanisms):

| **Code**                                  | **Definition**      |
|-------------------------------------------|---------------------------------------------------------------------|
| Voting rights                             |Control exercised through ownership of voting shares, including ordinary shares, preference shares with voting rights, or shares with enhanced voting rights Person holds 51% of voting shares, giving majority voting power|
| Board control                             | Control exercised through board of directors representation, including majority of board seats, chairmanship, or special board appointment rights Person appoints 3 out of 5 board members via shareholder agreement|
| Management / Executive roles              |Control exercised through executive positions such as CEO, CFO, Managing Director, or other C-suite roles with operational authority Person serves as CEO with authority to make operational decisions without board approval below certain thresholds|
| Contractual rights                        |Control exercised through contractual provisions such as veto rights, consent requirements, drag-along/tag-along rights, or put/call options Shareholder agreement grants Person veto rights over major corporate actions (M&A, capital increases, dividend policy)|
| Special shares                            |Control exercised through special classes of shares (golden shares, founder shares) that confer disproportionate voting rights or veto powers Person holds 1% of shares but "Class A" shares carry 10x voting power, giving effective 9.1% voting control|
| Power to appoint/remove management        |Control exercised through the contractual or statutory right to appoint or remove key executives or directors Majority shareholder has right to appoint/remove CEO per articles of association|
| Trustee                                   | Control exercised as trustee of a trust, foundation, or similar fiduciary arrangement where the trustee has discretionary decision-making powers Person acts as trustee of a family trust that owns 40% of the entity, with discretion over voting and corporate actions|
| Dominant influence                        | Control exercised through dominant influence mechanisms such as operational dependencies, exclusive supply/distribution agreements, or financing arrangements with control covenants Parent company provides 100% of entity's financing under loan agreement with covenants granting control over major decisions|
| Influence via parent or holding company   |Indirect control exercised through a parent or holding company that controls the subject entity Person controls Parent Co. (100% ownership), which controls Subject Entity (80% ownership), giving Person effective 80% indirect control|

Note: Multiple control mechanisms MAY apply to a single controller (e.g., a person may exercise control through both "Voting rights" AND "Board control"). In such cases, the control_mechanism attribute SHALL be encoded as an array containing all applicable codes.

List the owner multiple times with different categories, OR
Extend the ownership_category to an array of strings (see encoding-specific sections)

## 3 Attestation encoding

### 3.1 ISO/IEC 18013-5-compliant encoding

Control List Attestations are not intended for offline, proximity-based presentation scenarios due to the complexity and data volume of ownership structures, the need for dynamic verification against sanctions/PEP databases, and the requirement for real-time revocation checks.

Therefore, ISO/IEC 18013-5 mdoc encoding is out of scope for this attestation type.

### 3.2 SD-JWT VC-based encoding

The following table maps the data identifiers defined in Chapter 2 to SD-JWT VC claim names:
@TODO Florin&Bart - when the semantic is ready

The . notation is used to indicate the nesting of attributes.

@TOOD Florin&Mike - if is possible to referer some how the main class here over URI ?
**Verifiable Credential Type (`vct`):** `urn:eubw:controllist:1`

## 4 Attestation usage
### 4.1. Issuance process ###

### 4.2 Relying Party Obligations ###
When receiving and processing a ControlList Attestation, a Relying Party SHALL:

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

## 8 References