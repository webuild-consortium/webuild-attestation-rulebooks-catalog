(Template version: 1.1)

# WE BUILD Attestation Rulebook for attestations of type *Verified Skill*

*[Based on the WE BUILD Attestation Rulebook Template, the WE BUILD BU5 Micro-credential Attestation Rulebook, and the WE BUILD BU5 Verified Skill EAA Design.]*

* Author(s):
  * Paul den Hertog
* Previous Authors
  * N/A

| Version | Date | Description |
|---------|------|-------------|
| 0.1 | 2026-08-31 | Initial draft Rulebook for the Verified Skill Attestation |

**Feedback:**

* Github, portal, email, Slack

## 1 Introduction

### 1.1 Document scope and purpose

This Rulebook defines the *Verified Skill Attestation* for use in the European Digital Identity Wallet ecosystem.

The Verified Skill Attestation is a non-qualified Electronic Attestation of Attributes (EAA) that enables a natural person to demonstrate possession of one or more unregulated skills or competences. The attestation represents a structured and digitally verifiable claim that a specific skill or competence has been (self)assessed, validated, or otherwise established on the basis of defined evidence.

The attestation is intended for employment, workplace learning, non-formal learning, internal mobility, access to training, recruitment, onboarding, skills matching and other situations in which a Relying Party requires trustworthy evidence of a natural person's skills or competences.

Unlike a Micro-credential Attestation, a Verified Skill Attestation does not require the underlying achievement to be part of formal education, does not use an EQF level as its skill-proficiency measure, does not require workload to be expressed in ECTS, and does not assume quality assurance under the Standards and Guidelines for Quality Assurance in the European Higher Education Area (ESG).

Instead:

* proficiency SHALL be expressed using the Dreyfus Model of Skill Acquisition defined in this Rulebook;
* where workload is meaningful, it SHALL be expressed as study or learning load in hours;
* quality assurance SHALL be described using the quality-assurance method and quality-assurance level defined in this Rulebook;
* the attestation MAY refer to recognised external quality frameworks, certification schemes, accreditation mechanisms, audit procedures or standards, including applicable standards defined by e.g. ISO, or other applicable standardised frameworks;
* a skill SHOULD, where possible, be referenced to an ESCO skill or competence concept.

The Verified Skill Attestation does not in itself grant a legal licence, regulated professional status, protected title, formal qualification, ECTS credit(s), EQF level, or the right to practise a regulated profession.

The organisation that seals/issues the credential and the organisation or assessor responsible for establishing the skill may be the same organisation or different organisations.

### 1.2 Document structure

This Rulebook is structured as follows:

* Chapter 2 describes the attestation attributes and metadata in an encoding-independent manner.
* Chapter 3 specifies how the attestation attributes and metadata are encoded using SD-JWT VC. ISO/IEC 18013-5 and W3C VCDM encodings are not defined in this version.
* Chapter 4 specifies attestation usage, including presentation and verification expectations.
* Chapter 5 defines how trust anchors for attestation verification can be obtained.
* Chapter 6 defines revocation and expiry mechanisms.
* Chapter 7 provides compliance information.
* Chapter 8 lists references.

### 1.3 Key words

This document uses the capitalised key words 'SHALL', 'SHOULD' and 'MAY' as specified in RFC 2119.

In addition, 'must' (non-capitalised) indicates an external constraint. The word 'can' indicates a capability; other words such as 'will', 'is' and 'are' are statements of fact.

### 1.4 Terminology

This document uses the terminology specified in Annex 1 of the EUDI Wallet Architecture and Reference Framework (ARF).

| Term | Meaning |
|------|---------|
| Verified Skill Attestation | A Verifiable Credential representing a person's assessed or otherwise established possession of an unregulated skill or competence at a stated proficiency level. |
| Holder | The natural person to whom the Verified Skill Attestation relates. |
| Skill | An ability or competence demonstrated by the Holder and capable of being assessed against defined criteria. |
| Skill assertion | The statement linking a Holder to a defined skill or competence. |
| Skill Assessor | A person or organisation responsible for assessing or establishing the Holder's skill against defined criteria. |
| Issuer / Attestation Provider | The organisation that issues and cryptographically seals the Verified Skill Attestation. |
| Assessment evidence | Information or evidence on which the determination of the Holder's skill and proficiency is based. |
| Dreyfus Model | The five-stage proficiency model used by this Rulebook: novice, advanced beginner, competent, proficient and expert. |
| Study load | Where applicable, the estimated amount of learning, preparation, practice and/or assessment time associated with acquisition or demonstration of the skill, expressed in hours. |
| Quality-assurance method | The procedure, framework, standard, certification, accreditation, audit or organisational process underpinning the assessment and/or issuance process. |
| Quality-assurance level | The assurance classification defined by this Rulebook: self-asserted, third-party assessed, or audited assessment. |
| ESCO | European Skills, Competences, Qualifications and Occupations classification. |
| ELM | European Learning Model, used for semantic interoperability where a suitable ELM concept or property exists. |
| Relying Party | An organisation or system that verifies the Verified Skill Attestation to make a recruitment, mobility, training, access, matching or other decision. |

