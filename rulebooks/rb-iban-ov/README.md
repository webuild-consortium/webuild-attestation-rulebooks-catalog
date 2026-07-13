# Attestation Rulebook for attestations of type IBAN Ownership Verification (IBAN-OV)

* Author(s):
  * [Ricky Lamberty, Robert Bosch GmbH]
  * [Stephan-A Fuchs, Deutsche Bank AG]
* Previous Authors:
* Reviewer(s):
  * [Florin Coptil, Robert Bosch GmbH]
  * [Stefan, Kauhaus, Visa Inc.]
  * [Ivan Faltus, BankID.CZ]
  * [Filip Hladký, BankID.CZ]
  * @Reviewers: Contact Ricky to be added in the Reviewers section if you're missing. 

| Version | Date       | Description                                                     |
|---------|------------|-----------------------------------------------------------------|
| 0.1     | 15.05.2026 | Initial draft based on the WeBuild design attestations meetings |
| 0.2     | 17.06.2026 | Reviewed version based on the initial draft 					 |
| 0.3     | 25.06.2026 | Alignment with data schema and natural persons requirements	 |

* Contact:
  * [Ricky Lamberty](mailto:Ricky.Lamberty@bosch.com)*

* Feedback:

---

## 1 Introduction
This attestation addresses the following question:

**Is a specific IBAN legally owned by a designated legal entity or natural person, and has this ownership been verified and confirmed by the account-servicing financial institution?**

The IBAN Ownership Verification (IBAN-OV) Attestation provides trusted assurance to third parties that a specific IBAN is legally owned by a designated legal entity or natural person acting as a sole trader, enabling structured and fraud-resistant exchange of bank account ownership data for use in KYS, KYC, and payment compliance processes.

### 1.1 Attestation scope and purpose

The IBAN-OV attestation provides trusted assurance to third parties that a specific IBAN is legally owned by a designated legal entity or natural person (acting as soletraders which are registered in a national register). This verified proof of ownership can be used across various business processes (e.g. onboarding process, supporting payment-related triggers) to reduce errors and mitigate fraud risks. This attestation will not be used to initiate or execute any kind of payment.

The IBAN-OV attestation will be provided within the RP registration process (e.g. bank account opening) or upon request from the legal entity owning the IBAN account. Its purpose is to ensure that, at a later stage, payments for delivered services or sold products can be properly attributed to the verified legal entity.

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

This Rulebook is structured as follows:

- Chapter 1 provides an introduction to the IBAN-OV attestation, including its scope and purpose, document structure, keywords, and terminology.
- Chapter 2 describes the attestation attributes and metadata in an encoding-independent manner, including the data model.
- Chapter 3 specifies how the attestation attributes and metadata are encoded: Section 3.2 covers SD-JWT VC-based encoding.
- Chapter 4 specifies attestation usage scenarios, Relying Party obligations, and integration with KYC/KYS workflows.
- Chapter 5 defines trust anchors and verification mechanisms for issuer authorization.
- Chapter 6 defines revocation mechanisms for the attestation.
- Chapter 7 provides compliance information regarding the EUDI framework and applicable data
  protection laws.

### 1.3 Keywords

This document uses the capitalised keywords 'SHALL', 'SHOULD' and 'MAY' as specified in RFC 2119, i.e. to indicate requirements, recommendations and options specified in this document.

In addition, 'must' (non-capitalised) is used to indicate an external constraint, i.e. a requirement that is not mandated by this document, but, for instance, by an external document. The word 'can' indicates a capability, whereas other words, such as 'will', and 'is' or 'are' are intended as statements of fact.
### 1.4 Terminology

*Additional terminology specific to this attestation:*

