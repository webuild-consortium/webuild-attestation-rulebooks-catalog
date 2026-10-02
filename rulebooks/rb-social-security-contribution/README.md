# Attestation Rulebook for attestations of type Social Security Contribution

Category: non-qualified EAA

* Author(s):
    * [Bruno Salinier, Orange Business]
    
* Previous Authors
    
*Provide versioning information about the Rulebook in the following form:*


* Contact:
    * bruno.salinier@orange.com

**Feedback:**

| Version | Date | Description |
| --- | --- | --- |
| 1.1 | 2026-10-02 | Restructured onto the generic WE BUILD attestation rulebook template (11 chapters). No normative content removed. |

**Written against:** ARF version 3.0.0, WE BUILD template version 1.0 (generic)

**Feedback:** [GitHub issues](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/issues)

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
- [6 Protocols](#6-protocols)
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
- [10 Trust Framework](#10-trust-framework)
- [11 References](#11-references)


## 1 Introduction

### 1.1 Document scope and purpose

The SocialSecurityContribution (SSC for short) attestation allows a Customer to verify that their Supplier fullfills their legal obligation regarding social declarations and payment of social contributions. 

The SSC attestation is issued by public bodies to employers to certify that they have fulfilled their social reporting obligations for their establishments.

The primary purpose of this attestation is to provide proof that the employer has submitted the necessary social declarations and paid the corresponding contributions and contributions related to social security, family allowances, unemployment insurance, and wage guarantee fund contributions. It is intended for use in administrative or legal contexts to verify compliance with social security obligations. For example, the provision by suppliers of such an attestation is required by national law in some EU Countries when signing a contract and on a regular basis thereafter.

This attestation is therefore essential for Customers as Relying Parties to get the SSC attestation from their Suppliers as Holders in the Know Your Supplier (KYS) process. 

The main source for the design of the SSC attestation is the French "attestation de vigilance" issued by URSSAF in accordance to Article L243-15 of the social security code in France.

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

This document uses the terminology specified in Annex 1 of the ARF. In addition, the terminology below is used in this document.

> < TODO >

## 2 Compliance

### 2.1 Compliance statement

This Rulebook complies with the applicable requirements of Topic 12, Attestation
Rulebooks, in Annex 2 of the Architecture and Reference Framework, version 3.0.0. It
uses the terminology of Annex 1 of the ARF.

*In this section explicitly state how this specific rulebook complies with the
general EUDI framework, ARF, and relevant regulations*

[RULEBOOK AUTHOR TO DEFINE]

### 2.2 Regulatory basis

This attestation is not a qualified electronic attestation of attributes. The data
described in Annex V points b, c and e of Regulation (EU) 2024/1183 is addressed as
required by EW-DM-12-018 and as recommended by EW-DM-12-020 and EW-DM-12-022. Where a
recommendation is not followed, the reason is stated below.

### 2.3 Traceability

Every applicable requirement mapped to the section that satisfies it. Requirements
marked not applicable carry a stated reason.

| Requirement | Legacy ID | Applies | Satisfied in section | Note |
| --- | --- | --- | --- | --- |
| EW-DM-12-001 | ARB_01a | yes | 5 | W3C VCDM permitted for this category; no encoding defined in this version |
| EW-DM-12-002 | ARB_01b | yes | 5 | SD-JWT VC following the HAIP profile |
| EW-DM-12-003 | ARB_02 | no |  | Proximity presentation is not in scope |
| EW-DM-12-005 | ARB_04 | no |  | No W3C VCDM encoding is defined in this version |
| EW-DM-12-006 | ARB_05 | yes | 5 | Unique vct for this attestation type |
| EW-DM-12-007 | ARB_06 | yes | 3 | Attributes defined independently of encoding |
| EW-DM-12-008 | ARB_06a | no |  | No mdoc encoding is defined in this version |
| EW-DM-12-009 | ARB_06b | yes | 5 | SD-JWT VC claim naming |
| EW-DM-12-010 | ARB_07 | yes | 3 | Attributes reused from the catalogued vocabulary where one exists |
| EW-DM-12-012 | ARB_09 | yes | 3, 4 | Mandatory, optional and conditional stated per attribute |
| EW-DM-12-013 | ARB_10 | no |  | No domestic namespace is defined |
| EW-DM-12-014 | ARB_11 | no |  | Annex V and VII point a apply to QEAA and PuB-EAA |
| EW-DM-12-015 | ARB_12 | yes | 4.1 | EAA indication for a non-qualified EAA |
| EW-DM-12-016 / EW-DM-12-017 / EW-DM-12-018 | ARB_13 / ARB_14 / ARB_15 | yes | 2.2, 4.1 | Point b, EW-DM-12-018 for the non-qualified case |
| EW-DM-12-019 / EW-DM-12-020 | ARB_16 / ARB_17 | yes | 2.2 | Point c, recommendation for non-qualified EAA |
| EW-DM-12-021 / EW-DM-12-022 | ARB_18 / ARB_19 | yes | 2.2, 4.2 | Point e, recommendation for non-qualified EAA |
| EW-DM-12-023 / EW-DM-12-024 | ARB_20 / ARB_21 | yes | 4.2, 10 | Trust anchor location and the trust framework |
| EW-DM-12-029 | ARB_25 | yes | 4.1 | Legal category attribute; see the note in section 4.1 |
| EW-DM-12-030 | ARB_26 | yes | 10 | Trust anchor publication for non-qualified EAA |
| EW-DM-12-031 | ARB_27 | no |  | This attestation does not require the Relying Party to verify a PID |
| EW-DM-12-032 | ARB_28 | no |  | cryptographically_bound_to is not used by this attestation |
| EW-DM-12-034 | ARB_30 | yes | 5 | Selective disclosure stated per claim |
| EW-DM-12-035 | ARB_31 | no |  | No Claim Selective Disclosure Metadata document is used |
| EW-DM-12-038 | ARB_34 | yes | 7.1 | Device binding |

## 3 Attestation attributes

Attributes are defined here in an encoding-independent manner (EW-DM-12-007). The
encoding of each attribute is given in chapter 5.

### 3.1 Introduction

The SocialSecurityContribution attestation provides a standardized representation of the declaration and status of a company in regard to its social contributions.

The attestation structure is defined as a structured object:

**Data Model:**
````
SocialSecurityContribution
├─ liableEmployer (M)
│   └──legalName (M)
│   └──legalIdentifier (M)
├─ legalBasis (M)
├─ coveredObligationType (M)
├─ complianceStatus (M)
├─ validAsOfDate (M)
├─ reportingPeriod (C)
├─ averagePeriodWorkforce (O)
├─ totalPayroll (O)
├─ hasSite [1..n] (O)
│   └── siteIdentifier (M)
│   └── registeredAddress (M)
├─ coverageStatement (O)
└─ qualificationNote (O)

````
Note: M - Mandatory O - Optional C - Conditional

**Explanation:**

- `liableEmployer` identifies the employer whose obligations are certified and is an object **SHALL** appear exactly once and contains:
  - `legalName`, the legal name of the employer.
  - `legalIdentifier`, the official identifier of the employer.

- `legalBasis` is the legal provision or framework under which the attestation is issued.
- `coveredObligationType` is the type of social security, employment-related contribution, reporting, or payment obligation covered.
- `complianceStatus` is the assessed status of the employer’s fulfilment of the covered obligations.
- `validAsOfDate` is the date on which the facts or status were assessed.
- `reportingPeriod` is the period to which the declarations, payroll, workforce, or other reported data relate.
- `averagePeriodWorkforce` is the average number of employed persons for the reporting period.
- `totalPayroll` is the total gross payroll, wage sum, or declared remuneration for the reporting period.
- The `hasSite` object **MAY** appear at most once and **SHALL** contains at least one `Site` object defined by its `siteIdentifier` and `registeredAddress` and representing a site, establishment, local unit, branch, workplace, or comparable operational location covered by the attestation.
- `coverageStatement` provides a human-readable statement describing the establishments, sites, obligations, regimes, or reporting scope covered by the attestation.
-  `qualificationNote` provides a caveat, limitation, condition, or explanatory note that qualifies the interpretation of the attestation. 

**Attestation Classification:**

This attestation type MAY be classified as:

- **`QEAA`** when issued by a qualified trust service provider (QTSP) or authorised competent
  body (e.g. a social security agency).
- **`Pub-EAA`** when issued by a member state institution (To be verified).

#### 1 Introduction

### 3.2 Mandatory attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| liableEmployer | [employer](https://w3id.org/ebwv#employer) | Identifies the employer whose obligations are certified | Object |  |
| liableEmployer.legalName | [legalName](https://w3id.org/ebwv#legalName) | Official legal name of the employer | String | Orange Business Services SA |
| liableEmployer.legalIdentifier | [legalIdentifier](https://w3id.org/ebwv#legalIdentifier) | Legal identifier of the employer <Can be MS specific or EU-wide (VATID)> | String | 345039416 |
| legalBasis | [legalBasis](https://w3id.org/ebwv#legalBasis) | Legal provision or framework under which the attestation is issued | String | Article L243-15 du Code de la sécurité sociale |
| coveredObligationType | [coveredObligationType](https://w3id.org/ebwv#coveredObligationType) | Type of social security, employment-related contribution, reporting, or payment obligation covered | Array of Strings | ["familyAllowanceContribution", "employmentDeclarationObligation"] |
| complianceStatus | [complianceStatus](https://w3id.org/ebwv#complianceStatus) | Assessed status of the employer’s fulfilment of the covered obligations | String | upToDate |
| validAsOfDate | TBD <br> is this a cred: property? | Date on which the facts or status were assessed | Date (YYYY-MM-DD) | 2026-07-01 |

 **Possible `coveredObligationType` values:**

| Value | Meaning |
| --- | --- |
| `socialSecurityContribution` | Social security contribution obligations. |
| `familyAllowanceContribution` | Family allowance-related contributions. |
| `unemploymentInsuranceContribution` | Unemployment insurance contributions. |
| `wageGuaranteeFundContribution` | Wage guarantee fund contributions. |
| `employmentDeclarationObligation` | Obligations to submit employment-related declarations. |
| `agriculturalSocialContribution` | Agricultural-sector social contribution obligations. |
| `selfEmployedSocialContribution` | Self-employed worker contribution obligations. |
| `otherEmploymentRelatedContribution` | Other employment-related contribution obligations. |

**Possible `complianceStatus` values:**

| Value | Meaning |
| --- | --- |
| `upToDate` | The employer is assessed as up to date with the covered obligations. |
| `notUpToDate` | The employer is not assessed as up to date. |
| `compliantUnderPaymentPlan` | The employer is treated as compliant because an accepted payment plan exists. |
| `disputedAmount` | The status is affected by a disputed contribution amount. |
| `notApplicable` | The obligation is not applicable to the employer or period. |
| `unknown` | The status cannot be determined from the attestation data. |

### 3.3 Optional attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| averagePeriodWorkforce | [averagePeriodWorkforce](https://w3id.org/ebwv#averagePeriodWorkforce) | Average number of employed persons for the reporting period. Implies reportingPeriod to be present. | String | 2365 |
| totalPayroll | [totalPayroll](https://w3id.org/ebwv#totalPayroll) | Total payroll, wage sum, or declared remuneration for the reporting period. Implies reportingPeriod to be present. | String | 129350000.00 EUR |
| hasSite | [hasSite](https://w3id.org/ebwv#hasSite) | A site, establishment, local unit, branch, workplace, or comparable operational location | Object |  |
| hasSite.siteIdentifier | [identifier](https://w3id.org/ebwv#identifier) | identifier of the site, may be referenced in business register in some MS | String | 34503941600012 |
| hasSite.registeredAddress | [hasAddress](https://w3id.org/ebwv#hasAddress)<br>OR<br>[registeredAddress](https://w3id.org/ebwv#registeredAddress) <br> the latter can be used only if the Site is considered a legal entity (registered organisation) according to national legislation | Adress of the site | String | 1 Place des Droits de l'Homme, 93200 Saint-Denis, France |
| coverageStatement | [coverageStatement](https://w3id.org/ebwv#coverageStatement) | A human-readable statement describing the establishments, sites, obligations, regimes, or reporting scope covered by the attestation | String | This attestation covers the liable employer and the establishments declared to the issuing authority for the reporting period. Where obligations are handled centrally, the attestation applies within the scope of that centralised reporting arrangement. |
| qualificationNote | [qualificationNote](https://w3id.org/ebwv#qualificationNote) | A human-readable note about caveat, limitation, condition that qualifies the interpretation of the attestation. | String | The attestation confirms the status recorded by the issuing authority for the covered obligations at the valid-as-of date. It does not replace any separate attestation required for obligations outside the stated scope or outside the issuing jurisdiction |

### 3.4 Conditional attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| reportingPeriod | [reportingPeriod](https://w3id.org/ebwv#reportingPeriod) | Period to which declarations, payroll, workforce, or other reported data relate. Mandatory when averagePeriodWorkforce or totalPayroll are reported. | Object |  |
| reportingPeriod.startDate | [reportingPeriod](https://w3id.org/ebwv#reportingPeriod).[startDate](https://w3id.org/ebwv#startDate) | Starting date of the reporting Period | Date (YYYY-MM-DD) | 2026-06-01 |
| reportingPeriod.endDate | [reportingPeriod](https://w3id.org/ebwv#reportingPeriod).[startDate](https://w3id.org/ebwv#endDate) | Ending date of the reporting Period | Date (YYYY-MM-DD) | 2026-06-30 |

## 4 Metadata

Metadata describes the attestation rather than its subject.

### 4.1 Mandatory metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| *Provide a value* | *Provide a value or N/A* | *Provide succinct text* | *Provide a value* | *Provide a value* |

**Legal category.** This Rulebook retains the `attestation_legal_category` attribute.
Section 4.1 of the generic template replaces it with the `category` attribute of
[ETSI TS 119 472-1], whose value for this category is `eaa:eu:non-qualified`.
EW-DM-12-029, legacy ARB_25, of ARF version 3.0.0 is a SHALL that still requires
`attestation_legal_category`, so the template and the ARF disagree. The attribute is
left as written and the deviation is recorded for the rulebook quality assurance group.

### 4.2 Optional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| *Provide a value* | *Provide a value or N/A* | *Provide succinct text* | *Provide a value* | *Provide a value* |

### 4.3 Conditional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
| --- | --- | --- | --- | --- |
| *Provide a value* | *Provide a value or N/A* | *Provide succinct text* | *Provide a value* | *Provide a value* |

### 4.4 Code lists

*Use this section for controlled vocabularies, enumerations, value sets, or external catalogues
that are necessary to interpret one or more attributes or metadata items. Definitions may be reused
from the attestation description or other use-case documentation and refined here where needed.*

*For each code list, authors SHOULD state the field to which it applies, the allowed values, their
meaning, the source vocabulary or reference, and any extensibility rule or governance note.*

| **Field name** | **Allowed values** | **Meaning** | **Source / vocabulary** | **Notes / extensibility** |
| --- | --- | --- | --- | --- |
| *Provide a field name* | *List the allowed values* | *Explain what each value means* | *Reference the source* | *State whether extensions are allowed* |

> Example
>
> | **Field name** | **Allowed values** | **Meaning** | **Source / vocabulary** | **Notes / extensibility** |
> |----------------|--------------------|-------------|--------------------------|---------------------------|
> | `signatory_rule` | `sole`, `joint` | Indicates whether the representative may bind the organisation alone or only together with one or more additional representatives | EUCC attestation description / WE BUILD company representation model | Additional values SHOULD only be introduced if they are defined consistently across issuer and verifier implementations |

### 4.5 Integrity rules

*Use this section to define integrity or consistency rules that are not fully captured by the
encoding format or schema alone, such as cross-field dependencies, temporal consistency checks,
mutual exclusivity, or conditional combinations of values.*

*Integrity rules may be copied and refined from an attestation description, logical model, or
business-rule specification where available.*

| **Rule ID** | **Rule statement** | **Why it exists** | **Where enforced** | **Verifier / issuer behavior on failure** |
| --- | --- | --- | --- | --- |
| *Provide a rule identifier* | *State the rule precisely* | *Explain the rationale* | *Issuer, verifier, schema validation, or business process* | *Describe rejection, warning, or remediation behavior* |

> Example
>
> | **Rule ID** | **Rule statement** | **Why it exists** | **Where enforced** | **Verifier / issuer behavior on failure** |
> |-------------|--------------------|-------------------|--------------------|-------------------------------------------|
> | `IR-01` | If `legal_representative.natural_person` is present, `full_name` and `date_of_birth` SHALL be present. If `legal_representative.legal_person` is present, `name`, `id`, and `legal_form_type` SHALL be present. | Prevents incomplete representation statements and ensures that a relying party can determine whether the representative is a natural person or a legal person and validate the representation data accordingly. | Issuer business rules, schema validation, and verifier business validation. | Issuer SHALL reject incomplete representative data; verifier SHALL treat the representation information as invalid or insufficient for the transaction. |


## 5 Formats


### 5.1 SD-JWT VC-based encoding

*If the attestation type supports the format specified in "SD-JWT-based Verifiable
Credentials (SD-JWT VC)", then in this section the SD-JWT VC-compliant encoding
of attributes and metadata SHALL be defined. It SHALL be ensured that the attestations
comply with the 'SD-JWT VCs' profile specified in [HAIP] (see ARB_01b in [Topic 12]).*

*It is noted that a Schema Provider MAY specify in the Attestation
Rulebook that that type of attestation must be issued in the [SD-JWT VC]-compliant
format, provided the [SD-JWT VC] specification has been approved by an EU standardisation
body or by the European Digital Identity Cooperation Group established pursuant to
Article 46e(1) of the [European Digital Identity Regulation] (see ARB_03 in [Topic 12]).*

*In this section, a Verifiable Credential Type (`vct`) SHALL be defined,
which SHALL be unique within the scope of the EUDI Wallet ecosystem (see ARB_05 in [Topic 12]).*

[RULEBOOK AUTHOR TO DEFINE THE ATTESTATION TYPE]

*Additionally, when specifying new attributes, existing conventions
for attribute identifier values and attribute syntaxes SHOULD
be considered (see ARB_07 in [Topic 12]).*

*Rulebook authors SHALL ensure that each claim name is either

* included in the IANA registry for JWT claims,
* is a Public Name as defined in [RFC 7519], or
* or is a Private Name specific to the attestation type. (see ARB_06b in [Topic 12]).*

*For all claims (i.e., all top-level properties, all nested properties, and all array entries),
the Rulebook SHALL specify whether an Attestation Provider MUST, MAY, or MUST NOT make that
claim selectively disclosable (see ARB_30 in [Topic 12]).*

*Rulebook authors SHOULD consider defining a Type Metadata Document for the attestation type
specified in the Rulebook, as defined in Chapter 6 of [SD-JWT VC]. If such a document is defined,
it SHOULD contain the Claim Selective Disclosure Metadata (defined in Section 9.3 of [SD-JWT VC])
for each of the claims, in order to specify if that claim is selectively disclosable (see ARB_31
in [Topic 12]).*

*IANA-registered claims should be presented in table that
includes their data identifier, attribute identifier,
encoding format, and reference or note. For example,*

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Reference/Notes** | **Disclosable** |
| --- | --- | --- | --- | --- |
| family_name | family_name | string | Section 5.1 of [OIDC] | MUST |

*A similar table should be used for Public Names and for Private Names specific
to the attestation type defined in this document. For
example:*

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Notes** | **Disclosable** |
| --- | --- | --- | --- | --- |
| trust_anchor | trust_anchor | string | The trust anchor defined in Section 5 | MUST NOT |

*The corresponding entry for the "attestation_legal_category" attribute defined
in Section 2.1 SHALL be:*

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Notes** | **Disclosable** |
| --- | --- | --- | --- | --- |
| attestation_legal_category | attestation_legal_category | string | Defined in Attestation Rulebook template | MUST NOT |

Finally, illustrative examples SHALL be included.

[RULEBOOK AUTHOR TO PROVIDE AN EXAMPLE OF THE JWT CLAIM SET USED BY THE PROVIDER]

[RULEBOOK AUTHOR TO PROVIDE AN EXAMPLE OF THE ISSUED SD-JWT (IN base64 ENCODING)]

[RULEBOOK AUTHOR TO PROVIDE AN EXAMPLE OF A HUMAN READABLE VERSION OF THE SD-JWT PAYLOAD
AND A DESCRIPTION OF THE DISCLOSURES INCLUDED IN THE EXAMPLE]

### 5.2 ISO/IEC 18013-5-compliant encoding

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

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Namespace** |
| --- | --- | --- | --- |
| family_name | family_name | tstr | com.example.att.1 |

*The corresponding entry for the "attestation_legal_category" attribute defined
in Section 2.1 SHALL be:*

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Namespace** |
| --- | --- | --- | --- |
| attestation_legal_category | attestation_legal_category | tstr | com.example.att.1 |

Finally, illustrative examples SHALL be included.

[RULEBOOK AUTHOR TO PROVIDE AN EXAMPLE OF FULL OR PARTIAL mDOC OF THE ATTESTATION]

[RULEBOOK AUTHOR TO PROVIDE THE ATTRIBUTES AND THEIR VALUES INCLUDED IN THE EXAMPLE]

#### 3.2 SD-JWT VC-based encoding

*If the attestation type supports the format specified in "SD-JWT-based Verifiable
Credentials (SD-JWT VC)", then in this section the SD-JWT VC-compliant encoding
of attributes and metadata SHALL be defined. It SHALL be ensured that the attestations
comply with the 'SD-JWT VCs' profile specified in [HAIP] (see ARB_01b in [Topic 12]).*

*It is noted that a Schema Provider MAY specify in the Attestation
Rulebook that that type of attestation must be issued in the [SD-JWT VC]-compliant
format, provided the [SD-JWT VC] specification has been approved by an EU standardisation
body or by the European Digital Identity Cooperation Group established pursuant to
Article 46e(1) of the [European Digital Identity Regulation] (see ARB_03 in [Topic 12]).*

*In this section, a Verifiable Credential Type (`vct`) SHALL be defined,
which SHALL be unique within the scope of the EUDI Wallet ecosystem (see ARB_05 in [Topic 12]).*

[RULEBOOK AUTHOR TO DEFINE THE ATTESTATION TYPE]

*Additionally, when specifying new attributes, existing conventions
for attribute identifier values and attribute syntaxes SHOULD
be considered (see ARB_07 in [Topic 12]).*

*Rulebook authors SHALL ensure that each claim name is either

* included in the IANA registry for JWT claims,
* is a Public Name as defined in [RFC 7519], or
* or is a Private Name specific to the attestation type. (see ARB_06b in [Topic 12]).*

*For all claims (i.e., all top-level properties, all nested properties, and all array entries),
the Rulebook SHALL specify whether an Attestation Provider MUST, MAY, or MUST NOT make that
claim selectively disclosable (see ARB_30 in [Topic 12]).*

*Rulebook authors SHOULD consider defining a Type Metadata Document for the attestation type
specified in the Rulebook, as defined in Chapter 6 of [SD-JWT VC]. If such a document is defined,
it SHOULD contain the Claim Selective Disclosure Metadata (defined in Section 9.3 of [SD-JWT VC])
for each of the claims, in order to specify if that claim is selectively disclosable (see ARB_31
in [Topic 12]).*

*IANA-registered claims should be presented in table that
includes their data identifier, attribute identifier,
encoding format, and reference or note. For example,*

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Reference/Notes** | **Disclosable** |
| --- | --- | --- | --- | --- |
| family_name | family_name | string | Section 5.1 of [OIDC] | MUST |

*A similar table should be used for Public Names and for Private Names specific
to the attestation type defined in this document. For
example:*

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Notes** | **Disclosable** |
| --- | --- | --- | --- | --- |
| trust_anchor | trust_anchor | string | The trust anchor defined in Section 5 | MUST NOT |

*The corresponding entry for the "attestation_legal_category" attribute defined
in Section 2.1 SHALL be:*

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Notes** | **Disclosable** |
| --- | --- | --- | --- | --- |
| attestation_legal_category | attestation_legal_category | string | Defined in Attestation Rulebook template | MUST NOT |

Finally, illustrative examples SHALL be included.

[RULEBOOK AUTHOR TO PROVIDE AN EXAMPLE OF THE JWT CLAIM SET USED BY THE PROVIDER]

[RULEBOOK AUTHOR TO PROVIDE AN EXAMPLE OF THE ISSUED SD-JWT (IN base64 ENCODING)]

[RULEBOOK AUTHOR TO PROVIDE AN EXAMPLE OF A HUMAN READABLE VERSION OF THE SD-JWT PAYLOAD
AND A DESCRIPTION OF THE DISCLOSURES INCLUDED IN THE EXAMPLE]

#### 3.3 W3C Verifiable Credentials Data Model-based encoding

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

### 5.3 W3C Verifiable Credentials Data Model-based encoding

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

## 6 Protocols

This attestation is issued using OpenID for Verifiable Credential Issuance
[OpenID4VCI] and presented using OpenID for Verifiable Presentations [OpenID4VP], both
as profiled by [HAIP].

## 7 Issuance

### 7.1 Binding

| Field | Value | Source |
| --- | --- | --- |
| Device-bound | MAY | EW-DM-12-038 |
| Cryptographically bound to | none | EW-DM-12-032 |
| Relying Party must also verify a PID | no | EW-DM-12-031 |
| Binding subject | legal person |  |

### 7.2 Issuance Policy

*Briefly describe the primary use cases or scenarios for which this attestation
type is intended*

*Additionally, in this section it SHOULD  be specified whether a Relying Party receiving the attestation
must request and verify a PID (see ARB_27 in [Topic 12]). Also beyond PID verification,
it SHOULD be defined what other key obligations does a Relying Party have when processing
this attestation type (e.g., signature verification, freshness checks)*

*Furthermore, provide potential presentation requirements, e.g., are there specific
requirements for how this attestation must be presented (e.g., online, offline, specific protocols)?"*

*Specify whether an attestation of this type SHALL or SHOULD be device-bound or non-device-bound, see ARB_34 in [Topic 12]*

*If an attestation of this type is device-bound, specify if it SHALL, SHOULD or MAY be cryptographically bound to another type of attestation on the same Wallet Unit. If needed (based on this decision), include the attribute `cryptographically_bound_to` defined in ARB_28 as an optional, recommended, or mandatory attribure in [Section 2.5](#26-optional-metadata). If present in an Attestation Rulebook, the identifier for this attribute SHALL be "cryptographically_bound_to" for both ISO/IEC 18013-5 and SD-JWT VC-compliant attestations, and its contents SHALL be a `tstr` or `string` (as applicable) containing an attestation type or vct (see ARB_05). Finally, specify the value of the `tstr` or `string`.* 

*EXAMPLE   In case an attestation type of this type must be bound to a PID, the value of the `tstr` or `string` must be set to "eu.europa.ec.eudi.pid.1" or "urn:eudi:pid:1". Note that it does not matter whether the attestation type or the vct value is used.*

*Finally, in this section information about potential transactional data
SHALL be defined; see [Topic 20] of Annex 2 of the ARF.*


### 7.3 Lifecycle management

The issuer sets the validity period of the attestation and reissues it when the
underlying facts change, revoking the superseded attestation as described in chapter 8.

### 7.4 Embedded disclosure policy

This attestation defines no embedded disclosure policy.

## 8 Revocation

(Refer to [Topic 7] of the ARF for a list of High-Level Requirements related to Revocation)

*In this section information about the revocation mechanism used SHALL be defined.*

*For PID, QEAA, or PuB-EAA it SHALL  be defined whether  only short-lived attestations
will be used, having a validity period of 24 hours or less, such that revocation
will never be necessary, or that the attestations are revocable.*

*For revocable attestations it SHALL be defined which of the following methods must be implemented:*

* Use an Attestation Status List mechanism included in a Technical Specification
that will be specified by the Commission.
* Use an Attestation Revocation List mechanism included in a Technical Specification
that will be specified by the Commission.

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


### 9.2 Presentation modes

Remote presentation is in scope. Proximity presentation is in scope only where
chapter 5 records an mdoc encoding.

### 9.3 Transactional data

This Rulebook defines no transactional data.

## 10 Trust Framework

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

*For non-qualified EAA in this section it SHOULD  be defined (see ARB_26 in [Topic 12])
how the attributes or metadata representing the location at which a machine-readable
version of the trust anchor to be used for verifying the attestation can be found,
specified in section 2, are used. This includes a detailed description about how
a Relying Party can obtain the trust anchors, as well as a detailed description about
how this trust anchor can be used for verifying that the provider is authorized
to issue the attestation. Additionally, for non-qualified EAA Providers this section
MAY include a description of mechanisms that can be used by a Wallet Unit for
verifying that the provider is authorized to issue this type of attestation (see
ISSU_34 in [Topic 10])*

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
