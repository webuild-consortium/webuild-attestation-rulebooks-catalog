# Attestation Rulebook for attestations of type Company Information

Category: S-EAA

* Author(s):
  * [Ana Delmas, DFO]
  * [Florin Coptil, Robert Bosch GmbH]
* Previous Authors
  
* Reviewer(s):
  * [Dominic Hurni, SBB]
  * [Ricky Lamberty, Robert Bosch GmbH]
* Contact:
  * [Florin Coptil](mailto:florin.coptil@bosch.com)*  
* Feedback:

| Version | Date | Description |
| --- | --- | --- |
| 1.1 | 2026-10-02 | Restructured onto the generic WE BUILD attestation rulebook template (11 chapters). No normative content removed. |
| 1.2 | 2026-10-13 | Migrated to the current generic WE BUILD attestation rulebook template; attestation-specific normative content preserved. |

**Written against:** ARF version 3.0.0, WE BUILD template version 1.0 (generic)

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
   * [6.1 Issuance](#61-issuance)
   * [6.2 Presentation](#62-presentation)
- [7 Issuance](#7-issuance)
   * [7.1 Holder Key Binding at Issuance (Wallet Binding)](#71-holder-key-binding-at-issuance-wallet-binding)
   * [7.2 Issuance Policy](#72-issuance-policy)
   * [7.3 Lifecycle management](#73-lifecycle-management)
   * [7.4 Embedded disclosure policy](#74-embedded-disclosure-policy)
- [8 Revocation](#8-revocation)
- [9 Request, Presentation and Verification](#9-request-presentation-and-verification)
   * [9.1 Relying Party Role (RP Instance - EUDI Wallet)](#91-relying-party-role-rp-instance---eudi-wallet)
   * [9.2 EBW Relying Party Role (EBW Wallet - EBW Wallet)](#92-ebw-relying-party-role-ebw-wallet---ebw-wallet)
   * [9.3 Presentation modes](#93-presentation-modes)
   * [9.4 Transactional data](#94-transactional-data)
- [10 Trust Framework](#10-trust-framework)
   * [10.1 Relying Party Role (RP Instance - EUDI Wallet)](#101-relying-party-role-rp-instance---eudi-wallet)
   * [10.2 EBW Relying Party Role (EBW Wallet - EBW Wallet)](#102-ebw-relying-party-role-ebw-wallet---ebw-wallet)
- [11 References](#11-references)


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
- Submission Regulation – Commission on Implementing Regulation (EU) [number] on the formats for submitting beneficial ownership information.

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

| Term | Definition | Source |
| --- | --- | --- |
| CompanyInfo | The attestation type defined in this Rulebook, providing structured business profile attributes of a legal entity | |
| EUCC | EU Company Certificate – attestation establishing the legal existence and identity of a legal entity within the EU | |
| Financial Fact | A single reported financial data point (e.g., Revenue, Net Income) associated with a specific reporting period, taxonomy, unit, and value | |
| Financial Taxonomy | The financial reporting standard used to structure and label financial data (e.g., IFRS, US GAAP, Local GAAP) | |
| Fiscal Year | The twelve-month accounting period for which financial statements are prepared, represented in Gregorian calendar year format (YYYY) | |
| KYC | Know Your Customer – due diligence process for verifying customer identity and assessing risk in financial relationships | |
| KYS | Know Your Supplier – due diligence process for verifying supplier credentials, integrity, and risk exposure | |
| Trade Alias | A registered trade name or brand name under which a legal entity operates, distinct from its official legal name | |
| Previous Legal Name | A formerly registered legal name of the entity, as recorded in official company registers prior to the current legal name | |
| Employee Number | Total number of employees in the legal entity at the time of reporting | |
| ISO 4217 | International standard defining currency codes (e.g., EUR, USD, GBP) | |
| ISO 8601 | International standard for date and time representations (e.g., YYYY-MM-DD) | |

## 2 Compliance

This chapter states how this Rulebook complies with the Architecture and Reference
Framework and with the applicable Regulations. Sections 2.1 and 2.2 follow from the
legal category of this attestation. Section 2.3 maps each applicable requirement to
the section that satisfies it.

### 2.1 Compliance statement

This Rulebook complies with the applicable requirements of Topic 12, Attestation
Rulebooks, in Annex 2 of the Architecture and Reference Framework, version 3.0.0. It
uses the terminology of Annex 1 of the ARF.

### 2.2 Regulatory basis

FIXED

The regulatory basis below is the one applicable to the legal category of this
attestation.

**PID**

This Rulebook specifies how the mandatory and optional person identification data
defined in Tables 1 and 2 of the Annex to CIR (EU) 2024/2977, and the metadata
defined in Table 5 of that CIR, are encoded within the EUDI Wallet ecosystem.

**QEAA**

> This attestation includes the data required by Annex V of Regulation (EU)
> 2024/1183, points a, b, c, e and h, satisfying EW-DM-12-014, EW-DM-12-016,
> EW-DM-12-019, EW-DM-12-021 and EW-DM-12-023 respectively. It is issued by a
> qualified trust service provider.

**PuB-EAA**

> This attestation includes the data required by Annex VII of Regulation (EU)
> 2024/1183, points a, b, c, e and h, satisfying EW-DM-12-014, EW-DM-12-017,
> EW-DM-12-019, EW-DM-12-021 and EW-DM-12-023 respectively. It is issued by or on
> behalf of a public sector body responsible for an authentic source.

**Non-qualified EAA**

> This attestation is not a qualified electronic attestation of attributes. The data
> described in Annex V points b, c and e of Regulation (EU) 2024/1183 is addressed as
> required by EW-DM-12-018 and as recommended by EW-DM-12-020 and EW-DM-12-022.
> Where a recommendation is not followed, the reason is stated below.

**Non-qualified self EAA (S-EAA)** 

> This attestation is a subtype of a non-qualified electronic attestation of attributes.
> From a technical perspective, there is no difference between an EAA and an self EAA.
> The distinction lies primarily in the legal framework, particularly with regard to issuer liability.
> A self EAA is based on information owned or self-asserted by the issuer and
> is issued and used exclusively within a defined closed ecosystem
> and is intended to have no effect on third parties.
> Where Article 2(2) eIDAS applies, the service falls outside the scope of eIDAS;
> consequently, the eIDAS TSP liability regime does not apply, and
> liability is governed by applicable contractual and national law.

**EBWOID**

> TO AGREE. Do not assert qualified status unless the issuer is a QTSP, and do not
> cite Annex V or Annex VII by default.

### 2.3 Traceability

Every applicable requirement mapped to the section that satisfies it. Requirements
marked not applicable carry a stated reason. The Applies column records where a
requirement bites only in one of the two legal categories.

| Requirement | Legacy ID | Applies | Satisfied in section | Note |
| --- | --- | --- | --- | --- |
| EW-DM-12-001 | ARB_01a | yes | 5 | W3C VCDM permitted for this category; no encoding defined in this version |
| EW-DM-12-002 | ARB_01b | yes | 5.1 | SD-JWT VC following the HAIP profile |
| EW-DM-12-003 | ARB_02 | no |  | Proximity presentation is not in scope; mdoc is out of scope per section 5.2 |
| EW-DM-12-005 | ARB_04 | no |  | No W3C VCDM encoding is defined in this version |
| EW-DM-12-006 | ARB_05 | yes | 5.1 | Unique vct for this attestation type |
| EW-DM-12-007 | ARB_06 | yes | 3 | Attributes defined independently of encoding |
| EW-DM-12-008 | ARB_06a | no |  | No mdoc encoding is defined in this version |
| EW-DM-12-009 | ARB_06b | yes | 5.1 | SD-JWT VC claim naming |
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
| EW-DM-12-034 | ARB_30 | yes | 5.1 | Selective disclosure stated per claim |
| EW-DM-12-035 | ARB_31 | no |  | No Claim Selective Disclosure Metadata document is used |
| EW-DM-12-038 | ARB_34 | yes | 7.1 | Device binding |

*A non-qualified self EAA answers these rows as a non-qualified EAA (EW-DM-12-015, -018, -020, , -024 and -030).

## 3 Attestation attributes

The CompanyInfo Attestation is designed to provide a standardized, verifiable representation of a legal entity's business profile attributes, including workforce size 
and structured financial reporting data. This attestation complements the EUCC by providing additional non-core identity attributes required for KYS, KYC, supplier onboarding, 
and risk assessment processes.

Attributes are defined here in an encoding-independent manner (EW-DM-12-007). The
authoritative encoding lives in the machine-readable schema artefacts referenced in
section 3.1, not in this document. Do not paste schema fragments into the prose; they
will drift.

### 3.1 Introduction

**Data Model:**

The attestation structure is defined as a structured object with a nested array of financial facts:

```
CompanyInfo
├─ legal_entity (M)
│   ├─ legal_person  (M)
│   │   ├─ legal_person_name (tstr) (M)
│   │   ├─ legal_form_type (tstr) (M)
│   ├─ identifier  (M)                          // At least one identifier required
│   │   ├─ euid (str) (O)                       // European Unique Identifier
│   │   ├─ lei (str) (O)                        // Legal Entity Identifier per ISO 17442
│   │   ├─ tax (str) (O)                        // National tax or registration number    
│   │   ├─ gln (str) (O)                        // Global Location Number for legal entities, GS1 identifier
│   │   ├─ duns (str) (O)                       // Data Universal Numbering System, Dun & Bradstreet identifier
│   │   ├─ eori (str) (O)                       // Economic Operators Registration and Identification number, EU customs identifier
│   │   ├─ bpnl (str) (O)                       // Business Partner Number Legal entity, Catena-X identifier per ICD 0243
│   │   ├─ siren (str) (O)                      // Système d'Identification du Répertoire des ENtreprises, French company identifier
├─ number_of_employees  (String) (M)            // ex. less than 5, 52, 100 -> string   
├─ trade_alias [tstr] (O)                       // optional attributes 
├─ previous_legal_name [tstr] (O)     
└─ financial_statements (O)                     //optional 
    ├─ taxonomy (tstr) (M)
    └─ facts [1..n]
        ├─ id (tstr) (M)
        ├─ concept(tstr) (M) 
        ├─ value (number) (M)
        ├─ unit (tstr) (M)
        ├─ period_start (date) (M)
        └─ period_end((date) (M)
```
*Note*: M - mandatory / O - optional.

**Explanation:**
The `Legal_Entity` object **SHALL** appear exactly once and contains:
- `Legal_Person`, the official legal name and legal form of the entity issuing the attestation.
- `Identifier`, the EUID (mandatory) and optionally LEI and/or tax registration number.
- `number_of_employees` is mandatory top-level attributes.
- `trade_alias` and `previous_legal_name` are optional and may contain zero or more text values.
- `financial_statements` is a optional nested object containing the reporting taxonomy and at least one financial fact.
- Each `Fact` in the `facts` array is a self-contained reported financial data point with its own concept, value, unit, and reporting period.

**Attestation Classification:**

This attestation type MAY be classified as:
- **"EAA"** self-issued by the legal entity as part of its disclosures.
- **"QEAA"** issued by a Qualified Trust Service Provider (QTSP) or authorized competent body that can independently attest the company information (e.g., based on official company register data or audited financial statements).

**Schema artefacts**

| Format | Identifier | Schema artefact | Version | Location |
| --- | --- | --- | --- | --- |
| SD-JWT VC | `eu.we-build:companyinfo:1` | JSON schema | TODO: confirm schema version | `../data-schemas/sd-jwt/` |

The schema artefacts referenced above are normative for encoding. Where this
document and a referenced artefact disagree, the artefact prevails for encoding
questions and this document prevails for semantics, presence and disclosure rules.

TODO / Consistency issue: the source data model calls the mandatory workforce
attribute `number_of_employees`, while the mandatory attribute table calls it
`employee_number`. Align the logical model, schema and tables before publication.

TODO / Consistency issue: `trade_alias` and `previous_legal_name` appear in both
the mandatory and optional attribute sections. Their intended presence requirement
must be resolved.

### 3.2 Mandatory attributes

#### 3.2.1 CompanyInfo Top-Level Attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| employee_number | [numberOfEmployees](https://w3id.org/ebwv#numberOfEmployees) | Total number of employees in the legal entity at the time of reporting | uint |
| trade_alias | [alternativeName](https://w3id.org/ebwv#alternativeName) | Registered trade names or aliases under which the legal entity operates | Array of tstr |
| previous_legal_name | [previousLegalName](https://w3id.org/ebwv#previousLegalName) | Previously registered legal name(s) of the entity | Array of tstr |

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| legal_person_name | , | The complete official legal name of the legal entity | String |
| legal_form_type | , | The legal form of the legal entity (e.g., SA, GmbH, Ltd, BV) | String |

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| taxonomy | [conformsToTaxonomy](https://w3id.org/ebwv#conformsToTaxonomy) | Financial reporting standard used (e.g., IFRS, GAAP) | String |
| facts | [qb:dataSet](http://purl.org/linked-data/cube#dataSet) (inverse of) | List of reported financial facts | Array [Fact] |

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| `identifier` | , | A structured object of legal entity identifiers; at least one sub-field **SHALL** be provided. | Object |


| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| id | [dcterms:identifier](http://purl.org/dc/terms/identifier) | Unique identifier of the fact | String |
| concept | [observedMetric](https://w3id.org/ebwv#observedMetric) | Name of the reported metric (e.g., Revenue, NetIncome) | String |
| value | [sdmx-measure:obsValue](http://purl.org/linked-data/sdmx/2009/measure#obsValue) | Reported value of the fact | Decimal |
| unit | [sdmx-concept:unitMeasure](http://purl.org/linked-data/sdmx/2009/concept#unitMeasure) | Unit of measurement (e.g., EUR, %, shares) | String (ISO 4217 for currencies) |
| period_start | [dcat:startDate](https://www.w3.org/ns/dcat#startDate) | Start date of the reporting period | ISO 8601 (YYYY-MM-DD) |
| period_end | [dcat:endDate](https://www.w3.org/ns/dcat#endDate) | End date of the reporting period | ISO 8601 (YYYY-MM-DD) |

### 3.3 Optional attributes

**LegalPersonIdentifier Optional Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| euid | , | European Unique Identifier per Directive (EU) 2017/1132. | String |
| lei | , | Legal Entity Identifier (LEI) per ISO 17442. | String |
| tax | , | National tax or company registration number. | String |
| gln | , | Global Location Number for legal entities (GS1 identifier). | String |
| duns | , | Data Universal Numbering System (Dun & Bradstreet identifier). | String |
| eori | , | Economic Operators Registration and Identification number (EU customs). | String |
| bpnl | , | Business Partner Number Legal entity (Catena-X identifier). | String |
| siren | , | Système d'Identification du Répertoire des ENtreprises (French identifier). | String |

**Main Object**

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| trade_alias | [alternativeName](https://w3id.org/ebwv#alternativeName) | Registered trade names or aliases under which the legal entity operates. MAY contain zero or more text values. | Array of tstr |
| previous_legal_name | [previousLegalName](https://w3id.org/ebwv#previousLegalName) | Previously registered legal name(s) of the entity, as recorded in official company registers prior to the current legal name. MAY contain zero or more text values. | Array of tstr |

**financial_statements Optional Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| financial_statements | ... | financial_statements | Object |
| financial_statements.taxonomy | -- | Financial reporting standard used (e.g., IFRS, GAAP) | String |
| financial_statements.facts | -- | List of reported financial facts | Array [Fact] |
| financial_statements.facts[n].id | --- | Unique identifier of the fact | String |
| financial_statements.facts[n].concept | --- | Name of the reported metric (e.g., Revenue, NetIncome) | String |
| financial_statements.facts[n].value | --- | Reported value of the fact | Decimal |
| financial_statements.facts[n].unit | --- | Unit of measurement (e.g., EUR, %, shares) | String (ISO 4217 for currencies) |
| financial_statements.facts[n].period_start | --- | Start date of the reporting period | ISO 8601 (YYYY-MM-DD) |
| financial_statements.facts[n].period_end | --- | End date of the reporting period | ISO 8601 (YYYY-MM-DD) |

### 3.4 Conditional attributes

No conditional attributes are defined for this attestation type. All attributes are either mandatory or optional as specified above.

## 4 Metadata

Metadata describes the attestation rather than its subject.

### 4.1 Mandatory metadata

| **Data Identifier** | **Definition** | **Data type** |
| --- | --- | --- |
| category | Legal category of the CompanyInfo Attestation | String |
| cnf | Cryptographic Key Binding | String |

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| issuance_date | [cred:validFrom](https://www.w3.org/2018/credentials/#validFrom) | The date and time when the attestation was issued (ISO 8601) | DateTime |
| expiry_date | [cred:validUntil](https://www.w3.org/2018/credentials/#validUntil) | The date and time when the attestation expires (ISO 8601) | DateTime |
| issuing_entity | [cred:issuer](https://www.w3.org/2018/credentials/#issuer) | The identifier of the legal entity that issued the attestation (typically the subject entity itself for self-issued attestations, or the QTSP identifier for QEAA) | String |
| category | [attestationLegalCategory](https://w3id.org/ebwv#attestationLegalCategory) | Legal category of this attestation; for S-EAA use `eaa:eu:non-qualified` | String |
| vct |  | A URI or other collision-resistant identifier that defines the type of the SD-JWT Verifiable Credential | String |

**Legal category.** The current template uses the `category` attribute defined in
[ETSI TS 119 472-1]. For this S-EAA, the value is `eaa:eu:non-qualified`;
ETSI TS 119 472-1 has no separate value for self-issued EAA. The superseded
`attestation_legal_category` attribute SHALL NOT be used.

TODO / Consistency issue: the source encoding table still uses
`attestation_legal_category`. The encoding table and example payload must be aligned
with `category` before publication.

### 4.2 Optional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** |
| --- | --- | --- | --- |
| trust_anchor_url | cred:? | URL where the trust anchor for verifying this attestation can be retrieved | URI |
| schema_version | cred:? | Version of the schema used | String |

### 4.3 Conditional metadata

No conditional metadata elements are defined for this attestation type.

### 4.4 Code lists

#### 4.4.1 Currency Codes

The `unit` attribute within each `Fact` object, when representing a monetary value, SHALL follow **ISO 4217** currency codes.

| **Example Code** | **Definition** |
| --- | --- |
| EUR | Euro |
| USD | United States Dollar |
| GBP | Pound Sterling |
| CHF | Swiss Franc |

No standardized EU value lists apply to `employee_number` or `trade_alias`.

#### 4.4.2 Financial Taxonomy Codes

The `taxonomy` attribute SHOULD use one of the following standardized values:

| **Code** | **Definition** |
| --- | --- |
| IFRS | International Financial Reporting Standards |
| US-GAAP | United States Generally Accepted Accounting Principles |
| LOCAL-GAAP | Local Generally Accepted Accounting Principles (country-specific) |
| OECD | OECD reporting framework |

#### 4.4.3 Concept Codes

The `concept` attribute SHOULD use one of the following standardized values:

#### 4.4.4 Financial Fact Concept Codes

The `concept` attribute within each `Fact` object SHALL use one of the following standardized values:

**a. Income Statement (P&L)**

| **Code** | **Definition** |
| --- | --- |
| Revenue | Total income from sales of goods/services |
| Turnover | Total sales revenue generated by the company over a specific period |
| CostOfSales | Direct costs of producing goods/services |
| GrossProfit | Revenue minus cost of sales |
| OperatingExpenses | Costs for running business operations |
| EBIT | Earnings before interest and tax |
| NetIncome | Final profit after all expenses and taxes |

**b. Balance Sheet**

| **Code** | **Definition** |
| --- | --- |
| Assets | Total resources owned by the company |
| CurrentAssets | Short-term assets (cash, receivables, etc.) |
| NonCurrentAssets | Long-term assets (property, equipment) |
| Liabilities | Total obligations of the company |
| CurrentLiabilities | Short-term debt and obligations |
| Equity | Shareholder value in the company |

**c. Cash Flow Statement**

| **Code** | **Definition** |
| --- | --- |
| OperatingCashFlow | Cash generated from operations |
| InvestingCashFlow | Cash used/invested in assets |
| FinancingCashFlow | Cash from financing activities |
| NetCashFlow | Total change in cash position |

**d. Financial Ratios / KPIs**

| **Code** | **Definition** |
| --- | --- |
| EBITDA | Earnings before interest, taxes, depreciation, and amortization |
| GrossMargin | Profitability ratio of gross profit |
| NetMargin | Net income as percentage of revenue |
| DebtToEquity | Leverage ratio |

#### 4.4.5 Fiscal Year Format

Fiscal year, as referenced in the `period_start` and `period_end` attributes, SHALL follow the Gregorian calendar year format (**YYYY**) for year identification, with full ISO 8601 date representation (YYYY-MM-DD) for period boundaries.

### 4.5 Integrity rules

The following integrity rules SHALL be enforced:
- `Legal_Entity` **SHALL** appear exactly once and **SHALL** contain `legal_person_name`, `legal_form_type`, and at least one identifier.
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
- `category` **SHALL** be `eaa:eu:non-qualified` for this S-EAA.

## 5 Formats

| Format | Supported | Identifier | Specification | Notes |
| --- | --- | --- | --- | --- |
| ISO/IEC 18013-5 mdoc | no |  | [ISO/IEC 18013-5] | Out of scope, see section 5.2 |
| SD-JWT VC | yes | see section 5.1 | [SD-JWT VC], [HAIP] |  |
| W3C VCDM | no |  | [W3C VCDM v2.0] | Not defined in this version, see section 5.3 |

### 5.1 SD-JWT VC-based encoding

The CompanyInfo attestation uses the SD-JWT VC format to allow for selective disclosure of company attributes.

**Selective Disclosure:** Top-level claims (`employee_number`, `trade_alias`, `previous_legal_name`, `financial_statements`) SHALL be individually selectively disclosable, enabling a legal entity to disclose only the attributes requested by a Relying Party.

The `.` notation is used to indicate the nesting of attributes.

**Verifiable Credential Type (`vct`):** `eu.we-build:companyinfo:1`

#### 5.1.1 Attribute Encoding Table

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Reference/Notes** | **Disclosable** |
| --- | --- | --- | --- | --- |
| **Legal Entity** |  |  |  |  |
| legal_person_name | `legal_entity.legal_person.legal_person_name` | string | The complete official legal name of the company | MUST |
| legal_form_type | `legal_entity.legal_person.legal_form_type` | string | Legal form of the company (e.g., GmbH, S.A., Ltd.) | MUST |
| **Legal Entity Identifier** |  |  |  |  |
| euid | `legal_person.identifier.euid` | String | European Unique Identifier, optional sub-field | MUST |
| lei | `legal_person.identifier.lei` | String | Legal Entity Identifier per ISO 17442, optional sub-field | MUST |
| tax | `legal_person.identifier.tax` | String | National tax or registration number, optional sub-field | MUST |
| gln | `legal_person.identifier.gln` | String | Global Location Number for legal entities, optional sub-field | MUST |
| duns | `legal_person.identifier.duns` | String | Dun & Bradstreet company identifier, optional sub-field | MUST |
| eori | `legal_person.identifier.eori` | String | EU customs identifier, optional sub-field | MUST |
| bpnl | `legal_person.identifier.bpnl` | String | Catena-X BPNL identifier per ICD 0243, optional sub-field | MUST |
| siren | `legal_person.identifier.siren` | String | French company identifier (SIREN), optional sub-field | MUST |
| number_of_employees | `number_of_employees` | Integer (uint) | Total number of employees at time of reporting; SHALL be non-negative | MUST |
| trade_alias | `trade_alias` | Array of Strings | Zero or more registered trade names/aliases; optional | MUST |
| previous_legal_name | `previous_legal_name` | Array of Strings | Zero or more previously registered legal names; optional | MUST |
| **financial_statements** |  |  |  |  |
| financial_statements.taxonomy | `financial_statements.taxonomy` | String | Financial reporting standard used (e.g., IFRS, GAAP) | MUST |
| financial_statements.facts | `financial_statements.facts` | Array [Fact] | List of reported financial facts; at least one fact SHALL be present | MUST |
| **facts** |  |  |  |  |
| financial_statements.facts.id | `financial_statements.facts[n].id` | String | Unique identifier of the fact within the attestation | MUST |
| financial_statements.facts.concept | `financial_statements.facts[n].concept` | String | Name of the reported metric (e.g., Revenue, Turnover, NetIncome, TotalAssets) | MUST |
| financial_statements.facts.value | `financial_statements.facts[n].value` | Decimal (number) | Reported numeric value of the fact | MUST |
| financial_statements.facts.unit | `financial_statements.facts[n].unit` | String (ISO 4217 for currencies) | Unit of measurement (e.g., EUR, %, ratio) | MUST |
| financial_statements.facts.period_start | `financial_statements.facts[n].period_start` | String (ISO 8601 YYYY-MM-DD) | Start date of the reporting period | MUST |
| financial_statements.facts.period_end | `financial_statements.facts[n].period_end` | String (ISO 8601 YYYY-MM-DD) | End date of the reporting period | MUST |
| **Metadata** |  |  |  |  |
| issuance_date | `iat` | Number (Unix timestamp) | Date and time when the attestation was issued (ISO 8601); RFC 7519 | MUST NOT |
| expiry_date | `exp` | Number (Unix timestamp) | Date and time when the attestation expires (ISO 8601); RFC 7519 | MUST NOT |
| issuing_entity | `iss` | String (URI or DID) | Identifier of the competent institution that issued the attestation; RFC 7519 | MUST NOT |
| category | `category` | String | `eaa:eu:non-qualified` for this S-EAA | MUST NOT |
| vct | `vct` | String | The vct definition | MUST NOT |
| cnf | `cnf` | String | Cryptographic Key Binding | MUST NOT |
| trust_anchor_url | `trust_anchor_url` | String (URI) | URL where the trust anchor for verifying this attestation can be retrieved; optional | MAY |
| schema_version | `schema_version` | String | Version of the schema used; optional | MAY |

**Notes:**

- **MUST**: The claim SHALL be selectively disclosable, the holder MAY choose to disclose or
  withhold this claim when presenting the credential to a Relying Party.
- **MUST NOT**: The claim SHALL NOT be selectively disclosable, it is always present in plain
  text in the JWT header/payload and cannot be withheld by the holder, as it is required for
  credential verification and trust establishment.
- `financial_statements` facts are marked as `MUST` disclosable as a unit, individual facts
  within the array are not independently selectively disclosable in this version.
- `iat`, `exp`, and `iss` follow RFC 7519 standard JWT claim naming conventions.

#### 5.1.2 Status Claim

For SD-JWT VC-compliant Attestations, the attestation MUST include a `status` claim if  the technical validity period is greater than 24 hours. This claim enables Relying Parties to
determine if a credential has been revoked via a status list mechanism, as specified in SD-JWT VC.

The `status` claim SHALL be a JSON object with the following members:

| **Field** | **Type** | **Value / Constraint** |
| --- | --- | --- |
| `type` | String | SHALL be `"status-list"` |
| `status_list_credential` | String (URI) | URI of the Status List Credential document containing the status bitstring |
| `status_list_index` | Integer (>= 0) | Zero-based index into the status list bitstring for this credential |
| `status_purpose` | String | SHALL be `"revocation"` |

**Example:**

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
#### 5.1.3 Example Payload
The following example shows the payload of the attestation in SD-JWT VC format before the encoding into the SD-JWT format.
```
{
  "vct": "eu.we-build:companyinfo:1",
  "category": "eaa:eu:non-qualified",
  "iss": "https://issuer.example.com",
  "iat": "2025-01-15T10:00:00Z",
  "exp": "2026-01-15T10:00:00Z",
  "issuing_entity": "did:example:legal-entity-123",
  "schema_version": "1.0",
 
  "legal_entity": {
    "legal_person": {
      "legal_person_name": "Example GmbH",
      "legal_form_type": "GmbH"
    },
    "identifier": {
      "euid": "DE1212.HRB123456",
      "tax": "DE123456789"
    }
  },
  "number_of_employees": "1250",
  
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
Sample payloads are provided under ../data-schemas/sd-jwt/sample-data/company-info-sd-jwt-sample.json

### 5.2 ISO/IEC 18013-5-compliant encoding

ISO/IEC 18013-5 (also called mdoc) is out of scope for this Rulebook, as offline proximity presentation is not a current requirement for the CompanyInfo attestation.

### 5.3 W3C Verifiable Credentials Data Model-based encoding

This Rulebook does not define a W3C Verifiable Credentials Data Model encoding for this attestation type.

## 6 Protocols

This chapter identifies the protocols used to issue and present this attestation.
The substantive issuance rules are in chapter 7 and the presentation rules are in
chapter 9.

### 6.1 Issuance

This attestation is issued using OpenID for Verifiable Credential Issuance
[OpenID4VCI], as profiled by [HAIP].

### 6.2 Presentation

This attestation is presented using OpenID for Verifiable Presentations [OpenID4VP].
Only remote presentation is in scope, consistent with chapter 5, which records the
mdoc encoding as out of scope.

## 7 Issuance

### 7.1 Holder Key Binding at Issuance (Wallet Binding)

This is a fundamental security requirement that prevents credential theft and
ensures an attestation is bound to a specific wallet. Where the attestation is
device-bound, the Holder's wallet **MUST** perform a proof-of-possession challenge
to prove control of the corresponding private key. The Attestation Provider then
embeds the corresponding public key into the attestation before signing it.


| Field | Value | Source |
| --- | --- | --- |
| Device-bound | MAY | EW-DM-12-038 |
| Cryptographically bound to | none | EW-DM-12-032 |
| Relying Party must also verify a PID | no | EW-DM-12-031 |
| Binding subject | legal person |  |

### 7.2 Issuance Policy

An Issuance Policy defines the minimum rules, policies and procedures that any
compliant Attestation Provider **SHALL** follow when issuing attestations of this
type.

The Provider **SHALL** issue the attestation based on information and supporting
documentation that is valid and accurate at the moment of issuance. An issuance
timestamp (`iat` in SD-JWT VC) **MUST** be included. The Provider is responsible
for the ongoing accuracy of the attested information and **MUST** revoke the
attestation when a change affects the validity or accuracy of the underlying data.

For this S-EAA, the issuer is the legal entity itself. It issues CompanyInfo based
on company-owned or self-asserted information and supporting documentation
available at issuance.

The Issuer SHALL implement the base issuer obligation as defined in the Issuer
Obligation specification:
https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-base/verifier-base-verification.md#41-issuer-obligations

**Authorized Authentic Sources:** For the S-EAA path, the source rulebook does
not designate a single external authentic source for all CompanyInfo attributes.
Financial statements and company records are examples of supporting information,
but no stronger source requirement is inferred here.

**Attestation Lifecycle:** The issuer sets the validity period and reissues the
attestation when underlying facts change.

**Batch Issuance Designation:** TODO: determine whether batch issuance is
permitted, prohibited or not applicable for CompanyInfo.

**Attestation-Specific Obligations:** Selective-disclosure and format requirements
in chapters 3 and 5 apply.

TODO / Consistency issue: the source also defines a QEAA issuance path based on
official company-register data or audited financial statements. Confirm whether
that should be maintained as a separate rulebook/profile.

### 7.3 Lifecycle management

The issuer sets the validity period of the attestation and reissues it when the
underlying facts change, revoking the superseded attestation as described in chapter 8.

### 7.4 Embedded disclosure policy

| Field | Value |
| --- | --- |
| Policy present | no |
| Common policy applied | none |
| Encoding | pending upstream specification |

No embedded disclosure policy is defined for this attestation type.

## 8 Revocation

This attestation is revocable and SHALL remain valid only while its underlying
information is accurate, complete and legally effective.

**Revocation mechanism**

- The issuer must maintain an active status list aligned with the applicable
  Attestation Status List mechanism.
- The status information in every issued CompanyInfo attestation shall reference
  the status-list URI and the credential-specific index.
- Only the self-issuing legal entity may modify the status entry for this S-EAA.

**Revocation triggers and business rules**

The self-issuing legal entity is under an obligation to update or revoke its S-EAA
when underlying CompanyInfo facts change in a way that affects the validity or
accuracy of the attestation, including changes to company profile or reported
financial information.

A revoked or suspended attestation must be treated as invalid for
credential-validity purposes by Relying Parties. Business interpretation remains
subject to the Relying Party's internal compliance policies.

TODO: Expected time from revocation trigger to status-list update is not specified
by the source rulebook.

# 9. Request, Presentation and Verification

To verify and validate a received presentation of an attestation of this type,
the following steps SHALL be performed:

1. **Cryptographic Integrity Verification (Tamper Proof):** The Verifier **MUST**
   verify that the received attestation data has not been altered or tampered with
   since issuance, using a trusted public key obtained according to chapter 10.
2. **Issuer Authentication and Trust Evaluation:** The Verifier **MUST** verify
   the identity and trust status of the Attestation Provider.
3. **Temporal Validity Verification:** The Verifier **MUST** verify that the
   attestation is within its stated validity window.
4. **Revocation Status Verification:** The Verifier **MUST** verify revocation
   status as described in chapter 8 unless an applicable exception applies.
5. **Holder Wallet and Device Binding Verification:** Where the attestation is
   device-bound according to section 7.1, the Verifier **MUST** verify the Holder's
   presentation signature and binding.

## 9.1 Relying Party Role (RP Instance - EUDI Wallet)

The Relying Party SHALL perform the base attestation verification process defined
in the Base Verification specification:
https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-base/verifier-base-verification.md#42-relying-party-obligations

No additional CompanyInfo-specific EUDI-Wallet verification obligations are
defined in the source rulebook.

## 9.2 EBW Relying Party Role (EBW Wallet - EBW Wallet)

Following the principle of mutual identification, verification in the European
Business Wallet ecosystem is a mutual cryptographic process. When an EBW Owner
receives a presented attestation, it verifies the attestation before providing a
service or executing a transaction. Before releasing confidential, non-public
CompanyInfo data, the Holder verifies the identity and system integrity of the
requesting Relying Party.

### 9.2.1 Relying Party obligation during request

When requesting non-public and confidential CompanyInfo data, the Relying Party
**SHALL** include its own EBWOID and BWUA in the presentation request to support
mutual identification, authorisation and wallet-integrity checks.

The Relying Party **SHALL** request only attributes strictly necessary for the
stated business purpose. Where Relying Party registration is required, it
**SHALL** request only attributes it is registered and authorised to request.

### 9.2.2 Holder and Relying Party obligation during verification

Holder and Relying Party verification applies the five generic verification steps
at the beginning of this chapter. The EBW Wallet Provider **MUST** support the
cryptographic verification required to perform those checks.

No additional CompanyInfo-specific EBW verification obligations are defined in
the source rulebook.

### 9.3 Presentation modes

Remote presentation is in scope. Proximity presentation is not in scope,
consistent with chapter 5, where mdoc is out of scope.

### 9.4 Transactional data

No transactional data as defined in Topic 20 of Annex 2 of the ARF is associated
with this attestation type.

## 10 Trust Framework

The trust anchor for this attestation is obtained according to the S-EAA /
non-qualified EAA trust model.

### 10.1 Relying Party Role (RP Instance - EUDI Wallet)

The trust anchor is not obtained from a Trusted List of qualified trust service
providers. It is obtained as follows: **[CONSORTIUM DEFAULT MECHANISM, TO AGREE]**.
Authorisation of the Provider to issue this attestation type is then verified by
**[PROCEDURE]**.

A Wallet Unit MAY verify Provider authorisation using the mechanism described in
ISSU_34 of Topic 10 of Annex 2 of the ARF.

### 10.2 EBW Relying Party Role (EBW Wallet - EBW Wallet)

#### 10.2.1 Attestation Chaining

For this category, trust is established through a delegated trust model chaining
back to a qualified credential. The EAA Provider **MUST** embed its own EBWOID
credential, or the applicable reference/chain, in the issued EAA.

The Relying Party **MUST** verify the EBWOID. The verified EBWOID provides the
Provider's public `signing_key`, which becomes the direct trust anchor used to
verify the CompanyInfo S-EAA signature.

The trust chain is:

**TLoL -> QTSP -> EAA Provider's EBWOID -> EAA Provider's Signing Key -> EAA**

Following successful cryptographic verification, authorisation of the Provider to
issue CompanyInfo is a business-level decision for the Relying Party based on its
internal policies and trust lists.

#### 10.2.2 QSEAL

TODO: to be described.

#### 10.2.3 Additional trust mechanism

TODO: to be defined according to ADR#336.

**Trust anchor location**

The metadata carrying the trust anchor location contains at least the URL at
which a machine-readable version can be found or looked up. The attribute named
here SHALL be the same attribute declared in chapter 4.

**Deployment profile**

For the EBW deployment, CompanyInfo uses the EBWOID chaining model above.

TODO: The source rulebook also contains QEAA/PKI trust material. Because this
migration declares CompanyInfo as S-EAA, the QEAA branch is not treated as an
active deployment path. Confirm whether a separate QEAA profile is required.

## 11 References

| **Item Reference** | **Standard name/details** |
| --- | --- |
| [ETSI TS 119 461] | Policy and security requirements for trust service components providing identity proofing of trust service subjects |
| [ETSI TS 119 471] | Policy and security requirements for EAA service providers |
| [ETSI TS 119 472-1] | Profiles for Electronic Attestations of Attributes; Part 1 - General requirements |
| [OpenID4VCI] | OpenID for Verifiable Credential Issuance |
| [OpenID4VP] | OpenID for Verifiable Presentations |
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
