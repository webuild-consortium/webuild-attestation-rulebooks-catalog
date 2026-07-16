# Attestation Rulebook for attestations of type Employee (Employee Credential)

* Author(s):
    * [Loup, Laurent, SICPA]
* Previous Authors
    *
* Reviewer(s):

| Version | Date       | Description                                                      |
|---------|------------|------------------------------------------------------------------|
| 0.1     | 23.06.2026 | Initial draft based on the WeBuild design attestations meetings  |

* Contact:
    * [Loup, Laurent <laurent.loup@sicpa.com>] *
* Feedback:

## 1 Introduction

This document describes how the European Digital Identity (EUDI) Wallet ecosystem can simplify complex administrative processes for posted workers within the EU. The primary objective is to facilitate the **one-single market vision promoted by the EU-commission**, achieving seamless movement of services and people across Member States.

The Services Directive (Directive 2006/123/EC) strengthens the freedom to provide services within the EU. This directive is crucial for the completion of the internal market, since it has huge potential for delivering benefits to consumers and SMEs. The aim is to create an open single market in services within the EU, while at the same time ensuring the quality of services provided to consumers. According to the Commission communication entitled ‘Europe 2020 – A strategy for smart, sustainable and inclusive growth’, the full implementation of the Services Directive could increase trade in commercial services by 45% and foreign direct investment by 25%, bringing an increase of between 0.5% and 1.5% in GDP. The directive contributes to administrative and regulatory simplification and modernisation.

It is important to note that the European Commission has set ambitious goals for 2024-2029 and beyond. These goals are designed to boost Europe’s competitiveness by creating a faster, simpler, and more united Union. This starts with making business easier and faster across all sectors and tackling the skills and labour gap. Europe’s Single Market should allow services and people to move freely and opening up markets. The focus will be on reducing administrative burdens and simplifying implementation: less red tape and reporting, more trust, better enforcement, faster permitting. They will also address the patchwork of national regulations that makes doing doing business in different EU countries more complicated.

### 1.1 Document scope and purpose
The Employee Credential is a Verifiable Credential (VC) issued by an employer to all its employees to certify that they are part of the company. The only quality given to the employees by this credential is to certify they work for that company in a given point in time. Additional qualities could be provided such as Power of Attorney (PoA) or Signatory Rights (SR) to sign contracts or transactions. The employee credentials are given by employers to their employees to prove that they belong to their company.

### 1.2 Document structure

This Rulebook is structured as follows:

- Chapter 2 describes the Contact Person attestation attributes and metadata in an encoding-independent manner, including the data model.
- Chapter 3 specifies how the attestation attributes and metadata are encoded: Section 3.2  covers SD-JWT VC-based encoding.
- Chapter 4 specifies attestation usage scenarios, Relying Party obligations, and integration  with supplier onboarding and KYS workflows.
- Chapter 5 defines trust anchors and verification mechanisms for issuer authorization.
- Chapter 6 defines revocation mechanisms for the attestation.
- Chapter 7 provides compliance information regarding the EUDI framework and applicable data  protection laws.
- 
### 1.3 Keywords

This document uses the capitalised keywords `SHALL`, `SHOULD` and `MAY` as specified in [RFC 2119], i.e. to indicate requirements, recommendations and options specified in this document.

In addition, `must` (non-capitalised) is used to indicate an external constraint, i.e. a requirement that is not mandated by this document, but, for instance, by an external document. The word `can` indicates a capability, whereas other words, such as `will`, and `is` or `are` are intended as statements of fact.

### 1.4 Terminology

*Additional terminology specific to this attestation:*

| Term                | Description                                                                                                                               |
| :------------------ | :---------------------------------------------------------------------------------------------------------------------------------------- |
| Employee Credential | The attestation type defined in this Rulebook, providing verified employment details of an individual                                     |
| EUCC                | EU Company Certificate – attestation establishing the legal existence and identity of a legal entity within the EU                        |
| ISO 4217            | International standard defining currency codes (e.g., EUR, USD, GBP)                                                                      |
| ISO 8601            | International standard for date and time representations (e.g., YYYY-MM-DD)                                                               |
| PoA                 | Power of Attorney                                                                                                                         |
| SR                  | Signatory Rights                                                                                                                          |
| KYE                 | Know Your Employee - due diligence process for verifying employee identity and assessing risk, especially for posted workers              |

---

## 2 Attestation attributes and metadata

The Employee Credential provides a standardized, verifiable representation of an individual's employment status and details, linking them to their employer.

### 2.1 Introduction


The attestation structure is defined as a structured object:

