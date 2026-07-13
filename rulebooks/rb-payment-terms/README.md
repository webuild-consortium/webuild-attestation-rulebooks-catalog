# Attestation Rulebook for attestations of type Payment Terms

* Author(s):
  * [Florin Coptil, Robert Bosch GmbH]
  * [Dominic Hurni, SBB]
* Previous Authors

* Reviewer(s):
  * [Ricky Lamberty, Robert Bosch GmbH] 

| Version | Date       | Description                                                     |
|---------|------------|-----------------------------------------------------------------|
| 0.1     | 01.05.2026 | Initial draft based on the WeBuild design attestations meetings |
| 0.6     | 29.06.2026 | update layout and review gln                                    |
| 0.9     | 03.07.2026 | Updates in regard trust and revocation                            |

* Contact:
  * [Florin Coptil](mailto:florin.coptil@bosch.com)*

* Feedback:

## 1 Introduction

This attestation addresses the following question:

**What are the agreed financial conditions — including payment due date, currency, and delivery terms — between a buyer and a supplier?**

The Payment Terms Attestation provides a standardized, verifiable representation of the financial conditions agreed between a buyer and a supplier, enabling structured exchange of payment term attributes for use in KYS, KYC, supplier onboarding, financial risk assessment, and regulatory compliance processes

### 1.1 Document Scope and Purpose

Payment terms define the financial conditions under which a buyer settles a transaction with a
supplier. Key elements include:

- **Due Date** — Specifies when the payment must be made (e.g., on delivery, within 30 days
  of invoice, or at a future fixed date).
- **Currency** — Indicates the currency in which the payment will be made, aligning with
  international standards such as ISO 4217 numeric and alphabetic codes.
- **Associated Incoterm** — Connects the payment obligation to delivery and risk transfer terms
  defined by Incoterms 2020, clarifying which party is responsible for costs, shipping, and
  insurance.

Within the Know Your Supplier (KYS) process, payment terms are essential to:

- Mitigate financial risks through clearly defined payment conditions.
- Confirm supplier commitment to meet contractual and currency obligations.
- Ensure alignment with internal policies and regulatory standards.

Integrating payment terms into KYS strengthens financial control, transparency, and overall
supplier due diligence.

**Design Decisions**

This Payment Terms Attestation Rulebook is based on:
- ISO 8601 for date and duration formatting
- ISO 4217 for currency codes
- Incoterms 2020 published by the International Chamber of Commerce (ICC)
- EU Company Certificate (EUCC) framework as the foundational legal identity layer for buyer
  and supplier identification

### 1.2 Document Structure

This Rulebook is structured as follows:

- Chapter 2 describes the Payment Terms attestation attributes and metadata in an
  encoding-independent manner, including the data model.
- Chapter 3 specifies how the attestation attributes and metadata are encoded: Section 3.2
  covers SD-JWT VC-based encoding.
- Chapter 4 specifies attestation usage scenarios, Relying Party obligations, and integration
  with KYS workflows.
- Chapter 5 defines trust anchors and verification mechanisms for issuer authorization.
- Chapter 6 defines revocation mechanisms for the attestation.
- Chapter 7 provides compliance information regarding the EUDI framework and applicable data
  protection laws.

### 1.3 Keywords

This document uses the capitalised keywords `SHALL`, `SHOULD` and `MAY` as specified in
[RFC 2119], i.e. to indicate requirements, recommendations and options specified in this document.

In addition, `must` (non-capitalised) is used to indicate an external constraint, i.e. a
requirement that is not mandated by this document, but, for instance, by an external document.
The word `can` indicates a capability, whereas other words, such as `will`, and `is` or `are`
are intended as statements of fact.

### 1.4 Terminology

*Additional terminology specific to this attestation:*