| Term        | Description                                                                                                                                                                     |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IBAN-OV     | IBAN Ownership Verification (IBAN-OV) — the attestation type defined in this Rulebook, providing verified proof that a specific IBAN is owned by a designated legal entity or sole trader |
| ASPSP       | Account Servicing Payment Service Provider — the financial institution holding and managing the bank account                                                                    |
| IBAN        | International Bank Account Number — a standardized international numbering system for individual bank accounts, as defined in ISO 13616:2020                                    |
| BIC/SWIFT   | Bank Identifier Code — an international standard for identifying banks and financial institutions globally, as defined in ISO 9362:2022                                         |
| EUID        | European Unique Identifier — the unique identifier assigned to legal entities registered within the EU                                                                          |
| KYC         | Know Your Customer — due diligence process for verifying customer identity and assessing risk in financial relationships                                                        |
| KYS         | Know Your Supplier — due diligence process for verifying supplier identity and integrity.																						|
| Legal Person | A legal entity registered in a national or EU company register, identified by an EUID. For IBAN-OV purposes, the account owner in the legal_person case						|
| Sole Trader | A natural person operating a business who is registered in a national register                                                                                                  |
| Owner_Type  | A discriminator attribute within *Account_Ownership* that explicitly identifies whether the account owner is a legal person or a natural person.			     				|
| ISO 4217:2015    | International standard defining currency codes (e.g., EUR, USD, GBP)                                                                                                       |
| ISO 13616-1:2020   | International standard defining the IBAN format and validation rules                                                                                                     |
| ISO 9362:2014    | International standard defining the BIC/SWIFT code format                                                                                                                  |
| ISO 3166-1  | International standard defining country codes (Alpha-3 code)                                                                                                                    |

---

## 2 Attestation attributes and metadata

The IBAN-OV Attestation is a document that provides verified information about the bank account details of the account owner. It ensures that a legal entity (or natural person) can confidentially prove to a third party that this IBAN also belongs to the same legal entity (or natural person). 

### 2.1 Introduction

**Data Model:**

```
IBAN-OV Attestation
│
├── Bank_Account
│ ├── account_name
│ ├── iban
│ ├── account_type
│ └── account_currency
│
├── Account_Ownership 
│ ├── owner_type 
│ └── owner_name		(mandatory if legal person, 'entity')
│ └── euid
│ ├── given_name		(mandatory if natural person, 'person')
│ ├── surname			(mandatory if natural person, 'person')
│
└── Account_Provider
  ├── provider_name
  ├── euid
  ├── provider_country
  ├── bic_swift
  ├── national_bank_code
  ├── nace_code
  ├── clearing_number
```

**Explanation:**

- `Bank_Account` contains the core details of the account itself, such as IBAN, currency,
  and type.
- `Account_Ownership` identifies the legal owner of the account, including name and EUID.
- `Account_Provider` describes the financial institution that issued the account and metadata
  about the attestation.

This structure effectively separates the **what** (the bank account), the **who** (the bank
account owner) and the **where & how** (the provider & metadata).

**Attestation Classification:**

This attestation type MAY be classified as:
- **"EAA"** when issued by the bank (ASPSP) acting as an authorized issuer within the EUDI  framework according to ETSI 119 478.

### 2.2 Mandatory attributes

**Bank_Account Mandatory Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                                         | **Data type**                            |
|---------------------|------------------------|------------------------------------------------------------------------|------------------------------------------|
| account_name        | tbd                    | Name of the account, generated by the bank or customized by the owner. | String                                   |
| iban                | tbd                    | International Bank Account Number, as defined in ISO 13616:2020.       | [A-Z]{2}[0-9A-Z]{13,30}                  |
| account_type        | tbd                    | Nature of the bank account.                                            | String                                   |
| account_currency    | tbd                    | Currency code(s) used for the account, as defined in ISO 4217:2015.    | Array (3-digit code(s)) — ISO 4217:2015  |

**Account_Ownership Mandatory Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                                                                | **Data type** |
|---------------------|------------------------|-----------------------------------------------------------------------------------------------|---------------|
| owner_type          | tbd                    | Discriminator identifying whether the account owner is a legal person or a natural person.    | String - enum |
| owner_name          | tbd                    | Legal name of the legal person owning the account.											   | String        | Mandatory if owner_type = entity
| given_name	      | tbd                    | Given name(s) of the natural person owning the account.									   | String        | Mandatory if owner_type = person
| surname	          | tbd                    | Surname / family name of the natural person owning the account.							   | String        | Mandatory if owner_type = person

**Account_Provider Mandatory Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                                                                      | **Data type**   |
|---------------------|------------------------|-----------------------------------------------------------------------------------------------------|-----------------|
| provider_name       | tbd                    | Name of the financial institution providing the account.                                            | String          |
| euid                | tbd                    | Unique identification number of the issuing entity.                                                 | String          |
| provider_country    | tbd                    | Alpha-3 country code, as defined in ISO 3166-1, of the provider country or territory.               | 3-digit code    |
| bic_swift           | tbd                    | International code (i.e. BIC or SWIFT code), as defined in ISO 9362, of the financial institution. | String ISO 9362 |

