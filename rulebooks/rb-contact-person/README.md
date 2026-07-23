# Attestation Rulebook for attestations of type Contact Person

* Author(s):
  * [Florin Coptil, Robert Bosch GmbH]
  * [Dominic Hurni, SBB]
* Previous Authors
  *
* Reviewer(s):
  * [Werner Folkendt, Robert Bosch GmbH]
  * [Stephan-A Fuchs, Deutsche Bank]

| Version | Date       | Description                                                     |
|---------|------------|-----------------------------------------------------------------|
| 0.1     | 01.05.2026 | Initial draft based on the WeBuild design attestations meetings |
| 0.6     | 23.06.2026 | Review in regard to verifier perspective                        |
| 0.8     | 29.06.2026 | Review format and cleanup                                       |
| 0.9     | 14.07.2026 | Review attributes names and cardinality                         |

* Contact:
  * [Florin Coptil](mailto:florin.coptil@bosch.com)*

* Feedback:

## 1 Introduction

This attestation addresses the following question:

**Who are the designated contact persons within a legal entity and what are their roles and contact details?**

The Contact Person Attestation identifies natural persons acting as designated contacts within a legal entity, enabling automated and trusted exchange of contact person data between organizations in supply chain, procurement, and onboarding processes.

### 1.1 Document Scope and Purpose

Cross-company communication is daily business in supply management. To know the correct and
valid contact persons for different issues (e.g., finance, product, quality, logistics) is
crucial to conduct efficient business in the onboarding, pre-contracting, or contracting phase.
In the onboarding process, a minimum of one contact person is required.

**Use Cases:**

*Relying Party:*
- Logistics employees have instant access to valid logistics contact person data. For example,
  in the event of a wrongly delivered battery cell, an employee contacts the responsible sales
  representative by email or phone.
- The Relying Party Wallet validates the revocation status of contact person data. Workflows
  into internal systems (e.g., master data management) follow automatically. Administrative
  employees receive a notification if a contact person is no longer valid.

*Holder:*
- An administrative employee receives a request from a procurer to provide contact persons for
  sales, production, finance, and quality for a specific product (e.g., battery cell). The
  holder company has issued Contact Person attestations for all its employees into its Company
  Wallet. The system selects the fitting employee to answer the request (e.g., a Key Account
  Manager as the battery cell sales contact person).
- The Holder is responsible for the lifecycle of the attestation, including revocation and
  role changes.

The added value of the Contact Person attestation for organizations is to automate the
onboarding and maintenance process of contact person data, increasing data accuracy and
enabling fast and secure business interactions.

This attestation flows only between organizations where a business relationship exists.

**Design Decisions**

This Contact Person Attestation Rulebook is based on:
- EU Company Certificate (EUCC) / European Business Wallet (EBW) framework as the foundational
  legal identity layer for the employing organization
- Schema.org vocabulary for personal name attributes
- Core Public Organisation Vocabulary (CPOV) for contact point attributes
- The Organization Ontology for role classification
- RFC 4021 for email address formatting
- ITU-T E.164 for telephone number formatting

### 1.2 Document Structure
This Rulebook is structured as follows:

- Chapter 2 describes the Contact Person attestation attributes and metadata in an encoding-independent manner, including the data model.
- Chapter 3 specifies how the attestation attributes and metadata are encoded: Section 3.2  covers SD-JWT VC-based encoding.
- Chapter 4 specifies attestation usage scenarios, Relying Party obligations, and integration  with supplier onboarding and KYS workflows.
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

