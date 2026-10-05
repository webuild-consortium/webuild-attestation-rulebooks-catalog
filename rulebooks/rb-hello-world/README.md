# Attestation Rulebook for attestations of type Hello World

Category: non-qualified EAA

**Author(s):**  
Jochem Oosterlee, Cleverbase

**Previous Authors:**  
–

**Versioning**


**Feedback:**  
https://github.com/webuild-consortium/wp4-qtsp-group/issues

---

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

### 1.1 Document scope and purpose

This Rulebook defines the **Hello World Attestation (HWA)**, a minimal, short-lived Qualified Electronic Attestation of Attributes (QEAA) compliant with Regulation (EU) 2024/1183.  
Its purpose is to test pre-production QEAA issuance workflows with real Qualified Trust Service Providers (QTSPs) in production-like EUDI Wallet environments, supporting onboarding of trusted wallet systems, demonstration of compliant issuance capabilities, and interoperability across QEAA-compliant implementations.  
The HWA is intended for testing and has limited production trust value within the WEBUILD consortium’s controlled environment.

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

This document uses the terminology specified in Annex 1 of the ARF, including Qualified Electronic Attestation of Attributes (QEAA), Qualified Trust Service Provider (QTSP), Trusted List, and Annex V metadata requirements.

---

## 2 Compliance

### 2.1 Compliance statement

This Rulebook complies with the applicable requirements of Topic 12, Attestation
Rulebooks, in Annex 2 of the Architecture and Reference Framework, version 3.0.0. It
uses the terminology of Annex 1 of the ARF.

This Rulebook complies with Regulation (EU) 2024/1183 (Annex V) and the ARF for QEAAs:  
- Attributes defined encoding-independent (§2).  
- Encodings for ISO/IEC 18013-5 and SD-JWT VC (§3), compliant with ARB_01a/ARB_02/ARB_03.  
- Trusted List-bound issuance (§5) aligned with ARB_20.  
- Usage guidance (§4) and trust anchors (§5) aligned with ARB_21/ARB_26.  
- Short-lived validity (§6) aligned with Topic 7.  
- No transactional data defined (§4, Topic 20).  
It follows [RFC 2119], [RFC 8174], ISO/IEC 18013-5, SD-JWT VC, and Regulation (EU) 2024/1183.

---

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


The Hello World Attestation is a **Qualified EAA (QEAA)** for testing purposes.  
It defines a single fixed attribute and mandatory Annex V metadata to comply with Regulation (EU) 2024/1183.  
The attribute `attestation_legal_category` SHALL be `"QEAA"`.

### 3.2 Mandatory attributes

| Data Identifier | Definition | Data type | Example value |
| --- | --- | --- | --- |
| message | Fixed test string | string | "Hello World!" |
| attestation_legal_category | Legal category | string | "QEAA" |

### 3.3 Optional attributes

_None._

### 3.4 Conditional attributes

_None._

## 4 Metadata

Metadata describes the attestation rather than its subject.

### 4.1 Mandatory metadata


**Legal category.** This Rulebook retains the `attestation_legal_category` attribute.
Section 4.1 of the generic template replaces it with the `category` attribute of
[ETSI TS 119 472-1], whose value for this category is `eaa:eu:non-qualified`.
EW-DM-12-029, legacy ARB_25, of ARF version 3.0.0 is a SHALL that still requires
`attestation_legal_category`, so the template and the ARF disagree. The attribute is
left as written and the deviation is recorded for the rulebook quality assurance group.

| Data Identifier | Definition | Data type | Example value |
| --- | --- | --- | --- |
| issuing_authority | Issuer ID (resolvable via TL) | string | `https://issuer.webuildconsortium.eu` |
| issuer_legal_id | Legal person identifier | string | `LEI:1234567890` |
| trust_anchor_url | Trusted List URL | string | `https://trustedlist.eu/issuer` |
| attestation_scheme | Scheme details | string | `QEAA:HelloWorld` |
| issuance_date | Issue time *(mirrors auth. source)* | tdate | `2025-10-07T12:00:00Z` |
| expiry_date | Expiry time *(mirrors auth. source)* | tdate | `2025-10-07T23:59:59Z` (≤24h) |

> **Note:** `issuance_date` and `expiry_date` **SHALL** be present and **SHALL** match the authoritative validity source (`validityInfo` in mdoc, `iat`/`exp` in SD-JWT). They **SHALL NOT** be used for validation.

