# Attestation Rulebook for attestations of type VAT ID

Category: QEAA or PuB-EAA, as stated in `attestation_legal_category`

* Author(s):
    * [Sierd Westerfield](mailto:s.westerfield@belastingdienst.nl), Tax Administration Netherlands

| Version | Date | Description |
|---------|------------|------------|
| 1.0 |08-10-2026 | Removed Display |
| 0.99 | 05-10-2026 | Restructured onto the generic WE BUILD attestation rulebook template (11 chapters). No normative content removed. |
| 0.98 |08-09-2026 | Split Legal & natural person |
| 0.97 |03-09-2026 | Further enhancements |
| 0.95 |28-08-2026 | Updates by semantics |
| 0.9 |29-06-2026 | Multiple enhancements |
| 0.8 |05-06-2026 | Changed registration for xborder VAT and description of economic activity|
| 0.7 | 30-04-2026 | Copy from Open Social Rulebook specification |
| --- | --- | --- |

**Written against:** ARF version 3.0.0, WE BUILD template version 1.0 (generic)

**Feedback:**

* [mail the author](mailto:s.westerfield@belastingdienst.nl)

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
   * [9.4 Use cases](#94-use-cases)
- [10 Trust Framework](#10-trust-framework)
- [11 References](#11-references)
   * [11.1 List of Alternative Nomenclatures for Activity types](#111-list-of-alternative-nomenclatures-for-activity-types)


## 1 Introduction

### 1.1 Document scope and purpose

The VAT-ID attestation is an official document issued by a recognized authority, such as the Tax Administration, that verifies the validity of a VAT-ID. This attestation serves as proof of the company’s or administrative unit’s VAT-ID and its corresponding validity period. It contains only information directly related to the VAT-ID.

The VAT-ID attestation can be utilized by a company to substantiate its identity and ownership of the provided VAT-ID. The recipient of the attestation can trust its authenticity, eliminating the need for external verification through the VAT Information Exchange System (VIES) or the request for a physical VAT-ID Certificate.

The most practical applications of the VAT-ID attestation are within procurement processes. Both the buyer and seller provide proof of their VAT ID. This eliminates the necessity of relying on external databases to verify the validity of the VAT ID.

In tender procedures, proof of the VAT ID is required. For instance, companies seeking to participate in the WeBuild project were required to submit a VAT ID Certificate to the commission. For companies based in the Netherlands, the Tax Agency was contacted to request the proof. The Tax Agency provided the proof on paper, affixed with a stamp. The company then scanned the document and uploaded it to the commission as part of its application submission.

The VAT-ID attestation also provides information on:
* The address of the economic operator.
* The economic activities in which the economic operator engages. These activities are referenced in both NACE codes, local equivalents, and a concise description of the activity.
* The period in which the VAT-ID is valid.

The VAT-ID attestation seeks to replace the traditional paper-based proof with an attestation. The VAT-ID Attestation is expected to enhance both the efficiency and security of the process.

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

This document uses the terminology specified in Annex 1 of the ARF.

## 2 Compliance

### 2.1 Compliance statement

This Rulebook complies with the applicable requirements of Topic 12, Attestation
Rulebooks, in Annex 2 of the Architecture and Reference Framework, version 3.0.0. It
uses the terminology of Annex 1 of the ARF.

### 2.2 Regulatory basis

The VAT-ID attestation is issued as a QEAA or a PuB-EAA (section 3.1). The paragraph for the
category stated in `attestation_legal_category` applies.

**QEAA**

This attestation includes the data required by Annex V of Regulation (EU) 2024/1183,
points a, b, c, e and h, satisfying EW-DM-12-014, EW-DM-12-016, EW-DM-12-019, EW-DM-12-021
and EW-DM-12-023 respectively. It is issued by a qualified trust service provider.

**PuB-EAA**

This attestation includes the data required by Annex VII of Regulation (EU) 2024/1183,
points a, b, c, e and h, satisfying EW-DM-12-014, EW-DM-12-017, EW-DM-12-019, EW-DM-12-021
and EW-DM-12-023 respectively. It is issued by or on behalf of a public sector body
responsible for an authentic source.

### 2.3 Traceability

Every applicable requirement mapped to the section that satisfies it. Requirements
marked not applicable carry a stated reason.

| Requirement | Legacy ID | Applies | Satisfied in section | Note |
| --- | --- | --- | --- | --- |
| EW-DM-12-001 | ARB_01a | yes | 5 | SD-JWT VC only; W3C VCDM is not permitted for a QEAA or PuB-EAA |
| EW-DM-12-002 | ARB_01b | yes | 5.1 | SD-JWT VC following the HAIP profile |
| EW-DM-12-003 | ARB_02 | no |  | No proximity use case, see section 5.2 |
| EW-DM-12-005 | ARB_04 | no |  | W3C VCDM is not permitted for this category |
| EW-DM-12-006 | ARB_05 | yes | 5.1 | `uri:eu.eudi.vat.1` |
| EW-DM-12-007 | ARB_06 | yes | 3 | Attributes defined independently of encoding |
| EW-DM-12-008 | ARB_06a | no |  | No mdoc encoding is defined |
| EW-DM-12-009 | ARB_06b | yes | 5.1 | SD-JWT VC claim naming |
| EW-DM-12-010 | ARB_07 | yes | 3 | European Business Wallet Vocabulary references |
| EW-DM-12-012 | ARB_09 | yes | 3, 4 | Mandatory and optional stated per object |
| EW-DM-12-013 | ARB_10 | no |  | No domestic namespace is defined |
| EW-DM-12-014 | ARB_11 | yes | 4.1, 5.1 | `attestation_legal_category`, QEAA or PuB-EAA |
| EW-DM-12-015 | ARB_12 | no |  | Not a non-qualified EAA |
| EW-DM-12-016 / EW-DM-12-017 / EW-DM-12-018 | ARB_13 / ARB_14 / ARB_15 | yes | 2.2, 4.1 | Point b through the issuer metadata |
| EW-DM-12-019 / EW-DM-12-020 | ARB_16 / ARB_17 | yes | 2.2, 3.2 | Point c through the legal person or natural person attributes |
| EW-DM-12-021 / EW-DM-12-022 | ARB_18 / ARB_19 | yes | 2.2, 4.1 | Point e through the attestation issuing and expiry dates |
| EW-DM-12-023 / EW-DM-12-024 | ARB_20 / ARB_21 | yes | 4.2, 10 | `trust_anchor` metadata and the Trusted List |
| EW-DM-12-029 | ARB_25 | yes | 4.1, 5.1 | Legal category attribute; see the note in section 4.1 |
| EW-DM-12-030 | ARB_26 | no |  | Not a non-qualified EAA |
| EW-DM-12-031 | ARB_27 | no |  | Ownership is checked through the EBWOID, a PID or a mandate, see section 9.1 |
| EW-DM-12-032 | ARB_28 | no |  | `cryptographically_bound_to` is not used |
| EW-DM-12-034 | ARB_30 | yes | 5.1 | Selective disclosure stated per claim |
| EW-DM-12-035 | ARB_31 | no |  | No Claim Selective Disclosure Metadata document is used |
| EW-DM-12-038 | ARB_34 | yes | 7.1 | Non device-bound by design, see the justification in section 7.1 |

## 3 Attestation attributes

Attributes are defined here in an encoding-independent manner (EW-DM-12-007). The
encoding of each attribute is given in chapter 5.

### 3.1 Introduction

The VAT-ID attestation is an attestation provided by an authentic source such as a TAX-Administration. The attestation proves the VAT-ID of the company or administrative unit within the company and the validity period of that VAT-ID. The VAT-ID attestation only contains information directly related to the VAT-ID.
The VAT-ID attestation can be used by a company to prove that the company really is the company with that number. The receiver of the attestation can trust the content and there is no need for checking the VAT-ID at VIES (VAT Information Exchange System)1 or request a (paper) VAT-ID Certificate.

The VAT-ID attestation contains some information for which the TAX-agency usually is not the authentic source. We choose to include the information because:
* it is currently on the paper certificate,
* the information might be relevant to the receiver of the attestation. Alternatively the holder should present multiple attestations at once.

Both the attributes of the address and the economic activity usually are not administered by the TAX Agency but at the business register. However the TAX-Administration might hold different addresses and have specific economic activities registered for an administrative unit in the case that an economic operator has multiple administrative units.

*According to Annex V point a) and  Annex VII point a) of the [European Digital Identity Regulation]
an indication, at least in a form suitable for automated processing, that the attestation
has been issued as a QEAA or Pub-EAA SHALL be defined. Similarly, according to ARB_12
of [Topic 12] of Annex 2 of the ARF a similar indication SHOULD be defined for non-qualified EAA.

This document defines the attribute "VAT-ID" which SHALL either be issued as QEAA or a PuB-EAA

````
vat_id_attestation
├─ administrative_unit                            [1]
│   ├─ vat_id                                     [1]       (VAT-ID of the administrative unit)
│   ├─ name                                       [1]       (name of the administrative unit)
│   ├─ organisation_type                          [0]       (type of organisation in free text)
│   ├─ validity_period                            [1..n]    (period(s) for which the vat-id is valid)
│   │   ├─ start_date                             [1]       (start date of the validity period of the vat-id)
│   │   └─ end_date                               [0]       (end date of the validity period of the vat-id)
│   ├─ registered_eu_cross_border_transactions    [1]       (Boolean that describes if the VAT-ID may be used EU cross border transactions)
│   ├─ economic_operator                          [1]       (Reference to the Economic Operator that owns the VAT ID)
│   │   ├─ legal_person                           [0]
│   │   │   ├─ legal_identifier                   [1]
│   │   │   ├─ legal_name                         [1]
│   │   ├─ natural_person                         [0]
│   │   │   ├─ family_name                        [1]
│   │   │   ├─ given_name                         [1]
│   │   │   ├─ birth_date                         [1]
│   │   │   ├─ birth_place                        [0]
│   │   │   ├─ tin                                [0]
│   │   │   └─ personal_administrative_number     [0]
│   ├─ address                                    [0]       (the postal address registered for the administrative unit)
│   │   ├─ po_box                                 [0]
│   │   ├─ thoroughfare                           [0]
│   │   ├─ location_designator                    [0]
│   │   ├─ post_code                              [0]
│   │   ├─ post_name                              [0]
│   │   ├─ admin_unit_l1                          [0]
│   │   └─ admin_unit_l2                          [0]
│   └─ economic_activity                          [0..n]    (reference to the economic operator)
│       ├─ economic_activity_nomenclature         [1]       (nomenclature used to describe the economic activity)
│       ├─ economic_activity_nomenclature_version [0]     (version of the nomenclature)
│       ├─ economic_activity_id                   [1]       (id used in the nomenclature)
│       └─ economic_activity_description.         [1..n]    (object using language:, value)
└─ issuer                                         [1]   
    ├─ issuing_country                            [1]
    ├─ issuing_authority                          [1]        (the organisation that issues the vat-id, this may differ from the attestation issuing organisation)
    ├─ attestation_issuing_date                   [1]        (date on which the attestation is issued)
    └─ attestation_issuing_organisation           [1]
````

### 3.2 Mandatory attributes

Mandatory attributes are stated per object of the data model in section 3.1.

#### 3.2.1 VAT-ID Attestation

| data identifier | Semantic Reference | Definition | Data Type | Example Value |
| --- | --- | --- | --- | --- |
| administrative_unit | administrative unit | administrative unit within an economic operator that holds a separate administration to which the VAT-ID is issued | Administrative_unit  Object | .. |
| issuer | [cred:issuer](https://www.w3.org/2018/credentials#issuer) | Authority that issues the VAT ID | Issuer Object | .. |
| display | display |  | Display Object | .. |

#### 3.2.2 administrative_unit

| data identifier | Semantic Reference | Definition | Data Type | Example Value |
| --- | --- | --- | --- | --- |
| administrative_unit.vat_id | [identifier](https://w3id.org/ebwv#identifier) | Unique identifier for VAT purposes | String | DE123456789 |
| administrative_unit.name | [VATRegistrationUnit](https://w3id.org/ebwv#VATRegistrationUnit).[schema:name](https://schema.org/name) | Name of the unit responsible for VAT | String | Siemens |
| administrative_unit.validity_period | [cred:validFrom](https://www.w3.org/2018/credentials/#validFrom)<br>[cred:validUntil](https://www.w3.org/2018/credentials/#validUntil) | Duration during which the data is valid | Date Range | 2026-01-01 to 2026-12-31 |
| administrative_unit.economic_operator | [EconomicOperator](https://w3id.org/ebwv#EconomicOperator) | Entity responsible for economic operations | Economic Operator object | .. |

#### 3.2.3 Economic Operator

There SHALL be a reference from the Administrative Unit to the Economic Operator. However the the Economic Operator can either be a [Legal Person](https://iri.suomi.fi/terminology/webuild/concept-109) or a [Natural Person](https://iri.suomi.fi/terminology/webuild/concept-6005). The economic operator object SHALL be filled to one of the two, not to both.

#### 3.2.4 Legal person

| **data identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| legal_person.legal_identifier | [legalIdentifier](https://w3id.org/ebwv#legalIdentifier) | The relevant unique identifier attributed in accordance with Article 9 of EWB (WEBUILD specific EUID where available, otherwise a similar constructed, unique per issuer identifier. <Countrycode ISO 3166-1 alpha-2>. eks. SE +  BOLREG + 123456789 -> SEBOLREG.123456789 | string | SEBOLREG.123456789 |
| legal_person.legal_name | [legalName](https://w3id.org/ebwv#legalname) | the name under which the legal entity is legally registered | string | ACME |

#### 3.2.5 Natural person

| **data identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| natural_person.family_name | [familyName](https://w3id.org/ebwv#familyName) | Current last name(s) or surname(s) of the user to whom the person identification data relates. | string | Doe |
| natural_person.given_name | [givenName](https://w3id.org/ebwv#givenName) | Current first name(s), including middle name(s) where applicable, of the user to whom the person identification data relates. | string | John |
| natural_person.birth_date | [dateOfBirth](https://w3id.org/ebwv#dateOfBirth) | Day, month, and year on which the user to whom the person identification data relates was born. | Date | 1968-04-27 |

#### 3.2.6 Validity Period

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| validity_period.start_date | [startDate](https://w3id.org/ebwv#startDate) | Date of registration of the VAT-ID. | date | 2011-12-24 |

#### 3.2.7 Address

No mandatory attributes

#### 3.2.8 Economic Activity Type attributes

| **data identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| economic_activity.nomenclature | [activity](https://w3id.org/ebwv#activity) | The nomenclature that is used to describe the administrative unit. NACE should be used as default. However some countries have more elaborate nomenclature. | string | nace |
| economic_activity.id | [activity](https://w3id.org/ebwv#activity) | The ID that under which the Administrative unit is registered. | string | C26.5.2 |
| economic_activity.description | [activity](https://w3id.org/ebwv#activity) | The human readable text that describes the economic ativity in a specific language. The language is described in BCP 47 standard | array | en-GB: Manufacture of bearings, gears, gearing and driving elements |

### 3.3 Optional attributes

Optional attributes are stated per object of the data model in section 3.1.

#### 3.3.1 administrative_unit

| **data identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| administrative_unit.organisation_type | [type](https://w3id.org/ebwv#type) | Type (e.g., Government, Local Authority, B.V, GmbH) | String | GmbH |
| administrative_unit.address | [VATRegistrationUnit](https://w3id.org/ebwv#VATRegistrationUnit).[address](https://w3id.org/ebwv#address) | The address where the company is located based on the information from the authentic source of the VAT-ID. This address may differ from the address in the business register. | Address Object | ... |
| administrative_unit.economic_activity | [VATRegistrationUnit](https://w3id.org/ebwv#VATRegistrationUnit).[activity](https://w3id.org/ebwv#activity) | Type of business this administrative unit is registered | Economic Activity Type Object | ... |
| administrative_unit. registered_eu_cross_border_transactions | [VATRegistrationUnit](https://w3id.org/ebwv#VATRegistrationUnit).[references](https://w3id.org/ebwv#references) | Boolean to indicate that the VAT-identification number of the economic operator registered in the European Union for cross border transactions on goods or services | Boolean | TRUE |

#### 3.3.2 Economic Operator

| **data identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| legal_person | [legalPerson](https://w3id.org/ebwv#LegalPerson) | individual, company, or organization recognized by law. It possesses distinct rights and responsibilities, meaning it can own property, enter into contracts, incur debts, pay taxes, and sue or be sued in | oBeject |  |
| natural_person | [naturalPerson](https://w3id.org/ebwv#NaturalPerson) | The natural person the VAT-ID is issued to | Object |  |

#### 3.3.3 Legal person

If the Legal person is filled, there are no optional attributes

#### 3.3.4 Natural person

| **data identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| natural_person.birth_place | [placeOfBirth](https://w3id.org/ebwv#placeOfBirth) | The country as acountry code as specified in ISO 3166-1 alpha-2, or the state, province, district, or local area or the municipality, city, town, or village where the user to whom the person identification data relates was born. | string | Amsterdam |
| natural_person.tin | [identifier](https://w3id.org/ebwv#identifier) | tax reference number | string |  |
| natural_person.personal_administrative_number | [personalAdministrative Number](https://w3id.org/ebwv#personalAdministrativeNumber) | A value assigned to the natural person that is unique among all personal administrative numbers issued by the provider of person identification data. The personal Administrative Number may only be used if the local law allows for unrestricted use | string | 123456782 |

#### 3.3.5 Validity Period

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| validity_period.end_date | [endDate](https://w3id.org/ebwv#endDate) | The end date after which VAT-ID registration ended. | date | 2021-01-24 |

#### 3.3.6 Address

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| address.po_box | [poBox](https://w3id.org/ebwv#poBox) | P.O. box number or identifier within the address; optional | string | PO Box 123 |
| address.thoroughfare | [thoroughfare](https://w3id.org/ebwv#thoroughfare) | Street name and house number or other thoroughfare designation; optional | string | Main Street 10 |
| address.location_designator | [locationDesignator](https://w3id.org/ebwv#locatordesignator) | Internal location designation within a building (e.g., floor, unit); optional | string | Floor 3, Unit B |
| address.post_code | [postCode](https://w3id.org/ebwv#postcode) | Postal or ZIP code; optional | string | 12345 |
| address.post_name | [postName](https://w3id.org/ebwv#postname) | Town or locality name; optional | string | Amsterdam |
| address.admin_unit_L1 | [adminUnitL1](https://w3id.org/ebwv#adminUnitL1) | First-level administrative division (e.g., province, state); optional | string | North Holland |
| address.admin_unit_L2 | [adminUnitL2](https://w3id.org/ebwv#adminUnitL2) | Second-level administrative division (e.g., district, municipality); optional | string | Amsterdam Municipality |

#### 3.3.7 Economic Activity Type attributes

| **data identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| economic_activity.nomenclature_version | [activity](https://w3id.org/ebwv#activity) | The version of the nomenclature that is used to describe the administrative unit. | string | Rev 2.1 |

### 3.4 Conditional attributes

No conditional attributes are defined for this attestation type.

## 4 Metadata

Metadata describes the attestation rather than its subject.

### 4.1 Mandatory metadata

| **data identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| issuer.authentic_source_country | issuingCountry | Country code, as specified in ISO 3166-1 alpha-2, of the country or territory of the provider of the VAT ID. | string | NL |
| issuer.vat_id_authenticsource | authenticSource | Name of the administrative authority that issued the VAT ID. This is the authentic source for the VAT-ID, which may differ from the issuer of the attestation | string | Belastingdienst |
| issuer.country | issuingCountry | Country code, as specified in ISO 3166-1 alpha-2, of the country or territory of the provider of the VAT ID. | string | NL |
| issuer.issuing_authority | issuerAuthority | Name of the administrative authority or qualified trust service provider that issued the VAT ID attestation, in a specific language using  BCP 47 | string | en-GB |
| issuer.attestation_issuing_date | iat | The date the attestation was issued | Integer (Unix timestamp) |  |
| issuer.attestation_expiry_date | exp | The date the attestation was issued | Integer (Unix timestamp) |  |

**Legal category.** This Rulebook retains the `attestation_legal_category` attribute.
Section 4.1 of the generic template replaces it with the `category` attribute of
[ETSI TS 119 472-1]. EW-DM-12-029, legacy ARB_25, of ARF version 3.0.0 is a SHALL that
still requires the legal category attribute, so the template and the ARF disagree. The
attribute is left as written and the deviation is recorded for the rulebook quality
assurance group.

### 4.2 Optional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| issuer.location_status | locationStatus | The location of validity status information on the VAT ID used for revocation/suspension checks. | string |  |
| trust_anchor | trustAnchor | This meta-data attribute indicates at least the URL at which a machine‑readable version of the trust anchor to be used for verifying the VAT ID can be found or looked up. This corresponds to Annex V/VII point h) of the [European Digital Identity Regulation] and EBW Article 8 issuance as EAA/QEAA. | string |  |

### 4.3 Conditional metadata

No conditional metadata are defined for this attestation type.

### 4.4 Code lists

| **field name** | **Allowed values** | **Meaning** | **Source / vocabulary** | **Notes / extensibility** |
| --- | --- | --- | --- | --- |
| administrative_unit.economic_activity_type. nomenclature | NACE, NACE-BEL, CZ‑NACE, DB07, WZ, KAD, CNAE, NAF, NKD, ATECO, TEAOR, SBI, ONACE, PKD, CAE, CAEN, SKD, OKEC, TOL, SNI, UK SIC, NOGA | Each name refers to the local adaptation of the NACE list. | [Overview of alternative nomenclatures](#81-list-of-alternative-nace-codes) | List SHOULD be used or refer to NACE closest alternative |

### 4.5 Integrity rules

| **Rule ID** | **Rule statement** | **Why it exists** | **Where enforced** | **Verifier / issuer behavior on failure** |
| --- | --- | --- | --- | --- |
| EO1 | Exactly one of legal_person or natural_person SHALL be present. | There may only be one reference to the holder of the Wallet. If there is more than one, there could be an inconsistency | *Issuer, verifier, schema validation, or business process* | *Describe rejection, warning, or remediation behavior* |
| VP1 | If 'administrative_unit. validity_Period.end_Date' is not NULL, 'administrative_unit. validity_Period.end_Date' SHALL be higher than 'administrative_unit.validity_Period.start_Date' | Validity periods may not be negative | The VAT-ID attestation may not be issued, because there shouldn't be a negative period in the register |
| VP2 | If any 'validity_Period' overlaps with another validity period the attestation SHALL NOT be issued | Validity periods may not overlap because this should not happen and might create problems for relying parties. This rule also takes care of the issue of multiple validity periods without an enddate |  |
| VP3 | If 'administrative_unit. validity_Period.end_Date' < issuer. attestation_issuing_date - 5 years | Old validity periods are not relevant to relying parties, the limit of 5 years should be used as a rule of thumb |  |
| VP4 | If there is more than one 'administrative_unit.validity_Period' the issuer MAY omit older validity_Periods | Issuers have the freedom to omit older validity periods, when they find they are not relevant |  |
| EA1 | If ('administrative_unit. Economic_Activity_Type.ID' AND 'administrative_unit. Economic_Activity_Type.Nomenclature <>"NACE")  is equal ('administrative_unit. Economic_Activity_Type.ID' AND 'administrative_unit. Economic_Activity_Type.Nomenclature == "NACE") Then 'administrative_unit.Economic_Activity_Type.Nomenclature SHOULD be "NACE" | The default Nomenclature is NACE, if the ID in the local Nomenclature directly relates to the NACE ID, the NACE ID and TYPE SHOULD be used. | Issuers SHOULD implement a tranlation table to create mostly NACE codes |
| XB1 | If ('issuing_country' is not in EU Then  'registered_eu_ cross_border_transactions' SHOULD be false | Only countries in the EU can take part in the registered_eu_ cross_border_transactions |



## 5 Formats

| Format | Supported | Identifier | Specification | Notes |
| --- | --- | --- | --- | --- |
| ISO/IEC 18013-5 mdoc | no |  | [ISO/IEC 18013-5] | Not defined; no proximity use case, see section 5.2 |
| SD-JWT VC | yes | `vct` `uri:eu.eudi.vat.1` | [SD-JWT VC], [HAIP] | SHALL follow the HAIP profile, see section 5.1 |
| W3C VCDM | no |  | [W3C VCDM v2.0] | Not permitted for a QEAA or PuB-EAA |

### 5.1 SD-JWT VC-based encoding

The VAT-ID attestation uses the SD-JWT VC format to allow for selective disclosure of  attributes.

**Verifiable Credential Type (`vct`):** `uri:eu.eudi.vat.1`

#### 5.1.1 Attribute Encoding Table

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Reference/ Notes** | **Disclosable** |
| --- | --- | --- | --- | --- |
| administrative_unit.vat_id | vat_id | VAT Identification Number | String |  | MUST NOT |
| administrative_unit.name | administrative_unit_name | String |  | MUST NOT |
| administrative_unit.validity_period | validity_period | Array [validity period] |  | MUST NOT |
| administrative_unit.economic_operator | economic_operator | object | .. | MUST NOT |
| issuer | issuer | Object | .. | MUST NOT |
| administrative_unit.organisation_type | organisation_type | Object | ... | MUST |
| administrative_unit.address | administrative_unit_address | Object | ... | MUST |
| administrative_unit. registered_eu_cross_border_transactions | registered_eu_cross_ border_transactions | Boolean | .. | MUST NOT |
| administrative_unit. economic_operator.legal_person. legal_identifier | legal_identifier | String | .. | MUST |
| administrative_unit. economic_operator.legal_person. legal_name | legal_name | String | .. | MUST |
| administrative_unit. economic_operator.natural_person. family_name | family_name | String | .. | MUST |
| administrative_unit. economic_operator.natural_person. given_name | given_name | String | .. | MUST |
| administrative_unit. economic_operator.natural_person. birth_date | birth_date | String (ISO 8601 YYYY-MM-DD) | .. | MUST |
| administrative_unit. economic_operator.natural_person. birth_place | birth_place | String | .. | MUST |
| administrative_unit. economic_operator.natural_person. tin | tin | String | .. | MUST |
| administrative_unit. economic_operator.natural_person. epersonal_administrative_number | personal_administrative_number | String | .. | MUST |
| administrative_unit. validity_period.start_date | validity_period.start_date | String (ISO 8601 YYYY-MM-DD) | .. | MUST NOT |
| administrative_unit. validity_period.end_date | validity_period.end_date | String (ISO 8601 YYYY-MM-DD) | .. | MUST NOT |
| administrative_unit. address.po_box | address.po_box | String | .. | MUST |
| administrative_unit. address.thoroughfare | address.thoroughfare | String | .. | MUST |
| administrative_unit. address.location_designator | address.location_designator | String | .. | MUST |
| administrative_unit. address.post_code | address.post_code | String | .. | MUST |
| administrative_unit. address.post_name | address.post_name | String | .. | MUST |
| administrative_unit. address.admin_unit_L1 | address.admin_unit_L1 | String | .. | MUST |
| administrative_unit. address.admin_unit_L2 | address.admin_unit_L2 | String | .. | MUST |
| administrative_unit. economic_activity_type | economic_activity_type | Array | .. | MUST |
| administrative_unit. economic_activity_type. nomenclature | economic_activity_type. nomenclature | String one of(NACE, NACE-BEL, CZ‑NACE, DB07, WZ, KAD, CNAE, NAF, NKD, ATECO, TEAOR, SBI, ONACE, PKD, CAE, CAEN, SKD, OKEC, TOL, SNI, UK SIC, NOGA) | .. | MUST NOT |
| administrative_unit. economic_activity_type. id | economic_activity_type.id | String | .. | MUST |
| administrative_unit. economic_activity_type. description | economic_activity_type. description | object ("langue code iso 639-1": "description") | .. | MUST |
| issuer.authentic_source_country | issuer.authentic_source_country | String (ISO 3166-1 alpha-2) | .. | MUST NOT |
| issuer.vat_id_authenticsource | issuer.vat_id_authenticsource | String | .. | MUST NOT |
| issuer.country | issuer.country | String | .. | MUST NOT |
| issuer.issuing_authority | issuer.issuing_authority | String | .. | MUST NOT |
| issuer.attestation_legal_category | issuer.attestation_legal_category | String | .. | MUST NOT |
| issuer.location_status | issuer.location_status | String (URI) | .. | MUST NOT |
| trust_anchor | trustAnchor | String (URI) | .. | MUST NOT |
| iat | `iat` | Integer (Unix timestamp) | The date and time when the attestation was issued (ISO 8601); RFC 7519 / Section 3.2.4 | MUST NOT |
| exp | `exp` | Integer (Unix timestamp) | The date and time when the attestation expires (ISO 8601); RFC 7519 / Section 3.2.4 | MUST NOT |

**Notes:**

- **MUST**: The claim SHALL be selectively disclosable, the holder MAY choose to disclose or
  withhold this claim when presenting the credential to a Relying Party.
- **MUST NOT**: The claim SHALL NOT be selectively disclosable, it is always present in plain
  text in the JWT header/payload and cannot be withheld by the holder, as it is required for
  credential verification and trust establishment.
- `iat` and `exp` follow RFC 7519 standard JWT claim naming conventions.

#### 5.1.2 Status Claim

The revocable attestation (SD-JWT VC per HAIP [7]) carries the status reference in its signed payload. The claim is not selectively disclosable.

```json
{
  "status": {
    "status_list": {
      "idx": 422,
      "uri": "https://status-provider.example.com/statuslists/1"
    }
  }
}
```

- `uri` — the Status Provider's URI from which the Status List Token can be retrieved
- `idx` — the index of this attestation's entry within the status list, assigned per ISS-RV-03


### 5.2 ISO/IEC 18013-5-compliant encoding

Currently there is no usecase defined where proximity use of the VAT-ID attestation. For now there will be no ISO/IEC 18013-5-compliant encoding.

### 5.3 W3C Verifiable Credentials Data Model-based encoding

This Rulebook does not define a W3C Verifiable Credentials Data Model encoding; the format is not permitted for a QEAA or PuB-EAA.

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
| Device-bound | non device-bound | EW-DM-12-038 |
| Cryptographically bound to | none | EW-DM-12-032 |
| Relying Party must also verify a PID | no | EW-DM-12-031 |
| Binding subject | legal person or natural person, the economic operator |  |

The attestation SHALL be non-device-bound. The relying party SHOULD check the ownership of the VAT-ID using the method described above. Device binding might create a false sence of trustworthyness. Because the VAT-ID can be issued to an intermediary organisation, using a mandate, presenting the VAT-ID is no proof of ownership. The VAT-ID attestation will not be revoked by the issuer, when the mandate is revoked.

### 7.2 Issuance Policy

General obligations on Attestation Providers are out of scope of this Rulebook. They
are specified in Topic 10 of Annex 2 of the ARF, in the applicable Implementing
Regulations, and in [ETSI TS 119 471]. This Rulebook states only obligations specific
to this attestation type.

The VAT-ID attestation may only be issued to the wallet of the organisation that holds the VAT-ID, or to the wallet of an Agent (natural or legal person) that can prove that he is allowed to act upon the holder for this service. Although many of the information in the attestation is public information, the attestation itself should be considered private. In order to issue the VAT-ID attestation to the Economic Operator itself the issuing party SHOULD: Verify the identity of the Economic Opereator and issue the VAT-ID attestation to the wallet of that Economic Operator.

If an agent wishes to receive the attestation of another economic operator, the issuing party SHOULD:
* Check the identity of the Agent
    - check if the agent has a mandate with the right scope and actors
      -    the mandate is not revoked
      -    the mandate is currently valid

### 7.3 Lifecycle management

The issuer sets the validity period of the attestation and reissues it when the
underlying facts change, revoking the superseded attestation as described in chapter 8.

### 7.4 Embedded disclosure policy

This attestation defines no embedded disclosure policy.

## 8 Revocation

The VAT-ID Attestation SHOULD preferably be issued as a longlived attestation. In order to make sure the attestation reflects the current situation, the issuer MUST have revocation in place. An issuer must revoke the attestation following an event that would render any part of the content invalid.

When the attestation is issued by a QTSP outside the Authentic Source it should receive information from the authentic source in case attributes of the attestation change at the source. If the QTSP cannot receive this information, the attestation MUST be shortlived.

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

The VAT-ID provides proof that the Economic Operator, registered in the attestation, is the owner of the VAT-ID. It does not prove that the party that presents the attestation also is the owner of the attestation. The VAT-ID attestion can also be issued to an Agent ( Intermediary party), if they have the right mandate to receive the attestation. However the mandate may be revoked by the owner, but the VAT-ID attestation will (likely) not be revoked. Therefore the attestation itself (even if holderbinding is active) is not proof that the presenter actually holds, or may present the attestation.

The relying party SHOULD:
- Check the status of revocation and expiry date of the attestation.
- Check the validity period in the attestation.

- Check if the Economic Operator in the Attestation is:
   - equal to the owner of the EBW (via EBWOID, PID, or other means) OR
   - has a mandate with the right scope and actors
      -    the mandate is not revoked
      -    the mandate is currenty valid

If the relying party does not perform all verification aspects, he MUST accept the risks involved.

### 9.2 Presentation modes

Remote presentation is in scope. Proximity presentation is not in scope, consistent
with chapter 5, which records that no mdoc encoding is defined.

### 9.3 Transactional data

This Rulebook defines no transactional data.

### 9.4 Use cases

The VAT_ID attestation aims to be used in two general usecases, but it could be used elsewhere. The first usecae is where the relying party requires proof that the Economic Operator has a valid VAT-ID. In the 'paper' world, the relying party would request a 'Certificate of the VAT-ID' relyably issued by the relevant Tax Authority. The Economic Operator requests the Certificate, and it will be sent to the registered address of the Economic Operator. The Certificate is printed on paper of the Tax Authority and or contains stamps, signature or other ways to proof its validity.

The second usecase is where a seller needs proof, in case of intra-communitairy business, that the buyer will pay tax in his own country and that it can sell services or goods without TAX. In the current world the seller needs to check with VIES and keep proof in its administration. The VAT-ID attestation will provide the proof, and a check with VIES is not necessary anymore.

## 10 Trust Framework

The trust anchor is obtained as described in the branch below that corresponds to the
legal category under which the attestation was issued.

**PID, QEAA, PuB-EAA and attestations resolved via Trusted Lists**

The trust anchor is obtained from a Trusted List, as described in section 6.6.3.6 of the
ARF main document. The Provider may sign the attestation with an intermediate signing
certificate, in which case the trust anchor is used to verify that certificate rather
than the attestation directly.

**Trust anchor location**

The attribute or metadata carrying the trust anchor location contains at least the URL
at which a machine-readable version can be found or looked up.

## 11 References

| **Item Reference** | **Standard name/details** |
| --- | --- |
| [European Digital Identity Regulation] | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework |
| [HAIP] | Yasuda, K. *et al,* OpenID4VC High Assurance Interoperability Profile, OpenId Foundation, Version draft-03 |
| [IANA-JWT-Claims] | IANA JSON Web Token Claims Registry. Available: <https://www.iana.org/assignments/jwt/jwt.xhtml> |
| [ISO/IEC 18013-5] | ISO/IEC 18013-5, Personal identification --- ISO-compliant driving licence - Part 5: Mobile driving licence (mDL) application, First edition, 2021-09 |
| [OIDC] | Sakimura, N. et al., "OpenID Connect Core 1.0", OpenID Foundation. Available: <https://openid.net/specs/openid-connect-core-1_0.html> |
| [RFC 3339] | RFC 3339  - Date and Time on the Internet: Timestamps, G. Klyne et al., July 2002 |
| [RFC 8610] | RFC 8610  - Concise Data Definition Language (CDDL): A Notational Convention to Express Concise Binary Object Representation (CBOR) and JSON Data Structures, H. Birkholz et al., June 2019 |
| [RFC 8943] | RFC 8943  - Concise Binary Object Representation (CBOR) Tags for Date, M. Jones et al., November 2020 |
| [RFC 8949] | RFC 8949 - Concise Binary Object Representation (CBOR), C. Bormann et al., December 2020 |
| [SD-JWT VC] | SD-JWT-based Verifiable Credentials (SD-JWT VC). Available: <https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/>, version draft-ietf-oauth-sd-jwt-vc-09 |
| [Topic 7] | ARF Annex 2 - Topic 7 - Attestation revocation and revocation checking Available: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a237-topic-7-attestation-revocation-and-revocation-checking> |
| [Topic 10] | ARF Annex 2 - Topic 10 - Issuing a PID or attestation to a Wallet Unit: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a2310-topic-10-issuing-a-pid-or-attestation-to-a-wallet-unit> |
| [Topic 12] | ARF Annex 2 - Topic 12 - Attestation Rulebooks, Available: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a2312-topic-12-attestation-rulebooks> |
| [Topic 20] | ARF Annex 2 - Strong User authentication for electronic payments, Available: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a2320-topic-20-strong-user-authentication-for-electronic-payments> |
| [W3C VCDM v2.0] | Sporny, M. *et al,* Verifiable Credentials Data Model v2.0, W3C Recommendation. |

### 11.1 List of Alternative Nomenclatures for Activity types

Generated by DUCK.AI using ChatGPT 5.1 mini

| Country | National implementation / name |
| --- | --- |
| Belgium | NACE-BEL |
| Bulgaria | NACE (Bulgarian implementation, Rev.2) |
| Czech Republic | CZ‑NACE |
| Denmark | DB07 / Danish adaptations (mapped to NACE) |
| Germany | WZ 2008 (Klassifikation der Wirtschaftszweige) |
| Estonia | NACE (Estonian implementation) |
| Ireland | NACE (CSO adapted list) |
| Greece | KAD (Classification of Economic Activities) |
| Spain | CNAE |
| France | NAF |
| Croatia | NKD |
| Italy | ATECO (ISTAT) |
| Cyprus | NACE (Cyprus Statistical Service) |
| Latvia | NACE (Latvian implementation) |
| Lithuania | NACE (Lithuanian implementation) |
| Luxembourg | NACE (STATEC) |
| Hungary | TEÁOR (TEÁOR 08) |
| Malta | NACE (NSO) |
| Netherlands | SBI (Standard Industrial Classification) |
| Austria | ÖNACE |
| Poland | PKD |
| Portugal | CAE |
| Romania | CAEN |
| Slovenia | SKD |
| Slovakia | SK NACE / OKEČ |
| Finland | TOL |
| Sweden | SNI |
| United Kingdom* | UK SIC (historical mappings to NACE) |
| Norway | NACE‑mapped national classification (Statistics Norway) |
| Iceland | NACE/ISIC mappings (Statistics Iceland) |
| Liechtenstein | NACE‑mapped classification |
| Switzerland | NOGA |

*The UK is no longer an EU member; included due to extensive historical mappings.
