# Attestation Rulebook for attestations of type Boarding Pass

Category: non-qualified EAA

(Template version: 1.1)


*[Based on the WE BUILD Attestation Rulebook Template and the Ferry Boarding Pass Attestation model.]*

* Author(s):
    * Nikos Triantafyllou, UAegean
* Previous Authors
    * N/A


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

This Rulebook defines the *Ferry Boarding Pass Attestation* for use in the European Digital Identity Wallet ecosystem.

The Ferry Boarding Pass Attestation expresses the real-world fact that a natural person holds a valid boarding pass for a specific ferry journey and is entitled to board a specific vessel at a given departure date and time.

The attestation is intended to be issued by an authentic source, such as a ferry operator or an authorised ticketing system acting on behalf of the ferry operator. The Holder is the passenger to whom the boarding entitlement applies. Relying Parties include ferry operators, port boarding gates, authorised boarding control staff, and other authorised systems that need to verify boarding entitlement.

In practical terms, the attestation enables a passenger to present proof of boarding entitlement through an EUDI Wallet. It can reduce reliance on paper tickets and can reduce the need for real-time backend lookups during boarding, provided that the Relying Party can verify the issuer, the signature, the validity period, and the relevant journey details.

The attestation supports ferry boarding use cases, including online or offline verification at ports and boarding gates. It contains journey-specific and passenger-specific information strictly related to the boarding process, including passenger name, ticket identifiers, departure and arrival information, vessel information, and seat allocation where applicable.

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

In addition, the following domain-specific terms are used:

| Term | Meaning |
| --- | --- |
| Ferry Boarding Pass Attestation | A Verifiable Credential representing a passenger's entitlement to board a specific ferry journey. |
| Ferry operator | The organisation operating the ferry journey or acting as the authentic source for the boarding entitlement. |
| Authorised ticketing system | A system authorised by the ferry operator to issue or manage boarding passes. |
| Passenger | The natural person to whom the boarding entitlement applies. |
| Boarding gate | A physical or digital checkpoint where the boarding entitlement is verified. |
| Journey | A specific ferry trip between a departure port and an arrival port at a scheduled date and time. |

## 2 Compliance

### 2.1 Compliance statement

This Rulebook complies with the applicable requirements of Topic 12, Attestation
Rulebooks, in Annex 2 of the Architecture and Reference Framework, version 3.0.0. It
uses the terminology of Annex 1 of the ARF.

This Rulebook is designed to align with the EUDI Wallet architectural approach for Electronic Attestations of Attributes and with the Attestation Rulebook structure defined in the ARF.

The Rulebook supports the following compliance objectives:

* it defines the attestation purpose and scope;
* it defines mandatory, optional, and conditional attributes in an encoding-independent manner;
* it defines a legal category indication through `attestation_legal_category`;
* it defines an SD-JWT VC `vct` value for the attestation type;
* it defines issuer, validity, and status metadata needed for verification;
* it defines code lists and integrity rules required for consistent interpretation;
* it defines how trust anchors can be obtained and used;
* it defines expiry and revocation expectations;
* it supports selective disclosure and data minimisation.

This Rulebook does not define a qualified EAA or public-sector EAA profile. It also does not define ISO/IEC 18013-5 mdoc or W3C VCDM encodings in this version.

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


The Ferry Boarding Pass Attestation is defined as a non-qualified Electronic Attestation of Attributes unless a future version of this Rulebook explicitly defines a qualified or public-sector legal category.

The attribute `attestation_legal_category` SHALL be included and SHALL have the value `non-qualified-EAA`.

The attestation model consists of the following logical groups:

* passenger identification data;
* ticket identifiers;
* journey details;
* vessel and port information;
* issuer information;
* credential metadata.

The attestation is bound to a single passenger and a single ferry journey. It SHALL NOT be treated as a reusable credential after the scheduled departure time.

#### 1 Introduction

#### Chapter overview and requirements

