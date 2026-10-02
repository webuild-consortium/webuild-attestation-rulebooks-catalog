# Attestation Rulebook for attestations of type DUNS

Category: non-qualified EAA

* **Author(s):**
    * [Werner Folkendt, Robert Bosch GmbH]
* **Reviewer(s):**
    * [Dominic Hurni, SBB]
    * [Florin Coptil, Robert Bosch GmbH]


* **Contact:**
    * [Werner Folkendt](mailto:werner.folkendt@de.bosch.com) *

| Version | Date | Description |
| --- | --- | --- |
| 1.1 | 2026-10-02 | Restructured onto the generic WE BUILD attestation rulebook template (11 chapters). No normative content removed. |

**Written against:** ARF version 3.0.0, WE BUILD template version 1.0 (generic)

**Feedback:** [GitHub issues](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/issues)

## Table of contents

- [1 Introduction](#1-introduction)
   * [1.1 Document scope and purpose](#11-document-scope-and-purpose)
   * [1.2 Document structure](#12-document-structure)
   * [1.3 Key words](#13-key-words)
   * [1.4 Terminology](#14-terminology)
- [2 Compliance](#2-compliance)
   * [2.1 Compliance statement](#21-compliance-statement)
   * [2.2 Regulatory basis](#22-regulatory-basis)
   * [2.3 Traceability](#23-traceability)
- [3 Attestation attributes](#3-attestation-attributes)
   * [3.1 Introduction](#31-introduction)
   * [3.2 Mandatory attributes](#32-mandatory-attributes)
   * [3.3 Optional attributes](#33-optional-attributes)
   * [3.4 Conditional attributes](#34-conditional-attributes)
- [4 Metadata](#4-metadata)
   * [4.1 Mandatory metadata](#41-mandatory-metadata)
   * [4.2 Optional metadata](#42-optional-metadata)
   * [4.3 Conditional metadata](#43-conditional-metadata)
   * [4.4 Code lists](#44-code-lists)
   * [4.5 Integrity rules](#45-integrity-rules)
- [5 Formats](#5-formats)
- [6 Protocols](#6-protocols)
- [7 Issuance](#7-issuance)
   * [7.1 Binding](#71-binding)
   * [7.2 Issuance Policy](#72-issuance-policy)
   * [7.3 Lifecycle management](#73-lifecycle-management)
   * [7.4 Embedded disclosure policy](#74-embedded-disclosure-policy)
- [8 Revocation](#8-revocation)
- [9 Presentation](#9-presentation)
   * [9.1 Presentation Policy](#91-presentation-policy)
   * [9.2 Presentation modes](#92-presentation-modes)
   * [9.3 Transactional data](#93-transactional-data)
- [10 Trust Framework](#10-trust-framework)
- [11 References](#11-references)


## 1 Introduction

### 1.1 Document scope and purpose

The DUNS Legal Entity Attestation complements the EUCC by providing the DUNS number for a legal entity. With this number an EBW owner can acces the Dun & Bradstreet Database to request additional non-core
identity attributes required for KYS, KYC, supplier onboarding, and risk assessment processes.

### 1.2 Document structure

This Rulebook follows the generic WE BUILD attestation rulebook template. Chapter 2
states how it complies with the ARF and the applicable Regulations. Chapters 3 and 4
define the attributes and metadata in an encoding-independent manner. Chapter 5 states
the formats in which this attestation is issued. Chapters 6 to 9 cover protocols,
issuance, revocation and presentation. Chapter 10 sets out the trust framework, and
chapter 11 lists references.

### 1.3 Key words

This document uses the capitalised key words 'SHALL', 'SHOULD' and 'MAY' as specified
in [RFC 2119], to indicate requirements, recommendations and options.

In addition, 'must' (non-capitalised) indicates an external constraint, a requirement
not mandated by this document but by an external document. The word 'can' indicates a
capability. Other words such as 'will', 'is' and 'are' are statements of fact.

### 1.4 Terminology

*Additional terminology specific to this attestation:*

| Term | Description |
| --- | --- |
| DUNS | Data Universal Numbering System, a nine-digit identifier issued by Dun & Bradstreet to uniquely identify a business entity worldwide |
| EUCC | EU Company Certificate – attestation establishing the legal existence and identity of a legal entity within the EU |
| NAICS | North American Industry Classification System, a standard used to classify business establishments by industry |
| KYS | Know Your Supplier, due diligence process for verifying supplier identity and assessing supply chain risk |
| KYC | Know Your Customer, due diligence process for verifying customer identity |
| ISO 8601 | International standard for date and time representations (e.g., YYYY-MM-DD) |
| ISO 3166-1 | International standard for country codes (two-letter alpha-2 codes) |
| EAA | Electronic Attestation of Attributes as defined by eIDAS 2 |

---

## 2 Compliance

### 2.1 Compliance statement

This Rulebook complies with the applicable requirements of Topic 12, Attestation
Rulebooks, in Annex 2 of the Architecture and Reference Framework, version 3.0.0. It
uses the terminology of Annex 1 of the ARF.


### 2.2 Regulatory basis

This attestation is not a qualified electronic attestation of attributes. The data
described in Annex V points b, c and e of Regulation (EU) 2024/1183 is addressed as
required by EW-DM-12-018 and as recommended by EW-DM-12-020 and EW-DM-12-022. Where a
recommendation is not followed, the reason is stated below.

### 2.3 Traceability

Every applicable requirement mapped to the section that satisfies it. Requirements
marked not applicable carry a stated reason.

| Requirement | Legacy ID | Applies | Satisfied in section | Note |
| --- | --- | --- | --- | --- |
| EW-DM-12-001 | ARB_01a | yes | 5 | W3C VCDM permitted for this category; no encoding defined in this version |
| EW-DM-12-002 | ARB_01b | yes | 5 | SD-JWT VC following the HAIP profile |
| EW-DM-12-003 | ARB_02 | no |  | Proximity presentation is not in scope |
| EW-DM-12-005 | ARB_04 | no |  | No W3C VCDM encoding is defined in this version |
| EW-DM-12-006 | ARB_05 | yes | 5 | Unique vct for this attestation type |
| EW-DM-12-007 | ARB_06 | yes | 3 | Attributes defined independently of encoding |
| EW-DM-12-008 | ARB_06a | no |  | No mdoc encoding is defined in this version |
| EW-DM-12-009 | ARB_06b | yes | 5 | SD-JWT VC claim naming |
| EW-DM-12-010 | ARB_07 | yes | 3 | Attributes reused from the catalogued vocabulary where one exists |
| EW-DM-12-012 | ARB_09 | yes | 3, 4 | Mandatory, optional and conditional stated per attribute |
| EW-DM-12-013 | ARB_10 | no |  | No domestic namespace is defined |
| EW-DM-12-014 | ARB_11 | no |  | Annex V and VII point a apply to QEAA and PuB-EAA |
| EW-DM-12-015 | ARB_12 | yes | 4.1 | EAA indication for a non-qualified EAA |
| EW-DM-12-016 / EW-DM-12-017 / EW-DM-12-018 | ARB_13 / ARB_14 / ARB_15 | yes | 2.2, 4.1 | Point b, EW-DM-12-018 for the non-qualified case |
| EW-DM-12-019 / EW-DM-12-020 | ARB_16 / ARB_17 | yes | 2.2 | Point c, recommendation for non-qualified EAA |
| EW-DM-12-021 / EW-DM-12-022 | ARB_18 / ARB_19 | yes | 2.2, 4.2 | Point e, recommendation for non-qualified EAA |
| EW-DM-12-023 / EW-DM-12-024 | ARB_20 / ARB_21 | yes | 4.2, 10 | Trust anchor location and the trust framework |
| EW-DM-12-029 | ARB_25 | yes | 4.1 | Legal category attribute; see the note in section 4.1 |
| EW-DM-12-030 | ARB_26 | yes | 10 | Trust anchor publication for non-qualified EAA |
| EW-DM-12-031 | ARB_27 | no |  | This attestation does not require the Relying Party to verify a PID |
| EW-DM-12-032 | ARB_28 | no |  | cryptographically_bound_to is not used by this attestation |
| EW-DM-12-034 | ARB_30 | yes | 5 | Selective disclosure stated per claim |
| EW-DM-12-035 | ARB_31 | no |  | No Claim Selective Disclosure Metadata document is used |
| EW-DM-12-038 | ARB_34 | yes | 7.1 | Device binding |

## 3 Attestation attributes

Attributes are defined here in an encoding-independent manner (EW-DM-12-007). The
encoding of each attribute is given in chapter 5.

### 3.1 Introduction

The DUNS Legal Entity Attestation provides a standardized, verifiable representation of a legal entity DUNS number, name, legal form and main adress information.

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
- **"EAA"** self-issued by the legal entity as part of its disclosures or authorized competent body that can independently attest the company information (e.g., based on official Dun & Bradstreet registry data).

**VC Type:** `vct: eu.we-build:duns:1`

#### 1 Introduction

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

#### 3.2.3 Example Payload
The following is a non-normative example of a DUNS SD-JWT VC payload:
```
{
  "vct": "eu.we-build:duns:1",
  "iss": "did:example:duns-issuer-001",
  "iat": 1736935200,
  "exp": 1768471200,
  "attestation_legal_category": "EAA",
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

#### 4.2.1 – 4.2.8 Base Verification Process
The Relying Party SHALL perform the base attestation verification process as defined in the
Base Verification specification:
https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-base/verifier-base-verification.md#42-relying-party-obligations

#### 4.2.9 Validate Integrity Rules
Validation of integrity and policy rules will be specified in a future version of this Rulebook.

### 3.2 Mandatory attributes

**DUNS Attestation Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| `duns_number` | [identifier](http://w3id.org/ebwv#identifier) | Nine-digit unique identifier assigned by Dun & Bradstreet. | tstr |
| `legal_entity` | [businessEntity](http://w3id.org/ebwv#businessEntity).[Company](http://w3id.org/ebwv#Company) | An object encapsulating the legal identity of the entity. | Object |

**Nested Mandatory Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| `legal_entity.legal_name` | [legalName](http://w3id.org/ebwv#legalName) | The registered legal name of the entity. | tstr |
| `legal_entity.legal_form` | [legalForm](http://w3id.org/ebwv#legalForm) | The legal form of the entity (e.g., GmbH, AG, Ltd.). | tstr |
| `legal_entity.address` | [registeredAddress](http://w3id.org/ebwv#registeredAddress) | The official registered address of the entity. | Address Object |

### 3.3 Optional attributes

**Address Optional Attributes**
The following sub-fields within the `legal_entity.address` object are optional.

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| `street` | [thoroughfare](http://w3id.org/ebwv#thoroughfare) | Street name of the registered address. | tstr |
| `nr` | [locatorDesignator](http://w3id.org/ebwv#locatorDesignator) | Street or building number of the registered address. | tstr |
| `postal_code` | [postCode](http://w3id.org/ebwv#postCode) | Postal or ZIP code of the registered address. | tstr |
| `city` | [postName](http://w3id.org/ebwv#postName) | City or municipality of the registered address. | tstr |
| `country` | [adminUnitL1](http://w3id.org/ebwv#adminUnitL1) | Country of the registered address (ISO 3166-1 alpha-2). | tstr |

### 3.4 Conditional attributes

No conditional attributes are defined for this attestation type.

## 4 Metadata

Metadata describes the attestation rather than its subject.

### 4.1 Mandatory metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| `attestation_legal_category` | [attestationLegalCategory](http://w3id.org/ebwv#attestationLegalCategory) | Indicates the legal category of the Attestation ("EAA"). | String |
| `cnf` | N/A | Cryptographic Key Binding to prove holder possession. | Object |

*Note: Standard JWT claims (`iss`, `iat`, `exp`) are also mandatory.*

**Legal category.** This Rulebook retains the `attestation_legal_category` attribute.
Section 4.1 of the generic template replaces it with the `category` attribute of
[ETSI TS 119 472-1], whose value for this category is `eaa:eu:non-qualified`.
EW-DM-12-029, legacy ARB_25, of ARF version 3.0.0 is a SHALL that still requires
`attestation_legal_category`, so the template and the ARF disagree. The attribute is
left as written and the deviation is recorded for the rulebook quality assurance group.

### 4.2 Optional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| `trust_anchor_url` | [cred:termsOfUse](https://www.w3.org/2018/credentials#termsOfUse) | URL where the trust anchor for verifying this attestation can be retrieved. | URI |
| `schema_version` | N/A | Version of the schema used for this attestation. | String |

### 4.3 Conditional metadata

No conditional metadata elements are defined for this attestation type.

### 4.4 Code lists

#### 2.8.1 Country Codes
The `legal_entity.address.country` attribute, if provided, **SHALL** use a country code as defined by **ISO 3166-1 alpha-2** (e.g., `DE` for Germany, `US` for United States).

### 4.5 Integrity rules

The following integrity rules **SHALL** be enforced:
- `duns_number` **SHALL** be a non-empty nine-digit numeric string.
- The `legal_entity` object **SHALL** be present.
- `legal_entity.legal_name` and `legal_entity.legal_form` **SHALL** be non-empty strings.
- The `legal_entity.address` object **SHALL** be present.
- `legal_entity.address.country`, if provided, **SHALL** conform to **ISO 3166-1 alpha-2**.


## 5 Formats


### 5.1 SD-JWT VC-based encoding

The DUNS Legal Entity attestation uses the SD-JWT VC format to allow for selective disclosure.

**Verifiable Credential Type (`vct`):** `eu.we-build:duns:1`

#### 3.2.1 Attribute Encoding Table

| **Data Identifier** | **Attribute Identifier** | **Encoding Format** | **Reference/Notes** | **Disclosable** |
| --- | --- | --- | --- | --- |
| **DUNS Details** |  |  |  |  |
| duns_number | `duns_number` | String | Nine-digit DUNS identifier. | MUST |
| **Legal Entity** | `legal_entity` | Object | Object encapsulating legal identity. | MUST |
| legal_name | `legal_entity.legal_name` | String | Registered legal name of the entity. | MUST |
| legal_form | `legal_entity.legal_form` | String | Legal form of the entity. | MUST |
| **Address** | `legal_entity.address` | Object | The official registered address. | MUST |
| street | `legal_entity.address.street` | String | Street name; optional. | MUST |
| nr | `legal_entity.address.nr` | String | Street or building number; optional. | MUST |
| postal_code | `legal_entity.address.postal_code` | String | Postal or ZIP code; optional. | MUST |
| city | `legal_entity.address.city` | String | City or municipality; optional. | MUST |
| country | `legal_entity.address.country` | String (ISO 3166-1 alpha-2) | Country of address; optional. | MUST |
| **Metadata** |  |  |  |  |
| issuance_date | `iat` | Number (Unix timestamp) | Issuance timestamp. | MUST NOT |
| expiry_date | `exp` | Number (Unix timestamp) | Expiration timestamp. | MUST NOT |
| issuing_entity | `iss` | String (URI or DID) | Identifier of the issuer. | MUST NOT |
| attestation_legal_category | `attestation_legal_category` | String | "EAA". | MUST NOT |
| vct | `vct` | String | The vct definition. | MUST NOT |
| cnf | `cnf` | Object | Cryptographic Key Binding. | MUST NOT |
| trust_anchor_url | `trust_anchor_url` | String (URI) | Optional URL to the trust anchor. | MAY |
| schema_version | `schema_version` | String | Optional version of the schema. | MAY |

#### 3.2.2 Status Claim
For SD-JWT VC-compliant Attestations, the attestation MUST include a `status` claim if the technical validity period is greater than 24 hours.

The `status` claim SHALL be a JSON object with the following members:

| **Field** | **Type** | **Value / Constraint** |
| --- | --- | --- |
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

### 5.2 ISO/IEC 18013-5-compliant encoding

ISO/IEC 18013-5 is out of scope for this Rulebook.

### 5.3 W3C Verifiable Credentials Data Model-based encoding


## 6 Protocols

This attestation is issued using OpenID for Verifiable Credential Issuance
[OpenID4VCI] and presented using OpenID for Verifiable Presentations [OpenID4VP], both
as profiled by [HAIP].

## 7 Issuance

### 7.1 Binding

| Field | Value | Source |
| --- | --- | --- |
| Device-bound | MAY | EW-DM-12-038 |
| Cryptographically bound to | none | EW-DM-12-032 |
| Relying Party must also verify a PID | no | EW-DM-12-031 |
| Binding subject | legal person |  |

### 7.2 Issuance Policy


**For EAA (Self-Issued / Standard Issuance)**:
- The issuer (i.e., the legal entity itself) issues the attestation based on the information and supporting documentation available at the time of issuance.
- The issuer is responsible for ensuring that the attested information remains accurate and must immediately revoke the attestation if any change occurs that affects the validity or accuracy of the underlying data.

The Issuer SHALL implement the base issuer obligation as defined in the Issuer Obligation specification:
https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-base/verifier-base-verification.md#41-issuer-obligations

### 7.3 Lifecycle management

The issuer sets the validity period of the attestation and reissues it when the
underlying facts change, revoking the superseded attestation as described in chapter 8.

### 7.4 Embedded disclosure policy

This attestation defines no embedded disclosure policy.

## 8 Revocation

An attestation SHALL remain valid only while its underlying information is accurate, complete, and legally effective.

#### 6.1 Revocation Mechanism
- Token Status List: The issuer must maintain an active IETF Token Status List (aligned with the Attestation Status List mechanism specified by the EU Commission).
- Credential Metadata: The metadata status_list must be populated in every issued CompanyInfo attestation, referencing the status list URI and the credential's specific index.

Authorized Authority: Only the authorized issuer (the QTSP/competent body for QEAA, or the self-issuing legal entity for EAA) may modify the status list entry.

#### 6.2 Revocation Triggers & Business Rules
- EAA Trigger (Manual Obligation): The self-issuing legal entity is under strict obligation to immediately update or revoke its EAA if its available documents, financial thresholds, or ownership structures change.

Relying Party Action: A revoked or suspended attestation must be treated as invalid for credential-validity purposes by all RPs.
The business interpretation is determined by the Relying Party's internal compliance policies.

## 9 Presentation

### 9.1 Presentation Policy

To verify and validate a received presentation of an attestation of this type, the
following steps SHALL be performed:

1. verify the signature over the attestation using a trust anchor obtained as
   described in chapter 10;
2. verify that the attestation is within its validity period;
3. check revocation status as described in chapter 8, unless the attestation is
   short-lived, or its remaining lifetime is below the revocation time threshold;
4. verify device binding where section 7.1 records the attestation as device-bound;
5. request only those attributes that are necessary for the stated purpose of the
   transaction, and, where the trust model for this attestation requires Relying Party
   registration, only those attributes it is registered and authorised to request.

Obligations specific to this attestation type, carried over from the previous version
of this Rulebook:

When receiving and processing an attestation, the Relying Party SHALL perform the following verification obligations.

### 9.2 Presentation modes

Remote presentation is in scope. Proximity presentation is in scope only where
chapter 5 records an mdoc encoding.

### 9.3 Transactional data

This Rulebook defines no transactional data.

## 10 Trust Framework

This chapter specifies the trust anchor mechanisms used by Relying Parties to establish trust in the issuer of an Electronic Attestation of Attributes (EAA) . The corresponding verification procedures are defined in Sections 4.2.2–4.2.4.

#### 5.1 Qualified Electronic Attestations of Attributes (QEAAs)
not available.

#### 5.2 Electronic Attestations of Attributes (EAAs)

For EAAs, trust is established through a cryptographic chain anchored in the Electronic Business Wallet Owner Identity Document (EBWOID).
The EBWOID SHALL be included in the header of every EAA. During EBWOID issuance, the EBWOID provider verifies that the public key contained in the EBWOID is owned by the Electronic Business Wallet (EBW) owner.

The Relying Party SHALL verify the EBWOID in accordance with the verification procedure defined in this Rulebook. Upon successful verification, the Relying Party obtains:
- assurance that the EBWOID was issued by an authorized provider and is not self-issued;
- the verified identity of the issuer, including its name and EUID (or another globally unique EBW owner identifier); and
- the public key authorized to verify the EAA signature.

Authorization of the issuer is subsequently determined in accordance with the Relying Party's internal policies. Such authorization MAY be based on locally maintained wallet configuration or on trusted jurisdiction- or domain-specific trust list services that identify issuers authorized for a particular type of EAA

**Trust anchor location**

The attribute or metadata carrying the trust anchor location contains at least the URL
at which a machine-readable version can be found or looked up.

## 11 References

| **Item Reference** | **Standard name/details** |
| --- | --- |
| [European Digital Identity Regulation] | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework |
| [HAIP] | Yasuda, K. et al, OpenID4VC High Assurance Interoperability Profile, OpenId Foundation, Version draft-03 |
| [IANA-JWT-Claims] | IANA JSON Web Token Claims Registry. Available: https://www.iana.org/assignments/jwt/jwt.xhtml |
| [ISO/IEC 18013-5] | ISO/IEC 18013-5, Personal identification, ISO-compliant driving licence - Part 5: Mobile driving licence (mDL) application, First edition, 2021-09 |
| [ISO 4217] | ISO 4217, Currency codes. Available: https://www.iso.org/iso-4217-currency-codes.html |
| [ISO 8601] | ISO 8601, Date and time format. Available: https://www.iso.org/iso-8601-date-and-time-format.html |
| [OIDC] | Sakimura, N. et al., "OpenID Connect Core 1.0", OpenID Foundation. Available: https://openid.net/specs/openid-connect-core-1_0.html |
| [RFC 2119] | RFC 2119, Key words for use in RFCs to Indicate Requirement Levels, S. Bradner, March 1997 |
| [RFC 3339] | RFC 3339, Date and Time on the Internet: Timestamps, G. Klyne et al., July 2002 |
| [RFC 8610] | RFC 8610, Concise Data Definition Language (CDDL): A Notational Convention to Express Concise Binary Object Representation (CBOR) and JSON Data Structures, H. Birkholz et al., June 2019 |
| [RFC 8943] | RFC 8943, Concise Binary Object Representation (CBOR) Tags for Date, M. Jones et al., November 2020 |
| [RFC 8949] | RFC 8949, Concise Binary Object Representation (CBOR), C. Bormann et al., December 2020 |
| [SD-JWT VC] | SD-JWT-based Verifiable Credentials (SD-JWT VC). Available: https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/, version draft-ietf-oauth-sd-jwt-vc-09 |
| [Topic 7] | ARF Annex 2 - Topic 7 - Attestation revocation and revocation checking. Available: https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a237-topic-7-attestation-revocation-and-revocation-checking |