### 4.2 Optional metadata

_None._

### 4.3 Conditional metadata

_None._

---

### 4.4 Code lists


### 4.5 Integrity rules


## 5 Formats


### 5.1 SD-JWT VC-based encoding

- Encoding note: `_sd` contains base64url-encoded digests (no padding); `_sd_alg` indicates hash (e.g., `sha-256`).
- Header note: `cty` is **OPTIONAL** and **SHALL NOT** duplicate `vct`. Use `typ` (e.g., `sd-jwt`) for negotiation if needed.
- **Verifiable Credential Type (vct):** `eu.webuildconsortium.helloworld.v1`
- Claims:

| Data Identifier | Attribute identifier | Encoding format | Notes | Disclosable |
| --- | --- | --- | --- | --- |
| message | message | string | Fixed value | MUST |
| attestation_legal_category | attestation_legal_category | string | QEAA | MUST NOT |
| issuing_authority | iss | string | JWT claim | MUST NOT |
| issuer_legal_id | issuer_legal_id | string | Annex V | MUST NOT |
| trust_anchor_url | trust_anchor_url | string | Annex V | MUST NOT |
| attestation_scheme | attestation_scheme | string | Annex V | MUST NOT |
| **issuance_date** | **iat** | number (epoch) | **Authoritative** | MUST NOT |
| **expiry_date** | **exp** | number (epoch) | **≤24h after iat** | MUST NOT |

- **Validity:** The JWT claims `iat` and `exp` **SHALL** be the **sole source of truth** for validity. Verifiers **SHALL** enforce them.
- Note (ARB_31/ARB_32): TMD and JSON Schema required, see `data-schemas/sd-jwt/ds005-hello-world-sd-jwt.json`.
- Illustrative example:
  ```json
  {
    "vct": "eu.webuildconsortium.helloworld.v1",
    "iss": "https://issuer.webuildconsortium.eu",
    "iat": 1760025600,
    "exp": 1760111999,
    "attestation_legal_category": "QEAA",
    "issuer_legal_id": "LEI:1234567890",
    "trust_anchor_url": "https://trustedlist.eu/issuer",
    "attestation_scheme": "QEAA:HelloWorld",
    "_sd": [ "4vTz1zc7U-O1yQpltxsQ4xbB07Gefx4fX06PPmtaP4w" ],
    "_sd_alg": "sha-256"
  }
  ```
- Issued SD-JWT (base64 placeholder): `eyJhbGciOiJFUzI1NiIsInR5cCI6InNkLWp3dCJ9.eyJ2Y3QiOiJldS53ZWJ1aWxkY29uc29ydGl1bS5oZWxsb3dvcmxkLnYxIiwiaXNzIjoiaHR0cHM6Ly9pc3N1ZXIud2VidWlsZGNvbnNvcnRpdW0uZXUiLCJpYXQiOjE3NjAwMjU2MDAsImV4cCI6MTc2MDExMTk5OSwiYXR0ZXN0YXRpb25fbGVnYWxfY2F0ZWdvcnkiOiJRRUFBIiwiaXNzdWVyX2xlZ2FsX2lkIjoiTEVJOjEyMzQ1Njc4OTAiLCJ0cnVzdF9hbmNob3JfdXJsIjoiaHR0cHM6Ly90cnVzdGVkbGlzdC5ldS9pc3N1ZXIiLCJhdHRlc3RhdGlvbl9zY2hlbWUiOiJRRUFBOkhlbGxvd29ybGQiLCJfc2QiOlsiNHZUWjF6YzdaVytPMXlRcGx0eHNRNHhiQjA3R2VmNHhmWFg2UFBwbXRhUDR3PSJdLCJfc2RfYWxnIjoic2hhLTI1NiJ9.signature-placeholder`
- Disclosures: `["WyItQUlHRHFoemQxTGMwTVlucmtVS1F3IiwibWVzc2FnZSIsIkhlbGxvIFdvcmxkISJd"]`

> Note: The disclosure salt WyItQUlH... is demo-only. Real implementations SHALL use random, unique salts per selectively disclosable claim.”

---

### 5.2 ISO/IEC 18013-5-compliant encoding