This chapter defines the attributes and metadata that a Ferry Boarding Pass Attestation may contain. The attributes are defined in an encoding-independent manner. Each attribute is classified as mandatory, optional, or conditional.

The Ferry Boarding Pass Attestation is journey-specific and time-bound. It contains only the information necessary to verify that the Holder is entitled to board a specific ferry service. The attribute set is intentionally limited to support data minimisation.

### 3.2 Mandatory attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| `attestation_legal_category` | ARF Topic 12 / Rulebook legal category indication | Indicates the legal category of the attestation. | string | `non-qualified-EAA` |
| `identifier` | N/A | Unique identifier of the boarding pass. | string | `BP-2026-000123456` |
| `ticketQR` | N/A | Encoded ticket representation used for scanning at boarding control. | string | `M1_FASTFERRIES_20260615_000123456` |
| `ticketNumber` | N/A | Ferry ticket number. | string | `000123456` |
| `firstName` | OIDC `given_name` where applicable | Passenger given name. | string | `Nikos` |
| `lastName` | OIDC `family_name` where applicable | Passenger family name. | string | `Triantafyllou` |
| `departureDate` | ISO 8601 date | Scheduled departure date. | date | `2026-06-15` |
| `departureTime` | ISO 8601 / local time | Scheduled departure time, expressed in the local time of the departure port. | string | `07:30` |
| `arrivalDate` | ISO 8601 date | Scheduled arrival date. | date | `2026-06-15` |
| `arrivalTime` | ISO 8601 / local time | Scheduled arrival time, expressed in the local time of the arrival port. | string | `12:45` |
| `arrivalPort` | UN/LOCODE recommended | Destination port. | string | `GRMLO` |
| `vesselDescription` | N/A | Description or name of the ferry vessel. | string | `Fast Ferries Andros` |
| `issuer.issuing_country` | ISO 3166-1 alpha-2 | Country of the ferry operator or authorised ticketing operator. | string | `GR` |
| `issuer.issuing_organisation` | N/A | Legal name of the ferry operator or authorised ticketing operator. | string | `Fast Ferries S.A.` |
| `issuer.issuing_date` | ISO 8601 date | Date of issuance of the boarding pass. | date | `2026-06-01` |

### 3.3 Optional attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| `ticketLet` | N/A | Ticket letter, ticket class code, or other operator-specific classification. | string | `A` |
| `seatType` | N/A | Type of seat or accommodation. | string | `AIR_SEAT` |
| `seatNumber` | N/A | Assigned seat number. | string | `12A` |

### 3.4 Conditional attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| `seatNumber` | N/A | Assigned seat number. SHALL be present only where a specific seat is allocated to the passenger. MUST be omitted if free seating applies. | string | `12A` |
| `seatType` | N/A | Type of seat or accommodation. SHOULD be present where the ticket product or boarding process depends on the seat or accommodation category. | string | `DECK` |

## 4 Metadata

Metadata describes the attestation rather than its subject.

### 4.1 Mandatory metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| `vct` | SD-JWT VC | Verifiable Credential Type identifying this attestation type. | string | `urn:eu.europa.ec.eudi:ferry_boarding_pass:1` |
| `iss` | SD-JWT VC / JWT | Identifier of the issuer of the credential. | string | `https://issuer.example-ferry.gr` |
| `iat` | JWT | Time at which the credential was issued. | integer | `1780315200` |
| `exp` | JWT | Expiration time of the credential. For this attestation it SHALL NOT be later than the scheduled departure time unless operational rules explicitly require a short post-departure grace period. | integer | `1781508600` |
| `cnf` | SD-JWT VC / JOSE | Confirmation claim binding the credential to key material controlled by the Holder or Wallet Unit, where holder binding is used. | object | `{ "jwk": { ... } }` |
| `status` | SD-JWT VC status mechanism, where used | Status information enabling revocation or suspension checks, where revocation is supported. | object | `{ "status_list": { ... } }` |

