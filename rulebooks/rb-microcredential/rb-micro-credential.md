(Template version: 1.1)

# WE BUILD Attestation Rulebook for attestations of type *Micro-credential*

*[Based on the WE BUILD Attestation Rulebook Template and the WE BUILD BU5 Micro-credentials Attestation Design.]*

* Author(s):
    * Stefan Liström, Sunet
* Previous Authors
    * N/A

| Version | Date | Description |
|---------|------|-------------|
| 0.1 | 2026-07-21 | Initial draft rulebook for the Micro-credential Attestation |

**Feedback:**

* Github, portal, email, Slack

## 1 Introduction

### 1.1 Document scope and purpose

This Rulebook defines the *Micro-credential Attestation* for use in the European Digital Identity Wallet ecosystem.

The Micro-credential Attestation expresses the real-world fact that a natural person has successfully completed a small, coherent volume of formally assessed learning, delivered under the quality assurance of an educational organisation, and has thereby acquired specific learning outcomes. It follows the definition set out in the Council Recommendation of 16 June 2022 on a European approach to micro-credentials for lifelong learning and employability (2022/C 243/02): a portable, learner-owned record of assessed learning outcomes from a small volume of study, which can be aligned to a curriculum, carries a notional workload, and is issued under institutional quality assurance.

The attestation is intended to be issued by an authentic source acting as a formal education provider, such as a higher education institution (HEI) or vocational education and training (VET) provider, or by an authorised academic identity provider acting on that provider's behalf. The Holder is the natural person who completed the assessed learning. Relying Parties are expected to include universities and other HEIs evaluating admission, credit recognition, or advanced standing; employers assessing skills for recruitment or onboarding; and other organisations that need to rely on verified evidence of formally taught knowledge, skills, and competences.

In practical terms, the attestation enables a learner to present proof of one or more completed micro-credentials through an EUDI Wallet, for example to demonstrate fulfilment of entry requirements or eligibility for recognition of credits when applying to a course or programme in another country. This supports cross-border and domestic academic mobility, provided that the relying party can verify the issuer, credential signature, validity, status where applicable, and the disclosed attributes needed for its decision.

The attestation supports use cases including university admission and enrolment, recognition of prior learning and credit transfer, professional onboarding, and other formally taught knowledge-dependent procedures, in both domestic and cross-border contexts.

### 1.2 Document structure

This Rulebook is structured as follows:

* Chapter 2 describes the attestation attributes and metadata in an encoding-independent manner.
* Chapter 3 specifies how the attestation attributes and metadata are encoded using SD-JWT VC. ISO/IEC 18013-5 and W3C VCDM encodings are not defined in this version of the Rulebook.
* Chapter 4 specifies attestation usage, including presentation and verification expectations.
* Chapter 5 defines how trust anchors for attestation verification can be obtained.
* Chapter 6 defines revocation and expiry mechanisms.
* Chapter 7 provides compliance information.
* Chapter 8 lists references.

### 1.3 Key words

This document uses the capitalised key words 'SHALL', 'SHOULD' and 'MAY' as specified in [RFC 2119], i.e., to indicate requirements, recommendations and options specified in this document.

In addition, 'must' (non-capitalised) is used to indicate an external constraint, i.e., a requirement that is not mandated by this document, but, for instance, by an external document. The word 'can' indicates a capability, whereas other words, such as 'will', and 'is' or 'are' are intended as statements of fact.

### 1.4 Terminology

This document uses the terminology specified in Annex 1 of the ARF.

In addition, the following domain-specific terms are used:

| Term | Meaning |
|------|---------|
| Micro-credential Attestation | A Verifiable Credential representing a person's completion of a small, coherent volume of formally assessed learning and the associated learning outcomes. |
| Learner | The natural person to whom the completed learning outcomes apply; the Holder of the attestation. |
| Formal education provider | A higher education institution (HEI), vocational education and training (VET) provider, or other organisation providing formally taught learning under institutional quality assurance. |
| Authorised academic identity provider | A system or organisation authorised by a formal education provider to issue or manage micro-credential attestations on its behalf. |
| Learning outcome | What a learner knows, understands, and is able to do on completion of a learning process, as assessed against transparent criteria. |
| ECTS | European Credit Transfer and Accumulation System, used to express notional workload of learning. |
| EQF | European Qualifications Framework, used to express the level of a qualification or learning outcome. |
| ESCO | European Skills, Competences, Qualifications and Occupations classification. |
| ELM | European Learning Model, a multilingual data model for representing learning opportunities, qualifications, and credentials. |
| Relying Party | An organisation or system that verifies the Micro-credential Attestation to make an admission, credit-recognition, recruitment, or other eligibility decision. |

## 2 Attestation attributes and metadata

### Chapter overview and requirements

This chapter defines the attributes and metadata that a Micro-credential Attestation may contain. The attributes are defined in an encoding-independent manner. Each attribute is classified as mandatory, optional, or conditional.

The Micro-credential Attestation records a completed, formally assessed learning achievement. Unlike affiliation-based attestations, the underlying fact it attests does not lapse over time; any validity period defined in this Rulebook concerns the technical validity of the credential instance, not the continued truth of the achievement. The attribute set reflects the standard elements for describing micro-credentials set out in the Council Recommendation of 16 June 2022 (2022/C 243/02), as further specified by the European Learning Model (ELM) and the European Digital Credentials for Learning (EDC) application profile, and supports data minimisation by allowing a Holder to disclose only the attributes required for a specific transaction.

