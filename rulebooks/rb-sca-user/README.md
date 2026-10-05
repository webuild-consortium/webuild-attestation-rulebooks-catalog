# Attestation Rulebook for attestations of type SCA User

Category: non-qualified EAA

(Template version: 1.1)


*[Based on the WE BUILD attestation description: https://portal.webuildconsortium.eu/group/wp3-technology-standards/files?mid=6882&fid%5B0%5D=6880&fid%5B1%5D=7094]*

* Author(s):
    * Filip Hladký, Bank iD CZ, filip@bankid.cz
    * Stefan Kauhaus, Visa, kauhauss@visa.com


**Feedback:**

* Github, portal, email, Slack

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

SCA-User attestation specifies a User level SUA attestation described in [TS12] published by the European Commission.
SCA-User attestation represents a User that is using the EUDI Wallet for authentication and risk operation
authorisation in their online banking, banking mobile application, 3DS flows, and similar scenarios.

In this document we specify attributes, allowed formats, and processing rules for this attestation.
We also specify SD-JWT metadata for the SD-JWT credential format since those metadata are critical for correct
processing of presentation requests with attached transaction data.

Please note that terms credential and attestation are interchangeable for the purpose of this document.

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

This document uses the terminology specified in Annex 1 of the ARF.

## 2 Compliance

### 2.1 Compliance statement

This Rulebook complies with the applicable requirements of Topic 12, Attestation
Rulebooks, in Annex 2 of the Architecture and Reference Framework, version 3.0.0. It
uses the terminology of Annex 1 of the ARF.

This Rulebook is aligned with the following specifications:

* **[European Digital Identity Regulation]** (Regulation (EU) 2024/1183), This is a non-qualified EAA.
  Attributes and metadata satisfy the requirements of Annex V point b), c), and e) as applicable (ARB_15,
  ARB_17, ARB_19).
* **ARF [Topic 12]**, All ARB_ requirements applicable to non-qualified EAA have been addressed:
  ARB_01b, ARB_02, ARB_05, ARB_06, ARB_06a, ARB_06b, ARB_07, ARB_09, ARB_10, ARB_12, ARB_15, ARB_17,
  ARB_19, ARB_21, ARB_26, ARB_27, ARB_30, ARB_31, ARB_34.
* **ETSI TS 119 472-1**, The Rulebook structure and attestation lifecycle follow this standard.
* **[TS12]**, Attribute definitions and transaction data processing align with TS12 published by the
  European Commission.
* **[HAIP]**, The SD-JWT VC encoding complies with the OpenID4VC High Assurance Interoperability Profile.
* **[ISO/IEC 18013-5]**, The mdoc encoding follows the ISO mobile document standard.

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


SCA-User is a simple single-level attestation with only top-level attributes. It has a single mandatory attribute
identifying the user at the Bank, plus one optional masked identifier.

SCA-User does **not** support selective disclosure. All attributes are always fully disclosed on presentation.

SCA-User attestation is exclusively used in the **2-party model**: the issuer and verifier of such an attestation
are the same organisation (the bank). A Relying Party receiving this attestation is always the issuing bank itself.

This attestation is categorised as a **non-qualified EAA**.

This document defines the attribute `attestation_legal_category` which SHALL have the value `"non-qualified-EAA"`.

#### 1 Introduction

#### 2.8 VCT metadata handling and transaction data display in Wallet

SD-JWT VC specification (draft 14, chapter 5) allows definition of metadata documents associated with issued
credentials by the `vct` claim. For all SCA attestations, the following VCT inheritance model is used.

##### 2.8.1 VCT type hierarchy

The SCA hierarchy consists of three layers:

**Layer 1, Base SCA type (abstract, not directly issuable):**

```
https://webuildconsortium.eu/sca/1.0
```

This base VCT is not directly usable but defines common behaviour and rules as specified in [TS12]. It defines the
transaction data structure, processing rules, and display requirements that apply to all SCA attestation variants.

**Layer 2, SCA-User abstract base type:**

```
https://webuildconsortium.eu/sca/sca-user/1.0
```

This type has claims `"extends"` and `"extends#integrity"` pointing to the base SCA VCT above. It defines the
SCA-User-specific attribute set and selective disclosure rules (none for SCA-User).