## 2 Attestation attributes and metadata

### Chapter overview and requirements

This chapter defines the attributes and metadata that a Verified Skill Attestation may contain. Attributes are defined in an encoding-independent manner and classified as mandatory, optional or conditional.

The Verified Skill model is aligned with the European Learning Model (ELM) where a semantically appropriate ELM property exists. The ELM is capable of representing formal, non-formal and informal learning. This Rulebook therefore reuses ELM concepts where appropriate without treating education-specific properties such as EQF level or ECTS credit as suitable proxies for skill proficiency or workload.

Where ELM has no semantically correct property for a Verified Skill concept, this Rulebook defines a Verified-Skill-specific extension instead of overloading an unrelated ELM field.

### 2.1 Introduction

The Verified Skill Attestation is defined as a non-qualified Electronic Attestation of Attributes unless a future version explicitly defines another legal category.

The attribute `attestation_legal_category` SHALL be included and SHALL have the value `non-qualified-EAA`.

The model consists of:

* credential identification attributes;
* issuer and assessing/awarding organisation attributes;
* Holder identity attributes for subject matching;
* skill and proficiency attributes;
* assessment and evidence attributes;
* learning/workload attributes where relevant;
* taxonomy references;
* quality-assurance attributes;
* credential metadata.

The attestation SHALL be issued as a Verifiable Credential compatible with the EUDI Wallet using SD-JWT VC.

Issuer metadata parameters:

* `scope`: `VerifiedSkill`;
* `format`: `vc+sd-jwt`;
* `vct`: `VerifiableVerifiedSkill`;
* `claims`: the claims defined in this Rulebook;
* `proof_types_supported`: issuer-defined, including `jwt` where supported;
* `cryptographic_binding_methods_supported`: issuer-defined, for example `jwk` or `cose_key`.

### 2.2 Mandatory attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---------------------|------------------------|----------------|---------------|-------------------|
| `attestation_legal_category` | ARF Topic 12 / Rulebook legal category | Legal category of the attestation. | string | `non-qualified-EAA` |
| `identifier` | ELM `credential.identifier` or equivalent credential identifier | Unique identifier of the Verified Skill Attestation instance. | string | `VS-2026-0007421` |
| `title` | ELM credential title/display title | Human-readable title of the Verified Skill Attestation. | string | `Industrial Hydrogen Compressor Operation` |
| `givenName` | ELM Person / credential subject | Holder given name. | string | `Elena` |
| `familyName` | ELM Person / credential subject | Holder family name. | string | `Kowalska` |
| `issuerCountry` | ELM issuer organisation location/country | Country or region of the organisation that sealed/issued the credential. | string (ISO 3166-1 alpha-2) | `NL` |
| `awardingBody` | ELM `credential.credentialSubject.hasClaim[0].awardedBy.awardingBody[0].legalName`, where this claim structure is used | Organisation responsible for awarding or establishing the skill claim. | string | `Example Hydrogen Training Centre` |
| `issuanceDate` | ELM `credential.issued` | Date on which the credential was sealed and issued. | date | `2026-06-15` |
| `skillOutcome` | ELM `credential.credentialSubject.hasClaim[0].specifiedBy.learningOutcome`; skill-focused use | Description of the skill or competence assessed and demonstrated by the Holder. | string or array of strings | `Operates an industrial hydrogen compressor safely under normal operating conditions` |
| `skillProficiencyLevel` | Verified Skill extension; linked semantically to the attested skill/learning outcome | Degree of mastery according to the Dreyfus proficiency model. | string | `competent` |
| `typeOfAssessment` | ELM `credential.credentialSubject.hasClaim[0].specifiedBy.provenBy[0].dcType` | Method used to establish the skill. | string | `structured-observation` |
| `qualityAssuranceMethod` | ELM Accreditation when actual accreditation applies; otherwise Verified Skill extension | Procedure, framework, standard or organisational QA method underpinning assessment and/or issuance. | object | `{ "type": "ISO-standard", "reference": "ISO/IEC 17024" }` |
| `qualityAssuranceLevel` | Verified Skill extension | Assurance level of the assessment process as defined by this Rulebook. | string | `third-party-assessed` |

