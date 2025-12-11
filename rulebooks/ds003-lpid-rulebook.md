# Attestation Rulebook for attestations of type LPID (Legal Person Identification Data)

*Provide information about the author(s) of this Rulebook in the following form:*

* Author(s): 
    <!-- Usage help: (Name LastName, Affiliation) -->
  * Jonas Toennis , [Brønnøysund Registry Center](https://www.brreg.no)



*Provide versioning information about the Rulebook in the following form:*

| Version          | Date               | Description                                                                        |
|------------------|--------------------|------------------------------------------------------------------------------------|
| 0.1.0            | 06.11.2025         | Initial Description based on the IS 2024/2977, Potential Rulebook and EWC rulebook |
|0.9.0| 2025-12-12  | Feedback of WeBuild WP 4 Task 2 implemented                                        |


**Feedback:**
Main feedback channel: [GitHub issues](https://github.com/webuild-consortium/eudi-wallet-rulebooks-and-schemas/issues)
Alternative: Contact workpackage 4 in WE BUILD, or/and the author of the document.


## 1 Introduction

### 1.1 Document scope and purpose

The Legal Person Identification Data (LPID) attestation defines a legally defined, common set of data that uniquely identifies a legal person within the EUDI Wallet ecosystem. Its purpose is to provide a harmonised, interoperable attestation that enables Relying Parties to establish trust in a legal person entity. LPID focuses on the core identifiers needed across cross-border use cases while keeping the attestation stable and low‑revocation.

Primary objectives:
- Provide a cross‑border unique identifier for the legal person (EUID) and the legal person's name(s).
- Support verification of issuer authenticity and attestation integrity based on the Implementing Act and ARF trust requirements.
- Enable consistent consumption in EUDI Wallet flows as a Public‑Body Electronic Attestation of Attributes (PuB‑EAA) aligned with [Annex VII Eidas](https://eur-lex.europa.eu/eli/reg/2014/910/2024-10-18/eng#anx_VII).


### 1.2 Document structure

This Rulebook is structured as follows:
- Chapter 2 defines the LPID attestation attributes and metadata in an encoding‑independent manner.
- Chapter 3 specifies encodings. LPID is profiled for SD‑JWT VC and W3C VCDM; ISO/IEC 18013‑5 is out of scope for LPID.
- Chapter 4 defines the intended usage patterns and Relying Party obligations.
- Chapter 5 defines trust anchors and how Relying Parties verify LPID issuers.
- Chapter 6 defines revocation approaches.
- Chapter 7 states compliance to the EUDI framework and applicable regulations.


### 1.3 Keywords

*The following are the recommended keywords. Modify if necessary*

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

The terminology is extended as follows:

| Term                      | Definition in WE BUILD Context                                                                                                    |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Legal Person/Legal Entity | A self-employed person, company, or organization that has legal rights and obligations. [Following the EU Core business vocabulary](https://semiceu.github.io/Core-Business-Vocabulary/releases/2.2.0/#LegalEntity) |

## 2 Attestation attributes and metadata

*This section is used for defining all attributes that an
attestation of the defined type may contain. In this section
the attributes SHALL be defined in an encoding-independent manner (see ARB_06 in [Topic 12]). 
Each attribute can be mandatory, optional, or conditional, 
and it SHALL be specified in the corresponding section (see ARB_09 in [Topic 12]).*

*When attributes are defined, referring to attributes that
already exist in a catalogue of attestation attributes 
SHOULD be considered (see ARB_07 in [Topic 12]).*

*[Topic 12] of Annex 2 of the ARF defines the following High-Level Requirements with
respect to the Attestation Rulebooks*

**Requirements for QEAA**
* An attribute as meant in Annex V point a) of the [European Digital Identity Regulation] 
SHALL be included (see ARB_11 in [Topic 12]). See also [Section 2.1](#21-introduction).
* One or more attributes or metadata representing the set of data meant in Annex 
V point b) of the [European Digital Identity Regulation] SHALL be included (see ARB_13 in [Topic 12])
* One or more attributes representing the set of data meant in Annex V point c)  
of the [European Digital Identity Regulation] SHALL be included (see ARB_16 in [Topic 12]).
* One or more attributes or metadata representing the set of data meant in Annex V point e) 
of the [European Digital Identity Regulation] SHALL be included (see ARB_18 in [Topic 12]).
* One or more attributes or metadata representing the location meant in Annex V point h)
of the [European Digital Identity Regulation] SHALL be included. This location SHALL 
indicate at least the URL at which a machine-readable version of the trust anchor to be
used for verifying the QEAA can be found or looked up (see ARB_20 in [Topic 12])

