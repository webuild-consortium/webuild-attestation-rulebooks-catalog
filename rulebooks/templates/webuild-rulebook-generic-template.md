# Attestation Rulebook for attestations of type [ATTESTATION TYPE]

Category: [PID / EBWOID / QEAA / PuB-EAA / non-qualified EAA]

Generic WE BUILD template, structure agreed at the rulebook quality assurance workshop. Aligned to ARF v3.0.0 (21 July 2026) and EC attestation rulebook template v1.5 (8 July 2026).

**Markers.** FIXED means consortium-agreed text, copy verbatim and raise changes
upstream. [AUTHOR] means yours to write. TO AGREE means an open consortium decision,
leave it alone. Strip all three before submission to the EC catalogue.

- Author(s): [NAME SURNAME, AFFILIATION]
- Previous authors: [NAME SURNAME, AFFILIATION (versions)]

| Version | Date | Description |
| --- | --- | --- |
| [VERSION] | [DATE] | [DESCRIPTION OR LINK TO CHANGELOG] |

**Written against:** ARF version [ARF VERSION], WE BUILD template version [VERSION]

**Feedback:** [ISSUE TRACKER URL]

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
   * [6.1 Issuance](#61-issuance)
   * [6.2 Presentation](#62-presentation)
- [7 Issuance](#7-issuance)
   * [7.1 Binding](#71-binding)
   * [7.2 Issuance Policy](#72-issuance-policy)
   * [7.3 Lifecycle management](#73-lifecycle-management)
   * [7.4 Embedded disclosure policy](#74-embedded-disclosure-policy)
- [8 Revocation](#8-revocation)
- [9 Request, Presentation and Verification](#9-presentation)
   * [9.1 Relying Party Role ( RP Instance - EUDI Wallet)](#91-rp-role)
   * [9.2 Relying Party Role ( RP Instance - EUDI Wallet)](#91-ebw-rp-role)
   * [9.3 Presentation modes](#93-presentation-modes)
   * [9.4 Transactional data](#94-transactional-data)
- [10 Trust Framework](#10-trust-framework)
- [11 References](#11-references)


## 1 Introduction

### 1.1 Document scope and purpose

[AUTHOR] Describe in plain language what this attestation expresses and what it is
for. A reader who knows nothing about the domain should understand it from this
section alone. Cover:

- the real-world fact, entitlement, role, status or capability it expresses;
- the expected issuers, holders and relying parties;
- the use case or user journey it supports;
- the attestation description or functional specification it draws on;
- any use it is not intended for.

Keep terminology aligned with the source attestation description.

### 1.2 Document structure

FIXED

> Chapter 2 states how this Rulebook complies with the applicable regulatory and
> architectural requirements. Chapter 3 specifies the attestation attributes and
> chapter 4 the metadata, both in an encoding-independent manner, each referencing
> the machine-readable schema artefacts that define their encoding. Chapter 5 lists
> the attestation formats supported. Chapter 6 lists the issuance and presentation
> protocols supported. Chapter 7 specifies issuance, including binding and lifecycle
> management. Chapter 8 specifies revocation. Chapter 9 specifies presentation.
> Chapter 10 specifies the trust framework, including how trust anchors are
> obtained. Chapter 11 lists references.
>
> Chapters 5 and 6 identify formats and protocols only. The substantive rules for
> issuance and presentation are in chapters 7 and 9 respectively, and are not
> repeated in chapters 5 and 6.

### 1.3 Key words

FIXED

> This document uses the capitalised key words 'SHALL', 'SHOULD' and 'MAY' as
> specified in [RFC 2119], to indicate requirements, recommendations and options.
> In addition, 'must' (non-capitalised) indicates an external constraint, that is, a
> requirement mandated by an external document rather than by this document. The
> word 'can' indicates a capability. Other words such as 'will', 'is' and 'are' are
> statements of fact.

### 1.4 Terminology

FIXED

> This document uses the terminology specified in Annex 1 of the ARF.

[AUTHOR] Add only terms specific to this attestation type that Annex 1 does not
define. Do not restate ARF definitions.

| Term | Definition | Source |
| --- | --- | --- |
| | | |

## 2 Compliance

FIXED

> This chapter states how this Rulebook complies with the Architecture and Reference
> Framework and with the applicable Regulations. Sections 2.1 and 2.2 follow from the
> legal category of this attestation. Section 2.3 maps each applicable requirement to
> the section that satisfies it.

### 2.1 Compliance statement

FIXED

> This Rulebook complies with the applicable requirements of Topic 12, Attestation
> Rulebooks, in Annex 2 of the Architecture and Reference Framework, version
> [ARF VERSION]. It uses the terminology of Annex 1 of the ARF.

### 2.2 Regulatory basis

FIXED

> The regulatory basis below is the one applicable to the legal category of this
> attestation.

**PID**

> This Rulebook specifies how the mandatory and optional person identification data
> defined in Tables 1 and 2 of the Annex to CIR (EU) 2024/2977, and the metadata
> defined in Table 5 of that CIR, are encoded within the EUDI Wallet ecosystem.

**QEAA**

> This attestation includes the data required by Annex V of Regulation (EU)
> 2024/1183, points a, b, c, e and h, satisfying EW-DM-12-014, EW-DM-12-016,
> EW-DM-12-019, EW-DM-12-021 and EW-DM-12-023 respectively. It is issued by a
> qualified trust service provider.

**PuB-EAA**

> This attestation includes the data required by Annex VII of Regulation (EU)
> 2024/1183, points a, b, c, e and h, satisfying EW-DM-12-014, EW-DM-12-017,
> EW-DM-12-019, EW-DM-12-021 and EW-DM-12-023 respectively. It is issued by or on
> behalf of a public sector body responsible for an authentic source.

**Non-qualified EAA**

> This attestation is not a qualified electronic attestation of attributes. The data
> described in Annex V points b, c and e of Regulation (EU) 2024/1183 is addressed as
> required by EW-DM-12-018 and as recommended by EW-DM-12-020 and EW-DM-12-022.
> Where a recommendation is not followed, the reason is stated below.

**Non-qualified self EAA (S-EAA)** 

> This attestation is a subtype of non-qualified electronic attestation of attributes.
> From a technical perspective, there is no difference between an EAA and a S-EAA.
> The difference lies in the legal aspect in regard to issuer liability.
> It is based on self owned information, issued and used exclusively within a defined closed ecosystem
> and governed by its specific trust and governance framework, which have no effect on third parties.
> The issuer is not providing a trust service to others as described in Article 2 (2) of Regulation (EU) 2024/1183 
> therefore, TSP liability defined with-in eIDAS not apply, the liability is covered by contract law or existing contracts.

**EBWOID**

> TO AGREE. Do not assert qualified status unless the issuer is a QTSP, and do not
> cite Annex V or Annex VII by default.

### 2.3 Traceability

FIXED

> Every applicable requirement mapped to the section that satisfies it. Mark a
> requirement not applicable only with a stated reason. No blank rows at submission.

| Requirement | Legacy ID | Applies | Satisfied in section | Note |
| --- | --- | --- | --- | --- |
| EW-DM-12-001 | ARB_01a | | | Format restriction, W3C VCDM permitted for non-qualified EAA only |
| EW-DM-12-002 | ARB_01b | | | SD-JWT VC per the HAIP profile |
| EW-DM-12-003 | ARB_02 | | | mdoc required if proximity presentation is in scope |
| EW-DM-12-005 | ARB_04 | | | Approved specifications for W3C VCDM encoding |
| EW-DM-12-006 | ARB_05 | | | Unique attestation type or vct |
| EW-DM-12-007 | ARB_06 | | | Encoding-independent attribute definitions |
| EW-DM-12-008 | ARB_06a | | | mdoc attribute identifiers and namespaces |
| EW-DM-12-009 | ARB_06b | | | SD-JWT VC claim naming |
| EW-DM-12-010 | ARB_07 | | | Reuse of catalogued attributes |
| EW-DM-12-012 | ARB_09 | | | Mandatory, optional or conditional marking |
| EW-DM-12-013 | ARB_10 | | | Domestic namespace, if defined |
| EW-DM-12-014 | ARB_11 | | | Annex V or VII point a |
| EW-DM-12-015 | ARB_12 | | | EAA indication, non-qualified only |
| EW-DM-12-016 / EW-DM-12-017 / EW-DM-12-018 | ARB_13 / ARB_14 / ARB_15 | | | Point b, by category |
| EW-DM-12-019 / EW-DM-12-020 | ARB_16 / ARB_17 | | | Point c, by category |
| EW-DM-12-021 / EW-DM-12-022 | ARB_18 / ARB_19 | | | Point e, by category |
| EW-DM-12-023 / EW-DM-12-024 | ARB_20 / ARB_21 | | | Trust anchor or certificate location, by category |
| EW-DM-12-030 | ARB_26 | | | Trust anchor publication, non-qualified EAA |
| EW-DM-12-031 | ARB_27 | | | Whether the Relying Party must also verify a PID |
| EW-DM-12-032 | ARB_28 | | | `cryptographically_bound_to`, if used |
| EW-DM-12-034 | ARB_30 | | | Selective disclosure per claim |
| EW-DM-12-035 | ARB_31 | | | Claim Selective Disclosure Metadata |
| EW-DM-12-038 | ARB_34 | | | Device binding |

## 3 Attestation attributes

FIXED

> Attributes are defined here in an encoding-independent manner (EW-DM-12-007). The
> authoritative encoding lives in the machine-readable schema artefacts referenced in
> section 3.1, not in this document. Do not paste schema fragments into the prose,
> they will drift.

### 3.1 Introduction

[AUTHOR] Describe the design of the attribute set and the decisions behind it. For
complex attestations, include or reference a logical model showing the main entities,
relationships and attribute groupings.

**Schema artefacts.** FIXED table shape. One row per format supported in chapter 5.

| Format | Identifier | Schema artefact | Version | Location |
| --- | --- | --- | --- | --- |
| SD-JWT VC | `vct` value | JSON schema or Type Metadata Document | | [URL FOR SCHEMAS] |
| mdoc | doctype and namespace | CDDL or attribute definition file | | [URL FOR SCHEMAS] |
| W3C VCDM | type and context | JSON-LD context | | [URL] |

FIXED

> The schema artefacts referenced above are normative for encoding. Where this
> document and a referenced artefact disagree, the artefact prevails for encoding
> questions and this document prevails for semantics, presence and disclosure rules.
> Each artefact SHALL be versioned and immutably addressable. Versioning of the
> artefacts SHALL align on major releases.

Note on selective disclosure: for SD-JWT VC, whether a claim is selectively
disclosable is stated in the tables below, not in the schema (EW-DM-12-034). Where
a Claim Selective Disclosure Metadata document is used (EW-DM-12-035), reference it
above.

### 3.2 Mandatory attributes

FIXED

> Attributes that SHALL be present in every attestation of this type.

| Data identifier | Semantic reference | Definition | Data type | Selectively disclosable | Example value |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

### 3.3 Optional attributes

FIXED

> Attributes the Provider MAY include at its discretion.

| Data identifier | Semantic reference | Definition | Data type | Selectively disclosable | Example value |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

### 3.4 Conditional attributes

FIXED

> Attributes required only when a stated condition holds. State the condition
> explicitly in the definition, not in a footnote.

| Data identifier | Semantic reference | Definition | Condition | Data type | Selectively disclosable | Example value |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |


## 4 Metadata

FIXED

> Metadata describes the attestation rather than its subject. Use the same schema
> artefacts referenced in section 3.1.

### 4.1 Mandatory metadata

FIXED

> Includes the `category` attribute for all categories except PID.

| Category | `category` value |
| --- | --- |
| QEAA | `urn:etsi:esi:eaa:eu:qualified` |
| PuB-EAA | `urn:etsi:esi:eaa:eu:pub` |
| Non-qualified EAA | `eaa:eu:non-qualified` |
| EBWOID | TO AGREE |
| PID | not applicable, omit |

FIXED

> The `category` attribute is defined in [ETSI TS 119 472-1] and SHALL NOT be
> selectively disclosable. In the mdoc encoding it belongs to the namespace
> `org.etsi.01947201.010101`. The superseded `attestation_legal_category` attribute,
> with values QEAA, PuB-EAA and non-qualified-EAA, SHALL NOT be used.

| Data identifier | Semantic reference | Definition | Data type | Example value |
| --- | --- | --- | --- | --- |
| category | | Legal category of this attestation | string | |
| | | | | |

### 4.2 Optional metadata

FIXED

> Includes `cryptographically_bound_to` where section 7.1 records a cryptographic
> binding (EW-DM-12-032).

| Data identifier | Semantic reference | Definition | Data type | Example value |
| --- | --- | --- | --- | --- |
| | | | | |

### 4.3 Conditional metadata

| Data identifier | Semantic reference | Definition | Condition | Data type | Example value |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

### 4.4 Code lists

FIXED

> Controlled vocabularies, enumerations and value sets needed to interpret attributes
> consistently. Reference an external vocabulary wherever one exists rather than
> defining a local list.

| Field | Allowed values or vocabulary | Meaning | Source | Extensible |
| --- | --- | --- | --- | --- |
| | | | | |

### 4.5 Integrity rules

FIXED

> Consistency rules not captured by the schema alone: cross-field dependencies,
> temporal consistency, mutual exclusivity, conditional combinations.

| Rule ID | Rule statement | Why it exists | Where enforced | Behaviour on failure |
| --- | --- | --- | --- | --- |
| IR-01 | | | | |

## 5 Formats

FIXED

> This chapter identifies the formats in which this attestation is issued. The
> encoding detail lives in the schema artefacts referenced in section 3.1, and the
> rules for using each format are in chapters 7 and 9.

| Format | Supported | Identifier | Specification | Notes |
| --- | --- | --- | --- | --- |
| ISO/IEC 18013-5 mdoc | yes / no | doctype `[VALUE]`, namespace `[VALUE]` | [ISO/IEC 18013-5] | Required if proximity presentation is in scope (EW-DM-12-003) |
| SD-JWT VC | yes / no | `vct` `[VALUE]` | [SD-JWT VC], [HAIP] | SHALL follow the HAIP profile (EW-DM-12-002) |
| W3C VCDM | yes / no | type `[VALUE]`, context `[URL]` | [W3C VCDM v2.0] | Permitted for non-qualified EAA only (EW-DM-12-001) |

FIXED

> A PID SHALL be issued in both the ISO/IEC 18013-5 and SD-JWT VC formats. For other
> attestation types, at least one format SHALL be marked as supported. Identifiers
> SHALL be unique to this attestation type (EW-DM-12-006).

[AUTHOR] Where more than one format is supported, state whether a Provider SHALL
offer all of them or MAY choose.

## 6 Protocols

FIXED

> This chapter identifies the protocols used to issue and present this attestation.
> The substantive issuance rules are in chapter 7 and the presentation rules are in
> chapter 9.

### 6.1 Issuance

| Protocol | Supported | Profile or version | Specification | Notes |
| --- | --- | --- | --- | --- |
| OpenID4VCI | yes / no | [Specify URL to profile] | [OpenID4VCI], [HAIP], [ETSI TS 119 472-3], [CIR (EU) 2026/1731] | |
| [OTHER] | | | | |

### 6.2 Presentation

| Protocol | Supported | Profile or version | Specification | Notes |
| --- | --- | --- | --- | --- |
| OpenID4VP, remote | yes / no | [Specify URL to profile] | [OpenID4VP], [HAIP], [ETSI TS 119 472-2], [CIR (EU) 2026/1731] | |
| ISO/IEC 18013-5, proximity | yes / no | [Specify URL to profile] | [ISO/IEC 18013-5], [ETSI TS 119 472-2], [CIR (EU) 2026/1731] | Requires the mdoc format |
| [OTHER] | | | | |

FIXED

> Protocols listed here are those referenced in Topic 6 of Annex 2 of the ARF. This
> Rulebook does not profile these protocols beyond what is stated in the table.

## 7 Issuance

### 7.1 Holder Key Binding at Issuance (Wallet Binding)
FIXED
> This is a fundamental security requirement that prevents credential theft and ensures an attestation is bound to a specific wallet. 
> *   **What it is:** Before the attestation is created, the Holder's wallet **MUST** perform a "proof-of-possession" challenge to prove it controls a specific private key. The Attestation Provider then embeds the corresponding public key into the attestation payload before signing it.
> *   **Why it matters:** This process creates a permanent, cryptographic link between the attestation and the Holder's wallet. During presentation (as described in Chapter 9), a Relying Party can then challenge the presenting wallet to prove it still controls that same private key. This verification step makes stolen or copied attestation files useless to a thief, as they will not have the required private key.
> ---
FIXED table shape. Complete every row, none may be left blank.

| Field | Value | Source |
| --- | --- | --- |
| Device-bound | SHALL / SHOULD / MAY / non device-bound | EW-DM-12-038 |
| Cryptographically bound to | none / attestation type or vct value | EW-DM-12-032 |
| Relying Party must also verify a PID | yes / no / not applicable | EW-DM-12-031 |
| Binding subject | natural person / legal person / wallet unit | |

[AUTHOR] Justify any answer that departs from the category default. For QEAA and
PuB-EAA the defaults are device-bound and bound to the PID unless justified. For
EBWOID all four rows are TO AGREE.

### 7.2 Issuance Policy

FIXED

> An Issuance Policy defines the minimum rules, policies, and procedures that any compliant Attestation Provider **SHALL** follow when issuing attestations of this type. 

> For transparency and to allow Relying Parties to programmatically assess their trust in the attestation, each Attestation Provider **SHALL** publish their terms and conditions, a generic Trust Services Policy, and an EAA Policy (per attestation type) in accordance with **[ETSI TS 119 471]**. These policies must be accepted by the Holder upon receipt of the attestation.

> This section references key concepts from **[ETSI TS 119 471]** and **[ETSI TS 119 461]**. The most critical issuance concepts for a rulebook author to understand and specify are explained below:

> ---

#### **1. Core Issuer Obligations**

> Any entity acting as an authorized Attestation Provider under this rulebook **SHALL** comply with the following general obligations:

>   **Issuance Basis and Timestamping:** The Provider **SHALL** issue the attestation based on information and supporting documentation that is valid and accurate at the exact moment of issuance. A timestamp (`iat`) **MUST** be included in each attestation. This enables a Relying Party to not only verify the attestation's temporal validity but also to correctly validate the Attestation Provider's trust status as it was at the moment of issuance (e.g., by checking against a historical Trust List).

> *   **Data Currency and Revocation:** The Provider is responsible for the ongoing accuracy of the attested information. The Provider **MUST** immediately revoke the attestation if any change occurs that affects the validity or accuracy of the underlying data.

> ---

> #### **2. Identity and Attribute Proofing (as per ETSI TS 119 461)**

> This refers to the rigor with which the Attestation Provider verifies the information before issuing the attestation. The level of trust a Relying Party can place in an attestation depends directly on the quality of this proofing process.

> *   **Identity Proofing:** This is the process of verifying the legal identity of the subject. For a legal entity (a business), this **MUST** involve verifying its active registration in an official national business register.
> *   **Attribute Proofing:** This is the process of verifying the specific claims (attributes) being attested. The Provider **MUST** verify the attributes against a designated authentic data source (as defined by the author below).

> ---
> OPEN TOPICS
> To enable a EBW Provider to implement basic verification steps described in Chapter 9.2 the "General obligations of an Attestation Provider" that are out of scope of this rulebook need to be updated. The following requirements need to be considered:
> 1. The EAA Provider needs an attestation from a QTSP that binds his EUID to a "signing_key". This should be the EBWOID with the additional "signing_key" parameter. Where do we specify the solution? Proposed Answer: EBWOID rulebook
> 2. The EAA Provider needs a mechanism to transfer his attested public signing key and also the identity attestation of the QTSP to the unknown RP. e.g.: He can include his EBWOID in the Header of each EAA and in the Header of the EBWOID the QTSP has included his EBWOID or the x.509 identity chain. That is a general issuer obligation. Is this mechanism already specified? Where do we specify this mechanism?
> I personally prepare and have prepared the following text based on ADR#168 or a merged ADR between ADR#168 and ADR#336

> #### **3. Architectural Pattern for EAA Provider Trust**

> To enable the EBW Provider to implement the basic verification steps described in Chapter 9, the following general issuer obligations apply to all EAA Providers:

> 1.  **Provider Identity Credential:** The EAA Provider **MUST** possess their own European Business Wallet Owner Identity (EBWOID), issued by a Qualified Trust Service Provider (QTSP). To be authorized to sign and issue other EAAs, this EBWOID **MUST** contain a `signing_key` parameter holding the public key the Provider uses to sign the issued EAAs. *(This requirement is formally specified in the `rb-ebwoid` rulebook).*
> 2.  **Trust Chaining Mechanism:** The EAA Provider **MUST** include their own EBWOID (or a reference/chain to it) in the header of every EAA they issue. This allows a Relying Party to verify the EAA signature using the public key from the embedded EBWOID, and then verify the EBWOID itself against the eIDAS Trusted List. *(This general mechanism is specified in the `rb-base` rulebook).*

> ---

> #### **4. Batch Issuance (Protocol Optimization)**

> This is a technical efficiency and privacy feature defined in the underlying OpenID4VCI protocols.

> *   **What it is:** A technical capability allowing a Wallet to request, and an Attestation Provider to issue, multiple credentials simultaneously in a single API interaction, rather than requiring separate network connections for each credential.
> *   **Application to this Rulebook:** For unique, long-lived business attestations, batch issuance is typically **Optional** or **Not Applicable**, as these credentials do not require multi-copy anonymity and are issued on a one-off basis.

> ---

[AUTHOR]

Based on the explanations above, specify the following parameters for this specific attestation type:

*   **Authorized Authentic Sources:** State the exact authorized authentic source(s) that any Attestation Provider **MUST** use for attribute proofing (e.g., *"The 'iban' attribute MUST be verified against the official account records of the issuing account-servicing payment service provider (ASPSP)"*).
*   **Attestation Lifecycle:** Specify the maximum validity period (expiration) and rules for renewal of the issued attestation (e.g., 12 months, or dynamic real-time validity).
*   **Batch Issuance Designation:** Explicitly state whether Batch Issuance is permitted, prohibited, or designated as Not Applicable for this attestation type.
*   **Attestation-Specific Obligations:** List any other specific obligations (e.g., selective disclosure rules from Chapter 3, format obligations from Chapter 5, or trust anchor publishing rules from Chapter 10).


### 7.3 Lifecycle management

[AUTHOR] Specify:

- validity period, or the rule that determines it;
- reissuance and renewal, including cadence for short-lived attestations;
- update or correction when the underlying facts change.

Alternative: If the lifecycle management is specified in the EAA Policy and/or the Attestation Provider's trust services policy (as mentioned in the Issuance Policy section 7.2), then it is possible to refer these document(s) instead of specifying the details of the lifecycle management.

### 7.4 Embedded disclosure policy

| Field | Value |
| --- | --- |
| Policy present | yes / no |
| Common policy applied | none / authorised relying parties only / specific root of trust |
| Encoding | pending upstream specification |

FIXED

> Embedded disclosure policies are defined in CIR (EU) 2024/2979 and in Topic 43 of
> Annex 2 of the ARF. No standardised encoding exists in ISO/IEC 18013-5, SD-JWT VC,
> OpenID4VCI or OpenID4VP at the time of writing. This Rulebook declares which policy
> applies and does not specify a local encoding.

## 8 Revocation

FIXED

> This chapter states whether attestations of this type are revocable, and if so how
> revocation status is published and how a Relying Party checks it.

TO AGREE. The consortium default for this chapter is an open decision.

**Short-lived**

> Attestations of this type are short-lived, with a validity period of 24 hours or
> less. They are therefore not revocable and Relying Parties do not perform a
> revocation check.

**Revocable**

> Attestations of this type are revocable. Revocation status is published using
> [Attestation Status Lists / Attestation Revocation Lists], as specified in the
> relevant Technical Specification issued by the Commission. Relying Parties and
> other entities can retrieve the relevant lists at [DOMAIN OR URL]. The full
> location relevant to an individual attestation is included in that attestation.

[AUTHOR] State who may request revocation, and the grounds specific to this
attestation type, in addition to any grounds already imposed by regulation. State the
expected time from trigger to status list update.

# Chapter 9: Request, Presentation and Verification

## 9.1. Relying Party Role ( RP Instance - EUDI Wallet)

FIXED

> To verify and validate a received presentation of an attestation of this type,
> the following steps SHALL be performed:

> 1.  **Cryptographic Integrity Verification (Tamper Proof):**
>     The Verifier **MUST** verify that the received attestation data has not been altered or tampered with since its issuance. The wallet shall validate the digital signature over the attestation using a trusted public key (trust anchor) obtained according to the framework detailed in Chapter 10.
> 2.  **Issuer Authentication and Trust Evaluation:**
>      The Verifier **MUST** verify the identity and regulatory standing of the Attestation Provider. The Verifier **MUST** verify that a trust anchor (Qualified Trust Service Provider (QTSP) for EAAs (EBWOID check), or the designated national Supervisory Body for other attestation (EBWOID checks or X.509)), has confirmed that the attestation issuer owned the public key corresponding to the private key used to sign the verified attestation at the time of issuance.
> 3.  **Temporal Validity Verification:**
>      The Verifier **MUST** verify that the attestation is within its stated validity window. An attestation that has not yet taken effect or has already expired **SHOULD** be accepted, regardless of any other successful checks.
> 4.  **Revocation Status Verification:**
>    The Verifier **MUST** verify the real-time revocation status of the received attestation as described in Chapter 8, unless:
>     *   The attestation is explicitly defined as short-lived; or
>     *   The remaining lifetime of the attestation is below the designated revocation time threshold.
> 5.  **Holder Wallet and Device Binding Verification:**
> Where the attestation is device-bound according to section 7.1, the Verifier **MUST** verify the Holder's presentation signature and the presentation's binding to achieve two critical security checks:
>     *   Ensure that the presenter has not submitted a copied or replayed attestation (e.g., presenting a copied EBWOID belonging to a different legal entity).
>     *   Validate that the presented attestation was issued to this exact presenting wallet instance.

[AUTHOR] Add obligations specific to this attestation type below. Do not edit the
list above.


## 9.2. EBW Relying Party Role ( EBW Wallet - EBW Wallet)
>Following the principle of mutual identification the verification in the **European Business Wallet (EBW)** ecosystem is designed as a mutual cryptographic process. Unlike traditional consumer wallet flows, EBW transactions must satisfy high-assurance, machine-to-machine (M2M) environments. Verification of EAAs is executed under two distinct conditions:

> 1.  **Relying Party Role:** When an EBW Owner receives a presented attestation from a Holder and must verify its cryptographic claims before providing a service or executing a transaction.
> 2.  **Holder Role:** When an EBW Holder receives an incoming Presentation Request and must verify the identity and system integrity of the requesting Relying Party before releasing confidential, non-public attestation data.

> The system performs these verification steps to achieve three core business and regulatory objectives:
> *   **Trust Augmentation:** Establishing the absolute cryptographic authenticity of exchanged data and validating the identity of the participating legal entities.
> *   **Liability Allocation:** Fulfilling statutory due diligence to minimize operational risk and programmatically shift liability to the responsible party (Issuer or Holder).
> *   **Data Protection:** Safeguarding highly confidential corporate data (e.g., ultimate beneficial ownership, control structures) stored in the EBW against unauthorized harvest or access.

> ## 9.2.1 Relying Party obligation during request 
> 1.  **Include own identification and authorization data in presentation requests:**
> When requesting non-public and therefore confidential data, the Relying Party **SHALL** include its own **EBWOID** and **BWUA** (using the `ebwoid` and `ebw_wallet_unit` format blocks in the `verifier_info` array of the Request Object) to allow the receiving Holder to:
>    *   Enforce automated consent and exchange policies based on the Verifier’s legal identity and verified platform integrity.
>    *   Ensure the request originates from a valid wallet instance rather than uncertified or spoofed software.
>    *   *Operational Constraint:* Requesters that do not present a valid EBWOID and BWUA **SHOULD NOT** receive confidential attestations.
> 2.  **Request Wallet Unit Attestations (BWUA):**
> The Relying Party **SHOULD** include a request for the Holder’s Business Wallet Unit Attestation (BWUA)  to mitigate the risk of interacting with a revoked, compromised, or modified wallet instance.
> 3.  **Adhere to Data Minimization (Purpose Limitation):**
> The Relying Party **SHALL** only request attributes that are strictly necessary to fulfill the stated business purpose of the transaction.
> 4.  **Respect Trust Model Registration:**
> Where the trust model for a requested attestation requires Relying Party registration, the RP **SHALL** only request attributes it is explicitly registered and authorized to request.

FIXED
> ## 9.2.2. Holder and Relying Party obligation during verification

> To protect the Holder and Relying Party from processing fraudulent, tampered, or stolen attestations, they  **MUST** programmatically execute the following five verification steps on all received attestations. Holder and Relying Party performing the verification steps are called Verifier within the rest of this chapter. The Verifier can perform the steps only if the EBW supports the verification steps, therefore the EBW Wallet Provider **MUST** support the following verification steps with their EBW:

> 1.  **Cryptographic Integrity Verification (Tamper Proof):**
>     The Verifier **MUST** verify that the received attestation data has not been altered or tampered with since its issuance. The wallet shall validate the digital signature over the attestation using a trusted public key (trust anchor) obtained according to the framework detailed in Chapter 10.
> 2.  **Issuer Authentication and Trust Evaluation:**
>      The Verifier **MUST** verify the identity and regulatory standing of the Attestation Provider. The Verifier **MUST** verify that a trust anchor (Qualified Trust Service Provider (QTSP) for EAAs (EBWOID check), or the designated national Supervisory Body for other attestation (EBWOID checks or X.509)), has confirmed that the attestation issuer owned the public key corresponding to the private key used to sign the verified attestation at the time of issuance.
> 3.  **Temporal Validity Verification:**
>      The Verifier **MUST** verify that the attestation is within its stated validity window. An attestation that has not yet taken effect or has already expired **SHOULD** be accepted, regardless of any other successful checks.
> 4.  **Revocation Status Verification:**
>    The Verifier **MUST** verify the real-time revocation status of the received attestation as described in Chapter 8, unless:
>     *   The attestation is explicitly defined as short-lived; or
>     *   The remaining lifetime of the attestation is below the designated revocation time threshold.
> 5.  **Holder Wallet and Device Binding Verification:**
> Where the attestation is device-bound according to section 7.1, the Verifier **MUST** verify the Holder's presentation signature and the presentation's binding to achieve two critical security checks:
>     *   Ensure that the presenter has not submitted a copied or replayed attestation (e.g., presenting a copied EBWOID belonging to a different legal entity).
>     *   Validate that the presented attestation was issued to this exact presenting wallet instance.

> ### 9.2.2.1 Impact of Cryptographic Verification on Holder Liability
> The mandatory validation of incoming requests protects the Holder when operating in high-security, backend-to-backend environments:

> *   **Establishes Non-Repudiation (Defense Against Dispute):** By validating the signature of the Request Object against the public key attested inside the Relying Party's EBWOID, the Relying Party cannot later deny having initiated the transaction or requested the data. This protects the Holder from legal claims that they disclosed confidential business secrets without a valid, authorized request.
> *   **Protects Against Impersonation (Defense Against Data Breaches):** It cryptographically proves the request did not originate from a malicious actor who simply spoofed the Relying Party's public `client_id` or metadata. Because the transaction requires a signature generated by the private key securely held within the Relying Party's hardware wallet, the Holder is guaranteed they are communicating with the actual legal entity identified in the EBWOID.
> *   **Fulfills Statutory Due Diligence (Safe Harbor under GDPR):** Under data protection regulations, a corporate Holder has a legal duty to protect its confidential operational data. Executing these mandatory checks before releasing any data payload safe-harbors the Holder from charges of negligence or unauthorized data disclosure.
> ---

> ### 9.2.2.2 Impact of Cryptographic Verification on Relying Party Liability

> The execution of the mandatory cryptographic checks defined in this chapter directly determines the legal and liability posture of the Relying Party (RP). Under the European Business Wallet framework and eIDAS, performing these verifications shifts liability and protects the RP from negligence claims:

> | Verification Check | Cryptographic Fact | Impact on Relying Party Liability |
> | :--- | :--- | :--- |
> | **Integrity & Issuer Auth (Steps 1 & 2)** | Proves data has not been modified; validates the cryptographic identity of the issuer. | **Transfers Data-Accuracy Liability to Issuer.** The RP is legally protected against errors or falsehoods in the received data. Liability shifts to the Attestation Provider under eIDAS2 or their published terms. |
> | **Temporal & Revocation (Steps 3 & 4)** | Proves the credential was actively valid and unrevoked at the exact moment of the transaction. | **Protects Against Fraud Claims.** Safe-harbors the RP from claims arising from the use of credentials that were valid in the past but have since expired or been revoked. |
> | **Device Binding & Presentation Signature (Step 5)** | Proves the holder has possession of the private key associated with the credential and actively authorized this specific session. | **Protects Against Identity Theft & Establishes Safe Harbor.** Explained in detail below. |

> #### **Defense Against Identity Theft (Shifts Burden of Proof)**
> By verifying the device binding (e.g., via the Key Binding JWT, matching `nonce` and `aud`), the RP proves that the presenter has real-time, hardware-backed control over the private key associated with the credential.

> If a malicious actor steals a copy of another company's EBWOID file, they **cannot** generate a valid binding signature without access to that specific wallet's private key. By verifying this binding, the RP completely protects itself from claims of *"failing to prevent obvious credential-sharing or identity theft,"* shifting the burden of proof entirely to the claimant.

> #### **Safe Harbor for Data Access and Key Compromise**
> Under GDPR and eIDAS, if an RP discloses confidential data or executes a transaction based on a credential where device binding was fully and correctly verified, it is legally deemed to have fulfilled its due diligence. If it is later discovered that the Holder's private key was compromised at the time of the transaction, the liability shifts away from the RP to:
> *   The **Holder**, for failing to adequately secure and protect their private key/hardware device.
> *   The **Issuer**, if they were notified of the key compromise but failed to add the credential to their revocation list in a timely manner.

> #### **Eliminates Sole Negligence under eIDAS (Art 12a / 12b)**
> Under eIDAS Article 12a and 12b, a Relying Party has a duty of care to validate credentials. If an RP fails to verify the presentation signature and the corresponding trust chains, they are considered to have accepted an unauthenticated payload. In the event of a security breach or fraudulent transaction, the RP can be held **solely liable** due to technical negligence.

> ---

[AUTHOR] Add obligations specific to this attestation type below. Do not edit the
list above.

### 9.3 Presentation modes

[AUTHOR] State which of remote and proximity presentation are in scope, consistent
with chapters 5 and 6. If proximity is in scope, the mdoc format is required.

### 9.4 Transactional data

FIXED

> No transactional data as defined in Topic 20 of Annex 2 of the ARF is associated
> with this attestation type.

Replace only if this attestation is used for strong user authentication for
electronic payments.


## 10 Trust Framework

FIXED

> The trust anchor for this attestation is obtained as described in the branch below
> that corresponds to its legal category. The trust anchor location applies in either
> case.

**PID, QEAA, PuB-EAA and attestations resolved via Trusted Lists**

FIXED

> The trust anchor is obtained from a Trusted List, as described in section 6.6.3.6
> of the ARF main document. The Provider may sign the attestation with an
> intermediate signing certificate, in which case the trust anchor is used to verify
> that certificate rather than the attestation directly.

> **Non-qualified EAA with Attestation Chaining**

> For this category, the attestation is not issued directly by a Qualified Trust Service Provider (QTSP). Instead, trust is established through a **delegated trust model** that chains back to a qualified credential. The process for a Relying Party to establish the trust anchor is as follows:

> 1.  **Locating the Trust Link:** The EAA Provider **MUST** embed their own European Business Wallet Owner Identity (EBWOID) credential within the header of the issued EAA. This embedded EBWOID serves as the crucial link in the trust chain.

> 2.  **Verifying the Trust Link:** The Relying Party **MUST** first extract and fully verify the embedded EBWOID. Since the EBWOID is itself a QEAA, its trust anchor is found on the **EU Trusted List of Lists (TLoL)**. This verification confirms that the EAA Provider is a legitimate legal entity, as certified by a QTSP.

> 3.  **Establishing the EAA's Trust Anchor:** The payload of the verified EBWOID contains the EAA Provider's public signing key (the `signing_key`). This key becomes the **direct trust anchor** for the Non-qualified EAA itself.

> 4.  **Verifying the EAA:** The Relying Party uses this trust anchor (the `signing_key` from the EBWOID) to perform the cryptographic integrity verification of the EAA.

> In this model, trust is not directly established from the TLoL to the EAA, but is delegated from the **TLoL -> QTSP -> EAA Provider's EBWOID -> EAA Provider's Signing Key -> EAA**.

> Following successful cryptographic verification, the authorisation of the Provider to issue this specific type of attestation is a business-level decision for the Relying Party, based on its own internal policies and trust lists.

> **Non-qualified EAA signed with QSEAL**
> [to be described]

> **Non-qualified EAA based on ADR#336**
> [to be described]

> **Trust anchor location**

FIXED

> The attribute or metadata carrying the trust anchor location contains at least the
> URL at which a machine-readable version can be found or looked up. For a QEAA this
> location refers to the trust anchor (EW-DM-12-023). For a PuB-EAA it refers to the
> qualified certificate that signed the attestation (EW-DM-12-023). For a
> non-qualified EAA the location and its meaning are as described above
> (EW-DM-12-024, EW-DM-12-030).

Coherence check: the attribute named here SHALL be the same attribute declared in
chapter 4.

**Deployment profile**

[AUTHOR] Record the trust anchor arrangements specific to this attestation and to the
deployment it runs in. Do not edit the FIXED text above. Cover the following where
they apply, and state explicitly where one does not:

- how Provider trust anchors are distributed, naming any List of Trusted Entities or
  Trusted List involved and the registration or notification process behind it;
- how a Relying Party or Wallet Unit looks a trust anchor up, including the
  attributes the lookup keys on and any caching or update policy;
- the ordered steps a Relying Party follows to verify the authenticity of this
  attestation, and the ordered steps a Wallet Unit follows to authenticate a Relying
  Party before presentation;
- any consortium-specific endpoint, profile or extension the deployment depends on;
- worked examples.

## 11 References

| Reference | Details |
| --- | --- |
| [Regulation] | Regulation (EU) 2024/1183 amending Regulation (EU) No 910/2014 |
| [CIR 2024/2977] | Commission Implementing Regulation (EU) 2024/2977, PID and EAA |
| [CIR 2024/2979] | Commission Implementing Regulation (EU) 2024/2979, integrity and core functionality |
| [CIR 2026/1731] | Commission Implementing Regulation (EU) 2026/1731, as regards applicable standards and specifications |
| [ARF] | EUDI Wallet Architecture and Reference Framework, version [VERSION] |
| [ETSI TS 119 461] | Policy and security requirements for trust service components providing identity proofing of trust service subjects  |
| [ETSI TS 119 471] | Policy and security requirements for EAA service providers |
| [ETSI TS 119 472-1] | Profiles for Electronic Attestations of Attributes; Part 1 - General requirements |
| [ETSI TS 119 472-2] | Profiles for Electronic Attestations of Attributes; Part 2 - Profiles for EAA/PID Presentations to Relying Party  |
| [ETSI TS 119 472-3] | Profiles for Electronic Attestations of Attributes; Part 3 - Profiles for issuance of EAA or PID |
| [ETSI TS 119 478] | Specification of interfaces related to Authentic Sources |
| [HAIP] | OpenID4VC High Assurance Interoperability Profile |
| [ISO/IEC 18013-5] | Personal identification, ISO-compliant driving licence, Part 5, 2021 |
| [OpenID4VCI] | OpenID for Verifiable Credential Issuance |
| [OpenID4VP] | OpenID for Verifiable Presentations |
| [RFC 2119] | Key words for use in RFCs to Indicate Requirement Levels |
| [SD-JWT VC] | SD-JWT-based Verifiable Credentials |
| [W3C VCDM v2.0] | Verifiable Credentials Data Model v2.0 |