**Layer 3, Issuer-specific VCT (actual issued credential type):**

```
https://issuer.bank.cz/credentials/sca/user/1.0
```

Actual SCA-User attestations issued by a bank carry an issuer-specific VCT URL. The issuer's VCT metadata document
at that URL SHALL contain claims `"extends"` and `"extends#integrity"` pointing to the Layer 2 base SCA-User type.

##### 2.8.2 VCT metadata document structure

The issuer SHALL publish a VCT metadata document at the issuer-specific VCT URL. The document SHALL conform to
[SD-JWT VC] chapter 6 and SHALL include at minimum:

```json
{
  "vct": "https://issuer.bank.cz/credentials/sca/user/1.0",
  "name": "SCA-User, Bank CZ",
  "description": "Strong Customer Authentication user credential issued by Bank CZ for use in 2-party banking flows.",
  "extends": "https://webuildconsortium.eu/sca/sca-user/1.0",
  "extends#integrity": "sha256-<hash-of-sca-user-base-vct-document>",
  "display": [
    {
      "lang": "en",
      "name": "SCA User Credential",
      "description": "Used for authentication and transaction authorisation in online banking.",
      "rendering": {
        "simple": {
          "logo": {
            "uri": "https://issuer.bank.cz/assets/sca-logo.png",
            "uri#integrity": "sha256-<hash>",
            "alt_text": "Bank CZ SCA credential logo"
          },
          "background_color": "#1A3C8F",
          "text_color": "#FFFFFF"
        }
      }
    }
  ],
  "claims": [
    {
      "path": ["sub"],
      "display": [{"lang": "en", "label": "User identifier"}],
      "sd": "never"
    },
    {
      "path": ["masked_psu_id"],
      "display": [{"lang": "en", "label": "PSU identifier"}],
      "sd": "never"
    }
  ]
}
```

Key points:
* All claims SHALL have `"sd": "never"`, SCA-User does not support selective disclosure.
* The `display` array SHOULD include entries for all languages relevant to the deployment.
* `extends#integrity` SHALL be the SHA-256 hash of the referenced base VCT document to protect the inheritance chain.

##### 2.8.3 Transaction data display

Transaction data processing and display requirements are defined in [TS12] and in the base SCA VCT metadata at
`https://webuildconsortium.eu/sca/1.0`. The Wallet SHALL follow those rules when rendering transaction data
for user confirmation.

Issuers SHOULD define issuer-specific display rules in the `display` section of their VCT metadata document,
including at minimum a logo, background colour, and text colour for Wallet UI rendering.

##### 2.8.4 Versioning

Versioning of VCT types SHALL follow an `x.y` version model where:
- `x` is the major version, introduces breaking changes (removing claims from metadata, renaming or repurposing
  claims in transaction data).
- `y` is the minor version, introduces backward-compatible changes (adding elements, adding display claims,
  adding languages).

With this mechanism, integrity checks remain in place and the need for re-issuance of credentials across all
wallets is minimised. Relying Parties and Wallets SHALL reject credentials whose `extends#integrity` check fails.

#### 4.2 Presentation lifecycle

SCA-User SHOULD be used only when the presentation request comes from a Verifier that is allowed to request this
attestation. If another Verifier requests this attestation type and the Wallet does not have any matching
attestation for that Verifier, the Wallet SHALL display a warning and MAY fail such a presentation request.

### 3.2 Mandatory attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| sub | https://www.rfc-editor.org/info/rfc7519/#section-4.1.2 | Random unique value identifying the attestation subject in the authentic source. Usage of UUID or prefixed UUID is recommended. | String | urn:uuid:123e4567-e89b-12d3-a456-426614174000 |

### 3.3 Optional attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| masked_psu_id | N/A | Masked identifier of the PSU (Payment Service User) of the credential in the bank | string | DE89****3000 |

### 3.4 Conditional attributes


## 4 Metadata

Metadata describes the attestation rather than its subject.

