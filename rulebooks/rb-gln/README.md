# Attestation Rulebook for attestations of type GLN Number (Global Location Number)

* Author(s):
  * [Dominik Halbeisen, GS1 Switzerland]

* Previous Authors

* Reviewer(s):
  * [Florin Coptil, Robert Bosch GmbH]
  * [Dominic Hurni, SBB]

| Version | Date       | Description                                                     |
|---------|------------|-----------------------------------------------------------------|
| 0.1     | 01.06.2026 | Initial draft based on the WeBuild design attestations meetings |
| 0.6     | 29.06.2026 | update layout and review gln                                    |

* Contact:
  * [Florin Coptil](mailto:florin.coptil@bosch.com)*
  
* Feedback:

---

## 1 Introduction

This attestation addresses the following question:

**What is the GS1-registered identifier (Global Location Number, GLN) for a location or legal entity of a supplier, and is it valid and actively licensed?**

The GS1 GLN attestation provides a verifiable, standardized representation of a legal entity's GS1-registered identity and location data, based on a company's Global Company Prefix, thereby supporting supply chain transparency and supplier due diligence within KYS processes.

### 1.1 Document scope and purpose

Within the Know Your Supplier (KYS) process, the GS1 GLN Attestation supports supply chain
integrity by:

- Enabling to verify the supplier's registration in a globally recognized and globally
  interoperable identification system.
- Enabling trusted location data.
- Contributing to reduce fraud and counterfeit risks through validated identification.
- Providing documented evidence for regulatory and audit compliance.

Overall, integrating GS1 GLN attestation into KYS enhances transparency, data reliability, and
supplier due diligence across global operations.

The GS1 GLN attestation typically validates:

- The legal entity name registered with GS1
- The Global Location Number GLN of an organization, based on the Global Company Prefix licensed by GS1 to the holder of the GLN
- The entity's registered address and country
- Confirmation of active membership and authorization to issue GS1 identifiers

### 1.2 Document structure

This Rulebook is structured as follows:

- Chapter 2 describes the attestation attributes and metadata in an encoding-independent
  manner, including the data model.
- Chapter 3 specifies how the attestation attributes and metadata are encoded: Section 3.2
  covers SD-JWT VC-based encoding.
- Chapter 4 specifies attestation usage scenarios, Relying Party obligations (including UBO
  identity verification procedures per AMLR), and integration with KYC/KYS workflows.
- Chapter 5 defines trust anchors and verification mechanisms for issuer authorization,
  including integration with Transparency Registers.
- Chapter 6 defines revocation mechanisms for the attestation.
- Chapter 7 provides compliance information regarding the EUBW framework, AML regulations,
  corporate governance standards, and applicable data protection laws.
- Chapter 8 provides references to applicable standards and specifications.

### 1.3 Keywords

This document uses the capitalised keywords 'SHALL', 'SHOULD' and 'MAY' as specified in
[RFC 2119], i.e. to indicate requirements, recommendations and options specified in this
document.

In addition, 'must' (non-capitalised) is used to indicate an external constraint, i.e. a
requirement that is not mandated by this document, but, for instance, by an external document.
The word 'can' indicates a capability, whereas other words, such as 'will', and 'is' or 'are'
are intended as statements of fact.

### 1.4 Terminology

*Additional terminology specific to this attestation:*

| Term                                       | Description                                                                                                                                                                  |
|--------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GLN (Global Location Number)               | A 13-digit GS1 identifier used to uniquely identify legal entities and physical locations within global supply chains. Built upon a GS1-issued Global Company Prefix.        |
| GS1 Company Prefix (Global Company Prefix) | The licence key issued by GS1 to an organization, forming the basis upon which GLNs and other GS1 identifiers are constructed.                                               |
| GS1                                        | A global not-for-profit organization that develops and maintains standards for supply chain communication, including barcodes, RFID, and electronic data interchange (EDI).  |
| KYS (Know Your Supplier)                   | A due diligence process for verifying supplier credentials, integrity, and risk exposure within a supply chain.                                                               |
| Relying Party                              | An entity that relies on the attestation data presented by a Wallet Instance to make trust decisions.                                                                        |
| Issuer                                     | The entity responsible for creating and signing an attestation and ensuring mandatory attributes are present.                                                                 |

---

## 2 Attestation attributes and metadata

