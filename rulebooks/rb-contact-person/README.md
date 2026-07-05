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

* Contact:
  * [Florin Coptil](mailto:florin.coptil@bosch.com)*

* Feedback:

---

## 1 Introduction

This attestation addresses the following question:

**Who are the designated contact persons within a legal entity and what are their roles and contact details?**

The Contact Person Attestation identifies natural persons acting as designated contacts within a legal entity, enabling automated and trusted exchange of contact person data between organizations in supply chain, procurement, and onboarding processes.

### 1.1 Document scope and purpose

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

### 1.2 Document structure

This Rulebook is structured as follows:

- Chapter 2 describes the Contact Person attestation attributes and metadata in an encoding-independent manner, including the data model.
- Chapter 3 specifies how the attestation attributes and metadata are encoded: Section 3.2  covers SD-JWT VC-based encoding.
- Chapter 4 specifies attestation usage scenarios, Relying Party obligations, and integration  with supplier onboarding and KYS workflows.
- Chapter 5 defines trust anchors and verification mechanisms for issuer authorization.
- Chapter 6 defines revocation mechanisms for the attestation.
- Chapter 7 provides compliance information regarding the EUDI framework and applicable data protection laws.

### 1.3 Keywords

This document uses the capitalised keywords 'SHALL', 'SHOULD' and 'MAY' as specified in
[RFC 2119], i.e. to indicate requirements, recommendations and options specified in this
document.

In addition, 'must' (non-capitalised) is used to indicate an external constraint, i.e. a
requirement that is not mandated by this document, but, for instance, by an external document.
The word 'can' indicates a capability, whereas other words, such as 'will', and 'is' or 'are'
are intended as statements of fact.

### 1.4 Terminology

*Additional terminology specific to this attestation:*

| Term                  | Description                                                                                                                                                      |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Contact Person        | The attestation type defined in this Rulebook, identifying a natural person designated as a contact within a legal entity for specific business functions         |
| Economic Operator     | A legal entity participating in commercial or procurement activities, identified per the European Business Wallet (EBW) framework                                |
| EUCC                  | EU Company Certificate – attestation establishing the legal existence and identity of a legal entity within the EU                                               |
| EBW                   | European Business Wallet – the digital wallet framework for legal entities operating within the EU single market                                                 |
| Role                  | A designated function or responsibility assigned to a contact person within an organization (e.g., sales, finance, quality, logistics)                           |
| Employee Identifier   | An alphanumeric identifier assigned by the employing organization to uniquely identify an employee                                                               |
| KYS                   | Know Your Supplier – due diligence process for verifying supplier credentials, integrity, and risk exposure                                                      |
| Schema.org            | A collaborative, community-based vocabulary for structured data markup on the internet, used here for personal name attributes                                   |
| CPOV                  | Core Public Organisation Vocabulary – a standardized EU vocabulary for describing public organizations and their contact points                                  |
| Organization Ontology | A W3C ontology for describing organizational structures, roles, and memberships                                                                                  |
| RFC 4021              | IETF standard for the registration of mail and MIME header fields, used here as the reference for valid email address format                                     |
| E.164                 | ITU-T international public telecommunication numbering plan, used here as the reference for valid telephone number format                                        |
| ISO 8601              | International standard for date and time representations (e.g., YYYY-MM-DD)                                                                                     |

---

## 2 Attestation attributes and metadata

The Contact Person Attestation is designed to provide a standardized, verifiable representation
of a natural person designated as a contact within a legal entity. This attestation enables
trusted and automated exchange of contact person data between organizations in supply chain,
procurement, and onboarding processes.

### 2.1 Introduction

**Data Model:**
````
├─ legal_person_id (mandatory)
│ └── identifier [String] (M) identifier: euid, lei, tax, ...
├─ contact_persons (1-n)
├─── given_name (mandatory)
├─── family_name (mandatory)
├─── role (mandatory)
├─── employee_identifier (mandatory)
├─── email (mandatory)
└─── telephone (optional)
````