- **docType:** `eu.webuildconsortium.helloworld.v1`
- **Namespace:** `eu.webuildconsortium.helloworld.v1`
- Attributes:
  - `message`: `tstr` UTF-8
  - `attestation_legal_category`: `tstr` UTF-8
  - `issuing_authority`: `tstr` UTF-8
  - `issuer_legal_id`: `tstr` UTF-8
  - `trust_anchor_url`: `tstr` UTF-8
  - `attestation_scheme`: `tstr` UTF-8
- Proof: COSE_Sign1 in `issuerAuth`, signed by a QTSP key registered in a Trusted List.
- **Validity:** The MSO carries `validityInfo` (`signed`, `validFrom`, `validUntil`), which **SHALL** be the **sole source of truth** for validity. Verifiers **SHALL** enforce it.
- **Date mapping:** Profile metadata `issuance_date` **SHALL** equal `validityInfo.validFrom` (or `signed` if equal); `expiry_date` **SHALL** equal `validityInfo.validUntil`. These are **not** carried as namespace elements.
- Notation: Examples use `elementIdentifier`/`elementValue`, per ISO/IEC 18013-5.
- Illustrative example:
  ```json
  {
    "docType": "eu.webuildconsortium.helloworld.v1",
    "issuerSigned": {
      "nameSpaces": {
        "eu.webuildconsortium.helloworld.v1": [
          { "elementIdentifier": "message", "elementValue": "Hello World!" },
          { "elementIdentifier": "attestation_legal_category", "elementValue": "QEAA" },
          { "elementIdentifier": "issuing_authority", "elementValue": "https://issuer.webuildconsortium.eu" },
          { "elementIdentifier": "issuer_legal_id", "elementValue": "LEI:1234567890" },
          { "elementIdentifier": "trust_anchor_url", "elementValue": "https://trustedlist.eu/issuer" },
          { "elementIdentifier": "attestation_scheme", "elementValue": "QEAA:HelloWorld" }
        ]
      },
      "validityInfo": {
        "signed": 1759838400,
        "validFrom": 1759838400,
        "validUntil": 1759881599
      },
      "issuerAuth": "<COSE_Sign1 placeholder for QTSP issuer signature>"
    }
  }
  ```

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

- **Use case:** Testing (pre-production) QEAA issuance, presentation, and verification in production-like EUDI Wallet environments with trusted wallets and relying parties.
- **Wallets** SHALL reject attestations with expiry >24h.
- **Relying Parties** SHALL validate Trusted List-bound signatures, Annex V metadata, and (if present) status.
- PID binding not required.
- The HWA is intended for testing within the WEBUILD consortium and has limited production trust value.
- No transactional data defined as per Topic 20.
- **mdoc Issuance**: The full attestation SHALL be provided in the `issuerSigned` structure, containing all attributes (`message`, `attestation_legal_category`) and metadata (`issuing_authority`, `issuer_legal_id`, `trust_anchor_url`, `attestation_scheme`), with validity conveyed via MSO `validityInfo` (`signed`, `validFrom`, `validUntil`), signed with `issuerAuth` (COSE_Sign1) by a QTSP key (§3.1). See illustrative example in `data-schemas/mdoc/sample-data/ds005-hello-world-mdoc-issuance-sample.json` and schema `data-schemas/mdoc/ds005-hello-world-mdoc.json`.
- **mdoc Presentation**: Holders MAY selectively disclose the `message` attribute in the `deviceSigned` structure, signed with `deviceAuth` (COSE_Sign1) to prove possession. The full `issuerSigned` structure from issuance SHALL be included to allow verification of all attributes and metadata. See illustrative example in `data-schemas/mdoc/sample-data/ds005-hello-world-mdoc-device-response-sample.json` and schema `data-schemas/mdoc/ds005-hello-world-mdoc.json`.
  - DeviceResponse envelope: The example is wrapped in an ISO/IEC 18013-5 DeviceResponse with `version` = `"1.0"`, a `documents` array containing the presented document, and `status` = `"ok"`.
  - Illustrative example:
    ```json
    {
      "version": "1.0",
      "documents": [
        {
          "docType": "eu.webuildconsortium.helloworld.v1",
          "issuerSigned": {
            "nameSpaces": {
              "eu.webuildconsortium.helloworld.v1": [
                { "elementIdentifier": "message", "elementValue": "Hello World!" },
                { "elementIdentifier": "attestation_legal_category", "elementValue": "QEAA" },
                { "elementIdentifier": "issuing_authority", "elementValue": "https://issuer.webuildconsortium.eu" },
                { "elementIdentifier": "issuer_legal_id", "elementValue": "LEI:1234567890" },
                { "elementIdentifier": "trust_anchor_url", "elementValue": "https://trustedlist.eu/issuer" },
                { "elementIdentifier": "attestation_scheme", "elementValue": "QEAA:HelloWorld" }
              ]
            },
            "validityInfo": {
              "signed": 1759838400,
              "validFrom": 1759838400,
              "validUntil": 1759881599
            },
            "issuerAuth": "<COSE_Sign1 placeholder for QTSP issuer signature>"
          },
          "deviceSigned": {
            "nameSpaces": {
              "eu.webuildconsortium.helloworld.v1": [
                { "elementIdentifier": "message", "elementValue": "Hello World!" }
              ]
            },
            "deviceAuth": "<COSE_Sign1 placeholder for wallet device signature>"
          }
        }
      ],
      "status": "ok"
    }
    ```
