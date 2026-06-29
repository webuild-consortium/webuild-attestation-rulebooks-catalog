# Attestation Rulebook for attestations of type Company Information (CompanyInfo)

* Author(s):
  * [Ana Delmas, DFO]
  * [Florin Coptil, Robert Bosch GmbH]
* Previous Authors
  * 
* Reviewer(s):
  * [Ricky Lamberty, Robert Bosch GmbH]

| Version | Date       | Description                                                     |
|---------|------------|-----------------------------------------------------------------|
| 0.1     | 01.05.2026 | Initial draft based on the WeBuild design attestations meetings |
| 0.5     | 01.06.2026 | Review in regard to holder perspective                          |
| 0.6     | 23.06.2026 | Review in regard to verifier perspective                        |
| 0.8     | 29.06.2026 | Review attributes and type                                      |

* Contact:
  * [Florin Coptil](mailto:florin.coptil@bosch.com)* 

* Feedback:

---

## 1 Introduction

This attestation addresses the following question:

**What additional company information is available that is not publicly accessible can be atteested by the company or by a QTSP provider?**

The Company Information (CompanyInfo) Attestation describes additional company-level information which is not part of the EUCC core identity dataset. The attestation enables structured exchange of business profile attributes for use in KYS (Know Your Supplier), KYC (Know Your Customer), supplier onboarding, and risk assessment processes.

### 1.1 Document scope and purpose

The Company Information (CompanyInfo) Attestation describes additional company-level information which is not part of the EUCC core identity dataset. The attestation enables structured exchange of business profile attributes for use in KYS (Know Your Supplier), KYC (Know Your Customer), supplier onboarding, and risk assessment processes.

This attestation complements the EU Company Certificate (EUCC) by providing additional non-core identity attributes, in particular company size indicators and financial scale. It is intended for use by legal entities operating within the EU single market and by relying parties performing business due diligence.

**Design Decisions**

This CompanyInfo Attestation Rulebook is based on:
- EU Company Certificate (EUCC) framework as the foundational legal identity layer
- Standard financial reporting taxonomies (IFRS, GAAP) for structured financial data exchange
- XBRL-inspired fact-based financial reporting structure
- ISO 4217 for currency codes
- ISO 8601 for date formatting

### 1.2 Document structure

This Rulebook is structured as follows:

- Chapter 2 describes the CompanyInfo attestation attributes and metadata in an encoding-independent manner, including the data model.
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

| Term                | Description                                                                                                                               |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| CompanyInfo         | The attestation type defined in this Rulebook, providing structured business profile attributes of a legal entity                         |
| EUCC                | EU Company Certificate – attestation establishing the legal existence and identity of a legal entity within the EU                        |
| Financial Fact      | A single reported financial data point (e.g., Revenue, Net Income) associated with a specific reporting period, taxonomy, unit, and value |
| Financial Taxonomy  | The financial reporting standard used to structure and label financial data (e.g., IFRS, US GAAP, Local GAAP)                             |
| Fiscal Year         | The twelve-month accounting period for which financial statements are prepared, represented in Gregorian calendar year format (YYYY)      |
| KYC                 | Know Your Customer – due diligence process for verifying customer identity and assessing risk in financial relationships                  |
| KYS                 | Know Your Supplier – due diligence process for verifying supplier credentials, integrity, and risk exposure                               |
| Trade Alias         | A registered trade name or brand name under which a legal entity operates, distinct from its official legal name                          |
| Previous Legal Name | A formerly registered legal name of the entity, as recorded in official company registers prior to the current legal name                 |
| Employee Number     | Total number of employees in the legal entity at the time of reporting                                                                    |
| ISO 4217            | International standard defining currency codes (e.g., EUR, USD, GBP)                                                                      |
| ISO 8601            | International standard for date and time representations (e.g., YYYY-MM-DD)                                                               |

## 2 Attestation attributes and metadata
The CompanyInfo Attestation is designed to provide a standardized, verifiable representation of a legal entity's business profile attributes, including workforce size and structured financial reporting data. This attestation complements the EUCC by providing additional non-core identity attributes required for KYS, KYC, supplier onboarding, and risk assessment processes.

### 2.1 Introduction

**Data Model:**

The attestation structure is defined as a structured object with a nested array of financial facts:

```
CompanyInfo
├─ number_of_employees  (number) (M) 
├─ trade_alias [tstr] (O)
├─ previous_legal_name [tstr] (O)
└─ financial_statements (M) 
    ├─ taxonomy (tstr) (M)
    └─ facts [1..n]
        ├─ id (tstr) (M)
        ├─ concept(tstr) (M) 
        ├─ value (number) (M)
        ├─ unit (tstr) (M)
        ├─ period_start (date) (M)
        └─ period_end((date) (M)

Note:
M - mandatory
O - optional 
```