The GLN Number Attestation is designed to provide a verifiable, standardized representation of
a legal entity's GS1-registered identity and location data, supporting supply chain transparency
and supplier due diligence within KYS processes.

### 2.1 Introduction

The GLN attestation uses a structured model consisting of two primary components:

- **GS1** — Identity attributes of the registered legal entity including its legal name,
  company prefix, and Global Location Number.
- **RegisteredAddress** — The physical or registered address of the legal entity as held by GS1.

**Data Model:**

```
GLN
├─ GS1 (organizationLegalName (M), licenceKey (M), GlobalLocationNumber (M)) — mandatory
└─ Address (locality (M), postal_code (M), region (M), country (M)) — mandatory
```


The attributes below are based on schema.org and GS1 Web Vocabulary ontological definitions.

**Attestation Classification:**

This attestation type MAY be classified as:
- **"EAA"** when issued by the GS1

| **Data Identifier** | **Semantic Reference** | **Definition**                        | **Data type** |
|---------------------|------------------------|---------------------------------------|---------------|
| gs1                 | ...                    | Information about the gs1 information | Object        |
| address             | ...                    | Information about the address         | Object        |

### 2.2 Mandatory attributes

**GS1**

| **Data Identifier**   | **Semantic Reference** | **Definition**                                      | **Data type**  |
|-----------------------|------------------------|-----------------------------------------------------|----------------|
| organizationLegalName | ...                    | The legal entity name registered with GS1           | Rdf:langString |
| licenceKey            | ...                    | The GS1 Company Prefix assigned to the organization | xsd:integer    |
| globalLocationNumber  | ...                    | The GLN (Global Location Number)                    | xsd:String     |

**Address**

| **Data Identifier** | **Semantic Reference** | **Definition**                                                                        | **Data type**       |
|---------------------|------------------------|---------------------------------------------------------------------------------------|---------------------|
| postal_code         | ...                    | The postal code of the city where the legal owner currently is registered or operates | String              |
| locality            | ...                    | The city where the legal owner currently is registered or operates                    | String              |
| region              | ...                    | The region where the legal owner currently is registered or operates                  | String              |
| country             | ...                    | The country where the legal owner currently is registered or operates                 | ISO 3166-1 alpha-2  |

### 2.3 Optional attributes

No optional attributes are currently defined for this attestation type.

### 2.4 Conditional attributes

No conditional attributes are defined for this attestation type. All attributes are either
mandatory or optional as specified above.

### 2.5 Mandatory metadata

| **Data Identifier**        | **Definition**                                                                                                                                                     | **Data type** |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| attestation_legal_category | Indicates the legal category of this attestation ("EAA" or "pubEAA"/"QEAA")                                                                                       | String        |

### 2.6 Optional metadata

### 2.7 Conditional metadata

No conditional metadata elements are defined for this attestation type.

### 2.8 Value Lists

#### 2.8.1 Country Codes

The list of country codes SHALL follow the alpha-2 format based on ISO 3166-1 alpha-2.

| **Code** | **Example**  |
|----------|--------------|
| DE       | Germany      |
| CH       | Switzerland  |
| FR       | France       |
| IT       | Italy        |
| ES       | Spain        |

For a complete list, refer to the ISO 3166-1 alpha-2 standard.

### 2.9 Integrity Rules

The following integrity rules **SHALL** be enforced:

- The GLN attestation SHALL contain exactly one `GS1` object and exactly one `Address` object.
- `organizationLegalName` SHALL be a non-empty string.
- `licenceKey` SHALL be a valid integer representing the GS1 Company Prefix issued to the
  organization.
- `globalLocationNumber` SHALL be a valid 13-digit GS1 GLN string, consistent with the
  licenceKey upon which it is built.
- `postal_code` SHALL be a non-empty string.
- `locality` SHALL be a non-empty string.
- `region` SHALL be a non-empty string.
- `country` SHALL be a valid ISO 3166-1 alpha-2 country code.
- Each attribute identifier SHALL appear at most once within its respective object scope.
- The `GlobalLocationNumber` SHALL pass GS1 check-digit validation.
- The `licenceKey` SHOULD be verifiable against the GS1 registry API to confirm active
  membership status.

---

## 3 Attestation encoding

### 3.1 ISO/IEC 18013-5-compliant encoding

ISO/IEC 18013-5 (also called mdoc) is out of scope for this Rulebook, as offline proximity
presentation is not a current requirement for the GLN Number attestation.

