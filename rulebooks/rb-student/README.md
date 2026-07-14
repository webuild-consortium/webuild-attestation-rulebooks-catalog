(Template version: 1.1)

# WE BUILD Attestation Rulebook for attestations of type *Student ID*

*[Based on the WE BUILD Attestation Rulebook Template and the StudentID Attestation model.]*

* Author(s):
    * Nikos Triantafyllou, UAegean
* Previous Authors
    * N/A

| Version | Date | Description |
|---------|------|-------------|
| 0.1 | 2026-06-01 | Initial draft rulebook for the StudentID Attestation |
| 0.9 | 2026-06-23 | Draft, ready for review/QA |

**Feedback:**

* Github, portal, email, Slack

## 1 Introduction

### 1.1 Document scope and purpose

This Rulebook defines the *StudentID Attestation* for use in the European Digital Identity Wallet ecosystem.

The StudentID Attestation expresses the real-world fact that a natural person is, or was during the applicable validity period, affiliated with an educational organisation in a student capacity. It enables relying parties to verify student status and selected identity or affiliation attributes using the EUDI Wallet.

The attestation is intended to be issued by an authentic source, such as a university, higher-education institution, or authorised academic identity provider. The Holder is the natural person to whom the student status applies. Relying Parties may include campus service providers, libraries, laboratories, access-control systems, mobility services, student-discount service providers, public or private service providers accepting student status, and other authorised verifiers.

In practical terms, the attestation enables a student to present proof of student status through an EUDI Wallet using selective disclosure. It can reduce reliance on paper student cards, manual checks, or real-time backend lookups, provided that the relying party can verify the issuer, credential signature, validity period, credential status where applicable, and the disclosed attributes needed for the transaction.

The attestation supports education and student-service use cases, including online and offline verification for campus services, discounted services, access control, mobility scenarios, academic services, and other scenarios where proof of student affiliation is required.

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
| StudentID Attestation | A Verifiable Credential representing a person's student affiliation and selected student identity attributes. |
| Educational organisation | A university, higher-education institution, or other authorised academic organisation acting as the authentic source for student status. |
| Authorised academic identity provider | A system or organisation authorised by an educational organisation to issue or manage student identity attestations. |
| Student | The natural person to whom the student affiliation applies. |
| Relying Party | An organisation or system that verifies the StudentID Attestation to make an access, eligibility, discount, or service decision. |
| SCHAC | Schema for Academia, a set of attributes commonly used in research and education identity federations. |
| eduPerson | A set of attributes commonly used to represent persons and affiliations in education and research identity federations. |

## 2 Attestation attributes and metadata

### Chapter overview and requirements

This chapter defines the attributes and metadata that a StudentID Attestation may contain. The attributes are defined in an encoding-independent manner. Each attribute is classified as mandatory, optional, or conditional.

The StudentID Attestation is typically medium- to long-lived, for example for an academic year, and is intended for repeated presentation with selective disclosure. The attribute set is designed to support data minimisation by allowing a Holder to disclose only the student attributes required for a specific transaction.

### 2.1 Introduction

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

### 2.2 Mandatory attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---------------------|------------------------|----------------|---------------|-------------------|
| `attestation_legal_category` | ARF Topic 12 / Rulebook legal category indication | Indicates the legal category of the attestation. | string | `non-qualified-EAA` |
| `identifier` | Institutional student identifier | Unique student identifier, such as an institutional student number or equivalent. | string | `STU-2026-000123` |
| `schacHomeOrganization` | SCHAC `schacHomeOrganization` | Home organisation or institution domain or identifier. | string | `aegean.gr` |
| `firstName` | OIDC `given_name` where applicable | Student given name. | string | `Nikos` |
| `familyName` | OIDC `family_name` where applicable | Student family name. | string | `Triantafyllou` |
| `eduPersonPrincipalName` | eduPerson `eduPersonPrincipalName` | Principal name of the student, often expressed in `user@realm` format. | string | `ntriantafyllou@aegean.gr` |
| `eduPersonPrimaryAffiliation` | eduPerson `eduPersonPrimaryAffiliation` | Primary affiliation of the subject with the educational organisation. | string | `student` |

