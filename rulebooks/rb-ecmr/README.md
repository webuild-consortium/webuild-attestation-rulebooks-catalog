# Attestation Rulebook for attestations of type eCMR

Category: non-qualified EAA

**Author(s):**
- Christophe DANNA, IN Groupe
- Mohamed OULMAHDI, IN Groupe
- Heiti MERING, Digilogistika Keskus

**Reviewer(s)**
- [to be added] when passing to V0.7 

**Version History**

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

The eCMR Attestation is a verifiable electronic attestation designed to provide trusted, portable and interoperable evidence of an Electronic Consignment Note (eCMR) within the EUDI Wallet ecosystem. The attestation is issued by a trusted eCMR platform and enables transport stakeholders and competent authorities to verify the authenticity, integrity and provenance of transport information. The eCMR attestation issued to a company and presented by the driver with its EBW is a multi-purposes attestation: 
-	Link to eCMR, used to give access only to the right consignment data (MVP);
-	The document itself for offline presentation by the driver (PDF, MVP+);
-	eFTI QR Code for roadside checks by authorities (via eFTI network, MVP+).


The attestation expresses the existence of a valid eCMR and establishes a trusted link between:

- The transport consignment;
- The issuing eCMR platform;
- The identified business parties involved in the transport operation;
- The evidence document associated with the transport operation.

The attestation supports:

- Roadside inspections;
- Cross-border freight transport operations;
- Logistics ecosystem interoperability;
- Future eFTI integration scenarios;
- Both online and offline (MVP+) verification processes. 

The primary actors are:

| Role | Description |
| --- | --- |
| Issuer | Trusted eCMR platform |
| Holder | Driver, carrier representative or authorised business wallet holder |
| Relying Party | Logistics stakeholders (MVP) and roadside authorities (MVP+) |

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

Additional terms used in this document:

| Term | Definition |
| --- | --- |
| EBWOID | European Business Wallet Owner Identifier |
| Business Wallet | Wallet associated with a legal entity |
| eCMR Platform | Platform managing electronic consignment records |
| Consignment | Transport operation represented by an eCMR |
| CMDS | Consignment Movement DataSet -> the consignment XML data |
| Roadside Check | Verification procedure performed by enforcement authorities |

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


The eCMR Attestation SHALL be issued exclusively as an ISO/IEC 18013-5 compliant mDoc. The workshop concluded that mDoc is the preferred format because it supports proximity presentation, offline verification and compatibility with EUDI Wallet requirements. 

The attestation provides:

- Identification of a specific transport consignment;
- Trusted identification of involved business parties through EBWOIDs;
- Integrity protection of transport information;
- Support for both online and offline verification scenarios;
- Support for human-readable document presentation when required by national regulations. 

The attribute `attestation_legal_category` SHALL indicate the legal classification of the attestation. This attestation type is classified as "EAA" within the EBW Wallet ecosystem, as it is typically issued by an eCMR platform and no authentic source is used.

All attributes and metadate SHALL be disclosable.


### 3.2 Mandatory attributes

#### 2.2.1 Consignment identification 

| Data Identifier | Definition | Data Type | Example Value |
| --- | --- | --- | --- |
| consignment_identifier | Unique identifier of the consignment* | string | CMR-2026-000123 |
| ecmr_platform_url | URL of the originating eCMR platform | URI | https://platform.example.eu/ecmr/CMR-2026-000123 |


* The issuing eCMR platform can freely use whatever content needed to identify the consignment and its eCMR. On purpose, already defined Id fields in UN/CEFACT Electronic Road Consignment Note (eCMR)are not used [UN/CEFACT eCMR].

### 3.3 Optional attributes

Optional attributes are the eFTI Information and a human readable eCMR (MVP+).

#### 2.3.1 eFTI information (MVP+)

eFTI Unique Information Link.

| Data Identifier | Definition | Data Type | Example Value |
| --- | --- | --- | --- |
| efti_dataset_identifier | The unique ID of an eFTI CMDS, assigned by an eFTI platform | String-36 | EFTI-248811 |
| efti_platform_identifier | The identifier of an eFTI platform | String-17 | EFTI-PLAT-45 |
| efti_gate_identifier | The identifier of an eFTI gate | String-17 | EFTI-GATE-12 |

Note1: at the present time, the naming rule for eFTI platform and gate identifiers has not been defined yet by the eFTI technical guidance documents. Examples are fictional.

