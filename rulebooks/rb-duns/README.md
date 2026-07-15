# Attestation Rulebook for attestations of type DUNS Legal Entity Attestation

* **Author(s):**
    * [Werner Folkendt, Robert Bosch GmbH]
* **Reviewer(s):**
    * [Dominic Hurni, SBB]
    * [Florin Coptil, Robert Bosch GmbH]

| Version | Date       | Description                                                    |
|--------|------------|----------------------------------------------------------------|
| 0.1    | 23.06.2026 | Initial draft based on the WeBuild design attestation meetings |
| 0.6    | 29.06.2026 | update layout                                                  |
| 0.8    | 29.06.2026 | Review attributes and type                                     |
| 0.9    | 03.07.2026 | Updates in regard trust and revocation                         |
| 0.91   | 15.07.2026 | Updates after meeting with DUNS                                |
* **Contact:**
    * [Werner Folkendt](mailto:werner.folkendt@de.bosch.com) *

## 1 Introduction

A DUNS Legal Entity Attestation contains the DUNS number (DUNS – Data Universal
Numbering System) provided by Dun & Bradstreet to a legal entity and additional legal entity name and adress information.  A DUNS
number is a unique identifier issued by Dun & Bradstreet  for three types of business entities: a) legal entities b) sites and
c) locations.

The DUNS number is a nine-digit numeric code that uniquely identifies a business
entity worldwide, providing a standardized reference for suppliers, customers, and
regulatory authorities.

In the context of supplier verification and the Know Your Supplier (KYS) process, a
DUNS number serves several critical functions. In several industry branches it is
impossible for a legal entity to do business without providing this number to business
partners.

### 1.1 Document Scope and Purpose

The DUNS Legal Entity Attestation complements the EUCC by providing the DUNS number for a legal entity. With this number an EBW owner can acces the Dun & Bradstreet Database to request additional non-core
identity attributes required for KYS, KYC, supplier onboarding, and risk assessment processes.

### 1.2 Document Structure

This Rulebook is structured as follows:

- Chapter 2 describes the DUNS attestation attributes and metadata in an encoding-independent manner, including the data model.
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

| Term         | Description                                                                                                                          |
|:-------------|:-------------------------------------------------------------------------------------------------------------------------------------|
| DUNS         | Data Universal Numbering System — a nine-digit identifier issued by Dun & Bradstreet to uniquely identify a business entity worldwide |
| EUCC         | EU Company Certificate – attestation establishing the legal existence and identity of a legal entity within the EU                   |
| NAICS        | North American Industry Classification System — a standard used to classify business establishments by industry                     |
| KYS          | Know Your Supplier — due diligence process for verifying supplier identity and assessing supply chain risk                           |
| KYC          | Know Your Customer — due diligence process for verifying customer identity                                                           |
| ISO 8601     | International standard for date and time representations (e.g., YYYY-MM-DD)                                                         |
| ISO 3166-1   | International standard for country codes (two-letter alpha-2 codes)                                                                  |
| EAA          | Electronic Attestation of Attributes as defined by eIDAS 2                                                                           |
| QEAA         | Qualified Electronic Attestation of Attributes as defined by eIDAS 2                                                                 |

---

## 2 Attestation Attributes and Metadata

The DUNS Legal Entity Attestation provides a standardized, verifiable representation of a legal entity DUNS number, name, legal form and main adress information.

### 2.1 Introduction

**Data Model:**

The attestation structure is defined as a structured object with a nested array of financial facts:

```
DUNS
├─ duns_number (tstr)
├─ legal_entity (Object)
│   ├─ legal_name (tstr)
│   └─ legal_form (tstr)
│   └─ address (Address)
│       ├─ [street]
│       ├─ [nr]
│       ├─ [postal_code]
│       ├─ [city]
│       └─ [country]
```
*Note*: M - mandatory / O - optional.

**Explanation:**
- `duns_number` is the mandatory nine-digit unique identifier assigned by Dun & Bradstreet to
  the legal entity.