### 2.3 Optional attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---------------------|------------------------|----------------|---------------|-------------------|
| `schacPersonalUniqueCode` | SCHAC `schacPersonalUniqueCode` | Unique code associated with the student. | string | `urn:schac:personalUniqueCode:int:esi:example.edu:123456` |
| `schacPersonalUniqueID` | SCHAC `schacPersonalUniqueID` | One or more unique identifiers for the student. | array of strings | `["urn:schac:personalUniqueID:gr:student:123456"]` |
| `displayName` | OIDC `name` or education profile display name | Display name formatted for user interfaces. | string | `Nikos Triantafyllou` |
| `commonName` | Common name / CN | Alternate display or preferred name. | string | `Nikos Triantafyllou` |
| `dateOfBirth` | ISO 8601 date / OIDC `birthdate` where applicable | Student date of birth. | date | `1990-04-12` |
| `mail` | RFC 5322 mailbox | Email address. | string | `ntriantafyllou@aegean.gr` |
| `eduPersonAffiliation` | eduPerson `eduPersonAffiliation` | One or more affiliations, such as `student`, `member`, or `affiliate`. | array of strings | `["student", "member"]` |
| `eduPersonScopedAffiliation` | eduPerson `eduPersonScopedAffiliation` | One or more scoped affiliation values. | array of strings | `["student@aegean.gr"]` |
| `eduPersonAssurance` | eduPerson `eduPersonAssurance` | One or more assurance values for the subject or attributes. | array of strings | `["https://refeds.org/assurance"]` |

### 2.4 Conditional attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---------------------|------------------------|----------------|---------------|-------------------|
| `dateOfBirth` | ISO 8601 date / OIDC `birthdate` where applicable | SHALL be included only where needed for holder matching, age-related eligibility, or another justified relying-party purpose. If included, it SHALL represent the subject's birth date and SHALL NOT be in the future. | date | `1990-04-12` |
| `mail` | RFC 5322 mailbox | SHOULD be disclosed only where the transaction requires a contact email or account matching. | string | `ntriantafyllou@aegean.gr` |
| `eduPersonScopedAffiliation` | eduPerson `eduPersonScopedAffiliation` | SHOULD be included where a relying party needs both the affiliation value and the organisational scope. | array of strings | `["student@aegean.gr"]` |
| `eduPersonAssurance` | eduPerson `eduPersonAssurance` | SHOULD be included where a relying party needs assurance information to decide whether the credential is sufficient for a specific service. | array of strings | `["https://refeds.org/assurance"]` |

### 2.5 Mandatory metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---------------------|------------------------|----------------|---------------|-------------------|
| `vct` | SD-JWT VC | Verifiable Credential Type identifying this attestation type. | string | `VerifiableStudentID` |
| `iss` | SD-JWT VC / JWT | Identifier of the issuer of the credential. | string | `https://issuer.example-university.edu` |
| `iat` | JWT | Time at which the credential was issued. | integer | `1772366400` |
| `exp` | JWT | Expiration time of the credential. For this attestation it SHOULD reflect the end of the applicable student-status validity period, such as the academic year or enrolment period. | integer | `1798761600` |
| `cnf` | SD-JWT VC / JOSE | Confirmation claim binding the credential to key material controlled by the Holder or Wallet Unit, where holder binding is used. | object | `{ "jwk": { ... } }` |
| `status` | SD-JWT VC status mechanism, where used | Status information enabling revocation or suspension checks. | object | `{ "status_list": { ... } }` |

### 2.6 Optional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---------------------|------------------------|----------------|---------------|-------------------|
| `nbf` | JWT | Time before which the credential MUST NOT be accepted. | integer | `1772366400` |
| `jti` | JWT | Unique identifier of the credential instance. | string | `urn:uuid:4f6a8e9a-40c2-4d21-96f8-7b85cc3f6c20` |
| `trust_anchor` | ARF Topic 12 | Location or identifier of the machine-readable trust anchor or trust framework entry used to verify issuer authorisation. | string | `https://trust.example.eu/education/institutions/example-university` |
| `cryptographically_bound_to` | ARF Topic 12 / ARB_28 | Identifier of another attestation type to which this attestation is cryptographically bound, where such binding is used. | string | `urn:eudi:pid:1` |

### 2.7 Conditional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---------------------|------------------------|----------------|---------------|-------------------|
| `status` | SD-JWT VC status mechanism, where used | SHOULD be present where the StudentID Attestation is medium- or long-lived and may need to be revoked, suspended, or updated before expiry. | object | `{ "status_list": { ... } }` |
| `cryptographically_bound_to` | ARF Topic 12 / ARB_28 | SHOULD be present where the StudentID Attestation must be presented together with PID or another identity attestation for strong holder matching. | string | `urn:eudi:pid:1` |