| Term                   | Description                                                                                                                                               |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Contact Person         | The attestation type defined in this Rulebook, identifying a natural person designated as a contact within a legal entity for specific business functions |
| Economic Operator      | A legal entity participating in commercial or procurement activities, identified per the European Business Wallet (EBW) framework                         |
| EUCC                   | EU Company Certificate – attestation establishing the legal existence and identity of a legal entity within the EU                                        |
| EBW                    | European Business Wallet – the digital wallet framework for legal entities operating within the EU single market                                          |
| Role                   | A designated function or responsibility assigned to a contact person within an organization (e.g., sales, finance, quality, logistics)                    |
| Employee Identifier    | An alphanumeric identifier assigned by the employing organization to uniquely identify an employee                                                        |
| KYS                    | Know Your Supplier – due diligence process for verifying supplier credentials, integrity, and risk exposure                                               |
| Schema.org             | A collaborative, community-based vocabulary for structured data markup on the internet, used here for personal name attributes                            |
| CPOV                   | Core Public Organisation Vocabulary – a standardized EU vocabulary for describing public organizations and their contact points                           |
| Organization Ontology  | A W3C ontology for describing organizational structures, roles, and memberships                                                                           |
| RFC 4021               | IETF standard for the registration of mail and MIME header fields, used here as the reference for valid email address format                              |
| E.164                  | ITU-T international public telecommunication numbering plan, used here as the reference for valid telephone number format                                 |
| ISO 8601               | International standard for date and time representations (e.g., YYYY-MM-DD)                                                                               |

## 2 Attestation Attributes and Metadata

The Contact Person Attestation is designed to provide a standardized, verifiable representation of a natural person designated as a contact within a legal entity. This attestation enables trusted and automated exchange of contact person data between organizations in supply chain, procurement, and onboarding processes.

### 2.1 Introduction
The data model for the Contact Person Attestation is structured as follows:

*Data Model:**
````
ContactPerson Attestation
├─ legal_entity (M)
│   ├─ identifier  (M)                          // At least one identifier required
│   │   ├─ euid (str) (O)                       // European Unique Identifier
│   │   ├─ lei (str) (O)                        // Legal Entity Identifier per ISO 17442
│   │   ├─ tax (str) (O)                        // National tax or registration number    
│   │   ├─ gln (str) (O)                        // Global Location Number for legal entities — GS1 identifier
│   │   ├─ duns (str) (O)                       // Data Universal Numbering System — Dun & Bradstreet identifier
│   │   ├─ eori (str) (O)                       // Economic Operators Registration and Identification number — EU customs identifier
│   │   ├─ bpnl (str) (O)                       // Business Partner Number Legal entity — Catena-X identifier per ICD 0243
│   │   ├─ siren (str) (O)                      // Système d'Identification du Répertoire des ENtreprises — French company identifier
└── contact_persons [1..n]                      // Array of ContactPerson 
│   ├─  given_name (M)
│   ├─  family_name (M)
│   ├─  role (M)
│   ├─  email (M)
│   ├─  telephone (O)
````
*Note*: M - mandatory / O - optional.

**Explanation:**

- The `legal_entity` object **SHALL** appear exactly once and contains an `identifier` object with at least one official identifier of the company.
- The `Contact_Person` object **SHALL** appear at least once and **MAY** be repeated for each designated contact. Each instance contains the person's name, role, and contact details.

**Attestation Classification:**

This attestation type is classified as:
- **"EAA"** Self-issued by the legal entity as part of its disclosures.

| **Data Identifier** | **Semantic Reference** | **Definition**                                                       | **Data type**    |
|:--------------------|:-----------------------|:---------------------------------------------------------------------|:-----------------|
| `legal_entity`      | —                      | An object containing identifiers for the legal entity.               | Object           |
| `contact_persons`   | —                      | An array of objects, each representing an individual contact person. | Array of Objects |

### 2.2 Mandatory Attributes

**LegalEntity Attributes**
This object is defined once per attestation.

| **Data Identifier** | **Semantic Reference** | **Definition**                                                                                 | **Data type** |
|:--------------------|:-----------------------|:-----------------------------------------------------------------------------------------------|:--------------|
| `identifier`        | —                      | A structured object of legal entity identifiers; at least one sub-field **SHALL** be provided. | Object        |

