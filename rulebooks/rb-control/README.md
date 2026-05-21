# Attestation Rulebook for attestations of type Control List Attestation

* Author(s):
  * [Florin Coptil, Robert Bosch GmbH]

* Reviewer(s):
  * [......, Deutsche Bank]

| Version | Date       | Description                                                     |
|---------|------------|-----------------------------------------------------------------|
| 0.1     | 23.03.2026 | Initial draft based on the WeBuild design attestations mettings |
| 0.2     | 10.05.2026 | Updates for addresses and identifiers

* Contact:
  <a href="mailto:florin.coptil@bosch.com">Florin Coptil</a>

* Feedback: 

## 1 Introduction

This attestation addresses the following question:

**Who exercises effective control over this legal entity?**

A Controller is defined as any natural person or legal entity that directly or indirectly exercises effective control over a legal entity. A single person may exercise control through one or more control mechanisms simultaneously.
- Control is assessed based on the following mechanisms:
- Voting Rights — direct or indirect holding of voting rights above the defined threshold (typically 25%+)
- Board Control — ability to appoint, remove, or control board members or board decisions
- Management / Executive Roles — executive authority enabling operational or strategic control over the entity
- Contractual Rights — veto, consent, or other contractual rights enabling decisive influence over corporate actions
- Special Shares — ownership of share classes with enhanced voting rights or disproportionate control powers
- Power to Appoint or Remove Management — statutory or contractual authority to appoint or dismiss key executives or directors
- Trustee Control — discretionary control exercised through trusts, foundations, or similar fiduciary arrangements
- Dominant Influence — control arising from financial, operational, or commercial dependency relationships
- Influence via Parent or Holding Company — indirect control exercised through ownership or control of an intermediary entity

as required under AMLR / AMLD6 and applicable company law.

### 1.1 Document scope and purpose

The Control Attestation records all natural and legal persons which have control direct or indirect in a legal entity, providing comprehensive transparency on beneficial ownership structures and economic interests. This attestation is a critical component of both Know Your Customer (KYC) and Know Your Supplier (KYS) processes within the EUDI Wallet ecosystem, supporting effective risk management, regulatory compliance, and anti-money laundering (AML) obligations.

### 1.2 Document structure

This Rulebook is structured as follows:
- Chapter 2 describes the attestation attributes and metadata in an encoding-independent manner, including the data model.
- Chapter 3 specifies how the attestation attributes and metadata are encoded: Section 3.2 covers SD-JWT VC-based encoding.
- Chapter 4 specifies attestation usage scenarios, Relying Party obligations, and integration with KYC/KYS workflows.
- Chapter 5 defines trust anchors and verification mechanisms for issuer authorization.
- Chapter 6 defines revocation mechanisms for the attestation.
- Chapter 7 provides compliance information regarding the EUBW framework, AML regulations, corporate governance standards, and applicable data protection laws.
- Chapter 8 provides references to applicable standards and specifications.

### 1.3 Keywords

This document uses the capitalised keywords 'SHALL', 'SHOULD' and 'MAY' as specified in [RFC 2119], i.e. to indicate requirements, recommendations and options specified in this document.

In addition, 'must' (non-capitalised) is used to indicate an external constraint, i.e. a requirement that is not mandated by this document, but, for instance, by an external document. The word 'can' indicates a capability, whereas other words, such as 'will', and 'is' or 'are' are intended as statements of fact.

### 1.4 Terminology
This document uses the terminology specified in Annex 1 of the ARF.

**Additional terminology specific to this attestation:**