- `legal_entity` is a mandatory object encapsulating the legal identity of the entity,
  containing:
    - `legal_name`: the registered legal name of the entity (mandatory).
    - `legal_form`: the legal form of the entity (e.g., GmbH, AG, Ltd.) (mandatory).
    - `registered_address`: the official registered address of the entity (mandatory object),
      with all address sub-fields being optional:
        - `street`: street name of the registered address.
        - `nr`: street or building number.
        - `postal_code`: postal or ZIP code.
        - `city`: city or municipality.
        - `country`: country of the registered address (ISO 3166-1 alpha-2).

**Attestation Classification:**

This attestation type MAY be classified as:
- **"EAA"** self-issued by the legal entity as part of its disclosures.
- **"QEAA"** issued by a Qualified Trust Service Provider (QTSP) or authorized competent body that can independently attest the company information (e.g., based on official Dun & Bradstreet registry data).
  
**VC Type:** `vct: eu.we-build:duns:1`

### 2.2 Mandatory Attributes

**DUNS Attestation Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                             | **Data type** |
|:--------------------|:-----------------------|:-----------------------------------------------------------|:--------------|
| `duns_number`       | —                      | Nine-digit unique identifier assigned by Dun & Bradstreet. | tstr          |
| `legal_entity`      | —                      | An object encapsulating the legal identity of the entity.  | Object        |

**Nested Mandatory Attributes**

| **Data Identifier**       | **Semantic Reference** | **Definition**                                       | **Data type**  |
|:--------------------------|:-----------------------|:-----------------------------------------------------|:---------------|
| `legal_entity.legal_name` | —                      | The registered legal name of the entity.             | tstr           |
| `legal_entity.legal_form` | —                      | The legal form of the entity (e.g., GmbH, AG, Ltd.). | tstr           |
| `legal_entity.address`    | —                      | The official registered address of the entity.       | Address Object |


### 2.3 Optional Attributes

**Address Optional Attributes**
The following sub-fields within the `legal_entity.address` object are optional.

| **Data Identifier** | **Semantic Reference** | **Definition**                                          | **Data type** |
|:--------------------|:-----------------------|:--------------------------------------------------------|:--------------|
| `street`            | —                      | Street name of the registered address.                  | tstr          |
| `nr`                | —                      | Street or building number of the registered address.    | tstr          |
| `postal_code`       | —                      | Postal or ZIP code of the registered address.           | tstr          |
| `city`              | —                      | City or municipality of the registered address.         | tstr          |
| `country`           | —                      | Country of the registered address (ISO 3166-1 alpha-2). | tstr          |

### 2.4 Conditional Attributes
No conditional attributes are defined for this attestation type.

### 2.5 Mandatory Metadata

| **Data Identifier**          | **Definition**                                                     | **Data type** |
|:-----------------------------|:-------------------------------------------------------------------|:--------------|
| `attestation_legal_category` | Indicates the legal category of the Attestation ("EAA" or "QEAA"). | String        |
| `cnf`                        | Cryptographic Key Binding to prove holder possession.              | Object        |

*Note: Standard JWT claims (`iss`, `iat`, `exp`) are also mandatory.*

### 2.6 Optional Metadata

| **Data Identifier** | **Definition**                                                              | **Data type** |
|:--------------------|:----------------------------------------------------------------------------|:--------------|
| `trust_anchor_url`  | URL where the trust anchor for verifying this attestation can be retrieved. | URI           |
| `schema_version`    | Version of the schema used for this attestation.                            | String        |

### 2.7 Conditional metadata
No conditional metadata elements are defined for this attestation type.

### 2.8 Value Lists

#### 2.8.1 Country Codes
The `legal_entity.address.country` attribute, if provided, **SHALL** use a country code as defined by **ISO 3166-1 alpha-2** (e.g., `DE` for Germany, `US` for United States).

### 2.9 Integrity Rules
The following integrity rules **SHALL** be enforced:
- `duns_number` **SHALL** be a non-empty nine-digit numeric string.
- The `legal_entity` object **SHALL** be present.
- `legal_entity.legal_name` and `legal_entity.legal_form` **SHALL** be non-empty strings.
- The `legal_entity.address` object **SHALL** be present.
- `legal_entity.address.country`, if provided, **SHALL** conform to **ISO 3166-1 alpha-2**.

## 3 Attestation Encoding

### 3.1 ISO/IEC 18013-5-compliant encoding
ISO/IEC 18013-5 is out of scope for this Rulebook.