Note2: Other fields might be considered whith MVP+ scenario and added later if needed.
- QR Code image could be added later if needed.
- XML MMT file (base64).

#### 2.3.2 Human readable eCMR (MVP+)
| Data Identifier | Definition | Data Type | Example Value |
| --- | --- | --- | --- |
| embedded_ecmr_pdf | Embedded human-readable eCMR document for offline presentation | actual pdf/a file as base64 string |  |

Note: no embedded transport dataset representation, only a human readable document 

These attributes must be present when offline verification or human-readable presentation is required. Optional in MVP, mandatory in MVP+.

### 3.4 Conditional attributes

#### 2.4.1 Parties identification (MVP)

| Data Identifier | Definition | Data Type | Example Value |
| --- | --- | --- | --- |
| consignor_ebwoid | ebwoid of the issuing organisation | String | SEBOLREG.123456789 |
| carrier_ebwoid | ebwoid of the carrier | String | NOFOR.123456789 |
| consignee_ebwoid | ebwoid of the consignor | String | SEBOLREG.987654321 |

Note: At least One ebwoid SHALL be included in the attestation, depending on the step reached in process.

## 4 Metadata

Metadata describes the attestation rather than its subject.

### 4.1 Mandatory metadata

| Data Identifier | Definition | Data Type | Example Value |
| --- | --- | --- | --- |
| attestation_legal_category | Legal category of the attestation | String | non-qualified-EAA |
| issuer_ebwoid | ebwoid of the issuing organisation | String | EU.ebwoid.12345678 |
| trust_anchor_url | URL of trust anchor information | URI | https://trust.webuild.eu |
| expiry_date | Expiration date of the attestation | DateTime | 2026-07-30T00:00:00Z |
| attestation_scheme | Attestation schema | String | TBD |
| issuance_date | Timestamp of issuance | datetime | 2026-06-30T10:25:00Z |

**Legal category.** This Rulebook retains the `attestation_legal_category` attribute.
Section 4.1 of the generic template replaces it with the `category` attribute of
[ETSI TS 119 472-1], whose value for this category is `eaa:eu:non-qualified`.
EW-DM-12-029, legacy ARB_25, of ARF version 3.0.0 is a SHALL that still requires
`attestation_legal_category`, so the template and the ARF disagree. The attribute is
left as written and the deviation is recorded for the rulebook quality assurance group.

### 4.2 Optional metadata

None

### 4.3 Conditional metadata

None

### 4.4 Code lists

| Field Name | Allowed Values | Meaning | Source |
| --- | --- | --- | --- |
| attestation_legal_category | "non-qualified-EAA" | Legal classification of the attestation | EUDI Framework |

### 4.5 Integrity rules

| Rule ID | Rule Statement |
| --- | --- |
| IR-01 | A mandatory string attribute SHALL be a non-empty string |
| IR-02 | datetime SHALL be ISO 8601 compliant |


## 5 Formats


### 5.1 SD-JWT VC-based encoding

 SD-JWT is out of scope for this rulebook, as offline proximity is required.

### 5.2 ISO/IEC 18013-5-compliant encoding

The eCMR Attestation SHALL be issued exclusively as an ISO/IEC 18013-5 compliant mDoc. This format supports:

- Device-to-device proximity presentation;
- Offline verification;
- Integration within the EUDI Wallet ecosystem;
- Embedded transport evidence;
- Selective disclosure mechanisms. 

docType `"eu.webuildconsortium.ecmr.attestation.V1`

Namespace `"eu.webuildconsortium.ecmr.attestation.V1`

#### Illustrative example