### 4.1 Mandatory metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| iss | https://www.rfc-editor.org/info/rfc7519/#section-4.1.1 | Issuer URL identifying the attestation provider | string (URI) | https://issuer.bank.cz |
| aud | https://www.rfc-editor.org/info/rfc7519/#section-4.1.3 | Audience of this attestation; SHALL be URL(s) of the RP(s) that will request presentation of this attestation. Because SCA-User is 2-party only, this SHALL always be the issuing bank's own RP URL. | string or array of string | https://banking.bank.cz |
| iat | https://www.rfc-editor.org/info/rfc7519/#section-4.1.6 | Unix timestamp designating the time when the attestation was issued | integer (Long) | 1748736000 |
| exp | https://www.rfc-editor.org/info/rfc7519/#section-4.1.4 | Unix timestamp denoting the technical validity expiration of the attestation | integer (Long) | 1751328000 |
| vct | Section 3.2.1 of [SD-JWT VC] | Denotes type of attestation; SHALL be an issuer-specific URL extending the WE BUILD base VCT | string (URI) | https://issuer.bank.cz/credentials/sca/user/1.0 |
| cnf | https://www.rfc-editor.org/info/rfc7800 | Object containing the JWK of the holder's public key (device binding) | JSON Object | `{"jwk": {"kty":"EC","crv":"P-256",...}}` |

**Legal category.** This Rulebook retains the `attestation_legal_category` attribute.
Section 4.1 of the generic template replaces it with the `category` attribute of
[ETSI TS 119 472-1], whose value for this category is `eaa:eu:non-qualified`.
EW-DM-12-029, legacy ARB_25, of ARF version 3.0.0 is a SHALL that still requires
`attestation_legal_category`, so the template and the ARF disagree. The attribute is
left as written and the deviation is recorded for the rulebook quality assurance group.

### 4.2 Optional metadata


### 4.3 Conditional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| nbf | https://www.rfc-editor.org/info/rfc7519/#section-4.1.5 | Unix timestamp denoting the first time the attestation may be used. Conditionally mandatory when `nbf` and `iat` differ. | integer (Long) | 1748822400 |
| status_list | https://www.ietf.org/archive/id/draft-ietf-oauth-status-list-17.html | Status list object for revocation checking | JSON Object | `{"idx": 0, "uri": "https://issuer.bank.cz/statuslists/1"}` |

### 4.4 Code lists

This attestation does not use any code lists.

### 4.5 Integrity rules

SD-JWT and VCT type metadata integrity rules apply. No additional attestation-specific integrity rules are needed.

| **Rule ID** | **Rule statement** | **Why it exists** | **Where enforced** | **Verifier / issuer behavior on failure** |
| --- | --- | --- | --- | --- |
| IR-01 | `vct` metadata document SHALL carry a valid `extends#integrity` hash matching the referenced base VCT document | Ensures VCT inheritance chain has not been tampered with | Wallet (on issuance), Verifier | Reject credential / reject presentation |
| IR-02 | `cnf` key SHALL match the key used to sign the Key Binding JWT in presentation | Ensures device binding is intact | Verifier | Reject presentation |


## 5 Formats


### 5.1 SD-JWT VC-based encoding

The SCA-User attestation supports the SD-JWT VC format as specified in [SD-JWT VC], compliant with the [HAIP] profile.

**VCT (Verifiable Credential Type):** `https://issuer.bank.cz/credentials/sca/user/1.0`
(issuer-specific; MUST extend `https://webuildconsortium.eu/sca/sca-user/1.0` via `"extends"` and
`"extends#integrity"` claims in VCT metadata)

**Note:** SCA-User does NOT support selective disclosure. All claims are non-selectively disclosable (`MUST NOT`).

**IANA-registered JWT claims:**

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Reference/Notes** | **Disclosable** |
| --- | --- | --- | --- | --- |
| iss | iss | string (URI) | [RFC 7519] §4.1.1 | MUST NOT |
| aud | aud | string or array of string | [RFC 7519] §4.1.3, SHALL be the issuing bank's own RP URL(s); mandatory for 2-party model | MUST NOT |
| iat | iat | integer (NumericDate) | [RFC 7519] §4.1.6 | MUST NOT |
| exp | exp | integer (NumericDate) | [RFC 7519] §4.1.4 | MUST NOT |
| nbf | nbf | integer (NumericDate) | [RFC 7519] §4.1.5, conditionally mandatory when `nbf` differs from `iat` | MUST NOT |
| sub | sub | string | [RFC 7519] §4.1.2, UUID or prefixed UUID identifying the holder | MUST NOT |