**Explanation:**
- `number_of_employees` and `financial_statements` are mandatory top-level attributes.
- `trade_alias` and `previous_legal_name` are optional and may contain zero or more text values.
- `financial_statements` is a mandatory nested object containing the reporting taxonomy and at least one financial fact.
- Each `Fact` in the `facts` array is a self-contained reported financial data point with its own concept, value, unit, and reporting period.

**Attestation Classification:**

This attestation type MAY be classified as:
- **"EAA"** when self-issued by the legal entity subject to the disclosure.
- **"QEAA"** when issued by a qualified trust service provider (QTSP) or authorized competent body that can independently attest the company information (e.g., based on official company register data or audited financial statements).

### 2.2 Mandatory attributes

| **Data Identifier**                        | **Semantic Reference** | **Definition**                                                         | **Data type**                    |
|--------------------------------------------|------------------------|------------------------------------------------------------------------|----------------------------------|
| employee_number                            | ...                    | Total number of employees in the legal entity at the time of reporting | uint                             |
| financial_statements                       | ...                    | financial_statements                                                   | Object                           |
| financial_statements.taxonomy              | --                     | Financial reporting standard used (e.g., IFRS, GAAP)                   | String                           |
| financial_statements.facts                 | --                     | List of reported financial facts                                       | Array [Fact]                     |
| financial_statements.facts[n].id           | ---                    | Unique identifier of the fact                                          | String                           |
| financial_statements.facts[n].concept      | ---                    | Name of the reported metric (e.g., Revenue, NetIncome)                 | String                           |
| financial_statements.facts[n].value        | ---                    | Reported value of the fact                                             | Decimal                          |
| financial_statements.facts[n].unit         | ---                    | Unit of measurement (e.g., EUR, %, shares)                             | String (ISO 4217 for currencies) |
| financial_statements.facts[n].period_start | ---                    | Start date of the reporting period                                     | ISO 8601 (YYYY-MM-DD)            |
| financial_statements.facts[n].period_end   | ---                    | End date of the reporting period                                       | ISO 8601 (YYYY-MM-DD)            |

### 2.3 Optional attributes

| **Data Identifier** | **Semantic Reference** | **Definition**                                                                                                                                                                           | **Data type** |
|---------------------|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| trade_alias         | --                     | Registered trade names or aliases under which the legal entity operates. MAY contain zero or more text values.                                                                           | Array of tstr |
| previous_legal_name | --                     | Previously registered legal name(s) of the entity, as recorded in official company registers prior to the current legal name. MAY contain zero or more text values.                      | Array of tstr |

### 2.4 Conditional attributes

No conditional attributes are defined for this attestation type. All attributes are either mandatory or optional as specified above.

### 2.5 Mandatory metadata

| **Data Identifier**        | **Definition**                                                                                                                                                     | **Data type**   |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| attestation_legal_category | Indicates the legal category of this attestation ("EAA")                                                                                                           | String          |

## 2.6 Optional metadata

| **Data Identifier** | **Definition**                                                             | **Data type** |
|---------------------|----------------------------------------------------------------------------|---------------|
| trust_anchor_url    | URL where the trust anchor for verifying this attestation can be retrieved | URI           |
| schema_version      | Version of the schema used                                                 | String        |

### 2.7 Conditional metadata

No conditional metadata elements are defined for this attestation type.

### 2.8 Value Lists

#### 2.8.1 Currency Codes

The `unit` attribute within each `Fact` object, when representing a monetary value, SHALL follow **ISO 4217** currency codes.

| **Example Code** | **Definition**       |
|------------------|----------------------|
| EUR              | Euro                 |
| USD              | United States Dollar |
| GBP              | Pound Sterling       |
| CHF              | Swiss Franc          |

No standardized EU value lists apply to `employee_number` or `trade_alias`.

#### 2.8.2 Financial Taxonomy Codes

The `taxonomy` attribute SHOULD use one of the following standardized values:

| **Code**   | **Definition**                                                      |
|------------|---------------------------------------------------------------------|
| IFRS       | International Financial Reporting Standards                         |
| US-GAAP    | United States Generally Accepted Accounting Principles              |
| LOCAL-GAAP | Local Generally Accepted Accounting Principles (country-specific)   |
| OECD       | OECD reporting framework                                            |

#### 2.8.3 Concept Codes

The `concept` attribute SHOULD use one of the following standardized values:

#### 2.8.4 Financial Fact Concept Codes

The `concept` attribute within each `Fact` object SHALL use one of the following standardized values:

**a. Income Statement (P&L)**

