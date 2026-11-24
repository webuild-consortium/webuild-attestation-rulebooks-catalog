# Attestation Rulebook for attestations of type Verified Skill

**Category:** non-qualified Electronic Attestation of Attributes (EAA)  
**Version:** 0.3 — consolidated review candidate, **subject to publication approvals**  
**Date:** 2026-11-24  
**Basis:** WE BUILD Verified Skill Rulebook v0.2 (2026-10-05); WE BUILD Micro-credential Rulebook v1.0 (2026-10-20); Council Recommendation 2012/C 398/01.  
**Technical baseline:** ARF 3.0.0 as referenced by the original rulebook; deployment profile to be checked before publication. **Proposed** VS `vct`: `https://webuildconsortium.eu/credentials/verified-skill/0.3` (ownership and type metadata still require approval).  
**Document status:** complete candidate for WE BUILD review. Normative SHALL/SHOULD/MAY express proposed requirements, not existing approved WE BUILD policy. **All eleven chapters and Annexes A and B are included. ELM 3.3.1 EDC profile mapping is summarised in Annex A.6.**

## Table of contents

1. [Introduction](#1-introduction)
2. [Compliance](#2-compliance)
3. [Attestation attributes](#3-attestation-attributes)
4. [Metadata](#4-metadata)
5. [Formats](#5-formats)
6. [Protocols](#6-protocols)
7. [Issuance](#7-issuance)
8. [Revocation](#8-revocation)
9. [Presentation](#9-presentation)
10. [Trust Framework](#10-trust-framework)
11. [References](#11-references)
12. [Annex A — ELM mapping](#annex-a--elm-mapping-decisions)
13. [Annex B — Publication decisions](#annex-b--publication-decisions-and-verification)

## 1 Introduction

### 1.1 Document scope and purpose

This Rulebook defines a **Verified Skill Attestation**, a non-qualified EAA issued to a natural person in an EUDI Wallet ecosystem. It represents one or more knowledge, skill or competence learning outcomes acquired or demonstrated through non-formal or informal learning, workplace experience, or other settings. The credential is digitally verifiable; **the underlying skill claim is not necessarily formally validated**. Its assurance is communicated explicitly.

The status of a skill assertion SHALL be identified as `identified`, `documented`, or `validated`. These three labels are **WE BUILD profile terms**, not prescribed values or phases of Council Recommendation 2012/C 398/01. The Recommendation identifies four activities — identification, documentation, assessment and certification — which may be used individually or in combination. This Rulebook provides optional `validationProcess` information about those activities without implying that every attestation represents all four.

A claim marked `validated` SHALL be founded on an assessment against a relevant standard or criteria, confirmed by a competent body authorised under an applicable validation arrangement. An `identified` or `documented` claim SHALL NOT imply completed formal validation. A cryptographic signature confirms credential provenance, not the truth of a skill claim.

The attestation may be used for employment, recruitment, mobility, learning and recognition of prior learning. It does not by itself award ECTS credits, a qualification, an EQF/NQF level, a regulated occupational licence or an educational exemption. Such decisions belong to the competent recognising organisation.

**Alignment rule.** The WE BUILD Micro-credential Rulebook v1.0 is the **fixed reference** for shared attribute names, structures, data types and ELM semantics. The Micro-credential Rulebook is expected to be rewritten separately for PuB-EAA; **that work is outside the scope of this Rulebook**. Verified Skill stays non-qualified EAA. VS extensions are used only where MC/ELM concepts cannot express a required distinction. The legal-category difference does not justify unnecessary differences in learning outcome or assessment structures.

Dreyfus proficiency, where supplied, SHALL NOT be conflated with EQF/NQF levels. Learning volume MAY be stated as duration in hours when it can be established reliably; ECTS is not required and SHALL NOT be represented as Dreyfus proficiency. Educational ESG accreditation is not an automatic condition for workplace skill claims. ESCO references SHOULD be supplied where appropriate.

### 1.2 Document structure

Chapters 2–4 specify compliance, attribute obligations and metadata. Chapter 5 defines SD-JWT VC encoding; Chapter 6 protocols; Chapters 7–10 issuance, lifecycle, presentation and trust. Chapter 11 identifies reference sources. Annex A explains ELM mapping decisions and proposes ELM v3.4 improvements. Annex B records unresolved publication decisions.

### 1.3 Key words

**SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT** and **MAY** are interpreted in accordance with RFC 2119 and RFC 8174 when written in uppercase. Mandatory/optional/conditional obligations apply to the *issued* credential unless presentation is explicitly discussed.

### 1.4 Terminology

| Term | Definition |
|---|---|
| Verified Skill Attestation | Digitally verifiable assertion about an individual's knowledge, skills or competences, with explicit status of the underlying assertion. |
| Holder | Natural person who is the subject of the attestation. |
| Issuer / Attestation Provider | Entity issuing and cryptographically sealing the credential. |
| Awarding Body | Organisation responsible for awarding or formally recognising an underlying learning achievement, where an award takes place. Its JSON structure is identical to MC. Merely recording a self-declaration does not make an organisation an awarding body. |
| Assessor | Person or organisation carrying out an assessment against defined criteria. |
| Validating Body | Body confirming a result against the relevant assessment standard under an applicable, documented authorisation arrangement; may also be the assessor or issuer. |
| Learning outcome | Statement of what a person knows, understands or can do. |
| Identified | Skill declared or identified, without an established formal validation claim. |
| Documented | Skill backed by relevant retained evidence, without completed formal validation. |
| Validated | Successfully assessed against defined standards/criteria and confirmed under an applicable validation arrangement. |
| Validation phases | Identification, documentation, assessment and certification as described by the 2012 Council Recommendation. |
| Assessment independence | Organisational relationship of assessor to the entity responsible for the assertion; **not** a quality score. |
| Quality assurance | Documented controls over the applicable assessment/validation process; not synonymous with accreditation. |
| Dreyfus proficiency | One of five stages of skill acquisition: novice, advanced beginner, competent, proficient, expert. |
| Credential status | Lifecycle state such as valid/revoked/suspended, distinct from `validationStatus`. |
| Relying Party | Organisation evaluating a presented attestation for a defined purpose. |

## 2 Compliance

### 2.1 Compliance statement

This Rulebook is designed for the non-qualified EAA category and the applicable ARF Topic 12, SD-JWT VC and WE BUILD template requirements. A deployment SHALL be checked against the applicable ARF and technical profile before an actual conformance claim is made. It adopts the **policy principles** of the 2012 Council Recommendation; the Recommendation is **not a directly binding credential schema**.

The Rulebook defines domain attributes and conditional validation requirements; reuses MC-compatible structures for equivalent information; distinguishes the status of the assertion, its assessor independence and its QA; and separates technical authenticity from recognition or substantive acceptance.

### 2.2 Regulatory basis

The attestation falls under Regulation (EU) No 910/2014 as amended by Regulation (EU) 2024/1183, as a **non-qualified** EAA. Council Recommendation 2012/C 398/01 provides the policy basis for validation of non-formal and informal learning. Council Recommendation 2022/C 243/02 provides a complementary reference for convergence with Micro-credentials. The distinctions between the categories of EAA and PuB-EAA SHALL be retained in issuer eligibility and trust policy; this Rulebook does not amend the MC profile.

### 2.3 Traceability

The **original v0.2 ARF Topic 12 traceability table remains the authoritative starting checklist**, but shall be refreshed against the final ARF release and final Chapter 4–5 encoding before publication. In particular, the mappings for credential-type identifier, legal-category claim, binding and status require confirmation. No new ARF requirement identifiers are invented here.

| Policy principle from 2012 Recommendation | Rulebook location |
|---|---|
| Identification/documentation of learning outcomes | §§1.1, 3.1–3.4, 7.2 |
| Assessment against relevant standards | §§3.4, 4.5, 7.2 |
| Certification, where applicable, distinguished from digital issuance | §§1.1, 4.4, 7.2 |
| Four phases separately or in combination | §§3.3, 4.4 |
| Appropriate quality assurance and competent body | §§3.4, 7.2, 10 |
| Access to recognition of prior learning | §§7.2, 9.1 |

## 3 Attestation attributes

### 3.1 Introduction

Attributes are defined independent of their technical encoding. `M` means required on **every issued credential**; `O` optional; `C` required if its stated condition applies. The three claim statuses are **not** credential revocation status. A single attestation SHALL use one status and, when present, one Dreyfus proficiency and assurance context across all its learning outcomes. Distinct claims requiring different levels SHALL be issued separately.

### 3.2 Mandatory attributes

These logical claims SHALL be present in all issued VS credentials. The structured fields below follow the fixed MC v1.0 schema where the meanings match.

| Claim | Type / structure | Meaning |
|---|---|---|
| `category` | string, `eaa:eu:non-qualified` | Non-qualified EAA category following the newer EUDI Rulebook template; see §4.1. |
| `identifier` | string | Unique attestation identifier. |
| `title` | string | Human-readable credential title. |
| `givenName` | string | Holder given name. |
| `familyName` | string | Holder family name. |
| `issuerCountry` | string, EU country authority URI | Issuer country, same representation as MC. |
| `issuanceDate` | ISO 8601 calendar date | Credential issue date. |
| `learningOutcomes` | non-empty array of `{title, description}` objects | Learning outcomes, identical structural shape to MC. |
| `validationStatus` | enumeration | `identified`, `documented`, `validated`. |

### 3.3 Optional attributes

| Claim | Type | Requirement or note |
|---|---|---|
| `skillProficiencyLevel` | Dreyfus enum | MAY for identified/documented, SHALL for validated. |
| `volumeOfLearning` | ISO 8601 duration | MAY when measurable, e.g. `PT80H`; identical meaning/format to MC, not ECTS. |
| `formOfParticipation` | MC vocabulary identifier | MAY when a learning activity is identifiable. |
| `escoReference` | array of URI strings | MAY reference relevant ESCO concepts. |
| `awardingBody` | MC organisation object (`legalName`, optional `legalIdentifier`) | MAY where an organisation actually awards or recognises the achievement; SHALL for `validated`, and SHALL NOT be used solely for a recorded self-declaration. |
| `supportingEvidence` | array of objects | MAY provide references or summaries; sensitive records MAY be held externally. Uses ELM supplementary-document semantics where applicable; assessment provenance through `provenBy`. |
| `validationProcess` | object | MAY identify phase records using §4.4. |
| `accreditation` | object | MAY only if actual relevant accreditation exists. |
| `reviewDate` | ISO 8601 date | MAY indicate recommended reassessment, distinct from credential expiry. |
| `dateOfBirth`, `placeOfBirth`, `citizenshipCountry`, `nationalID`, `registeredAddress`, `mail` | MC-compatible types | MAY only where necessary and lawful. |
| `recognitionReference` | array of objects | MAY identify actual recognition decisions (not implied recognition). |

### 3.4 Conditional attributes

For `validationStatus = validated`, **all** claims in the following table SHALL be present in the **issued** payload.

| Claim | Type / constraint | Function |
|---|---|---|
| `skillProficiencyLevel` | Dreyfus enum | Assessed proficiency. |
| `typeOfAssessment` | non-empty array of assessment-type identifiers, MC-compatible | Method(s) used. |
| `assessmentStandard` | object (`title` required; optional `identifier`, `version`, `reference`, `criteria`) | Assessment specification/standard, mapped to ELM `LearningAssessmentSpecification`; `specifiedBy` links assessment to specification. |
| `grade` | string, as in MC | Successful result according to `gradingScheme`; default `Pass` within `Pass/Fail`. Failed results SHALL NOT substantiate `validated`. |
| `gradingScheme` | string, as in MC | Mandatory for `validated`; default `Pass/Fail`, other defined schemes permitted. |
| `awardingBody` | MC organisation object | Mandatory for `validated`; optional for other statuses if an achievement was actually awarded. |
| `assessmentDate` | ISO 8601 calendar date | Date of assessment. |
| `assessor` | MC organisation object, or individual `{fullName}` | Assessment-responsible entity; reuse ELM `LearningAssessment.assessedBy` when equivalent. |
| `validatingBody` | MC organisation object | Separately identifies body confirming formal validation; VS extension where distinct from awarding role. |
| `assessmentIndependence` | enum | Relationship of assessor to responsible organisation. |
| `qualityAssurance` | MC-compatible top-level representation (string) | Applicable assessment/validation QA arrangement; permitted values defined in §4.4 (VS additions provisional). |

`gradingScheme` SHALL accompany `grade` for `validated` claims. A binary `Pass`/`Fail` grade using `Pass/Fail` is the default; other grading schemes MAY be used where their successful outcome is defined. The issuer SHALL establish successful completion using the actual grading scheme, not merely a non-empty grade string. For `documented`, a relevant and traceable evidence basis SHALL exist, but its disclosure in `supportingEvidence` SHALL NOT be mandatory. For `identified`, a source of identification or declaration SHALL be recorded under issuer governance; formal assessment SHALL NOT be inferred. `qualityAssurance` MAY be included for other statuses only if it accurately describes an actual relevant QA arrangement.

No separate top-level `assessmentResult`, `assessmentCriteria`, `assessmentBasis`, `qualityAssuranceMethod`, `qualityAssuranceLevel`, `qualityFramework` or `auditInformation` is defined in v0.3. Standard details MAY be structured within `assessmentStandard`, and QA documents MAY be referenced under the relevant arrangement. **Where MC semantics are applicable, do not invent duplicate result or organisation claims.**

## 4 Metadata

Metadata describes the credential and its lifecycle, not the skill claim.

### 4.1 Mandatory metadata

| Claim | Type | Requirement |
|---|---|---|
| `vct` | URI string | SHALL identify the approved VS version, **provisionally** `https://webuildconsortium.eu/credentials/verified-skill/0.3`. |
| `iss` | string | SHALL identify issuer. |
| `iat` | NumericDate integer | SHALL specify issuance time. |
| `cnf` | object | SHALL be included where required by applicable Holder-binding profile; see §4.3. |

**Legal-category encoding:** VS SHALL use `category: "eaa:eu:non-qualified"` as defined for non-qualified EAAs by the current EUDI Rulebook template. The legacy `attestation_legal_category` SHALL NOT also be emitted. The value is template-defined for non-qualified EAA and is **not** the ETSI value reserved for a PuB-EAA or QEAA. Final confirmation against the selected production ARF/ETSI profile is a release gate. This decision changes VS only, not MC.

### 4.2 Optional metadata

| Claim | Type | Meaning |
|---|---|---|
| `exp`, `nbf` | NumericDate integer | Expiry and not-before. |
| `jti` | string | Credential instance identifier. |
| `status` | object | Credential status information (not skill validation). |
| `trust_anchor` | string | Trust-framework reference subject to the applicable profile. |
| `cryptographically_bound_to` | string | Reference to another credential when supported/appropriate. |

### 4.3 Conditional metadata

`cnf` SHALL be present whenever the applicable holder-binding profile requires cryptographic key confirmation. If a deployed profile permits another binding arrangement, the issuer SHALL follow that profile; a JSON Schema check alone does not establish secure binding.

`status` SHALL be present when mandated by the applicable lifecycle technical profile or deployment policy. `cryptographically_bound_to` MAY be present for supported cross-credential binding, but **shall not be confused with or substituted for** `cnf` without a defined protocol. The original `trust_anchor` semantics shall be reconciled with the final issuer trust profile.

### 4.4 Code lists

#### 4.4.1 Skill proficiency

| Code | Meaning |
|---|---|
| `novice` | Uses rules and instruction in relatively unfamiliar situations. |
| `advanced-beginner` | Recognises recurrent aspects but needs guidance. |
| `competent` | Plans and prioritises deliberately in context. |
| `proficient` | Interprets situations holistically and adapts. |
| `expert` | Demonstrates highly developed contextual skill. |

The values refer to Dreyfus proficiency, **not EQF/NQF or occupational grade**. No sixth `not-assessed` Dreyfus level is introduced. If proficiency cannot be stated, omit it except when status is `validated`.

#### 4.4.2 Validation status

| Code | Meaning |
|---|---|
| `identified` | Skill identified or declared; not established as formally validated. |
| `documented` | Supporting evidence exists; not established as formally validated. |
| `validated` | Successful assessment and authorised confirmation against relevant criteria. |

These are WE BUILD domain codes. The four **validation phases** of the 2012 Recommendation are separate metadata, not additional statuses.

#### 4.4.3 Assessment type / participation

`typeOfAssessment` and `formOfParticipation` SHALL reuse the **same controlled vocabularies and URI representations as the existing MC Rulebook** whenever the concept is applicable. Do not create VS aliases for existing MC codes. Any extension identifiers SHALL be documented and uniquely resolvable.

#### 4.4.4 Assessment independence

| Code | Meaning |
|---|---|
| `internal-assessment` | Assessor belongs to the organisation responsible for the assertion. |
| `independent-third-party` | Assessment by organisationally independent person/entity under a documented arrangement. |

Independence does not imply quality, proficiency, accreditation or validation status on its own.

#### 4.4.5 Quality assurance — agreed VS vocabulary

| Code | Use |
|---|---|
| `documented-internal-qa` | Documented internal assessment/validation QA controls. |
| `sectoral-quality-assurance` | Documented sectoral/professional QA arrangement. |
| `independent-external-qa` | Independent review or audit of the relevant arrangement. |
| `institutional-accreditation` | Applicable formal accreditation of the organisation. |
| `programme-accreditation` | Applicable formal accreditation of the programme/scheme. |
| `national-quality-agency` | Relevant national agency QA mechanism. |

The four MC-compatible labels (`sectoral-quality-assurance`, `institutional-accreditation`, `programme-accreditation`, `national-quality-agency`) are reused without changes to MC. The two VS additions (`documented-internal-qa`, `independent-external-qa`) are **agreed WE BUILD VS v0.3 draft codes**, not official ELM or EU vocabulary identifiers. Formal consortium publication approval remains a governance step. Issuers SHALL substantiate external QA and accreditation claims. General issuer claim-handling policy is not assessment QA.

#### 4.4.5a Assessment grade and grading scheme

`grade` and `gradingScheme` SHALL use the **same string representation as MC**. For `validated` claims both SHALL be present. The default scheme is `Pass/Fail`, with successful grade `Pass`. Other defined schemes are permitted where the issuer can establish which grade constitutes successful completion. `skillProficiencyLevel` is a separate Dreyfus proficiency classification, not the assessment grade. No separate `assessmentResult` claim is defined.

#### 4.4.6 Validation phases

Where `validationProcess` is present, `phases` MAY contain objects with `type` equal to `identification`, `documentation`, `assessment` or `certification`, and optional `completionDate`, `responsibleBody` and `evidenceReference`. Record completed activities truthfully. Credential issuance alone does **not** establish that certification under the Council Recommendation occurred.

#### 4.4.7 Legal category

The mandatory `category` claim SHALL be `eaa:eu:non-qualified`. The legacy `attestation_legal_category` SHALL NOT appear in newly issued VS v0.3 credentials. For this claim, the newer EUDI Rulebook template takes precedence over the older MC v1.0 convention, solely because VS is a non-qualified EAA; no change to MC is proposed.

### 4.5 Integrity rules

| ID | Rule / applicable check |
|---|---|
| VS-IR-01 | All §3.2 and §4.1 mandatory claims SHALL exist at **issuance**, subject to the applicable `cnf` policy; `category` SHALL be `eaa:eu:non-qualified`, and the legacy category claim SHALL be absent. |
| VS-IR-02 | `validationStatus` SHALL be one of the three codes in §4.4.2. |
| VS-IR-03 | Dreyfus code, when present, SHALL be one of the five §4.4.1 codes; it SHALL be present if validated. |
| VS-IR-04 | EQF/NQF SHALL NOT substitute for Dreyfus proficiency. |
| VS-IR-05 | `learningOutcomes` SHALL be non-empty and each element SHALL have MC-compatible `title` and `description`. |
| VS-IR-06 | All outcomes in one attestation SHALL share validation status, stated proficiency and assurance context. |
| VS-IR-07 | A validated claim SHALL contain all §3.4 required fields, including `awardingBody` and `gradingScheme`, and SHALL reflect successful assessment under the stated scheme. |
| VS-IR-08 | The relevant assessment standard, assessor, confirmation, authorisation, evidence and QA SHALL exist for validated status, even if evidence is not disclosed. |
| VS-IR-09 | Documented status SHALL have traceable supporting evidence in underlying records. |
| VS-IR-10 | Identified/documented status SHALL NOT be presented as formal validation. |
| VS-IR-11 | `assessmentIndependence` SHALL be a permitted code; claimed third-party independence SHALL be substantiated. |
| VS-IR-12 | QA/accreditation claims SHALL reflect real arrangements within their valid scope. |
| VS-IR-13 | `volumeOfLearning` SHALL be a positive ISO 8601 duration, if stated; never invented from unmeasurable work experience. |
| VS-IR-14 | `issuanceDate` SHALL NOT precede recorded `assessmentDate` for validated claims. |
| VS-IR-15 | `validationProcess` SHALL NOT falsely record phases as completed. |
| VS-IR-16 | Credential validity/`status` SHALL be assessed independently of `validationStatus`. |
| VS-IR-17 | Technical verification SHALL NOT imply automatic credit, professional recognition or qualification equivalence. |
| VS-IR-18 | Mandatory issued attributes MAY be selectively undisclosed; verifier SHALL assess sufficiency of the **disclosed** claims for its purpose. |

Schema checks MAY enforce type/presence/enumerations and a subset of conditions. They **cannot** verify assessment competence, real evidence, authority, trust, signatures or semantic truth.

## 5 Formats

| Format | In scope | Identifier / note |
|---|---|---|
| SD-JWT VC | **Yes** | `vct` provisional URI in §4.1; `dc+sd-jwt` for relevant OpenID4VCI credential configuration. |
| ISO/IEC 18013-5 mdoc | No | No namespace or document type defined. |
| W3C VCDM | No | No VCDM encoding defined. |

### 5.1 SD-JWT VC-based encoding

The payload SHALL use claims in Chapters 3–4 and an approved, published versioned `vct`. Shared logical claims SHALL follow the existing MC v1.0 JSON structures. Identifiers `iss`, `iat`, `vct` SHALL be present as required by the agreed technical profile. The applicable profile SHALL define Holder binding, status, signing and disclosures. The `dc+sd-jwt` label belongs to the OpenID4VCI credential configuration, **not** to a payload claim.

A reconstruction of the **issued full payload** SHALL satisfy the normative schema, once approved. Disclosure handling SHALL follow SD-JWT VC: `givenName`, `familyName`, outcomes, status of skill claim, proficiency and assurance data MAY be selectively encoded as appropriate, while protocol-critical claims follow the technical profile. A verifier SHALL request sufficient related claims to interpret a skill correctly. Disclosure of `skillProficiencyLevel` without `validationStatus` may be misleading; issuers and verifiers SHOULD support coherent presentation of these claims.

The schema cannot establish the validity of SD-JWT signatures, cryptographic binding, disclosure digests or authorisations. No unsupported assumptions about automatic disclosure of all required issuance fields shall be made.

#### 5.1.1 Selective-disclosure classification

The table below sets the **issuer-side** disclosure classification. A claim being mandatory on the issued credential does not mean it must be revealed in every presentation. "MUST" means the issuer must encode the claim so it can be selectively disclosed, not that the holder must disclose it. SD-JWT VC type metadata SHOULD express the same rules. For nested values and array elements, the issuer SHALL follow the same classification as the parent unless a more protective explicit per-property rule is provided in published type metadata.

| Claim(s) | Issuer selective-disclosure rule | Notes |
|---|---|---|
| `iss`, `iat`, `vct`, `cnf`, `category` | **MUST NOT** | Protocol, binding, type and legal-category context remains visible. |
| `exp`, `nbf`, `status`, `trust_anchor` when used | **MUST NOT** | Credential validity and trust mechanisms require contextual access. |
| `identifier`, `title`, `issuanceDate`, `issuerCountry`, `awardingBody` (when present) | **MAY** | `awardingBody` is mandatory at issuance only for validated claims; sufficient issuer context is still needed for relying-party decisions. |
| `givenName`, `familyName`, optional additional person claims | **MUST** for given/family names; **MAY** for other person claims | Data minimisation; mandatory issuance does not force disclosure. |
| `learningOutcomes`, `validationStatus` | **MUST** | Verifiers SHOULD request both for meaningful interpretation. |
| `skillProficiencyLevel`, `typeOfAssessment`, `assessmentStandard`, `grade`, `assessmentDate` | **MAY** | Claim presence at issuance remains conditional; assess sufficiency of disclosures. |
| `assessor`, `validatingBody`, `assessmentIndependence`, `qualityAssurance` | **MAY** | Assurance information can be required by the verifier for a validated-skill decision. |
| `volumeOfLearning`, `formOfParticipation`, `escoReference`, `supportingEvidence`, `validationProcess`, `accreditation`, `reviewDate`, `recognitionReference`, `gradingScheme` | **MAY** | Underlying evidence need not be placed in the credential. |

At issuance, a top-level structure may be disclosed as a unit or through individually disclosed nested elements where supported and where doing so preserves semantic clarity. Presentation sufficiency SHALL be evaluated by the Relying Party; successful cryptographic verification alone does not imply enough attributes have been disclosed to establish formal validation.

#### 5.1.2 Illustrative reconstructed issued payload

The following is a **test example**, not a complete cryptographically issued SD-JWT VC. All organisations and the standard are fictitious; the `vct` is provisional.

```json
{
  "vct": "https://webuildconsortium.eu/credentials/verified-skill/0.3",
  "iss": "https://issuer.example.org",
  "iat": 1795521600,
  "category": "eaa:eu:non-qualified",
  "identifier": "VS-2026-0007421",
  "title": "Industrial Compressor Operation",
  "givenName": "Elena",
  "familyName": "Kowalska",
  "issuerCountry": "http://publications.europa.eu/resource/authority/country/NLD",
  "awardingBody": {"legalName": "Example Skills Organisation"},
  "issuanceDate": "2026-11-24",
  "learningOutcomes": [{"title": "Industrial compressor operation", "description": "Operates industrial compressors safely under normal operating conditions."}],
  "validationStatus": "validated",
  "skillProficiencyLevel": "competent",
  "typeOfAssessment": ["http://data.europa.eu/snb/assessment/6a4db9f11d"],
  "assessmentStandard": {"title": "Example Workplace Competency Standard", "version": "2.0"},
  "grade": "Pass",
  "gradingScheme": "Pass/Fail",
  "assessmentDate": "2026-11-20",
  "assessor": {"legalName": "Example Assessment Organisation"},
  "validatingBody": {"legalName": "Example Validation Body"},
  "assessmentIndependence": "independent-third-party",
  "qualityAssurance": "documented-internal-qa"
}
```

An actual Holder-bound credential SHALL additionally satisfy the chosen HAIP/key-binding profile, including `cnf` as required. The assessment-type URI shown is illustrative pending vocabulary resolution.

### 5.2 ISO/IEC 18013-5-compliant encoding

Not defined in v0.3. Any future mdoc format requires its own normative namespaces, types and presentation policy.

### 5.3 W3C Verifiable Credentials Data Model-based encoding

Not defined in v0.3; ELM JSON-LD mappings are informative and do not implicitly create a W3C VCDM profile.

## 6 Protocols

### 6.1 Issuance

The Issuer SHALL use OpenID4VCI under the applicable EUDI/HAIP profile. Issuer metadata SHALL identify a configuration with `format: dc+sd-jwt` and the approved `vct`. Before issuance, the Issuer SHALL complete the claim-status-dependent checks in Chapter 7; protocol success is not evidence of a substantively validated skill.

### 6.2 Presentation

Remote presentations SHALL use OpenID4VP under the applicable EUDI/HAIP profile. A Relying Party SHOULD use DCQL where required by the selected protocol release, requesting only the claims necessary to decide on the specific purpose. Proximity presentation is out of scope. A successful OpenID4VP exchange does not grant recognition.

## 7 Issuance

### 7.1 Binding

The attestation SHALL relate to a natural person. The Issuer SHALL reliably link the recipient to the individual who made the assertion or underwent the assessment, proportionate to purpose and risk. Cryptographic holder binding and subject identity verification are distinct. A PID MAY be requested when strong cross-credential identity matching is needed under the applicable EUDI policy. The actual binding claims SHALL follow the technical profile, not assumed universal requirements.

### 7.2 Issuance Policy

The Issuer SHALL ensure that it is authorised for the VS attestation type and that the responsible party is identified. The Issuer, Awarding Body, Assessor and Validating Body MAY coincide or be separate; relationships SHALL be documented as needed. The Issuer SHALL not claim to have performed assessment or validation it did not perform.

**Identified:** the source of declaration/identification and applicable issuer acceptance policy SHALL be recorded. Assessment and independent validation are **not** implied. Dreyfus proficiency is optional.

**Documented:** relevant evidence SHALL exist, be subject to an identifiable evidence-acceptance policy and be retained or traceable by a responsible organisation. Evidence MAY be referenced rather than disclosed. Formal validation is **not** implied.

**Validated:** before issuance, the Issuer SHALL establish an appropriate standard, completed successful assessment, assessment date, assessor, competent and authorised validating body, assessment independence, supporting evidence and applicable QA. The validating body need not hold educational accreditation merely because the skill is unregulated; any actual scheme-specific authorisation/accreditation requirements still apply. The issuer SHALL document how it establishes the body’s scope and competence.

Evidence retention SHALL respect data protection, confidentiality, security and applicable retention rules. Recognition decisions MAY be referenced but are not automatically awarded by a VS.

### 7.3 Lifecycle management

The Issuer SHALL maintain procedures for correction, withdrawal, expiry, review and supersession. A newer assessment SHOULD result in a new credential if material proficiency/status changes. An earlier historically correct credential is not automatically false merely because a new one exists. `reviewDate` is not `exp`.

### 7.4 Embedded disclosure policy

No special embedded disclosure policy is defined. Data-minimisation and selective-disclosure requirements of the selected technical profile continue to apply.

## 8 Revocation

Revocation removes confidence in an attestation **as issued**; expiry ends technical credential validity; reassessment determines current competence. These are separate events. The Issuer SHALL revoke or correct an attestation where material incorrectness, misissuance, fraud or overturning of the supporting validation makes the original claim unreliable under its policy. For `documented`, discovery of fraudulent or unsuitable evidence may trigger revocation; for `validated`, overturning the assessment/validation may do so.

Skill obsolescence, expiry of a review period or an assessor organisation's later loss of authorisation does not **automatically** retroactively invalidate a historically accurate claim. Relevant scheme rules and the temporal scope of authorisation decisions SHALL be applied. The Issuer SHALL communicate with assessment/validation organisations where separate and use a permitted, privacy-preserving credential-status mechanism. A replacement credential SHALL have a new identifier; revoke the earlier one where correction or applicable policy requires it.

## 9 Presentation

### 9.1 Presentation Policy

A Relying Party SHALL distinguish: (1) cryptographic verification and credential status; (2) issuer authorisation; (3) interpretation and assurance of the underlying skill assertion; (4) substantive acceptance/recognition. Successful checks at one stage SHALL NOT automatically settle the others.

- `identified` means a declaration or identification was recorded; it is **not** proof of independent assessment.
- `documented` means supporting evidence exists; it is **not** proof of formal validation.
- `validated` means successful assessment against a relevant standard and confirmation by the competent validating body; it does **not** confer universal professional or educational recognition.

Where the use case demands formal validation, a Relying Party SHALL request the relevant disclosed `validationStatus`, learning outcomes, standard, assessment and QA information and SHALL evaluate sufficient trust in the relevant body. Dreyfus proficiency SHALL NOT be mapped algorithmically to EQF. An ESCO identifier supports semantic matching but does not define a proficiency level or assessment standard.

A Relying Party MAY use VS as evidence for recognition of prior learning but SHALL make any credit, qualification, admission or exemption decision through its applicable recognising procedures. Only necessary personal and assessment data SHOULD be requested. Missing disclosure is not necessarily a malformed signed credential; it may mean insufficient evidence for the transaction.

### 9.2 Presentation modes

Remote OpenID4VP presentation only. No mdoc proximity mode is defined. DCQL requests SHALL follow the applicable protocol release and profile.

### 9.3 Transactional data

No attestation-type-specific transactional data is defined; protocol nonces and transaction-binding data remain subject to the selected technical profile.

## 10 Trust Framework

Trust in an authentic non-qualified EAA issuer SHALL be separated from trust in the underlying assertion, assessment and QA. An Issuer SHALL be authorised for the approved `vct` under an applicable trust framework. Issuer metadata alone is not proof of authorisation unless authenticated by the chosen trust mechanism. This Rulebook does not mandate a single central registry or federation technology.

For `validated`, the competent Validating Body SHALL be identifiable and its scope under the relevant assessment standard SHALL be substantiated by an applicable sectoral, employer, professional or public validation arrangement. The assessor may differ from the validating body; independence SHALL be independently assessable. A public or private organisation may operate a valid non-formal scheme, but entry into a trust list or possession of accreditation does not automatically establish competence for every skill.

QA information SHALL distinguish documented internal QA, external oversight and actual accreditation. An ISO-standard reference alone does not demonstrate certification. Trust and authorisation changes SHALL be evaluated in relation to the assessment date and applicable scheme rather than presumed retroactive. Relying Parties MAY impose proportionate, use-case-specific acceptance rules.

## 11 References

- Council Recommendation 2012/C 398/01, validation of non-formal and informal learning: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32012H1222(01)
- Council Recommendation 2022/C 243/02, European approach to Micro-credentials: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022H0627(02)
- Cedefop (2023), *European guidelines for validating non-formal and informal learning*, third edition: https://doi.org/10.2801/389827
- Regulation (EU) No 910/2014 as amended by Regulation (EU) 2024/1183.
- European Digital Identity Wallet Architecture and Reference Framework (ARF), original basis 3.0.0; reconfirm applicable release.
- European Learning Model (ELM), version 3.3: https://europa.eu/europass/elm-browser/index.html
- ESCO classification: https://esco.ec.europa.eu/
- WE BUILD Micro-credential Rulebook v1.0 (fixed technical and semantic reference): https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/tree/main/rulebooks/rb-microcredential
- WE BUILD Verified Skill Rulebook v0.2 (source): https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/tree/main/rulebooks/rb-verified-skill
- SD-JWT / SD-JWT VC, OpenID4VCI 1.0, OpenID4VP 1.0, HAIP and their applicable versions.
- JSON Schema Draft 2020-12; RFC 2119; RFC 8174.
- Dreyfus, S.E. and Dreyfus, H.L. (1980), *A Five-Stage Model of the Mental Activities Involved in Directed Skill Acquisition*.
- ISO/IEC 17024 (personnel certification), ISO 21001 (educational organisation management systems), where applicable.

## Annex A — ELM mapping decisions

**Informative.** SD-JWT claim names are not identical to ELM ontology paths. An ELM concept mapping is not a claim of an exact verified v3.3 property path unless explicitly identified below.

| VS claim/concept | ELM / MC relationship | Status |
|---|---|---|
| `identifier`, `title`, Holder identity, `issuerCountry`, `issuanceDate` | Reuse MC-compatible credential/person/organisation semantics | Common structures adopted; exact full ontology paths to be checked. |
| `awardingBody` | MC organisation object (`legalName`, optional `legalIdentifier`) | **Same JSON structure**; optional for identified/documented and mandatory for validated; represents an actual award, not recordkeeping. |
| `learningOutcomes` | Learning Outcome / Learning Achievement Specification | Reuse MC shape; exact ELM link/path to confirm. |
| `typeOfAssessment` | Learning Assessment Specification assessment type | Reuse MC vocabulary/shape. |
| `grade`, `gradingScheme` | Learning Assessment and grading scheme | Reuse MC strings; Pass/Fail is default. Positive result checked under grading scheme in issuer business logic. |
| `assessmentStandard` | Learning Assessment Specification and external standards | `LearningAssessmentSpecification` (`title`, `description`, `identifier`, `homepage` where appropriate); `LearningAssessment.specifiedBy` links the assessment to its specification. Flattened fields are VS JSON profile conventions. |
| `assessor` | Learning Assessment actor/agent | Reuse `LearningAssessment.assessedBy` for the responsible assessor/assessment body where semantically equivalent; allow a separate individual assessor representation. |
| `validatingBody` | Distinct confirming body | May require narrow VS extension if ELM cannot distinguish role. |
| `supportingEvidence` | ELM evidence-related model | Use `supplementaryDocument` for associated documents where appropriate and `provenBy` for assessment provenance; retain private evidence off-credential. |
| `volumeOfLearning` | ELM learning volume | Reuse MC representation, optional. |
| `escoReference` | Related ESCO skill or competence | Reuse applicable concept and canonical URI. |
| `accreditation` | ELM Accreditation | Only actual accreditation; not generic QA. |
| `validationStatus` | WE BUILD profile | VS extension. |
| `skillProficiencyLevel` | Dreyfus proficiency | VS extension, separate from EQF. |
| `assessmentIndependence` | Relationship / independence of assessor | VS extension. |
| `validationProcess` | Identification/documentation/assessment/certification phases | VS extension. |
| `qualityAssurance` | MC attribute with compatible string shape | Includes the two agreed VS-specific QA values; not a substitute for ELM Accreditation. |

### Annex A.1 Semantic distinction

Verification of an SD-JWT VC attests issuer provenance/integrity; validation of skills is a separate substantive process. The 2012 Recommendation defines four phases, not three mandatory status codes. No mapping SHALL substitute credential status for learning validation status, Dreyfus for EQF, or an Accreditation object for ordinary QA.

### Annex A.2 Guidance on extensions

Use existing ELM classes/properties where the mapping accurately describes the real-world fact. New VS terms SHALL have stable definitions, explicit JSON data types and testable cardinalities. Do not add a new ELM property solely to mirror an existing WE BUILD claim name. Assessment authorisation may be established by external trust arrangements rather than embedded in the credential.

### Annex A.3 Recognition pathway

A VS can serve as supporting evidence for a learning-recognition process. The result of recognition, such as exemption or an awarded qualification/micro-credential, is a **separate decision** by the appropriate body and SHOULD be separately evidenced or referenced. Mere VS issuance does not trigger such recognition.

### Annex A.4 ELM v3.3 mapping decisions and residual technical verification

1. **Assessment standard:** reuse `LearningAssessmentSpecification`; the assessment-to-specification relationship is `specifiedBy`. The VS `assessmentStandard` object is a flattened representation with `title` and optional `identifier`, `description`, `version`, `reference` and `criteria`. A reference to the external standard must not be mistaken for proof of assessment quality.
2. **Evidence:** use `supplementaryDocument` when the supplied evidence genuinely describes a supporting document, and `provenBy` for a learning achievement's assessment provenance. `supportingEvidence` is optional disclosure metadata; underlying sensitive records may remain with the responsible body. Do not misuse ELM credential-level `Evidence` as generic workplace assessment evidence.
3. **Assessment performer:** use `LearningAssessment.assessedBy` where the referenced person/body corresponds to the responsible assessor; the VS claim supports both organisations (MC-shaped) and individual assessors.
4. **Validating body:** preserve the explicit VS `validatingBody` role if organisational validation responsibility differs from the awarding or assessment role. The `awardingBody` object shape is unchanged from MC and is required only for validated skills; it may be supplied otherwise only when an actual achievement was awarded.
5. **Assessment outcome:** reuse MC `grade` and `gradingScheme` strings; default `Pass` with `Pass/Fail`, while scheme-specific success remains an issuer/business-rule check.

**ELM 3.3.1 review:** see Annex A.6 for checked paths, expected value classes and EDC-profile cardinalities. These constraints do not automatically become required VS JSON claim cardinalities. An executed RDF/SHACL round-trip test remains outstanding.

### Annex A.5 Recommendations for ELM v3.4

**Proposals, not claims about an already released ELM v3.4.** WE BUILD recommends evaluating the following enhancements against existing v3.3 ontology and application profiles, prioritising guidance or existing concepts before introducing new properties.

| Priority | Proposed enhancement |
|---|---|
| High | Explicit distinction between identified, documented and formally validated learning-outcome assertions. |
| High | Optional structured provenance for the four Council Recommendation validation phases. |
| High | Framework-neutral proficiency referencing (including Dreyfus), without inferring EQF equivalence. |
| High | Assessment-independence semantics independent from QA and accreditation. |
| High | Links from prior-learning validation to distinct recognition decisions, exemptions and qualifications. |
| Evaluate existing support first | Structured assessment standards and observable criteria; assessor and validating roles; evidence provenance with privacy-preserving external references; workplace/sectoral QA; learning volume without ECTS. |

The purpose is **one semantic ecosystem**, not a competing Verified Skills ontology or a requirement to change the MC Rulebook as part of this work.


### Annex A.6 — ELM 3.3.1 EDC application-profile property audit

The following property ranges and cardinalities were checked against the European Commission's **ELM 3.3.1 EDC application-profile SHACL constraint documentation** (documentation release 1.3.0, last updated 3 February 2026). They describe the EDC profile, **not** the obligation of flattened SD-JWT VS attributes. Canonical ELM property namespace: `http://data.europa.eu/snb/model/ontology/`. `dc:` and `adms:` remain their own namespaces.

| EDC subject | Property | EDC range | EDC cardinality | VS mapping implication |
|---|---|---|---|---|
| `LearningAssessment` | `elm:specifiedBy` | `LearningAssessmentSpecification` | 0..1 | VS `assessmentStandard` requires specification when validated, exceeding EDC minimum. |
| `LearningAssessment` | `elm:grade` | `Note` | 1..1 | Flattened MC/VS `grade` string requires an explicit Note conversion. |
| `LearningAssessment` | `elm:gradeStatus` | `Concept` | 0..1 | Binary Pass/Fail may be mapped to pass/fail Concept; not a replacement for MC `grade`. |
| `LearningAssessment` | `elm:assessedBy` | Agent / Person / Organisation | 0..* | Supports responsible assessor, not necessarily each individual examination observer. |
| `LearningAssessment` | `elm:awardedBy` | `AwardingProcess` | 1..1 | An EDC conversion needs an AwardingProcess even if VS flattened `awardingBody` is absent. |
| `LearningAssessmentSpecification` | `elm:gradingScheme` | `GradingScheme` | 0..1 | Flattened `gradingScheme` string requires a GradingScheme conversion. |
| `LearningAssessmentSpecification` | `elm:specialisationOf` | `LearningAssessmentSpecification` | 0..* | May link a specific assessment scheme to a broader scheme. |
| `AwardingProcess` | `elm:awardingBody` | Agent / Person / Organisation | 0..* | EDC itself does not impose a mandatory body; VS does for validated claims. |
| `LearningAchievement` | `elm:provenBy` | `LearningAssessment` | 0..* | Links an achievement to its assessment. |
| `LearningAchievement` / `LearningAssessment` | `elm:supplementaryDocument` | `WebResource` | 0..* | Describes public supplementary documents, **not** restricted evidence repositories. |
| `LearningAchievementSpecification` | `elm:learningOutcome` | `LearningOutcome` | 0..* | VS requires at least one outcome in its issued claim representation. |

**Evidence boundary:** `elm:supplementaryDocument` is described in the EDC profile as a *public web document*. It SHALL NOT be used to claim that a confidential or access-controlled workplace portfolio is publicly resolvable. Use the VS `supportingEvidence` extension for limited summaries or appropriately scoped non-public references, with privacy and access control governed outside the credential.

**Terminology boundary:** `LearningAssessment.grade` is an `elm:Note`, not a native string, and the grading scheme is a structured `GradingScheme` class. Using MC-compatible strings in SD-JWT is a deliberate **profile flattening**, not literal RDF equivalence. A JSON-to-RDF transform SHALL construct the expected ELM objects and respect language tags and profile constraints.

**Conformance boundary:** This annex records documented SHACL constraint values; raw RDF graph validation against the complete EDC shape graph has not been executed. Final ELM interoperability testing SHALL include transformation of at least one validated VS example to RDF, SHACL validation and round-trip preservation of its semantics.

**Authoritative reference:** https://europa.eu/europass/elm-browser/documentation/3-3-1/rdf/ap/edc/documentation/edc-generic-full_en.html

## Annex B — Publication decisions and verification

**This appendix is editorial, not normative. The draft is NOT publication-ready until the following are resolved.**

| Ref | Open decision / verification | Required action |
|---|---|---|
| B-01 | Legal-category production sign-off | This draft uses `category=eaa:eu:non-qualified` and prohibits legacy `attestation_legal_category`; confirm it against the deployment's final ARF/ETSI profile. **Do not edit MC**. |
| B-02 | `vct` ownership | Approve and publish `https://webuildconsortium.eu/credentials/verified-skill/0.3` or a controlled alternative with matching schema and issuer metadata. |
| B-03 | ELM mapping conformance | Official ELM 3.3.1 EDC property/range/cardinality documentation reviewed (Annex A.6). An RDF conversion, actual SHACL validation and datatype/profile-path round-trip remain to be tested before an end-to-end ELM conformance claim. |
| B-04 | QA vocabulary | Two VS-only values agreed for the v0.3 draft; final consortium publication approval and code-list publication still apply. |
| B-05 | Assessment grade semantics | Resolved: `grade` and `gradingScheme` are mandatory for validated skills. Default `Pass` / `Pass/Fail`; alternative schemes require documented issuer-side success logic. |
| B-06 | Holder binding / status | Ratify deployment-specific HAIP, `cnf`, PID binding, and status requirements; align with actual ARF release. |
| B-07 | Full template traceability | Update every original EW-DM-12 line with verified current section references; avoid claiming conformance solely on the basis of this draft. |
| B-08 | End-to-end testing | Local schema/signature/selective-disclosure/holder-binding smoke tests have passed with test keys, but real OpenID4VCI issuer, wallet, OpenID4VP/DCQL verifier, status and trust interoperability and HAIP conformance remain untested. |
| B-09 | Awarding-body semantics | Resolved in VS profile: `awardingBody` is required for validated skills, optional for other statuses only when an actual award occurred; MC structure unchanged. |

**Change log:** v0.3 consolidates the chapter drafts and subsequent simplifications; keeps MC v1.0 fixed as the semantic baseline; does not undertake MC's separate PuB-EAA rewrite; retains VS as a non-qualified EAA; rationalises attributes and QA; adopts the newer `category` convention; documents open approval points rather than silently resolving them.
