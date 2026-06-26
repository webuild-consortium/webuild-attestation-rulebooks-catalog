# WE BUILD Rulebook for attestations of type _eReceipt_

## Abstract

An **eReceipt** is the digital, cryptographically verifiable equivalent of a paper till receipt. It is issued by a merchant (or its Payment Service Provider) to the customer's EUDI Wallet after a payment, and contains the same information a paper receipt would, in a structured, machine-readable form. The customer can then present it to an employer's expense system, an accounting tool, or a tax authority, and the recipient can verify it without contacting the merchant.

This document is designed to be applicable to use cases involving both individual digital identity wallets (EUDIW) and enterprise wallets, named European Business Wallets (EBW).

This document is the Rulebook that defines what data goes into an eReceipt, how that data is encoded, how the eReceipt (or credential) is issued, presented and revoked, and how the trust in the issuer of eReceipt is established. It is structured to follow the EUDI Attestation Rulebook Template and, where relevant, points to the EUDI Architecture and Reference Framework (ARF) for further detail.

- Author(s):
  - Teemu Varpanen, ReceiptHero, Finland
  - Tomi Rusi, Valtiokonttori (State Treasury), Finland
  - Lal Chandran, iGrant.io, Sweden
  - Florin Coptil, Bosch, Germany
  - Sylvie Calsacy, onepoint, France

