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
- [9 Presentation](#9-presentation)
   * [9.1 Presentation Policy](#91-presentation-policy)
   * [9.2 Presentation modes](#92-presentation-modes)
   * [9.3 Transactional data](#93-transactional-data)
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

### 7.1 Binding

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

[AUTHOR] Specify:

- reference to the Attestion Provider's generic trust services policy in accordance with ETSI TS 119 471;
- reference to the EAA Policy (for each attestation type) in accordance with ETSI TS 119 471;

**Attestation Provider obligations.** FIXED opening, then attestation-specific
additions.

> General obligations on Attestation Providers are out of scope of this Rulebook.
> They are specified in Topic 10 of Annex 2 of the ARF, in the applicable Implementing
> Regulations, and in [ETSI TS 119 471]. This Rulebook states only obligations
> specific to this attestation type.
> More specifically, the Attestation Provider's generic trust services policy can be provided in accordance with ETSI TS 119 471.
> Each EAA Policy (per attestation type) can specify:
> - identity proofing in accordance with ETSI TS 119 461;
> - attribute proofing in accordance with ETSI TS 119 461;
> - batch issuance, if used, and any limits on reuse;
> - authentic source of the attributes (if applicable according to ETSI TS 119 478), and how currency is assured;

[AUTHOR] List the attestation-specific obligations, if any, each as a pointer to the
section that states it, for example format obligations from chapter 5, selective
disclosure rules from chapter 3, trust anchor publication from chapter 10.

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

# Chapter 9: Presentation and Mutual Verification

FIXED
> ## 9.1 Presentation and Verification Policy

> ### 9.1.1 Principles of Mutual Identification and Verification

> Verification in the **European Business Wallet (EBW)** ecosystem is designed as a mutual cryptographic process. Unlike traditional consumer wallet flows, EBW transactions must satisfy high-assurance, machine-to-machine (M2M) environments. Verification is executed under two distinct conditions:

> 1.  **Relying Party Role:** When an EBW Owner receives a presented attestation from a Holder and must verify its cryptographic claims before providing a service or executing a transaction.
> 2.  **Holder Role:** When an EBW Holder receives an incoming Presentation Request and must verify the identity and system integrity of the requesting Relying Party before releasing confidential, non-public attestation data.

> The system performs these verification steps to achieve three core business and regulatory objectives:
> *   **Trust Augmentation:** Establishing the absolute cryptographic authenticity of exchanged data and validating the identity of the participating legal entities.
> *   **Liability Allocation:** Fulfilling statutory due diligence to minimize operational risk and programmatically shift liability to the responsible party (Issuer or Holder).
> *   **Data Protection:** Safeguarding highly confidential corporate data (e.g., ultimate beneficial ownership, control structures) stored in the EBW against unauthorized harvest or access.

---

> ### 9.1.2 Mandatory Verification Steps for Received Attestations

> To protect the EBW Owner from processing fraudulent, tampered, or stolen credentials, the EBW Wallet **MUST** programmatically execute the following five verification steps on all received attestations:

> 1.  **Cryptographic Integrity Verification (Tamper Proof):**
>     The EBW **MUST** verify that the received attestation data has not been altered or tampered with since its issuance. The wallet shall validate the digital signature over the attestation using a trusted public key (trust anchor) obtained according to the framework detailed in Chapter 10.
> 2.  **Issuer Authentication and Trust Evaluation:**
>     The EBW **MUST** verify the identity and regulatory standing of the Attestation Provider:
>     *   The wallet shall confirm that a Qualified Trust Service Provider (QTSP) for EAAs, or the designated national Supervisory Body for other attestations, has confirmed that the attestation issuer owned the public key corresponding to the private key used to sign the verified attestation at the time of issuance.
>     *   The EBW **MUST** verify the name and European Unique Identifier (EUID) of the issuer of the received attestation. For EAAs, this is done based on the EBWOID issued by a QTSP. For other attestations, this is done based on the X.509 certificates included in the Trust List of Lists (TLoL) or EBWOIDs.
>     *   *Business Rule:* This step is required to enable the EBW Owner to decide if attestations from this specific issuer are accepted according to internal policies.
> 3.  **Temporal Validity Verification:**
>     The EBW **MUST** verify that the attestation is within its stated validity window. An attestation that has not yet taken effect or has already expired **MUST NOT** be accepted, regardless of any other successful checks.
> 4.  **Revocation Status Verification:**
>     The EBW **MUST** verify the real-time revocation status of the received attestation as described in Chapter 8, unless:
>     *   The attestation is explicitly defined as short-lived; or
>     *   The remaining lifetime of the attestation is below the designated revocation time threshold.
> 5.  **Holder Wallet and Device Binding Verification:**
>     Where Section 7.1 records the attestation as device-bound, the EBW **MUST** verify the Holder's presentation signature and the presentation's > > binding to achieve two critical security checks:
>     *   Ensure that the presenter has not submitted a copied or replayed attestation (e.g., presenting a copied EBWOID belonging to a different legal entity).
>     *   Validate that the presented attestation was issued to this exact presenting wallet instance.

> ---

> ### 9.1.3 Impact of Cryptographic Verification on Relying Party Liability

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

> ### 9.1.4 Impact of Cryptographic Verification on Holder Liability

> Just as verification protects the Relying Party, the mandatory validation of incoming requests protects the Holder when operating in high-security, backend-to-backend environments:

> *   **Establishes Non-Repudiation (Defense Against Dispute):** By validating the signature of the Request Object against the public key attested inside the Verifier's EBWOID, the Verifier cannot later deny having initiated the transaction or requested the data. This protects the Holder from legal claims that they disclosed confidential business secrets without a valid, authorized request.
> *   **Protects Against Impersonation (Defense Against Data Breaches):** It cryptographically proves the request did not originate from a malicious actor who simply spoofed the Verifier’s public `client_id` or metadata. Because the transaction requires a signature generated by the private key securely held within the Verifier’s hardware wallet, the Holder is guaranteed they are communicating with the actual legal entity identified in the EBWOID.
> *   **Fulfills Statutory Due Diligence (Safe Harbor under GDPR):** Under data protection regulations, a corporate Holder has a legal duty to protect its confidential operational data. Executing these mandatory checks before releasing any data payload safe-harbors the Holder from charges of negligence or unauthorized data disclosure.

> ---

> ### 9.1.5 Relying Party (Verifier) Obligations

> To maintain ecosystem security and protect business-critical processes, a Relying Party operating within the WE BUILD trust framework **SHALL** comply with the following obligations:

> 1.  **Request Wallet Unit Attestations (BWUA):**
>     The Relying Party **SHALL** include a request for the Holder’s Business Wallet Unit Attestation (BWUA) in all high-trust presentation requests to mitigate the risk of interacting with a revoked, compromised, or modified wallet instance.
> 2.  **Present Mutual Identification in Presentation Requests:**
>     When requesting non-public or confidential data, the Relying Party **SHALL** include its own **EBWOID** and **BWUA** (using the `ebwoid` and `ebw_wallet_unit` format blocks in the `verifier_info` array of the Request Object) to allow the Holder to:
>    *   Enforce automated consent and exchange policies based on the Verifier’s legal identity and verified platform integrity.
>    *   Ensure the request originates from a valid wallet instance rather than uncertified or spoofed software.
>     *   *Operational Constraint:* Requesters that do not present a valid EBWOID and BWUA **SHALL NOT** receive confidential attestations.
> 3.  **Adhere to Data Minimization (Purpose Limitation):**
    The Relying Party **SHALL** only request attributes that are strictly necessary to fulfill the stated business purpose of the transaction.
> 4.  **Respect Trust Model Registration:**
    Where the trust model for a requested attestation requires Relying Party registration, the RP **SHALL** only request attributes it is explicitly registered and authorized to request.

[AUTHOR] Add obligations specific to this attestation type below. Do not edit the
list above.

### 9.2 Presentation modes

[AUTHOR] State which of remote and proximity presentation are in scope, consistent
with chapters 5 and 6. If proximity is in scope, the mdoc format is required.

### 9.3 Transactional data

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

**Non-qualified EAA**

> The trust anchor is not obtained from a Trusted List of qualified trust service
> providers. It is obtained as follows: [CONSORTIUM DEFAULT MECHANISM, TO AGREE].
> Authorisation of the Provider to issue this attestation type is then verified by
> [PROCEDURE].
>
> A Wallet Unit MAY verify Provider authorisation using the mechanism described in
> ISSU_34 of Topic 10 of Annex 2 of the ARF.

**Trust anchor location**

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
