* Template version: 1.1, 20-08-2025


# Attestation Rulebook for attestations of type Legal Entity Identifier (LEI)

* Authors:
  * Martin Westerkamp, [Spherity](https://www.spherity.com)
  * Monika Nowicki, [Bundesanzeiger Verlag](https://www.bundesanzeiger-verlag.de)

| Version          | Date               | Description                                      |
|------------------|--------------------|--------------------------------------------------|
| 0.1                | 08.06.2026         | Initial Draft based on the WE BUILD LEI attestation description, using the [GLEIF LEI-CDF 3.1 data model](https://www.gleif.org/en/lei-data/access-and-use-lei-data/level-1-data-lei-cdf-3-1-format) |

**Feedback:**
Main feedback channel: [GitHub issues](https://github.com/webuild-consortium/eudi-wallet-rulebooks-and-schemas/issues)
Alternative: Contact the relevant WE BUILD business use case contact points.

## 1 Introduction

### 1.1 Attestation introduction

This document is the Legal Entity Identifier Data Rulebook (referred to as LEI). It contains the specific requirements, issuance process, formatting and content of the LEI attestation.
This document is created and used by the WEBUILD consortium to provide a common understanding, data schema, format and usage guidelines for the WEBUILD eco system.

The Legal Entity Identifier (LEI) is a unique, 20-character alphanumeric code used to strictly identify distinct legal entities that participate in global financial transactions. Established by the G20 in the wake of the 2008 financial crisis, its primary purpose is to improve transparency and risk management across the international financial system. Yet, it can also be utilized in other contexts to enable global authentication of legal entities.

Each LEI links to a public database containing company information. By providing a standardized, machine-readable identity, the system reduces the complexity of verifying counterparts in cross-border markets. Essentially, it acts as a global "social security number" for businesses, ensuring that every participant in a trade is clearly and universally recognized.

To reduce the need for querying an external database, the base information about the company is included in the attestation. This allows a broad range of applications, from KYC in finance to proving the identity of DPP issuers in an international setting.

This document is based on the data model provided by GLEIF: <https://www.gleif.org/en/lei-data/access-and-use-lei-data/level-1-data-lei-cdf-3-1-format>.

This attestation represents a Legal Entity Identifier (LEI) record. It embodies:
- The LEI code uniquely identifying the legal entity (ISO 17442)
- Base information about the legal entity (name, addresses, jurisdiction, legal form, status, creation date)
- Registration metadata about the LEI record (managing LOU, registration dates, registration status)

### 1.2 Introduction attribute specification

The attestation attributes are defined in the tables of Chapter 2 of this document. These tables contain the following information:
- The first column specifies the identifiers of the attestation attributes. The attribute identifiers in this column SHALL be used in requests and responses. There SHALL be at most one attribute with the same attribute identifier in each attestation attribute.
- The second column describes the meaning of the attribute.
- The third column specifies whether the presence of the attribute in an attestation is mandatory (M), or optional (O).
    - NOTE: If the table indicates an attribute as mandatory, this solely means that the Issuer SHALL ensure that this element is present in the attestation. It does not imply that a Relying Party is required to request such an attribute when interacting with the Wallet Instance. Neither does it imply that the User cannot refuse to release a mandatory attribute if requested.
- The fourth column indicates how the data elements SHALL be encoded, using the CDDL representation types defined in [RFC 8610].
- The fifth column provides the semantic reference for the attribute in the [European Business Wallet Vocabulary](https://webuild-consortium.github.io/wp4-semantics-group/ebwv//vocabulary.html).

### 1.3 Document structure

- Chapter 2, Attestation attributes and metadata in an encoding-independent manner.
- Chapter 3, Attestation attributes for the specific encodings SD-JWT VC and W3C VCDM v2.0.
- Chapter 4, Attestation usage.
- Chapter 5, Trust anchors
- Chapter 6, Revocation mechanisms
- Chapter 7, Compliance information


### 1.4 Keywords


This document uses the capitalised keywords 'SHALL', 'SHOULD' and 'MAY' as
specified in [RFC 2119], i.e. to indicate requirements, recommendations and
options specified in this document.

In addition, 'must' (non-capitalised) is used to indicate an external
constraint, i.e. a requirement that is not mandated by this document, but, for
instance, by an external document. The word 'can' indicates a capability,
whereas other words, such as 'will', and 'is' or 'are' are intended as
statements of fact.

### 1.5 Terminology

This document uses terminology specified in [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/eli/reg/2024/1183/oj/eng) and [Annex 1 of the ARF](https://eudi.dev/1.4.0/annexes/annex-1/annex-1-definitions/).

In addition to the attributes definition necessary to understand the data schema, it's important to understand:

| Term                 | Definition in WE BUILD Context                                                                                                                                                                                                                                                                                                                                                                                  |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Legal entity         | an organization or structure that is recognized by law as having legal rights and responsibilities distinct from those of its members or owners. A legal entity can enter into contracts, own property, incur debts, and be held liable for legal actions in its own name.                                                                                                                                       |
| LEI                  | Legal Entity Identifier: a unique, 20-character alphanumeric code conforming to ISO 17442 that uniquely identifies a legal entity participating in financial and other transactions globally.                                                                                                                                                                                                                   |
| LOU                  | Local Operating Unit: an organization accredited by GLEIF to issue and administer LEIs (also referred to as an LEI Issuer).                                                                                                                                                                                                                                                                                     |
| GLEIF                | Global Legal Entity Identifier Foundation: the not-for-profit organization that oversees the Global LEI System and the integrity of LEI data.                                                                                                                                                                                                                                                                   |


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
SHALL be included (see ARB_11 in [Topic 12]). See also section 2.1.
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
SHALL be included (see ARB_11 in [Topic 12]). See also section 2.1.
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
See also section 2.1.
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

### 2.1 Overview attributes attestation

The LEI attestation is structured as a top-level `LegalEntityIdentifier` object containing the `lei` code and two nested objects: `legal_entity` (base entity information) and `registration` (LEI record registration metadata). The model is as follows:

```
LegalEntityIdentifier
├── lei (tstr)
├── legal_entity (LegalEntity)
│   ├── legal_name (tstr)
│   ├── legal_address (Address)
│   │   └── [Address attributes]
│   ├── headquarters_address (Address)
│   │   └── [Address attributes]
│   ├── legal_jurisdiction (tstr)
│   ├── entity_status (tstr)
│   ├── entity_creation_date (tstr)
│   └── legal_form (tstr)
└── registration (Registration)
    ├── managing_lou (tstr)
    ├── initial_registration_date (tstr)
    ├── last_update_date (tstr)
    ├── registration_status (tstr)
    └── next_renewal_date (tstr)
```

The following table lists the top-level attributes of the LEI attestation. Attribute identifiers SHALL be used in requests and responses.

| **Data Identifier** | **Definition** | **Optionality** | **Encoding format** | **Semantic reference** |
|---|---|---|---|---|
| lei | A Legal Entity Identifier (LEI) code, in the format specified by ISO 17442. | M | tstr | [lei](https://webuild-consortium.github.io/wp4-semantics-group/ebwv/vocabulary.html#lei) |
| legal_entity | Base information about the legal entity. See [section 2.4](#24-legalentity-attributes). | M | LegalEntity (object) | — |
| registration | Registration metadata about the LEI record. See [section 2.5](#25-registration-attributes). | M | Registration (object) | — |

### 2.2 Code lists

The following code lists apply to specific attributes:

**entity_status**

Values:
- ACTIVE
- INACTIVE
- NULL

**registration_status**

Values:
- PENDING_VALIDATION
- ISSUED
- DUPLICATE
- LAPSED
- RETIRED
- ANNULLED
- CANCELLED
- TRANSFERRED
- PENDING_TRANSFER
- PENDING_ARCHIVAL

**legal_jurisdiction**

A 2-character country code conforming to ISO 3166-1 alpha-2, or a region code conforming to ISO 3166-2.

**legal_form**

A code taken from the ISO 20275 Entity Legal Form (ELF) code list maintained by GLEIF.

### 2.3 Integrity rules

- lei MUST conform to the format specified by ISO 17442 (a 20-character alphanumeric code).
- legal_jurisdiction, where present, MUST be a valid ISO 3166-1 alpha-2 country code or ISO 3166-2 region code.
- legal_form, where present, MUST be a valid ISO 20275 (ELF) code.
- entity_status MUST be one of the values defined in the entity_status code list.
- registration_status MUST be one of the values defined in the registration_status code list.
- All date and date-time attributes MUST follow ISO 8601.
- managing_lou MUST be a valid LEI conforming to ISO 17442, identifying the LEI Issuer responsible for administering the record.

### 2.4 LegalEntity attributes

The `legal_entity` object carries the base information about the legal entity identified by the LEI.

| **Data Identifier** | **Definition** | **Optionality** | **Encoding format** | **Semantic reference** |
|---|---|---|---|---|
| legal_name | The Legal Name of the Entity. If an Entity is in a jurisdiction with more than one Legal Name (e.g., in different languages), this is the Primary Legal Name. | M | tstr | [legalName](https://webuild-consortium.github.io/wp4-semantics-group/ebwv/vocabulary.html#legalName) |
| legal_address | The address of the Entity as recorded in the registration of the Entity in its legal jurisdiction. See [section 2.6](#26-address). | M | Address (object) | [registeredAddress](https://webuild-consortium.github.io/wp4-semantics-group/ebwv/vocabulary.html#registeredAddress) |
| headquarters_address | The address of the headquarters of the Entity. May be equivalent to legal_address. See [section 2.6](#26-address). | O | Address (object) | [correspondenceAddress](https://webuild-consortium.github.io/wp4-semantics-group/ebwv/vocabulary.html#correspondenceAddress) |
| legal_jurisdiction | The jurisdiction of legal formation and registration of the Entity (and on which the legal_form data element is also dependent). Either a 2-character country code conforming to ISO 3166-1 alpha-2 or a region code conforming to ISO 3166-2. | O | tstr | [jurisdiction](https://webuild-consortium.github.io/wp4-semantics-group/ebwv/vocabulary.html#jurisdiction) |
| legal_form | The legal form of the Entity, taken from the ISO Entity Legal Form (ELF) code list maintained by GLEIF. | O | tstr | [legalForm](https://webuild-consortium.github.io/wp4-semantics-group/ebwv/vocabulary.html#legalForm) |
| entity_status | The status of the Legal Entity. Either "ACTIVE", "INACTIVE" or "NULL". | M | tstr | [legalStatus](https://webuild-consortium.github.io/wp4-semantics-group/ebwv/vocabulary.html#legalStatus) |
| entity_creation_date | The date on which the legal entity was first established as defined in ISO 17442. | O | tstr | [dateOfRegistration](https://webuild-consortium.github.io/wp4-semantics-group/ebwv/vocabulary.html#dateOfRegistration) |

### 2.5 Registration attributes

The `registration` object carries metadata about the LEI record's registration with the managing LEI Issuer (LOU).

| **Data Identifier** | **Definition** | **Optionality** | **Encoding format** | **Semantic reference** |
|---|---|---|---|---|
| managing_lou | The LEI of the LEI Issuer that is responsible for administering this LEI Record. | M | tstr | [managingLeiIssuer](https://webuild-consortium.github.io/wp4-semantics-group/ebwv/vocabulary.html#managingLeiIssuer) |
| initial_registration_date | The date at which the information was first collected by the managing_lou. | M | tstr | [leiRegistrationDate](https://webuild-consortium.github.io/wp4-semantics-group/ebwv/vocabulary.html#leiRegistrationDate) |
| last_update_date | The date at which the information was most recently updated by the managing_lou. A date and time, including the timezone, based on ISO 8601. | M | tstr | [leiLastUpdate](https://webuild-consortium.github.io/wp4-semantics-group/ebwv/vocabulary.html#leiLastUpdate) |
| registration_status | The status of the Legal Entity's LEI Record registration with the managing_lou. One of: "PENDING_VALIDATION", "ISSUED", "DUPLICATE", "LAPSED", "RETIRED", "ANNULLED", "CANCELLED", "TRANSFERRED", "PENDING_TRANSFER", "PENDING_ARCHIVAL". | M | tstr | [leiRegistrationStatus](https://webuild-consortium.github.io/wp4-semantics-group/ebwv/vocabulary.html#leiRegistrationStatus) |
| next_renewal_date | A date and time, including the timezone, based on ISO 8601, indicating the next renewal date of the LEI record. | M | tstr | [leiNextRenewal](https://webuild-consortium.github.io/wp4-semantics-group/ebwv/vocabulary.html#leiNextRenewal) |

### 2.6 Address

The `Address` structure applies to both `legal_address` and `headquarters_address`. The attributes follow the `Address` class defined in the [European Business Wallet Vocabulary](https://webuild-consortium.github.io/wp4-semantics-group/ebwv//vocabulary.html#Address), which in turn re-uses the INSPIRE/ISA Core Location address components.

| **Data Identifier** | **Definition** | **Optionality** | **Encoding format** | **Semantic reference** |
|---|---|---|---|---|
| full_address | The complete address written out as a formatted string. | M | string | [fullAddress](https://webuild-consortium.github.io/wp4-semantics-group/ebwv//vocabulary.html#fullAddress) |
| thorough_fare | An address component that represents the name of a passage or way through from one location to another (e.g., a street). | O | string | [thoroughfare](https://webuild-consortium.github.io/wp4-semantics-group/ebwv//vocabulary.html#thoroughfare) |
| locator_designator | A number or a sequence of characters that uniquely identifies the locator within the relevant scope(s) (e.g., a house number). | O | string | [locatorDesignator](https://webuild-consortium.github.io/wp4-semantics-group/ebwv//vocabulary.html#locatorDesignator) |
| locator_name | Proper noun(s) applied to the real-world entity identified by the locator (e.g., a building name). | O | string | [locatorName](https://webuild-consortium.github.io/wp4-semantics-group/ebwv//vocabulary.html#locatorName) |
| address_area | The name of a geographic area that groups a number of addressable objects for addressing purposes, without being an administrative unit. | O | string | [addressArea](https://webuild-consortium.github.io/wp4-semantics-group/ebwv//vocabulary.html#addressArea) |
| post_code | The code created and maintained for postal purposes to identify a subdivision of addresses and postal delivery points. | O | string | [postCode](https://webuild-consortium.github.io/wp4-semantics-group/ebwv//vocabulary.html#postCode) |
| post_name | A name created and maintained for postal purposes to identify a subdivision of addresses and postal delivery points (e.g., a city or town). | O | string | [postName](https://webuild-consortium.github.io/wp4-semantics-group/ebwv//vocabulary.html#postName) |
| po_box | A location designator for a postal delivery point at a post office, usually a number. | O | string | [poBox](https://webuild-consortium.github.io/wp4-semantics-group/ebwv//vocabulary.html#poBox) |
| admin_unit_level_1 | The name of the uppermost level of the administrative hierarchy of a country (the country itself). | O | string | [adminUnitL1](https://webuild-consortium.github.io/wp4-semantics-group/ebwv//vocabulary.html#adminUnitL1) |
| admin_unit_level_2 | The name of a secondary level/region of the administrative hierarchy of a country (e.g., a region, province, or state). | O | string | [adminUnitL2](https://webuild-consortium.github.io/wp4-semantics-group/ebwv//vocabulary.html#adminUnitL2) |

### 2.7 Mandatory metadata

| **Data Identifier**  | **Definition**                                                                                                                                                                                           |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| expiry_date          | Date (and if possible time) when the attestation will expire. Does not need to be an attribute and can be covered by credential format metadata, such as for example the "exp" field on the sd-jwt format. |
| issuing_authority    | Name of the administrative authority (LEI Issuer / LOU) that issued the LEI attestation, or the ISO 3166 alpha-2 country code of the respective Member State if there is no separate authority entitled to issue the LEI attestation. |
| issuing_country      | Alpha-2 country code, as specified in ISO 3166-1, of the country or territory of the provider of the attestation data.                                                                                   |
| attestation_legal_category | Indicates the legal category of this attestation ("EAA" or "pubEAA"/"QEAA")                                                                                       |

### 2.8 Conditional metadata

| **Data Identifier**  | **Definition**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| location_status      | The location of validity status information on the attestation data where the providers of the attestation revoke it. This attribute is required when the validity time period of the attestation exceeds 24 hours.                                                                                                                                                                                                                                                                                                                  |
| trust_anchor         | This attribute indicates at least the URL at which a machine-readable version of the trust anchor to be used for verifying the LEI attestation can be found or looked up. *Note: This attribute corresponds to the location meant in Annex V point h) or Annex VII point h) of the [European Digital Identity Regulation], which is mandatory for QEAAs. This Rulebook adds this as an optional attribute for LEI attestations as well, so LEI Providers are able to ensure that LEI attestations can be validated by Relying Parties in the same manner as QEAAs.* |



# 3 Attestation encoding

## 3.1 ISO/IEC 18013-5-compliant encoding

ISO/IEC 18013-5 (also called mdoc) is out of scope for this rulebook, as offline proximity presentation is not a current requirement for the LEI attestation.

### 3.2 SD-JWT VC-based encoding

The LEI attestation is available in the SD-JWT VC format to be aligned with the WeBuild formats.
Yet, selective disclosure is not required for any claim because the included data is public.

The . notation is used to indicate the nesting of attributes.


**Verifiable Credential Type (`vct`):** `eu.we-build.lei.1`


| **Data Identifier**                                | **Attribute identifier**                          | **Encoding format** | **Reference/Notes**                                                        |
|----------------------------------------------------|---------------------------------------------------|---------------------|----------------------------------------------------------------------------|
| issuing_authority                                  | iss                                               | string              | RFC 7519 / Section 2.7                                                     |
| expiry_date                                        | exp                                               | number              | RFC 7519 / Section 2.7 (Unix timestamp)                                    |
| attestation_legal_category                                    | attestation_legal_category                                   | string              | Section 2.7                                                         |
| issuing_country                                    | issuing_country                                   | string              | ISO 3166-1 alpha-2                                                         |
| lei                                                | lei                                               | string              | ISO 17442 (20-character alphanumeric)                                      |
| legal_entity                                       | legal_entity                                      | object              | See section 2.4                                                            |
| legal_entity.legal_name                            | legal_entity.legal_name                           | string              | Primary Legal Name of the Entity                                          |
| legal_entity.legal_address                         | legal_entity.legal_address                        | object              | See section 2.6 for structure                                             |
| legal_entity.legal_address.full_address            | legal_entity.legal_address.full_address           | string              |                                                                            |
| legal_entity.legal_address.thorough_fare           | legal_entity.legal_address.thorough_fare          | string              |                                                                            |
| legal_entity.legal_address.locator_designator      | legal_entity.legal_address.locator_designator     | string              |                                                                            |
| legal_entity.legal_address.locator_name            | legal_entity.legal_address.locator_name           | string              |                                                                            |
| legal_entity.legal_address.address_area            | legal_entity.legal_address.address_area           | string              |                                                                            |
| legal_entity.legal_address.post_code               | legal_entity.legal_address.post_code              | string              |                                                                            |
| legal_entity.legal_address.post_name               | legal_entity.legal_address.post_name              | string              |                                                                            |
| legal_entity.legal_address.po_box                  | legal_entity.legal_address.po_box                 | string              |                                                                            |
| legal_entity.legal_address.admin_unit_level_1      | legal_entity.legal_address.admin_unit_level_1     | string              |                                                                            |
| legal_entity.legal_address.admin_unit_level_2      | legal_entity.legal_address.admin_unit_level_2     | string              |                                                                            |
| legal_entity.headquarters_address                  | legal_entity.headquarters_address                 | object              | See section 2.6 for structure                                             |
| legal_entity.legal_jurisdiction                    | legal_entity.legal_jurisdiction                   | string              | ISO 3166-1 alpha-2 or ISO 3166-2                                          |
| legal_entity.legal_form                            | legal_entity.legal_form                           | string              | ISO 20275 (ELF) code                                                      |
| legal_entity.entity_status                         | legal_entity.entity_status                        | string              | ACTIVE / INACTIVE / NULL                                                  |
| legal_entity.entity_creation_date                  | legal_entity.entity_creation_date                 | string              | ISO 8601                                                                  |
| registration                                       | registration                                      | object              | See section 2.5                                                            |
| registration.managing_lou                          | registration.managing_lou                         | string              | LEI of the managing LOU                                                   |
| registration.initial_registration_date            | registration.initial_registration_date           | string              | ISO 8601                                                                  |
| registration.last_update_date                      | registration.last_update_date                     | string              | ISO 8601 (date-time with timezone)                                        |
| registration.registration_status                  | registration.registration_status                 | string              | See registration_status code list                                         |
| registration.next_renewal_date                     | registration.next_renewal_date                    | string              | ISO 8601 (date-time with timezone)                                        |
| location_status                                    | status                                            | object              | See chapter [3.2.1](#321-attribute-status)                                |


#### 3.2.1 Attribute status
For SD-JWT VC-compliant LEI attestations, the attestation MUST include a status claim if the technical validity period is greater than 24 hours. This claim enables Relying Parties to determine if a credential has been revoked via a status list mechanism, as specified in [SD-JWT VC](https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/12/).

The status claim SHALL be a JSON object with the following members:

* 'type' (string): SHALL be "status-list".
* 'status_list_credential' (string, URI): The URI of the Status List Credential document that contains the status bitstring.
* 'status_list_index' (integer, >= 0): The zero-based index into the status list bitstring that corresponds to this credential.
* 'status_purpose' (string): SHALL be "revocation".

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

#### 3.2.2 Example Payload
Sample payloads to be provided under `../../data-schemas/sd-jwt-vc/sample-data/rb-lei-sd-jwt-sample.json`.

### 3.3 W3C Verifiable Credentials Data Model-based encoding

W3C Verifiable Credentials are defined using linked data (JSON-LD). Ontologies (vocabularies) are used to semantically define the different aspects of credentials including the credential subject. Validation of data structures is optional. If required, either JSON-schemes (data structure) or SHACL (data graph) can be used to validate data.

#### Metadata
The metadata of a W3C Verifiable Credential are defined in the [Verifiable Credentials Vocabulary v2.0](https://www.w3.org/2018/credentials/). The following extensions are defined in the [European Business Wallet Vocabulary v0.1](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary) in order to support Electronic Attestations of Attributes:
* [attestationLegalCategory](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#attestationLegalCategory) in order to specify the category of the EAA (QEAA, Pub-EAA or EAA).

The semantic terms used for the LEI attributes are defined in the [European Business Wallet Vocabulary] (WP4 semantics group): <https://webuild-consortium.github.io/wp4-semantics-group/ebwv/vocabulary.html>.

#### Holder Binding

LEI attestations are held by the organization identified by the LEI. Corresponding key binding is provided by using DIDs. Please note that every node of a JSON-LD tree is addressable by its own locally or globally unique identifier `@id`. Using [Decentralized Identifiers (DIDs) v1.0](https://www.w3.org/TR/did-1.0/) as identifiers allows to cryptographically bind any node to its underlying identity.

The Verifiable Credential Data Model (VCDM) doesn't dictate any specific DID method. Instead, any DID method that supports the underlying trust framework and is able to provide the required level of assurance can be used:
* PKI-Infrastructure (e.g. EU-TLOL based on X.509 certificates): [did:key](https://github.com/digitalbazaar/did-method-key) - the public key is directly encoded in the identifier
* DTL (e.g.: Ethereum): [did:ethr](https://github.com/uport-project/ethr-did)
* European Blockchain Infrastructure: [did:ebsi](https://hub.ebsi.eu/vc-framework/did/legal-entities)
* Domain Name System (DNS): [did:web](https://w3c-ccg.github.io/did-method-web/)
* Domain Name System verifiable history: [did:webvh](https://identity.foundation/didwebvh/v1.0/)

#### Proof mechanisms

The preferred proof mechanism for the LEI attestation is [ecdsa-sd-2023](https://www.w3.org/TR/vc-di-ecdsa/#ecdsa-sd-2023-functions) as specified in [Data Integrity ECDSA Cryptosuites v1.0](https://www.w3.org/TR/vc-di-ecdsa). ecdsa-sd-2023 supports selective disclosure out of the box. The holder chooses which claims to disclose and derives a proof from the original assertion proof.

For backward compatibility and for trust frameworks whose policies require a particular proof mechanism, [JOSE](https://www.w3.org/TR/vc-jose-cose/#with-jose) and [SD-JWT](https://www.w3.org/TR/vc-jose-cose/#with-sd-jwt) as specified in [Securing Verifiable Credentials using JOSE and COSE](https://www.w3.org/TR/vc-jose-cose/) should be supported, too.

The [Security Vocabulary](https://www.w3.org/2025/credentials/vcdi/vocab/v2/vocabulary.html) is used to embed the proofs into the credentials.

#### Credential status

The LEI attestation SHALL include a status claim `credentialStatus` if the technical validity period is greater than 24 hours. This claim enables Relying Parties to determine if a credential has been revoked via a status list mechanism, as specified in [Bitstring Status List v1.0](https://www.w3.org/TR/vc-bitstring-status-list/).

## 4 Attestation usage

The LEI attestation is intended to be used as a standardised, machine-verifiable proof of a legal entity's identity and base registration information, to be presented by a Wallet User to a Relying Party in cross-border and domestic contexts.

Typical scenarios include, but are not limited to:

- **Know Your Customer (KYC) and onboarding in finance**: providing a globally recognized, registry-backed identifier and base entity data during customer onboarding and counterparty verification.
- **Cross-border business onboarding (B2B)**: sharing official legal entity identification during supplier/customer onboarding, procurement qualification, or partner due diligence.
- **Authentication of issuers in international settings**: proving the identity of issuers (e.g. of Digital Product Passports) where a globally unique entity identifier is required.
- **Reducing external database queries**: including base entity information in the attestation so that Relying Parties do not need to query the GLEIF database for every verification.

The LEI attestation is **not** intended to be used as a standalone authentication mechanism to replace processes that legally require a natural person to act and be authenticated in their own right.

**Note:** The LEI attestation identifies a legal entity but does not, by itself, prove that the current presenter is authorised to act on behalf of that entity unless the Relying Party also performs an appropriate binding to the presenter (typically via PID and/or additional authorisation evidence outside the scope of this rulebook).

**Note:** The LEI attestation is intended for **online, remote presentation** using EUDI Wallet-compatible presentation protocols.


### 4.1 Issuance of the LEI attestation

* The Authentic Source of the data contained in the LEI attestation MUST be the Global LEI System (GLEIF) and the managing LEI Issuer (LOU). The LOU can or MUST authorize an issuer to issue LEI attestations on their behalf.
* The Issuance SHALL be based on up-to-date, authoritative data from the authoritative source (the Global LEI System).
* The LEI attestation SHALL be key bound to the wallet, IF the wallet belongs to the entity that the LEI attestation is issued for.
* If the LEI attestation is issued to a wallet that is not owned by the entity that the attestation is issued for, the attestation SHALL NOT be key bound to the wallet.
* The LEI attestation SHALL be issued in a format that is compatible with the EUDI Wallet ecosystem (e.g., **OpenID4VP** profiles adopted by the ecosystem).
* To receive an LEI attestation with key binding, the application shall ensure that the wallet is owned by the entity that the attestation is issued for through presentation and matching of key material of the European business wallet owner identification data (OID).

### 4.5 Relying Party obligations when processing an LEI attestation

Beyond protocol-level checks, an RP processing an LEI attestation presentation **SHALL** perform at least the following controls:

1. **Verify authenticity and integrity**
    - Verify the LEI attestation cryptographic protections (signature/seal chain validation as applicable for the legal category).
    - Verify that the issuer is authorised to issue LEI attestations according to the trust anchor mechanism defined in this rulebook (see Chapter 5).

2. **Verify time validity / freshness**
    - Verify the LEI attestation is within its validity period (e.g., using `exp` in SD-JWT VC).

3. **Check revocation / status (where applicable)**
    - Where the LEI attestation validity exceeds 24 hours and a status mechanism is provided, the RP **SHALL** check the attestation validity status using the mechanism defined in Chapter 6.

4. **Process according to purpose limitation**
    - RPs **SHOULD** request and process the LEI attestation only when needed for the specific transaction, and only for the purpose of the transaction, in line with applicable legal requirements.


LEI attestation presentation may involve **transactional data** exchanged as part of the presentation protocol. The following transactional data elements are relevant:

- **Relying Party request parameters**, including the requested credential type(s) and any policy constraints (e.g., requirement to include PID alongside the LEI attestation).
- **Challenge/nonce and session identifiers** used to prevent replay and bind the presentation to a specific session.
- **Presentation timestamp** (implicit or explicit), to support auditability and freshness validation.
- **Relying Party identification information** presented to the Wallet Unit (e.g., RP name, domain, certificate details), to support user transparency and consent decisions.

The specific protocol artefacts and parameter names depend on the adopted OpenID4VP profile(s). This rulebook does not prescribe additional LEI-specific transactional data beyond what is required by the underlying presentation protocol(s).


## 5 Trust anchors


#TODO


*Mechanisms for the provision of a trust anchor that SHALL
be used for the verification of an attestation SHALL be defined in this section.*

*It is noted that the ARF specifies the following for QEAAs and Pub-EAAs*

> To do this for [...] QEAAs the Relying Party Instance uses a trust anchor of
> the Provider obtained from a Trusted List. Note that the PID Provider or QEAA
> Provider may use an intermediate signing certificate to sign the PID or
attestation and use the trust anchor to sign the signing certificate, instead
> of signing the PID or attestation directly with the trust anchor.

> For PuB-EAAs, the Relying Party Instance verifies a PuB-EAA by first
> verifying the signature of the PuB-EAA Provider over the PuB-EAA, using the
> PuB-EAA Provider certificate issued by a QTSP. Subsequently, the Relying Party
> Instance verifies the signature over this certificate, using the corresponding
> trust anchor from the QTSP Trusted List. Note that both the PuB-EAA Provider
> and the QTSP may use an intermediate signing certificate. All other things
> being equal, the verification of a PuB-EAA will therefore involve one or more
> extra certificates, compared to the verification of a PID or QEAA.

*For non-qualified EAA in this section it SHOULD be defined (see ARB_26 in [Topic 12])
how the attributes or metadata representing the location at which a machine-readable
version of the trust anchor to be used for verifying the attestation can be found,
specified in section 2, are used. This includes a detailed description about how
a Relying Party can obtain the trust anchor, as well as a detailed description about
how this trust anchor can be used for verifying that the provider is authorised
to issue the attestation. Additionally, for non-qualified EAA Provider this section
MAY include a description of mechanisms that can be used by a Wallet Unit for
verifying that the provider is authorised to issue this type of attestation (see
ISSU_34 in [Topic 10])*




## 6 Revocation
# TODO

(Refer to [Topic 7] of the ARF for a list of High-Level Requirements related to Revocation)

*In this section information about the revocation mechanism used SHALL be defined.*

*For PID, QEAA, or PuB-EAA it SHALL be defined whether only short-lived attestations
will be used, having a validity period of 24 hours or less, such that revocation
will never be necessary, or that the attestations are revocable.*

*For revocable attestations it SHALL be defined which of the following methods must be implemented:*
* Use an Attestation Status List mechanism included in a Technical Specification
that will be specified by the Commission.
* Use an Attestation Revocation List mechanism included in a Technical Specification
that will be specified by the Commission.


## 8 References
| **Item Reference** | **Standard name/details**|
|--------------------|---------------------------|
| [European Business Wallet Vocabulary] | WE BUILD WP4 Semantics Group, European Business Wallet Vocabulary. Available: <https://webuild-consortium.github.io/wp4-semantics-group/ebwv/vocabulary.html> |
| [European Digital Identity Regulation] | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework |
| [GLEIF LEI-CDF] | GLEIF, LEI Common Data File (LEI-CDF) Format 3.1. Available: <https://www.gleif.org/en/lei-data/access-and-use-lei-data/level-1-data-lei-cdf-3-1-format> |
| [HAIP] | Yasuda, K. *et al,* OpenID4VC High Assurance Interoperability Profile, OpenId Foundation, Version draft-03 |
| [IANA-JWT-Claims] | IANA JSON Web Token Claims Registry. Available: <https://www.iana.org/assignments/jwt/jwt.xhtml> |
| [ISO 17442] | ISO 17442-1:2020, Financial services --- Legal entity identifier (LEI) --- Part 1: Assignment |
| [ISO 20275] | ISO 20275:2017, Financial services --- Entity legal forms (ELF) |
| [ISO 3166-1] | ISO 3166-1, Codes for the representation of names of countries and their subdivisions --- Part 1: Country code |
| [ISO/IEC 18013-5] |  ISO/IEC 18013-5, Personal identification --- ISO-compliant driving licence - Part 5: Mobile driving licence (mDL) application, First edition, 2021-09 |
| [OIDC] | Sakimura, N. et al., "OpenID Connect Core 1.0", OpenID Foundation. Available: <https://openid.net/specs/openid-connect-core-1_0.html> |
| [RFC 3339] | RFC 3339  - Date and Time on the Internet: Timestamps, G. Klyne et al., July 2002 |
| [RFC 8610] | RFC 8610  - Concise Data Definition Language (CDDL): A Notational Convention to Express Concise Binary Object Representation (CBOR) and JSON Data Structures, H. Birkholz et al., June 2019 |
| [RFC 8943] | RFC 8943  - Concise Binary Object Representation (CBOR) Tags for Date, M. Jones et al., November 2020 |
| [RFC 8949] | RFC 8949 - Concise Binary Object Representation (CBOR), C. Bormann et al., December 2020 |
| [SD-JWT VC] |  SD-JWT-based Verifiable Credentials (SD-JWT VC). Available: <https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/>, version draft-ietf-oauth-sd-jwt-vc-09  |
| [Topic 7] | ARF Annex 2 - Topic 7 - Attestation revocation and revocation checking Available: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a237-topic-7-attestation-revocation-and-revocation-checking>|
| [Topic 10] | ARF Annex 2 - Topic 10 - Issuing a PID or attestation to a Wallet Unit: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a2310-topic-10-issuing-a-pid-or-attestation-to-a-wallet-unit>|
| [Topic 12] | ARF Annex 2 - Topic 12 - Attestation Rulebooks, Available: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a2312-topic-12-attestation-rulebooks>|
| [W3C VCDM v2.0] | Sporny, M. *et al,* Verifiable Credentials Data Model v2.0, W3C Recommendation.  |
