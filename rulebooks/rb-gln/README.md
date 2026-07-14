# Attestation Rulebook for attestations of type GLN Number (Global Location Number)

* Author(s):
  * [Dominik Halbeisen, GS1 Switzerland](dominik.halbeisen@gs1.ch)
  * [Dr. Sebastian Schmittner, EECC](mailto:sebastian.schmittner@eecc.de)
  * [Christian Fries, EECC](mailto:christian.fries@eecc.de)
* Previous Authors
* Reviewer(s):
  * [Florin Coptil, Robert Bosch GmbH](florin.coptil@de.bosch.com)
  * [Dominic Hurni, SBB]

| Version | Date       | Description                                                     |
|---------|------------|-----------------------------------------------------------------|
| 0.1     | 01.06.2026 | Initial draft based on the WeBuild design attestations meetings |
| 0.6     | 29.06.2026 | update layout and review gln                                    |
| 0.7     | 30.06.2026 | Major updates to include the GS1 Trust Chain details            |
| 0.8     | 13.07.2026 | Data model refinement, aligning rule book with existing GS1 Trust Chain Data Models        |


* Contact:
  * [Florin Coptil](mailto:florin.coptil@bosch.com)*
  
* Feedback:

---

## 1 Introduction

This document describes the productive GS1 Trust Eco System, in particular the trust chain leading to the Organization Data Credential. The Organization Data Credential serves as the electronic attribute attestation (EAA) of the companies GLN, legal name and further properties such as address, parent organization, etc. [see gs1:organization Data Model in the gs1 web vocabulary](https://ref.gs1.org/voc/Organization). Certificates further up in the credential chain, such as the GS1 Company Prefix (GCP) credential, may be used as an EAA covering the most important attributes, such as GLN and legal name only in case of the GCP credential. The normative definition of the credential chain and its verification constraints is given in [Section 4](#4-GS1-Trust-Chain).

The GS1 GLN attestation provides a verifiable, standardized representation of a legal entity's GS1-registered identity and organization data, based on a company's Global Company Prefix, thereby supporting supply chain transparency and supplier due diligence within KYS processes.

The main advantage of the GLN credential is to connect the well established GS1 eco system of item, location and company identifiers to the EUBW. Since the GS1 ecosystem is already using verifiable Credentials (VC) as trusted and verifiable electronic attribute attestations, the connection to the EUBW is straight forward, even in terms of the technology.

### 1.1 Document scope and purpose

Within the Know Your Supplier (KYS) process, the GS1 GLN Attestation supports supply chain integrity by:

- Enabling to verify the supplier's registration in a globally recognized and globally interoperable identification system.
- Enabling trusted location and organization data.
- Contributing to reduce fraud and counterfeit risks through validated identification.
- Providing documented evidence for regulatory and audit compliance.

Overall, integrating GS1 GLN attestation into the EUBW KYS process enhances transparency, data reliability, and, most importantly, connects an already existing well established ID system for supplier due diligence across global operations.

The GS1 GLN attestation typically validates:

- The legal entity name registered with GS1
- The Global Location Number GLN of an organization, based on the Global Company Prefix licensed by GS1 to the holder of the GLN
- The entity's address and country as registered with GS1
- Confirmation of active membership and authorization to issue GS1 identifiers

The last point is a major benefit of adding the GLN attestation to the EUBW. The GCP license credential, which **must** be present in the credential chain leading to the `OrganizationDataCredential` used as the GLN EAA (see [Section 4](#4-GS1-Trust-Chain)), authorizes the holder to issue GS1 Key Credentials. This means that the provenance of Global Trade Item Identification Numbers (GTINs) **can** be verified on the basis of the GLN EAA.



### 1.2 Document structure

This Rulebook is structured as follows:

- Chapter 2 describes the attestation attributes and metadata in an encoding-independent
  manner, including the data model.
- Chapter 3 specifies how the attestation attributes and metadata are encoded: 
  - Section 3.2 covers SD-JWT VC-based encoding
  - Section 3.3 covers W3C VCDM (GS1 Digital Licenses) encoding
- Chapter 4 defines the GS1 credential chain, its verification constraints, the issuance process, and Relying Party obligations in KYS workflows.
- Chapter 5 defines the GS1 trust model, trust anchors, and how chain validation fits into the broader GS1 Digital License hierarchy.
- Chapter 6 defines revocation mechanisms for the attestation.
- Chapter 7 provides compliance information regarding the EUBW framework and applicable data protection laws.
- Chapter 8 provides references to applicable standards and specifications.

### 1.3 Keywords

This document uses the capitalised keywords '**SHALL**' or '**MUST**' ('**NOT**'), '**SHOULD**' ('**NOT**')/('**NOT**') '**RECOMMENDED**' and '**MAY**' as specified in
[RFC 2119](https://www.rfc-editor.org/info/rfc2119/), i.e. to indicate requirements, recommendations and options specified in this
document. 

In addition, '**must**' (non-capitalised) is used to indicate an external constraint, i.e. a
requirement that is not mandated by this document, but, for instance, by an external document.
The word '**can**' indicates a capability, whereas other words, such as 'will', and 'is' or 'are'
are intended as statements of fact.

### 1.4 Terminology

| Term                                       | Description                                                                                                                                                                  |
|--------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Global Location Number (GLN)               | A 13-digit GS1 identifier used to uniquely identify legal entities and physical locations within global supply chains. Issued by the legal entity with a matching GS1-issued Global Company Prefix        |
| GS1 Company Prefix (GCP) | The licence issued by a GS1 MO to an legal entity (organization), forming the basis upon which GLNs and other GS1 identifiers are constructed.                                               |
| GS1 Member Organization (GS1 MO) | A member organization of GS1 such as GS1 Germany, GS1 US, GS1 France, etc. |
| GS1 Global Office (GS1 GO, legal name: GS1 AISBL)           | Overarching GS1 orchanization for the global coordination of all GS1 MOs                                                           |
| Electronic Attribute Attestation (EAA)                              |
| Relying Party                              | An entity that relies on the attestation data presented by a Wallet Instance to make trust decisions. Relying Party and "Verifier" are used to mean exactly the same when refering to a party/role.                                                                        |
| Issuer                                     | The entity responsible for creating and signing an attestation and ensuring mandatory attributes are present.                                                                 |

## 2 Attestation attributes and metadata

The GLN Number Attestation is designed to provide a verifiable, standardized representation of
a legal entity's GS1-registered identity and organization data, supporting supply chain transparency and 
supplier due diligence within KYS processes.

This attestation type **SHOULD** be classified as **"EAA"** when issued based on the GS1 trust eco system, i.e. when a complete credential chain certifies this. The normative definition of a valid chain and its verification constraints are given in [Section 4](#4-GS1-Trust-Chain).


### 2.1 Data Model

The GLN EAA is a [GS1 Organization Data Credential, as described in https://gs1.github.io/GS1DigitalLicenses section 7.3.2](https://gs1.github.io/GS1DigitalLicenses/#organization-data-credential).

The attributes below are based on the [GS1 Web Vocabulary](https://ref.gs1.org/voc/). Terms use the `gs1:` prefix (namespace `https://ref.gs1.org/voc/`). JSON-LD paths for the WeBuild KYS address extension are specified in Section 3.3.3.

#### Data types

Attribute **Type** values in the tables below use standard RDF / JSON-LD datatype IRIs. JSON-LD uses the `xsd:` prefix for [XML Schema Definition (XSD)](https://www.w3.org/TR/xmlschema11-2/) datatypes (namespace `http://www.w3.org/2001/XMLSchema#`), not `xs:`.

| **Type** | **Description** |
|----------|-----------------|
| `rdf:langString` | A language-tagged string. Properties of this type are **localized**: each value **MUST** carry a BCP 47 language tag. Multiple language variants **MAY** be provided. |
| `xsd:string` | A plain lexical string without a language tag. |
| `xsd:anyURI` | A URI or IRI. |

**Example — localized `rdf:langString` property:**

```json
"gs1:organizationLegalName": {
  "@value": "EECC GmbH",
  "@language": "de"
}
```

Multiple localized values **MAY** be expressed as an array of such objects.



### 2.2 Mandatory Attributes

#### 2.2.1 GLN and Name

The GLN EAA **must** contain a `credentialSubject["gs1:organization"]` which **must** contain the following attributes:

| **Attribute** | **Definition**                                      | **Type**  |
|------------------------|-----------------------------------------------------|----------------|
| `gs1:organizationName` | The entity name registered with GS1 (localized)      | `rdf:langString` |
| `gs1:partyGLN`         | The 13 digit main party GLN of the company           | `xsd:string`   |

Notice that the GLN might start with a 0 and hence `xsd:integer` is not an apropriate representation of this id.

| **Attribute** | **Definition**                                      | **Type**  |
|------------------------|-----------------------------------------------------|----------------|
| `credentialSubject.id` | Digital Link URI representation of the GLN           | `xsd:anyURI`   |

The `credentialSubject.id` **must** be a url with a path ending in `/417/{gs1:partyGLN}`.

Additionally, the GLN EAA's `credentialSubject["gs1:organization"]` **MUST** contain

| **Attribute** | **Definition**                                      | **Type**  |
|------------------------|-----------------------------------------------------|----------------|
| `gs1:organizationLegalName` | The legal entity name registered with GS1 (localized)      | `rdf:langString` |

#### 2.2.2 Address

The GLN EAA of type `OrganizationDataCredential` **MUST** contain a `credentialSubject["gs1:organization"]["gs1:address"]` which is a `gs1:PostalAddress` per the [GS1 Web Vocabulary PostalAddress](https://ref.gs1.org/voc/PostalAddress) data model. The country code of the address **MUST** be present. Depending on the country, all other attributes needed to make a valid postal address in that country **SHOULD** be present.

For a typical European postal addresses, `gs1:streetAddress` **SHOULD** be used for the primary address line. Additional address detail **MAY** be expressed in `gs1:streetAddressLine2` through `gs1:streetAddressLine4`. For post-office-box addresses, `gs1:postOfficeBoxNumber` **SHOULD** be used instead of street address lines.

The most important attributes of `credentialSubject["gs1:organization"]["gs1:address"]` that **SHOULD** be used depending on address type and country for the GLN EAA are

| **Attribute** | **Definition**                                                                        | **Type**       |
|------------------------|---------------------------------------------------------------------------------------|---------------------|
| `gs1:streetAddress`    | The primary street address line as free-form text (e.g. street name and house number, or building name). **SHOULD** be used before populating additional street lines. (localized) | `rdf:langString`    |
| `gs1:streetAddressLine2` | The second street address line as free-form text (e.g. building, unit, or c/o information). (localized) | `rdf:langString`    |
| `gs1:streetAddressLine3` | The third street address line as free-form text. (localized)                          | `rdf:langString`    |
| `gs1:streetAddressLine4` | The fourth street address line as free-form text. (localized)                          | `rdf:langString`    |
| `gs1:postOfficeBoxNumber` | The number identifying a post-office box; **SHOULD** be used instead of street address lines for PO box addresses. | `xsd:string`        |
| `gs1:postalName`       | The postal recipient name; **MAY** differ from `gs1:organizationName`. (localized)    | `rdf:langString`    |
| `gs1:postalCode`       | The postal code where the legal entity is registered or operates                      | `xsd:string`        |
| `gs1:addressLocality`  | The locality (e.g. city) where the legal entity is registered or operates. (localized) | `rdf:langString`    |
| `gs1:addressRegion`    | The province or state (e.g. in abbreviated form) where the legal entity is registered or operates. (localized) | `rdf:langString`    |
| `gs1:addressSuburb`    | A suburb within a town or city. (localized)                                           | `rdf:langString`    |
| `gs1:countryCode`      | ISO 3166-1 alpha-2 country code (nested in `gs1:addressCountry` → `gs1:Country`)      | `xsd:string`        |

Other attributes of `gs1:PostalAddress` data model **MAY** also be used if needed.


#### 2.2.3 GS1 Trust Chain Link

The `OrganizationDataCredential` **must** link into the GS1 credential chain as specified in [Section 4](#4-GS1-Trust-Chain):

- When a GLN `KeyCredential` is present in the chain, `credentialSubject.keyAuthorization` (**SHOULD** be present) **must** be a resolvable URL referencing that `KeyCredential`.
- When no GLN `KeyCredential` is present, the `OrganizationDataCredential` **must** reference the matching `GS1CompanyPrefixLicenseCredential` directly (via `credentialSubject.keyAuthorization` or an equivalent resolvable chain link), in the same way a `KeyCredential` references its parent GCP credential via `extendsCredential`.

See [Section 4](#4-GS1-Trust-Chain) for the full set of chain composition and linkage constraints.


### 2.4 Mandatory metadata

The GLN EAA is a [GS1 Organization Data Credential](https://gs1.github.io/GS1DigitalLicenses/#organization-data-credential), which is a subtype of `DataCredential`. GS1 Data Credentials use the [W3C Verifiable Credentials Data Model Version 2.0](https://www.w3.org/TR/vc-data-model-2.0/) ([vc-data-model-2.0]). The VCDM credential format uses JSON-LD to encapsulate the details in a format that is well understood worldwide. A few optional properties of the W3C VCDM are mandatory in GS1 Data Credentials. These are outlined in [GS1 Data Credential Details (Section 7.2)](https://gs1.github.io/GS1DigitalLicenses/#data-credential-details).

#### 2.4.1 GS1 Data Credential VCDM core properties

| **Property** | **Requirement** |
|--------------|-----------------|
| `@context` | In addition to the W3C VCDM 2.0 context, the GS1 Data Credential context **MUST** be included. For `OrganizationDataCredential`, this is the [organization context](https://ref.gs1.org/gs1/vc/organization-context) (see Section 3.3.1). |
| `id` | This property is optional in the VCDM but **MUST** be present in all GS1 Data Credentials. |
| `type` | This property **MUST** contain `VerifiableCredential` and **MUST** also contain `DataCredential`. For the GLN EAA, the type array **MUST** additionally include `OrganizationDataCredential` (see Section 3.3.1). |
| `issuer.id` | This property **MUST** be a Decentralized Identifier (DID) as defined in [did-1.1]. |
| `credentialSubject.id` | This property is optional in the VCDM but **MUST** be present and **MUST** be a [GS1 Digital Link URI](https://www.gs1.org/standards/Digital-Link/) as defined in [gs1-digital-link] (see Section 2.2.1). |
| `credentialStatus` | This property is optional in the VCDM but **MAY** be present. If present, this property **MUST** be of the type `BitstringStatusListEntry` defined in [vc-bitstring-status-list]. |
| `credentialSchema` | This property is optional in the VCDM but **MUST** be present in all GS1 Data Credentials and **MUST** be of the type `JsonSchema` defined in [vc-json-schema]. |
| `validFrom` | This property is optional in the VCDM but **MUST** be present in all GS1 Data Credentials. |
| `renderMethod` | This property is optional in the VCDM but **SHOULD** be present and **SHOULD** be of the type `TemplateRenderMethod` in [vc-render-method]. |

#### 2.4.2 WeBuild / EUBW additional mandatory metadata

When the GLN EAA is encoded as SD-JWT VC (Section 3.2), the following additional top-level claims are mandatory:

| **Data Identifier**        | **Definition**                                                                                              | **Type** |
|----------------------------|-------------------------------------------------------------------------------------------------------------|----------|
| `attestation_legal_category` | Indicates the legal category of this attestation (`EAA` or `QEAA`)                                        | `xsd:string` |
| `vct`                      | A unique identifier (URL or URN) for the credential type, indicating which claims **must** be present and which **can** be selectively disclosed | `xsd:anyURI` |

Encoding-independent metadata identifiers used elsewhere in this rulebook map to the GS1 VCDM properties above as follows: `issuance_date` → `validFrom`; `expiry_date` → `validUntil` (**SHOULD** be set); `issuing_entity` → `issuer.id`. See Section 3.4 for the full mapping.

### 2.5 Optional metadata

| **Data Identifier** | **Definition**                                                             | **Type** |
|---------------------|----------------------------------------------------------------------------|----------|
| `trust_anchor_url`  | URL where the trust anchor for verifying this attestation **can** be retrieved | `xsd:anyURI` |
| `schema_version`    | Version of the schema used                                                 | `xsd:string` |
| `description`       | A human readable description of the content and purpouse of this credential/attestation | `xsd:string` |


### 2.7 Value Lists

#### 2.7.1 Country Codes

For a complete list, refer to the ISO 3166-1 alpha-2 standard. Some Examples:

| **Code** | **Country**  |
|----------|--------------|
| DE       | Germany      |
| CH       | Switzerland  |
| FR       | France       |
| IT       | Italy        |
| ES       | Spain        |
| ... | ... |



### 2.8 Integrity Rules

The following integrity rules **MUST** be enforced:

- `organizationName` **must not** be empty and contain at least one non-empty localized string.
- `organizationLegalName` **MUST NOT** be empty and contain at least one non-empty localized string.
- `partyGLN` **must** be the 13 digit GLN string.
- `postal_code` **MUST** be a non-empty string.
- `locality` **MUST** be a non-empty string.
- `region` **MUST** be a non-empty string.
- `country` **MUST** be a valid ISO 3166-1 alpha-2 country code.
- Each attribute identifier **MUST** appear at most once within its respective object scope.
- `partyGLN` **MUST** match the `{GLN}` assigned in the matching `GS1CompanyPrefixLicenseCredential` in the credential chain.
- When a GLN `KeyCredential` is present in the chain, `partyGLN` **MUST** also be verifiable against that credential (see [Section 4](#4-GS1-Trust-Chain)).

For the detailed constraints of credential-chain verification, see [Section 4](#4-GS1-Trust-Chain).


## 3 Attestation encoding

### 3.1 ISO/IEC 18013-5-compliant encoding

ISO/IEC 18013-5 (also called mdoc) is out of scope for this Rulebook, as offline proximity
presentation is not a current requirement for the GLN Number attestation.

### 3.2 SD-JWT VC-based encoding

The GLN EAA **MAY** be encoded in the SD-JWT VC format to allow for selective disclosure of attestation attributes.

However, the only actual use case for selective disclosure that is foreseen at the time of writing would be to present the GLN while not disclosing the address, in which case the holder might as well present just the GLN `KeyCredential` from the credential chain or even just the `GS1CompanyPrefixLicenseCredential` rather than presenting the `OrganizationDataCredential`. Either credential **must** still be validated as part of the complete chain defined in [Section 4](#4-GS1-Trust-Chain). This would serve exactly the same purpose without the technical complexity of hash obfuscation/disclosure.


The SD-JWT payload for the GLN EAA **MUST** embed a [W3C Verifiable Credentials Data Model 2.0](https://www.w3.org/TR/vc-data-model-2.0/) (VCDM) credential structure as defined in [RFC 9901] Appendix A.4. 
The top-level VCDM properties (`@context`, `type`, `issuer`, `credentialSubject`, `credentialSchema`, and related metadata) are carried directly in the JWT claims set. Selectively disclosable claims within `credentialSubject` are represented as `_sd` digests at issuance time per [RFC 9901]. Holder binding (only applicable to the license credentials in the credential chain; see Section 4) **MUST** use a `cnf` claim at the top level of the SD-JWT payload. The WeBuild-specific `vct` and `attestation_legal_category` claims are additional top-level JWT claims REQUIRED by the SD-JWT VC profile. Revocation status for SD-JWT verification **MUST** use the SD-JWT VC `status` claim (see Section 3.2.2).

The embedded VCDM payload of the GLN EAA **SHOULD** use the GS1 `OrganizationDataCredential` type (see Section 2), although the `KeyCredential` or `GS1CompanyPrefixLicenseCredential` which **must** be present in the credential chain of the `OrganizationDataCredential` (Section 4) may be presented instead when the GS1 registered address is not to be disclosed.

**Selective Disclosure:** When using the `OrganizationDataCredential` data model, the `gs1:address` porperty **MAY** be selectively disclosable, enabling a legal entity to disclose only the attributes requested by a Relying Party.


**Verifiable Credential Type (`vct`):** `vct: eu.we-build.gln.1`



> :warning: **TBD:** Also assign vcts to `KeyCredential`, etc.?
> Could be `"vct": "https://gs1.org/voc/OrganizationDataCredential"`

#### 3.2.1 Attribute Encoding Table


All claims listed in Section 2 above **MUST** be present in plain text in the JWT payload and **MUST NOT** be hash-obfuscated, unless explicitly listed below.

**Claims that MAY be hash-obfuscated** (`_sd` digests per [RFC 9901]):

- `credentialSubject.organization.gs1:address` 
  - the entire object, including all nested address properties
- `renderMethod`
  - the entire object, including all nested properties

**Notes:**

- Attribute paths use dot notation for nested JWT claims; GS1 vocabulary terms retain their `gs1:` prefix as JSON property names (compact JSON-LD form).
- Issuers **SHOULD** include `https://ref.gs1.org/voc/` in `@context` when emitting address and legal-name properties (Section 3.3.3).
- `iat`, `exp`, and `iss` follow RFC 7519; `validFrom`, `validUntil`, and `issuer` follow VCDM 2.0. Issuers **SHOULD** keep JWT and VCDM temporal and issuer values consistent.

#### 3.2.2 Status Claim

For SD-JWT VC-compliant GLN EAA, revocation status **MUST** be expressed and
validated using the SD-JWT VC `status` claim. When the attestation technical validity period is
greater than 24 hours, the `status` claim **MUST** be present.

The embedded W3C VCDM payload **MAY** additionally carry a `credentialStatus` property
(`BitstringStatusListEntry`) for structural parity with GS1 Digital Licenses (Section 6.1), but it the issuer **SHULD** rather just include the status list in one place matching the chosen serialization format. If the status list is represented twice it **MUST** be the exact same status list.
Relying Parties verifying an SD-JWT VC presentation **MUST** validate revocation only via the
`status` claim and **MUST NOT** treat `credentialStatus` as authoritative in the SD-JWT path,
even when both are present.

The `status` claim **MUST** be a JSON object with the following members:

- `type` (string): **MUST** be `"status-list"`.
- `status_list_credential` (string, URI): The URI of the Status List Credential document that
  contains the status bitstring.
- `status_list_index` (integer, >= 0): The zero-based index into the status list bitstring that
  corresponds to this credential.
- `status_purpose` (string): **MUST** be `"revocation"` for this attestation.

When present in the embedded VCDM payload, `credentialStatus` **SHOULD** describe the same
status list entry as the `status` claim (equivalent `statusListCredential` /
`status_list_credential` and index values).

**Examples:**

**SD-JWT VC `status` claim**

Defined in https://www.ietf.org/archive/id/draft-ietf-oauth-status-list-21.html

The SD-JWT definition of status lists omits purpose. Therefor the purpose `revocation` is assumed for GS1 specific credentials.

```json
"status": {
    "status_list": {
      "idx": 67609,
      "uri": "https://company-wallet-dev.prod-k8s.eecc.de/api/registry/status/revocation/20c50bdb-40f0-4466-bcc9-1ce695900dad"
    }
  }
```


**W3C Data Model 2.0 `credentialStatus` claim**

Defined in https://www.w3.org/TR/vc-bitstring-status-list

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
the SD-JWT compact serialization. 

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
  "status": {
    "status_list": {
      "idx": 67609,
      "uri": "https://company-wallet-dev.prod-k8s.eecc.de/api/registry/status/revocation/20c50bdb-40f0-4466-bcc9-1ce695900dad"
    }
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

For examples of the credentials in the credential chain (Section 4), see Section 3.3.6 below.


> :warning: TBD: Should we also include an SD-JWT representation of the other credentials in the chain? 
> Proposition: Apply the same the same W3C DM wrapper to have a generic solution


### 3.3 W3C Verifiable Credentials Data Model-based encoding

The GLN EAA **MAY** be encoded using the [W3C Verifiable Credentials Data Model 2.0](https://www.w3.org/TR/vc-data-model-2.0/) (VCDM). It is an `OrganizationDataCredential` as defined in the [GS1 Digital Licenses](https://gs1.github.io/GS1DigitalLicenses/) specification.

GLN verification in the GS1 ecosystem relies on a credential chain whose composition and validation constraints are defined normatively in [Section 4](#4-GS1-Trust-Chain). At minimum, the chain comprises an `OrganizationDataCredential`, a matching `GS1CompanyPrefixLicenseCredential` (GCP credential), and a matching `GS1PrefixLicenseCredential` (Prefix credential); it **may** additionally include a matching GLN `KeyCredential`. The credential types involved are:

| Credential type | Role in the chain |
|-----------------|-------------------|
| `GS1PrefixLicenseCredential` | Root license issued by GS1 Global Office (GO) to a Member Organization (MO); **mandatory** in every chain (Section 4). |
| `GS1CompanyPrefixLicenseCredential` | Company prefix license issued by an MO; carries the mandatory party GLN in `credentialSubject.organization.gs1:partyGLN`; **mandatory** in every chain (Section 4). |
| `KeyCredential` | Asserts that a specific GLN has been commissioned; **optional** but **must** be validated when present; extends from the GCP credential via `extendsCredential` (Section 4). |
| `OrganizationDataCredential` | Carries organization facts (legal name, party GLN, address); the GLN EAA; see [Organization Data Credential Examples](https://gs1.github.io/GS1DigitalLicenses/#sample-organization-data-credential). |

Encoding-specific VCDM requirements for each credential type are given in Sections 3.3.1–3.3.3; GS1-specific `extendsCredential` resolution rules are in Section 3.3.5.


> :warning: TBD: What are the WeBuild Credential format requirements?
> Needs to be determined by Florin and Dominik


European Business Wallet presentations in the WeBuild KYS workflow **MAY** use SD-JWT VC (Section 3.2) or W3C VCDM depending on wallet and verifier capability. SD-JWT VC encoding (Section 3.2) embeds the same GS1 VCDM 2.0 payload structure as JSON-LD or JWT-secured credentials (Section 3.3), following [RFC 9901] Appendix A.4; selective disclosure applies to claims within `credentialSubject` while VCDM envelope properties remain always visible.

##### 3.3.1 JSON-LD contexts and credential types

| Credential type | `@context` entries (minimum) | Defined in |
|-----------------|------------------------------|------------|
| `GS1CompanyPrefixLicenseCredential` | `https://www.w3.org/ns/credentials/v2`, `https://ref.gs1.org/gs1/vc/license-context` | [license-context](https://ref.gs1.org/gs1/vc/license-context) |
| `KeyCredential` | `https://www.w3.org/ns/credentials/v2`, `https://ref.gs1.org/gs1/vc/declaration-context` | [declaration-context](https://ref.gs1.org/gs1/vc/declaration-context) |
| `OrganizationDataCredential` | above + `https://ref.gs1.org/gs1/vc/organization-context` | [organization-context](https://ref.gs1.org/gs1/vc/organization-context) |

The `type` array **MUST** include `VerifiableCredential` and the respective GS1 type. License credentials in the backing chain use `https://ref.gs1.org/gs1/vc/license-context` — see Section 3.2.3. The company prefix license **must** includes `credentialSubject.organization.gs1:partyGLN` (the main party GLN only).

##### 3.3.2 KeyCredential (GLN identity)

A GLN `KeyCredential` asserts that the licensee has commissioned a specific GLN. The party GLN **MAY**
alternatively be verified via the parent `GS1CompanyPrefixLicenseCredential` (Section 3.3.5).
Normative requirements from [ID Key Credential Details](https://gs1.github.io/GS1DigitalLicenses/#key-credentials-details):

| **VCDM property** | **Requirement** |
|-------------------|-----------------|
| `credentialSubject.id` | **MUST** be a [GS1 Digital Link URI](https://www.gs1.org/standards/Digital-Link/) for the GLN (primary key **K**, no key qualifiers) |
| `extendsCredential` | **Mandatory** — **MUST** reference the parent GS1 Company Prefix Credential per Section 3.3.5 |
| `issuer.id` | **MUST** be a DID |
| `validFrom` | **MUST** be present |
| `name` | **MUST** be present (**SHOULD** be `"GS1 ID Key Credential"`) |
| `description` | **MUST** be present |
| `credentialStatus` | **MUST** be present; type `BitstringStatusListEntry` |
| `credentialSchema` | **MUST** be present; type `JsonSchema` (e.g. `https://id.gs1.org/vc/schema/v1/key`) |
| `id` | **MUST** be present; **SHOULD** be a globally unique resolvable URL |
| `renderMethod` | **SHOULD** be present; type `TemplateRenderMethod` |

The GLN is encoded in `credentialSubject.id` as a GS1 Digital Link URI with application identifier **417** (e.g. `https://id.gs1.org/417/{GLN}`), not as a separate claim property. See the [GLN Key Credential example](https://gs1.github.io/GS1DigitalLicenses/#gln-key-credential) in GS1 Digital Licenses.

##### 3.3.3 OrganizationDataCredential (organization data)

The GLN EAA is a `OrganizationDataCredential` which is a `DataCredential` subtype that carries organization facts for the GLN identified in `credentialSubject.id`. Normative requirements from [Organization Data Credential](https://gs1.github.io/GS1DigitalLicenses/#organization-data-credential) and [GS1 Data Credential Details](https://gs1.github.io/GS1DigitalLicenses/#data-credential-details):

| **Property** | **Requirement** |
|--------------|-----------------|
| `id` | **MUST** be present |
| `credentialSubject.id` | **MUST** be the same GLN GS1 Digital Link URI as the corresponding `KeyCredential` |
| `organization` | **Mandatory** — **MUST** contain `gs1:partyGLN` and `gs1:organizationName` (see [Organization Data JSON Schema](https://id.gs1.org/vc/schema/v1/organizationdata)) |
| `keyAuthorization` | **SHOULD** reference the GLN `KeyCredential` when present; if no `KeyCredential` is in the chain, **MUST** reference the matching `GS1CompanyPrefixLicenseCredential` directly (Section 4) |
| `validFrom` | **MUST** be present (DataCredential base requirement) |
| `credentialStatus` | **MAY** be present; if present, **MUST** be `BitstringStatusListEntry` |
| `credentialSchema` | **MUST** be present; type `JsonSchema` |
| `renderMethod` | **SHOULD** be present (DataCredential base requirement) |

See Section 2 for the detailed data model.


**Note:** In the GS1 Web Vocabulary, `gs1:address` is an optional object property of `gs1:Organization` (typed `gs1:PostalAddress`). The normative GS1 `OrganizationDataCredential` schema does not require it; this rulebook makes address attributes mandatory for the WeBuild KYS attestation. The value under `gs1:address` reflects the organization's address as recorded in GS1 membership data. It **MAY** therefore differ from the statutory registered address held by national commercial registers (e.g. the German Handelsregister) or from addresses attested by other authentic sources in European Business Wallet (EUBW) KYS flows (e.g. EUCC). Relying Parties assembling multi-credential wallet presentations **SHOULD** treat each address as source-specific and **MUST NOT** assume equivalence across attestations without explicit cross-checking.

Issuers **SHOULD** include `https://ref.gs1.org/voc/` (or an equivalent GS1 vocabulary context) in `@context` alongside `organization-context` when emitting extended organization properties. MO policy **MAY** restrict which optional vocabulary terms (e.g. `gs1:streetAddress`) may not or must be included.


##### 3.3.5 Link to GS1 license chain (`extendsCredential`)

The `extendsCredential` property on license credentials and GLN `KeyCredential`s is **Mandatory** per [GS1 Digital Licenses](https://gs1.github.io/GS1DigitalLicenses/). Chain composition and the required references between credentials are defined normatively in [Section 4](#4-GS1-Trust-Chain). This section specifies additional GS1-specific resolution rules for `extendsCredential` that complement Section 4.

Verifiers **MUST** apply these rules when resolving the chain:

**Party GLN vs. additional GLNs:** Each `GS1CompanyPrefixLicenseCredential` carries exactly one
mandatory party GLN in `credentialSubject.organization.gs1:partyGLN` — the main legal-entity
GLN assigned with the company prefix. It does **not** list other location GLNs under that
prefix.

- When the attested GLN equals the party GLN on a valid `GS1CompanyPrefixLicenseCredential`,
  verifiers **MAY** accept either that license credential (reading `organization.gs1:partyGLN`) **or**
  a GLN `KeyCredential` for the same GLN as sufficient evidence of GLN assignment.
- When the attested GLN is **not** the party GLN, verifiers **MUST** require a valid GLN
  `KeyCredential` whose `credentialSubject.id` Digital Link URI identifies that GLN.

**`extendsCredential` chain rules:**
- If `credentialSubject.id` contains a GS1 Digital Link with primary key **K** and **no key qualifiers**, then `extendsCredential` **MUST** reference a GS1 License Credential whose `licenseValue` is the prefix string that **K** starts with (typically the `GS1CompanyPrefixLicenseCredential` for the company prefix).
- If `credentialSubject.id` contains primary key **K** **with key qualifiers**, then `extendsCredential` **MUST** reference a `KeyCredential` whose `credentialSubject.id` contains the same primary key **K** without qualifiers.

Verifiers **MUST** additionally validate the full license chain back to a GS1 Global Office root credential (`GS1PrefixLicenseCredential`), including signature verification and revocation status at each hop — see [Validating GS1 ID Key Credentials](https://gs1.github.io/GS1DigitalLicenses/validating_keys.html), [Validating GS1 License Credentials](https://gs1.github.io/GS1DigitalLicenses/license_validation.html), and [Section 4](#4-GS1-Trust-Chain). A reference implementation of GS1 chain validation is available at https://github.com/european-epc-competence-center/vc-verifier-rules

For a GLN `KeyCredential` **K** with subject Digital Link **D** and parent credential **P** (at `extendsCredential`), verifiers **MUST** also apply ([validating_keys.html](https://gs1.github.io/GS1DigitalLicenses/validating_keys.html)):

- **K** **MUST** be valid VCDM 2.0 with a valid issuer DID signature; **K** `validFrom` **MUST NOT** be in the future.
- If **D** has primary key **PK** without key qualifiers: **P** **MUST** be a valid GS1 License Credential; `issuer(K)` **MUST** match `credentialSubject(P)`; **PK** **MUST** begin with `licenseValue` from **P**.
- If **D** has key qualifiers: **P** **MUST** be a valid GS1 ID Key Credential; `issuer(K)` **MUST** match `issuer(P)`; primary key of **P**'s subject **MUST** equal **PK**.

The `OrganizationDataCredential` links into the chain via `keyAuthorization` as specified in [Section 4](#4-GS1-Trust-Chain) (referencing either the GLN `KeyCredential` or, when absent, the `GS1CompanyPrefixLicenseCredential` directly).

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

The following non-normative example shows the parent `GS1CompanyPrefixLicenseCredential`
from the credential chain (Section 4) in JSON-LD form with an embedded `DataIntegrityProof`. A Member
Organization issues this credential to authorize a company to use a GS1 Company Prefix.
`credentialSubject.organization.gs1:partyGLN` is **mandatory** and identifies the company's
main **party GLN** — the primary legal-entity GLN assigned with the prefix license. The
company prefix license carries **only** this party GLN, not additional location GLNs.

GLN `KeyCredential`s for other GLNs commissioned under the same prefix **MUST** extend from
this company prefix license (or from another `KeyCredential` per Section 3.3.5) via
`extendsCredential`. For the **party GLN** itself, verifiers **MAY** establish GLN validity from
either the `GS1CompanyPrefixLicenseCredential` (via `organization.gs1:partyGLN`) or a GLN
`KeyCredential` whose `credentialSubject.id` Digital Link URI identifies the same GLN. For
**any other GLN** under the company prefix, a valid GLN `KeyCredential` **MUST** be present in the chain (Section 4).

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


### 3.4 Mapping of attestation attributes

The following table summarizes where each attribute of the general data model (Section 2) is mapped in VCDM JSON-LD serialization (Section 3.3) and SD-JWT VC serialization (Section 3.2). Paths use dot notation; GS1 vocabulary terms retain their `gs1:` prefix as JSON property names (compact JSON-LD form). In SD-JWT VC, the embedded VCDM payload is carried as top-level JWT claims per [RFC 9901] Appendix A.4 — paths below are therefore identical unless a separate JWT-native claim is listed.

| **Section 2 attribute** | **VCDM JSON-LD** | **SD-JWT VC** |
|---------------------------|------------------|---------------|
| **Mandatory organization attributes** | | |
| `gs1:partyGLN` | `credentialSubject.organization.gs1:partyGLN` | `credentialSubject.organization.gs1:partyGLN` |
| `gs1:organizationName` | `credentialSubject.organization.gs1:organizationName` | `credentialSubject.organization.gs1:organizationName` |
| `gs1:organizationLegalName` | `credentialSubject.organization.gs1:organizationLegalName` | `credentialSubject.organization.gs1:organizationLegalName` |
| `credentialSubject.id` (GLN Digital Link URI) | `credentialSubject.id` (path **MUST** end in `/417/{gs1:partyGLN}`) | `credentialSubject.id` (path **MUST** end in `/417/{gs1:partyGLN}`) |
| `gs1:address` (`gs1:PostalAddress`) | `credentialSubject.organization.gs1:address` | `credentialSubject.organization.gs1:address` (MAY be selectively disclosable via `_sd`; Section 3.2.1) |
| `credentialSubject.keyAuthorization` | `credentialSubject.keyAuthorization` | `credentialSubject.keyAuthorization` |
| **Derived from credential chain (Section 4)** | | |
| Company Prefix (`licenceKey`) | Not stored on `OrganizationDataCredential`; derived by resolving the chain per Section 4 → `KeyCredential` (if present) → `extendsCredential` → `licenseValue` on the referenced `GS1CompanyPrefixLicenseCredential` | Same as VCDM JSON-LD |
| **Mandatory credential metadata** | | |
| `@context` | `@context` | `@context` |
| `id` | `id` | `id` |
| `type` | `type` (includes `VerifiableCredential`, `DataCredential`, `OrganizationDataCredential`) | `type` |
| `issuing_entity` | `issuer.id` (DID) | `issuer.id`; also JWT `iss` (RFC 7519; **SHOULD** match `issuer.id`) |
| `issuance_date` | `validFrom` (ISO 8601 date-time) | `validFrom`; also JWT `iat` (Unix timestamp; **SHOULD** be consistent with `validFrom`) |
| `expiry_date` | `validUntil` (ISO 8601 date-time; **SHOULD** be set) | `validUntil`; also JWT `exp` (Unix timestamp; **SHOULD** be consistent with `validUntil`) |
| `credentialSchema` | `credentialSchema` (`JsonSchema`) | `credentialSchema` |
| `credentialStatus` (revocation) | `credentialStatus` (`BitstringStatusListEntry`; Section 6.1) | `status` (authoritative for revocation; Section 3.2.2). `credentialStatus` **MAY** be present for structural parity but **MUST NOT** be used for revocation checks |
| `renderMethod` | `renderMethod` (`TemplateRenderMethod`) | `renderMethod` (MAY be selectively disclosable via `_sd`; Section 3.2.1) |
| **WeBuild / SD-JWT additional mandatory metadata** | | |
| `attestation_legal_category` | — (SD-JWT VC only) | `attestation_legal_category` |
| `vct` | — (SD-JWT VC only) | `vct` (`eu.we-build.gln.1`) |
| **Optional metadata** | | |
| `trust_anchor_url` | `trust_anchor_url` (top-level WeBuild extension; **MAY**) | `trust_anchor_url` |
| `schema_version` | `schema_version` (top-level WeBuild extension; **MAY**) | `schema_version` |
| `description` | `description` (**MAY**; GS1 Data Credential) | `description` |

**Notes:**

- `gs1:partyGLN` is also represented implicitly in `credentialSubject.id` as the GS1 Digital Link URI with application identifier **417**. When validating the credential chain (Section 4), verifiers **MAY** additionally read the party GLN from `GS1CompanyPrefixLicenseCredential` `credentialSubject.organization.gs1:partyGLN` (Section 3.3.5).
- SD-JWT VC embeds the same VCDM claim structure as JSON-LD; selectively disclosable claims within `credentialSubject` are replaced by `_sd` digests at issuance time (Section 3.2.1).
- Issuers **SHOULD** keep JWT-native claims (`iss`, `iat`, `exp`) and their VCDM counterparts (`issuer`, `validFrom`, `validUntil`) consistent (Section 3.2.1).


## 4 GS1 Trust Chain

A complete credential chain for the GLN EAA, i.e. an `OrganizationDataCredential`, **must** consist of at least the following three credentials:

- The `OrganizationDataCredential`
- A matching `GS1CompanyPrefixLicenseCredential` (GCP credential)
- A matching `GS1PrefixLicenseCredential` (Prefix credential)

It **may** also contain:

- A matching GLN `KeyCredential`

The chain — i.e. all credentials in the chain — **must** be verified in order to verify the `OrganizationDataCredential`.

To verify the chain, the verifier **must** check that all cryptographic signatures are valid according to the usual VC verification; see [VC Data Model](https://www.w3.org/TR/vc-data-model-2.0/). Additionally, the following constraints **must** be validated:

- The `OrganizationDataCredential` **must** contain `credentialSubject["gs1:organization"]["gs1:partyGLN"]`, which **must** be the 13-digit (party) GLN of the organization. This string is called `{GLN}` in the following.
- The `OrganizationDataCredential` **should** have an attribute `credentialSubject.keyAuthorization` which references the GLN `KeyCredential` when one is present in the chain. This reference **must** be a resolvable URL.
- When a GLN `KeyCredential` is present in the chain, the `OrganizationDataCredential` **must** be issued by the same entity that issued that `KeyCredential` (same issuer `did`).
- When a GLN `KeyCredential` is present, it **must** reference the matching `GS1CompanyPrefixLicenseCredential` via `credentialSubject.extendsCredential`. This reference **must** be a resolvable URL leading to the GCP credential.
- When the `OrganizationDataCredential` does not reference a GLN `KeyCredential`, it **must** reference a `GS1CompanyPrefixLicenseCredential` directly via `credentialSubject.keyAuthorization` (or an equivalent resolvable chain link), in the same way a `KeyCredential` references the GCP credential via `extendsCredential`.
- When a GLN `KeyCredential` is present, it **must** contain `credentialSubject.id`, which **must** be a URL with path suffix `/417/{GLN}` where `{GLN}` is the same 13-digit GLN as in the `OrganizationDataCredential`.
- The `GS1CompanyPrefixLicenseCredential` **must** contain `credentialSubject["gs1:organization"]["gs1:partyGLN"]`, which **must** match `{GLN}` as specified above.
- The `GS1CompanyPrefixLicenseCredential` **must** reference its parent `GS1PrefixLicenseCredential` via `credentialSubject.extendsCredential`. This reference **must** be a resolvable URL.
- The `GS1PrefixLicenseCredential` **must** be issued by GS1 Global Office (GO) and **must** terminate the license chain (Section 5.2).

GS1-specific `extendsCredential` resolution rules (primary key matching, party GLN vs. additional GLNs) are specified in Section 3.3.5. Trust anchors, issuer roles, and the operational verification workflow are specified in Section 5.



### 4.1 Issuance process

GLN Number attestations **MUST** only be issued when the underlying GS1 Company Prefix (GCP) license is valid and active. The attestation establishes that a specific GLN is assigned to a legal entity within the scope of that prefix; it does not replace the GS1 license credentials that form the root of trust.

#### 4.1.1 Trust chain prerequisites

Before issuing a GLN attestation, the Issuer **MUST** confirm the GS1 credential chain defined in [Section 4](#4-GS1-Trust-Chain) is intact for the target GLN and company prefix. In addition, the Issuer **MUST** verify:

1. **Revocation status** — No credential in the chain is revoked on the issuer's Bitstring Status List (Section 6).
2. **GLN integrity** — The GLN passes check-digit validation and its numeric prefix is consistent with the licensed company prefix (Section 2.8).
3. **Registry consistency** — Organization name and address match GS1 registry records

#### 4.1.2 Issuer roles

Issuer roles and responsibilities within the GS1 trust hierarchy are defined in Section 5.2. E.g. at GS1 Global Office, the issuance of the highes trust level credentials follows a multi-controller process: an Authorized Staff Member (ASM) prepares the credential and a GS1 Office Holder (OH) co-signs before publication. 

#### 4.1.3 Issuance steps

The Issuer **MUST** perform the following steps:


> :warning: TBD: The Issuer of an `OrganizationDataCredential` would normally be the same as the holder, namely the holder of the GCP Credential. How is this forseen to integrate with the WeBuild Trust Eco system?



1. **Identify the subject** — Resolve the legal entity DID (`credentialSubject.id`) and confirm it controls the DID used in the parent Company Prefix License.
2. **Select backing license** — Obtain the URI of the valid `GS1CompanyPrefixLicenseCredential`. The GLN `KeyCredential` `extendsCredential` **MUST** satisfy the rules in Section 3.3.5.
3. **Validate prefix and GLN** — Apply integrity rules from Section 2.8 against registry data.
4. **Construct the credential** — Populate mandatory attributes (Section 2.2) and metadata (Section 2.4) using the chosen encoding (Section 3.2 or 3.3).
5. **Attach status entry** — Allocate a `statusListIndex` on the issuer's revocation list when validity exceeds 24 hours.
6. **Sign and publish** — Sign with the issuer's assertion key; publish to the issuer registry when required for resolution (Company Prefix and Prefix licenses **MUST** be publicly resolvable per GS1 policy).
7. **Deliver to holder** — Issue via OpenID4VCI (Business Wallet), export for manual import or publish it to a registry of choice, e.g. making the credential available under the credentialId like it is mandatory for GS1 license credentials.

See reference implementation by EECC and GS1 US https://github.com/european-epc-competence-center/vc-verifier-rules/ for verification of the GS1 credential chain (Section 4).

#### 4.1.4 Attestation legal category

When the GLN attestation is issued by GS1 or an authorized GS1 Member Organization acting as an authentic source, `attestation_legal_category` **MUST** be `EAA`. Qualified variants (`QEAA`) are out of scope for this Rulebook unless the issuer is a QTSP with a registered attestation scheme under eIDAS Implementing Regulation (EU) 2025/1569.

### 4.2 Relying Party Obligations

When receiving and processing a GLN attestation, the Relying Party **MUST** validate the GS1 credential chain ([Section 4](#4-GS1-Trust-Chain)) and apply the GS1 trust-model verification workflow (Section 5.3), in addition to the base attestation verification process below.

#### 4.2.1 – 4.2.8 Base Verification Process
The Relying Party **MUST** perform the base attestation verification process as defined in the Base Verification specification:
https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-base/verifier-base-verification.md#42-relying-party-obligations

## 5 GS1 trust model

This section defines the GS1 Digital License trust hierarchy, root trust anchors, and the operational verification workflow for GLN credentials. [Section 4](#4-GS1-Trust-Chain) defines the **credential chain composition and linkage constraints** normatively; this section explains **why** those constraints establish trust and **how** Relying Parties apply them in practice. Section 4.1 describes the **issuance process**.




### 5.1 Trust hierarchy and credential chain

GS1 identity and licensing trust is rooted at **GS1 Global Office (GO)**. GO issues `GS1PrefixLicenseCredential` credentials to **Member Organizations (MOs)**. Each MO issues `GS1CompanyPrefixLicenseCredential` credentials to **Member Companies (MCs)** within its jurisdiction; each company prefix license **mandatorily** includes the company's main **party GLN** in `credentialSubject.organization.gs1:partyGLN` and no other GLNs. A licensed MC (or MO, when policy allows) may then issue GLN **`KeyCredential`** and companion **`OrganizationDataCredential`** pairs for each GLN commissioned under the prefix (and **MAY** also issue a `KeyCredential` for the party GLN itself).

The normative rules for which credentials **must** be present, how they link together, and what verifiers **must** check are defined in [Section 4](#4-GS1-Trust-Chain). At minimum, every valid chain contains an `OrganizationDataCredential`, a matching `GS1CompanyPrefixLicenseCredential`, and a matching `GS1PrefixLicenseCredential`; a GLN `KeyCredential` **may** additionally be present.

```
GS1 Global Office (root trust anchor)
  └─ GS1PrefixLicenseCredential  →  Member Organization DID
       └─ GS1CompanyPrefixLicenseCredential  →  Member Company DID
            │  (mandatory party GLN in organization.gs1:partyGLN)
            ├─ OrganizationDataCredential (party GLN; keyAuthorization → GCP when no KeyCredential)
            ├─ KeyCredential (party GLN; optional)
            │    └─ OrganizationDataCredential (keyAuthorization → KeyCredential)
            └─ KeyCredential (each additional GLN)
                 └─ OrganizationDataCredential (keyAuthorization → KeyCredential)
```

License credentials and GLN `KeyCredential`s link to their parent via **`extendsCredential`** (Mandatory per GS1 Digital Licenses). `OrganizationDataCredential`s link into the chain via **`keyAuthorization`**, referencing either the GLN `KeyCredential` or, when absent, the `GS1CompanyPrefixLicenseCredential` directly (Section 4). Data credentials **must** carry `keyAuthorization` to derive trust in the declared organization data from the GS1 key or prefix license.

The party GLN **MAY** be verified directly from the company prefix license without a `KeyCredential`; all other GLNs under the prefix require a valid GLN `KeyCredential` (Section 3.3.5).

**Company Prefix (`licenceKey`):** The attestation attribute `licenceKey` is not stored directly on the GLN credentials; verifiers derive it by resolving the chain (Section 4) to the `GS1CompanyPrefixLicenseCredential` and reading `licenseValue`.

### 5.2 Root trust anchors and issuer DIDs

| Anchor | Identifier / location | Purpose |
|--------|----------------------|---------|
| **GS1 Global Office DID** | `did:web:vc.gs1.org` (`did:web:vc-st.gs1.org` for staging environment) | Root issuer for `GS1PrefixLicenseCredential`; DID document publishes assertion keys |
| **Member Organization DID** | MO-specific `did:web:` (e.g. national GS1 body) | Issues company prefix licenses and **MAY** issue GLN credentials |
| **Member Company DID** | MC `did:web:` registered with MO | Subject of company prefix license; **MAY** issue GLN credentials when authorized |
| **Published credentials** | Resolvable credential URLs (e.g. `https://vc.gs1.org/...`, MO registry endpoints) | Chain resolution and signature verification |
| **GS1 contexts & schemas** | `https://ref.gs1.org/gs1/vc/*`, `https://id.gs1.org/vc/schema/v1/*` | Type definitions and JSON Schema validation |
| **GS1 Web Vocabulary** | `https://ref.gs1.org/voc/` | Organization and address semantics (Section 3.3.3 extension) |

Verifiers **MUST** treat GO as the ultimate trust root: every valid GLN credential chain **MUST** terminate at a `GS1PrefixLicenseCredential` whose `issuer.id` resolves to a GO-controlled DID `did:web:vc.gs1.org` with a valid signature of an assertion allowed key.

**Roles:**

| Role | Trust responsibility |
|------|---------------------|
| **GS1 Global Office** | Root of trust; issues prefix licenses to MOs; maintains GO DID document and revocation infrastructure |
| **Member Organization (MO)** | Regional licensing authority; issues company prefix licenses; **MAY** issue GLN credential pairs |
| **Member Company (MC)** | Licensee; **MAY** issue GLN credential pairs for GLNs under its prefix when MO policy permits |
| **Business Wallet (holder)** | Stores credentials; presents to Relying Parties via OpenID4VP |
| **Relying Party (verifier)** | Validates the credential chain (Section 4), status, and attribute integrity (Sections 3.3.5, 5.3, 6) |

### 5.3 Verification obligations

When a Relying Party receives a GLN attestation, it **MUST** validate the complete credential chain according to [Section 4](#4-GS1-Trust-Chain) before trusting the `OrganizationDataCredential`. The following operational steps apply in addition to the Section 4 constraints:

When the attestation is encoded as W3C VCDM (Section 3.3), the Relying Party **MUST** perform the following trust checks in order:

1. **Chain validation (Section 4)** — Resolve and validate all credentials in the chain: verify signatures, linkage constraints (`keyAuthorization`, `extendsCredential`), and `{GLN}` consistency across credentials.
2. **Temporal validity** — `validFrom` **MUST NOT** be in the future; `validUntil` (if present) **MUST NOT** be expired.
3. **GLN assignment (Section 3.3.5)** — If the attested GLN is the party GLN, verify it against `GS1CompanyPrefixLicenseCredential` `organization.gs1:partyGLN` **or** a valid GLN `KeyCredential` for the same GLN. For any other GLN, apply GLN `KeyCredential` rules (`extendsCredential`, issuer/subject matching, primary-key prefix rules) per [Validating GS1 ID Key Credentials](https://gs1.github.io/GS1DigitalLicenses/validating_keys.html).
4. **License chain resolution** — Recursively resolve and validate each `extendsCredential` reference back to a GO-issued `GS1PrefixLicenseCredential` per [Validating GS1 License Credentials](https://gs1.github.io/GS1DigitalLicenses/license_validation.html).
5. **Revocation (Section 6)** — Check revocation status on every credential in the chain. A revoked link invalidates the entire chain.
6. **Attribute integrity** — Validate Section 2 mandatory attributes, including GLN check digit and prefix consistency (Section 2.8).

When the attestation is encoded as SD-JWT VC (Section 3.2), the Relying Party **MUST** apply the base verification process (Section 4.2), validate the embedded W3C VCDM payload structure per [RFC 9901] Appendix A.4, validate revocation via the SD-JWT `status` claim only (Section 3.2.2), and **MAY** use `trust_anchor_url` (Section 5.4) to locate supplementary trust metadata. The underlying GS1 credential chain validation per Section 4 remains applicable when cross-checking against published GS1 credentials referenced via `credentialSubject.keyAuthorization` and `extendsCredential`.

### 5.4 Trust anchor metadata (`trust_anchor_url`)

GLN attestations **MAY** include the optional `trust_anchor_url` metadata attribute (Section 2.6). When present, it **SHOULD** point to a document that helps verifiers establish issuer authorization within the WeBuild / EUBW trust framework — for example, a GS1 MO entry in a consortium trust list, GO DID document, or MO-published trust policy.

`trust_anchor_url` supplements but does **not replace** GS1 chain validation: verifiers **MUST** still resolve and validate the credential chain per [Section 4](#4-GS1-Trust-Chain) regardless of whether `trust_anchor_url` is present.

### 5.5 Relationship to WeBuild and EUBW

Within the WeBuild KYS workflow, the GLN attestation acts as an **Electronic Attestation of Attributes (EAA)** when issued by GS1 or an authorized MO (Section 4.1.4). The GS1 trust model provides **authentic-source** assurance for organization identity and GLN assignment; it does not, by itself, satisfy broader KYS obligations (e.g. beneficial ownership, financial standing) covered by other rulebooks in the WeBuild catalog.

Relying Parties integrating GLN attestations into EUBW-compliant KYS flows **SHOULD** treat a valid GS1 credential chain (Section 4) as evidence that the presented GLN and organization attributes originate from an authorized GS1 issuer, subject to the verification obligations in Sections 4, 5.3, and 6.

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
| `OrganizationDataCredential` | **MAY** be present; if present, **MUST** be `BitstringStatusListEntry` |
| License credentials (chain) | **MUST** be present on all GS1 License Credentials |

### 6.2 Relying Party verification obligations

When verifying a GLN credential presentation, the Relying Party **MUST** validate revocation on every credential in the chain defined in [Section 4](#4-GS1-Trust-Chain):

1. Validate `credentialStatus` on the GLN `KeyCredential` (when present), the `GS1CompanyPrefixLicenseCredential`, the `GS1PrefixLicenseCredential`, and each credential in the `extendsCredential` license chain.
2. Apply the validation rules in Section 3.2 of [[vc-bitstring-status-list]] — a `credentialStatus` entry is valid only if those rules return `valid: true`.
3. Treat a revoked credential in any link of the chain as invalidating the entire chain.
4. Follow the GS1 status validation rules in [Validating Credential Status](https://gs1.github.io/GS1DigitalLicenses/validating_status.html).

Temporary unavailability of a status list endpoint does **not** imply revocation. Verifiers **MAY** use a cached copy of the status list and **SHOULD** inform the user of the cache timestamp. Issuers **SHOULD** set `validUntil` on credentials so that credentials do not remain valid indefinitely if status lists become permanently unavailable.

### 6.3 Issuer obligations

Issuers **MUST**:

- Maintain a published `BitstringStatusListCredential` with high availability (this is the GS1 component most requiring uptime).
- Allocate a unique `statusListIndex` for each issued credential at issuance time.
- Revoke credentials by setting the corresponding bit in the status list when a GLN or license is withdrawn.
- Publish status lists at a stable, resolvable URI (JWT or JSON-LD).
- Publish KeyCredentials or deliver them within a presentation to guarantee integrity of the GS1 credential chain (Section 4)

GS1 Global Office publishes revocation lists via its VC wallet API; Member Organizations **MUST** publish equivalent lists for credentials they issue. Verifiers **MAY** use cached status lists when endpoints are temporarily unavailable and **SHOULD** record the cache timestamp (Section 6.2).

### 6.4 Relationship to SD-JWT VC status (Section 3.2)

When the GLN attestation is encoded as SD-JWT VC (Section 3.2), revocation **MUST** be
validated using the SD-JWT VC `status` claim (Section 3.2.2). The embedded VCDM payload **MAY**
include a `credentialStatus` property (`BitstringStatusListEntry`) for structural parity with
GS1 license credentials, but verifiers **MUST NOT** use `credentialStatus` for revocation
checks in the SD-JWT path. W3C VCDM and JSON-LD credentials (Section 3.3) continue to use
`credentialStatus` as defined in Section 6.1–6.2. But status properties **SHOULD** point to the same status list credential bit.

## 7 Compliance

This GLN Attestation Rulebook is designed for use within the European Business Wallet (EUBW) framework and WeBuild consortium attestation catalog. Key compliance considerations:

- **eIDAS 2 / EAA classification** — When issued by GS1 or an authorized MO, the attestation is classified as an Electronic Attestation of Attributes (`attestation_legal_category: EAA`) per Regulation (EU) 2024/1183 (Section 4.1.4).
- **Data minimization** — Selective disclosure (Section 3.2) and optional attributes (Section 2.3) support GDPR-aligned data minimization; issuers **SHOULD NOT** include attributes beyond those required for the KYS use case.
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
