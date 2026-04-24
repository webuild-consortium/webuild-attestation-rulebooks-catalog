# WE BUILD Rulebook for attestations of type _eReceipt_

## Abstract

An **eReceipt** is the digital, cryptographically verifiable equivalent of a paper till receipt. It is issued by a merchant (or its Payment Service Provider) to the customer's EUDI Wallet straight after a card payment, and contains the same information a paper receipt would, in a structured, machine-readable form. The customer can then present it to an employer's expense system, an accounting tool, or a tax authority, and the recipient can verify it without contacting the merchant.

This document is the Rulebook that defines what data goes into an eReceipt, how that data is encoded, how the credential is issued, presented and revoked, and how the trust in the issuer is established. It is structured to follow the EUDI Attestation Rulebook Template and, where relevant, points to the EUDI Architecture and Reference Framework (ARF) for further detail.

- Author(s):
  - Teemu Varpanen, WE BUILD Consortium (WP3)
  - Tomi Rusi, WE BUILD Consortium (WP3)
  - Lal Chandran, iGrant.io, Sweden

| Version | Date       | Description                                                                                                                                                                                                                                                                                                    |
| ------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.0     | 27-02-2026 | Initial version, architecture-first format.                                                                                                                                                                                                                                                                    |
| 2.0     | 03-2026    | Reworded to standard WE BUILD attestation template format (Teemu Varpanen / Tomi Rusi).                                                                                                                                                                                                                        |
| 2.1     | 03-2026    | Added Section 2.5 (Process Scope: Card-Based B2B Expense Management) and scoping paragraphs in Section 1 explicitly referencing the card-payment expense-management process and distinguishing from the IPC attestation.                                                                                       |
| 2.2     | 03-2026    | Review corrections: added `products[].categorization{}` (O/map) to §4.1.3; added Organisational Wallet bullet to lifecycle; added conditional-M note to journey; added M\* footnote to verifications table.                                                                                                    |
| 3.0     | 23-04-2026 | Restructured to align with the WE BUILD v1 Attestation Rulebook Template (Sections 1 to 8), introducing encoding-independent attribute tables, formal Code Lists and Integrity Rules sections, SD-JWT VC and ISO/IEC 18013-5 encoding chapters, and explicit Trust Anchor, Revocation and Compliance sections. |

**Feedback:**

- <https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/issues>