### 2.3 Optional attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---------------------|------------------------|----------------|---------------|-------------------|
| `dateOfBirth` | ELM credential subject date of birth | Holder date of birth. | date | `1998-11-02` |
| `placeOfBirth` | ELM credential subject place of birth | Holder place of birth. | string | `Kraków, Poland` |
| `citizenshipCountry` | ELM credential subject citizenship country | Holder country of citizenship. | string | `PL` |
| `nationalID` | ELM credential subject national identifier | National or government-issued identifier. | string | issuer-defined |
| `registeredAddress` | ELM credential subject location/address | Holder address. | string | issuer-defined |
| `mail` | RFC 5322 / ELM credential subject contact point | Holder email address. | string | `elena@example.eu` |
| `escoReference` | ELM Learning Outcome `relatedESCOSkill` | URI reference to the corresponding ESCO skill or competence concept. | array of URI strings | `["http://data.europa.eu/esco/skill/..."]` |
| `studyLoadHours` | ELM `credential.credentialSubject.hasClaim[0].specifiedBy.volumeOfLearning` | Estimated workload associated with learning, practice and/or assessment, expressed in hours. | number | `80` |
| `assessmentBasis` | Verified Skill extension / ELM additionalNote or supporting evidence where suitable | Description of the evidence basis supporting the assessment. | string | `Observed operation during three supervised production shifts` |
| `assessmentEvidence` | ELM evidence where semantically suitable; otherwise Verified Skill extension | Structured references to evidence used to establish the skill claim. | array of objects | issuer-defined |
| `formOfParticipation` | ELM `credential.credentialSubject.hasClaim[0].specifiedBy.influencedBy[0].mode`, where a learning activity exists | Mode in which learning or demonstration occurred. | string | `workplace-based` |
| `learningActivityType` | ELM `credential.credentialSubject.hasClaim[0].specifiedBy.influencedBy[0].dcType`, where a learning activity exists | Type of activity through which the skill was acquired or demonstrated. | string | `work-experience` |
| `languageOfAssessment` | ELM / BCP 47 | Language in which the assessment was conducted. | string | `en` |
| `idVerificationMethod` | ELM `credential.credentialSubject.hasClaim[0].specifiedBy.provenBy[0].idVerification` | Supervision and identity-verification method used during assessment. | string | `onsite-with-identity-verification` |
| `assessor` | ELM assessment/agent structure where applicable; otherwise Verified Skill extension | Person or organisation that performed the skill assessment. | object | issuer-defined |
| `assessmentDate` | ELM assessment date where supported by the chosen claim structure; otherwise extension | Date on which the skill assessment was completed. | date | `2026-06-12` |
| `grade` | ELM `credential.credentialSubject.hasClaim[0].specifiedBy.provenBy[0].grade` | Grade/result where the assessment scheme produces one. | string | `Pass` |
| `gradingScheme` | ELM Grading Scheme | Scheme needed to interpret the grade/result. | string or object | `Pass/Fail` |
| `qualityFramework` | ELM Accreditation where actual accreditation applies; otherwise Verified Skill extension | Named framework, standard, scheme or documented QA process. | object | `{ "name": "ISO/IEC 17024", "uri": "..." }` |
| `accreditation` | ELM `credential.evidence[0].accreditation` | Structured accreditation details, only where an actual accreditation record exists. | object | issuer-defined |
| `auditInformation` | Verified Skill extension | Details of an independent audit relevant to QA level `audited-assessment`. | object | issuer-defined |
| `reviewDate` | Verified Skill extension / ELM accreditation review date where the review concerns an accreditation | Date on which reassessment or review is recommended or required. | date | `2029-06-15` |
| `additionalNote` | ELM `additionalNote` (generic) | Supplementary information not covered by another field. | string | issuer-defined |

### 2.4 Conditional attributes