**Private claim names and SD-JWT-specific claims:**

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Notes** | **Disclosable** |
| --- | --- | --- | --- | --- |
| vct | vct | string (URI) | Denotes attestation type; SHALL be an issuer-specific URL extending the WE BUILD base VCT | MUST NOT |
| cnf | cnf | JSON Object | JWK of holder's public key (device binding); see [RFC 7800] | MUST NOT |
| status_list | status_list | JSON Object | Status list reference per draft-ietf-oauth-status-list-17; optional | MUST NOT |
| attestation_legal_category | attestation_legal_category | string | SHALL be `"non-qualified-EAA"` | MUST NOT |
| masked_psu_id | masked_psu_id | string | Masked identifier of the PSU in the bank; optional | MUST NOT |

**Example JWT claim set (provider-side):**

```json
{
  "iss": "https://issuer.bank.cz",
  "aud": "https://banking.bank.cz",
  "iat": 1748736000,
  "exp": 1748822400,
  "vct": "https://issuer.bank.cz/credentials/sca/user/1.0",
  "vct#integrity": "sha256-abc123def456...",
  "extends": "https://webuildconsortium.eu/sca/sca-user/1.0",
  "extends#integrity": "sha256-def456abc123...",
  "sub": "urn:uuid:123e4567-e89b-12d3-a456-426614174000",
  "masked_psu_id": "DE89****3000",
  "cnf": {
    "jwk": {
      "kty": "EC",
      "crv": "P-256",
      "x": "TCAER19Zvu3OHF4j4W4vfSVoHIP1ILilDls7vCeGemc",
      "y": "ZxjiWWbZMQGHVWKVQ4hbSIirsVfuecCE6t4jT9F2HZQ"
    }
  },
  "attestation_legal_category": "non-qualified-EAA"
}
```

Note the absence of `_sd_alg` and `_sd` arrays, SCA-User has no selectively disclosable claims.

**Example issued SD-JWT (compact serialization):**

```
eyJhbGciOiJFUzI1NiIsInR5cCI6InZjK3NkLWp3dCIsImtpZCI6Imlzc3Vlci1rZXktMSJ9
.
eyJpc3MiOiJodHRwczovL2lzc3Vlci5iYW5rLmN6IiwiYXVkIjoiaHR0cHM6Ly9iYW5raW5n
LmJhbmsuY3oiLCJpYXQiOjE3NDg3MzYwMDAsImV4cCI6MTc0ODgyMjQwMCwidmN0IjoiaHR0
cHM6Ly9pc3N1ZXIuYmFuay5jei9jcmVkZW50aWFscy9zY2EvdXNlci8xLjAiLCJzdWIiOiJ1
cm46dXVpZDoxMjNlNDU2Ny1lODliLTEyZDMtYTQ1Ni00MjY2MTQxNzQwMDAiLCJtYXNrZWRf
cHN1X2lkIjoiREU4OSoqKiozMDAwIiwiY25mIjp7Imp3ayI6eyJrdHkiOiJFQyJ9fSwiYXR0
ZXN0YXRpb25fbGVnYWxfY2F0ZWdvcnkiOiJub24tcXVhbGlmaWVkLUVBQSJ9
.
<issuer-signature>~<KB-JWT>
```

No `~disclosure` lines are appended because there are no selectively disclosable claims.

**Human-readable SD-JWT payload:**

All claims are always present in the JWT body. There are no disclosures.

| Claim | Value |
| --- | --- |
| `iss` | `https://issuer.bank.cz` |
| `aud` | `https://banking.bank.cz` |
| `iat` | `1748736000` (2025-05-31T00:00:00Z) |
| `exp` | `1748822400` (2025-06-01T00:00:00Z) |
| `vct` | `https://issuer.bank.cz/credentials/sca/user/1.0` |
| `sub` | `urn:uuid:123e4567-e89b-12d3-a456-426614174000` |
| `masked_psu_id` | `DE89****3000` |
| `cnf` | `{jwk: {kty: "EC", crv: "P-256", ...}}` |
| `attestation_legal_category` | `non-qualified-EAA` |