### 3.2 SD-JWT VC-based encoding
The DUNS Legal Entity attestation uses the SD-JWT VC format to allow for selective disclosure.

**Verifiable Credential Type (`vct`):** `eu.we-build:duns:1`

#### 3.2.1 Attribute Encoding Table

| **Data Identifier**         | **Attribute Identifier**           | **Encoding Format**         | **Reference/Notes**                  | **Disclosable** |
|:----------------------------|:-----------------------------------|:----------------------------|:-------------------------------------|:----------------|
| **DUNS Details**            |                                    |                             |                                      |                 |
| duns_number                 | `duns_number`                      | String                      | Nine-digit DUNS identifier.          | MUST            |
| **Legal Entity**            | `legal_entity`                     | Object                      | Object encapsulating legal identity. | MUST            |
| legal_name                  | `legal_entity.legal_name`          | String                      | Registered legal name of the entity. | MUST            |
| legal_form                  | `legal_entity.legal_form`          | String                      | Legal form of the entity.            | MUST            |
| **Address**                 | `legal_entity.address`             | Object                      | The official registered address.     | MUST            |
| street                      | `legal_entity.address.street`      | String                      | Street name; optional.               | MUST            |
| nr                          | `legal_entity.address.nr`          | String                      | Street or building number; optional. | MUST            |
| postal_code                 | `legal_entity.address.postal_code` | String                      | Postal or ZIP code; optional.        | MUST            |
| city                        | `legal_entity.address.city`        | String                      | City or municipality; optional.      | MUST            |
| country                     | `legal_entity.address.country`     | String (ISO 3166-1 alpha-2) | Country of address; optional.        | MUST            |
| **Metadata**                |                                    |                             |                                      |                 |
| issuance_date               | `iat`                              | Number (Unix timestamp)     | Issuance timestamp.                  | MUST NOT        |
| expiry_date                 | `exp`                              | Number (Unix timestamp)     | Expiration timestamp.                | MUST NOT        |
| issuing_entity              | `iss`                              | String (URI or DID)         | Identifier of the issuer.            | MUST NOT        |
| attestation_legal_category  | `attestation_legal_category`       | String                      | "EAA" or "QEAA".                     | MUST NOT        |
| vct                         | `vct`                              | String                      | The vct definition.                  | MUST NOT        |
| cnf                         | `cnf`                              | Object                      | Cryptographic Key Binding.           | MUST NOT        |
| trust_anchor_url            | `trust_anchor_url`                 | String (URI)                | Optional URL to the trust anchor.    | MAY             |
| schema_version              | `schema_version`                   | String                      | Optional version of the schema.      | MAY             |

#### 3.2.2 Status Claim
For SD-JWT VC-compliant Attestations, the attestation MUST include a `status` claim if the technical validity period is greater than 24 hours.

The `status` claim SHALL be a JSON object with the following members:

| **Field** | **Type** | **Value / Constraint** |
| :--- | :--- | :--- |
| `type` | String | SHALL be `"status-list"` |
| `status_list_credential` | String (URI) | URI of the Status List Credential document |
| `status_list_index` | Integer (>= 0) | Zero-based index into the status list |
| `status_purpose` | String | SHALL be `"revocation"` |

**Example:**
```json
{
  "status": {
    "type": "status-list",
    "status_list_credential": "https://issuer.example.com/status/duns/2025",
    "status_list_index": 456,
    "status_purpose": "revocation"
  }
}
```

### 3.2.3 Example Payload
The following is a non-normative example of a DUNS SD-JWT VC payload:
```
{
  "vct": "eu.we-build:duns:1",
  "iss": "did:example:duns-issuer-001",
  "iat": 1736935200,
  "exp": 1768471200,
  "attestation_legal_category": "QEAA",
  "duns_number": "123456789",
  "legal_entity": {
    "legal_name": "Example GmbH",
    "legal_form": "GmbH",
    "address": {
      "street": "Musterstraße",
      "nr": "42",
      "postal_code": "70174",
      "city": "Stuttgart",
      "country": "DE"
    }
  },
  "status": {
    "type": "status-list",
    "status_list_credential": "https://issuer.example.com/status/duns/2025",
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
Sample payloads are provided under ../data-schemas/sd-jwt/sample-data/duns-sd-jwt-sample.json

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
