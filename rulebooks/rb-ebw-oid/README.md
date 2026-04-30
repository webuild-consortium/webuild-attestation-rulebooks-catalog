# Attestation Rulebook for attestations of type EBW‑OID (European Business Wallet – Owner Identification Data)

*Provide information about the author(s) of this Rulebook in the following form:*

* Author(s): 
    <!-- Usage help: (Name LastName, Affiliation) -->
  * Jonas Toennis , [Brønnøysund Registry Center](https://www.brreg.no)



*Provide versioning information about the Rulebook in the following form:*

| Version | Date       | Description                                                                                                                                                              |
|---------|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0.9.1   | 13.02.2026 | EBW‑OID created based on the [EBW proposal (Articles 8–9)](https://digital-strategy.ec.europa.eu/en/library/proposal-regulation-establishment-european-business-wallets) plus feedback from semantics.|


**Feedback:**
Main feedback channel: [GitHub issues](https://github.com/webuild-consortium/eudi-wallet-rulebooks-and-schemas/issues)
Alternative: Contact workpackage 4 in WE BUILD, or/and the author of the document.


## 1 Introduction

### 1.1 Document scope and purpose

The European Business Wallet – Owner Identification Data (EBW‑OID) attestation defines a legally defined, common set of data that uniquely identifies an EBW owner (economic operator or public sector body) within the European Business Wallets (EBW) ecosystem. Its purpose is to provide a harmonised, interoperable attestation that enables Relying Parties and business wallets to establish trust in an EBW owner entity. EBW‑OID focuses on the core identifiers needed across national and cross‑border use cases.

Primary objectives:
- Provide a cross‑border unique identifier for the EBW owner (In **WEBUILD** EUID where available, otherwise a similar constructed, unique per issuer identifier. <Countrycode ISO 3166-1 alpha-2><Issuer-reference>.<unique identificator> eks. SEBOLREG.123456789 ) and the official name of the EBW owner.
- Serving as the activation and ownership attestation enabler for the EBW.
- Support verification of issuer authenticity and attestation integrity based on the EBW proposal (Articles 8–9) and ARF trust requirements.
- Enable consistent consumption in EBW and EUDI flows as Electronic Attestations of Attributes (QEAA/Pub-EAA) aligned with applicable implementing acts.


### 1.2 Document structure

This Rulebook is structured as follows:
- Chapter 2 defines the EBW‑OID attestation attributes and metadata in an encoding‑independent manner.
- Chapter 3 specifies encodings. EBW‑OID is profiled for SD‑JWT VC and W3C VCDM; ISO/IEC 18013‑5 is out of scope for EBW‑OID.
- Chapter 4 defines the intended usage patterns and Relying Party obligations.
- Chapter 5 defines trust anchors and how Relying Parties verify EBW‑OID issuers.
- Chapter 6 defines revocation approaches.
- Chapter 7 states compliance to the EUDI framework and applicable regulations.


### 1.3 Keywords

This document uses the capitalised keywords 'SHALL', 'SHOULD' and 'MAY' as specified in [RFC 2119], i.e. to indicate requirements, recommendations and options specified in this document.

In addition, 'must' (non-capitalised) is used to indicate an external constraint, i.e. a requirement that is not mandated by this document, but, for instance, by an external document. The word 'can' indicates a capability, whereas other words, such as 'will', and 'is' or 'are' are intended as statements of fact.

### 1.4 Terminology

This document uses the terminology specified in [Annex 1](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-1/annex-1-definitions/) of the ARF.

The terminology is extended as follows:

| Term               | Definition in WE BUILD Context                                                                                                                                                                                                |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EBW                | European Business Wallet                                                                                                                                                                                                      |
| EBW owner          | An economic operator or public sector body that owns an EBW, including Union entities; corresponds to the bearer of EBWOID.                                                                                                  |
| EWBOID            | European Business Wallet owner identification data. a set of data that enables the establishment of the identity of a European Business Wallet owner                                                                          |
| economic operator  | any natural or legal person, or a group of such persons, including temporary associations of undertakings, acting in a commercial or professional capacity for purposes related to their trade, business, craft or profession |

For more terminology, please refer to Article 3 of the legislation draft [COM 2025/838](https://digital-strategy.ec.europa.eu/en/library/proposal-regulation-establishment-european-business-wallets)

## 2 Attestation attributes and metadata

**Requirements for the EBWOID QEAA**
* An attribute as meant in Annex V point a) of the [European Digital Identity Regulation] SHALL be included (see ARB_11 in [Topic 12]). See also [Section 2.1](#21-introduction).
* One or more attributes or metadata representing the set of data meant in Annex V point b) of the [European Digital Identity Regulation] SHALL be included (see ARB_13 in [Topic 12])
* One or more attributes representing the set of data meant in Annex V point c) of the [European Digital Identity Regulation] SHALL be included (see ARB_16 in [Topic 12]).
* One or more attributes or metadata representing the set of data meant in Annex V point e) of the [European Digital Identity Regulation] SHALL be included (see ARB_18 in [Topic 12]).
* One or more attributes or metadata representing the location meant in Annex V point h) of the [European Digital Identity Regulation] SHALL be included. This location SHALL 
indicate at least the URL at which a machine-readable version of the trust anchor to be used for verifying the QEAA can be found or looked up (see ARB_20 in [Topic 12])

