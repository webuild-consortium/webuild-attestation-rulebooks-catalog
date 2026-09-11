# Attestation Rulebook for attestations of type EBWOID (European Business Wallet – Owner Identification Data)

Category: EBWOID

* Author(s): 
    <!-- Usage help: (Name LastName, Affiliation) -->
  * Jonas Toennis, [Brønnøysund Registry Center](https://www.brreg.no)

| Version | Date       | Description                                                                                                                                                                                           |
|---------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0.9.1   | 13.02.2026 | EBWOID created based on the [EBW proposal (Articles 8–9)](https://digital-strategy.ec.europa.eu/en/library/proposal-regulation-establishment-european-business-wallets) plus feedback from semantics. |
| 1.0.0   | 22.05.2026 | Updated following review feedback.                                                                                                                                                                     |
| 1.1.0   | 2026-09-11 | Restructured onto the generic WE BUILD attestation rulebook template (11 chapters). No normative content removed. |

**Written against:** ARF version 3.0.0, WE BUILD template version 1.0 (generic)

**Feedback:** [GitHub issues](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/issues), or contact Work Package 4 in WE BUILD.

## Table of contents

- [1 Introduction](#1-introduction)
   * [1.1 Document scope and purpose](#11-document-scope-and-purpose)
   * [1.2 Document structure](#12-document-structure)
   * [1.3 Key words](#13-key-words)
   * [1.4 Terminology](#14-terminology)
- [2 Certification](#2-certification)
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
   * [6.1 Issuance](#61-issuance)
   * [6.2 Presentation](#62-presentation)
- [7 Issuance](#7-issuance)
   * [7.1 Binding](#71-binding)
   * [7.2 Lifecycle management](#72-lifecycle-management)
   * [7.3 Issuance Policy](#73-issuance-policy)
   * [7.4 Embedded disclosure policy](#74-embedded-disclosure-policy)
- [8 Revocation](#8-revocation)
- [9 Presentation](#9-presentation)
   * [9.1 Relying Party policy](#91-relying-party-policy)
   * [9.2 Presentation modes](#92-presentation-modes)
   * [9.3 Transactional data](#93-transactional-data)
- [10 Trust Framework](#10-trust-framework)
- [11 References](#11-references)


## 1 Introduction

### 1.1 Document scope and purpose

The European Business Wallet – Owner Identification Data (EBWOID) is based on the European Business Wallet Regulation draft COM(2025) 838. While this document is still in draft status, WE BUILD decided at the beginning of 2026 that the draft would be accepted as the basis for the Business Wallet work. This means that the suggested amendments to Regulation 2024/1183 will be applied within WE BUILD. 

The European Business Wallet – Owner Identification Data (EBWOID) attestation defines a legally defined, common set of data that uniquely identifies an EBW owner (economic operator or public sector body) within the European Business Wallets (EBW) ecosystem. Its purpose is to provide a harmonised, interoperable attestation that enables Relying Parties and business wallets to establish trust in an EBW owner entity. EBWOID focuses on the core identifiers needed across national and cross‑border use cases.

Primary objectives:
- Provide a cross‑border unique identifier for the EBW owner (In **WE BUILD** EUID where available, otherwise a similarly constructed, unique per issuer identifier. <CountryCode ISO 3166-1 alpha-2><Issuer-reference>.<unique identifier> e.g. SEBOLREG.123456789) and the official name of the EBW owner.
- Serving as the activation and ownership attestation enabler for the EBW.
- Support verification of issuer authenticity and attestation integrity based on the EBW proposal (Articles 8–9) and ARF trust requirements.
- Enable consistent consumption in EBW and EUDI flows as Electronic Attestations of Attributes (QEAA/Pub-EAA) aligned with applicable implementing acts.

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

This document uses the terminology specified in [Annex 1](https://eudi.dev/3.0.0/annexes/annex-1/annex-1-definitions/) of the ARF.

The terminology is extended as follows:

| Term              | Definition in WE BUILD Context                                                                                                                                                                                                |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EBW               | European Business Wallet                                                                                                                                                                                                      |
| EBW owner         | An economic operator or public sector body that owns an EBW, including Union entities; corresponds to the bearer of EBWOID.                                                                                                   |
| EBWOID            | European Business Wallet owner identification data. A set of data that enables the establishment of the identity of a European Business Wallet owner                                                                          |
| Economic operator | Any natural or legal person, or a group of such persons, including temporary associations of undertakings, acting in a commercial or professional capacity for purposes related to their trade, business, craft or profession |

For more terminology, please refer to Article 3 of the legislation draft [COM 2025/838](https://digital-strategy.ec.europa.eu/en/library/proposal-regulation-establishment-european-business-wallets)

## 2 Certification

### 2.1 Compliance statement

> This Rulebook complies with the applicable requirements of Topic 12, Attestation
> Rulebooks, in Annex 2 of the Architecture and Reference Framework, version 3.0.0.
> It uses the terminology of Annex 1 of the ARF.

This EBWOID rulebook is compliant with the draft for regulation COM(2025) 838, and in line with the ARF version 2.8.0. 
While the legislative process for the EBW Regulation continues, major updates to this rulebook within the WE BUILD context are not expected unless required by exceptional circumstances or requested by the WE BUILD Management Board. 

### 2.2 Regulatory basis

> **TO AGREE.** Section 2.2 of the generic template treats EBWOID as a legal category
> in its own right, with a regulatory basis that is an open consortium decision, and
> directs authors not to assert qualified status unless the issuer is a QTSP, nor to
> cite Annex V or Annex VII by default. This Rulebook, as written by its authors,
> instead treats EBWOID as a QEAA or a PuB-EAA and cites both Annex V and Annex VII.
> The two positions are recorded together here rather than one being chosen during
> restructuring. The quality assurance group needs to settle which applies before this
> chapter can be finalised. See also the note in section 4.1.

The requirements below are as recorded by the authors of this Rulebook.

**Requirements for the EBWOID QEAA**
* An attribute as meant in Annex V point a) of the [European Digital Identity Regulation] SHALL be included (see ARB_11 in [Topic 12]). See also [Section 2.1](#21-introduction).
* One or more attributes or metadata representing the set of data meant in Annex V point b) of the [European Digital Identity Regulation] SHALL be included (see ARB_13 in [Topic 12])
* One or more attributes representing the set of data meant in Annex V point c) of the [European Digital Identity Regulation] SHALL be included (see ARB_16 in [Topic 12]).
* One or more attributes or metadata representing the set of data meant in Annex V point e) of the [European Digital Identity Regulation] SHALL be included (see ARB_18 in [Topic 12]).
* One or more attributes or metadata representing the location meant in Annex V point h) of the [European Digital Identity Regulation] SHALL be included. This location SHALL 
indicate at least the URL at which a machine-readable version of the trust anchor to be used for verifying the QEAA can be found or looked up (see ARB_20 in [Topic 12])

**Requirements for PuB-EAA**
* Αn attribute as meant in Annex VII point a) of the [European Digital Identity Regulation] SHALL be included (see ARB_11 in [Topic 12]). See also [Section 2.1](#21-introduction).
* Οne or more attributes or metadata representing the set of data meant in Annex VII point b) of the [European Digital Identity Regulation] SHALL be included (see ARB_14 in [Topic 12]).
* Οne or more attributes representing the set of data meant in Annex VII point c) of the [European Digital Identity Regulation] SHALL be included (see ARB_16 in [Topic 12]).
* Οne or more attributes or metadata representing the set of data meant in Annex VII point e) of the [European Digital Identity Regulation] SHALL be included (see ARB_18 in [Topic 12]).
* one or more attributes or metadata representing the location meant in Annex VII point h) of the [European Digital Identity Regulation] SHALL be included. This location SHALL 
indicate at least the URL at which a machine-readable version of the qualified certificate that signed the PuB-EAA can be found or looked up. (see ARB_20 in [Topic 12]) 

### 2.3 Traceability

Every applicable requirement mapped to the section that satisfies it. Requirements
marked not applicable carry a stated reason. Rows marked TO AGREE depend on the legal
category question recorded in section 2.2.

| Requirement | Legacy ID | Applies | Satisfied in section | Note |
| --- | --- | --- | --- | --- |
| EW-DM-12-001 | ARB_01a | yes | 5 | W3C VCDM is named as a profiled format; no encoding is defined in this version |
| EW-DM-12-002 | ARB_01b | yes | 5 | SD-JWT VC |
| EW-DM-12-003 | ARB_02 | no | | Proximity presentation is not in scope; mdoc is out of scope per section 5.2 |
| EW-DM-12-005 | ARB_04 | no | | No W3C VCDM encoding is defined in this version |
| EW-DM-12-006 | ARB_05 | yes | 5 | `vct` `uri:eu.ebw.oid.1` |
| EW-DM-12-007 | ARB_06 | yes | 3 | Attributes defined independently of encoding |
| EW-DM-12-008 | ARB_06a | no | | No mdoc encoding is defined in this version |
| EW-DM-12-009 | ARB_06b | yes | 5 | SD-JWT VC claim naming |
| EW-DM-12-010 | ARB_07 | yes | 3 | Attributes derived from the EBW proposal, Articles 8 and 9 |
| EW-DM-12-012 | ARB_09 | yes | 3, 4 | Presence stated per attribute and per metadata item |
| EW-DM-12-013 | ARB_10 | no | | No domestic namespace is defined |
| EW-DM-12-014 | ARB_11 | TO AGREE | 2.2 | Annex V or VII point a, depending on the legal category question |
| EW-DM-12-015 | ARB_12 | TO AGREE | | Applies only if EBWOID is a non-qualified EAA |
| EW-DM-12-016 / EW-DM-12-017 / EW-DM-12-018 | ARB_13 / ARB_14 / ARB_15 | TO AGREE | 2.2 | Point b, by category |
| EW-DM-12-019 / EW-DM-12-020 | ARB_16 / ARB_17 | TO AGREE | 2.2 | Point c, by category |
| EW-DM-12-021 / EW-DM-12-022 | ARB_18 / ARB_19 | TO AGREE | 2.2 | Point e, by category |
| EW-DM-12-023 / EW-DM-12-024 | ARB_20 / ARB_21 | yes | 4.2, 10 | `trust_anchor` metadata and the trust framework |
| EW-DM-12-029 | ARB_25 | yes | 4.1 | Legal category attribute; see the note in section 4.1 |
| EW-DM-12-030 | ARB_26 | TO AGREE | | Applies only if EBWOID is a non-qualified EAA |
| EW-DM-12-031 | ARB_27 | yes | 9.1 | A Relying Party SHOULD also verify a PID for the representative |
| EW-DM-12-032 | ARB_28 | no | | `cryptographically_bound_to` is not used by this attestation |
| EW-DM-12-034 | ARB_30 | yes | 5 | Selective disclosure is not permitted; stated in section 5.1 |
| EW-DM-12-035 | ARB_31 | no | | No Claim Selective Disclosure Metadata document is used |
| EW-DM-12-038 | ARB_34 | TO AGREE | 7.1 | Device binding; the template records all EBWOID binding rows as TO AGREE |

## 3 Attestation attributes

Attributes are defined here in an encoding-independent manner (EW-DM-12-007). The
encoding of each attribute per format is given in chapter 5.

### 3.1 Introduction

The EBW Owner Identification Data (EBWOID) is a structured digital attribute designed to uniquely and verifiably identify economic operators and public sector bodies—within the EBW ecosystem in both national and cross‑border digital interactions. It encapsulates a claim (e.g. “This is the official name and unique identifier of the EBW owner”), metadata about the source of that claim (such as the registry or official record), and cryptographic assurances that validate the claim’s authenticity and issuer. EBWOIDs SHOULD be issued in SD‑JWT and/or W3C VCDM formats as Pub-EAAs/QEAAs.
This chapter defines the legally required minimum attributes, as well as optional attributes.


**In the WE BUILD context**, EBWOIDs can be issued for any EBW owner, provided the attributes are derived from authentic sources notified to the Commission (EBW Article 8(2)). 

All data identifiers and definitions in this chapter are independent of any encoding used. Consequently, the data identifiers in these tables are not necessarily the same as the claim names used for EBWOID complying with [SD-JWT VC]. [Chapter 3.2](#32-sd-jwt-vc-based-encoding) specifies the claim names to be
  used for such EBWOID.

> **Note on schema artefacts.** Section 3.1 of the generic template requires a
> machine-readable schema artefact for every format marked supported in chapter 5,
> versioned and immutably addressable. No such artefact exists yet for this
> attestation under `data-schemas/`. Adding one is follow-up work, tracked as a known
> gap rather than resolved here.

### 3.2 Mandatory attributes

| **Data Identifier** | **Definition**                                                                                                                                                                                                                                                                                                                 |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| legal_name          | The official name of the EBW owner (economic operator or public sector body), from the relevant register or official record.                                                                                                                                                                                                   |
| id                  | The relevant unique identifier attributed in accordance with Article 9 of EBW (**WE BUILD specific** EUID where available, otherwise a similarly constructed, unique per issuer identifier. <CountryCode ISO 3166-1 alpha-2><Issuer-reference>.<unique identifier> e.g. `SE` +  `BOLREG` + `123456789` -> `SEBOLREG.123456789` |

### 3.3 Optional attributes

This Rulebook defines no optional attributes. The optional items it defines are
metadata rather than attributes, and are recorded in section 4.2.

### 3.4 Conditional attributes

This Rulebook defines no conditional attributes.

## 4 Metadata

Metadata describes the attestation rather than its subject.

### 4.1 Mandatory metadata

| **Data Identifier**        | **Definition**                                                                                                                                                   |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| issuing_authority          | Name of the administrative authority or qualified trust service provider that issued the EBWOID, or the ISO 3166‑1 alpha‑2 of the Member State where applicable. |
| issuing_country            | Alpha‑2 country code, as specified in ISO 3166‑1, of the country or territory of the provider of the EBWOID.                                                     |
| attestation_legal_category | The type of attestation category. (Pub-EAA/QEAA)                                                                                                                 |

> **Legal category, TO AGREE.** The table above carries
> `attestation_legal_category` with the values Pub-EAA or QEAA. Section 4.1 of the
> generic template states that this attribute is superseded by the `category`
> attribute of [ETSI TS 119 472-1] and SHALL NOT be used, and records the `category`
> value for EBWOID as an open consortium decision. Two questions are therefore open
> and they are linked: whether EBWOID is a legal category in its own right or a QEAA
> or PuB-EAA, recorded in section 2.2, and which attribute and value express that.
> The attribute has been left as the authors wrote it. Note also that EW-DM-12-029
> (legacy ARB_25) of ARF v3.0.0 is a SHALL that still requires
> `attestation_legal_category`, so the template and the ARF currently disagree.

### 4.2 Optional metadata

| **Data Identifier** | **Definition**                                                                                                                                                                                                                                                                                            |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| location_status     | The location of validity status information on the EBWOID used for revocation/suspension checks.                                                                                                                                                                                                          |
| expiry_date         | Administrative Date when the EBWOID will expire, following ISO 8601 **Clarification** This is in case the administrative validity is different from the technical expiry date of the credential.                                                                                                          |
| trust_anchor        | This meta-data attribute indicates at least the URL at which a machine‑readable version of the trust anchor to be used for verifying the EBWOID can be found or looked up. This corresponds to Annex V/VII point h) of the [European Digital Identity Regulation] and EBW Article 8 issuance as EAA/QEAA. |

### 4.3 Conditional metadata

This Rulebook defines no conditional metadata.

### 4.4 Code lists

| Code list | Source | Extensible |
| --- | --- | --- |
| `attestation_legal_category` | `QEAA`, `PUB-EAA` as recorded in section 4.1 | no, and subject to the open question in section 4.1 |
| `issuing_country` | ISO 3166-1 alpha-2 | no, follows the source standard |
| `status.type`, `status.status_purpose` | `status-list` and `revocation` respectively, as recorded in section 5.1 | no |

### 4.5 Integrity rules

| Rule | Enforcement point | Behaviour on failure |
| --- | --- | --- |
| A `status` claim SHALL be present when the technical validity period exceeds 24 hours | EBWOID Provider, at issuance | The EBWOID is not issued |
| `exp` SHALL be present and SHALL NOT be in the past | Relying Party, at verification | The EBWOID is refused |
| The EBWOID SHALL be presented atomically; no attribute is selectively disclosable | Wallet Unit, at presentation | The presentation is refused |
| `id` SHALL be the unique identifier attributed under Article 9 of the EBW proposal | EBWOID Provider, at issuance | The EBWOID is not issued |

## 5 Formats

| Format | Supported | Identifier | Specification | Notes |
| --- | --- | --- | --- | --- |
| ISO/IEC 18013-5 mdoc | no | | [ISO/IEC 18013-5] | Out of scope, see section 5.2 |
| SD-JWT VC | yes | `vct` `uri:eu.ebw.oid.1` | [SD-JWT VC] | |
| W3C VCDM | named, not specified | | [W3C VCDM v2.0] | See the note below |

> **Inconsistency carried forward.** Sections 1.1 and 9.1 of this Rulebook state that
> EBWOID is profiled for both SD-JWT VC and W3C VCDM, but no W3C VCDM encoding is
> defined anywhere in the document. This was true of the previous version and has not
> been resolved during restructuring. Either the encoding needs writing or the claim
> needs withdrawing.

### 5.1 SD-JWT VC-based encoding

Verifiable Credential Type (vct): `uri:eu.ebw.oid.1`

Claim names and disclosure policy (aligned with Chapter 2 attributes):
 
| Data Identifier             | Attribute Identifier        | Encoding format | Reference/Notes                                                                                                                                                                                                                                                                         |
|-----------------------------|-----------------------------|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                          | id                          | string          | Cross‑border unique identifier per EBW Article 9. In **WE BUILD** EUID where available, otherwise a similarly constructed, unique per issuer identifier. <CountryCode ISO 3166-1 alpha-2><Issuer-reference>.<unique identifier> e.g. `SE` +  `BOLREG` + `123456789` -> `SEBOLREG.123456789`  |
| name                        | name                        | string          | Official name from relevant register or official record.                                                                                                                                                                                                                                |
| attestation_legal_category  | attestation_legal_category  | string          | The type of attestation category. Can be one of QEAA or PUB-EAA                                                                                                                                                                                                                         | 
| expiry_date                 | date_of_expiry              | string          | Administrative expiry date given on ISO 8601-1 date format. YYYY‑MM‑DD                                                                                                                                                                                                                  |
| issuing_authority           | issuing_authority           | string          | Name of the administrative authority, Commission (for Union entities), or QTSP issuing the EAA/QEAA; or ISO 3166‑1 alpha‑2 where applicable.                                                                                                                                            |
| issuing_country             | issuing_country             | string          | ISO 3166‑1 alpha‑2 code of the provider’s country/territory.                                                                                                                                                                                                                            |
| location_status             | status                      | JSON Object     | See [Section 3.2.1](#321-attribute-status).                                                                                                                                                                                                                                             |
| trust_anchor                | trust_anchor                | string (URI)    | URL of machine‑readable trust anchor as per Annex V/VII point h).                                                                                                                                                                                                                       |

Selective Disclosure: Attributes of the EBWOID SHALL NOT be selectively disclosable.


#### 3.2.1 Attribute status
For SD‑JWT VC‑compliant EBWOID, the EBWOID MUST include a status claim if the technical validity period is greater than 24 hours. This claim enables Relying Parties to determine if a credential has been revoked via a status list mechanism, as specified in [SD‑JWT VC](https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/).

The status claim SHALL be a JSON object with the following members:

* 'type' (string): SHALL be "status-list".
* 'status_list_credential' (string, URI): The URI of the Status List Credential document that contains the status bitstring.
* 'status_list_index' (integer, >= 0): The zero-based index into the status list bitstring that corresponds to this credential.
* 'status_purpose' (string): SHALL be "revocation" for this PID.

Example:
```json
{
  "status": {
    "type": "status-list",
    "status_list_credential": "https://issuer.example.com/status/1",
    "status_list_index": 42,
    "status_purpose": "revocation"
  }
}
```

### 5.2 ISO/IEC 18013-5-compliant encoding

The ISO/IEC 18013-5 encoding is out of scope for the WE BUILD rulebook. This decision is based on the results of the specification phase of the WE BUILD consortium, during which no requirements or use cases for proximity sharing of the EBWOID credential were identified.

### 5.3 Example

Illustrative examples:
- Example claim set (human‑readable):
```json
{
  "vct": "uri:eu.ebw.oid.1",
  "id": "NOFOR.123456789",
  "name": "Example AS",
  "attestation_legal_category": "PUB-EAA",
  "issuing_authority": "Brønnøysundregistrene",
  "issuing_country": "NO",
  "date_of_expiry": "2026-12-31",
  "trust_anchor": "https://tl.eidas.europa.eu/tl-browser/#/",
  "status": {
    "type": "status-list",
    "status_list_credential": "https://issuer.example.no/status/1",
    "status_list_index": 42,
    "status_purpose": "revocation"
  },
  "cnf": {
    "jwk": {
        "kty": "EC",
        "crv": "P-256",
        "x": "52aDI_ur05n1f_p3jiYGUU82oKZr3m4LsAErM536crQ",
        "y": "ckhZ-KQ5aXNL91R8Eufg1aOf8Z5pZJnIvuCzNGfdnzo"
    }
  }
}
```
Note: The `cnf` claim is used for expressing key binding in SD-JWT VCs.
The example above shows a public key in JWK format.

Note: Additional technical claims are not shown here, including
references to the issuer and more.

## 6 Protocols

### 6.1 Issuance

EBWOID is issued using OpenID for Verifiable Credential Issuance [OpenID4VCI].

### 6.2 Presentation

EBWOID is presented using OpenID for Verifiable Presentations [OpenID4VP]. Only remote
presentation is in scope, consistent with chapter 5, which records mdoc as out of
scope.

## 7 Issuance

### 7.1 Binding

> **TO AGREE.** Section 7.1 of the generic template records all four binding rows for
> EBWOID as open consortium decisions. The values below are the reading that follows
> from the rest of this Rulebook, offered so the table is not blank, and they are not
> yet agreed.

| Field | Value | Source |
| --- | --- | --- |
| Device-bound | TO AGREE | EW-DM-12-038 |
| Cryptographically bound to | none | EW-DM-12-032 |
| Relying Party must also verify a PID | SHOULD, for the representative, see section 9.1 | EW-DM-12-031 |
| Binding subject | legal person, the EBW owner | EBW proposal, Articles 8 and 9 |

The `cnf` claim shown in the example in section 5.3 expresses key binding.

### 7.2 Lifecycle management

- EBWOID is issued by an administrative authority, by the Commission for Union
  entities, or by a QTSP, as recorded in section 4.1.
- EBWOID is expected to be long-lived but revocable, as recorded in chapter 8.
- `expiry_date`, where present, expresses an administrative validity period distinct
  from the technical validity expressed by `exp`. See section 4.2.

### 7.3 Issuance Policy

EBWOID Providers SHALL support revocation as described in chapter 8.

### 7.4 Embedded disclosure policy

This attestation defines no embedded disclosure policy.

## 8 Revocation

TODO: WE BUILD WP4 - EBW owner identification data revocation task 5

EBWOID is expected to be long‑lived but revocable. This Rulebook adopts the following policy:
- EBWOID SHALL include `exp`. Validity longer than 24 hours is permitted; therefore, revocation MUST be supported.
- When the Commission specifies the Attestation Status List (ASL) or Attestation Revocation List (ARL) mechanism, EBWOID Providers SHALL implement that mechanism.
- Until such mechanisms are specified, EBWOID Providers SHALL publish revocation status via a machine‑readable endpoint referenced from the issuer’s policy, and Relying Parties SHALL implement status checking per that policy. Issuers SHOULD implement the [oauth status list](https://datatracker.ietf.org/doc/draft-ietf-oauth-status-list/) until otherwise specified. 

Relying Party checks:
- Validate `exp` not in the past.
- Query the designated ASL/ARL (or interim status endpoints) to determine the current status.
- Treat any indeterminate status as non‑valid per risk policy.

## 9 Presentation

### 9.1 Relying Party policy

> A Relying Party receiving an attestation of this type SHALL:
>
> 1. verify the signature over the attestation using a trust anchor obtained as
>    described in chapter 10;
> 2. verify that the attestation is within its validity period;
> 3. check revocation status as described in chapter 8, unless the attestation is
>    short-lived; or remaining lifetime of the attestation is below revocation time
>    threshold;
> 4. verify device binding where section 7.1 records the attestation as device-bound;
> 5. request only those attributes that are necessary for the stated purpose of the
>    transaction, and, where the trust model for this attestation requires Relying
>    Party registration, only those attributes it is registered and authorised to
>    request.

Obligations specific to this attestation type, carried over from the use-case context
of the previous version of this Rulebook:

The EBWOID attestation serves diverse types of EBW owners across European digital services:

- **Public sector body** — a Union entity, a national, state, regional or local authority, a body governed by public law or an association formed by one or several such entities or bodies, or a private entity mandated by at least one such entities, authorities, bodies or associations to provide public services, when acting under such a mandate.
- **Economic operator** — any natural or legal person, or a group of such persons, including temporary associations of undertakings, acting in a commercial or professional capacity for purposes related to their trade, business, craft or profession

EBWOID is profiled for **SD-JWT VC** and **W3C VCDM** because these formats:
- Are mandated or recommended by the ARF and applicable implementing acts for electronic attestations of attributes.
- Support selective disclosure (SD-JWT VC) and linked-data integrity (W3C VCDM), enabling both privacy and semantical presentations.

Primary use cases:
- Proving the legal identity of an organisation (holder) to a Relying Party in national and cross‑border digital online services.
- Activating and enabling the ownership binding of the EBW.
- Establishing a trust context for additional legal‑person attestations that reference the EBWOID `id`.

Relying Party obligations:
- Verify the SD‑JWT VC signature and ensure the issuer is an authorised public body by validating the qualified certificate chain against the appropriate QTSP Trusted List (see Chapter 5).
- Check freshness: validate `exp` and consider `iat`.
- Apply revocation/status checks as defined in Chapter 6.
- Where the transaction requires binding to a natural person representative, the RP SHOULD request and verify a PID for the representative in addition to the EBWOID.

Presentation requirements:
- Selective disclosure is NOT permitted for the core EBWOID attributes; the holder presents EBWOID atomically.

Transactional data:
- The RP MAY keep minimal logs necessary to demonstrate lawful processing and verification events; no additional transaction‑specific attributes are introduced by EBWOID.

### 9.2 Presentation modes

Remote presentation is in scope. Proximity presentation is not in scope, consistent
with chapter 5, which records the mdoc encoding as out of scope.

### 9.3 Transactional data

No additional transaction-specific attributes are introduced by EBWOID. Relying Party
logging expectations are recorded in section 9.1.

## 10 Trust Framework

**PID, QEAA, PuB-EAA and attestations resolved via Trusted Lists**

> The trust anchor is obtained from a Trusted List, as described in section 6.6.3.6
> of the ARF main document. The Provider may sign the attestation with an
> intermediate signing certificate, in which case the trust anchor is used to verify
> that certificate rather than the attestation directly.
>
> For a PuB-EAA, a Relying Party Instance first verifies the Provider signature using
> the Provider certificate issued by a QTSP, then verifies that certificate using the
> corresponding trust anchor from the QTSP Trusted List. One or more extra
> certificates are therefore involved compared with a PID or QEAA.

Which branch of the template applies here depends on the legal category question
recorded in section 2.2. The Trusted List branch is reproduced above because it
matches the trust model the authors describe in the deployment profile below.

**Trust anchor location**

> The attribute or metadata carrying the trust anchor location contains at least the
> URL at which a machine-readable version can be found or looked up.

Coherence check: the attribute named here is `trust_anchor`, declared in section 4.2.
Note that step 4 of the verification sequence below refers to `trust_list_location`,
which is not defined anywhere in this Rulebook. That inconsistency is carried forward
from the previous version and needs an author decision.

**Deployment profile**

For EBWOID as a PUB-EAA/QEAA, Relying Parties SHALL verify the EBWOID using the issuer credential:
- Public‑body issuer certificate issued by a Qualified Trust Service Provider (QTSP) when provided by or on behalf of a public sector body responsible for an authentic source;
- Qualified electronic attestation of attributes when provided by a QTSP; or
- Commission issuance for Union entities (having the same legal effect per EBW Article 8(4)).
Relying Parties SHALL verify the relevant certificate chain up to the appropriate trust anchor (eIDAS Trust List or Commission trust anchor as applicable).

Verification steps:
1) Verify the SD‑JWT VC signature over the EBWOID using the issuer certificate.
2) Build and validate the certificate chain from the issuer certificate to a QTSP trust anchor listed in the appropriate Trusted List.
3) Validate certificate status (validity, revocation) per eIDAS trust list rules.
4) Use the `trust_list_location` metadata to discover the appropriate Trusted List or machine‑readable pointer.

Issuers MAY use intermediate signing certificates. RPs SHALL handle such chains. The trust model is equivalent to Annex VII for PuB‑EAA.

For information regarding the use of the trust list in WE BUILD, please consult the Architecture Blueprint.

## 11 References

| **Item Reference**                     | **Standard name/details**                                                                                                                                                                                                                                                                           |
|----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [European Digital Identity Regulation] | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework                            |
| [ISO/IEC 18013-5]                      | ISO/IEC 18013-5, Personal identification --- ISO-compliant driving licence - Part 5: Mobile driving licence (mDL) application, First edition, 2021-09                                                                                                                                               |
| [OIDC]                                 | Sakimura, N. et al., "OpenID Connect Core 1.0", OpenID Foundation. Available: <https://openid.net/specs/openid-connect-core-1_0.html>                                                                                                                                                               | |
| [SD-JWT VC]                            | SD-JWT-based Verifiable Credentials (SD-JWT VC). Available: <https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/>, version draft-ietf-oauth-sd-jwt-vc-09                                                                                                                                   |
| [Topic 7]                              | ARF Annex 2 - Topic 7 - Attestation revocation and revocation checking Available: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/3.0.0/annexes/annex-2/annex-2.02-high-level-requirements-by-topic/#a237-topic-7-attestation-revocation-and-revocation-checking>  |
| [Topic 10]                             | ARF Annex 2 - Topic 10 - Issuing a PID or attestation to a Wallet Unit: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/3.0.0/annexes/annex-2/annex-2.02-high-level-requirements-by-topic/#a2310-topic-10-issuing-a-pid-or-attestation-to-a-wallet-unit>           |
| [Topic 12]                             | ARF Annex 2 - Topic 12 - Attestation Rulebooks, Available: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/3.0.0/annexes/annex-2/annex-2.02-high-level-requirements-by-topic/#a2312-topic-12-attestation-rulebooks>                                                |
| [Topic 20]                             | ARF Annex 2 - Strong User authentication for electronic payments, Available: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/3.0.0/annexes/annex-2/annex-2.02-high-level-requirements-by-topic/#a2320-topic-20-strong-user-authentication-for-electronic-payments> |
| [W3C VCDM v2.0]                        | Sporny, M. *et al,* Verifiable Credentials Data Model v2.0, W3C Recommendation.                                                                                                                                                                                                                     |