| Term                    | Description                                                                                                                            |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Payment Terms           | The financial conditions under which a buyer agrees to pay a supplier, including the due date, currency, and associated delivery terms |
| Payment Due             | The number of days within which payment must be made, expressed as a duration in ISO 8601 format (e.g., P30D)                          |
| Incoterm                | International Commercial Terms published by the ICC defining delivery and risk transfer obligations between buyer and seller           |
| Currency                | The monetary unit in which the payment is to be executed, following ISO 4217 alphabetic codes                                          |
| Buyer                   | The party obligated to make payment under the agreed payment terms                                                                     |
| Supplier                | The party entitled to receive payment under the agreed payment terms                                                                   |
| Payment Reference Event | The event that triggers the start of the payment due period (e.g., invoice date, delivery date, order date)                            |
| EUID                    | European Unique Identifier – a standardized identifier for legal entities registered in EU Member States                               |
| LEI                     | Legal Entity Identifier — a global identifier for legal entities per ISO 17442                                                         |
| DUNS                    | Data Universal Numbering System — a nine-digit identifier for business entities                                                        |
| KYS                     | Know Your Supplier – due diligence process for verifying supplier credentials, integrity, and risk exposure                            |
| KYC                     | Know Your Customer – due diligence process for verifying customer identity and assessing risk in financial relationships               |
| ISO 4217                | International standard defining currency codes (e.g., EUR, USD, GBP)                                                                   |
| ISO 8601                | International standard for date, time, and duration representations (e.g., YYYY-MM-DD, P30D)                                           |
| EUCC                    | EU Company Certificate – attestation establishing the legal existence and identity of a legal entity within the EU                     |

## 2 Attestation Attributes and Metadata

The Payment Terms Attestation is designed to provide a standardized, verifiable representation
of the financial conditions agreed between a buyer and a supplier. This attestation enables
structured exchange of payment term attributes for use in KYS, KYC, supplier onboarding,
financial risk assessment, and regulatory compliance processes.

### 2.1 Introduction

Payment terms define the financial conditions under which a buyer settles a transaction with a
supplier. Key elements include:

- **Due Date** — Specifies when the payment must be made (e.g., on delivery, within 30 days of
  invoice, or at a future fixed date).
- **Currency** — Indicates the currency in which the payment will be made, aligning with
  international standards such as ISO 4217 numeric and alphabetic codes.
- **Associated Incoterm** — Connects the payment obligation to delivery and risk transfer terms
  defined by Incoterms 2020, clarifying which party is responsible for costs, shipping, and
  insurance.

The attestation structure is defined as a structured object:

**Data Model:**
```
PaymentTerms
├─ payment_due (M)                          // ISO 8601 duration (e.g., P30D)
├─ currency (M)                             // ISO 4217 alphabetic code
├─ incoterm (M)                             // Incoterms 2020 three-letter ICC code
├─ buyer_identifier (Object) (M            // At least one identifier required
│   ├─ euid (str) (O)                       // European Unique Identifier
│   ├─ lei (str) (O)                        // Legal Entity Identifier per ISO 17442
│   ├─ tax (str) (O)                        // National tax or registration number
│   └─ duns (str) (O)                       // Data Universal Numbering System number
├─ supplier_identifier (object) (M)           // At least one identifier required
│   ├─ euid (str) (O)                       // European Unique Identifier
│   ├─ lei (str) (O)                        // Legal Entity Identifier per ISO 17442
│   ├─ tax (str) (O)                        // National tax or registration number
│   └─ duns (str) (O)                       // Data Universal Numbering System number
├─ agreement_date (M)                       // ISO 8601 date (YYYY-MM-DD)
├─ payment_reference_event (O)              // Enum: invoice_date | delivery_date | order_date | ...
├─ contract_reference (O)                   // Reference to underlying contract or PO
├─ transaction_amount (O)                   // Monetary value of the transaction (Decimal)
└─ delivery_location (O)                    // Agreed delivery location (address or identifier)
```
**Explanation:**

- `payment_due`, `currency`, `incoterm`, `buyer_identifier`, `supplier_identifier`, and
  `agreement_date` are mandatory top-level attributes.
- `payment_reference_event`, `contract_reference`, `transaction_amount`, and
  `delivery_location` are optional attributes.
- The attestation is a flat object — no nested sub-objects are required for the mandatory
  attributes.

**Attestation Classification:**

This attestation type MAY be classified as:
- **"EAA"** when self-issued by the legal entity subject to the payment terms disclosure.

### 2.2 Mandatory attributes

#### 2.2.1 PaymentTerms Attributes

| **Data Identifier** | **Semantic Reference** | **Definition**                                                                              | **Optionality** | **Encoding format**          |
|---------------------|------------------------|---------------------------------------------------------------------------------------------|-----------------|------------------------------|
| payment_due         | --                     | The number of days within which payment must be made, defined as a duration (e.g., P30D)    | M               | ISO 8601 duration (PnD)      |
| currency            | --                     | The currency in which the payment is to be executed, following international standards      | M               | String (ISO 4217)            |
| incoterm            | --                     | The delivery and risk transfer term agreed between buyer and seller                         | M               | String (3-letter ICC code)   |
| buyer_identifier    | --                     | Unique identifier of the buyer party (e.g., EUID, VAT number, or DUNS number)              | M               | String                       |
| supplier_identifier | --                     | Unique identifier of the supplier party (e.g., EUID, VAT number, or DUNS number)           | M               | String                       |
| agreement_date      | --                     | Date when the payment terms were agreed upon                                                | M               | String (ISO 8601 YYYY-MM-DD) |