| **Term**                       | **Definition**                                                                                                                                                                                           |
|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Control                        | A comprehensive record of all natural and legal persons who exercise direct or indirect control over a legal entity, including control percentages and the mechanisms through which control is exercised |
| Effective Control              | The power to direct or influence the management, operations, or strategic decisions of a legal entity, regardless of ownership percentage                                                                |
| Control Mechanism              | The specific means by which a person exercises control (e.g., voting rights, board seats, management roles, contractual veto rights, golden shares, trustee authority, dominant influence)               |
| Controller                     | A natural or legal person who exercises control over a legal entity, either directly or indirectly                                                                                                       |
| Direct Control                 | Control exercised directly by a person through ownership of voting shares, board membership, or executive roles in the subject entity                                                                    |
| Indirect Control               | Control exercised through one or more intermediary entities or contractual arrangements (e.g., control via a parent company, nominee arrangements, or proxy voting agreements)                           |
| Control Percentage             | A quantitative measure of the degree of control a person exercises, typically based on voting rights percentage, board representation percentage, or other control metrics                               |
| KYC Know Your Customer         | due diligence process for verifying customer identity and assessing risk in financial relationships                                                                                                      |
| KYS Know Your Supplier         | due diligence process for verifying supplier credentials, integrity, and risk exposure                                                                                                                   |
| PEP Politically Exposed Person | individual entrusted with prominent public functions, posing higher risk for corruption or bribery                                                                                                       |
| EUCC EU Company Certificate    | attestation establishing the legal existence and identity of a legal entity within the EU                                                                                                                |
| Evidence                       | Supporting documentation substantiating the control structure calculation (e.g., governance chart, shareholder agreement, articles of association, trust deed)                                           |

## 2 Attestation attributes and metadata

The Control Attestation is designed to provide a complete, verifiable representation of an entity's control structure in a standardized digital format. This attestation supports transparency, compliance, and risk management by enabling automated verification of effective control across complex, multi-tiered corporate structures where control may be exercised through diverse mechanisms beyond simple shareholding.

### 2.1 Introduction

The Control follows a hierarchical structure:
````
Control
├─ NaturalPerson   [1...n]   (at least one natural person controller required)
│   ├─ Identifier        [1]       (the identifier of the natural person )
│   ├─ ResidenceAddress  [1]       (residence address per natural person controller)
│   ├─ ContactAddress    [0]       (contact address per natural person controller)
│   └─ Stake             [1]       (one stake record per natural person controller)
├─ LegalPerson     [0...m]   (zero or more legal entity controllers)
│   ├─ Identifier        [1]       (the identifier of the legal person )
│   ├─ RegisteredAddress [1]       (registered address per legal entity controller)
│   ├─ ContactAddress    [0]       (contact address per legal entity controller)
│   └─ Stake             [1]       (one stake record per natural person controller)
└─ Evidence        [1...n]   (at least one piece of supporting evidence required)
````
*Explanation:*
- The `control` attestation SHALL contain at least one natural_person who exercises control (to comply with AML requirements that mandate identification of natural persons who ultimately control the entity).
- The `control` attestation MAY contain zero or more legal_person entries, representing intermediate legal entities in the control chain.
- For each `natural_person` controller:
  - It SHALL include a family_name and given_name.
  - It MAY include birth_date, nationality.
  - It MAY include an identifier object containing issuing_country and document_number.
  - It SHALL include a mandatory residence_address.
  - It MAY include an optional contact_address.
  - It SHALL include exactly one stake record detailing the control interest.
- For each legal_person controller:
  - It SHALL include legal_entity_name, legal_form.
  - It SHALL include a mandatory legal_person_identifier object (with at least one of EUID, LEI, TAX specified).
  - It MAY include lei (as a specific field) and registration_number.
  - It SHALL include a mandatory registered_address.
  - It MAY include an optional contact_address.
  - It SHALL include exactly one stake record detailing the control interest.
- The `control` attestation SHALL include at least one piece of evidence (e.g., governance chart, shareholder agreement, articles of association) substantiating the control calculation. Multiple pieces of evidence MAY be included for complex structures.
  evidence MAY be provided as a URI reference (pointing to a publicly accessible or securely shared document) or as an embedded base64-encoded document (attached directly within the attestation).

| **Data Identifier**                    | **Semantic Reference** | **Definition**                                                                      | **Data type**                                                                    |
|----------------------------------------|------------------------|-------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| Natural Person attributes              | --                     | Identification and personal details of natural persons with control interests       | Object                                                                           |
| Legal Person attributes                | --                     | Identification and legal details of legal entities with control interests           | Object                                                                           |
| Stake attributes                       | --                     | Quantitative control data (control percentage) and control mechanism classification | Object                                                                           |
| Residence Address attributes           | ---                    | Residence address for natural person                                                | Object                                                                           |
| Registered Address attributes          | ---                    | Registered address for legal person                                                 | Object                                                                           |
| Contact Address attributes             | ---                    | Contact address for controller (natural or legal persons)                           | Object                                                                           |
| Evidence attributes                    | --                     | References to supporting documentation substantiating the control structure         | Object                                                                           |

