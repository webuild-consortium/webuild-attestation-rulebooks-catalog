# Attestation Rulebook for attestations of type Student ID

Category: non-qualified EAA



*[Based on the WE BUILD Attestation Rulebook Template and the StudentID Attestation model.]*

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
   * [5.1 SD-JWT VC-based encoding](#51-sd-jwt-vc-based-encoding)
   * [5.2 ISO/IEC 18013-5-compliant encoding](#52-isoiec-18013-5-compliant-encoding)
   * [5.3 W3C Verifiable Credentials Data Model-based encoding](#53-w3c-verifiable-credentials-data-model-based-encoding)
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

This Rulebook defines the *StudentID Attestation* for use in the European Digital Identity Wallet ecosystem.

The StudentID Attestation expresses the real-world fact that a natural person is, or was during the applicable validity period, affiliated with an educational organisation in a student capacity. It enables relying parties to verify student status and selected identity or affiliation attributes using the EUDI Wallet.

The attestation is intended to be issued by an authentic source, such as a university, higher-education institution, or authorised academic identity provider. The Holder is the natural person to whom the student status applies. Relying Parties may include campus service providers, libraries, laboratories, access-control systems, mobility services, student-discount service providers, public or private service providers accepting student status, and other authorised verifiers.

In practical terms, the attestation enables a student to present proof of student status through an EUDI Wallet using selective disclosure. It can reduce reliance on paper student cards, manual checks, or real-time backend lookups, provided that the relying party can verify the issuer, credential signature, validity period, credential status where applicable, and the disclosed attributes needed for the transaction.

The attestation supports education and student-service use cases, including online and offline verification for campus services, discounted services, access control, mobility scenarios, academic services, and other scenarios where proof of student affiliation is required.

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
| StudentID Attestation | A Verifiable Credential representing a person's student affiliation and selected student identity attributes. |
| Educational organisation | A university, higher-education institution, or other authorised academic organisation acting as the authentic source for student status. |
| Authorised academic identity provider | A system or organisation authorised by an educational organisation to issue or manage student identity attestations. |
| Student | The natural person to whom the student affiliation applies. |
| Relying Party | An organisation or system that verifies the StudentID Attestation to make an access, eligibility, discount, or service decision. |
| SCHAC | Schema for Academia, a set of attributes commonly used in research and education identity federations. |
| eduPerson | A set of attributes commonly used to represent persons and affiliations in education and research identity federations. |

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


The StudentID Attestation is defined as a non-qualified Electronic Attestation of Attributes unless a future version of this Rulebook explicitly defines a qualified or public-sector legal category.

The attribute `attestation_legal_category` SHALL be included and SHALL have the value `non-qualified-EAA`.

The attestation model consists of the following logical groups:

* student identification attributes;
* organisation attributes;
* core identity attributes for holder matching;
* contact attributes;
* affiliation and status attributes;
* credential metadata.

The attestation is issued as a Verifiable Credential compatible with the EUDI Wallet using SD-JWT VC. The model aligns with the following issuer metadata parameters:

* `scope`: `StudentID`;
* `format`: `vc+sd-jwt`;
* `vct`: `VerifiableStudentID`;
* `claims`: the claims defined in this Rulebook;
* `proof_types_supported`: issuer-defined, including `jwt` where supported;
* `cryptographic_binding_methods_supported`: issuer-defined, for example `jwk` or `cose_key`.

#### Chapter overview and requirements

This chapter defines the attributes and metadata that a StudentID Attestation may contain. The attributes are defined in an encoding-independent manner. Each attribute is classified as mandatory, optional, or conditional.

The StudentID Attestation is typically medium- to long-lived, for example for an academic year, and is intended for repeated presentation with selective disclosure. The attribute set is designed to support data minimisation by allowing a Holder to disclose only the student attributes required for a specific transaction.

### 3.2 Mandatory attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| `attestation_legal_category` | ARF Topic 12 / Rulebook legal category indication | Indicates the legal category of the attestation. | string | `non-qualified-EAA` |
| `identifier` | Institutional student identifier | Unique student identifier, such as an institutional student number or equivalent. | string | `STU-2026-000123` |
| `schacHomeOrganization` | SCHAC `schacHomeOrganization` | Home organisation or institution domain or identifier. | string | `aegean.gr` |
| `firstName` | OIDC `given_name` where applicable | Student given name. | string | `Nikos` |
| `familyName` | OIDC `family_name` where applicable | Student family name. | string | `Triantafyllou` |
| `eduPersonPrincipalName` | eduPerson `eduPersonPrincipalName` | Principal name of the student, often expressed in `user@realm` format. | string | `ntriantafyllou@aegean.gr` |
| `eduPersonPrimaryAffiliation` | eduPerson `eduPersonPrimaryAffiliation` | Primary affiliation of the subject with the educational organisation. | string | `student` |

### 3.3 Optional attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| `schacPersonalUniqueCode` | SCHAC `schacPersonalUniqueCode` | Unique code associated with the student. | string | `urn:schac:personalUniqueCode:int:esi:example.edu:123456` |
| `schacPersonalUniqueID` | SCHAC `schacPersonalUniqueID` | One or more unique identifiers for the student. | array of strings | `["urn:schac:personalUniqueID:gr:student:123456"]` |
| `displayName` | OIDC `name` or education profile display name | Display name formatted for user interfaces. | string | `Nikos Triantafyllou` |
| `commonName` | Common name / CN | Alternate display or preferred name. | string | `Nikos Triantafyllou` |
| `dateOfBirth` | ISO 8601 date / OIDC `birthdate` where applicable | Student date of birth. | date | `1990-04-12` |
| `mail` | RFC 5322 mailbox | Email address. | string | `ntriantafyllou@aegean.gr` |
| `eduPersonAffiliation` | eduPerson `eduPersonAffiliation` | One or more affiliations, such as `student`, `member`, or `affiliate`. | array of strings | `["student", "member"]` |
| `eduPersonScopedAffiliation` | eduPerson `eduPersonScopedAffiliation` | One or more scoped affiliation values. | array of strings | `["student@aegean.gr"]` |
| `eduPersonAssurance` | eduPerson `eduPersonAssurance` | One or more assurance values for the subject or attributes. | array of strings | `["https://refeds.org/assurance"]` |

### 3.4 Conditional attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| `dateOfBirth` | ISO 8601 date / OIDC `birthdate` where applicable | SHALL be included only where needed for holder matching, age-related eligibility, or another justified relying-party purpose. If included, it SHALL represent the subject's birth date and SHALL NOT be in the future. | date | `1990-04-12` |
| `mail` | RFC 5322 mailbox | SHOULD be disclosed only where the transaction requires a contact email or account matching. | string | `ntriantafyllou@aegean.gr` |
| `eduPersonScopedAffiliation` | eduPerson `eduPersonScopedAffiliation` | SHOULD be included where a relying party needs both the affiliation value and the organisational scope. | array of strings | `["student@aegean.gr"]` |
| `eduPersonAssurance` | eduPerson `eduPersonAssurance` | SHOULD be included where a relying party needs assurance information to decide whether the credential is sufficient for a specific service. | array of strings | `["https://refeds.org/assurance"]` |

## 4 Metadata

Metadata describes the attestation rather than its subject.

### 4.1 Mandatory metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| `vct` | SD-JWT VC | Verifiable Credential Type identifying this attestation type. | string | `VerifiableStudentID` |
| `iss` | SD-JWT VC / JWT | Identifier of the issuer of the credential. | string | `https://issuer.example-university.edu` |
| `iat` | JWT | Time at which the credential was issued. | integer | `1772366400` |
| `exp` | JWT | Expiration time of the credential. For this attestation it SHOULD reflect the end of the applicable student-status validity period, such as the academic year or enrolment period. | integer | `1798761600` |
| `cnf` | SD-JWT VC / JOSE | Confirmation claim binding the credential to key material controlled by the Holder or Wallet Unit, where holder binding is used. | object | `{ "jwk": { ... } }` |
| `status` | SD-JWT VC status mechanism, where used | Status information enabling revocation or suspension checks. | object | `{ "status_list": { ... } }` |

**Legal category.** This Rulebook retains the `attestation_legal_category` attribute.
Section 4.1 of the generic template replaces it with the `category` attribute of
[ETSI TS 119 472-1], whose value for this category is `eaa:eu:non-qualified`.
EW-DM-12-029, legacy ARB_25, of ARF version 3.0.0 is a SHALL that still requires
`attestation_legal_category`, so the template and the ARF disagree. The attribute is
left as written and the deviation is recorded for the rulebook quality assurance group.

### 4.2 Optional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| `nbf` | JWT | Time before which the credential MUST NOT be accepted. | integer | `1772366400` |
| `jti` | JWT | Unique identifier of the credential instance. | string | `urn:uuid:4f6a8e9a-40c2-4d21-96f8-7b85cc3f6c20` |
| `trust_anchor` | ARF Topic 12 | Location or identifier of the machine-readable trust anchor or trust framework entry used to verify issuer authorisation. | string | `https://trust.example.eu/education/institutions/example-university` |
| `cryptographically_bound_to` | ARF Topic 12 / ARB_28 | Identifier of another attestation type to which this attestation is cryptographically bound, where such binding is used. | string | `urn:eudi:pid:1` |

### 4.3 Conditional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| `status` | SD-JWT VC status mechanism, where used | SHOULD be present where the StudentID Attestation is medium- or long-lived and may need to be revoked, suspended, or updated before expiry. | object | `{ "status_list": { ... } }` |
| `cryptographically_bound_to` | ARF Topic 12 / ARB_28 | SHOULD be present where the StudentID Attestation must be presented together with PID or another identity attestation for strong holder matching. | string | `urn:eudi:pid:1` |

### 4.4 Code lists

| **Field name** | **Allowed values** | **Meaning** | **Source / vocabulary** | **Notes / extensibility** |
| --- | --- | --- | --- | --- |
| `dateOfBirth` | ISO 8601 date values | Subject's date of birth. | ISO 8601 | Date-only format `YYYY-MM-DD` SHALL be used where possible. |
| `mail` | RFC 5322-compliant mailbox strings | Email address. | RFC 5322 | Implementations SHOULD apply practical email validation appropriate for the issuing context. |
| `schacHomeOrganization` | Issuer-defined organisation identifiers, commonly domain-style values | Identifies the home educational organisation. | SCHAC / issuer-defined controlled values | Values SHOULD be stable and consistently interpreted across issuers and relying parties. |
| `eduPersonPrimaryAffiliation` | Issuer-defined controlled vocabulary; recommended values include `student` | Primary affiliation of the subject. | eduPerson / issuer-defined controlled values | For this attestation, the value SHOULD be `student` unless the issuer has a specific student-equivalent category. |
| `eduPersonAffiliation` | Issuer-defined controlled vocabulary; examples include `student`, `member`, `affiliate` | One or more affiliations of the subject. | eduPerson / issuer-defined controlled values | Values SHOULD be consistent with `eduPersonPrimaryAffiliation`. |
| `eduPersonScopedAffiliation` | Scoped affiliation strings, commonly `affiliation@scope` | Affiliation value scoped to an organisation or domain. | eduPerson / SCHAC context | Scope SHOULD be consistent with `schacHomeOrganization`. |
| `eduPersonAssurance` | Assurance URIs or issuer-defined assurance values | Assurance information for the subject or attributes. | eduPerson / REFEDS or issuer-defined assurance framework | Additional values SHOULD only be used if documented by the issuer or trust framework. |
| `attestation_legal_category` | `non-qualified-EAA`, `QEAA`, `PuB-EAA` | Indicates the legal category of the attestation. | ARF Topic 12 / Rulebook template | This Rulebook uses `non-qualified-EAA`. |

### 4.5 Integrity rules

| **Rule ID** | **Rule statement** | **Why it exists** | **Where enforced** | **Verifier / issuer behavior on failure** |
| --- | --- | --- | --- | --- |
| `SID-IR-01` | `identifier`, `firstName`, `familyName`, `schacHomeOrganization`, `eduPersonPrincipalName`, and `eduPersonPrimaryAffiliation` SHALL be present. | Ensures that the credential contains the mandatory student identification, organisation, identity, and affiliation data. | Issuer business rules, schema validation, verifier business validation. | Issuer SHALL reject incomplete credential data. Verifier SHALL treat the attestation as invalid or insufficient if mandatory claims are missing. |
| `SID-IR-02` | If `dateOfBirth` is included, it SHALL represent the subject's birth date and SHALL NOT be in the future. | Prevents invalid identity data and supports correct age-related or matching checks. | Issuer business rules and verifier business validation. | Issuer SHALL reject invalid dates. Verifier SHALL reject or ignore an invalid `dateOfBirth` claim depending on the transaction. |
| `SID-IR-03` | If `eduPersonScopedAffiliation` values are included, they SHOULD be consistent with `schacHomeOrganization`, for example by using a matching scoping domain. | Ensures that scoped affiliation can be interpreted consistently. | Issuer business rules and verifier business validation. | Issuer SHOULD prevent inconsistent scoped affiliations. Verifier MAY reject or downgrade confidence in inconsistent values. |
| `SID-IR-04` | If `eduPersonAffiliation` is present, it SHOULD include the value of `eduPersonPrimaryAffiliation`. | Ensures that the primary affiliation is consistent with the broader affiliation list. | Issuer business rules and verifier business validation. | Issuer SHOULD align the values. Verifier MAY treat inconsistent affiliation data as insufficient. |
| `SID-IR-05` | If `schacPersonalUniqueID` is multi-valued, each entry SHOULD be unique within the array. | Prevents duplicate identifiers and ambiguity. | Issuer business rules and schema validation. | Issuer SHOULD remove duplicates. Verifier MAY ignore duplicate entries. |
| `SID-IR-06` | Selective disclosure SHALL allow the Holder to reveal only the attributes required for the transaction. | Supports privacy and data minimisation. | Issuer credential construction and Wallet presentation logic. | Verifier SHALL request only necessary claims. Wallet SHOULD allow the Holder to review the disclosed claims. |
| `SID-IR-07` | `eduPersonPrimaryAffiliation` SHOULD be `student` or an issuer-defined student-equivalent value for this attestation type. | Ensures that the attestation actually represents student status. | Issuer business rules and verifier business validation. | Verifier SHOULD reject the credential for student-status decisions if the affiliation does not indicate student status. |


## 5 Formats


### 5.1 SD-JWT VC-based encoding

The StudentID Attestation SHALL be issued as an SD-JWT VC.

The Verifiable Credential Type (`vct`) for this attestation type is:

```text
VerifiableStudentID
```

The credential claims defined in this section SHALL follow SD-JWT VC and HAIP conventions where applicable. Claim names are either IANA-registered JWT claims, public names, or private names specific to this attestation type.

For all claims, this Rulebook specifies whether an Attestation Provider MUST, MAY, or MUST NOT make the claim selectively disclosable.

#### 5.1.1 IANA-registered and standard JWT / SD-JWT VC claims

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Reference/Notes** | **Disclosable** |
| --- | --- | --- | --- | --- |
| `iss` | `iss` | string | JWT issuer identifier. | MUST NOT |
| `iat` | `iat` | integer | Issued-at timestamp. | MUST NOT |
| `nbf` | `nbf` | integer | Not-before timestamp, where used. | MUST NOT |
| `exp` | `exp` | integer | Expiration timestamp. SHOULD reflect the end of the applicable student-status validity period. | MUST NOT |
| `jti` | `jti` | string | Unique credential instance identifier, where used. | MUST NOT |
| `cnf` | `cnf` | object | Holder binding confirmation claim, where used. | MUST NOT |
| `status` | `status` | object | Status or revocation information, where used. | MUST NOT |
| `vct` | `vct` | string | SD-JWT VC type. Value SHALL be `VerifiableStudentID`. | MUST NOT |

#### 5.1.2 Public or reusable claims

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Reference/Notes** | **Disclosable** |
| --- | --- | --- | --- | --- |
| `firstName` | `firstName` | string | Student given name. May be mapped to OIDC `given_name` in implementations that use OIDC naming conventions. | MUST |
| `familyName` | `familyName` | string | Student family name. May be mapped to OIDC `family_name` in implementations that use OIDC naming conventions. | MUST |
| `displayName` | `displayName` | string | Display name formatted for user interfaces. | MAY |
| `commonName` | `commonName` | string | Alternate display or preferred name. | MAY |
| `dateOfBirth` | `dateOfBirth` | string | Date of birth formatted as ISO 8601 date, where disclosed. | MAY |
| `mail` | `mail` | string | Email address. | MAY |

#### 5.1.3 Private claims specific to the StudentID Attestation

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Notes** | **Disclosable** |
| --- | --- | --- | --- | --- |
| `attestation_legal_category` | `attestation_legal_category` | string | SHALL be `non-qualified-EAA`. | MUST NOT |
| `identifier` | `identifier` | string | Unique student identifier, such as institutional student number or equivalent. | MUST |
| `schacPersonalUniqueCode` | `schacPersonalUniqueCode` | string | Unique code associated with the student. | MAY |
| `schacPersonalUniqueID` | `schacPersonalUniqueID` | array of strings | One or more unique identifiers for the student. | MAY |
| `schacHomeOrganization` | `schacHomeOrganization` | string | Home organisation or institution domain or identifier. | MUST |
| `eduPersonPrincipalName` | `eduPersonPrincipalName` | string | Principal name, often in `user@realm` format. | MAY |
| `eduPersonPrimaryAffiliation` | `eduPersonPrimaryAffiliation` | string | Primary affiliation, expected to indicate student status. | MUST |
| `eduPersonAffiliation` | `eduPersonAffiliation` | array of strings | One or more affiliations. | MAY |
| `eduPersonScopedAffiliation` | `eduPersonScopedAffiliation` | array of strings | One or more scoped affiliation values. | MAY |
| `eduPersonAssurance` | `eduPersonAssurance` | array of strings | One or more assurance values for the subject or attributes. | MAY |
| `trust_anchor` | `trust_anchor` | string | Location or identifier of the trust anchor or trust framework entry used to verify issuer authorisation, where used. | MUST NOT |
| `cryptographically_bound_to` | `cryptographically_bound_to` | string | Identifier of another attestation type to which this attestation is bound, where used. | MUST NOT |

#### 5.1.4 Example JWT claim set

```json
{
  "iss": "https://issuer.example-university.edu",
  "iat": 1772366400,
  "nbf": 1772366400,
  "exp": 1798761600,
  "jti": "urn:uuid:4f6a8e9a-40c2-4d21-96f8-7b85cc3f6c20",
  "vct": "VerifiableStudentID",
  "attestation_legal_category": "non-qualified-EAA",
  "identifier": "STU-2026-000123",
  "schacPersonalUniqueCode": "urn:schac:personalUniqueCode:int:esi:example.edu:123456",
  "schacPersonalUniqueID": [
    "urn:schac:personalUniqueID:gr:student:123456"
  ],
  "schacHomeOrganization": "aegean.gr",
  "firstName": "Nikos",
  "familyName": "Triantafyllou",
  "displayName": "Nikos Triantafyllou",
  "commonName": "Nikos Triantafyllou",
  "dateOfBirth": "1990-04-12",
  "mail": "ntriantafyllou@aegean.gr",
  "eduPersonPrincipalName": "ntriantafyllou@aegean.gr",
  "eduPersonPrimaryAffiliation": "student",
  "eduPersonAffiliation": [
    "student",
    "member"
  ],
  "eduPersonScopedAffiliation": [
    "student@aegean.gr"
  ],
  "eduPersonAssurance": [
    "https://refeds.org/assurance"
  ],
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

#### 5.1.5 Example issued SD-JWT

The following is a non-normative placeholder example. A production SD-JWT SHALL be generated by the issuer using the applicable signing algorithm, disclosure construction, holder binding, and SD-JWT VC rules.

```text
<issuer-signed-sd-jwt>~<disclosure-1>~<disclosure-2>~<disclosure-n>~<holder-binding-jwt>
```

#### 5.1.6 Example human-readable disclosed payload

A verifier that requests only proof of student status for a discounted service may receive a presentation disclosing the following claims:

```json
{
  "vct": "VerifiableStudentID",
  "identifier": "STU-2026-000123",
  "schacHomeOrganization": "aegean.gr",
  "firstName": "Nikos",
  "familyName": "Triantafyllou",
  "eduPersonPrimaryAffiliation": "student",
  "eduPersonScopedAffiliation": [
    "student@aegean.gr"
  ]
}
```

A verifier that only needs to know whether the Holder has student status SHOULD request the minimum claims necessary for that decision and SHOULD NOT request `dateOfBirth`, `mail`, or unique identifiers unless required for the transaction.

The issuer identity, credential type, expiry time, signature, holder binding proof, and trust anchor information are not treated as selectively disclosable student attributes and SHALL remain available to the verifier for technical validation.

### 5.2 ISO/IEC 18013-5-compliant encoding

This version of the Rulebook does not define an ISO/IEC 18013-5 mdoc encoding for the StudentID Attestation.

The StudentID Attestation defined in this Rulebook is specified for SD-JWT VC-based issuance and presentation. If a future version of this Rulebook defines an ISO/IEC 18013-5-compliant mdoc representation, that version SHALL define a unique document type, namespaces, attribute identifiers, CBOR encoding rules, and illustrative mdoc examples.

### 5.3 W3C Verifiable Credentials Data Model-based encoding

This version of the Rulebook does not define a W3C Verifiable Credentials Data Model encoding for the StudentID Attestation.

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

The StudentID Attestation is intended for verifying student status and selected student identity or affiliation attributes.

Typical usage scenarios include:

* presentation by the student for campus services such as libraries, laboratories, rooms, buildings, or academic platforms;
* presentation for student discounts or eligibility checks;
* presentation for mobility scenarios involving another educational organisation or service provider;
* online verification by a service provider using remote presentation protocols;
* offline or low-connectivity verification where the verifier can validate the credential signature, issuer, validity period, status where available, and disclosed attributes without relying on a real-time issuer backend.

A Relying Party receiving the attestation SHALL verify:

* the issuer signature;
* the SD-JWT VC type (`vct`);
* the issuer authorisation to issue StudentID Attestations;
* the credential validity period;
* the credential status, where a status mechanism is present;
* holder binding, where used;
* the integrity rules defined in Section 2.9;
* that the disclosed student attributes are sufficient for the relying-party decision.

The Relying Party SHOULD request and verify PID or another accepted identity credential where the transaction requires strong identity matching. For low-risk student-status checks, the Relying Party MAY rely on the StudentID Attestation alone, provided that the issuer, signature, validity, status, and holder binding checks are successful and this is consistent with the relying party's policy.

The Relying Party SHALL apply data minimisation and SHALL request only the attributes required for the transaction. For example, a discount service may only need `eduPersonPrimaryAffiliation` and `schacHomeOrganization`, while an account-linking process may require `eduPersonPrincipalName` or `mail`.

The attestation SHOULD be device-bound through holder binding where supported by the EUDI Wallet and the applicable SD-JWT VC profile. The attestation MAY be cryptographically bound to a PID or another accepted identity attestation where strong identity matching is required. Where this binding is used, the metadata attribute `cryptographically_bound_to` SHOULD contain:

```text
urn:eudi:pid:1
```

No payment-specific transactional data is defined by this Rulebook. If the StudentID Attestation is used as part of a transaction that also involves payment, payment-related requirements SHALL be defined in a separate payment attestation, payment profile, or transaction-specific rulebook.


### 7.3 Lifecycle management

The issuer sets the validity period of the attestation and reissues it when the
underlying facts change, revoking the superseded attestation as described in chapter 8.

### 7.4 Embedded disclosure policy

This attestation defines no embedded disclosure policy.

## 8 Revocation

The StudentID Attestation is typically medium- to long-lived and intended for repeated presentation, for example during an academic year or enrolment period.

The credential expiration time (`exp`) SHOULD be aligned with the end of the applicable student-status validity period, such as the end of an academic year, enrolment period, mobility period, or other issuer-defined validity period.

Because student status can change before the planned expiry date, the issuer SHOULD support revocation or suspension where the attestation is valid for more than 24 hours.

Revocation MAY be handled by one or more of the following mechanisms:

* an attestation status list mechanism, where supported;
* an attestation revocation list mechanism, where supported;
* backend verification by the educational organisation or authorised academic identity provider;
* short validity with periodic re-issuance, where appropriate for the service model.

If a status or revocation mechanism is included in the credential, the Relying Party SHALL check the status before accepting the attestation, unless offline operating rules explicitly allow deferred status checking.

The issuer SHOULD revoke or suspend the attestation if the student is no longer enrolled, loses the relevant student status, the credential was issued incorrectly, the credential is reported compromised, or the underlying student identifier is no longer valid for presentation.

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

A Relying Party SHALL verify that the issuer of the StudentID Attestation is authorised to issue this attestation type.

For non-qualified EAA deployments, the Relying Party SHOULD obtain trust anchor information through one or more of the following mechanisms:

* a machine-readable trust list or trust registry used by the relevant education or EUDI Wallet ecosystem;
* an issuer metadata endpoint published by the educational organisation or authorised academic identity provider;
* a trust framework entry managed by the WE BUILD ecosystem or by another authorised governance body;
* a pilot trust list used for controlled interoperability testing;
* a federation or sectoral trust framework used by research and education identity providers, where applicable.

Where the metadata attribute `trust_anchor` is present, it SHOULD identify the location or registry entry from which the Relying Party can obtain the issuer trust anchor or issuer authorisation information.

The Relying Party SHALL use the trust anchor to verify that:

* the issuer signing key or certificate chains to a trusted authority or registered trust anchor;
* the issuer is authorised to issue the `VerifiableStudentID` attestation type;
* the issuer metadata or trust framework entry has not expired or been revoked;
* the issuer identity in the credential is consistent with the issuer identity in the trust framework;
* the issuer is an educational organisation or authorised academic identity provider for the relevant student population.

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
| [RFC 5322] | RFC 5322 - Internet Message Format, P. Resnick, October 2008 |
| [RFC 8610] | RFC 8610 - Concise Data Definition Language (CDDL): A Notational Convention to Express Concise Binary Object Representation, H. Birkholz et al., June 2019 |
| [RFC 8943] | RFC 8943 - Concise Binary Object Representation (CBOR) Tags for Date, M. Jones et al., November 2020 |
| [RFC 8949] | RFC 8949 - Concise Binary Object Representation (CBOR), C. Bormann et al., December 2020 |
| [SD-JWT VC] | SD-JWT-based Verifiable Credentials. Available: <https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/> |
| [SCHAC] | Schema for Academia attributes used in research and education identity contexts |
| [eduPerson] | eduPerson schema attributes used in research and education identity contexts |
| [Topic 7] | ARF Annex 2 - Topic 7 - Attestation revocation and revocation checking |
| [Topic 10] | ARF Annex 2 - Topic 10 - Issuing a PID or attestation to a Wallet Unit |
| [Topic 12] | ARF Annex 2 - Topic 12 - Attestation Rulebooks |
| [Topic 20] | ARF Annex 2 - Strong User authentication for electronic payments |
| [W3C VCDM v2.0] | Verifiable Credentials Data Model v2.0, W3C Recommendation |
