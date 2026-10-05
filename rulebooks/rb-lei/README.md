# Attestation Rulebook for attestations of type Legal Entity Identifier

Category: non-qualified EAA

* Authors:
  * Martin Westerkamp, [Spherity](https://www.spherity.com)
  * Monika Nowicki, [Bundesanzeiger Verlag](https://www.bundesanzeiger-verlag.de)


**Feedback:**
Main feedback channel: [GitHub issues](https://github.com/webuild-consortium/eudi-wallet-rulebooks-and-schemas/issues)
Alternative: Contact the relevant WE BUILD business use case contact points.

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

This document is the Legal Entity Identifier Data Rulebook (referred to as LEI). It contains the specific requirements, issuance process, formatting and content of the LEI attestation.
This document is created and used by the WEBUILD consortium to provide a common understanding, data schema, format and usage guidelines for the WEBUILD eco system.

The Legal Entity Identifier (LEI) is a unique, 20-character alphanumeric code used to strictly identify distinct legal entities that participate in global financial transactions. Established by the G20 in the wake of the 2008 financial crisis, its primary purpose is to improve transparency and risk management across the international financial system. Yet, it can also be utilized in other contexts to enable global authentication of legal entities.

Each LEI links to a public database containing company information. By providing a standardized, machine-readable identity, the system reduces the complexity of verifying counterparts in cross-border markets. Essentially, it acts as a global "social security number" for businesses, ensuring that every participant in a trade is clearly and universally recognized.

This attestation provides a minimal, verifiable proof that a given LEI exists, is currently valid, and belongs to the attestation owner.

This document is based on the data model provided by GLEIF: <https://www.gleif.org/en/lei-data/access-and-use-lei-data/level-1-data-lei-cdf-3-1-format>.

This attestation represents a Legal Entity Identifier (LEI) record. It embodies only:
- The LEI code uniquely identifying the legal entity (ISO 17442)
- The current status of the LEI (LEI Status)
- The next renewal date of the LEI (LEI Renewal Date)

**Issuance by an LOU.** The LEI attestation SHALL be issued by an accredited Local Operating Unit (LOU). This need not be the LOU that originally issued the LEI: any accredited LOU may issue the attestation on the basis of authoritative LEI data. Within the Global LEI System, an LOU (not GLEIF) is the authentic source: each LOU validates entity data against local registers and is accountable for its correctness, up to loss of accreditation. GLEIF acts only as an aggregator: it publishes a periodically refreshed copy of the LOUs' records in the Global LEI Index, performs a data-quality check but still publishes the data it receives even where it believes them to be incorrect, has no regulatory authority to guarantee accuracy, and bears no legal responsibility for errors. Because the Global LEI Index is synchronised only at intervals and depends on LOU systems being reachable at collection time, it may disseminate stale status or renewal information.

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

This document uses terminology specified in [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/eli/reg/2024/1183/oj/eng) and [Annex 1 of the ARF](https://eudi.dev/1.4.0/annexes/annex-1/annex-1-definitions/).

In addition to the attributes definition necessary to understand the data schema, it's important to understand:

| Term | Definition in WE BUILD Context |
| --- | --- |
| Legal entity | an organization or structure that is recognized by law as having legal rights and responsibilities distinct from those of its members or owners. A legal entity can enter into contracts, own property, incur debts, and be held liable for legal actions in its own name. |
| LEI | Legal Entity Identifier: a unique, 20-character alphanumeric code conforming to ISO 17442 that uniquely identifies a legal entity participating in financial and other transactions globally. |
| LOU | Local Operating Unit: an organization accredited by GLEIF to issue and administer LEIs (also referred to as an LEI Issuer). |
| GLEIF | Global Legal Entity Identifier Foundation: the not-for-profit organization that oversees the Global LEI System and the integrity of LEI data. |

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

*This section is used for defining all attributes that an
attestation of the defined type may contain. In this section
the attributes SHALL be defined in an encoding-independent manner (see ARB_06 in [Topic 12]).
Each attribute can be mandatory, optional, or conditional,
and it SHALL be specified in the corresponding section (see ARB_09 in [Topic 12]).*

*When attributes are defined, referring to attributes that
already exist in a catalogue of attestation attributes
SHOULD be considered (see ARB_07 in [Topic 12]).*

*[Topic 12] of Annex 2 of the ARF defines the following High-Level Requirements with
respect to the Attestation Rulebooks*

**Requirements for QEAA**
* An attribute as meant in Annex V point a) of the [European Digital Identity Regulation]
SHALL be included (see ARB_11 in [Topic 12]). See also section 2.1.
* One or more attributes or metadata representing the set of data meant in Annex
V point b) of the [European Digital Identity Regulation] SHALL be included (see ARB_13 in [Topic 12])
* One or more attributes representing the set of data meant in Annex V point c)
of the [European Digital Identity Regulation] SHALL be included (see ARB_16 in [Topic 12]).
* One or more attributes or metadata representing the set of data meant in Annex V point e)
of the [European Digital Identity Regulation] SHALL be included (see ARB_18 in [Topic 12]).
* One or more attributes or metadata representing the location meant in Annex V point h)
of the [European Digital Identity Regulation] SHALL be included. This location SHALL
indicate at least the URL at which a machine-readable version of the trust anchor to be
used for verifying the QEAA can be found or looked up (see ARB_20 in [Topic 12])