| **Data Identifier** | **Semantic Reference** | **Condition** | **Data type** | **Example value** |
|---------------------|------------------------|---------------|---------------|-------------------|
| `dateOfBirth` | ELM credential subject | SHALL be included only where required for Holder matching or another justified purpose. | date | `1998-11-02` |
| `escoReference` | ELM `relatedESCOSkill` | SHOULD be included where the attested skill can be mapped to ESCO. | array of URI strings | `["http://data.europa.eu/esco/skill/..."]` |
| `studyLoadHours` | ELM `volumeOfLearning` | SHOULD be included only where a meaningful workload can be established. It SHALL NOT be invented solely to imitate ECTS. | number | `80` |
| `grade` | ELM assessment grade | SHALL be included only where the assessment produces a grade/result. If present, `gradingScheme` SHOULD also be present. | string | `Pass` |
| `accreditation` | ELM `credential.evidence[0].accreditation` | SHOULD be included where the QA method relies on an actual accreditation that can be represented by the ELM Accreditation class. | object | issuer-defined |
| `auditInformation` | Verified Skill extension | SHALL be present when `qualityAssuranceLevel` is `audited-assessment`, unless equivalent audit evidence is represented through `accreditation` or another structured evidence object. | object | issuer-defined |
| `assessmentEvidence` | ELM evidence / extension | SHOULD be present for `third-party-assessed` and `audited-assessment` where evidence can be disclosed without violating confidentiality, security, trade-secret or data-protection constraints. | array of objects | issuer-defined |

### 2.5 Mandatory metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---------------------|------------------------|----------------|---------------|-------------------|
| `vct` | SD-JWT VC | Verifiable Credential Type. | string | `VerifiableVerifiedSkill` |
| `iss` | SD-JWT VC / JWT | Identifier of credential issuer. | string | `https://issuer.example.eu` |
| `iat` | JWT | Credential issued-at time. | integer | `1781740800` |
| `cnf` | SD-JWT VC / JOSE | Holder binding confirmation where holder binding is used. | object | `{ "jwk": { ... } }` |

### 2.6 Optional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---------------------|------------------------|----------------|---------------|-------------------|
| `exp` | JWT | Expiration time of the credential instance. | integer | `1970361600` |
| `nbf` | JWT | Time before which credential MUST NOT be accepted. | integer | `1781740800` |
| `jti` | JWT | Unique credential-instance identifier. | string | `urn:uuid:...` |
| `status` | SD-JWT VC status mechanism | Status information enabling revocation/correction checks. | object | issuer-defined |
| `trust_anchor` | ARF Topic 12 | Trust anchor or trust-framework entry for issuer authorisation. | string | issuer-defined |
| `cryptographically_bound_to` | ARF Topic 12 | Identifier of another attestation to which this attestation is bound. | string | `urn:eudi:pid:1` |

### 2.7 Conditional metadata

| **Data Identifier** | **Semantic Reference** | **Condition** | **Data type** | **Example value** |
|---------------------|------------------------|---------------|---------------|-------------------|
| `status` | SD-JWT VC status mechanism | SHOULD be present where the issuer needs to revoke, suspend or correct a Verified Skill Attestation after issuance. | object | issuer-defined |
| `cryptographically_bound_to` | ARF Topic 12 | SHOULD be present where strong identity matching with PID or another identity attestation is required. | string | `urn:eudi:pid:1` |

### 2.8 Code lists

#### 2.8.1 Skill proficiency level

`skillProficiencyLevel` SHALL use the Dreyfus Model of Skill Acquisition:

| Value | Meaning |
|-------|---------|
| `novice` | Relies primarily on context-free rules and instructions; limited situational experience. |
| `advanced-beginner` | Recognises recurring situational aspects but still relies substantially on rules and guidance. |
| `competent` | Can plan, prioritise and perform deliberately in context, using experience to select appropriate actions. |
| `proficient` | Perceives situations more holistically, recognises salient aspects and adapts action based on experience. |
| `expert` | Demonstrates highly developed intuitive and analytical command of the skill in context. |

The Dreyfus value describes **skill proficiency**, not educational level, qualification level, seniority, job grade, or EQF level. Issuers SHALL NOT algorithmically equate Dreyfus stages with EQF levels.

#### 2.8.2 Quality-assurance level

`qualityAssuranceLevel` SHALL use one of the following values:

| Value | Meaning |
|-------|---------|
| `self-asserted` | The issuer/assessing organisation defines and operates the assessment and QA process without independent external assessment of that process. |
| `third-party-assessed` | An organisationally independent third party assesses the Holder, the assessment result, or the assessment process against documented criteria. |
| `audited-assessment` | The assessment process, assessment organisation or relevant quality-management/certification process is subject to a documented independent audit, certification or accreditation against a recognised standard, scheme or framework. |