The issued SD-JWT still uses the `~<KB-JWT>` Key Binding JWT suffix to bind presentation to the holder's key
(included in `cnf`), even though no selective disclosure is used.

### 5.2 ISO/IEC 18013-5-compliant encoding

The SCA-User attestation supports the mdoc format specified in ISO/IEC 18013-5.

**Document type:** `eu.webuildconsortium.sca.user.1`

**Encoding conventions:**

* `tstr`, `uint`, `bstr`, `bool`, and `tdate` are CDDL representation types defined in [RFC 8610].
    * `tstr` SHALL be encoded in UTF-8 and SHALL support the full Unicode range (per [RFC 8949]).
    * All `tstr` attributes SHALL have a maximum length of 150 characters.
    * `full-date` is defined as `full-date = #6.1004(tstr)` where tag 1004 is specified in [RFC 8943].
    * A `tdate` attribute SHALL contain a date-time string as specified in [RFC 3339] (per [RFC 8949] §3.4.1).
    * A `full-date` attribute SHALL contain a full-date string as specified in [RFC 3339] (per [RFC 8943]).
    * Fractions of seconds SHALL NOT be used.
    * A local offset from UTC SHALL NOT be used; the time-offset SHALL be `"Z"`.
    * The following canonical CBOR rules (per [RFC 8949] §4.2) SHALL be implemented:
        * Integers (major types 0 and 1) SHALL be as small as possible.
        * The expression of the length in a `bstr`, `tstr`, array, or map SHALL be as short as possible.
        * Indefinite-length items SHALL be made into definite-length items.

**Attribute encoding table:**

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Namespace** |
| --- | --- | --- | --- |
| sub | sub | tstr | eu.webuildconsortium.sca.user.1 |
| masked_psu_id | masked_psu_id | tstr | eu.webuildconsortium.sca.user.1 |
| attestation_legal_category | attestation_legal_category | tstr | eu.webuildconsortium.sca.user.1 |

**Example mdoc (CBOR diagnostic notation):**

```cbor
{
  "version": "1.0",
  "documents": [{
    "docType": "eu.webuildconsortium.sca.user.1",
    "issuerSigned": {
      "nameSpaces": {
        "eu.webuildconsortium.sca.user.1": [
          { "digestID": 1, "random": h'a1b2c3d4', "elementIdentifier": "sub",
            "elementValue": "urn:uuid:123e4567-e89b-12d3-a456-426614174000" },
          { "digestID": 2, "random": h'e5f6a7b8', "elementIdentifier": "masked_psu_id",
            "elementValue": "DE89****3000" },
          { "digestID": 3, "random": h'c9d0e1f2', "elementIdentifier": "attestation_legal_category",
            "elementValue": "non-qualified-EAA" }
        ]
      },
      "issuerAuth": << IssuerAuth COSE_Sign1 structure >>
    }
  }],
  "status": 0
}
```

Attribute values in the example:

| Attribute | Value |
| --- | --- |
| sub | urn:uuid:123e4567-e89b-12d3-a456-426614174000 |
| masked_psu_id | DE89****3000 |
| attestation_legal_category | non-qualified-EAA |

### 5.3 W3C Verifiable Credentials Data Model-based encoding


## 6 Protocols

This attestation is issued using OpenID for Verifiable Credential Issuance
[OpenID4VCI] and presented using OpenID for Verifiable Presentations [OpenID4VP], both
as profiled by [HAIP].

## 7 Issuance

### 7.1 Binding

| Field | Value | Source |
| --- | --- | --- |
| Device-bound | SHALL | EW-DM-12-038 |
| Cryptographically bound to | none | EW-DM-12-032 |
| Relying Party must also verify a PID | should | EW-DM-12-031 |
| Binding subject | legal person |  |

### 7.2 Issuance Policy

SCA-User is exclusively designed for the **2-party model**: the issuing bank and the verifying bank are the same
organisation. A PISP or other third party SHALL NOT be able to verify this attestation.

**Primary use cases:**