### 2.3 Optional attributes

**Account_Provider Optional Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                                                                | **Data type** |
|---------------------|------------------------|-----------------------------------------------------------------------------------------------|---------------|
| national_bank_code  | tbd                    | Country-specific code for internal routing within a specific country's clearing system.       | String        |
| nace_code           | tbd                    | NACE code for activity specification (e.g. 64.19) of the institution providing the account.   | String        |
| clearing_number     | tbd                    | Clearing number for identification of the financial institution, used only in some countries. | String        |

**Account_Ownershpi Optional Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                                                                | **Data type** |
|---------------------|------------------------|-----------------------------------------------------------------------------------------------|---------------|
| euid 				  | tbd                    | Unique identification number of the owner of the account.                                     | String        |


### 2.4 Conditional attributes

The following conditional attributes are defined for the `Account_Ownership` object. Their presence is mandatory or prohibited depending on the value of `owner_type`:

- owner_name SHALL be present if and only if owner_type = entity.
- euid SHALL be present if and only if owner_type = entity.
- given_name and surname SHALL be present if and only if owner_type = person.
- given_name and surname SHALL NOT be present when owner_type = legal_person.

This conditional structure is enforced via JSON Schema if/then validation (Draft 2020-12) in the accompanying data schema.


### 2.5 Mandatory metadata

| **Data Identifier**        | **Definition**                                                                                                                                                     | **Data type** |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| iat			             | The date and time when the verifiable credential was issued (ISO 8601)                                                                                             | DateTime      |
| exp		                 | The date and time when the attestation expires (ISO 8601)                                                                                                          | DateTime      |
| iss			             | The identifier of the legal entity that issued the attestation (typically the subject entity itself for self-issued attestations)                                  | String        |
| attestation_legal_category | Indicates the legal category of this attestation ("EAA")                                                                                                           | String        |
| vct                        | A unique identifier (URL or URN) for the credential type, indicating which claims must be present and which can be selectively disclosed                           | String        |
| cnf                        | Cryptographic key binding element																										                          | String        |

### 2.6 Optional metadata

| **Data Identifier** | **Definition**                                                             | **Data type** |
|---------------------|----------------------------------------------------------------------------|---------------|
| trust_anchor_url    | URL where the trust anchor for verifying this attestation can be retrieved | URI           |
| schema_version      | Version of the schema used                                                 | String        |

### 2.7 Conditional metadata

No conditional metadata elements are defined for this attestation type.

### 2.8 Value Lists

#### 2.8.1 Currency Codes

The `account_currency` attribute SHALL follow ISO 4217:2015 currency codes.

| **Code** | **Definition**       |
|----------|----------------------|
| EUR      | Euro                 |
| USD      | United States Dollar |
| GBP      | Pound Sterling       |
| CHF      | Swiss Franc      	  |
| …        | …                    |

#### 2.8.2 Account Type Codes

The `account_type` attribute SHOULD use one of the following standardized values:

| **Example Code** | **Definition**     |
|------------------|--------------------|
| CURRENT          | Current Account    |
| SAVINGS          | Savings Account    |
| BASIC            | Basic Bank Account |
| LOAN             | Loan Account       |
| OTHER            | Other              |

#### 2.8.3 OWner Type Codes

| **Example Code** | **Definition**      |
|------------------|---------------------|
| person	  	   | Natural Person      |
| entity		   | Legal Person/Entity |
										

### 2.9 Integrity Rules

The following integrity rules SHALL be enforced:

- The IBAN-OV attestation SHALL be cryptographically bound and issued exclusively to the   specific Holder wallet that was onboarded by the Issuer (the bank).
- `expiry_date` SHALL be dated after the `issuance_date`.
- `iban` SHALL conform to the ISO 13616:2020 format: [A-Z]{2}[0-9A-Z]{13,30}.
- `bic_swift` SHALL conform to the ISO 9362:2022 format: [A-Z]{6}[A-Z0-9]{2}([A-Z0-9]{3}).
- `provider_country` SHALL be a valid ISO 3166-1 alpha-3 country code.
- `account_currency` SHALL contain at least one valid ISO 4217:2015 currency code.
- `euid` in Account_Ownership SHALL be a non-empty string identifying the register entry of the account owner, regardless of whether the owner is a legal person or a natural person (sole trader).
- `euid` in Account_Provider SHALL be a non-empty string identifying the issuing financial   institution.
- Each attribute SHALL appear at most once in the attestation.
- `owner_type` in Account_Ownership SHALL be present and SHALL contain exactly one of the values `legal_person` or `natural_person`.
- If `owner_type` = `legal_person`, owner_name SHALL be present and `given_name` and `surname` SHALL NOT be present.
- If `owner_type` = `natural_person`, `given_name` and `surname` SHALL both be present and `owner_name` MAY be present as a derived display name.
- The attestation SHALL NOT be used to directly initiate or execute payments.