### 2.1 Introduction

The Micro-credential Attestation is defined as a non-qualified Electronic Attestation of Attributes unless a future version of this Rulebook explicitly defines a qualified or public-sector legal category.

The attribute `attestation_legal_category` SHALL be included and SHALL have the value `non-qualified-EAA`.

The attestation model consists of the following logical groups:

* credential identification attributes;
* issuer and awarding body attributes;
* learner identity attributes for holder matching;
* learning achievement attributes (outcomes, level, workload, assessment, participation);
* classification and taxonomy references;
* quality assurance and accreditation attributes;
* credential metadata.

Note that, consistent with the European Learning Model, the organisation that seals/issues the credential (see `issuerCountry`) and the organisation that awarded the underlying learning achievement (see `awardingBody`) may or may not be the same organisation; one organisation may seal credentials on behalf of another.

The attestation is issued as a Verifiable Credential compatible with the EUDI Wallet using SD-JWT VC. The model aligns with the following issuer metadata parameters:

* `scope`: `MicroCredential`;
* `format`: `vc+sd-jwt`;
* `vct`: `VerifiableMicroCredential`;
* `claims`: the claims defined in this Rulebook;
* `proof_types_supported`: issuer-defined, including `jwt` where supported;
* `cryptographic_binding_methods_supported`: issuer-defined, for example `jwk` or `cose_key`.

### 2.2 Mandatory attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---------------------|------------------------|----------------|---------------|-------------------|
| `attestation_legal_category` | ARF Topic 12 / Rulebook legal category indication | Indicates the legal category of the attestation. | string | `non-qualified-EAA` |
| `identifier` | ELM `credential.identifier` | Unique identifier of the micro-credential instance, assigned by the awarding body. | string | `MC-2026-0007421` |
| `title` | ELM `credential.displayParameter.title` / Council Recommendation standard element 2 | Title of the micro-credential. | string | `Introduction to Applied Data Ethics` |
| `givenName` | ELM `credential.credentialSubject.givenName` / Council Recommendation standard element 1 | Learner given name. | string | `Elena` |
| `familyName` | ELM `credential.credentialSubject.familyName` / Council Recommendation standard element 1 | Learner family name. | string | `Kowalska` |
| `issuerCountry` | ELM `credential.issuer.location.address.countryCode.prefLabel` / Council Recommendation standard element 3 | Country or region of the organisation that sealed/issued the credential. May differ from the awarding body's country. | string (ISO 3166-1 alpha-2) | `SE` |
| `awardingBody` | ELM `credential.credentialSubject.hasClaim[0].awardedBy.awardingBody[0].legalName` / Council Recommendation standard element 4 | Name of the formal education provider that awarded the micro-credential. | string | `Linköping University` |
| `issuanceDate` | ELM `credential.issued` / Council Recommendation standard element 5 | Date on which the credential was sealed and issued. Distinct from any validity start date. | date | `2026-06-15` |
| `learningOutcomes` | ELM `credential.credentialSubject.hasClaim[0].specifiedBy.learningOutcome` / Council Recommendation standard element 7 | Description of the learning outcomes acquired by the learner. | array of strings | `["Applies core ethical frameworks to data-driven decision making", "Evaluates bias and fairness risks in a dataset"]` |
| `notionalWorkload` | ELM `credential.credentialSubject.hasClaim[0].specifiedBy.creditPoint[0].point` or `volumeOfLearning` / Council Recommendation standard element 8 | Notional workload needed to complete the learning activity, expressed as a value and a unit. | object | `{ "value": 3, "unit": "ECTS" }` |
| `typeOfAssessment` | ELM `credential.credentialSubject.hasClaim[0].specifiedBy.provenBy[0].dcType` / Council Recommendation standard element 9 | Type of assessment used to validate the learning outcomes. | string | `written-examination` |
| `formOfParticipation` | ELM `credential.credentialSubject.hasClaim[0].specifiedBy.influencedBy[0].mode` / Council Recommendation standard element 10 | Form of participation in the learning activity. | string | `online` |
| `qualityAssurance` | ELM Accreditation `dcType` / Council Recommendation standard element 11 | Type of quality assurance used to underpin the micro-credential. | string | `institutional-accreditation` |

### 2.3 Optional attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---------------------|------------------------|----------------|---------------|-------------------|
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

### 2.4 Conditional attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---------------------|------------------------|----------------|---------------|-------------------|
| `dateOfBirth` | ELM `credential.credentialSubject.dateOfBirth` | SHALL be included only where needed for holder matching, or another justified relying-party purpose. If included, it SHALL represent the subject's birth date and SHALL NOT be in the future. | date | `1998-11-02` |
| `level` | ELM `eqfLevel` | SHALL be included where the learning experience leading to the micro-credential can be positioned within the EQF or an applicable national or sectoral level framework; MAY be omitted where no such framework applies. | string | `EQF-6` |
| `grade` | ELM `provenBy[0].grade` | SHALL be included where `typeOfAssessment` produces a grade or result, and SHALL be omitted where the assessment is pass/fail-only without a graded outcome. Where `grade` is present, `gradingScheme` SHOULD also be included. | string | `Pass` |
| `escoReference` | ELM `relatedESCOSkill` | SHOULD be included where the attested learning outcomes can be mapped to one or more ESCO skills or competences. | array of strings | `["http://data.europa.eu/esco/skill/abc12345"]` |
| `stackable` | ELM `hasPart` / `isPartOf` | SHOULD be included where the awarding body has defined a stacking pathway for this micro-credential towards a larger qualification. | boolean | `true` |
| `partOfQualification` | ELM `isPartOf` | SHOULD be included where `stackable` is `true`. | string | `BSc Data Science, Linköping University` |

