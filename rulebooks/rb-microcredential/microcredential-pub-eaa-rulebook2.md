# Attestation Rulebook for attestations of type Micro-credential

Category: PuB-EAA

*[Based on the WE BUILD Attestation Rulebook Template and the WE BUILD BU5 Micro-credentials Attestation Design. PuB-EAA profile aligned with Article 45f and Annex VII of Regulation (EU) 2024/1183, Commission Implementing Regulation (EU) 2025/1569 and ETSI TS 119 472-1.]*

* Author(s):
    * Stefan Liström, Sunet
    * Johan Peterson, Linköping University
    * Per von Bahr, Sunet
* Previous Authors
    * N/A

| Version | Date | Description |
| --- | --- | --- |
| 0.2 | 2026-09-11 | Restructured onto the generic WE BUILD attestation rulebook template (11 chapters). No normative content removed. |
| 1.0 | 2026-10-20 | Updated attributes and metadata and fixed index errors. Focus on mandatory attributes for 1.0. |
| 2.0-draft | 2026-11-23 | Converted from a non-qualified EAA into a PuB-EAA profile. Added Annex VII points a–i, the ETSI TS 119 472-1 PuB-EAA profile for SD-JWT VC, qualified seal and certificate requirements, mandatory revocation without suspension, issuer eligibility and notification, a trust framework based on the Commission's list of PuB-EAA providers, and scheme registration. Replaced `attestation_legal_category` with `category`. New `vct`. |

**Written against:** ARF version 3.0.0; WE BUILD template version 1.0 (generic); EUDI Attestation Rulebook Template v1.5; Regulation (EU) 2024/1183 (Article 45f, Annex VII); Commission Implementing Regulation (EU) 2025/1569 as amended by Commission Implementing Regulation (EU) 2026/1735; ETSI TS 119 472-1 V1.2.1 (2026-02); ETSI TS 119 412-6.

**Feedback:** [GitHub issues](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/issues), or contact Work Package 4 in WE BUILD.

## Table of contents