**Requirements for PuB-EAA**
* Αn attribute as meant in Annex VII point a) of the [European Digital Identity Regulation] 
SHALL be included (see ARB_11 in [Topic 12]). See also [Section 2.1](#21-introduction).
* Οne or more attributes or metadata representing the set of data meant in Annex
 VII point b) of the [European Digital Identity Regulation] SHALL be included (see ARB_14 in [Topic 12]).
* Οne or more attributes representing the set of data meant in Annex VII point c) 
of the [European Digital Identity Regulation] SHALL be included (see ARB_16 in [Topic 12]).
* Οne or more attributes or metadata representing the set of data meant in Annex VII point e)
of the [European Digital Identity Regulation] SHALL be included (see ARB_18 in [Topic 12]).
* one or more attributes or metadata representing the location meant in Annex VII point h)
of the [European Digital Identity Regulation] SHALL be included. This location SHALL 
indicate at least the URL at which a machine-readable version of the qualified 
certificate that signed the PuB-EAA can be found or looked up. (see ARB_20 in [Topic 12]) 

**Requirements for non-qualified EAA**
* An attribute indicating that the attestation is an EAA should be included (see ARB_12 in [Topic 12]).
See also [Section 2.1](#21-introduction).
* Οne or more attributes or metadata representing the set of data meant in Annex 
V point b) of the [European Digital Identity Regulation] SHALL be included (see ARB_15 in [Topic 12]).
* Οne or more attributes representing the set of data meant in Annex V point c) of the 
[European Digital Identity Regulation] SHOULD be included (see ARB_17 in [Topic 12])
* Οne or more attributes representing the set of data meant in Annex V point e) of 
the [European Digital Identity Regulation] SHOULD be defined (see ARB_19 in [Topic 12]).
 * Οne or more attributes or metadata representing the location at which a machine-readable 
version of the trust anchor to be used for verifying the EAA can be found or
looked up SHOULD be defined. What this location indicates precisely is dependent 
on the nature of the mechanism used for distributing trust anchors, detailed in section 
5 (see ARB_21 in [Topic 12])

### 2.1 Introduction

The Legal Person Identification Data (LPID) is a structured digital attribute designed to uniquely and verifiably identify legal entities—such as companies, foundations, and public institutions—within the European Digital Identity ecosystem in both national and cross-border digital interactions. It encapsulates a claim (e.g. “I am a registered business”), metadata about the source of that claim (such as the registry where the entity is listed), and cryptographic assurances that validate the claim’s authenticity and issuer1. LPIDs 'SHOULD' be issued in SD-JWT and or W3C VCDM.
This rulebook defines in this chapter the legally required minimum attributes, as well as the legally optional attributes. National adoptions can be done by allowing for national extensions to meet domestic needs. 


**In the WE BUILD context**, LPIDs can be issued to any Legal Entity, provided the operator is registered in an authentic source (such as government entities, Company branches and other). 

All data identifiers and definitions in this chapter are independent of any
encoding used. Consequently,