**Requirements for PuB-EAA**
* Αn attribute as meant in Annex VII point a) of the [European Digital Identity Regulation] SHALL be included (see ARB_11 in [Topic 12]). See also [Section 2.1](#21-introduction).
* Οne or more attributes or metadata representing the set of data meant in Annex VII point b) of the [European Digital Identity Regulation] SHALL be included (see ARB_14 in [Topic 12]).
* Οne or more attributes representing the set of data meant in Annex VII point c) of the [European Digital Identity Regulation] SHALL be included (see ARB_16 in [Topic 12]).
* Οne or more attributes or metadata representing the set of data meant in Annex VII point e) of the [European Digital Identity Regulation] SHALL be included (see ARB_18 in [Topic 12]).
* one or more attributes or metadata representing the location meant in Annex VII point h) of the [European Digital Identity Regulation] SHALL be included. This location SHALL 
indicate at least the URL at which a machine-readable version of the qualified certificate that signed the PuB-EAA can be found or looked up. (see ARB_20 in [Topic 12]) 


### 2.1 Introduction

The EBW Owner Identification Data (EBWOID) is a structured digital attribute designed to uniquely and verifiably identify economic operators and public sector bodies—within the EBW ecosystem in both national and cross‑border digital interactions. It encapsulates a claim (e.g. “This is the official name and unique identifier of the EBW owner”), metadata about the source of that claim (such as the registry or official record), and cryptographic assurances that validate the claim’s authenticity and issuer. EBWOIDs SHOULD be issued in SD‑JWT and/or W3C VCDM formats as Pub-EAAs/QEAAs.
This chapter defines the legally required minimum attributes, as well as optional attributes.


**In the WE BUILD context**, EBWOIDs can be issued for any EBW owner, provided the attributes are derived from authentic sources notified to the Commission (EBW Article 8(2)). 

