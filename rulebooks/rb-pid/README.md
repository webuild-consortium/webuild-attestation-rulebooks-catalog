# Attestation Rulebook for attestations of type Personal Identification Data (PID)

Category: PID

*  Authors
    * Jonas Toennis , [Brønnøysund Registry Center](https://www.brreg.no)

* Previous authors
  * David Bakker, On behalf of the ARF working group 

| Version | Date        | Description                                                                                                                                                                                                                                                                                                                                                                                                                      |
|---------|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0.1.3   | 27 Oct 2025 | Transferred main structure and content from [EUDI repository](https://github.com/eu-digital-identity-wallet/eudi-doc-attestation-rulebooks-catalog/blob/main/rulebooks/pid/pid-rulebook.md) and modified template to closer align to [EUDI template](https://github.com/eu-digital-identity-wallet/eudi-doc-attestation-rulebooks-catalog/blob/main/template/attestation-rulebook-template.md). First specific draft for WE BUILD |
| 0.9.0   | 2025-12-12  | Feedback of WE BUILD WP 4 Task 2 implemented                                                                                                                                                                                                                                                                                                                                                                                      |
| 0.9.9   | 2026-05-21  | Alignment to the ARF version 2.8.0 defined [PID version 1.5  ](https://github.com/eu-digital-identity-wallet/eudi-doc-attestation-rulebooks-catalog/blob/main/rulebooks/pid/pid-rulebook.md)                                                                                                                                                                                                                                     |
| 1.0.0   | 2026-05-22  | Minor language and consistency adjustments                                                                                                                                                                                                                                                                                                                                                                                       |
| 1.1.0   | 2026-09-11  | Restructured onto the generic WE BUILD attestation rulebook template (11 chapters). No normative content removed. Requirement references renumbered to the ARF v3.0.0 identifiers. |

**Written against:** ARF version 3.0.0, WE BUILD template version 1.0 (generic)

**Feedback:** [GitHub issues](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/issues), or contact Work Package 4 in WE BUILD.

## Table of contents

- [1 Introduction](#1-introduction)
   * [1.1 Document scope and purpose](#11-document-scope-and-purpose)
   * [1.2 Document structure](#12-document-structure)
   * [1.3 Key words](#13-key-words)
   * [1.4 Terminology](#14-terminology)
- [2 Certification](#2-certification)
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
   * [7.2 Lifecycle management](#72-lifecycle-management)
   * [7.3 Issuance Policy](#73-issuance-policy)
   * [7.4 Embedded disclosure policy](#74-embedded-disclosure-policy)
- [8 Revocation](#8-revocation)
- [9 Presentation](#9-presentation)
   * [9.1 Relying Party policy](#91-relying-party-policy)
   * [9.2 Presentation modes](#92-presentation-modes)
   * [9.3 Transactional data](#93-transactional-data)
- [10 Trust Framework](#10-trust-framework)
- [11 References](#11-references)


## 1 Introduction

### 1.1 Document scope and purpose


This document is the natural person identification data (PID) Rulebook
and is part of the Architecture Reference Framework (ARF). It specifies
how the mandatory and optional person identification data for the natural
person, as defined in Tables 1 and 2 in the Annex of the Commission Implementing
Regulation on PID and EAA [CIR 2024/2977], as well as the metadata specified in
Table 5 of that CIR, will be encoded within the EUDI Wallet ecosystem.
Additionally, this document specifies further optional PID attributes that are
not included in the CIR.

This document also specifies how a PID and all attributes in it are encoded if
the PID complies with [ISO/IEC 18013-5] and if it complies with [SD-JWT VC].

This PID Rulebook should be read in conjunction with the high-level requirements for PIDs in [Topic 3](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/annexes/annex-2/annex-2.02-high-level-requirements-by-topic.md#a232-topic-3---pid-rulebook) in Annex 2 of the Architecture Reference Framework. In particular, the values to be used for the namespace and document type for [ISO/IEC 18013-5]-compliant PIDs and for the vct claim in [SD-JWT VC]-compliant PIDs are defined in Topic 3.

Person identification data for the legal person is out of scope of this document.

**Relationship to the ARF PID Rulebook.** This Rulebook derives from the PID Rulebook
in Annex 3.01 of the ARF and diverges from it in the following ways. The attribute and
metadata tables carry links to the WE BUILD semantic vocabulary. An explicit status
list based revocation mapping is specified for SD-JWT VC, in line with the
[WE BUILD Architecture Decision Record on attestation revocation](https://github.com/webuild-consortium/wp4-architecture/blob/main/adr/attestation-revocation-mechanism.md),
see chapter 8. Chapters 6, 7, 9
and 10 are expanded relative to the ARF PID Rulebook, in particular the deployment
profile in chapter 10.

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


This document uses the terminology specified in [Annex 1](https://eudi.dev/3.0.0/annexes/annex-1/annex-1-definitions/) of the ARF.

## 2 Certification

### 2.1 Compliance statement

> This Rulebook complies with the applicable requirements of Topic 12, Attestation
> Rulebooks, in Annex 2 of the Architecture and Reference Framework, version 3.0.0.
> It uses the terminology of Annex 1 of the ARF.

This Rulebook also complies with all applicable requirements in
[Topic 12 (Attestation Rulebooks)](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/annexes/annex-2/annex-2.02-high-level-requirements-by-topic.md#a239-topic-12---attestation-rulebooks)
in Annex 2 of the Architecture Reference Framework.

The attributes specified in this Rulebook comply with
[CIR 2024/2977](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402977).

Further requirements in this Rulebook comply with or reference the applicable
requirements in the ARF and the relevant Implementing Acts.

This Rulebook follows the generic WE BUILD attestation rulebook template, which is
aligned to the
[EC template for Attestation Rulebooks](https://github.com/eu-digital-identity-wallet/eudi-doc-attestation-rulebooks-catalog/blob/main/template/attestation-rulebook-template.md)
version 1.5.

### 2.2 Regulatory basis

> This Rulebook specifies how the mandatory and optional person identification data
> defined in Tables 1 and 2 of the Annex to CIR (EU) 2024/2977, and the metadata
> defined in Table 5 of that CIR, are encoded within the EUDI Wallet ecosystem.

### 2.3 Traceability

Every applicable requirement mapped to the section that satisfies it. Requirements
marked not applicable carry a stated reason.

| Requirement | Legacy ID | Applies | Satisfied in section | Note |
| --- | --- | --- | --- | --- |
| EW-DM-12-001 | ARB_01a | no | | W3C VCDM is permitted for non-qualified EAA only; PID is not an EAA |
| EW-DM-12-002 | ARB_01b | yes | 5 | SD-JWT VC per the HAIP profile |
| EW-DM-12-003 | ARB_02 | yes | 5 | mdoc supported; proximity presentation is in scope |
| EW-DM-12-005 | ARB_04 | no | | W3C VCDM is not a supported format for this attestation |
| EW-DM-12-006 | ARB_05 | yes | 5 | doctype `eu.europa.ec.eudi.pid.1`, vct `urn:eudi:pid:1` |
| EW-DM-12-007 | ARB_06 | yes | 3 | Attributes defined independently of encoding |
| EW-DM-12-008 | ARB_06a | yes | 5 | mdoc attribute identifiers and namespace |
| EW-DM-12-009 | ARB_06b | yes | 5 | SD-JWT VC claim naming |
| EW-DM-12-010 | ARB_07 | yes | 3 | Attributes taken from CIR 2024/2977 |
| EW-DM-12-012 | ARB_09 | yes | 3, 4 | Presence stated per attribute and per metadata item |
| EW-DM-12-013 | ARB_10 | yes | 5 | Domestic namespace per PID_06 of Topic 3 |
| EW-DM-12-014 | ARB_11 | no | | Annex V and VII point a apply to QEAA and PuB-EAA; PID is neither |
| EW-DM-12-015 | ARB_12 | no | | Applies to non-qualified EAA only |
| EW-DM-12-016 / EW-DM-12-017 / EW-DM-12-018 | ARB_13 / ARB_14 / ARB_15 | no | | Point b, by category; PID is not an EAA |
| EW-DM-12-019 / EW-DM-12-020 | ARB_16 / ARB_17 | no | | Point c, by category; PID is not an EAA |
| EW-DM-12-021 / EW-DM-12-022 | ARB_18 / ARB_19 | no | | Point e, by category; PID is not an EAA |
| EW-DM-12-023 / EW-DM-12-024 | ARB_20 / ARB_21 | yes | 4.2, 10 | `trust_anchor` metadata and the trust framework |
| EW-DM-12-029 | ARB_25 | yes | 4.1 | Legal category attribute; see the deviation recorded in section 4.1 |
| EW-DM-12-030 | ARB_26 | no | | Trust anchor publication for non-qualified EAA |
| EW-DM-12-031 | ARB_27 | no | | Whether the Relying Party must also verify a PID; this attestation is the PID |
| EW-DM-12-032 | ARB_28 | no | | `cryptographically_bound_to` is not used by this attestation |
| EW-DM-12-034 | ARB_30 | yes | 3, 5 | Selective disclosure stated per claim |
| EW-DM-12-035 | ARB_31 | no | | No Claim Selective Disclosure Metadata document is used |
| EW-DM-12-038 | ARB_34 | yes | 7.1 | Device binding |

## 3 Attestation attributes

Attributes are defined here in an encoding-independent manner (EW-DM-12-007). The
encoding of each attribute per format is given in chapter 5.

### 3.1 Introduction


Sections [2.2](#22-mandatory-attributes-specified-in-cir-20242977), [2.3](#23-optional-attributes-specified-in-cir-20242977), [2.4](#24-condition-attributes), [2.5](#25-mandatory-metadata-specified-in-cir-20242977) and [2.6](#26-optional-metadata-specified-in-cir-20242977) of this chapter list the mandatory and optional
PID attributes and PID metadata defined in CIR 2024/2977. [Section 2.7](#27-additional-optional-attributes-specified-in-this-rulebook) lists the optional PID attributes additionally defined in this PID Rulebook.

Note that, when requesting PID attributes from a Wallet Unit, a Relying Party is not required to request all mandatory attributes. Also, a user is allowed to refuse to present a mandatory attribute, if it is requested by a Relying Party.

The data identifiers and definitions given in Sections 2.2, 2.3, 2.4, and 2.5
are identical to those in CIR 2024/2977, except where explicitly indicated that
some further explanations have been added in this Rulebook.

All data identifiers and definitions in this chapter are independent of any
encoding used. Consequently,

- the data identifiers in these tables are not necessarily the same as the
attribute identifiers used for PIDs complying with [ISO/IEC 18013-5]. [Chapter 3.1](#31-isoiec-18013-5-compliant-encoding) specifies the attribute
identifiers to be used for PIDs in [ISO/IEC 18013-5] format
- the data identifiers in these tables are not necessarily the same as the claim
names used for PIDs complying with [SD-JWT VC]. [Section 3.2](#32-sd-jwt-vc-based-encoding-of-pid) specifies the claim names to be used for such PIDs.

The machine-readable schema artefacts for this attestation are:

| Format | Identifier | Schema artefact | Sample |
| --- | --- | --- | --- |
| ISO/IEC 18013-5 mdoc | doctype `eu.europa.ec.eudi.pid.1` | `data-schemas/mdoc/ds002-pid-mdoc.json` | `data-schemas/mdoc/sample-data/ds002-pid-mdoc-sample.json` |
| SD-JWT VC | `vct` `urn:eudi:pid:1` | `data-schemas/sd-jwt/ds002-pid-sd-jwt.json` | `data-schemas/sd-jwt/sample-data/ds002-pid-sd-jwt-sample.json` |

### 3.2 Mandatory attributes


| Data Identifier | Semantic Reference                                                                   | Definition                                                                                                                                                                                                                             | Example value |
|-----------------|--------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| family_name     | [familyName](https://w3id.org/ebwv#familyName)     | Current last name(s) or surname(s) of the user to whom the person identification data relates.                                                                                                                                         | 't Hart       |
| given_name      | [givenName](https://w3id.org/ebwv#givenName)       | Current first name(s), including middle name(s) where applicable, of the user to whom the person identification data relates.                                                                                                          | Jan Wijnand   |
| birth_date      | [dateOfBirth](https://w3id.org/ebwv#dateOfBirth)   | Day, month, and year on which the user to whom the person identification data relates was born.                                                                                                                                        | 12/02/1978    |
| birth_place     | [placeOfBirth](https://w3id.org/ebwv#placeOfBirth) | The country as an alpha-2 country code as specified in ISO 3166-1, or the state, province, district, or local area or the municipality, city, town, or village where the user to whom the person identification data relates was born. | Amsterdam     |
| nationality     | [citizenship](https://w3id.org/ebwv#citizenship)   | One or more alpha-2 country codes as specified in ISO 3166-1, representing the nationality of the user to whom the person identification data relates.                                                                                 | NL            |

### 3.3 Optional attributes

| \*\*Data Identifier\*\*        | \*\*Semantic Reference\*\*                                                                                                                                             | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Example value                                               |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| resident_address               | [domicile](https://w3id.org/ebwv#domicile).[fullAddress](https://w3id.org/ebwv#fullAddress)        | The full address of the place where the user to whom the person identification data relates currently resides or can be contacted (street name, house number, city etc.).                                                                                                                                                                                                                                                                                                    | Rietveld 1, 2312 JD, Leiden                                 |
| resident_country               | [domicile](https://w3id.org/ebwv#domicile).[adminUnitL1](https://w3id.org/ebwv#adminUnitL1)        | The country where the user to whom the person identification data relates currently resides, as an alpha-2 country code as specified in ISO 3166-1.                                                                                                                                                                                                                                                                                                                          | NL                                                          |
| resident_state                 | [domicile](https://w3id.org/ebwv#domicile).[adminUnitL2](https://w3id.org/ebwv#adminUnitL2)        | The state, province, district, or local area where the user to whom the person identification data relates currently resides.                                                                                                                                                                                                                                                                                                                                                | Zuid-Holland                                                |
| resident_city                  | [domicile](https://w3id.org/ebwv#domicile).[postName](https://w3id.org/ebwv#postName)              | The municipality, city, town, or village where the user to whom the person identification data relates currently resides.                                                                                                                                                                                                                                                                                                                                                    | Leiden                                                      |
| resident_postal_code           | [domicile](https://w3id.org/ebwv#domicile).[postCode](https://w3id.org/ebwv#postCode)              | The postal code of the place where the user to whom the person identification data relates currently resides.                                                                                                                                                                                                                                                                                                                                                                | 2312 JD                                                     |
| resident_street                | [domicile](https://w3id.org/ebwv#domicile).[thoroughfare](https://w3id.org/ebwv#thoroughfare)      | The name of the street where the user to whom the person identification data relates currently resides.                                                                                                                                                                                                                                                                                                                                                                      | Rietveld                                                    |
| resident_house_number          |                                                                                                                                                                        | The house number where the user to whom the person identification data relates currently resides, including any affix or suffix.                                                                                                                                                                                                                                                                                                                                             | 1                                                           |
| personal_administrative_number | [personalAdministrativeNumber](https://w3id.org/ebwv#personalAdministrativeNumber)                                                   | A value assigned to the natural person that is unique among all personal administrative numbers issued by the provider of person identification data. Where Member States opt to include this attribute, they shall describe in their electronic identification schemes under which the person identification data is issued, the policy that they apply to the values of this attribute, including, where applicable, specific conditions for the processing of this value. | 123456782                                                   |
| portrait                       | [portrait](https://w3id.org/ebwv#portrait)                                                                                           | [Facial image of the wallet user compliant with ISO 19794-5 or ISO 39794 specifications. Further clarification added in this PID Rulebook: The detailed format of the portrait is specified in requirement PID_03 in Annex 2, Topic 3.](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/annexes/annex-2/annex-2.02-high-level-requirements-by-topic.md#a232-topic-3---pid-rulebook)                               | \-                                                          |
| family_name_birth              | [birthName](https://w3id.org/ebwv#birthName)                                                                                         | Last name(s) or surname(s) of the user to whom the person identification data relates at the time of birth.                                                                                                                                                                                                                                                                                                                                                                  | Poepjes                                                     |
| given_name_birth               | [birthName](https://w3id.org/ebwv#birthName)                                                                                         | First name(s), including middle name(s), of the user to whom the person identification data relates at the time of birth.                                                                                                                                                                                                                                                                                                                                                    | Björn                                                       |
| sex                            | [gender](https://w3id.org/ebwv#gender)                                                                                               | Values shall be one of the following: 0 = not known; 1 = male; 2 = female; 3 = other; 4 = inter; 5 = diverse; 6 = open; 9 = not applicable. For values 0, 1, 2 and 9, ISO/IEC 5218 applies.                                                                                                                                                                                                                                                                                  | 1                                                           |
| email_address                  | [contactPoint](https://w3id.org/ebwv#contactPoint).[hasEmail](https://w3id.org/ebwv#email)         | Electronic mail address of the user to whom the person identification data relates, in conformance with [RFC 5322].                                                                                                                                                                                                                                                                                                                                                          | [wijnandthart@example.com](mailto:wijnandthart@example.com) |
| mobile_phone_number            | [contactPoint](https://w3id.org/ebwv#contactPoint).[hasTelephone](https://w3id.org/ebwv#telephone) | Mobile telephone number of the user to whom the person identification data relates, starting with the '+' symbol as the international code prefix and the country code, followed by numbers only.                                                                                                                                                                                                                                                                            | 31123456789                                                 |                                                                                                                                                                                                                                                         |

The following optional attributes are specified by this Rulebook rather than by
CIR 2024/2977.


| **Data Identifier**        | **Definition**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | **Example value**                       |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| issuance_date              | Date (and if possible time) when the person identification data was issued and/or the administrative validity period of the person identification data began. See also the clarification for expiry_date in [Section 2.5](#25-mandatory-metadata-specified-in-cir-20242977).                                                                                                                                                                                                                                                        | 19-12-2025                              |
| trust_anchor               | This attribute indicates at least the URL at which a machine-readable version of the trust anchor to be used for verifying the PID can be found or looked up. *Note: This attribute corresponds to the location meant in Annex V point h) or Annex VII point h) of the [European Digital Identity Regulation], which is mandatory for QEAAs. This PID Rulebook adds this as an optional attribute for PIDs as well, so PID Providers are able to ensure that PIDs can be validated by Relying Parties in the same manner as QEAAs.* | <https://example.com/trustanchors/pid/> |
| attestation_legal_category | This attribute indicates that a PID has indeed been issued as a PID. *Note: According to Annex V point a) and Annex VII point a) of the [European Digital Identity Regulation] an indication, at least in a form suitable for automated processing, that the attestation has been issued as a QEAA or Pub-EAA SHALL be defined. This PID Rulebook adds this as an optional attribute for PIDs as well, so PID Providers are able to ensure that PIDs can be validated by Relying Parties in the same manner as QEAAs.*              | PID                                     |

### 3.4 Conditional attributes

The PID defined in this rulebook does not contain any condition attributes.

## 4 Metadata

Metadata describes the attestation rather than its subject.

### 4.1 Mandatory metadata


| **Data Identifier** | **Definition**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | **Example value**                    |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| expiry_date         | Date (and if possible time) when the person identification data will expire. **Further clarification added in this PID Rulebook:** This attribute, as well as the optional issuance_date attribute specified in [Section 2.7](#27-additional-optional-attributes-specified-in-this-rulebook), pertains to the administrative validity period of the PID. It is up to the PID Provider to decide whether a PID has an administrative validity period. However, if present, it in general is different from the technical validity period of a PID. The technical validity period is a mandatory element of all PIDs (and also attestations) in the EUDI Wallet ecosystem. It typically is short, a few days or weeks at most, if not shorter, to mitigate challenges regarding tracking of users by malicious Relying Parties based on the repeated presentation of the same PID. On the other hand, the administrative validity period is typically at least a few years long. During the administrative validity period of a PID, the PID Provider will therefore provide multiple successive PIDs to a user, typically without any actions being expected from the user. However, when the administrative validity period of a PID ends, typically the user has to apply for an entirely new PID. | 19-12-2025                           |
| issuing_authority   | Name of the administrative authority that issued the person identification data, or the ISO 3166 alpha-2 country code of the respective Member State if there is no separate authority entitled to issue person identification data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Rijksdienst voor Identiteitsgegevens |
| issuing_country     | Alpha-2 country code, as specified in ISO 3166-1, of the country or territory of the provider of the person identification data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | NL                                   |

**Legal category.** This Rulebook retains the `attestation_legal_category` attribute
with the value `PID`, as specified in section 3.3 above.

> **Deviation from the generic template.** Section 4.1 of the generic WE BUILD template
> states that `attestation_legal_category` is superseded by the `category` attribute of
> [ETSI TS 119 472-1] and SHALL NOT be used, and that PID omits `category` entirely.
> This Rulebook does not follow that instruction, for three reasons. First,
> EW-DM-12-029 (legacy ARB_25) of ARF v3.0.0 is a SHALL that still requires
> `attestation_legal_category` to be included. Second, the `category` values defined in
> [ETSI TS 119 472-1] cover qualified and public-sector EAA only, so there is no value
> for a PID to migrate to. Third, this Rulebook already relies on the attribute in the
> verification sequence in chapter 10. This deviation is recorded for the rulebook
> quality assurance group to resolve.

### 4.2 Optional metadata


| **Data Identifier**  | **Definition**                                                                                                                                                                                                         | **Example value**                      |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| document_number      | A number for the person identification data, assigned by the provider of person identification data.                                                                                                                   | A01234567                              |
| issuing_jurisdiction | Country subdivision code of the jurisdiction that issued the person identification data, as specified in ISO 3166-2:2020, Clause 8. The first part of the code shall be the same as the value for the issuing country. | NL                                     |
| location_status      | The location of validity status information on the person identification data where the providers of person identification data revoke person identification data.                                                     | <https://example.com/statuslists/pid/> |

### 4.3 Conditional metadata

This attestation defines no conditional metadata.

### 4.4 Code lists

| Code list | Source | Extensible |
| --- | --- | --- |
| `sex` | ISO/IEC 5218 for values 0, 1, 2 and 9; values 3 to 6 are specified in section 3.3 | no |
| `nationality`, `resident_country`, `issuing_country` | ISO 3166-1 alpha-2 | no, follows the source standard |
| `issuing_jurisdiction` | ISO 3166-2:2020, Clause 8 | no, follows the source standard |

### 4.5 Integrity rules

| Rule | Enforcement point | Behaviour on failure |
| --- | --- | --- |
| The first part of `issuing_jurisdiction` SHALL equal `issuing_country` | PID Provider, at issuance | The PID is not issued |
| `place_of_birth` SHALL contain at least one of `country`, `region` or `locality` | PID Provider, at issuance | The PID is not issued |
| A `status` claim SHALL be present when the technical validity period exceeds 25 hours | PID Provider, at issuance | The PID is not issued |
| `trust_anchor`, where present, SHALL be the attribute referenced by chapter 10 | Relying Party, at verification | The Relying Party applies its risk analysis under chapter 10 |

## 5 Formats

| Format | Supported | Identifier | Specification | Notes |
| --- | --- | --- | --- | --- |
| ISO/IEC 18013-5 mdoc | yes | doctype `eu.europa.ec.eudi.pid.1`, namespace `eu.europa.ec.eudi.pid.1` | [ISO/IEC 18013-5] | Required, proximity presentation is in scope |
| SD-JWT VC | yes | `vct` `urn:eudi:pid:1` | [SD-JWT VC], [HAIP] | SHALL follow the HAIP profile |
| W3C VCDM | no | | | Permitted for non-qualified EAA only |

A PID SHALL be issued in both the ISO/IEC 18013-5 and SD-JWT VC formats.

### 5.1 ISO/IEC 18013-5-compliant encoding

##### 3.1.1 Document type and namespace

As specified in [Topic 3](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/annexes/annex-2/annex-2.02-high-level-requirements-by-topic.md#a232-topic-3---pid-rulebook) in Annex 2 of the ARF, "eu.europa.ec.eudi.pid.1" will be used as the attestation type for ISO/IEC 18013-5-compliant PIDs.

Similarly, "eu.europa.ec.eudi.pid.1" will be used for the namespace of the attributes specified below.

##### 3.1.2 Attributes overview

The ISO/IEC 18013-5-compliant encoding of PID attributes and metadata is
specified in the table below. The table contains the following information for
all attributes:

- The first column lists the data identifier specified in
  [Chapter 2](#2-pid-attributes-and-metadata) above.
- The second column lists the corresponding attribute identifier to be used in
  presentation requests and responses according to [ISO/IEC 18013-5].
- The third column indicates the encoding of each attribute. This column uses
  CDDL representation types defined in [RFC 8610]. The following notes and
  requirements apply:
  - ``tstr``, ``uint``, ``bstr``, ``bool`` and ``tdate`` are CDDL representation types defined in [RFC 8610].
  - Regarding type ``tstr``: this document confirms that, as specified in RFC
    8949, a ``tstr`` SHALL be encoded in UTF-8 and SHALL support the full Unicode
    range.
  - All attributes having encoding type ``tstr`` SHALL have a maximum length of
    150 characters.
  - This document specifies ``full-date`` as ``full-date = #6.1004(tstr)``, where tag
    1004 is specified in [RFC 8943].
  - In accordance with [RFC 8949], section 3.4.1, a ``tdate`` attribute SHALL
    contain a date-time string as specified in [RFC 3339]. In accordance with
    [RFC 8943], a ``full-date`` attribute SHALL contain a full-date string as
    specified in [RFC 3339].
  - The following requirements apply to the representation of dates in
    attributes, unless otherwise indicated:
    - Fractions of seconds SHALL NOT be used;
    - A local offset from UTC SHALL NOT be used; the time-offset defined in
      [RFC 3339] SHALL be to "Z".
  - RFC 8949, section 4.2, describes four rules for canonical CBOR. Three of
    those rules SHALL be implemented for all CBOR structures in PIDs, as
    follows:
    - integers (major types 0 and 1) SHALL be as small as possible;
    - the expression of the length in a ``bstr``, ``tstr``, array or map SHALL be as
      short as possible;
    - indefinite-length items SHALL be made into definite-length items.

Note that the presence of each attribute (mandatory or optional) is already specified in [Chapter 2](#2-pid-attributes-and-metadata) above.

| **Data Identifier**            | **Attribute identifier**       | **Encoding format**                                                                                      |
|--------------------------------|--------------------------------|----------------------------------------------------------------------------------------------------------|
| family_name                    | family_name                    | ``tstr``                                                                                                 |
| given_name                     | given_name                     | ``tstr``                                                                                                 |
| birth_date                     | birth_date                     | ``full-date``, see [Section 3.1.5](#315-attribute-birth_date).                                           |
| birth_place                    | place_of_birth                 | ``place_of_birth``, see [Section 3.1.6](#316-attribute-place_of_birth).                                  |
| nationality                    | nationality                    | ``nationalities``, see [Section 3.1.3](#313-attribute-nationality).                                      |
| resident_address               | resident_address               | ``tstr``                                                                                                 |
| resident_country               | resident_country               | ``tstr``                                                                                                 |
| resident_state                 | resident_state                 | ``tstr``                                                                                                 |
| resident_city                  | resident_city                  | ``tstr``                                                                                                 |
| resident_postal_code           | resident_postal_code           | ``tstr``                                                                                                 |
| resident_street                | resident_street                | ``tstr``                                                                                                 |
| resident_house_number          | resident_house_number          | ``tstr``                                                                                                 |
| personal_administrative_number | personal_administrative_number | ``tstr``                                                                                                 |
| portrait                       | portrait                       | ``bstr``; see additional information in [Section 2.3](#23-optional-attributes-specified-in-cir-20242977) |
| family_name_birth              | family_name_birth              | ``tstr``                                                                                                 |
| given_name_birth               | given_name_birth               | ``tstr``                                                                                                 |
| sex                            | sex                            | ``uint``; see additional information in [Section 2.3](#23-optional-attributes-specified-in-cir-20242977) |
| email_address                  | email_address                  | ``tstr``                                                                                                 |
| mobile_phone_number            | mobile_phone_number            | ``tstr``                                                                                                 |
| expiry_date                    | expiry_date                    | ``tdate`` or ``full-date``                                                                               |
| issuing_authority              | issuing_authority              | ``tstr``                                                                                                 |
| issuing_country                | issuing_country                | ``tstr``                                                                                                 |
| document_number                | document_number                | ``tstr``                                                                                                 |
| issuing_jurisdiction           | issuing_jurisdiction           | ``tstr``                                                                                                 |
| location_status                | -                              | See [Section 3.1.4](#314-attribute-location_status).                                                     |
| issuance_date                  | issuance_date                  | ``tdate`` or ``full-date``                                                                               |
| trust_anchor                   | trust_anchor                   | ``tstr``                                                                                                 |
| attestation_legal_category     | attestation_legal_category     | ``tstr``                                                                                                 |

##### 3.1.3 Attribute nationality

The attribute nationality is encoded as a type ``nationalities``, i.e., an array of Alpha-2 country codes as specified in ISO 3166-1. Using CDDL notation as specified in RFC 8610, the
encoding of this attribute is:

``` cddl
nationalities = [+ CountryCode]

CountryCode = tstr ; Alpha-2 country code specified in ISO 3166-1
```

Note: If the user to whom the person identification data relates has multiple
nationalities (and the PID Provider is willing to attest to these multiple
nationalities), the PID Provider can include all of the nationalities in the
nationalities array. A potential drawback of this solution is that the user
cannot selectively disclose only one of these nationalities, since for ISO/IEC
18013-5-compliant attestations, always the entire array will be presented if the
user approves the presentation of the nationality attribute. A potential
solution to this challenge is for the PID Provider to include only one
nationality in the nationality attribute, and for the remaining nationalities
use one or more domestic data attributes specified according to requirement
PID_06 in [Annex 2, Topic 3](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/annexes/annex-2/annex-2.02-high-level-requirements-by-topic.md#a232-topic-3---pid-rulebook).

##### 3.1.4 Attribute location_status

For ISO/IEC 18013-5-compliant PIDs, the attribute location_status is
absent, since the PID issuer will add revocation information, if needed, to the MSO as specified in [ISO/IEC 18013-5].

##### 3.1.5 Attribute birth_date

For PIDs compliant with ISO/IEC 18013-5, dates are encoded as specified in RFC 8949 (which references RFC 3339). This encoding does not contain provisions for encoding partial dates. This
may cause challenges in case the birth date of a user is not (fully) known. To
deal with such cases, a PID Provider could adopt a policy to choose appropriate (and RFC 3339-compliant) values for the unknown date elements. However, mandating such a policy is out of
scope of this document.

##### 3.1.6 Attribute place_of_birth

The attribute place_of_birth is encoded as a type ``place_of_birth``.
Using CDDL notation as specified in RFC 8610, the encoding of this attribute is:

``` cddl
place_of_birth =
{
  ? "country": tstr  ; a single alpha-2 country code as specified in ISO 3166-1
  ? "region": tstr   ; the name of a state, province, district, or local area
  ? "locality": tstr ; the name of a municipality, city, town, or village
}
```

place_of_birth SHALL contain at least one of the following key-value pairs: ``"country"``, ``"region"``, or ``"locality"``.

### 5.2 SD-JWT VC-based encoding


#### 3.2.1 Overview

Following requirement ARB_06b, SD-JWT VC-encoded PIDs use claim names that are either registered in the JSON Web
Token Claims Registry [IANA-JWT-Claims], are Public Names as defined in [RFC 7519], or are Private Names specific
to the attestation type. The tables below map the data
identifiers defined above to the corresponding claim names and specify the encoding format of the claim value.

A JSON string used in an SD-JWT VC-encoded PID SHALL be encoded in UTF-8, and SHALL support the full Unicode range, unless explicitly specified otherwise in the tables below or the references therein.

Note that a hierarchical claim name structure can be used in SD-JWT VC encoded
PIDs as SD-JWT allows for individual selective disclosure of objects
and their properties. A hierarchical claim name structure is indicated by the
notation `parent.child` in the tables below.

The following IANA registered claim names are to be used for PIDs:

| **Data Identifier**   | **Attribute identifier** | **Encoding format** | **Reference/Notes**                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------------|--------------------------|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| family_name           | family_name              | string              | [OIDC] definition: Surname(s) or last name(s) to whom the person identification data relates. Note that in some cultures, people can have multiple family names or no family name; all can be present, with the names being separated by space characters.                                                                                                                                                   |
| given_name            | given_name               | string              | [OIDC] definition: Given name(s) or first name(s) to whom the person identification data relates. Note that in some cultures, people can have multiple given names; all can be present, with the names being separated by space characters.                                                                                                                                                                  |
| birth_date            | birthdate                | string              | [OIDC] definition: ISO 8601-1 [ISO8601‑1] YYYY-MM-DD format                                                                                                                                                                                                                                                                                                                                                  |
| birth_place           | place_of_birth           | JSON structure      | [EKYC] definition: At least one of the members (country, region or locality) SHALL be present in the JSON structure                                                                                                                                                                                                                                                                                          |
| nationality           | nationalities            | array of strings    | Using alpha-2 country codes as defined in [Section 2.2](#22-mandatory-attributes-specified-in-cir-20242977)                                                                                                                                                                                                                                                                                                  |
| resident_address      | address.formatted        | string              | [OIDC] definition: Full mailing address, formatted for display or use on a mailing label. This field MAY contain multiple lines, separated by newlines. Newlines can be represented either as a carriage return/line feed pair ("\r\n") or as a single line feed character ("\n")                                                                                                                            |
| resident_country      | address.country          | string              | [OIDC] definition: Country name component                                                                                                                                                                                                                                                                                                                                                                    |
| resident_state        | address.region           | string              | [OIDC] definition: State, province, prefecture, or region component.                                                                                                                                                                                                                                                                                                                                         |
| resident_city         | address.locality         | string              | [OIDC] definition: City or locality component.                                                                                                                                                                                                                                                                                                                                                               |
| resident_postal_code  | address.postal_code      | string              | [OIDC] definition: Zip code or postal code component.                                                                                                                                                                                                                                                                                                                                                        |
| resident_street       | address.street_address   | string              | [OIDC] definition: Full street address component, which MAY include house number, street name, Post Office Box, and multi-line extended street address information. This field MAY contain multiple lines, separated by newlines. Newlines can be represented either as a carriage return/line feed pair ("\r\n") or as a single line feed character ("\n").                                                 |
| family_name_birth     | birth_family_name        | string              | [EKYC] definition:  Family name(s) when they were born, or at least from the time they were a child to whom the person identification data relates. This term can be used by a person who changes the family name later in life for any reason. Note that in some cultures, people can have multiple family names or no family name; all can be present, with the names being separated by space characters. |
| given_name_birth      | birth_given_name         | string              | [EKYC] definition:  Given name(s) when they were born, or at least from the time they were a child to whom the person identification data relates. This term can be used by a person who changes the given name later in life for any reason. Note that in some cultures, people can have multiple given names; all can be present, with the names being separated by space characters.                      |
| email_address         | email                    | string              | [OIDC] definition:  Preferred e-mail address to whom the person identification data relates.. Its value MUST conform to the RFC 5322 [RFC5322] addr-spec syntax. The RP MUST NOT rely upon this value being unique                                                                                                                                                                                           |
| mobile_phone_number   | phone_number             | string              | [OIDC] definition:  Preferred telephone number to whom the person identification data relates.. E.164 [E.164] is RECOMMENDED as the format of this Claim, for example, +1 (425) 555-1212 or +56 (2) 687 2400. If the phone number contains an extension, it is RECOMMENDED that the extension be represented using the RFC 3966 [RFC3966] extension syntax, for example, +1 (604) 555-1234;ext=5678          |
| portrait              | picture                  | string              | data URL containing the base64-encoded portrait in JPEG format according to PID_03 in [Annex 2, Topic 3](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/3.0.0/annexes/annex-2/annex-2.01-high-level-requirements/)                                                                                                                                                 |

Note: The standard JWT claims nbf and exp are used to express the technical validity period of a SD-JWT VC-compliant PID.

The following Private Names specific to the attestation type defined in this document are to be used for PIDs:

| **Data Identifier**            | **Attribute identifier**       | **Encoding format** | **Notes**                                                                                                                                                                    |
|--------------------------------|--------------------------------|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| attestation_legal_category     | attestation_legal_category     | string              | SHALL be `PID`                                                                                                                                                                |
| expiry_date                    | date_of_expiry                 | string              | ISO 8601-1 [ISO8601‑1] YYYY-MM-DD format, as defined in Section 5.4.4.2 of [EKYC Schema]                                                                                     |
| issuance_date                  | date_of_issuance               | string              | ISO 8601-1 [ISO8601‑1] YYYY-MM-DD format, as defined in Section 5.4.4.2 of [EKYC Schema]                                                                                     |
| personal_administrative_number | personal_administrative_number | string              |                                                                                                                                                                              |
| resident_house_number          | address.house_number           | string              | This document extends the specification of ``address`` in [OIDC] with an additional member ``address.house_number``                                                          |
| sex                            | sex                            | number              | numeric encoding as described in [Section 2.3](#23-optional-attributes-specified-in-cir-20242977); gender from [OIDC] uses a different value range and is therefore not used |
| issuing_authority              | issuing_authority              | string              |                                                                                                                                                                              |
| issuing_country                | issuing_country                | string              |                                                                                                                                                                              |
| document_number                | document_number                | string              |                                                                                                                                                                              |
| issuing_jurisdiction           | issuing_jurisdiction           | string              |                                                                                                                                                                              |
| location_status                         | status                         | JSON object         | See [Section 3.2.2](#322-attribute-status)                                                                                                                                   |
| trust_anchor                   | trust_anchor                   | string              |                                                                                                                                                                              |


#### 3.2.2 Attribute status

For SD-JWT VC-compliant PIDs, the PID MUST include a `status` claim if the technical validity period is greater than 25 hours. This claim enables Relying Parties to determine if a credential has been revoked via a status list mechanism, as specified in [SD-JWT VC].

The `status` claim SHALL be a JSON object with the following members:
- `type` (string): SHALL be `"status-list"`.
- `status_list_credential` (string, URI): The URI of the Status List Credential document that contains the status bitstring.
- `status_list_index` (integer, >= 0): The zero-based index into the status list bitstring that corresponds to this credential.
- `status_purpose` (string): SHALL be `"revocation"` for this PID.

Example:
```json
{
  "status": {
    "type": "status-list",
    "status_list_credential": "https://issuer.example.com/status/1",
    "status_list_index": 42,
    "status_purpose": "revocation"
  }
}
```

#### 3.2.3 Note on VCT

SD-JWT VC defines the Verifiable Credential Type (`vct`). A type comes
with associated metadata that, for instance, provides information about
the type itself, outlines a schema detailing the claims that are
optional or mandatory in the SD-JWT VC, and specifies their display
methods. Additionally, a type can extend another type, enabling
the creation of domestic types based on a common EU-wide type, while preserving
the mandatory claims from the base type. Domestic
types MAY however define additional claims and display information. Details
are defined in [SD-JWT VC].

Requirement PID_14 in ARF Annex 2 defines the base type to be "urn:eudi:pid:1". As a convention, all PIDs must use types in the namespace "urn:eudi:pid:".

SD-JWT VC specifies Type Metadata as a machine-readable format for information
regarding a type, including the information on claims such as what is contained
in this document. Requirement PID_15 in [Annex 2, Topic 3](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/annexes/annex-2/annex-2.02-high-level-requirements-by-topic.md#a232-topic-3---pid-rulebook) requires that the information on the
common EU-wide type as well as on any domestic types is published and
accessible in a catalog.

### 5.3 Example


EXAMPLE: The following example shows the payload of a PID in SD-JWT VC format before the encoding into the SD-JWT format.

```json
{
    "vct": "urn:eudi:pid:de:1",
    "attestation_legal_category": "PUB-EAA",

    "given_name": "Jean",
    "family_name": "Dupont",
    "birthdate": "1980-05-23",

    "address": {
        "street_address": "123 Via Appia",
        "locality": "Rome",
        "region": "Lazio",
        "postal_code": "00100",
        "country": "IT"
    },

    "nationalities": ["FR"],

    "sex": 5,

    "place_of_birth": {
        "country": "DD"
    },

    "cnf": {
        "jwk": {
            "kty": "EC",
            "crv": "P-256",
            "x": "52aDI_ur05n1f_p3jiYGUU82oKZr3m4LsAErM536crQ",
            "y": "ckhZ-KQ5aXNL91R8Eufg1aOf8Z5pZJnIvuCzNGfdnzo"
        }
    },

    "issuing_authority": "DE",
    "issuing_country": "DE",

    "status": {
        "type": "status-list",
        "status_list_credential": "https://issuer.example.com/status/1",
        "status_list_index": 42,
        "status_purpose": "revocation"
    }
}
```

Note: The `cnf` claim is used for expressing key binding in SD-JWT VCs.
The example above shows a public key in JWK format.

Note: Additional technical claims are not shown here, including
references to the issuer and more.

## 6 Protocols

### 6.1 Issuance

PIDs are issued using OpenID for Verifiable Credential Issuance [OpenID4VCI], as
profiled by [HAIP].

### 6.2 Presentation

PIDs are presented using OpenID for Verifiable Presentations [OpenID4VP] for remote
presentation, and ISO/IEC 18013-5 device retrieval for proximity presentation.

## 7 Issuance

### 7.1 Binding

| Field | Value | Source |
| --- | --- | --- |
| Device-bound | SHALL | EW-DM-12-038 |
| Cryptographically bound to | none | EW-DM-12-032 |
| Relying Party must also verify a PID | not applicable | EW-DM-12-031 |
| Binding subject | natural person | CIR 2024/2977, person identification data for the natural person |

A PID SHALL be bound to the Wallet Unit key material. For SD-JWT VC this is expressed
through the `cnf` claim, as stated in section 5.2. The row for EW-DM-12-031 is not
applicable because this attestation is itself the PID.

### 7.2 Lifecycle management

- PID Providers SHALL issue a PID only after identity verification according to the
  applicable Member State PID issuance framework.
- PID Providers SHALL set the technical validity period, using `exp` and, where
  present, `nbf`.
- The administrative validity period, expressed through `expiry_date` and
  `issuance_date`, is distinct from the technical validity period. See the
  clarification recorded against `expiry_date` in section 4.1.
- During the administrative validity period the PID Provider will provide multiple
  successive PIDs to a user, typically without action by the user. Reissuance cadence
  is set by the PID Provider.

### 7.3 Issuance Policy

PID Providers SHALL provide a revocation capability as specified in chapter 8, or
issue short-lived PIDs as described there.

### 7.4 Embedded disclosure policy

This attestation defines no embedded disclosure policy.

## 8 Revocation


PIDs MAY be either (a) short-lived and non-revocable, or (b) long-lived and revocable, in line with ARF Annex 2 Topic 7.

Revocation strategy:
- A PID Provider SHALL use one of the following approaches:
  - Issue short-lived PIDs with a technical validity period of 24 hours or less; or
  - Support revocation using an Attestation Status List (ASL) or Attestation Revocation List (ARL) mechanism.
- If a PID is revocable, the PID Provider SHALL be the only party responsible for executing revocation of that PID, and SHALL NOT reverse revocation once executed.
- The PID Provider MAY support temporary suspension before permanent revocation, with a maximum suspension period defined in the revocation policy.
- The PID Provider SHALL maintain a revocation policy specifying under which conditions it revokes a PID (e.g. compromise, attribute changes, explicit user request, death of the subject), notification procedures for users, and user rights including the right to request revocation at any time.

Technical mechanisms:
- For SD-JWT VC-based PIDs, revocation is expressed via the `status` claim (see Section 3.2.2) using the status-list mechanism.
- For ISO/IEC 18013-5-compliant PIDs, revocation information is provided via the MSO as defined in ISO/IEC 18013-5; no `location_status` attribute is used (see Section 3.1.3).

Relying Party (RP) checks:
- A RP Instance SHOULD verify revocation status when the PID is revocable, and SHALL perform a risk analysis if it decides not to.
- Relying Parties SHOULD NOT fetch status information at presentation time. Instead, they SHOULD periodically retrieve and cache the relevant ASL/ARL and distribute it to their RP Instances.
- If reliable revocation information is unavailable or indeterminate, the RP SHALL decide whether to accept or refuse the PID based on its risk analysis. The RP SHALL log such incidents and MAY report recurring failures to the PID Provider.
- Revocation status checking SHALL be designed to prevent correlation of user identity across Relying Parties (e.g., using batch status lists rather than per-credential status endpoints).

Timing:
- Where revocation is supported, the PID Provider SHOULD ensure that revocation is reflected in published status information within 24 hours of the revocation decision.
- For emergency revocations (e.g., security compromise), the PID Provider SHOULD propagate revocation within a shorter timeframe where technically feasible.

## 9 Presentation

### 9.1 Relying Party policy

> A Relying Party receiving an attestation of this type SHALL:
>
> 1. verify the signature over the attestation using a trust anchor obtained as
>    described in chapter 10;
> 2. verify that the attestation is within its validity period;
> 3. check revocation status as described in chapter 8, unless the attestation is
>    short-lived; or remaining lifetime of the attestation is below revocation time
>    threshold;
> 4. verify device binding where section 7.1 records the attestation as device-bound;
> 5. request only those attributes that are necessary for the stated purpose of the
>    transaction, and, where the trust model for this attestation requires Relying
>    Party registration, only those attributes it is registered and authorised to
>    request.

Obligations specific to this attestation type, carried over from the use-case context
of the previous version of this Rulebook:


PID is used to identify a natural person (user) in national and cross-border digital services within the EUDI Wallet ecosystem.

Primary use cases:
- Proving the identity of a natural person (user) to a Relying Party(RP) in online services.
- Supporting regulated or high-trust onboarding and access control flows where identification is required.
- Supporting attribute verification (e.g., residency, age) subject to data minimisation and proportionality.

Issuance requirements and expectations:
- PID Providers SHALL issue PID only after identity verification according to the applicable Member State PID issuance framework.
- PID Providers SHALL bind PID to the Wallet Unit key material as defined in Chapter 3 (e.g., `cnf` for SD-JWT VC).
- PID Providers SHALL set technical validity (`exp`, and `nbf` if present) and SHALL provide status/revocation capability as defined in Chapter 6.
- For SD-JWT VC PIDs, the PID SHALL include a `status` claim when required by Section 3.2.2 (technical validity period > 25 hours).

Expected user behaviours:
- The user SHOULD approve PID presentation only when the Wallet Unit shows the RP identity, intended use, and a privacy policy reference.
- The user SHOULD approve presentation only when the requested attributes are necessary for the transaction.
- Preferably, the user SHOULD either approve all requested attributes or deny the request. If the user does not want to disclose a requested attribute, the user SHOULD deny the request and allow the RP to send a revised request (see Section 2.1).
- Where selective disclosure is supported by the format, the user SHOULD disclose only the minimum attributes required by the transaction.

Relying Party (RP) behaviours:
- The RP SHALL be registered as a Wallet RP and SHALL request only attributes justified for the intended use.
- The RP SHALL authenticate to the Wallet Unit (e.g., using its access certificate chain) in the applicable presentation protocol.
- The RP SHOULD include (or enable retrieval of) the registered intended use information and privacy policy reference so the Wallet Unit can inform the user.
- The RP SHALL verify the PID signature according to Chapter 3 and SHALL validate issuer trust and authorisation using applicable trust anchors (Chapter 5).
- The RP SHALL validate technical validity (check `exp`, and `nbf` if present) and SHALL apply revocation/status checks as defined in Chapter 6.
- The RP MAY verify device binding / proof of possession where supported. If the RP requests cryptographic holder binding in the presentation protocol, it SHALL NOT accept a non-device-bound PID.

Presentation requirements:
- The RP SHOULD request only the minimum attributes needed for the transaction (data minimisation).
- The RP SHALL NOT rely on non-unique contact attributes (e.g., `email_address`) as unique identifiers, as already stated in Chapter 3.

Transactional data:
- The RP MAY keep minimal logs necessary to demonstrate verification events and security-relevant auditability (e.g., timestamps, verification outcome, issuer identifier, status-check result).
- The RP SHOULD avoid storing full PID payloads unless required by law or strictly necessary for dispute handling.

### 9.2 Presentation modes

Both remote and proximity presentation are in scope, consistent with chapters 5 and 6.
Proximity presentation requires the mdoc format, which section 5 records as supported.

### 9.3 Transactional data

This attestation defines no transactional data.

## 10 Trust Framework

**PID, QEAA, PuB-EAA and attestations resolved via Trusted Lists**

> The trust anchor is obtained from a Trusted List, as described in section 6.6.3.6
> of the ARF main document. The Provider may sign the attestation with an
> intermediate signing certificate, in which case the trust anchor is used to verify
> that certificate rather than the attestation directly.

**Trust anchor location**

> The attribute or metadata carrying the trust anchor location contains at least the
> URL at which a machine-readable version can be found or looked up.

Coherence check: the attribute named here is `trust_anchor`, declared in section 4.2.

**Deployment profile**


This section specifies how trust anchors relevant to PID are distributed and looked up. Two trust relationships are in scope:
- PID authenticity - the RP verifies the PID signature.
- RP authenticity - the Wallet Unit authenticates the RP before presenting PID attributes.

For PID and QEAAs, trust anchors of the Provider are obtained from a List of Trusted Entities (LoTE) or Trusted List. For PuB-EAAs, the RP uses the QTSP Trusted List to validate the certificate chain of the PuB-EAA Provider certificate. The applicable rulebook specifies the mechanisms enabling trust anchor distribution and lookup for non-qualified cases.

Trust anchor distribution:
- PID Provider trust anchors SHALL be distributed via LoTE following the PID Provider registration and notification process, where applicable.
- Qualified trust anchors (QTSP trust anchors) SHALL be obtained via eIDAS Trusted Lists (and their corresponding publication mechanisms).
- Access Certificate Authority trust anchors (used for RP authentication towards the Wallet Unit) SHALL be distributed via LoTE.
- PID Providers SHOULD populate the optional PID metadata `trust_anchor` (Section 2.6) with at least one machine-readable pointer to the applicable trust anchor source (LoTE entry, Trusted List, or an index pointing to the authoritative source).

Trust anchor lookup mechanisms:
- RPs and Wallet Units SHALL support trust anchor lookup based on:
  - `issuing_country` (Section 2.5) for selecting the relevant national LoTE / Trusted List context, and
  - the optional `trust_anchor` metadata (Section 2.6) as a machine-readable pointer when present.
- RPs and Wallet Units SHOULD cache trust anchor artefacts and apply an update policy appropriate for the deployment, including re-fetching when a pointer changes or when cached artefacts expire.

Verification steps - RP verifies PID authenticity:
1) Determine the legal category of the PID using `attestation_legal_category` (Section 2.5).
2) Verify the PID signature according to Chapter 3.
3) Obtain the relevant trust anchor(s):
   - For PID or QEAA, obtain the Provider trust anchor from the applicable LoTE / Trusted List.
   - For PuB-EAA, validate the PuB-EAA Provider certificate chain up to the QTSP trust anchor from the QTSP Trusted List.
   - For non-qualified EAA cases, obtain the applicable domain trust anchor using the mechanism defined below (WE BUILD profile).
4) Validate the trust chain (including intermediate certificates where used) and validate revocation/status information as specified in Chapter 6.
5) Where a trust anchor source is retrieved dynamically, validate the authenticity and integrity of the retrieved artefact before use (for example, using a signed LoTE/Trusted List artefact or an authenticated distribution channel).

Verification steps - Wallet Unit authenticates the RP (precondition for PID presentation):
1) Obtain the trust anchor of the Access Certificate Authority from the applicable LoTE.
2) Validate the RP access certificate chain included in the presentation request up to the Access CA trust anchor.
3) Validate revocation/status of certificates in the chain as required by the applicable ecosystem rules and Chapter 6.
4) Proceed to user approval only after successful RP authentication.

WE BUILD specific profile and extensions:
- WE BUILD SHALL support a machine-readable LoTE endpoint (or equivalent distribution mechanism) that contains:
  - trust anchors for PID Providers participating in WE BUILD, and
  - trust anchors for the Access Certificate Authorities used by WE BUILD participants.
- The WE BUILD LoTE SHOULD be structured so that entries can be resolved by `issuing_country` and entity identifier, and SHOULD support inclusion of pointers to authoritative national LoTE / Trusted List sources where available.
- Wallet Units and RPs in WE BUILD SHALL be able to resolve trust anchors using either:
  - the `trust_anchor` metadata carried in the PID, or
  - a pre-configured WE BUILD LoTE entry point based on `issuing_country`.

Practical examples (illustrative):
- Example 1 - PID includes `trust_anchor` pointing to a LoTE entry:
  - `trust_anchor`: `https://lote.example.org/XX/pid-providers.json`
  - RP retrieves the LoTE artefact, selects the PID Provider entry, and uses the contained trust anchor to validate the PID Provider signing chain.
- Example 2 - Wallet Unit authenticates an RP:
  - Wallet Unit retrieves the Access CA trust anchor for `issuing_country = "XX"` from LoTE.
  - RP includes its access certificate and intermediate certificates in the request.
  - Wallet Unit validates the chain up to the Access CA trust anchor before showing the request to the user.

For information regarding the use of the trust list in WE BUILD, please consult the Architecture Blueprint

## 11 References


| **Item Reference**                     | **Standard name/details**                                                                                                                                                                                                                                                |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [European Digital Identity Regulation] | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework |
| [ISO/IEC 18013-5]                      | ISO/IEC 18013-5, Personal identification --- ISO-compliant driving licence - Part 5: Mobile driving licence (mDL) application, First edition, 2021-09                                                                                                                    |
| [OIDC]                                 | Sakimura, N. et al., "OpenID Connect Core 1.0", OpenID Foundation. Available: <https://openid.net/specs/openid-connect-core-1_0.html>                                                                                                                                    | 
| [EKYC]                                 | OpenID Connect for Identity Assurance Claims Registration <https://openid.net/specs/openid-connect-4-ida-claims-1_0-final.html#ICAO-Doc9303>                                                                                                                             |
| [SD-JWT VC]                            | SD-JWT-based Verifiable Credentials (SD-JWT VC). Available: <https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/>                                                                                                                                               |
| [Topic 3]                              | ARF Annex 2 - Topic 3 - Attestation revocation and revocation checking Available: <https://eudi.dev/3.0.0/annexes/annex-2/annex-2.02-high-level-requirements-by-topic/>                                                                                                 |
| [Topic 12]                             | ARF Annex 2 - Topic 12 - Attestation Rulebooks, Available: <https://eudi.dev/3.0.0/annexes/annex-2/annex-2.02-high-level-requirements-by-topic/>                                                                                                                        |
| [W3C VCDM v2.0]                        | Sporny, M. *et al,* Verifiable Credentials Data Model v2.0, W3C Recommendation.                                                                                                                                                                                          |

For further references please see [ARF Chapter 10](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#10-references) of the ARF main document.
| [CIR 2024/2977] | [Commission Implementing Regulation (EU) 2024/2977](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402977) of 28 November 2024 on person identification data and electronic attestations of attributes |
| [ETSI TS 119 472-1] | ETSI TS 119 472-1, Electronic Signatures and Trust Infrastructures; Profiles for Electronic Attestations of Attributes; Part 1: General requirements |
| [HAIP] | OpenID4VC High Assurance Interoperability Profile. Available: <https://openid.net/specs/openid4vc-high-assurance-interoperability-profile-1_0.html> |
| [OpenID4VCI] | OpenID for Verifiable Credential Issuance. Available: <https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html> |
| [OpenID4VP] | OpenID for Verifiable Presentations. Available: <https://openid.net/specs/openid-4-verifiable-presentations-1_0.html> |