The QA level expresses the **assurance context of the assessment process**. It SHALL NOT be used as a proxy for the Holder's proficiency.

A higher QA level does not automatically imply that the Holder has a higher skill-proficiency level.

#### 2.8.3 Assessment type

`typeOfAssessment` SHOULD reuse a suitable controlled-vocabulary value where available. Values may include:

* `performance-task`
* `simulation`
* `structured-observation`
* `work-product-evaluation`
* `portfolio-assessment`
* `project-assessment`
* `assessor-judgement`
* `supervisor-judgement`
* `written-examination`
* `oral-examination`
* `other`

#### 2.8.4 Form of participation

Where `formOfParticipation` is used, values may include:

* `workplace-based`
* `online`
* `on-site`
* `blended`
* `work-experience`
* `other`

#### 2.8.5 Quality-assurance method and framework

`qualityAssuranceMethod` and `qualityFramework` are intentionally extensible. The issuer SHOULD identify the method/framework precisely and SHOULD include a stable reference where available.

Examples include:

* documented internal QA procedure;
* external assessment scheme;
* professional certification scheme;
* sectoral assessment standard;
* ISO/IEC 17024 where certification of persons is applicable;
* ISO 21001 where an educational organisation's management system is relevant;
* another applicable ISO standard;
* accreditation by a competent accreditation body;
* independent audit against a documented assessment framework;
* another recognised national, sectoral, professional or organisational QA framework.

Merely naming an ISO standard SHALL NOT be interpreted as evidence of certification or accreditation. Where certification, accreditation or audit status is claimed, supporting evidence SHOULD be identifiable.

#### 2.8.6 Legal category

`attestation_legal_category` SHALL be `non-qualified-EAA` for this version of the Rulebook.

### 2.9 Integrity rules

| **Rule ID** | **Rule statement** | **Why it exists** |
|-------------|--------------------|-------------------|
| `VS-IR-01` | `identifier`, `title`, `givenName`, `familyName`, `issuerCountry`, `awardingBody`, `issuanceDate`, `skillOutcome`, `skillProficiencyLevel`, `typeOfAssessment`, `qualityAssuranceMethod`, and `qualityAssuranceLevel` SHALL be present. | Establishes the minimum interoperable Verified Skill claim. |
| `VS-IR-02` | `skillProficiencyLevel` SHALL be one of the five Dreyfus values in Section 2.8.1. | Prevents ambiguous proficiency semantics. |
| `VS-IR-03` | EQF, NQF or other qualification-framework levels SHALL NOT be used as substitutes for `skillProficiencyLevel`. | Keeps skill proficiency distinct from qualification level. |
| `VS-IR-04` | `studyLoadHours`, when present, SHALL be a positive number representing hours. ECTS SHALL NOT be used as its unit. | Keeps workload meaningful outside formal credit systems. |
| `VS-IR-05` | `qualityAssuranceLevel` SHALL be one of the values in Section 2.8.2 and SHALL be accompanied by `qualityAssuranceMethod`. | Ensures QA assurance is explicit and interpretable. |
| `VS-IR-06` | `audited-assessment` SHALL be supported by `auditInformation`, `accreditation`, or equivalent structured evidence identifying the audit/certification/accreditation basis. | Prevents unsupported high-assurance claims. |
| `VS-IR-07` | `third-party-assessed` SHALL identify, directly or through evidence, the third party responsible for the assessment or review. | Makes independent assessment verifiable. |
| `VS-IR-08` | An ISO standard SHALL NOT be represented as an accreditation or certification unless such status actually exists. | Prevents false QA semantics. |
| `VS-IR-09` | Where `escoReference` is present, it SHOULD identify a resolvable ESCO skill or competence concept corresponding to `skillOutcome`. | Supports semantic interoperability. |
| `VS-IR-10` | `issuanceDate` SHALL NOT precede completion of the assessment or other process establishing the skill claim. | Preserves chronology and integrity. |
| `VS-IR-11` | If `grade` is present, `gradingScheme` SHOULD also be present. | Makes results interpretable. |
| `VS-IR-12` | Selective disclosure SHALL allow the Holder to reveal only attributes required for the transaction. | Supports privacy and data minimisation. |
| `VS-IR-13` | ELM mappings SHALL only be claimed where the Verified Skill concept is semantically compatible with the ELM property. Verified-Skill-specific concepts SHALL use extensions rather than overloaded ELM fields. | Prevents false semantic alignment. |

## 3 Attestation encoding

### 3.1 ISO/IEC 18013-5-compliant encoding