### 3.2 SD-JWT VC-based encoding

The GLN Number attestation uses the SD-JWT VC format to allow for selective disclosure of
attestation attributes.

**Selective Disclosure:** Claims within the attestation (e.g., `organizationLegalName`,
`GlobalLocationNumber`, address) SHALL be individually selectively disclosable, enabling a
legal entity to disclose only the attributes requested by a Relying Party.

**Verifiable Credential Type (`vct`):** `vct: eu.we-build:gln:1`

#### 3.2.1 Attribute Encoding Table


| **Data Identifier**        | **Attribute Identifier**   | **Encoding Format**         | **Reference / Notes**                                                      | **Disclosable** |
|----------------------------|----------------------------|-----------------------------|----------------------------------------------------------------------------|-----------------|
| **GS1**                    |                            |                             |                                                                            |                     |
| organizationLegalName      | gs1.organizationLegalName  | String                      | The legal entity name registered with GS1                                  | MUST            |
| licenceKey                 | gs1.licenceKey             | Integer                     | The GS1 Company Prefix assigned to the organization                        | MUST            |
| globalLocationNumber       | gs1.globalLocationNumber   | String                      | The 13-digit GLN assigned to the entity                                    | MUST            |
| **Address**                |                            |                             |                                                                            |                     |
| address.postal_code        | address.postal_code        | String                      | Postal code of the registered address                                      | MUST            |
| address.locality           | address.locality           | String                      | City of the registered address                                             | MUST            |
| address.region             | address.region             | String                      | Region of the registered address                                           | MUST            |
| address.country            | address.country            | String (ISO 3166-1 alpha-2) | Country of the registered address                                          | MUST            |
| **Metadata**               |                            |                             |                                                                            |                     |
| vct                                   | vct                                           | String                       | A URI or other collision-resistant identifier that defines the type of the SD-JWT Verifiable Credential                  | MUST            |

**Notes:**

- **MUST**: The claim **SHALL** be selectively disclosable — the holder **MAY** choose to
  disclose or withhold this claim when presenting the credential to a Relying Party.
- **MAY**: The claim **MAY** be selectively disclosable if the issuer supports it.
- **MUST NOT**: The claim **SHALL NOT** be selectively disclosable — it is always present in
  plain text in the JWT header/payload and cannot be withheld by the holder, as it is required
  for credential verification and trust establishment.
- `iat`, `exp`, and `iss` follow RFC 7519 standard JWT claim naming conventions.

#### 3.2.2 Status Claim

For SD-JWT VC-compliant GLN Number attestations, the attestation **MUST** include a `status`
claim if the technical validity period is greater than 24 hours. This claim enables Relying
Parties to determine if a credential has been revoked via a status list mechanism, as specified
in SD-JWT VC.

The `status` claim **SHALL** be a JSON object with the following members:

- `type` (string): **SHALL** be `"status-list"`.
- `status_list_credential` (string, URI): The URI of the Status List Credential document that
  contains the status bitstring.
- `status_list_index` (integer, >= 0): The zero-based index into the status list bitstring that
  corresponds to this credential.
- `status_purpose` (string): **SHALL** be `"revocation"` for this attestation.

**Example:**

```json
{
  "status": {
 "type": "status-list",
 "status_list_credential": "https://issuer.example.com/status/gln/2025",
 "status_list_index": 123,
 "status_purpose": "revocation"
  }
}
```
### 3.2.3 Example Payload

The following is a non-normative example of a GLN Number SD-JWT VC payload:
```
{
  "vct": "eu.we-build.gln.1",
  "attestation_legal_category": "EAA",
  "iss": "did:example:gs1-issuer-456",
  "iat": 1710000000,
  "exp": 1741536000,
  "gs1": {
    "organizationLegalName": "Example Supply GmbH",
    "licenceKey": 4012345,
    "globalLocationNumber": "4012345000009"
  },
  "address": {
    "postal_code": "10115",
    "locality": "Berlin",
    "region": "Berlin",
    "country": "DE"
  },
  "status": {
    "type": "status-list",
    "status_list_credential": "https://example.com/status/gln-list-1",
    "status_list_index": 123,
    "status_purpose": "revocation"
  },
  "trust_anchor_url": "https://trust.webuildconsortium.eu/anchors/gs1/eidas-tl",
  "schema_version": "0.1.0",
  "cnf": {
    "jwk": {
      "kty": "EC",
      "crv": "P-256",
      "x": "abc-123_def-456_ghi-789_jkl-012",
      "y": "mno-345_pqr-678_stu-901_vwx-234"
    }
  }
}
```
Sample payloads are provided under ../data-schemas/sd-jwt/sample-data/gln-sd-jwt-sample.json