### 2.5 Mandatory metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---------------------|------------------------|----------------|---------------|-------------------|
| `vct` | SD-JWT VC | Verifiable Credential Type identifying this attestation type. | string | `VerifiableMicroCredential` |
| `iss` | SD-JWT VC / JWT | Identifier of the issuer of the credential. | string | `https://issuer.example-university.edu` |
| `iat` | JWT | Time at which the credential was issued. | integer | `1781740800` |
| `cnf` | SD-JWT VC / JOSE | Confirmation claim binding the credential to key material controlled by the Holder or Wallet Unit, where holder binding is used. | object | `{ "jwk": { ... } }` |

### 2.6 Optional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---------------------|------------------------|----------------|---------------|-------------------|
| `exp` | JWT | Expiration time of the credential instance. Where present, this reflects the technical validity of the credential instance rather than the continued truth of the underlying achievement. | integer | `1970361600` |
| `nbf` | JWT | Time before which the credential MUST NOT be accepted. | integer | `1781740800` |
| `jti` | JWT | Unique identifier of the credential instance. | string | `urn:uuid:9a3f6b2e-1c44-4b8a-9e21-6f0a2d7c5b31` |
| `status` | SD-JWT VC status mechanism, where used | Status information enabling revocation or correction checks. | object | `{ "status_list": { ... } }` |
| `trust_anchor` | ARF Topic 12 | Location or identifier of the machine-readable trust anchor or trust framework entry used to verify issuer authorisation. | string | `https://trust.example.eu/education/institutions/example-university` |
| `cryptographically_bound_to` | ARF Topic 12 / ARB_28 | Identifier of another attestation type to which this attestation is cryptographically bound, where such binding is used. | string | `urn:eudi:pid:1` |

### 2.7 Conditional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---------------------|------------------------|----------------|---------------|-------------------|
| `status` | SD-JWT VC status mechanism, where used | SHOULD be present where the awarding body needs the ability to revoke or correct a Micro-credential Attestation after issuance, for example due to an issuance error or academic integrity finding. | object | `{ "status_list": { ... } }` |
| `cryptographically_bound_to` | ARF Topic 12 / ARB_28 | SHOULD be present where the Micro-credential Attestation must be presented together with PID or another identity attestation for strong holder matching. | string | `urn:eudi:pid:1` |

### 2.8 Code lists

| **Field name** | **Allowed values** | **Meaning** | **Source / vocabulary** | **Notes / extensibility** |
|----------------|--------------------|-------------|--------------------------|---------------------------|
| `level` | `EQF-1` through `EQF-8` | Level of the learning outcomes against the EQF. | European Qualifications Framework (EQF) controlled vocabulary | Where a national or sectoral framework is used instead, use `nationalQualificationsFrameworkLevel` and/or `educationLevelDescriptor`. |
| `educationLevelDescriptor` | `beginner`, `intermediate`, `advanced`, issuer-defined | Framework-independent level descriptor. | Issuer-defined, informed by ELM | — |
| `notionalWorkload.unit` | `ECTS`, `hours` | Unit in which the notional workload is expressed. | ECTS (EQF Recommendation Annex V) / issuer-defined | HEIs SHOULD use ECTS where possible; other providers MAY use hours or another documented unit. |
| `typeOfAssessment` | `written-examination`, `oral-examination`, `practical-assessment`, `portfolio-assessment`, `peer-assessment`, `project-assessment`, issuer-defined | Type of assessment used to validate learning outcomes. | EU "Assessment type" multilingual controlled vocabulary, or issuer-defined | Issuers SHOULD reuse an existing value before introducing a new one. |
| `formOfParticipation` | `online`, `on-site`, `blended` | Mode in which the learner participated in the learning activity. | EU "Mode of learning and assessment" multilingual controlled vocabulary, or issuer-defined | — |
| `learningActivityType` | `classroom-coursework`, `e-learning`, `internship`, `volunteering`, issuer-defined | Category of learning activity. | EU "Learning activity type" multilingual controlled vocabulary, or issuer-defined | — |
| `idVerificationMethod` | `proctored-online-exam`, `in-person-supervision`, `identity-verified-remote-exam`, issuer-defined | Method used to supervise assessment and verify learner identity. | EU "Method of supervision and verification" multilingual controlled vocabulary, or issuer-defined | — |
| `qualityAssurance` / `accreditation.type` | `institutional-accreditation`, `programme-accreditation`, `national-quality-agency`, `sectoral-quality-assurance`, issuer-defined | Type of quality assurance underpinning the micro-credential. | Issuer-defined, informed by ELM Accreditation class and DEQAR | — |
| `fieldOfEducation` | ISCED-F 2013 codes | Field of education or training. | ISCED-F 2013 | — |
| `attestation_legal_category` | `non-qualified-EAA`, `QEAA`, `PuB-EAA` | Indicates the legal category of the attestation. | ARF Topic 12 / Rulebook template | This Rulebook uses `non-qualified-EAA`. |

### 2.9 Integrity rules