This version does not define an ISO/IEC 18013-5 mdoc encoding for the Verified Skill Attestation.

If a future version defines an mdoc representation, that version SHALL define a unique document type, namespaces, attribute identifiers, CBOR encoding rules and illustrative examples.

### 3.2 SD-JWT VC-based encoding

The Verified Skill Attestation SHALL be issued as an SD-JWT VC.

The Verifiable Credential Type (`vct`) is:

```text
VerifiableVerifiedSkill
```

Claims SHALL follow SD-JWT VC and HAIP conventions where applicable.

#### 3.2.1 Standard JWT / SD-JWT VC claims

| Claim | Encoding | Disclosable |
|-------|----------|-------------|
| `iss` | string | MUST NOT |
| `iat` | integer | MUST NOT |
| `nbf` | integer | MUST NOT |
| `exp` | integer | MUST NOT |
| `jti` | string | MUST NOT |
| `cnf` | object | MUST NOT |
| `status` | object | MUST NOT |
| `vct` | string; SHALL be `VerifiableVerifiedSkill` | MUST NOT |

#### 3.2.2 Public or reusable claims

| Claim | Encoding | Disclosable |
|-------|----------|-------------|
| `givenName` | string | MUST |
| `familyName` | string | MUST |
| `dateOfBirth` | ISO 8601 date string | MAY |
| `mail` | string | MAY |

#### 3.2.3 Claims specific to the Verified Skill Attestation

| Claim | Encoding | Disclosable |
|-------|----------|-------------|
| `attestation_legal_category` | string | MUST NOT |
| `identifier` | string | MUST |
| `title` | string | MUST |
| `issuerCountry` | string | MUST |
| `awardingBody` | string | MUST |
| `issuanceDate` | ISO 8601 date | MUST |
| `skillOutcome` | string or array | MUST |
| `escoReference` | array of URI strings | MAY |
| `skillProficiencyLevel` | string | MUST |
| `studyLoadHours` | number | MAY |
| `typeOfAssessment` | string | MUST |
| `assessmentBasis` | string | MAY |
| `assessmentEvidence` | array of objects | MAY |
| `formOfParticipation` | string | MAY |
| `learningActivityType` | string | MAY |
| `languageOfAssessment` | string | MAY |
| `idVerificationMethod` | string | MAY |
| `assessor` | object | MAY |
| `assessmentDate` | string | MAY |
| `grade` | string | MAY |
| `gradingScheme` | string or object | MAY |
| `qualityAssuranceMethod` | object | MUST |
| `qualityAssuranceLevel` | string | MUST |
| `qualityFramework` | object | MAY |
| `accreditation` | object | MAY |
| `auditInformation` | object | MAY |
| `reviewDate` | string | MAY |
| `additionalNote` | string | MAY |
| `trust_anchor` | string | MUST NOT |
| `cryptographically_bound_to` | string | MUST NOT |

#### 3.2.4 Example JWT claim set

