# Attestation Rulebook for attestations of type Payment Terms

* Author(s):
  * [Florin Coptil, Robert Bosch GmbH]
* Previous Authors

* Reviewer(s):

| Version | Date       | Description                                                     |
|---------|------------|-----------------------------------------------------------------|
| 0.1     | 13.03.2026 | Initial draft based on the WeBuild design attestations mettings |

* Contact:
  <a href="mailto:florin.coptil@bosch.com">Florin Coptil</a>

* Feedback:

## 1 Introduction

### 1.1 Document scope and purpose

The Payment Terms Attestation defines the financial conditions under which a buyer settles a transaction with a supplier within the EUDI Wallet ecosystem. This attestation is designed to support Know Your Supplier (KYS) processes by providing verifiable, standardized payment obligation data.

*The primary objectives of this attestation type are:*

- Supplier Commitment Verification – Confirm that suppliers agree to and can meet contractual and currency obligations.
- Regulatory and Policy Alignment – Ensure that payment terms comply with internal organizational policies and applicable regulatory standards.
- Cross-border Transaction Support – Enable interoperable payment term verification across Member States using internationally recognized standards (ISO 4217 for currencies, Incoterms for delivery terms).

### 1.2 Document structure

This Rulebook is structured as follows:

- Chapter 2 describes the attestation attributes and metadata in an encoding-independent manner, defining payment due periods, currency, and Incoterm specifications.
- Chapter 3 specifies how the attestation attributes and metadata are encoded for ISO/IEC 18013-5-compliant format (Section 3.1), SD-JWT VC-based format (Section 3.2), and W3C VCDM v2.0-based format (Section 3.3).
- Chapter 4 specifies attestation usage scenarios, Relying Party obligations, and integration with KYC/KYS workflows.
- Chapter 5 defines trust anchors and verification mechanisms for issuer authorization.
- Chapter 6 defines revocation mechanisms for the attestation.
- Chapter 7 provides compliance information regarding the EUBW framework, AML regulations, and applicable data protection laws.

###  1.3 Keywords

This document uses the capitalised keywords 'SHALL', 'SHOULD' and 'MAY' as specified in [RFC 2119], i.e. to indicate requirements, recommendations and options specified in this document.

In addition, 'must' (non-capitalised) is used to indicate an external constraint, i.e. a requirement that is not mandated by this document, but, for instance, by an external document. The word 'can' indicates a capability, whereas other words, such as 'will', and 'is' or 'are' are intended as statements of fact.

### 1.4 Terminology

This document uses the terminology specified in Annex 1 of the ARF.

*Additionally, the following terms are used:*

| Term        | Description                                                                                                                                                         | 
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Incoterms   | International Commercial Terms published by the International Chamber of Commerce (ICC) defining responsibilities between buyers and sellers in international trade |
| KYS         | Know Your Supplierdue diligence processes for verifying and assessing business partners                                                                             |
| Payment Due | The number of days within which payment must be made from a reference date (typically invoice date or delivery date)                                                |

## 2 Attestation attributes and metadata

### 2.1 Introduction

The Payment Terms attestation specifies three key elements of a commercial transaction:

### 2.2 Mandatory attributes

@TODO Florin still to confirmed with Barth the type (after matching in vocabulary document)

