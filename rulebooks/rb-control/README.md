# Attestation Rulebook for attestations of type Control Attestation

* Author(s):
  * [Florin Coptil, Robert Bosch GmbH]
* Reviewer(s):
  * [Baumgardt Michaela, Commerzbank]
  * [Stephan Fuchs, Deutsche Bank]

| Version | Date       | Description                                                     |
|---------|------------|-----------------------------------------------------------------|
| 0.1     | 23.03.2026 | Initial draft based on the WeBuild design attestations meetings |
| 0.3     | 01.06.2026 | Updates of content based on meetings                            |

* Contact:
  * [Florin Coptil](mailto:florin.coptil@bosch.com)

* Feedback:

---

## 1 Introduction

This attestation addresses the following question:

**Who exercises effective control over this legal entity?**

A Controller is any natural person or legal entity that directly or indirectly exercises effective control over a legal entity.

### 1.1 Document scope and purpose

The Control Attestation records all natural and legal persons which have control direct or
indirect in a legal entity, providing comprehensive transparency on beneficial ownership
structures and economic interests. This attestation is a critical component of both Know Your
Customer (KYC) and Know Your Supplier (KYS) processes within the EUDI Wallet ecosystem,
supporting effective risk management, regulatory compliance, and anti-money laundering (AML)
obligations.

A Controller is any natural person or legal entity that directly or indirectly
exercises effective control over a legal entity, based on:

- **Voting rights** — direct or indirect control through voting rights held,  including enhanced voting rights that exceed the ownership percentage,  expressed as a percentage (0–100) or null where not applicable
- **Control type** — direct (exercised without intermediaries) or indirect (exercised through one or more intermediate legal entities)
- **Board rights** — right to appoint or remove directors or senior management
- **Veto rights** — right to block key corporate decisions
- **Contractual control** — control via formal or informal agreements
- **Nominee arrangements** — control exercised behind a nominee shareholder  or director
- **Profit distribution** — right to determine how profits are distributed, regardless of whether the 25% ownership threshold is met, as required under AMLR / AMLD6 and applicable company law

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
- Chapter 7 provides compliance information regarding the EBW framework, AML regulations,
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

*Additional terminology specific to this attestation:*

| **Term**                           | **Definition**                                                                                                                                                                                           |
|------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Control                            | A comprehensive record of all natural and legal persons who exercise direct or indirect control over a legal entity, including control percentages and the mechanisms through which control is exercised |
| Controller                         | A natural or legal person who exercises control over a legal entity, either directly or indirectly                                                                                                       |
| Direct Control                     | Control exercised directly by a person through ownership of voting shares, board membership, or executive roles in the subject entity                                                                    |
| Indirect Control                   | Control exercised through one or more intermediary entities or contractual arrangements (e.g., control via a parent company, nominee arrangements, or proxy voting agreements)                           |
| Control Percentage                 | A quantitative measure of the degree of control a person exercises, typically based on voting rights percentage, board representation percentage, or other control metrics                               |
| Know Your Customer (KYC)             | Due diligence process for verifying customer identity and assessing risk in financial relationships                                                                                                      |
| Know Your Supplier (KYS)             | Due diligence process for verifying supplier credentials, integrity, and risk exposure                                                                                                                   |
| Politically Exposed Person (PEP)     | Individual entrusted with prominent public functions, posing higher risk for corruption or bribery                                                                                                       |
| EU Company Certificate (EUCC)        | Attestation establishing the legal existence and identity of a legal entity within the EU                                                                                                                |
| Evidence                           | Supporting documentation substantiating the control structure calculation (e.g., governance chart, shareholder agreement, articles of association, trust deed)                                           |

---

## 2 Attestation attributes and metadata

The Control Attestation is designed to provide a complete, verifiable representation of an
entity's control structure in a standardized digital format. This attestation supports
transparency, compliance, and risk management by enabling automated verification of effective
control across complex, multi-tiered corporate structures where control may be exercised through
diverse mechanisms beyond simple shareholding.

### 2.1 Introduction
//TODO Merge later -> extension for legal arrangements 
The Control follows a hierarchical structure:
```
Controller[1..n]
├── type (M) NP = natural person | LE = legal entity
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
└── control[]
│ ├── legal_identifier (M) identifier of the control entity
│ ├── type (M) direct | indirect
│ ├── voting_rights (M) % | null
│ ├── mechanism [String] (M) one or many of values [board | veto | contractual | nominee | profit distribution]
│ ├── legal_arrangement (M) identifier 
│ ├── place of administration (O) (in case of different != residence )
└── Evidence [1..n] (at least one piece of supporting evidence required)
```

*(M) = Mandatory   (O) = Optional*

*Explanation:*

- The attestation SHALL contain at least one `NaturalPerson` controller to
  comply with AML requirements that mandate identification of natural persons
  who ultimately control the entity.