### 2.3 Optional attributes

| **Data Identifier**     | **Semantic Reference** | **Definition**                                                                                                                         | **Optionality** | **Encoding format**  |
|-------------------------|------------------------|----------------------------------------------------------------------------------------------------------------------------------------|-----------------|----------------------|
| payment_reference_event | --                     | The event that triggers the start of the payment due period (e.g., "invoice_date", "delivery_date", "order_date")                     | O               | Enum (String)        |
| contract_reference      | --                     | Reference to the underlying contract or purchase order                                                                                 | O               | String               |
| transaction_amount      | --                     | The monetary value of the transaction                                                                                                  | O               | Decimal (ISO 4217)   |
| delivery_location       | --                     | The agreed location for delivery of goods or services, specified as a full address or standardized location identifier                 | O               | String (Address)     |

### 2.4 Conditional attributes

No conditional attributes are defined for this attestation type. All attributes are either
mandatory or optional as specified above.

The following conditionality rules apply to identifier objects:

| **Condition** | **Rule** |
|---------------|----------|
| `buyer_identifier` is present | At least one of `euid`, `lei`, `tax`, or `duns` SHALL be populated |
| `supplier_identifier` is present | At least one of `euid`, `lei`, `tax`, or `duns` SHALL be populated |
| `buyer_identifier` and `supplier_identifier` | SHALL NOT be identical within the same attestation |

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

#### 2.8.1 Incoterm Codes

The `incoterm` attribute SHALL use one of the following standardized values as defined by
**Incoterms 2020** (International Chamber of Commerce):

| **Code**  | **Description**                | **Mode of Transport**  |
|-----------|--------------------------------|------------------------|
| `EXW`     | Ex Works                       | Any                    |
| `FCA`     | Free Carrier                   | Any                    |
| `CPT`     | Carriage Paid To               | Any                    |
| `CIP`     | Carriage and Insurance Paid To | Any                    |
| `DAP`     | Delivered At Place             | Any                    |
| `DPU`     | Delivered Place Unloaded       | Any                    |
| `DDP`     | Delivered Duty Paid            | Any                    |
| `FAS`     | Free Alongside Ship            | Sea / Inland waterway  |
| `FOB`     | Free On Board                  | Sea / Inland waterway  |
| `CFR`     | Cost and Freight               | Sea / Inland waterway  |
| `CIF`     | Cost, Insurance and Freight    | Sea / Inland waterway  |

#### 2.8.2 Currency Codes

The `currency` attribute SHALL follow **ISO 4217** alphabetic currency codes.

| **Example Code** | **Definition**          |
|------------------|-------------------------|
| EUR              | Euro                    |
| USD              | United States Dollar    |
| GBP              | Pound Sterling          |
| CHF              | Swiss Franc             |
| JPY              | Japanese Yen            |
| `CNY`            | Chinese Yuan Renminbi   |
| `SEK`            | Swedish Krona           |
| `NOK`            | Norwegian Krone         |

**Note:** Any valid ISO 4217 alphabetic currency code is permitted. The examples above are non-exhaustive.

#### 2.8.3 Payment Reference Event Codes

The `payment_reference_event` attribute, when present, SHOULD use one of the following
standardized values:

| **Code**          | **Definition**                                                           |
|-------------------|--------------------------------------------------------------------------|
| `invoice_date`    | Payment due period starts from the date of the invoice                   |
| `delivery_date`   | Payment due period starts from the date of delivery of goods or services |
| `order_date`      | Payment due period starts from the date the order was placed             |
| `acceptance_date` | Payment due period starts from the date of formal acceptance of goods    |
| `shipment_date`   | Payment due period starts from the date of shipment                      |

#### 2.8.4 Identifier Type Reference

The following identifier types are supported within `buyer_identifier` and
`supplier_identifier` objects:

| **Identifier** | **Standard**                   | **Format**                                   | **Description**                                             |
|----------------|--------------------------------|----------------------------------------------|-------------------------------------------------------------|
| `euid`         | EU Digital Identity Regulation | Country code + registry code + entity number | European Unique Identifier for EU-registered legal entities |
| `lei`          | ISO 17442                      | 20 alphanumeric characters                   | Global Legal Entity Identifier                              |
| `tax`          | National                       | Country-specific                             | National tax or company registration number                 |
| `duns`         | Dun & Bradstreet               | 9-digit numeric                              | Data Universal Numbering System identifier                  |

