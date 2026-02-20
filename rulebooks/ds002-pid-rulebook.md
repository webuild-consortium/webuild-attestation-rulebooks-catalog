---
title: "European Digital Identity Wallet"
subtitle: "ARF Annex 3.01 - PID Rulebook"
...

#  Attestation Rulebook for attestations of type Personal Identification Data (PID)

| Version | Date        | Description                                                                                                                                                                                                                                                                                                                                                                                                                       |
|---------|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|
| 0.1.3   | 27 Oct 2025 | Transferred main structure and content from [EUDI repository](https://github.com/eu-digital-identity-wallet/eudi-doc-attestation-rulebooks-catalog/blob/main/rulebooks/pid/pid-rulebook.md) and modified template to closer align to [EUDI template](https://github.com/eu-digital-identity-wallet/eudi-doc-attestation-rulebooks-catalog/blob/main/template/attestation-rulebook-template.md). First specific draft for WE BUILD |
|0.9.0| 2025-12-12  | Feedback of WeBuild WP 4 Task 2 implemented                                                                                                                                                                                                                                                                                                                                                                                       |
<!-- Usage help: (Name LastName, Affiliation) -->
*  Authors
    * Jonas Toennis , [Brønnøysund Registry Center](https://www.brreg.no)

* Previous authors
  * David Bakker, Unknown Affiliation
* 
### Feedback and contact
Main feedback channel: [GitHub issues](https://github.com/webuild-consortium/eudi-wallet-rulebooks-and-schemas/issues)
Alternative: Contact workpackage 4 in WE BUILD, or/and the author of the document. 

## 1 Introduction

### 1.1 Document scope and purpose

This document is the natural-person Person Identification Data (PID) Rulebook
and is part of the Architecture Reference Framework (ARF). It specifies
how the mandatory and optional person identification data for the natural
person, as defined in Tables 1 and 2 in the Annex of the Commission Implementing
Regulation on PID and EAA [CIR 2024/2977], as well as the metadata specified in
Table 5 of that CIR, will be encoded within the EUDI Wallet ecosystem.
Additionally, this document specifies further optional PID attributes that are
not included in the CIR.

This document also specifies how a PID and all attributes in it are encoded if
the PID complies with [ISO/IEC 18013-5] and if it complies with [SD-JWT VC].

European Business Wallet – Owner Identification Data (formerly known as Legal Person Identification Data, LPID, or Person identification data for the legal person) is out of the scope of this document and is specified in the [European Business Wallet - Owner Identification Data Rulebook](../rulebooks/ds001-ebw-oid-rulebook.md).

This PID Rulebook complies with all applicable requirements in Topic 12
(Attestation Rulebooks) in Annex 2 of the Architecture Reference Framework.

### 1.2 Document structure

This PID Rulebook is structured as follows:

- [Chapter 2](#2-attestation-attributes-and-metadata) describes the PID attributes and
metadata on a generic level, regardless of the encoding used for the PID. Most
of the content of this chapter is a direct copy of the Annex of Commission
Implementing Regulation 2024/2977 on PID and EAA. However, a few additional
attributes are specified in this chapter.
- [Chapter 3](#3-attestation-encoding) specifies how the PID
attributes and metadata are encoded in the required formats
- [Section 3.2](#32-sd-jwt-vc-based-encoding-of-pid) specifies how the PID
attributes and metadata are encoded in case the PID complies with [SD-JWT VC].
- **TODO: Add Chapter for W3C Json-ld** 
- [Chapter 5](#4-attestation-usage) describes attestation usage guidelines, user
and RP behaviours, and applicability scenarios. TODO: WE BUILD addition on the EUDI rulebook document based on the EUDI rulebook template.
- [Chapter 6](#5-trust-anchors) describes trust anchor distribution and lookup
mechanisms. TODO: WE BUILD addition on the EUDI rulebook document based on the EUDI rulebook template.
- [Chapter 7](#6-revocation) describes revocation strategy and mechanisms.
TODO: WE BUILD addition on the EUDI rulebook document based on the EUDI rulebook template.
- [Chapter 8](#7-compliance) describes compliance criteria and conformance
statements. TODO: WE BUILD addition on the EUDI rulebook document based on the EUDI rulebook template.
- [Chapter 9](#8-references) lists references.

### 1.3 Keywords

This document uses the capitalised keywords 'SHALL', 'SHOULD' and 'MAY' as
specified in [RFC 2119], i.e. to indicate requirements, recommendations and
options specified in this document.

In addition, 'must' (non-capitalised) is used to indicate an external
constraint, i.e. a requirement that is not mandated by this document, but, for
instance, by an external document. The word 'can' indicates a capability,
whereas other words, such as 'will', and 'is' or 'are' are intended as
statements of fact.



### 1.4 Terminology

This document uses the terminology specified in [Annex 1](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-1/annex-1-definitions/) of the ARF.

In addition, the following terms are used in this document:

| Term | Definition in WE BUILD Context                                                                                                                                                                                                   |
|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CDDL | CDDL stands for Concise Data Definition Language. It’s a formal notation used to describe the structure and constraints of data, especially in contexts where data is encoded using CBOR (Concise Binary Object Representation) |

## 2 Attestation attributes and metadata

### 2.1 Introduction

Sections [2.2](#22-mandatory-attributes-specified-in-cir-20242977), [2.3](#23-optional-attributes-specified-in-cir-20242977), [2.4](#24-condition-attributes), [2.5](#25-mandatory-metadata-specified-in-cir-20242977) and [2.6](#26-optional-metadata-specified-in-cir-20242977) of this chapter list the mandatory and optional
PID attributes and PID metadata defined in CIR 2024/2977. [Section 2.7](#27-additional-optional-attributes-specified-in-this-rulebook) lists the optional PID attributes additionally defined in this PID Rulebook.

Note that, when requesting PID attributes from a Wallet Unit, a Relying Party is not required to request all mandatory attributes. Also, a User is allowed to refuse to present a mandatory attribute if it is requested by a Relying Party.

The data identifiers and definitions given in Sections 2.2, 2.3, 2.4, and 2.5
are identical to those in CIR 2024/2977, except where explicitly indicated that
some further explanations have been added in this Rulebook.

All data identifiers and definitions in this chapter are independent of any
encoding used. Consequently,

- the data identifiers in these tables are not necessarily the same as the
attribute identifiers used for PIDs complying with [ISO/IEC 18013-5]. [Chapter 3](#31-isoiec-18013-5-compliant-encoding) specifies the attribute
identifiers to be used for PIDs in [ISO/IEC 18013-5] format
- the data identifiers in these tables are not necessarily the same as the claim
names used for PIDs complying with [SD-JWT VC]. [Section 3.2](#32-sd-jwt-vc-based-encoding-of-pid) specifies the claim names to be
used for such PIDs.

### 2.2 Mandatory attributes specified in CIR 2024/2977

| **Data Identifier**  | **Definition**                                                                                                                                                                                                                         |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| family_name          | Current last name(s) or surname(s) of the user to whom the person identification data relates.                                                                                                                                         |
| given_name           | Current first name(s), including middle name(s) where applicable, of the user to whom the person identification data relates.                                                                                                          |
| birth_date           | Day, month, and year on which the user to whom the person identification data relates was born.                                                                                                                                        |
| birth_place          | The country as an alpha-2 country code as specified in ISO 3166-1, or the state, province, district, or local area or the municipality, city, town, or village where the user to whom the person identification data relates was born. |
| nationality          | One or more alpha-2 country codes as specified in ISO 3166-1, representing the nationality of the user to whom the person identification data relates.                                                                                 |

### 2.3 Optional attributes specified in CIR 2024/2977

| **Data Identifier**            | **Definition**                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| resident_address               | The full address of the place where the user to whom the person identification data relates currently resides or can be contacted (street name, house number, city etc.).                                                                                                                                                                                                                                                                                                    |
| resident_country               | The country where the user to whom the person identification data relates currently resides, as an alpha-2 country code as specified in ISO 3166-1.                                                                                                                                                                                                                                                                                                                          |
| resident_state                 | The state, province, district, or local area where the user to whom the person identification data relates currently resides.                                                                                                                                                                                                                                                                                                                                                |
| resident_city                  | The municipality, city, town, or village where the user to whom the person identification data relates currently resides.                                                                                                                                                                                                                                                                                                                                                    |
| resident_postal_code           | The postal code of the place where the user to whom the person identification data relates currently resides.                                                                                                                                                                                                                                                                                                                                                                |
| resident_street                | The name of the street, which may include the house number, where the user to whom the person identification data relates currently resides.                                                                                                                                                                                                                                                                                                                                 |
| personal_administrative_number | A value assigned to the natural person that is unique among all personal administrative numbers issued by the provider of person identification data. Where Member States opt to include this attribute, they shall describe in their electronic identification schemes under which the person identification data is issued, the policy that they apply to the values of this attribute, including, where applicable, specific conditions for the processing of this value. |
| portrait                       | Facial image of the wallet user compliant with ISO 19794-5 or ISO 39794 specifications.                                                                                                                                                                                                                                                                                                                                                                                      |
| family_name_birth              | Last name(s) or surname(s) of the User to whom the person identification data relates at the time of birth.                                                                                                                                                                                                                                                                                                                                                                  |
| given_name_birth               | First name(s), including middle name(s), of the User to whom the person identification data relates at the time of birth.                                                                                                                                                                                                                                                                                                                                                    |
| sex                            | Values shall be one of the following: 0 = not known; 1 = male; 2 = female; 3 = other; 4 = inter; 5 = diverse; 6 = open; 9 = not applicable. For values 0, 1, 2 and 9, ISO/IEC 5218 applies.                                                                                                                                                                                                                                                                                  |
| email_address                  | Electronic mail address of the user to whom the person identification data relates, in conformance with [RFC 5322].                                                                                                                                                                                                                                                                                                                                                          |
| mobile_phone_number            | Mobile telephone number of the User to whom the person identification data relates, starting with the '+' symbol as the international code prefix and the country code, followed by numbers only.                                                                                                                                                                                                                                                                            |

### 2.4 Condition Attributes
The PID defined in this rulebook does not contain any condition attributes.

### 2.5 Mandatory metadata specified in CIR 2024/2977

| **Data Identifier** | **Definition**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| attestation_legal_category | An indication, in a form suitable for automated processing, that the attestation has been issued as a QEAA, PUB-EAA or EAA.  This attribute is defined in accordance with ARB_25 in [Topic 12] of Annex 2 of the ARF, which requires that each attestation carry an indication of its legal category.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| expiry_date         | Date (and if possible time) when the person identification data will expire. **Further clarification added in this PID Rulebook:** This attribute, as well as the optional issuance_date attribute specified in [Section 2.5](#25-mandatory-metadata-specified-in-cir-20242977), pertains to the administrative validity period of the PID. It is up to the PID Provider to decide whether a PID has an administrative validity period. However, if present, it in general is different from the technical validity period of a PID. The technical validity period is a mandatory element of all PIDs (and also attestations) in the EUDI Wallet ecosystem. It typically is short, a few days or weeks at most, if not shorter, to mitigate challenges regarding tracking of Users by malicious Relying Parties based on the repeated presentation of the same PID. On the other hand, the administrative validity period is typically at least a few years long. During the administrative validity period of a PID, the PID Provider will therefore provide multiple successive PIDs to a User, typically without any actions being expected from the User. However, when the administrative validity period of a PID ends, typically the User has to apply for an entirely new PID. |
| issuing_authority   | Name of the administrative authority that issued the person identification data, or the ISO 3166 alpha-2 country code of the respective Member State if there is no separate authority entitled to issue person identification data. TODO: Is name okay here, or do we want something like the EUID here if available?                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| issuing_country     | Alpha-2 country code, as specified in ISO 3166-1, of the country or territory of the provider of the person identification data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

### 2.6 Optional metadata specified in CIR 2024/2977

| **Data Identifier**  | **Definition**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| document_number      | A number for the person identification data, assigned by the provider of person identification data. **Further clarification added in this rulebook** This number is of administrative purpose for the issuer, and not relate to the status lists numbering.                                                                                                                                                                                                                                                                         |
| issuing_jurisdiction | Country subdivision code of the jurisdiction that issued the person identification data, as specified in ISO 3166-2:2020, Clause 8. The first part of the code shall be the same as the value for the issuing country.                                                                                                                                                                                                                                                                                                               |
| location_status      | The location of validity status information on the person identification data where the providers of person identification data revoke person identification data.                                                                                                                                                                                                                                                                                                                                                                   |
| trust_anchor        | This attribute indicates at least the URL at which a machine-readable version of the trust anchor to be used for verifying the PID can be found or looked up. *Note: This attribute corresponds to the location meant in Annex V point h) or Annex VII point h) of the [European Digital Identity Regulation], which is mandatory for QEAAs. This PID Rulebook adds this as an optional attribute for PIDs as well, so PID Providers are able to ensure that PIDs can be validated by Relying Parties in the same manner as QEAAs.*  |


### 2.7 Additional optional attributes specified in this Rulebook

| **Data Identifier** | **Definition**                                                                                                                                                                                                                                                                |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| issuance_date       | Date (and if possible time) when the person identification data was issued and/or the administrative validity period of the person identification data began. See also the clarification for expiry_date in [Section 2.5](#25-mandatory-metadata-specified-in-cir-20242977).  |

# 3 Attestation encoding

## 3.1 ISO/IEC 18013-5-compliant encoding
#### 3.1.1 Overview

The ISO/IEC 18013-5-compliant encoding of PID attributes and metadata is
specified in the table below. The table contains the following information for
all attributes:

- The first column lists the data identifier specified in
[Chapter 2](#2-attestation-attributes-and-metadata) above.
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

| **Data Identifier**            | **Attribute identifier**       | **Encoding format**                                                                                      |
|--------------------------------|--------------------------------|----------------------------------------------------------------------------------------------------------|
| family_name                    | family_name                    | ``tstr``                                                                                                 |
| given_name                     | given_name                     | ``tstr``                                                                                                 |
| birth_date                     | birth_date                     | ``full-date``, see [Section 3.1.4](#314-attribute-birth_date).                                           |
| birth_place                    | place_of_birth                 | ``place_of_birth``, see [Section 3.1.5](#315-attribute-place_of_birth).                                  |
| nationality                    | nationality                    | ``nationalities``, see [Section 3.1.2](#312-attribute-nationality).                                      |
| resident_address               | resident_address               | ``tstr``                                                                                                 |
| resident_country               | resident_country               | ``tstr``                                                                                                 |
| resident_state                 | resident_state                 | ``tstr``                                                                                                 |
| resident_city                  | resident_city                  | ``tstr``                                                                                                 |
| resident_postal_code           | resident_postal_code           | ``tstr``                                                                                                 |
| resident_street                | resident_street                | ``tstr``                                                                                                 |
| personal_administrative_number | personal_administrative_number | ``tstr``                                                                                                 |
| portrait                       | portrait                       | ``bstr``; see additional information in [Section 2.3](#23-optional-attributes-specified-in-cir-20242977) |
| family_name_birth              | family_name_birth              | ``tstr``                                                                                                 |
| given_name_birth               | given_name_birth               | ``tstr``                                                                                                 |
| sex                            | sex                            | ``uint``; see additional information in [Section 2.3](#23-optional-attributes-specified-in-cir-20242977) |
| email_address                  | email_address                  | ``tstr``                                                                                                 |
| mobile_phone_number            | mobile_phone_number            | ``tstr``                                                                                                 |
| attestation_legal_category     | attestation_legal_category     | ``tstr``                                                                                                 |
| expiry_date                    | expiry_date                    | ``tdate`` or ``full-date``                                                                               |
| issuing_authority              | issuing_authority              | ``tstr``                                                                                                 |
| issuing_country                | issuing_country                | ``tstr``                                                                                                 |
| document_number                | document_number                | ``tstr``                                                                                                 |
| issuing_jurisdiction           | issuing_jurisdiction           | ``tstr``                                                                                                 |
| location_status                | -                              | See [Section 3.1.3](#313-attribute-location_status).                                                     |
| issuance_date                  | issuance_date                  | ``tdate`` or ``full-date``                                                                               |
| trust_anchor                   | trust_anchor                   | ``tstr``                                                                                                 |

#### 3.1.2 Attribute nationality

The attribute nationality is encoded as a type ``nationalities``, i.e., an array of Alpha-2 country codes as specified in ISO 3166-1. Using CDDL notation as specified in RFC 8610, the
encoding of this attribute is:

``` cddl
nationalities = [+ CountryCode]

CountryCode = tstr ; Alpha-2 country code specified in ISO 3166-1
```

Note: If the User to whom the person identification data relates has multiple
nationalities (and the PID Provider is willing to attest to these multiple
nationalities), the PID Provider can include all the nationalities in the
nationality array. A potential drawback of this solution is that the User
cannot selectively disclose only one of these nationalities, since for ISO/IEC
18013-5-compliant attestations, always the entire array will be presented if the
User approves the presentation of the nationality attribute. A potential
solution to this challenge is for the PID Provider to include only one
nationality in the nationality attribute, and for the remaining nationalities
use one or more domestic data attributes specified according to requirement
PID_06 in [Annex 2, Topic 3](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/).

#### 3.1.3 Attribute location_status

For ISO/IEC 18013-5-compliant PIDs, the attribute location_status is
absent, since the PID issuer will add revocation information, if needed, to the MSO as specified in [ISO/IEC 18013-5].

#### 3.1.4 Attribute birth_date

For PIDs compliant with ISO/IEC 18013-5, dates are encoded as specified in RFC 8943. This encoding does not contain provisions for encoding partial dates. This may cause challenges in case the birthdate of a User is not (fully) known. To deal with such cases, a PID Provider could adopt a policy to choose appropriate values for the unknown date elements. However, mandating such a policy is out of the scope of this document.

#### 3.1.5 Attribute place_of_birth

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

### 3.1.6 Example mdoc

TODO: Provide an illustrative mdoc (ISO/IEC 18013-5) example showing a PID with representative attributes and their encoding.

## 3.2 SD-JWT VC-based encoding of PID

### 3.2.1 Overview

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
| portrait              | picture                  | string              | data URL containing the base64-encoded portrait in JPEG format according to PID_03 in [Annex 2, Topic 3](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/)                                                                                                                                                 |

Note: The standard JWT claims nbf and exp are used to express the technical validity period of a SD-JWT VC-compliant PID.

The following Private Names specific to the attestation type defined in this document are to be used for PIDs:

| **Data Identifier**            | **Attribute identifier**       | **Encoding format** | **Notes**                                                                                                                                                                    |
|--------------------------------|--------------------------------|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| attestation_legal_category     | attestation_legal_category     | string              | SHALL be one of QEAA, PUB-EAA or EAA                                                                                                                                                               |
| expiry_date                    | date_of_expiry                 | string              | ISO 8601-1 [ISO8601‑1] YYYY-MM-DD format, as defined in Section 5.4.4.2 of [EKYC Schema]                                                                                     |
| issuance_date                  | date_of_issuance               | string              | ISO 8601-1 [ISO8601‑1] YYYY-MM-DD format, as defined in Section 5.4.4.2 of [EKYC Schema]                                                                                     |
| personal_administrative_number | personal_administrative_number | string              |                                                                                                                                                                              |
| sex                            | sex                            | number              | numeric encoding as described in [Section 2.3](#23-optional-attributes-specified-in-cir-20242977); gender from [OIDC] uses a different value range and is therefore not used |
| issuing_authority              | issuing_authority              | string              |                                                                                                                                                                              |
| issuing_country                | issuing_country                | string              |                                                                                                                                                                              |
| document_number                | document_number                | string              |                                                                                                                                                                              |
| issuing_jurisdiction           | issuing_jurisdiction           | string              |                                                                                                                                                                              |
| status                         | status                         | JSON object         | See [Section 3.2.2](#322-attribute-status)                                                                                                                                   |
| trust_anchor                   | trust_anchor                   | string              |                                                                                                                                                                              |

### 3.2.2 Attribute status

For SD-JWT VC-compliant PIDs, the PID MUST include a `status` claim if the technical validity period is greater than 25 hours. This claim enables Relying Parties to determine if a credential has been revoked via a status list mechanism, as specified in [SD-JWT VC](https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/12/).

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

### 3.2.3 Note on VCT

SD-JWT VC defines the Verifiable Credential Type (`vct`). A type comes
with associated metadata that, for instance, provides information about
the type itself, outlines a schema detailing the claims that are
optional or mandatory in the SD-JWT VC, and specifies their display
methods. Additionally, a type can extend another type, enabling
the creation of domestic types based on a common EU-wide type, while preserving
the mandatory claims from the base type. Domestic
types MAY, however, define additional claims and display information. Details
are defined in [SD-JWT VC].

This document defines the base type to be "urn:eudi:pid:1". As a convention, all
PIDs must use types in the namespace "urn:eudi:pid:".

SD-JWT VC specifies Type Metadata as a machine-readable format for information
regarding a type, including the information on claims such as what is contained
in this document. Requirement PID_15 in [Annex 2, Topic 3](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/) requires that the information on the
common EU-wide type as well as on any domestic types is published and
accessible in a catalogue.

**Further clarification added in this rulebook for WE BUILD**: We encourage the use of the EUDI standard for WE BUILD Pilots, over national standards and extensions.

### 3.3 SD-JWT version 
For WE BUILD we focus on following the sd-jwt standard draft version 12, [which can be found here](https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/12/)

### 3.4 Example

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

## 4 Attestation usage

TODO: WE BUILD WP4 - PID/EBW-OID group task 3?

## 5 Trust anchors

TODO: WE BUILD WP4 - Trust Registry Infrastucture / Architecture group?

## 6 Revocation

PIDs MAY be either (a) short-lived and non-revocable, or (b) long-lived and revocable, in line with ARF Annex 2 Topic 7.

Revocation strategy:
- A PID Provider SHALL use one of the following approaches:
  - Issue short-lived PIDs with a technical validity period of 24 hours or less; or
  - Support revocation using an Attestation Status List (ASL) or Attestation Revocation List (ARL) mechanism.
- If a PID is revocable, the PID Provider SHALL be the only party responsible for executing revocation of that PID, and SHALL NOT reverse revocation once executed.
- The PID Provider MAY support temporary suspension before permanent revocation, with a maximum suspension period defined in the revocation policy.
- The PID Provider SHALL maintain a revocation policy specifying under which conditions it revokes a PID (e.g. compromise, attribute changes, explicit User request, death of the subject), notification procedures for Users, and User rights including the right to request revocation at any time.

Technical mechanisms:
- For SD-JWT VC-based PIDs, revocation is expressed via the `status` claim (see Section 3.2.2) using the status-list mechanism.
- For ISO/IEC 18013-5-compliant PIDs, revocation information is provided via the MSO as defined in ISO/IEC 18013-5; no `location_status` attribute is used (see Section 3.1.3).

Relying Party (RP) checks:
- A Relying Party Instance SHOULD verify revocation status when the PID is revocable, and SHALL perform a risk analysis if it decides not to.
- Relying Parties SHOULD NOT fetch status information at presentation time. Instead, they SHOULD periodically retrieve and cache the relevant ASL/ARL and distribute it to their Relying Party Instances.
- If reliable revocation information is unavailable or indeterminate, the RP SHALL decide whether to accept or refuse the PID based on its risk analysis. The RP SHALL log such incidents and MAY report recurring failures to the PID Provider.
- Revocation status checking SHALL be designed to prevent correlation of User identity across Relying Parties (e.g., using batch status lists rather than per-credential status endpoints).

Timing:
- Where revocation is supported, the PID Provider SHOULD ensure that revocation is reflected in published status information within 24 hours of the revocation decision.
- For emergency revocations (e.g., security compromise), the PID Provider SHOULD propagate revocation within a shorter timeframe where technically feasible.

## 7 Compliance


## 8 References

| **Item Reference**                     | **Standard name/details**                                                                                                                                                                                                                                                                          |
|----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [European Digital Identity Regulation] | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework                           |
| [ISO/IEC 18013-5]                      | ISO/IEC 18013-5, Personal identification --- ISO-compliant driving licence - Part 5: Mobile driving licence (mDL) application, First edition, 2021-09                                                                                                                                              |
| [OIDC]                                 | Sakimura, N. et al., "OpenID Connect Core 1.0", OpenID Foundation. Available: <https://openid.net/specs/openid-connect-core-1_0.html>                                                                                                                                                              | 
| [EKYC]                                 | OpenID Connect for Identity Assurance Claims Registration <https://openid.net/specs/openid-connect-4-ida-claims-1_0-final.html#ICAO-Doc9303>                                                                                                                                                       |
| [SD-JWT VC]                            | SD-JWT-based Verifiable Credentials (SD-JWT VC). Available: <https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/>, version draft-ietf-oauth-sd-jwt-vc-09                                                                                                                                  |
| [Topic 3]                              | ARF Annex 2 - Topic 3 - Attestation revocation and revocation checking Available: <https://eudi.dev/latest/annexes/annex-2/annex-2.02-high-level-requirements-by-topic/> |
| [Topic 12]                             | ARF Annex 2 - Topic 12 - Attestation Rulebooks, Available: <https://eudi.dev/latest/annexes/annex-2/annex-2.02-high-level-requirements-by-topic/>                                               |
| [W3C VCDM v2.0]                        | Sporny, M. *et al,* Verifiable Credentials Data Model v2.0, W3C Recommendation.                                                                                                                                                                                                                    |

For further references please see [ARF Chapter 10](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/architecture-and-reference-framework-main.md#10-references) of the ARF main document.