- The attestation MAY contain zero or more `LegalPerson` entries representing
  intermediate legal entities in the control chain.
- For each `NaturalPerson` controller:
  - It SHALL include `first_name`, `surname`, and `date_of_birth`.
  - It SHALL include a mandatory `address`.
  - It SHALL include at least one `control[]` record detailing the control
    interest.
- For each `LegalPerson` controller:
  - It SHALL include `legal_name`, `legal_form`, and at least one `identifier`
    (EUID, LEI, or TAX).
  - It SHALL include a mandatory `address`.
  - It SHALL include at least one `control[]` record detailing the control
    interest.
- The attestation SHALL include at least one `Evidence` entry substantiating
  the control calculation. Multiple evidence entries MAY be included for complex
  structures. Evidence MAY be provided as a URI reference or as an embedded
  base64-encoded document.

**Attribute Overview**

| **Data Identifier**        | **Semantic Reference** | **Definition**                                                                            | **Data Type** |
|----------------------------|------------------------|-------------------------------------------------------------------------------------------|---------------|
| Natural Person attributes  | —                      | Identification and personal details of natural persons with control interests             | Object        |
| Legal Person attributes    | —                      | Identification and legal details of legal entities with control interests                 | Object        |
| Address attributes         | —                      | Mandatory address for natural person (residence) or legal person (registered)             | Object        |
| Control attributes         | —                      | Quantitative control data (voting rights percentage) and control mechanism classification | Object        |
| Evidence attributes        | —                      | References to supporting documentation substantiating the control structure               | Object        |

**Attestation Classification:**

This attestation type is classified as:
- **`EAA`** within the EUBW Wallet ecosystem, as it is typically self-issued by
  the legal entity subject to the control disclosure (i.e., the entity issues an
  attestation about its own control structure).

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

**Control Mandatory Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                                                                        | **Data type**            |
|---------------------|------------------------|-------------------------------------------------------------------------------------------------------|--------------------------|
| legal_identifier    | --                     | Identifier of the owned entity                                                                        | String                   |
| type                | --                     | Type of ownership: direct or indirect                                                                 | String (direct/indirect) |
| voting_rights       | —                      | The percentage of voting rights held (0–100), or `null` where voting rights are not applicable        | Decimal \| null          |
| mechanism           | —                      | The mechanism(s) through which control is exercised — SHALL use one or more values from Section 2.8.1 | Array of Strings         |

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
| evidence_date         | --                     | The date when the evidence document was created or last updated (ISO 8601)                                                                         | Date (YYYY-MM-DD)            |

### 2.4 Conditional attributes

No conditional attributes are defined for this attestation type. All attributes
are either mandatory or optional as specified above.

### 2.5 Mandatory metadata

| **Data Identifier**        | **Definition**                                                                                                                    | **Data type** |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------|---------------|
| issuance_date              | The date and time when the attestation was issued (ISO 8601)                                                                      | Date (YYYY-MM-DD)      |
| expiry_date                | The date and time when the attestation expires (ISO 8601)                                                                         | Date (YYYY-MM-DD)      |
| issuing_entity             | The identifier of the legal entity that issued the attestation (typically the subject entity itself for self-issued attestations) | String        |
| attestation_legal_category | Indicates the legal category of this attestation ("EAA")                                                                          | String        |
| Version Control Tool (vct)                        | A URI or other collision-resistant identifier that defines the type of the SD-JWT Verifiable Credential                                                            | String          |

### 2.6 Optional metadata

| **Data Identifier** | **Definition**                                                             | **Data type** |
|---------------------|----------------------------------------------------------------------------|---------------|
| trust_anchor_url    | URL where the trust anchor for verifying this attestation can be retrieved | URI           |
| schema_version      | Version of the schema used                                                 | String        |

### 2.7 Conditional metadata

No conditional metadata elements are defined for this attestation type.

### 2.8 Value Lists

#### 2.8.1 Control Mechanism Codes

The `mechanism` attribute SHALL use one or more of the following standardised
values, represented as an array to accommodate multiple simultaneous control
mechanisms:

