# Attestation Rulebook for attestations of type IBAN Ownership Verification

Category: non-qualified EAA

* Author(s):
  * [Ricky Lamberty, Robert Bosch GmbH]
  * [Stephan Fuchs, Deutsche Bank AG]
* Previous Authors:
* Reviewer(s):
  * [Florin Coptil, Robert Bosch GmbH]
  * [Stefan, Kauhaus, Visa Inc.]
  * [Ivan Faltus, BankID.CZ]
  * [Filip Hladký, BankID.CZ]
  * @Reviewers: Contact Ricky to be added in the Reviewers section if you're missing. 


* Contact:
  * [Ricky Lamberty](mailto:Ricky.Lamberty@bosch.com) 
  * [Stephan Fuchs](mailto:stephan-a.fuchs@db.com) 
* Feedback:

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
   * [5.1 SD-JWT VC-based encoding](#51-sd-jwt-vc-based-encoding)
   * [5.2 ISO/IEC 18013-5-compliant encoding](#52-isoiec-18013-5-compliant-encoding)
   * [5.3 W3C Verifiable Credentials Data Model-based encoding](#53-w3c-verifiable-credentials-data-model-based-encoding)
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

This attestation addresses the following question:

**Is a specific IBAN legally owned by a designated legal entity or natural person, and has this ownership been verified and confirmed by the account-servicing financial institution?**

The IBAN Ownership Verification (IBAN-OV) Attestation provides trusted assurance to third parties that a specific IBAN is legally owned by a designated legal entity or natural person (e.g. acting as a sole trader), enabling structured and fraud-resistant exchange of bank account ownership data for use in KYS, KYC, and payment compliance processes.

### 1.1 Document scope and purpose

The IBAN-OV attestation provides trusted assurance to third parties that a specific IBAN is legally owned by a designated legal entity or natural person. This verified proof of ownership can be used across various business processes (e.g. onboarding process, supporting payment-related triggers) to reduce errors and mitigate fraud risks. This attestation will not be used to initiate or execute any kind of payment.

The IBAN-OV attestation will be provided within the RP registration process (e.g. bank account opening) or upon request from the legal entity or natural person owning the IBAN account. Its purpose is to ensure that, at a later stage, payments for delivered services or sold products can be properly attributed to the verified legal entity or natural person.

Once issued and securely stored in the EBW wallet, the IBAN-OV attestation can be reused for multiple transactions as long as it will not be revoked. This increases operational efficiency while ensuring continued compliance with banking regulations and applicable legal standards.

**Design Decisions**

This IBAN-OV Attestation Rulebook is based on:

- IBAN Attestation Data Rulebook from EWC: https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb003_IBAN_attestation.md
- PSD2 / PSD3 framework as the foundational payment services regulatory layer
- ISO 13616:2020 for IBAN formatting and validation
- ISO 9362:2022 for BIC/SWIFT code formatting
- ISO 4217:2015 for currency codes
- ISO 3166-1 for country codes (Alpha-3)

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
| IBAN-OV | IBAN Ownership Verification (IBAN-OV), the attestation type defined in this Rulebook, providing verified proof that a specific IBAN is owned by a designated legal entity or sole trader |
| ASPSP | Account Servicing Payment Service Provider, the financial institution holding and managing the bank account |
| IBAN | International Bank Account Number, a standardized international numbering system for individual bank accounts, as defined in ISO 13616:2020 |
| BIC/SWIFT | Bank Identifier Code, an international standard for identifying banks and financial institutions globally, as defined in ISO 9362:2022 |
| EUID | European Unique Identifier, the unique identifier assigned to legal entities registered within the EU |
| KYC | Know Your Customer, due diligence process for verifying customer identity and assessing risk in financial relationships |
| KYS | Know Your Supplier, due diligence process for verifying supplier identity and integrity. |
| Legal Person | A legal entity registered in a national or EU company register, identified by an appropriate identifier. For IBAN-OV purposes, the account owner in the legal_person case |
| Sole Trader | A natural person operating a business who is registered in a national register |
| Owner Type | A discriminator attribute within *Account_Ownership* that explicitly identifies whether the account owner is a legal entity or a natural person. |
| ISO 4217:2015 | International standard defining currency codes (e.g., EUR, USD, GBP) |
| ISO 13616-1:2020 | International standard defining the IBAN format and validation rules |
| ISO 9362:2014 | International standard defining the BIC/SWIFT code format |
| ISO 3166-1 | International standard defining country codes (Alpha-3 code) |

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

The IBAN-OV Attestation is a document that provides verified information about the bank account details of the account owner. It ensures that a legal entity (or natural person) can confidentially prove to a third party that this IBAN also belongs to the same legal entity (or natural person). 

**Data Model:**
```
IBAN-OV Attestation
│
├── Bank_Account 				(m)
│ ├── account_name				(m)
│ ├── iban						(m)
│ ├── national_account_number	(o)
│ ├── account_type				(m)
│ └── account_currency			(m)
│
├── Account_Ownership 			(m)
│ ├── owner_type 				(m)
│ ├── owner_name				(m)		(mandatory if legal person, 'entity')
│ ├── legal_person_identifiers	(m)     (array of objects, mandatory if 'entity')
│ │   ├── type					(m)
│ │   └── value					(m)
│ ├── given_name				(m)		(mandatory if natural person, 'person')
│ └── surname					(m)		(mandatory if natural person, 'person')
│
└── Account_Provider			(m)
  ├── provider_name				(m)
  ├── legal_person_identifiers	(m)     (array of objects)
  │   ├── type					(m)
  │   └── value					(m)
  ├── provider_country			(m)
  ├── bic_swift					(m)
  ├── national_bank_code		(o)	
  ├── nace_code					(o)	
  └── clearing_number			(o)
```

**Explanation:**

- `Bank_Account` contains the core details of the account itself, such as IBAN, currency,
  and type.
- `Account_Ownership` identifies the legal owner of the account, including name and an array of flexible company identifiers (e.g., EUID, LEI, TAX) to accommodate global entities.
- `Account_Provider` describes the financial institution that issued the account (also utilizing flexible identifiers) and metadata about the attestation.

This structure effectively separates the **what** (the bank account), the **who** (the bank
account owner) and the **where & how** (the provider & metadata).

**Attestation Classification:**

This attestation type MAY be classified as:

- **"EAA"** when issued by the bank (ASPSP) acting as an authorized issuer within the EUDI  framework according to ETSI 119 478.

### 3.2 Mandatory attributes

**Bank_Account Mandatory Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| account_name | tbd | Name of the account, generated by the bank or customized by the owner. | String |
| iban | tbd | International Bank Account Number, as defined in ISO 13616:2020. | [A-Z]{2}[0-9A-Z]{13,30} |
| account_type | tbd | Nature of the bank account. | String |
| account_currency | tbd | Currency code(s) used for the account, as defined in ISO 4217:2015. | Array (3-digit code(s)), ISO 4217:2015 |

**Account_Ownership Mandatory Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| owner_type | tbd | Discriminator identifying whether the account owner is a legal person or a natural person. | String - enum |
| owner_name | tbd | Legal name of the legal person owning the account. | String |
| legal_person_identifiers | tbd | Array of objects containing unique identification strings of the legal entity owning the account. | Array [Object] |
| legal_person_identifiers[n].type | tbd | Scheme or type of the identifier used (e.g., 'EUID', 'LEI', 'TAX'). | String |
| legal_person_identifiers[n].value | tbd | The actual identifier value. | String |
| given_name | tbd | Given name(s) of the natural person owning the account. | String |
| surname | tbd | Surname / family name of the natural person owning the account. | String |

**Account_Provider Mandatory Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| provider_name | tbd | Name of the financial institution providing the account. | String |
| legal_person_identifiers | tbd | Array of objects containing unique identification strings of the financial institution. | Array [Object] |
| legal_person_identifiers[n].type | tbd | Scheme or type of the identifier used (e.g., 'EUID', 'LEI', 'TAX'). | String |
| legal_person_identifiers[n].value | tbd | The actual identifier value. | String |
| provider_country | tbd | Alpha-3 country code, as defined in ISO 3166-1, of the provider country or territory. | 3-digit code |
| bic_swift | tbd | International code (i.e. BIC or SWIFT code), as defined in ISO 9362, of the financial institution. | String ISO 9362 |

### 3.3 Optional attributes

**Account_Provider Optional Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| national_bank_code | tbd | Country-specific code for internal routing within a specific country's clearing system. | String |
| nace_code | tbd | NACE code for activity specification (e.g. 64.19) of the institution providing the account. | String |
| clearing_number | tbd | Clearing number for identification of the financial institution, used only in some countries. | String |

### 3.4 Conditional attributes

The following conditional attributes are defined for the `Account_Ownership` object. Their presence is mandatory or prohibited depending on the value of `owner_type`:

- `owner_name` and `legal_person_identifiers` SHALL be present if and only if `owner_type` = 'entity'.
- `given_name` and `surname` SHALL be present if and only if `owner_type` = 'person'.
- `given_name` and `surname` SHALL NOT be present when `owner_type` = 'entity'.

This conditional structure is enforced via JSON Schema if/then validation (Draft 2020-12) in the accompanying data schema.

## 4 Metadata

Metadata describes the attestation rather than its subject.

### 4.1 Mandatory metadata

| **Data Identifier** | **Definition** | **Data type** |
| --- | --- | --- |
| iat | The date and time when the verifiable credential was issued (ISO 8601) | DateTime |
| exp | The date and time when the attestation expires (ISO 8601) | DateTime |
| iss | The identifier of the legal entity that issued the attestation (typically the subject entity itself for self-issued attestations) | String |
| attestation_legal_category | Indicates the legal category of this attestation ("EAA") | String |
| vct | A unique identifier (URL or URN) for the credential type, indicating which claims must be present and which can be selectively disclosed | String |
| cnf | Cryptographic key binding element | String |

**Legal category.** This Rulebook retains the `attestation_legal_category` attribute.
Section 4.1 of the generic template replaces it with the `category` attribute of
[ETSI TS 119 472-1], whose value for this category is `eaa:eu:non-qualified`.
EW-DM-12-029, legacy ARB_25, of ARF version 3.0.0 is a SHALL that still requires
`attestation_legal_category`, so the template and the ARF disagree. The attribute is
left as written and the deviation is recorded for the rulebook quality assurance group.

### 4.2 Optional metadata

| **Data Identifier** | **Definition** | **Data type** |
| --- | --- | --- |
| trust_anchor_url | URL where the trust anchor for verifying this attestation can be retrieved | URI |
| schema_version | Version of the schema used | String |

### 4.3 Conditional metadata

No conditional metadata elements are defined for this attestation type.

### 4.4 Code lists

#### 4.4.1 Currency Codes

The `account_currency` attribute SHALL follow ISO 4217:2015 currency codes.

| **Code** | **Definition** |
| --- | --- |
| EUR | Euro |
| USD | United States Dollar |
| GBP | Pound Sterling |
| CHF | Swiss Franc |
| … | … |

#### 4.4.2 Account Type Codes

The `account_type` attribute SHOULD use one of the following standardized values:

| **Example Code** | **Definition** |
| --- | --- |
| CURRENT | Current Account |
| SAVINGS | Savings Account |
| BASIC | Basic Bank Account |
| LOAN | Loan Account |
| OTHER | Other |

#### 4.4.3 Owner Type Codes

| **Example Code** | **Definition** |
| --- | --- |
| person | Natural Person |
| entity | Legal Person/Entity |

### 4.5 Integrity rules

The following integrity rules SHALL be enforced:

- The IBAN-OV attestation SHALL be cryptographically bound and issued exclusively to the   specific Holder wallet that was onboarded by the Issuer (the bank).
- `expiry_date` SHALL be dated after the `issuance_date`.
- `iban` SHALL conform to the ISO 13616:2020 format: [A-Z]{2}[0-9A-Z]{13,30}.
- `bic_swift` SHALL conform to the ISO 9362:2022 format: [A-Z]{6}[A-Z0-9]{2}([A-Z0-9]{3}).
- `provider_country` SHALL be a valid ISO 3166-1 alpha-3 country code.
- `account_currency` SHALL contain at least one valid ISO 4217:2015 currency code.
- `legal_person_identifiers` in Account_Provider SHALL be present, be an array, and contain at least one valid identifier object with `type` and `value` identifying the issuing financial institution.
- If `owner_type` = `entity`, `legal_person_identifiers` in Account_Ownership SHALL be present, be an array, and contain at least one valid identifier object with `type` and `value` identifying the account owner.
- Each attribute SHALL appear at most once in the attestation.
- `owner_type` in Account_Ownership SHALL be present and SHALL contain exactly one of the values `entity` or `person`.
- If `owner_type` = `entity`, `owner_name` SHALL be present and `given_name` and `surname` SHALL NOT be present.
- If `owner_type` = `person`, `given_name` and `surname` SHALL both be present and `owner_name` SHALL NOT be present.
- The attestation SHALL NOT be used to directly initiate or execute payments.


## 5 Formats


### 5.1 SD-JWT VC-based encoding

The IBAN-OV attestation uses the SD-JWT VC format to allow for selective disclosure of account attributes.

**Selective Disclosure:** Top-level claims (`bank_account`, `account_ownership`, `account_provider`) SHALL be individually selectively disclosable, enabling the account holder to disclose only the attributes requested by a Relying Party.

The `.` notation is used to indicate the nesting of attributes.

**Verifiable Credential Type (`vct`):** `vct: eu.we-build:iban-ov.1`

#### 5.1.1 Attribute Encoding Table

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Reference/Notes** | **Disclosable** |
| --- | --- | --- | --- | --- |
| **Bank_Account** |  |  |  |  |
| account_name | bank_account.account_name | String | Name of the account | MUST |
| iban | bank_account.iban | String | ISO 13616:2020 format | MUST |
| account_type | bank_account.account_type | String | Nature of the bank account | MUST |
| account_currency | bank_account.account_currency | Array of Strings | ISO 4217:2015 currency codes | MUST |
| **Account_Ownership** |  |  |  |  |
| owner_type | account_ownership.owner_type | String | Discriminator identifying the owner type. Enum: `entity` \| `person` | MUST |
| owner_name | account_ownership.owner_name | String | Legal name of the legal entity owning the account. Present only if `owner_type = entity` | MUST |
| legal_person_identifiers | account_ownership.legal_person_identifiers | Array [Object] | Array of identifier objects. Present only if `owner_type = entity` | MUST |
| legal_person_identifiers.type | account_ownership.legal_person_identifiers[n].type | String | Scheme of the identifier (e.g., 'EUID', 'LEI', 'TAX') | MUST |
| legal_person_identifiers.value | account_ownership.legal_person_identifiers[n].value | String | Value of the identifier | MUST |
| given_name | account_ownership.given_name | String | Given name(s) of the natural person owning the account. Present only if `owner_type = person` | MUST |
| surname | account_ownership.surname | String | Surname of the natural person owning the account. Present only if `owner_type = person` | MUST |
| **Account_Provider** |  |  |  |  |
| provider_name | account_provider.provider_name | String | Name of the financial institution | MUST |
| legal_person_identifiers | account_provider.legal_person_identifiers | Array [Object] | Array of identifier objects for the provider | MUST |
| legal_person_identifiers.type | account_provider.legal_person_identifiers[n].type | String | Scheme of the identifier (e.g., 'EUID', 'LEI', 'BIC') | MUST |
| legal_person_identifiers.value | account_provider.legal_person_identifiers[n].value | String | Value of the identifier | MUST |
| provider_country | account_provider.provider_country | String | ISO 3166-1 alpha-3 country code | MUST |
| bic_swift | account_provider.bic_swift | String | ISO 9362 BIC/SWIFT format | MUST |
| national_bank_code | account_provider.national_bank_code | String | Country-specific routing code | MUST |
| nace_code | account_provider.nace_code | String | NACE activity code | MUST |
| clearing_number | account_provider.clearing_number | String | Country-specific clearing number | MUST |
| **Metadata** |  |  |  |  |
| issuance_date | iat | Number (Unix timestamp) | ISO 8601, RFC 7519 / Section 2.5 | MUST NOT |
| expiry_date | exp | Number (Unix timestamp) | ISO 8601, RFC 7519 / Section 2.5 | MUST NOT |
| issuing_entity | iss | String | Identifier of the issuing financial institution | MUST NOT |
| attestation_legal_category | attestation_legal_category | String | "EAA" defined by eIDAS 2 | MUST NOT |
| vct | vct | String | A URI or other collision-resistant identifier that defines the type of the SD-JWT Verifiable Credential | MUST |
| schema_version | schema_version | String | Version of the schema used for this attestation | MAY |
| trust_anchor_url | trust_anchor_url | String (URI) | URL where the trust anchor for verifying this attestation can be retrieved | MAY |

**Notes:**

- **MUST**: The claim SHALL be selectively disclosable, the holder MAY choose to disclose or
  withhold this claim when presenting the credential to a Relying Party.
- **MUST NOT**: The claim SHALL NOT be selectively disclosable, it is always present in plain
  text in the JWT header/payload and cannot be withheld by the holder, as it is required for
  credential verification and trust establishment.
- `iat`, `exp`, and `iss` follow RFC 7519 standard JWT claim naming conventions.

#### 5.1.2 Status Claim

For SD-JWT VC-compliant IBAN-OV attestations, the attestation MUST include a `status` claim if
the technical validity period is greater than 24 hours. This claim enables Relying Parties to
determine if a credential has been revoked via a status list mechanism, as specified in SD-JWT VC.

The `status` claim SHALL be a JSON object containing a `status_list` member with the following fields:

- `idx` (integer, >= 0): The zero-based index into the status list bitstring that corresponds to this credential.
- `uri` (string, URI): The URI of the Status List Token that contains the status bitstring for this credential.

This structure follows the Token Status List specification as defined in [draft-ietf-oauth-status-list-21]:
https://datatracker.ietf.org/doc/draft-ietf-oauth-status-list/21/

Example:
```
{
  "status": {
    "status_list": {
      "idx": 456,
      "uri": "https://issuer.example.com/status/iban-ov/2026"
    }
  }
}
```


#### 5.1.3 Example Payload

The following is a non-normative example of an IBAN-OV SD-JWT VC payload for a **legal person**:
```
{
  "vct": "eu.we-build:iban-ov:1",
  "iss": "https://bank.example.com",
  "iat": 1736935200,
  "exp": 1768471200,
  "issuing_entity": "did:example:bank-123",
  "attestation_legal_category": "EAA",
  "schema_version": "1.0",
  "bank_account": {
    "account_name": "Company A Main Account",
    "iban": "DE89370400440532013000",
    "account_type": "CURRENT",
    "account_currency": ["EUR"]
  },
  "account_ownership": {
    "owner_type": "entity",
    "owner_name": "Company A GmbH",
    "legal_person_identifiers": [
      {
        "type": "EUID",
        "value": "DE-HRB-123456"
      },
      {
        "type": "LEI",
        "value": "529900T8BM49AURSDO55"
      },
      {
        "type": "TAX",
        "value": "123/456/7890"
      }
    ]
  },
  "account_provider": {
    "provider_name": "Example Bank AG",
    "legal_person_identifiers": [
      {
        "type": "EUID",
        "value": "DE12121.HRB654321"
      },
      {
        "type": "BIC",
        "value": "DEUTDEDB"
      },
      {
        "type": "LEI",
        "value": "529900XYZ123ABCDEF99"
      }
    ],
    "provider_country": "DEU",
    "bic_swift": "DEUTDEDB",
    "national_bank_code": "37040044",
    "nace_code": "64.19",
    "clearing_number": "37040044"
  },
  "status": {
    "status_list": {
      "idx": 456,
      "uri": "https://bank.example.com/status/iban-ov/2025"
    }
  }
}
```
The following is a non-normative example of an IBAN-OV SD-JWT VC payload for a **natural person (sole trader)**:
```
{
  "vct": "eu.we-build:iban-ov:1",
  "iss": "https://bank.example.com",
  "iat": 1736935200,
  "exp": 1768471200,
  "issuing_entity": "did:example:bank-123",
  "attestation_legal_category": "EAA",
  "schema_version": "1.0",
  "bank_account": {
    "account_name": "Maria Müller Consulting",
    "iban": "DE89370400440532013001",
    "account_type": "CURRENT",
    "account_currency": ["EUR"]
  },
  "account_ownership": {
    "owner_type": "person",
    "given_name": "Maria",
    "surname": "Müller"
  },
  "account_provider": {
    "provider_name": "Example Bank AG",
    "legal_person_identifiers": [
      {
        "type": "EUID",
        "value": "DE1212.HRB654321"
      },
      {
        "type": "BIC",
        "value": "DEUTDEDB"
      }
    ],
    "provider_country": "DEU",
    "bic_swift": "DEUTDEDB",
    "national_bank_code": "37040044",
    "nace_code": "64.19",
    "clearing_number": "37040044"
  },
  "status": {
  "status_list": {
    "idx": 457,
    "uri": "https://bank.example.com/status/iban-ov/2026"
  }
}
```
Sample payloads are provided under ../data-schemas/sd-jwt/sample-data/iban-ov-sd-jwt-sample.json

### 5.2 ISO/IEC 18013-5-compliant encoding

ISO/IEC 18013-5 (also called mdoc) is out of scope for this Rulebook, as offline proximity presentation is not a current requirement for the IBAN-OV attestation.

### 5.3 W3C Verifiable Credentials Data Model-based encoding

This Rulebook does not define a W3C Verifiable Credentials Data Model encoding for this attestation type.

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


The IBAN-OV attestation is issued by the bank (ASPSP) holding the account, either:

- Within the RP registration process, or
- Upon explicit request from the legal entity owning the IBAN account.

- The issuer (i.e., the legal entity itself) issues the attestation based on the information and
  supporting documentation available at the time of issuance.
- The issuer is responsible for ensuring that the attested information remains accurate and
  must immediately revoke the attestation if any change occurs that affects the validity or accuracy of the underlying data.
- The issuer is responsible for ensuring that the device binding is assured
  - ex. EUDI Wallet
  - ex. EBW Wallet - always in the same wallet by onboarding

### 7.3 Lifecycle management

The issuer sets the validity period of the attestation and reissues it when the
underlying facts change, revoking the superseded attestation as described in chapter 8.

### 7.4 Embedded disclosure policy

This attestation defines no embedded disclosure policy.

## 8 Revocation

This chapter will be completed in a future version of this Rulebook.

## 9 Presentation

#### Base Verification Process
The Relying Party SHALL perform the base attestation verification process as defined in the Base Verification specification:

https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-base/verifier-base-verification.md

In accordance with sections 4.2.5 and 4.2.6 of the Base Verification Process, relying parties are required to automatically verify the credential's revocation status. This verification confirms the current status of the bank account, thereby rendering an additional 'bank_account_status' attribute obsolete.

#### Validate Integrity Rules
- The Relying Party SHALL verify that the attestation is NOT being used to initiate or execute a payment.
- The Relying Party SHALL verify that the `IBAN conforms` to ISO 13616:2020 format.
- The Relying Party SHALL verify that the `bic_swift` conforms to ISO 9362 format.
- The Relying Party SHALL verify that the `expiry_date` is after the issuance_date.
- The Relying Party SHALL verify that owner_type is present in account_ownership and contains exactly one of the permitted values ('entity', 'person').
- The Relying Party SHALL verify that the name attributes present in account_ownership are consistent with the declared owner_type: owner_name for legal persons; given_name and surname for natural persons.

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

This chapter will be completed in a future version of this Rulebook.

**Trust anchor location**

The attribute or metadata carrying the trust anchor location contains at least the URL
at which a machine-readable version can be found or looked up.

## 11 References

This chapter will be completed in a future version of this Rulebook.

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
| [Token Status List] | OAuth Status List. draft-ietf-oauth-status-list-21. Available: https://www.ietf.org/archive/id/draft-ietf-oauth-status-list-21.html |
