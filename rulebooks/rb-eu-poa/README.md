# Attestation Rulebook for attestations of type EU Power of Attorney (EU PoA)

Category: QEAA, PuB-EAA or non-qualified EAA, as stated in `attestation_legal_category`

* Author(s):
    * Erwin Nieuwlaar, [KVK](https://kvk.nl)
    * Astrid Verhallen, [Infogreffe](https://www.infogreffe.fr/)

| Version | Date | Description |
| --- | --- | --- |
| 0.2 | 2026-10-05 | Restructured onto the generic WE BUILD attestation rulebook template (11 chapters). No normative content removed. |

**Written against:** ARF version 3.0.0, WE BUILD template version 1.0 (generic)

**Feedback:**
Main feedback channel: [GitHub issues](https://github.com/webuild-consortium/eudi-wallet-rulebooks-and-schemas/issues)

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

This attestation represents a legally valid Power of Attorney (EU PoA) issued within the European Union.
It embodies:

- The identification of a principal (natural person acting on behalf of a legal entity)
- The identification and registration details of the company
- The designation of an attorney (delegate)
- The defined scope of representation
- The validity period
- The applicable law
- The signing details
- A reference to the EU Company Certificate (EUCC) if applicable

This attestation enables a relying party to verify that an attorney (delegate) has been granted specific powers of representation by a principal acting on behalf of a legal entity. The specific powers are limited to 6: the formation of companies; changes to the instrument of constitution of companies and the statutes if contained in a separate instrument; registration and closure of branches of the company; all legal transactions regarding cross-border conversions involving the company; all legal transactions regarding cross-border mergers involving the company; and all legal transactions regarding cross-border divisions involving the company. The EU PoA complements the EU Company Certificate (EUCC) by providing granular delegation information beyond the company's registered legal representatives.

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

This document uses terminology specified in [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/eli/reg/2024/1183/oj/eng).

In addition to the attributes definition necessary to understand the data schema, it is important to understand:

| Term | Definition in WE BUILD Context |
| --- | --- |
| Principal | A natural person who acts on behalf of a legal entity and grants authority to an attorney (delegate) through a Power of Attorney. |
| Attorney (Delegate) | A natural person designated by the principal to act on behalf of the legal entity within the defined scope of representation. |
| Power of Attorney | A legal instrument by which one person (the principal) authorises another person (the attorney) to act on their behalf in specified legal or business matters. |
| Scope of Representation | The defined set of powers and authorities granted to the attorney under the Power of Attorney. |

## 2 Compliance

### 2.1 Compliance statement

This Rulebook complies with the applicable requirements of Topic 12, Attestation
Rulebooks, in Annex 2 of the Architecture and Reference Framework, version 3.0.0. It
uses the terminology of Annex 1 of the ARF.

#TODO

### 2.2 Regulatory basis

The EU PoA attestation may be issued as a QEAA, a PuB-EAA or a non-qualified EAA, as stated in
`attestation_legal_category` (section 3.2). The paragraph for that category applies.

**QEAA**

This attestation includes the data required by Annex V of Regulation (EU) 2024/1183,
points a, b, c, e and h, satisfying EW-DM-12-014, EW-DM-12-016, EW-DM-12-019, EW-DM-12-021
and EW-DM-12-023 respectively. It is issued by a qualified trust service provider.

**PuB-EAA**

This attestation includes the data required by Annex VII of Regulation (EU) 2024/1183,
points a, b, c, e and h, satisfying EW-DM-12-014, EW-DM-12-017, EW-DM-12-019, EW-DM-12-021
and EW-DM-12-023 respectively. It is issued by or on behalf of a public sector body
responsible for an authentic source.

**Non-qualified EAA**

This attestation is not a qualified electronic attestation of attributes. The data
described in Annex V points b, c and e of Regulation (EU) 2024/1183 is addressed as
required by EW-DM-12-018 and as recommended by EW-DM-12-020 and EW-DM-12-022. Where a
recommendation is not followed, the reason is stated below.

### 2.3 Traceability

Every applicable requirement mapped to the section that satisfies it. Requirements
marked not applicable carry a stated reason.

| Requirement | Legacy ID | Applies | Satisfied in section | Note |
| --- | --- | --- | --- | --- |
| EW-DM-12-001 | ARB_01a | yes | 5 | SD-JWT VC only |
| EW-DM-12-002 | ARB_01b | yes | 5.1 | SD-JWT VC following the HAIP profile |
| EW-DM-12-003 | ARB_02 | no |  | mdoc not included, see section 5.2 |
| EW-DM-12-005 | ARB_04 | no |  | No W3C VCDM encoding is defined |
| EW-DM-12-006 | ARB_05 | yes | 5.1 | `uri:eu.eudi.eu-poa.1` |
| EW-DM-12-007 | ARB_06 | yes | 3 | Attributes defined independently of encoding |
| EW-DM-12-008 | ARB_06a | no |  | No mdoc encoding is defined |
| EW-DM-12-009 | ARB_06b | yes | 5.1 | SD-JWT VC claim naming |
| EW-DM-12-010 | ARB_07 | yes | 3 | Semantic references are marked TBD in this version |
| EW-DM-12-012 | ARB_09 | yes | 3, 4 | Mandatory, optional and conditional stated per attribute |
| EW-DM-12-013 | ARB_10 | no |  | No domestic namespace is defined |
| EW-DM-12-014 | ARB_11 | yes | 3.2 | `attestation_legal_category` where issued as a QEAA or PuB-EAA |
| EW-DM-12-015 | ARB_12 | yes | 3.2 | `attestation_legal_category` where issued as a non-qualified EAA |
| EW-DM-12-016 / EW-DM-12-017 / EW-DM-12-018 | ARB_13 / ARB_14 / ARB_15 | yes | 2.2, 4.1 | Point b through `issuing_authority` and `issuing_country` |
| EW-DM-12-019 / EW-DM-12-020 | ARB_16 / ARB_17 | yes | 2.2, 3.2 | Point c through the principal and attorney attributes |
| EW-DM-12-021 / EW-DM-12-022 | ARB_18 / ARB_19 | yes | 2.2, 3.2, 4.1 | Point e through the validity period and `expiry_date` |
| EW-DM-12-023 / EW-DM-12-024 | ARB_20 / ARB_21 | yes | 4.2, 10 | `trust_anchor` metadata; chapter 10 is marked TODO by the authors |
| EW-DM-12-029 | ARB_25 | yes | 3.2 | Legal category attribute; see the note in section 4.1 |
| EW-DM-12-030 | ARB_26 | pending | 10 | Marked TODO by the authors |
| EW-DM-12-031 | ARB_27 | pending | 9.1 | The usage chapter is marked TODO by the authors |
| EW-DM-12-032 | ARB_28 | no |  | `cryptographically_bound_to` is not used |
| EW-DM-12-034 | ARB_30 | yes | 5.1 | Selective disclosure stated per claim |
| EW-DM-12-035 | ARB_31 | no |  | No Claim Selective Disclosure Metadata document is used |
| EW-DM-12-038 | ARB_34 | pending | 7.1 | Template default recorded until the authors complete chapter 9 |

## 3 Attestation attributes

Attributes are defined here in an encoding-independent manner (EW-DM-12-007). The
encoding of each attribute is given in chapter 5.

### 3.1 Introduction

The EU Power of Attorney attestation SHALL be represented as a single flat object.

The attestation attributes are defined in the sections below. The attribute identifiers SHALL be used in requests and responses. There SHALL be at most one attribute with the same attribute identifier in each attestation.

The optionality column specifies whether the presence of the attribute in an attestation is mandatory (M) or optional (O).

NOTE: If an attribute is indicated as mandatory, this solely means that the Issuer SHALL ensure that this element is present in the attestation. It does not imply that a Relying Party is required to request such an attribute when interacting with the Wallet Instance. Neither does it imply that the User cannot refuse to release a mandatory attribute if requested.

The encoding format column indicates how the data elements SHALL be encoded, using the CDDL representation types defined in [RFC 8610].

### 3.2 Mandatory attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| attestation_legal_category | TBD | One of EAA, Pub-EAA or QEAA | string | QEAA |
| date_of_execution | TBD | Date the PoA was executed | string (date) | 2026-01-15 |
| euid_reference | TBD | EUID reference | string | NLNHR.12345678 |
| principal_full_name | TBD | Legal full name of the principal | string | Frouke Janssen |
| principal_date_of_birth | TBD | Date of birth of the principal | string (date) | 1980-03-22 |
| company_statutory_full_name | TBD | Registered legal name of the company | string | FictiveCo B.V. |
| company_business_register_name | TBD | Name of the business register | string | Kamer van Koophandel |
| company_jurisdiction | TBD | Country of incorporation | string | NL |
| attorney_full_name | TBD | Legal full name of the attorney | string | Maria Schmidt |
| scope_of_representation_powers | TBD | Granted powers | array\<string\> | ["The formation of companies", "Registration and closure of branches of the Company"] |
| validity_period_valid_from | TBD | Start date of validity | string (date) | 2026-01-15 |
| validity_period_valid_until | TBD | End date of validity | string (date) | 2027-01-15 |
| applicable_law_jurisdiction | TBD | Governing Member State law | string | NL |
| signing_place | TBD | Place of signing | string | Hardenberg |
| signing_date | TBD | Date of signing | string (date) | 2026-01-15 |

### 3.3 Optional attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| principal_identification_document_kind | TBD | Type of ID document of the principal | string | passport |
| principal_identification_document_number | TBD | ID document number of the principal | string | NZ1234567 |
| principal_place_of_birth | TBD | Place of birth of the principal | string | Utrecht |
| principal_full_address | TBD | Residential address of the principal | string | Herengracht 100, 1015 AA Amsterdam, Netherlands |
| company_business_register_location | TBD | Location of the business register | string | The Hague |
| company_kind_of_legal_entity | TBD | Legal form (e.g. GmbH, SARL, SA) | string | B.V. |
| company_registered_office | TBD | Registered office address | string | Keizersgracht 200, 1016 DW Amsterdam, Netherlands |
| attorney_date_of_birth | TBD | Date of birth of the attorney | string (date) | 1985-07-10 |
| attorney_identification_document_kind | TBD | Type of ID document of the attorney | string | national_id_card |
| attorney_identification_document_number | TBD | ID document number of the attorney | string | DE9876543 |
| attorney_place_of_birth | TBD | Place of birth of the attorney | string | Groningen |
| attorney_full_address | TBD | Residential address of the attorney | string | Friesestraatweg 3157, 7772CP Groningen, Netherlands |
| scope_of_representation_power_of_substitution | TBD | Whether substitution is allowed | string | not_allowed |

### 3.4 Conditional attributes

No conditional attributes are defined for this attestation.

## 4 Metadata

Metadata describes the attestation rather than its subject.

### 4.1 Mandatory metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| expiry_date | TBD | Date (and if possible time) when the attestation will expire. Does not need to be an attribute and can be covered by credential format metadata, such as for example the "exp" field on the SD-JWT format (TBD if we can remove this attribute and use the "exp" field only). | date | 2027-01-15 |
| issuing_authority | TBD | Name of the administrative authority that issued the EU PoA, or the ISO 3166 alpha-2 country code of the respective Member State if there is no separate authority entitled to issue the EU PoA. | string | Kamer van Koophandel |
| issuing_country | TBD | Alpha-2 country code, as specified in ISO 3166-1, of the country or territory of the provider of the attestation. | string | NL |

**Legal category.** This Rulebook retains the `attestation_legal_category` attribute.
Section 4.1 of the generic template replaces it with the `category` attribute of
[ETSI TS 119 472-1]. EW-DM-12-029, legacy ARB_25, of ARF version 3.0.0 is a SHALL that
still requires the legal category attribute, so the template and the ARF disagree. The
attribute is left as written and the deviation is recorded for the rulebook quality
assurance group.

### 4.2 Optional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| location_status | TBD | The location of validity status information where the providers revoke attestations. This attribute is required when the validity time period of the attestation exceeds 24 hours. | string | https://issuer.example.com/status/1 |
| trust_anchor | TBD | This attribute indicates at least the URL at which a machine-readable version of the trust anchor to be used for verifying the EU PoA can be found or looked up. | string | https://issuer.example.com/trust-anchor |

### 4.3 Conditional metadata

No conditional metadata are defined for this attestation.

### 4.4 Code lists

| **Field name** | **Allowed values** | **Meaning** | **Source / vocabulary** | **Notes / extensibility** |
| --- | --- | --- | --- | --- |
| `principal_identification_document_kind` / `attorney_identification_document_kind` | `passport`, `national_id_card`, `residence_permit`, `driving_license` | Type of identification document presented by the principal or attorney | EU PoA attestation definition |  |
| `scope_of_representation_power_of_substitution` | `allowed`, `not_allowed`, `limited` | Whether the attorney may delegate the granted powers to a third party | EU PoA attestation definition | If `limited`, additional limitation details MUST be included in `scope_of_representation_powers` |
| `scope_of_representation_powers` | `The formation of companies`, `Changes to the instrument of constitution of companies and the statutes if contained in a separate instrument`, `Registration and closure of branches of the Company`, `All legal transactions regarding cross-border conversions involving the Company`, `All legal transactions regarding cross border mergers involving the Company`, `All legal transactions regarding cross border divisions involving the Company` | The specific powers granted to the attorney | EU PoA attestation definition |  |

### 4.5 Integrity rules

| **Rule ID** | **Rule statement** | **Why it exists** | **Where enforced** | **Verifier / issuer behavior on failure** |
| --- | --- | --- | --- | --- |
| `IR-01` | `validity_period_valid_until` MUST be later than `validity_period_valid_from`. | Prevents nonsensical validity periods where the PoA would expire before it becomes effective. | Issuer business rules, schema validation, and verifier business validation. | Issuer SHALL reject the PoA; verifier SHALL treat the attestation as invalid. |
| `IR-02` | `date_of_execution` MUST be equal to or earlier than `validity_period_valid_from`. | Ensures the PoA was executed before or on the date it becomes effective. A PoA cannot take effect before it was executed. | Issuer business rules, schema validation, and verifier business validation. | Issuer SHALL reject the PoA; verifier SHALL treat the attestation as invalid. |
| `IR-03` | The principal must have legal authority to act on behalf of the company. | Prevents invalid delegation chains where a person without authority grants powers to an attorney. | Issuer business rules (verified during issuance). | Issuer SHALL reject issuance if principal authority cannot be established. |
| `IR-04` | If `scope_of_representation_power_of_substitution` = `limited`, additional limitation details MUST be included in `scope_of_representation_powers`. | Ensures that when substitution is restricted, the exact limitations are clearly specified and verifiable. | Issuer business rules and schema validation. | Issuer SHALL reject the PoA if limitation details are missing; verifier SHALL treat the scope as ambiguous and request clarification. |

## 5 Formats

| Format | Supported | Identifier | Specification | Notes |
| --- | --- | --- | --- | --- |
| ISO/IEC 18013-5 mdoc | no |  | [ISO/IEC 18013-5] | Not included in this version, see section 5.2 |
| SD-JWT VC | yes | `vct` `uri:eu.eudi.eu-poa.1` | [SD-JWT VC], [HAIP] | SHALL follow the HAIP profile, see section 5.1 |
| W3C VCDM | no |  | [W3C VCDM v2.0] | Not defined in this version |

### 5.1 SD-JWT VC-based encoding

The EU PoA attestation uses the SD-JWT VC format to allow for selective disclosure of PoA attributes.

**Verifiable Credential Type (`vct`):** `uri:eu.eudi.eu-poa.1`

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Reference/Notes** | **Disclosable** |
| --- | --- | --- | --- | --- |
| attestation_legal_category | attestation_legal_category | string | One of EAA, Pub-EAA, QEAA as defined by eIDAS 2 | MUST NOT |
| issuing_authority | iss | string | RFC 7519 / Section 4.1 | MUST NOT |
| expiry_date | exp | number | RFC 7519 / Section 4.1 (Unix timestamp) | MUST NOT |
| issuing_country | issuing_country | string | ISO 3166-1 alpha-2 | MUST NOT |
| date_of_execution | date_of_execution | string | ISO 8601 (YYYY-MM-DD) | MUST |
| euid_reference | euid_reference | string | EUID | MUST |
| principal_full_name | principal_full_name | string |  | MUST |
| principal_date_of_birth | principal_date_of_birth | string | ISO 8601 (YYYY-MM-DD) | MUST |
| principal_identification_document_kind | principal_identification_document_kind | string | See code list in Section 4.4 | MUST |
| principal_identification_document_number | principal_identification_document_number | string |  | MUST |
| principal_place_of_birth | principal_place_of_birth | string |  | MUST |
| principal_full_address | principal_full_address | string |  | MUST |
| company_statutory_full_name | company_statutory_full_name | string |  | MUST |
| company_business_register_name | company_business_register_name | string |  | MUST |
| company_business_register_location | company_business_register_location | string |  | MUST |
| company_kind_of_legal_entity | company_kind_of_legal_entity | string |  | MUST |
| company_jurisdiction | company_jurisdiction | string | ISO 3166-1 alpha-2 | MUST |
| company_registered_office | company_registered_office | string |  | MUST |
| attorney_full_name | attorney_full_name | string |  | MUST |
| attorney_date_of_birth | attorney_date_of_birth | string | ISO 8601 (YYYY-MM-DD) | MUST |
| attorney_identification_document_kind | attorney_identification_document_kind | string | See code list in Section 4.4 | MUST |
| attorney_identification_document_number | attorney_identification_document_number | string |  | MUST |
| attorney_place_of_birth | attorney_place_of_birth | string |  | MUST |
| attorney_full_address | attorney_full_address | string |  | MUST |
| scope_of_representation_powers | scope_of_representation_powers | array\<string\> | See code list in Section 4.4 | MUST |
| scope_of_representation_power_of_substitution | scope_of_representation_power_of_substitution | string | See code list in Section 4.4 | MUST |
| validity_period_valid_from | validity_period_valid_from | string | ISO 8601 (YYYY-MM-DD) | MUST NOT |
| validity_period_valid_until | validity_period_valid_until | string | ISO 8601 (YYYY-MM-DD) | MUST NOT |
| applicable_law_jurisdiction | applicable_law_jurisdiction | string | ISO 3166-1 alpha-2 | MUST |
| signing_place | signing_place | string |  | MUST |
| signing_date | signing_date | string | ISO 8601 (YYYY-MM-DD) | MUST |

#TODO: Provide an example of the issued SD-JWT (in Base64 encoding).

### 5.2 ISO/IEC 18013-5-compliant encoding

ISO/IEC 18013-5 (also called mdoc) is not currently included in this rulebook. Should a use case arise that requires offline proximity presentation for the EU PoA, support for this standard may be added in a future version.

### 5.3 W3C Verifiable Credentials Data Model-based encoding

## 6 Protocols

### 6.1 Issuance

This attestation is issued using OpenID for Verifiable Credential Issuance
[OpenID4VCI], as profiled by [HAIP].

### 6.2 Presentation

This attestation is presented using OpenID for Verifiable Presentations [OpenID4VP].
Only remote presentation is in scope, consistent with chapter 5, which records the
mdoc encoding as out of scope.

## 7 Issuance

### 7.1 Binding

| Field | Value | Source |
| --- | --- | --- |
| Device-bound | MAY | EW-DM-12-038 |
| Cryptographically bound to | none | EW-DM-12-032 |
| Relying Party must also verify a PID | pending | EW-DM-12-031 |
| Binding subject | natural person (the attorney), acting on behalf of a legal person |  |

The usage chapter of the previous version is marked TODO by its authors. The rows above record the
template defaults until the authors complete it.

### 7.2 Issuance Policy

General obligations on Attestation Providers are out of scope of this Rulebook. They
are specified in Topic 10 of Annex 2 of the ARF, in the applicable Implementing
Regulations, and in [ETSI TS 119 471]. This Rulebook states only obligations specific
to this attestation type.

### 7.3 Lifecycle management

The issuer sets the validity period of the attestation and reissues it when the
underlying facts change, revoking the superseded attestation as described in chapter 8.

### 7.4 Embedded disclosure policy

This attestation defines no embedded disclosure policy.

## 8 Revocation

#TODO

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

#TODO: *Briefly describe the primary use cases or scenarios for which this attestation type is intended.*

### 9.2 Presentation modes

Remote presentation is in scope. Proximity presentation is not in scope, consistent
with chapter 5, which records the mdoc encoding as not included.

### 9.3 Transactional data

This Rulebook defines no transactional data.

## 10 Trust Framework

The trust anchor is obtained as described in the branch below that corresponds to the
legal category under which the attestation was issued.

**PID, QEAA, PuB-EAA and attestations resolved via Trusted Lists**

The trust anchor is obtained from a Trusted List, as described in section 6.6.3.6 of the
ARF main document. The Provider may sign the attestation with an intermediate signing
certificate, in which case the trust anchor is used to verify that certificate rather
than the attestation directly.

#TODO

**Trust anchor location**

The attribute or metadata carrying the trust anchor location contains at least the URL
at which a machine-readable version can be found or looked up.

## 11 References

| **Item Reference** | **Standard name/details** |
| --- | --- |
| [European Digital Identity Regulation] | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework |
| [ISO/IEC 18013-5] | ISO/IEC 18013-5, Personal identification --- ISO-compliant driving licence - Part 5: Mobile driving licence (mDL) application, First edition, 2021-09 |
| [RFC 3339] | RFC 3339  - Date and Time on the Internet: Timestamps, G. Klyne et al., July 2002 |
| [RFC 8610] | RFC 8610  - Concise Data Definition Language (CDDL): A Notational Convention to Express Concise Binary Object Representation (CBOR) and JSON Data Structures, H. Birkholz et al., June 2019 |
| [RFC 8943] | RFC 8943  - Concise Binary Object Representation (CBOR) Tags for Date, M. Jones et al., November 2020 |
| [RFC 8949] | RFC 8949 - Concise Binary Object Representation (CBOR), C. Bormann et al., December 2020 |
| [SD-JWT VC] | SD-JWT-based Verifiable Credentials (SD-JWT VC). Available: <https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/>, version draft-ietf-oauth-sd-jwt-vc-09 |
| [Topic 7] | ARF Annex 2 - Topic 7 - Attestation revocation and revocation checking Available: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a237-topic-7-attestation-revocation-and-revocation-checking> |
| [Topic 12] | ARF Annex 2 - Topic 12 - Attestation Rulebooks, Available: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a2312-topic-12-attestation-rulebooks> |