| **Code**            | **Definition**                                                                                                   |
|---------------------|------------------------------------------------------------------------------------------------------------------|
| board               | Control exercised through the right to appoint or remove members of the board of directors or supervisory board  |
| veto                | Control exercised through veto rights over major corporate decisions (e.g., M&A, capital increases, dissolution) |
| contractual         | Control exercised through formal or informal agreements (e.g., shareholders' agreements, management agreements)  |
| nominee             | Control exercised through nominee shareholders, nominee directors, or other nominee arrangements                 |
| profit_distribution | Control exercised through the right to control the distribution of profits                                       |

**Note:** Multiple mechanisms MAY apply to a single controller. For example, a person may exercise control through both `board` AND `contractual`simultaneously. In such cases, the `mechanism` attribute SHALL be encoded as  an array containing all applicable codes.

### 2.9 Integrity Rules

## 3 Attestation encoding

### 3.1 ISO/IEC 18013-5-compliant encoding

ISO/IEC 18013-5 (also called mdoc) is out of scope for this Rulebook, as
offline proximity presentation is not a current requirement for the Control
attestation.

### 3.2 SD-JWT VC-based encoding

The Control attestation uses the SD-JWT VC format to allow for selective
disclosure of control structure attributes.

**Selective Disclosure:** Top-level claims (`controller`, `evidence`) SHALL be
individually selectively disclosable, enabling a legal entity to disclose only
the attributes requested by a Relying Party.

The `.` notation is used to indicate the nesting of attributes.

**Verifiable Credential Type (`vct`):** `eu.we-build.control.1`

#### 3.2.1 Attribute Encoding Table

| **Data Identifier**          | **Attribute Identifier**                     | **Encoding Format**          | **Reference / Notes**                                                                                | **Disclosable** |
|------------------------------|----------------------------------------------|------------------------------|------------------------------------------------------------------------------------------------------|-----------------|
| controller                 | controller                                 | Array [controller]           | Array of controller objects — SHALL contain at least one entry                                       | MUST            |
| type                       | controller[n].type                         | String                       | NP = natural person / LE = legal entity — SHALL be non-empty                                     | MUST            |
| **NaturalPerson**            |                                              |                              |                                                                                                      |                 |
| first_name                 | controller[n].natural_person.first_name    | String                       | First name(s) of the natural person controller — SHALL be non-empty                                  | MUST            |
| surname                    | controller[n].natural_person.surname       | String                       | Surname(s) of the natural person controller — SHALL be non-empty                                     | MUST            |
| date_of_birth              | controller[n].natural_person.date_of_birth | String (ISO 8601 YYYY-MM-DD) | Date of birth of the natural person controller — SHALL be non-empty                                  | MUST            |
| **LegalPerson**              |                                              |                              |                                                                                                      |                 |
| legal_name                 | controller[n].legal_person.legal_name      | String                       | Complete official name of the legal entity controller — SHALL be non-empty                           | MUST            |
| legal_form                 | controller[n].legal_person.legal_form      | String                       | Legal form of the controlling legal entity (e.g., GmbH, AG, Ltd) — SHALL be non-empty                | MUST            |
| identifier                 | controller[n].legal_person.identifier      | String                       | At least one legal entity identifier (euid, lei, or tax) — SHALL be non-empty                        | MUST            |
| **LegalPerson Identifier**   |                                              |                              |                                                                                                      |                 |
| euid                       | controller[n].legal_person.identifier.euid | String                       | European Unique Identifier of the controlling legal entity — optional                                | MAY             |
| lei                        | controller[n].legal_person.identifier.lei  | String (20 characters)       | LEI code of the controlling legal entity per ISO 17442 — optional                                    | MAY             |
| tax                        | controller[n].legal_person.identifier.tax  | String                       | National tax or company registration number — optional                                               | MAY             |
| **Address**                  |                                              |                              |                                                                                                      |                 |
| street                     | controller[n].address.street               | String                       | Street name of the address — SHALL be non-empty                                                      | MUST            |
| house_number               | controller[n].address.house_number         | String                       | House or building number — SHALL be non-empty                                                        | MUST            |
| locality                   | controller[n].address.locality             | String                       | City or locality — SHALL be non-empty                                                                | MUST            |
| region                     | controller[n].address.region               | String                       | State, province, or region — SHALL be non-empty                                                      | MUST            |
| postal_code                | controller[n].address.postal_code          | String                       | Postal or ZIP code — SHALL be non-empty                                                              | MUST            |
| country                    | controller[n].address.country              | String (ISO 3166-1 alpha-2)  | Country code of the address — SHALL be non-empty                                                     | MUST            |
| **Control**                  |                                              |                              |                                                                                                      |                 |
| legal_identifier           | controller[n].control.legal_identifier     | String                       | Identifier of the controlled entity — SHALL be non-empty                                             | MUST            |
| type                       | controller[n].control.type                 | String                       | direct or indirect — SHALL use values from Section 2.8.1                                         | MUST            |
| voting_rights              | controller[n].control.voting_rights        | Decimal (0–100) \| null      | Percentage of voting rights held — SHALL be non-empty or explicitly null                           | MUST            |
| mechanism                  | controller[n].control.mechanism            | Array of Strings             | Control mechanism(s) exercised — SHALL use values from Section 2.8.1 — at least one value required   | MUST            |
| **Evidence**                 |                                              |                              |                                                                                                      |                 |
| evidence_id                | evidence[n].evidence_id                    | String (URI)                 | URI reference to the evidence document — SHALL be non-empty                                          | MUST            |
| evidence_type              | evidence[n].evidence_type                  | String                       | SHALL be "Evidence"                                                                                | MUST            |
| evidence_data              | evidence[n].evidence_data                  | String (base64)              | Base64-encoded evidence document — required if evidence_id is not a publicly accessible URI        | MAY             |
| evidence_confirmation      | evidence[n].evidence_confirmation          | Boolean                      | Confirmation that the evidence document is current and used as the basis for the control calculation | MAY             |
| evidence_date              | evidence[n].evidence_date                  | String (ISO 8601 YYYY-MM-DD) | Date when the evidence document was created or last updated                                          | MAY             |
| **Metadata**                 |                                              |                              |                                                                                                      |                 |
| issuance_date              | iat                                        | Number (Unix timestamp)      | Date and time when the attestation was issued (ISO 8601) — RFC 7519                                  | MUST NOT        |
| expiry_date                | exp                                        | Number (Unix timestamp)      | Date and time when the attestation expires (ISO 8601) — RFC 7519                                     | MUST NOT        |
| issuing_entity             | iss                                        | String (URI or DID)          | Identifier of the entity that issued the attestation — RFC 7519                                      | MUST NOT        |
| attestation_legal_category | attestation_legal_category                 | String                       | SHALL be "EAA" as defined by eIDAS 2                                                               | MUST NOT        |
| vct                        | vct                                        | String                       | URI or other collision-resistant identifier for the credential type                                  | MUST NOT        |
| schema_version             | schema_version                             | String                       | Version of the schema used — optional                                                                | MAY             |
| trust_anchor_url           | trust_anchor_url                           | String (URI)                 | URL where the trust anchor for verifying this attestation can be retrieved — optional                | MAY             |

**Notes:**

- **MUST**: The claim SHALL be selectively disclosable — the holder MAY choose to disclose or
  withhold this claim when presenting the credential to a Relying Party.
- **MUST NOT**: The claim SHALL NOT be selectively disclosable — it is always present in plain
  text in the JWT header/payload and cannot be withheld by the holder, as it is required for
  credential verification and trust establishment.
- `controller` entries are indexed as `[n]` where `n` starts at 0; at least one owner SHALL be
  present, and at least one SHALL be a natural person.
- `control` entries within each owner are indexed as `[m]` where `m` starts at 0; at least
  one ownership record SHALL be present per owner.
- `evidence` entries are indexed as `[n]` where `n` starts at 0; at least one evidence entry
  SHALL be present.
- `iat`, `exp`, and `iss` follow RFC 7519 standard JWT claim naming conventions.

#### 3.2.2 Status Claim

For SD-JWT VC-compliant Controller attestations, the attestation MUST include a `status` claim
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

### 3.2.3 Example Payload
The following is a non-normative example of a Controller SD-JWT VC payload:

```json
{
  "vct": "eu.we-build.control.1",
  "attestation_legal_category": "EAA",
  "issuing_entity": "did:example:company-456",
  
  "controller": [
    {
      "type": "NP",
      "natural_person": {
        "first_name": "Alice",
        "surname": "Smith",
        "date_of_birth": "1975-03-20"
      },
      "address": {
        "street": "Hauptstrasse",
        "house_number": "10",
        "locality": "Berlin",
        "region": "Berlin",
        "postal_code": "10115",
        "country": "DE"
      },
      "control": [
        {
          "legal_identifier": "EUID:DE123456789",
          "type": "direct",
          "voting_rights": 60,
          "mechanism": ["board", "contractual"]
        }
      ]
    },
    {
      "type": "LE",
      "legal_person": {
        "legal_name": "HoldCo GmbH",
        "legal_form": "GmbH",
        "identifier": {
          "euid": "DE987654321",
          "lei": "529900T8BM49AURSDO55",
          "tax": "DE123456789"
        }
      },
      "address": {
        "street": "Berliner Allee",
        "house_number": "5",
        "locality": "Düsseldorf",
        "region": "Nordrhein-Westfalen",
        "postal_code": "40213",
        "country": "DE"
      },
      "control": [
        {
          "legal_identifier": "EUID:DE123456789",
          "type": "indirect",
          "voting_rights": 40,
          "mechanism": ["nominee"]
        }
      ]
    }
  ],
  "evidence": [
    {
      "evidence_id": "https://example.com/docs/governance-chart-2024.pdf",
      "evidence_type": "Evidence",
      "evidence_confirmation": true,
      "evidence_date": "2024-01-15"
    }
  ],
  "status": {
    "type": "status-list",
    "status_list_credential": "https://issuer.example.com/status/control/2025",
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

Sample payloads are provided under `../data-schemas/sd-jwt/sample-data/control-sd-jwt-sample.json`

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