- [1 Introduction](#1-introduction)
   * [1.1 Document scope and purpose](#11-document-scope-and-purpose)
   * [1.2 Document structure](#12-document-structure)
   * [1.3 Key words](#13-key-words)
   * [1.4 Terminology](#14-terminology)
   * [1.5 Authentic source and legal basis](#15-authentic-source-and-legal-basis)
- [2 Compliance](#2-compliance)
   * [2.1 Compliance statement](#21-compliance-statement)
   * [2.2 Regulatory basis](#22-regulatory-basis)
   * [2.3 Traceability](#23-traceability)
   * [2.4 Registration in the catalogue of attestation schemes](#24-registration-in-the-catalogue-of-attestation-schemes)
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
   * [4.6 Issuer identification](#46-issuer-identification)
- [5 Formats](#5-formats)
   * [5.1 SD-JWT VC-based encoding](#51-sd-jwt-vc-based-encoding)
      + [5.1.0 JWS protected header](#510-jws-protected-header)
      + [5.1.1 IANA-registered and standard JWT / SD-JWT VC claims](#511-iana-registered-and-standard-jwt--sd-jwt-vc-claims)
      + [5.1.2 Claims defined in ETSI TS 119 472-1](#512-claims-defined-in-etsi-ts-119-472-1)
      + [5.1.3 Public or reusable claims](#513-public-or-reusable-claims)
      + [5.1.4 Private claims specific to the Micro-credential Attestation](#514-private-claims-specific-to-the-micro-credential-attestation)
      + [5.1.5 Example protected header and minimum JWT claim set (option A)](#515-example-protected-header-and-minimum-jwt-claim-set-option-a)
      + [5.1.6 Example JWT claim set (not implemented yet)](#516-example-jwt-claim-set-not-implemented-yet)
      + [5.1.7 Example issued SD-JWT](#517-example-issued-sd-jwt)
      + [5.1.8 Example human-readable disclosed payload](#518-example-human-readable-disclosed-payload)
   * [5.2 ISO/IEC 18013-5-compliant encoding](#52-isoiec-18013-5-compliant-encoding)
   * [5.3 W3C Verifiable Credentials Data Model-based encoding](#53-w3c-verifiable-credentials-data-model-based-encoding)
- [6 Protocols](#6-protocols)
   * [6.1 Issuance](#61-issuance)
   * [6.2 Presentation](#62-presentation)
- [7 Issuance](#7-issuance)
   * [7.1 Binding](#71-binding)
   * [7.2 Issuance Policy](#72-issuance-policy)
   * [7.3 Lifecycle management](#73-lifecycle-management)
   * [7.4 Embedded disclosure policy](#74-embedded-disclosure-policy)
   * [7.5 Provider requirements](#75-provider-requirements)
   * [7.6 Signature and signing certificate](#76-signature-and-signing-certificate)
- [8 Revocation](#8-revocation)
- [9 Presentation](#9-presentation)
   * [9.1 Presentation Policy](#91-presentation-policy)
   * [9.2 Presentation modes](#92-presentation-modes)
   * [9.3 Transactional data](#93-transactional-data)
- [10 Trust Framework](#10-trust-framework)
- [11 References](#11-references)


## 1 Introduction

### 1.1 Document scope and purpose

This Rulebook defines the *Micro-credential Attestation* as an electronic attestation of attributes issued by or on behalf of a public sector body responsible for an authentic source (PuB-EAA), for use in the European Digital Identity Wallet ecosystem.

The Micro-credential Attestation expresses the real-world fact that a natural person has successfully completed a small, coherent volume of formally assessed learning, delivered under the quality assurance of an educational organisation, and has thereby acquired specific learning outcomes. It follows the definition set out in the Council Recommendation of 16 June 2022 on a European approach to micro-credentials for lifelong learning and employability (2022/C 243/02): a portable, learner-owned record of assessed learning outcomes from a small volume of study, which can be aligned to a curriculum, carries a notional workload, and is issued under institutional quality assurance.

The attestation SHALL be issued by a public sector body within the meaning of Article 3, point (46), of Regulation (EU) 2024/1183. The issuer is either:

* a public higher education institution or other public formal education provider that is, under Union or national law, responsible for the authentic source holding the study records on which the attestation is based; or
* a public sector body designated under Union or national law to issue such attestations on behalf of the public sector body responsible for that authentic source.

An organisation that is not such a public sector body, including an academic identity provider that has not been designated in this way, SHALL NOT issue attestations under this Rulebook. Micro-credentials awarded by private providers, or learning not recorded in an authentic source within the public sector, are out of scope of this Rulebook and can be issued under the non-qualified EAA version of the Micro-credential Rulebook.

The Holder is the natural person who completed the assessed learning. Relying Parties are expected to include universities and other HEIs evaluating admission, credit recognition, or advanced standing; employers assessing skills for recruitment or onboarding; and other organisations that need to rely on verified evidence of formally taught knowledge, skills, and competences.

In practical terms, the attestation enables a learner to present proof of one or more completed micro-credentials through an EUDI Wallet, for example to demonstrate fulfilment of entry requirements or eligibility for recognition of credits when applying to a course or programme in another country. This supports cross-border and domestic academic mobility, provided that the relying party can verify the issuer, the qualified electronic seal or signature, validity, status, and the disclosed attributes needed for its decision. Under Article 45f of Regulation (EU) 2024/1183, an attestation complying with this Rulebook has the legal standing of a PuB-EAA.

The attestation supports use cases including university admission and enrolment, recognition of prior learning and credit transfer, professional onboarding, and other formally taught knowledge-dependent procedures, in both domestic and cross-border contexts.

### 1.2 Document structure

This Rulebook follows the generic WE BUILD attestation rulebook template. Chapter 1
sets out the scope, terminology, and the authentic source and legal basis. Chapter 2
states how the Rulebook complies with the ARF and the applicable Regulations, and how
the scheme is registered. Chapters 3 and 4 define the attributes and metadata in an
encoding-independent manner, including the issuer identification required by Annex VII.
Chapter 5 states the formats in which this attestation is issued. Chapters 6 to 9 cover
protocols, issuance (including provider and signature requirements), revocation and
presentation. Chapter 10 sets out the trust framework, and chapter 11 lists references.

### 1.3 Key words

This document uses the capitalised key words 'SHALL', 'SHOULD' and 'MAY' as specified
in [RFC 2119], to indicate requirements, recommendations and options.

In addition, 'must' (non-capitalised) indicates an external constraint, a requirement
not mandated by this document but by an external document. The word 'can' indicates a
capability. Other words such as 'will', 'is' and 'are' are statements of fact.

### 1.4 Terminology

This document uses the terminology specified in Annex 1 of the ARF and in ETSI TS 119 472-1.

In addition, the following domain-specific terms are used:

| Term | Meaning |
| --- | --- |
| Micro-credential Attestation | A Verifiable Credential representing a person's completion of a small, coherent volume of formally assessed learning and the associated learning outcomes, issued as a PuB-EAA under this Rulebook. |
| PuB-EAA | Electronic attestation of attributes issued by or on behalf of a public sector body responsible for an authentic source, as defined in Article 3 and Article 45f of Regulation (EU) 2024/1183. |
| Authentic source | A repository or system, held under the responsibility of a public sector body, that contains attributes about a natural person and is considered a primary source of that information or recognised as authentic under Union or national law. For this Rulebook, the authentic source is the issuing institution's official record of studies. |
| Designated public sector body | A public sector body designated under Union or national law to issue PuB-EAAs on behalf of the public sector body responsible for the authentic source. |
| PuB-EAA Provider | The public sector body (responsible or designated) that issues the Micro-credential Attestation and is notified to the Commission under Article 45f(3) of Regulation (EU) 2024/1183. |
| Learner | The natural person to whom the completed learning outcomes apply; the Holder and subject of the attestation. |
| Formal education provider | A higher education institution (HEI), vocational education and training (VET) provider, or other organisation providing formally taught learning under institutional quality assurance. Under this Rulebook, the awarding formal education provider is a public sector body. |
| Learning outcome | What a learner knows, understands, and is able to do on completion of a learning process, as assessed against transparent criteria. |
| ECTS | European Credit Transfer and Accumulation System, used to express notional workload of learning. |
| EQF | European Qualifications Framework, used to express the level of a qualification or learning outcome. |
| ESCO | European Skills, Competences, Qualifications and Occupations classification. |
| ELM | European Learning Model, a multilingual data model for representing learning opportunities, qualifications, and credentials. |
| Technical validity period | The period between `nbf` and `exp` in which the attestation instance can be accepted (ETSI TS 119 472-1). |
| Administrative validity period | The period in which the attested attributes are valid in the administrative sense (ETSI TS 119 472-1). Not used by this Rulebook, since the learning achievement does not lapse. |
| Relying Party | An organisation or system that verifies the Micro-credential Attestation to make an admission, credit-recognition, recruitment, or other eligibility decision. |

### 1.5 Authentic source and legal basis

The authentic source for the Micro-credential Attestation is the official record of studies kept by the public formal education provider that awarded the micro-credential.

For Swedish deployments, the authentic source is the issuing institution's local study documentation, kept in the Ladok system, under:

* Förordning (1993:1153) om redovisning av studier m.m. vid universitet och högskolor (Ordinance on the recording of studies etc. at universities and university colleges); and
* Högskoleförordningen (1993:100) (Higher Education Ordinance).

> **Editor's note.** The identification of the authentic source and the legal basis
> above SHALL be confirmed by legal review before this Rulebook is published. Other
> Member States SHALL state their own authentic source and legal basis in a national
> annex. The legal basis stated here is the one that must be identified in the
> qualified certificate of the PuB-EAA Provider (section 7.6) and in the notification
> under Article 45f(3) of Regulation (EU) 2024/1183.

Where a designated public sector body issues on behalf of the responsible body, the act of designation (Union or national law) SHALL also be identified.

## 2 Compliance

### 2.1 Compliance statement

This Rulebook complies with the applicable requirements of Topic 12, Attestation
Rulebooks, in Annex 2 of the Architecture and Reference Framework, version 3.0.0.
It uses the terminology of Annex 1 of the ARF.

This Rulebook defines a PuB-EAA as referred to in Article 45f and Annex VII of Regulation (EU) 2024/1183. Attestations issued under this Rulebook SHALL comply with Commission Implementing Regulation (EU) 2025/1569, as amended by Commission Implementing Regulation (EU) 2026/1735, and with the SD-JWT VC PuB-EAA profile in ETSI TS 119 472-1 V1.2.1 (clauses 4.2.x.3, 5.2.x.3 and 5.6.3).

The Rulebook supports the following compliance objectives:

* it defines the attestation purpose and scope, aligned with the Council Recommendation of 16 June 2022 on a European approach to micro-credentials for lifelong learning and employability (2022/C 243/02);
* it identifies the authentic source and the legal basis under which the issuer is responsible for it or designated to act on its behalf;
* it defines mandatory, optional, and conditional attributes in an encoding-independent manner, reflecting the standard elements for describing micro-credentials set out in that Recommendation, as further specified by the European Learning Model (ELM) and the European Digital Credentials for Learning (EDC) application profile;
* it contains all data required by Annex VII points (a) to (i) of Regulation (EU) 2024/1183;
* it defines the PuB-EAA category indication through the `category` claim with the value `urn:etsi:esi:eaa:eu:pub`;
* it defines an SD-JWT VC `vct` value for the attestation type, together with SD-JWT VC Type Metadata;
* it defines issuer identification, awarding body, validity, attestation identifier, and status data needed for verification, including a clear distinction between the public sector body that issues and seals the credential and the organisation that awarded the underlying learning achievement;
* it requires a qualified electronic seal or qualified electronic signature supported by a qualified certificate that follows the PSB profile of ETSI TS 119 412-6;
* it defines code lists and integrity rules required for consistent interpretation;
* it defines how trust anchors are obtained from the Commission's list of PuB-EAA providers;
* it defines mandatory revocation, appropriate to a non-lapsing learning achievement, distinguishing technical credential validity from the continued truth of the achievement;
* it supports selective disclosure and data minimisation.

This Rulebook defines an SD-JWT VC encoding only. W3C VCDM encodings are not permitted for PuB-EAA (ARB_01). An ISO/IEC 18013-5 mdoc encoding is not defined in this version.

This Rulebook does not define assurance or quality levels for the Micro-credential Attestation. Where a future version of this Rulebook introduces such levels, Chapters 3 and 4 SHALL be updated accordingly.

This Rulebook does not define transactional or payment-related data. Where a Micro-credential Attestation is used in a transaction involving payment, such requirements SHALL be defined in a separate payment attestation, payment profile, or transaction-specific rulebook.

### 2.2 Regulatory basis

This attestation is an electronic attestation of attributes issued by or on behalf of a
public sector body responsible for an authentic source (PuB-EAA). Article 45f and all
points (a) to (i) of Annex VII of Regulation (EU) 2024/1183 apply. They are mapped as
follows:

| Annex VII point | Content | Satisfied by | Section |
| --- | --- | --- | --- |
| (a) | Indication, suitable for automated processing, that the attestation is a PuB-EAA | `category` = `urn:etsi:esi:eaa:eu:pub` | 3.1, 4.1, 5.1.2 |
| (b) | Data unambiguously representing the issuing public body: Member State, name, and registration number where applicable | Qualified certificate subject (option A) or `issuing_authority`, `issuing_country`, `iss_reg_id` (option B) | 4.6, 7.6 |
| (c) | Data unambiguously representing the entity to which the attested attributes refer; pseudonyms clearly indicated | `givenName`, `familyName`; optionally `sub` or `also_known_as` | 3.2, 3.4 |
| (d) | The attested attributes, including information necessary to identify their scope | Attributes in chapter 3 | 3 |
| (e) | Beginning and end of the validity period | `nbf`, `exp` | 4.1 |
| (f) | Attestation identity code, unique for the issuing body, and indication of the scheme | `jti`; `vct` and scheme registration | 4.1, 2.4 |
| (g) | Qualified electronic signature or qualified electronic seal of the issuing body | JWS signature with qualified seal or signature | 7.6 |
| (h) | Location where the certificate supporting (g) is available free of charge | JOSE header `x5u` (with `x5t#S256`) | 5.1.0, 7.6 |
| (i) | Information or location of services to enquire about validity status | `status` (Token Status List) | 4.1, 8 |

Article 45f(1)(b) (content of the qualified certificate), Article 45f(2) (reliability
equivalent to qualified trust service providers), Article 45f(3) (notification),
Article 45f(4) (revocation cannot be reverted) and Article 45f(8) (interface with EUDI
Wallets) are addressed in sections 7.5, 7.6 and 8.

### 2.3 Traceability

Every applicable requirement mapped to the section that satisfies it. Requirements
marked not applicable carry a stated reason.

| Requirement | Legacy ID | Applies | Satisfied in section | Note |
| --- | --- | --- | --- | --- |
| – | ARB_01 | yes | 5 | PuB-EAA: mdoc or SD-JWT VC only; SD-JWT VC is used |
| EW-DM-12-001 | ARB_01a | no |  | Applies to non-qualified EAA only |
| EW-DM-12-002 | ARB_01b | yes | 5 | SD-JWT VC following the HAIP SD-JWT VC profile |
| EW-DM-12-003 | ARB_02 | yes | 9.2 | Assessed: proximity presentation is not in scope in this version, so mdoc is not required. To be reassessed if offline presentation is needed. |
| EW-DM-12-005 | ARB_04 | no |  | W3C VCDM is not permitted for PuB-EAA |
| EW-DM-12-006 | ARB_05 | yes | 5 | `vct` `https://webuildconsortium.eu/credentials/microcredential/pub/1.0` |
| EW-DM-12-007 | ARB_06 | yes | 3 | Attributes defined independently of encoding |
| EW-DM-12-008 | ARB_06a | no |  | No mdoc encoding is defined in this version |
| EW-DM-12-009 | ARB_06b | yes | 5 | IANA-registered, public and private claim names |
| EW-DM-12-010 | ARB_07 | yes | 3 | Attributes aligned to the European Learning Model |
| EW-DM-12-012 | ARB_09 | yes | 3, 4 | Mandatory, optional and conditional stated per attribute |
| EW-DM-12-013 | ARB_10 | no |  | No domestic namespace is defined |
| EW-DM-12-014 | ARB_11 | yes | 3.1, 4.1 | Annex VII point (a): `category` = `urn:etsi:esi:eaa:eu:pub` |
| EW-DM-12-015 | ARB_12 | no |  | Applies to non-qualified EAA only |
| EW-DM-12-017 | ARB_14 | yes | 4.6, 7.6 | Annex VII point (b) |
| EW-DM-12-016 / EW-DM-12-018 | ARB_13 / ARB_15 | no |  | Apply to QEAA and non-qualified EAA respectively |
| EW-DM-12-019 | ARB_16 | yes | 3.2, 3.4 | Annex VII point (c) |
| EW-DM-12-020 | ARB_17 | no |  | Applies to non-qualified EAA only |
| EW-DM-12-021 | ARB_18 | yes | 4.1 | Annex VII point (e): `nbf`, `exp` |
| EW-DM-12-022 | ARB_19 | no |  | Applies to non-qualified EAA only |
| EW-DM-12-023 | ARB_20 | yes | 5.1.0, 7.6, 10 | Annex VII point (h): `x5u` |
| EW-DM-12-024 | ARB_21 | no |  | Applies to non-qualified EAA only |
| – | ARB_23 | yes | 8 | Attestation Status List (Token Status List) |
| – | ARB_24a | yes | 8 | Status list URL specified |
| EW-DM-12-029 | ARB_25 | yes | 3.1, 4.1, 4.3 | `category` per Rulebook template v1.5; `attestation_legal_category` kept as a transitional conditional claim, see 4.3 |
| EW-DM-12-030 | ARB_26 | no |  | Applies to non-qualified EAA; trust anchors for PuB-EAA come from the Commission's list (chapter 10) |
| EW-DM-12-031 | ARB_27 | yes | 4.3 | `cryptographically_bound_to` where presented with PID |
| EW-DM-12-032 | ARB_28 | yes | 4.3 | `cryptographically_bound_to` is defined as conditional |
| – | ARB_29 | yes | all | Structure follows the Rulebook template |
| EW-DM-12-034 | ARB_30 | yes | 5 | Selective disclosability stated per claim |
| EW-DM-12-035 | ARB_31 | yes | 3.1, 5.1 | SD-JWT VC Type Metadata is defined; `vct#integrity` is required by ETSI TS 119 472-1 |
| – | ARB_33 | yes | 2.4 | Scheme registration references this Rulebook |
| EW-DM-12-038 | ARB_34 | yes | 7.1 | Device binding |
| Annex VII (f) | – | yes | 4.1, 2.4 | `jti` and scheme indication |
| Annex VII (g) | – | yes | 7.6 | Qualified electronic seal or signature |
| Annex VII (i) | – | yes | 4.1, 8 | `status` |
| Art. 45f(1)(b) | – | yes | 7.6 | Content of the qualified certificate |
| Art. 45f(2), (3) | – | yes | 7.5 | Reliability and notification |
| Art. 45f(4) | – | yes | 8 | No reversion after revocation |
| Art. 45f(8) | – | yes | 7.5 | Interface with EUDI Wallets |

### 2.4 Registration in the catalogue of attestation schemes

The scheme defined by this Rulebook SHALL be registered in the Commission's catalogue of schemes for the attestation of attributes, in accordance with Article 8 of Commission Implementing Regulation (EU) 2025/1569. The registration SHALL reference this Rulebook (ARB_33) and SHALL contain at least:

* the name of the scheme, unique within the catalogue;
* the name and contact information of the scheme owner;
* the status and version of the scheme;
* references to the laws, standards and guidelines that apply, including those listed in sections 1.5 and 2.1;
* the format: SD-JWT VC;
* the namespace, attribute identifiers, semantic descriptions and data types of each attribute, by reference to the catalogue of attributes where possible;
* a description of the trust model and governance, including the revocation mechanism (chapters 8 and 10);
* the requirements on PuB-EAA Providers and on the authentic sources on which they rely (sections 1.5 and 7.5);
* a statement that attestations within the scope of the scheme are issued as electronic attestations of attributes issued by or on behalf of a public sector body responsible for an authentic source.

Only attributes identifiable by unique identifiers SHALL be part of the scheme. The registration request SHALL be signed or sealed with a qualified electronic signature or seal, or an advanced electronic signature or seal based on a qualified certificate.

Under Article 3(2) of Commission Implementing Regulation (EU) 2025/1569, PuB-EAA Providers issuing attestations of this scheme SHALL comply with its requirements. Their policies and procedures for doing so are part of the conformity assessment.

Together with `vct`, the registered scheme forms the indication of the scheme of attestations required by Annex VII point (f).

## 3 Attestation attributes

This chapter defines the attributes and metadata that a Micro-credential Attestation may contain. The attributes are defined in an encoding-independent manner. Each attribute is classified as mandatory, optional, or conditional.

The Micro-credential Attestation records a completed, formally assessed learning achievement. Unlike affiliation-based attestations, the underlying fact it attests does not lapse over time. Any validity period defined in this Rulebook concerns the technical validity of the credential instance, not the continued truth of the achievement. The attribute set reflects the standard elements for describing micro-credentials set out in the Council Recommendation of 16 June 2022 (2022/C 243/02), as further specified by the European Learning Model (ELM) and the European Digital Credentials for Learning (EDC) application profile. It supports data minimisation by allowing a Holder to disclose only the attributes required for a specific transaction.

### 3.1 Introduction

The Micro-credential Attestation is defined as a PuB-EAA.

The claim `category` SHALL be included and SHALL have the value `urn:etsi:esi:eaa:eu:pub` (ETSI TS 119 472-1, PuB-EAA-5.2.2.3-01/02). This claim provides the indication required by Annex VII point (a) and replaces `attestation_legal_category` (EUDI Attestation Rulebook Template v1.5). For the transitional use of `attestation_legal_category`, see section 4.3.

The attestation model consists of the following logical groups:

* credential identification attributes;
* issuer identification data (section 4.6) and awarding body attributes;
* learner identity attributes for holder matching;
* learning achievement attributes (outcomes, level, workload, assessment, participation);
* classification and taxonomy references;
* quality assurance and accreditation attributes;
* credential metadata.

Consistent with the European Learning Model, the public sector body that issues and seals the credential (the PuB-EAA Provider, identified as described in section 4.6) and the organisation that awarded the underlying learning achievement (see `awardingBody`) may or may not be the same organisation. A designated public sector body may seal credentials on behalf of the responsible body. The ELM attribute `issuerCountry` describes the country of the sealing organisation in the ELM sense. It does not satisfy Annex VII point (b).

All attributes in the attestation SHALL refer to the subject of the attestation, the Learner (ETSI TS 119 472-1, PuB-EAA-5.2.5.6-01). Attributes such as `awardingBody` and `accreditation` describe the Learner's achievement and are not attributes about another entity. The `subAttrs` claim of ETSI TS 119 472-1 SHALL NOT be used.

The attestation is issued as a Verifiable Credential compatible with the EUDI Wallet using SD-JWT VC. The model aligns with the following issuer metadata parameters:

* `scope`: `MicroCredentialPub`;
* `format`: `dc+sd-jwt`;
* `vct`: `https://webuildconsortium.eu/credentials/microcredential/pub/1.0`;
* `claims`: the claims defined in this Rulebook;
* `proof_types_supported`: issuer-defined, including `jwt` where supported;
* `cryptographic_binding_methods_supported`: issuer-defined, for example `jwk`.

> **Note on format identifier.** Version 1.0 of this Rulebook used `vc+sd-jwt`. Current
> versions of OpenID4VCI, SD-JWT VC and HAIP use `dc+sd-jwt`. The value SHALL be aligned
> with the HAIP version referenced in chapter 11 before publication.

> **Schema artefacts.** A machine-readable SD-JWT VC Type Metadata document and a
> JSON Schema SHALL be published for this attestation type, versioned and immutably
> addressable under `data-schemas/`. `vct` SHALL resolve to the Type Metadata, and the
> attestation SHALL contain `vct#integrity` (ETSI TS 119 472-1, EAA-5.2.1.2-01–03). The
> Type Metadata SHOULD contain Claim Selective Disclosure Metadata for each claim
> (ARB_31). Producing these artefacts is a prerequisite for publication of this version.

### 3.2 Mandatory attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| `identifier` | ELM `credential.identifier` | Unique identifier of the micro-credential achievement, assigned by the awarding body. Distinct from the attestation identity code `jti` (section 4.1). | string | `MC-2026-0007421` |
| `title` | ELM `credential.displayParameter.title` / Council Recommendation standard element 2 | Title of the micro-credential. | string | `Introduction to Applied Data Ethics` |
| `givenName` | ELM `credential.credentialSubject.givenName` / Council Recommendation standard element 1 / Annex VII (c) | Learner given name. | string | `Elena` |
| `familyName` | ELM `credential.credentialSubject.familyName` / Council Recommendation standard element 1 / Annex VII (c) | Learner family name. | string | `Kowalska` |
| `issuerCountry` | ELM `credential.issuer.location.address.countryCode.prefLabel` / Council Recommendation standard element 3 | Country or region of the organisation that sealed the credential, in the ELM sense. May differ from the awarding body's country. Does not satisfy Annex VII (b); see section 4.6. | string [code list: country] | `http://publications.europa.eu/resource/authority/country/SWE` |
| `awardingBody` | ELM `credential.credentialSubject.hasClaim[0].awardedBy.awardingBody[0].legalName` / Council Recommendation standard element 4 | Name and identifier of the public formal education provider that awarded the micro-credential. The awarding body SHALL be a public sector body responsible for the authentic source, or a body on whose behalf a designated public sector body issues. | object | `{"legalName":"Linköping University","legalIdentifier":"999852236"}` |
| `issuanceDate` | ELM `credential.issued` / Council Recommendation standard element 5 | Date on which the credential was sealed and issued. Distinct from any validity start date. | date (ISO 8601) | `2026-06-15` |
| `learningOutcomes` | ELM `credential.credentialSubject.hasClaim[0].specifiedBy.learningOutcome` / Council Recommendation standard element 7 | Description of the learning outcomes acquired by the learner. | array of objects | `[{"title": "The title of the learning outcome", "description": "The actual learning outcome"}]` |
| `ECTS` | ELM `credential.credentialSubject.hasClaim[0].specifiedBy.creditPoint[0].point` / Council Recommendation standard element 8 | Notional workload in ECTS credits. Mandatory for formal learning; see section 3.4. | float | 3.0 |
| `typeOfAssessment` | ELM `credential.credentialSubject.hasClaim[0].specifiedBy.provenBy[0].dcType` / Council Recommendation standard element 9 | Type of assessment used to validate the learning outcomes. | array of strings [code list: typeOfAssessment] | `["http://data.europa.eu/snb/assessment/6e6cb2cc78","http://data.europa.eu/snb/assessment/6a4db9f11d"]` |
| `formOfParticipation` | ELM `credential.credentialSubject.hasClaim[0].specifiedBy.influencedBy[0].mode` / Council Recommendation standard element 10 | Form of participation in the learning activity. | string [code list: formOfParticipation] | `http://data.europa.eu/snb/learning-assessment/920fbb3cbe` |
| `qualityAssurance` | ELM Accreditation `dcType` / Council Recommendation standard element 11 | Type of quality assurance used to underpin the micro-credential. | string | `institutional-accreditation` |

The category indication (`category`) and the metadata required by Annex VII are defined in chapter 4.

### 3.3 Optional attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| `dateOfBirth` | ELM `credential.credentialSubject.dateOfBirth` | Learner date of birth. | date | `1998-11-02` |
| `placeOfBirth` | ELM `credential.credentialSubject.placeOfBirth.address[0].fullAddress.noteLiteral` | Learner place of birth. | string | `Kraków, Poland` |
| `citizenshipCountry` | ELM `credential.credentialSubject.citizenshipCountry.prefLabel` | Learner country of citizenship. | string (ISO 3166-1 alpha-2) | `PL` |
| `nationalID` | ELM `credential.credentialSubject.nationalID.notation` | National or other government-issued identifier of the learner. | string | issuer-defined |
| `registeredAddress` | ELM `credential.credentialSubject.location.address[0].fullAddress.noteLiteral` | Learner's registered or contact address. | string | issuer-defined |
| `mail` | RFC 5322 mailbox / ELM `credential.credentialSubject.contactPoint.emailAddress` | Learner email address. | string | `elena.kowalska@example.edu` |
| `level` | ELM `credential.credentialSubject.hasClaim[0].specifiedBy.eqfLevel.prefLabel` | Level of the learning outcomes, expressed against the EQF or an applicable national or sectoral framework, where applicable. | string | `EQF-6` |
| `nationalQualificationsFrameworkLevel` | ELM `credential.credentialSubject.hasClaim[0].specifiedBy.nqfLevel[0].prefLabel` | Level expressed against a national or regional qualifications framework, where used instead of or alongside the EQF. | string | issuer-defined |
| `educationLevelDescriptor` | ELM `credential.credentialSubject.hasClaim[0].specifiedBy.educationLevel` | Framework-independent descriptor of the learning experience level. | string | `intermediate` |
| `learningOutcomeSummary` | ELM `credential.credentialSubject.hasClaim[0].specifiedBy.learningOutcomeSummary` | Free-text collective description of the learning outcomes, complementing the structured `learningOutcomes` list. | string | `Applies ethical reasoning to real-world data science scenarios.` |
| `fieldOfEducation` | ISCED-F 2013 | Field of education or training classification code. | string | `0613` |
| `escoReference` | ELM `credential.credentialSubject.hasClaim[0].specifiedBy.learningOutcome[0].relatedESCOSkill[0].prefLabel` | One or more references to the ESCO classification of the skill or competence attested. | array of strings | `["http://data.europa.eu/esco/skill/abc12345"]` |
| `learningActivityType` | ELM `credential.credentialSubject.hasClaim[0].specifiedBy.influencedBy[0].dcType` | Categorisation of the learning activity, e.g. classroom coursework, e-learning, internship, volunteering. | string | `e-learning` |
| `languageOfAssessment` | ELM / BCP 47 | Language in which the assessment was conducted. | string (BCP 47) | `en` |
| `idVerificationMethod` | ELM `credential.credentialSubject.hasClaim[0].specifiedBy.provenBy[0].idVerification` | Method used to supervise the assessment and verify the identity of the learner during assessment. | string | `proctored-online-exam` |
| `grade` | ELM `credential.credentialSubject.hasClaim[0].provenBy[0].grade` | Grade or result obtained in the assessment, where the type of assessment produces one. | string | `Pass` |
| `gradingScheme` | ELM Grading Scheme property | Description of the grading scheme, enabling a third party to interpret the disclosed `grade`. | string | `Pass/Fail` |
| `entryRequirements` | ELM `credential.credentialSubject.hasClaim[0].specifiedBy.entryRequirement` | Prerequisites the learner needed to fulfil to enrol in the learning activity. | array of strings | `["Beginner-level Python programming"]` |
| `stackable` | ELM `hasClaim[0].hasPart` / `isPartOf` relationship indicator | Indicates whether the micro-credential is designed to stack towards a larger qualification or award. | boolean | `true` |
| `partOfQualification` | ELM `isPartOf` relationship indicator | Identifier or title of the larger qualification or credential that this micro-credential can contribute towards. | string | `BSc Data Science, Linköping University` |
| `accreditation` | ELM Accreditation class | Structured accreditation details underpinning `qualityAssurance`: title, type, accrediting agent, decision, decision date, review date, and any field/jurisdiction/EQF-level limits on the accreditation's scope. | object | `{ "title": "Institutional Accreditation 2024", "type": "institutional-accreditation", "accreditingAgent": "Swedish Higher Education Authority", "decision": "approved", "decisionDate": "2024-01-15", "reviewDate": "2029-01-15" }` |
| `awardingBodyAddress` | ELM `awardingBody[0].location[0].address[0].fullAddress.noteLiteral` | Registered or contact address of the awarding body. | string | issuer-defined |
| `awardingBodyHomepage` | ELM `awardingBody[0].homepage` | Homepage URL of the awarding body. | string | `https://liu.se` |
| `awardingBodyIdentifier` | ELM `awardingBody[0].identifier[0].notation` | Additional identifier(s) for the awarding body, e.g. a national registry or ROR identifier. | string | issuer-defined |
| `additionalNote` | ELM `additionalNote` (generic) | Free-text field for information not covered by another attribute in this Rulebook. | string | issuer-defined |

### 3.4 Conditional attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| `ECTS` | ELM `credential.credentialSubject.hasClaim[0].specifiedBy.creditPoint[0].point` | SHALL be included for formal learning. SHALL NOT be included where `volumeOfLearning` is present. | float | 3.0 |
| `volumeOfLearning` | ELM `credential.credentialSubject.hasClaim[0].specifiedBy.volumeOfLearning` | Notional workload for non-formal learning, as an ISO 8601 duration. MAY be included only where the authentic source identified in section 1.5 records such learning. SHALL NOT be included where `ECTS` is present. | string (ISO 8601) | `PT8H` |
| `sub` | SD-JWT VC / ETSI TS 119 472-1 EAA-5.2.5.1 | Subject identifier. MAY be included as an alternative or complement to `givenName`/`familyName` for Annex VII (c). If included, it SHALL NOT be a pseudonym. | string | issuer-defined |
| `also_known_as` | ETSI TS 119 472-1 EAA-5.2.5.2 | Pseudonym of the subject. SHALL be used, instead of `sub`, if the subject is represented by a pseudonym, so that the pseudonym is clearly indicated (Annex VII (c)). This version of the Rulebook does not foresee pseudonymous issuance. | string | – |
| `dateOfBirth` | ELM `credential.credentialSubject.dateOfBirth` | SHALL be included only where needed for holder matching, or another justified relying-party purpose. If included, it SHALL represent the subject's birth date and SHALL NOT be in the future. | date | `1998-11-02` |
| `level` | ELM `eqfLevel` | SHALL be included where the learning experience leading to the micro-credential can be positioned within the EQF or an applicable national or sectoral level framework; MAY be omitted where no such framework applies. | string | `EQF-6` |
| `grade` | ELM `provenBy[0].grade` | SHALL be included where `typeOfAssessment` produces a grade or result, and SHALL be omitted where the assessment is pass/fail-only without a graded outcome. Where `grade` is present, `gradingScheme` SHOULD also be included. | string | `Pass` |
| `escoReference` | ELM `relatedESCOSkill` | SHOULD be included where the attested learning outcomes can be mapped to one or more ESCO skills or competences. | array of strings | `["http://data.europa.eu/esco/skill/abc12345"]` |
| `stackable` | ELM `hasPart` / `isPartOf` | SHOULD be included where the awarding body has defined a stacking pathway for this micro-credential towards a larger qualification. | boolean | `true` |
| `partOfQualification` | ELM `isPartOf` | SHOULD be included where `stackable` is `true`. | string | `BSc Data Science, Linköping University` |

## 4 Metadata

Metadata describes the attestation rather than its subject.

### 4.1 Mandatory metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| `vct` | SD-JWT VC / ETSI TS 119 472-1 EAA-5.2.1.2 | Verifiable Credential Type identifying this attestation type. SHALL resolve to the SD-JWT VC Type Metadata of this attestation type. | string | `https://webuildconsortium.eu/credentials/microcredential/pub/1.0` |
| `vct#integrity` | SD-JWT VC / ETSI TS 119 472-1 EAA-5.2.1.2 | Integrity hash of the Type Metadata document. | string | `sha256-...` |
| `category` | ETSI TS 119 472-1 PuB-EAA-5.2.2.3 / Annex VII (a) | Indication that the attestation is a PuB-EAA. | string | `urn:etsi:esi:eaa:eu:pub` |
| `iss` | SD-JWT VC / JWT | Identifier of the issuer (the PuB-EAA Provider). SHALL be consistent with the subject of the qualified certificate (section 4.6). | string | `https://issuer.example-university.se` |
| `iat` | JWT / ETSI TS 119 472-1 EAA-5.2.6 | Time at which the credential was issued. | integer | `1781740800` |
| `nbf` | JWT / ETSI TS 119 472-1 EAA-5.2.7.1 / Annex VII (e) | Beginning of the technical validity period. | integer | `1781740800` |
| `exp` | JWT / ETSI TS 119 472-1 EAA-5.2.7.1 / Annex VII (e) | End of the technical validity period. Reflects the technical validity of the credential instance, not the continued truth of the underlying achievement. | integer | `1813276800` |
| `jti` | JWT / ETSI TS 119 472-1 EAA-5.2.3 / Annex VII (f) | Attestation identity code, unique for the issuing PuB-EAA Provider. SHALL be a UUID URN. | string | `urn:uuid:9a3f6b2e-1c44-4b8a-9e21-6f0a2d7c5b31` |
| `status` | IETF Token Status List / ETSI TS 119 472-1 PuB-EAA-5.2.10.3 / Annex VII (i) | Status information enabling revocation checks. SHALL be present, since attestations of this type are not short-lived (chapter 8). | object | `{ "status_list": { "idx": 4711, "uri": "https://status.example-university.se/lists/1" } }` |
| `cnf` | SD-JWT VC / JOSE / ETSI TS 119 472-1 EAA-5.5 | Confirmation claim binding the credential to key material controlled by the Holder or Wallet Unit, where holder binding is used. | object | `{ "jwk": { ... } }` |

The signature data required by Annex VII points (g) and (h) is carried in the JWS protected header (`x5u`, `x5t#S256`, `x5c`), as defined in sections 5.1.0 and 7.6.

**Legal category.** The legal category is indicated by `category` with the value
`urn:etsi:esi:eaa:eu:pub`, in line with ETSI TS 119 472-1 and the EUDI Attestation
Rulebook Template v1.5. This resolves the open point recorded in version 1.0 of this
Rulebook. ARB_25 (EW-DM-12-029) of ARF v3.0.0 still names `attestation_legal_category`;
the transitional handling is defined in section 4.3.

### 4.2 Optional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| `adm_nbf` / `adm_exp` | ETSI TS 119 472-1 EAA-5.2.7.2 | Administrative validity period. NOT used by this Rulebook, since the learning achievement does not lapse. If a future version uses them, both SHALL be present or neither. | integer | – |

### 4.3 Conditional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| `issuing_authority` | ETSI TS 119 472-1 EAA-5.2.4.1, PuB-EAA-5.2.4.3-01 / Annex VII (b) | Name of the issuing public sector body. SHALL be included if the qualified certificate is not incorporated in the `x5c` header (option B, section 4.6). SHALL NOT be included if it is. | string | `Linköpings universitet` |
| `issuing_country` | ETSI TS 119 472-1 EAA-5.2.4.1, PuB-EAA-5.2.4.3-02 / Annex VII (b) | Member State in which the issuing public sector body is established. Same condition as `issuing_authority`. | string (ISO 3166-1 alpha-2) | `SE` |
| `iss_reg_id` | ETSI TS 119 472-1 EAA-5.2.4.1, PuB-EAA-5.2.4.3-03/04 / Annex VII (b) | Registration number of the issuing public sector body as stated in official records, built as an organizationIdentifier per ETSI EN 319 412-1 clause 5.1.4. Same condition as `issuing_authority`. | string | `NTRSE-xxxxxxxxxx` |
| `attestation_legal_category` | ARF Topic 12 ARB_25 (ARF v3.0.0) | Transitional. SHALL be included with the value `PuB-EAA` only where a deployment needs to claim conformance with ARB_25 of ARF v3.0.0. SHALL NOT be used as a substitute for `category`. To be removed when the ARF aligns with ETSI TS 119 472-1. | string | `PuB-EAA` |
| `cryptographically_bound_to` | ARF Topic 12 / ARB_28 | SHALL be present where the Micro-credential Attestation must be presented together with PID or another identity attestation for strong holder matching. | string | `urn:eudi:pid:1` |

`shortLived` (ETSI TS 119 472-1 EAA-5.2.12) and `oneTime` (EAA-5.2.8.2) SHALL NOT be used by this Rulebook.

### 4.4 Code lists

| **Field name** | **Allowed values** | **Meaning** | **Source / vocabulary** | **Notes / extensibility** |
| --- | --- | --- | --- | --- |
| `category` | `urn:etsi:esi:eaa:eu:pub` | Indication that the attestation is a PuB-EAA. | ETSI TS 119 472-1 PuB-EAA-4.2.2.3-02 | Fixed value for this Rulebook. |
| `attestation_legal_category` | `PuB-EAA` | Transitional legal category indication. | ARF Topic 12 / Rulebook template | Transitional only; see 4.3. |
| `issuing_country` | ISO 3166-1 alpha-2 codes of EU Member States | Member State of establishment of the issuer. | ISO 3166-1 | – |
| `country` | Identifier from the item in the list | A country | https://op.europa.eu/en/web/eu-vocabularies/concept-scheme/-/resource?uri=http://publications.europa.eu/resource/authority/country | Used by `issuerCountry` (ELM). |
| `typeOfAssessment` | Identifier from the item in the list | Type of assessment used to validate learning outcomes. | https://op.europa.eu/en/web/eu-vocabularies/concept-scheme/-/resource?uri=http://data.europa.eu/snb/assessment/25831c2 | Issuers SHOULD reuse an existing value before introducing a new one. |
| `formOfParticipation` | Identifier from the item in the list | Mode in which the learner participated in the learning activity. | https://op.europa.eu/en/web/eu-vocabularies/concept-scheme/-/resource?uri=http://data.europa.eu/snb/learning-assessment/25831c2 | – |
| `level` | `EQF-1` through `EQF-8` | Level of the learning outcomes against the EQF. | European Qualifications Framework (EQF) controlled vocabulary | Where a national or sectoral framework is used instead, use `nationalQualificationsFrameworkLevel` and/or `educationLevelDescriptor`. |
| `educationLevelDescriptor` | `beginner`, `intermediate`, `advanced`, issuer-defined | Framework-independent level descriptor. | Issuer-defined, informed by ELM | – |
| `ECTS` / `volumeOfLearning` | positive number / ISO 8601 duration | Notional workload. | ECTS (EQF Recommendation Annex V) / ISO 8601 | HEIs SHALL use ECTS for formal learning. |
| `learningActivityType` | `classroom-coursework`, `e-learning`, `internship`, `volunteering`, issuer-defined | Category of learning activity. | EU "Learning activity type" multilingual controlled vocabulary, or issuer-defined | – |
| `idVerificationMethod` | `proctored-online-exam`, `in-person-supervision`, `identity-verified-remote-exam`, issuer-defined | Method used to supervise assessment and verify learner identity. | EU "Method of supervision and verification" multilingual controlled vocabulary, or issuer-defined | – |
| `qualityAssurance` / `accreditation.type` | `institutional-accreditation`, `programme-accreditation`, `national-quality-agency`, `sectoral-quality-assurance`, issuer-defined | Type of quality assurance underpinning the micro-credential. | Issuer-defined, informed by ELM Accreditation class and DEQAR | – |
| `fieldOfEducation` | ISCED-F 2013 codes | Field of education or training. | ISCED-F 2013 | – |
| `status` list values | `0x00` VALID, `0x01` INVALID | Status of the attestation in the Token Status List. | IETF Token Status List | `0x02` SUSPENDED SHALL NOT be used (Art. 45f(4)). |

### 4.5 Integrity rules

| **Rule ID** | **Rule statement** | **Why it exists** | **Where enforced** | **Verifier / issuer behavior on failure** |
| --- | --- | --- | --- | --- |
| `MC-IR-01` | `identifier`, `title`, `givenName`, `familyName`, `issuerCountry`, `awardingBody`, `issuanceDate`, `learningOutcomes`, `ECTS` or `volumeOfLearning`, `typeOfAssessment`, `formOfParticipation`, and `qualityAssurance` SHALL be present. | Ensures the credential contains all standard elements required by the Council Recommendation on micro-credentials. | Issuer business rules, schema validation, verifier business validation. | Issuer SHALL reject incomplete credential data. Verifier SHALL treat the attestation as invalid or insufficient if mandatory claims are missing. |
| `MC-IR-02` | If `dateOfBirth` is included, it SHALL represent the subject's birth date and SHALL NOT be in the future. | Prevents invalid identity data and supports correct holder-matching checks. | Issuer business rules and verifier business validation. | Issuer SHALL reject invalid dates. Verifier SHALL reject or ignore an invalid `dateOfBirth` claim depending on the transaction. |
| `MC-IR-03` | `issuanceDate` SHALL NOT be in the future and SHALL NOT precede the completion of the assessment underlying the micro-credential. | Ensures the awarded date reflects a genuinely completed and assessed learning activity. | Issuer business rules. | Issuer SHALL reject issuance where this cannot be confirmed. |
| `MC-IR-04` | If `grade` is present, `typeOfAssessment` SHALL indicate an assessment type capable of producing a graded outcome, and `gradingScheme` SHOULD also be present. | Prevents inconsistent or uninterpretable grading information. | Issuer business rules and verifier business validation. | Issuer SHALL NOT include `grade` inconsistent with the assessment type. Verifier MAY disregard an inconsistent or unexplained `grade` claim. |
| `MC-IR-05` | If `escoReference` values are included, each SHALL resolve to a valid ESCO skill or competence URI. | Ensures semantic interoperability of skill references. | Issuer business rules and schema validation. | Issuer SHOULD validate references before issuance. Verifier MAY ignore unresolvable references. |
| `MC-IR-06` | `ECTS` SHALL be a positive number, and `ECTS` SHALL NOT be used together with `volumeOfLearning`. | Ensures workload information is meaningful and consistently interpretable. | Issuer business rules and schema validation. | Issuer SHALL reject the credential if `ECTS` and `volumeOfLearning` are both present. |
| `MC-IR-07` | `volumeOfLearning` SHALL be an ISO 8601 duration, and `volumeOfLearning` SHALL NOT be used together with `ECTS`. | Ensures workload information is meaningful and consistently interpretable. | Issuer business rules and schema validation. | Issuer SHALL reject the credential if `ECTS` and `volumeOfLearning` are both present. |
| `MC-IR-08` | If `stackable` is `true`, `partOfQualification` SHOULD be present. | Ensures a stated stacking intent is backed by an identifiable target qualification. | Issuer business rules. | Issuer SHOULD include the target qualification. Verifier MAY treat an unsupported stackability claim with reduced confidence. |
| `MC-IR-09` | If `accreditation` is present, its `type` value SHALL be consistent with the top-level `qualityAssurance` value. | Prevents contradictory quality-assurance information within a single credential. | Issuer business rules and schema validation. | Issuer SHALL ensure consistency before issuance. Verifier MAY disregard an internally inconsistent `accreditation` claim. |
| `MC-IR-10` | Selective disclosure SHALL allow the Holder to reveal only the attributes required for the transaction. | Supports privacy and data minimisation. | Issuer credential construction and Wallet presentation logic. | Verifier SHALL request only necessary claims. Wallet SHOULD allow the Holder to review the disclosed claims. |
| `MC-IR-11` | `category` SHALL be present with the value `urn:etsi:esi:eaa:eu:pub`. | Annex VII (a); allows automated identification as PuB-EAA. | Issuer credential construction; verifier validation. | Verifier SHALL NOT treat the attestation as a PuB-EAA if `category` is missing or has another value. |
| `MC-IR-12` | `nbf` and `exp` SHALL be present, and `nbf` ≤ `exp`. `iat` ≤ `nbf` is RECOMMENDED. | Annex VII (e); unambiguous technical validity period. | Issuer credential construction; verifier validation. | Verifier SHALL reject the attestation outside its validity period or if `nbf` or `exp` is missing. |
| `MC-IR-13` | `jti` SHALL be present and unique for the issuing PuB-EAA Provider. | Annex VII (f). | Issuer business rules. | Issuer SHALL NOT reuse a `jti`. Verifier SHALL reject the attestation if `jti` is missing. |
| `MC-IR-14` | `status` SHALL be present. Once a status list entry has been set to INVALID, it SHALL never be set back to VALID. | Annex VII (i); Art. 45f(4). | Issuer status management; verifier status check. | Verifier SHALL reject the attestation if `status` is missing or indicates INVALID. |
| `MC-IR-15` | The issuer identification data (qualified certificate subject, or `issuing_authority`, `issuing_country` and `iss_reg_id`) SHALL satisfy Annex VII (b). The claims SHALL NOT be present if `x5c` is included. `iss` and the issuer data SHALL be consistent with the qualified seal certificate. | Annex VII (b); ETSI TS 119 472-1 EAA-5.2.4.1-03/07/11. | Issuer credential construction; verifier validation. | Verifier SHALL reject the attestation if the issuer cannot be identified or is inconsistent with the certificate. |
| `MC-IR-16` | All attributes SHALL refer to the subject of the attestation. `subAttrs` SHALL NOT be used. | ETSI TS 119 472-1 PuB-EAA-5.2.5.6-01. | Issuer credential construction. | Verifier SHALL reject an attestation containing `subAttrs`. |

### 4.6 Issuer identification

Annex VII point (b) requires data unambiguously representing the issuing public sector body, including at least the Member State in which it is established, its name and, where applicable, its registration number as stated in official records. The PuB-EAA Provider SHALL provide this data using one of the following options and SHALL declare the chosen option in its issuer metadata and EAAS practice statement.

**Option A (RECOMMENDED): qualified certificate.** The qualified certificate supporting the seal or signature is included in the `x5c` protected header parameter. The issuer data is read from the certificate subject: countryName (C), organizationName (O) and organizationIdentifier. In this case `issuing_authority`, `issuing_country` and `iss_reg_id` SHALL NOT be included as claims (ETSI TS 119 472-1 EAA-5.2.4.1-03/07/11).

**Option B: claims.** The `x5c` header parameter is not included, and `issuing_authority`, `issuing_country` and `iss_reg_id` (where a registration number exists) SHALL be included as defined in section 4.3. They are not selectively disclosable.

In both options, `iss` SHALL be consistent with the identity of the PuB-EAA Provider in the qualified certificate, and the issuing public sector body SHALL be the one notified under Article 45f(3) of Regulation (EU) 2024/1183.

The ELM attribute `issuerCountry` does not satisfy Annex VII (b), because it uses the EU country vocabulary rather than ISO 3166-1 alpha-2 and describes the sealing organisation in the ELM sense.

## 5 Formats

| Format | Supported | Identifier | Specification | Notes |
| --- | --- | --- | --- | --- |
| ISO/IEC 18013-5 mdoc | no |  | [ISO/IEC 18013-5] | Not defined in this version; see section 5.2 |
| SD-JWT VC | yes | `vct` `https://webuildconsortium.eu/credentials/microcredential/pub/1.0` | [SD-JWT VC], [HAIP], [ETSI TS 119 472-1] clause 5 | Follows SD-JWT VC, HAIP and the ETSI PuB-EAA profile |
| W3C VCDM | no |  | [W3C VCDM v2.0] | Not permitted for PuB-EAA (ARB_01); see section 5.3 |

### 5.1 SD-JWT VC-based encoding

The Micro-credential Attestation SHALL be issued as an SD-JWT VC that complies with the SD-JWT VC profile in [HAIP] and with the PuB-EAA requirements of clause 5 of [ETSI TS 119 472-1].

The Verifiable Credential Type (`vct`) for this attestation type is:

```text
https://webuildconsortium.eu/credentials/microcredential/pub/1.0
```

The `vct` value differs from that of the non-qualified EAA version of this Rulebook, because the two attestation types have different rules (ARB_05).

The credential claims defined in this section SHALL follow SD-JWT VC and HAIP conventions where applicable. Claim names are either IANA-registered JWT claims, claims defined in ETSI TS 119 472-1, public or reusable names, or private names specific to this attestation type.

For all claims, this Rulebook specifies whether an Attestation Provider MUST, MAY, or MUST NOT make the claim selectively disclosable.

#### 5.1.0 JWS protected header

| **Header parameter** | **Status** | **Value / notes** | **Reference** |
| --- | --- | --- | --- |
| `alg` | SHALL | Signature algorithm per HAIP and compliant with ENISA's Agreed Cryptographic Mechanisms, e.g. `ES256`. | [HAIP]; CIR 2025/1569 Annex I |
| `typ` | SHALL | `dc+sd-jwt` | [SD-JWT VC] |
| `x5u` | SHALL | URL at which the qualified certificate supporting the seal or signature is available free of charge (Annex VII (h)). | ETSI TS 119 472-1 PuB-EAA-5.6.3-02 |
| `x5t#S256` | SHALL | base64url-encoded SHA-256 thumbprint of the qualified certificate. | ETSI TS 119 472-1 PuB-EAA-5.6.3-02 |
| `x5c` | SHOULD | Qualified certificate and, where applicable, intermediate CA certificates. Determines the issuer identification option (section 4.6). | ETSI TS 119 472-1 PuB-EAA-5.6.3-03 |

#### 5.1.1 IANA-registered and standard JWT / SD-JWT VC claims

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Reference/Notes** | **Disclosable** |
| --- | --- | --- | --- | --- |
| `iss` | `iss` | string | JWT issuer identifier. | MUST NOT |
| `iat` | `iat` | integer | Issued-at timestamp. | MUST NOT |
| `nbf` | `nbf` | integer | Not-before timestamp. Mandatory. | MUST NOT |
| `exp` | `exp` | integer | Expiration timestamp. Mandatory. Reflects technical validity of the credential instance only. | MUST NOT |
| `jti` | `jti` | string | Attestation identity code. Mandatory. | MUST NOT |
| `sub` | `sub` | string | Subject identifier, where used (section 3.4). | MAY |
| `cnf` | `cnf` | object | Holder binding confirmation claim, where used. | MUST NOT |
| `status` | `status` | object | Token Status List reference. Mandatory. | MUST NOT |
| `vct` | `vct` | string | SD-JWT VC type. Value SHALL be `https://webuildconsortium.eu/credentials/microcredential/pub/1.0`. | MUST NOT |
| `vct#integrity` | `vct#integrity` | string | Integrity of the Type Metadata. Mandatory. | MUST NOT |

#### 5.1.2 Claims defined in ETSI TS 119 472-1

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Reference/Notes** | **Disclosable** |
| --- | --- | --- | --- | --- |
| `category` | `category` | string | SHALL be `urn:etsi:esi:eaa:eu:pub`. | MUST NOT |
| `issuing_authority` | `issuing_authority` | string | Option B only (section 4.6). | MUST NOT |
| `issuing_country` | `issuing_country` | string | ISO 3166-1 alpha-2. Option B only. | MUST NOT |
| `iss_reg_id` | `iss_reg_id` | string | organizationIdentifier format per ETSI EN 319 412-1 clause 5.1.4. Option B only. | MUST NOT |
| `also_known_as` | `also_known_as` | string | Pseudonym, where used (section 3.4). | MAY |

#### 5.1.3 Public or reusable claims

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Reference/Notes** | **Disclosable** |
| --- | --- | --- | --- | --- |
| `givenName` | `givenName` | string | Learner given name. ELM Person class property. | MUST |
| `familyName` | `familyName` | string | Learner family name. ELM Person class property. | MUST |
| `dateOfBirth` | `dateOfBirth` | string | Date of birth formatted as ISO 8601 date, where disclosed. | MAY |
| `mail` | `mail` | string | Email address, where disclosed. | MAY |

#### 5.1.4 Private claims specific to the Micro-credential Attestation

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Notes** | **Disclosable** |
| --- | --- | --- | --- | --- |
| `attestation_legal_category` | `attestation_legal_category` | string | Transitional only (section 4.3). If present, SHALL be `PuB-EAA`. | MUST NOT |
| `identifier` | `identifier` | string | Unique identifier of the micro-credential achievement. | MUST |
| `title` | `title` | string | Title of the micro-credential. | MUST |
| `issuerCountry` | `issuerCountry` | string | ELM country of the sealing organisation. | MUST |
| `awardingBody` | `awardingBody` | object | Name and identifiers of the public formal education provider that awarded the micro-credential. | MUST |
| `issuanceDate` | `issuanceDate` | string | Date on which the credential was sealed and issued, formatted as ISO 8601 date. | MUST |
| `learningOutcomes` | `learningOutcomes` | array of objects | Structured descriptions of the learning outcomes acquired by the learner. | MUST |
| `ECTS` | `ECTS` | number | ECTS workload, where applicable under Section 3.4. | MUST |
| `volumeOfLearning` | `volumeOfLearning` | string | ISO 8601 duration for volume of learning, where applicable under Section 3.4. | MUST |
| `typeOfAssessment` | `typeOfAssessment` | array of strings | Type or types of assessment used to validate the learning outcomes. | MUST |
| `formOfParticipation` | `formOfParticipation` | string | Form of participation in the learning activity. | MUST |
| `learningActivityType` | `learningActivityType` | string | Category of the learning activity, where disclosed. | MAY |
| `qualityAssurance` | `qualityAssurance` | string | Type of quality assurance underpinning the micro-credential. | MUST |
| `cryptographically_bound_to` | `cryptographically_bound_to` | string | Identifier of another attestation type to which this attestation is bound, where used. | MUST NOT |

The `trust_anchor` claim used in version 1.0 is not used for PuB-EAA. Annex VII (h) is satisfied by the `x5u` header parameter, and trust anchors are obtained as described in chapter 10.


<!-- | `awardingBodyAddress` | `awardingBodyAddress` | string | Registered or contact address of the awarding body, where disclosed. | MAY | -->
<!-- | `awardingBodyHomepage` | `awardingBodyHomepage` | string | Homepage URL of the awarding body, where disclosed. | MAY | -->
<!-- | `awardingBodyIdentifier` | `awardingBodyIdentifier` | string | Additional identifier(s) of the awarding body, where disclosed. | MAY | -->
<!-- | `level` | `level` | string | Level of the learning outcomes against the EQF or an applicable framework, where applicable. | MAY | -->
<!-- | `nationalQualificationsFrameworkLevel` | `nationalQualificationsFrameworkLevel` | string | Level against a national or regional qualifications framework, where disclosed. | MAY | -->
<!-- | `educationLevelDescriptor` | `educationLevelDescriptor` | string | Framework-independent level descriptor, where disclosed. | MAY | -->
<!-- | `learningOutcomeSummary` | `learningOutcomeSummary` | string | Free-text summary of the learning outcomes, where disclosed. | MAY | -->
<!-- | `fieldOfEducation` | `fieldOfEducation` | string | ISCED-F 2013 field of education code, where disclosed. | MAY | -->
<!-- | `escoReference` | `escoReference` | array of strings | ESCO skill/competence references, where disclosed. | MAY | -->
<!-- | `languageOfAssessment` | `languageOfAssessment` | string | Language of assessment, where disclosed. | MAY | -->
<!-- | `idVerificationMethod` | `idVerificationMethod` | string | Supervision/identity-verification method used, where disclosed. | MAY | -->
<!-- | `grade` | `grade` | string | Grade or result obtained, where the assessment produces one. | MAY | -->
<!-- | `gradingScheme` | `gradingScheme` | string | Description of the grading scheme, where disclosed. | MAY | -->
<!-- | `entryRequirements` | `entryRequirements` | array of strings | Prerequisites needed to enrol, where disclosed. | MAY | -->
<!-- | `stackable` | `stackable` | boolean | Whether the micro-credential is designed to stack towards a larger qualification, where disclosed. | MAY | -->
<!-- | `partOfQualification` | `partOfQualification` | string | Identifier or title of the larger qualification, where disclosed. | MAY | -->
<!-- | `accreditation` | `accreditation` | object | Structured accreditation details underpinning `qualityAssurance`, where disclosed. | MAY | -->
<!-- | `additionalNote` | `additionalNote` | string | Free-text supplementary information, where disclosed. | MAY | -->
<!-- | `placeOfBirth` | `placeOfBirth` | string | Learner place of birth, where disclosed. | MAY | -->
<!-- | `citizenshipCountry` | `citizenshipCountry` | string | Learner country of citizenship, where disclosed. | MAY | -->
<!-- | `nationalID` | `nationalID` | string | National or government identifier of the learner, where disclosed. | MAY | -->
<!-- | `registeredAddress` | `registeredAddress` | string | Learner registered/contact address, where disclosed. | MAY | -->

#### 5.1.5 Example protected header and minimum JWT claim set (option A)

Protected header:

```json
{
  "alg": "ES256",
  "typ": "dc+sd-jwt",
  "x5u": "https://pki.example-university.se/certs/eaa-seal-2026.pem",
  "x5t#S256": "<base64url SHA-256 of the qualified certificate>",
  "x5c": ["<qualified seal certificate, PSB profile>", "<intermediate CA certificate>"]
}
```

Claim set (before selective-disclosure processing):

```json
{
  "iss": "https://issuer.example-university.se",
  "iat": 1781740800,
  "nbf": 1781740800,
  "exp": 1813276800,
  "jti": "urn:uuid:9a3f6b2e-1c44-4b8a-9e21-6f0a2d7c5b31",
  "vct": "https://webuildconsortium.eu/credentials/microcredential/pub/1.0",
  "vct#integrity": "sha256-<hash of Type Metadata>",
  "category": "urn:etsi:esi:eaa:eu:pub",
  "status": {
    "status_list": {
      "idx": 4711,
      "uri": "https://status.example-university.se/lists/1"
    }
  },
  "identifier": "MC-2026-0007421",
  "title": "Introduction to Applied Data Ethics",
  "givenName": "Elena",
  "familyName": "Kowalska",
  "issuerCountry": "http://publications.europa.eu/resource/authority/country/SWE",
  "awardingBody": {
    "legalName": "Linköping University",
    "legalIdentifier": "999852236"
  },
  "issuanceDate": "2026-06-15",
  "learningOutcomes": [
    {
      "title": "The title of the learning outcome 1",
      "description": "The actual learning outcome 1"
    },
    {
      "title": "The title of the learning outcome 2",
      "description": "The actual learning outcome 2"
    }
  ],
  "ECTS": 3.0,
  "typeOfAssessment": [
    "http://data.europa.eu/snb/assessment/6a4db9f11d"
  ],
  "formOfParticipation": "http://data.europa.eu/snb/learning-assessment/920fbb3cbe",
  "qualityAssurance": "institutional-accreditation",
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

Under option B, `x5c` is omitted from the header and the following claims are added: `"issuing_authority": "Linköpings universitet"`, `"issuing_country": "SE"` and `"iss_reg_id": "NTRSE-xxxxxxxxxx"`.

> **Editor's note.** The structure of `status` SHALL be checked for alignment between
> IETF Token Status List / HAIP (`status.status_list.idx` / `uri`) and ETSI TS 119 472-1
> clause 5.2.10 before publication.

#### 5.1.6 Example JWT claim set (not implemented yet)

```json
{
  "iss": "https://issuer.example-university.se",
  "iat": 1781740800,
  "nbf": 1781740800,
  "exp": 1813276800,
  "jti": "urn:uuid:9a3f6b2e-1c44-4b8a-9e21-6f0a2d7c5b31",
  "vct": "https://webuildconsortium.eu/credentials/microcredential/pub/1.0",
  "vct#integrity": "sha256-<hash of Type Metadata>",
  "category": "urn:etsi:esi:eaa:eu:pub",
  "status": {
    "status_list": {
      "idx": 4711,
      "uri": "https://status.example-university.se/lists/1"
    }
  },
  "identifier": "MC-2026-0007421",
  "title": "Introduction to Applied Data Ethics",
  "givenName": "Elena",
  "familyName": "Kowalska",
  "issuerCountry": "http://publications.europa.eu/resource/authority/country/SWE",
  "awardingBody": {
    "legalName": "Linköping University",
    "legalIdentifier": "999852236"
  },
  "awardingBodyHomepage": "https://liu.se",
  "issuanceDate": "2026-06-15",
  "level": "EQF-6",
  "learningOutcomes": [
    {
      "title": "The title of the learning outcome 1",
      "description": "The actual learning outcome 1"
    },
    {
      "title": "The title of the learning outcome 2",
      "description": "The actual learning outcome 2"
    }
  ],
  "fieldOfEducation": "0613",
  "escoReference": [
    "http://data.europa.eu/esco/skill/abc12345"
  ],
  "ECTS": 3.0,
  "typeOfAssessment": [
    "http://data.europa.eu/snb/assessment/6a4db9f11d"
  ],
  "formOfParticipation": "http://data.europa.eu/snb/learning-assessment/920fbb3cbe",
  "grade": "Pass",
  "gradingScheme": "Pass/Fail",
  "qualityAssurance": "institutional-accreditation",
  "accreditation": {
    "title": "Institutional Accreditation 2024",
    "type": "institutional-accreditation",
    "accreditingAgent": "Swedish Higher Education Authority",
    "decision": "approved",
    "decisionDate": "2024-01-15",
    "reviewDate": "2029-01-15"
  },
  "stackable": true,
  "partOfQualification": "BSc Data Science, Linköping University",
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

#### 5.1.7 Example issued SD-JWT

The following is a non-normative placeholder example. A production SD-JWT SHALL be generated by the issuer using the applicable signing algorithm, a qualified electronic seal or signature, disclosure construction, holder binding, and SD-JWT VC rules.

```text
<issuer-signed-sd-jwt>~<disclosure-1>~<disclosure-2>~<disclosure-n>~<key-binding-jwt>
```

#### 5.1.8 Example human-readable disclosed payload

A university admissions office requesting evidence of a completed prerequisite micro-credential for course entry may receive a presentation disclosing the following claims, in addition to the non-disclosable claims:

```json
{
  "vct": "https://webuildconsortium.eu/credentials/microcredential/pub/1.0",
  "category": "urn:etsi:esi:eaa:eu:pub",
  "identifier": "MC-2026-0007421",
  "title": "Introduction to Applied Data Ethics",
  "givenName": "Elena",
  "familyName": "Kowalska",
  "issuerCountry": "http://publications.europa.eu/resource/authority/country/SWE",
  "awardingBody": {
    "legalName": "Linköping University",
    "legalIdentifier": "999852236"
  },
  "learningOutcomes": [
    {
      "title": "The title of the learning outcome 1",
      "description": "The actual learning outcome 1"
    },
    {
      "title": "The title of the learning outcome 2",
      "description": "The actual learning outcome 2"
    }
  ],
  "ECTS": 3.0,
  "typeOfAssessment": [
    "http://data.europa.eu/snb/assessment/6a4db9f11d"
  ]
}
```

A verifier that only needs to confirm completion of the micro-credential SHOULD request the minimum claims necessary for that decision. It SHOULD NOT request `dateOfBirth`, `mail`, `nationalID`, `placeOfBirth`, `citizenshipCountry`, or `registeredAddress` unless required for the transaction, for example strong holder matching.

The issuer identity, category, credential type, validity period, attestation identifier, status, signature, signing certificate, and holder binding proof are not selectively disclosable and SHALL remain available to the verifier for technical validation.

### 5.2 ISO/IEC 18013-5-compliant encoding

This version of the Rulebook does not define an ISO/IEC 18013-5 mdoc encoding for the Micro-credential Attestation.

If a future version of this Rulebook defines an ISO/IEC 18013-5-compliant mdoc representation, that version SHALL define a unique document type, namespaces, attribute identifiers, CBOR encoding rules, and illustrative mdoc examples. It SHALL also include the `category` data element (namespace `org.etsi.01947201.010101`) and the CB-AdES header parameters required by ETSI TS 119 472-1 clauses 6.2.2.3 and 6.6.3.

### 5.3 W3C Verifiable Credentials Data Model-based encoding

W3C VCDM encodings are not permitted for attestations that are PuB-EAA (ARB_01). This Rulebook therefore does not define a W3C VCDM encoding.

The European Learning Model's own JSON-LD-based encoding, as used by the European Digital Credentials for Learning infrastructure, can continue to be used outside the EUDI Wallet ecosystem, or in the non-qualified EAA version of this Rulebook.

## 6 Protocols

### 6.1 Issuance

The Micro-credential Attestation is issued using OpenID for Verifiable Credential
Issuance [OpenID4VCI], with the issuer metadata parameters recorded in section 3.1,
including `scope` `MicroCredentialPub` and `format` `dc+sd-jwt`. The PuB-EAA Provider
SHALL authenticate to the Wallet Unit using a valid access certificate, and SHALL
validate the Wallet Unit and verify that it has not been revoked (section 7.5).

### 6.2 Presentation

The Micro-credential Attestation is presented using OpenID for Verifiable
Presentations [OpenID4VP]. Only remote presentation is in scope, consistent with the
formats recorded in chapter 5.

## 7 Issuance

### 7.1 Binding

| Field | Value | Source |
| --- | --- | --- |
| Device-bound | SHOULD | EW-DM-12-038 |
| Cryptographically bound to | attestation type or vct value, where used | EW-DM-12-032 |
| Relying Party must also verify a PID | no | EW-DM-12-031 |
| Binding subject | natural person | The learner to whom the learning achievement relates |

Holder binding is expressed through the `cnf` claim recorded in section 4.1, where it
is used. Where the attestation must be presented together with PID or another identity
attestation, `cryptographically_bound_to` is used as recorded in section 4.3.

### 7.2 Issuance Policy

* Attestations SHALL be issued only by a PuB-EAA Provider meeting the requirements in section 7.5.
* The attested attributes SHALL be taken from the authentic source identified in section 1.5.
* Attestations SHALL be issued only after the underlying learning achievement has been formally assessed and recorded in the authentic source.
* Every attestation SHALL be revocable as described in chapter 8. Short-lived attestations without status are not issued under this Rulebook.
* Every attestation SHALL be sealed or signed as described in section 7.6.

### 7.3 Lifecycle management

- The PuB-EAA Provider issues the attestation after the underlying learning achievement
  has been formally assessed, completed and recorded in the authentic source.
- The `nbf` and `exp` claims define the technical validity of the credential instance,
  not the continued truth of the learning achievement, as recorded in chapter 8.
  A Holder can request re-issuance when the technical validity period ends.
- Where a corrected or superseding credential is issued, the original SHALL be revoked,
  and the relationship between the two is recorded as described in chapter 8. A revoked
  attestation SHALL NOT be reinstated; a new attestation with a new `jti` is issued
  instead.

### 7.4 Embedded disclosure policy

This attestation defines no embedded disclosure policy.

### 7.5 Provider requirements

A PuB-EAA Provider issuing attestations under this Rulebook SHALL:

* be a public sector body within the meaning of Article 3, point (46), of Regulation (EU) 2024/1183, responsible for the authentic source identified in section 1.5 or designated to issue on its behalf;
* be notified by its Member State to the Commission under Article 45f(3) of Regulation (EU) 2024/1183 and Article 5 and Annex III of Commission Implementing Regulation (EU) 2025/1569, with a conformity assessment report from a conformity assessment body, and thereby be included in the Commission's list of PuB-EAA providers;
* meet a level of reliability and trustworthiness equivalent to a qualified trust service provider under Article 24 of Regulation (EU) No 910/2014 (Article 45f(2));
* comply with ETSI TS 119 471 and ETSI EN 319 401, with the adaptations in Annex I of Commission Implementing Regulation (EU) 2025/1569. This includes an EAAS practice statement documenting the revocation mechanism (REQ-EAASP-6.1-02), and the use of a qualified seal or signature creation device for sealing or signing the attestations (REQ-EAASP-7.5.3-02);
* use cryptographic mechanisms compliant with ENISA's Agreed Cryptographic Mechanisms (REQ-EAASP-7.5.3-01B);
* provide an interface with EUDI Wallets (Article 45f(8)); during issuance, authenticate to the Wallet Unit using a valid access certificate, and validate the Wallet Unit and whether it has been revoked (REQ-EAASP-4.2.2.3-02/03);
* comply with the scheme registered in the catalogue of attestation schemes (section 2.4).

### 7.6 Signature and signing certificate

The attestation SHALL be signed with a qualified electronic seal or a qualified electronic signature of the PuB-EAA Provider (Annex VII (g); ETSI TS 119 472-1 PuB-EAA-5.6.3-01).

The supporting qualified certificate SHALL:

* meet the requirements of the PSB profile specified in ETSI TS 119 412-6 (PuB-EAA-4.6.2-04);
* identify the PuB-EAA Provider with at least countryName, organizationName and, where applicable, organizationIdentifier (ETSI EN 319 412-1 clause 5.1.4);
* contain, in a form suitable for automated processing (Article 45f(1)(b) of Regulation (EU) 2024/1183):
  1. an indication that the issuing body is established under Union or national law as responsible for the authentic source on which the attestation is based, or as the body designated to act on its behalf;
  2. a set of data unambiguously representing that authentic source;
  3. an identification of the Union or national law concerned (section 1.5);
* be available free of charge at the URL given in the `x5u` header (Annex VII (h)), with its SHA-256 thumbprint in `x5t#S256` (PuB-EAA-5.6.3-02).

The certificate SHOULD also be included in the `x5c` header (PuB-EAA-5.6.3-03); see section 4.6 for the effect on issuer identification claims.

## 8 Revocation

The Micro-credential Attestation records a completed, formally assessed learning achievement. Unlike affiliation-based attestations, the underlying fact it attests, that the learner achieved the stated learning outcomes, does not lapse over time and does not need to be periodically re-established. Consequently, revocation of a Micro-credential Attestation is not a mechanism for expressing that the achievement is "no longer valid" in a temporal sense. It is a mechanism for withdrawing a credential instance where the original issuance was defective, the credential instance is compromised, or the law or the Holder requires it.

The credential expiration time (`exp`) SHALL be understood as reflecting only the technical validity of the credential instance, for example to encourage periodic re-issuance onto current cryptographic material. A Relying Party SHALL NOT interpret it as an indication that the underlying learning achievement itself has expired.

**Revocability.** Attestations under this Rulebook are issued with a validity period of more than 24 hours. They SHALL therefore be revocable (Article 4(3) of Commission Implementing Regulation (EU) 2025/1569 as amended), and SHALL contain the `status` claim (ETSI TS 119 472-1 PuB-EAA-5.2.10.3-01). The `shortLived` claim SHALL NOT be used.

**Mechanism.** The PuB-EAA Provider SHALL use an Attestation Status List mechanism, implemented as an IETF Token Status List, as specified in [Topic 7] of Annex 2 of the ARF and Annex II to Commission Implementing Regulation (EU) 2024/2979 (ARB_23). Status lists SHALL be published under the domain of the PuB-EAA Provider, `https://status.<provider-domain>/` (ARB_24a). The full status list URL for each attestation is included in its `status` claim.

**No suspension.** A revoked PuB-EAA loses its validity from the moment of revocation, and its status SHALL NOT be reverted (Article 45f(4) of Regulation (EU) 2024/1183). Suspension SHALL NOT be used, and status list entries SHALL use only VALID and INVALID.

**Who may revoke.** Only the PuB-EAA Provider that issued the attestation SHALL be able to revoke it (Article 4(2) of Commission Implementing Regulation (EU) 2025/1569).

**Grounds for revocation.** The PuB-EAA Provider SHALL revoke a Micro-credential Attestation in at least the following circumstances (Article 4(3)):

* at the request of the person to whom the attestation was issued or, where applicable, of the subject of the attestation;
* where the provider becomes aware of a compromise of the security or trustworthiness of the attestation;
* in other situations as required by Union or national law.

In addition, the PuB-EAA Provider SHALL revoke the attestation where:

* the credential was issued in error, for example to the wrong natural person or with incorrect attribute values;
* the underlying assessment is subsequently found to have been invalid, for example due to an academic integrity finding such as plagiarism or assessment fraud;
* the awarding body's authorisation or accreditation to award the underlying qualification is withdrawn or successfully challenged with retroactive effect;
* the credential is reported lost, compromised, or fraudulently obtained;
* the awarding body issues a corrected or superseding version of the credential, for example following a grade appeal or administrative correction.

**Privacy and integrity.** The revocation technique SHALL be privacy-preserving and hinder linkability and traceability, for example through random allocation of status list indices and sufficiently large lists (Article 4(4)). Status information SHALL be made available to Relying Parties in a manner that ensures its integrity and authenticity (Article 4(5)); status list tokens SHALL be signed by the PuB-EAA Provider.

**Status checking.** The Relying Party SHALL check the status before accepting the attestation, unless offline operating rules explicitly allow deferred status checking.

**Retention.** Because the Micro-credential Attestation is not time-bound in the same way as an affiliation-based attestation, the PuB-EAA Provider SHALL maintain status information for each attestation at least until its `exp` has passed.

**Superseding credentials.** Where a Micro-credential Attestation is revoked and superseded by a corrected version, the superseding attestation receives a new `jti`. The PuB-EAA Provider SHOULD ensure that the `identifier` of the superseding credential allows a Relying Party, where necessary and with the Holder's cooperation, to establish the relationship to the revoked credential.

## 9 Presentation

### 9.1 Presentation Policy

To verify and validate a received presentation of an attestation of this type,
the following steps SHALL be performed:

1. verify the qualified electronic seal or signature over the attestation, using the
   certificate referenced in `x5u`/`x5t#S256` (or included in `x5c`) and a trust anchor
   obtained as described in chapter 10;
2. verify that `category` is `urn:etsi:esi:eaa:eu:pub`;
3. verify that the attestation is within its technical validity period (`nbf`, `exp`);
4. check revocation status as described in chapter 8;
5. verify device binding where section 7.1 records the attestation as device-bound;
6. request only those attributes that are necessary for the stated purpose of the
   transaction, and only those it is registered and authorised to request.

Obligations specific to this attestation type:

The Micro-credential Attestation is intended for verifying that a natural person has completed a specific, formally assessed learning achievement and the associated learning outcomes.

Typical usage scenarios include:

* presentation by a learner to a university or other higher education institution to demonstrate fulfilment of entry requirements or eligibility for recognition of credits when applying for a course or programme;
* presentation for professional onboarding or recruitment where formally taught knowledge, skills, or competences are relevant to the role;
* presentation for recognition of prior learning or credit transfer between formal education providers;
* presentation in both domestic and cross-border contexts, subject to semantic interpretation, policy alignment, and recognition practices that may vary across sectors and jurisdictions.

Usage covers both:

* online verification by a service provider using remote presentation protocols;
* offline or low-connectivity verification, where the verifier can validate the seal, issuer, validity period, status (from a recently cached status list) and disclosed attributes without relying on a real-time issuer backend.

A Relying Party receiving the attestation SHALL verify:

* the qualified electronic seal or signature of the issuer;
* that the signing certificate is a qualified certificate following the PSB profile of ETSI TS 119 412-6, and that it chains to a trust anchor in the Commission's list of PuB-EAA providers;
* that the authentic source and legal basis indicated in the certificate cover this attestation type;
* that `iss` and the issuer identification data (section 4.6) are consistent with the certificate;
* the `category` claim and the SD-JWT VC type (`vct`, `vct#integrity`);
* the technical validity period;
* the credential status;
* holder binding, where used;
* the integrity rules defined in Section 4.5;
* that the disclosed attributes are sufficient for the relying-party decision.

The Relying Party SHALL distinguish between verification of the attestation and evaluation of whether the attested learning outcomes are sufficient for its purpose. Successful cryptographic or technical verification alone SHALL NOT be treated as sufficient proof that the attested learning outcomes meet the Relying Party's acceptance criteria. The Relying Party SHALL evaluate the attested skill claim against its own defined criteria relevant to the intended use context, for example admission requirements or credit recognition rules.

The Relying Party SHOULD be able to interpret:

* any assurance or quality level associated with the attestation, where such levels are defined by a future version of this Rulebook;
* recognised taxonomy or classification references, such as ESCO or ISCED-F references, where included in the attestation.

The Relying Party SHOULD request and verify a PID or another accepted identity credential where the transaction requires strong identity matching between the Holder and the attestation subject. For low-risk checks, the Relying Party MAY rely on the Micro-credential Attestation alone, provided that the issuer, seal, validity, status, and holder binding checks are successful and this is consistent with the relying party's policy.

The Relying Party SHALL apply data minimisation and SHALL request only the attributes required for the transaction. For example, a credit-recognition decision may only need `title`, `awardingBody`, `level`, `learningOutcomes`, and `ECTS`, while an identity-sensitive enrolment process may additionally require `givenName`, `familyName`, and strong holder-binding verification via a PID.

The Relying Party SHOULD be able to evaluate the Micro-credential Attestation together with other supporting attestations where combined evidence is required, for example where several micro-credentials are presented to demonstrate cumulative fulfilment of entry requirements.

The Relying Party SHOULD define fallback handling for cases in which the attestation cannot be accepted, including rejection, request for additional evidence, deferred decision, or referral to an alternative process.

The attestation SHOULD be device-bound through holder binding where supported by the EUDI Wallet and the applicable SD-JWT VC profile. The attestation MAY be cryptographically bound to a PID or another accepted identity attestation where strong identity matching is required. Where this binding is used, the metadata attribute `cryptographically_bound_to` SHOULD contain:

```text
urn:eudi:pid:1
```

No payment-specific transactional data is defined by this Rulebook. If the Micro-credential Attestation is used as part of a transaction that also involves payment, for example a paid enrolment or examination fee, payment-related requirements SHALL be defined in a separate payment attestation, payment profile, or transaction-specific rulebook; see [Topic 20] of Annex 2 of the ARF.

### 9.2 Presentation modes

Remote presentation is in scope. Proximity presentation is not in scope in this
version, consistent with chapter 5, which records no mdoc encoding. If proximity
presentation without internet connectivity becomes a requirement, a future version
SHALL define an mdoc encoding (ARB_02).

### 9.3 Transactional data

This Rulebook does not define transactional or payment-related data. Where a
Micro-credential Attestation is used in a transaction involving payment, such
requirements are out of scope of this version.

## 10 Trust Framework

**PuB-EAA**

The trust anchor for verifying a Micro-credential Attestation SHALL be obtained from the
list of providers of electronic attestations of attributes issued by or on behalf of a
public sector body responsible for an authentic source. The Commission establishes,
maintains and publishes this list on the basis of Member State notifications (Article
45f(3) of Regulation (EU) 2024/1183; Article 6 of Commission Implementing Regulation
(EU) 2025/1569). The list is electronically signed or sealed and suitable for automated
processing, and it uses the List of Trusted Entities (LoTE) data model of ETSI TS 119 602.
The Relying Party SHALL obtain the list location and the certificates for verifying the
list from the Commission's publication under Article 6(3) of Commission Implementing
Regulation (EU) 2025/1569.

The Provider may sign attestations with an intermediate signing certificate that chains
to the trust anchor in the list, instead of signing directly with the trust anchor.

A Wallet Unit MAY verify Provider authorisation during issuance using the mechanism
described in ISSU_34 of Topic 10 of Annex 2 of the ARF.

**Certificate location**

The location of the certificate supporting the qualified seal or signature (Annex VII
(h)) is the URL in the `x5u` protected header parameter, at which a machine-readable
version of the certificate can be retrieved free of charge (ARB_20). The `trust_anchor`
claim of version 1.0 is not used.

**Deployment profile**

A Relying Party SHALL verify that the issuer of the Micro-credential Attestation is a PuB-EAA Provider authorised to issue this attestation type.

The Relying Party SHALL use the trust anchor and the signing certificate to verify that:

* the signing certificate chains to a trust anchor of a PuB-EAA Provider in the Commission's list;
* the signing certificate is a qualified certificate following the PSB profile of ETSI TS 119 412-6, and is valid and not revoked;
* the authentic source and the legal basis indicated in the certificate correspond to the authentic source for study records defined in section 1.5;
* the issuer is authorised to issue the `https://webuildconsortium.eu/credentials/microcredential/pub/1.0` attestation type;
* the list entry for the PuB-EAA Provider has not expired or been withdrawn;
* the issuer identity in the attestation (`iss` and the issuer identification data in section 4.6) is consistent with the certificate and the list entry.

The public sector body that seals the credential (the PuB-EAA Provider) may differ from the organisation that awarded the underlying learning achievement (`awardingBody`), for example where a designated public sector body issues on behalf of the responsible body. The Relying Party SHALL verify issuer trust based on the PuB-EAA Provider's trust anchor. It MAY additionally seek confirmation, for example through the accreditation information in Section 3.3, that the awarding body was itself entitled to award the micro-credential at the time of issuance.

For controlled interoperability testing within WE BUILD, pilot trust lists MAY be used in addition to the Commission's list. Attestations verified only against a pilot list SHALL NOT be treated as PuB-EAA.

Wallet Units MAY also use the same trust framework information during issuance to determine whether the provider is authorised to issue this attestation type.

## 11 References

| **Item Reference** | **Standard name/details** |
| --- | --- |
| [CIR 2024/2979] | Commission Implementing Regulation (EU) 2024/2979 laying down rules for the application of Regulation (EU) No 910/2014 as regards the integrity and core functionalities of European Digital Identity Wallets. Available: <https://eur-lex.europa.eu/eli/reg_impl/2024/2979/oj> |
| [CIR 2025/1569] | Commission Implementing Regulation (EU) 2025/1569 of 29 July 2025 as regards qualified electronic attestations of attributes and electronic attestations of attributes provided by or on behalf of a public sector body responsible for an authentic source, as amended by Commission Implementing Regulation (EU) 2026/1735. Consolidated text: <https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02025R1569-20270101> |
| [Council Recommendation on Micro-credentials] | Council Recommendation of 16 June 2022 on a European approach to micro-credentials for lifelong learning and employability (2022/C 243/02). Available: <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:32022H0627(02)> |
| [DEQAR] | Database of External Quality Assurance Results, used as a source controlled list for accreditation decisions in the European Learning Model. |
| [ELM] | European Learning Model, a multilingual data model supporting the interoperable representation of learning opportunities, qualifications, accreditation, and credentials. Available: <https://europa.eu/europass/elm-browser/index.html> |
| [EQF Recommendation] | Council Recommendation of 22 May 2017 on the European Qualifications Framework for lifelong learning (2017/C 189/03). Available: <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32017H0615(01)> |
| [ESCO] | European Skills, Competences, Qualifications and Occupations, the European multilingual classification of skills, competences, qualifications and occupations. Available: <https://esco.ec.europa.eu/en/classification/skill_main> |
| [ETSI EN 319 401] | ETSI EN 319 401, Electronic Signatures and Trust Infrastructures (ESI); General Policy Requirements for Trust Service Providers. |
| [ETSI EN 319 412-1] | ETSI EN 319 412-1, Electronic Signatures and Trust Infrastructures (ESI); Certificate Profiles; Part 1: Overview and common data structures. |
| [ETSI TS 119 412-6] | ETSI TS 119 412-6, Electronic Signatures and Trust Infrastructures (ESI); Certificate Profiles; Part 6: Certificate profile requirements for PID, Wallet, EAA, QEAA, and PSBEAA providers. |
| [ETSI TS 119 471] | ETSI TS 119 471 V1.1.1 (2025-05), Electronic Signatures and Trust Infrastructures (ESI); Policy and Security requirements for Providers of Electronic Attestation of Attributes Services. |
| [ETSI TS 119 472-1] | ETSI TS 119 472-1 V1.2.1 (2026-02), Electronic Signatures and Trust Infrastructures (ESI); Profiles for Electronic Attestation of Attributes; Part 1: General requirements. Available: <https://www.etsi.org/deliver/etsi_ts/119400_119499/11947201/01.02.01_60/ts_11947201v010201p.pdf> |
| [ETSI TS 119 602] | ETSI TS 119 602, Electronic Signatures and Trust Infrastructures (ESI); Lists of trusted entities; Data model. |
| [EU Vocabularies] | EU multilingual controlled vocabularies published via the EU Vocabularies concept scheme service, including Assessment Type, Mode of Learning and Assessment, Learning Activity Type, and Method of Supervision and Verification, as used by the European Learning Model. Available: <https://op.europa.eu/en/web/eu-vocabularies> |
| [EUDI Rulebook Template] | EUDI Wallet Attestation Rulebook Template, version 1.5. Available: <https://github.com/eu-digital-identity-wallet/eudi-doc-attestation-rulebooks-catalog/blob/main/template/attestation-rulebook-template.md> |
| [European Digital Identity Regulation] | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework, in particular Article 45f and Annex VII |
| [HAIP] | Yasuda, K. *et al,* OpenID4VC High Assurance Interoperability Profile, OpenID Foundation |
| [IANA-JWT-Claims] | IANA JSON Web Token Claims Registry. Available: <https://www.iana.org/assignments/jwt/jwt.xhtml> |
| [IETF Token Status List] | Token Status List, IETF OAuth Working Group. Available: <https://datatracker.ietf.org/doc/draft-ietf-oauth-status-list/> |
| [ISCED-F 2013] | International Standard Classification of Education, Fields of Education and Training 2013, UNESCO Institute for Statistics. |
| [ISO/IEC 18013-5] | ISO/IEC 18013-5, Personal identification --- ISO-compliant driving licence - Part 5: Mobile driving licence application |
| [OpenID4VCI] | OpenID for Verifiable Credential Issuance, OpenID Foundation |
| [OpenID4VP] | OpenID for Verifiable Presentations, OpenID Foundation |
| [RFC 2119] | RFC 2119 - Key words for use in RFCs to Indicate Requirement Levels, S. Bradner, March 1997 |
| [RFC 3339] | RFC 3339 - Date and Time on the Internet: Timestamps, G. Klyne et al., July 2002 |
| [RFC 5322] | RFC 5322 - Internet Message Format, P. Resnick, October 2008 |
| [RFC 7515] | RFC 7515 - JSON Web Signature (JWS), M. Jones et al., May 2015 |
| [RFC 8610] | RFC 8610 - Concise Data Definition Language (CDDL): A Notational Convention to Express Concise Binary Object Representation, H. Birkholz et al., June 2019 |
| [RFC 8943] | RFC 8943 - Concise Binary Object Representation (CBOR) Tags for Date, M. Jones et al., November 2020 |
| [RFC 8949] | RFC 8949 - Concise Binary Object Representation (CBOR), C. Bormann et al., December 2020 |
| [SD-JWT VC] | SD-JWT-based Verifiable Credentials. Available: <https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/> |
| [Topic 7] | ARF Annex 2 - Topic 7 - Attestation revocation and revocation checking |
| [Topic 10] | ARF Annex 2 - Topic 10 - Issuing a PID or attestation to a Wallet Unit |
| [Topic 12] | ARF Annex 2 - Topic 12 - Attestation Rulebooks |
| [Topic 20] | ARF Annex 2 - Strong User authentication for electronic payments |
| [W3C VCDM v2.0] | Verifiable Credentials Data Model v2.0, W3C Recommendation |