**ContactPerson Attributes**
This object is defined for each person represented in the Contact Person Attestation.

| **Data Identifier** | **Semantic Reference**                                                                    | **Definition**                                         | **Data type** |
|:--------------------|:------------------------------------------------------------------------------------------|:-------------------------------------------------------|:--------------|
| `given_name`        | [givenName – Schema.org](https://schema.org/givenName)                                    | The given name (first name) of the contact person.     | String        |
| `family_name`       | [familyName – Schema.org](https://schema.org/familyName)                                  | The family name (last name) of the contact person.     | String        |
| `role`              | [The Organization Ontology](https://www.w3.org/TR/vocab-org/)                             | The designated function or role of the contact person. | String        |
| `email`             | [Core Public Organisation Vocabulary (CPOV)](https://joinup.ec.europa.eu/collection/cpov) | The email address of the contact person.               | String        |

### 2.3 Optional Attributes

**LegalEntity Identifier Optional Attributes**
At least one of the following sub-fields **SHALL** be provided within the `legal_entity.identifier` object.

| **Data Identifier** | **Semantic Reference**  | **Definition**                                                              | **Data type** |
|:--------------------|:------------------------|:----------------------------------------------------------------------------|:--------------|
| `euid`              | —                       | European Unique Identifier per ISO 3166-1 alpha-2.                          | String        |
| `lei`               | —                       | Legal Entity Identifier (LEI) per ISO 17442.                                | String        |
| `tax`               | —                       | National tax or company registration number.                                | String        |
| `gln`               | —                       | Global Location Number for legal entities (GS1 identifier).                 | String        |
| `duns`              | —                       | Data Universal Numbering System (Dun & Bradstreet identifier).              | String        |
| `eori`              | —                       | Economic Operators Registration and Identification number (EU customs).     | String        |
| `bpnl`              | —                       | Business Partner Number Legal entity (Catena-X identifier).                 | String        |
| `siren`             | —                       | Système d'Identification du Répertoire des ENtreprises (French identifier). | String        |

**ContactPerson Optional Attributes**

| **Data Identifier** | **Semantic Reference**                                                                    | **Definition**                              | **Data type** |
|:--------------------|:------------------------------------------------------------------------------------------|:--------------------------------------------|:--------------|
| `telephone`         | [Core Public Organisation Vocabulary (CPOV)](https://joinup.ec.europa.eu/collection/cpov) | The telephone number of the contact person. | String        |

### 2.4 Conditional Attributes
No conditional attributes are defined for this attestation type.

### 2.5 Mandatory Metadata

| **Data Identifier**          | **Definition**                                           | **Data type** |
|:-----------------------------|:---------------------------------------------------------|:--------------|
| `attestation_legal_category` | Indicates the legal category of the Attestation ("EAA"). | String        |
| `cnf`                        | Cryptographic Key Binding to prove holder possession.    | Object        |

*Note: Standard JWT claims (`iss`, `iat`, `exp`) are also mandatory.*

### 2.6 Optional Metadata

| **Data Identifier**   | **Definition**                                                              | **Data type**  |
|:----------------------|:----------------------------------------------------------------------------|:---------------|
| `trust_anchor_url`    | URL where the trust anchor for verifying this attestation can be retrieved. | URI            |
| `schema_version`      | Version of the schema used for this attestation.                            | String         |

### 2.7 Conditional metadata
No conditional metadata elements are defined for this attestation type.

### 2.8 Value Lists

#### 2.8.1 Role Values
The `role` attribute SHOULD use descriptive role labels aligned with organizational functions. The following non-exhaustive list is provided for guidance:

| **Example Role Value**   | **Definition**                                              |
|:-------------------------|:------------------------------------------------------------|
| `sales`                  | Responsible for sales and commercial relationships.         |
| `finance`                | Responsible for financial matters, invoicing, and payments. |
| `quality`                | Responsible for quality assurance and non-conformance.      |
| `logistics`              | Responsible for delivery, shipping, and coordination.       |
| `procurement`            | Responsible for purchasing and supplier management.         |
| `legal`                  | Responsible for legal and compliance matters.               |

### 2.9 Integrity Rules
The following integrity rules **SHALL** be enforced:
- The `legal_entity.identifier` object **SHALL** contain at least one non-empty identifier sub-field.
- The `contact_persons` array **SHALL** contain at least one entry.
- Each `contact_person` entry **SHALL** contain a non-empty `given_name`, `family_name`, `role`, and `email`.
- `email` **SHALL** be a valid email address conforming to **RFC 4021**.
- `telephone`, if provided, **SHALL** conform to **ITU-T E.164**.

## 3 Attestation Encoding

### 3.1 ISO/IEC 18013-5-compliant encoding
ISO/IEC 18013-5 is out of scope for this Rulebook.

### 3.2 SD-JWT VC-based encoding
The Contact Person Attestation uses the SD-JWT VC format to allow for selective disclosure of contact attributes.

**Verifiable Credential Type (`vct`):** `eu.we-build:contactperson:1`

#### 3.2.1 Attribute Encoding Table

| **Data Identifier**          | **Attribute Identifier**                        | **Encoding Format**     | **Reference/Notes**                                                                            | **Disclosable** |
|:-----------------------------|:------------------------------------------------|:------------------------|:-----------------------------------------------------------------------------------------------|:----------------|
| **Legal Entity**             | `legal_entity`                                  | Object                  | The legal entity that employs the contact persons.                                             | MUST            |
| **Legal Entity Identifier**  |                                                 |                         |                                                                                                |                 |
| euid                         | `legal_entity.identifier.euid`                  | String                  | European Unique Identifier — optional sub-field.                                               | MUST            |
| lei                          | `legal_entity.identifier.lei`                   | String                  | Legal Entity Identifier (LEI) — optional sub-field.                                            | MUST            |
| tax                          | `legal_entity.identifier.tax`                   | String                  | National tax or registration number — optional sub-field.                                      | MUST            |
| gln                          | `legal_entity.identifier.gln`                   | String                  | Global Location Number for legal entities — optional sub-field.                                | MUST            |
| duns                         | `legal_entity.identifier.duns`                  | String                  | Dun & Bradstreet company identifier — optional sub-field.                                      | MUST            |
| eori                         | `legal_entity.identifier.eori`                  | String                  | EU customs identifier — optional sub-field.                                                    | MUST            |
| bpnl                         | `legal_entity.identifier.bpnl`                  | String                  | Catena-X BPNL identifier — optional sub-field.                                                 | MUST            |
| siren                        | `legal_entity.identifier.siren`                 | String                  | French company identifier (SIREN) — optional sub-field.                                        | MUST            |
| **Contact Persons**          | `contact_persons`                               | Array                   | Array of contact person objects; SHALL contain at least one entry.                             | MUST            |
| **ContactPerson Attributes** | `contact_person`                                | Object                  |                                                                                                |                 |
| given_name                   | `given_name`                                    | String                  | Given name of the contact person; [givenName – Schema.org](https://schema.org/givenName).      | MUST            |
| family_name                  | `family_name`                                   | String                  | Family name of the contact person; [familyName – Schema.org](https://schema.org/familyName).   | MUST            |
| role                         | `role`                                          | String                  | Role of the contact person; [Organization Ontology](https://www.w3.org/TR/vocab-org/).         | MUST            |
| email                        | `email`                                         | String                  | Email address; SHALL conform to RFC 4021; [CPOV](https://joinup.ec.europa.eu/collection/cpov). | MUST            |
| telephone                    | `telephone`                                     | String                  | Telephone number; SHALL conform to ITU-T E.164; optional.                                      | MUST            |
| **Metadata**                 |                                                 |                         |                                                                                                |                 |
| issuance_date                | `iat`                                           | Number (Unix timestamp) | Date and time of issuance (RFC 7519).                                                          | MUST NOT        |
| expiry_date                  | `exp`                                           | Number (Unix timestamp) | Date and time of expiration (RFC 7519).                                                        | MUST NOT        |
| issuing_entity               | `iss`                                           | String (URI or DID)     | Identifier of the issuer (RFC 7519).                                                           | MUST NOT        |
| attestation_legal_category   | `attestation_legal_category`                    | String                  | "EAA" or "QEAA" as defined by eIDAS 2.                                                         | MUST NOT        |
| vct                          | `vct`                                           | String                  | The verifiable credential type definition.                                                     | MUST NOT        |
| cnf                          | `cnf`                                           | Object                  | Cryptographic Key Binding.                                                                     | MUST NOT        |
| trust_anchor_url             | `trust_anchor_url`                              | String (URI)            | URL to the trust anchor; optional.                                                             | MAY             |
| schema_version               | `schema_version`                                | String                  | Version of the schema used; optional.                                                          | MAY             |

#### 3.2.2 Status Claim
For SD-JWT VC-compliant Attestations, the attestation MUST include a `status` claim if the technical validity period is greater than 24 hours.

The `status` claim SHALL be a JSON object with the following members:

| **Field**                | **Type**       | **Value / Constraint**                     |
|:-------------------------|:---------------|:-------------------------------------------|
| `type`                   | String         | SHALL be `"status-list"`                   |
| `status_list_credential` | String (URI)   | URI of the Status List Credential document |
| `status_list_index`      | Integer (>= 0) | Zero-based index into the status list      |
| `status_purpose`         | String         | SHALL be `"revocation"`                    |

**Example:**
```json
{
  "status": {
    "type": "status-list",
    "status_list_credential": "https://issuer.example.com/status/contactperson/2026",
    "status_list_index": 321,
    "status_purpose": "revocation"
  }
}
```

#### 3.2.3 Example Payload
Here is a non-normative example payload reflecting the new model:
```json
{
  "vct":"eu.we-build:contactperson:1",
  "iss":"did:example:webuild-company-456",
  "iat":1736935200,
  "exp":1768471200,
  "attestation_legal_category":"EAA",
  "schema_version":"1.0",
  "trust_anchor_url":"https://trust.webuildconsortium.eu/anchors/eidas-tl",
  "legal_entity":{
    "identifier":{
      "euid":"DE-HRB-123456",
      "tax":"DE123456789",
      "lei":"529900T8BM49AURSDO55"
    }
  },
  "contact_persons":[
    {
      "given_name":"Anna",
      "family_name":"Schmidt",
      "role":"logistics",
      "email":"anna.schmidt@example.com",
      "telephone":"+4915123456789"
    },
    {
      "given_name":"Max",
      "family_name":"Mustermann",
      "role":"finance",
      "email":"max.mustermann@example.com"
    }
  ],
  "status":{
    "type":"status-list",
    "status_list_credential":"https://issuer.example.com/status/contactperson/2026",
    "status_list_index":321,
    "status_purpose":"revocation"
  },
  "cnf":{
    "jwk":{
      "kty":"EC",
      "crv":"P-256",
      "x":"TCAER19Zvu3OHF4j4W4vfSVoHIP1ILilDls7vCeGemc",
      "y":"ZxjiWWbZMQGHVWKVQ4hbSIirsVfuecCE6t4jT9F2HZQ"
    }
  }
}
```
Sample payloads are provided under ../data-schemas/sd-jwt/sample-data/contact-person-sd-jwt-sample.json

### 3.3 W3C Verifiable Credentials Data Model-based encoding

## 4 Attestation usage

### 4.1. Issuance process ###
**For EAA (Self-Issued / Standard Issuance)**:
- The issuer (i.e., the legal entity itself) issues the attestation based on the information and supporting documentation available at the time of issuance.
- The issuer is responsible for ensuring that the attested information remains accurate and must immediately revoke the attestation if any change occurs that affects the validity or accuracy of the underlying data.

The Issuer SHALL implement the base issuer obligation as defined in the Issuer Obligation specification:
https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-base/verifier-base-verification.md#41-issuer-obligations

### 4.2 Relying Party Obligations
When receiving and processing an attestation, the Relying Party SHALL perform the following verification obligations.
### 4.2.1 – 4.2.8 Base Verification Process
The Relying Party SHALL perform the base attestation verification process as defined in the Base Verification specification:
https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-base/verifier-base-verification.md
### 4.2.9 Validate Integrity Rules
Validation of integrity and policy rules will be specified in a future version of this Rulebook.

## 5 Trust anchors
This chapter specifies the trust anchor mechanisms used by Relying Parties to establish trust in the issuer of an Electronic Attestation of Attributes (EAA) or a Qualified Electronic Attestation of Attributes (QEAA). The corresponding verification procedures are defined in Sections 4.2.2–4.2.4.

### 5.1 Electronic Attestations of Attributes (EAAs)
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

Authorized Authority: Only the authorized issuer (the self-issuing legal entity for EAA) may modify the status list entry.

### 6.2 Revocation Triggers & Business Rules
- EAA Trigger (Manual Obligation): The self-issuing legal entity is under strict obligation to immediately update or revoke its EAA if its available documents, financial thresholds, or ownership structures change.

Relying Party Action: A revoked or suspended attestation must be treated as invalid for credential-validity purposes by all RPs.
The business interpretation is determined by the Relying Party's internal compliance policies.

## 7 References
| **Item Reference**                     | **Standard name/details**                                                                                                                                                                                                                                                                           |
|----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [European Digital Identity Regulation] | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework                            |
| [HAIP]                                 |Yasuda, K. et al, OpenID4VC High Assurance Interoperability Profile, OpenId Foundation, Version draft-03|
| [IANA-JWT-Claims]                      | IANA JSON Web Token Claims Registry. Available: https://www.iana.org/assignments/jwt/jwt.xhtml|
| [ISO/IEC 18013-5]                      | ISO/IEC 18013-5, Personal identification — ISO-compliant driving licence - Part 5: Mobile driving licence (mDL) application, First edition, 2021-09|
| [ISO 4217]                             | ISO 4217 — Currency codes. Available: https://www.iso.org/iso-4217-currency-codes.html|
| [ISO 8601]                             | ISO 8601 — Date and time format. Available: https://www.iso.org/iso-8601-date-and-time-format.html|
| [OIDC]                                 |Sakimura, N. et al., "OpenID Connect Core 1.0", OpenID Foundation. Available: https://openid.net/specs/openid-connect-core-1_0.html|
| [RFC 2119]                             | RFC 2119 — Key words for use in RFCs to Indicate Requirement Levels, S. Bradner, March 1997|
| [RFC 3339]                             |RFC 3339 — Date and Time on the Internet: Timestamps, G. Klyne et al., July 2002|
| [RFC 8610]                             |RFC 8610 — Concise Data Definition Language (CDDL): A Notational Convention to Express Concise Binary Object Representation (CBOR) and JSON Data Structures, H. Birkholz et al., June 2019|
| [RFC 8943]                             |RFC 8943 — Concise Binary Object Representation (CBOR) Tags for Date, M. Jones et al., November 2020|
| [RFC 8949]                             |RFC 8949 — Concise Binary Object Representation (CBOR), C. Bormann et al., December 2020|
| [SD-JWT VC]                            | SD-JWT-based Verifiable Credentials (SD-JWT VC). Available: https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/, version draft-ietf-oauth-sd-jwt-vc-09|
| [Topic 7]                              |ARF Annex 2 - Topic 7 - Attestation revocation and revocation checking. Available: https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a237-topic-7-attestation-revocation-and-revocation-checking|