| **Code**          | **Definition**                                                      |
|-------------------|---------------------------------------------------------------------|
| Revenue           | Total income from sales of goods/services                           |
| Turnover          | Total sales revenue generated by the company over a specific period |
| CostOfSales       | Direct costs of producing goods/services                            |
| GrossProfit       | Revenue minus cost of sales                                         |
| OperatingExpenses | Costs for running business operations                               |
| EBIT              | Earnings before interest and tax                                    |
| NetIncome         | Final profit after all expenses and taxes                           |

**b. Balance Sheet**

| **Code**            | **Definition**                                        |
|---------------------|-------------------------------------------------------|
| Assets              | Total resources owned by the company                  |
| CurrentAssets       | Short-term assets (cash, receivables, etc.)           |
| NonCurrentAssets    | Long-term assets (property, equipment)                |
| Liabilities         | Total obligations of the company                      |
| CurrentLiabilities  | Short-term debt and obligations                       |
| Equity              | Shareholder value in the company                      |

**c. Cash Flow Statement**

| **Code**             | **Definition**                                       |
|----------------------|------------------------------------------------------|
| OperatingCashFlow    | Cash generated from operations                       |
| InvestingCashFlow    | Cash used/invested in assets                         |
| FinancingCashFlow    | Cash from financing activities                       |
| NetCashFlow          | Total change in cash position                        |

**d. Financial Ratios / KPIs**

| **Code**       | **Definition**                                                          |
|----------------|-------------------------------------------------------------------------|
| EBITDA         | Earnings before interest, taxes, depreciation, and amortization         |
| GrossMargin    | Profitability ratio of gross profit                                     |
| NetMargin      | Net income as percentage of revenue                                     |
| DebtToEquity   | Leverage ratio                                                          |

#### 2.8.3 Fiscal Year Format

Fiscal year, as referenced in the `period_start` and `period_end` attributes, SHALL follow the Gregorian calendar year format (**YYYY**) for year identification, with full ISO 8601 date representation (YYYY-MM-DD) for period boundaries.

### 2.9 Integrity Rules

The following integrity rules SHALL be enforced:

- `employee_number` SHALL be a non-negative integer.
- `financial_statements` SHALL contain at least one `Fact` in the `facts` array.
- Each `Fact` SHALL have a `value` that is a non-negative numeric value where applicable (e.g., revenue, total assets).
- If a monetary `value` is reported, the corresponding `unit` SHALL be a valid ISO 4217 currency code.
- `period_start` SHALL be a valid ISO 8601 date (YYYY-MM-DD).
- `period_end` SHALL be a valid ISO 8601 date (YYYY-MM-DD).
- `period_end` SHALL be equal to or later than `period_start`.
- `trade_alias` MAY contain zero or more text values.
- `previous_legal_name` MAY contain zero or more text values.
- `previous_legal_name` SHALL NOT contain the current legal name of the entity.
- Each attribute SHALL appear at most once in the attestation.
- The `id` field within each `Fact` SHALL be unique within the `facts` array of a single attestation.
- `taxonomy` SHALL be a non-empty string identifying the applicable financial reporting standard.

## 3 Attestation encoding

### 3.1 ISO/IEC 18013-5-compliant encoding

ISO/IEC 18013-5 (also called mdoc) is out of scope for this Rulebook, as offline proximity presentation is not a current requirement for the CompanyInfo attestation.

### 3.2 SD-JWT VC-based encoding

The CompanyInfo attestation uses the SD-JWT VC format to allow for selective disclosure of company attributes.

**Selective Disclosure:** Top-level claims (`employee_number`, `trade_alias`, `previous_legal_name`, `financial_statements`) SHALL be individually selectively disclosable, enabling a legal entity to disclose only the attributes requested by a Relying Party.

The `.` notation is used to indicate the nesting of attributes.

**Verifiable Credential Type (`vct`):** `vct: eu.we-build:companyinfo:1`

#### 3.2.1 Attribute Encoding Table