#### 3.3 W3C Verifiable Credentials Data Model-based encoding
@TODO — To be discussed: which stakeholders will support this format and which use cases require it.

## 4 Attestation usage

### 4.1. Issuance process ###
TODO Doominik 

### 4.2 Relying Party Obligations
When receiving and processing an attestation, the Relying Party SHALL perform the following verification obligations.
### 4.2.1 – 4.2.8 Base Verification Process
The Relying Party SHALL perform the base attestation verification process as defined in the Base Verification specification:
https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-base/verifier-base-verification.md#42-relying-party-obligations

## 5 Trust anchors

### 5.1 Trust Model for UBO  Attestations

### 5.2 Trust Anchor Location Metadata
UBO  Attestations SHOULD include the trust_anchor_url metadata attribute (see Section 2.6).
@Florin -> trust topic

## 6 Revocation
Details on the revocation mechanisms and processes for UBO  attestations will be completed in a future version of this Rulebook. This will cover how Relying Parties can check the revocation status of an attestation.
@Florin -> revocation  topic

## 7 References
This chapter will be completed in a future version of this Rulebook to include specific references relevant to UBO  attestations.

## 7 Compliance
This UBO  Attestation Rulebook is specifically designed to comply with AMLR 2024/1624:
*Article 3(17) – Definition of Beneficial Owner:*
*Article 60 – Beneficial Ownership Registers:*
*Article 62 – Beneficial Ownership Information Requirements:*

## 8 References
| **Item Reference**                      | **Standard name/details**|
|-----------------------------------------|---------------------------|
| [European Digital Identity Regulation]  | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework |
| [European Digital Identity Regulation]	 | Regulation (EU) 2024/1183 of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework|
| [HAIP]	                                 | Yasuda, K. et al, OpenID4VC High Assurance Interoperability Profile, OpenId Foundation, Version draft-03|
| [IANA-JWT-Claims]	                      | IANA JSON Web Token Claims Registry. Available: https://www.iana.org/assignments/jwt/jwt.xhtml|
| [ISO/IEC 18013-5]	                      | ISO/IEC 18013-5, Personal identification — ISO-compliant driving licence - Part 5: Mobile driving licence (mDL) application, First edition, 2021-09|
| [ISO 3166-1 alpha-3]                    | 	ISO 3166-1 alpha-3, Codes for the representation of names of countries and their subdivisions — Part 1: Country codes. Available: https://www.iso.org/iso-3166-country-codes.html|
| [ISO 4217]                              | 	ISO 4217 — Currency codes. Available: https://www.iso.org/iso-4217-currency-codes.html|
| [ISO 8601]                              | 	ISO 8601 — Date and time format. Available: https://www.iso.org/iso-8601-date-and-time-format.html|
| [OIDC]	                                 | Sakimura, N. et al., "OpenID Connect Core 1.0", OpenID Foundation. Available: https://openid.net/specs/openid-connect-core-1_0.html|
| [RFC 2119]	                             | RFC 2119 — Key words for use in RFCs to Indicate Requirement Levels, S. Bradner, March 1997|
| [RFC 3339]	                             | RFC 3339 — Date and Time on the Internet: Timestamps, G. Klyne et al., July 2002|
| [RFC 7519]	                             | RFC 7519 — JSON Web Token (JWT), M. Jones et al., May 2015|
| [RFC 8610]	                             | RFC 8610 — Concise Data Definition Language (CDDL): A Notational Convention to Express Concise Binary Object Representation (CBOR) and JSON Data Structures, H. Birkholz et al., June 2019|
| [RFC 8943]	                             | RFC 8943 — Concise Binary Object Representation (CBOR) Tags for Date, M. Jones et al., November 2020|
| [RFC 8949]	                             | RFC 8949 — Concise Binary Object Representation (CBOR), C. Bormann et al., December 2020|
| [SD-JWT VC]	                            | SD-JWT-based Verifiable Credentials (SD-JWT VC). Available: https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/, version draft-ietf-oauth-sd-jwt-vc-09|