- the data identifiers in these tables are not necessarily the same as the
  attribute identifiers used for LPIDs complying
  with [ISO/IEC 18013-5]. [Chapter 3.1](#31-isoiec-18013-5-compliant-encoding) specifies the attribute
  identifiers to be used for LPIDs in [ISO/IEC 18013-5] format
- the data identifiers in these tables are not necessarily the same as the claim
  names used for LPIDs complying with [SD-JWT VC]. [Chapter 3.2](#32-sd-jwt-vc-based-encoding) specifies the claim names to be
  used for such LPIDs.



### 2.2 Mandatory attributes specified in CIR 2024/2977

| **Data Identifier**  | **Definition**                                                                                                                                                                                                                                                                                                                            |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name                 | The current, registered name of the Legal Person                                                                                                                                                                                                                                                                                          |
| id                   | A unique identifier constructed by the sending Member State in accordance with the technical specifications for the purposes of cross-border identification and which is as persistent as possible in time **In WE BUILD context** we use the EUID as identificator if available, or a similar constructed, unique per issuer identifier. |



### 2.3 Optional attributes specified in CIR 2024/2977

| **Data Identifier**          | **Definition**                                                                                                 |
|------------------------------|----------------------------------------------------------------------------------------------------------------|
| address                      | The officially registered business address of the company, as recorded with government authorities.            | 
| vat                          | VAT registration number                                                                                        |
| tin                          | tax reference number, and registered for TIN if possible                                                       |
| euid                         | European unique identifier referred to in Directive (EU) 2017/1132 of the European Parliament and  of the Council |
| lei                          | Legal Entity Identifier (LEI) referred to in Commission Implementing Regulation (EU) 2022/1860                 |
| eori                         | Economic Operator Registration and Identification (EORI) referred to in Commission Implementing  Regulation (EU) No 1352/2013 |
| excise                       | excise number provided in Article 2(12) of Council Regulation (EU) No 389/2012                                 |

### 2.4 Mandatory metadata specified in CIR 2024/2977

| **Data Identifier**  | **Definition**                                                                                                                                                                                                                        |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| expiry_date          | Date (and if possible time) when the person identification data will expire.                                                                                                                                                          |
| issuing_authority    | Name of the administrative authority that issued the person identification data, or the ISO 3166 alpha-2 country code of the respective Member State if there is no separate authority entitled to issue person identification data.  |
| issuing_country      | Alpha-2 country code, as specified in ISO 3166-1, of the country or territory of the provider of the person identification data.                                                                                                      |


### 2.5 Optional metadata specified in CIR 2024/2977

| **Data Identifier**  | **Definition**                                                                                                                                                                                                                                                      |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| document_number      | A number for the person identification data, assigned by the provider of legal person identification data.  **Further clarification added in this rulebook** This number is of administrative purpose for the issuer, and not relate to the status lists numbering. |
| issuing_jurisdiction | Country subdivision code of the jurisdiction that issued the person identification data, as specified in ISO 3166-2:2020, Clause 8. The first part of the code shall be the same as the value for the issuing country.                                              |
| location_status      | The location of validity status information on the person identification data where the providers of person identification data revoke person identification data.                                                                                                  |

### 2.6 Additional conditional attributes specified in this Rulebook

| **Data Identifier**  | **Definition**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| trust_anchor         | This attribute indicates at least the URL at which a machine-readable version of the trust anchor to be used for verifying the LPID can be found or looked up. *Note: This attribute corresponds to the location meant in Annex V point h) or Annex VII point h) of the [European Digital Identity Regulation], which is mandatory for QEAAs. This LPID Rulebook adds this as an optional attribute for LPIDs as well, so LPID Providers are able to ensure that LPIDs can be validated by Relying Parties in the same manner as QEAAs. This attribute is also required when the * |


# 3 Attestation encoding

## 3.1 ISO/IEC 18013-5-compliant encoding

Out of scope. LPID is defined only for SD‑JWT VC in this Rulebook. No ISO/IEC 18013‑5 mdoc encoding is defined for LPID, as offline proximity presentation is not a current requirement for LPID.