## Table of contents
- [WE BUILD Rulebook for attestations of type _eReceipt_](#we-build-rulebook-for-attestations-of-type-ereceipt)
  - [Abstract](#abstract)
  - [Table of contents](#table-of-contents)
  - [1 Introduction](#1-introduction)
    - [1.1 Document scope and purpose](#11-document-scope-and-purpose)
    - [1.2 Document structure](#12-document-structure)
    - [1.3 Key words](#13-key-words)
    - [1.4 Terminology](#14-terminology)
  - [2 Attestation attributes and metadata](#2-attestation-attributes-and-metadata)
    - [Chapter overview](#chapter-overview)
    - [2.1 Introduction](#21-introduction)
    - [2.2 Mandatory attributes](#22-mandatory-attributes)
    - [2.3 Optional attributes](#23-optional-attributes)
    - [2.4 Conditional attributes](#24-conditional-attributes)
    - [2.5 Mandatory metadata](#25-mandatory-metadata)
    - [2.6 Optional metadata](#26-optional-metadata)
    - [2.7 Conditional metadata](#27-conditional-metadata)
    - [2.8 Code lists](#28-code-lists)
    - [2.9 Integrity rules](#29-integrity-rules)
  - [3 Attestation encoding](#3-attestation-encoding)
    - [3.1 ISO/IEC 18013-5-compliant encoding](#31-isoiec-18013-5-compliant-encoding)
    - [3.2 SD-JWT VC-based encoding](#32-sd-jwt-vc-based-encoding)
      - [3.2.1 IANA-registered claims](#321-iana-registered-claims)
      - [3.2.2 Public names](#322-public-names)
      - [3.2.3 Private names (specific to the eReceipt attestation)](#323-private-names-specific-to-the-ereceipt-attestation)
      - [3.2.4 Illustrative example](#324-illustrative-example)
    - [3.3 W3C Verifiable Credentials Data Model-based encoding](#33-w3c-verifiable-credentials-data-model-based-encoding)
  - [4 Attestation usage](#4-attestation-usage)
    - [4.1 Primary use cases](#41-primary-use-cases)
    - [4.2 Delivery methods](#42-delivery-methods)
    - [4.3 Relying-party obligations](#43-relying-party-obligations)
    - [4.4 Presentation requirements](#44-presentation-requirements)
    - [4.5 Device binding](#45-device-binding)
    - [4.6 Transactional data](#46-transactional-data)
  - [5 Trust anchors](#5-trust-anchors)
  - [6 Revocation](#6-revocation)
  - [7 Compliance](#7-compliance)
  - [8 References](#8-references)

## 1 Introduction

### 1.1 Document scope and purpose

The eReceipt attestation enables a merchant, or a Payment Service Provider (PSP) acting on behalf of the merchant, to issue a verifiable, structured proof of purchase to a Holder's EUDI Wallet following a completed card-based point-of-sale (POS) payment transaction. It expresses, in machine-readable and cryptographically verifiable form, the same real-world
fact that a paper till receipt expresses: that a particular merchant accepted a card payment from a particular cardholder for a particular set of itemised goods or services at a specific date, time and location, and captured the EMV/PSP cryptographic evidence of that transaction.

The attestation is intended for use in both Business-to-Consumer (B2C) and Business-to-Business (B2B) flows, with the primary B2B use case being _expense management_: an employee purchases goods or services (travel, meals, office supplies, etc.) using a personal or corporate card and subsequently submits the receipt for reimbursement, VAT reclaim, or accounting purposes. The eReceipt credential replaces the paper receipt in this process, providing a credential that can be routed directly to an employer's expense system or organisational wallet.

The expected ecosystem actors are:

- **Issuers:** merchants and PSPs/acquirers acting on behalf of merchants.
- **Holders:** natural persons (consumers, employees, company cardholders) holding an Individual EUDI Wallet, or organisations holding an Organisational Wallet (employer expense systems).
- **Relying Parties:** employer expense management systems, organisational wallets, accounting and bookkeeping platforms, tax authorities (for VAT reclaim and ViDA-aligned digital reporting), sustainability reporting systems (for CSRD Scope 3 emissions), and other Relying Parties that need to verify proof of purchase.

This attestation is **distinct from the Invoice Payment Confirmation (IPC) attestation**, which covers structured purchase-to-pay e-invoice flows settled via SEPA Credit Transfer (Peppol / EN 16931 framework). Where the IPC attestation proves that an invoice has been paid, the eReceipt attestation proves that a card transaction took place and captures the itemised POS data at the moment of payment. Where an organisation operates a structured purchase-to-pay flow with Peppol invoices and SEPA Credit Transfers, the IPC attestation applies; where an employee makes an ad-hoc card purchase and seeks reimbursement, the eReceipt attestation applies.

The functional description, actor terminology and field names are aligned with the HeroJSON and CEN/TS 16931-8 semantics, and follow the EWC RFC011 delivery model. The canonical SD-JWT data schema is maintained by the EWC consortium at:

> <https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/data-schemas/ds011-vReceipts.json>

### 1.2 Document structure

This Rulebook is structured as follows:

- **Chapter 2** describes the eReceipt attestation attributes and metadata in an encoding-independent manner, including code lists (Section 2.8) and integrity rules (Section 2.9).
- **Chapter 3** specifies how the attestation attributes and metadata are encoded. The primary encoding is SD-JWT VC (Section 3.2). An informational ISO/IEC 18013-5 mDoc encoding is outlined in Section 3.1. The W3C VCDM v2.0 encoding (Section 3.3) is not currently in scope for this Rulebook.
- **Chapter 4** specifies attestation usage, including delivery methods, presentation scenarios and device-binding requirements.
- **Chapter 5** defines how trust anchors for attestation verification can be obtained.
- **Chapter 6** defines attestation revocation mechanisms.
- **Chapter 7** provides compliance information against the EUDI ARF and the European Digital Identity Regulation.
- **Chapter 8** lists the normative and informative references.

### 1.3 Key words

This document uses the capitalised key words 'SHALL', 'SHOULD' and 'MAY' to indicate, respectively, requirements, recommendations, and options specified in this document.

In addition, 'must' (non-capitalised) is used to indicate an external constraint, that is, a requirement that is not mandated by this document but is imposed by some other document. The word 'can' indicates a capability; other words such as 'will', 'is' and 'are' are statements of fact.

The terms _credential_ and _attestation_ are used interchangeably in this document.

### 1.4 Terminology

This document uses the terminology specified in Annex 1 of the ARF. In addition, the following terms are used with the meaning given here:

- **eReceipt**: the attestation defined by this Rulebook, providing cryptographically verifiable proof of a card-based point-of-sale purchase.
- **Individual Wallet**: an EUDI Wallet Unit held by a natural person.
- **Organisational Wallet**: a Wallet Unit held by a legal person (typically an employer) used to receive, store and process attestations on behalf of the organisation.
- **PSP**: Payment Service Provider, including the acquirer responsible for authorising and settling card transactions on behalf of the merchant.
- **EMV**: the chip-card payment standard governing card-based POS transactions; provides the cryptographic data captured in `verifications[]`.

## 2 Attestation attributes and metadata

### Chapter overview

This chapter lists every piece of data an eReceipt may carry, independent of how it is encoded on the wire. Each attribute is marked as **Mandatory** (the issuer must include it), **Optional** (the issuer may include it), or **Conditional** (the issuer must include it only when a stated condition is met). The actual on-the-wire encoding, including the
exact data types and selective-disclosure rules, is specified later in Chapter 3.

Where an attribute is taken from an external standard (HeroJSON, EN 16931-1, ISO codes, EMV/PSP terminal data, and so on), the _Semantic Reference_ column points to the source. Two extra sections close out the chapter: Section 2.8 lists the controlled vocabularies (code lists) used by the attributes, and Section 2.9 lists the consistency rules
(integrity rules) the issuer must observe.

The eReceipt is, by default, a **non-qualified Electronic Attestation of Attributes (EAA)**. That is reflected in the `attestation_legal_category` attribute (Section 2.2). If a specific issuer is itself a Qualified Trust Service Provider and chooses to issue the eReceipt as a **PuB-EAA**, the value of `attestation_legal_category` SHALL be set to
`"PuB-EAA"` and the issuer SHALL satisfy the additional requirements in Annex VII of the [European Digital Identity Regulation].

### 2.1 Introduction

The eReceipt attestation is a structured credential whose primary objects are the **header** (transaction-level totals and identifiers), the **merchant** (with branch and address sub-objects), the **products** array (line items, each with a per-line VAT breakdown), the receipt-level **vats** array, the **payments** array, the **verifications** array (EMV/PSP
cryptographic evidence binding the credential to the POS transaction), an optional **journey** object (for travel and mobility receipts) and an optional **attachments** array.

The high-level logical model is:

```
eReceipt
├── (Header: type, receiptNumber, receiptTimeStamp, currencyISOCode, totals…)
├── merchant
│   ├── branch
│   └── address
├── products[ ]      ── vats[ ]   (per line)
│                    ── discounts[ ], categorization{ }, customAttributes[ ]
├── vats[ ]          (receipt level)
├── payments[ ]      ── attributes{ } (EMV/PSP)
├── verifications[ ] ── transactionBegin / transactionEnd
├── journey{ }       (optional; origin & destination mandatory if present)
└── attachments[ ]
```

In line with ARB_11/ARB_12 of [Topic 12] and Annex V/VII of the [European Digital Identity Regulation], this Rulebook defines the attribute `attestation_legal_category`, which SHALL have the value `"QEAA"`, `"PuB-EAA"` or `"non-qualified-EAA"`. For the baseline eReceipt profile defined here, the value SHALL be `"non-qualified-EAA"`.

In the following subsections 2.2 to 2.7 the mandatory, optional and conditional attributes and metadata are defined. Sections 2.8 and 2.9 document the code lists and integrity rules that are needed to interpret the attributes consistently.

### 2.2 Mandatory attributes

| **Data Identifier**                         | **Semantic Reference**         | **Definition**                                                                                                                                                          | **Data type** | **Example value**                                                                             |
| ------------------------------------------- | ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | --------------------------------------------------------------------------------------------- |
| `attestation_legal_category`                | WE BUILD Rulebook Template     | Indicates the legal category of the attestation. SHALL be `"QEAA"`, `"PuB-EAA"` or `"non-qualified-EAA"`. For this Rulebook the default value is `"non-qualified-EAA"`. | tstr          | `"non-qualified-EAA"`                                                                         |
| `type`                                      | HeroJSON / CEN/TS 16931-8      | Transaction type. One of: `PURCHASE`, `RETURN`, `PURCHASE_AND_RETURN`.                                                                                                  | tstr          | `"PURCHASE"`                                                                                  |
| `receiptNumber`                             | HeroJSON                       | Merchant-assigned receipt identifier. Unique within the issuing branch.                                                                                                 | tstr          | `"R-2026-04-23-000412"`                                                                       |
| `receiptTimeStamp`                          | ISO 8601 / RFC 3339            | Date and time at which the receipt was issued by the merchant POS.                                                                                                      | tdate         | `"2026-04-23T10:14:32Z"`                                                                      |
| `currencyISOCode`                           | ISO 4217                       | Currency of the transaction.                                                                                                                                            | tstr          | `"EUR"`                                                                                       |
| `totalPriceExcVAT`                          | HeroJSON                       | Total amount of the transaction excluding VAT, expressed in the currency minor unit.                                                                                    | int           | `4250`                                                                                        |
| `totalVATAmount`                            | HeroJSON                       | Total VAT amount across all lines, in the currency minor unit.                                                                                                          | int           | `1020`                                                                                        |
| `totalPriceIncVAT`                          | HeroJSON                       | Total amount including VAT, in the currency minor unit. SHALL equal `totalPriceExcVAT + totalVATAmount`.                                                                | int           | `5270`                                                                                        |
| `merchant.name`                             | EN 16931-1 / HeroJSON          | Legal name of the merchant.                                                                                                                                             | tstr          | `"Acme Retail Oy"`                                                                            |
| `merchant.companyID`                        | EN 16931-1 (Seller identifier) | Merchant company identifier (VAT ID or national register).                                                                                                              | tstr          | `"FI12345678"`                                                                                |
| `branch.id`                                 | HeroJSON                       | Unique identifier of the branch or store.                                                                                                                               | tstr          | `"BR-HEL-001"`                                                                                |
| `branch.posId`                              | HeroJSON                       | Identifier of the point-of-sale terminal.                                                                                                                               | tstr          | `"POS-12"`                                                                                    |
| `branch.name`                               | HeroJSON                       | Name of the branch or store.                                                                                                                                            | tstr          | `"Acme Helsinki Centre"`                                                                      |
| `address.streetAddress`                     | EN 16931-1                     | Street address of the branch.                                                                                                                                           | tstr          | `"Mannerheimintie 10"`                                                                        |
| `address.city`                              | EN 16931-1                     | City of the branch.                                                                                                                                                     | tstr          | `"Helsinki"`                                                                                  |
| `address.zipCode`                           | EN 16931-1                     | Postal/ZIP code of the branch.                                                                                                                                          | tstr          | `"00100"`                                                                                     |
| `address.country`                           | ISO 3166-1 alpha-2             | Country code of the branch.                                                                                                                                             | tstr          | `"FI"`                                                                                        |
| `products[].name`                           | HeroJSON                       | Name or description of the product or service.                                                                                                                          | tstr          | `"Espresso"`                                                                                  |
| `products[].quantity`                       | HeroJSON                       | Quantity purchased. Encoded as a string to preserve precision (e.g. `"1.500"`).                                                                                         | tstr          | `"2"`                                                                                         |
| `products[].quantityCode`                   | UN/ECE Rec 20                  | Unit of measurement code (e.g. `PCS`, `KG`, `LTR`).                                                                                                                     | tstr          | `"PCS"`                                                                                       |
| `products[].unitPriceIncVAT`                | HeroJSON                       | Unit price including VAT, in the currency minor unit.                                                                                                                   | int           | `350`                                                                                         |
| `products[].totalAmountExcVAT`              | HeroJSON                       | Total line amount excluding VAT, in the currency minor unit.                                                                                                            | int           | `565`                                                                                         |
| `products[].totalAmountIncVAT`              | HeroJSON                       | Total line amount including VAT, in the currency minor unit.                                                                                                            | int           | `700`                                                                                         |
| `products[].vats[]`                         | HeroJSON                       | VAT breakdown per line item; see Section 2.2 (Product VAT).                                                                                                             | array         | `[{ "VATRate": "24", "VATAmount": 135, "totalAmountExcVAT": 565, "totalAmountIncVAT": 700 }]` |
| `products[].vats[].VATRate`                 | HeroJSON                       | VAT rate applied to this line item, expressed as a percentage string.                                                                                                   | tstr          | `"24"`                                                                                        |
| `products[].vats[].VATAmount`               | HeroJSON                       | VAT amount for this line item, in the currency minor unit.                                                                                                              | int           | `135`                                                                                         |
| `products[].vats[].totalAmountExcVAT`       | HeroJSON                       | Line amount excluding VAT, in the currency minor unit.                                                                                                                  | int           | `565`                                                                                         |
| `products[].vats[].totalAmountIncVAT`       | HeroJSON                       | Line amount including VAT, in the currency minor unit.                                                                                                                  | int           | `700`                                                                                         |
| `vats[].VATRate`                            | HeroJSON                       | VAT rate at receipt level, expressed as a percentage string.                                                                                                            | tstr          | `"24"`                                                                                        |
| `vats[].totalVATAmount`                     | HeroJSON                       | Total VAT amount at this rate, in the currency minor unit.                                                                                                              | int           | `1020`                                                                                        |
| `vats[].totalAmountExcVAT`                  | HeroJSON                       | Total amount at this rate excluding VAT, in the currency minor unit.                                                                                                    | int           | `4250`                                                                                        |
| `vats[].totalAmountIncVAT`                  | HeroJSON                       | Total amount at this rate including VAT, in the currency minor unit.                                                                                                    | int           | `5270`                                                                                        |
| `payments[].type`                           | HeroJSON                       | Payment method type (e.g. `CARD`, `CASH`, `MOBILEPAY`, `GIFTCARD`).                                                                                                     | tstr          | `"CARD"`                                                                                      |
| `payments[].amount`                         | HeroJSON                       | Amount paid with this payment method, in the currency minor unit.                                                                                                       | int           | `5270`                                                                                        |
| `verifications[].type`                      | EMV / PSP                      | Verification type identifier.                                                                                                                                           | tstr          | `"EMV-AC"`                                                                                    |
| `verifications[].version`                   | EMV / PSP                      | Version of the verification schema used.                                                                                                                                | tstr          | `"1.0"`                                                                                       |
| `verifications[].publicKey`                 | EMV / PSP                      | Public key used for transaction signing, base64url-encoded.                                                                                                             | tstr          | `"MIIBIjANBg…"`                                                                               |
| `verifications[].transactionId`             | EMV / PSP                      | Unique identifier of the POS transaction.                                                                                                                               | tstr          | `"T-20260423-000871"`                                                                         |
| `verifications[].currentType`               | EMV                            | Cryptogram type. One of: `AC` (Authorisation Cryptogram), `DC` (Dynamic Cryptogram).                                                                                    | tstr          | `"AC"`                                                                                        |
| `verifications[].transactionEnd.signedData` | EMV / PSP                      | Signed data captured at transaction end.                                                                                                                                | bstr          | (binary)                                                                                      |

### 2.3 Optional attributes

| **Data Identifier**                 | **Semantic Reference** | **Definition**                                                                                                                                                                     | **Data type** | **Example value**                                                                             |
| ----------------------------------- | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | --------------------------------------------------------------------------------------------- |
| `freeText`                          | HeroJSON               | Free-text field for merchant notes (e.g. promotional message).                                                                                                                     | tstr          | `"Thank you for your purchase!"`                                                              |
| `customAttributes`                  | HeroJSON               | Array of `{key, value}` pairs for merchant-specific receipt-level data.                                                                                                            | array         | `[{ "key": "loyaltyId", "value": "L-9981" }]`                                                 |
| `branch.subName`                    | HeroJSON               | Sub-name or department within the branch.                                                                                                                                          | tstr          | `"Café"`                                                                                      |
| `branch.email`                      | EN 16931-1             | Contact email of the branch.                                                                                                                                                       | tstr          | `"helsinki@acme.fi"`                                                                          |
| `branch.phone`                      | EN 16931-1             | Contact phone of the branch.                                                                                                                                                       | tstr          | `"+358 9 1234 5678"`                                                                          |
| `branch.websiteURL`                 | EN 16931-1             | Website URL of the merchant.                                                                                                                                                       | tstr          | `"https://www.acme.fi"`                                                                       |
| `products[].unitPriceIncVATDecimal` | HeroJSON               | Unit price including VAT in decimal form, for display only.                                                                                                                        | tstr          | `"3.50"`                                                                                      |
| `products[].discounts[]`            | HeroJSON               | Array of discounts applied to this line item.                                                                                                                                      | array         | `[{ "type": "PROMO", "amount": 50 }]`                                                         |
| `products[].EANCode`                | GS1                    | EAN/GTIN barcode of the product.                                                                                                                                                   | tstr          | `"6411400000123"`                                                                             |
| `products[].productId`              | HeroJSON               | Merchant-internal product identifier.                                                                                                                                              | tstr          | `"SKU-ESP-200"`                                                                               |
| `products[].freeText`               | HeroJSON               | Free-text note for this line item.                                                                                                                                                 | tstr          | `"Decaf"`                                                                                     |
| `products[].categorization`         | HeroJSON               | Merchant-defined categorisation object (e.g. category code, department). Structure defined by issuer.                                                                              | map           | `{ "category": "F&B", "department": "Café" }`                                                 |
| `products[].customAttributes[]`     | HeroJSON               | Array of `{key, value}` pairs for merchant-specific line-level data.                                                                                                               | array         | `[{ "key": "warranty", "value": "12m" }]`                                                     |
| `vats[].VATCode`                    | EN 16931-1             | VAT category code (e.g. `S`, `Z`, `E`, `AE`, `K`, `G`, `O`, `L`, `M`).                                                                                                             | tstr          | `"S"`                                                                                         |
| `payments[].handedAmount`           | HeroJSON               | Cash tendered by the customer, in the currency minor unit (cash payments only).                                                                                                    | int           | `6000`                                                                                        |
| `payments[].attributes`             | EMV / PSP              | EMV/PSP payment attributes. Supported sub-fields: `AID`, `TVR`, `TSI`, `AC`, `CID`, `CVM`, `authorizationCode`, `transactionId`, `terminalId`, `maskedPAN`, `APP`, `ENTRY`, `ARC`. | map           | `{ "AID": "A0000000031010", "maskedPAN": "411111******1111", "authorizationCode": "AB12CD" }` |
| `journey.id`                        | WE BUILD Journey model | Journey or booking identifier.                                                                                                                                                     | tstr          | `"BK-7781"`                                                                                   |
| `journey.distance`                  | WE BUILD Journey model | Distance travelled, in metres.                                                                                                                                                     | int           | `184000`                                                                                      |
| `journey.duration`                  | WE BUILD Journey model | Duration of the journey, in minutes.                                                                                                                                               | int           | `92`                                                                                          |
| `journey.CO2Emissions`              | CSRD Scope 3           | CO₂ emissions for this journey, in grams.                                                                                                                                          | int           | `12500`                                                                                       |
| `attachments[].description`         | HeroJSON               | Human-readable description of the attachment.                                                                                                                                      | tstr          | `"Boarding pass"`                                                                             |
| `attachments[].validUntil`          | ISO 8601 / RFC 3339    | Expiry date/time of the attachment.                                                                                                                                                | tdate         | `"2026-04-24T08:00:00Z"`                                                                      |

### 2.4 Conditional attributes

| **Data Identifier**                           | **Semantic Reference** | **Definition**                                                                                                                                                                                                                         | **Data type** | **Example value**                                                                                         |
| --------------------------------------------- | ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | --------------------------------------------------------------------------------------------------------- |
| `verifications[].transactionBegin.signedData` | EMV / PSP              | Signed data captured at transaction begin. **REQUIRED when `verifications[].currentType == "AC"`**; otherwise OPTIONAL.                                                                                                                | bstr          | (binary)                                                                                                  |
| `journey`                                     | WE BUILD Journey model | Journey object. **Present only for travel and mobility receipts** (where `journey.type` is one of `TRAIN`, `BUS`, `TAXI`, `FLIGHT`, `FERRY`). When the `journey` object is present, the conditional attributes below SHALL be present. | map           | (see below)                                                                                               |
| `journey.type`                                | WE BUILD Journey model | Mode of transport. **Mandatory if the `journey` object is present.** One of: `TRAIN`, `BUS`, `TAXI`, `FLIGHT`, `FERRY`.                                                                                                                | tstr          | `"TRAIN"`                                                                                                 |
| `journey.origin`                              | WE BUILD Journey model | Origin of the journey, with sub-fields: `name`, `city`, `country`, `latitude`, `longitude`, `datetime`. **Mandatory if the `journey` object is present.**                                                                              | map           | `{ "name": "Helsinki Central", "city": "Helsinki", "country": "FI", "datetime": "2026-04-23T08:00:00Z" }` |
| `journey.destination`                         | WE BUILD Journey model | Destination of the journey, with the same sub-fields as `journey.origin`. **Mandatory if the `journey` object is present.**                                                                                                            | map           | `{ "name": "Tampere", "city": "Tampere", "country": "FI", "datetime": "2026-04-23T09:32:00Z" }`           |
| `attachments[].type`                          | HeroJSON               | Attachment encoding type. **Mandatory if an `attachments[]` entry is present.** One of: `BARCODE`, `QRCODE`.                                                                                                                           | tstr          | `"QRCODE"`                                                                                                |
| `attachments[].kind`                          | HeroJSON               | Attachment purpose. **Mandatory if an `attachments[]` entry is present.** One of: `TICKET`, `RETURN`, `VOUCHER`.                                                                                                                       | tstr          | `"TICKET"`                                                                                                |
| `attachments[].title`                         | HeroJSON               | Title or label for the attachment. **Mandatory if an `attachments[]` entry is present.**                                                                                                                                               | tstr          | `"Boarding pass HEL→TPE"`                                                                                 |
| `attachments[].data`                          | HeroJSON               | Encoded attachment data (string). **Mandatory if an `attachments[]` entry is present.**                                                                                                                                                | tstr          | `"BAR:1234567890ABC…"`                                                                                    |

### 2.5 Mandatory metadata

| **Data Identifier** | **Semantic Reference** | **Definition**                                                                                                                         | **Data type**       | **Example value**                                                |
| ------------------- | ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ---------------------------------------------------------------- |
| `iss`               | JWT (IANA registered)  | Issuer URL. SHALL resolve to the merchant or PSP's OIDC4VCI metadata endpoint.                                                         | tstr                | `"https://issuer.merchant.example"`                              |
| `iat`               | JWT (IANA registered)  | Unix timestamp at which the credential was issued.                                                                                     | int (epoch seconds) | `1745402075`                                                     |
| `exp`               | JWT (IANA registered)  | Unix timestamp at which the credential technically expires.                                                                            | int (epoch seconds) | `1761127275`                                                     |
| `vct`               | SD-JWT VC              | Verifiable Credential Type. SHALL be a URL that uniquely identifies the eReceipt attestation type within the EUDI Wallet ecosystem.    | tstr                | `"https://issuer.merchant.example/credentials/ereceipt/2.2"`     |
| `cnf`               | SD-JWT VC key binding  | Confirmation claim. JSON object containing the JWK of the Holder's public key, used to bind the credential to the Holder's wallet key. | JSON object         | `{ "jwk": { "kty": "EC", "crv": "P-256", "x": "…", "y": "…" } }` |

### 2.6 Optional metadata

| **Data Identifier**          | **Semantic Reference** | **Definition**                                                                                                                                       | **Data type** | **Example value**                                                   |
| ---------------------------- | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ------------------------------------------------------------------- |
| `status_list`                | IETF Token Status List | Status list object enabling the Relying Party to check whether the credential has been revoked. See Chapter 6.                                       | JSON object   | `{ "idx": 17, "uri": "https://issuer.merchant.example/status/v1" }` |
| `cryptographically_bound_to` | ARB_28 ([Topic 12])    | If present, identifies another attestation type (or `vct`) on the same Wallet Unit to which this eReceipt is cryptographically bound. See Chapter 4. | tstr          | `"urn:eudi:pid:1"`                                                  |

### 2.7 Conditional metadata

No conditional metadata is defined for the eReceipt attestation in this version of the
Rulebook.

### 2.8 Code lists

| **Field name**                                | **Allowed values**                                                                                                              | **Meaning**                                                                         | **Source / vocabulary**              | **Notes / extensibility**                                                                                                                           |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`                                        | `PURCHASE`, `RETURN`, `PURCHASE_AND_RETURN`                                                                                     | Nature of the transaction recorded by the receipt.                                  | HeroJSON / CEN/TS 16931-8            | Closed list. New values SHALL only be introduced through a major version of this Rulebook.                                                          |
| `attestation_legal_category`                  | `QEAA`, `PuB-EAA`, `non-qualified-EAA`                                                                                          | Legal category of the attestation under the [European Digital Identity Regulation]. | WE BUILD Rulebook Template           | Closed list.                                                                                                                                        |
| `currencyISOCode`                             | All ISO 4217 alphabetic codes                                                                                                   | Currency in which monetary amounts are expressed.                                   | ISO 4217                             | Open list (governed by ISO).                                                                                                                        |
| `address.country`                             | All ISO 3166-1 alpha-2 codes                                                                                                    | Country of the merchant branch.                                                     | ISO 3166-1                           | Open list (governed by ISO).                                                                                                                        |
| `vats[].VATCode`, `products[].vats[].VATCode` | `S`, `Z`, `E`, `AE`, `K`, `G`, `O`, `L`, `M`                                                                                    | EN 16931-1 duty/tax/fee category codes.                                             | EN 16931-1                           | Closed list (governed by EN 16931-1).                                                                                                               |
| `products[].quantityCode`                     | `PCS`, `KG`, `LTR`, `MTR`, …                                                                                                    | Unit of measurement of the line item quantity.                                      | UN/ECE Recommendation 20             | Open list (governed by UN/ECE).                                                                                                                     |
| `products[].EANCode`                          | Valid EAN-8, EAN-13 or GTIN-14                                                                                                  | Product barcode.                                                                    | GS1                                  | Open list (governed by GS1).                                                                                                                        |
| `payments[].type`                             | `CARD`, `CASH`, `MOBILEPAY`, `GIFTCARD` (typical values)                                                                        | Payment method used to settle the corresponding `payments[].amount`.                | Issuer-defined; common values listed | Extensible. Issuers SHOULD reuse the listed values where applicable; additional values SHOULD be agreed across issuer and verifier implementations. |
| `journey.type`                                | `TRAIN`, `BUS`, `TAXI`, `FLIGHT`, `FERRY`                                                                                       | Mode of transport for travel/mobility receipts.                                     | WE BUILD Journey model               | Closed list. New values SHALL only be introduced through a minor version of this Rulebook.                                                          |
| `verifications[].currentType`                 | `AC`, `DC`                                                                                                                      | EMV cryptogram type. `AC` = Authorisation Cryptogram; `DC` = Dynamic Cryptogram.    | EMV                                  | Closed list.                                                                                                                                        |
| `attachments[].type`                          | `BARCODE`, `QRCODE`                                                                                                             | Encoding format of the attachment payload.                                          | HeroJSON                             | Closed list.                                                                                                                                        |
| `attachments[].kind`                          | `TICKET`, `RETURN`, `VOUCHER`                                                                                                   | Purpose of the attachment.                                                          | HeroJSON                             | Closed list. New values SHALL only be introduced through a minor version of this Rulebook.                                                          |
| `payments[].attributes` keys                  | `AID`, `TVR`, `TSI`, `AC`, `CID`, `CVM`, `authorizationCode`, `transactionId`, `terminalId`, `maskedPAN`, `APP`, `ENTRY`, `ARC` | EMV/PSP terminal data sub-fields.                                                   | EMV / PSP specifications             | Open list; additional EMV-defined keys MAY be added.                                                                                                |

### 2.9 Integrity rules

| **Rule ID** | **Rule statement**                                                                                                                                                                                                                 | **Why it exists**                                                                       | **Where enforced**                                   | **Verifier / issuer behaviour on failure**                                       |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------- | -------------------------------------------------------------------------------- |
| `IR-01`     | `totalPriceIncVAT` SHALL equal `totalPriceExcVAT + totalVATAmount`.                                                                                                                                                                | Guarantees that header totals are internally consistent.                                | Issuer business rules; verifier business validation. | Issuer SHALL reject the receipt; verifier SHALL treat the credential as invalid. |
| `IR-02`     | The sum of `vats[].totalVATAmount` at receipt level SHALL equal `totalVATAmount`.                                                                                                                                                  | Guarantees that the per-rate VAT breakdown reconciles with the receipt-level VAT total. | Issuer business rules; verifier business validation. | Issuer SHALL reject the receipt; verifier SHALL treat the credential as invalid. |
| `IR-03`     | The sum of `payments[].amount` SHALL equal `totalPriceIncVAT`.                                                                                                                                                                     | Guarantees that the recorded payments cover (and do not exceed) the receipt total.      | Issuer business rules; verifier business validation. | Issuer SHALL reject the receipt; verifier SHALL treat the credential as invalid. |
| `IR-04`     | `receiptTimeStamp` SHALL be greater than or equal to the timestamp embedded in `verifications[].transactionEnd.signedData`, where present.                                                                                         | Prevents back-dating of the receipt relative to the underlying POS transaction.         | Issuer business rules; verifier business validation. | Issuer SHALL reject; verifier SHALL flag the credential as untrustworthy.        |
| `IR-05`     | If `verifications[].currentType == "AC"`, then `verifications[].transactionBegin.signedData` SHALL be present.                                                                                                                     | Ensures complete EMV evidence for Authorisation Cryptogram transactions.                | Schema validation; issuer business rules.            | Issuer SHALL reject; verifier SHALL treat the credential as invalid.             |
| `IR-06`     | If `attachments[].validUntil` is present, its value SHALL be later than `receiptTimeStamp`.                                                                                                                                        | Prevents the issuance of attachments that are already expired at issuance time.         | Issuer business rules; verifier business validation. | Issuer SHALL reject; verifier MAY warn the user that the attachment is expired.  |
| `IR-07`     | If the `journey` object is present, both `journey.origin` and `journey.destination` SHALL be present, and `journey.type` SHALL be one of the values listed in Section 2.8.                                                         | Ensures that travel/mobility receipts are interpretable.                                | Schema validation; issuer business rules.            | Issuer SHALL reject; verifier SHALL treat the credential as invalid.             |
| `IR-08`     | When the `push` or `pull` delivery methods (Chapter 4) are used, the endpoint URI SHALL use TLS (HTTPS).                                                                                                                           | Protects credential delivery against on-path attackers.                                 | Issuer/Wallet at delivery time.                      | Wallet SHALL refuse delivery; issuer SHALL surface failure to the user.          |
| `IR-09`     | The `iss` claim SHALL be a URL resolvable to the merchant or PSP's OIDC4VCI metadata endpoint.                                                                                                                                     | Enables a Relying Party to discover and authenticate the issuer.                        | Issuer at issuance; verifier at verification.        | Verifier SHALL reject the credential.                                            |
| `IR-10`     | All monetary amount fields with `int` encoding SHALL be expressed in the currency minor unit (e.g., cents for EUR) and SHALL be non-negative for `PURCHASE` and `PURCHASE_AND_RETURN` types, and MAY be non-positive for `RETURN`. | Avoids ambiguity in currency representation and supports return semantics.              | Issuer business rules.                               | Issuer SHALL reject inconsistent values.                                         |

## 3 Attestation encoding

### 3.1 ISO/IEC 18013-5-compliant encoding

The eReceipt attestation is **not currently profiled** for offline, proximity-based presentation. Consequently, the canonical encoding defined by this Rulebook is SD-JWT VC (Section 3.2), and Schema Providers issuing the eReceipt SHALL use that encoding by default.

This section is provided as **informational guidance** for implementers who wish to issue the eReceipt as an ISO/IEC 18013-5-compliant mdoc, for example in order to support an offline B2B expense capture flow where the Wallet presents the receipt to an organisational verifier without internet access (see ARB_02 in [Topic 12]).

If an mdoc encoding is profiled in a future version of this Rulebook, the following SHALL apply:

- A document type SHALL be defined that is unique within the EUDI Wallet ecosystem (see ARB_05 in [Topic 12]). The reserved value is:

  > `eu.we-build.ereceipt.1`

- The default attribute namespace SHALL be:

  > `eu.we-build.ereceipt.1`

- The CDDL representation types listed in [RFC 8610] (`tstr`, `uint`, `int`, `bstr`, `bool`, `tdate`) SHALL be used. `tstr` SHALL be encoded in UTF-8 per [RFC 8949] and SHALL support the full Unicode range; `tstr` attributes SHALL have a maximum length of 150 characters unless explicitly overridden by this Rulebook. `tdate` attributes SHALL contain a date-time string per [RFC 3339], without fractional seconds and with `Z` as the time offset. `full-date` SHALL be defined as `full-date = #6.1004(tstr)` per [RFC 8943].
- The three canonical CBOR rules from [RFC 8949] Section 4.2 SHALL be applied: integers as small as possible; lengths as short as possible; indefinite-length items made definite-length.

The mapping of the encoding-independent data identifiers in Chapter 2 to mdoc attribute identifiers and namespaces SHALL follow the pattern below. Existing conventions for attribute identifier values and syntaxes SHOULD be considered (see ARB_07 in [Topic 12]). Where this Rulebook defines new attributes that are not part of an EU-wide or sectoral
namespace, they SHALL be defined within the WE BUILD eReceipt domestic namespace (see ARB_10 in [Topic 12]).

| **Data Identifier**          | **Attribute identifier**     | **Encoding format** | **Namespace**            |
| ---------------------------- | ---------------------------- | ------------------- | ------------------------ |
| `attestation_legal_category` | `attestation_legal_category` | tstr                | `eu.we-build.ereceipt.1` |
| `type`                       | `type`                       | tstr                | `eu.we-build.ereceipt.1` |
| `receiptNumber`              | `receipt_number`             | tstr                | `eu.we-build.ereceipt.1` |
| `receiptTimeStamp`           | `receipt_timestamp`          | tdate               | `eu.we-build.ereceipt.1` |
| `currencyISOCode`            | `currency`                   | tstr                | `eu.we-build.ereceipt.1` |
| `totalPriceExcVAT`           | `total_price_exc_vat`        | int                 | `eu.we-build.ereceipt.1` |
| `totalVATAmount`             | `total_vat_amount`           | int                 | `eu.we-build.ereceipt.1` |
| `totalPriceIncVAT`           | `total_price_inc_vat`        | int                 | `eu.we-build.ereceipt.1` |
| `merchant.name`              | `merchant_name`              | tstr                | `eu.we-build.ereceipt.1` |
| `merchant.companyID`         | `merchant_company_id`        | tstr                | `eu.we-build.ereceipt.1` |
| `address.country`            | `address_country`            | tstr                | `eu.we-build.ereceipt.1` |
| …                            | …                            | …                   | …                        |

A complete mdoc mapping table will be included once the offline-presentation profile is formally adopted by the WE BUILD consortium.

> [TODO: PROVIDE A FULL OR PARTIAL mDOC EXAMPLE OF THE ATTESTATION WHEN THE > > mdoc PROFILE IS ADOPTED.]

### 3.2 SD-JWT VC-based encoding

The eReceipt attestation **SHALL** be issued in SD-JWT VC format and SHALL comply with the 'SD-JWT VCs' profile specified in [HAIP] (see ARB_01b in [Topic 12]).

A Verifiable Credential Type (`vct`) SHALL be defined and SHALL be unique within the EUDI Wallet ecosystem (see ARB_05 in [Topic 12]). The base `vct` for this attestation is:

> `https://<domain to be defined>/ereceipt/<version>`

Actual eReceipt attestations issued by a merchant or PSP SHALL use an issuer-specific `vct` URL (e.g., `https://issuer.merchant.example/credentials/ereceipt/2.2`) that extends this base type via the `extends` field of the corresponding Type Metadata Document (Chapter 6 of [SD-JWT VC]).

Versioning of the `vct` follows the `x.y` model:

- **Minor version (y):** backward-compatible changes, such as adding optional attributes, display claims, or new languages.
- **Major version (x):** breaking changes, such as removing or renaming claims, or changes to mandatory fields.

Every claim name used in an eReceipt SHALL fall into one of three groups: (a) an IANA-registered JWT claim (Section 3.2.1), (b) a publicly-defined name reused from another specification such as OpenID Connect or SD-JWT VC (Section 3.2.2), or (c) a private name defined specifically for the eReceipt attestation in this Rulebook (Section 3.2.3).

For every claim, this Rulebook specifies whether the issuer MUST, MAY or MUST NOT make the claim selectively disclosable. Issuers SHALL also publish a Type Metadata Document for the eReceipt attestation type (as defined in Chapter 6 of [SD-JWT VC]), and the Type Metadata Document SHALL include Claim Selective Disclosure Metadata that matches the "Disclosable" column in the tables below.

#### 3.2.1 IANA-registered claims

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Reference / Notes**                                          | **Disclosable** |
| ------------------- | ------------------------ | ------------------- | -------------------------------------------------------------- | --------------- |
| `iss`               | `iss`                    | string              | Standard JWT issuer claim (IANA JWT Claims Registry)           | MUST NOT        |
| `iat`               | `iat`                    | NumericDate         | Standard JWT "issued at" claim (IANA JWT Claims Registry)      | MUST NOT        |
| `exp`               | `exp`                    | NumericDate         | Standard JWT expiry claim (IANA JWT Claims Registry)           | MUST NOT        |
| `cnf`               | `cnf`                    | JSON object         | Holder key binding, used by SD-JWT VC ([SD-JWT VC], Section 4) | MUST NOT        |

#### 3.2.2 Public names

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Reference / Notes**      | **Disclosable** |
| ------------------- | ------------------------ | ------------------- | -------------------------- | --------------- |
| `vct`               | `vct`                    | string              | [SD-JWT VC], Section 3.2.2 | MUST NOT        |
| `status_list`       | `status`                 | JSON object         | IETF Token Status List     | MUST NOT        |

#### 3.2.3 Private names (specific to the eReceipt attestation)

| **Data Identifier**                   | **Attribute identifier**     | **Encoding format** | **Notes**                                                           | **Disclosable**                                              |
| ------------------------------------- | ---------------------------- | ------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------ |
| `attestation_legal_category`          | `attestation_legal_category` | string              | Defined in WE BUILD Rulebook Template                               | MUST NOT                                                     |
| `type`                                | `type`                       | string              | Section 2.2                                                         | MUST                                                         |
| `receiptNumber`                       | `receiptNumber`              | string              | Section 2.2                                                         | MUST                                                         |
| `receiptTimeStamp`                    | `receiptTimeStamp`           | string (ISO 8601)   | Section 2.2                                                         | MUST                                                         |
| `currencyISOCode`                     | `currencyISOCode`            | string              | Section 2.2                                                         | MUST                                                         |
| `totalPriceExcVAT`                    | `totalPriceExcVAT`           | integer             | Section 2.2; minor unit                                             | MUST                                                         |
| `totalVATAmount`                      | `totalVATAmount`             | integer             | Section 2.2; minor unit                                             | MUST                                                         |
| `totalPriceIncVAT`                    | `totalPriceIncVAT`           | integer             | Section 2.2; minor unit                                             | MUST                                                         |
| `freeText`                            | `freeText`                   | string              | Section 2.3                                                         | MAY                                                          |
| `customAttributes`                    | `customAttributes`           | array               | Section 2.3                                                         | MAY                                                          |
| `merchant`                            | `merchant`                   | object              | Section 2.2; container for `name`, `companyID`, `branch`, `address` | MAY (per-claim)                                              |
| `merchant.name`                       | `name`                       | string              | Section 2.2                                                         | MUST                                                         |
| `merchant.companyID`                  | `companyID`                  | string              | Section 2.2                                                         | MUST                                                         |
| `branch`                              | `branch`                     | object              | Section 2.2                                                         | MAY (per-claim)                                              |
| `branch.id`                           | `id`                         | string              | Section 2.2                                                         | MUST                                                         |
| `branch.posId`                        | `posId`                      | string              | Section 2.2                                                         | MUST                                                         |
| `branch.name`                         | `name`                       | string              | Section 2.2                                                         | MUST                                                         |
| `branch.subName`                      | `subName`                    | string              | Section 2.3                                                         | MAY                                                          |
| `branch.email`                        | `email`                      | string              | Section 2.3                                                         | MAY                                                          |
| `branch.phone`                        | `phone`                      | string              | Section 2.3                                                         | MAY                                                          |
| `branch.websiteURL`                   | `websiteURL`                 | string              | Section 2.3                                                         | MAY                                                          |
| `address`                             | `address`                    | object              | Section 2.2                                                         | MAY (per-claim)                                              |
| `address.streetAddress`               | `streetAddress`              | string              | Section 2.2                                                         | MUST                                                         |
| `address.city`                        | `city`                       | string              | Section 2.2                                                         | MUST                                                         |
| `address.zipCode`                     | `zipCode`                    | string              | Section 2.2                                                         | MUST                                                         |
| `address.country`                     | `country`                    | string              | Section 2.2                                                         | MUST                                                         |
| `products`                            | `products`                   | array of objects    | Section 2.2 / 2.3                                                   | MUST (per-element)                                           |
| `products[].name`                     | `name`                       | string              | Section 2.2                                                         | MUST                                                         |
| `products[].quantity`                 | `quantity`                   | string              | Section 2.2                                                         | MUST                                                         |
| `products[].quantityCode`             | `quantityCode`               | string              | Section 2.2                                                         | MUST                                                         |
| `products[].unitPriceIncVAT`          | `unitPriceIncVAT`            | integer             | Section 2.2                                                         | MUST                                                         |
| `products[].unitPriceIncVATDecimal`   | `unitPriceIncVATDecimal`     | string              | Section 2.3                                                         | MAY                                                          |
| `products[].totalAmountExcVAT`        | `totalAmountExcVAT`          | integer             | Section 2.2                                                         | MUST                                                         |
| `products[].totalAmountIncVAT`        | `totalAmountIncVAT`          | integer             | Section 2.2                                                         | MUST                                                         |
| `products[].vats`                     | `vats`                       | array of objects    | Section 2.2                                                         | MUST                                                         |
| `products[].vats[].VATRate`           | `VATRate`                    | string              | Section 2.2                                                         | MUST                                                         |
| `products[].vats[].VATAmount`         | `VATAmount`                  | integer             | Section 2.2                                                         | MUST                                                         |
| `products[].vats[].totalAmountExcVAT` | `totalAmountExcVAT`          | integer             | Section 2.2                                                         | MUST                                                         |
| `products[].vats[].totalAmountIncVAT` | `totalAmountIncVAT`          | integer             | Section 2.2                                                         | MUST                                                         |
| `products[].discounts`                | `discounts`                  | array               | Section 2.3                                                         | MAY                                                          |
| `products[].EANCode`                  | `EANCode`                    | string              | Section 2.3                                                         | MAY                                                          |
| `products[].productId`                | `productId`                  | string              | Section 2.3                                                         | MAY                                                          |
| `products[].freeText`                 | `freeText`                   | string              | Section 2.3                                                         | MAY                                                          |
| `products[].categorization`           | `categorization`             | object              | Section 2.3                                                         | MAY                                                          |
| `products[].customAttributes`         | `customAttributes`           | array               | Section 2.3                                                         | MAY                                                          |
| `vats`                                | `vats`                       | array of objects    | Section 2.2                                                         | MUST (per-element)                                           |
| `vats[].VATRate`                      | `VATRate`                    | string              | Section 2.2                                                         | MUST                                                         |
| `vats[].totalVATAmount`               | `totalVATAmount`             | integer             | Section 2.2                                                         | MUST                                                         |
| `vats[].totalAmountExcVAT`            | `totalAmountExcVAT`          | integer             | Section 2.2                                                         | MUST                                                         |
| `vats[].totalAmountIncVAT`            | `totalAmountIncVAT`          | integer             | Section 2.2                                                         | MUST                                                         |
| `vats[].VATCode`                      | `VATCode`                    | string              | Section 2.3                                                         | MAY                                                          |
| `payments`                            | `payments`                   | array of objects    | Section 2.2                                                         | MUST (per-element)                                           |
| `payments[].type`                     | `type`                       | string              | Section 2.2                                                         | MUST                                                         |
| `payments[].amount`                   | `amount`                     | integer             | Section 2.2                                                         | MUST                                                         |
| `payments[].handedAmount`             | `handedAmount`               | integer             | Section 2.3                                                         | MAY                                                          |
| `payments[].attributes`               | `attributes`                 | object              | Section 2.3                                                         | MAY (per-sub-field)                                          |
| `verifications`                       | `verifications`              | array of objects    | Section 2.2 / 2.4                                                   | MUST NOT (technical proof; required for verifier validation) |
| `verifications[].type`                | `type`                       | string              | Section 2.2                                                         | MUST NOT                                                     |
| `verifications[].version`             | `version`                    | string              | Section 2.2                                                         | MUST NOT                                                     |
| `verifications[].publicKey`           | `publicKey`                  | string              | Section 2.2                                                         | MUST NOT                                                     |
| `verifications[].transactionId`       | `transactionId`              | string              | Section 2.2                                                         | MUST NOT                                                     |
| `verifications[].currentType`         | `currentType`                | string              | Section 2.2                                                         | MUST NOT                                                     |
| `verifications[].transactionBegin`    | `transactionBegin`           | object              | Section 2.4 (conditional)                                           | MUST NOT                                                     |
| `verifications[].transactionEnd`      | `transactionEnd`             | object              | Section 2.2                                                         | MUST NOT                                                     |
| `journey`                             | `journey`                    | object              | Section 2.4 (conditional)                                           | MAY (per-claim)                                              |
| `journey.type`                        | `type`                       | string              | Section 2.4                                                         | MAY                                                          |
| `journey.id`                          | `id`                         | string              | Section 2.3                                                         | MAY                                                          |
| `journey.distance`                    | `distance`                   | integer             | Section 2.3                                                         | MAY                                                          |
| `journey.duration`                    | `duration`                   | integer             | Section 2.3                                                         | MAY                                                          |
| `journey.CO2Emissions`                | `CO2Emissions`               | integer             | Section 2.3                                                         | MAY                                                          |
| `journey.origin`                      | `origin`                     | object              | Section 2.4                                                         | MAY                                                          |
| `journey.destination`                 | `destination`                | object              | Section 2.4                                                         | MAY                                                          |
| `attachments`                         | `attachments`                | array of objects    | Section 2.4                                                         | MAY (per-element)                                            |
| `attachments[].type`                  | `type`                       | string              | Section 2.4                                                         | MAY                                                          |
| `attachments[].kind`                  | `kind`                       | string              | Section 2.4                                                         | MAY                                                          |
| `attachments[].title`                 | `title`                      | string              | Section 2.4                                                         | MAY                                                          |
| `attachments[].data`                  | `data`                       | string              | Section 2.4                                                         | MAY                                                          |
| `attachments[].description`           | `description`                | string              | Section 2.3                                                         | MAY                                                          |
| `attachments[].validUntil`            | `validUntil`                 | string (ISO 8601)   | Section 2.3                                                         | MAY                                                          |
| `cryptographically_bound_to`          | `cryptographically_bound_to` | string              | Section 2.6; per ARB_28 in [Topic 12]                               | MUST NOT                                                     |

#### 3.2.4 Illustrative example

The following non-normative example shows the JWT claim set (before SD-JWT processing) of an eReceipt issued for a small B2B expense purchase (a coffee and a sandwich at an Acme Helsinki Centre café), paid with a corporate card.

```json
{
  "iss": "https://issuer.merchant.example",
  "iat": 1745402075,
  "exp": 1761127275,
  "vct": "https://issuer.merchant.example/credentials/ereceipt/2.2",
  "cnf": { "jwk": { "kty": "EC", "crv": "P-256", "x": "…", "y": "…" } },
  "attestation_legal_category": "non-qualified-EAA",
  "type": "PURCHASE",
  "receiptNumber": "R-2026-04-23-000412",
  "receiptTimeStamp": "2026-04-23T10:14:32Z",
  "currencyISOCode": "EUR",
  "totalPriceExcVAT": 4250,
  "totalVATAmount": 1020,
  "totalPriceIncVAT": 5270,
  "merchant": {
    "name": "Acme Retail Oy",
    "companyID": "FI12345678",
    "branch": {
      "id": "BR-HEL-001",
      "posId": "POS-12",
      "name": "Acme Helsinki Centre",
      "subName": "Café"
    },
    "address": {
      "streetAddress": "Mannerheimintie 10",
      "city": "Helsinki",
      "zipCode": "00100",
      "country": "FI"
    }
  },
  "products": [
    {
      "name": "Espresso",
      "quantity": "2",
      "quantityCode": "PCS",
      "unitPriceIncVAT": 350,
      "totalAmountExcVAT": 565,
      "totalAmountIncVAT": 700,
      "vats": [
        {
          "VATRate": "24",
          "VATAmount": 135,
          "totalAmountExcVAT": 565,
          "totalAmountIncVAT": 700
        }
      ],
      "categorization": { "category": "F&B", "department": "Café" }
    },
    {
      "name": "Sandwich",
      "quantity": "1",
      "quantityCode": "PCS",
      "unitPriceIncVAT": 4570,
      "totalAmountExcVAT": 3685,
      "totalAmountIncVAT": 4570,
      "vats": [
        {
          "VATRate": "24",
          "VATAmount": 885,
          "totalAmountExcVAT": 3685,
          "totalAmountIncVAT": 4570
        }
      ]
    }
  ],
  "vats": [
    {
      "VATRate": "24",
      "totalVATAmount": 1020,
      "totalAmountExcVAT": 4250,
      "totalAmountIncVAT": 5270,
      "VATCode": "S"
    }
  ],
  "payments": [
    {
      "type": "CARD",
      "amount": 5270,
      "attributes": {
        "AID": "A0000000031010",
        "maskedPAN": "411111******1111",
        "authorizationCode": "AB12CD",
        "terminalId": "POS-12",
        "transactionId": "T-20260423-000871"
      }
    }
  ],
  "verifications": [
    {
      "type": "EMV-AC",
      "version": "1.0",
      "publicKey": "MIIBIjANBg…",
      "transactionId": "T-20260423-000871",
      "currentType": "AC",
      "transactionBegin": { "signedData": "<base64url-encoded bytes>" },
      "transactionEnd": { "signedData": "<base64url-encoded bytes>" }
    }
  ],
  "status": { "idx": 17, "uri": "https://issuer.merchant.example/status/v1" }
}
```

In the issued SD-JWT, the disclosable claims listed in Section 3.2.3 are wrapped in `_sd` arrays per [SD-JWT VC]; the non-disclosable claims (`iss`, `iat`, `exp`, `vct`, `cnf`, `status`, `attestation_legal_category`, all of `verifications[]`) appear as plain JWT claims.

> [RULEBOOK AUTHOR TO PROVIDE THE FULL ISSUED SD-JWT (BASE64-ENCODED) AND THE LIST OF
> > DISCLOSURES INCLUDED IN THE EXAMPLE.]

### 3.3 W3C Verifiable Credentials Data Model-based encoding

The W3C VCDM v2.0-based encoding is **out of scope** for the current version of this Rulebook. As noted in ARB_01a of [Topic 12], only a non-qualified EAA may use this format; the eReceipt baseline profile is non-qualified, so this option remains available for future profiling. If, in a future version, this Rulebook adopts a VCDM v2.0 encoding, tables similar to those in Section 3.2 SHALL be defined and the Rulebook SHALL reference a specification, approved by an EU standardisation body or the European Digital Identity Cooperation Group (Article 46e(1) of the [European Digital Identity Regulation]), detailing how a Relying Party can request attributes from such an attestation and how a User can selectively disclose attributes from it (see ARB_04 in [Topic 12]).

## 4 Attestation usage

### 4.1 Primary use cases

The eReceipt attestation is intended for the following scenarios:

- **B2B expense management**: the primary use case. An employee or company cardholder pays at a merchant POS terminal (physical or online) using a personal or corporate card. Within 2 to 4 seconds of payment confirmation, the merchant or PSP issues the eReceipt to the Holder's EUDI Wallet. The employee subsequently presents the eReceipt to their employer's expense management system or organisational wallet, which can verify the credential without contacting the merchant, match it against a corporate-card transaction, and approve reimbursement. The structured product line data supports automated categorisation and policy checks. Note that, particularly in the SME sector, personal cards are widely used for business purchases; the card payer and the buying entity (company) are frequently different parties.
- **VAT reclaim and bookkeeping**: the eReceipt provides itemised VAT amounts per line (`products[].vats[]`) and a receipt-level VAT summary (`vats[]`), enabling direct import into accounting software for VAT reclaim submissions.
- **Tax authority submission and ViDA-aligned digital reporting**: the eReceipt may be presented directly to a tax authority or sustainability reporting system. The `journey` object (Section 2.4) supports CO₂ emission data for travel receipts, supporting CSRD Scope 3 emissions reporting.
- **B2C proof of purchase**: for warranty claims, returns and consumer rights.
- **Cross-border B2B payment verification**, combined with IBAN and LPID attestations.

### 4.2 Delivery methods

In line with EWC RFC011, three delivery methods are supported:

| **Method**          | **Description**                                                                                                                                                                                              |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Embedded (deferred) | Merchant sends a dynamic payment authorisation request (OIDC4VP); the eReceipt is issued after PSP confirmation. The Wallet polls with `transaction_id` until the credential is available.                   |
| Pull                | Merchant generates an eReceipt invitation URI; the Wallet follows the URI to complete OIDC4VCI issuance.                                                                                                     |
| Push                | Merchant pushes the eReceipt to an endpoint resolved via an eAddress controlled by the Holder. Delivery failures SHALL be surfaced to the user (per `IR-08` in Section 2.9, the endpoint URI SHALL use TLS). |

Issuance SHALL use OIDC4VCI (per EWC RFC001) and presentation SHALL use OIDC4VP
(per EWC RFC002).

### 4.3 Relying-party obligations

When processing an eReceipt, a Relying Party SHALL:

- verify the SD-JWT signature using a trust anchor obtained as described in Chapter 5;
- verify the freshness of the credential against `iat`/`exp`;
- verify the Holder's key binding via the `cnf` claim;
- check the credential against the status mechanism described in Chapter 6;
- validate the integrity rules in Section 2.9 (in particular `IR-01` to `IR-07`).

Whether the Relying Party must additionally request and verify a PID (per ARB_27 in
[Topic 12]) depends on the use case:

- For **B2B expense management** flows where the Relying Party is the employer's expense system or organisational wallet, requesting a PID is **NOT REQUIRED** at the receipt level: identification of the employee is established through the corporate authentication context (e.g., SSO into the expense system), and the eReceipt itself is intentionally not bound to the Holder's identity in order to preserve flexibility for personal-card / company-cardholder mismatches (see Section 4.1).
- For **tax authority submission** flows, the Relying Party SHOULD request a PID and bind the eReceipt presentation to the verified holder identity, in line with national tax reporting requirements.
- For **B2C consumer flows** (e.g., warranty claims, returns), the Relying Party MAY request a PID at its discretion.

### 4.4 Presentation requirements

The eReceipt is intended to be presented **online**, using OIDC4VP. Offline / proximity presentation per [ISO/IEC 18013-5] is **not in scope** for this version of the Rulebook (see Section 3.1).

### 4.5 Device binding

An eReceipt **SHALL** be device-bound (see ARB_34 in [Topic 12]). Device binding is expressed via the `cnf` claim defined in Section 2.5, which carries the JWK of the Holder's public key. This allows the Holder to demonstrate possession of the corresponding private key at presentation time and prevents replay of a copied credential by another party.

The eReceipt **MAY** be cryptographically bound to another attestation type on the same Wallet Unit. When such binding is required by the issuer or by a use-case profile, the optional metadata `cryptographically_bound_to` (Section 2.6) SHALL be included.

> EXAMPLE: where a tax authority requires the eReceipt to be bound to the PID of the
> Holder, the value of `cryptographically_bound_to` would be set to `"urn:eudi:pid:1"`
> (or, equivalently, to the PID `vct` value).

In all other cases, the `cryptographically_bound_to` metadata is OMITTED, and the eReceipt remains bound only to the Holder's wallet key via `cnf`.

### 4.6 Transactional data

The eReceipt itself records transactional data (the `payments[]` and `verifications[]` arrays) as part of its core payload. No additional transactional-data signing requirement under [Topic 20] of Annex 2 of the ARF applies to the _presentation_ of the eReceipt: the credential is consumed as evidence of a past transaction rather than as authorisation of a new one.

## 5 Trust anchors

For the **non-qualified EAA** profile defined here (see ARB_26 in [Topic 12]), the trust anchor that a Relying Party uses to verify an eReceipt is obtained as follows:

- The `iss` claim of the eReceipt (Section 2.5) SHALL be a URL resolvable to the merchant or PSP's OIDC4VCI metadata endpoint (per `IR-09` in Section 2.9).
- The OIDC4VCI metadata SHALL publish the issuer's signing key(s) (or a JWKS URI from which they can be retrieved) and SHALL identify the issuer using a domain name that the Relying Party can validate via TLS (X.509 server certificate from a publicly-trusted CA).
- The Relying Party uses the published key(s) as the trust anchor for verifying the signature of the eReceipt SD-JWT.
- In addition, a Wallet Unit MAY use the EWC trust framework registry (when available) to verify that the issuer is an authorised eReceipt provider (per ISSU_34 in [Topic 10]).

If, in a future version of this Rulebook, the eReceipt is profiled as a **PuB-EAA** issued by a QTSP, the standard ARF mechanism applies: the Relying Party Instance verifies the signature of the PuB-EAA Provider over the eReceipt using a PuB-EAA Provider certificate issued by a QTSP, and verifies that certificate against the corresponding trust anchor from the QTSP Trusted List. Intermediate signing certificates may be used by both the PuB-EAA Provider and the QTSP.

> [!NOTE]
> The eReceipt provides three layers of assurance between the receipt data and the underlying payment: (i) EMV cryptographic evidence captured in `verifications[]`, which proves that a genuine terminal event occurred at the stated merchant, terminal and timestamp; (ii) issuer-side integrity rules `IR-01`, `IR-02` and `IR-03` (Section 2.9), which reconcile line items, VAT and payments against the receipt total; and (iii) process-level assurance that issuance occurs only after the PSP or acquirer has confirmed settlement (Section 2.3). An independent cryptographic binding between the PSP-confirmed authorised amount and the receipt total is not defined in this version of the Rulebook. Cross-verification against a separate Payment Data Confirmation attestation (DS-008) is under consideration for a future revision, and Relying Parties with heightened assurance requirements (for example, tax authorities performing VAT deduction verification) should take this limitation into account.

## 6 Revocation

(See [Topic 7] of the ARF for the high-level requirements related to revocation.)

The eReceipt attestation is a record of a past transaction and is therefore **typically not revoked** in normal operation. However, because the attestation may be presented over extended periods (for VAT reclaim and tax submissions, this may be several years), the eReceipt is **defined as revocable** rather than short-lived.

The following mechanism SHALL be used:

- **Token Status List**: the issuer SHALL maintain a Token Status List, and the optional metadata `status_list` (Section 2.6) SHALL be populated in every issued eReceipt with the list URI and the credential's index. The Status List mechanism follows the IETF Token Status List specification, aligned with the Attestation Status List mechanism that will be specified by the Commission.

Issuers SHALL revoke an eReceipt when:

- the underlying card transaction is reversed or charged back by the acquirer/PSP, in which case the eReceipt MUST be marked revoked;
- the eReceipt was issued in error (for example, where the POS reported a successful payment that the acquirer subsequently rejected); or
- a fraud investigation by the merchant or PSP determines that the receipt does not reflect a genuine transaction.

A revoked eReceipt SHALL be treated as invalid by all Relying Parties.

## 7 Compliance

This Rulebook complies with the EUDI Architecture and Reference Framework (ARF), with the [European Digital Identity Regulation], and with the EUDI Attestation Rulebook Template. In particular:

The structure of this document follows the Attestation Rulebook Template, with the attribute and metadata definitions in Chapter 2, encoding rules in Chapter 3, usage in Chapter 4, trust anchors in Chapter 5, revocation in Chapter 6, and references in Chapter 8.

The high-level requirements for attestation rulebooks (Topic 12 of Annex 2 of the ARF) are met across Chapters 2 to 6: every attribute is defined in an encoding-independent form first; mandatory, optional and conditional attributes are clearly marked; both ISO/IEC 18013-5 and SD-JWT VC encodings are addressed; selective-disclosure metadata is specified per claim; trust-anchor and revocation mechanisms are defined; and any attribute that is not part of an EU-wide namespace is placed in the WE BUILD eReceipt domestic namespace.

The revocation approach in Chapter 6 is aligned with Topic 7 of Annex 2 of the ARF (attestation revocation and revocation checking) and uses a Token Status List approach consistent with the forthcoming Commission Technical Specification on Attestation Status Lists. The issuance approach (Chapter 4 and Chapter 5) is aligned with Topic 10 of Annex 2 of the ARF and with EWC RFC001 (OIDC4VCI) and EWC RFC011 (delivery profile).

The semantics of receipt-level attributes are aligned with HeroJSON, EN 16931-1 and CEN/TS 16931-8; country, currency, date, unit-of-measure and barcode codes are aligned with ISO 3166-1, ISO 4217, ISO 8601, UN/ECE Recommendation 20 and GS1. The
_Semantic Reference_ column in the Chapter 2 tables and the code-list table in Section 2.8 record these alignments per attribute.

The canonical SD-JWT data schema for this attestation is maintained by the EWC consortium at the URL referenced in Section 1.1 and in the [EWC ds011] entry in Chapter 8. Any divergence between this Rulebook and that schema SHALL be resolved in favour of the EWC schema for normative encoding details, and shall be reflected in a subsequent revision of this Rulebook.

## 8 References

| **Item Reference**                     | **Standard name / details**                                                                                                                                                                                                                                                                        |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [European Digital Identity Regulation] | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework.                          |
| [HAIP]                                 | Yasuda, K. _et al,_ OpenID4VC High Assurance Interoperability Profile, OpenID Foundation, Version draft-03.                                                                                                                                                                                        |
| [IANA-JWT-Claims]                      | IANA JSON Web Token Claims Registry. <https://www.iana.org/assignments/jwt/jwt.xhtml>.                                                                                                                                                                                                             |
| [ISO/IEC 18013-5]                      | ISO/IEC 18013-5, Personal identification, ISO-compliant driving licence, Part 5: Mobile driving licence (mDL) application, First edition, 2021-09.                                                                                                                                                 |
| [ISO 3166-1]                           | ISO 3166-1, Codes for the representation of names of countries and their subdivisions, Part 1: Country code.                                                                                                                                                                                       |
| [ISO 4217]                             | ISO 4217, Codes for the representation of currencies.                                                                                                                                                                                                                                              |
| [ISO 8601]                             | ISO 8601, Date and time, Representations for information interchange.                                                                                                                                                                                                                              |
| [EN 16931-1]                           | EN 16931-1, Electronic invoicing, Part 1: Semantic data model of the core elements of an electronic invoice.                                                                                                                                                                                       |
| [CEN/TS 16931-8]                       | CEN/TS 16931-8, Electronic invoicing, Part 8: Use of payment messages in conjunction with electronic invoicing in public procurement.                                                                                                                                                              |
| [HeroJSON]                             | HeroJSON receipt data model, <https://hero.json.com> (informational; field names aligned).                                                                                                                                                                                                         |
| [EWC RFC001]                           | EWC OIDC4VCI Issuance Profile.                                                                                                                                                                                                                                                                     |
| [EWC RFC002]                           | EWC OIDC4VP Presentation Profile.                                                                                                                                                                                                                                                                  |
| [EWC RFC011]                           | EWC eReceipt Issuance and Delivery Profile.                                                                                                                                                                                                                                                        |
| [EWC ds011]                            | EWC canonical SD-JWT schema for the eReceipt attestation: <https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/data-schemas/ds011-vReceipts.json>.                                                                                                                       |
| [OIDC]                                 | Sakimura, N. et al., "OpenID Connect Core 1.0", OpenID Foundation. <https://openid.net/specs/openid-connect-core-1_0.html>.                                                                                                                                                                        |
| [RFC 3339]                             | RFC 3339, Date and Time on the Internet: Timestamps, G. Klyne et al., July 2002.                                                                                                                                                                                                                   |
| [RFC 8610]                             | RFC 8610, Concise Data Definition Language (CDDL): A Notational Convention to Express CBOR and JSON Data Structures, H. Birkholz et al., June 2019.                                                                                                                                                |
| [RFC 8943]                             | RFC 8943, Concise Binary Object Representation (CBOR) Tags for Date, M. Jones et al., November 2020.                                                                                                                                                                                               |
| [RFC 8949]                             | RFC 8949, Concise Binary Object Representation (CBOR), C. Bormann et al., December 2020.                                                                                                                                                                                                           |
| [SD-JWT VC]                            | SD-JWT-based Verifiable Credentials (SD-JWT VC). <https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/>, version draft-ietf-oauth-sd-jwt-vc-09.                                                                                                                                            |
| [Token Status List]                    | IETF OAuth Token Status List specification (work in progress).                                                                                                                                                                                                                                     |
| [Topic 7]                              | ARF Annex 2, Topic 7, Attestation revocation and revocation checking. <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a237-topic-7-attestation-revocation-and-revocation-checking>.            |
| [Topic 10]                             | ARF Annex 2, Topic 10, Issuing a PID or attestation to a Wallet Unit. <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a2310-topic-10-issuing-a-pid-or-attestation-to-a-wallet-unit>.           |
| [Topic 12]                             | ARF Annex 2, Topic 12, Attestation Rulebooks. <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a2312-topic-12-attestation-rulebooks>.                                                           |
| [Topic 20]                             | ARF Annex 2, Topic 20, Strong User authentication for electronic payments. <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a2320-topic-20-strong-user-authentication-for-electronic-payments>. |
| [W3C VCDM v2.0]                        | Sporny, M. _et al,_ Verifiable Credentials Data Model v2.0, W3C Recommendation.                                                                                                                                                                                                                    |
| [UN/ECE Rec 20]                        | UN/ECE Recommendation No. 20, Codes for Units of Measure used in International Trade.                                                                                                                                                                                                              |
| [GS1]                                  | GS1 General Specifications (EAN/GTIN).                                                                                                                                                                                                                                                             |