**Explanation:**
- `legal_person_id` links the contact person to their employing legal entity, identified per the European Business Wallet (EBW) framework.
- The `contact_persons` object encapsulates all details for a specific contact, including `given_name`, `family_name`, `role`, `employee_identifier`, and `email` which are mandatory for a valid, actionable contact person record.
- `telephone` is an optional attribute within the contact_persons object and may be provided for direct voice communication.
- The attestation structure allows for one or more contact_persons entries, each being a distinct object.

**Attestation Classification:**

This attestation type is classified as:
- **"EAA"** within the EBW Wallet ecosystem, as it is typically self-issued by the legal entity employing the contact person 

### 2.2 Mandatory attributes

#### 2.2.1 ContactPerson List Attributes

| **Data Identifier**               | **Semantic Reference**                                                                    | **Definition**                                                                                                                          | **Data type** |
|-----------------------------------|-------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|---------------|
| legal_person_id                   | --                                                                                        | EBW Organization Identifier — Identifier of the employing legal entity according to the European Business Wallet (EBW) framework        | String        |
| contact_persons                   | --                                                                                        | Object representing details of an individual contact person. This can be repeated for multiple contacts.                                |        Object |
| legal_person.identifier           | --                                                                                        |                                                                                                                                         | Object        |
| contactperson.given_name          | [givenName – Schema.org Property](https://schema.org/givenName)                           | Given name. In the U.S., the first name of a Person.                                                                                    | String        |
| contactperson.family_name         | [familyName – Schema.org Property](https://schema.org/familyName)                         | Family name. In the U.S., the last name of a Person.                                                                                    | String        |
| contactperson.role                | [The Organization Ontology](https://www.w3.org/TR/vocab-org/)                             | Denotes a role that a Person takes in an organization (e.g., sales, finance, quality, logistics)                                        | String        |
| contactperson.employee_identifier | --                                                                                        | An alphanumeric identifier of the employee assigned by the organization                                                                 | String        |
| contactperson.email               | [Core Public Organisation Vocabulary (CPOV)](https://joinup.ec.europa.eu/collection/cpov) | An electronic address through which the Contact Person can be contacted                                                                 | tstr          |

### 2.3 Optional attributes

**LegalPersonIdentifier Optional Attributes**

| **Data Identifier**           | **Semantic Reference** | **Definition**                              | **Data type** |
|-------------------------------|------------------------|---------------------------------------------|---------------|
| legal_person.identifier.euid  | --                     | EUID per ISO 3166-1 alpha-2                 | String        |
| legal_person.identifier.lei   | --                     | Legal Entity Identifier (LEI) per ISO 17442 | String        |
| legal_person.identifier.tax   | --                     | National company registration number        | String        |
| telephone                     | [Core Public Organisation Vocabulary (CPOV)](https://joinup.ec.europa.eu/collection/cpov) | A telephone number through which the Contact Person can be contacted | O               | tstr                |

### 2.4 Conditional attributes

No conditional attributes are defined for this attestation type. All attributes are either
mandatory or optional as specified above.

### 2.5 Mandatory metadata

| **Data Identifier**         | **Definition**                                                                                                                                                     | **Data type** |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| attestation_legal_category  | Indicates the legal category of this attestation ("EAA")                                                                                                           | String        |

### 2.6 Optional metadata

| **Data Identifier** | **Definition**                                                             | **Data type** |
|---------------------|----------------------------------------------------------------------------|---------------|
| trust_anchor_url    | URL where the trust anchor for verifying this attestation can be retrieved | URI           |
| schema_version      | Version of the schema used                                                 | String        |

### 2.7 Conditional metadata

No conditional metadata elements are defined for this attestation type.

### 2.8 Value Lists

#### 2.8.1 Organization Identifier

The `legal_person_id` attribute SHALL use identifiers from official company registers or
commercial registers, consistent with the European Business Wallet (EBW) framework. Examples
include:

| **Register Type**         | **Example Identifier Format**    |
|---------------------------|----------------------------------|
| EU Company Register       | EUID (e.g., DE-HRB-123456)       |
| VAT Register              | VAT number (e.g., DE123456789)   |
| National Company Register | Country-specific registration ID |

For all other attributes within the Contact Person attestation, no standardized public EU
value lists are currently available.

#### 2.8.2 Role Values

The `role` attribute SHOULD use descriptive role labels aligned with organizational function.
The following non-exhaustive list of example values is provided for guidance:

| **Example Role Value** | **Definition**                                                    |
|------------------------|-------------------------------------------------------------------|
| sales                  | Responsible for sales and commercial relationships                |
| finance                | Responsible for financial matters, invoicing, and payment queries |
| quality                | Responsible for quality assurance and non-conformance handling    |
| logistics              | Responsible for delivery, shipping, and logistics coordination    |
| production             | Responsible for manufacturing and production planning             |
| procurement            | Responsible for purchasing and supplier management                |
| legal                  | Responsible for legal and compliance matters                      |
| technical              | Responsible for technical support and engineering queries         |

Note: Role values are free-text strings in this version of the Rulebook. Standardized role
taxonomies MAY be adopted in future versions.

### 2.9 Integrity Rules

The following integrity rules SHALL be enforced:

- `given_name` SHALL be a non-empty string.
- `family_name` SHALL be a non-empty string.
- `role` SHALL be a non-empty string describing the function of the contact person within the
  organization.
- `employee_identifier` SHALL be a non-empty alphanumeric string assigned by the employing
  organization.
- `email` SHALL be a valid email address conforming to **RFC 4021** (Registration of Mail and
  MIME Header Fields).
- `telephone`, if provided, SHALL conform to **ITU-T E.164** (The international public
  telecommunication numbering plan), including the country code prefix (e.g., +49123456789).
- `legal_person_id` SHALL be a non-empty string uniquely identifying the employing
  organization.
- Each attribute SHALL appear at most once in the attestation.
- The attestation SHALL be issued by the employing organization (self-issued EAA) or by an
  authorized issuer.
- The contact person named in the attestation SHALL be an active employee of the
  `legal_person_id` at the time of issuance.

---

## 3 Attestation encoding

### 3.1 ISO/IEC 18013-5-compliant encoding

ISO/IEC 18013-5 (also called mdoc) is out of scope for this Rulebook, as offline proximity
presentation is not a current requirement for the Contact Person attestation.

### 3.2 SD-JWT VC-based encoding

The Contact Person attestation uses the SD-JWT VC format to allow for selective disclosure of
contact person attributes.

**Selective Disclosure:** Top-level claims (`given_name`, `family_name`, `role`,
`employee_identifier`, `email`, `telephone`) SHALL be individually selectively disclosable,
enabling an organization to disclose only the attributes requested by a Relying Party.

The `.` notation is used to indicate the nesting of attributes.

**Verifiable Credential Type (`vct`):** `vct: eu.we-build:contactperson:1`

#### 3.2.1 Attribute Encoding Table

**ControlNaturalPerson**

| **Data Identifier**         | **Attribute identifier**        | **Encoding format**     | **Reference/Notes**                                                                                                            | **Disclosable**     |
|-----------------------------|---------------------------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------|---------------------|
| legal_person_id             | `legal_person`                  | object                  | Identifier of the employing legal entity per EBW framework (e.g., EUID, VAT number)                                            | MUST                |
| **LegalPersonIdentifier**   |                                 |                         |                                                                                                                                |
| euid                        | `legal_person.identifier.euid`  | String                  | EUID of the  legal entity; optional                                                                                            | MUST                |
| lei                         | `legal_person.identifier.lei`   | String (20 characters)  | LEI code of the legal entity; optional                                                                                         | MUST                |
| tax                         | `legal_person.identifier.tax`   | String                  | National company registration number; optional                                                                                 | MUST                |
| **ContactPersons**          | `contact_persons`               | Array                   | Array of contact person objects. Each object in the array is itself disclosable, and its members are individually disclosable. | MUST (Array itself) |
| given_name                  | `given_name`                    | String                  | Given name of the contact person; [givenName – Schema.org](https://schema.org/givenName)                                       | MUST                |
| family_name                 | `family_name`                   | String                  | Family name of the contact person; [familyName – Schema.org](https://schema.org/familyName)                                    | MUST                |
| role                        | `role`                          | String                  | Role of the contact person within the organization; [Organization Ontology](https://www.w3.org/TR/vocab-org/)                  | MUST                |
| employee_identifier         | `employee_identifier`           | String                  | Alphanumeric employee identifier assigned by the employing organization                                                        | MUST                |
| email                       | `email`                         | String                  | Email address of the contact person; SHALL conform to RFC 4021; [CPOV](https://joinup.ec.europa.eu/collection/cpov)            | MUST                |
| telephone                   | `telephone`                     | String                  | Telephone number; SHALL conform to ITU-T E.164; [CPOV](https://joinup.ec.europa.eu/collection/cpov); optional                  | MUST                |
| **Metadata**                |                                 |                         |                                                                                                                                |                     |
| attestation_legal_category  | `attestation_legal_category`    | String                  | One of `EAA` as defined by eIDAS 2                                                                                             | MUST NOT            |

*Notes:**

- **MUST**: The claim SHALL be selectively disclosable — the holder MAY choose to disclose or
  withhold this claim when presenting the credential to a Relying Party.
- **MUST NOT**: The claim SHALL NOT be selectively disclosable — it is always present in plain
  text in the JWT header/payload and cannot be withheld by the holder, as it is required for
  credential verification and trust establishment.
- `iat`, `exp`, and `iss` follow RFC 7519 standard JWT claim naming conventions.

#### 3.2.2 Status Claim

For SD-JWT VC-compliant Contact Person attestations, the attestation MUST include a `status`
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
    "status_list_credential": "https://issuer.example.com/status/contactperson/2025",
    "status_list_index": 321,
    "status_purpose": "revocation"
  }
}
```

### 3.2.3 Example Payload
The following is a non-normative example of a Contact Person SD-JWT VC payload:

```
{
  "vct": "eu.we-build:contactperson:1",
  "iss": "https://issuer.example.com",
  "iat": 1736935200,
  "exp": 1768471200,
  "issuing_entity": "did:example:webuild-company-456",
  "attestation_legal_category": "EAA",
  "schema_version": "1.0",
  "trust_anchor_url": "https://trust.webuildconsortium.eu/anchors/eidas-tl",
  "legal_identifier":  {
        "euid":"DE-HRB-123456"  
        "tax": "tax21212"
        "lei": "lei1121"      
   },
  "contact_persons": [
    {
      "given_name": "Anna",
      "family_name": "Schmidt",
      "role": "logistics",
      "employee_identifier": "EMP-DE-00789",
      "email": "anna.schmidt@example.com",
      "telephone": "+4915123456789"
    },
    {
      "given_name": "Max",
      "family_name": "Mustermann",
      "role": "finance",
      "employee_identifier": "EMP-DE-00790",
      "email": "max.mustermann@example.com",
      "telephone": "+4915298765432"
    }
  ],
  "status": {
     "type": "status-list",
     "status_list_credential": "https://issuer.example.com/status/contactperson/2025",
     "status_list_index": 321,
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
Sample payloads are provided under ../data-schemas/sd-jwt/sample-data/contact-person-sd-jwt-sample.json

### 3.3 W3C Verifiable Credentials Data Model-based encoding

@TODO — To be discussed: which stakeholders will support this format and which use cases require it.

## 4 Attestation usage
### 4.1. Issuance process ###

### 4.2 Relying Party Obligations
When receiving and processing an attestation, the Relying Party SHALL perform the following verification obligations.
### 4.2.1 – 4.2.8 Base Verification Process
The Relying Party SHALL perform the base attestation verification process as defined in the Base Verification specification:
https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-base/verifier-base-verification.md
### 4.2.9 Validate Integrity Rules
Validation of integrity and policy rules will be specified in a future version of this Rulebook.

## 5 Trust anchors
This chapter will be completed in a future version of this Rulebook.

## 6 Revocation
This chapter will be completed in a future version of this Rulebook.

## 7 References
This chapter will be completed in a future version of this Rulebook.

## 8 References
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