**Requirements for PuB-EAA**
* Αn attribute as meant in Annex VII point a) of the [European Digital Identity Regulation]
SHALL be included (see ARB_11 in [Topic 12]). See also section 2.1.
* Οne or more attributes or metadata representing the set of data meant in Annex
 VII point b) of the [European Digital Identity Regulation] SHALL be included (see ARB_14 in [Topic 12]).
* Οne or more attributes representing the set of data meant in Annex VII point c)
of the [European Digital Identity Regulation] SHALL be included (see ARB_16 in [Topic 12]).
* Οne or more attributes or metadata representing the set of data meant in Annex VII point e)
of the [European Digital Identity Regulation] SHALL be included (see ARB_18 in [Topic 12]).
* one or more attributes or metadata representing the location meant in Annex VII point h)
of the [European Digital Identity Regulation] SHALL be included. This location SHALL
indicate at least the URL at which a machine-readable version of the qualified
certificate that signed the PuB-EAA can be found or looked up. (see ARB_20 in [Topic 12])

**Requirements for non-qualified EAA**
* An attribute indicating that the attestation is an EAA should be included (see ARB_12 in [Topic 12]).
See also section 2.1.
* Οne or more attributes or metadata representing the set of data meant in Annex
V point b) of the [European Digital Identity Regulation] SHALL be included (see ARB_15 in [Topic 12]).
* Οne or more attributes representing the set of data meant in Annex V point c) of the
[European Digital Identity Regulation] SHOULD be included (see ARB_17 in [Topic 12])
* Οne or more attributes representing the set of data meant in Annex V point e) of
the [European Digital Identity Regulation] SHOULD be defined (see ARB_19 in [Topic 12]).
 * Οne or more attributes or metadata representing the location at which a machine-readable
version of the trust anchor to be used for verifying the EAA can be found or
looked up SHOULD be defined. What this location indicates precisely is dependent
on the nature of the mechanism used for distributing trust anchors, detailed in section
5 (see ARB_21 in [Topic 12])

The attestation attributes are defined in the tables of Chapter 2 of this document. These tables contain the following information:
- The first column specifies the identifiers of the attestation attributes. The attribute identifiers in this column SHALL be used in requests and responses. There SHALL be at most one attribute with the same attribute identifier in each attestation attribute.
- The second column describes the meaning of the attribute.
- The third column specifies whether the presence of the attribute in an attestation is mandatory (M), or optional (O).
    - NOTE: If the table indicates an attribute as mandatory, this solely means that the Issuer SHALL ensure that this element is present in the attestation. It does not imply that a Relying Party is required to request such an attribute when interacting with the Wallet Instance. Neither does it imply that the User cannot refuse to release a mandatory attribute if requested.