### 2.9 Integrity Rules

The following integrity rules SHALL be enforced:

| **Rule ID**  | **Rule**                                                                                                          |
|--------------|-------------------------------------------------------------------------------------------------------------------|
| IR-01        | `payment_due` SHALL be expressed as a valid ISO 8601 duration (e.g., `P30D` for 30 days)                          |
| IR-02        | `payment_due` SHALL represent a non-negative duration                                                             |
| IR-03        | `currency` SHALL be a valid ISO 4217 alphabetic currency code (3 uppercase letters)                               |
| IR-04        | `incoterm` SHALL be a valid Incoterms 2020 three-letter code as defined in Section 2.8.1                          |
| IR-05        | `buyer_identifier` SHALL contain at least one non-empty identifier: `euid`, `lei`, `tax`, or `duns`               |
| IR-06        | `supplier_identifier` SHALL contain at least one non-empty identifier: `euid`, `lei`, `tax`, or `duns`            |
| IR-07        | `buyer_identifier` and `supplier_identifier` SHALL NOT be identical within the same attestation                   |
| IR-08        | `agreement_date` SHALL be a valid ISO 8601 date in `YYYY-MM-DD` format                                            |
| IR-09        | `agreement_date` SHALL NOT be a future date at time of attestation issuance                                       |
| IR-10        | `transaction_amount`, if provided, SHALL be a non-negative decimal value                                          |
| IR-11        | `payment_reference_event`, if provided, SHALL use one of the enumerated values defined in Section 2.8.3           |
| IR-12        | `delivery_location`, if provided, SHALL be a non-empty string representing a valid address or location identifier |
| IR-13        | Each attribute SHALL appear at most once in the attestation                                                       |
| IR-14        | `lei` identifiers SHALL conform to the 20-character ISO 17442 format                                              |

---

## 3 Attestation encoding

### 3.1 ISO/IEC 18013-5-compliant encoding

ISO/IEC 18013-5 (also called mdoc) is out of scope for this Rulebook, as offline proximity
presentation is not a current requirement for the Payment Terms attestation.

### 3.2 SD-JWT VC-based encoding

The Payment Terms attestation uses the SD-JWT VC format to allow for selective disclosure of
payment term attributes.

**Selective Disclosure:** Top-level claims (`payment_due`, `currency`, `incoterm`,
`buyer_identifier`, `supplier_identifier`, `agreement_date`, `payment_reference_event`,
`contract_reference`, `transaction_amount`, `delivery_location`) SHALL be individually
selectively disclosable, enabling a legal entity to disclose only the attributes requested by a
Relying Party.

The `.` notation is used to indicate the nesting of attributes.

**Verifiable Credential Type (`vct`):** `eu.we-build:paymentterms:1`

#### 3.2.1 Attribute Encoding Table

