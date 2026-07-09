# Attestation Rulebook for attestations of type GLN Number (Global Location Number)

* Author(s):
  * [Dominik Halbeisen, GS1 Switzerland]
  * [Dr. Sebastian Schmittner, EECC](mailto:sebastian.schmittner@eecc.de)
  * [Christian Fries, EECC](mailto:christian.fries@eecc.de)
* Previous Authors
* Reviewer(s):
  * [Florin Coptil, Robert Bosch GmbH]
  * [Dominic Hurni, SBB]

| Version | Date       | Description                                                     |
|---------|------------|-----------------------------------------------------------------|
| 0.1     | 01.06.2026 | Initial draft based on the WeBuild design attestations meetings |
| 0.6     | 29.06.2026 | update layout and review gln                                    |
| 0.7     | 30.06.2026 | Updates by EECC to include the GS1 Trust Chain details          |


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
- Chapter 3 specifies how the attestation attributes and metadata are encoded: 
  - Section 3.2 covers SD-JWT VC-based encoding
  - Section 3.3 covers W3C VCDM (GS1 Digital Licenses) encoding
- Chapter 4 specifies attestation usage scenarios and Relying Party obligations in KYS workflows.
- Chapter 5 defines the GS1 trust model, trust anchors, and verification of the credential chain.
- Chapter 6 defines revocation mechanisms for the attestation.
- Chapter 7 provides compliance information regarding the EUBW framework and applicable data protection laws.
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
| Global Location Number (GLN)               | A 13-digit GS1 identifier used to uniquely identify legal entities and physical locations within global supply chains. Issued by the legal entity with a matching GS1-issued Global Company Prefix        |
| GS1 Company Prefix (GCP) | The licence issued by a GS1 MO to an legal entity (organization), forming the basis upon which GLNs and other GS1 identifiers are constructed.                                               |
| GS1 Member Organization (GS1 MO) | A member organization of GS1 such as GS1 Germany, GS1 US, GS1 France, etc. |
| GS1 Global Office (GS1 GO, legal name: GS1 AISBL)           | Overarching GS1 orchanization for the global coordination of all GS1 MOs                                                           |
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