| **Rule ID** | **Rule statement** | **Why it exists** | **Where enforced** | **Verifier / issuer behavior on failure** |
|-------------|--------------------|-------------------|--------------------|-------------------------------------------|
| `MC-IR-01` | `identifier`, `title`, `givenName`, `familyName`, `issuerCountry`, `awardingBody`, `issuanceDate`, `learningOutcomes`, `notionalWorkload`, `typeOfAssessment`, `formOfParticipation`, and `qualityAssurance` SHALL be present. | Ensures the credential contains all standard elements required by the Council Recommendation on micro-credentials. | Issuer business rules, schema validation, verifier business validation. | Issuer SHALL reject incomplete credential data. Verifier SHALL treat the attestation as invalid or insufficient if mandatory claims are missing. |
| `MC-IR-02` | If `dateOfBirth` is included, it SHALL represent the subject's birth date and SHALL NOT be in the future. | Prevents invalid identity data and supports correct holder-matching checks. | Issuer business rules and verifier business validation. | Issuer SHALL reject invalid dates. Verifier SHALL reject or ignore an invalid `dateOfBirth` claim depending on the transaction. |
| `MC-IR-03` | `issuanceDate` SHALL NOT be in the future and SHALL NOT precede the completion of the assessment underlying the micro-credential. | Ensures the awarded date reflects a genuinely completed and assessed learning activity. | Issuer business rules. | Issuer SHALL reject issuance where this cannot be confirmed. |
| `MC-IR-04` | If `grade` is present, `typeOfAssessment` SHALL indicate an assessment type capable of producing a graded outcome, and `gradingScheme` SHOULD also be present. | Prevents inconsistent or uninterpretable grading information. | Issuer business rules and verifier business validation. | Issuer SHALL NOT include `grade` inconsistent with the assessment type. Verifier MAY disregard an inconsistent or unexplained `grade` claim. |
| `MC-IR-05` | If `escoReference` values are included, each SHALL resolve to a valid ESCO skill or competence URI. | Ensures semantic interoperability of skill references. | Issuer business rules and schema validation. | Issuer SHOULD validate references before issuance. Verifier MAY ignore unresolvable references. |
| `MC-IR-06` | `notionalWorkload.value` SHALL be a positive number, and `notionalWorkload.unit` SHALL be a value from the code list in Section 2.8. | Ensures workload information is meaningful and consistently interpretable. | Issuer business rules and schema validation. | Issuer SHALL reject non-conformant workload values. Verifier MAY treat non-conformant values as unusable for its purpose. |
| `MC-IR-07` | If `stackable` is `true`, `partOfQualification` SHOULD be present. | Ensures a stated stacking intent is backed by an identifiable target qualification. | Issuer business rules. | Issuer SHOULD include the target qualification. Verifier MAY treat an unsupported stackability claim with reduced confidence. |
| `MC-IR-08` | If `accreditation` is present, its `type` value SHALL be consistent with the top-level `qualityAssurance` value. | Prevents contradictory quality-assurance information within a single credential. | Issuer business rules and schema validation. | Issuer SHALL ensure consistency before issuance. Verifier MAY disregard an internally inconsistent `accreditation` claim. |
| `MC-IR-09` | Selective disclosure SHALL allow the Holder to reveal only the attributes required for the transaction. | Supports privacy and data minimisation. | Issuer credential construction and Wallet presentation logic. | Verifier SHALL request only necessary claims. Wallet SHOULD allow the Holder to review the disclosed claims. |

# 3 Attestation encoding

## 3.1 ISO/IEC 18013-5-compliant encoding

This version of the Rulebook does not define an ISO/IEC 18013-5 mdoc encoding for the Micro-credential Attestation.

The Micro-credential Attestation defined in this Rulebook is specified for SD-JWT VC-based issuance and presentation. If a future version of this Rulebook defines an ISO/IEC 18013-5-compliant mdoc representation, that version SHALL define a unique document type, namespaces, attribute identifiers, CBOR encoding rules, and illustrative mdoc examples.

## 3.2 SD-JWT VC-based encoding

The Micro-credential Attestation SHALL be issued as an SD-JWT VC.

The Verifiable Credential Type (`vct`) for this attestation type is:

```text
VerifiableMicroCredential
```

The credential claims defined in this section SHALL follow SD-JWT VC and HAIP conventions where applicable. Claim names are either IANA-registered JWT claims, public or reusable names, or private names specific to this attestation type.

For all claims, this Rulebook specifies whether an Attestation Provider MUST, MAY, or MUST NOT make the claim selectively disclosable.

### 3.2.1 IANA-registered and standard JWT / SD-JWT VC claims

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Reference/Notes** | **Disclosable** |
|---------------------|--------------------------|---------------------|---------------------|-----------------|
| `iss` | `iss` | string | JWT issuer identifier. | MUST NOT |
| `iat` | `iat` | integer | Issued-at timestamp. | MUST NOT |
| `nbf` | `nbf` | integer | Not-before timestamp, where used. | MUST NOT |
| `exp` | `exp` | integer | Expiration timestamp, where used. Reflects technical validity of the credential instance only. | MUST NOT |
| `jti` | `jti` | string | Unique credential instance identifier, where used. | MUST NOT |
| `cnf` | `cnf` | object | Holder binding confirmation claim, where used. | MUST NOT |
| `status` | `status` | object | Status or revocation information, where used. | MUST NOT |
| `vct` | `vct` | string | SD-JWT VC type. Value SHALL be `VerifiableMicroCredential`. | MUST NOT |