## 3 Attestation encoding

### 3.1 ISO/IEC 18013-5-compliant encoding

ISO/IEC 18013-5 (also called mdoc) is out of scope for this Rulebook, as offline proximity presentation is not a current requirement for the IBAN-OV attestation.

### 3.2 SD-JWT VC-based encoding

The IBAN-OV attestation uses the SD-JWT VC format to allow for selective disclosure of account attributes.

**Selective Disclosure:** Top-level claims (`bank_account`, `account_ownership`, `account_provider`) SHALL be individually selectively disclosable, enabling the account holder to disclose only the attributes requested by a Relying Party.

The `.` notation is used to indicate the nesting of attributes.

**Verifiable Credential Type (`vct`):** `vct: eu.we-build.iban-ov.1`


#### 3.2.1 Attribute Encoding Table

| **Data Identifier**        | **Attribute identifier**            | **Encoding format**     | **Reference/Notes**                                                                                     | **Disclosable** |
|----------------------------|-------------------------------------|-------------------------|---------------------------------------------------------------------------------------------------------|-----------------|
| **Bank_Account**           |                                     |                         |                                                                                                         |                 |
| account_name               | bank_account.account_name           | String                  | Name of the account                                                                                     | MUST            |
| iban                       | bank_account.iban                   | String                  | ISO 13616:2020 format                                                                                   | MUST            |
| account_type               | bank_account.account_type           | String                  | Nature of the bank account                                                                              | MUST            |
| account_currency           | bank_account.account_currency       | Array of Strings        | ISO 4217:2015 currency codes                                                                            | MUST            |
| **Account_Ownership**      |                                      |                         |                                                                                                        |                 |
| owner_type                 | account_ownership.owner_type         | String                  | Discriminator identifying the owner type. Enum: `entity` \| `person`			                       | MUST            |
| owner_name                 | account_ownership.owner_name         | String                  | Legal name of the legal entity owning the account. Present only if `owner_type = entity`	           | MUST            |
| euid                       | account_ownership.euid               | String                  | EUID of the owner of the account																	   | MUST			 |   
| given_name           	     | account_ownership.given_name         | String                  | Given name(s) of the natural person owning the account. Present only if `owner_type = person`          | MUST            |
| surname                    | account_ownership.surname            | String                  | Surname of the natural person owning the account. Present only if `owner_type = person`                | MUST            |
| **Account_Provider**       |                                     |                         |                                                                                                         |                 |
| provider_name              | account_provider.provider_name      | String                  | Name of the financial institution                                                                       | MUST            |
| bank_identifier            | account_provider.euid               | String                  | EUID of the financial institution                                                                       | MUST            |
| provider_country           | account_provider.provider_country   | String                  | ISO 3166-1 alpha-3 country code                                                                         | MUST            |
| bic_swift                  | account_provider.bic_swift          | String                  | ISO 9362 BIC/SWIFT format                                                                               | MUST            |
| national_bank_code         | account_provider.national_bank_code | String                  | Country-specific routing code                                                                           | MUST            |
| nace_code                  | account_provider.nace_code          | String                  | NACE activity code                                                                                      | MUST            |
| clearing_number            | account_provider.clearing_number    | String                  | Country-specific clearing number                                                                        | MUST            |
| **Metadata**               |                                     |                         |                                                                                                         |                 |
| issuance_date              | iat                                 | Number (Unix timestamp) | ISO 8601 — RFC 7519 / Section 2.5                                                                       | MUST NOT        |
| expiry_date                | exp                                 | Number (Unix timestamp) | ISO 8601 — RFC 7519 / Section 2.5                                                                       | MUST NOT        |
| issuing_entity             | iss				                   | String                  | Identifier of the issuing financial institution                                                         | MUST NOT        |
| attestation_legal_category | attestation_legal_category          | String                  | "EAA" defined by eIDAS 2                                                                   | MUST NOT        |
| vct                        | vct                                 | String                  | A URI or other collision-resistant identifier that defines the type of the SD-JWT Verifiable Credential | MUST            |
| schema_version             | schema_version                      | String                  | Version of the schema used for this attestation                                                         | MAY             |
| trust_anchor_url           | trust_anchor_url                    | String (URI)            | URL where the trust anchor for verifying this attestation can be retrieved                              | MAY             |