| **Data Identifier**        | **Definition**                                                                                                         | **Data type**                        |
|----------------------------|------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| payment_due                | The number of days within which payment must be made from the reference date (typically invoice date or delivery date) | integer                              |
| currency                   | The currency in which the payment is to be executed, as defined in ISO 4217:2015 (3-character alphabetic code)         | string (3 characters)                |
| incoterm                   | The delivery and risk transfer term agreed between buyer and seller, as defined in Incoterms® 2020                     | string (3 characters - see code list |
| buyer_identifier           | Unique identifier of the buyer party (e.g., EUID, VAT number, or DUNS number)                                          | string                               |
| supplier_identifier        | Unique identifier of the supplier party (e.g., EUID, VAT number, or DUNS number)                                       | string                               |
| agreement_date             | Date when the payment terms were agreed upon, according to ISO 8601                                                    | string (YYYY-MM-DD)                  |
| attestation_legal_category | Indicates the legal category of the attestation (EAA)                                                                  | string                               |

### 2.3 Optional attributes

| **Data Identifier**     | **Definition**                                                                                                    | **Data type** |
|-------------------------|-------------------------------------------------------------------------------------------------------------------|---------------|
| payment_reference_event | The event that triggers the start of the payment due period (e.g., "invoice_date", "delivery_date", "order_date") | string        |
| contract_reference      | Reference to the underlying contract or purchase order                                                            | string                               |
| transaction_amount      | The monetary value of the transaction                                                                             |decimal|
| delivery_location       | Destination location relevant to the Incoterm                                                                     |string |

### 2.4 Conditional attributes
No conditional attributes are defined for this attestation type. All attributes are either mandatory or optional as specified above.

### 2.5 Mandatory metadata

| **Data Identifier**   | **Definition**                                                                                                                                                     | **Data type**                          |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| issuance_date         | The date and time when the attestation was issued ISO 8601                                                                                                         |DateTime|
| expiry_date           | The date and time when the attestation expires ISO 8601                                                                                                            | DateTime |
| issuing_entity        | The identifier of the legal entity that issued the attestation (typically the subject entity itself for self-issued attestations, or the QTSP identifier for QEAA) | String  |

#### 2.6 Optional metadata

| **Data Identifier** | **Definition**      | **Data type**                          |
|---------------------|---------------------------------------------------------------------|----------------------------------------|
| trust_anchor_url    |URL where the trust anchor for verifying this attestation can be retrieved| URI|
| schema_version      |Version of the UBO List schema used |String |

### 2.7 Conditional metadata
No conditional metadata are defined for the Payment Terms attestation.

#### 2.8 Value Lists

#### 2.8.1 Type of Identity Document Codes

The type_of_identity_document attribute SHALL use one of the following standardized values:

| **Code** | **Definition**                                                       |
|----------|----------------------------------------------------------------------|
| EXW      | Ex Works Any mode of transport                                       |
| FCA      | Free Carrier Any mode of transport                                   |
| CPT      | Carriage Paid To Any mode of transport                               |
| CIP      | Carriage and Insurance Paid To Any mode of transport                 |
| DAP      | Delivered At Place Any mode of transport                             |
| DPU      | Delivered at Place Unloaded Any mode of transport                    |          
| DDP      | Delivered Duty Paid Any mode of transport                            |
| FAS      | Free Alongside Ship Sea and inland waterway transport only           |
| FOB      | Free On Board Sea and inland waterway transport only                 |
| CFR      | Cost and Freight Sea and inland waterway transport only              |
| CIF      | Cost, Insurance and Freight Sea and inland waterway transport only   |

#### 2.8.2 Currency Codes
The currency attribute SHALL use 3-character alphabetic currency codes as defined in ISO 4217:2015.
The complete list of valid codes is maintained by ISO and the Swiss Association for Standardization (SNV).

#### 2.9 Integrity Rules

*The following integrity rules SHALL be enforced:*
- The expiry_date SHALL be temporally after the issuance_date.
- The payment_due attribute SHALL be a positive integer (≥ 0, where 0 indicates immediate payment).
- The currency attribute SHALL be a valid ISO 4217:2015 3-character alphabetic currency code.
- The incoterm attribute SHALL be one of the valid codes defined in Section 2.8.1.

## 3 Attestation encoding

### 3.1 ISO/IEC 18013-5-compliant encoding
ISO/IEC 18013-5 (also called mdoc) is out of scope for this rulebook, as offline proximity presentation is not a current requirement for UBO.

### 3.2 SD-JWT VC-based encoding
The Payment Terms attestation supports the format specified in SD-JWT-based Verifiable Credentials (SD-JWT VC) and complies with the 'SD-JWT VCs' profile specified in [HAIP].

@TODO Florin&Monika - when the semantic is ready

The . notation is used to indicate the nesting of attributes.

**Verifiable Credential Type (`vct`):** `urn:eubw:payment_terms:1`

| **Data Identifier**        | **Attribute identifier**                                                       | **Encoding format** | **Reference/Notes** |
|----------------------------|--------------------------------------------------------------------------------|---------------------|-----------------|
| payment_due                |payment_due |uint ||
| currency                   |currency| tstr ||
| incoterm                   |incoterm |tstr| |
| attestation_legal_category | attestation_legal_category |tstr||
| payment_reference_event    |payment_reference_event |tstr| |
| buyer_identifier           |buyer_identifier |string||
| supplier_identifier        |supplier_identifier| string ||
| agreement_date             |agreement_date| string ISO 8601 |T|
| payment_reference_event    |payment_reference_event |string ||
| contract_reference         | contract_reference |string ||
| transaction_amount         |transaction_amount| number ||

example
```json
{
"iss": "https://tradeplatform.example.com",
"iat": 1705327800,
"exp": 1736863800,
"jti": "PT-2024-00123456",
"vct": "https://example.europa.eu/credentials/payment-terms/v1",
"attestation_legal_category": "non-qualified-EAA",
"payment_due": 30,
"currency": "EUR",
"incoterm": "CIP",
"buyer_identifier": "NL.KVK.12345678",
"supplier_identifier": "DE.HRB.98765432",
"agreement_date": "2024-01-15",
"payment_reference_event": "invoice_date",
"contract_reference": "PO-2024-0123",
"transaction_amount": 50000.00,
"delivery_location": "Rotterdam, Netherlands"
}
```

### 3.3 W3C Verifiable Credentials Data Model-based encoding
..

## 4 Attestation usage

The Payment Terms attestation is designed for the following primary use cases:
- Know Your Supplier (KYS) Processes: Verification of agreed commercial terms during supplier onboarding and due diligence processes.
- Automated Payment Processing: Supporting automated systems that need to verify payment due dates and currency before processing payments.
- Risk Management: Enabling buyers and suppliers to demonstrate creditworthiness and commercial reliability based on agreed payment terms.
- Regulatory Compliance: Meeting regulatory requirements for transparency in commercial transactions and payment terms disclosure.

### 4.1. Issuance process ###

### 4.2 Relying Party Obligations ###
When receiving and processing a Payment Term Attestation, a Relying Party SHALL:

@TODO Florin -> WP4 submission
The first 4 steps are basic verification - similar for all attestations:

### 4.2.1 Verify Cryptographic Integrity ###
- Validate the digital signature over the attestation using the issuer's public key
- For SD-JWT VC: Verify JWT signature and validate all disclosed claims
### 4.2.2 Validate Issuer ###


@TODO Werner
- Issuer Authentification 
- Issuer Identification 
- Issuer  Authorization 
  - Verify that the issuer is authorized to issue Payment Terms Attestations
  - Check the issuer's credentials against the appropriate trust framework (see Chapter 5)
  - For "EAA": Confirm issuer authorization mechanisms

### 4.2.3 Holder Related check ###
- Revocation status check 
  - Query the designated revocation/status mechanism (Cap 6)
  - Treat revoked or suspended attestations as invalid
  - @TODO Forin Check Handle indeterminate status according to organizational risk policy

- Check Temporal Validity ####  
  - Validate issuanceDate / iat to ensure the attestation was issued in the past 
  - Validate expirationDate / exp to ensure the attestation has not expired
  - Consider attestation age in relation to business risk (e.g., payment terms updated recently vs. stale data)

### 4.2.4  Holder Wallet Related check ###
#### 4.2.4.1.Device binding  ####
@TODO Werner  
- avoid copy & reply
- WUA check

#### 4.2.5 Validate Integrity Rules ####
@TODO Context check 

## 5 Trust anchors
@TODO Florin

## 6 Revocation
@TODO Florin

## 7 References