| **Data Identifier**          | **Attribute Identifier**     | **Encoding Format**          | **Reference / Notes** | **Disclosable** |
|------------------------------|------------------------------|------------------------------|-----------------------|-----------------|
| `payment_due`                | `payment_due`                | String (ISO 8601 PnD)        | Non-negative duration; SHALL be a valid ISO 8601 duration | MUST |
| `currency`                   | `currency`                   | String (ISO 4217)            | Valid 3-letter ISO 4217 alphabetic currency code | MUST |
| `incoterm`                   | `incoterm`                   | String (3-letter ICC code)   | Valid Incoterms 2020 code — see Section 2.8.1 | MUST |
| `agreement_date`             | `agreement_date`             | String (ISO 8601 YYYY-MM-DD) | SHALL NOT be a future date at issuance | MUST |
| **Buyer Identifier**         |                              |                              | | |
| `buyer_identifier`           | `buyer_identifier`           | Object                       | At least one of `euid`, `lei`, `tax`, `duns` SHALL be present | MUST |
| `buyer_identifier.euid`      | `buyer_identifier.euid`      | String                       | European Unique Identifier of the buyer — optional | MAY |
| `buyer_identifier.lei`       | `buyer_identifier.lei`       | String (20 characters)       | LEI per ISO 17442 — optional | MAY |
| `buyer_identifier.tax`       | `buyer_identifier.tax`       | String                       | National tax or registration number — optional | MAY |
| `buyer_identifier.duns`      | `buyer_identifier.duns`      | String                       | DUNS number of the buyer — optional | MAY |
| **Supplier Identifier**      |                              |                              | | |
| `supplier_identifier`        | `supplier_identifier`        | Object                       | At least one of `euid`, `lei`, `tax`, `duns` SHALL be present | MUST |
| `supplier_identifier.euid`   | `supplier_identifier.euid`   | String                       | European Unique Identifier of the supplier — optional | MAY |
| `supplier_identifier.lei`    | `supplier_identifier.lei`    | String (20 characters)       | LEI per ISO 17442 — optional | MAY |
| `supplier_identifier.tax`    | `supplier_identifier.tax`    | String                       | National tax or registration number — optional | MAY |
| `supplier_identifier.duns`   | `supplier_identifier.duns`   | String                       | DUNS number of the supplier — optional | MAY |
| **Optional Attributes**      |                              |                              | | |
| `payment_reference_event`    | `payment_reference_event`    | String (Enum)                | Triggers payment due period; SHALL use values from Section 2.8.3 — optional | MUST |
| `contract_reference`         | `contract_reference`         | String                       | Reference to underlying contract or purchase order — optional | MUST |
| `transaction_amount`         | `transaction_amount`         | Decimal (number)             | Non-negative monetary value — optional | MUST |
| `delivery_location`          | `delivery_location`          | String (Address)             | Full address or standardized location identifier — optional | MUST |
| **Metadata**                 |                              |                              | | |
| `issuance_date`               | `iat`                                                  | Number (Unix timestamp)     | Date and time when the attestation was issued (ISO 8601); RFC 7519                    | MUST NOT           |
| `expiry_date`                 | `exp`                                                  | Number (Unix timestamp)     | Date and time when the attestation expires (ISO 8601); RFC 7519                       | MUST NOT           |
| `issuing_entity`              | `iss`                                                  | String (URI or DID)         | Identifier of the competent institution that issued the attestation; RFC 7519         | MUST NOT           |
| `attestation_legal_category`  | `attestation_legal_category`                           | String                      | One of "EAA" or "QEAA" as defined by eIDAS 2                                          | MUST NOT           |
| `vct`                         | `vct`                                                  | String                      | The vct definition                                                                    | MUST NOT           |
| `cnf`                         | `cnf`                                                  | String                      | Cryptographic Key Binding                                                             | MUST NOT           |
| `schema_version`              | `schema_version`                                       | String                      | Version of the schema used; optional                                                  | MAY                |
| `trust_anchor_url`            | `trust_anchor_url`                                     | String (URI)                | URL where the trust anchor for verifying this attestation can be retrieved; optional  | MAY                |

**Notes:**

- **MUST**: The claim SHALL be selectively disclosable — the holder MAY choose to disclose or
  withhold this claim when presenting the credential to a Relying Party.
- **MUST NOT**: The claim SHALL NOT be selectively disclosable — it is always present in plain
  text in the JWT header/payload and cannot be withheld by the holder, as it is required for
  credential verification and trust establishment.
- `iat`, `exp`, and `iss` follow RFC 7519 standard JWT claim naming conventions.

#### 3.2.2 Status Claim

For SD-JWT VC-compliant Ownership Attestations, the attestation MUST include a `status` claim
if the technical validity period is greater than 24 hours. This claim enables Relying Parties
to determine if a credential has been revoked via a status list mechanism.

The `status` claim SHALL be a JSON object with the following members:

| **Field**                | **Type**       | **Value**                                       |
|--------------------------|----------------|-------------------------------------------------|
| `type`                   | String         | SHALL be `"status-list"`                        |
| `status_list_credential` | String (URI)   | URI of the Status List Credential document      |
| `status_list_index`      | Integer (>= 0) | Zero-based index into the status list bitstring |
| `status_purpose`         | String         | SHALL be `"revocation"`                         |

**Example:**

