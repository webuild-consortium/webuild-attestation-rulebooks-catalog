# Attestation Rulebook for attestations of type Membership Credential

Category: non-qualified EAA

*This WE BUILD Rulebook specifies the Membership Credential used in the WE BUILD Supply Chain 2
(SC2) MVP scenario "seamless onboarding" piloted by the Data Sharing Initiatives (DSI) DjustConnect
(ILVO), DADS (ITC) and Tritom (Dataspace Europe), and the common agriculture dataspace "Agri-X".*

- Author(s): Ingo Wolf, [Spherity GmbH](https://www.spherity.com); Martin Domajnko, [Lutra Labs d.o.o.](https://lutralabs.io)
- Previous authors: none

| Version | Date | Description |
| --- | --- | --- |
| 01 | 2026-06-25 | Initial Rulebook derived from the MVP Membership credential attestation description. |
| 02 | 2026-08-26 | consolidated draft |
| 03 | 2026-08-26 | BREAKING: `role`/`roles` values changed from bare strings to absolute URIs under `https://w3id.org/ebwv/roles#`; `memberOf` values changed from bare strings to absolute URIs minted per-DSI under the DSI's own domain. See Section 2.8. |
| 04 | 2026-08-27 | `onboardedBy` gains `memberIdentifier`, the platform-local identifier of the **holder** (Section 2.2.2/2.2.4), bridging the EBWOID/EUID to legacy identifiers; code list 2.8 corrected accordingly. Chapter 3 (SD-JWT VC and W3C VCDM) realigned with the Chapter 2 attribute names (`member`, `role`, `termsOfUse`) after drift; holder `legalName` folded into `member`. Disclosability rules made consistent (Section 3.2.2). Use of the credential in data-sharing transactions marked out of scope for the pilot. |
| 05 | 2026-09-01 | Editorial: "SC2" expanded to "Supply Chain 2 (SC2)" on first use; feedback channel now points to the Supply Chain 2 contact points. |
| 06 | 2026-09-01 | BREAKING, aligns the Rulebook with the published European Business Wallet Vocabulary and its JSON-LD context. Reverts entry 03: `role` and `memberOf` values return from absolute URIs to plain terms, since both properties are typed `xsd:string` in the vocabulary and the `https://w3id.org/ebwv/roles#` namespace does not exist — role individuals are published under `https://w3id.org/ebwv#`. Namespace-prefix trust withdrawn accordingly (Section 5), IR-05 added. `onboardedBy.memberIdentifier` refactored to credential-level `evidence` (Section 2.6), recording the identification means used to prove the holder's identity during initial onboarding; `onboardedBy` now describes the onboarding platform only. Identifiers adopt the vocabulary's typed-literal pattern; the Identifier object of entry 04 is withdrawn and `member` uses `legalIdentifier`. Cardinality in compacted and expanded JSON-LD documented (Section 3.3.1). New Section 3.3.2 records the type declarations required for expansion, after a round-trip through a JSON-LD processor showed that the previous credential-level `type` of `Membership` caused `member`, `memberOf`, `role` and `onboardedBy` to be dropped silently; `Membership` now types the credential subject. |
| 07 | 2026-09-02 | The credential subject gains the optional `holderIdentifier` attribute (Section 2.3), derived from the source attestation description (*MVP Membership credential — attestation description*, v1.0, section 1.4.1). It carries the identifier by which the onboarding platform refers to the holder, and is populated only where the value differs from `member.legalIdentifier`. It sits alongside `memberOf` on the credential subject rather than inside `onboardedBy`, because it describes the holder and not the onboarding platform; `onboardedBy` now identifies the onboarding party only. No companion `holderIdentifierType` is defined: the scheme follows from the onboarding platform named in `onboardedBy`, and where it must be stated explicitly the identifier is carried as `evidence`, whose scheme is machine-readable. IR-06 and IR-07 added. The attribute has no property term in the published vocabulary context, so it is recorded among the known expansion gaps in Section 3.3.2. The credential-level `type` now includes `ElectronicAttestationOfAttributes`, which is what brings `attestationLegalCategory` into scope; that attribute previously dropped on expansion and now resolves to the `EAA` individual, closing the gap recorded in entry 06. `attestation_legal_category` moved from the Membership attribute table (Section 2.2) to mandatory metadata (Section 2.5), since it qualifies the attestation rather than the member and is carried at credential level. |
| 08 | 2026-09-02 | BREAKING, follows the European Business Wallet Vocabulary context republished on 2 September 2026. That context retypes `role` and `memberOf` from `xsd:string` to `@id`, so both now carry **absolute IRIs** and expand to node references; the plain terms introduced in entry 06 are withdrawn. Role values are the `DataSpaceRole` individuals under `https://w3id.org/ebwv#`. Verified by expansion: a relative value such as `DataRightsHolder` resolves against the document base, yielding a different IRI for every location a credential is served from. Namespace-prefix trust for `role` is reinstated (Section 5) and a DSI may now mint its own role IRIs without a vocabulary or Rulebook change. The same context adds `holderIdentifier` to the `Membership` type-scoped context, closing the last expansion gap from entry 07; Section 3.3.2 now records full coverage. IR-05 restated in terms of IRI matching. |
| 09 | 2026-09-09 | Splits a proposed redesign of the illustrative example into the part that the published vocabulary supports today and the part that does not. **Deferred, pending a change request to the WE BUILD Semantics work group:** an `OnboardingDetails` class to replace `Platform`, a `member` property in that class's type-scoped context to carry the holder as the onboarding platform knows them, and identifier scheme individuals `Bpn` and `KmgMid`. None of the four is published, and each was verified to fail: an undefined scheme used as the datatype of a typed literal aborts JSON-LD expansion outright, while an undefined class name silently deactivates the type-scoped context, dropping `platformId` and `operator` without error. The illustrative example in Section 3.3 is therefore kept on `Platform`, and the platform-local identifier of the holder continues to be carried by `holderIdentifier` (Section 2.3) or `evidence` (Section 2.6). `member` MAY now carry additional identifiers beyond `legalIdentifier` via the repeatable `identifier` property (Section 2.2.3), in both encodings. `holderIdentifier` is withdrawn: `member.identifier` subsumes it, since code list 2.8 already permits an untyped string where the scheme has no published individual, which was the only case `holderIdentifier` still covered. IR-06 and IR-07 are restated against `member.identifier`, keeping the rule that `member.legalIdentifier` remains the authoritative identifier of the holder. The data type of `id` (Section 2.2) is corrected from `UUID` to an absolute URI, a DID or a `urn:uuid:` URN, which is what every example in this Rulebook has always used and what the `@id` keyword requires. `termsOfUse` moves from the Membership attributes (Section 2.2) to mandatory metadata (Section 2.5), carried at credential level: W3C VCDM defines it as a property of the credential rather than of its subject, and the SD-JWT VC encoding already carried it as a top-level claim, so the two encodings now agree. IR-01 is unchanged in meaning. |
| 10 | 2026-09-16 | BREAKING, follows the European Business Wallet Vocabulary context republished on 16 September 2026, which acted on the change requests recorded in entry 09. The `Platform` class is **withdrawn** and replaced by [OnboardingDetails](https://w3id.org/ebwv#OnboardingDetails), whose type-scoped context carries `platform`, `operator` and `member`. `platformId` is withdrawn with it: the platform is now identified by the `id` of the `onboardedBy` object itself, since the vocabulary defines no property for it, and its commercial name moves from `name` to `platform`. The `name` row is dropped rather than kept alongside `platform`, which would have given two spellings of one fact. `onboardedBy` gains the optional `member`, the holder as the onboarding platform knows it, which is where a platform-local identifier now belongs; the example carries `DC-2026-004711` there instead of on `member.identifier`. IR-06 and IR-07 widen to cover an identifier of the holder wherever it appears. `KmgMid` is published, so the DADS farm id can be a typed literal; code list 2.8 lists it and the untyped-string fallback is narrowed to genuinely platform-specific values. The vocabulary also removed `holderIdentifier`, confirming its withdrawal in entry 09. Three requests remain open: a generic `PlatformSpecific` scheme, an `OnboardingEvidence` class so evidence entries need not be typed `EconomicOperator`, and `Bpn`, which is withdrawn as out of scope for the MVP. |
| 11 | 2026-10-05 | Restructured onto the generic WE BUILD attestation rulebook template (11 chapters). No normative content removed. The restructure started from the content of version 08; versions 09 and 10 were re-applied in version 12. |
| 12 | 2026-10-07 | Re-applies versions 09 and 10, and the subsequent mapping note for `holderIdentifier`, onto the template structure of version 11: `termsOfUse` at credential level (Section 4.1.1); `onboardedBy` typed `OnboardingDetails`, identified by its own `id` and named by `platform`, with the optional `member` (Section 3.2.1); `holderIdentifier` withdrawn in favour of the repeatable `member.identifier`, with a mapping from the source attestation description (Section 3.1); IR-06 and IR-07 covering both places an identifier of the holder can appear; `KmgMid` in code list 4.4. Also corrects section cross-references left over from the pre-template numbering, removes a reference to a cardinality section that no longer exists, and aligns Section 9.1 with IR-05, which requires IRI rather than string comparison for `role` and `memberOf`. Section references in entries 01 to 10 refer to the numbering in force at the time. |
| 13 | 2026-10-21 | Aligns the Rulebook with the generic WE BUILD attestation rulebook template. Fixed template text reproduced verbatim where it applies to a non-qualified EAA; schema-artefacts table added (Section 3.1); a selectively-disclosable column added to the attribute tables (Sections 3.2 to 3.4); template columns adopted for the code lists, integrity rules and conditional tables; protocol tables (Chapter 6), embedded disclosure policy table (Section 7.4), issuance policy and lifecycle content (Sections 7.2, 7.3), revocation grounds (Chapter 8) and a deployment profile (Chapter 10) added; terms table added (Section 1.4); reference list completed. Two template fixed texts are deliberately not reproduced, because they conflict with choices this Rulebook retains pending a decision of the rulebook quality assurance group: the `category` attribute of Section 4.1, and the Commission status lists of Chapter 8. No change to attributes, encodings, examples or schemas. |
| 14 | 2026-10-21 | Aligns the Rulebook with revision #195 of the generic WE BUILD attestation rulebook template. Section 7.1 renamed Holder Key Binding at Issuance (Wallet Binding); Section 7.2 replaced by the new Issuance Policy text, with the parameters for this attestation type: authorised authentic sources, a maximum validity period of 12 months, and batch issuance not permitted; Chapter 8 states that revocation takes effect immediately on the issuer's trigger event; Chapter 9 restructured into Request, Presentation and Verification, with the EBW Relying Party role of Section 9.2 as the applicable one; Chapter 10 split into Sections 10.1 and 10.2. The legal category remains non-qualified EAA. Recorded deviation, pending a decision of the rulebook quality assurance group: attestation chaining through the Provider's EBWOID (Sections 7.2 and 10.2.1) is not yet adopted. |
| 15 | 2026-10-21 | Adds Section 5.3.2, Semantic verification: the limits of JSON Schema for a JSON-LD credential, the advantages of validating the expanded graph with SHACL, and an example SHACL constraint. Republishes the SHACL shapes next to the JSON Schema in `data-schemas/jsonld/`, renumbered to the template section structure and extended to the status entry and identifier schemes the JSON Schema checks. Section 3.1 lists both as supporting artefacts. No change to attributes, encodings or examples. |

**Written against:** ARF version 3.0.0, WE BUILD template version 1.0 (generic)

**Feedback:** https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/issues. Alternatively, contact the Supply Chain 2 contact points in WE BUILD.

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
   * [6.1 Issuance](#61-issuance)
   * [6.2 Presentation](#62-presentation)
- [7 Issuance](#7-issuance)
   * [7.1 Holder Key Binding at Issuance (Wallet Binding)](#71-holder-key-binding-at-issuance-wallet-binding)
   * [7.2 Issuance Policy](#72-issuance-policy)
   * [7.3 Lifecycle management](#73-lifecycle-management)
   * [7.4 Embedded disclosure policy](#74-embedded-disclosure-policy)
- [8 Revocation](#8-revocation)
- [9 Request, Presentation and Verification](#9-request-presentation-and-verification)
   * [9.1 Relying Party Role (RP Instance - EUDI Wallet)](#91-relying-party-role-rp-instance---eudi-wallet)
   * [9.2 EBW Relying Party Role (EBW Wallet - EBW Wallet)](#92-ebw-relying-party-role-ebw-wallet---ebw-wallet)
   * [9.3 Presentation modes](#93-presentation-modes)
   * [9.4 Transactional data](#94-transactional-data)
- [10 Trust Framework](#10-trust-framework)
   * [10.1 Relying Party Role (RP Instance - EUDI Wallet)](#101-relying-party-role-rp-instance---eudi-wallet)
   * [10.2 EBW Relying Party Role (EBW Wallet - EBW Wallet)](#102-ebw-relying-party-role-ebw-wallet---ebw-wallet)
- [11 References](#11-references)


## 1 Introduction

### 1.1 Document scope and purpose

The Membership Credential expresses that its holder is a member of a specific Data Sharing
Initiative (DSI) or dataspace, which roles the holder has within that DSI or dataspace, and to
which dataspace governance rulebook the holder has conformed. It exists to enable *seamless
onboarding*: common information already presented in a previous onboarding flow is trusted and not
requested again when the holder onboards into a further DSI or the common dataspace.

In plain language, the credential combines all necessary information about the dataspace or DSI
membership into a single attestation held in an EU Business Wallet (EBW), independent of any
dataspace-specific connector technology.

* **Real-world fact expressed:** membership of a DSI or dataspace, the roles held within it
  (e.g. Data Rights Holder, Data Provider, Data Consumer, Operator, Onboarding Service Provider),
  and acceptance of the dataspace governance rulebook.
* **Issuers:** trusted issuers / onboarding service providers (the participating DSIs, or another
  technology partner acting as onboarding service provider). Agri-X is envisaged as a federation of
  DSIs; participants join Agri-X via a DSI or directly via a trusted issuer.
* **Holders:** organisations (legal persons) participating in a DSI or dataspace. The MVP scenario
  is limited to legal persons.
* **Relying parties:** DSI / dataspace platforms and participants that verify membership and roles
  during onboarding. Use during data-sharing transactions is a *potential* future application and
  is **out of scope for this pilot**: a data-transfer flow would likely require the Membership
  Credential to be transformed into a connector-native credential (for instance an EDC / dataspace
  protocol participant credential) rather than presented directly.
* **Use case:** WE BUILD SC2 "seamless onboarding" piloted by DjustConnect (ILVO), DADS (ITC) and
  Tritom (Dataspace Europe), targeting the common agriculture dataspace "Agri-X".
* **Source document:** *MVP Membership credential, attestation description*.

The schema is designed to be re-usable and interoperable with other dataspaces. It is aligned with
the membership credential used within Catena-X; attributes that must remain interoperable with such
operational dataspaces are marked as dataspace-specific (DS-specific) terminology that SHALL NOT be
renamed.

### 1.2 Document structure

Chapter 2 states how this Rulebook complies with the applicable regulatory and
architectural requirements. Chapter 3 specifies the attestation attributes and
chapter 4 the metadata, both in an encoding-independent manner, each referencing
the machine-readable schema artefacts that define their encoding. Chapter 5 lists
the attestation formats supported. Chapter 6 lists the issuance and presentation
protocols supported. Chapter 7 specifies issuance, including binding and lifecycle
management. Chapter 8 specifies revocation. Chapter 9 specifies presentation.
Chapter 10 specifies the trust framework, including how trust anchors are
obtained. Chapter 11 lists references.

Chapters 5 and 6 identify formats and protocols only. The substantive rules for
issuance and presentation are in chapters 7 and 9 respectively, and are not
repeated in chapters 5 and 6.

### 1.3 Key words

This document uses the capitalised key words 'SHALL', 'SHOULD' and 'MAY' as
specified in [RFC 2119], to indicate requirements, recommendations and options.
In addition, 'must' (non-capitalised) indicates an external constraint, that is, a
requirement mandated by an external document rather than by this document. The
word 'can' indicates a capability. Other words such as 'will', 'is' and 'are' are
statements of fact.

### 1.4 Terminology

This document uses the terminology specified in Annex 1 of the ARF.

| Term | Definition | Source |
| --- | --- | --- |
| Data Sharing Initiative (DSI) | An operational data-sharing platform whose members exchange data under a common governance rulebook; in this Rulebook DjustConnect, DADS and Tritom. | WE BUILD SC2 use case |
| Agri-X | The common agriculture dataspace, envisaged as a federation of DSIs. | WE BUILD SC2 use case |
| Dataspace governance rulebook | The rules a member of a DSI or dataspace accepts on joining it, referenced by `termsOfUse`. | WE BUILD SC2 use case |
| Onboarding Service Provider | A DSI or technology partner that onboards members into a DSI or into Agri-X and issues the Membership Credential. | WE BUILD SC2 use case; Catena-X |
| EUBWOID | European Business Wallet Owner Identification Data, the attestation identifying the organisation that owns a European Business Wallet; its EUID is reused as `member.legalIdentifier`. | `rb-ebwoid` |

## 2 Compliance

This chapter states how this Rulebook complies with the Architecture and Reference
Framework and with the applicable Regulations. Sections 2.1 and 2.2 follow from the
legal category of this attestation. Section 2.3 maps each applicable requirement to
the section that satisfies it.

### 2.1 Compliance statement

This Rulebook complies with the applicable requirements of Topic 12, Attestation
Rulebooks, in Annex 2 of the Architecture and Reference Framework, version 3.0.0. It
uses the terminology of Annex 1 of the ARF.

### 2.2 Regulatory basis

The regulatory basis below is the one applicable to the legal category of this
attestation.

**Non-qualified EAA**

This attestation is not a qualified electronic attestation of attributes. The data
described in Annex V points b, c and e of Regulation (EU) 2024/1183 is addressed as
required by EW-DM-12-018 and as recommended by EW-DM-12-020 and EW-DM-12-022.
Where a recommendation is not followed, the reason is stated below.

Both recommendations are followed: point c through the `member` attributes (section 3.2)
and point e through the validity metadata of each format (chapter 5).

### 2.3 Traceability

Every applicable requirement mapped to the section that satisfies it. Mark a
requirement not applicable only with a stated reason. No blank rows at submission.

| Requirement | Legacy ID | Applies | Satisfied in section | Note |
| --- | --- | --- | --- | --- |
| EW-DM-12-001 | ARB_01a | yes | 5.3 | W3C VCDM is the primary format; permitted because this is a non-qualified EAA |
| EW-DM-12-002 | ARB_01b | yes | 5.1 | SD-JWT VC following the HAIP profile, as an additional flow |
| EW-DM-12-003 | ARB_02 | no |  | Proximity presentation is not in scope; no mdoc encoding, see section 5.2 |
| EW-DM-12-005 | ARB_04 | yes | 5.3 | W3C VCDM v2.0 with the European Business Wallet Vocabulary context |
| EW-DM-12-006 | ARB_05 | yes | 5.1, 5.3 | Unique vct and credential type for this attestation type |
| EW-DM-12-007 | ARB_06 | yes | 3 | Attributes defined independently of encoding |
| EW-DM-12-008 | ARB_06a | no |  | No mdoc encoding is defined |
| EW-DM-12-009 | ARB_06b | yes | 5.1 | SD-JWT VC claim naming |
| EW-DM-12-010 | ARB_07 | yes | 3 | Attributes taken from the European Business Wallet Vocabulary |
| EW-DM-12-012 | ARB_09 | yes | 3, 4 | Mandatory, optional and conditional stated per attribute |
| EW-DM-12-013 | ARB_10 | no |  | No domestic namespace is defined |
| EW-DM-12-014 | ARB_11 | no |  | Annex V and VII point a apply to QEAA and PuB-EAA |
| EW-DM-12-015 | ARB_12 | yes | 4.1 | EAA indication through `attestationLegalCategory` |
| EW-DM-12-016 / EW-DM-12-017 / EW-DM-12-018 | ARB_13 / ARB_14 / ARB_15 | yes | 2.2, 5 | Point b through the issuer metadata of each format |
| EW-DM-12-019 / EW-DM-12-020 | ARB_16 / ARB_17 | yes | 2.2, 3.2 | Point c, recommendation for non-qualified EAA, through the member attributes |
| EW-DM-12-021 / EW-DM-12-022 | ARB_18 / ARB_19 | yes | 2.2, 5 | Point e through the validity metadata of each format |
| EW-DM-12-023 / EW-DM-12-024 | ARB_20 / ARB_21 | yes | 10 | Trust anchor resolved from the issuer DID |
| EW-DM-12-029 | ARB_25 | yes | 4.1 | Legal category attribute; see the note in section 4.1 |
| EW-DM-12-030 | ARB_26 | yes | 10 | Trust anchor published through the issuer DID document |
| EW-DM-12-031 | ARB_27 | no |  | The holder is a legal person identified through the EUBWOID; no PID verification, see section 7.1 |
| EW-DM-12-032 | ARB_28 | no |  | `cryptographically_bound_to` is not used, see section 7.1 |
| EW-DM-12-034 | ARB_30 | yes | 3.2, 3.3, 4.1, 4.2 | Selective disclosure stated per attribute; per claim for SD-JWT VC, ZKP-based for W3C VCDM |
| EW-DM-12-035 | ARB_31 | no |  | No Claim Selective Disclosure Metadata document is used |
| EW-DM-12-038 | ARB_34 | yes | 7.1 | Binding to the holder organisation's EU Business Wallet |

## 3 Attestation attributes

Attributes are defined here in an encoding-independent manner (EW-DM-12-007). The
authoritative encoding lives in the machine-readable schema artefacts referenced in
section 3.1, not in this document. Do not paste schema fragments into the prose,
they will drift.

### 3.1 Introduction

The Membership Credential is a **non-qualified EAA**. This document defines the attribute
[attestationLegalCategory](https://w3id.org/ebwv#attestationLegalCategory) which SHALL have the value `EAA`.
It qualifies the attestation as a whole rather than the member, and is therefore carried at
credential level, outside the credential subject; in the W3C VCDM encoding the credential-level
`type` SHALL include
[ElectronicAttestationOfAttributes](https://w3id.org/ebwv#ElectronicAttestationOfAttributes), which
is what defines the attribute. See Section 5.3.1.

The credential describes the member (the `CredentialSubject`) together with the roles the
member has within the DSI or dataspace (`role`), and the platform through which the member was onboarded
(`onboardedBy`). Separately, at credential level, `evidence` records the identification means by
which the holder's identity was proven during the initial onboarding process.

**Logical model.** The Membership Credential is structured as follows:

* The credential subject is identified by `id` (a URI, may change) and `member`, an object of type
  [EconomicOperator](https://w3id.org/ebwv#EconomicOperator) carrying the stable identifier of the
  holder in `legalIdentifier`; for the MVP this re-uses the EUID from the EUBWOID of that economic
  operator.
* `memberOf` names the DSI or dataspace the membership is for.
* `role` is an array of roles the holder has within that DSI or dataspace. The membership and its
  set of roles share the same lifecycle: a change of roles requires re-issuance of the credential.
* `onboardedBy` is an object of type [OnboardingDetails](https://w3id.org/ebwv#OnboardingDetails)
  describing the onboarding: the platform, identified by the object's own `id` and named by
  `platform`; the `operator` — the economic operator hosting and running that platform; and,
  optionally, `member`, the holder as that platform knows it.
* `termsOfUse` is an object of type [GovernanceRulebook](https://w3id.org/ebwv#GovernanceRulebook)
  referencing the accepted dataspace governance rulebook (URL, version, SHA-256 hash, and
  acceptance datetime). It is carried at credential level, not in the credential subject: W3C VCDM
  defines `termsOfUse` as a property of the credential, and the SD-JWT VC encoding already carried
  it as a top-level claim, so this placement makes the two encodings agree (Section 4.1.1).
* `evidence` records the identification means used to prove the holder's identity during the
  initial onboarding process, for example the VAT identifier presented in a paper-based onboarding
  flow. It is credential metadata about the issuance, not an attribute of the subject, and is
  therefore carried at credential level rather than inside the credential subject (Section 4.2).

Note that `evidence` describes how **the holder** was identified, whereas `onboardedBy` describes
the platform and the organisation that performed the onboarding. Keeping the two apart is
deliberate: an identifier recorded as evidence belongs to the holder, never to the platform
operator. As a side effect, `evidence` also bridges the EU-level identifier in
`member.legalIdentifier` to a legacy or platform-local identifier of the same holder, which may not
be recognisable or interoperable outside the onboarding platform; see IR-03 and IR-04 for the
limits on that use.

Standard credential metadata (issuer, issuance time, expiry, status) follows from the chosen VC
format and is documented in Chapter 5 rather than as attributes here. Each Membership Credential
has its own unique identifier.

**DS-specific terminology.** Attributes marked `(*)` below (`id`, `member`, `memberOf`) keep their
names for cross-dataspace interoperability (e.g. with Catena-X) and SHALL NOT be renamed. For
extensibility purposes the JSON Schema definition allows additional properties in the `onboardedBy`
data type definition.

**Mapping from the source attestation description.** Two attribute names in the source document,
*MVP Membership credential — attestation description* v1.0, do not appear in this Rulebook. They
carried a flat string where this Rulebook models the holder as an
[EconomicOperator](https://w3id.org/ebwv#EconomicOperator) object, so the names could not survive
the structure; the information they carried is unchanged and is mapped as follows.

| Source attribute | Carried here by | Note |
|---|---|---|
| `holderIdentifier` | `member.legalIdentifier` (Section 3.2.2) | The stable, EU-level identifier of the holder — for the MVP the EUID from the EUBWOID, which is the value the source document specifies. |
| `holderIdentifierType` | the datatype of that typed literal, e.g. `Euid` | The scheme is carried by the value itself rather than by a companion attribute, so the two cannot drift apart. See Section 4.4. |

A consumer expecting the Catena-X field names therefore needs a rename in its mapping table and
nothing more: no information is lost, and the authoritative identifier of the holder remains a
single, clearly named property. An identifier that is *not* authoritative — a further scheme, or
the reference used by the onboarding platform — is deliberately carried elsewhere, by
`member.identifier` or by `onboardedBy.member.identifier` respectively, so that its status is
evident from the property name rather than from prose. See IR-04, IR-06 and IR-07.

*Sections 3.2 to 4.3 define the attributes and metadata in an encoding-independent manner. Code
lists are in Section 4.4 and integrity rules in Section 4.5. The structured object `onboardedBy` is
defined as a sub-table in Section 3.2; `termsOfUse` is defined in Section 4.1 and `evidence` in
Section 4.2.*

**Schema artefacts.**

| Format | Identifier | Schema artefact | Version | Location |
| --- | --- | --- | --- | --- |
| SD-JWT VC | `vct` `eu.we-build.ds-membership.1` | JSON schema | 0.8.0 | [`data-schemas/sd-jwt/ds-membership-sd-jwt.json`](../../data-schemas/sd-jwt/ds-membership-sd-jwt.json) |
| W3C VCDM | type `VerifiableCredential`, `ElectronicAttestationOfAttributes`; credential subject `Membership`; contexts `https://www.w3.org/ns/credentials/v2`, `https://w3id.org/ebwv/v0.1` | JSON-LD context of the European Business Wallet Vocabulary | v0.1 | <https://w3id.org/ebwv/v0.1> |

The schema artefacts referenced above are normative for encoding. Where this document
and a referenced artefact disagree, the artefact prevails for encoding questions and
this document prevails for semantics, presence and disclosure rules. Each artefact
SHALL be versioned and immutably addressable. Versioning of the artefacts SHALL align
on major releases.

Note on selective disclosure: for SD-JWT VC, whether a claim is selectively
disclosable is stated in the tables below, not in the schema (EW-DM-12-034). No Claim
Selective Disclosure Metadata document is used (EW-DM-12-035).

Supporting, non-normative artefacts: sample payloads for both formats
([`ds-membership-sd-jwt-sample.json`](../../data-schemas/sd-jwt/sample-data/ds-membership-sd-jwt-sample.json),
[`ds-membership-jsonld-sample.json`](../../data-schemas/jsonld/sample-data/ds-membership-jsonld-sample.json)),
and, for the W3C VCDM encoding, a JSON Schema and SHACL shapes described in Section 5.3.2.

### 3.2 Mandatory attributes

Attributes that SHALL be present in every attestation of this type.

The attributes below belong to the object [Membership](https://w3id.org/ebwv#Membership).

| Data identifier | Semantic reference | Definition | Data type | Selectively disclosable | Example value |
| --- | --- | --- | --- | --- | --- |
| `id` (*) | @id | Identifier of the credential subject, as an absolute URI: either a DID or a UUID expressed as a `urn:uuid:` URN. May change, in contrast to `member.legalIdentifier` which is a persistent, stable identifier. Name kept for cross-dataspace interoperability. | URI (DID or `urn:uuid:` URN) | yes | `did:web:example.org:holder` |
| `member` (*) | [member](https://w3id.org/ebwv#member) | The holder, as an economic operator carrying the stable identifier that uniquely identifies it. For the MVP this re-uses the EUID (part of the EUBWOID); scope is legal persons only. Name kept for cross-dataspace interoperability. Object, see table below. | [EconomicOperator](https://w3id.org/ebwv#EconomicOperator) | yes | *see 3.2.2* |
| `memberOf` (*) | [memberOf](https://w3id.org/ebwv#memberOf) | The DSI or dataspace the holder is a member of. Within a DSI/DS all issued membership credentials use the same value. The value is an absolute IRI registered in code list 4.4, matched by exact IRI comparison. Name kept for cross-dataspace interoperability. | URL | yes | `https://agri-x.eu` |
| `role` | [role](https://w3id.org/ebwv#role) | The roles the holder has within the DSI or dataspace. A member may have multiple roles; the set of roles shares the membership lifecycle. Each value is an absolute IRI from code list 4.4. | array of IRIs | yes, per element | `["https://w3id.org/ebwv#DataProvider"]` |
| `onboardedBy` | [onboardedBy](https://w3id.org/ebwv#onboardedBy) | The onboarding through which the holder joined the DSI or dataspace: the platform, the economic operator hosting it, and optionally the holder as that platform knows it. Object, see table below. | [OnboardingDetails](https://w3id.org/ebwv#OnboardingDetails) | yes | *see 3.2.1* |

#### 3.2.1 `onboardedBy` object of type [OnboardingDetails](https://w3id.org/ebwv#OnboardingDetails)

This object describes **the onboarding**: which platform performed it, which legal entity hosts
that platform, and how that platform knows the holder. Example reading: *"DjustConnect, a platform
hosted by ILVO, onboarded farmer XYZ, whom it knows as 012345676789."*

Two identifiers of different subjects appear here and SHALL NOT be confused.
`operator.identifier` belongs to the organisation hosting the platform. `member.identifier` belongs
to **the holder**, as known within this platform, and is subject to IR-06 and IR-07 exactly as
`member.identifier` on the credential subject is. The identification means used to prove the
holder's identity remains `evidence`, at credential level (Section 4.2).

| Data identifier | Semantic reference | Definition | Data type | Optionality | Selectively disclosable | Example value |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | @id | The platform through which the holder was onboarded, identified by an absolute URI, normally a DID. Carried as the identity of this object rather than as an attribute: the vocabulary defines no property for it. | URI (DID) | M | yes | `did:web:djustconnect.be` |
| `platform` | [platform](https://w3id.org/ebwv#platform) | Commercial name of the platform (DSI or onboarding partner). | string | M | yes | `DjustConnect` |
| `operator` | [operator](https://w3id.org/ebwv#operator) | The economic operator hosting and running the platform. Object, see 3.2.2. | [EconomicOperator](https://w3id.org/ebwv#EconomicOperator) | M | yes | *see 3.2.2* |
| `member` | [member](https://w3id.org/ebwv#member) | The holder, as the onboarding platform knows it. Carries only what the platform adds to the credential subject's `member`, normally its own identifier for the same legal person. SHALL be omitted where the platform knows the holder by the identifier already in `member.legalIdentifier`, which is the ordinary case when a DSI issues to one of its own members. Object, see 3.2.2. See IR-06, IR-07. | [EconomicOperator](https://w3id.org/ebwv#EconomicOperator) | O | yes | *see 3.2.2* |

#### 3.2.2 [EconomicOperator](https://w3id.org/ebwv#EconomicOperator) object

Used by `member` (the holder) and by `onboardedBy.operator` (the organisation hosting the
onboarding platform). Identifier values follow the European Business Wallet Vocabulary pattern for
identifiers: a typed literal whose datatype is the identifier scheme. See Section 4.4.

An economic operator MAY be known by more than one identifier scheme, so `identifier` is
repeatable. Only schemes published as individuals by the vocabulary may be used as the datatype:
an unpublished scheme name is not an absolute IRI and **aborts JSON-LD expansion**, taking the
whole credential with it rather than degrading gracefully. Where no published scheme applies, carry
the value as an untyped string (Section 4.4).

| Data identifier | Semantic reference | Definition | Data type | Optionality | Selectively disclosable | Example value |
| --- | --- | --- | --- | --- | --- | --- |
| `legalName` | [legalName](https://w3id.org/ebwv#legalName) | Official legal name of the economic operator. For `member`, see integrity rule IR-02. | string | M | yes | `Farm Example BV` |
| `legalIdentifier` | [legalIdentifier](https://w3id.org/ebwv#legalIdentifier) | The stable, EU-level identifier of the economic operator. Used by `member`: for the MVP the EUID taken from the holder's EUBWOID. Scheme SHALL be `Euid` or `PublicSectorBodyId` (range of the property). | typed literal | M for `member` | yes | `{"@type":"Euid","@value":"BEEUID0123456789"}` |
| `identifier` | [identifier](https://w3id.org/ebwv#identifier) | Further identifiers of the economic operator, in any scheme from code list 4.4. Repeatable: an operator may be known by several schemes at once. Used by `onboardedBy.operator` to identify the organisation hosting the platform, and optionally by `member` to carry identifiers of the holder additional to `legalIdentifier`, which remains the authoritative one (IR-04). | typed literal, repeatable | M for `operator`, O for `member` | yes, per element | `{"@type":"VatId","@value":"BE0848278827"}` |

### 3.3 Optional attributes

Attributes the Provider MAY include at its discretion.

*No optional attributes are defined on the credential subject. The holder's official name is
carried by `member.legalName`, and any further identifier of the holder — including a platform-local
reference with no published scheme — by the repeatable `member.identifier` (both Section 3.2.2). The
identification means used to prove the holder's identity at onboarding is the credential-level
`evidence` metadata (Section 4.2).*

| Data identifier | Semantic reference | Definition | Data type | Selectively disclosable | Example value |
| --- | --- | --- | --- | --- | --- |
| N/A | N/A | N/A | N/A | N/A | N/A |

### 3.4 Conditional attributes

Attributes required only when a stated condition holds. State the condition
explicitly in the definition, not in a footnote.

No conditional attributes are defined for this attestation type.

| Data identifier | Semantic reference | Definition | Condition | Data type | Selectively disclosable | Example value |
| --- | --- | --- | --- | --- | --- | --- |
| N/A | N/A | N/A | N/A | N/A | N/A | N/A |

## 4 Metadata

Metadata describes the attestation rather than its subject. Use the same schema
artefacts referenced in section 3.1.

### 4.1 Mandatory metadata

*Standard VC metadata (issuer, issuance time, expiry, status, credential `id`) is provided by the
chosen VC format and specified per encoding in Chapter 5. This Rulebook defines two additional
mandatory metadata attributes.*

| Data identifier | Semantic reference | Definition | Data type | Example value |
| --- | --- | --- | --- | --- |
| `attestation_legal_category` | [attestationLegalCategory](https://w3id.org/ebwv#attestationLegalCategory) | Indication that the attestation is a non-qualified EAA (per ARB_12). Qualifies the attestation as a whole, not the member, and is therefore carried at credential level rather than in the credential subject. SHALL be `EAA`. See Sections 3.1 and 5.3.1. | [AttestationLegalCategory](https://w3id.org/ebwv#AttestationLegalCategory) | [EAA](https://w3id.org/ebwv#EAA) |
| `termsOfUse`                 | [termsOfUse](https://www.w3.org/2018/credentials#termsOfUse)               | The dataspace governance rulebook the holder has conformed to. Carried at credential level, as W3C VCDM defines `termsOfUse` as a property of the credential rather than of its subject. Object, see 4.1.1. | [GovernanceRulebook](https://w3id.org/ebwv#GovernanceRulebook) | *see 4.1.1* |

**Legal category.** This Rulebook retains the `attestationLegalCategory` attribute.
Section 4.1 of the generic template replaces it with the `category` attribute of
[ETSI TS 119 472-1]. EW-DM-12-029, legacy ARB_25, of ARF version 3.0.0 is a SHALL that
still requires the legal category attribute, so the template and the ARF disagree. The
attribute is left as written and the deviation is recorded for the rulebook quality
assurance group. For the same reason the fixed text of section 4.1 of the template, which
introduces `category` and states that `attestation_legal_category` SHALL NOT be used, is not
reproduced here.

`attestation_legal_category` SHALL NOT be selectively disclosable. The members of `termsOfUse`
SHALL be individually selectively disclosable.

#### 4.1.1 `termsOfUse` object of type [GovernanceRulebook](https://w3id.org/ebwv#GovernanceRulebook)

| Data identifier | Semantic reference | Definition | Data type | Optionality | Example value |
| --- | --- | --- | --- | --- | --- |
| `url`               | N/A                    | Reference to the online dataspace governance rulebook for the given DSI or DS. | string (URI) | M | `https://agri-x.eu/rulebook` |
| `version`           | N/A                    | Version of the online rulebook at the time of acceptance. | string | M | `1.2` |
| `hash`              | N/A                    | SHA-256 hash of the rulebook, for quick comparison. | string (SHA-256 hash) | M | `9f86d081...` |
| `acceptedAt`        | N/A                    | Datetime when the rulebook was accepted. May differ from issuance time in an outbound flow where a credential is issued to an existing member based on a previously completed onboarding flow. | datetime | O | `2026-06-01T10:00:00Z` |

### 4.2 Optional metadata

Includes `cryptographically_bound_to` where section 7.1 records a cryptographic binding
(EW-DM-12-032). Section 7.1 records none, so it is not included.

Elements of `evidence` SHALL be individually selectively disclosable.

| Data identifier | Semantic reference | Definition | Data type | Example value |
| --- | --- | --- | --- | --- |
| `evidence`          | [evidence](https://www.w3.org/2018/credentials#evidence)          | The identification means used to prove the identity of the holder during the initial onboarding process. Metadata about the issuance, carried at credential level. Object or array of objects, see 4.2.1. | array of objects   | *see 4.2.1*       |

#### 4.2.1 `evidence` attribute

Each `evidence` entry records one identification means presented by, or verified for, the holder
during the initial onboarding process — for example the VAT identifier checked in a paper-based
onboarding flow. `evidence` is optional; where the onboarding platform holds such a record, the
issuer SHOULD include it.

| Data identifier | Semantic reference | Definition | Data type | Optionality | Example value |
| --- | --- | --- | --- | --- | --- |
| `type`              | @type                                          | The evidence entry describes the holder as an economic operator identified by the means used at onboarding. SHALL be `EconomicOperator`; see Section 5.3.1 for why this declaration is required. | class name     | M in W3C VCDM; omitted in SD-JWT VC | `EconomicOperator`                          |
| `identifier`        | [identifier](https://w3id.org/ebwv#identifier) | The identification means: the identifier by which the holder's identity was proven, as a typed literal whose datatype is the identifier scheme. Where no scheme from code list 4.4 applies, an untyped string. | typed literal  | M               | `{"@type":"VatId","@value":"BE0123456789"}` |

`evidence` describes the **holder**. It SHALL NOT be used to carry an identifier of the onboarding
platform or of its operator; those belong in `onboardedBy` (Section 3.2.1). See IR-03 and IR-04.


### 4.3 Conditional metadata

| Data identifier | Semantic reference | Definition | Condition | Data type | Example value |
| --- | --- | --- | --- | --- | --- |
| N/A | N/A | N/A | N/A | N/A | N/A |

### 4.4 Code lists

Controlled vocabularies, enumerations and value sets needed to interpret attributes
consistently. Reference an external vocabulary wherever one exists rather than
defining a local list.

The following code lists apply to attributes defined in Section 3. Lists are kept fit-for-pilot:
they cover the minimal set needed by the three participating DSIs and are not exhaustive.

**`memberOf`** — fixes the DSI or dataspace the holder is a member of. The value is agreed at the
governance level of the DSI or dataspace itself and registered in the code list below, as a URL
under that DSI's or dataspace's own domain. Uniqueness therefore rests on domain ownership, and two
DSIs cannot collide by independently choosing the same label.

The [memberOf](https://w3id.org/ebwv#memberOf) property is typed `@id` in the European Business
Wallet Vocabulary, so the value is an **absolute IRI** and expands to a node reference,
`{"@id": "https://agri-x.eu"}`. A Relying Party matches it by exact IRI comparison. The value need
not dereference to anything, and a Relying Party SHALL NOT depend on it resolving. A relative value
SHALL NOT be used: it would be resolved against the document base, so the same credential would
yield different IRIs depending on where it was retrieved from. A new DSI or dataspace SHALL
register its IRI in this code list before issuing.

| Field | Allowed values or vocabulary | Meaning | Source | Extensible |
| --- | --- | --- | --- | --- |
| `memberOf` | `https://agri-x.eu` | The common agriculture dataspace (federation level). | WE BUILD SC2 use case | yes, by registration in this list |
| `memberOf` | `https://dataspace.dih-agrifood.com` | DSI operated by ITC. | WE BUILD SC2 use case | yes, by registration in this list |
| `memberOf` | `https://djustconnect.be` | DSI operated by ILVO. | WE BUILD SC2 use case | yes, by registration in this list |
| `memberOf` | `https://www.dataspace.fi` | DSI operated by DataSpace Europe Oy. | WE BUILD SC2 use case | yes, by registration in this list |

**`role`** — roles a member can have. A member may have multiple roles in one credential. Based on
the common roles agreed across the piloting DSIs, treating Agri-X as a federation of DSIs.

The [role](https://w3id.org/ebwv#role) property is typed `@id` in the European Business Wallet
Vocabulary, so each value is an **absolute IRI** and expands to a node reference. The values below
are the `DataSpaceRole` individuals published in that vocabulary, under the
`https://w3id.org/ebwv#` namespace. A relative value such as `DataRightsHolder` SHALL NOT be used:
it would be resolved against the document base, so the same credential would yield different role
IRIs depending on where it was retrieved from.

| Field | Allowed values or vocabulary | Meaning | Source | Extensible |
| --- | --- | --- | --- | --- |
| `role` | `https://w3id.org/ebwv#DataRightsHolder` | Owns the rights to the data (e.g. farmers) and can consent to data being shared from a data provider to a data consumer. | WE BUILD SC2 use case | yes, see below |
| `role` | `https://w3id.org/ebwv#DataProvider` | Partner that enables sharing data, e.g. via an API. | WE BUILD SC2 use case | yes, see below |
| `role` | `https://w3id.org/ebwv#DataConsumer` | Partner that wants to use data, e.g. by calling an API. | WE BUILD SC2 use case | yes, see below |
| `role` | `https://w3id.org/ebwv#Operator` | Partner providing DSSC building-block services (identity management, consent management, logging, …). | WE BUILD SC2 use case (custom role part of DADS) | yes, see below |
| `role` | `https://w3id.org/ebwv#OnboardingServiceProvider` | Partner that onboards members into Agri-X; may be a DSI or another technology partner. | WE BUILD SC2 use case (role part of Catena-X) | yes, see below |

Because values are IRIs, a DSI MAY mint an additional role under a namespace it owns without any
change to this Rulebook, to the JSON Schema, or to the vocabulary context, and a Relying Party MAY
trust roles by namespace prefix rather than enumerating each value. Roles minted outside
`https://w3id.org/ebwv#` are governed by the minting DSI's own trust framework; see Section 10. New
roles intended for common use across the piloting DSIs SHOULD still be published as `DataSpaceRole`
individuals by the WE BUILD Semantics work group and registered here.

**Identifier schemes** — the datatype of an identifier typed literal, wherever one appears:
`member.legalIdentifier`, `onboardedBy.operator.identifier` and `evidence.identifier`. The
European Business Wallet Vocabulary publishes these as named individuals used as datatypes, in the
pattern `{"@type": "VatId", "@value": "…"}`.

| Field | Allowed values or vocabulary | Meaning | Source | Extensible |
| --- | --- | --- | --- | --- |
| `@type` | `Euid` | The unique identifier attributed in accordance with Article 9 of EBW, taken from the holder's EUBWOID. The expected scheme of `member.legalIdentifier` in the MVP. In range of `legalIdentifier`. | [European Business Wallet Vocabulary v0.1], `rb-ebwoid` | yes, as the vocabulary publishes further schemes |
| `@type` | `PublicSectorBodyId` | Identifier of a public sector body. In range of `legalIdentifier`. | [European Business Wallet Vocabulary v0.1] | yes, as the vocabulary publishes further schemes |
| `@type` | `KmgMid` | Unique farm id used in Slovenia, issued by the Ministry of Agriculture. Used by the DADS platform to identify holders locally. | [European Business Wallet Vocabulary v0.1] | yes, as the vocabulary publishes further schemes |
| `@type` | `VatId` | VAT identifier. Used by DjustConnect and Tritom as an identification means during onboarding. | [European Business Wallet Vocabulary v0.1] | yes, as the vocabulary publishes further schemes |
| `@type` | `Lei`, `Eori`, `Tin`, `Iban`, `Bic`, `PeppolId`, `GlobalLocationNumber`, `ClearingNumber`, `Excise` | Further schemes published by the vocabulary, available where applicable. Not used in the MVP. | [European Business Wallet Vocabulary v0.1] | yes, as the vocabulary publishes further schemes |

*A purely platform-specific identifier, one whose scheme is meaningful only inside the issuing
platform, still has no individual in the vocabulary. Such a value SHALL be carried as an untyped
string — `"identifier": "DC-2026-004711"` — which is valid and expands correctly but does not
record the scheme. Publishing a generic `PlatformSpecific` scheme would remove the need for it; see
version history entry 10.*

*A platform-local identifier of the holder whose scheme has no published individual is carried as an
untyped string in `member.identifier` (Section 3.2.2). It is then interpreted by reference to the
onboarding platform named in `onboardedBy`: a Relying Party that knows the platform knows which
identifier that platform issues.*

A common code list distinguishing Legal Person from Natural Person identifiers is being prepared by
the WE BUILD Semantics work group. It is not required for this version: the MVP scenario pilots
legal persons only. Values will be added once provided.

### 4.5 Integrity rules

Consistency rules not captured by the schema alone: cross-field dependencies,
temporal consistency, mutual exclusivity, conditional combinations.

| Rule ID | Rule statement | Why it exists | Where enforced | Behaviour on failure |
| --- | --- | --- | --- | --- |
| `IR-01` | If `termsOfUse.acceptedAt` is present, its value SHALL be a datetime less than or equal to the issuance datetime of the credential. | Acceptance of the rulebook cannot logically occur after the credential was issued; supports outbound flows where acceptance happened during an earlier onboarding. | Issuer business rules, schema validation, and verifier business validation. | Issuer SHALL reject the value; verifier SHALL treat `termsOfUse` as invalid. |
| `IR-02` | If the member is a Legal Person, `member.legalName` SHOULD carry the official name as registered.                                   | Improves readability and identification of legal-person holders. | Issuer business rules. | Issuer SHOULD populate `member.legalName`; verifier MAY warn if absent. |
| `IR-03` | Every `evidence` entry SHALL record an identification means by which the identity of the holder — the legal person identified by `member` — was proven during the initial onboarding process. `evidence` SHALL NOT carry an identifier of the onboarding platform or of its operator. | Evidence is about proofing the holder. Recording the platform operator's own identifier there would misidentify the holder, which is the failure this separation exists to prevent. | Issuer business rules and verifier business validation. | Issuer SHALL NOT issue the credential; verifier SHALL treat the credential as inconsistent. |
| `IR-04` | A Relying Party SHALL NOT treat an `evidence` identifier as an authoritative identifier of the holder. `member.legalIdentifier` is authoritative. | An identification means may be a legacy or platform-local identifier with no recognition or interoperability outside the onboarding platform, and it records how proofing was done rather than who the holder is at EU level. | Verifier business validation. | Verifier MAY use the value only to reconcile the holder against its own legacy records, never as the basis of identification. |
| `IR-05` | `role` and `memberOf` values SHALL be absolute IRIs. A Relying Party SHALL match them by exact IRI comparison against code list 4.4, or for `role` by namespace prefix where its policy permits, and SHALL ignore any value it does not recognise. | A relative value is resolved against the document base, so the same credential would yield different IRIs depending on where it was retrieved from. Inferring authorisation from an unrecognised value would grant access on an unverifiable claim. | Verifier business validation. | Verifier SHALL disregard the unrecognised value and SHALL NOT treat it as conferring any role or membership. |
| `IR-06` | A value of `member.identifier`, whether on the credential subject or on `onboardedBy`, SHALL NOT repeat the value of `member.legalIdentifier`. | All of them describe the same holder, so repeating the authoritative identifier under a further property adds no information and risks the values drifting apart. | Issuer business rules and verifier business validation. | Issuer SHALL NOT issue the credential; verifier SHALL treat the credential as inconsistent. |
| `IR-07` | A Relying Party SHALL NOT treat a value of `member.identifier`, on the credential subject or on `onboardedBy`, as an authoritative identifier of the holder. `member.legalIdentifier` is authoritative. | A further identifier may be a legacy or platform-local reference with no recognition or interoperability outside the platform that issued it. | Verifier business validation. | Verifier MAY use the value only to reconcile the holder against its own records, never as the basis of identification. |

## 5 Formats

This chapter identifies the formats in which this attestation is issued. The
encoding detail lives in the schema artefacts referenced in section 3.1, and the
rules for using each format are in chapters 7 and 9.

| Format | Supported | Identifier | Specification | Notes |
| --- | --- | --- | --- | --- |
| ISO/IEC 18013-5 mdoc | no |  | [ISO/IEC 18013-5] | Not defined; proximity presentation is not in scope (EW-DM-12-003), see section 5.2 |
| SD-JWT VC | yes | `vct` `eu.we-build.ds-membership.1` | [SD-JWT VC], [HAIP] | SHALL follow the HAIP profile (EW-DM-12-002); additional flow that MAY be piloted, see section 5.1 |
| W3C VCDM | yes | type `VerifiableCredential`, `ElectronicAttestationOfAttributes`; contexts `https://www.w3.org/ns/credentials/v2`, `https://w3id.org/ebwv/v0.1` | [W3C VCDM v2.0] | Permitted for non-qualified EAA only (EW-DM-12-001); primary format for the MVP, see section 5.3 |

A PID SHALL be issued in both the ISO/IEC 18013-5 and SD-JWT VC formats. For other
attestation types, at least one format SHALL be marked as supported. Identifiers
SHALL be unique to this attestation type (EW-DM-12-006).

A Provider SHALL offer the W3C VCDM format and MAY additionally offer the SD-JWT VC
format.

### 5.1 SD-JWT VC-based encoding

*Considered as an additional flow (not the primary format for the MVP).* The Membership Credential
MAY additionally be piloted as an SD-JWT VC. If issued in this format, attestations
SHALL comply with the 'SD-JWT VCs' profile specified in [HAIP] (ARB_01b). This Rulebook follows
the catalog baseline of [HAIP] draft-03 and [SD-JWT VC] draft-ietf-oauth-sd-jwt-vc-09.

**Verifiable Credential Type (`vct`):** `eu.we-build.ds-membership.1`

The issued SD-JWT VC SHALL use the JOSE `typ` header value required by [SD-JWT VC]. For draft -09,
this value is `dc+sd-jwt`.

#### 5.1.1 IANA-registered and standard JWT / SD-JWT VC claims

The following claims are standard JWT or SD-JWT VC claims.

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Reference / Notes** | **Disclosable** |
| --- | --- | --- | --- | --- |
| `iss` | `iss` | string (HTTPS URL) | Issuer identifier. | MUST NOT |
| `iat` | `iat` | NumericDate | Issued-at timestamp. | MUST NOT |
| `nbf` | `nbf` | NumericDate | Not-before timestamp, where used. | MUST NOT |
| `exp` | `exp` | NumericDate | Expiration timestamp. | MUST NOT |
| `jti` | `jti` | string | Unique credential instance identifier. | MUST NOT |
| `vct` | `vct` | string | SHALL be `eu.we-build.ds-membership.1`. | MUST NOT |
| `status` | `status` | JSON object | Status-list revocation information. See Section 5.1.3. | MUST NOT |
| `cnf` | `cnf` | JSON object | Holder binding confirmation claim, where used. | MUST NOT |

#### 5.1.2 Private names specific to the Membership Credential

The following private claims map to the attributes defined in Chapter 3. Claim names are identical
to the Chapter 3 data identifiers; the two SHALL be kept in step.

| **Data Identifier**               | **Attribute identifier**          | **Encoding format** | **Reference / Notes** | **Optionality** | **Disclosable** |
|-----------------------------------|-----------------------------------|---------------------|-----------------------|-----------------|-----------------|
| `attestationLegalCategory`        | `attestation_legal_category`      | string | SHALL be `EAA`. Credential-level metadata, see Section 4.1. | M | MUST NOT |
| `id`                              | `id`                              | string (URI) | Identifier of the credential subject: a DID or a `urn:uuid:` URN. | M | MUST |
| `member`                          | `member`                          | JSON object | The holder as an economic operator. See Section 3.2.2. | M | MUST |
| `member.legalName`                | `member.legalName`                | string | Official name of the holder. See IR-02. | M | MUST |
| `member.legalIdentifier`          | `member.legalIdentifier`          | JSON object | Stable, EU-level identifier of the holder. See Section 3.2.2. | M | MUST |
| `member.legalIdentifier.scheme`   | `member.legalIdentifier.scheme`   | string | Identifier scheme; `Euid` in the MVP. See code list 4.4. | M | MUST |
| `member.legalIdentifier.value`    | `member.legalIdentifier.value`    | string | Identifier value. For the MVP this re-uses the EUID from the EUBWOID. | M | MUST |
| `member.identifier`               | `member.identifier`               | array of JSON objects | Further identifiers of the holder, each as `scheme` and `value`. Repeatable; `member.legalIdentifier` remains authoritative. See Section 3.2.2. | O | MUST |
| `memberOf`                        | `memberOf`                        | string (absolute IRI, see code list 4.4) | DSI or dataspace membership value. | M | MUST |
| `role`                            | `role`                            | array of strings (absolute IRIs, see code list 4.4) | Non-empty array of role values. | M | MUST (per element) |
| `termsOfUse`                      | `termsOfUse`                      | JSON object | Dataspace governance rulebook information. See Section 4.1.1. | M | MUST |
| `termsOfUse.url`                  | `termsOfUse.url`                  | string (URI) | Reference to the online dataspace governance rulebook. | M | MUST |
| `termsOfUse.version`              | `termsOfUse.version`              | string | Version of the online rulebook at the time of acceptance. | M | MUST |
| `termsOfUse.hash`                 | `termsOfUse.hash`                 | string (SHA-256 hash) | SHA-256 hash of the rulebook, represented as 64 hexadecimal characters. | M | MUST |
| `termsOfUse.acceptedAt`           | `termsOfUse.acceptedAt`           | string (date-time) | Datetime when the rulebook was accepted, where present. See IR-01. | O | MUST |
| `onboardedBy`                     | `onboardedBy`                     | JSON object | The onboarding through which the holder joined. See Section 3.2.1. | M | MUST |
| `onboardedBy.id`                  | `onboardedBy.id`                  | string (URI) | The onboarding platform, identified by an absolute URI, normally a DID. | M | MUST |
| `onboardedBy.platform`            | `onboardedBy.platform`            | string | Commercial name of the onboarding platform. | M | MUST |
| `onboardedBy.operator`            | `onboardedBy.operator`            | JSON object | Economic operator hosting the platform. See Section 3.2.2. | M | MUST |
| `onboardedBy.operator.legalName`  | `onboardedBy.operator.legalName`  | string | Legal name of the organisation hosting the platform. | M | MUST |
| `onboardedBy.operator.identifier` | `onboardedBy.operator.identifier` | JSON object | Identifier of that organisation, as `scheme` and `value`. See Section 3.2.2. | M | MUST |
| `onboardedBy.member`              | `onboardedBy.member`              | JSON object | The holder as the onboarding platform knows it. See Section 3.2.1 and IR-06, IR-07. | O | MUST |
| `evidence`                        | `evidence`                        | array of JSON objects | Identification means used to prove the holder's identity during initial onboarding. Credential-level metadata, see Section 4.2.1 and IR-03, IR-04. | O | MUST |
| `evidence[].identifier`           | `evidence[].identifier`           | JSON object | The identification means, as `scheme` and `value`. Where no scheme from code list 4.4 applies, a plain string. | M within an entry | MUST |

**Identifier representation in this encoding.** SD-JWT VC is not JSON-LD, so an identifier is
encoded as a plain JSON object with `scheme` and `value` members — for example
`{"scheme": "VatId", "value": "BE0123456789"}`. This is the SD-JWT VC form of the typed literal
described in Section 3.2.2; the W3C VCDM encoding uses the JSON-LD form
`{"@type": "VatId", "@value": "BE0123456789"}` (Section 5.3). Both carry the same scheme and value,
and the scheme is drawn from the same code list 4.4. Where no published scheme applies, the
identifier is a plain string in both encodings.

**Reading the Disclosable column.** `MUST` means the issuer SHALL make the claim selectively
disclosable; `MAY` means the issuer MAY do so; `MUST NOT` means the claim SHALL remain in the
always-visible signed payload.

Disclosability is independent of whether an attribute is mandatory in the credential. Optionality
governs what the *issuer* SHALL include when issuing; disclosability governs what the *holder* may
withhold when presenting. All subject attributes are therefore selectively disclosable, including
the mandatory ones: a Relying Party enforces the set it needs through its presentation request and
rejects a presentation that omits any of them, so disclosability costs the Relying Party nothing
while leaving the holder in control of everything beyond that set. The claims marked `MUST NOT` are
exactly those required to process or validate the credential itself, which no presentation can
omit.

**Granularity for structured attributes.** Where an attribute is an object or an array, the
following applies:

* Members of `termsOfUse`, `member`, `onboardedBy` and their nested objects SHALL be individually
  disclosable (structured/recursive selective disclosure), so that a holder can present, for
  example, `termsOfUse.hash` and `termsOfUse.version` without disclosing
  `termsOfUse.acceptedAt`, which is onboarding-date metadata a Relying Party rarely needs.
* Elements of `role` SHALL be individually disclosable, so that a holder with several roles can
  present only the role or roles the Relying Party's policy requires.
* Elements of `evidence` SHALL be individually disclosable. Evidence reveals how the holder was
  identity-proofed and carries an identifier that may correlate the holder across services, so a
  holder SHOULD be able to withhold it entirely or disclose a single entry.

Note that the granularity, not the requirement, is what depends on the data type: `MUST` applies
uniformly to `memberOf`, `role` and `termsOfUse` alike, since all three are part of the atomic set
a Relying Party uses to decide whether to accept the credential. The distinction between a string,
an array of strings and an object determines only *how* selective disclosure is applied to each.

#### 5.1.3 Status Claim

The Membership Credential is revocable (Chapter 8). Therefore, an SD-JWT VC-compliant
Membership Credential SHALL include a `status` claim unless a future profile explicitly
defines a short-lived, non-revocable variant.

The `status` claim SHALL use the status-list mechanism used by the other SD-JWT VC rulebooks in
this catalog. It SHALL be a JSON object with the following members:

* `type` (string): SHALL be `"status-list"`.
* `status_list_credential` (string, URI): URI of the Status List Credential that contains the
  status bitstring.
* `status_list_index` (integer, >= 0): zero-based index into the status list bitstring for this
  credential.
* `status_purpose` (string): SHALL be `"revocation"` for this attestation.

Example:

```json
{
  "status": {
    "type": "status-list",
    "status_list_credential": "https://djustconnect.be/status/membership/1",
    "status_list_index": 42,
    "status_purpose": "revocation"
  }
}
```

#### 5.1.4 Example Payload

The following non-normative example shows the JWT claim set before SD-JWT processing.

```json
{
  "iss": "https://djustconnect.be",
  "iat": 1782205200,
  "nbf": 1782205200,
  "exp": 1813741200,
  "jti": "urn:uuid:8d6f0e3c-1c2a-4e2b-9f1a-1234567890ab",
  "vct": "eu.we-build.ds-membership.1",
  "attestation_legal_category": "EAA",
  "id": "did:web:example.com:participant:123",
  "member": {
    "legalName": "Farm Example BV",
    "legalIdentifier": {
      "scheme": "Euid",
      "value": "BEEUID0123456789"
    },
    "identifier": [
      { "scheme": "VatId", "value": "BE0123456789" }
    ]
  },
  "memberOf": "https://agri-x.eu",
  "role": ["https://w3id.org/ebwv#DataRightsHolder", "https://w3id.org/ebwv#DataProvider"],
  "termsOfUse": {
    "url": "https://agri-x.eu/rulebook",
    "version": "1.2",
    "hash": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
    "acceptedAt": "2026-06-20T14:30:00Z"
  },
  "onboardedBy": {
    "id": "did:web:djustconnect.be",
    "platform": "DjustConnect",
    "operator": {
      "legalName": "Instituut voor Landbouw-, Visserij- en Voedingsonderzoek (ILVO)",
      "identifier": {
        "scheme": "VatId",
        "value": "BE0848278827"
      }
    },
    "member": {
      "identifier": "DC-2026-004711"
    }
  },
  "evidence": [
    {
      "identifier": {
        "scheme": "VatId",
        "value": "BE0123456789"
      }
    }
  ],
  "status": {
    "type": "status-list",
    "status_list_credential": "https://djustconnect.be/status/membership/1",
    "status_list_index": 42,
    "status_purpose": "revocation"
  },
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

Note the distinct roles of the identifiers. `member.legalIdentifier` is the holder's authoritative
EU-level identifier, its EUID; `member.identifier` carries a further identifier of the same holder,
its VAT-ID. `onboardedBy.operator.identifier` is the VAT-ID of ILVO, the organisation hosting the
platform, not of the holder. `evidence[0].identifier` is the identification means by which the
holder's identity was proven at onboarding. `onboardedBy.member.identifier`, `DC-2026-004711`, is
DjustConnect's own reference for the same holder: a platform-local value whose scheme has no
published individual, so it is carried as an untyped string rather than as a typed literal.

The SD-JWT VC JSON Schema and sample payload are published at:

* `data-schemas/sd-jwt/ds-membership-sd-jwt.json`
* `data-schemas/sd-jwt/sample-data/ds-membership-sd-jwt-sample.json`

### 5.2 ISO/IEC 18013-5-compliant encoding

*Not applicable for this version.* The Membership Credential is used in online onboarding flows;
no proximity / offline presentation requirement applies (ARB_02). The primary
format is W3C VCDM (JSON-LD), see Section 5.3, with SD-JWT VC considered as an additional flow
(Section 5.1). No ISO/IEC 18013-5 mdoc document type is defined.

### 5.3 W3C Verifiable Credentials Data Model-based encoding

**This is the primary format for the MVP.** The Membership Credential is a non-qualified EAA, which
is the only legal category permitted to use the W3C VCDM format (ARB_01a). W3C VCDM (JSON-LD) is
chosen for semantic interoperability with the dataspaces domain and because it supports selective
disclosure via ZKP.

The credential subject carries the attributes defined in Chapter 3. Standard VCDM metadata is used
for the credential envelope: `issuer`, `validFrom`, `validUntil`, `credentialStatus`, and the
credential `id` (unique per credential).
The credential subject is modeled by the [Membership](https://w3id.org/ebwv#Membership) class 

**`evidence` is credential-level, not part of the credential subject.** The W3C VCDM v2 context
defines [evidence](https://www.w3.org/2018/credentials#evidence) inside the type-scoped context of
`VerifiableCredential`. It is therefore only defined as a member of the credential itself. Placing
it inside `credentialSubject`, whose type is `Membership`, leaves the term undefined; since the VCDM
v2 context is `@protected` and sets no `@vocab`, that is an expansion failure rather than a silent
omission. This placement is also the semantically correct one: evidence records how the issuer
verified the holder's identity, which is a statement about the issuance, not an attribute of the
subject.

`evidence` is optional, but where the onboarding platform holds a record of the identification
means used, the issuer SHOULD include it: it is what allows a Relying Party operating a legacy
system to reconcile the holder against its existing records. It SHALL NOT be confused with
`onboardedBy.operator.identifier`, which identifies the organisation hosting the platform. See
IR-03 and IR-04.


**Illustrative example (informative):**

```json
{
  "@context": [
    "https://www.w3.org/ns/credentials/v2",
    "https://w3id.org/ebwv/v0.1"
  ],
  "type": ["VerifiableCredential","ElectronicAttestationOfAttributes"],
  "id": "urn:uuid:8d6f0e3c-1c2a-4e2b-9f1a-1234567890ab",
  "issuer": "did:web:djustconnect.be",
  "validFrom": "2026-06-23T09:00:00Z",
  "validUntil": "2027-06-23T09:00:00Z",
  "attestationLegalCategory": "EAA",
  "credentialStatus": {
    "id": "https://djustconnect.be/status/membership/1#42",
    "type": "BitstringStatusListEntry",
    "statusPurpose": "revocation",
    "statusListIndex": "42",
    "statusListCredential": "https://djustconnect.be/status/membership/1"
  },
  "evidence": [
    {
      "type": "EconomicOperator",
      "identifier": { "@type": "VatId", "@value": "BE0123456789" }
    }
  ],
  "termsOfUse": {
    "type": "GovernanceRulebook",
    "url": "https://agri-x.eu/rulebook",
    "version": "1.2",
    "hash": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
    "acceptedAt": "2026-06-20T14:30:00Z"
  },
  "credentialSubject": {
    "id": "did:web:example:org:holder",
    "type": "Membership",
    "member": {
      "type": "EconomicOperator",
      "legalName": "Farm Example BV",
      "legalIdentifier": { "@type": "Euid", "@value": "BEEUID0123456789" },
      "identifier": [
        { "@type": "VatId", "@value": "BE0123456789" }
      ]
    },
    "memberOf": "https://agri-x.eu",
    "role": ["https://w3id.org/ebwv#DataRightsHolder", "https://w3id.org/ebwv#DataProvider"],
    "onboardedBy": {
      "id": "did:web:djustconnect.be",
      "type": "OnboardingDetails",
      "platform": "DjustConnect",
      "operator": {
        "id": "did:web:example:org:onboarding-operator",
        "type": "EconomicOperator",
        "legalName": "Instituut voor Landbouw-, Visserij- en Voedingsonderzoek (ILVO)",
        "identifier": { "@type": "VatId", "@value": "BE0848278827" }
      },
      "member": {
        "type": "EconomicOperator",
        "identifier": "DC-2026-004711"
      }
    }
  }
}
```

This example reads: *"DjustConnect, a platform hosted by ILVO, onboarded Farm Example BV — proven
during onboarding by VAT-ID BE0123456789 and identified at EU level by EUID BEEUID0123456789 — into
Agri-X as a Data Rights Holder and Data Provider, where DjustConnect knows it as
DC-2026-004711."* Note which subject each identifier belongs to: the VAT-ID under
`operator.identifier` is ILVO's; the VAT-ID under `evidence` is the identification means used for
the holder; and `onboardedBy.member.identifier` is the platform's own reference for that same
holder, untyped because its scheme has no published individual. Note that `onboardedBy.member`
carries no `legalName`: the holder's name is already stated once, on the credential subject's
`member`, and the onboarding object repeats nothing it does not change.

Expanding this example makes three things explicit. `role` and `memberOf` become **node
references** — `{"@id": "https://w3id.org/ebwv#DataProvider"}`, `{"@id": "https://agri-x.eu"}` —
because the vocabulary types both properties `@id` (Section 4.4). This is why their values are
absolute IRIs: a relative value would be resolved against the document base, producing a different
IRI for every location the credential is served from. Identifiers expand as **typed literals**
carrying their scheme as the datatype IRI, for example
`{"@value": "BE0123456789", "@type": "https://w3id.org/ebwv#VatId"}`. And
`attestationLegalCategory` expands to a node reference, `{"@id": "https://w3id.org/ebwv#EAA"}`,
because the vocabulary types it `@vocab`. Section 5.3.1 sets out the type declarations this
depends on.

#### 5.3.1 Type declarations required for expansion

The European Business Wallet Vocabulary context defines almost all of its properties inside
**type-scoped contexts**, not at the top level. Only `description`, `issuer`, `name` and
`termsOfUse` are defined globally. A property is therefore undefined — and, since the context sets
no `@vocab`, **silently dropped on expansion** — unless the enclosing object declares the type that
scopes it. Issuers SHALL declare the following types, and verifiers SHOULD reject a credential in
which an expected attribute does not survive expansion:

| Object | `type` that SHALL be declared | Properties it brings into scope |
|---|---|---|
| the credential | `VerifiableCredential` and `ElectronicAttestationOfAttributes` | `attestationLegalCategory`; `evidence` and the other VCDM envelope terms come from `VerifiableCredential` |
| `credentialSubject` | `Membership` | `member`, `memberOf`, `role`, `onboardedBy` |
| `credentialSubject.member`, `onboardedBy.operator`, `onboardedBy.member`, each `evidence` entry | `EconomicOperator` | `legalName`, `legalIdentifier`, `identifier` |
| `credentialSubject.onboardedBy` | `OnboardingDetails` | `platform`, `operator`, `member` |
| `termsOfUse` (credential level) | `GovernanceRulebook` | `url`, `version`, `hash`, `acceptedAt` |

Three consequences worth stating plainly:

* **`ElectronicAttestationOfAttributes` SHALL appear in the credential-level `type`.** It is what
  brings `attestationLegalCategory` into scope; without it the attribute required by Section 3.1 is
  dropped on expansion. The vocabulary types that property `@type: @vocab` with a nested context
  mapping `EAA`, `QEAA` and `Pub-EAA` to their individuals, so the value expands to a node
  reference — `{"@id": "https://w3id.org/ebwv#EAA"}` — rather than a string literal. That nested
  context also sets `"@vocab": "ebwv:INVALID_VALUE:"`, so a value outside the three published
  categories expands to a visibly invalid IRI instead of being silently dropped.

* **`Membership` types the credential subject, not the credential.** The credential-level `type`
  is `["VerifiableCredential", "ElectronicAttestationOfAttributes"]`, neither of which is
  `Membership`. `Membership` is declared a subclass of `CredentialSubject` in the
  vocabulary, and putting it in the credential-level `type` array leaves every Membership property
  undefined inside `credentialSubject`, so `member`, `memberOf`, `role` and `onboardedBy` are all
  dropped on expansion without any error being raised.
* **Each `evidence` entry is typed `EconomicOperator`.** The `identifier` property is scoped to that
  type, and the entry does describe the holder as an economic operator identified by the means used
  at onboarding, so the typing is both necessary and semantically correct. It also satisfies the
  domain of [identifier](https://w3id.org/ebwv#identifier).

**Coverage.** Every attribute defined by this Rulebook now has a property term in the European
Business Wallet Vocabulary context, and the illustrative example in Section 5.3 expands without
loss. This was verified against the context published on 2 September 2026.

Because that context sets no `@vocab`, an attribute with no term is **silently dropped on
expansion** rather than raising an error. Issuers and verifiers SHOULD therefore treat a successful
expansion as something to check rather than assume: a Relying Party SHALL NOT infer the absence of
an attribute from an expanded document alone without confirming that its context set defines the
corresponding term.

*Proof type: an EU-approved Data Integrity proof / VC-JOSE-COSE securing mechanism SHALL be used.
[PROOF TYPE TO BE FIXED once the WE BUILD profile selects it; e.g. a Data Integrity ECDSA proof to
support ZKP-based selective disclosure.]*

#### 5.3.2 Semantic verification

A JSON-LD credential can be validated at two levels: the compacted JSON document as it is
transmitted, and the RDF graph it expands to. Only the second captures what the credential means.
This Rulebook publishes a supporting, non-normative artefact for each level:

* [`ds-membership-jsonld.schema.json`](../../data-schemas/jsonld/ds-membership-jsonld.schema.json), a JSON
  Schema for the compacted form;
* [`../../data-schemas/jsonld/ds-membership-shacl.ttl`](../../data-schemas/jsonld/ds-membership-shacl.ttl), SHACL Core shapes
  for the expanded graph, with the companion
  [`../../data-schemas/jsonld/ds-membership-shacl-sparql.ttl`](../../data-schemas/jsonld/ds-membership-shacl-sparql.ttl) for
  the one rule that needs SHACL-SPARQL (IR-06).

The illustrative example in Section 5.3 conforms to both.

**Limits of JSON Schema.** JSON Schema checks the shape of a JSON document; it does no JSON-LD
processing. In particular:

* it cannot detect a term that is **silently dropped on expansion** (Section 5.3.1). A credential
  whose `credentialSubject` lacks the `Membership` type still has every expected key in its JSON,
  and passes, although `member`, `memberOf`, `role` and `onboardedBy` carry no meaning;
* it checks one serialisation of the data, not the data. The same credential can be compacted in
  more than one way — a single role as a scalar or an array, `@type` or its alias `type`, an
  identifier scheme as a short name or a full IRI — and every variant has to be enumerated in the
  schema;
* it cannot compare values held in different properties, so it cannot check IR-01
  (`termsOfUse.acceptedAt` not after `validFrom`), that `validUntil` is later than `validFrom`, or
  IR-06 (`member.identifier` not repeating `member.legalIdentifier`);
* it has a single severity: a value missing from an open code list either fails the credential or is
  not checked at all.

**Advantages of SHACL.** SHACL validates the graph produced by JSON-LD expansion, so it checks
what a Relying Party actually receives once the contexts are applied:

* a dropped term is detected as a missing value, because SHACL sees only what survived expansion;
* the result does not depend on how the credential was compacted, and the same shapes apply to any
  RDF serialisation of the credential;
* constraints are stated over vocabulary IRIs (`ebwv:role`, `ebwv:EAA`) and RDF datatypes
  (`ebwv:VatId`), the terms the Rulebook defines in Chapters 3 and 4;
* SHACL Core compares properties (`sh:lessThan`, `sh:lessThanOrEquals`), including along a path
  through nested objects, and SHACL-SPARQL covers rules beyond that;
* `sh:Warning` expresses advisory checks, used here for IR-05: a `role` or `memberOf` value that is
  not registered in code list 4.4 is reported, not rejected.

**Example.** The following excerpt of the credential shape checks the mandatory legal category of
Section 4.1 and the integrity rule IR-01. The first holds only if `attestationLegalCategory`
survived expansion. Where `ElectronicAttestationOfAttributes` is missing from the credential-level
`type`, the attribute is dropped; JSON Schema still sees the key, whereas the shapes reject the
credential, because the shape for the credential subject checks the type of the enclosing
credential. The second constraint compares a value inside `termsOfUse` with one on the credential,
which JSON Schema cannot express.

```turtle
dsm:MembershipCredentialShape
    a sh:NodeShape ;
    sh:targetClass ebwv:ElectronicAttestationOfAttributes ;

    # Section 4.1 - mandatory metadata
    sh:property [
        sh:path ebwv:attestationLegalCategory ;
        sh:minCount 1 ; sh:maxCount 1 ;
        sh:nodeKind sh:IRI ;
        sh:hasValue ebwv:EAA ;
    ] ;

    # IR-01, as a SHACL Core comparison over a sequence path
    sh:property [
        sh:path ( cred:termsOfUse ebwv:acceptedAt ) ;
        sh:lessThanOrEquals cred:validFrom ;
        sh:message "IR-01: termsOfUse.acceptedAt must be less than or equal to the issuance datetime (validFrom)." ;
    ] .
```

To validate, convert the credential to RDF with a conformant JSON-LD 1.1 processor, such as
jsonld.js or pyld, then run a SHACL engine over the result. Include the SPARQL companion where the
engine supports SHACL-SPARQL; pySHACL takes a single shapes graph, so concatenate the two files:

```bash
cat ds-membership-shacl.ttl ds-membership-shacl-sparql.ttl > all-shapes.ttl
uv run --python 3.12 --with pyld --with requests python -c "import json,sys; from pyld import jsonld; \
  print(jsonld.to_rdf(json.load(open(sys.argv[1])), {'format': 'application/n-quads'}), end='')" \
  ./sample-data/ds-membership-jsonld-sample.json > sample-data/ds-membership-jsonld-sample.nt \ 
pyshacl -s all-shapes.ttl -df nt sample-data/ds-membership-jsonld-sample.nt
```

Do not let pySHACL parse the JSON-LD itself (`-df json-ld`). Its parser, rdflib (verified with
version 7.6.0), applies the type-scoped context of only the first entry in a `type` array, whereas
JSON-LD 1.1 applies all of them. For the credential-level `type`
`["VerifiableCredential", "ElectronicAttestationOfAttributes"]`, rdflib therefore drops
`attestationLegalCategory` and reports a conformant credential as violating Section 4.1. Swapping
the two types only moves the loss to `validFrom` and the other VCDM terms.

Both artefacts are aids for implementers. Where they differ from this Rulebook, the Rulebook
prevails.

## 6 Protocols

This chapter identifies the protocols used to issue and present this attestation.
The substantive issuance rules are in chapter 7 and the presentation rules are in
chapter 9.

### 6.1 Issuance

| Protocol | Supported | Profile or version | Specification | Notes |
| --- | --- | --- | --- | --- |
| OpenID4VCI | yes | [HAIP] draft-03 | [OpenID4VCI], [HAIP], [ETSI TS 119 472-3], [CIR 2026/1731] | |

### 6.2 Presentation

| Protocol | Supported | Profile or version | Specification | Notes |
| --- | --- | --- | --- | --- |
| OpenID4VP, remote | yes | [HAIP] draft-03 | [OpenID4VP], [HAIP], [ETSI TS 119 472-2], [CIR 2026/1731] | |
| ISO/IEC 18013-5, proximity | no | | [ISO/IEC 18013-5], [ETSI TS 119 472-2], [CIR 2026/1731] | Requires the mdoc format, which is not supported (chapter 5) |

Protocols listed here are those referenced in Topic 6 of Annex 2 of the ARF. This
Rulebook does not profile these protocols beyond what is stated in the table.

## 7 Issuance

### 7.1 Holder Key Binding at Issuance (Wallet Binding)

This is a fundamental security requirement that prevents credential theft and ensures an attestation is bound to a specific wallet.
*   **What it is:** Where the attestation is device-bound (see table below), the Holder's wallet **MUST** perform a "proof-of-possession" challenge to prove it controls a specific private key. The Attestation Provider then embeds the corresponding public key into the attestation payload before signing it.
*   **Why it matters:** This process creates a permanent, cryptographic link between the attestation and the Holder's wallet. During presentation (as described in Chapter 9), a Relying Party can then challenge the presenting wallet to prove it still controls that same private key. This verification step makes stolen or copied attestation files useless to a thief, as they will not have the required private key.

| Field | Value | Source |
| --- | --- | --- |
| Device-bound | MAY | EW-DM-12-038 |
| Cryptographically bound to | none | EW-DM-12-032 |
| Relying Party must also verify a PID | no | EW-DM-12-031 |
| Binding subject | legal person |  |

The attestation is bound to an organisation (legal person) holding an EU Business Wallet, not to
a natural person's device. The holder is identified through the EUBWOID and its EUID, not through a
PID, so a Relying Party does not request and verify a PID (EW-DM-12-031), and the MVP requires no
cryptographic binding: `cryptographically_bound_to` (EW-DM-12-032) is not included. If a future
scenario requires binding to the EUBWOID, `cryptographically_bound_to` is to be added as optional
metadata in section 4.2, with the corresponding attestation type or `vct` value.

### 7.2 Issuance Policy

An Issuance Policy defines the minimum rules, policies, and procedures that any compliant Attestation Provider **SHALL** follow when issuing attestations of this type.

For transparency and to allow Relying Parties to programmatically assess their trust in the attestation, each Attestation Provider **SHALL** publish their terms and conditions, a generic Trust Services Policy, and an EAA Policy (per attestation type) in accordance with **[ETSI TS 119 471]**. These policies must be accepted by the Holder upon receipt of the attestation.

This section references key concepts from **[ETSI TS 119 471]** and **[ETSI TS 119 461]**. The most critical issuance concepts for a rulebook author to understand and specify are explained below:

**1. Core Issuer Obligations**

Any entity acting as an authorized Attestation Provider under this rulebook **SHALL** comply with the following general obligations:

  **Issuance Basis and Timestamping:** The Provider **SHALL** issue the attestation based on information and supporting documentation that is valid and accurate at the exact moment of issuance. A timestamp of issuance (iat in SD-JWT VC) **MUST** be included in each attestation. This enables a Relying Party to not only verify the attestation's temporal validity but also to correctly validate the Attestation Provider's trust status as it was at the moment of issuance (e.g., by checking against a historical Trust List).

*   **Data Currency and Revocation:** The Provider is responsible for the ongoing accuracy of the attested information. The Provider **MUST** immediately revoke the attestation if any change occurs that affects the validity or accuracy of the underlying data.

**2. Identity and Attribute Proofing (as per ETSI TS 119 461)**

This refers to the rigor with which the Attestation Provider verifies the information before issuing the attestation. The level of trust a Relying Party can place in an attestation depends directly on the quality of this proofing process.

*   **Identity Proofing:** This is the process of verifying the identity of the subject. For example, for registered legal entities in a national register, this **MUST** involve verifying its active registration in the respective register.
*   **Attribute Proofing:** This is the process of verifying the specific claims (attributes) being attested. The Provider **MUST** verify the attributes against a designated authentic data source (as defined by the author below).

**3. Architectural Pattern for EAA Provider Trust**

To enable the EAA Provider to implement the basic verification steps described in Chapter 9, the following general issuer obligations apply to all EAA Providers:
* EAA Provider SHALL make the key it signs with verifiable through the trust framework of chapter 10.
* Issuer obligation differ for the different trust mechanisms

**Attestation Chaining (Issuer Component with Access Certificate)**
1.  **Provider Identity Credential:** The EAA Provider **MUST** possess an **Access Certificate** issued by a Qualified Trust Service Provider (QTSP). This certicate already contain a `signing_key` parameter holding the public key the Provider uses to sign the issued EAAs.
2.  **Trust Chaining Mechanism:** The EAA Provider **MUST** include their access certificate in the header of every EAA they issue. This allows a Relying Party to verify the EAA signature using the public key from the embedded access certificate and then verify the access certificate itself against the eIDAS Trusted List.

**Attestation Chaining (EBW with EBWOID)**
1.  **Provider Identity Credential:** The EAA Provider **MUST** possess their own European Business Wallet Owner Identity (EBWOID), issued by a Qualified Trust Service Provider (QTSP). To be authorized to sign and issue other EAAs, this EBWOID **MUST** contain a `signing_key` parameter holding the public key the Provider uses to sign the issued EAAs.
2.  **Trust Chaining Mechanism:** The EAA Provider **MUST** include their own EBWOID (or a reference/chain to it) in the header of every EAA they issue. This allows a Relying Party to verify the EAA signature using the public key from the embedded EBWOID, and then verify the EBWOID itself against the eIDAS Trusted List.

**QSEAL**
[to be described]

**to be defined according to ADR#336**
[to be described]

**4. Batch Issuance (Protocol Optimization)**

This is a technical efficiency and privacy feature defined in the underlying OpenID4VCI protocols.

*   **What it is:** A technical capability allowing a Wallet to request, and an Attestation Provider to issue, multiple credentials simultaneously in a single API interaction, rather than requiring separate network connections for each credential.
*   **Application to this Rulebook:** For unique, long-lived business attestations, batch issuance is typically **Optional** or **Not Applicable**, as these credentials do not require multi-copy anonymity and are issued on a one-off basis.

Parameters for this attestation type:

* **Authorized Authentic Sources.** `member.legalName` and `member.legalIdentifier` MUST be taken
  from the EUBWOID the holder presents at onboarding (section 1.1). `memberOf`, `role` and
  `onboardedBy` MUST be taken from the issuing DSI's or dataspace's own membership records.
  `termsOfUse` MUST record the governance rulebook the holder accepted during onboarding, and
  `evidence`, where present, the identification means actually checked.
* **Attestation Lifecycle.** The maximum validity period is 12 months from `validFrom` (`iat` in
  the SD-JWT VC encoding). Where the membership continues, the issuer renews it by issuing a new
  credential before the current one expires; see section 7.3.
* **Batch Issuance Designation.** Batch issuance is not permitted for this attestation type.
* **Attestation-Specific Obligations.**

- offer the W3C VCDM format, and optionally SD-JWT VC (chapter 5);
- declare the types that JSON-LD expansion depends on (section 5.3.1);
- apply the selective disclosure rules stated per attribute (sections 3.2, 3.3, 4.1, 4.2);
- satisfy the integrity rules, in particular IR-01, IR-03 and IR-06 (section 4.5);
- issue only for a `memberOf` value registered in code list 4.4 and for which the Provider is
  authorised (section 4.4 and chapter 10);
- publish revocation status (chapter 8).

**Deviation.** The architectural patterns for EAA Provider trust above, attestation chaining
through an access certificate or through the Provider's EBWOID, are not yet adopted by this
Rulebook. Issuer keys are currently resolved as described in section 10.1. The choice between the
patterns, and how the chosen trust link is carried in each format, is open and recorded for the
rulebook quality assurance group.

### 7.3 Lifecycle management

- **Validity period.** At most 12 months from `validFrom`, set by the issuing onboarding service
  provider (section 7.2).
- **Reissuance and renewal.** Membership and its set of roles share one lifecycle. Adding,
  changing or removing a role requires reissuance of the credential, and a continuing membership is
  renewed by issuing a new credential before the current one expires.
- **Update or correction.** When the underlying facts change, the issuer reissues the credential
  and revokes the superseded one, as described in chapter 8.

### 7.4 Embedded disclosure policy

| Field | Value |
| --- | --- |
| Policy present | no |
| Common policy applied | none |
| Encoding | pending upstream specification |

Embedded disclosure policies are defined in CIR (EU) 2024/2979 and in Topic 43 of
Annex 2 of the ARF. No standardised encoding exists in ISO/IEC 18013-5, SD-JWT VC,
OpenID4VCI or OpenID4VP at the time of writing. This Rulebook declares which policy
applies and does not specify a local encoding.

## 8 Revocation

This chapter states whether attestations of this type are revocable, and if so how
revocation status is published and how a Relying Party checks it.

Attestations of this type are **revocable**. The credential carries a status entry, a
`credentialStatus` of type `BitstringStatusListEntry` in the W3C VCDM encoding (section 5.3) and a
`status` claim in the SD-JWT VC encoding (section 5.1.3), through which status is published.

**Deviation.** The template's fixed text for revocable attestations publishes status through the
Attestation Status Lists or Attestation Revocation Lists of the Technical Specification issued by
the Commission. The mechanisms above predate that alignment and are left as written; the deviation
is recorded for the rulebook quality assurance group, and the fixed text is not reproduced here.

- **Who may request revocation.** The issuing onboarding service provider revokes; this version
  does not define a request procedure for other parties.
- **Grounds.** In addition to any grounds imposed by regulation: the holder's membership of the
  DSI or dataspace ends; any change affecting the validity or accuracy of the attested data; or the
  credential is superseded by reissuance, because membership and its set of roles share one
  lifecycle and a role change requires a new credential.
- **Time from trigger to status update.** Immediate: the issuer SHALL update the status list as
  soon as the trigger event occurs (section 7.2, Data Currency and Revocation).

## 9 Request, Presentation and Verification

To verify and validate a received presentation of an attestation of this type,
the following steps SHALL be performed:

1.  **Cryptographic Integrity Verification (Tamper Proof):**
    The Verifier **MUST** verify that the received attestation data has not been altered or tampered with since its issuance. The wallet shall validate the digital signature over the attestation using a trusted public key (trust anchor) obtained according to the framework detailed in Chapter 10.
2.  **Issuer Authentication and Trust Evaluation:**
     The Verifier **MUST** verify the Attestation Provider's identity, ownership of the signing key at issuance, and authorisation to issue this attestation for the stated `memberOf` value using the trust mechanism described in Chapter 10.
3.  **Temporal Validity Verification:**
     The Verifier **MUST** verify that the attestation is within its stated validity window. An attestation that has not yet taken effect or has already expired **SHALL NOT** be accepted, regardless of any other successful checks.
4.  **Revocation Status Verification:**
   The Verifier **MUST** verify the real-time revocation status of the received attestation as described in Chapter 8, unless:
    *   The attestation is explicitly defined as short-lived; or
    *   The remaining lifetime of the attestation is below the designated revocation time threshold.
5.  **Holder Wallet and Device Binding Verification:**
Where the attestation is device-bound according to section 7.1, the Verifier **MUST** verify the Holder's presentation signature and the presentation's binding to achieve two critical security checks:
    *   Ensure that the presenter has not submitted a copied or replayed attestation
    *   Validate that the presented attestation was issued to this exact presenting wallet instance.

### 9.1 Relying Party Role (RP Instance - EUDI Wallet)

The Membership Credential is held by organisations, legal persons, in a European Business Wallet.
Presentation from an EUDI Wallet to a Relying Party Instance is not in scope; the applicable role
is the EBW role of section 9.2.

### 9.2 EBW Relying Party Role (EBW Wallet - EBW Wallet)

Following the principle of mutual identification the verification in the **European Business Wallet (EBW)** ecosystem is designed as a mutual cryptographic process. Unlike traditional consumer wallet flows, EBW transactions must satisfy high-assurance, machine-to-machine (M2M) environments. Verification of EAAs is executed under two distinct conditions:

1.  **Relying Party Role:** When an EBW Owner receives a presented attestation from a Holder and must verify its cryptographic claims before providing a service or executing a transaction.
2.  **Holder Role:** When an EBW Holder receives an incoming Presentation Request and must verify the identity and system integrity of the requesting Relying Party before releasing confidential, non-public attestation data.

The system performs these verification steps to achieve three core business and regulatory objectives:
*   **Trust Augmentation:** Establishing the absolute cryptographic authenticity of exchanged data and validating the identity of the participating legal entities.
*   **Liability Allocation:** Fulfilling statutory due diligence to minimize operational risk and programmatically shift liability to the responsible party (Issuer or Holder).
*   **Data Protection:** Safeguarding highly confidential corporate data (e.g., ultimate beneficial ownership, control structures) stored in the EBW against unauthorized harvest or access.

#### 9.2.1 Relying Party obligation during request
1.  **Include own identification and authorization data in presentation requests:**
When requesting non-public and therefore confidential data, the Relying Party **SHALL** include its own **EBWOID** and **BWUA** (using the `ebwoid` and `ebw_wallet_unit` format blocks in the `verifier_info` array of the Request Object) to allow the receiving Holder to:
   *   Enforce automated consent and exchange policies based on the Verifier’s legal identity and verified platform integrity.
   *   Ensure the request originates from a valid wallet instance rather than uncertified or spoofed software.
   *   *Operational Constraint:* Requesters that do not present a valid EBWOID and BWUA **SHOULD NOT** receive confidential attestations.
2.  **Request Wallet Unit Attestations (BWUA):**
The Relying Party **SHOULD** include a request for the Holder’s Business Wallet Unit Attestation (BWUA)  to mitigate the risk of interacting with a revoked, compromised, or modified wallet instance.
3.  **Adhere to Data Minimization (Purpose Limitation):**
The Relying Party **SHALL** only request attributes that are strictly necessary to fulfill the stated business purpose of the transaction.
4.  **Respect Trust Model Registration:**
Where the trust model for a requested attestation requires Relying Party registration, the RP **SHALL** only request attributes it is explicitly registered and authorized to request.

#### 9.2.2 Holder and Relying Party obligation during verification

To protect the Holder and Relying Party from processing fraudulent, tampered, or stolen attestations, they  **MUST** programmatically execute the following five verification steps on all received attestations. Holder and Relying Party performing the verification steps are called Verifier within the rest of this chapter. The Verifier can perform the steps only if the EBW supports the verification steps, therefore the EBW Wallet Provider **MUST** support the following verification steps with their EBW:

##### 9.2.2.1 Impact of Cryptographic Verification on Holder Liability
The mandatory validation of incoming requests protects the Holder when operating in high-security, backend-to-backend environments:

*   **Establishes Non-Repudiation (Defense Against Dispute):** By validating the signature of the Request Object against the public key attested inside the Relying Party's EBWOID, the Relying Party cannot later deny having initiated the transaction or requested the data. This protects the Holder from legal claims that they disclosed confidential business secrets without a valid, authorized request.
*   **Protects Against Impersonation (Defense Against Data Breaches):** It cryptographically proves the request did not originate from a malicious actor who simply spoofed the Relying Party's public `client_id` or metadata. Because the transaction requires a signature generated by the private key securely held within the Relying Party's hardware wallet, the Holder is guaranteed they are communicating with the actual legal entity identified in the EBWOID.
*   **Fulfills Statutory Due Diligence (Safe Harbor under GDPR):** Under data protection regulations, a corporate Holder has a legal duty to protect its confidential operational data. Executing these mandatory checks before releasing any data payload safe-harbors the Holder from charges of negligence or unauthorized data disclosure.

##### 9.2.2.2 Impact of Cryptographic Verification on Relying Party Liability

The execution of the mandatory cryptographic checks defined in this chapter directly determines the legal and liability posture of the Relying Party (RP). Under the European Business Wallet framework and eIDAS, performing these verifications shifts liability and protects the RP from negligence claims:

| Verification Check | Cryptographic Fact | Impact on Relying Party Liability |
| :--- | :--- | :--- |
| **Integrity & Issuer Auth (Steps 1 & 2)** | Proves data has not been modified; validates the cryptographic identity of the issuer. | **Transfers Data-Accuracy Liability to Issuer.** The RP is legally protected against errors or falsehoods in the received data. Liability shifts to the Attestation Provider under eIDAS2 or their published terms. |
| **Temporal & Revocation (Steps 3 & 4)** | Proves the credential was actively valid and unrevoked at the exact moment of the transaction. | **Protects Against Fraud Claims.** Safe-harbors the RP from claims arising from the use of credentials that were valid in the past but have since expired or been revoked. |
| **Device Binding & Presentation Signature (Step 5)** | Proves the holder has possession of the private key associated with the credential and actively authorized this specific session. | **Protects Against Identity Theft & Establishes Safe Harbor.** Explained in detail below. |

**Defense Against Identity Theft (Shifts Burden of Proof)**
By verifying the device binding (e.g., via the Key Binding JWT, matching `nonce` and `aud`), the RP proves that the presenter has real-time, hardware-backed control over the private key associated with the credential.

If a malicious actor steals a copy of another company's EBWOID file, they **cannot** generate a valid binding signature without access to that specific wallet's private key. By verifying this binding, the RP completely protects itself from claims of *"failing to prevent obvious credential-sharing or identity theft,"* shifting the burden of proof entirely to the claimant.

**Safe Harbor for Data Access and Key Compromise**
Under GDPR and eIDAS, if an RP discloses confidential data or executes a transaction based on a credential where device binding was fully and correctly verified, it is legally deemed to have fulfilled its due diligence. If it is later discovered that the Holder's private key was compromised at the time of the transaction, the liability shifts away from the RP to:
*   The **Holder**, for failing to adequately secure and protect their private key/hardware device.
*   The **Issuer**, if they were notified of the key compromise but failed to add the credential to their revocation list in a timely manner.

**Eliminates Sole Negligence under eIDAS (Art 12a / 12b)**
Under eIDAS Article 12a and 12b, a Relying Party has a duty of care to validate credentials. If an RP fails to verify the presentation signature and the corresponding trust chains, they are considered to have accepted an unauthenticated payload. In the event of a security breach or fraudulent transaction, the RP can be held **solely liable** due to technical negligence.

Obligations specific to this attestation type:

The Membership Credential is used in the WE BUILD SC2 "seamless onboarding" scenario. Its use case
in this pilot is:

* **Onboarding into a DSI or into Agri-X.** The holder presents the EUBWOID to identify their
  organisation, accepts the applicable dataspace governance rulebook, and receives a Membership
  Credential reflecting their membership and roles. Information already presented during a previous
  onboarding flow is trusted and not requested again. Where the onboarding platform holds a
  record of the identification means used to prove the holder's identity, it is recorded in `evidence`, so that a
  later Relying Party can reconcile the holder with its own legacy records.

**Potential future use, out of scope for this pilot.** Verifying membership and roles during
data-sharing transactions between participants of a DSI or dataspace is a plausible further
application, but it is not piloted in the MVP and is not specified by this Rulebook. Direct
presentation of the Membership Credential inside a data-transfer flow is not assumed: such a flow
would most likely require the credential to be transformed into a connector-native credential (for
instance an EDC / dataspace protocol participant credential) first. Any statement about
data-sharing use elsewhere in this document is to be read in that light.

**Relying Party obligations.** A Relying Party SHALL verify the issuer signature/proof, check
credential validity (`validFrom`/`validUntil`) and revocation status (Section 8), and confirm the
issuer is an authorised onboarding service provider for the relevant `memberOf` value (Section 10).
Where rulebook conformance matters, the Relying Party MAY compare `termsOfUse.hash` /
`termsOfUse.version` against the expected rulebook. A Relying Party MAY additionally use
`evidence` to reconcile the holder with its own legacy records, subject to IR-04. It SHALL match
`role` and `memberOf` by exact IRI comparison per IR-05.

### 9.3 Presentation modes

Remote presentation is in scope. Proximity presentation is not in scope, consistent
with chapter 5, which records the mdoc encoding as out of scope. The primary format is W3C VCDM
(JSON-LD), presented through OpenID4VP; an SD-JWT VC flow MAY be piloted additionally.

### 9.4 Transactional data

No transactional data as defined in Topic 20 of Annex 2 of the ARF is associated
with this attestation type.

## 10 Trust Framework

The trust anchor for this attestation is obtained as described in the branch below
that corresponds to its legal category. The trust anchor location applies in either
case.

**Non-qualified EAA (including S-EAA)**

### 10.1 Relying Party Role (RP Instance - EUDI Wallet)

The trust anchor is not obtained from a Trusted List of qualified trust service
providers. It is obtained as follows. In the W3C VCDM encoding, the `issuer` is a DID, normally
`did:web`, and the trust anchor is the public key in the DID document it resolves to. In the
SD-JWT VC encoding, `iss` is the Provider's HTTPS URL and the key is obtained as specified by
[SD-JWT VC]. Authorisation of the Provider to issue
this attestation type is then verified by the WE BUILD and dataspace trust framework (WP4), for
the specific `memberOf` value the credential carries.

The trust anchor is not obtained from a Trusted List of qualified trust service
providers. 
A Wallet Unit MAY verify Provider authorisation using the mechanism described in
ISSU_34 of Topic 10 of Annex 2 of the ARF.

### 10.2 EBW Relying Party Role (EBW Wallet - EBW Wallet)

#### 10.2.1 Attestation Chaining

**Deviation.** The template's fixed text for this section requires the EAA Provider to embed its own
EBWOID in the header of every issued EAA, and the Relying Party to take the EBWOID's `signing_key`
as the trust anchor, delegated from the EU Trusted List of Lists through the QTSP that issued the
EBWOID. This Rulebook has not yet adopted attestation chaining: the issuer key is resolved as in
section 10.1, for the EBW role as well. Adoption, and how the EBWOID or a reference to it is carried
in each format, is open and recorded for the rulebook quality assurance group; the fixed text is
therefore not reproduced here.

#### 10.2.2 QSEAL

Not yet described by the template. Not used by this Rulebook.

#### 10.2.3 To be defined according to ADR#336

Not yet described by the template. Not used by this Rulebook.

**Trust anchor location**

The attribute or metadata carrying the trust anchor location contains at least the
URL at which a machine-readable version can be found or looked up. For a QEAA this
location refers to the trust anchor (EW-DM-12-023). For a PuB-EAA it refers to the
qualified certificate that signed the attestation (EW-DM-12-023). For a
non-qualified EAA the location and its meaning are as described above
(EW-DM-12-024, EW-DM-12-030).

In this Rulebook that location is the issuer identifier, carried by the standard issuer metadata
of each format (section 4.1): the issuer DID in the W3C VCDM encoding, the `iss` URL in the
SD-JWT VC encoding.

**Deployment profile**

- **Distribution of Provider trust anchors.** Through the Provider's DID document (W3C VCDM) or
  as specified by [SD-JWT VC] for the `iss` URL. No List of Trusted Entities or Trusted List is
  involved in this version.
- **Lookup.** A Relying Party or Wallet Unit resolves the issuer identifier; it keys on that
  identifier only. No caching or update policy is defined in this version.
- **Verifying authenticity.** A Relying Party verifies the proof against the issuer's key, then the validity period, then the revocation status (chapter 8), then that the
  issuer is authorised for the `memberOf` value, and finally matches `memberOf` and `role` as set
  out below.
- **Authenticating the Relying Party.** The steps a Wallet Unit follows before presentation are not
  specified by this Rulebook in this version.
- **Consortium-specific dependencies.** The European Business Wallet Vocabulary JSON-LD context,
  <https://w3id.org/ebwv/v0.1>, maintained by the WE BUILD Semantics work group.
- **Worked example.** The illustrative credential in section 5.3.

**memberOf vocabulary governance.** `memberOf` values are absolute IRIs registered in code list 4.4
by the governance level of the owning DSI or dataspace, under that DSI's or dataspace's own domain.
A Relying Party SHALL match `memberOf` by exact IRI comparison and confirm WP4 authorisation of the
issuer for that specific value (IR-05). Domain ownership makes the values globally unique. Prefix
matching does not apply, since each value identifies a distinct DSI or dataspace rather than a term
in a shared vocabulary, and a Relying Party SHALL NOT depend on the IRI dereferencing. Registering
the value in code list 4.4 before issuing remains a governance obligation, not a convenience.

**Role vocabulary governance.** `role` values are absolute IRIs. Those registered in code list 4.4
are the `DataSpaceRole` individuals published by the WE BUILD Semantics work group under
`https://w3id.org/ebwv#`, independently of this Rulebook's own versioning. Because the vocabulary
types `role` as `@id`, a Relying Party MAY trust roles by namespace prefix rather than an
exact-match list, so that new individuals published under that namespace do not require a Relying
Party policy change. A DSI MAY likewise mint role IRIs under a namespace it owns without a change
to this Rulebook or to the vocabulary context; such values SHALL be governed by that DSI's own
trust framework, and a Relying Party SHALL ignore any role IRI it does not recognise (IR-05).

## 11 References

| Reference | Details |
| --- | --- |
| [ARF] | EUDI Wallet Architecture and Reference Framework, version 3.0.0 |
| [CIR 2024/2977] | Commission Implementing Regulation (EU) 2024/2977, PID and EAA |
| [CIR 2024/2979] | Commission Implementing Regulation (EU) 2024/2979, integrity and core functionality |
| [CIR 2026/1731] | Commission Implementing Regulation (EU) 2026/1731, as regards applicable standards and specifications |
| [ETSI TS 119 461] | Policy and security requirements for trust service components providing identity proofing of trust service subjects |
| [ETSI TS 119 471] | Policy and security requirements for EAA service providers |
| [ETSI TS 119 472-1] | Profiles for Electronic Attestations of Attributes; Part 1 - General requirements |
| [ETSI TS 119 472-2] | Profiles for Electronic Attestations of Attributes; Part 2 - Profiles for EAA/PID Presentations to Relying Party |
| [ETSI TS 119 472-3] | Profiles for Electronic Attestations of Attributes; Part 3 - Profiles for issuance of EAA or PID |
| [ETSI TS 119 478] | Specification of interfaces related to Authentic Sources |
| [European Business Wallet Vocabulary v0.1] | WE BUILD Semantics work group, European Business Wallet Vocabulary, version 0.1 |
| [HAIP] | Yasuda, K. *et al,* OpenID4VC High Assurance Interoperability Profile, OpenId Foundation, Version draft-03 |
| [IANA-JWT-Claims] | IANA JSON Web Token Claims Registry. Available: <https://www.iana.org/assignments/jwt/jwt.xhtml> |
| [ISO/IEC 18013-5] | ISO/IEC 18013-5, Personal identification --- ISO-compliant driving licence - Part 5: Mobile driving licence (mDL) application, First edition, 2021-09 |
| [OIDC] | Sakimura, N. et al., "OpenID Connect Core 1.0", OpenID Foundation. Available: <https://openid.net/specs/openid-connect-core-1_0.html> |
| [OpenID4VCI] | OpenID for Verifiable Credential Issuance |
| [OpenID4VP] | OpenID for Verifiable Presentations |
| [Regulation] | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework |
| [RFC 2119] | Key words for use in RFCs to Indicate Requirement Levels |
| [RFC 3339] | RFC 3339  - Date and Time on the Internet: Timestamps, G. Klyne et al., July 2002 |
| [RFC 8610] | RFC 8610  - Concise Data Definition Language (CDDL): A Notational Convention to Express Concise Binary Object Representation (CBOR) and JSON Data Structures, H. Birkholz et al., June 2019 |
| [RFC 8943] | RFC 8943  - Concise Binary Object Representation (CBOR) Tags for Date, M. Jones et al., November 2020 |
| [RFC 8949] | RFC 8949 - Concise Binary Object Representation (CBOR), C. Bormann et al., December 2020 |
| [SD-JWT VC] | SD-JWT-based Verifiable Credentials (SD-JWT VC). Available: <https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/>, version draft-ietf-oauth-sd-jwt-vc-09 |
| [Topic 10] | ARF Annex 2 - Topic 10 - Issuing a PID or attestation to a Wallet Unit: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a2310-topic-10-issuing-a-pid-or-attestation-to-a-wallet-unit> |
| [Topic 12] | ARF Annex 2 - Topic 12 - Attestation Rulebooks, Available: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a2312-topic-12-attestation-rulebooks> |
| [Topic 20] | ARF Annex 2 - Strong User authentication for electronic payments, Available: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a2320-topic-20-strong-user-authentication-for-electronic-payments> |
| [Topic 7] | ARF Annex 2 - Topic 7 - Attestation revocation and revocation checking Available: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a237-topic-7-attestation-revocation-and-revocation-checking> |
| [W3C VCDM v2.0] | Sporny, M. *et al,* Verifiable Credentials Data Model v2.0, W3C Recommendation. |