### 3.2.2 Public or reusable claims

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Reference/Notes** | **Disclosable** |
|---------------------|--------------------------|---------------------|---------------------|-----------------|
| `givenName` | `givenName` | string | Learner given name. ELM Person class property. | MUST |
| `familyName` | `familyName` | string | Learner family name. ELM Person class property. | MUST |
| `dateOfBirth` | `dateOfBirth` | string | Date of birth formatted as ISO 8601 date, where disclosed. | MAY |
| `mail` | `mail` | string | Email address, where disclosed. | MAY |

### 3.2.3 Private claims specific to the Micro-credential Attestation

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Notes** | **Disclosable** |
|---------------------|--------------------------|---------------------|-----------|-----------------|
| `attestation_legal_category` | `attestation_legal_category` | string | SHALL be `non-qualified-EAA`. | MUST NOT |
| `identifier` | `identifier` | string | Unique identifier of the micro-credential instance. | MUST |
| `title` | `title` | string | Title of the micro-credential. | MUST |
| `issuerCountry` | `issuerCountry` | string | Country/region of the organisation that sealed/issued the credential. | MUST |
| `awardingBody` | `awardingBody` | string | Name of the formal education provider that awarded the micro-credential. | MUST |
| `awardingBodyAddress` | `awardingBodyAddress` | string | Registered or contact address of the awarding body, where disclosed. | MAY |
| `awardingBodyHomepage` | `awardingBodyHomepage` | string | Homepage URL of the awarding body, where disclosed. | MAY |
| `awardingBodyIdentifier` | `awardingBodyIdentifier` | string | Additional identifier(s) of the awarding body, where disclosed. | MAY |
| `issuanceDate` | `issuanceDate` | string | Date on which the credential was sealed and issued, formatted as ISO 8601 date. | MUST |
| `level` | `level` | string | Level of the learning outcomes against the EQF or an applicable framework, where applicable. | MAY |
| `nationalQualificationsFrameworkLevel` | `nationalQualificationsFrameworkLevel` | string | Level against a national or regional qualifications framework, where disclosed. | MAY |
| `educationLevelDescriptor` | `educationLevelDescriptor` | string | Framework-independent level descriptor, where disclosed. | MAY |
| `learningOutcomes` | `learningOutcomes` | array of strings | Description of the learning outcomes acquired by the learner. | MUST |
| `learningOutcomeSummary` | `learningOutcomeSummary` | string | Free-text summary of the learning outcomes, where disclosed. | MAY |
| `fieldOfEducation` | `fieldOfEducation` | string | ISCED-F 2013 field of education code, where disclosed. | MAY |
| `escoReference` | `escoReference` | array of strings | ESCO skill/competence references, where disclosed. | MAY |
| `notionalWorkload` | `notionalWorkload` | object | Notional workload, expressed as `{ "value": ..., "unit": ... }`. | MUST |
| `typeOfAssessment` | `typeOfAssessment` | string | Type of assessment used to validate the learning outcomes. | MUST |
| `formOfParticipation` | `formOfParticipation` | string | Form of participation in the learning activity. | MUST |
| `learningActivityType` | `learningActivityType` | string | Category of the learning activity, where disclosed. | MAY |
| `languageOfAssessment` | `languageOfAssessment` | string | Language of assessment, where disclosed. | MAY |
| `idVerificationMethod` | `idVerificationMethod` | string | Supervision/identity-verification method used, where disclosed. | MAY |
| `grade` | `grade` | string | Grade or result obtained, where the assessment produces one. | MAY |
| `gradingScheme` | `gradingScheme` | string | Description of the grading scheme, where disclosed. | MAY |
| `entryRequirements` | `entryRequirements` | array of strings | Prerequisites needed to enrol, where disclosed. | MAY |
| `qualityAssurance` | `qualityAssurance` | string | Type of quality assurance underpinning the micro-credential. | MUST |
| `stackable` | `stackable` | boolean | Whether the micro-credential is designed to stack towards a larger qualification, where disclosed. | MAY |
| `partOfQualification` | `partOfQualification` | string | Identifier or title of the larger qualification, where disclosed. | MAY |
| `accreditation` | `accreditation` | object | Structured accreditation details underpinning `qualityAssurance`, where disclosed. | MAY |
| `additionalNote` | `additionalNote` | string | Free-text supplementary information, where disclosed. | MAY |
| `placeOfBirth` | `placeOfBirth` | string | Learner place of birth, where disclosed. | MAY |
| `citizenshipCountry` | `citizenshipCountry` | string | Learner country of citizenship, where disclosed. | MAY |
| `nationalID` | `nationalID` | string | National or government identifier of the learner, where disclosed. | MAY |
| `registeredAddress` | `registeredAddress` | string | Learner registered/contact address, where disclosed. | MAY |
| `trust_anchor` | `trust_anchor` | string | Location or identifier of the trust anchor or trust framework entry, where used. | MUST NOT |
| `cryptographically_bound_to` | `cryptographically_bound_to` | string | Identifier of another attestation type to which this attestation is bound, where used. | MUST NOT |

### 3.2.4 Example JWT claim set