```json
{
  "status": {
 "type": "status-list",
 "status_list_credential": "https://issuer.example.com/status/paymentterms/2025",
 "status_list_index": 789,
 "status_purpose": "revocation"
  }
}
```
#### 3.2.3 Example Payload
The following is a non-normative example of a Payment Terms SD-JWT VC payload:
```
{
  "vct": "eu.we-build.paymentterms.1",
  "iss": "https://issuer.example.com",
  "iat": 1736935200,
  "exp": 1768471200,
  "issuing_entity": "did:example:legal-entity-456",
  "issuing_country": "DE",
  "attestation_legal_category": "EAA",
  "schema_version": "1.0",
  "trust_anchor_url": "https://trust.webuildconsortium.eu/anchors/eidas-tl",

  "payment_due": "P30D",
  "currency": "EUR",
  "incoterm": "DAP",
  "buyer_identifier": "DE-HRB-123456",
  "supplier_identifier": "NL-KVK-987654",
  "agreement_date": "2025-01-10",
  "payment_reference_event": "invoice_date",
  "contract_reference": "PO-2025-00123",
  "transaction_amount": 250000.00,
  "delivery_location": "Hauptstraße 12, 10115 Berlin, Germany",

  "status": {
    "type": "status-list",
    "status_list_credential": "https://issuer.example.com/status/paymentterms/2025",
    "status_list_index": 789,
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
Sample payloads are provided under ../data-schemas/sd-jwt/sample-data/payment-terms-sd-jwt-sample.json

### 3.3 W3C Verifiable Credentials Data Model-based encoding

## 4 Attestation usage

### 4.1. Issuance process ###
**For EAA (Self-Issued / Standard Issuance)**:
- The issuer (i.e., the legal entity itself) issues the attestation based on the information and supporting documentation available at the time of issuance.
- The issuer is responsible for ensuring that the attested information remains accurate and must immediately revoke the attestation if any change occurs that affects the validity or accuracy of the underlying data.

- The Issuer SHALL implement the base issuer obligation as defined in the Issuer Obligation specification:
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

| **Item Reference**                       | **Standard name/details**                                                                                                                                                                                                                                                                         |
|------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [European Digital Identity Regulation]   | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework                          |
| [HAIP]	                                  | Yasuda, K. et al, OpenID4VC High Assurance Interoperability Profile, OpenId Foundation, Version draft-03                                                                                                                                                                                          |
| [IANA-JWT-Claims]	                       | IANA JSON Web Token Claims Registry. Available: https://www.iana.org/assignments/jwt/jwt.xhtml                                                                                                                                                                                                    |
| [ICC Incoterms 2020]	                    | International Chamber of Commerce, Incoterms® 2020. Available: https://iccwbo.org/business-solutions/incoterms-rules/incoterms-2020/                                                                                                                                                              |
| [ISO/IEC 18013-5]	                       | ISO/IEC 18013-5, Personal identification — ISO-compliant driving licence - Part 5: Mobile driving licence (mDL) application, First edition, 2021-09                                                                                                                                               |
| [ISO 4217]	                              | ISO 4217 — Currency codes. Available: https://www.iso.org/iso-4217-currency-codes.html                                                                                                                                                                                                            |
| [ISO 8601]                               | 	ISO 8601 — Date and time format. Available: https://www.iso.org/iso-8601-date-and-time-format.html                                                                                                                                                                                               |
| [OIDC]	                                  | Sakimura, N. et al., "OpenID Connect Core 1.0", OpenID Foundation. Available: https://openid.net/specs/openid-connect-core-1_0.html                                                                                                                                                               |
| [RFC 2119]	                              | RFC 2119 — Key words for use in RFCs to Indicate Requirement Levels, S. Bradner, March 1997                                                                                                                                                                                                       |
| [RFC 3339]	                              | RFC 3339 — Date and Time on the Internet: Timestamps, G. Klyne et al., July 2002                                                                                                                                                                                                                  |
| [RFC 7519]	                              | RFC 7519 — JSON Web Token (JWT), M. Jones et al., May 2015                                                                                                                                                                                                                                        |
| [RFC 8610]	                              | RFC 8610 — Concise Data Definition Language (CDDL): A Notational Convention to Express Concise Binary Object Representation (CBOR) and JSON Data Structures, H. Birkholz et al., June 2019                                                                                                        |
| [RFC 8943]	                              | RFC 8943 — Concise Binary Object Representation (CBOR) Tags for Date, M. Jones et al., November 2020                                                                                                                                                                                              |
| [RFC 8949]	                              | RFC 8949 — Concise Binary Object Representation (CBOR), C. Bormann et al., December 2020                                                                                                                                                                                                          |
| [SD-JWT VC]                              | 	SD-JWT-based Verifiable Credentials (SD-JWT VC). Available: https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/, version draft-ietf-oauth-sd-jwt-vc-09                                                                                                                                  |
| [Topic 7] 	                              | ARF Annex 2 - Topic 7 - Attestation revocation and revocation checking. Available: https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a237-topic-7-attestation-revocation-and-revocation-checking |