- The fourth column indicates how the data elements SHALL be encoded, using the CDDL representation types defined in [RFC 8610].
- The fifth column provides the semantic reference for the attribute in the [European Business Wallet Vocabulary](https://webuild-consortium.github.io/wp4-semantics-group/ebwv//vocabulary.html).

#### TODO

(Refer to [Topic 7] of the ARF for a list of High-Level Requirements related to Revocation)

*In this section information about the revocation mechanism used SHALL be defined.*

*For PID, QEAA, or PuB-EAA it SHALL be defined whether only short-lived attestations
will be used, having a validity period of 24 hours or less, such that revocation
will never be necessary, or that the attestations are revocable.*

*For revocable attestations it SHALL be defined which of the following methods must be implemented:*
* Use an Attestation Status List mechanism included in a Technical Specification
that will be specified by the Commission.
* Use an Attestation Revocation List mechanism included in a Technical Specification
that will be specified by the Commission.

#### 3.1.1 Overview attributes attestation

The LEI attestation is structured as a flat `LegalEntityIdentifier` object containing the `lei` code together with its current status and next renewal date. The model is as follows:

```
LegalEntityIdentifier
├── lei (tstr)
├── lei_status (tstr)
└── lei_renewal_date (tstr)
```

The following table lists the attributes of the LEI attestation. Attribute identifiers SHALL be used in requests and responses.

| **Data Identifier** | **Definition** | **Optionality** | **Encoding format** | **Semantic reference** |
| --- | --- | --- | --- | --- |
| lei | A Legal Entity Identifier (LEI) code, in the format specified by ISO 17442. | M | tstr | [lei](https://webuild-consortium.github.io/wp4-semantics-group/ebwv//vocabulary.html#lei) |
| lei_status | The status of the LEI record registration with the managing LOU. One of the values defined in [section 2.2](#22-code-lists). | M | tstr | [leiRegistrationStatus](https://webuild-consortium.github.io/wp4-semantics-group/ebwv//vocabulary.html#leiRegistrationStatus) |
| lei_renewal_date | The next renewal date of the LEI record, given as a date and time including the timezone, based on ISO 8601. | M | tstr | [leiNextRenewal](https://webuild-consortium.github.io/wp4-semantics-group/ebwv//vocabulary.html#leiNextRenewal) |

### 3.2 Mandatory attributes


### 3.3 Optional attributes


### 3.4 Conditional attributes


## 4 Metadata

Metadata describes the attestation rather than its subject.

### 4.1 Mandatory metadata

| **Data Identifier** | **Definition** |
| --- | --- |
| expiry_date | Date (and if possible time) when the attestation will expire. Does not need to be an attribute and can be covered by credential format metadata, such as for example the "exp" field on the sd-jwt format. |
| issuing_authority | Name of the administrative authority (LEI Issuer / LOU) that issued the LEI attestation, or the ISO 3166 alpha-2 country code of the respective Member State if there is no separate authority entitled to issue the LEI attestation. |
| issuing_country | Alpha-2 country code, as specified in ISO 3166-1, of the country or territory of the provider of the attestation data. |
| attestation_legal_category | Indicates the legal category of this attestation ("EAA" or "pubEAA"/"QEAA") |

**Legal category.** This Rulebook retains the `attestation_legal_category` attribute.
Section 4.1 of the generic template replaces it with the `category` attribute of
[ETSI TS 119 472-1], whose value for this category is `eaa:eu:non-qualified`.
EW-DM-12-029, legacy ARB_25, of ARF version 3.0.0 is a SHALL that still requires
`attestation_legal_category`, so the template and the ARF disagree. The attribute is
left as written and the deviation is recorded for the rulebook quality assurance group.

### 4.2 Optional metadata


### 4.3 Conditional metadata

| **Data Identifier** | **Definition** |
| --- | --- |
| location_status | The location of validity status information on the attestation data where the providers of the attestation revoke it. This attribute is required when the validity time period of the attestation exceeds 24 hours. |
| trust_anchor | This attribute indicates at least the URL at which a machine-readable version of the trust anchor to be used for verifying the LEI attestation can be found or looked up. *Note: This attribute corresponds to the location meant in Annex V point h) or Annex VII point h) of the [European Digital Identity Regulation], which is mandatory for QEAAs. This Rulebook adds this as an optional attribute for LEI attestations as well, so LEI Providers are able to ensure that LEI attestations can be validated by Relying Parties in the same manner as QEAAs.* |

### 4.4 Code lists

The following code list applies to the `lei_status` attribute:

**lei_status**

Values:
- PENDING_VALIDATION
- ISSUED
- DUPLICATE
- LAPSED
- RETIRED
- ANNULLED
- CANCELLED
- TRANSFERRED
- PENDING_TRANSFER
- PENDING_ARCHIVAL

### 4.5 Integrity rules

- lei MUST conform to the format specified by ISO 17442 (a 20-character alphanumeric code).
- lei_status MUST be one of the values defined in the lei_status code list (section 2.2).
- lei_renewal_date MUST follow ISO 8601.


## 5 Formats


### 5.1 SD-JWT VC-based encoding

The LEI attestation is available in the SD-JWT VC format to be aligned with the WeBuild formats.
Yet, selective disclosure is not required for any claim because the included data is public.

The . notation is used to indicate the nesting of attributes.


**Verifiable Credential Type (`vct`):** `eu.we-build.lei.1`


| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Reference/Notes** |
| --- | --- | --- | --- |
| issuing_authority | iss | string | RFC 7519 / Section 2.4 |
| expiry_date | exp | number | RFC 7519 / Section 2.4 (Unix timestamp) |
| attestation_legal_category | attestation_legal_category | string | Section 2.4 |
| issuing_country | issuing_country | string | ISO 3166-1 alpha-2 |
| lei | lei | string | ISO 17442 (20-character alphanumeric) |
| lei_status | lei_status | string | See lei_status code list (section 2.2) |
| lei_renewal_date | lei_renewal_date | string | ISO 8601 (date-time with timezone) |
| location_status | status | object | See chapter [3.2.1](#321-attribute-status) |


#### 5.1.1 Attribute status
For SD-JWT VC-compliant LEI attestations, the attestation MUST include a status claim if the technical validity period is greater than 24 hours. This claim enables Relying Parties to determine if a credential has been revoked via a status list mechanism, as specified in [SD-JWT VC](https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/12/).

The status claim SHALL be a JSON object with the following members:

* 'type' (string): SHALL be "status-list".
* 'status_list_credential' (string, URI): The URI of the Status List Credential document that contains the status bitstring.
* 'status_list_index' (integer, >= 0): The zero-based index into the status list bitstring that corresponds to this credential.
* 'status_purpose' (string): SHALL be "revocation".

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

#### 5.1.2 Example Payload
Sample payloads to be provided under `../../data-schemas/sd-jwt-vc/sample-data/rb-lei-sd-jwt-sample.json`.

### 5.2 ISO/IEC 18013-5-compliant encoding

ISO/IEC 18013-5 (also called mdoc) is out of scope for this rulebook, as offline proximity presentation is not a current requirement for the LEI attestation.

### 5.3 W3C Verifiable Credentials Data Model-based encoding

W3C Verifiable Credentials are defined using linked data (JSON-LD). Ontologies (vocabularies) are used to semantically define the different aspects of credentials including the credential subject. Validation of data structures is optional. If required, either JSON-schemes (data structure) or SHACL (data graph) can be used to validate data.

#### Metadata
The metadata of a W3C Verifiable Credential are defined in the [Verifiable Credentials Vocabulary v2.0](https://www.w3.org/2018/credentials/). The following extensions are defined in the [European Business Wallet Vocabulary v0.1](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary) in order to support Electronic Attestations of Attributes:
* [attestationLegalCategory](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#attestationLegalCategory) in order to specify the category of the EAA (QEAA, Pub-EAA or EAA).

The semantic terms used for the LEI attributes are defined in the [European Business Wallet Vocabulary] (WP4 semantics group): <https://webuild-consortium.github.io/wp4-semantics-group/ebwv/vocabulary.html>.

#### Holder Binding

LEI attestations are held by the organization identified by the LEI. Corresponding key binding is provided by using DIDs. Please note that every node of a JSON-LD tree is addressable by its own locally or globally unique identifier `@id`. Using [Decentralized Identifiers (DIDs) v1.0](https://www.w3.org/TR/did-1.0/) as identifiers allows to cryptographically bind any node to its underlying identity.

The Verifiable Credential Data Model (VCDM) doesn't dictate any specific DID method. Instead, any DID method that supports the underlying trust framework and is able to provide the required level of assurance can be used:
* PKI-Infrastructure (e.g. EU-TLOL based on X.509 certificates): [did:key](https://github.com/digitalbazaar/did-method-key) - the public key is directly encoded in the identifier
* DTL (e.g.: Ethereum): [did:ethr](https://github.com/uport-project/ethr-did)
* European Blockchain Infrastructure: [did:ebsi](https://hub.ebsi.eu/vc-framework/did/legal-entities)
* Domain Name System (DNS): [did:web](https://w3c-ccg.github.io/did-method-web/)
* Domain Name System verifiable history: [did:webvh](https://identity.foundation/didwebvh/v1.0/)

#### Proof mechanisms

The preferred proof mechanism for the LEI attestation is [ecdsa-sd-2023](https://www.w3.org/TR/vc-di-ecdsa/#ecdsa-sd-2023-functions) as specified in [Data Integrity ECDSA Cryptosuites v1.0](https://www.w3.org/TR/vc-di-ecdsa). ecdsa-sd-2023 supports selective disclosure out of the box. The holder chooses which claims to disclose and derives a proof from the original assertion proof.

For backward compatibility and for trust frameworks whose policies require a particular proof mechanism, [JOSE](https://www.w3.org/TR/vc-jose-cose/#with-jose) and [SD-JWT](https://www.w3.org/TR/vc-jose-cose/#with-sd-jwt) as specified in [Securing Verifiable Credentials using JOSE and COSE](https://www.w3.org/TR/vc-jose-cose/) should be supported, too.

The [Security Vocabulary](https://www.w3.org/2025/credentials/vcdi/vocab/v2/vocabulary.html) is used to embed the proofs into the credentials.

#### Credential status

The LEI attestation SHALL include a status claim `credentialStatus` if the technical validity period is greater than 24 hours. This claim enables Relying Parties to determine if a credential has been revoked via a status list mechanism, as specified in [Bitstring Status List v1.0](https://www.w3.org/TR/vc-bitstring-status-list/).

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

The LEI attestation is intended to be used as a standardised, machine-verifiable proof of a legal entity's LEI and its current registration status, to be presented by a Wallet User to a Relying Party in cross-border and domestic contexts.

Typical scenarios include, but are not limited to:

- **Know Your Customer (KYC) and onboarding in finance**: providing a globally recognized, registry-backed identifier and its current status during customer onboarding and counterparty verification.
- **Cross-border business onboarding (B2B)**: sharing an authoritative legal entity identifier during supplier/customer onboarding, procurement qualification, or partner due diligence.
- **Authentication of issuers in international settings**: proving the identity of issuers (e.g. of Digital Product Passports) where a globally unique entity identifier is required.
- **Confirming LEI validity without external lookups**: including the LEI status and renewal date in the attestation so that Relying Parties can confirm the LEI is currently valid without querying the Global LEI Index at verification time.

The LEI attestation is **not** intended to be used as a standalone authentication mechanism to replace processes that legally require a natural person to act and be authenticated in their own right.

**Note:** The LEI attestation identifies a legal entity but does not, by itself, prove that the current presenter is authorised to act on behalf of that entity unless the Relying Party also performs an appropriate binding to the presenter (typically via PID and/or additional authorisation evidence outside the scope of this rulebook).

**Note:** The LEI attestation is intended for **online, remote presentation** using EUDI Wallet-compatible presentation protocols.

* The LEI attestation SHALL be issued by an accredited Local Operating Unit (LOU). This need not be the LOU that originally issued the LEI; any accredited LOU may issue the attestation on the basis of authoritative LEI data. An LOU can authorize an issuer to issue LEI attestations on its behalf.
* The Authentic Source of the data contained in the LEI attestation MUST be an LOU, which validates the data against local registers and is accountable for its correctness. The Global LEI Index operated by GLEIF is an aggregated, periodically refreshed copy and MUST NOT be used as the authentic source, as it may disseminate stale or incorrect status and renewal information.
* The Issuance SHALL be based on up-to-date, authoritative data obtained directly from an LOU.
* The LEI attestation SHALL be key bound to the wallet, IF the wallet belongs to the entity that the LEI attestation is issued for.
* If the LEI attestation is issued to a wallet that is not owned by the entity that the attestation is issued for, the attestation SHALL NOT be key bound to the wallet.
* The LEI attestation SHALL be issued in a format that is compatible with the EUDI Wallet ecosystem (e.g., **OpenID4VP** profiles adopted by the ecosystem).
* To receive an LEI attestation with key binding, the application shall ensure that the wallet is owned by the entity that the attestation is issued for through presentation and matching of key material of the European business wallet owner identification data (OID).

### 7.3 Lifecycle management

The issuer sets the validity period of the attestation and reissues it when the
underlying facts change, revoking the superseded attestation as described in chapter 8.

### 7.4 Embedded disclosure policy

This attestation defines no embedded disclosure policy.

## 8 Revocation


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

Beyond protocol-level checks, an RP processing an LEI attestation presentation **SHALL** perform at least the following controls:

1. **Verify authenticity and integrity**
    - Verify the LEI attestation cryptographic protections (signature/seal chain validation as applicable for the legal category).
    - Verify that the issuer is authorised to issue LEI attestations according to the trust anchor mechanism defined in this rulebook (see Chapter 5).

2. **Verify time validity / freshness**
    - Verify the LEI attestation is within its validity period (e.g., using `exp` in SD-JWT VC).

3. **Check revocation / status (where applicable)**
    - Where the LEI attestation validity exceeds 24 hours and a status mechanism is provided, the RP **SHALL** check the attestation validity status using the mechanism defined in Chapter 6.

4. **Process according to purpose limitation**
    - RPs **SHOULD** request and process the LEI attestation only when needed for the specific transaction, and only for the purpose of the transaction, in line with applicable legal requirements.


LEI attestation presentation may involve **transactional data** exchanged as part of the presentation protocol. The following transactional data elements are relevant:

- **Relying Party request parameters**, including the requested credential type(s) and any policy constraints (e.g., requirement to include PID alongside the LEI attestation).
- **Challenge/nonce and session identifiers** used to prevent replay and bind the presentation to a specific session.
- **Presentation timestamp** (implicit or explicit), to support auditability and freshness validation.
- **Relying Party identification information** presented to the Wallet Unit (e.g., RP name, domain, certificate details), to support user transparency and consent decisions.

The specific protocol artefacts and parameter names depend on the adopted OpenID4VP profile(s). This rulebook does not prescribe additional LEI-specific transactional data beyond what is required by the underlying presentation protocol(s).

### 9.2 Presentation modes

Remote presentation is in scope. Proximity presentation is in scope only where
chapter 5 records an mdoc encoding.

### 9.3 Transactional data

This Rulebook defines no transactional data.

## 10 Trust Framework

#TODO


*Mechanisms for the provision of a trust anchor that SHALL
be used for the verification of an attestation SHALL be defined in this section.*

*It is noted that the ARF specifies the following for QEAAs and Pub-EAAs*

> To do this for [...] QEAAs the Relying Party Instance uses a trust anchor of
> the Provider obtained from a Trusted List. Note that the PID Provider or QEAA
> Provider may use an intermediate signing certificate to sign the PID or
attestation and use the trust anchor to sign the signing certificate, instead
> of signing the PID or attestation directly with the trust anchor.

> For PuB-EAAs, the Relying Party Instance verifies a PuB-EAA by first
> verifying the signature of the PuB-EAA Provider over the PuB-EAA, using the
> PuB-EAA Provider certificate issued by a QTSP. Subsequently, the Relying Party
> Instance verifies the signature over this certificate, using the corresponding
> trust anchor from the QTSP Trusted List. Note that both the PuB-EAA Provider
> and the QTSP may use an intermediate signing certificate. All other things
> being equal, the verification of a PuB-EAA will therefore involve one or more
> extra certificates, compared to the verification of a PID or QEAA.

*For non-qualified EAA in this section it SHOULD be defined (see ARB_26 in [Topic 12])
how the attributes or metadata representing the location at which a machine-readable
version of the trust anchor to be used for verifying the attestation can be found,
specified in section 2, are used. This includes a detailed description about how
a Relying Party can obtain the trust anchor, as well as a detailed description about
how this trust anchor can be used for verifying that the provider is authorised
to issue the attestation. Additionally, for non-qualified EAA Provider this section
MAY include a description of mechanisms that can be used by a Wallet Unit for
verifying that the provider is authorised to issue this type of attestation (see
ISSU_34 in [Topic 10])*

**Trust anchor location**

The attribute or metadata carrying the trust anchor location contains at least the URL
at which a machine-readable version can be found or looked up.

## 11 References

| **Item Reference** | **Standard name/details** |
| --- | --- |
| [European Business Wallet Vocabulary] | WE BUILD WP4 Semantics Group, European Business Wallet Vocabulary. Available: <https://webuild-consortium.github.io/wp4-semantics-group/ebwv/vocabulary.html> |
| [European Digital Identity Regulation] | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework |
| [GLEIF LEI-CDF] | GLEIF, LEI Common Data File (LEI-CDF) Format 3.1. Available: <https://www.gleif.org/en/lei-data/access-and-use-lei-data/level-1-data-lei-cdf-3-1-format> |
| [HAIP] | Yasuda, K. *et al,* OpenID4VC High Assurance Interoperability Profile, OpenId Foundation, Version draft-03 |
| [IANA-JWT-Claims] | IANA JSON Web Token Claims Registry. Available: <https://www.iana.org/assignments/jwt/jwt.xhtml> |
| [ISO 17442] | ISO 17442-1:2020, Financial services --- Legal entity identifier (LEI) --- Part 1: Assignment |
| [ISO 3166-1] | ISO 3166-1, Codes for the representation of names of countries and their subdivisions --- Part 1: Country code |
| [ISO/IEC 18013-5] | ISO/IEC 18013-5, Personal identification --- ISO-compliant driving licence - Part 5: Mobile driving licence (mDL) application, First edition, 2021-09 |
| [OIDC] | Sakimura, N. et al., "OpenID Connect Core 1.0", OpenID Foundation. Available: <https://openid.net/specs/openid-connect-core-1_0.html> |
| [RFC 3339] | RFC 3339  - Date and Time on the Internet: Timestamps, G. Klyne et al., July 2002 |
| [RFC 8610] | RFC 8610  - Concise Data Definition Language (CDDL): A Notational Convention to Express Concise Binary Object Representation (CBOR) and JSON Data Structures, H. Birkholz et al., June 2019 |
| [RFC 8943] | RFC 8943  - Concise Binary Object Representation (CBOR) Tags for Date, M. Jones et al., November 2020 |
| [RFC 8949] | RFC 8949 - Concise Binary Object Representation (CBOR), C. Bormann et al., December 2020 |
| [SD-JWT VC] | SD-JWT-based Verifiable Credentials (SD-JWT VC). Available: <https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/>, version draft-ietf-oauth-sd-jwt-vc-09 |
| [Topic 7] | ARF Annex 2 - Topic 7 - Attestation revocation and revocation checking Available: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a237-topic-7-attestation-revocation-and-revocation-checking> |
| [Topic 10] | ARF Annex 2 - Topic 10 - Issuing a PID or attestation to a Wallet Unit: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a2310-topic-10-issuing-a-pid-or-attestation-to-a-wallet-unit> |
| [Topic 12] | ARF Annex 2 - Topic 12 - Attestation Rulebooks, Available: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a2312-topic-12-attestation-rulebooks> |
| [W3C VCDM v2.0] | Sporny, M. *et al,* Verifiable Credentials Data Model v2.0, W3C Recommendation. |