**Legal category.** This Rulebook retains the `attestation_legal_category` attribute.
Section 4.1 of the generic template replaces it with the `category` attribute of
[ETSI TS 119 472-1], whose value for this category is `eaa:eu:non-qualified`.
EW-DM-12-029, legacy ARB_25, of ARF version 3.0.0 is a SHALL that still requires
`attestation_legal_category`, so the template and the ARF disagree. The attribute is
left as written and the deviation is recorded for the rulebook quality assurance group.

### 4.2 Optional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| `nbf` | JWT | Time before which the credential MUST NOT be accepted. | integer | `1780315200` |
| `jti` | JWT | Unique identifier of the credential instance. | string | `urn:uuid:1ddcf8dc-3f0b-4b30-987d-5eacb9dba111` |
| `trust_anchor` | ARF Topic 12 | Location or identifier of the machine-readable trust anchor or trust framework entry used to verify issuer authorisation. | string | `https://trust.example.eu/ferry/operators/fast-ferries` |
| `cryptographically_bound_to` | ARF Topic 12 / ARB_28 | Identifier of another attestation type to which this attestation is cryptographically bound, where such binding is used. | string | `urn:eudi:pid:1` |

### 4.3 Conditional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| `status` | SD-JWT VC status mechanism, where used | SHALL be present if the issuer supports revocation or suspension for the boarding pass. MAY be omitted where the attestation is short-lived and expires at or before departure time. | object | `{ "status_list": { ... } }` |
| `cryptographically_bound_to` | ARF Topic 12 / ARB_28 | SHOULD be present where the boarding pass is required to be presented together with PID or another identity attestation for passenger identity matching. | string | `urn:eudi:pid:1` |

### 4.4 Code lists

| **Field name** | **Allowed values** | **Meaning** | **Source / vocabulary** | **Notes / extensibility** |
| --- | --- | --- | --- | --- |
| `arrivalPort` | Valid port identifiers | Identifies the destination port. | UN/LOCODE recommended | Implementations MAY also support operator-specific port identifiers during pilots, provided mapping to UN/LOCODE is maintained where available. |
| `issuer.issuing_country` | ISO 3166-1 alpha-2 country codes | Identifies the country of the ferry operator or authorised ticketing operator. | ISO 3166-1 alpha-2 | Extensions SHALL NOT be used. |
| `departureDate` | ISO 8601 date | Scheduled departure date. | ISO 8601 | Date-only format SHOULD be used. |
| `arrivalDate` | ISO 8601 date | Scheduled arrival date. | ISO 8601 | Date-only format SHOULD be used. |
| `issuer.issuing_date` | ISO 8601 date | Date on which the boarding pass was issued. | ISO 8601 | Date-only format SHOULD be used. |
| `departureTime` | Local time string | Scheduled departure time in the local time of the departure port. | ISO 8601 time representation recommended | Time-zone handling SHALL be clear to the verifier. |
| `arrivalTime` | Local time string | Scheduled arrival time in the local time of the arrival port. | ISO 8601 time representation recommended | Time-zone handling SHALL be clear to the verifier. |
| `attestation_legal_category` | `non-qualified-EAA`, `QEAA`, `PuB-EAA` | Indicates the legal category of the attestation. | ARF Topic 12 / Rulebook template | This Rulebook uses `non-qualified-EAA`. |

### 4.5 Integrity rules