**Attestation Classification:**

This attestation type is classified as
- **"EAA"** within the EUBW Wallet ecosystem, as it is typically self-issued by the legal entity subject to the ownership disclosure (i.e., the entity issues an attestation about its own control structure).


### 2.2 Mandatory attributes
**NaturalPerson Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                                                  | **Data type** |
|---------------------|------------------------|---------------------------------------------------------------------------------|---------------|
| family_name         | --                     | Last name(s) or surname(s) of the natural person who holds control              | String        |
| given_name          | --                     | First name(s), including middle name(s) where applicable, of the natural person | String        |

**LegalPerson Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                                                                                 | **Data type** |
|---------------------|------------------------|----------------------------------------------------------------------------------------------------------------|---------------|
| legal_person_name   | --                     | The complete official name of the legal entity which exercises control over this entity                        | String        |
| legal_form_type     | --                     | The legal form of the controlling legal entity (e.g., SA, GmbH, Ltd, BV)                                       | String        |

**Stake Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                                                                                                                                       | **Data type**    |
|---------------------|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| effective_control   | --                     | The percentage of direct control exercised by this controller (based on voting rights, decision-making power, or other control metrics)                              | Decimal          |
| legal_person_id     | --                     | The list of legal entity identifier where the controller's interests belong (direct legal entity and all indirect legal entities through which control is exercised) | Array of String  |
| control_mechanism   | --                     | Classification of the control mechanism(s) through which control is exercised                                                                                        | Array of Strings |

**Evidence Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                                                              | **Data type** |
|---------------------|------------------------|---------------------------------------------------------------------------------------------|---------------|
| evidence_id         | --                     | URI reference to the evidence document (e.g., organizational chart, shareholder register)   | String        |
| evidence_type       | --                     | Defines the type of the object, which SHALL be "Evidence"                                   | String        |

#### 2.3 Optional attributes

**NaturalPerson Optional Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                                                                     | **Data type**     |
|---------------------|------------------------|----------------------------------------------------------------------------------------------------|-------------------|
| birth_date          | --                     | Day, month, and year of birth of the natural person ISO 8601                                       | Date (YYYY-MM-DD) |

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

| **Data Identifier** | **Semantic Reference**  | **Definition**                                                         | **Data type** |
|---------------------|-------------------------|------------------------------------------------------------------------|---------------|
| address             | --                      | The street address where the controller currently resides              | String        |
| locality            | --                      | The city where the controller currently resides d                      | String        |
| postal_code         | --                      | The postal or ZIP code of the controller's address                     | String        |
| region              | --                      | The state, province, or region of the controller's address             | String        |                                            
| country             | --                      | ISO 3166-1 alpha-3 country code where the controller currently resides | String        | 

**RegisteredAddress Optional Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                                                          | **Data type** |
|---------------------|------------------------|-----------------------------------------------------------------------------------------|---------------|
| address             | --                     | The street address where the legal controller currently is registered                   | String        |
| locality            | --                     | The city where the  legal controller currently is registered                            | String        |
| postal_code         | --                     | The postal or ZIP code of the legal controller's address                                | String        |
| region              | --                     | The state, province, or region of the lega controller's address                         | String        |                                            
| country             | --                     | ISO 3166-1 alpha-3 country code where the legal controller currently is registered      | String        | 

**ContactAddress Optional Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                                         | **Data type** |
|---------------------|------------------------|------------------------------------------------------------------------|---------------|
| address             | --                     | The street address where the controller  can be contacted              | String        |
| locality            | --                     | The city where the controller  can be contacted                        | String        |
| postal_code         | --                     | The postal or ZIP code of the controller's address                     | String        |
| region              | --                     | The state, province, or region of the controller's address             | String        |                                            
| country             | --                     | ISO 3166-1 alpha-3 country code where the controller can be contacted  | String        | 

**Evidence Optional Attributes**