- **SD-JWT Issuance**: The attestation SHALL include the `message` attribute as a selectively disclosable claim via the `_sd` collection, with non-disclosable metadata (`attestation_legal_category`, `iss`, `issuer_legal_id`, `trust_anchor_url`, `attestation_scheme`, `iat`, `exp`) in the main payload, signed by a QTSP key (§3.2). See illustrative example in `data-schemas/sd-jwt/sample-data/ds005-hello-world-sd-jwt-issuance-sample.json` and schema `data-schemas/sd-jwt/ds005-hello-world-sd-jwt.json`.
- **SD-JWT Presentation**: Holders MAY selectively disclose the `message` attribute via disclosures, with non-disclosable metadata included in the main payload. See illustrative example in `data-schemas/sd-jwt/sample-data/ds005-hello-world-sd-jwt-presentation-sample.json` and schema `data-schemas/sd-jwt/ds005-hello-world-sd-jwt.json`.

---


### 7.3 Lifecycle management

The issuer sets the validity period of the attestation and reissues it when the
underlying facts change, revoking the superseded attestation as described in chapter 8.

### 7.4 Embedded disclosure policy

This attestation defines no embedded disclosure policy.

## 8 Revocation

- Attestations SHALL be short-lived (≤24h), aligning with Topic 7, which makes revocation OPTIONAL for such profiles.  
- Revocation SHALL NOT be implemented. Attestations SHALL be valid until expiry. 
- If implemented, SD-JWT MAY use Status List 2021.  
- If not, attestation SHALL be valid until expiry.

---

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


### 9.2 Presentation modes

Remote presentation is in scope. Proximity presentation is in scope only where
chapter 5 records an mdoc encoding.

### 9.3 Transactional data

This Rulebook defines no transactional data.

## 10 Trust Framework

- The HWA SHALL be issued by QTSPs with keys registered in a Member State’s Trusted List, per Regulation (EU) 2024/1183 (Annex V) and ARB_20.  
- Issuer keys SHALL be discoverable via trust anchor URLs provided in the `trustAnchorUrl` metadata.  
- RPs SHALL resolve signing keys via Trusted List URLs and verify signatures against trust anchors.  

---

**Trust anchor location**

The attribute or metadata carrying the trust anchor location contains at least the URL
at which a machine-readable version can be found or looked up.

## 11 References

| Item Reference | Standard name/details |
| --- | --- |
| [European Digital Identity Regulation] | Regulation (EU) 2024/1183 |
| [ARF] | EUDI Architecture and Reference Framework |
| [ISO/IEC 18013-5] | ISO/IEC 18013-5:2021, mDL |
| [SD-JWT VC] | IETF draft-ietf-oauth-sd-jwt-vc-11 |
| [IANA JWT Claims] | IANA JSON Web Token Claims Registry |
| [RFC 2119] | Key words for use in RFCs |
| [RFC 8174] | Ambiguity of uppercase key words |
| [RFC 3339] | Date and Time on the Internet |
| [RFC 8949] | CBOR |
| [RFC 8610] | CDDL |
| [RFC 8943] | CBOR Tags for Date |
| [OIDC] | OpenID Connect Core 1.0 |
| [HAIP] | OpenID4VC High Assurance Interop Profile draft-03 |
| [Topic 7] | ARF Annex 2 – Revocation |
| [Topic 10] | ARF Annex 2 – Issuance |
| [Topic 12] | ARF Annex 2 – Attestation Rulebooks |
| [Topic 20] | ARF Annex 2 – Strong User Authentication |