| **Rule ID** | **Rule statement** | **Why it exists** | **Where enforced** | **Verifier / issuer behavior on failure** |
| --- | --- | --- | --- | --- |
| `BP-IR-01` | `arrivalDate` SHALL NOT precede `departureDate`. | Prevents temporally inconsistent journey information. | Issuer business rules, schema validation, verifier business validation. | Issuer SHALL reject inconsistent journey data. Verifier SHALL reject the attestation for boarding if this rule fails. |
| `BP-IR-02` | The boarding pass SHALL be bound to a single journey. | Prevents reuse across different services, vessels, or dates. | Issuer business rules and verifier business validation. | Verifier SHALL reject the attestation if it cannot determine the specific journey. |
| `BP-IR-03` | The attestation SHALL NOT be reusable after the scheduled departure time. | Boarding entitlement is time-bound and journey-specific. | Issuer validity period and verifier freshness checks. | Verifier SHALL reject the attestation after expiry, unless a locally defined operational grace period applies. |
| `BP-IR-04` | `seatNumber` MUST be omitted if free seating applies. | Prevents misleading seat allocation information. | Issuer business rules and schema validation. | Issuer SHALL omit `seatNumber` for free seating. Verifier SHOULD ignore or reject inconsistent seat allocation data. |
| `BP-IR-05` | `identifier` SHALL be unique for each boarding pass issued by the issuer. | Enables unambiguous identification, audit, and status checking. | Issuer business rules. | Issuer SHALL prevent duplicate identifiers. Verifier MAY reject duplicated identifiers if detected. |
| `BP-IR-06` | Passenger name attributes in the boarding pass SHOULD be compared with PID or another accepted identity source when the boarding process requires identity matching. | Ensures that the person presenting the boarding pass is the intended passenger. | Relying Party business validation. | Verifier SHOULD reject the boarding transaction where required identity matching fails. |


## 5 Formats


### 5.1 SD-JWT VC-based encoding

The Ferry Boarding Pass Attestation SHALL be issued as an SD-JWT VC.

The Verifiable Credential Type (`vct`) for this attestation type is:

```text
urn:eu.europa.ec.eudi:ferry_boarding_pass:1
```

The credential claims defined in this section SHALL follow SD-JWT VC and HAIP conventions where applicable. Claim names are either IANA-registered JWT claims, public names, or private names specific to this attestation type.

For all claims, this Rulebook specifies whether an Attestation Provider MUST, MAY, or MUST NOT make the claim selectively disclosable.

#### 3.2.1 IANA-registered and standard JWT / SD-JWT VC claims

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Reference/Notes** | **Disclosable** |
| --- | --- | --- | --- | --- |
| `iss` | `iss` | string | JWT issuer identifier. | MUST NOT |
| `iat` | `iat` | integer | Issued-at timestamp. | MUST NOT |
| `nbf` | `nbf` | integer | Not-before timestamp, where used. | MUST NOT |
| `exp` | `exp` | integer | Expiration timestamp. SHALL NOT be later than the scheduled departure time unless operational rules define a short grace period. | MUST NOT |
| `jti` | `jti` | string | Unique credential instance identifier, where used. | MUST NOT |
| `cnf` | `cnf` | object | Holder binding confirmation claim, where used. | MUST NOT |
| `status` | `status` | object | Status or revocation information, where used. | MUST NOT |
| `vct` | `vct` | string | SD-JWT VC type. Value SHALL be `urn:eu.europa.ec.eudi:ferry_boarding_pass:1`. | MUST NOT |

#### 3.2.2 Public or reusable claims

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Reference/Notes** | **Disclosable** |
| --- | --- | --- | --- | --- |
| `firstName` | `firstName` | string | Passenger given name. May be mapped to OIDC `given_name` in implementations that use OIDC naming conventions. | MUST |
| `lastName` | `lastName` | string | Passenger family name. May be mapped to OIDC `family_name` in implementations that use OIDC naming conventions. | MUST |