## 3.2 SD-JWT VC-based encoding


Verifiable Credential Type (vct): `uri:eu.eudi.lpid.1`

Claim names and disclosure policy (aligned with Chapter 2 attributes):

| Data Identifier      | Attribute Identifier | Encoding format | Reference/Notes                                                                                                                                                                                              |
|----------------------|----------------------|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                   | id                   | string          | Cross-border unique identifier. In WE BUILD context, EUID if available, or a similar constructed, unique per issuer identifier.                                                                              |
| name                 | name                 | string          | Registered legal name of the Legal Person.                                                                                                                                                                   |
| expiry_date          | date_of_expiry       | string          | ISO 8601-1 [ISO8601‑1] YYYY-MM-DD format, as defined in Section 5.4.4.2 of [EKYC Schema]                                                                                                                     |
| issuing_authority    | issuing_authority    | string          | Name of the administrative authority or ISO 3166-1 alpha-2 of Member State if no separate body.                                                                                                              |
| issuing_country      | issuing_country      | string          | ISO 3166‑1 alpha‑2 code of the provider’s country/territory.                                                                                                                                                 |
| document_number      | document_number      | string          | Administrative number assigned by the provider; not related to status list numbering.                                                                                                                        |
| issuing_jurisdiction | issuing_jurisdiction | string          | ISO 3166‑2 subdivision code; first part equals issuing country.                                                                                                                                              |
| location_status      | status               | JSON Object     | Se Section [Section 3.2.1](#321-attribute-status)                                                                                                                                                            |
| trust_anchor         | trust_anchor         | string (URI)    | URL of machine‑readable trust anchor as per Annex V/VII point h).                                                                                                                                            |
| address              | address              | Json Object     | The full, registered business address, following the [OIDC section 5.1.1](https://openid.net/specs/openid-connect-core-1_0-final.html#AddressClaim) definintion. See [Section 3.2.2](#322-attribute-address) |
| vat                  | vat                  | string          | VAT registration number.                                                                                                                                                                                     |
| tin                  | tin                  | string          | Tax reference number.                                                                                                                                                                                        |
| euid                 | euid                 | string          | European Unique Identifier (EUID as used by BRIS).                                                                                                                                                           |
| lei                  | lei                  | string          | Legal Entity Identifier (LEI).                                                                                                                                                                               |
| eori                 | eori                 | string          | Economic Operator Registration and Identification (EORI).                                                                                                                                                    |
| excise               | excise               | string          | Excise number.                                                                                                                                                                                               |

Selective Disclosure: Core identity claims of LPID (`id`, `name`) SHALL NOT be selectively disclosable to preserve the atomic nature of LPID. Other attributes MAY be selectively disclosable, according to issuer policy. This remains technically compatible with SD‑JWT VC while enforcing the atomic presentation requirement for LPID.


### 3.2.1 Attribute status
For SD-JWT VC-compliant LPIDs, the LPID MUST include a status claim if the technical validity period is greater than 24 hours. This claim enables Relying Parties to determine if a credential has been revoked via a status list mechanism, as specified in [SD-JWT VC](https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/12/).

The status claim SHALL be a JSON object with the following members:

* 'type' (string): SHALL be "status-list".
* 'status_list_credential' (string, URI): The URI of the Status List Credential document that contains the status bitstring.
* 'status_list_index' (integer, >= 0): The zero-based index into the status list bitstring that corresponds to this credential.
* 'status_purpose' (string): SHALL be "revocation" for this PID.

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

### 3.2.2 Attribute address

The address attribute follows the OpenID Connect Core 1.0 address claim structure defined
in [OIDC section 5.1.1](https://openid.net/specs/openid-connect-core-1_0-final.html#AddressClaim). It is represented as
a JSON object containing the following fields:

| Field          | Type   | Description                                               |
|----------------|--------|-----------------------------------------------------------|
| street_address | string | Full street address component                             |
| house_number   | string | House number component                                    |
| locality       | string | City or locality component                                |
| region         | string | State, province, prefecture, or region component          |
| postal_code    | string | Zip or postal code component                              |
| country        | string | Country component as ISO 3166-1 alpha-2 code              |
| formatted      | string | Full mailing address with all components in correct order |

Example:

```json
{
  "address": {
    "street_address": "123 Via Appia",
    "house_number": "123",
    "locality": "Rome", 
    "region": "Lazio",
    "postal_code": "00100",
    "country": "IT",
    "formatted": "123 Via Appia 123, 00100 Rome, Lazio, IT"
  }
}
```

### 3.3 Example

Illustrative examples:
- Example claim set (human‑readable):
```json
{
  "vct": "uri:eu.eudi.lpid.1",
  "id": "NOFOR.123456789",
  "name": "Example AS",
  "issuing_authority": "Brønnøysundregistrene",
  "issuing_country": "NO",
  "date_of_expiry": "2026-12-31",
  "trust_anchor": "https://tl.eidas.europa.eu/tl-browser/#/",
  "document_number": "LPID-2025-000123",
  "issuing_jurisdiction": "NO-03",
  "status": {
    "type": "status-list",
    "status_list_credential": "https://issuer.example.no/status/1",
    "status_list_index": 42,
    "status_purpose": "revocation"
  },
  "cnf": {
    "jwk": {
        "kty": "EC",
        "crv": "P-256",
        "x": "52aDI_ur05n1f_p3jiYGUU82oKZr3m4LsAErM536crQ",
        "y": "ckhZ-KQ5aXNL91R8Eufg1aOf8Z5pZJnIvuCzNGfdnzo"
    }
  }
}
```
Note: The `cnf` claim is used for expressing key binding in SD-JWT VCs.
The example above shows a public key in JWK format.

Note: Additional technical claims are not shown here, including
references to the issuer and more.




## 3.3 W3C Verifiable Credentials Data Model-based encoding

TODO: Add W3C VC encoding.

## 4 Attestation usage

TODO: WE BUILD WP4 - PID/LPID group task 3?


Primary use cases:
- Proving the legal identity of an organisation (holder) to a Relying Party in national and cross‑border digital services.
- Establishing a trust context for additional legal‑person attestations that reference the LPID EUID.

Relying Party obligations:
- Verify the SD‑JWT VC signature and ensure the issuer is an authorised public body by validating the qualified certificate chain against the appropriate QTSP Trusted List (see Chapter 5).
- Check freshness: validate `exp` and consider `iat` and policy‑defined maximum age.
- Apply revocation/status checks as defined in Chapter 6.
- Where the transaction requires binding to a natural person representative, the RP SHOULD request and verify a PID for the representative in addition to the LPID, as per service policy and ARF Topic 12 (ARB_27).

Presentation requirements:
- Online presentation over OpenID4VP is RECOMMENDED; LPID is not specified for offline proximity modes.
- Selective disclosure is NOT permitted for the core LPID attributes; the holder presents LPID atomically.

Transactional data:
- The RP MAY keep minimal logs necessary to demonstrate lawful processing and verification events; no additional transaction‑specific attributes are introduced by LPID.

## 5 Trust anchors

TODO: WE BUILD WP4 - Trust Registry Infrastucture / Architecture group? 


For LPID as a PuB‑EAA, Relying Parties SHALL verify the LPID using the public‑body issuer certificate issued by a Qualified Trust Service Provider (QTSP), and SHALL verify the QTSP certificate chain up to the trust anchor present in the QTSP Trusted List.

Verification steps:
1) Verify the SD‑JWT VC signature over the LPID using the issuer certificate.
2) Build and validate the certificate chain from the issuer certificate to a QTSP trust anchor listed in the appropriate Trusted List.
3) Validate certificate status (validity, revocation) per eIDAS trust list rules.
4) Use the `trust_list_location` metadata to discover the appropriate Trusted List or machine‑readable pointer.