1. **Authentication in online banking:** User presents SCA-User with transaction data to authenticate into their
   bank's online banking portal.
2. **Risk operation authorization in banking mobile application:** User authorises sensitive operations (e.g.
   new beneficiary, limit changes) in the bank's mobile app.
3. **3DS flows:** User authenticates via Wallet during a 3-D Secure challenge initiated by the bank.
4. **Other bank-internal SCA scenarios** where the issuer is also the verifier.

SCA-User is almost exclusively used in presentation scenarios where transaction data is present in the presentation
request. Processing of transaction data follows [TS12].

**Relying Party obligations:**

* The Relying Party (which is always the issuing bank) SHALL verify the issuer signature and the `cnf` key binding.
* The Relying Party SHALL verify that the `aud` claim matches its own identifier before accepting the attestation.
* The Relying Party SHALL check the `status_list` claim if present.
* The Relying Party SHALL verify that transaction data in the presentation request is correctly bound and displayed
  to the user prior to signing, as defined in [Topic 20] and [TS12].
* If a Wallet presents this attestation in response to a request from a Relying Party that is not the issuing bank,
  the Wallet SHALL display a warning and MAY reject the presentation request.
* Verification of a PID alongside this attestation is not required.

**Presentation requirements:**

* SCA-User SHALL be presented online using OID4VP.
* Transaction data MUST be present in all SCA presentation requests (see [Topic 20]).
* The Wallet SHOULD respect VC metadata published by the Issuer at the VCT metadata endpoint for transaction
  data display rules.
* SCA-User SHALL NOT be presented to Relying Parties other than the issuing bank.

**Device binding:**

* This attestation SHALL be device-bound (ARB_34 in [Topic 12]).
* The device binding key SHALL be attested at AVA_VAN.3 or higher.
* The attestation MAY be cryptographically bound to the holder's PID. If so, `cryptographically_bound_to`
  SHALL carry the value `"eu.europa.ec.eudi.pid.1"` (ISO/IEC 18013-5) or `"urn:eudi:pid:1"` (SD-JWT VC).

Issuer of SCA-User is, for the purpose of WE BUILD, a Bank acting as ASPSP in PSD2.

Before issuance, the Bank SHALL check Wallet eligibility:

* Wallet provider is trusted for this purpose via a trust list.
* Wallet Unit is in operational state with valid WUA/WIA and PID.
* Wallet Unit has an eligible WSCD available at AVA_VAN.4 or higher.
* The user identified by this Wallet Unit is the same user logged into the banking environment.

Eligibility checks MAY be performed by:

* Requesting WUA and WIA and validating the signing certificate and key attestations.
* Requesting a PID and matching its attributes with the authenticated user's data.

When issuing the attestation, the Issuer SHALL:

* Use a sender-constrained token (DPoP) to ensure that only the requesting Wallet may receive the issued credential.
* Provide means to refresh the attestation (i.e., refresh tokens).
* Ensure that the attestation is device-bound with sufficient secure storage (AVA_VAN.4 or higher).
* Include or publish information about allowed verifiers; Embedded Disclosure policies or the `aud` claim SHALL
  be used for this purpose.

Deferred issuance is not recommended, the user is in the loop and banks should be able to process the issuance
request online.

After receiving the attestation, the Wallet SHOULD notify the Issuer of successful acceptance.

### 7.3 Lifecycle management

The issuer sets the validity period of the attestation and reissues it when the
underlying facts change, revoking the superseded attestation as described in chapter 8.

### 7.4 Embedded disclosure policy

This attestation defines no embedded disclosure policy.

## 8 Revocation

SCA-User attestations are intended to be **short-lived**. The recommended validity period is 24 hours or less,
combined with a token refresh mechanism at the Issuer. For such short-lived attestations, revocation is not
necessary.