| **Data Identifier**   | **Semantic Reference** | **Definition**                                                                                                                                     | **Data type**   |
|-----------------------|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| evidence_data         | --                     | The actual organizational structure document as a base64-encoded string (required if evidence_id does not contain a URI to an accessible location) | String (base64) |
| evidence_confirmation | --                     | Boolean confirmation that the organizational structure document is current and has been used as the basis for the control calculation              | Boolean         |
| evidence_date         | --                     | The date when the evidence document was created or last updated ISO 8601                                                                           | Date            |

#### 2.4 Conditional attributes
No conditional attributes are defined for this attestation type. All attributes are either mandatory or optional as specified above.

#### 2.5 Mandatory metadata

| **Data Identifier**          | **Definition**                                                                                                                    | **Data type**    |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|------------------|
| issuance_date                | The date and time when the attestation was issued ISO 8601                                                                        | DateTime         |
| expiry_date                  | The date and time when the attestation expires ISO 8601                                                                           | DateTime         |
| issuing_entity               | The identifier of the legal entity that issued the attestation (typically the subject entity itself for self-issued attestations) | String           | 
| attestation_legal_category   | Indicates the legal category of this attestation ("EAA")                                                                          | String           |

### 2.6 Optional metadata

| **Data Identifier**  | **Definition**                                                             | **Data type** |
|----------------------|----------------------------------------------------------------------------|---------------|
| trust_anchor_url     | URL where the trust anchor for verifying this attestation can be retrieved | URI           |
| schema_version       | Version of the schema used                                                 | String        |

#### 2.7 Conditional metadata
No conditional metadata elements are defined for this attestation type.

### 2.8 Value Lists

#### 2.8.1 Control Category Codes

The control_mechanism attribute SHALL use one or more of the following standardized values (represented as an array to accommodate multiple simultaneous control mechanisms):

| **Code**                                  | **Definition**                                                                                                                                                                                                                                                                                                    |
|-------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Voting rights                             | Control exercised through ownership of voting shares, including ordinary shares, preference shares with voting rights, or shares with enhanced voting rights Person holds 51% of voting shares, giving majority voting power                                                                                      |
| Board control                             | Control exercised through board of directors representation, including majority of board seats, chairmanship, or special board appointment rights Person appoints 3 out of 5 board members via shareholder agreement                                                                                              |
| Management / Executive roles              | Control exercised through executive positions such as CEO, CFO, Managing Director, or other C-suite roles with operational authority Person serves as CEO with authority to make operational decisions without board approval below certain thresholds                                                            |
| Contractual rights                        | Control exercised through contractual provisions such as veto rights, consent requirements, drag-along/tag-along rights, or put/call options Shareholder agreement grants Person veto rights over major corporate actions (M&A, capital increases, dividend policy)                                               |
| Special shares                            | Control exercised through special classes of shares (golden shares, founder shares) that confer disproportionate voting rights or veto powers Person holds 1% of shares but "Class A" shares carry 10x voting power, giving effective 9.1% voting control                                                         |
| Power to appoint/remove management        | Control exercised through the contractual or statutory right to appoint or remove key executives or directors Majority shareholder has right to appoint/remove CEO per articles of association                                                                                                                    |
| Trustee                                   | Control exercised as trustee of a trust, foundation, or similar fiduciary arrangement where the trustee has discretionary decision-making powers Person acts as trustee of a family trust that owns 40% of the entity, with discretion over voting and corporate actions                                          |
| Dominant influence                        | Control exercised through dominant influence mechanisms such as operational dependencies, exclusive supply/distribution agreements, or financing arrangements with control covenants Parent company provides 100% of entity's financing under loan agreement with covenants granting control over major decisions |
| Influence via parent or holding company   | Indirect control exercised through a parent or holding company that controls the subject entity Person controls Parent Co. (100% ownership), which controls Subject Entity (80% ownership), giving Person effective 80% indirect control                                                                          |

Note: Multiple control mechanisms MAY apply to a single controller (e.g., a person may exercise control through both "Voting rights" AND "Board control"). In such cases, the control_mechanism attribute SHALL be encoded as an array containing all applicable codes.

### 2.9 Integrity Rules
TODO Florin
The following integrity rules SHALL be enforced:

## 3 Attestation encoding

### 3.1 ISO/IEC 18013-5-compliant encoding

ISO/IEC 18013-5 (also called mdoc) is out of scope for this Rulebook, as offline proximity
presentation is not a current requirement for the Control attestation.

