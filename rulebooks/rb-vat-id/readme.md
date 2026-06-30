# WE BUILD Attestation Rulebook of type VAT ID


* Author(s):
    * [Sierd Westerfield](mailto:s.westerfield@belastingdienst.nl), Tax Administration Netherlands



| Version | Date | Description |
|---------|------------|------------|
| 0.9 |29-06-2026 | Multiple enhancements |
| 0.8 |05-06-2026 | Changed registration for xborder VAT and description of economic activity|
| 0.7 | 30-04-2026 | Copy from Open Social Rulebook specification |

*Provide a contact email address and/or a link to an issue tracking system that can be used for
providing feedback, e.g.:*

**Feedback:**

* [mail the author](mailto:s.westerfield@belastingdienst.nl)

## Table of Contents

- [1 Introduction](#1-introduction)
  - [1.1 Document scope and purpose](#11-document-scope-and-purpose)
  - [1.2 Document structure](#12-document-structure)
  - [1.3 Key words](#13-key-words)
  - [1.4 Terminology](#14-terminology)
- [2 Attestation attributes and metadata](#2-attestation-attributes-and-metadata)
  - [Chapter overview and requirements](#chapter-overview-and-requirements)
  - [2.1 Introduction](#21-introduction)
  - [2.2 Administrative Unit](#22-administrative-unit)
  - [2.3 Economic Operator](#23-economic-operator)
  - [2.4 Validity Period](#24-validity-period)
  - [2.5 Address](#25-address)
  - [2.6 Economic Activity Type attributes](#26-economic-activity-type-attributes)
  - [2.7 Metadata](#27-metadata)
  - [2.8 Display](#28-display)
  - [2.9 Code lists](#29-code-lists)
  - [2.10 Integrity rules](#210-integrity-rules)
- [3 Attestation encoding](#3-attestation-encoding)
  - [3.1 ISO/IEC 18013-5-compliant encoding](#31-isoiec-18013-5-compliant-encoding)
  - [3.2 SD-JWT VC-based encoding](#32-sd-jwt-vc-based-encoding)
- [4 Attestation usage](#4-attestation-usage)
  - [4.1 Usecases](#41-usecases)
  - [4.2 Issuing requirements](#42-issuing-requirements)
  - [4.3 Verification needs](#43-verification-needs)
- [5 Trust anchors](#5-trust-anchors)
- [6 Revocation](#6-revocation)
- [7 Compliance](#7-compliance)
- [8 References](#8-references)
  - [8.1 List of Alternative Nomenclatures for Activity types](#81-list-of-alternative-nomenclatures-for-activity-types)

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


* Chapter 2, which describes the attestation attributes and metadata in an
encoding-independent manner.
* Chapter 3, which specifies how the attestation
attributes and metadata are encoded in case the attestation complies with [ISO/IEC
18013-5] and/or [SD-JWT VC] and/or [W3C VCDM v2.0]. Each encoding SHALL be specified in a separate section, or even in a separate chapter.
* Chapter 4, which specifies attestation usage.
* Chapter 5, which defines how trust anchors for attestation verification can be obtained.
* Chapter 6, which defines attestation revocation mechanisms.
* Chapter 7, which provides compliance information.

### 1.3 Key words

This document uses the capitalised key words 'SHALL', 'SHOULD' and 'MAY' as
specified in [RFC 2119], i.e., to indicate requirements, recommendations and
options specified in this document.

In addition, 'must' (non-capitalised) is used to indicate an external
constraint, i.e., a requirement that is not mandated by this document, but, for
instance, by an external document. The word 'can' indicates a capability,
whereas other words, such as 'will', and 'is' or 'are' are intended as
statements of fact.

### 1.4 Terminology

This document uses the terminology specified in Annex 1 of the ARF.

## 2 Attestation attributes and metadata

### Chapter overview and requirements

**Requirements for QEAA**

* An attribute as meant in Annex V point a)  of the [European Digital Identity Regulation]
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
used for verifying the QEAA can be found or looked up (see ARB_20 in [Topic 12]).

**Requirements for PuB-EAA**

* An attribute as meant in  Annex VII point a) of the [European Digital Identity Regulation]
SHALL be included (see ARB_11 in [Topic 12]). See also section 2.1.
* One or more attributes or metadata representing the set of data meant in Annex
 VII point b) of the [European Digital Identity Regulation] SHALL be included (see ARB_14 in [Topic 12]).
* One or more attributes representing the set of data meant in Annex VII point c)
of the [European Digital Identity Regulation] SHALL be included (see ARB_16 in [Topic 12]).
* One or more attributes or metadata representing the set of data meant in Annex VII point e)
of the [European Digital Identity Regulation] SHALL be included (see ARB_18 in [Topic 12]).
* one or more attributes or metadata representing the location meant in Annex VII point h)
of the [European Digital Identity Regulation] SHALL be included. This location SHALL
indicate at least the URL at which a machine-readable version of the qualified
certificate that signed the PuB-EAA can be found or looked up. (see ARB_20 in [Topic 12])


### 2.1 Introduction

The VAT-ID attestation is an attestation provided by an authentic source such as a TAX-Administration. The attestation proves the VAT-ID of the company or administrative unit within the company and the validity period of that VAT-ID. The VAT-ID attestation only contains information directly related to the VAT-ID. 
The VAT-ID attestation can be used by a company to prove that the company really is the company with that number. The receiver of the attestation can trust the content and there is no need for checking the VAT-ID at VIES (VAT Information Exchange System)1 or request a (paper) VAT-ID Certificate. 

*According to Annex V point a) and  Annex VII point a) of the [European Digital Identity Regulation]
an indication, at least in a form suitable for automated processing, that the attestation
has been issued as a QEAA or Pub-EAA SHALL be defined. Similarly, according to ARB_12
of [Topic 12] of Annex 2 of the ARF a similar indication SHOULD be defined for non-qualified EAA.

This document defines the attribute "VAT-ID" which SHALL have
the value "QEAA" or "PuB-EAA".*

````
Administrative unit
├─ vat_id                                  [1]       (name of the administrative unit)
├─ administrative_unit_name                [1]       (name of the administrative unit)
├─ economic_operator                       [1]       (Reference to the Economic Operator that owns the VAT ID)
│   ├─ legal_identifier                    [0]       
│   ├─ legal_name                          [0]       
│   ├─ family_name                         [0]       
│   ├─ given_name                          [0]       
│   ├─ birth_date                          [0]       
│   ├─ birth_place                         [0]       
│   ├─ tin                                 [0]       
│   └─ personal_administrative_number      [0]       
├─ validity_period                         [1..n]    (period(s) for which the vat-id is valid)
│   ├─ start_date                          [1]       (start date of the validity period of the vat-id)
│   └─ end_date                            [0]       (end date of the validity period of the vat-id)
├─ registered_EU_cross_border_transactions [1]       (Boolean that describes if the VAT-ID may be used EU cross border transactions)
├─ adminitrative_unit_type                 [0]       (type of organisation in free text)
├─ administrative_unit_address             [0]       (the postal address registered for the administrative unit)
│   ├─ po_box                              [0]  
│   ├─ thoroughfare                        [0]  
│   ├─ location_designator                 [0]  
│   ├─ post_code                           [0]  
│   ├─ post_name                           [0]  
│   ├─ admin_unit_l1                       [0]  
│   └─ admin_unit_l2                       [0]  
├─ economic_activity_type                  [0..n]    (reference to the economic operator)
│   ├─ economic_activity_type_nomenclature [1]       (nomenclature used to describe the economic activity)
│   ├─ economic_activity_type_id           [1]       (id used in the nomenclature)
│   └─ economic_activity_type_description  [0..n]    (object using language:, value)
├─ issuer                                  [1]   
│   ├─ issuing_country                     [1]
│   ├─ issuing_organisation                [1]        (the organisation that issues the vat-id, this may differ from the attestation issuing organisation)
│   ├─ issuing_date                        [1]        (date on which the attestation is issued)
│   └─ attestation_issuing_organisation    [1]
└─ display                                 [1]       Items to be displayd on the card in the wallet
    ├─ title                               [1]       Name of the card displayed in wallet (VAT-ID)
    ├─ organisation_name                   [1]       legal_name of the organisation that owns the VAT-ID
    ├─ subtitle                            [0]       
    ├─ issuer_logo                         [0]       
    ├─ isuer_name                          [1]       issuing_organisation
    ├─ background_color                    [0]       
    └─ text_color                          [0]       
````

### 2.2 Administrative Unit 
#### 2.2.1 Mandatory attributes
| data identifier                | Semantic Reference                          | Definition                              | Data Type       | Example Value      |
|--------|----------|--------------------------------------------------------------------------|------------|--------------|
| vat_id                         | VAT Identification Number                   | Unique identifier for VAT purposes     | String           | DE123456789        |
| administrative_unit_name       | Name of the Administrative Unit             | Name of the unit responsible for VAT    | String           | Siemens        |
| validity_period                | Period of Validity                          | Duration during which the data is valid| Date Range       | 2026-01-01 to 2026-12-31 |
| economic_operator              | Operator conducting economic activity       | Entity responsible for economic operations | Economic Operator object        | ..|
| issuer                         | Issuing Authority                           | Authority that issues the VAT ID       | Issuer Object           | ..   |



#### 2.2.2 Optional attributes
| **data identifier**  | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|--------|----------|--------------------------------------------------------------------------|------------|--------------|
| administrative_unit_type                | ...                 | Type (e.g., Government, Local Authority, B.V, GmbH)| String | GmbH          |
| administrative_unit_address             | ...                 |  The address where the company is located based on the information from the authentic source of the VAT-ID. This address may differ from the address in the business register.           | Address Object           | ...  |
| economic_activity_type                  | ...                 | Type of business this administrative unit is registered| Economic Activity Type Object | ...     |
| registered_EU_cross_border_transactions | ...                 | Boolean to indicate that the VAT-identification number of the economic operator registered in the European Union for cross border transactions on goods or services   | Boolean            | TRUE |

### 2.3 Economic Operator 
#### 2.3.1 Mandatory attributes
There SHALL be a reference from the Administrative Unit to the Economic Operator. However the the Economic Operator can either be a [Legal Person](https://iri.suomi.fi/terminology/webuild/concept-109) or a [Natural Person](https://iri.suomi.fi/terminology/webuild/concept-6005). The economic operator object SHALL be filled to one of the two, not to both. 

#### 2.3.2 Optional attributes

| **data identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|--------|----------|---------------------------------------------------------------|------------|--------------|
| economic_operator.legal_identifier | [legalIdentifier](https://iri.suomi.fi/terminology/webuild/legalidentifier) |The relevant unique identifier attributed in accordance with Article 9 of EWB (WEBUILD specific EUID where available, otherwise a similar constructed, unique per issuer identifier. <Countrycode ISO 3166-1 alpha-2>. eks. SE +  BOLREG + 123456789 -> SEBOLREG.123456789 | tstr | SEBOLREG.123456789 |
| economic_operator.legal_name | [legalName](https://iri.suomi.fi/terminology/webuild/legalname) | the name under which the legal entity is legally registered | tstr | ACME |
| economic_operator.family_name | [familyName](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#familyName) | Current last name(s) or surname(s) of the user to whom the person identification data relates. | tstr | Doe |
| economic_operator.given_name | [givenName](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#givenName) | Current first name(s), including middle name(s) where applicable, of the user to whom the person identification data relates. | tstr | John |
| economic_operator.birth_date | [dateOfBirth](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#dateOfBirth) | Day, month, and year on which the user to whom the person identification data relates was born. | Date | 1968-04-27 |
| economic_operator.birth_place | [placeOfBirth](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#placeOfBirth) | The country as an alpha-2 country code as specified in ISO 3166-1, or the state, province, district, or local area or the municipality, city, town, or village where the user to whom the person identification data relates was born. | tstr | Amsterdam |
| economic_operator.tin | tin | tax reference number | tstr |  |
| economic_operator. personal_administrative_number | [personalAdministrative Number](https://webuild-consortium.github.io/wp4-semantics-group/ebwv/vocabulary.html#personalAdministrativeNumber) | A value assigned to the natural person that is unique among all personal administrative numbers issued by the provider of person identification data. The personal Administrative Number may only be used if the local law allows for unrestricted use | tstr | 123456782 |

### 2.4 Validity Period
#### 2.4.1 Mandatory attributes
| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|--------|----------|--------------------------------------------------------------------------|------------|--------------|
| validity_period.start_date| [PeriodOfTime.startDate](https://webuild-consortium.github.io/wp4-semantics-group/ebwv/vocabulary.html#startDate) | Date of registration of the VAT-ID. | date |2011-12-24 | 

### 2.4.2 Optional attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|--------|----------|--------------------------------------------------------------------------|------------|--------------|
| validity_period.end_date | [PeriodOfTime.endDate](https://webuild-consortium.github.io/wp4-semantics-group/ebwv/vocabulary.html#endDate) | The end date after which VAT-ID registration ended. | date | 2021-01-24|

### 2.5 Address
#### 2.5.1 Mandatory attributes
No mandatory attributes
#### 2.5.2 Optional attributes
| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|--------|----------|--------------------------------------------------------------------------|------------|--------------|
| address.po_box | [registeredAddress.poBox](https://webuild-consortium.github.io/wp4-semantics-group/ebwv/vocabulary.html#poBox) | P.O. box number or identifier within the address; optional | tstr | PO Box 123 |
| address.thoroughfare | [registeredAddress.thoroughfare](https://sanastot.suomi.fi/en/terminology/webuild/concept/thoroughfare) | Street name and house number or other thoroughfare designation; optional | tstr | Main Street 10 |
| address.location_designator | [registeredAddress.locationDesignator](https://iri.suomi.fi/terminology/webuild/locatordesignator) | Internal location designation within a building (e.g., floor, unit); optional | tstr | Floor 3, Unit B |
| address.post_code | [registeredAddress.postCode](https://iri.suomi.fi/terminology/webuild/postcode) | Postal or ZIP code; optional | tstr | 12345 |
| address.post_name | [registeredAddress.postName](https://iri.suomi.fi/terminology/webuild/postname) | Town or locality name; optional | tstr | Amsterdam |
| address.admin_unit_L1 | [registeredAddress.adminUnitL1](https://iri.suomi.fi/terminology/webuild/adminUnitL1) | First-level administrative division (e.g., province, state); optional | tstr | North Holland |
| address.admin_unit_L2 | [registeredAddress.adminUnitL2](https://iri.suomi.fi/terminology/webuild/adminUnitL2) | Second-level administrative division (e.g., district, municipality); optional | tstr | Amsterdam Municipality

### 2.6 Economic Activity Type attributes
#### 2.6.1 Mandatory attributes

| **data identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|--------|----------|--------------------------------------------------------------------------|------------|--------------|
| economic_activity_type.nomenclature | tbd | The nomenclature that is used to describe the administrative unit. NACE should be used as default. However some countries have more elaborate nomenclature. | tstr | nace |
| economic_activity_type.id | tbd | The ID that under which the Administrative unit is registered. | tstr | C26.5.2 |
| economic_activity_type.description | Economic Activity Description | The human readable text that describes the economic ativity in a specific language. The language is described in BCP 47 standard  | array | en-EN: Manufacture of bearings, gears, gearing and driving elements  |

### 2.7 Metadata
#### 2.7.1 Mandatory metadata 

| **data identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|--------|----------|--------------------------------------------------------------------------|------------|--------------|
| issuer.authentic_source_country | issuing_country | Alpha‑2 country code, as specified in ISO 3166‑2, of the country or territory of the provider of the VAT ID. | date | 05 |
| issuer.vat_id_authenticsource | authenticSource | Name of the administrative authority that issued the VAT ID. This is the authentic source for the VAT-ID, which may differ from the issuer of the attestation| tstr |  |
| issuer.country | issuing_country | Alpha‑2 country code, as specified in ISO 3166‑2, of the country or territory of the provider of the VAT ID. | tstr |  |
| issuer.issuing_authority | issuerAuthority | Name of the administrative authority or qualified trust service provider that issued the VAT ID attestation, in a specific language using  BCP 47 | tstr |  |
| issuer.attestation_legal_category | issuerLegalCategory | The type of attestation category. (Pub-EAA/QEAA) | tstr | PUB-EAA |
| issuer.attestation_issuing_date | iat | The date the attestation was issued | Number (Unix timestamp) | |
| issuer.attestation_expiry_date | exp | The date the attestation was issued | Number (Unix timestamp) | |


#### 2.7.2 Optional metadata

| **Data Identifier** |**Semantic Reference** | **Definition** | **Data type** | **Example value** | 
|--------|----------|--------------------------------------------------------------------------|------------|--------------|
| issuer.location_status      | locationStatus| The location of validity status information on the VAT ID used for revocation/suspension checks.|tstr||
| trust_anchor         | trustAnchor| This meta-data attribute indicates at least the URL at which a machine‑readable version of the trust anchor to be used for verifying the VAT ID can be found or looked up. This corresponds to Annex V/VII point h) of the [European Digital Identity Regulation] and EBW Article 8 issuance as EAA/QEAA.  |tstr||



### 2.8 Display
#### 2.8.1 Mandatory Display items 

| **data identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|--------|----------|--------------------------------------------------------------------------|------------|--------------|
| display.title | title | VAT-ID of the card as shown in the wallet with the label in a specific language using  BCP 47 | String | en-EN: VAT-ID: DE123456789 |
| display.organisation_name| organisation_name | Name of the administrative organisation,SHOULD be the same as economic_operator.organisation_name| tstr |  |
| display.issuing_authority | issuing_authority | The name of the issuing party in a specific language using  BCP 47, should be the same as issuer.issuing_authority | tstr | nl-NL: Belastingdienst |


#### 2.8.2 Optional display items

| **Data Identifier** |**Semantic Reference** | **Definition** | **Data type** | **Example value** | 
|--------|----------|--------------------------------------------------------------------------|------------|--------------|
| display.subtitle | subtitle | Additional reference to a part of the organisation if the organisation has multiple administrative units | tstr |  |
| display.issuer_logo | issuer_logo | Logo of the issuer base64 encoded SVG, PNG or JPG | tstr |  |
| background_color | background_color | Hex-colour voor de background. **formally not part of the Display object** | tstr | |
| text_color | text_color |Hex-colour voor de text **formally not part of the Display object**  | tstr | |

```
  "display": [
    {
      "name": "title",
      "locale": "en-EN",
      "label": "VAT-ID: "
    }
    {
      "name": "title"
      "locale": "nl_NL",
      "label": "BTW-Nummer: "
    }
  ]
```

### 2.9 Code lists


| **field name** | **Allowed values** | **Meaning** | **Source / vocabulary** | **Notes / extensibility** |
|--------|----------|--------------------------------------------------------------------------|------------|--------------|
| economic_activity_type.nomenclature | NACE, NACE-BEL, CZ‑NACE, DB07, WZ, KAD, CNAE, NAF, NKD, ATECO, TEAOR, SBI, ONACE, PKD, CAE, CAEN, SKD, OKEC, TOL, SNI, UK SIC, NOGA | Each name refers to the local adaptation of the NACE list. | [Overview of alternative nomenclatures](#81-list-of-alternative-nace-codes) | List SHOULD be used or refer to NACE closest alternative |

### 2.10 Integrity rules


| **Rule ID** | **Rule statement** | **Why it exists** | **Where enforced** | **Verifier / issuer behavior on failure** |
|-------------|--------------------|-------------------|--------------------|-------------------------------------------|
| EO1 | If 'economic_Operator.legal_identifier' is present, only 'economic_Operator.legal_name', all other variables SHALL be NULL. If 'economic_Operator.legal_identifier' is NULL, 'Tin' OR 'personal_Administrative_Number' OR "Personal Identifiers that can be linked to the PID" SHALL be filled. | There may only be one reference to the holder of the Wallet. If there is more than one, there could be an inconsistancy  | *Issuer, verifier, schema validation, or business process* | *Describe rejection, warning, or remediation behavior* |
| VP1 | If 'validity_Period.end_Date' is not NULL, 'validity_Period.end_Date' SHALL be higher than 'validity_Period.start_Date'| Validity periods may not be negative | The VAT-ID attestation may not be issued, because there shouldn't be a negative period in the register|
| VP2 | If any 'validity_Period' overlaps with another validity period the attestation SHALL NOT be issued| Validity periods may not overlap because this should not happen and might create problems for relying parties. This rule also takes care of the issue of multiple validity periods without an enddate||
| VP3 | If 'validity_Period.end_Date' < issuer.attestation_issuing_date - 5 years| Old validity periods are not relevant to relying parties, the limit of 5 years should be used as a rule of thumb ||
| VP4 | If there is more than one 'validity_Period' the issuer MAY omit older validity_Periods| Issuers have the freedom to omit older validity periods, when they find they are not relevant ||
| EA1 | If ('Economic_Activity_Type.ID' AND 'Economic_Activity_Type.Nomenclature <>"NACE")  is equal ('Economic_Activity_Type.ID' AND 'Economic_Activity_Type.Nomenclature == "NACE") Then 'Economic_Activity_Type.Nomenclature SHOULD be "NACE"| The default Nomenclature is NACE, if the ID in the local Nomenclature directly relates to the NACE ID, the NACE ID and TYPE SHOULD be used. | Issuers SHOULD implement a tranlation table to create mostly NACE codes|
| XB1 | If ('issuing_country' is not in EU Then  'registered_EU_cross_border_transactions' SHOULD be false| Only countries in the EU can take part in the registered_EU_cross_border_transactions|


# 3 Attestation encoding

## 3.1 ISO/IEC 18013-5-compliant encoding

Currently there is no usecase defined where proximity use of the VAT-ID attestation. For now there will be no ISO/IEC 18013-5-compliant encoding.


### 3.2 SD-JWT VC-based encoding

The VAT-ID attestation uses the SD-JWT VC format to allow for selective disclosure of  attributes.

**Verifiable Credential Type (`vct`):** `uri:eu.eudi.vat.1`

#### 3.2.1 Attribute Encoding Table

| **Data Identifier**                | **Attribute identifier**             | **Encoding format**    |**Reference/Notes** |**Disclosable**|
|----------------------------------- |--------------------------------------|------------------------|--------------------|---------------|
| vat_id                             |vat_id | VAT Identification Number    | String                 |                    | MUST NOT|
| administrative_unit_name           |administrative_unit_name              | String                 |                    | MUST NOT|
| validity_period                    |validity_period                       | Array [validity period]|                    | MUST NOT|
| economic_operator                  | economic_operator                    | object                 | ..                 | MUST NOT|
| issuer                             | issuer                               | Object                 | ..                 | MUST NOT|
| administrative_unit_type           | administrative_unit_type             | Object                 | ...                | MUST   |
| administrative_unit_address        | administrative_unit_address          | Object                 | ...                | MUST|
| registered_EU_cross_border_transactions| registered_EU_cross_border_transactions         | Boolean | ..                 | MUST NOT|
| economic_operator.legal_identifier | economic_operator.legal_identifier   | String                 | ..                 | MUST |
| economic_operator.legal_name       | economic_operator.legal_name         | String                 | ..|  MUST |
| economic_operator.family_name      | economic_operator.family_name        | String                 | .. | MUST|
| economic_operator.given_name       | economic_operator.given_name         | String                 | .. |MUST|
| economic_operator.birth_date       | economic_operator.birth_date         | String (ISO 8601 YYYY-MM-DD)| ..| MUST|
| economic_operator.birth_place      | economic_operator.birth_place        | String                 | .. | MUST|
| economic_operator.tin              | economic_operator.tin                | String                 | .. |MUST|
| economic_operator. personal_administrative_number                         | economic_operator. personal_administrative_number |String | .. |MUST|
| validity_period.start_date         | validity_period.start_date        | String (ISO 8601 YYYY-MM-DD)| .. |MUST NOT| 
| validity_period.end_date           | validity_period.end_date          | String (ISO 8601 YYYY-MM-DD)| .. |MUST NOT| 
| address.po_box                     | address.po_box                       | String                 | .. |MUST|
| address.thoroughfare               | address.thoroughfare                 | String                 | .. |MUST|
| address.location_designator        | address.location_designator          | String                 | .. |MUST|
| address.post_code                  | address.post_code                    | String                 | .. |MUST|
| address.post_name                  | address.post_name                    | String                 | .. |MUST|
| address.admin_unit_L1              | address.admin_unit_L1                | String                 | .. |MUST|
| address.admin_unit_L2              | address.admin_unit_L2                | String                 | .. |MUST|
| economic_activity_type             | economic_activity_type            | Array [economic_activity_type]|..|MUST|
| economic_activity_type.nomenclature| economic_activity_type.nomenclature|String one of(NACE, NACE-BEL, CZ‑NACE, DB07, WZ, KAD, CNAE, NAF, NKD, ATECO, TEAOR, SBI, ONACE, PKD, CAE, CAEN, SKD, OKEC, TOL, SNI, UK SIC, NOGA)|..|MUST NOT|
| economic_activity_type.id          | economic_activity_type.id         | String | .. |MUST|
| economic_activity_type.description | economic_activity_type.description |object ("langue code iso 639-1": "description")|..|MUST| 
| issuer.authentic_source_country    | issuer.authentic_source_country      |String (iso 3166-2)|..| MUST NOT 
| issuer.vat_id_authenticsource      | issuer.vat_id_authenticsource        | String | ..| MUST NOT|
| issuer.country                     | issuer.country                       |String | ..| MUST NOT| 
| issuer.issuing_authority           | issuer.issuing_authority             | String | ..| MUST NOT|
| issuer.attestation_legal_category  | issuer.attestation_legal_category    |String | ..| MUST NOT| 
| issuer.location_status             | issuer.location_status               |String (URI)|..|MUST NOT|
| trust_anchor                       | trustAnchor                          | String (URI) |..|MUST NOT|
| issuer.issuance_date               | `iat`                                | Number (Unix timestamp)      | The date and time when the attestation was issued (ISO 8601); RFC 7519 / Section 2.5  | MUST NOT        |
| issuer.expiry_date                   | `exp`                                | Number (Unix timestamp)      | The date and time when the attestation expires (ISO 8601); RFC 7519 / Section 2.5    | MUST NOT        |

**Notes:**

- **MUST**: The claim SHALL be selectively disclosable — the holder MAY choose to disclose or
  withhold this claim when presenting the credential to a Relying Party.
- **MUST NOT**: The claim SHALL NOT be selectively disclosable — it is always present in plain
  text in the JWT header/payload and cannot be withheld by the holder, as it is required for
  credential verification and trust establishment.
- `iat` and `exp` follow RFC 7519 standard JWT claim naming conventions.

#### 3.2.2 Status Claim

For SD-JWT VC-compliant Ownership attestations, the attestation MUST include a `status`
claim if the technical validity period is greater than 24 hours. This claim enables Relying
Parties to determine if a credential has been revoked via a status list mechanism, as specified
in SD-JWT VC.

The `status` claim SHALL be a JSON object with the following members:

- `type` (string): SHALL be `"status-list"`.
- `status_list_credential` (string, URI): The URI of the Status List Credential document that
  contains the status bitstring.
- `status_list_index` (integer, >= 0): The zero-based index into the status list bitstring that
  corresponds to this credential.
- `status_purpose` (string): SHALL be `"revocation"` for this attestation.

Example:

```json
{
  "status": {
 "type": "status-list",
 "status_list_credential": "https://issuer.example.com/status/ownership/2025",
 "status_list_index": 456,
 "status_purpose": "revocation"
  }
}
```

## 4 Attestation usage

### 4.1 Usecases
The VAT_ID attestion aims to be used in two general usecases, but it could be used elsewhere. The first usecae is where the relying party requires proof that the Economic Operator has a valid VAT-ID. In the 'paper' world, the relying party would request a 'Certificate of the VAT-ID' relyably issued by the relevant Tax Authority. The Economic Operator requests the Certificate, and it will be sent to the registered address of the Economic Operator. The Certificate is printed on paper of the Tax Authority and or contains stamps, signature or other ways to proof its validity. 

The second usecase is where a seller needs proof, in case of intra-communitairy business, that the buyer will pay tax in his own country and that it can sell services or goods without TAX. In the current world the seller needs to check with VIES and keep proof in its administration. The VAT-ID attestation will provide the proof, and a check with VIES is not necessary anymore. 

### 4.2 Issuing requirements
The VAT-ID attestation may only be issued to the wallet of the organisation that holds the VAT-ID, or to the wallet of an Agent (natural or legal person) that can prove that he is allowed to act upon the holder for this service. Although many of the information in the attestation is public information, the attestation itself should be considered private. In order to issue the VAT-ID attestation to the Economic Operator itself the issuing party SHOULD: Verify the identity of the Economic Opereator and issue the VAT-ID attestation to the wallet of that Economic Operator. 

If an agent wishes to receive the attestation of another economic operator, the issuing party SHOULD:
* Check the identity of the Agent
    - check if the agent has a mandate with the right scope and actors
      -    the mandate is not revoked
      -    the mandate is currenty valid     


### 4.3 Verification needs
The VAT-ID provides proof that the Economic Operator, registered in the attestation, is the owner of the VAT-ID. It does not prove that the party that presents the attestation also is the owner of the attestation. The VAT-ID attestion can also be issued to an Agent ( Intermediary party), if they have the right mandate to receive the attestation. However the mandate may be revoked by the owner, but the VAT-ID attestation will (likely) not be revoked. Therefore the attestation itself (even if holderbinding is active) is not proof that the presenter actually holds, or may present the attestation. 

The relying party SHOULD:
- Check the status of revocation and expiary date of the attestation.
- Check the validy period in the attestation.

- Check if the Economic Operator in the Attestation is:
   - equal to the owner of the EBW (via EBWOID, PID, or other means) OR
   - has a mandate with the right scope and actors
      -    the mandate is not revoked
      -    the mandate is currenty valid     

If the relying party does not perform all verification aspects, he MUST accept the risks involved. 

The attestation SHALL be non-device-bound. The relying party SHOULD check the ownership of the VAT-ID using the method described above. Device binding might create a false sence of trustworthyness. Because the VAT-ID can be issued to an itermediary organisation, using a mandate, presenting the VAT-ID is no proof of owenership. The VAT-ID attestation will not be revoked by the issuer, when the mandate is revoked. 

## 5 Trust anchors

*Mechanisms for the provision of a trust anchor that SHALL
be used for the verification of an attestation SHALL be defined in this section.*

*It is noted that the ARF specifies the following for QEAAs and Pub-EAAs:*

> To do this for [...] QEAAs the Relying Party Instance uses a trust anchor of
the Provider obtained from a Trusted List. Note that the PID Provider or QEAA
Provider may use an intermediate signing certificate to sign the PID or
attestation, and use the trust anchor to sign the signing certificate, instead
of signing the PID or attestation directly with the trust anchor.
>
> For PuB-EAAs, the Relying Party Instance verifies a PuB-EAA by first
verifying the signature of the PuB-EAA Provider over the PuB-EAA, using the
PuB-EAA Provider certificate issued by a QTSP. Subsequently, the Relying Party
Instance verifies the signature over this certificate, using the corresponding
trust anchor from the QTSP Trusted List. Note that both the PuB-EAA Provider
and the QTSP may use an intermediate signing certificate. All other things
being equal, the verification of a PuB-EAA will therefore involve one or more
extra certificates, compared to the verification of a PID or QEAA.


## 6 Revocation
The VAT-ID Attestation SHOULD preferably be issued as a longlived attestation. In order to make sure the attestation reflects the current situation, the issuer MUST have revocation in place. An issuer must revoke the attestation following an event that would render any part of the content invalid.

When the attestation is issued by a QTSP outside the Authentic Source it should receive information from the authentic source in case attributes of the attestation change at the source. If the QTSP cannot receive this information, the attestation MUST be shortlived. 

## 7 Compliance

*In this section explicitly state how this specific rulebook complies with the
general EUDI framework, ARF, and relevant regulations*

[RULEBOOK AUTHOR TO DEFINE]

## 8 References

| **Item Reference** | **Standard name/details**|
|--------------------|---------------------------|
| [European Digital Identity Regulation] | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework |
| [HAIP] | Yasuda, K. *et al,* OpenID4VC High Assurance Interoperability Profile, OpenId Foundation, Version draft-03 |
| [IANA-JWT-Claims] | IANA JSON Web Token Claims Registry. Available: <https://www.iana.org/assignments/jwt/jwt.xhtml> |
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
| [Topic 20] | ARF Annex 2 - Strong User authentication for electronic payments, Available: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a2320-topic-20-strong-user-authentication-for-electronic-payments>|
| [W3C VCDM v2.0] | Sporny, M. *et al,* Verifiable Credentials Data Model v2.0, W3C Recommendation.  |


### 8.1 List of Alternative Nomenclatures for Activity types

Generated by DUCK.AI using ChatGPT 5.1 mini

| Country | National implementation / name |
|---|---|
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