The attributes below are based on the [GS1 Web Vocabulary](https://ref.gs1.org/voc/). Terms use the `gs1:` prefix (namespace `https://ref.gs1.org/voc/`). JSON-LD paths for the WeBuild KYS address extension are specified in Section 3.3.3.

**Attestation Classification:**

This attestation type MAY be classified as:
- **"EAA"** when issued by GS1 or an authorized GS1 Member Organization acting as an authentic source

| **Data Identifier** | **Semantic Reference** | **Definition**                        | **Data type** |
|---------------------|------------------------|---------------------------------------|---------------|
| gs1                 | `gs1:Organization`     | GS1 identity attributes of the legal entity | Object    |
| address             | `gs1:PostalAddress`    | Registered address via `gs1:address` on Organization | Object |

### 2.2 Mandatory attributes

**GS1** (identity)

Per [GS1 Digital Licenses](https://gs1.github.io/GS1DigitalLicenses/) and GS1 Web Vocabulary:

| **Data Identifier**   | **Semantic Reference** | **Definition**                                      | **Data type**  |
|-----------------------|------------------------|-----------------------------------------------------|----------------|
| organizationLegalName | `gs1:organizationLegalName` | The legal entity name registered with GS1      | `rdf:langString` |
| licenceKey            | *(derived)*            | The GS1 Company Prefix (`licenseValue` from backing `GS1CompanyPrefixLicenseCredential`) | `xsd:integer` |
| globalLocationNumber  | `gs1:partyGLN`         | The 13-digit GLN (Global Location Number)         | `xsd:string`   |

**Address** (via `gs1:address` → `gs1:PostalAddress` on `gs1:Organization`)

| **Data Identifier** | **Semantic Reference** | **Definition**                                                                        | **Data type**       |
|---------------------|------------------------|---------------------------------------------------------------------------------------|---------------------|
| postal_code         | `gs1:postalCode`       | The postal code where the legal entity is registered or operates                      | `xsd:string`        |
| locality            | `gs1:addressLocality`  | The city where the legal entity is registered or operates                             | `rdf:langString`    |
| region              | `gs1:addressRegion`    | The region where the legal entity is registered or operates                           | `rdf:langString`    |
| country             | `gs1:countryCode`      | ISO 3166-1 alpha-2 country code (nested in `gs1:addressCountry` → `gs1:Country`)      | `xsd:string`        |

### 2.3 Optional attributes

No optional attributes are currently defined for this attestation type.

### 2.4 Conditional attributes

No conditional attributes are defined for this attestation type. All attributes are either
mandatory or optional as specified above.

### 2.5 Mandatory metadata

| **Data Identifier**        | **Definition**                                                                                                                                                     | **Data type** |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| issuance_date              | The date and time when the attestation was issued (ISO 8601)                                                                                                       | DateTime      |
| expiry_date              | The date and time when the attestation will expire (ISO 8601)                                                                                                       | DateTime      |
| issuing_entity             | The identifier of the legal entity that issued the attestation (typically the subject entity itself for self-issued attestations, or the QTSP identifier for QEAA) | String        |
| attestation_legal_category | Indicates the legal category of this attestation ("EAA" or "pubEAA"/"QEAA")                                                                                       | String        |
| vct                          | A unique identifier (URL or URN) for the credential type, indicating which claims must be present and which can be selectively disclosed                  | String        |

### 2.6 Optional metadata

| **Data Identifier** | **Definition**                                                             | **Data type** |
|---------------------|----------------------------------------------------------------------------|---------------|
| trust_anchor_url    | URL where the trust anchor for verifying this attestation can be retrieved | URI           |
| schema_version      | Version of the schema used                                                 | String        |

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

The SD-JWT payload **SHALL** embed a [W3C Verifiable Credentials Data Model 2.0](https://www.w3.org/TR/vc-data-model-2.0/) (VCDM) credential structure as defined in [RFC 9901] Appendix A.4: top-level VCDM properties (`@context`, `type`, `issuer`, `credentialSubject`, `credentialSchema`, and related metadata) are carried directly in the JWT claims set, and selectively disclosable claims within `credentialSubject` are represented as `_sd` digests at issuance time per [RFC 9901]. Holder binding **SHALL** use a `cnf` claim at the top level of the SD-JWT payload. The WeBuild-specific `vct` and `attestation_legal_category` claims are additional top-level JWT claims required by the SD-JWT VC profile. Revocation status for SD-JWT verification **SHALL** use the SD-JWT VC `status` claim (Section 3.2.2); a VCDM `credentialStatus` property MAY be included in the payload for structural parity but is **not** used for revocation validation in the SD-JWT path.

For GLN attestations, the embedded VCDM payload **SHALL** use the GS1 `OrganizationDataCredential` type (Section 3.3.3), including WeBuild KYS mandatory address and legal-name extensions via GS1 Web Vocabulary terms under `credentialSubject.organization`.

**Selective Disclosure:** Claims within `credentialSubject` (e.g., `gs1:organizationLegalName`,
`gs1:partyGLN`, registered address) SHALL be individually selectively disclosable, enabling a
legal entity to disclose only the attributes requested by a Relying Party.

**Verifiable Credential Type (`vct`):** `vct: eu.we-build.gln.1`

#### 3.2.1 Attribute Encoding Table


| **Data Identifier**        | **Attribute Identifier**   | **Encoding Format**         | **Reference / Notes**                                                      | **May be hidden in SD-JWT** |
|----------------------------|----------------------------|-----------------------------|----------------------------------------------------------------------------|-----------------|
| **GS1**                    |                            |                             |                                                                            |                     |
| organizationLegalName      | `credentialSubject.organization.gs1:organizationLegalName` | String (`rdf:langString`) | WeBuild KYS extension; legal entity name registered with GS1 (Section 3.3.3) | NO            |
| licenceKey                 | *(derived)*                | Integer                     | Derived from the `extendsCredential` chain on the paired GLN `KeyCredential` (Section 3.3.5); not stored on `OrganizationDataCredential` | NO |
| globalLocationNumber       | `credentialSubject.id`, `credentialSubject.organization.gs1:partyGLN` | String (Digital Link URI / GLN) | GLN as GS1 Digital Link URI (AI 417) in `credentialSubject.id`; same GLN in `gs1:partyGLN` (Section 3.3.2) | NO |
| **Address**                |                            |                             | Under `credentialSubject.organization.gs1:address` → `gs1:PostalAddress` (Section 3.3.3) |                     |
| address.postal_code        | `credentialSubject.organization.gs1:address.gs1:postalCode` | String | Postal code of the registered address                                      | YES            |
| address.locality           | `credentialSubject.organization.gs1:address.gs1:addressLocality` | String (`rdf:langString`) | City of the registered address                                             | YES            |
| address.region             | `credentialSubject.organization.gs1:address.gs1:addressRegion` | String (`rdf:langString`) | Region of the registered address                                           | YES            |
| address.country            | `credentialSubject.organization.gs1:address.gs1:addressCountry.gs1:countryCode` | String (ISO 3166-1 alpha-2) | Country of the registered address                                          | YES            |
| **VCDM envelope**          |                            |                             | [RFC 9901] Appendix A.4; Section 3.3.1                                     |                     |
| *(credential type)*        | `type`                     | Array of strings            | MUST include `VerifiableCredential` and `OrganizationDataCredential`       | NO        |
| *(JSON-LD context)*        | `@context`                 | Array of URIs               | MUST include VCDM 2.0 and GS1 organization context (Section 3.3.1)         | NO        |
| *(credential id)*          | `id`                       | URI                         | Globally unique resolvable credential identifier                           | NO        |
| *(human-readable name)*    | `name`                     | String                      | SHOULD describe the credential (e.g. `"GS1 Organization Data Credential"`) | NO        |
| *(human-readable description)* | `description`          | String                      | Description of the credential purpose                                      | NO        |
| *(schema reference)*       | `credentialSchema`         | Object                      | MUST reference `https://id.gs1.org/vc/schema/v1/organizationdata`          | NO        |
| *(rendering)*              | `renderMethod`             | Array                       | SHOULD be present; type `TemplateRenderMethod` (Section 3.3.3)             | YES        |
| *(GLN key link)*           | `credentialSubject.keyAuthorization` | URI                 | SHOULD reference the paired GLN `KeyCredential` (Section 3.3.5)            | NO             |
| **Metadata**               |                            |                             |                                                                            |                     |
| issuance_date              | `validFrom`, `iat`         | ISO 8601 / Unix timestamp   | VCDM `validFrom` (ISO 8601) and JWT `iat` (RFC 7519); values SHOULD be consistent | NO |
| expiry_date                | `validUntil`, `exp`        | ISO 8601 / Unix timestamp   | VCDM `validUntil` (ISO 8601) and JWT `exp` (RFC 7519); values SHOULD be consistent | NO |
| issuing_entity             | `issuer.id`, `iss`         | String (URI or DID)         | VCDM `issuer.id` and JWT `iss` (RFC 7519); values MUST match               | NO       |
| *(holder binding)*         | `sub`, `cnf`               | String / object             | `sub` identifies the holder DID; `cnf` carries the holder binding key ([RFC 9901] A.4) | NO |
| attestation_legal_category | `attestation_legal_category` | String                    | One of EAA or QEAA as defined by eIDAS 2                                   | NO        |
| vct                        | `vct`                      | String                      | Collision-resistant identifier for the SD-JWT VC type                      | NO        |
| schema_version             | `schema_version`           | String                      | Version of the schema used for this attestation                            | NO             |
| trust_anchor_url           | `trust_anchor_url`         | String (URI)                | URL where the trust anchor for verifying this attestation can be retrieved | NO             |
| *(revocation status)*      | `status`                   | Object                      | SD-JWT VC status-list claim; **SHALL** be validated for SD-JWT presentations (Section 3.2.2) | NO |
| *(VCDM status mirror)*     | `credentialStatus`         | Object                      | MAY be carried in the embedded VCDM payload for structural parity; **SHALL NOT** be used for revocation validation in the SD-JWT path | NO |

**Notes:**

- **MUST**: The claim **SHALL** be selectively disclosable — the holder **MAY** choose to
  disclose or withhold this claim when presenting the credential to a Relying Party.
- **MAY**: The claim **MAY** be selectively disclosable if the issuer supports it.
- **MUST NOT**: The claim **SHALL NOT** be selectively disclosable — it is always present in
  plain text in the JWT header/payload and cannot be withheld by the holder, as it is required
  for credential verification and trust establishment.
- Attribute paths use dot notation for nested JWT claims; GS1 vocabulary terms retain their
  `gs1:` prefix as JSON property names (compact JSON-LD form).
- `iat`, `exp`, and `iss` follow RFC 7519; `validFrom`, `validUntil`, and `issuer` follow VCDM 2.0.
  Issuers SHOULD keep JWT and VCDM temporal and issuer values consistent.

#### 3.2.2 Status Claim

For SD-JWT VC-compliant GLN Number attestations, revocation status **SHALL** be expressed and
validated using the SD-JWT VC `status` claim. When the attestation technical validity period is
greater than 24 hours, the `status` claim **MUST** be present.

The embedded W3C VCDM payload **MAY** additionally carry a `credentialStatus` property
(`BitstringStatusListEntry`) for structural parity with GS1 Digital Licenses (Section 6.1).
Relying Parties verifying an SD-JWT VC presentation **SHALL** validate revocation only via the
`status` claim and **SHALL NOT** treat `credentialStatus` as authoritative in the SD-JWT path,
even when both are present.

The `status` claim **SHALL** be a JSON object with the following members:

- `type` (string): **SHALL** be `"status-list"`.
- `status_list_credential` (string, URI): The URI of the Status List Credential document that
  contains the status bitstring.
- `status_list_index` (integer, >= 0): The zero-based index into the status list bitstring that
  corresponds to this credential.
- `status_purpose` (string): **SHALL** be `"revocation"` for this attestation.

When present in the embedded VCDM payload, `credentialStatus` **SHOULD** describe the same
status list entry as the `status` claim (equivalent `statusListCredential` /
`status_list_credential` and index values).

**Examples:**

**SD-JWT VC (`status` claim — validated)**
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

**Embedded VCDM payload (`credentialStatus` — carried, not validated in SD-JWT path)**
```json
"credentialStatus": {
  "id": "https://company-wallet-dev.prod-k8s.eecc.de/api/registry/status/revocation/20c50bdb-40f0-4466-bcc9-1ce695900dad#67609",
  "type": "BitstringStatusListEntry",
  "statusPurpose": "revocation",
  "statusListIndex": "67609",
  "statusListCredential": "https://company-wallet-dev.prod-k8s.eecc.de/api/registry/status/revocation/20c50bdb-40f0-4466-bcc9-1ce695900dad"
}
```

**W3C Data Model 2.0 (JSON-LD / Data Integrity proof — validated)**
```json
"credentialStatus": {
  "id": "https://company-wallet-dev.prod-k8s.eecc.de/api/registry/status/revocation/20c50bdb-40f0-4466-bcc9-1ce695900dad#67609",
  "type": "BitstringStatusListEntry",
  "statusPurpose": "revocation",
  "statusListIndex": "67609",
  "statusListCredential": "https://company-wallet-dev.prod-k8s.eecc.de/api/registry/status/revocation/20c50bdb-40f0-4466-bcc9-1ce695900dad"
}
```
### 3.2.3 Example Payload

The following is a non-normative example of a GLN Number SD-JWT VC payload embedding a W3C
VCDM 2.0 `OrganizationDataCredential` per [RFC 9901] Appendix A.4. The example shows the
pre-issuance JWT claims set; at issuance, selectively disclosable claims within
`credentialSubject` are replaced by `_sd` digests and corresponding Disclosures are appended to
the SD-JWT compact serialization. The example includes both `credentialStatus` (VCDM mirror,
not validated in SD-JWT) and `status` (validated for revocation).

```json
{
  "vct": "eu.we-build.gln.1",
  "attestation_legal_category": "EAA",
  "iss": "did:web:company-wallet-dev.prod-k8s.eecc.de:api:registry:did:eecc",
  "iat": 1710000000,
  "exp": 1741536000,
  "sub": "did:web:company-wallet-dev.prod-k8s.eecc.de:api:registry:did:eecc",
  "@context": [
    "https://www.w3.org/ns/credentials/v2",
    "https://ref.gs1.org/gs1/vc/organization-context",
    "https://ref.gs1.org/voc/"
  ],
  "type": [
    "VerifiableCredential",
    "OrganizationDataCredential"
  ],
  "id": "https://company-wallet-dev.prod-k8s.eecc.de/api/registry/vc/organization-data/4047111000006",
  "issuer": {
    "id": "did:web:company-wallet-dev.prod-k8s.eecc.de:api:registry:did:eecc",
    "name": "EECC"
  },
  "validFrom": "2024-03-09T12:00:00Z",
  "validUntil": "2025-03-09T12:00:00Z",
  "name": "GS1 Organization Data Credential",
  "description": "Carries organization facts for a commissioned GLN, including legal name and registered address. Extends the GS1 Digital License trust chain via the paired GLN KeyCredential referenced in keyAuthorization.",
  "credentialSubject": {
    "id": "https://id.gs1.org/417/4047111000006",
    "keyAuthorization": "https://company-wallet-dev.prod-k8s.eecc.de/api/registry/vc/key/4047111000006",
    "organization": {
      "@type": "gs1:Organization",
      "gs1:partyGLN": "4047111000006",
      "gs1:organizationName": "EECC",
      "gs1:organizationLegalName": "EECC GmbH",
      "gs1:address": {
        "@type": "gs1:PostalAddress",
        "gs1:postalCode": "10115",
        "gs1:addressLocality": "Berlin",
        "gs1:addressRegion": "Berlin",
        "gs1:addressCountry": {
          "@type": "gs1:Country",
          "gs1:countryCode": "DE"
        }
      }
    }
  },
  "credentialStatus": {
    "id": "https://company-wallet-dev.prod-k8s.eecc.de/api/registry/status/revocation/20c50bdb-40f0-4466-bcc9-1ce695900dad#67609",
    "type": "BitstringStatusListEntry",
    "statusPurpose": "revocation",
    "statusListIndex": "67609",
    "statusListCredential": "https://company-wallet-dev.prod-k8s.eecc.de/api/registry/status/revocation/20c50bdb-40f0-4466-bcc9-1ce695900dad"
  },
  "status": {
    "type": "status-list",
    "status_list_credential": "https://company-wallet-dev.prod-k8s.eecc.de/api/registry/status/revocation/20c50bdb-40f0-4466-bcc9-1ce695900dad",
    "status_list_index": 67609,
    "status_purpose": "revocation"
  },
  "credentialSchema": {
    "id": "https://id.gs1.org/vc/schema/v1/organizationdata",
    "type": "JsonSchema"
  },
  "renderMethod": [
    {
      "template": {
        "id": "https://gs1.github.io/GS1DigitalLicenses/templates/gs1-sample-license-template.svg",
        "mediaType": "image/svg+xml"
      },
      "renderSuite": "svg-mustache",
      "name": "SVG for web display",
      "type": "TemplateRenderMethod"
    }
  ],
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

The following non-normative example shows the parent `GS1CompanyPrefixLicenseCredential`
from the GS1 license chain in JSON-LD form with an embedded `DataIntegrityProof`. A Member
Organization issues this credential to authorize a company to use a GS1 Company Prefix.
`credentialSubject.organization.gs1:partyGLN` is **mandatory** and identifies the company's
main **party GLN** — the primary legal-entity GLN assigned with the prefix license. The
company prefix license carries **only** this party GLN, not additional location GLNs.

GLN `KeyCredential`s for other GLNs commissioned under the same prefix **SHALL** extend from
this company prefix license (or from another `KeyCredential` per Section 3.3.5) via
`extendsCredential`. For the **party GLN** itself, verifiers MAY establish GLN validity from
either the `GS1CompanyPrefixLicenseCredential` (via `organization.gs1:partyGLN`) or a GLN
`KeyCredential` whose `credentialSubject.id` Digital Link URI identifies the same GLN. For
**any other GLN** under the company prefix, a valid GLN `KeyCredential` **SHALL** be present.

The credential uses the same W3C VCDM 2.0 property envelope as GLN credentials (`@context`,
`type`, `credentialSubject`, `credentialStatus`, `credentialSchema`, `renderMethod`, `name`,
`description`). An SD-JWT encoding would carry the identical VCDM claims set (excluding `proof`)
in the JWT payload per [RFC 9901] Appendix A.4.

```json
{
  "type": [
    "VerifiableCredential",
    "GS1CompanyPrefixLicenseCredential"
  ],
  "proof": {
    "type": "DataIntegrityProof",
    "created": "2026-06-29T13:00:01Z",
    "verificationMethod": "did:web:company-wallet-dev.prod-k8s.eecc.de:api:registry:did:gs1_germany#companyPrefix",
    "proofPurpose": "assertionMethod",
    "proofValue": "z4PSocSkkzFfMfkzzQWRAgZ1Xk47dtpRWY9Wq48sEjk435W9pK3kDLTrx2M6uVfQDW683XQx8wgEKeZambefVNMMb",
    "cryptosuite": "ecdsa-rdfc-2019"
  },
  "issuer": {
    "id": "did:web:company-wallet-dev.prod-k8s.eecc.de:api:registry:did:gs1_germany",
    "name": "GS1 Germany"
  },
  /**
   *
   * This is the important bit defined by the data model
   *
   */
  "credentialSubject": {
    "id": "did:web:company-wallet-dev.prod-k8s.eecc.de:api:registry:did:eecc",
    "extendsCredential": "https://company-wallet-dev.prod-k8s.eecc.de/api/registry/vc/license/gs1_prefix/406",
    "licenseValue": "04065544",
    "alternativeLicenseValue": "4065544",
    "organization": {
      "gs1:partyGLN": "4047111000006",
      "gs1:organizationName": "EECC"
    }
  },
  "id": "https://company-wallet-dev.prod-k8s.eecc.de/api/registry/vc/license/gs1_prefix/4065544",
  "validFrom": "2026-06-29T12:58:17Z",
  "credentialStatus": {
    "id": "https://company-wallet-dev.prod-k8s.eecc.de/api/registry/status/revocation/20c50bdb-40f0-4466-bcc9-1ce695900dad#67609",
    "type": "BitstringStatusListEntry",
    "statusPurpose": "revocation",
    "statusListIndex": "67609",
    "statusListCredential": "https://company-wallet-dev.prod-k8s.eecc.de/api/registry/status/revocation/20c50bdb-40f0-4466-bcc9-1ce695900dad"
  },
  "credentialSchema": {
    "id": "https://id.gs1.org/vc/schema/v1/companyprefix",
    "type": "JsonSchema"
  },
  "@context": [
    "https://www.w3.org/ns/credentials/v2",
    "https://ref.gs1.org/gs1/vc/license-context",
    "https://raw.githubusercontent.com/european-epc-competence-center/jsonld-context/refs/heads/main/context/render-method"
  ],
  "renderMethod": [
    {
      "template": {
        "id": "https://gs1.github.io/GS1DigitalLicenses/templates/gs1-sample-license-template.svg",
        "mediaType": "image/svg+xml"
      },
      "renderSuite": "svg-mustache",
      "name": "SVG for web display",
      "type": "TemplateRenderMethod"
    }
  ],
  "name": "GS1 Company Prefix License",
  "description": "Authorizes a member company to use a specific GS1 Company Prefix for creating globally unique product identifiers. Issued by a Member Organization to companies within their region, this credential extends from a GS1 Prefix License and enables the company to generate GTINs, GLNs, and other GS1 identification keys for their products, locations, and business entities. Essential for supply chain traceability and global commerce."
}
```

#### 3.3 W3C Verifiable Credentials Data Model-based encoding

The GLN Number attestation MAY be encoded using the [W3C Verifiable Credentials Data Model 2.0](https://www.w3.org/TR/vc-data-model-2.0/) (VCDM) as defined in the [GS1 Digital Licenses](https://gs1.github.io/GS1DigitalLicenses/) specification. GLN verification in the GS1 ecosystem uses credentials from the license chain and GLN-specific declarations:

1. **`GS1CompanyPrefixLicenseCredential`** — issued by the Member Organization when licensing a company prefix; **mandatory** `credentialSubject.organization.gs1:partyGLN` identifies the company's main party GLN. This credential carries **only** the party GLN, not additional location GLNs. Verifiers MAY use it to validate the party GLN without a separate `KeyCredential` (Section 3.3.5).
2. **`KeyCredential`** — cryptographically asserts that a specific GLN has been commissioned; **required** for GLNs other than the party GLN, and also valid when the party GLN is explicitly commissioned as a key. Extends from the company prefix license via `extendsCredential`; see [GLN ID Key Credential](https://gs1.github.io/GS1DigitalLicenses/#gln-key-credential).
3. **`OrganizationDataCredential`** — carries organization facts (legal name, party GLN, address) associated with a GLN; see [Organization Data Credential Examples](https://gs1.github.io/GS1DigitalLicenses/#sample-organization-data-credential). MAY be issued by the organization itself and SHOULD reference a valid GLN `KeyCredential` via `keyAuthorization`.

Both GLN credential types (`KeyCredential`, `OrganizationDataCredential`) conform to VCDM 2.0. The GS1 specification provides normative examples in **JWT** (`application/vc+jwt`) and **JSON-LD** (with embedded `DataIntegrityProof`) form — these are alternative serializations of the same data model, not competing standards. VCDM 2.0 defines both securing mechanisms in [Securing Verifiable Credentials using JOSE and COSE](https://www.w3.org/TR/vc-jose-cose/) (enveloping JWT proof, media type `application/vc+jwt`) and embedded Linked Data proofs. Implementers MAY use either serialization; GS1 tooling accepts both.

European Business Wallet presentations in the WeBuild KYS workflow MAY use SD-JWT VC (Section 3.2) or W3C VCDM depending on wallet and verifier capability. SD-JWT VC encoding (Section 3.2) embeds the same GS1 VCDM 2.0 payload structure as JSON-LD or JWT-secured credentials (Section 3.3), following [RFC 9901] Appendix A.4; selective disclosure applies to claims within `credentialSubject` while VCDM envelope properties remain always visible.

##### 3.3.1 JSON-LD contexts and credential types

| Credential type | `@context` entries (minimum) | Defined in |
|-----------------|------------------------------|------------|
| `GS1CompanyPrefixLicenseCredential` | `https://www.w3.org/ns/credentials/v2`, `https://ref.gs1.org/gs1/vc/license-context` | [license-context](https://ref.gs1.org/gs1/vc/license-context) |
| `KeyCredential` | `https://www.w3.org/ns/credentials/v2`, `https://ref.gs1.org/gs1/vc/declaration-context` | [declaration-context](https://ref.gs1.org/gs1/vc/declaration-context) |
| `OrganizationDataCredential` | above + `https://ref.gs1.org/gs1/vc/organization-context` | [organization-context](https://ref.gs1.org/gs1/vc/organization-context) |

The `type` array MUST include `VerifiableCredential` and the respective GS1 type. License credentials in the backing chain use `https://ref.gs1.org/gs1/vc/license-context` — see Section 3.2.3. The company prefix license **mandatorily** includes `credentialSubject.organization.gs1:partyGLN` (the main party GLN only).

##### 3.3.2 KeyCredential (GLN identity)

A GLN `KeyCredential` asserts that the licensee has commissioned a specific GLN. It is
**required** for every GLN under the company prefix **except** the party GLN, which MAY
alternatively be verified via the parent `GS1CompanyPrefixLicenseCredential` (Section 3.3.5).
Normative requirements from [ID Key Credential Details](https://gs1.github.io/GS1DigitalLicenses/#key-credentials-details):

| **VCDM property** | **Requirement** |
|-------------------|-----------------|
| `credentialSubject.id` | MUST be a [GS1 Digital Link URI](https://www.gs1.org/standards/Digital-Link/) for the GLN (primary key **K**, no key qualifiers) |
| `extendsCredential` | **Mandatory** — MUST reference the parent GS1 Company Prefix Credential per Section 3.3.5 |
| `issuer.id` | MUST be a DID |
| `validFrom` | MUST be present |
| `name` | MUST be present (SHOULD be `"GS1 ID Key Credential"`) |
| `description` | MUST be present |
| `credentialStatus` | MUST be present; type `BitstringStatusListEntry` |
| `credentialSchema` | MUST be present; type `JsonSchema` (e.g. `https://id.gs1.org/vc/schema/v1/key`) |
| `id` | MUST be present; SHOULD be a globally unique resolvable URL |
| `renderMethod` | SHOULD be present; type `TemplateRenderMethod` |

The GLN is encoded in `credentialSubject.id` as a GS1 Digital Link URI with application identifier **417** (e.g. `https://id.gs1.org/417/{GLN}`), not as a separate claim property. See the [GLN Key Credential example](https://gs1.github.io/GS1DigitalLicenses/#gln-key-credential) in GS1 Digital Licenses.

##### 3.3.3 OrganizationDataCredential (organization data)

An `OrganizationDataCredential` is a `DataCredential` subtype that carries organization facts for the GLN identified in `credentialSubject.id`. Normative requirements from [Organization Data Credential](https://gs1.github.io/GS1DigitalLicenses/#organization-data-credential) and [GS1 Data Credential Details](https://gs1.github.io/GS1DigitalLicenses/#data-credential-details):

| **Property** | **Requirement** |
|--------------|-----------------|
| `id` | MUST be present |
| `credentialSubject.id` | MUST be the same GLN GS1 Digital Link URI as the corresponding `KeyCredential` |
| `organization` | **Mandatory** — MUST contain `gs1:partyGLN` and `gs1:organizationName` (see [Organization Data JSON Schema](https://id.gs1.org/vc/schema/v1/organizationdata)) |
| `keyAuthorization` | Optional; **SHOULD** reference the `KeyCredential` when the licensee creates data credentials |
| `validFrom` | MUST be present (DataCredential base requirement) |
| `credentialStatus` | MAY be present; if present, MUST be `BitstringStatusListEntry` |
| `credentialSchema` | MUST be present; type `JsonSchema` |
| `renderMethod` | SHOULD be present (DataCredential base requirement) |

**WeBuild KYS extension (address and legal name):** The normative GS1 `OrganizationDataCredential` JSON Schema requires only `gs1:partyGLN` and `gs1:organizationName`. Section 2 additionally requires `organizationLegalName` and registered address attributes. For W3C VCDM encoding, these **SHALL** be included by extending `credentialSubject.organization` with [GS1 Web Vocabulary](https://ref.gs1.org/voc/) terms:

| **Section 2 attribute** | **GS1 Web Vocabulary term** | **JSON-LD path under `organization`** |
|-------------------------|-------------------------------|---------------------------------------|
| `organizationLegalName` | `gs1:organizationLegalName` | `gs1:organizationLegalName` |
| `postal_code` | `gs1:postalCode` | `gs1:address` → `gs1:postalCode` |
| `locality` | `gs1:addressLocality` | `gs1:address` → `gs1:addressLocality` |
| `region` | `gs1:addressRegion` | `gs1:address` → `gs1:addressRegion` |
| `country` | `gs1:countryCode` (via `gs1:addressCountry`) | `gs1:address` → `gs1:addressCountry` → `gs1:countryCode` |

The address container is `gs1:address` → `gs1:PostalAddress`; country is an object property to `gs1:Country`, not a plain string. There is no `gs1:registeredAddress` term in the GS1 Web Vocabulary — use `gs1:address`. Full term URIs follow `https://ref.gs1.org/voc/{term}` (e.g. `https://ref.gs1.org/voc/postalCode`, `https://ref.gs1.org/voc/addressCountry`).

Issuers **SHOULD** include `https://ref.gs1.org/voc/` (or an equivalent GS1 vocabulary context) in `@context` alongside `organization-context` when emitting extended organization properties. MO policy MAY restrict which optional vocabulary terms (e.g. `gs1:streetAddress`) may be included.

##### 3.3.4 Mapping to attestation attributes (Section 2)

The encoding-independent attributes from Section 2 map to the GS1 credential pair as follows:

| **Section 2 attribute** | **GS1 encoding** |
|-------------------------|-------------------|
| `globalLocationNumber` | GLN in `KeyCredential` `credentialSubject.id` (Digital Link URI) and `organization.gs1:partyGLN`; for the **party GLN only**, MAY also be read from `GS1CompanyPrefixLicenseCredential` `credentialSubject.organization.gs1:partyGLN` (Section 3.3.5) |
| `organizationLegalName` | `organization.gs1:organizationLegalName` (WeBuild KYS); `organization.gs1:organizationName` remains required by GS1 schema |
| `licenceKey` (Company Prefix) | Derived from the `extendsCredential` chain — `licenseValue` of the referenced `GS1CompanyPrefixLicenseCredential` |
| `address.postal_code` | `organization.gs1:address.gs1:postalCode` |
| `address.locality` | `organization.gs1:address.gs1:addressLocality` |
| `address.region` | `organization.gs1:address.gs1:addressRegion` |
| `address.country` | `organization.gs1:address.gs1:addressCountry.gs1:countryCode` (ISO 3166-1 alpha-2) |
| `issuance_date` | `validFrom` on each credential |
| `expiry_date` | `validUntil` on each credential (SHOULD be set) |
| `issuing_entity` | `issuer.id` (DID) |

For SD-JWT VC encoding of the same attributes (embedded VCDM payload per [RFC 9901] A.4), see Section 3.2.1.

##### 3.3.5 Link to GS1 license chain (`extendsCredential`)

The `extendsCredential` property on a GLN `KeyCredential` is **Mandatory** ([GS1 Digital Licenses — ID Key Credential extendsCredential](https://gs1.github.io/GS1DigitalLicenses/#key-credential-extends-credential)). Verifiers MUST apply these rules:

**Party GLN vs. additional GLNs:** Each `GS1CompanyPrefixLicenseCredential` carries exactly one
mandatory party GLN in `credentialSubject.organization.gs1:partyGLN` — the main legal-entity
GLN assigned with the company prefix. It does **not** list other location GLNs under that
prefix.

- When the attested GLN equals the party GLN on a valid `GS1CompanyPrefixLicenseCredential`,
  verifiers MAY accept either that license credential (reading `organization.gs1:partyGLN`) **or**
  a GLN `KeyCredential` for the same GLN as sufficient evidence of GLN assignment.
- When the attested GLN is **not** the party GLN, verifiers **SHALL** require a valid GLN
  `KeyCredential` whose `credentialSubject.id` Digital Link URI identifies that GLN.

**`extendsCredential` chain rules:**
- If `credentialSubject.id` contains a GS1 Digital Link with primary key **K** and **no key qualifiers**, then `extendsCredential` MUST reference a GS1 License Credential whose `licenseValue` is the prefix string that **K** starts with (typically the `GS1CompanyPrefixLicenseCredential` for the company prefix).
- If `credentialSubject.id` contains primary key **K** **with key qualifiers**, then `extendsCredential` MUST reference a `KeyCredential` whose `credentialSubject.id` contains the same primary key **K** without qualifiers.

Verifiers MUST additionally validate the full license chain back to a GS1 Global Office root credential (`GS1PrefixLicenseCredential`), including signature verification and revocation status at each hop — see [Validating GS1 ID Key Credentials](https://gs1.github.io/GS1DigitalLicenses/validating_keys.html) and [Validating GS1 License Credentials](https://gs1.github.io/GS1DigitalLicenses/license_validation.html).

For a GLN `KeyCredential` **K** with subject Digital Link **D** and parent credential **P** (at `extendsCredential`), verifiers MUST also apply ([validating_keys.html](https://gs1.github.io/GS1DigitalLicenses/validating_keys.html)):

- **K** MUST be valid VCDM 2.0 with a valid issuer DID signature; **K** `validFrom` MUST NOT be in the future.
- If **D** has primary key **PK** without key qualifiers: **P** MUST be a valid GS1 License Credential; `issuer(K)` MUST match `credentialSubject(P)`; **PK** MUST begin with `licenseValue` from **P**.
- If **D** has key qualifiers: **P** MUST be a valid GS1 ID Key Credential; `issuer(K)` MUST match `issuer(P)`; primary key of **P**'s subject MUST equal **PK**.

The `OrganizationDataCredential` links to the GLN `KeyCredential` via `keyAuthorization` (SHOULD be included when the licensee creates data credentials).

##### 3.3.6 Examples

Normative GS1 examples (JWT and decoded JSON-LD) are published in [GS1 Digital Licenses](https://gs1.github.io/GS1DigitalLicenses/):

- GLN KeyCredential: [gln-key-credential](https://gs1.github.io/GS1DigitalLicenses/#gln-key-credential)
- Organization data (minimal schema): [sample-organization-data-credential](https://gs1.github.io/GS1DigitalLicenses/#sample-organization-data-credential)

License examples (Company Prefix, Prefix) are in [License Examples](https://gs1.github.io/GS1DigitalLicenses/#License-Examples).

The following non-normative example extends `OrganizationDataCredential` with WeBuild KYS mandatory address and legal-name attributes via GS1 Web Vocabulary:

```json
{
  "@context": [
    "https://www.w3.org/ns/credentials/v2",
    "https://ref.gs1.org/gs1/vc/organization-context",
    "https://ref.gs1.org/voc/"
  ],
  "type": ["VerifiableCredential", "OrganizationDataCredential"],
  "id": "https://example.gs1.org/vc/organization-data/0810159550000",
  "issuer": {
    "id": "did:web:example.gs1.org",
    "name": "GS1 Example MO"
  },
  "validFrom": "2026-01-15T10:00:00Z",
  "credentialSubject": {
    "id": "https://id.gs1.org/417/0810159550000",
    "keyAuthorization": "https://example.gs1.org/vc/key/0810159550000",
    "organization": {
      "@type": "gs1:Organization",
      "gs1:partyGLN": "0810159550000",
      "gs1:organizationName": "Healthy Tots",
      "gs1:organizationLegalName": "Healthy Tots GmbH",
      "gs1:address": {
        "@type": "gs1:PostalAddress",
        "gs1:postalCode": "10115",
        "gs1:addressLocality": "Berlin",
        "gs1:addressRegion": "Berlin",
        "gs1:addressCountry": {
          "@type": "gs1:Country",
          "gs1:countryCode": "DE"
        }
      }
    }
  },
  "credentialStatus": {
    "type": "BitstringStatusListEntry",
    "statusPurpose": "revocation",
    "statusListIndex": "42",
    "statusListCredential": "https://example.gs1.org/status/revocation/1"
  },
  "credentialSchema": {
    "id": "https://id.gs1.org/vc/schema/v1/organizationdata",
    "type": "JsonSchema"
  }
}
```

## 4 Attestation usage

### 4.1 Issuance process

GLN Number attestations SHALL only be issued when the underlying GS1 Company Prefix (GCP) license is valid and active. The attestation establishes that a specific GLN is assigned to a legal entity within the scope of that prefix; it does not replace the GS1 license credentials that form the root of trust.

#### 4.1.1 Trust chain prerequisites

Before issuing a GLN attestation, the Issuer SHALL confirm the GS1 trust chain defined in Section 5 is intact for the target GLN and company prefix. In addition, the Issuer SHALL verify:

1. **Revocation status** — No credential in the chain is revoked on the issuer's Bitstring Status List (Section 6).
2. **GLN integrity** — The GLN passes check-digit validation and its numeric prefix is consistent with the licensed company prefix (Section 2.9).
3. **Registry consistency** — Organization name and address match GS1 registry records (where an authoritative API is available).

#### 4.1.2 Issuer roles

Issuer roles and responsibilities within the GS1 trust hierarchy are defined in Section 5.2. At GS1 Global Office, credential issuance follows a multi-controller process: an Authorized Staff Member (ASM) prepares the credential and a GS1 Office Holder (OH) co-signs before publication.

#### 4.1.3 Issuance steps

The Issuer SHALL perform the following steps:

1. **Identify the subject** — Resolve the legal entity DID (`credentialSubject.id`) and confirm it controls the DID used in the parent Company Prefix License.
2. **Select backing license** — Obtain the URI of the valid `GS1CompanyPrefixLicenseCredential`. The GLN `KeyCredential` `extendsCredential` MUST satisfy the rules in Section 3.3.5.
3. **Validate prefix and GLN** — Apply integrity rules from Section 2.9 against registry data.
4. **Construct the credential** — Populate mandatory attributes (Section 2.2) and metadata (Section 2.5) using the chosen encoding (Section 3.2 or 3.3).
5. **Attach status entry** — Allocate a `statusListIndex` on the issuer's revocation list when validity exceeds 24 hours.
6. **Sign and publish** — Sign with the issuer's assertion key; publish to the issuer registry when required for resolution (Company Prefix and Prefix licenses MUST be publicly resolvable per GS1 policy).
7. **Deliver to holder** — Issue via OpenID4VCI (Business Wallet) or export for manual import.

See reference implementation by EECC and GS1 US https://github.com/european-epc-competence-center/vc-verifier-rules/

#### 4.1.4 Attestation legal category

When the GLN attestation is issued by GS1 or an authorized GS1 Member Organization acting as an authentic source, `attestation_legal_category` SHALL be `EAA`. Qualified variants (`QEAA`) are out of scope for this Rulebook unless the issuer is a QTSP with a registered attestation scheme under eIDAS Implementing Regulation (EU) 2025/1569.

### 4.2 Relying Party Obligations
When receiving and processing an attestation, the Relying Party SHALL perform the following verification obligations.
### 4.2.1 – 4.2.8 Base Verification Process
The Relying Party SHALL perform the base attestation verification process as defined in the Base Verification specification:
https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-base/verifier-base-verification.md#42-relying-party-obligations

## 5 GS1 trust model

This section defines the GS1 Digital License trust hierarchy, root trust anchors, and verification obligations for GLN credentials. Section 4.1 describes the **issuance process**; this section describes **why** those steps establish trust and **how** Relying Parties validate the chain.

### 5.1 Trust hierarchy and credential chain

GS1 identity and licensing trust is rooted at **GS1 Global Office (GO)**. GO issues `GS1PrefixLicenseCredential` credentials to **Member Organizations (MOs)**. Each MO issues `GS1CompanyPrefixLicenseCredential` credentials to **Member Companies (MCs)** within its jurisdiction; each company prefix license **mandatorily** includes the company's main **party GLN** in `credentialSubject.organization.gs1:partyGLN` and no other GLNs. A licensed MC (or MO, when policy allows) may then issue GLN **`KeyCredential`** and companion **`OrganizationDataCredential`** pairs for each additional GLN commissioned under the prefix (and MAY also issue a `KeyCredential` for the party GLN itself).

```
GS1 Global Office (root trust anchor)
  └─ GS1PrefixLicenseCredential  →  Member Organization DID
       └─ GS1CompanyPrefixLicenseCredential  →  Member Company DID
            │  (mandatory party GLN in organization.gs1:partyGLN)
            ├─ KeyCredential (party GLN — optional; license alone may suffice)
            └─ KeyCredential (each additional GLN; extendsCredential → company prefix license)
                 ├─ OrganizationDataCredential (organization facts; keyAuthorization → KeyCredential)
                 └─ ProductDataCredential (product facts; keyAuthorization → KeyCredential)
```

Each credential in the chain links to its parent via **`extendsCredential`** (Mandatory on `KeyCredential`; Mandatory on license credentials per GS1 Digital Licenses). The GLN `KeyCredential` `extendsCredential` MUST reference the `GS1CompanyPrefixLicenseCredential` whose `licenseValue` is the numeric prefix that the GLN starts with — see Section 3.3.5. The party GLN MAY be verified directly from the company prefix license without a `KeyCredential`; all other GLNs require one.

The **`OrganizationDataCredential`** associates organization data with the same GLN (`credentialSubject.id` Digital Link URI) and SHOULD reference the GLN `KeyCredential` via **`keyAuthorization`**.

**Company Prefix (`licenceKey`):** The attestation attribute `licenceKey` is not stored directly on the GLN credentials; verifiers derive it by resolving the `extendsCredential` chain to the `GS1CompanyPrefixLicenseCredential` and reading `licenseValue`.

### 5.2 Root trust anchors and issuer DIDs

| Anchor | Identifier / location | Purpose |
|--------|----------------------|---------|
| **GS1 Global Office DID** | `did:web:vc.gs1.org` (also `did:web:id.gs1.org` in some deployments) | Root issuer for `GS1PrefixLicenseCredential`; DID document publishes assertion keys |
| **Member Organization DID** | MO-specific `did:web:` (e.g. national GS1 body) | Issues company prefix licenses and MAY issue GLN credentials |
| **Member Company DID** | MC `did:web:` registered with MO | Subject of company prefix license; MAY issue GLN credentials when authorized |
| **Published credentials** | Resolvable credential URLs (e.g. `https://vc.gs1.org/...`, MO registry endpoints) | Chain resolution and signature verification |
| **GS1 contexts & schemas** | `https://ref.gs1.org/gs1/vc/*`, `https://id.gs1.org/vc/schema/v1/*` | Type definitions and JSON Schema validation |
| **GS1 Web Vocabulary** | `https://ref.gs1.org/voc/` | Organization and address semantics (Section 3.3.3 extension) |

Verifiers SHALL treat GO as the ultimate trust root: every valid GLN credential chain MUST terminate at a `GS1PrefixLicenseCredential` whose `issuer.id` resolves to a GO-controlled DID `did:web:vc.gs1.org` with a valid signature.

**Roles:**

| Role | Trust responsibility |
|------|---------------------|
| **GS1 Global Office** | Root of trust; issues prefix licenses to MOs; maintains GO DID document and revocation infrastructure |
| **Member Organization (MO)** | Regional licensing authority; issues company prefix licenses; MAY issue GLN credential pairs |
| **Member Company (MC)** | Licensee; MAY issue GLN credential pairs for GLNs under its prefix when MO policy permits |
| **Business Wallet (holder)** | Stores credentials; presents to Relying Parties via OpenID4VP |
| **Relying Party (verifier)** | Validates signatures, chain, status, and attribute integrity (Sections 3.3.5, 5.3, 6) |

### 5.3 Verification obligations

When a Relying Party receives a GLN attestation encoded as W3C VCDM (Section 3.3), it SHALL perform the following trust checks in order:

1. **Signature and format** — Each presented credential MUST be valid VCDM 2.0 with a verifiable issuer DID signature.
2. **Temporal validity** — `validFrom` MUST NOT be in the future; `validUntil` (if present) MUST NOT be expired.
3. **GLN assignment** — If the attested GLN is the party GLN, verify it against
   `GS1CompanyPrefixLicenseCredential` `organization.gs1:partyGLN` **or** a valid GLN
   `KeyCredential` for the same GLN (Section 3.3.5). For any other GLN, apply GLN
   `KeyCredential` rules (`extendsCredential`, issuer/subject matching, primary-key prefix
   rules) per [Validating GS1 ID Key Credentials](https://gs1.github.io/GS1DigitalLicenses/validating_keys.html).
4. **License chain** — Recursively resolve and validate each `extendsCredential` reference back to a GO-issued `GS1PrefixLicenseCredential` per [Validating GS1 License Credentials](https://gs1.github.io/GS1DigitalLicenses/license_validation.html).
5. **OrganizationDataCredential linkage** — `credentialSubject.id` MUST match the GLN Digital Link URI on the paired `KeyCredential`; `keyAuthorization` (if present) MUST resolve to that KeyCredential.
6. **Revocation** — Check `credentialStatus` on the GLN `KeyCredential` (when present), the `GS1CompanyPrefixLicenseCredential`, and every credential in the license chain (Section 6). A revoked link invalidates the entire chain.
7. **Attribute integrity** — Validate Section 2 mandatory attributes, including GLN check digit and prefix consistency (Section 2.9).

When the attestation is encoded as SD-JWT VC (Section 3.2), the Relying Party SHALL apply the base verification process (Section 4.2), validate the embedded W3C VCDM payload structure per [RFC 9901] Appendix A.4, validate revocation via the SD-JWT `status` claim only (Section 3.2.2), and MAY use `trust_anchor_url` (Section 5.4) to locate supplementary trust metadata; the underlying GS1 license chain validation remains applicable when cross-checking against published GS1 credentials referenced via `credentialSubject.keyAuthorization` and `extendsCredential`.

### 5.4 Trust anchor metadata (`trust_anchor_url`)

GLN attestations MAY include the optional `trust_anchor_url` metadata attribute (Section 2.6). When present, it SHOULD point to a document that helps verifiers establish issuer authorization within the WeBuild / EUBW trust framework — for example, a GS1 MO entry in a consortium trust list, GO DID document, or MO-published trust policy.

`trust_anchor_url` supplements but does **not replace** GS1 chain validation: verifiers MUST still resolve and validate the `extendsCredential` license chain regardless of whether `trust_anchor_url` is present.

### 5.5 Relationship to WeBuild and EUBW

Within the WeBuild KYS workflow, the GLN attestation acts as an **Electronic Attestation of Attributes (EAA)** when issued by GS1 or an authorized MO (Section 4.1.4). The GS1 trust model provides **authentic-source** assurance for organization identity and GLN assignment; it does not, by itself, satisfy broader KYS obligations (e.g. beneficial ownership, financial standing) covered by other rulebooks in the WeBuild catalog.

Relying Parties integrating GLN attestations into EUBW-compliant KYS flows SHOULD treat a valid GS1 credential chain as evidence that the presented GLN and organization attributes originate from an authorized GS1 issuer, subject to the verification obligations in Sections 5.3 and 6.

## 6 Revocation and credential status

GS1 credentials use the W3C [Bitstring Status List](https://www.w3.org/TR/vc-bitstring-status-list/) mechanism. This section specifies revocation and status requirements for GLN credentials encoded per Section 3.3.

### 6.1 Status mechanism

All GS1-issued credentials use `credentialStatus` of type `BitstringStatusListEntry` as defined in [[vc-bitstring-status-list]]. Each entry references:

- `statusListCredential` — URI of the issuer's `BitstringStatusListCredential`
- `statusListIndex` — zero-based index into the status bitstring
- `statusPurpose` — `"revocation"` (GS1 governance for suspension is under development)

| Credential type | `credentialStatus` requirement |
|-----------------|--------------------------------|
| `KeyCredential` | **MUST** be present |
| `OrganizationDataCredential` | **MAY** be present; if present, MUST be `BitstringStatusListEntry` |
| License credentials (chain) | **MUST** be present on all GS1 License Credentials |

### 6.2 Relying Party verification obligations

When verifying a GLN credential presentation, the Relying Party SHALL:

1. Validate `credentialStatus` on the GLN `KeyCredential` and on each credential in the `extendsCredential` license chain.
2. Apply the validation rules in Section 3.2 of [[vc-bitstring-status-list]] — a `credentialStatus` entry is valid only if those rules return `valid: true`.
3. Treat a revoked credential in any link of the chain as invalidating the entire chain.
4. Follow the GS1 status validation rules in [Validating Credential Status](https://gs1.github.io/GS1DigitalLicenses/validating_status.html).

Temporary unavailability of a status list endpoint does **not** imply revocation. Verifiers MAY use a cached copy of the status list and SHOULD inform the user of the cache timestamp. Issuers SHOULD set `validUntil` on credentials so that credentials do not remain valid indefinitely if status lists become permanently unavailable.

### 6.3 Issuer obligations

Issuers SHALL:

- Maintain a published `BitstringStatusListCredential` with high availability (this is the GS1 component most requiring uptime).
- Allocate a unique `statusListIndex` for each issued credential at issuance time.
- Revoke credentials by setting the corresponding bit in the status list when a GLN or license is withdrawn.
- Publish status lists at a stable, resolvable URI (JWT or JSON-LD).

GS1 Global Office publishes revocation lists via its VC wallet API; Member Organizations SHOULD publish equivalent lists for credentials they issue. Verifiers MAY use cached status lists when endpoints are temporarily unavailable and SHOULD record the cache timestamp (Section 6.2).

### 6.4 Relationship to SD-JWT VC status (Section 3.2)

When the GLN attestation is encoded as SD-JWT VC (Section 3.2), revocation **SHALL** be
validated using the SD-JWT VC `status` claim (Section 3.2.2). The embedded VCDM payload MAY
include a `credentialStatus` property (`BitstringStatusListEntry`) for structural parity with
GS1 license credentials, but verifiers **SHALL NOT** use `credentialStatus` for revocation
checks in the SD-JWT path. W3C VCDM and JSON-LD credentials (Section 3.3) continue to use
`credentialStatus` as defined in Section 6.1–6.2.

## 7 Compliance

This GLN Attestation Rulebook is designed for use within the European Business Wallet (EUBW) framework and WeBuild consortium attestation catalog. Key compliance considerations:

- **eIDAS 2 / EAA classification** — When issued by GS1 or an authorized MO, the attestation is classified as an Electronic Attestation of Attributes (`attestation_legal_category: EAA`) per Regulation (EU) 2024/1183 (Section 4.1.4).
- **Data minimization** — Selective disclosure (Section 3.2) and optional attributes (Section 2.3) support GDPR-aligned data minimization; issuers SHOULD not include attributes beyond those required for the KYS use case.
- **KYS scope** — This rulebook covers GS1 organization identity and registered address only. Broader KYS requirements (beneficial ownership, AML, financial verification) are addressed by separate rulebooks in the WeBuild catalog.
- **GS1 licensing terms** — Credential issuance and use remain subject to GS1 Member Organization licensing policies and the [GS1 Digital Licenses](https://gs1.github.io/GS1DigitalLicenses/) governance model.

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
| [RFC 9901]                               | RFC 9901 — Selective Disclosure for JWTs (SD-JWT), T. Looker et al., January 2026. Appendix A.4 defines embedding W3C VCDM 2.0 payloads in SD-JWT |
| [SD-JWT VC]	                            | SD-JWT-based Verifiable Credentials (SD-JWT VC). Available: https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/, version draft-ietf-oauth-sd-jwt-vc-09|
| [GS1 Digital Licenses]                 | GS1 Digital Licenses — Developers Introduction to the GS1 Digital License Ecosystem. Available: https://gs1.github.io/GS1DigitalLicenses/ ([GitHub](https://github.com/gs1/GS1DigitalLicenses)) |
| [GS1 Web Vocabulary]                   | GS1 Web Vocabulary (Organization, PostalAddress, Country). Available: https://ref.gs1.org/voc/ |
| [VC-DATA-MODEL-2.0]                    | W3C Verifiable Credentials Data Model 2.0. Available: https://www.w3.org/TR/vc-data-model-2.0/ |
| [VC-JOSE-COSE]                         | Securing Verifiable Credentials using JOSE and COSE. Available: https://www.w3.org/TR/vc-jose-cose/ |
| [VC-BITSTRING-STATUS-LIST]             | W3C Bitstring Status List. Available: https://www.w3.org/TR/vc-bitstring-status-list/ |