### 2.8 Code lists

| **Field name** | **Allowed values** | **Meaning** | **Source / vocabulary** | **Notes / extensibility** |
|----------------|--------------------|-------------|--------------------------|---------------------------|
| `dateOfBirth` | ISO 8601 date values | Subject's date of birth. | ISO 8601 | Date-only format `YYYY-MM-DD` SHALL be used where possible. |
| `mail` | RFC 5322-compliant mailbox strings | Email address. | RFC 5322 | Implementations SHOULD apply practical email validation appropriate for the issuing context. |
| `schacHomeOrganization` | Issuer-defined organisation identifiers, commonly domain-style values | Identifies the home educational organisation. | SCHAC / issuer-defined controlled values | Values SHOULD be stable and consistently interpreted across issuers and relying parties. |
| `eduPersonPrimaryAffiliation` | Issuer-defined controlled vocabulary; recommended values include `student` | Primary affiliation of the subject. | eduPerson / issuer-defined controlled values | For this attestation, the value SHOULD be `student` unless the issuer has a specific student-equivalent category. |
| `eduPersonAffiliation` | Issuer-defined controlled vocabulary; examples include `student`, `member`, `affiliate` | One or more affiliations of the subject. | eduPerson / issuer-defined controlled values | Values SHOULD be consistent with `eduPersonPrimaryAffiliation`. |
| `eduPersonScopedAffiliation` | Scoped affiliation strings, commonly `affiliation@scope` | Affiliation value scoped to an organisation or domain. | eduPerson / SCHAC context | Scope SHOULD be consistent with `schacHomeOrganization`. |
| `eduPersonAssurance` | Assurance URIs or issuer-defined assurance values | Assurance information for the subject or attributes. | eduPerson / REFEDS or issuer-defined assurance framework | Additional values SHOULD only be used if documented by the issuer or trust framework. |
| `attestation_legal_category` | `non-qualified-EAA`, `QEAA`, `PuB-EAA` | Indicates the legal category of the attestation. | ARF Topic 12 / Rulebook template | This Rulebook uses `non-qualified-EAA`. |

### 2.9 Integrity rules

| **Rule ID** | **Rule statement** | **Why it exists** | **Where enforced** | **Verifier / issuer behavior on failure** |
|-------------|--------------------|-------------------|--------------------|-------------------------------------------|
| `SID-IR-01` | `identifier`, `firstName`, `familyName`, `schacHomeOrganization`, `eduPersonPrincipalName`, and `eduPersonPrimaryAffiliation` SHALL be present. | Ensures that the credential contains the mandatory student identification, organisation, identity, and affiliation data. | Issuer business rules, schema validation, verifier business validation. | Issuer SHALL reject incomplete credential data. Verifier SHALL treat the attestation as invalid or insufficient if mandatory claims are missing. |
| `SID-IR-02` | If `dateOfBirth` is included, it SHALL represent the subject's birth date and SHALL NOT be in the future. | Prevents invalid identity data and supports correct age-related or matching checks. | Issuer business rules and verifier business validation. | Issuer SHALL reject invalid dates. Verifier SHALL reject or ignore an invalid `dateOfBirth` claim depending on the transaction. |
| `SID-IR-03` | If `eduPersonScopedAffiliation` values are included, they SHOULD be consistent with `schacHomeOrganization`, for example by using a matching scoping domain. | Ensures that scoped affiliation can be interpreted consistently. | Issuer business rules and verifier business validation. | Issuer SHOULD prevent inconsistent scoped affiliations. Verifier MAY reject or downgrade confidence in inconsistent values. |
| `SID-IR-04` | If `eduPersonAffiliation` is present, it SHOULD include the value of `eduPersonPrimaryAffiliation`. | Ensures that the primary affiliation is consistent with the broader affiliation list. | Issuer business rules and verifier business validation. | Issuer SHOULD align the values. Verifier MAY treat inconsistent affiliation data as insufficient. |
| `SID-IR-05` | If `schacPersonalUniqueID` is multi-valued, each entry SHOULD be unique within the array. | Prevents duplicate identifiers and ambiguity. | Issuer business rules and schema validation. | Issuer SHOULD remove duplicates. Verifier MAY ignore duplicate entries. |
| `SID-IR-06` | Selective disclosure SHALL allow the Holder to reveal only the attributes required for the transaction. | Supports privacy and data minimisation. | Issuer credential construction and Wallet presentation logic. | Verifier SHALL request only necessary claims. Wallet SHOULD allow the Holder to review the disclosed claims. |
| `SID-IR-07` | `eduPersonPrimaryAffiliation` SHOULD be `student` or an issuer-defined student-equivalent value for this attestation type. | Ensures that the attestation actually represents student status. | Issuer business rules and verifier business validation. | Verifier SHOULD reject the credential for student-status decisions if the affiliation does not indicate student status. |