| **Data Identifier**                     | **Attribute identifier**                     | **Encoding format**              | **Reference/Notes**                                                                                      | **Disclosable** |
|-----------------------------------------|----------------------------------------------|----------------------------------|----------------------------------------------------------------------------------------------------------|-----------------|
| number_of_employees                     | `number_of_employees`                        | Integer (uint)                   | Total number of employees at time of reporting; SHALL be non-negative                                    | MUST            |
| trade_alias                             | `trade_alias`                                | Array of Strings                 | Zero or more registered trade names/aliases; optional                                                    | MUST            |
| previous_legal_name                     | `previous_legal_name`                        | Array of Strings                 | Zero or more previously registered legal names; optional                                                 | MUST            |
| **financial_statements**                |                                              |                                  |                                                                                                          |                 |
| financial_statements.taxonomy           | `financial_statements.taxonomy`              | String                           | Financial reporting standard used (e.g., IFRS, GAAP)                                                     | MUST            |
| financial_statements.facts              | `financial_statements.facts`                 | Array [Fact]                     | List of reported financial facts; at least one fact SHALL be present                                     | MUST            |
| **facts**                               |                                              |                                  |                                                                                                          |                 |
| financial_statements.facts.id           | `financial_statements.facts[n].id`           | String                           | Unique identifier of the fact within the attestation                                                     | MUST            |
| financial_statements.facts.concept      | `financial_statements.facts[n].concept`      | String                           | Name of the reported metric (e.g., Revenue, Turnover, NetIncome, TotalAssets)                            | MUST            |
| financial_statements.facts.value        | `financial_statements.facts[n].value`        | Decimal (number)                 | Reported numeric value of the fact                                                                       | MUST            |
| financial_statements.facts.unit         | `financial_statements.facts[n].unit`         | String (ISO 4217 for currencies) | Unit of measurement (e.g., EUR, %, ratio)                                                                | MUST            |
| financial_statements.facts.period_start | `financial_statements.facts[n].period_start` | String (ISO 8601 YYYY-MM-DD)     | Start date of the reporting period                                                                       | MUST            |
| financial_statements.facts.period_end   | `financial_statements.facts[n].period_end`   | String (ISO 8601 YYYY-MM-DD)     | End date of the reporting period                                                                         | MUST            |
| **Metadata**                            |                                              |                                  |                                                                                                          |                 |
| attestation_legal_category              | `attestation_legal_category`                 | String                           | One of `EAA` as defined by eIDAS 2                                                                       | MUST NOT        |

**Notes:**

- **MUST**: The claim SHALL be selectively disclosable — the holder MAY choose to disclose or
  withhold this claim when presenting the credential to a Relying Party.
- **MUST NOT**: The claim SHALL NOT be selectively disclosable — it is always present in plain
  text in the JWT header/payload and cannot be withheld by the holder, as it is required for
  credential verification and trust establishment.
- `financial_statements` facts are marked as `MUST` disclosable as a unit — individual facts
  within the array are not independently selectively disclosable in this version.
- `iat`, `exp`, and `iss` follow RFC 7519 standard JWT claim naming conventions.

#### 3.2.2 Status Claim

For SD-JWT VC-compliant CompanyInfo attestations, the attestation MUST include a `status` claim if the technical validity period is greater than 24 hours. This claim enables Relying Parties to determine if a credential has been revoked via a status list mechanism, as specified in SD-JWT VC.

The `status` claim SHALL be a JSON object with the following members:

- `type` (string): SHALL be `"status-list"`.
- `status_list_credential` (string, URI): The URI of the Status List Credential document that contains the status bitstring.
- `status_list_index` (integer, >= 0): The zero-based index into the status list bitstring that corresponds to this credential.
- `status_purpose` (string): SHALL be `"revocation"` for this attestation.

Example:

```json
{
  "status": {
    "type": "status-list",
    "status_list_credential": "https://issuer.example.com/status/companyinfo/2025",
    "status_list_index": 123,
    "status_purpose": "revocation"
  }
}
```
### 3.2.3 Example Payload

The following example shows the payload of the attestation in SD-JWT VC format before the encoding into the SD-JWT format.
```
{
  "vct": "eu.we-build:companyinfo:1",
  "iss": "https://issuer.example.com",
  "iat": "2025-01-15T10:00:00Z",
  "exp": "2026-01-15T10:00:00Z",
  "issuing_entity": "did:example:legal-entity-123",
  "schema_version": "1.0",

  "number_of_employees": 1250,
  "trade_alias": ["BuildCo", "WeBuild Solutions"],
  "previous_legal_name": ["Former Company Name GmbH"],
  
  "financial_statements": {
    "taxonomy": "IFRS",
    "facts": [
      {
        "id": "fact-001",
        "concept": "Revenue",
        "value": 45000000.00,
        "unit": "EUR",
        "period_start": "2024-01-01",
        "period_end": "2024-12-31"
      },
      {
        "id": "fact-002",
        "concept": "NetIncome",
        "value": 3200000.00,
        "unit": "EUR",
        "period_start": "2024-01-01",
        "period_end": "2024-12-31"
      }
    ]
  },
  
  "status": {
    "type": "status-list",
    "status_list_credential": "https://issuer.example.com/status/companyinfo/2025",
    "status_list_index": 123,
    "status_purpose": "revocation"
  }
}
```
Sample payloads are provided under ../data-schemas/sd-jwt/sample-data/company-info-sd-jwt-sample.json

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