```json
{
  "iss": "https://issuer.example-university.edu",
  "iat": 1781740800,
  "nbf": 1781740800,
  "jti": "urn:uuid:9a3f6b2e-1c44-4b8a-9e21-6f0a2d7c5b31",
  "vct": "VerifiableMicroCredential",
  "attestation_legal_category": "non-qualified-EAA",
  "identifier": "MC-2026-0007421",
  "title": "Introduction to Applied Data Ethics",
  "givenName": "Elena",
  "familyName": "Kowalska",
  "issuerCountry": "SE",
  "awardingBody": "Linköping University",
  "awardingBodyHomepage": "https://liu.se",
  "issuanceDate": "2026-06-15",
  "level": "EQF-6",
  "learningOutcomes": [
    "Applies core ethical frameworks to data-driven decision making",
    "Evaluates bias and fairness risks in a dataset"
  ],
  "fieldOfEducation": "0613",
  "escoReference": [
    "http://data.europa.eu/esco/skill/abc12345"
  ],
  "notionalWorkload": {
    "value": 3,
    "unit": "ECTS"
  },
  "typeOfAssessment": "written-examination",
  "formOfParticipation": "online",
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
  "trust_anchor": "https://trust.example.eu/education/institutions/example-university",
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

### 3.2.5 Example issued SD-JWT

The following is a non-normative placeholder example. A production SD-JWT SHALL be generated by the issuer using the applicable signing algorithm, disclosure construction, holder binding, and SD-JWT VC rules.

```text
<issuer-signed-sd-jwt>~<disclosure-1>~<disclosure-2>~<disclosure-n>~<holder-binding-jwt>
```

### 3.2.6 Example human-readable disclosed payload

A university admissions office requesting evidence of a completed prerequisite micro-credential for course entry may receive a presentation disclosing the following claims:

```json
{
  "vct": "VerifiableMicroCredential",
  "identifier": "MC-2026-0007421",
  "title": "Introduction to Applied Data Ethics",
  "givenName": "Elena",
  "familyName": "Kowalska",
  "issuerCountry": "SE",
  "awardingBody": "Linköping University",
  "level": "EQF-6",
  "learningOutcomes": [
    "Applies core ethical frameworks to data-driven decision making",
    "Evaluates bias and fairness risks in a dataset"
  ],
  "notionalWorkload": {
    "value": 3,
    "unit": "ECTS"
  },
  "typeOfAssessment": "written-examination",
  "grade": "Pass"
}
```

A verifier that only needs to confirm completion of the micro-credential SHOULD request the minimum claims necessary for that decision and SHOULD NOT request `dateOfBirth`, `mail`, `nationalID`, `placeOfBirth`, `citizenshipCountry`, or `registeredAddress` unless required for the transaction, for example strong holder matching.

The issuer identity, credential type, expiry time, signature, holder binding proof, and trust anchor information are not treated as selectively disclosable attributes and SHALL remain available to the verifier for technical validation.

## 3.3 W3C Verifiable Credentials Data Model-based encoding

This version of the Rulebook does not define a W3C Verifiable Credentials Data Model encoding for the Micro-credential Attestation.

If a future version defines a W3C VCDM representation, that version SHALL define the credential context, type, credential subject structure, proof type, selective disclosure mechanism, and presentation requirements. Note that the European Learning Model's own JSON-LD-based encoding (as used by the European Digital Credentials for Learning infrastructure) is a W3C VCDM-compatible representation and MAY inform such a future encoding, subject to alignment with the EUDI Wallet's SD-JWT VC-based interoperability requirements.

## 4 Attestation usage

The Micro-credential Attestation is intended for verifying that a natural person has completed a specific, formally assessed learning achievement and the associated learning outcomes.

Typical usage scenarios include:

* presentation by a learner to a university or other higher education institution to demonstrate fulfilment of entry requirements or eligibility for recognition of credits when applying for a course or programme;
* presentation for professional onboarding or recruitment where formally taught knowledge, skills, or competences are relevant to the role;
* presentation for recognition of prior learning or credit transfer between formal education providers;
* presentation in both domestic and cross-border contexts, subject to semantic interpretation, policy alignment, and recognition practices that may vary across sectors and jurisdictions.

Usage covers both:

* online verification by a service provider using remote presentation protocols;
* offline or low-connectivity verification where the verifier can validate the credential signature, issuer, validity period, status where available, and disclosed attributes without relying on a real-time issuer backend.

A Relying Party receiving the attestation SHALL verify:

* the issuer signature;
* the SD-JWT VC type (`vct`);
* the issuer authorisation to issue Micro-credential Attestations;
* the credential validity period, where present;
* the credential status, where a status mechanism is present;
* holder binding, where used;
* the integrity rules defined in Section 2.9;
* that the disclosed attributes are sufficient for the relying-party decision.

The Relying Party SHALL distinguish between verification of the attestation and evaluation of whether the attested learning outcomes are sufficient for its purpose. Successful cryptographic or technical verification alone SHALL NOT be treated as sufficient proof that the attested learning outcomes meet the Relying Party's acceptance criteria; the Relying Party SHALL evaluate the attested skill claim against its own defined criteria relevant to the intended use context, for example admission requirements or credit recognition rules.

The Relying Party SHOULD be able to interpret:

* any assurance or quality level associated with the attestation, where such levels are defined by a future version of this Rulebook;
* recognised taxonomy or classification references, such as ESCO or ISCED-F references, where included in the attestation.

The Relying Party SHOULD request and verify a PID or another accepted identity credential where the transaction requires strong identity matching between the Holder and the attestation subject. For low-risk checks, the Relying Party MAY rely on the Micro-credential Attestation alone, provided that the issuer, signature, validity, status, and holder binding checks are successful and this is consistent with the relying party's policy.

The Relying Party SHALL apply data minimisation and SHALL request only the attributes required for the transaction. For example, a credit-recognition decision may only need `title`, `awardingBody`, `level`, `learningOutcomes`, and `notionalWorkload`, while an identity-sensitive enrolment process may additionally require `givenName`, `familyName`, and strong holder-binding verification via a PID.

The Relying Party SHOULD be able to evaluate the Micro-credential Attestation together with other supporting attestations where combined evidence is required, for example where several micro-credentials are presented to demonstrate cumulative fulfilment of entry requirements.

The Relying Party SHOULD define fallback handling for cases in which the attestation cannot be accepted, including rejection, request for additional evidence, deferred decision, or referral to an alternative process.

The attestation SHOULD be device-bound through holder binding where supported by the EUDI Wallet and the applicable SD-JWT VC profile. The attestation MAY be cryptographically bound to a PID or another accepted identity attestation where strong identity matching is required. Where this binding is used, the metadata attribute `cryptographically_bound_to` SHOULD contain:

```text
urn:eudi:pid:1
```

No payment-specific transactional data is defined by this Rulebook. If the Micro-credential Attestation is used as part of a transaction that also involves payment, for example a paid enrolment or examination fee, payment-related requirements SHALL be defined in a separate payment attestation, payment profile, or transaction-specific rulebook; see [Topic 20] of Annex 2 of the ARF.

## 5 Trust anchors

A Relying Party SHALL verify that the issuer of the Micro-credential Attestation is authorised to issue this attestation type.

For non-qualified EAA deployments, the Relying Party SHOULD obtain trust anchor information through one or more of the following mechanisms:

* a machine-readable trust list or trust registry used by the relevant education or EUDI Wallet ecosystem, such as the general trust lists supplied by the WE BUILD project;
* an issuer metadata endpoint published by the formal education provider or authorised academic identity provider;
* a trust framework entry managed by the WE BUILD ecosystem or by another authorised governance body;
* a pilot trust list used for controlled interoperability testing;
* a sectoral trust framework used by higher education, VET, or research and education identity providers, where applicable, such as trust registries aligned with the European Digital Credentials for Learning infrastructure.

Where the metadata attribute `trust_anchor` is present, it SHOULD identify the location or registry entry from which the Relying Party can obtain the issuer trust anchor or issuer authorisation information.

The Relying Party SHALL use the trust anchor to verify that:

* the issuer signing key or certificate chains to a trusted authority or registered trust anchor;
* the issuer is authorised to issue the `VerifiableMicroCredential` attestation type;
* the issuer metadata or trust framework entry has not expired or been revoked;
* the issuer identity in the credential is consistent with the issuer identity in the trust framework;
* the issuer is a formal education provider, or an authorised academic identity provider acting on behalf of one, for the relevant type of learning outcome.

Because the organisation that seals/issues the credential (`issuerCountry`) may differ from the organisation that awarded the underlying learning achievement (`awardingBody`), the Relying Party SHALL verify issuer trust based on the sealing organisation's trust anchor, and MAY additionally seek confirmation, for example through the accreditation information in Section 2.8 or through the trust framework entry, that the awarding body was itself entitled to award the micro-credential at the time of issuance.

Wallet Units MAY also use the same trust framework information during issuance to determine whether the provider is authorised to issue this attestation type.

## 6 Revocation

The Micro-credential Attestation records a completed, formally assessed learning achievement. Unlike affiliation-based attestations, the underlying fact it attests — that the learner achieved the stated learning outcomes — does not lapse over time and does not need to be periodically re-established. Consequently, revocation of a Micro-credential Attestation is not a mechanism for expressing that the achievement is "no longer valid" in a temporal sense, but a mechanism for correcting the record where the original issuance was defective or the credential instance itself needs to be withdrawn.

The credential expiration time (`exp`), where present, SHALL be understood as reflecting only the technical validity of the credential instance, for example to encourage periodic re-issuance onto current cryptographic material, and SHALL NOT be interpreted by a Relying Party as an indication that the underlying learning achievement itself has expired.

The issuer SHOULD support revocation or suspension of a Micro-credential Attestation where any of the following applies:

* the credential was issued in error, for example to the wrong natural person or with incorrect attribute values;
* the underlying assessment is subsequently found to have been invalid, for example due to an academic integrity finding such as plagiarism or assessment fraud;
* the awarding body's authorisation or accreditation to award the underlying qualification is withdrawn or successfully challenged with retroactive effect;
* the credential is reported lost, compromised, or fraudulently obtained;
* the awarding body issues a corrected or superseding version of the credential, for example following a grade appeal or administrative correction.

Revocation MAY be handled by one or more of the following mechanisms:

* an attestation status list mechanism, where supported (see [Topic 7] of Annex 2 of the ARF);
* an attestation revocation list mechanism, where supported;
* backend verification by the awarding body or authorised academic identity provider;
* publication of a corrected or superseding credential together with revocation of the original.

If a status or revocation mechanism is included in the credential, the Relying Party SHALL check the status before accepting the attestation, unless offline operating rules explicitly allow deferred status checking.

Because the Micro-credential Attestation is not time-bound in the same way as an affiliation-based attestation, the issuer SHOULD retain the ability to check and communicate status for as long as the credential can reasonably be expected to be presented, which may extend well beyond a single academic year or enrolment period.

Where a Micro-credential Attestation is revoked and superseded by a corrected version, the issuer SHOULD ensure that the `identifier` of the superseding credential allows a Relying Party, where necessary and with the Holder's cooperation, to establish the relationship to the revoked credential.

## 7 Compliance

This Rulebook is designed to align with the EUDI Wallet architectural approach for Electronic Attestations of Attributes and with the Attestation Rulebook structure defined in the ARF.

The Rulebook supports the following compliance objectives:

* it defines the attestation purpose and scope, aligned with the Council Recommendation of 16 June 2022 on a European approach to micro-credentials for lifelong learning and employability (2022/C 243/02);
* it defines mandatory, optional, and conditional attributes in an encoding-independent manner, reflecting the standard elements for describing micro-credentials set out in that Recommendation, as further specified by the European Learning Model (ELM) and the European Digital Credentials for Learning (EDC) application profile;
* it defines a legal category indication through `attestation_legal_category`;
* it defines an SD-JWT VC `vct` value for the attestation type;
* it defines issuer, awarding body, validity, and status metadata needed for verification, including a clear distinction between the organisation that seals/issues the credential and the organisation that awarded the underlying learning achievement;
* it defines code lists and integrity rules required for consistent interpretation;
* it defines how trust anchors can be obtained and used;
* it defines revocation expectations appropriate to a non-lapsing learning achievement, distinguishing technical credential validity from the continued truth of the achievement;
* it supports selective disclosure and data minimisation.

This Rulebook does not define a qualified EAA or public-sector EAA profile. It also does not define ISO/IEC 18013-5 mdoc or W3C VCDM encodings in this version, although the ELM/EDC JSON-LD-based representation is noted in Section 3.3 as a potential future basis for a W3C VCDM encoding.

This Rulebook does not define assurance or quality levels for the Micro-credential Attestation. Where a future version of this Rulebook introduces such levels, Sections 2.5 to 2.7 and Chapter 4 SHALL be updated accordingly.

This Rulebook does not define transactional or payment-related data. Where a Micro-credential Attestation is used in a transaction involving payment, such requirements SHALL be defined in a separate payment attestation, payment profile, or transaction-specific rulebook.

## 8 References

| **Item Reference** | **Standard name/details** |
|--------------------|---------------------------|
| [Council Recommendation on Micro-credentials] | Council Recommendation of 16 June 2022 on a European approach to micro-credentials for lifelong learning and employability (2022/C 243/02). Available: <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:32022H0627(02)> |
| [DEQAR] | Database of External Quality Assurance Results, used as a source controlled list for accreditation decisions in the European Learning Model. |
| [ELM] | European Learning Model, a multilingual data model supporting the interoperable representation of learning opportunities, qualifications, accreditation, and credentials. Available: <https://europa.eu/europass/elm-browser/index.html> |
| [EQF Recommendation] | Council Recommendation of 22 May 2017 on the European Qualifications Framework for lifelong learning (2017/C 189/03). Available: <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32017H0615(01)> |
| [ESCO] | European Skills, Competences, Qualifications and Occupations, the European multilingual classification of skills, competences, qualifications and occupations. Available: <https://esco.ec.europa.eu/en/classification/skill_main> |
| [EU Vocabularies] | EU multilingual controlled vocabularies published via the EU Vocabularies concept scheme service, including Assessment Type, Mode of Learning and Assessment, Learning Activity Type, and Method of Supervision and Verification, as used by the European Learning Model. Available: <https://op.europa.eu/en/web/eu-vocabularies> |
| [European Digital Identity Regulation] | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework |
| [HAIP] | Yasuda, K. *et al,* OpenID4VC High Assurance Interoperability Profile, OpenID Foundation |
| [IANA-JWT-Claims] | IANA JSON Web Token Claims Registry. Available: <https://www.iana.org/assignments/jwt/jwt.xhtml> |
| [ISCED-F 2013] | International Standard Classification of Education, Fields of Education and Training 2013, UNESCO Institute for Statistics. |
| [ISO/IEC 18013-5] | ISO/IEC 18013-5, Personal identification --- ISO-compliant driving licence - Part 5: Mobile driving licence application |
| [RFC 2119] | RFC 2119 - Key words for use in RFCs to Indicate Requirement Levels, S. Bradner, March 1997 |
| [RFC 3339] | RFC 3339 - Date and Time on the Internet: Timestamps, G. Klyne et al., July 2002 |
| [RFC 5322] | RFC 5322 - Internet Message Format, P. Resnick, October 2008 |
| [RFC 8610] | RFC 8610 - Concise Data Definition Language (CDDL): A Notational Convention to Express Concise Binary Object Representation, H. Birkholz et al., June 2019 |
| [RFC 8943] | RFC 8943 - Concise Binary Object Representation (CBOR) Tags for Date, M. Jones et al., November 2020 |
| [RFC 8949] | RFC 8949 - Concise Binary Object Representation (CBOR), C. Bormann et al., December 2020 |
| [SD-JWT VC] | SD-JWT-based Verifiable Credentials. Available: <https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/> |
| [Topic 7] | ARF Annex 2 - Topic 7 - Attestation revocation and revocation checking |
| [Topic 10] | ARF Annex 2 - Topic 10 - Issuing a PID or attestation to a Wallet Unit |
| [Topic 12] | ARF Annex 2 - Topic 12 - Attestation Rulebooks |
| [Topic 20] | ARF Annex 2 - Strong User authentication for electronic payments |
| [W3C VCDM v2.0] | Verifiable Credentials Data Model v2.0, W3C Recommendation |
| [WE BUILD BU5 Micro-credentials UC Scenario Specification] | WE BUILD consortium, WP2 -- BU5 Issue Micro-credentials, Scenario 1 -- Micro-credentials Specification, v1.0, 18 June 2026. |