For deployments where attestation validity exceeds 24 hours, the Issuer SHALL implement revocation using the
**Attestation Status List** mechanism referenced in the `status_list` claim, in accordance with the Technical
Specification to be specified by the Commission (currently tracked as
[draft-ietf-oauth-status-list-17](https://www.ietf.org/archive/id/draft-ietf-oauth-status-list-17.html)).

Relying Parties SHALL check the `status_list` reference when present and reject attestations whose status
indicates revocation or suspension.

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

SCA-User is a non-qualified EAA. The following trust anchor mechanism applies:

The Issuer SHALL publish a machine-readable trust anchor at a URL referenced in the `vct` metadata document.
Relying Parties SHALL use this URL to retrieve the trust anchor and verify that the provider is authorized to
issue the attestation.

Because SCA-User is exclusively 2-party, the Relying Party is always the issuing bank itself. The bank SHALL
maintain an internal trust anchor registry that maps VCT URLs to their corresponding signing keys, and SHALL
use this registry to verify presented credentials.

For the Wallet Unit, issuance eligibility verification (see section 4.1) serves as the mechanism for confirming
that the provider is authorized to issue this attestation type (see ISSU_34 in [Topic 10]).

The trust anchor SHALL be published as a JSON Web Key Set (JWKS) at a URL of the form:

```
https://issuer.bank.cz/.well-known/jwt-vc-issuer
```

conforming to the issuer metadata discovery mechanism defined in [SD-JWT VC] §5.3.

**Trust anchor location**

The attribute or metadata carrying the trust anchor location contains at least the URL
at which a machine-readable version can be found or looked up.

## 11 References

| **Item Reference** | **Standard name/details** |
| --- | --- |
| [European Digital Identity Regulation] | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework |
| [HAIP] | Yasuda, K. *et al,* OpenID4VC High Assurance Interoperability Profile, OpenId Foundation, Version draft-03 |
| [IANA-JWT-Claims] | IANA JSON Web Token Claims Registry. Available: <https://www.iana.org/assignments/jwt/jwt.xhtml> |
| [ISO/IEC 18013-5] | ISO/IEC 18013-5, Personal identification, ISO-compliant driving licence - Part 5: Mobile driving licence (mDL) application, First edition, 2021-09 |
| [OIDC] | Sakimura, N. et al., "OpenID Connect Core 1.0", OpenID Foundation. Available: <https://openid.net/specs/openid-connect-core-1_0.html> |
| [RFC 2119] | RFC 2119 - Key words for use in RFCs to Indicate Requirement Levels, S. Bradner, March 1997 |
| [RFC 3339] | RFC 3339 - Date and Time on the Internet: Timestamps, G. Klyne et al., July 2002 |
| [RFC 7519] | RFC 7519 - JSON Web Token (JWT), M. Jones et al., May 2015 |
| [RFC 7800] | RFC 7800 - Proof-of-Possession Key Semantics for JSON Web Tokens (JWTs), M. Jones et al., April 2016 |
| [RFC 8610] | RFC 8610 - Concise Data Definition Language (CDDL), H. Birkholz et al., June 2019 |
| [RFC 8943] | RFC 8943 - Concise Binary Object Representation (CBOR) Tags for Date, M. Jones et al., November 2020 |
| [RFC 8949] | RFC 8949 - Concise Binary Object Representation (CBOR), C. Bormann et al., December 2020 |
| [SD-JWT VC] | SD-JWT-based Verifiable Credentials (SD-JWT VC). Available: <https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/>, version draft-ietf-oauth-sd-jwt-vc-09 |
| [Topic 7] | ARF Annex 2 - Topic 7 - Attestation revocation and revocation checking Available: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a237-topic-7-attestation-revocation-and-revocation-checking> |
| [Topic 10] | ARF Annex 2 - Topic 10 - Issuing a PID or attestation to a Wallet Unit: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a2310-topic-10-issuing-a-pid-or-attestation-to-a-wallet-unit> |
| [Topic 12] | ARF Annex 2 - Topic 12 - Attestation Rulebooks, Available: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a2312-topic-12-attestation-rulebooks> |
| [Topic 20] | ARF Annex 2 - Strong User authentication for electronic payments, Available: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a2320-topic-20-strong-user-authentication-for-electronic-payments> |
| [TS12] | TS12 - Electronic Payments SCA Implementation with Wallet, European Commission. Available: <https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts12-electronic-payments-SCA-implementation-with-wallet.md> |
| [W3C VCDM v2.0] | Sporny, M. *et al,* Verifiable Credentials Data Model v2.0, W3C Recommendation. |