#### 3.2.3 Private claims specific to the Ferry Boarding Pass Attestation

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Notes** | **Disclosable** |
| --- | --- | --- | --- | --- |
| `attestation_legal_category` | `attestation_legal_category` | string | SHALL be `non-qualified-EAA`. | MUST NOT |
| `identifier` | `identifier` | string | Unique boarding pass identifier. | MUST |
| `ticketQR` | `ticketQR` | string | Encoded ticket representation used for scanning. | MAY |
| `ticketNumber` | `ticketNumber` | string | Ferry ticket number. | MUST |
| `ticketLet` | `ticketLet` | string | Ticket letter, class, or operator-specific code. | MAY |
| `seatType` | `seatType` | string | Seat or accommodation type. | MAY |
| `seatNumber` | `seatNumber` | string | Assigned seat number, where applicable. | MAY |
| `departureDate` | `departureDate` | string | Scheduled departure date, formatted as ISO 8601 date. | MUST |
| `departureTime` | `departureTime` | string | Scheduled departure time in local time of the departure port. | MUST |
| `arrivalDate` | `arrivalDate` | string | Scheduled arrival date, formatted as ISO 8601 date. | MUST |
| `arrivalTime` | `arrivalTime` | string | Scheduled arrival time in local time of the arrival port. | MUST |
| `arrivalPort` | `arrivalPort` | string | Destination port. UN/LOCODE recommended. | MUST |
| `vesselDescription` | `vesselDescription` | string | Name or description of the ferry vessel. | MUST |
| `issuer` | `issuer` | object | Issuer object containing ferry operator or authorised ticketing operator information. | MUST NOT |
| `issuer.issuing_country` | `issuing_country` | string | Country of the ferry operator or authorised ticketing operator. | MUST NOT |
| `issuer.issuing_organisation` | `issuing_organisation` | string | Legal name of the ferry operator or authorised ticketing operator. | MUST NOT |
| `issuer.issuing_date` | `issuing_date` | string | Date of issuance of the boarding pass, formatted as ISO 8601 date. | MUST NOT |
| `trust_anchor` | `trust_anchor` | string | Location or identifier of the trust anchor or trust framework entry used to verify issuer authorisation, where used. | MUST NOT |
| `cryptographically_bound_to` | `cryptographically_bound_to` | string | Identifier of another attestation type to which this attestation is bound, where used. | MUST NOT |

#### 3.2.4 Example JWT claim set

```json
{
  "iss": "https://issuer.example-ferry.gr",
  "iat": 1780315200,
  "nbf": 1780315200,
  "exp": 1781508600,
  "jti": "urn:uuid:1ddcf8dc-3f0b-4b30-987d-5eacb9dba111",
  "vct": "urn:eu.europa.ec.eudi:ferry_boarding_pass:1",
  "attestation_legal_category": "non-qualified-EAA",
  "identifier": "BP-2026-000123456",
  "ticketQR": "M1_FASTFERRIES_20260615_000123456",
  "ticketNumber": "000123456",
  "ticketLet": "A",
  "firstName": "Nikos",
  "lastName": "Triantafyllou",
  "seatType": "AIR_SEAT",
  "seatNumber": "12A",
  "departureDate": "2026-06-15",
  "departureTime": "07:30",
  "arrivalDate": "2026-06-15",
  "arrivalTime": "12:45",
  "arrivalPort": "GRMLO",
  "vesselDescription": "Fast Ferries Andros",
  "issuer": {
    "issuing_country": "GR",
    "issuing_organisation": "Fast Ferries S.A.",
    "issuing_date": "2026-06-01"
  },
  "trust_anchor": "https://trust.example.eu/ferry/operators/fast-ferries",
  "cnf": {
    "jwk": {
      "kty": "EC",
      "crv": "P-256",
      "x": "...",
      "y": "..."
    }
  }
}
```

#### 3.2.5 Example issued SD-JWT

The following is a non-normative placeholder example. A production SD-JWT SHALL be generated by the issuer using the applicable signing algorithm, disclosure construction, holder binding, and SD-JWT VC rules.

```text
<issuer-signed-sd-jwt>~<disclosure-1>~<disclosure-2>~<disclosure-n>~<holder-binding-jwt>
```

#### 3.2.6 Example human-readable disclosed payload

A verifier that requests the minimum data needed for boarding may receive a presentation disclosing the following claims:

```json
{
  "vct": "urn:eu.europa.ec.eudi:ferry_boarding_pass:1",
  "identifier": "BP-2026-000123456",
  "ticketNumber": "000123456",
  "firstName": "Nikos",
  "lastName": "Triantafyllou",
  "departureDate": "2026-06-15",
  "departureTime": "07:30",
  "arrivalDate": "2026-06-15",
  "arrivalTime": "12:45",
  "arrivalPort": "GRMLO",
  "vesselDescription": "Fast Ferries Andros"
}
```

The issuer identity, credential type, expiry time, signature, holder binding proof, and trust anchor information are not treated as selectively disclosable passenger attributes and SHALL remain available to the verifier for technical validation.

### 5.2 ISO/IEC 18013-5-compliant encoding

This version of the Rulebook does not define an ISO/IEC 18013-5 mdoc encoding for the Ferry Boarding Pass Attestation.

The Ferry Boarding Pass Attestation defined in this Rulebook is specified for SD-JWT VC-based issuance and presentation. If a future version of this Rulebook defines an ISO/IEC 18013-5-compliant mdoc representation, that version SHALL define a unique document type, namespaces, attribute identifiers, CBOR encoding rules, and illustrative mdoc examples.

### 5.3 W3C Verifiable Credentials Data Model-based encoding

This version of the Rulebook does not define a W3C Verifiable Credentials Data Model encoding for the Ferry Boarding Pass Attestation.

If a future version defines a W3C VCDM representation, that version SHALL define the credential context, type, credential subject structure, proof type, selective disclosure mechanism, and presentation requirements.

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

The Ferry Boarding Pass Attestation is intended for verifying passenger boarding entitlement for a specific ferry journey.

Typical usage scenarios include:

* presentation by the passenger at a port or boarding gate;
* scanning or digital verification by authorised boarding staff;
* online verification by a ferry operator system;
* offline or low-connectivity verification where the verifier can validate the credential signature, issuer, validity period, and disclosed journey data without relying on a real-time ticketing backend.

A Relying Party receiving the attestation SHALL verify:

* the issuer signature;
* the SD-JWT VC type (`vct`);
* the issuer authorisation to issue Ferry Boarding Pass Attestations;
* the credential validity period;
* the credential status, where a status mechanism is present;
* holder binding, where used;
* the integrity rules defined in Section 2.9;
* that the journey details match the boarding context.

The Relying Party SHOULD request and verify PID or another accepted identity credential when the boarding process requires passenger identity matching. In such cases, the Relying Party SHOULD compare the relevant identity attributes, such as passenger name, with the Ferry Boarding Pass Attestation. The Relying Party SHALL apply data minimisation and SHALL request only the attributes required for the boarding decision.

The attestation SHOULD be device-bound through holder binding where supported by the EUDI Wallet and the applicable SD-JWT VC profile. The attestation MAY be cryptographically bound to a PID or another accepted identity attestation where the boarding process requires stronger passenger identity matching. Where this binding is used, the metadata attribute `cryptographically_bound_to` SHOULD contain:

```text
urn:eudi:pid:1
```

No payment-specific transactional data is defined by this Rulebook. If the Ferry Boarding Pass Attestation is used as part of a transaction that also involves payment, payment-related requirements SHALL be defined in a separate payment attestation, payment profile, or transaction-specific rulebook.


### 7.3 Lifecycle management

The issuer sets the validity period of the attestation and reissues it when the
underlying facts change, revoking the superseded attestation as described in chapter 8.

### 7.4 Embedded disclosure policy

This attestation defines no embedded disclosure policy.

## 8 Revocation

The Ferry Boarding Pass Attestation is typically short-lived and journey-specific.

The preferred validity model for this attestation is short validity. The credential expiration time (`exp`) SHALL be set no later than the scheduled departure time unless a clearly defined operational grace period is required by the ferry operator or port boarding process.

After departure, the attestation SHALL be considered expired and SHALL NOT be accepted for boarding.

Revocation MAY be handled by one or more of the following mechanisms:

* short validity, where the attestation expires at or before departure time;
* backend verification by the ferry operator or authorised boarding system;
* an attestation status list mechanism, where supported;
* an attestation revocation list mechanism, where supported.

If a status or revocation mechanism is included in the credential, the Relying Party SHALL check the status before accepting the attestation, unless offline operating rules explicitly allow deferred status checking.

If a ticket is cancelled, refunded, exchanged, duplicated, or otherwise invalidated before departure, the issuer SHOULD either revoke or suspend the attestation, or ensure that backend verification detects the invalid state.

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

A Relying Party SHALL verify that the issuer of the Ferry Boarding Pass Attestation is authorised to issue this attestation type.

For non-qualified EAA deployments, the Relying Party SHOULD obtain trust anchor information through one or more of the following mechanisms:

* a machine-readable trust list or trust registry used by the relevant ecosystem;
* an issuer metadata endpoint published by the ferry operator or authorised ticketing operator;
* a trust framework entry managed by the WE BUILD ecosystem or by another authorised governance body;
* a pilot trust list used for controlled interoperability testing.

Where the metadata attribute `trust_anchor` is present, it SHOULD identify the location or registry entry from which the Relying Party can obtain the issuer trust anchor or issuer authorisation information.

The Relying Party SHALL use the trust anchor to verify that:

* the issuer signing key or certificate chains to a trusted authority or registered trust anchor;
* the issuer is authorised to issue the `urn:eu.europa.ec.eudi:ferry_boarding_pass:1` attestation type;
* the issuer metadata or trust framework entry has not expired or been revoked;
* the issuer identity in the credential is consistent with the issuer identity in the trust framework.

Wallet Units MAY also use the same trust framework information during issuance to determine whether the provider is authorised to issue this attestation type.

**Trust anchor location**

The attribute or metadata carrying the trust anchor location contains at least the URL
at which a machine-readable version can be found or looked up.

## 11 References

| **Item Reference** | **Standard name/details** |
| --- | --- |
| [European Digital Identity Regulation] | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework |
| [HAIP] | Yasuda, K. *et al,* OpenID4VC High Assurance Interoperability Profile, OpenID Foundation |
| [IANA-JWT-Claims] | IANA JSON Web Token Claims Registry. Available: <https://www.iana.org/assignments/jwt/jwt.xhtml> |
| [ISO/IEC 18013-5] | ISO/IEC 18013-5, Personal identification --- ISO-compliant driving licence - Part 5: Mobile driving licence application |
| [OIDC] | Sakimura, N. et al., OpenID Connect Core 1.0, OpenID Foundation. Available: <https://openid.net/specs/openid-connect-core-1_0.html> |
| [RFC 2119] | RFC 2119 - Key words for use in RFCs to Indicate Requirement Levels, S. Bradner, March 1997 |
| [RFC 3339] | RFC 3339 - Date and Time on the Internet: Timestamps, G. Klyne et al., July 2002 |
| [RFC 8610] | RFC 8610 - Concise Data Definition Language (CDDL): A Notational Convention to Express Concise Binary Object Representation, H. Birkholz et al., June 2019 |
| [RFC 8943] | RFC 8943 - Concise Binary Object Representation (CBOR) Tags for Date, M. Jones et al., November 2020 |
| [RFC 8949] | RFC 8949 - Concise Binary Object Representation (CBOR), C. Bormann et al., December 2020 |
| [SD-JWT VC] | SD-JWT-based Verifiable Credentials. Available: <https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/> |
| [Topic 7] | ARF Annex 2 - Topic 7 - Attestation revocation and revocation checking |
| [Topic 10] | ARF Annex 2 - Topic 10 - Issuing a PID or attestation to a Wallet Unit |
| [Topic 12] | ARF Annex 2 - Topic 12 - Attestation Rulebooks |
| [Topic 20] | ARF Annex 2 - Strong User authentication for electronic payments |
| [W3C VCDM v2.0] | Verifiable Credentials Data Model v2.0, W3C Recommendation |
