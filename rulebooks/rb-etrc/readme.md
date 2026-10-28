| Version | Date | Description |
|---------|------------|------------|
| 0.9 | 02-04-2026 | Copy created from the EUDI attestation rulebook template as the basis for the WE BUILD template. |
| 1.0 | 02-04-2026 | Added WE BUILD v1 author guidance in Sections 1.1 and 2.1 and introduced Sections 2.8 Code lists and 2.9 Integrity rules. |
| 1.1 | 08-04-2026 | Added a Semantic Reference column to Chapter 2 attribute and metadata tables. |

# WE BUILD Attestation Rulebook Template for attestations of type *etrc electronic tax residence certificate*

*This WE BUILD v1 template is derived from the EUDI attestation rulebook template and keeps its
main chapter structure while adding practical author guidance and reusable placeholders.*

*Provide information about the author(s) of this Rulebook in the following form:*

* Author(s):
    * [Pasi Sinervo Finnish Tax Administration]

*Provide versioning information about the Rulebook in the following form:*

| Version | Date | Description |
|---------|------------|------------|
| [VERSION NUMBER] | [PUBLICATION DATE] | [DESCRIPTION OR LINK TO THE CHANGELOG] |
| [VERSION NUMBER] | [PUBLICATION DATE] | [DESCRIPTION OR LINK TO THE CHANGELOG] |

*Provide a contact email address and/or a link to an issue tracking system that can be used for
providing feedback, e.g.:*

**Feedback:**
* [mail the author](pasi.sinervo@vero.fi)

## Table of contents