**Data Model:**
````
Employee
├─ name (M)
├─ surname (M)
├─ birth_date (O)
├─ employee_id (M)
└─ company_info (M)
│   └──euid (M)
│   └──name (M)
└─ employment (Optional)
│   └──start_date (M)
│   └──type (M)
│   └──country (M)
````

**Explanation:**

- `name` is the given name of the employee and is mandatory for identification purposes.
- `surname` is the family name of the employee and is mandatory for identification purposes.
- `birth_date` is an optional attribute providing the date of birth of the employee.
- `employee_id` is a mandatory alphanumeric identifier assigned to the employee by the employing organization.
- `company_info` is a mandatory object that encapsulates the employer's identity, containing:
    - `euid`: the European Unique Identifier of the employing company (mandatory).
    - `name`: the registered name of the employing company (mandatory).
- `employment` is an optional object providing details about the employee's current employment, containing:
    - `start_date`: the date on which the employment started (mandatory if `employment` is present).
    - `type`: the type of employment contract (mandatory if `employment` is present).
    - `country`: the country in which the employee is employed (mandatory if `employment` is present).

**Attestation Classification:**

This attestation type is classified as:
- **"EAA"** within the EBW Wallet ecosystem, as it is typically issued by the legal entity
  employing the individual (i.e., the organization issues an attestation about its own employee
  into the employee's Natural Person Wallet).

**VC Type:** `vct: eu.europa.ec.eudi.employee.1`

### 2.2 Mandatory attributes

#### 2.2.1 Employee Attributes

| **Data Identifier** | **Semantic Reference**                                                                    | **Definition**                                                                                 | **Optionality** | **Encoding format** |
|---------------------|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|-----------------|---------------------|
| name                | [givenName – Schema.org Property](https://schema.org/givenName)                           | Given name of the employee.                                                                    | M               | tstr                |
| surname             | [familyName – Schema.org Property](https://schema.org/familyName)                         | Family name of the employee.                                                                   | M               | tstr                |
| employee_id         | --                                                                                        | An alphanumeric identifier of the employee assigned by the employing organization.             | M               | tstr                |

#### 2.2.2 Company Info Attributes

| **Data Identifier**    | **Semantic Reference** | **Definition**                                                                                  | **Optionality** | **Encoding format** |
|------------------------|------------------------|-------------------------------------------------------------------------------------------------|-----------------|---------------------|
| company_info           | --                     | Object encapsulating the identity of the employing organization.                                | M               | Object              |
| company_info.euid      | --                     | European Unique Identifier (EUID) of the employing legal entity.                                | M               | tstr                |
| company_info.name      | --                     | Registered name of the employing legal entity.                                                  | M               | tstr                |

#### 2.2.3 Employment Attributes (when `employment` object is present)

When the optional `employment` object is included, the following attributes are mandatory
within it:

| **Data Identifier**       | **Semantic Reference** | **Definition**                                                                 | **Optionality**                   | **Encoding format** |
|---------------------------|------------------------|--------------------------------------------------------------------------------|-----------------------------------|---------------------|
| employment.start_date     | --                     | The date on which the employment relationship started (ISO 8601 format).       | M (if `employment` is present)    | tstr (ISO 8601)     |
| employment.type           | --                     | The type of employment (e.g., full-time, part-time, temporary, permanent).     | M (if `employment` is present)    | tstr                |
| employment.country        | --                     | The country in which the employee performs their work (ISO 3166-1 alpha-2).    | M (if `employment` is present)    | tstr                |

### 2.3 Optional attributes

| **Data Identifier** | **Semantic Reference** | **Definition**                                              | **Optionality** | **Encoding format** |
|---------------------|------------------------|-------------------------------------------------------------|-----------------|---------------------|
| birth_date          | --                     | Date of birth of the employee (ISO 8601 format, YYYY-MM-DD) | O               | tstr (ISO 8601)     |
| employment          | --                     | Object providing details about the employee's employment.   | O               | Object              |

### 2.4 Conditional attributes

No conditional attributes are defined for this attestation type beyond those described in
section 2.2.3. When the `employment` object is present, `start_date`, `type`, and `country`
SHALL all be provided.

### 2.5 Mandatory Metadata

| **Data Identifier**        | **Definition**                                                                | **Data type** |
|----------------------------|-------------------------------------------------------------------------------|---------------|
| attestation_legal_category | Indicates the legal category of the AuthorisedSignatories Attestation ("EAA") | String        |
| cnf                        | cryptographic Key Binding                                                                             | String        |

*Note*: Only the additional mandatory attributes are listed; the mandatory attributes defined by the protocol are not specified.

### 2.6 Optional Metadata

| **Data Identifier** | **Definition**                                                             | **Data type** |
|---------------------|----------------------------------------------------------------------------|---------------|
| trust_anchor_url    | URL where the trust anchor for verifying this attestation can be retrieved | URI           |
| schema_version      | Version of the schema used for this attestation                            | String        |

### 2.7 Conditional Metadata

No conditional metadata elements are defined for this attestation type.

### 2.8 Value Lists

#### 2.8.1 Employment Type Values

The `employment.type` attribute SHOULD use descriptive employment type labels. The following
non-exhaustive list of example values is provided for guidance:

| **Example Value** | **Definition**                                                              |
|-------------------|-----------------------------------------------------------------------------|
| full-time         | Employee works the standard number of hours defined by the employer         |
| part-time         | Employee works fewer hours than the standard full-time schedule             |
| temporary         | Employment is for a fixed or limited period of time                         |
| permanent         | Employment is of indefinite duration                                        |
| posted            | Employee is temporarily sent by their employer to work in another EU Member State |
| apprenticeship    | Employee is undergoing a formal apprenticeship or vocational training       |

Note: Employment type values are free-text strings in this version of the Rulebook.
Standardized taxonomies MAY be adopted in future versions.

#### 2.8.2 Country Values

The `employment.country` attribute SHALL use country codes as defined by **ISO 3166-1 alpha-2**
(e.g., `DE` for Germany, `FR` for France, `IT` for Italy).

### 2.9 Integrity Rules

The following integrity rules SHALL be enforced:

- `name` SHALL be a non-empty string representing the given name of the employee.
- `surname` SHALL be a non-empty string representing the family name of the employee.
- `employee_id` SHALL be a non-empty alphanumeric string assigned by the employing organization.
- `birth_date`, if provided, SHALL conform to **ISO 8601** date format (YYYY-MM-DD).
- `company_info.euid` SHALL be a non-empty string conforming to the EUID format as defined by
  the EU Business Registers Interconnection System (BRIS).
- `company_info.name` SHALL be a non-empty string representing the registered name of the
  employing legal entity.
- If the `employment` object is present:
    - `employment.start_date` SHALL conform to **ISO 8601** date format (YYYY-MM-DD).
    - `employment.type` SHALL be a non-empty string.
    - `employment.country` SHALL conform to **ISO 3166-1 alpha-2** (two-letter country code).
- Each attribute SHALL appear at most once in the attestation.
- The attestation SHALL be issued by the employing organization or by an authorized issuer
  acting on behalf of the employer.
- The employee named in the attestation SHALL be an active employee of the issuing organization
  at the time of issuance.

---

## 3 Attestation Encoding

### 3.1 ISO/IEC 18013-5-Compliant Encoding

ISO/IEC 18013-5 (also called mdoc) is out of scope for this Rulebook, as offline proximity
presentation is not a current requirement for the Employee Credential attestation.

### 3.2 SD-JWT VC-Based Encoding

The Employee Credential attestation uses the SD-JWT VC format to allow for selective
disclosure of employee attributes.

**Selective Disclosure:** All claims (`name`, `surname`, `birth_date`, `employee_id`,
`company_info`, `employment`) SHALL be individually selectively disclosable, enabling an
employee to disclose only the attributes requested by a Relying Party.

The `.` notation is used to indicate the nesting of attributes.

**Verifiable Credential Type (`vct`):** `vct: eu.europa.ec.eudi:employee:1`

#### 3.2.1 Attribute Encoding Table

| **Data Identifier**          | **Attribute Identifier**     | **Encoding format**     | **Reference/Notes**                                                                   | **Disclosable** |
|------------------------------|------------------------------|-------------------------|---------------------------------------------------------------------------------------|-----------------|
| name                         | name                         | String                  | Given name of the employee; [givenName – Schema.org](https://schema.org/givenName)    | MUST            |
| surname                      | surname                      | String                  | Family name of the employee; [familyName – Schema.org](https://schema.org/familyName) | MUST            |
| birth_date                   | birth_date                   | String (ISO 8601)       | Date of birth of the employee; optional                                               | MUST            |
| employee_id                  | employee_id                  | String                  | Alphanumeric employee identifier assigned by the employing organization               | MUST            |
| **CompanyInfo**              | company_info                 | Object                  | Object encapsulating the identity of the employing organization                       | MUST            |
| company_info.euid            | company_info.euid            | String                  | European Unique Identifier (EUID) of the employing legal entity                       | MUST            |
| company_info.name            | company_info.name            | String                  | Registered name of the employing legal entity                                         | MUST            |
| **Employment**               | employment                   | Object                  | Object providing employment details; optional                                         | MUST            |
| employment.start_date        | employment.start_date        | String (ISO 8601)       | Start date of the employment relationship; mandatory if `employment` is present       | MUST            |
| employment.type              | employment.type              | String                  | Type of employment (e.g., full-time, posted); mandatory if `employment` is present    | MUST            |
| employment.country           | employment.country           | String (ISO 3166-1 a-2) | Country of employment; mandatory if `employment` is present                           | MUST            |
| **Metadata**                 |                              |                         |                                                                                       |                 |
| `issuance_date`              | `iat`                        | Number (Unix timestamp) | Date and time when the attestation was issued (ISO 8601); RFC 7519                    | MUST NOT        |
| `expiry_date`                | `exp`                        | Number (Unix timestamp) | Date and time when the attestation expires (ISO 8601); RFC 7519                       | MUST NOT        |
| `issuing_entity`             | `iss`                        | String (URI or DID)     | Identifier of the competent institution that issued the attestation; RFC 7519         | MUST NOT        |
| `attestation_legal_category` | `attestation_legal_category` | String                  | One of "EAA" or "QEAA" as defined by eIDAS 2                                          | MUST NOT        |
| `vct`                        | `vct`                        | String                  | The vct definition                                                                    | MUST NOT        |
| `cnf`                        | `cnf`                        | String                  | Cryptographic Key Binding                                                             | MUST NOT        |
| `schema_version`             | `schema_version`             | String                  | Version of the schema used; optional                                                  | MAY             |
| `trust_anchor_url`           | `trust_anchor_url`           | String (URI)            | URL where the trust anchor for verifying this attestation can be retrieved; optional  | MAY             |

**Notes:**

- **MUST**: The claim SHALL be selectively disclosable — the holder MAY choose to disclose or
  withhold this claim when presenting the credential to a Relying Party.
- **MUST NOT**: The claim SHALL NOT be selectively disclosable — it is always present in plain
  text in the JWT header/payload and cannot be withheld by the holder, as it is required for
  credential verification and trust establishment.
- `iat`, `exp`, and `iss` follow RFC 7519 standard JWT claim naming conventions.

#### 3.2.2 Status Claim

For SD-JWT VC-compliant Control Attestations, the attestation MUST include a `status` claim if
the technical validity period is greater than 24 hours. This claim enables Relying Parties to
determine if a credential has been revoked via a status list mechanism, as specified in SD-JWT VC.

The `status` claim SHALL be a JSON object with the following members:

| **Field**                | **Type**       | **Value / Constraint**                                                     |
|--------------------------|----------------|----------------------------------------------------------------------------|
| `type`                   | String         | SHALL be `"status-list"`                                                   |
| `status_list_credential` | String (URI)   | URI of the Status List Credential document containing the status bitstring |
| `status_list_index`      | Integer (>= 0) | Zero-based index into the status list bitstring for this credential        |
| `status_purpose`         | String         | SHALL be `"revocation"`                                                    |

**Example:**

```json
{
  "status": {
 "type": "status-list",
 "status_list_credential": "https://issuer.example.com/status/employee/2025",
 "status_list_index": 142,
 "status_purpose": "revocation"
  }
}
```
### 3.2.3 Example Payload

The following is a non-normative example of a CompanyInfo SD-JWT VC payload:
```
{
  "vct": "eu.europa.ec.eudi:employee:1",
  "iss": "https://issuer.example.com",
  "iat": 1736935200,
  "exp": 1768471200,
  "issuing_entity": "did:example:company-de-123456",
  "issuing_country": "DE",
  "attestation_legal_category": "EAA",
  "schema_version": "1.0",
  "trust_anchor_url": "https://trust.webuildconsortium.eu/anchors/eidas-tl",
  "name": "Anna",
  "surname": "Schmidt",
  "birth_date": "1990-05-15",
  "employee_id": "EMP-DE-00789",
  "company_info": {
 "euid": "DE-HRB-123456",
 "name": "Example GmbH"
  },
  "employment": {
 "start_date": "2020-03-01",
 "type": "full-time",
 "country": "DE"
  },
  "status": {
 "type": "status-list",
 "status_list_credential": "https://issuer.example.com/status/employee/2025",
 "status_list_index": 142,
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
Sample payloads are provided under ../data-schemas/sd-jwt/sample-data/employee-sd-jwt-sample.json

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
The Relying Party SHALL perform the base attestation verification process as defined in the
Base Verification specification:
https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-base/verifier-base-verification.md#42-relying-party-obligations

### 4.2.9 Validate Integrity Rules
Validation of integrity and policy rules will be specified in a future version of this Rulebook.

## 5 Trust anchors
This chapter specifies the trust anchor mechanisms used by Relying Parties to establish trust in the issuer of an Electronic Attestation of Attributes (EAA) or a Qualified Electronic Attestation of Attributes (QEAA). The corresponding verification procedures are defined in Sections 4.2.2–4.2.4.

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