```json
{
  "iss": "https://issuer.skills.example.eu",
  "iat": 1781740800,
  "jti": "urn:uuid:4a3f6b2e-1c44-4b8a-9e21-6f0a2d7c5b31",
  "vct": "VerifiableVerifiedSkill",
  "attestation_legal_category": "non-qualified-EAA",
  "identifier": "VS-2026-0007421",
  "title": "Industrial Hydrogen Compressor Operation",
  "givenName": "Elena",
  "familyName": "Kowalska",
  "issuerCountry": "NL",
  "awardingBody": "Example Hydrogen Training Centre",
  "issuanceDate": "2026-06-15",
  "skillOutcome": "Operates an industrial hydrogen compressor safely under normal operating conditions",
  "escoReference": [
    "http://data.europa.eu/esco/skill/example"
  ],
  "skillProficiencyLevel": "competent",
  "studyLoadHours": 80,
  "typeOfAssessment": "structured-observation",
  "assessmentBasis": "Observed operation during three supervised production shifts",
  "formOfParticipation": "workplace-based",
  "idVerificationMethod": "onsite-with-identity-verification",
  "qualityAssuranceLevel": "third-party-assessed",
  "qualityAssuranceMethod": {
    "type": "external-assessment-procedure",
    "name": "Independent Workplace Skills Assessment Scheme"
  },
  "assessor": {
    "name": "Example Independent Skills Assessment Foundation"
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

#### 3.2.5 Example issued SD-JWT

```text
<issuer-signed-sd-jwt>~<disclosure-1>~<disclosure-2>~<disclosure-n>~<holder-binding-jwt>
```

#### 3.2.6 Example human-readable disclosed payload

A Relying Party assessing whether a candidate possesses a required skill may request:

```json
{
  "vct": "VerifiableVerifiedSkill",
  "title": "Industrial Hydrogen Compressor Operation",
  "awardingBody": "Example Hydrogen Training Centre",
  "skillOutcome": "Operates an industrial hydrogen compressor safely under normal operating conditions",
  "skillProficiencyLevel": "competent",
  "typeOfAssessment": "structured-observation",
  "qualityAssuranceLevel": "third-party-assessed"
}
```

The verifier SHOULD request only the minimum claims necessary for the decision.

### 3.3 W3C Verifiable Credentials Data Model-based encoding

This version does not define a W3C VCDM encoding.

The ELM/EDC JSON-LD representation MAY inform a future W3C VCDM encoding, subject to alignment with EUDI Wallet interoperability requirements.

## 4 Attestation usage

The Verified Skill Attestation is intended to verify that a natural person possesses an identified skill or competence at a stated Dreyfus proficiency level and that the claim was established through a described assessment and QA process.

Typical scenarios include:

* recruitment and candidate screening;
* internal mobility and role assignment;
* workplace learning and skills recognition;
* access to further training;
* recognition of non-formal or informal learning;
* skills-based matching between individuals and opportunities;
* cross-border presentation of workplace or non-formal skills.

A Relying Party SHALL verify:

* issuer signature;
* SD-JWT VC type (`vct`);
* issuer authorisation to issue Verified Skill Attestations;
* credential validity period, where present;
* credential status, where present;
* holder binding, where used;
* integrity rules in Section 2.9;
* sufficiency of disclosed attributes.

A Relying Party SHALL distinguish:

1. **technical verification** of the credential;
2. **assurance evaluation** of how the skill was assessed and quality-assured; and
3. **substantive evaluation** of whether the skill and proficiency are sufficient for the Relying Party's purpose.

Successful cryptographic verification SHALL NOT by itself imply acceptance of the skill claim for a particular role or activity.

The Relying Party SHOULD be able to interpret both `skillProficiencyLevel` and `qualityAssuranceLevel`. These dimensions SHALL be evaluated independently.

The Relying Party SHOULD request PID or another accepted identity credential where strong Holder matching is required.

The Relying Party SHALL apply data minimisation.

## 5 Trust anchors

A Relying Party SHALL verify that the issuer is authorised to issue the `VerifiableVerifiedSkill` attestation type.

For non-qualified EAA deployments, trust may be established through one or more of:

* a machine-readable trust list or trust registry used by the relevant EUDI Wallet or sectoral ecosystem;
* issuer metadata;
* a WE BUILD trust-framework entry;
* a pilot trust list;
* a sectoral trust framework;
* another governance mechanism authorised for the deployment.

Issuer authorisation and assessment/QA assurance are distinct.

A valid trust anchor proving that an organisation may issue Verified Skill Attestations does not by itself prove that a particular assessment method is externally audited, accredited or certified. Conversely, QA evidence does not by itself establish EUDI issuer authorisation.

Where the assessing organisation differs from the issuer, the Relying Party MAY evaluate the assessor and QA evidence separately from the issuer trust anchor.

## 6 Revocation and review

A Verified Skill Attestation represents an assessed skill at a given point or period in time. Unlike a formal educational achievement that necessarily remains historically true once awarded, the practical relevance of some skills may diminish due to technological change, non-use, safety requirements, changing procedures, or sector-specific revalidation requirements.

Therefore, this Rulebook distinguishes:

* **revocation** — withdrawal because the credential should no longer be relied on as issued;
* **expiry** — technical end of validity of the credential instance;
* **review/reassessment date** — a domain-specific signal that the skill should be reassessed.

The issuer SHOULD support revocation or suspension where:

* the credential was issued in error;
* the underlying assessment is found invalid or fraudulent;
* the credential was fraudulently obtained;
* the credential is superseded by a corrected version;
* the assessment or QA evidence on which issuance relied is invalidated with relevant retroactive effect.

The issuer MAY include a `reviewDate` where skill currency matters.

A Relying Party SHALL NOT interpret absence of a review date as evidence that a skill can never become outdated. Skill currency is a relying-party/domain decision unless a governing framework states otherwise.

## 7 Compliance

This Rulebook is designed to align with the EUDI Wallet architectural approach for Electronic Attestations of Attributes and the Attestation Rulebook structure defined by the ARF.

It:

* defines a non-qualified EAA for Verified Skills;
* defines mandatory, optional and conditional attributes;
* defines a Dreyfus-based proficiency model instead of EQF;
* uses workload in hours through the ELM-compatible `volumeOfLearning` concept rather than ECTS;
* defines three independent QA assurance levels;
* allows documented internal QA, external assessment, audit, certification and accreditation mechanisms;
* preserves ELM interoperability where semantically appropriate;
* defines explicit extensions where ELM has no suitable property;
* supports ESCO references;
* defines an SD-JWT VC `vct`;
* supports selective disclosure and data minimisation;
* distinguishes issuer trust, assessment assurance and substantive skill acceptance;
* defines revocation, expiry and reassessment expectations.

This Rulebook SHALL NOT use:

* EQF or NQF level as a proxy for Dreyfus skill proficiency;
* ECTS as the unit for `studyLoadHours`;
* ESG as a mandatory QA basis for non-formal/workplace Verified Skills;
* the ELM `educationLevel` property as a substitute for Dreyfus proficiency;
* an ELM Accreditation object to represent a QA process that is not actually an accreditation.

## 8 References

| **Item Reference** | **Standard name/details** |
|--------------------|---------------------------|
| [Dreyfus Model] | Dreyfus, S.E. and Dreyfus, H.L., five-stage model of skill acquisition: novice, advanced beginner, competent, proficient, expert. |
| [ELM] | European Learning Model, European Commission / Europass. |
| [ELM Micro-credential Mapping] | European Commission / Europass mapping of the standard elements of micro-credentials to ELM/EDC. Used in this Rulebook to verify reusable ELM paths, not to import formal-education-specific semantics. |
| [ESCO] | European Skills, Competences, Qualifications and Occupations classification. |
| [European Digital Identity Regulation] | Regulation (EU) 2024/1183 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework. |
| [ISO/IEC 17024] | ISO/IEC 17024, Conformity assessment — General requirements for bodies operating certification of persons. |
| [ISO 21001] | ISO 21001, Educational organizations — Management systems for educational organizations. |
| [HAIP] | OpenID4VC High Assurance Interoperability Profile, OpenID Foundation. |
| [RFC 2119] | Key words for use in RFCs to Indicate Requirement Levels. |
| [SD-JWT VC] | SD-JWT-based Verifiable Credentials. |
| [ARF Topic 12] | EUDI Wallet ARF topic governing Attestation Rulebooks. |
| [W3C VCDM v2.0] | W3C Verifiable Credentials Data Model v2.0. |

---

## Annex A — ELM mapping decisions for Verified Skills

This annex is informative but records the semantic mapping decisions used by this Rulebook.

| Verified Skill concept | ELM treatment | Decision |
|------------------------|---------------|----------|
| Skill / competence description | `LearningOutcome` can represent knowledge/skill/competence concepts and link to ESCO | Reuse ELM |
| ESCO skill reference | `LearningOutcome.relatedESCOSkill` | Reuse ELM; prefer URI/reference semantics |
| Study load in hours | `LearningAchievementSpecification.volumeOfLearning` | Reuse ELM |
| Assessment type | `LearningAssessmentSpecification.dcType` through `specifiedBy.provenBy[]` | Reuse ELM |
| Identity verification during assessment | `provenBy[].idVerification` | Reuse ELM |
| Form/mode of participation | `influencedBy[].mode` where there is a learning activity | Reuse conditionally |
| Dreyfus proficiency | No verified native ELM property with the same semantics | Verified Skill extension |
| QA level: self-asserted / third-party / audited | No native ELM three-level assurance scale | Verified Skill extension |
| Actual accreditation | `credential.evidence[].accreditation` | Reuse only when an actual accreditation exists |
| General QA procedure or ISO-inspired internal process | Not automatically an ELM Accreditation | Verified Skill extension, optionally linked to a framework URI |
| EQF / NQF | Qualification/education level semantics | Do not use for Verified Skill proficiency |
| ECTS | Formal credit framework | Do not use for Verified Skill study load |

### Annex A.1 Important semantic distinction

The three main confidence dimensions in a Verified Skill Attestation are independent:

1. **What skill is claimed?** — `skillOutcome`, preferably linked to ESCO.
2. **How proficient is the Holder?** — `skillProficiencyLevel` using Dreyfus.
3. **How much assurance exists around the assessment?** — `qualityAssuranceLevel` plus `qualityAssuranceMethod`.

Implementations SHALL NOT collapse these dimensions into one score or level.