- [1 Introduction](#1-introduction)
  - [1.1 Document scope and purpose](#11-document-scope-and-purpose)
  - [1.2 Document structure](#12-document-structure)
  - [1.3 Key words](#13-key-words)
  - [1.4 Terminology](#14-terminology)
- [2 Attestation attributes and metadata](#2-attestation-attributes-and-metadata)
  - [Chapter overview and requirements](#chapter-overview-and-requirement]
  - [2.1 Entity](#21-entity)
  - [2.2 Validity period](#22-validity_period)
  - [2.3 Relevant tax treaty](#23 relevantDoubleTaxTreaty)
  - [2.4 person](#24-Person)
  - [2.3 Address](#23-Address)
  - [2.6 Metadata](#27-metadata)
  - [2.7 Code lists](#27-code-lists)
  - [2.8 Integrity rules](#28-integrity-rules)
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


## 1 Introduction

### 1.1 Document scope and purpose

The electronic tax residence certificate (etrc) attestation is an official document issued by a Tax Administration, that verifies the country in which the taxable person is resident for tax purposes. This attestation serves as a proof of the company’s, administrative unit’s or natural paerson's tax liability towards different jurisdictions on tax issues: unlimited or limited tax liability. It contains only information directly related to the etrc. This model is based on the Council directive 2025/50 on faster and safer relief of excess withholdinh taxes. 

The etrc attestation can be utilized by a company to substantiate its identity and ownership of the provided etrc. The recipient of the attestation can trust its authenticity, eliminating the need for external verification if such a process is available.

One of the most important use cases is taxation of the investment revenues from other countries. In order to tax the income correctly the receiver of the income must present the etrc to the payer, the custodian or the tax administration in a refund application. The Council directive 2025/50 seeks to improve this use of the etrc. 

The etrc attestation improves other processes including opening a bank account (We Build PA1 and PA3) and opening an account of a merchant in a platform (BU1).


The etrc attestation seeks to replace the traditional paper-based proof with an attestation. The etrc Attestation is expected to enhance both the efficiency and security of the process. 


### 1.2 Document structure

*Provide a brief overview of the Rulebook's sections and their purpose. The main
sections of the Rulebook SHOULD be*

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

*The following are the recommended keywords. Modify if necessary*

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

The etrc attestation is an attestation provided by an authentic source such as a TAX-Administration. The attestation proves how a taxable person should be taxed in the jurisdiction of the registration and of the RP. It indicates whether the taxable person has unlimiten or limited tax liability in the jurisdiction of the RP. The etrc attestation only contains information directly related to the etrc. 
 
*According to Annex V point a) and  Annex VII point a) of the [European Digital Identity Regulation]
an indication, at least in a form suitable for automated processing, that the attestation
has been issued as a QEAA or Pub-EAA SHALL be defined. Similarly, according to ARB_12
of [Topic 12] of Annex 2 of the ARF a similar indication SHOULD be defined for non-qualified EAA.

This document defines the attribute "etrc" which SHALL have
the value "QEAA" or "PuB-EAA".*

````
etrc
├─ reference number                        [1]       (Number of the document)
├─ entity                                  [1]       (entity that owns the etrc)
│   ├─ name                                [1]    
│   ├─ tax_identification_number           [1]       (tax identification number)
│   └─ tax_identification_number_type      [1]       
├─ natural person                          [1]       (person that owns the etrc)
│   ├─ family_name                         [1]       
│   ├─ given_name                          [1]       
│   ├─ date_of_birth                       [1]       
│   ├─ tax_identification_number           [1]              
│   └─ tax_identification_number_type      [1]       
├─ validity_period                         [1]       (period for which the etrc is valid)
│   ├─ start_date                          [1]       (start date of the validity period of the etrc)
│   ├─ end_date                            [1]       (end date of the validity period of the etrc)
│   ├─ validity_period_type                [1]       (calendar or fiscal year)
│   └─ remark                              [1]       (legal remark)
├─ issuer                                  [1]          
│   ├─ issuing_country                     [1]        
│   ├─ issuing_organisation                [1]        (tax authority)
│   ├─ issuing_date                        [1]        (date on which the attestation is issued)
│   └─ attestation_issuing_organisation    [1]
├─ treaty                                  [1]          
│   ├─ tax_treaty_name                     [1]        (tax treaty name)
│   ├─ tax_treaty_reference                [1]        (article of the treaty)
│   ├─ applicable_member_state             [1]        (jurisdiction of the RP)
│   └─ remark                              [1]
└─ address                                 [0]          
    ├─ po_box                              [0]        
    ├─ thoroughfare                        [0]        
    ├─ location_designator                 [0]       
    ├─ post_code                           [0]       
    ├─ post_name                           [0]       
    ├─ admin_unit_L1                       [0]              
    └─ admin_unit_L2                       [0]       

````






### 2. Attributes

### 2.1 Entity

| data identifier                | Semantic Reference                          | Definition                              | Data Type       | Example Value      |
|--------|----------|--------------------------------------------------------------------------|------------|--------------|
| name  | [legalName](https://w3id.org/ebwv#legalName) | Name of the entity     | String           | Siemens AG        |
| tax_identification_number       | [identifier](https://w3id.org/ebwv#identifier)   | tax identification number    | String           | 012345678-9        |
| tax_identification_number_type                | Semantics: Needs property in separate "Identifier" class, but unclear if this is going to be introduced <br> type of identifier                          | class type | string       | legalIdentifier |


### 2.2 Validity Period

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|--------|----------|--------------------------------------------------------------------------|------------|--------------|
| validity_period.start_date| [coveragePeriod](http://w3id.org/ebwv#coveragePeriod).[PeriodOfTime](http://w3id.org/ebwv#PeriodOfTime).[startDate](https://w3id.org/ebwv#startDate) | Date of registration of the VAT-ID. | date |2011-12-24 | 
| validity_period.end_date | [coveragePeriod](http://w3id.org/ebwv#coveragePeriod).[PeriodOfTime](http://w3id.org/ebwv#PeriodOfTime).[endDate](https://w3id.org/ebwv#endDate) | The end date after which VAT-ID registration ended. | date | 2021-01-24|
| validity_period_type               | Additional property needed in "PeriodOfTime" class? <br> covered period                | fiscal or calendar year | String | fiscal year          |
| remark            | Either reuse of [qualificationNote](http://w3id.org/ebwv#qualificationNote) <br> or a separate "remark" property? |  Legal remark           | Legal remark           | ...  |


### 2.3 Relevant Double Tax Treaty 

| data identifier                | Semantic Reference                          | Definition                              | Data Type       | Example Value      |
|--------|----------|--------------------------------------------------------------------------|------------|--------------|
| tax_treaty_name                        | [legalInstrument](https://w3id.org/ebwv#legalInstrument).[dct:title](http://purl.org/dc/terms/title)<br>The tax treaty is the "instrument", and this string is its title > see https://verdragenbank.overheid.nl/en/Treaty/Details/006833 <br> relevantDoubleTaxTreaty                  | Double Tax Treaty    | String        | Netherlands and Finland       |
| tax_treaty_reference      | [legalProvision](https://w3id.org/ebwv#legalProvision).[dct:identifier](http://purl.org/dc/terms/identifier) <br>Assumes an article/paragraph reference as in the example; purpose of request is a different fact. <br> additionalInformation             | for which purposes is requested    | String           | article 10 dividends      |
| applicable_member_state       |  [LegalContext](https://w3id.org/ebwv#LegalContext).[applicableJurisdiction](https://w3id.org/ebwv#applicableJurisdiction) <br> Demands the introduction of a separate "LegalContext" class<br>theAuthoritiesOf                        | States where treaty is apllied  | String       | Netherlands and Finland |
| remark          |        | legal remark | string        | ..|


#### 2.4 Person

| **data identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|--------|----------|---------------------------------------------------------------|------------|--------------|
| family_name | [familyName](https://w3id.org/ebwv#familyName) | Current last name(s) or surname(s) of the user to whom the person identification data relates. | tstr | Doe |
| person.given_name | [givenName](https://w3id.org/ebwv#givenName) | Current first name(s), including middle name(s) where applicable, of the user to whom the person identification data relates. | tstr | John |
| person.birth_date | [dateOfBirth](https://w3id.org/ebwv#dateOfBirth) | Day, month, and year on which the user to whom the person identification data relates was born. | Date | 1968-04-27 |
| economic_operator.birth_place | [placeOfBirth](https://w3id.org/ebwv#placeOfBirth) | The country as an alpha-2 country code as specified in ISO 3166-1, or the state, province, district, or local area or the municipality, city, town, or village where the user to whom the person identification data relates was born. | tstr | Amsterdam |
| person.tin | [identifier](https://w3id.org/ebwv#identifier) OR <br> [hasIdentifier].[Identifier] if we introduce a adms:Identifier type of class in EBWV | tax reference number | tstr |  |
| tax_identification_number_type. | No solution yet in EBWV, but Identifier class could solve this <br> type if number | tax identification number | tstr | 123456782 |


### 2.5 Address optional

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|--------|----------|--------------------------------------------------------------------------|------------|--------------|
| address.po_box | [registeredAddress](https://w3id.org/ebwv#registeredAddress).[poBox](https://w3id.org/ebwv#poBox) | P.O. box number or identifier within the address; optional | tstr | PO Box 123 |
| address.thoroughfare | [registeredAddress](https://w3id.org/ebwv#registeredAddress).[thoroughfare](https://w3id.org/ebwv#thoroughfare) | Street name and house number or other thoroughfare designation; optional | tstr | Main Street 10 |
| address.location_designator | [registeredAddress](https://w3id.org/ebwv#registeredAddress).[locatorDesignator](https://w3id.org/ebwv#locatorDesignator) | Internal location designation within a building (e.g., floor, unit); optional | tstr | Floor 3, Unit B |
| address.post_code | [registeredAddress](https://w3id.org/ebwv#registeredAddress).[postCode](https://w3id.org/ebwv#postCode) | Postal or ZIP code; optional | tstr | 12345 |
| address.post_name | [registeredAddress](https://w3id.org/ebwv#registeredAddress).[postName](https://w3id.org/ebwv#postName) | Town or locality name; optional | tstr | Amsterdam |
| address.admin_unit_L1 | [registeredAddress](https://w3id.org/ebwv#registeredAddress).[adminUnitL1](https://w3id.org/ebwv#adminUnitL1) | First-level administrative division (e.g., province, state); optional | tstr | North Holland |
| address.admin_unit_L2 | [registeredAddress](https://w3id.org/ebwv#registeredAddress).[adminUnitL2](https://w3id.org/ebwv#adminUnitL2) | Second-level administrative division (e.g., district, municipality); optional | tstr | Amsterdam Municipality

### 2.6 Mandatory metadata
#### 2.6.1 Mandatory metadata 

| **data identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|--------|----------|--------------------------------------------------------------------------|------------|--------------|
| issuer.authentic_source_country | No solution for this yet in Semantics <br>issuing_country | Alpha‑2 country code, as specified in ISO 3166‑2, of the country or territory of the provider of the etrc. | date | 05 |
| issuer.etrc_authenticsource | No solution for this yet in Semantics <br> authenticSource | Name of the administrative authority that issued the etrc. This is the authentic source for the etrc, which may differ from the issuer of the attestation| tstr |  |
| issuer.country | issuing_country | No solution for this yet in Semantics <br> Alpha‑2 country code, as specified in ISO 3166‑2, of the country or territory of the provider of the etrc. | tstr |  |
| issuer.issuing_authority | [cred:issuer] <br> issuerAuthority | Name of the administrative authority or qualified trust service provider that issued the etrc attestation, in a specific language using  BCP 47 | tstr |  |
| issuer.attestation_legal_category | [attestationLegalCategory](https://w3id.org/ebwv#attestationLegalCategory) <br> issuerLegalCategory | The type of attestation category. (Pub-EAA/QEAA) | tstr | PUB-EAA |
| issuer.attestation_issuing_date | [cred:validFrom] <br> iat | The date the attestation was issued | Number (Unix timestamp) | |
| issuer.attestation_expiry_date | [cred:validUntil] <br> exp | The date the attestation was issued | Number (Unix timestamp) | |


#### 2.6.2 Optional metadata

| **Data Identifier** |**Semantic Reference** | **Definition** | **Data type** | **Example value** | 
|--------|----------|--------------------------------------------------------------------------|------------|--------------|
| issuer.location_status      | No solution for this yet in Semantics <br>locationStatus| The location of validity status information on the VAT ID used for revocation/suspension checks.|tstr||
| trust_anchor         | [cred:termsOfUse] <br> trustAnchor| This meta-data attribute indicates at least the URL at which a machine‑readable version of the trust anchor to be used for verifying the etrc can be found or looked up. This corresponds to Annex V/VII point h) of the [European Digital Identity Regulation] and EBW Article 8 issuance as EAA/QEAA.  |tstr||



### 2.7 Code lists

*Use this section for controlled vocabularies, enumerations, value sets, or external catalogues
that are necessary to interpret one or more attributes or metadata items. Definitions may be reused
from the attestation description or other use-case documentation and refined here where needed.*

*For each code list, authors SHOULD state the field to which it applies, the allowed values, their
meaning, the source vocabulary or reference, and any extensibility rule or governance note.*

| **Field name** | **Allowed values** | **Meaning** | **Source / vocabulary** | **Notes / extensibility** |
|----------------|--------------------|-------------|--------------------------|---------------------------|
| *Provide a field name* | *List the allowed values* | *Explain what each value means* | *Reference the source* | *State whether extensions are allowed* |

> Example
>
> | **Field name** | **Allowed values** | **Meaning** | **Source / vocabulary** | **Notes / extensibility** |
> |----------------|--------------------|-------------|--------------------------|---------------------------|
> | `signatory_rule` | `sole`, `joint` | Indicates whether the representative may bind the organisation alone or only together with one or more additional representatives | EUCC attestation description / WE BUILD company representation model | Additional values SHOULD only be introduced if they are defined consistently across issuer and verifier implementations |

### 2.8 Integrity rules


| **Rule ID** | **Rule statement** | **Why it exists** | **Where enforced** | **Verifier / issuer behavior on failure** |
|-------------|--------------------|-------------------|--------------------|-------------------------------------------|
| EO1 | If 'economic_Operator.legal_identifier' is present, only 'economic_Operator.legal_name', all other variables SHALL be NULL. If 'economic_Operator.legal_identifier' is NULL, 'Tin' OR 'personal_Administrative_Number' OR "Personal Identifiers that can be linked to the PID" SHALL be filled. | There may only be one reference to the holder of the Wallet. If there is more than one, there could be an inconsistancy  | *Issuer, verifier, schema validation, or business process* | *Describe rejection, warning, or remediation behavior* |
| VP1 | validity_Period.end_Date' <= 'issuer.issuance_date' | Validity period ends at issuance date | The etrc may not be given for the future|
| VP2 | 'validity_period.start_date' >= previous year's first date || == tax year's start date ; 

using namespace std::chrono;   const auto today = floor<days>(system_clock::now());
    const year_month_day ymd{today};
    const year_month_day start_prev_year{
        (ymd.year() - years{1}) / January / 1
    }; | Validity periods can start from the 1st day of the previous calendar or tax year|


| **Rule ID** | **Rule statement** | **Why it exists** | **Where enforced** | **Verifier / issuer behavior on failure** |
|-------------|--------------------|-------------------|--------------------|-------------------------------------------|
| *Provide a rule identifier* | *State the rule precisely* | *Explain the rationale* | *Issuer, verifier, schema validation, or business process* | *Describe rejection, warning, or remediation behavior* |

> Example
>
> | **Rule ID** | **Rule statement** | **Why it exists** | **Where enforced** | **Verifier / issuer behavior on failure** |
> |-------------|--------------------|-------------------|--------------------|-------------------------------------------|
> | `IR-01` | If `legal_representative.natural_person` is present, `full_name` and `date_of_birth` SHALL be present. If `legal_representative.legal_person` is present, `name`, `id`, and `legal_form_type` SHALL be present. | Prevents incomplete representation statements and ensures that a relying party can determine whether the representative is a natural person or a legal person and validate the representation data accordingly. | Issuer business rules, schema validation, and verifier business validation. | Issuer SHALL reject incomplete representative data; verifier SHALL treat the representation information as invalid or insufficient for the transaction. |

# 3 Attestation encoding

## 3.1 ISO/IEC 18013-5-compliant encoding

*If the attestation type supports the the format specified in ISO/IEC 18013-5,
then in this section the  ISO/IEC 18013-5-compliant encoding of attributes and metadata
should be defined.*

*It is noted that (see ARB_02 in [Topic 12]) the Schema Provider SHALL analyse whether it must
be possible for a User to present that type of attestation when the Wallet Unit
and the Relying Party are in proximity and attestations are presented without
using the internet. If so,the attestations must be issued in the ISO/IEC 18013-5-compliant
mdoc format.*

*Furthermore, in this section a document type SHALL be defined, which SHALL be
unique within the scope of the EUDI Wallet ecosystem (see ARB_05 in [Topic 12]).*

[RULEBOOK AUTHOR TO DEFINE THE ATTESTATION TYPE]

*Provide a list of available encoding formats and their specifications (e.g., encoding, maximum lengths,
date formats, etc). For example:*

* tstr, uint, bstr, bool and tdate are CDDL representation types defined in
  [RFC 8610].
    * Regarding type tstr: this document confirms that, as specified in [RFC
    8949], a tstr SHALL be encoded in UTF-8 and SHALL support the full Unicode
    range.
    * All attributes having encoding type tstr SHALL have a maximum length of
    150 characters.
    * This document specifies full-date as full-date = #6.1004(tstr), where tag
    1004 is specified in [RFC 8943].
    * In accordance with [RFC 8949], section 3.4.1, a tdate attribute SHALL
    contain a date-time string as specified in [RFC 3339]. In accordance with
    [RFC 8943], a full-date attribute SHALL contain a full-date string as
    specified in [RFC 3339].
    * The following requirements apply to the representation of dates in
    attributes, unless otherwise indicated:
        * Fractions of seconds SHALL NOT be used;
        * A local offset from UTC SHALL NOT be used; the time-offset defined in
        [RFC 3339] SHALL be to "Z".
    * [RFC 8949], section 4.2, describes four rules for canonical CBOR. Three of
    those rules SHALL be implemented for all CBOR structures, as
    follows:
        * integers (major types 0 and 1) SHALL be as small as possible;
        * the expression of the length in a bstr, tstr, array or map SHALL be as
        short as possible;
        * indefinite-length items SHALL be made into definite-length items.

*This section should include a table the data identifier specified in
Chapter 2,  the corresponding attribute identifier to be used in
presentation requests and responses according to [ISO/IEC 18013-5] and the encoding
of each attribute.*

*Additionally, the following rules should be followed:*

* When specifying new attributes, existing conventions
for attribute identifier values and attribute syntaxes SHOULD
be considered (see ARB_07 in [Topic 12]).
* Each attribute SHALL be defined within an attribute namespace.
    * An attribute namespace
SHALL fully define the identifier, the syntax, and the semantics of each attribute
within that namespace.
    * An attribute namespace SHALL have an identifier that is
unique within the scope of the EUDI Wallet ecosystem, and each attribute
identifier SHALL be unique within that namespace (see ARB_06a in [Topic 12])
    * A domestic namespace MAY defined
to specify attributes that are specific to this Rulebook and are not included in
the applicable EU-wide or sectoral namespace (see ARB_10 in [Topic 12]).

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Namespace**|
|------------------------|--------------|------------------|------------------|
| family_name | family_name | tstr | com.example.att.1|

*The corresponding entry for the "attestation_legal_category" attribute defined
in Section 2.1 SHALL be:*

| **Data Identifier** | **Attribute identifier** | **Encoding format** |**Namespace**|
|------------------------|--------------|------------------|------------------|
| attestation_legal_category | attestation_legal_category | tstr |com.example.att.1|

Finally, illustrative examples SHALL be included.

[RULEBOOK AUTHOR TO PROVIDE AN EXAMPLE OF FULL OR PARTIAL mDOC OF THE ATTESTATION]

[RULEBOOK AUTHOR TO PROVIDE THE ATTRIBUTES AND THEIR VALUES INCLUDED IN THE EXAMPLE]

### 3.2 SD-JWT VC-based encoding
#### 3.2.1 Attribute Encoding Table
| **Data Identifier**                | **Attribute identifier**             | **Encoding format**    |**Reference/Notes** |**Disclosable**|
|----------------------------------- |--------------------------------------|------------------------|--------------------|---------------|
| entity.name              |legal.name |  String            |   name of an entity                   | MUST NOT|
| entity.tax_identification_number           |tax_identification_number              | String                 |                    | MUST NOT|
| validity_period                    |validity_period                       | Array [validity period]|                    | MUST NOT|
| entity                  | economic_operator                    | Object                 | ..                 | MUST NOT|
| issuer                             | issuer                               | Object                 | ..                 | MUST NOT|
| treaty           | tax treaty             | Object                 | ...                | MUST NOT   |
| person        | natural person          | Object                 | ...                | MUST NOT|
| address| address         | Object | ..                 | MUST |
| entity.legal_identifier | entity.legal_identifier   | String                 | ..                 | MUST NOT |
| entity.legal_name       | entity.legal_name         | String                 | ..|  MUST NOT |
| person.family_name      | person.family_name        | String                 | .. | MUST NOT|
| person.given_name       | person.given_name         | String                 | .. |MUST NOT|
| person.birth_date       | person.birth_date         | String (ISO 8601 YYYY-MM-DD)| ..| MUST NOT|
| treaty.tax_treaty_name      | relevantDoubleTaxTreaty        | String                 | .. | MUST NOT|
| treaty.tax_treaty_reference              | additionalInformation                | String                 | .. |MUST NOT|
| person.tax_identification_number                         | person.tin |String | .. |MUST|
| validity_period.start_date         | validity_period.start_date        | String (ISO 8601 YYYY-MM-DD)| .. |MUST NOT| 
| validity_period.end_date           | validity_period.end_date          | String (ISO 8601 YYYY-MM-DD)| .. |MUST NOT| 
| address.po_box                     | address.po_box                       | String                 | .. |MUST|
| address.thoroughfare               | address.thoroughfare                 | String                 | .. |MUST|
| address.location_designator        | address.location_designator          | String                 | .. |MUST|
| address.post_code                  | address.post_code                    | String                 | .. |MUST|
| address.post_name                  | address.post_name                    | String                 | .. |MUST|
| address.admin_unit_L1              | address.admin_unit_L1                | String                 | .. |MUST|
| address.admin_unit_L2              | address.admin_unit_L2                | String                 | .. |MUST|
| issuer.authentic_source_country    | issuer.authentic_source_country      |String (iso 3166-2)|..| MUST NOT 
| issuer.etrc_authenticsource      | issuer.etrc_authenticsource        | String | ..| MUST NOT|
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




### 3.3 W3C Verifiable Credentials Data Model-based encoding

*If the attestation type supports the the format specified in W3C Verifiable Credentials
Data Model, then in this section the  corresponding encoding  of attributes and
metadata should be defined.*

*It is noted that only a a non-qualified EAA can use this format (see ARB_01a in [Topic 12])*

*Tables similar to the ones specified in section 4 SHALL be defined.*

*This section SHALL reference one or more documents specifying in detail how a
Relying Party can request attributes from a such an attestation, and how a User
can selectively disclose attributes from such an attestation. Moreover, these
referenced documents SHALL be approved by an EU standardisation body or by the European
Digital Identity Cooperation Group established pursuant to Article 46e(1) of the
[European Digital Identity Regulation] (see ARB_04 in [Topic 12]).*

*Finally, illustrative examples SHALL be included.*

[RULEBOOK AUTHOR TO PROVIDE HUMAN READABLE EXAMPLE OF THE ISSUED ATTESTATION]

[RULEBOOK AUTHOR TO PROVIDE AN EXAMPLE OF THE PROOF TYPE]

## 4 Attestation usage

### 4.1 Usecases
The etrc attestion aims to be used in two general usecases, but it could be used elsewhere. The first usecae is where the relying party requires proof that the taxable person is resident for tax issues in some country. This helps the RP to determine whether this taxable person has unlimited or limited tax responsibility in the country of RP. In the 'paper' world, the relying party would request a 'Tax Residence or Tax Domicile Certificate' relyably issued by the relevant Tax Authority, and in some cases notarized and shared through Apostille. The taxable person requests the Certificate, and it will be sent to the registered address of the taxable person or downloaded from a portal. The Certificate is printed on paper (or pdf) of the Tax Authority and or contains stamps, signature or other ways to proof its validity. If required, the certificate is notarized before sharing to the RP.

The second usecase is where a taxable person wants to open an account in a bank. The bank needs for its' KYC procedure a proof of the taxable person's residency for taxation: use cases We Build PA1 and PA3. 

### 4.2 Issuing requirements
The etrc attestation may only be issued to the wallet of the organisation that holds the etrc, or to the wallet of an Agent (natural or legal person) that can prove that he is allowed to act upon the holder for this service. The attestation should be considered private. In order to issue the etrc attestation to the Economic Operator itself the issuing party SHOULD: Verify the identity of the Economic Opereator and issue the etrc attestation to the wallet of that Economic Operator. 

If an agent wishes to receive the attestation of another economic operator, the issuing party SHOULD:
* Check the identity of the Agent
    - check if the agent has a mandate with the right scope and actors
      -    the mandate is not revoked
      -    the mandate is currenty valid     


### 4.3 Verification needs
The etrc provides a proof that the Economic Operator or natural person, registered in the attestation, is the owner of the etrc. It does not prove that the party that presents the attestation also is the owner of the attestation. The etrc attestion can also be issued to an Agent ( Intermediary party including financial institutions or custodians), if they have the right mandate to receive the attestation. However the mandate may be revoked by the owner, but the etrc attestation will (likely) not be revoked. Therefore the attestation itself (even if holderbinding is active) is not proof that the presenter actually holds, or may present the attestation. 

The relying party SHOULD:
- Check the status of revocation and expiary date of the attestation.
- Check the validy period in the attestation.

- Check if the Economic Operator in the Attestation is:
   - equal to the owner of the EBW (via EBWOID, PID, or other means) OR
   - has a mandate with the right scope and actors
      -    the mandate is not revoked
      -    the mandate is currenty valid     

If the relying party does not perform all verification aspects, he MUST accept the risks involved. 

The attestation SHALL be non-device-bound. The relying party SHOULD check the ownership of the etrc using the method described above. Device binding might create a false sence of trustworthyness. Because the etrc can be issued to an itermediary organisation, using a mandate, presenting the etrc is no proof of owenership. The etrc attestation will not be revoked by the issuer, when the mandate is revoked. 

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
The etrc Attestation SHOULD preferably be issued as a longlived attestation. In order to make sure the attestation reflects the current situation, the issuer MUST have revocation in place. An issuer must revoke the attestation following an event that would render any part of the content invalid.

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




 |