Issuers MAY use intermediate signing certificates. RPs SHALL handle such chains. The trust model is equivalent to Annex VII for PuB‑EAA.




## 6 Revocation

TODO: WE BUILD WP4 - PID/LPID group task 5

LPIDs are expected to be long‑lived but revocable. This Rulebook adopts the following policy:
- LPIDs SHALL include `exp`. Validity longer than 24 hours is permitted; therefore, revocation MUST be supported.
- When the Commission specifies the Attestation Status List (ASL) or Attestation Revocation List (ARL) mechanism, LPID Providers SHALL implement that mechanism.
- Until such mechanisms are specified, LPID Providers SHALL publish revocation status via a machine‑readable endpoint referenced from the issuer’s policy, and Relying Parties SHALL implement status checking per that policy.

Relying Party checks:
- Validate `exp` not in the past.
- Query the designated ASL/ARL (or interim status endpoints) to determine the current status.
- Treat any indeterminate status as non‑valid per risk policy.


## 7 Compliance



## 8 References
| **Item Reference**                     | **Standard name/details**                                                                                                                                                                                                                                                                           |
|----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [European Digital Identity Regulation] | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework                            |
| [HAIP]                                 | Yasuda, K. *et al,* OpenID4VC High Assurance Interoperability Profile, OpenId Foundation, Version draft-03                                                                                                                                                                                          |
| [IANA-JWT-Claims]                      | IANA JSON Web Token Claims Registry. Available: <https://www.iana.org/assignments/jwt/jwt.xhtml>                                                                                                                                                                                                    |
| [ISO/IEC 18013-5]                      | ISO/IEC 18013-5, Personal identification --- ISO-compliant driving licence - Part 5: Mobile driving licence (mDL) application, First edition, 2021-09                                                                                                                                               |
| [OIDC]                                 | Sakimura, N. et al., "OpenID Connect Core 1.0", OpenID Foundation. Available: <https://openid.net/specs/openid-connect-core-1_0.html>                                                                                                                                                               |
| [RFC 3339]                             | RFC 3339  - Date and Time on the Internet: Timestamps, G. Klyne et al., July 2002                                                                                                                                                                                                                   |
| [RFC 8610]                             | RFC 8610  - Concise Data Definition Language (CDDL): A Notational Convention to Express Concise Binary Object Representation (CBOR) and JSON Data Structures, H. Birkholz et al., June 2019                                                                                                         |
| [RFC 8943]                             | RFC 8943  - Concise Binary Object Representation (CBOR) Tags for Date, M. Jones et al., November 2020                                                                                                                                                                                               |
| [RFC 8949]                             | RFC 8949 - Concise Binary Object Representation (CBOR), C. Bormann et al., December 2020                                                                                                                                                                                                            |
| [SD-JWT VC]                            | SD-JWT-based Verifiable Credentials (SD-JWT VC). Available: <https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/>, version draft-ietf-oauth-sd-jwt-vc-09                                                                                                                                   |
| [Topic 7]                              | ARF Annex 2 - Topic 7 - Attestation revocation and revocation checking Available: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a237-topic-7-attestation-revocation-and-revocation-checking>  |
| [Topic 10]                             | ARF Annex 2 - Topic 10 - Issuing a PID or attestation to a Wallet Unit: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a2310-topic-10-issuing-a-pid-or-attestation-to-a-wallet-unit>           |
| [Topic 12]                             | ARF Annex 2 - Topic 12 - Attestation Rulebooks, Available: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a2312-topic-12-attestation-rulebooks>                                                |
| [Topic 20]                             | ARF Annex 2 - Strong User authentication for electronic payments, Available: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a2320-topic-20-strong-user-authentication-for-electronic-payments> |
| [W3C VCDM v2.0]                        | Sporny, M. *et al,* Verifiable Credentials Data Model v2.0, W3C Recommendation.                                                                                                                                                                                                                     |








 