All data identifiers and definitions in this chapter are independent of any encoding used. Consequently, the data identifiers in these tables are not necessarily the same as the claim names used for EBWOID complying with [SD-JWT VC]. [Chapter 3.2](#32-sd-jwt-vc-based-encoding) specifies the claim names to be
  used for such EBWOID.



### 2.2 Mandatory attributes per EBW proposal (Articles 8–9)

| **Data Identifier**    | **Definition**                                                                                                                                                                                                                                                                                                         |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| legal_name             | The official name of the EBW owner (economic operator or public sector body), from the relevant register or official record.                                                                                                                                                                                           |
| id                     | The relevant unique identifier attributed in accordance with Article 9 of EWB (**WEBUILD specific** EUID where available, otherwise a similar constructed, unique per issuer identifier. <Countrycode ISO 3166-1 alpha-2><Issuer-reference>.<unique identificator> eks. `SE` +  `BOLREG` + `123456789` -> `SEBOLREG.123456789`  |




### 2.4 Mandatory metadata 

| **Data Identifier**         | **Definition**                                                                                                                                                    |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| issuing_authority           | Name of the administrative authority or qualified trust service provider that issued the EBWOID, or the ISO 3166‑1 alpha‑2 of the Member State where applicable. |
| issuing_country             | Alpha‑2 country code, as specified in ISO 3166‑1, of the country or territory of the provider of the EBWOID.                                                     |
| attestation_legal_category  | The type of attestation category. (Pub-EAA/QEAA)                                                                                                                  |


### 2.5 Optional metadata

| **Data Identifier**  | **Definition**                                                                                                                                                                                                                                                                                              |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| location_status      | The location of validity status information on the EBWOID used for revocation/suspension checks.                                                                                                                                                                                                            |
| expiry_date          | Administrave Date when the EBWOID will expire, following ISO 8601 **Clarification** This is in case the administrative validity is different from the technical expiry date of the credential.                                                                                                              |
| trust_anchor         | This meta-data attribute indicates at least the URL at which a machine‑readable version of the trust anchor to be used for verifying the EBW‑OID can be found or looked up. This corresponds to Annex V/VII point h) of the [European Digital Identity Regulation] and EBW Article 8 issuance as EAA/QEAA.  |




# 3 Attestation encoding

## 3.1 ISO/IEC 18013-5-compliant encoding

Out of scope. EBW‑OID is defined only for SD‑JWT VC in this Rulebook. No ISO/IEC 18013‑5 mdoc encoding is defined for EBW‑OID, as offline proximity presentation is not a current requirement.

## 3.2 SD-JWT VC-based encoding


Verifiable Credential Type (vct): `uri:eu.ebw.oid.1`

Claim names and disclosure policy (aligned with Chapter 2 attributes):
 
| Data Identifier             | Attribute Identifier        | Encoding format | Reference/Notes                                                                                                                                                                                                                                                                         |
|-----------------------------|-----------------------------|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                          | id                          | string          | Cross‑border unique identifier per EBW Article 9. In **WEBUILD** EUID where available, otherwise a similar constructed, unique per issuer identifier. <Countrycode ISO 3166-1 alpha-2><Issuer-reference>.<unique identificator> `SE` +  `BOLREG` + `123456789` -> `SEBOLREG.123456789`  |
| name                        | name                        | string          | Official name from relevant register or official record.                                                                                                                                                                                                                                |
| attestation_legal_category  | attestation_legal_category  | string          | The type of attestation category. Can be one of QEAA or PUB-EAA                                                                                                                                                                                                                         | 
| expiry_date                 | date_of_expiry              | string          | Addministrative expiry date given on ISO 8601-1  date fomat. YYYY‑MM‑DD ]                                                                                                                                                                                                               |
| issuing_authority           | issuing_authority           | string          | Name of the administrative authority, Commission (for Union entities), or QTSP issuing the EAA/QEAA; or ISO 3166‑1 alpha‑2 where applicable.                                                                                                                                            |
| issuing_country             | issuing_country             | string          | ISO 3166‑1 alpha‑2 code of the provider’s country/territory.                                                                                                                                                                                                                            |
| location_status             | status                      | JSON Object     | See [Section 3.2.1](#321-attribute-status).                                                                                                                                                                                                                                             |
| trust_anchor                | trust_anchor                | string (URI)    | URL of machine‑readable trust anchor as per Annex V/VII point h).                                                                                                                                                                                                                       |

Selective Disclosure: Attributes of the EBWOID SHALL NOT be selectively disclosable.


### 3.2.1 Attribute status
For SD‑JWT VC‑compliant EBW‑OID, the EBW‑OID MUST include a status claim if the technical validity period is greater than 24 hours. This claim enables Relying Parties to determine if a credential has been revoked via a status list mechanism, as specified in [SD‑JWT VC](https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/12/).

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

### 3.3 Example