**Notes:**

- **MUST**: The claim SHALL be selectively disclosable — the holder MAY choose to disclose or
  withhold this claim when presenting the credential to a Relying Party.
- **MUST NOT**: The claim SHALL NOT be selectively disclosable — it is always present in plain
  text in the JWT header/payload and cannot be withheld by the holder, as it is required for
  credential verification and trust establishment.
- `iat`, `exp`, and `iss` follow RFC 7519 standard JWT claim naming conventions.

#### 3.2.2 Status Claim

For SD-JWT VC-compliant IBAN-OV attestations, the attestation MUST include a `status` claim if
the technical validity period is greater than 24 hours. This claim enables Relying Parties to
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
    "status_list_credential": "https://issuer.example.com/status/iban-ov/2025",
    "status_list_index": 456,
    "status_purpose": "revocation"
  }
}
```

#### 3.2.3 Example Payload

The following is a non-normative example of an IBAN-OV SD-JWT VC payload for a **legal person**:

```json
{
  "vct": "eu.we-build.iban-ov.1",
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
    "euid": "DE-HRB-123456"
  },
  "account_provider": {
    "provider_name": "Example Bank AG",
    "bank_identifier": "DE-HRB-654321",
    "provider_country": "DEU",
    "bic_swift": "DEUTDEDB",
    "national_bank_code": "37040044",
    "nace_code": "64.19",
    "clearing_number": "37040044"
  },
  "status": {
    "type": "status-list",
    "status_list_credential": "https://bank.example.com/status/iban-ov/2025",
    "status_list_index": 456,
    "status_purpose": "revocation"
  }
}
```

The following is a non-normative example of an IBAN-OV SD-JWT VC payload for a **natural person (sole trader)**:

```json
{
  "vct": "eu.we-build.iban-ov.1",
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
    "bank_identifier": "DE-HRB-654321",
    "provider_country": "DEU",
    "bic_swift": "DEUTDEDB",
    "national_bank_code": "37040044",
    "nace_code": "64.19",
    "clearing_number": "37040044"
  },
  "status": {
    "type": "status-list",
    "status_list_credential": "https://bank.example.com/status/iban-ov/2025",
    "status_list_index": 457,
    "status_purpose": "revocation"
  }
}
```

Sample payloads are provided under ../data-schemas/sd-jwt/sample-data/iban-ov-sd-jwt-sample.json

#### 3.3 W3C Verifiable Credentials Data Model-based encoding
...

## 4 Attestation usage
### 4.1. Issuance process ###
The IBAN-OV attestation is issued by the bank (ASPSP) holding the account, either:
- Within the RP registration process, or
- Upon explicit request from the legal entity owning the IBAN account.

### 4.2 Relying Party Obligations
When receiving and processing an attestation, the Relying Party SHALL perform the following verification obligations.

### 4.2.1 – 4.2.8 Base Verification Process
The Relying Party SHALL perform the base attestation verification process as defined in the Base Verification specification:
https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-base/verifier-base-verification.md

In accordance with sections 4.2.5 and 4.2.6 of the Base Verification Process, relying parties are required to automatically verify the credential's revocation status. This verification confirms the current status of the bank account, thereby rendering an additional 'bank_account_status' attribute obsolete.

### 4.2.9 Validate Integrity Rules
Validation of integrity and policy rules will be specified in a future version of this Rulebook.

- The Relying Party SHALL verify that the attestation is NOT being used to initiate or execute a payment.
- The Relying Party SHALL verify that the `IBAN conforms` to ISO 13616:2020 format.
- The Relying Party SHALL verify that the `bic_swift` conforms to ISO 9362 format.
- The Relying Party SHALL verify that the `expiry_date` is after the issuance_date.
- The Relying Party SHALL verify that owner_type is present in account_ownership and contains exactly one of the permitted values ('entity', 'person').
- The Relying Party SHALL verify that the name attributes present in account_ownership are consistent with the declared owner_type: owner_name for legal persons; given_name and surname for natural persons.
- Additional validation of integrity and policy rules will be specified in a future version of this Rulebook.

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