| Version | Date       | Description                                                                                                                                                                                                                                                                                                    |
| ------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.0     | 27-02-2026 | Initial baseline consolidating earlier drafts: architecture-first format; reworded to the WE BUILD attestation template; Section 2.5 added on Card-Based B2B Expense Management; review corrections (categorization, Organisational Wallet, journey conditional-M, verifications footnote).                    |
| 1.1     | 23-04-2026 | Restructured to align with the WE BUILD v1 Attestation Rulebook Template (Sections 1 to 8): encoding-independent attribute tables, Code Lists and Integrity Rules sections, SD-JWT VC and ISO/IEC 18013-5 encoding chapters, and explicit Trust Anchor, Revocation and Compliance sections.                    |
| 1.2     | 08-05-2026 | Adopted reverse-DNS base `vct` (`eu.we-build.ereceipt.1`); added §3.2.4 ontology binding to the WP4 semantics vocabulary; moved primary use cases to §1.5; restructured Chapter 4 around §4.1 Issuer obligations and §4.2 Relying Party obligations (4.2.1–4.2.5, with TLOL / WUA placeholders).               |
| 1.3     | 02-06-2026 | Amendment to be agnostic on payment means and on customer journey (POS and eCommerce). |
| 1.4     | 18-06-2026 | iGrant.io editorial consolidation and comment resolutions on the live document. |
| 1.5     | 19-06-2026 | RH review pass (tracked changes): instrument-agnostic model completed (`verifications[].type` EMV/OCMF/SCT/SCT-INST; `payments[].type` adds `CREDIT_TRANSFER`); revocation reframed as a technical status mechanism with business handling delegated to the application layer (`originalReceiptNumber` retained, `IR-10` refund signs); Chapter 8 references updated (OpenID4VCI/VP, EWC RFC008/ds008); WE BUILD-specific trust framework and WUA; standards conformance fixes (UN/ECE Rec 20, EN 16931 VAT, GS1); canonical schema realigned to the HeroJSON model (`vct` `eu.we-build.ereceipt.1`), EWC ds011 made informative; CASH and handedAmount removed; SD-JWT VC media type pinned to `dc+sd-jwt` with a worked example added in Section 3.2.5; three SD-JWT VC references corrected to Section 4; journey-agnostic wording (Sections 1.4 and 1.5) and the nested Token Status List status form aligned in final QA. |
| 2.0     | 22-06-2026 | Published release following management and internal review, consolidating revisions 1.3 to 1.5. |

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
    - [1.5 Primary use cases](#15-primary-use-cases)
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
      - [3.2.4 Ontology binding (`extend` attribute)](#324-ontology-binding-extend-attribute)
      - [3.2.5 Illustrative example](#325-illustrative-example)
    - [3.3 W3C Verifiable Credentials Data Model-based encoding](#33-w3c-verifiable-credentials-data-model-based-encoding)
  - [4 Attestation usage](#4-attestation-usage)
    - [4.1 Issuer obligations](#41-issuer-obligations)
      - [4.1.1 Issuer authorisation](#411-issuer-authorisation)
      - [4.1.2 Attestation construction](#412-attestation-construction)
      - [4.1.3 Signing and key management](#413-signing-and-key-management)
      - [4.1.4 Holder binding](#414-holder-binding)
      - [4.1.5 Delivery](#415-delivery)
      - [4.1.6 Lifecycle and revocation](#416-lifecycle-and-revocation)
    - [4.2 Relying Party obligations](#42-relying-party-obligations)
      - [4.2.1 Verify cryptographic integrity](#421-verify-cryptographic-integrity)
      - [4.2.2 Validate issuer](#422-validate-issuer)
        - [4.2.2.1 Authentication](#4221-authentication)
        - [4.2.2.2 Identification](#4222-identification)
        - [4.2.2.3 Authorization](#4223-authorization)
      - [4.2.3 Holder Wallet related check](#423-holder-wallet-related-check)
        - [4.2.3.1 Device binding](#4231-device-binding)
          - [4.2.3.1.1 WUA check](#42311-wua-check)
      - [4.2.4 Holder related check](#424-holder-related-check)
        - [4.2.4.1 Revocation status check](#4241-revocation-status-check)
        - [4.2.4.2 Temporal validity check](#4242-temporal-validity-check)
      - [4.2.5 Use-case dependent identity binding](#425-use-case-dependent-identity-binding)
    - [4.3 Delivery methods](#43-delivery-methods)
    - [4.4 Presentation requirements](#44-presentation-requirements)
    - [4.5 Transactional data](#45-transactional-data)
  - [5 Trust anchors](#5-trust-anchors)
  - [6 Revocation](#6-revocation)
  - [7 Compliance](#7-compliance)
  - [8 References](#8-references)

## 1 Introduction

### 1.1 Document scope and purpose

The eReceipt attestation enables a merchant, or a Payment Service Provider (PSP) acting on behalf of the merchant, to issue a verifiable, structured proof of purchase to a Holder's EUDI Wallet following the completion of an electronic payment transaction. It expresses, in machine-readable and cryptographically verifiable form, the same real-world
fact that a paper till receipt expresses: that a merchant has received a payment from a particular payer for a particular set of itemised goods or services at a specific date, time and location, and has captured the relevant cryptographic and transactional evidence provided by the payment instrument and/or PSP.

The attestation is intended for use in both Business-to-Consumer (B2C) and Business-to-Business (B2B) flows, with the primary B2B use case being _expense management_: an employee purchases goods or services (travel, meals, office supplies, etc.) using an electronic payment instrument (such as a payment card or a credit transfer based on an IBAN) and subsequently submits the receipt for reimbursement, VAT reclaim, or accounting purposes. The eReceipt credential replaces the paper receipt in this process, providing a credential that can be routed directly to an employer's expense system via an organisational wallet or other back-office systems.

The expected ecosystem actors are:

- **Issuers:** merchants and PSPs/acquirers acting on behalf of merchants.
- **Holders:** natural persons (consumers, employees, company representatives) holding an Individual EUDI Wallet, or organisations holding an Organisational Wallet (for example, an employer expense management or back office system) used to receive, store and process eReceipt attestations.
- **Relying Parties:** employer expense management systems, organisational wallets, accounting and bookkeeping platforms, tax authorities (for VAT reclaim and ViDA-aligned digital reporting), sustainability reporting systems (for CSRD Scope 3 emissions), and other Relying Parties that need to verify proof of purchase.

This version of the Rulebook is agnostic to the payment instrument (card or account-to-account credit transfer) and to the customer journey: both in-store (POS) and ecommerce or remote payment flows are in scope (see amendment 1.3).

This attestation is **distinct from the Invoice Payment Confirmation (IPC) attestation**, which covers structured purchase-to-pay e-invoice flows settled via SEPA Credit Transfer (Peppol / EN 16931 framework). Where the IPC attestation proves that an invoice has been paid, the eReceipt attestation proves that an electronic payment transaction has taken place and captures the itemised transaction data at the moment of payment. Where an organisation operates a structured purchase-to-pay flow with eInvoices (Peppol, etc.) and SEPA Credit Transfers, the IPC attestation applies; where an employee or a representative makes an ad-hoc purchase using an electronic payment instrument and seeks reimbursement, the eReceipt attestation applies. Where a credit transfer settles an ad-hoc purchase with no associated structured e-invoice (for example an instant SEPA Credit Transfer at point of sale or in ecommerce checkout), the eReceipt applies and MAY carry `payments[].type` `CREDIT_TRANSFER` with a `verifications[].type` of SCT or SCT-INST; where a structured Peppol or EN 16931 e-invoice exists, the Invoice Payment Confirmation (IPC) attestation applies instead.

The functional description, actor terminology and field names are aligned with the HeroJSON and CEN/TS 16931-8 semantics, and follow the EWC RFC011 delivery model. The canonical data model for this attestation is defined by Chapters 2 and 3 of this Rulebook; a HeroJSON-derived SD-JWT VC schema (`vct` `eu.we-build.ereceipt.1`) is to be published in the WE BUILD attestation catalog. The earlier EWC vReceipt schema [EWC ds011] is informative only (see Chapter 8) and is published at:

> <https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/data-schemas/ds011-vReceipts.json>

### 1.2 Document structure

This Rulebook is structured as follows:

- **Chapter 2** describes the eReceipt attestation attributes and metadata in an encoding-independent manner, including code lists (Section 2.8) and integrity rules (Section 2.9).
- **Chapter 3** specifies how the attestation attributes and metadata are encoded. The primary encoding is SD-JWT VC (Section 3.2). An informational ISO/IEC 18013-5 mDoc encoding is outlined in Section 3.1. The W3C VCDM v2.0 encoding (Section 3.3) is not currently in scope for this Rulebook.
- **Chapter 4** specifies issuer and Relying Party obligations, together with the supporting attestation-usage material (delivery methods, presentation requirements and transactional-data handling).
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

- **Electronic Payment Transaction**: a payment transaction initiated and processed using an electronic payment instrument, including but not limited to payment card transactions and credit transfers based on an IBAN. In the context of this Rulebook, electronic payment transactions occur in in-store (POS), ecommerce and remote payment settings.
- **eReceipt**: the attestation defined by this Rulebook, providing cryptographically verifiable proof of a purchase settled via an electronic payment transaction (for example, a payment card transaction or a credit transfer based on an IBAN), in in-store (POS), ecommerce and remote payment context.
- **Individual Wallet**: an EUDI Wallet Unit held by a natural person, used by the Holder to receive, store and present attestations on their own behalf.
- **Organisational Wallet**: a Wallet Unit held by a legal person (such as a company, public body or non-profit organisation) used to receive, store and process attestations on behalf of the organisation. Organisational Wallets are typically operated by authorised representatives of the organisation and may integrate with back-office systems such as accounting, tax or expense management platforms.
- **European Business Wallet (EBW)**: a specific type of Organisational Wallet, as defined in the relevant EUDI and European Digital Identity framework documents, intended to support cross-border B2B use cases within the EU. In the context of this Rulebook, a European Business Wallet is considered a form of Organisational Wallet capable of receiving, storing and presenting eReceipt attestations on behalf of the legal person.
- **PSP**: Payment Service Provider, including the card acquirer and payment service provider responsible for executing credit transfers on behalf of the merchant.
- **EMV**: the chip-card payment standard governing card-based POS transactions; the card authorisation cryptogram and related terminal data are carried in `payments[].attributes`.

### 1.5 Primary use cases

The eReceipt attestation is intended for the following scenarios:

- **B2B expense management**: the primary use case. An employee or company representative settles an in-store (POS), ecommerce or remote purchase with an electronic payment instrument (for example, a payment card or a credit transfer based on an IBAN). Shortly after payment confirmation, the merchant or PSP issues the eReceipt to the Holder's EUDI Wallet. The employee or representative subsequently presents the eReceipt to their employer's expense management system or organisational wallet (including the European Business Wallet), which can verify the credential without contacting the merchant, match it against a corporate-card transaction record, and approve reimbursement. The structured product line data supports automated categorisation and policy checks. In particular in the SME sector, personal payment instruments are frequently used for business purchases; the payer and the buying entity (company) may be different parties.
- **VAT reclaim and bookkeeping**: the eReceipt provides itemised VAT amounts per line (`products[].vats[]`) and a receipt-level VAT summary (`vats[]`), enabling direct import into accounting software for VAT reclaim submissions.
- **Tax authority submission and ViDA-aligned digital reporting**: the eReceipt may be presented directly to a tax authority or sustainability reporting system. The `journey` object (Section 2.4) supports CO₂ emission data for travel receipts, supporting CSRD Scope 3 emissions reporting.
- **B2C proof of purchase**: for warranty claims, returns and consumer rights.
- **Cross-border B2B payment verification**, combined with IBAN and LPID attestations.

## 2 Attestation attributes and metadata

### Chapter overview

This chapter lists every piece of data an eReceipt may carry, independent of how it is encoded on the wire. Each attribute is marked as **Mandatory** (the issuer must include it), **Optional** (the issuer may include it), or **Conditional** (the issuer must include it only when a stated condition is met). The actual on-the-wire encoding, including the
exact data types and selective-disclosure rules, is specified later in Chapter 3.

Where an attribute is taken from an external standard (HeroJSON, EN 16931-1, ISO codes, EMV/PSP terminal data, and so on), the _Semantic Reference_ column points to the source. Two extra sections close out the chapter: Section 2.8 lists the controlled vocabularies (code lists) used by the attributes, and Section 2.9 lists the consistency rules
(integrity rules) the issuer must observe.

The eReceipt is, by default, a **non-qualified Electronic Attestation of Attributes (EAA)**. That is reflected in the `attestation_legal_category` attribute (Section 2.2). If a specific issuer is itself a Qualified Trust Service Provider and chooses to issue the eReceipt as a **PuB-EAA**, the value of `attestation_legal_category` SHALL be set to
`"PuB-EAA"` and the issuer SHALL satisfy the additional requirements in Annex VII of the [European Digital Identity Regulation].

### 2.1 Introduction

The eReceipt attestation is a structured credential whose primary objects are the **header** (transaction-level totals and identifiers), the **merchant** (with branch and address sub-objects), the **products** array (line items, each with a per-line VAT breakdown), the receipt-level **vats** array, the **payments** array, the **verifications** array (an optional, typed technical proof that the payment event occurred, with its listed sub-fields mandatory once a `verifications[]` entry is present), an optional **journey** object (for travel and mobility receipts) and an optional **attachments** array.

The `payments[]` array carries the payment data shown on the receipt, including any card (EMV) data in `payments[].attributes` (for example the application cryptogram, cryptogramType ARQC, TVR, TSI, AID, CID, CVM and masked PAN). The `verifications[]` array carries an optional, independent, typed proof that the payment event occurred: `verifications[].type` names the standard of that proof (for example EMV, OCMF or a credit-transfer scheme), and the type-specific fields below it apply only for that type.

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
| `products[].quantityCode`                   | UN/ECE Rec 20                  | Unit of measurement code (e.g. `H87` piece, `KGM` kilogram, `LTR` litre).                                                                                                                     | tstr          | `"H87"`                                                                                       |
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
| `payments[].type`                           | HeroJSON                       | Payment method type (e.g. `CARD`, `CREDIT_TRANSFER`, `MOBILEPAY`, `GIFTCARD`).                                                                                                     | tstr          | `"CARD"`                                                                                      |
| `payments[].amount`                         | HeroJSON                       | Amount paid with this payment method, in the currency minor unit. For `RETURN` and `PURCHASE_AND_RETURN` this amount MAY be non-positive (negative).                                                                                                       | int           | `5270`                                                                                        |
| `verifications[].type`                      | EMV / OCMF / EPC SCT/SCT-INST                      | Standard of the technical proof carried in `verifications[]`: EMV for card authorisation cryptograms; OCMF for charge-metering proofs; SCT or SCT-INST for SEPA credit transfer (account-to-account). The EMV cryptogram itself (the AC and its cryptogramType ARQC) is carried in `payments[].attributes`, not here. The type-specific fields below apply only for the named type.                                                                                                                                           | tstr          | `"EMV"`                                                                                    |
| `verifications[].version`                   | Verification profile (per `verifications[].type`)                      | Version of the verification schema used.                                                                                                                                | tstr          | `"1.0"`                                                                                       |
| `verifications[].publicKey`                 | Verification profile (per `verifications[].type`)                      | Public key used for transaction signing, base64url-encoded.                                                                                                             | tstr          | `"MIIBIjANBg…"`                                                                               |
| `verifications[].transactionId`             | Verification profile (per `verifications[].type`)                      | Unique identifier of the underlying payment transaction, as assigned by the PSP or payment scheme. When `payments[].attributes.transactionId` is also present, both SHALL identify the same payment transaction.                                                                                                                               | tstr          | `"T-20260423-000871"`                                                                         |

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
| `vats[].VATCode`                    | EN 16931-1             | VAT category code (e.g. `S`, `Z`, `E`, `AE`, `K`, `G`, `O`, `L`, `M`, `B`).                                                                                                             | tstr          | `"S"`                                                                                         |
| `products[].vats[].VATCode`           | EN 16931-1             | VAT category code for the line item (for example `S`, `Z`, `E`, `AE`, `K`, `G`, `O`, `L`, `M`, `B`).                                                                               | tstr          | `"S"`                                                                                         |
| `originalReceiptNumber`               | HeroJSON receiptNumber; analogous to EN 16931-1 BT-25 (Preceding Invoice Reference) | For a correction eReceipt (type `RETURN` or `PURCHASE_AND_RETURN` that reverses or corrects a prior transaction), the `receiptNumber` of the original eReceipt being corrected. Establishes the correction linkage (see the Chapter 6 note). | tstr          | `"R-2026-04-23-000412"`                                                                       |
| `payments[].attributes`             | EMV / PSP              | EMV/PSP payment attributes. Supported sub-fields: `AID`, `TVR`, `TSI`, `AC`, `cryptogramType`, `CID`, `CVM`, `authorizationCode`, `transactionId`, `terminalId`, `maskedPAN`, `APP`, `ENTRY`, `ARC`. | map           | `{ "AID": "A0000000031010", "maskedPAN": "411111******1111", "authorizationCode": "AB12CD" }` |
| `journey.id`                        | WE BUILD Journey model | Journey or booking identifier.                                                                                                                                                     | tstr          | `"BK-7781"`                                                                                   |
| `journey.distance`                  | WE BUILD Journey model | Distance travelled, in metres.                                                                                                                                                     | int           | `184000`                                                                                      |
| `journey.duration`                  | WE BUILD Journey model | Duration of the journey, in minutes.                                                                                                                                               | int           | `92`                                                                                          |
| `journey.CO2Emissions`              | CSRD Scope 3           | CO₂ emissions for this journey, in grams.                                                                                                                                          | int           | `12500`                                                                                       |
| `attachments[].description`         | HeroJSON               | Human-readable description of the attachment.                                                                                                                                      | tstr          | `"Boarding pass"`                                                                             |
| `attachments[].validUntil`          | ISO 8601 / RFC 3339    | Expiry date/time of the attachment.                                                                                                                                                | tdate         | `"2026-04-24T08:00:00Z"`                                                                      |

### 2.4 Conditional attributes

| **Data Identifier**                           | **Semantic Reference** | **Definition**                                                                                                                                                                                                                         | **Data type** | **Example value**                                                                                         |
| --------------------------------------------- | ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | --------------------------------------------------------------------------------------------------------- |
| `verifications[].transactionBegin.signedData` | OCMF / PSP              | Signed data captured at the beginning of the verification event, as defined by the `verifications[].type` profile (for example OCMF metering data). **REQUIRED when `verifications[].type` is OCMF**; not applicable otherwise.                                                                                                                | bstr          | (binary)                                                                                                  |
| `journey`                                     | WE BUILD Journey model | Journey object. **Present only for travel and mobility receipts** (where `journey.type` is one of `TRAIN`, `BUS`, `TAXI`, `FLIGHT`, `FERRY`). When the `journey` object is present, the conditional attributes below SHALL be present. | map           | (see below)                                                                                               |
| `journey.type`                                | WE BUILD Journey model | Mode of transport. **Mandatory if the `journey` object is present.** One of: `TRAIN`, `BUS`, `TAXI`, `FLIGHT`, `FERRY`.                                                                                                                | tstr          | `"TRAIN"`                                                                                                 |
| `journey.origin`                              | WE BUILD Journey model | Origin of the journey, with sub-fields: `name`, `city`, `country`, `latitude`, `longitude`, `datetime`. **Mandatory if the `journey` object is present.**                                                                              | map           | `{ "name": "Helsinki Central", "city": "Helsinki", "country": "FI", "datetime": "2026-04-23T08:00:00Z" }` |
| `journey.destination`                         | WE BUILD Journey model | Destination of the journey, with the same sub-fields as `journey.origin`. **Mandatory if the `journey` object is present.**                                                                                                            | map           | `{ "name": "Tampere", "city": "Tampere", "country": "FI", "datetime": "2026-04-23T09:32:00Z" }`           |
| `attachments[].type`                          | HeroJSON               | Attachment encoding type. **Mandatory if an `attachments[]` entry is present.** One of: `BARCODE`, `QRCODE`.                                                                                                                           | tstr          | `"QRCODE"`                                                                                                |
| `attachments[].kind`                          | HeroJSON               | Attachment purpose. **Mandatory if an `attachments[]` entry is present.** One of: `TICKET`, `RETURN`, `VOUCHER`.                                                                                                                       | tstr          | `"TICKET"`                                                                                                |
| `attachments[].title`                         | HeroJSON               | Title or label for the attachment. **Mandatory if an `attachments[]` entry is present.**                                                                                                                                               | tstr          | `"Boarding pass HEL→TPE"`                                                                                 |
| `attachments[].data`                          | HeroJSON               | Encoded attachment data (string). **Mandatory if an `attachments[]` entry is present.**                                                                                                                                                | tstr          | `"BAR:1234567890ABC…"`                                                                                    |
| `verifications[].currentType`                 | OCMF                   | For an OCMF (Open Charge Metering Format) metering proof, the electrical-current type: `AC` (alternating current) or `DC` (direct current). This is not an EMV cryptogram type; card (EMV) evidence is carried in `payments[].attributes`. **REQUIRED when `verifications[].type` is OCMF**; not applicable otherwise. | tstr          | `"AC"`                                                                                                    |
| `verifications[].transactionEnd.signedData`   | OCMF / PSP             | Signed data captured at the end of the verification event, as defined by the `verifications[].type` profile (for example OCMF metering data). **REQUIRED when the profile defines it**; not applicable otherwise. | bstr          | (binary)                                                                                                  |

### 2.5 Mandatory metadata

| **Data Identifier** | **Semantic Reference** | **Definition**                                                                                                                         | **Data type**       | **Example value**                                                |
| ------------------- | ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ---------------------------------------------------------------- |
| `iss`               | RFC 7519 / SD-JWT VC  | Issuer identifier; an HTTPS URL resolvable to the issuer's OpenID4VCI metadata (see `IR-09`).                                                         | tstr                | `"https://issuer.merchant.example"`                              |
| `iat`               | RFC 7519  | Issuance time as a NumericDate.                                                                                     | int | `1776939275`                                                     |
| `exp`               | RFC 7519  | Expiry time as a NumericDate; SHALL be greater than `iat` and SHALL reflect the long-validity policy of Section 4.1.6.                                                                            | int | `1966328075`                                                     |
| `vct`               | SD-JWT VC              | Attestation type identifier. SHALL be `eu.we-build.ereceipt.1`.  | tstr                | `"eu.we-build.ereceipt.1"`                                       |
| `cnf`               | RFC 7800 / SD-JWT VC  | Holder key binding (JWK) establishing proof of possession (see Section 4.1.4). | JSON object         | `{ "jwk": { "kty": "EC", "crv": "P-256", "x": "…", "y": "…" } }` |

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
| `vats[].VATCode`, `products[].vats[].VATCode` | `S`, `Z`, `E`, `AE`, `K`, `G`, `O`, `L`, `M`, `B`                                                                                    | EN 16931-1 duty/tax/fee category codes.                                             | EN 16931-1                           | Closed list (governed by EN 16931-1).                                                                                                               |
| `products[].quantityCode`                     | `H87`, `KGM`, `LTR`, `MTR`, …                                                                                                    | Unit of measurement of the line item quantity.                                      | UN/ECE Recommendation 20             | Open list (governed by UN/ECE).                                                                                                                     |
| `products[].EANCode`                          | Valid EAN-8, EAN-13 or GTIN-14                                                                                                  | Product barcode.                                                                    | GS1                                  | Open list (governed by GS1).                                                                                                                        |
| `payments[].type`                             | `CARD`, `CREDIT_TRANSFER`, `MOBILEPAY`, `GIFTCARD` (typical values)                                                                        | Payment method used to settle the corresponding `payments[].amount`.                | Issuer-defined; common values listed | Extensible. Issuers SHOULD reuse the listed values where applicable; additional values SHOULD be agreed across issuer and verifier implementations. |
| `journey.type`                                | `TRAIN`, `BUS`, `TAXI`, `FLIGHT`, `FERRY`                                                                                       | Mode of transport for travel/mobility receipts.                                     | WE BUILD Journey model               | Closed list. New values SHALL only be introduced through a minor version of this Rulebook.                                                          |
| `verifications[].type`                        | `EMV`, `OCMF`, `SCT`, `SCT-INST`                                                                                                | Standard of the technical proof in `verifications[]`.                               | EMV / OCMF / EPC SCT/SCT-INST        | Extensible through a minor version of this Rulebook.                                                                                                |
| `verifications[].currentType`                 | `AC`, `DC`                                                                                                                      | OCMF electrical-current type: `AC` = alternating current, `DC` = direct current. Applies only to OCMF verifications.    | OCMF                                  | Closed list.                                                                                                                                        |
| `attachments[].type`                          | `BARCODE`, `QRCODE`                                                                                                             | Encoding format of the attachment payload.                                          | HeroJSON                             | Closed list.                                                                                                                                        |
| `attachments[].kind`                          | `TICKET`, `RETURN`, `VOUCHER`                                                                                                   | Purpose of the attachment.                                                          | HeroJSON                             | Closed list. New values SHALL only be introduced through a minor version of this Rulebook.                                                          |
| `payments[].attributes` keys                  | `AID`, `TVR`, `TSI`, `AC`, `cryptogramType`, `CID`, `CVM`, `authorizationCode`, `transactionId`, `terminalId`, `maskedPAN`, `APP`, `ENTRY`, `ARC` | EMV/PSP terminal data sub-fields.                                                   | EMV / PSP specifications             | Open list; additional EMV-defined keys MAY be added.                                                                                                |

### 2.9 Integrity rules

| **Rule ID** | **Rule statement**                                                                                                                                                                                                                 | **Why it exists**                                                                       | **Where enforced**                                   | **Verifier / issuer behaviour on failure**                                       |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------- | -------------------------------------------------------------------------------- |
| `IR-01`     | `totalPriceIncVAT` SHALL equal `totalPriceExcVAT + totalVATAmount`.                                                                                                                                                                | Guarantees that header totals are internally consistent.                                | Issuer business rules; verifier business validation. | Issuer SHALL reject the receipt; verifier SHALL treat the credential as invalid. |
| `IR-02`     | The sum of `vats[].totalVATAmount` at receipt level SHALL equal `totalVATAmount`.                                                                                                                                                  | Guarantees that the per-rate VAT breakdown reconciles with the receipt-level VAT total. | Issuer business rules; verifier business validation. | Issuer SHALL reject the receipt; verifier SHALL treat the credential as invalid. |
| `IR-03`     | The sum of `payments[].amount` SHALL equal `totalPriceIncVAT`.                                                                                                                                                                     | Guarantees that the recorded payments reconcile to the receipt total, which may be negative for a refund.      | Issuer business rules; verifier business validation. | Issuer SHALL reject the receipt; verifier SHALL treat the credential as invalid. |
| `IR-04`     | `receiptTimeStamp` SHALL be greater than or equal to the timestamp embedded in `verifications[].transactionEnd.signedData`, where present.                                                                                         | Prevents back-dating of the receipt relative to the underlying payment transaction.         | Issuer business rules; verifier business validation. | Issuer SHALL reject; verifier SHALL flag the credential as untrustworthy.        |
| `IR-05`     | When `verifications[].type` is OCMF, the OCMF profile fields (`verifications[].currentType` and `verifications[].transactionBegin.signedData`) SHALL be present. For non-OCMF proof types these fields are not applicable.                                                                                                                     | Ensures a complete OCMF metering proof when that proof type is used, without imposing OCMF fields on card or credit-transfer receipts.                | Schema validation; issuer business rules.            | Issuer SHALL reject; verifier SHALL treat the credential as invalid.             |
| `IR-06`     | If `attachments[].validUntil` is present, its value SHALL be later than `receiptTimeStamp`.                                                                                                                                        | Prevents the issuance of attachments that are already expired at issuance time.         | Issuer business rules; verifier business validation. | Issuer SHALL reject; verifier MAY warn the user that the attachment is expired.  |
| `IR-07`     | If the `journey` object is present, both `journey.origin` and `journey.destination` SHALL be present, and `journey.type` SHALL be one of the values listed in Section 2.8.                                                         | Ensures that travel/mobility receipts are interpretable.                                | Schema validation; issuer business rules.            | Issuer SHALL reject; verifier SHALL treat the credential as invalid.             |
| `IR-08`     | When the `push` or `pull` delivery methods (Chapter 4) are used, the endpoint URI SHALL use TLS (HTTPS).                                                                                                                           | Protects credential delivery against on-path attackers.                                 | Issuer/Wallet at delivery time.                      | Wallet SHALL refuse delivery; issuer SHALL surface failure to the user.          |
| `IR-09`     | The `iss` claim SHALL be a URL resolvable to the merchant or PSP's OpenID4VCI metadata endpoint.                                                                                                                                     | Enables a Relying Party to discover and authenticate the issuer.                        | Issuer at issuance; verifier at verification.        | Verifier SHALL reject the credential.                                            |
| `IR-10`     | All monetary amount fields with `int` encoding SHALL be expressed in the currency minor unit (e.g., cents for EUR). Amounts SHALL be non-negative for `PURCHASE`. For `RETURN`, amounts MAY be non-positive (negative). For `PURCHASE_AND_RETURN`, purchased lines SHALL be non-negative and returned lines MAY be non-positive (negative); the header totals reflect the net of the purchased and returned lines. For `RETURN` and `PURCHASE_AND_RETURN`, `payments[].amount` MAY likewise be non-positive (negative) so that the recorded payments reconcile with the net (possibly negative) header total. | Avoids ambiguity in currency representation and supports return semantics.              | Issuer business rules.                               | Issuer SHALL reject inconsistent values.                                         |

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

### 3.2 SD-JWT VC-based encoding

The eReceipt attestation **SHALL** be issued in SD-JWT VC format and SHALL comply with the 'SD-JWT VCs' profile specified in [HAIP] (see ARB_01b in [Topic 12]). The issued SD-JWT VC SHALL use the `typ` header value `dc+sd-jwt` as defined in [SD-JWT VC]; consumers SHOULD also accept the earlier value `vc+sd-jwt` during the transition period.

A Verifiable Credential Type (`vct`) SHALL be defined and SHALL be unique within the EUDI Wallet ecosystem (see ARB_05 in [Topic 12]). The base `vct` for this attestation is:

> `eu.we-build.ereceipt.1`

This follows the WE BUILD reverse-DNS naming convention `eu.we-build.<attestation_name>.<major-version>` used across WE BUILD attestations. Issuer-specific subtypes, if defined, SHALL extend this base type via the `extends` field of the corresponding Type Metadata Document (Section 4 of [SD-JWT VC]).

Versioning of the `vct` follows the `x.y` model:

- **Minor version (y):** backward-compatible changes, such as adding optional attributes, display claims, or new languages.
- **Major version (x):** breaking changes, such as removing or renaming claims, or changes to mandatory fields.

Every claim name used in an eReceipt SHALL fall into one of three groups: (a) an IANA-registered JWT claim (Section 3.2.1), (b) a publicly-defined name reused from another specification such as OpenID Connect or SD-JWT VC (Section 3.2.2), or (c) a private name defined specifically for the eReceipt attestation in this Rulebook (Section 3.2.3).

For every claim, this Rulebook specifies whether the issuer MUST, MAY or MUST NOT make the claim selectively disclosable. Issuers SHALL also publish a Type Metadata Document for the eReceipt attestation type (as defined in Section 4 of [SD-JWT VC]), and the Type Metadata Document SHALL include Claim Selective Disclosure Metadata that matches the "Disclosable" column in the tables below.

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

- The `verifications[].type` proof is not limited to card/EMV: it also covers OCMF charge-metering proofs and SEPA credit-transfer (`SCT`, `SCT-INST`) scheme proofs.
- The `payments[].type` value `CREDIT_TRANSFER` covers IBAN-based (account-to-account) credit transfers.
- Issuers SHOULD reuse the listed values where applicable; additional payment-method or verification-proof values SHOULD be agreed across issuer and verifier implementations.

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
| `originalReceiptNumber`               | `originalReceiptNumber`      | string              | Section 2.3                                                         | MAY                                                          |
| `payments`                            | `payments`                   | array of objects    | Section 2.2                                                         | MUST (per-element)                                           |
| `payments[].type`                     | `type`                       | string              | Section 2.2                                                         | MUST                                                         |
| `payments[].amount`                   | `amount`                     | integer             | Section 2.2                                                         | MUST                                                         |
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

#### 3.2.4 Ontology binding (`extend` attribute)

To support semantic interoperability across WE BUILD attestations, claims defined in this Rulebook MAY include an `extend` attribute pointing to the corresponding term in the WE BUILD WP4 semantics vocabulary, published at:

> <https://webuild-consortium.github.io/wp4-semantics-group/ebwv/vocabulary.html>

Where a matching term exists in the current vocabulary, the binding SHOULD be expressed as a fragment URI of the form `…/vocabulary.html#<term>`. The mappings below cover the eReceipt claims for which a direct term is currently published; remaining claims will be bound as the WP4 vocabulary is extended to cover receipt-specific terminology.

| **Data Identifier** | **`extend` URI**                                                                         |
| ------------------- | ---------------------------------------------------------------------------------------- |
| `currencyISOCode`   | `https://webuild-consortium.github.io/wp4-semantics-group/ebwv/vocabulary.html#currency` |
| `payments[].amount` | `https://webuild-consortium.github.io/wp4-semantics-group/ebwv/vocabulary.html#amount`   |
| `merchant`          | `https://webuild-consortium.github.io/wp4-semantics-group/ebwv/vocabulary.html#supplier` |

Until the corresponding terms are published in the WP4 vocabulary, additional bindings are added manually to this section as the vocabulary evolves. Ontology bindings appear in this Rulebook only and are **not** carried in the issued attestation document.

#### 3.2.5 Illustrative example

The following non-normative example shows the JWT claim set (before SD-JWT processing) of an eReceipt issued for a small B2B expense purchase (a coffee and a sandwich at an Acme Helsinki Centre café), paid with a corporate card.

```json
{
  "iss": "https://issuer.merchant.example",
  "iat": 1745402075,
  "exp": 1761127275,
  "vct": "eu.we-build.ereceipt.1",
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
      "quantityCode": "H87",
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
      "quantityCode": "H87",
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
      "type": "EMV",
      "version": "1.0",
      "publicKey": "MIIBIjANBg…",
      "transactionId": "T-20260423-000871"
    }
  ],
  "status": { "status_list": { "idx": 17, "uri": "https://issuer.merchant.example/status/v1" } }
}
```

In the issued SD-JWT, the disclosable claims listed in Section 3.2.3 are wrapped in `_sd` arrays per [SD-JWT VC]; the non-disclosable claims (`iss`, `iat`, `exp`, `vct`, `cnf`, `status`, `attestation_legal_category`, all of `verifications[]`) appear as plain JWT claims.

The full issued SD-JWT for the example above (`typ` `dc+sd-jwt`): a base64url JWS followed by eleven Disclosures, tilde-separated.

```
eyJhbGciOiJFUzI1NiIsInR5cCI6ImRjK3NkLWp3dCIsImtpZCI6ImFjbWUtZXJlY2VpcHQta2V5LTEifQ.eyJpc3MiOiJodHRwczovL2lzc3Vlci5tZXJjaGFudC5leGFtcGxlIiwiaWF0IjoxNzQ1NDAyMDc1LCJleHAiOjE3NjExMjcyNzUsInZjdCI6ImV1LndlLWJ1aWxkLmVyZWNlaXB0LjEiLCJjbmYiOnsiandrIjp7Imt0eSI6IkVDIiwiY3J2IjoiUC0yNTYiLCJ4IjoiTThMaVFEckJ6LXU2Y2NMZUc0TlczbnBNRHlXc2plcHZQdWJuWWFrbmtLZyIsInkiOiJPNnZUMUFqR3RyeG16Qmg3V25VbFYycDJXN0lKbHVXYTFzdy0zN1ZHTlhVIn19LCJhdHRlc3RhdGlvbl9sZWdhbF9jYXRlZ29yeSI6Im5vbi1xdWFsaWZpZWQtRUFBIiwidmVyaWZpY2F0aW9ucyI6W3sidHlwZSI6IkVNViIsInZlcnNpb24iOiIxLjAiLCJwdWJsaWNLZXkiOiJNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QSIsInRyYW5zYWN0aW9uSWQiOiJULTIwMjYwNDIzLTAwMDg3MSJ9XSwic3RhdHVzIjp7InN0YXR1c19saXN0Ijp7ImlkeCI6MTcsInVyaSI6Imh0dHBzOi8vaXNzdWVyLm1lcmNoYW50LmV4YW1wbGUvc3RhdHVzL3YxIn19LCJfc2QiOlsiNC05MmZUM0pyc0djNDRQdEtMUVFCNEJuZ19LQjFaRFBESXlLVDRzd3RmdyIsIjdHWkMxNWtSbHdPZUhqSUU3V182Nng5ci1lZ0dvY0dvSU9ydlJ0Vm4wSkEiLCI5NklhTnFPbU5vUGJkTE9uWG1YUTItWW1wSkNiUXFMREFlZXVkTTkzTGJvIiwiRVdKd3dsY3YtaWJRMHZxdEtPa0JQbVBEakx3VG1tNlByWlpmT3lDeVlBbyIsIktXQklEaTY1OVExdUp6dl9IYVBBQUZHRTM4TGp6UmV6T09pTW0tcmoxX28iLCJNbmFSdkpjbWhxX1hTNHVnLUhfVWpsbGtTT1VmY2dqQkZ5MjhEVUpmdHBrIiwiT3NaS1lUODhqbGtIbXBzLUh6NjhWZnZtam50NHI0VjR5Vnp2T3hpR0dyUSIsIlJwa0lwV2RKWGJ6SWdKbVhwcFdlWVR5bDNTOWVHRmJxdHQ2WUhZRkNnNWMiLCJTVTVoV3lxV2dHNFduX0FQU3YtemY0dUdUb2xSdjlKaC05amg2dEdJNGRvIiwiY0xfeXFwVTV6N2dOQ2Fpa2xGbS1wTzU2Y3I1ZzZQMl85N1VUTjYwTV9XayIsInNlMFU4ZzE5UjhfRVNCeG40Qnp3QWpPTFdSbm5hYmt2OFAtYjRfTVF5TG8iXSwiX3NkX2FsZyI6InNoYS0yNTYifQ.q7gy-ARToyFFjfLpR4DWxGLMegyYG-8o6JipFnlr6YjFjE7dCYBWMJ2kN1fCjwZtK06gR_yYj6OSHSV8c6bQoQ~WyJGMGJJdDR2QTNxTTRqLXJlQVpiaml3IiwgInR5cGUiLCAiUFVSQ0hBU0UiXQ~WyJ1LWRKbERDMjFzRGZ0WVI1RmROakZ3IiwgInJlY2VpcHROdW1iZXIiLCAiUi0yMDI2LTA0LTIzLTAwMDQxMiJd~WyJHTEZrVm1EcEJfeHJYcFUtZDJ5eEFBIiwgInJlY2VpcHRUaW1lU3RhbXAiLCAiMjAyNi0wNC0yM1QxMDoxNDozMloiXQ~WyJVemtXamNDczZ4eTI5dmozejVHd29nIiwgImN1cnJlbmN5SVNPQ29kZSIsICJFVVIiXQ~WyJGZDFMM2JTYXg2UXJ3bFpjcHF6eTVRIiwgInRvdGFsUHJpY2VFeGNWQVQiLCA0MjUwXQ~WyJzT2JVbXJIcXc0Uy0yU1Z6aVZuQTBRIiwgInRvdGFsVkFUQW1vdW50IiwgMTAyMF0~WyJwOFpHYW14WE9hME5QTlRlSU4xNGJRIiwgInRvdGFsUHJpY2VJbmNWQVQiLCA1MjcwXQ~WyJyZWJpUkxHUk00WWo1dkhtclhDRWJnIiwgIm1lcmNoYW50IiwgeyJuYW1lIjogIkFjbWUgUmV0YWlsIE95IiwgImNvbXBhbnlJRCI6ICJGSTEyMzQ1Njc4IiwgImJyYW5jaCI6IHsiaWQiOiAiQlItSEVMLTAwMSIsICJwb3NJZCI6ICJQT1MtMTIiLCAibmFtZSI6ICJBY21lIEhlbHNpbmtpIENlbnRyZSIsICJzdWJOYW1lIjogIkNhZlx1MDBlOSJ9LCAiYWRkcmVzcyI6IHsic3RyZWV0QWRkcmVzcyI6ICJNYW5uZXJoZWltaW50aWUgMTAiLCAiY2l0eSI6ICJIZWxzaW5raSIsICJ6aXBDb2RlIjogIjAwMTAwIiwgImNvdW50cnkiOiAiRkkifX1d~WyJTOXh5bmJrU0JTaDR2bkJwbnF3MTZ3IiwgInByb2R1Y3RzIiwgW3sibmFtZSI6ICJFc3ByZXNzbyIsICJxdWFudGl0eSI6ICIyIiwgInF1YW50aXR5Q29kZSI6ICJIODciLCAidW5pdFByaWNlSW5jVkFUIjogMzUwLCAidG90YWxBbW91bnRFeGNWQVQiOiA1NjUsICJ0b3RhbEFtb3VudEluY1ZBVCI6IDcwMCwgInZhdHMiOiBbeyJWQVRSYXRlIjogIjI0IiwgIlZBVEFtb3VudCI6IDEzNSwgInRvdGFsQW1vdW50RXhjVkFUIjogNTY1LCAidG90YWxBbW91bnRJbmNWQVQiOiA3MDB9XSwgImNhdGVnb3JpemF0aW9uIjogeyJjYXRlZ29yeSI6ICJGJkIiLCAiZGVwYXJ0bWVudCI6ICJDYWZcdTAwZTkifX0sIHsibmFtZSI6ICJTYW5kd2ljaCIsICJxdWFudGl0eSI6ICIxIiwgInF1YW50aXR5Q29kZSI6ICJIODciLCAidW5pdFByaWNlSW5jVkFUIjogNDU3MCwgInRvdGFsQW1vdW50RXhjVkFUIjogMzY4NSwgInRvdGFsQW1vdW50SW5jVkFUIjogNDU3MCwgInZhdHMiOiBbeyJWQVRSYXRlIjogIjI0IiwgIlZBVEFtb3VudCI6IDg4NSwgInRvdGFsQW1vdW50RXhjVkFUIjogMzY4NSwgInRvdGFsQW1vdW50SW5jVkFUIjogNDU3MH1dfV1d~WyJKNUkxMkRmU3lUSUtiWkUtMkhIRDNnIiwgInZhdHMiLCBbeyJWQVRSYXRlIjogIjI0IiwgInRvdGFsVkFUQW1vdW50IjogMTAyMCwgInRvdGFsQW1vdW50RXhjVkFUIjogNDI1MCwgInRvdGFsQW1vdW50SW5jVkFUIjogNTI3MCwgIlZBVENvZGUiOiAiUyJ9XV0~WyJOYjRXb1NpejRaTzVMNDNNbkZOelpnIiwgInBheW1lbnRzIiwgW3sidHlwZSI6ICJDQVJEIiwgImFtb3VudCI6IDUyNzAsICJhdHRyaWJ1dGVzIjogeyJBSUQiOiAiQTAwMDAwMDAwMzEwMTAiLCAibWFza2VkUEFOIjogIjQxMTExMSoqKioqKjExMTEiLCAiYXV0aG9yaXphdGlvbkNvZGUiOiAiQUIxMkNEIiwgInRlcm1pbmFsSWQiOiAiUE9TLTEyIiwgInRyYW5zYWN0aW9uSWQiOiAiVC0yMDI2MDQyMy0wMDA4NzEifX1dXQ~
```

Each tilde-separated Disclosure after the JWS is base64url([salt, claim, value]). The eleven disclosed claims are: `type`, `receiptNumber`, `receiptTimeStamp`, `currencyISOCode`, `totalPriceExcVAT`, `totalVATAmount`, `totalPriceIncVAT`, `merchant`, `products`, `vats` and `payments` (their values are those shown in the JSON claim set above). The claims `iss`, `iat`, `exp`, `vct`, `cnf`, `status`, `attestation_legal_category` and all of `verifications[]` are plain JWT claims and are not selectively disclosable. The decoded Disclosures, the issuer and holder verification keys, and a verification walkthrough are provided in the companion example file `rb-e-receipt_sd-jwt-example_v0_1.md`.

### 3.3 W3C Verifiable Credentials Data Model-based encoding

The W3C VCDM v2.0-based encoding is **out of scope** for the current version of this Rulebook. As noted in ARB_01a of [Topic 12], only a non-qualified EAA may use this format; the eReceipt baseline profile is non-qualified, so this option remains available for future profiling. If, in a future version, this Rulebook adopts a VCDM v2.0 encoding, tables similar to those in Section 3.2 SHALL be defined and the Rulebook SHALL reference a specification, approved by an EU standardisation body or the European Digital Identity Cooperation Group (Article 46e(1) of the [European Digital Identity Regulation]), detailing how a Relying Party can request attributes from such an attestation and how a User can selectively disclose attributes from it (see ARB_04 in [Topic 12]).

## 4 Attestation usage

### 4.1 Issuer obligations

When issuing an eReceipt, the issuer (the merchant, or the PSP/acquirer acting on behalf of the merchant) SHALL meet the obligations below.

#### 4.1.1 Issuer authorisation

- The issuer SHALL be authorised, under the legal regime applicable to its jurisdiction, to issue an eReceipt under the legal category recorded in the `attestation_legal_category` claim (Section 2.2). The default profile of this Rulebook is `non-qualified-EAA`. Issuers operating under a `QEAA` or `PuB-EAA` profile SHALL additionally be a Qualified Trust Service Provider (QTSP) or a Public Body authorised to issue PuB-EAAs, respectively.
- The issuer SHALL be registered or otherwise listed in the applicable WE BUILD trust framework so that Relying Parties can resolve issuer authorisation as described in Chapter 5.

#### 4.1.2 Attestation construction

- The issuer SHALL construct the eReceipt in accordance with the attribute and metadata definitions of Chapter 2, including all mandatory attributes (Section 2.2) and mandatory metadata (Section 2.5), and SHALL respect the conditional-presence rules of Sections 2.4 and 2.7.
- The issuer SHALL apply the integrity rules of Section 2.9 (in particular `IR-01` to `IR-07`) before issuance and SHALL refuse to issue an eReceipt that fails any of those checks.
- The issuer SHALL use the base `vct` `eu.we-build.ereceipt.1` (Section 3.2). Issuer-specific subtypes, where defined, SHALL extend this base type via the `extends` field of the corresponding Type Metadata Document (Section 4 of [SD-JWT VC]).
- The issuer SHALL publish a Type Metadata Document whose Claim Selective Disclosure Metadata matches the **Disclosable** column of Section 3.2.3.

#### 4.1.3 Signing and key management

- The issuer SHALL sign the eReceipt SD-JWT with a private key whose corresponding public key is discoverable from the issuer's OpenID4VCI metadata endpoint, resolved from the `iss` claim (per `IR-09` in Section 2.9).
- The OpenID4VCI metadata SHALL publish the issuer's signing key(s) (or a JWKS URI from which they can be retrieved) and SHALL identify the issuer using a domain name that a Relying Party can validate via TLS using an X.509 server certificate from a publicly-trusted CA.
- The issuer SHALL operate key rotation in line with its trust-framework obligations, and SHALL ensure that historical keys remain resolvable for the validity period of any eReceipt previously signed with them.

#### 4.1.4 Holder binding

- The issuer SHALL bind the eReceipt to the Holder's wallet key by populating the `cnf` claim (Section 2.5) with the JWK of the public key supplied by the Wallet Unit during OpenID4VCI issuance.
- Where an issuer policy or use-case profile requires the eReceipt to be cryptographically bound to another attestation (e.g., a PID), the issuer SHALL include the `cryptographically_bound_to` optional metadata (Section 2.6) referencing the `vct` of the bound attestation. Otherwise, the metadata SHALL be omitted.

#### 4.1.5 Delivery

- The issuer SHALL deliver the eReceipt using one of the methods specified in Section 4.3 (Embedded / deferred, Pull, or Push).
- Issuance SHALL use OpenID4VCI (per EWC RFC001).
- For `push` and `pull` delivery methods, the endpoint URIs SHALL use TLS (per `IR-08` in Section 2.9). Delivery failures SHALL be surfaced to the user, and the issuer SHALL NOT consider an eReceipt delivered until the Wallet has acknowledged receipt.

#### 4.1.6 Lifecycle and revocation

- The issuer SHALL operate the status mechanism described in Chapter 6 (IETF Token Status List) and SHALL include the `status_list` optional metadata (Section 2.6) referencing the issued credential's status entry.
- The issuer SHALL use accurate values for the `iat` and `exp` claims, with `exp > iat`, and SHALL define an expiry policy consistent with the long-term presentation requirements of the eReceipt (typically several years for VAT reclaim and tax submission use cases; see Chapter 6).

### 4.2 Relying Party obligations

When receiving and processing an eReceipt, a Relying Party SHALL perform the checks defined in this section.

#### 4.2.1 Verify cryptographic integrity

- Validate the digital signature over the eReceipt SD-JWT using the issuer's public key, resolved as described in Section 4.2.2 and Chapter 5.
- Process the SD-JWT VC payload according to [SD-JWT VC], including verification of the `_sd` digest array(s) for any selectively-disclosed claims presented by the Holder.
- Validate the integrity rules of Section 2.9 (in particular `IR-01` to `IR-07`).

#### 4.2.2 Validate issuer

##### 4.2.2.1 Authentication

- Verify the certification chain over the issuer's signing certificate (or, for the `non-qualified-EAA` profile, the TLS server certificate of the issuer's OpenID4VCI metadata endpoint) up to a trust anchor as defined in Chapter 5.

##### 4.2.2.2 Identification

- Verify the intermediate certifications in the chain against the applicable EU Trust List(s) — in particular the active **TLOL** (Trusted List of Lists) and, where required for credentials issued in the past, the corresponding **TLOL-historic** snapshot for the time at which the eReceipt was issued.

> NOTE: TLOL-based identification applies primarily to the `QEAA` and `PuB-EAA` profiles. For the default `non-qualified-EAA` profile defined in this Rulebook, identification reduces to TLS server-certificate validation of the issuer's OpenID4VCI metadata endpoint against a publicly-trusted CA (Chapter 5).

For the WE BUILD pilot, trust is established through the WE BUILD trust framework: the WE BUILD List of Trusted Lists (LOTL), the WE BUILD CA, and the Wallet Unit Attestation as defined in the WE BUILD Blueprint. In production this maps to the EU trust infrastructure: the EU Trusted Lists (ETSI TS 119 612/615/602) and the ETSI Electronic Attestation of Attributes framework (TS 119 471/472/412-6), with Relying Party access governed by TS 119 411-8. The pilot mechanisms are the WE BUILD equivalents of these EU production mechanisms.

##### 4.2.2.3 Authorization

- Verify that the issuer is authorised to issue eReceipt attestations under the legal category recorded in the `attestation_legal_category` claim (Section 2.2).
- Check the issuer's credentials against the appropriate trust framework as described in Chapter 5. For the `non-qualified-EAA` profile this consists of resolving the `iss` URL to the issuer's OpenID4VCI metadata and validating the published signing key(s); for `QEAA` it consists of confirming the issuer's QTSP qualification status; for `PuB-EAA` it consists of confirming the issuer's authorisation as a Public Body authorised to issue PuB-EAAs.

#### 4.2.3 Holder Wallet related check

##### 4.2.3.1 Device binding

- Verify the Holder's key binding via the `cnf` claim (Section 2.5). An eReceipt **SHALL** be device-bound (see ARB_34 in [Topic 12]); the `cnf` claim carries the JWK of the Holder's public key, and the Holder MUST demonstrate possession of the corresponding private key at presentation time. This prevents replay of a copied credential by another party.
- Where the eReceipt carries the `cryptographically_bound_to` optional metadata (Section 2.6), verify the binding to the referenced attestation on the same Wallet Unit.

> EXAMPLE: where a tax authority requires the eReceipt to be bound to the PID of the
> Holder, the value of `cryptographically_bound_to` would be set to `"urn:eudi:pid:1"`
> (or, equivalently, to the PID `vct` value).

In all other cases, the `cryptographically_bound_to` metadata is OMITTED, and the eReceipt remains bound only to the Holder's wallet key via `cnf`.

###### 4.2.3.1.1 WUA check

- For the WE BUILD pilot, the Relying Party SHALL verify the Wallet Unit Attestation (WUA) presented alongside the eReceipt against the applicable Wallet Provider trust framework as defined in the WE BUILD Blueprint, to confirm that the Holder's wallet is a conformant EUDI Wallet Unit.

> NOTE: WUA verification is governed by the EUDI Wallet ARF (Topic 6 / Topic 8) and is not eReceipt-specific. The detailed protocol is out of scope for this Rulebook.

#### 4.2.4 Holder related check

##### 4.2.4.1 Revocation status check

- Query the designated revocation / status mechanism described in Chapter 6 (IETF Token Status List), resolved via the `status_list` optional metadata (Section 2.6).
- Treat revoked or suspended attestations as invalid.
- Handle the status outcome according to the Relying Party's organisational risk policy.

##### 4.2.4.2 Temporal validity check

- Validate `iat` to ensure the attestation was issued in the past.
- Validate `exp` to ensure the attestation has not expired.
- Where the use case implies long-term presentation (e.g., VAT reclaim or tax submission spanning several years), the Relying Party SHOULD additionally verify the issuer's key history (Section 4.1.3) to confirm the credential was valid at the time it was relied upon.

#### 4.2.5 Use-case dependent identity binding

Whether the Relying Party must additionally request and verify a PID (per ARB_27 in
[Topic 12]) depends on the use case:

- For **B2B expense management** flows where the Relying Party is the employer's expense system or organisational wallet, requesting a PID is **NOT REQUIRED** at the receipt level: identification of the employee is established through the corporate authentication context (e.g., SSO into the expense system), and the eReceipt itself is intentionally not bound to the Holder's identity in order to preserve flexibility where the payer's payment instrument (e.g. card or credit transfer account) does not formally belong to the benefiting organisation (see Section 1.5).
- For **tax authority submission** flows, the Relying Party SHOULD request a PID and bind the eReceipt presentation to the verified holder identity, in line with national tax reporting requirements.
- For **B2C consumer flows** (e.g., warranty claims, returns), the Relying Party MAY request a PID at its discretion.

### 4.3 Delivery methods

In line with EWC RFC011, three delivery methods are supported:

| **Method**          | **Description**                                                                                                                                                                                              |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Embedded (deferred) | Merchant sends a dynamic payment authorisation request (OpenID4VP); the eReceipt is issued after PSP confirmation. The Wallet polls with `transaction_id` until the credential is available.                   |
| Pull                | Merchant generates an eReceipt invitation URI; the Wallet follows the URI to complete OpenID4VCI issuance.                                                                                                     |
| Push                | Merchant pushes the eReceipt to an endpoint resolved via an eAddress controlled by the Holder. Delivery failures SHALL be surfaced to the user (per `IR-08` in Section 2.9, the endpoint URI SHALL use TLS). |

Issuance SHALL use OpenID4VCI (per EWC RFC001) and presentation SHALL use OpenID4VP
(per EWC RFC002).

### 4.4 Presentation requirements

The eReceipt is intended to be presented **online**, using OpenID4VP. Offline / proximity presentation per [ISO/IEC 18013-5] is **not in scope** for this version of the Rulebook (see Section 3.1).

### 4.5 Transactional data

The eReceipt itself records transactional data (the `payments[]` and `verifications[]` arrays) as part of its core payload. No additional transactional-data signing requirement under [Topic 20] of Annex 2 of the ARF applies to the _presentation_ of the eReceipt: the credential is consumed as evidence of a past transaction rather than as authorisation of a new one.

## 5 Trust anchors

For the **non-qualified EAA** profile defined here (see ARB_26 in [Topic 12]), the trust anchor that a Relying Party uses to verify an eReceipt is obtained as follows:

- The `iss` claim of the eReceipt (Section 2.5) SHALL be a URL resolvable to the merchant or PSP's OpenID4VCI metadata endpoint (per `IR-09` in Section 2.9).
- The OpenID4VCI metadata SHALL publish the issuer's signing key(s) (or a JWKS URI from which they can be retrieved) and SHALL identify the issuer using a domain name that the Relying Party can validate via TLS (X.509 server certificate from a publicly-trusted CA (or, for the WE BUILD pilot, a WE BUILD CA as defined in the WE BUILD Blueprint)).
- The Relying Party uses the published key(s) as the trust anchor for verifying the signature of the eReceipt SD-JWT.
- In addition, a Wallet Unit MAY use the EWC trust framework registry (when available) to verify that the issuer is an authorised eReceipt provider (per ISSU_34 in [Topic 10]).

If, in a future version of this Rulebook, the eReceipt is profiled as a **PuB-EAA** issued by a QTSP, the standard ARF mechanism applies: the Relying Party Instance verifies the signature of the PuB-EAA Provider over the eReceipt using a PuB-EAA Provider certificate issued by a QTSP, and verifies that certificate against the corresponding trust anchor from the QTSP Trusted List. Intermediate signing certificates may be used by both the PuB-EAA Provider and the QTSP.

> [!NOTE]
> The eReceipt provides three layers of assurance between the receipt data and the underlying payment: (i) EMV or payment-scheme cryptographic evidence carried in `payments[].attributes` (and, where a typed proof is supplied, in `verifications[]`), which proves that a genuine payment event occurred at the stated merchant, terminal and timestamp; (ii) issuer-side integrity rules `IR-01`, `IR-02` and `IR-03` (Section 2.9), which reconcile line items, VAT and payments against the receipt total; and (iii) process-level assurance that issuance occurs only after the PSP or acquirer has confirmed settlement (Section 4.3). An independent cryptographic binding between the PSP-confirmed authorised amount and the receipt total is not defined in this version of the Rulebook. Cross-verification against a separate Payment Data Confirmation attestation ([EWC RFC008] / [EWC ds008]) is under consideration for a future revision, and Relying Parties with heightened assurance requirements (for example, tax authorities performing VAT deduction verification) should take this limitation into account.

## 6 Revocation

(See [Topic 7] of the ARF for the high-level requirements related to revocation.)

The eReceipt attestation is a record of a past transaction and is therefore **typically not revoked** in normal operation. However, because the attestation may be presented over extended periods (for VAT reclaim and tax submissions, this may be several years), the eReceipt is **defined as revocable** rather than short-lived.

The following mechanism SHALL be used:

- **Token Status List**: the issuer SHALL maintain a Token Status List, and the metadata `status_list` (Section 2.6) SHALL be populated in every issued eReceipt with the list URI and the credential's index. The Status List mechanism follows the IETF Token Status List specification, aligned with the Attestation Status List mechanism that will be specified by the Commission.

Only the issuer may set or change the status of an eReceipt it issued. The conditions under which the issuer revokes are defined by the issuer's policy and are out of scope of this Rulebook. A revoked or suspended eReceipt SHALL be treated as invalid for credential-validity purposes by all Relying Parties; the business interpretation of a revoked or corrected eReceipt, and any resulting business action, are determined by the Relying Party's own policy.

NOTE (informative): A reversal, refund or chargeback of a completed transaction is a business event, not a credential fault. A common and recommended pattern is to keep the original eReceipt valid and to issue a new, linked correction eReceipt (for example of type `PURCHASE_AND_RETURN`) that references the original through the `originalReceiptNumber` attribute (Section 2.3), consistent with the EN 16931 corrective-document model and accounting-retention practice. Whether to revoke, to correct, or to take no action is an issuer and business decision and is out of scope of this Rulebook.

## 7 Compliance

This Rulebook complies with the EUDI Architecture and Reference Framework (ARF), with the [European Digital Identity Regulation], and with the EUDI Attestation Rulebook Template. In particular:

The structure of this document follows the Attestation Rulebook Template, with the attribute and metadata definitions in Chapter 2, encoding rules in Chapter 3, issuer and Relying Party obligations in Chapter 4, trust anchors in Chapter 5, revocation in Chapter 6, and references in Chapter 8.

The high-level requirements for attestation rulebooks (Topic 12 of Annex 2 of the ARF) are met across Chapters 2 to 6: every attribute is defined in an encoding-independent form first; mandatory, optional and conditional attributes are clearly marked; both ISO/IEC 18013-5 and SD-JWT VC encodings are addressed; selective-disclosure metadata is specified per claim; trust-anchor and revocation mechanisms are defined; and any attribute that is not part of an EU-wide namespace is placed in the WE BUILD eReceipt domestic namespace.

The revocation approach in Chapter 6 is aligned with Topic 7 of Annex 2 of the ARF (attestation revocation and revocation checking) and uses a Token Status List approach consistent with the forthcoming Commission Technical Specification on Attestation Status Lists. The issuance approach (Chapter 4 and Chapter 5) is aligned with Topic 10 of Annex 2 of the ARF and with EWC RFC001 (OpenID4VCI) and EWC RFC011 (delivery profile).

The semantics of receipt-level attributes are aligned with HeroJSON, EN 16931-1 and CEN/TS 16931-8; country, currency, date, unit-of-measure and barcode codes are aligned with ISO 3166-1, ISO 4217, ISO 8601, UN/ECE Recommendation 20 and GS1. The
_Semantic Reference_ column in the Chapter 2 tables and the code-list table in Section 2.8 record these alignments per attribute.

The canonical data model for this attestation is defined by Chapters 2 and 3 of this Rulebook. A HeroJSON-derived SD-JWT VC schema bearing the `vct` `eu.we-build.ereceipt.1` is to be published in the WE BUILD attestation catalog and, once published, becomes the canonical machine-readable schema; until then Chapters 2 and 3 are the single source of truth. The earlier EWC vReceipt schema [EWC ds011] (Chapter 8) is informative only and is not the schema for this attestation. Any divergence SHALL be resolved in favour of this Rulebook and the WE BUILD eReceipt schema, not [EWC ds011].

## 8 References

| **Item Reference**                     | **Standard name / details**                                                                                                                                                                                                                                                                        |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [European Digital Identity Regulation] | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework.                          |
| [HAIP]                                 | Yasuda, K. _et al,_ OpenID4VC High Assurance Interoperability Profile, OpenID Foundation, Version 1.0 Final, 29.12.2025.                                                                                                                                                                                        |
| [IANA-JWT-Claims]                      | IANA JSON Web Token Claims Registry. <https://www.iana.org/assignments/jwt/jwt.xhtml>.                                                                                                                                                                                                             |
| [ISO/IEC 18013-5]                      | ISO/IEC 18013-5, Personal identification, ISO-compliant driving licence, Part 5: Mobile driving licence (mDL) application, First edition, 2021-09.                                                                                                                                                 |
| [ISO 3166-1]                           | ISO 3166-1, Codes for the representation of names of countries and their subdivisions, Part 1: Country code.                                                                                                                                                                                       |
| [ISO 4217]                             | ISO 4217, Codes for the representation of currencies.                                                                                                                                                                                                                                              |
| [ISO 8601]                             | ISO 8601, Date and time, Representations for information interchange.                                                                                                                                                                                                                              |
| [EN 16931-1]                           | EN 16931-1, Electronic invoicing, Part 1: Semantic data model of the core elements of an electronic invoice.                                                                                                                                                                                       |
| [CEN/TS 16931-8]                       | CEN/TS 16931-8:2024, Electronic invoicing, Part 8: Semantic data model of the elements of an e-receipt or a simplified electronic invoice.                                                                                                                                                              |
| [HeroJSON]                             | HeroJSON receipt data model, <https://docs.receipthero.io/filetypes/receipthero-json/herojson-specification> (informational; field names aligned).                                                                                                                                                                                                         |
| [EWC RFC001]                           | EWC OpenID4VCI Issuance Profile. <https://github.com/EWC-consortium/eudi-wallet-rfcs/blob/main/ewc-rfc001-issue-verifiable-credential.md>                                                                                                                                                                                                                                                                     |
| [EWC RFC002]                           | EWC OpenID4VP Presentation Profile. <https://github.com/EWC-consortium/eudi-wallet-rfcs/blob/main/ewc-rfc002-present-verifiable-credentials.md>                                                                                                                                                                                                                                                                  |
| [EWC RFC011]                           | Payments with Verifiable Receipts (eReceipt issuance and delivery profile). <https://github.com/EWC-consortium/eudi-wallet-rfcs/blob/main/ewc-rfc011-payments-with-verifiable-receipts.md>                                                                                                                                                                                                                                                        |
| [EWC ds011]                            | Earlier EWC vReceipt SD-JWT schema (UBL / OASIS PurchaseReceipt-derived, vct VerifiablevReceiptSDJWT). Informative; superseded for the eReceipt attestation by the WE BUILD eReceipt schema (vct eu.we-build.ereceipt.1): <https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/data-schemas/ds011-vReceipts.json>.                                                                                                                       |
| [OIDC]                                 | Sakimura, N. et al., "OpenID Connect Core 1.0", OpenID Foundation. <https://openid.net/specs/openid-connect-core-1_0.html>.                                                                                                                                                                        |
| [EWC ds008]                            | Payment Data Confirmation schema. <https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/data-schemas/ds008-payment-data-confirmation.json> |
| [EWC RFC008]                           | Payment Data Confirmation, v1.0. <https://github.com/EWC-consortium/eudi-wallet-rfcs/blob/main/payment-rfcs/ewc-rfc008-payment-data-confirmation.md> |
| [OpenID4VP]                            | OpenID for Verifiable Presentations 1.0, OpenID Foundation. <https://openid.net/specs/openid-4-verifiable-presentations-1_0.html> |
| [OpenID4VCI]                           | OpenID for Verifiable Credential Issuance 1.0, OpenID Foundation, Final Specification, 16 September 2025. <https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html> |
| [RFC 3339]                             | RFC 3339, Date and Time on the Internet: Timestamps, G. Klyne et al., July 2002.                                                                                                                                                                                                                   |
| [RFC 8610]                             | RFC 8610, Concise Data Definition Language (CDDL): A Notational Convention to Express CBOR and JSON Data Structures, H. Birkholz et al., June 2019.                                                                                                                                                |
| [RFC 8943]                             | RFC 8943, Concise Binary Object Representation (CBOR) Tags for Date, M. Jones et al., November 2020.                                                                                                                                                                                               |
| [RFC 8949]                             | RFC 8949, Concise Binary Object Representation (CBOR), C. Bormann et al., December 2020.                                                                                                                                                                                                           |
| [SD-JWT VC]                            | SD-JWT-based Verifiable Credentials (SD-JWT VC). <https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/>, draft-ietf-oauth-sd-jwt-vc-16 (24 April 2026).                                                                                                                                            |
| [Token Status List]                    | Token Status List (TSL), IETF OAuth Working Group, draft-ietf-oauth-status-list-20 (work in progress). <https://datatracker.ietf.org/doc/draft-ietf-oauth-status-list/>                                                                                                                                                                                                                                     |
| [Topic 7]                              | ARF Annex 2, Topic 7, Attestation revocation and revocation checking. <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a237-topic-7-attestation-revocation-and-revocation-checking>.            |
| [Topic 10]                             | ARF Annex 2, Topic 10, Issuing a PID or attestation to a Wallet Unit. <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a2310-topic-10-issuing-a-pid-or-attestation-to-a-wallet-unit>.           |
| [Topic 12]                             | ARF Annex 2, Topic 12, Attestation Rulebooks. <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a2312-topic-12-attestation-rulebooks>.                                                           |
| [Topic 20]                             | ARF Annex 2, Topic 20, Strong User authentication for electronic payments. <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a2320-topic-20-strong-user-authentication-for-electronic-payments>. |
| [W3C VCDM v2.0]                        | Sporny, M. _et al,_ Verifiable Credentials Data Model v2.0, W3C Recommendation.                                                                                                                                                                                                                    |
| [UN/ECE Rec 20]                        | UN/ECE Recommendation No. 20, Codes for Units of Measure used in International Trade.                                                                                                                                                                                                              |
| [GS1]                                  | GS1 General Specifications (EAN/GTIN).                                                                                                                                                                                                                                                             |