Illustrative examples:
- Example claim set (human‑readable):
```json
{
  "vct": "uri:eu.ebw.oid.1",
  "id": "NOFOR.123456789",
  "name": "Example AS",
  "attestation_legal_category": "PUB-EAA",
  "issuing_authority": "Brønnøysundregistrene",
  "issuing_country": "NO",
  "date_of_expiry": "2026-12-31",
  "trust_anchor": "https://tl.eidas.europa.eu/tl-browser/#/",
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

### 4.1 Use-case context

The EBW-OID attestation serves diverse types of EBW owners across European digital services:

- **Public sector body** — a Union entity, a national, state, regional or local authority, a body governed by public law or an association formed by one or several such entities or bodies , or a private entity mandated by at least one such entities, authorities, bodies or associations to provide public services, when acting under such a mandate.
- **Economic operator** — any natural or legal person, or a group of such persons, including temporary associations of undertakings, acting in a commercial or professional capacity for purposes related to their trade, business, craft or profession

EBW-OID is profiled for **SD-JWT VC** and **W3C VCDM** because these formats:
- Are mandated or recommended by the ARF and applicable implementing acts for electronic attestations of attributes.
- Support selective disclosure (SD-JWT VC) and linked-data integrity (W3C VCDM), enabling both privacy and semantical presentations.

Primary use cases:
- Proving the legal identity of an organisation (holder) to a Relying Party in national and cross‑border digital online services.
- Activating and enabling the ownership binding of the EBW.
- Establishing a trust context for additional legal‑person attestations that reference the EBW‑OID `id`.

Relying Party obligations:
- Verify the SD‑JWT VC signature and ensure the issuer is an authorised public body by validating the qualified certificate chain against the appropriate QTSP Trusted List (see Chapter 5).
- Check freshness: validate `exp` and consider `iat`.
- Apply revocation/status checks as defined in Chapter 6.
- Where the transaction requires binding to a natural person representative, the RP SHOULD request and verify a PID for the representative in addition to the EBW‑OID.

Presentation requirements:
- Selective disclosure is NOT permitted for the core EBW‑OID attributes; the holder presents EBW‑OID atomically.

Transactional data:
- The RP MAY keep minimal logs necessary to demonstrate lawful processing and verification events; no additional transaction‑specific attributes are introduced by EBWOID. No additional transaction‑specific attributes are introduced by EBW‑OID.

## 5 Trust anchors

For EBW‑OID as an PUB-EAA/QEAA, Relying Parties SHALL verify the EBW‑OID using the issuer credential:
- Public‑body issuer certificate issued by a Qualified Trust Service Provider (QTSP) when provided by or on behalf of a public sector body responsible for an authentic source;
- Qualified electronic attestation of attributes when provided by a QTSP; or
- Commission issuance for Union entities (having the same legal effect per EBW Article 8(4)).
Relying Parties SHALL verify the relevant certificate chain up to the appropriate trust anchor (eIDAS Trust List or Commission trust anchor as applicable).

Verification steps:
1) Verify the SD‑JWT VC signature over the EBW‑OID using the issuer certificate.
2) Build and validate the certificate chain from the issuer certificate to a QTSP trust anchor listed in the appropriate Trusted List.
3) Validate certificate status (validity, revocation) per eIDAS trust list rules.
4) Use the `trust_list_location` metadata to discover the appropriate Trusted List or machine‑readable pointer.

Issuers MAY use intermediate signing certificates. RPs SHALL handle such chains. The trust model is equivalent to Annex VII for PuB‑EAA.

## 6 Revocation

TODO: WE BUILD WP4 - EBW owner identification data revocation task 5

EBW‑OID is expected to be long‑lived but revocable. This Rulebook adopts the following policy:
- EBW‑OID SHALL include `exp`. Validity longer than 24 hours is permitted; therefore, revocation MUST be supported.
- When the Commission specifies the Attestation Status List (ASL) or Attestation Revocation List (ARL) mechanism, EBW‑OID Providers SHALL implement that mechanism.
- Until such mechanisms are specified, EBW‑OID Providers SHALL publish revocation status via a machine‑readable endpoint referenced from the issuer’s policy, and Relying Parties SHALL implement status checking per that policy. Issuers SHOULD implement the [oauth status list](https://datatracker.ietf.org/doc/draft-ietf-oauth-status-list/) until otherwise specified. 

Relying Party checks:
- Validate `exp` not in the past.
- Query the designated ASL/ARL (or interim status endpoints) to determine the current status.
- Treat any indeterminate status as non‑valid per risk policy.


## 7 Compliance



## 8 References
| **Item Reference**                     | **Standard name/details**                                                                                                                                                                                                                                                                           |
|----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [European Digital Identity Regulation] | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework                            |
| [ISO/IEC 18013-5]                      | ISO/IEC 18013-5, Personal identification --- ISO-compliant driving licence - Part 5: Mobile driving licence (mDL) application, First edition, 2021-09                                                                                                                                               |
| [OIDC]                                 | Sakimura, N. et al., "OpenID Connect Core 1.0", OpenID Foundation. Available: <https://openid.net/specs/openid-connect-core-1_0.html>                                                                                                                                                               | |
| [SD-JWT VC]                            | SD-JWT-based Verifiable Credentials (SD-JWT VC). Available: <https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/>, version draft-ietf-oauth-sd-jwt-vc-09                                                                                                                                   |
| [Topic 7]                              | ARF Annex 2 - Topic 7 - Attestation revocation and revocation checking Available: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a237-topic-7-attestation-revocation-and-revocation-checking>  |
| [Topic 10]                             | ARF Annex 2 - Topic 10 - Issuing a PID or attestation to a Wallet Unit: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a2310-topic-10-issuing-a-pid-or-attestation-to-a-wallet-unit>           |
| [Topic 12]                             | ARF Annex 2 - Topic 12 - Attestation Rulebooks, Available: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a2312-topic-12-attestation-rulebooks>                                                |
| [Topic 20]                             | ARF Annex 2 - Strong User authentication for electronic payments, Available: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a2320-topic-20-strong-user-authentication-for-electronic-payments> |
| [W3C VCDM v2.0]                        | Sporny, M. *et al,* Verifiable Credentials Data Model v2.0, W3C Recommendation.                                                                                                                                                                                                                     |








 