# 3 Attestation encoding

## 3.1 ISO/IEC 18013-5-compliant encoding

This version of the Rulebook does not define an ISO/IEC 18013-5 mdoc encoding for the StudentID Attestation.

The StudentID Attestation defined in this Rulebook is specified for SD-JWT VC-based issuance and presentation. If a future version of this Rulebook defines an ISO/IEC 18013-5-compliant mdoc representation, that version SHALL define a unique document type, namespaces, attribute identifiers, CBOR encoding rules, and illustrative mdoc examples.

## 3.2 SD-JWT VC-based encoding

The StudentID Attestation SHALL be issued as an SD-JWT VC.

The Verifiable Credential Type (`vct`) for this attestation type is:

```text
VerifiableStudentID
```

The credential claims defined in this section SHALL follow SD-JWT VC and HAIP conventions where applicable. Claim names are either IANA-registered JWT claims, public names, or private names specific to this attestation type.

For all claims, this Rulebook specifies whether an Attestation Provider MUST, MAY, or MUST NOT make the claim selectively disclosable.

### 3.2.1 IANA-registered and standard JWT / SD-JWT VC claims

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Reference/Notes** | **Disclosable** |
|---------------------|--------------------------|---------------------|---------------------|-----------------|
| `iss` | `iss` | string | JWT issuer identifier. | MUST NOT |
| `iat` | `iat` | integer | Issued-at timestamp. | MUST NOT |
| `nbf` | `nbf` | integer | Not-before timestamp, where used. | MUST NOT |
| `exp` | `exp` | integer | Expiration timestamp. SHOULD reflect the end of the applicable student-status validity period. | MUST NOT |
| `jti` | `jti` | string | Unique credential instance identifier, where used. | MUST NOT |
| `cnf` | `cnf` | object | Holder binding confirmation claim, where used. | MUST NOT |
| `status` | `status` | object | Status or revocation information, where used. | MUST NOT |
| `vct` | `vct` | string | SD-JWT VC type. Value SHALL be `VerifiableStudentID`. | MUST NOT |

### 3.2.2 Public or reusable claims

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Reference/Notes** | **Disclosable** |
|---------------------|--------------------------|---------------------|---------------------|-----------------|
| `firstName` | `firstName` | string | Student given name. May be mapped to OIDC `given_name` in implementations that use OIDC naming conventions. | MUST |
| `familyName` | `familyName` | string | Student family name. May be mapped to OIDC `family_name` in implementations that use OIDC naming conventions. | MUST |
| `displayName` | `displayName` | string | Display name formatted for user interfaces. | MAY |
| `commonName` | `commonName` | string | Alternate display or preferred name. | MAY |
| `dateOfBirth` | `dateOfBirth` | string | Date of birth formatted as ISO 8601 date, where disclosed. | MAY |
| `mail` | `mail` | string | Email address. | MAY |

### 3.2.3 Private claims specific to the StudentID Attestation

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Notes** | **Disclosable** |
|---------------------|--------------------------|---------------------|-----------|-----------------|
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

### 3.2.4 Example JWT claim set

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

### 3.2.5 Example issued SD-JWT

The following is a non-normative placeholder example. A production SD-JWT SHALL be generated by the issuer using the applicable signing algorithm, disclosure construction, holder binding, and SD-JWT VC rules.

```text
<issuer-signed-sd-jwt>~<disclosure-1>~<disclosure-2>~<disclosure-n>~<holder-binding-jwt>
```

### 3.2.6 Example human-readable disclosed payload

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

## 3.3 W3C Verifiable Credentials Data Model-based encoding

This version of the Rulebook does not define a W3C Verifiable Credentials Data Model encoding for the StudentID Attestation.

If a future version defines a W3C VCDM representation, that version SHALL define the credential context, type, credential subject structure, proof type, selective disclosure mechanism, and presentation requirements.

## 4 Attestation usage

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

## 5 Trust anchors

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

## 6 Revocation

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

## 7 Compliance

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

## 8 References

| **Item Reference** | **Standard name/details** |
|--------------------|---------------------------|
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