### 3.2 SD-JWT VC-based encoding

The Control attestation uses the SD-JWT VC format to allow for selective disclosure of
control structure attributes.

**Selective Disclosure:** Top-level claims (`ControlNaturalPerson`, `ControlLegalPerson`,
`Evidence`) SHALL be individually selectively disclosable, enabling a legal entity to disclose
only the attributes requested by a Relying Party.

The `.` notation is used to indicate the nesting of attributes.

**Verifiable Credential Type (`vct`):** `vct: eu.we-build.control.1`

#### 3.2.1 Attribute Encoding Table

| **Data Identifier**        | **Attribute identifier**                                                        | **Encoding format**          | **Reference/Notes**                                                                                                                                   | **Disclosable**  |
|----------------------------|---------------------------------------------------------------------------------|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| control                    | `control`                                                                       | Array [Control]              | Array [Control]	Array of control objects. Each object represents a natural or legal person controller. SHALL contain at least one control             | MUST             |
| **NaturalPerson**          |                                                                                 |                              |                                                                                                                                                       |                  |
| family_name                | `control[n].natural_person.family_name`                                         | String                       | Last name(s) or surname(s) of the natural person who holds control                                                                                    | MUST             |
| given_name                 | `control[n].natural_person.given_name`                                          | String                       | First name(s), including middle name(s) where applicable                                                                                              | MUST             |
| birth_date                 | `control[n].natural_person.birth_date`                                          | String (ISO 8601 YYYY-MM-DD) | Day, month, and year of birth of the natural person; optional                                                                                         | MUST             |
| **NaturalPersonIdentifier** |                                                                                 | Optional identification details for the natural person.                             |                                                                                                                                                       |                  |
| document_type              | `control[n].natural_person.identifier.document_type`                            | String                       | A value defining the type of the identity document according to the nationality of the UBO (e.g., Passport, National identity card, Driver's license) | MUST             |
| document_number            | `control[n].natural_person.identifier.document_number`                          | String                       | The number of the identity document (passport number, national ID number, driver's license number, etc.)                                              | MUST             |
| issuing_country            | `control[n].natural_person.identifier.issuing_country`                        / | String (ISO 3166-1 alpha-3)  | The country that issued the identity document                                                                                                         | MUST             |
| **ResidenceAddress**       |                                                                                 |                              |                                                                                                                                                         |                  |
| address                    | `control[n].natural_person.residence_address.address`                           | String                       | Street address where the controller currently resides ; optional                                                                                        | MUST             |
| locality                   | `control[n].natural_person.residence_address.locality`                          | String                       | City where the controller currently resides optional                                                                                                    | MUST             |
| state                      | `control[n].natural_person.residence_address.state`                             | String                       | State, province, or region of the controller's address; optional                                                                                        | MUST             |
| postal_code                | `control[n].natural_person.residence_address.postal_code`                       | String                       | Postal or ZIP code of the controller's address; optional                                                                                                | MUST             |
| country                    | `control[n].natural_person.residence_address.country`                           | String (ISO 3166-1 alpha-3)  | Country where the controller currently resides ; optional                                                                                               | MUST             |
| **ContactAddress**         |                                                                                 |                              |                                                                                                                                                         |                  |
| address                    | `control[n].natural_person.contact_address.address`                             | String                       | Street address where the controller can be contacted; optional                                                                                          | MUST             |
| locality                   | `control[n].natural_person.contact_address.locality`                            | String                       | City where the controller can be contacted; optional                                                                                                    | MUST             |
| state                      | `control[n].natural_person.contact_address.state`                               | String                       | State, province, or region of the controller's address; optional                                                                                        | MUST             |
| postal_code                | `control[n].natural_person.contact_address.postal_code`                         | String                       | Postal or ZIP code of the controller's address; optional                                                                                                | MUST             |
| country                    | `control[n].natural_person.contact_address.country`                             | String (ISO 3166-1 alpha-3)  | Country where the controller can be contacted; optional                                                                                                 | MUST             |
| **Stake**                  |                                                                                 |                              |                                                                                                                                                         |                  |
| effective_control          | `control[n].natural_person.stake.effective_control`                             | Decimal (number)             | Percentage of direct control exercised by this controller (based on voting rights, decision-making power, or other control metrics)                     | MUST             |
| legal_person_id            | `control[n].natural_person.stake.legal_person_id`                               | String                       | Unique legal entity identifier where the controller's interests belong (direct and all indirect legal entities through which control is exercised)      | MUST             |
| control_mechanism          | `control[n].natural_person.stake.control_mechanism`                             | Array of Strings             | Classification of the control mechanism(s) through which control is exercised                                                                           | MUST             |
| **LegalPerson**            |                                                                                 |                              |                                                                                                                                                         |                  |
| legal_entity_name          | `control[n].legal_person.legal_entity_name`                                     | String                       | Complete official name of the legal entity which exercises control                                                                                      | MUST             |
| legal_form_type            | `control[n].legal_person.legal_form_type`                                       | String                       | Legal form of the controlling legal entity (e.g., SA, GmbH, Ltd, BV)                                                                                    | MUST             |
| **LegalPersonIdentifier**  |                                                                                 |                              |                                                                                                                                                         |                  |
| euid                       | `control[n].legal_person.identifier.euid`                                  | String                       | Complete official name of the legal entity which exercises control                                                                                      | MUST             |
| lei                        | `control[n].legal_person.identifier.lei`                                   | String (20 characters)       | LEI code of the controlling legal entity; optional                                                                                                      | MUST             |
| tax                        | `control[n].legal_person.identifier.tax`                                   | String                       | National company registration number; optional                                                                                                          | MUST             |
| **RegisteredAddress**      |                                                                                 |                              | Mandatory residence address for the natural person controller. All sub-fields are optional.                                                                                                                                                        |                  |
| address                    | `control[n].legal_person.registered_address.address`                            | String                       | Street address where the controling entity is registered ; optional                                                                                     | MUST             |
| locality                   | `control[n].legal_person.registered_address.locality`                           | String                       | City where the controling entity is registered ; optional                                                                                               | MUST             |
| postal_code                | `control[n].legal_person.registered_address.postal_code`                        | String                       | Postal or ZIP code of the controling entity's address; optional                                                                                         | MUST             |
| region                     | `control[n].legal_person.registered_address.region`                             | String                       | State, province, or region of the controling entity's address; optional                                                                                 | MUST             |
| country                    | `control[n].legal_person.registered_address.country`                            | String (ISO 3166-1 alpha-3)  | Country where the controling entity is registered ; optional                                                                                            | MUST             |
| **ContactAddress**         |                                                                                 |                              | Optional contact address for the natural person controller. All sub-fields are optional.                                                                                                                                                        |                  |
| address                    | `control[n].legal_person.contact_address.address`                               | String                       | Street address where the controling entity can be contacted; optional                                                                                   | MUST             |
| locality                   | `control[n].legal_person.contact_address.locality`                              | String                       | City where the controling entity can be contacted; optional                                                                                             | MUST             |
| postal_code                | `control[n].legal_person.contact_address.postal_code`                           | String                       | Postal or ZIP code of the controling entity's address; optional                                                                                         | MUST             |
| region                     | `control[n].legal_person.contact_address.region`                                | String                       | State, province, or region of the controling entity's address; optional                                                                                 | MUST             |
| country                    | `control[n].legal_person.contact_address.country`                               | String (ISO 3166-1 alpha-3)  | Country where the controling entity can be contacted; optional                                                                                          | MUST             |
| **Stake**                  |                                                                                 |                              |                                                                                                                                                         |                  |
| effective_control          | `control[n].legal_person.stake.effective_control`                               | Decimal (number)             | Percentage of direct control exercised by this controlling legal entity                                                                                 | MUST             |
| legal_person_id            | `control[n].legal_person.stake.legal_person_id`                                 | String                       | Unique legal entity identifier where the controller's interests belong                                                                                  | MUST             |
| control_mechanism          | `control[n].legal_person.stake.control_mechanism`                               | Array of Strings             | Classification of the control mechanism(s) through which control is exercised                                                                           | MUST             |
| **Evidence**               |                                                                                 |                              |                                                                                                                                                         |                  |
| evidence_id                | `evidence[n].evidence_id`                                                       | String (URI)                 | URI reference to the evidence document (e.g., organizational chart, shareholder register)                                                               | MUST             |
| evidence_type              | `evidence[n].evidence_type`                                                     | String                       | Defines the type of the object, which SHALL be "Evidence"                                                                                               | MUST             |
| evidence_data              | `evidence[n].evidence_data`                                                     | String (base64)              | Actual organizational structure document as a base64-encoded string; required if evidence_id does not contain a URI to an accessible location; optional | MUST             |
| evidence_confirmation      | `evidence[n].evidence_confirmation`                                             | Boolean                      | Confirmation that the organizational structure document is current and has been used as the basis for the control calculation; optional                 | MUST             |
| evidence_date              | `evidence[n].evidence_date`                                                     | String (ISO 8601 YYYY-MM-DD) | Date when the evidence document was created or last updated; optional                                                                                   | MUST             |
| **Metadata**               |                                                                                 |                              |                                                                                                                                                         |                  |
| issuance_date              | `iat`                                                                           | Number (Unix timestamp)      | The date and time when the attestation was issued (ISO 8601); RFC 7519 / Section 2.5                                                                    | MUST NOT         |
| expiry_date                | `exp`                                                                           | Number (Unix timestamp)      | The date and time when the attestation expires (ISO 8601); RFC 7519 / Section 2.5                                                                       | MUST NOT         |
| issuing_entity             | `issuing_entity`                                                                | String                       | Identifier of the legal entity that issued the attestation (subject entity for EAA)                                                                     | MUST NOT         |
| attestation_legal_category | `attestation_legal_category`                                                    | String                       | One of `EAA` as defined by eIDAS 2                                                                                                                      | MUST NOT         |
| trust_anchor_url           | `trust_anchor_url`                                                              | String (URI)                 | URL where the trust anchor for verifying this attestation can be retrieved; optional                                                                    | MUST NOT         |
| schema_version             | `schema_version`                                                                | String                       | Version of the schema used; optional                                                                                                                    | MUST NOT         |

**Notes:**

- **MUST**: The claim SHALL be selectively disclosable — the holder MAY choose to disclose or
  withhold this claim when presenting the credential to a Relying Party.
- **MUST NOT**: The claim SHALL NOT be selectively disclosable — it is always present in plain
  text in the JWT header/payload and cannot be withheld by the holder, as it is required for
  credential verification and trust establishment.
- `ControlNaturalPerson` entries are indexed as `[n]` where `n` starts at 0; at least one
  natural person controller SHALL be present.
- `ControlLegalPerson` entries are indexed as `[m]` where `m` starts at 0; zero or more legal
  person controllers MAY be present.
- `Evidence` entries are indexed as `[n]` where `n` starts at 0; at least one evidence entry
  SHALL be present.
- `iat`, `exp`, and `iss` follow RFC 7519 standard JWT claim naming conventions.

#### 3.2.2 Status Claim

For SD-JWT VC-compliant Control attestations, the attestation MUST include a `status` claim
if the technical validity period is greater than 24 hours. This claim enables Relying Parties to
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
 "status_list_credential": "https://issuer.example.com/status/control/2025",
 "status_list_index": 456,
 "status_purpose": "revocation"
  }
}
```

### 3.2.3 Example Payload

The following is a non-normative example of a CompanyInfo SD-JWT VC payload:
```
{
  "vct": "eu.we-build.control.1",
  "attestation_legal_category": "EAA",
  "issuing_entity": "did:example:legal-entity-456",
  "control": [
    {
      "natural_person": {
        "family_name": "Garcia",
        "given_name": "Maria",
        "birth_date": "1968-07-22",
        "natural_person_identifier": {
          "document_type": "National identity card",
          "document_number": "ES12345678X",
          "issuing_country": "ESP"
        },
        "residence_address": {
          "address": "Calle Mayor 10",
          "locality": "Madrid",
          "postal_code": "28001",
          "country": "ESP"
        },
        "stake": {
          "effective_control": 55.00,
          "legal_person_id": "54321098765432109876",
          "control_mechanism": ["Voting rights", "Board control"]
        }
      }
    },
    {
      "legal_person": {
        "legal_person_name": "Global Solutions Ltd.",
        "legal_form_type": "Private Limited Company",
        "legal_person_identifier": {
          "lei": "54321098765432109876"
        },
        "registered_address": {
          "address": "1 Global Plaza",
          "locality": "London",
          "postal_code": "EC2Y 5AU",
          "country": "GBR"
        },
        "stake": {
          "effective_control": 30.00,
          "legal_person_id": "54321098765432109876",
          "control_mechanism": ["Influence via parent or holding company"]
        }
      }
    }
  ],
  "evidence": [
    {
      "evidence_id": "https://example.com/governance-chart-2024.pdf",
      "evidence_type": "Evidence",
      "evidence_confirmation": true,
      "evidence_date": "2024-03-01"
    },
    {
      "evidence_id": "urn:webuild:articles-of-association",
      "evidence_type": "Evidence",
      "evidence_data": "PGh0bWw+DQogIDxoZWFkPg0KICAgIDx0aXRsZT5BcnRpY2xlcyBvZiBBc3NvY2lhdGlvbjwvdGl0bGU+DQogIDwvaGVhZD4NCiAgPGJvZHk+DQogICAgPHA+VGhpcyBpcyBhIGxhdyBkb2N1bWVudC48L3A+DQogIDwvYm9keT4NCjwvaHRtbD4="
    }
  ],
  "status": {
    "type": "status-list",
    "status_list_credential": "https://example.com/status/control-list-1",
    "status_list_index": 789,
    "status_purpose": "revocation"
  },
  "trust_anchor_url": "https://webuildconsortium.eu/trust-anchor.json",
  "schema_version": "0.1.0",
  "cnf": {
    "jwk": {
      "kty": "RSA",
      "n": "q_u_X8P_S0_0F8_C_f83_oX1f8m5y_B7D9S9-C_0R5-Q0_u_X8P_S0_0F8_C",
      "e": "AQAB"
    }
  }
}
```
Sample payloads are provided under
../data-schemas/sd-jwt/sample-data/control-sd-jwt-sample.json

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
| **Item Reference**                     | **Standard name/details**                                                                                                                                                                                                                      |
|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [European Digital Identity Regulation] | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework |
| [HAIP]                                 | 	Yasuda, K. et al, OpenID4VC High Assurance Interoperability Profile, OpenId Foundation, Version draft-03                                                                                                                                      |
| [IANA-JWT-Claims]	                     | IANA JSON Web Token Claims Registry. Available: https://www.iana.org/assignments/jwt/jwt.xhtml                                                                                                                                                 |
| [ISO/IEC 18013-5]	                     | ISO/IEC 18013-5, Personal identification — ISO-compliant driving licence - Part 5: Mobile driving licence (mDL) application, First edition, 2021-09                                                                                            |
| [ISO 4217]	                            | ISO 4217 — Currency codes. Available: https://www.iso.org/iso-4217-currency-codes.htmlv                                                                                                                                                        | 
| [OIDC]	                                | Sakimura, N. et al., "OpenID Connect Core 1.0", OpenID Foundation. Available: https://openid.net/specs/openid-connect-core-1_0.html                                                                                                            |
| [RFC 2119]	                            | RFC 2119 — Key words for use in RFCs to Indicate Requirement Levels, S. Bradner, March 1997                                                                                                                                                    |
| [RFC 3339]	                            | RFC 3339 — Date and Time on the Internet: Timestamps, G. Klyne et al., July 2002                                                                                                                                                               |
| [RFC 8610]	                            | RFC 8610 — Concise Data Definition Language (CDDL): A Notational Convention to Express Concise Binary Object Representation (CBOR) and JSON Data Structures, H. Birkholz et al., June 2019                                                     |
| [RFC 8943]	                            | RFC 8943 — Concise Binary Object Representation (CBOR) Tags for Date, M. Jones et al., November 2020                                                                                                                                           |
| [RFC 8949]	                            | RFC 8949 — Concise Binary Object Representation (CBOR), C. Bormann et al., December 2020                                                                                                                                                       |
| [SD-JWT VC]                            | 	SD-JWT-based Verifiable Credentials (SD-JWT VC). Available: https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/, version draft-ietf-oauth-sd-jwt-vc-09                                                                               |
| [Topic 7]	                             | ARF Annex 2 - Topic 7 - Attestation revocation and revocation checking. Available: https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a237-topic-7-attestation-revocation-and-revocation-checking |