Example for MVP scenario (mandatory fields only). See clarification about MVP and MVP+ scenarios in section [1.1 Document scope and purpose ](#1.1-Document-scope-and-purpose).


```json
{
  "docType": "eu.webuildconsortium.ecmr.attestation.V1",
  "issuerSigned": {
    "namespaces": {
      "eu.webuild.ecmr.attestation.1": [
        {"elementIdentifier": "attestation_legal_category", "elementValue": "non-qualified-EAA"},
        {"elementIdentifier": "trust_anchor_url", "elementValue": ""},
        {"elementIdentifier": "attestation_scheme", "elementValue": "TBD"},
        {"elementIdentifier": "consignment_identifier", "elementValue": "CMR-2026-000123"},
        {"elementIdentifier": "ecmr_platform_url", "elementValue": "https://platform.example.eu/ecmr/CMR-2026-000123"},
        {"elementIdentifier": "issuer_ebwoid", "elementValue": "EU.ebwoid.12345678"},
        {"elementIdentifier": "carrier_ebwoid", "elementValue": "EU.ebwoid.87654321"},
        {"elementIdentifier": "consignor_ebwoid", "elementValue": "EU.ebwoid.11223344"},
        {"elementIdentifier": "consignee_ebwoid", "elementValue": "EU.ebwoid.11789463"},
        {"elementIdentifier": "expiry_date", "elementValue": "2026-07-30T00:00:00Z"},
        {"elementIdentifier": "issuance_date", "elementValue": "2026-06-30T10:25:00Z"}
      ]     
    }    
}
```

### 5.3 W3C Verifiable Credentials Data Model-based encoding


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


The eCMR attestation is issued and managed by an eCMR platform throughout the transport lifecycle. 
- The platform creates the initial eCMR and generates a unique identifier linked to the consignment. 
- Pickup and delivery activities are initiated and managed through the platform using Business Wallet authentication. 
- The eCMR platform issues updated eCMR version. 
- The eCMR platform revoke the older eCMR Attestation when a new version is issued.

### 7.3 Lifecycle management

The issuer sets the validity period of the attestation and reissues it when the
underlying facts change, revoking the superseded attestation as described in chapter 8.

### 7.4 Embedded disclosure policy

This attestation defines no embedded disclosure policy.

## 8 Revocation

A balance between security and usability must be found:
- Short-lived (24 hours) needs re-issuance / renewal by the issuer. ECMR lifecycle is much longer than one day. 
- Status List or revocation List requires internet access to retrieve trusted lists. 
Maintaining a cached copy of the trusted list and revocation information, updated regularly, may enable offline verification (MVP+).

The eCmr Platform (self-issuing entity) SHALL immediately update or revoke its EAA eCMR Attestation when a new version is issued. Nonetheless, the expiracy date SHALL always be set, especially when the eCMR is not the final one.

Note: WeBuild IETF Token Status List SHOULD be used to perform revocation checks to validate credentials.

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

The relying party, typically a competent authority, receives the eCMR attestation presented through the Business Wallet.
Where available, the relying party extracts the eFTI UIL from the eCMR attestation. 
The UIL is used to submit a query through the national eFTI Gate to locate the authoritative dataset. 
In offline situations, verification may rely solely on the wallet-based presentation

### 9.2 Presentation modes

Remote presentation is in scope. Proximity presentation is in scope only where
chapter 5 records an mdoc encoding.

### 9.3 Transactional data

This Rulebook defines no transactional data.

## 10 Trust Framework

The trust model relies on:

- Trusted eCMR platform issuers;
- Business Wallet identities;
- ebwoid-based legal entity identification;
- Cryptographically signed attestations. 

Each participating organisation SHALL possess a Business Wallet containing an ebwoid identifying both its legal and technical identity. 

The trust chain SHALL enable verification of:

1. The attestation signature.
2. The issuing eCMR platform.
3. The identified legal entity.
4. The associated trust anchor. 

For EAAs, trust is established through a cryptographic chain anchored in the Electronic Business Wallet Owner Identity Document (EBWOID). The EBWOID SHALL be included in the header of every EAA. During EBWOID issuance, the EBWOID provider verifies that the public key contained in the EBWOID is owned by the Electronic Business Wallet (EBW) owner.

The Relying Party (eCMR Platform) SHALL verify the EBWOID. Upon successful verification, the Relying Party obtains:

- assurance that the EBWOID was issued by an authorized provider and is not self-issued;
- the verified identity of the issuer, including its name and EUID (or another globally unique EBW owner identifier); and
- the public key authorized to verify the EAA signature.

**Trust anchor location**

The attribute or metadata carrying the trust anchor location contains at least the URL
at which a machine-readable version can be found or looked up.

## 11 References

| Reference | Description |
| --- | --- |
| Regulation (EU) 2024/1183 | European Digital Identity Regulation |
| ISO/IEC 18013-5 | Mobile Driving Licence (mDoc) Standard |
| ISO 8601 | International standard for date and time representations |
| EUDI ARF | European Digital Identity Architecture Reference Framework |
| eFTI Regulation | Electronic Freight Transport Information Regulation |
| [UN/CEFACT eCMR] | Electronic Consignment Note Specification https://unece.org/trade/documents/2024/12/standards/ecmr-d24a |
