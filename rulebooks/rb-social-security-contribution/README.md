
# WE BUILD Attestation Rulebook for attestations of type Social Security Contribution

* Author(s):
    * [Bruno Salinier, Orange Business]
    
* Previous Authors
    
*Provide versioning information about the Rulebook in the following form:*

| Version | Date | Description |
|---------|------------|------------|
| 0.1 | 30/06/2026 | Initial draft based on SSC attestation description |

* Contact:
    * bruno.salinier@orange.com

**Feedback:**

## 1 Introduction

### 1.1 Document scope and purpose

The SocialSecurityContribution (SSC for short) attestation allows a Customer to verify that their Supplier fullfills their legal obligation regarding social declarations and payment of social contributions. 

The SSC attestation is issued by public bodies to employers to certify that they have fulfilled their social reporting obligations for their establishments.

The primary purpose of this attestation is to provide proof that the employer has submitted the necessary social declarations and paid the corresponding contributions and contributions related to social security, family allowances, unemployment insurance, and wage guarantee fund contributions. It is intended for use in administrative or legal contexts to verify compliance with social security obligations. For example, the provision by suppliers of such an attestation is required by national law in some EU Countries when signing a contract and on a regular basis thereafter.

This attestation is therefore essential for Customers as Relying Parties to get the SSC attestation from their Suppliers as Holders in the Know Your Supplier (KYS) process. 

The main source for the design of the SSC attestation is the French "attestation de vigilance" issued by URSSAF in accordance to Article L243-15 of the social security code in France.

### 1.2 Document structure

The rulebook is structured as follows:

* Chapter 2 describes the attestation attributes and metadata in an encoding-independent manner,
* Chapter 3 specifies how the attestation,
attributes and metadata are encoded following [SD-JWT VC],
* Chapter 4 specifies attestation usage,
* Chapter 5 defines how trust anchors for attestation verification can be obtained,
* Chapter 6 defines attestation revocation mechanisms,
* Chapter 7 provides compliance information.

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

This document uses the terminology specified in Annex 1 of the ARF. In addition, the terminology below is used in this document.

> < TODO >


## 2 Attestation attributes and metadata

The SocialSecurityContribution attestation provides a standardized representation of the declaration and status of a company in regard to its social contributions.

### 2.1 Introduction

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
  - `legalName` — the legal name of the employer.
  - `legalIdentifier` — the official identifier of the employer.

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

### 2.2 Mandatory attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------|--------------|--------------|--------------|
| liableEmployer |  | Identifies the employer whose obligations are certified | Object |  |
| liableEmployer.legalName | | Official legal name of the employer | String | Orange Business Services SA |
| liableEmployer.legalIdentifier | | Legal identifier of the employer <Can be MS specific or EU-wide (VATID)> | String | 345039416 |
| legalBasis |  | Legal provision or framework under which the attestation is issued | String | Article L243-15 du Code de la sécurité sociale |
| coveredObligationType  |  | Type of social security, employment-related contribution, reporting, or payment obligation covered | Array of Strings | ["familyAllowanceContribution", "employmentDeclarationObligation"] |
| complianceStatus |  | Assessed status of the employer’s fulfilment of the covered obligations | String | upToDate |
| validAsOfDate |  | Date on which the facts or status were assessed | Date (YYYY-MM-DD) | 2026-07-01 |

 **Possible `coveredObligationType` values:**

| Value | Meaning |
|---|---|
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
|---|---|
| `upToDate` | The employer is assessed as up to date with the covered obligations. |
| `notUpToDate` | The employer is not assessed as up to date. |
| `compliantUnderPaymentPlan` | The employer is treated as compliant because an accepted payment plan exists. |
| `disputedAmount` | The status is affected by a disputed contribution amount. |
| `notApplicable` | The obligation is not applicable to the employer or period. |
| `unknown` | The status cannot be determined from the attestation data. |

### 2.3 Optional attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------|--------------|--------------|--------------|
| averagePeriodWorkforce |  | Average number of employed persons for the reporting period. Implies reportingPeriod to be present.  | String | 2365 |
| totalPayroll |  | Total payroll, wage sum, or declared remuneration for the reporting period. Implies reportingPeriod to be present.  | String | 129350000.00 EUR |
| hasSite |  | A site, establishment, local unit, branch, workplace, or comparable operational location | Object |  |
| hasSite.siteIdentifier |  | identifier of the site, may be referenced in business register in some MS | String | 34503941600012 |
| hasSite.registeredAddress | Address | Adress of the site | String | 1 Place des Droits de l'Homme, 93200 Saint-Denis, France |
| coverageStatement |  | A human-readable statement describing the establishments, sites, obligations, regimes, or reporting scope covered by the attestation | String | This attestation covers the liable employer and the establishments declared to the issuing authority for the reporting period. Where obligations are handled centrally, the attestation applies within the scope of that centralised reporting arrangement. |
| qualificationNote |  | A human-readable note about caveat, limitation, condition that qualifies the interpretation of the attestation. | String | The attestation confirms the status recorded by the issuing authority for the covered obligations at the valid-as-of date. It does not replace any separate attestation required for obligations outside the stated scope or outside the issuing jurisdiction |

### 2.4 Conditional attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------|--------------|--------------|--------------|
| reportingPeriod |  | Period to which declarations, payroll, workforce, or other reported data relate. Mandatory when averagePeriodWorkforce or totalPayroll are reported. | Object |  |
| reportingPeriod.startDate |  | Starting date of the reporting Period | Date (YYYY-MM-DD) | 2026-06-01 |
| reportingPeriod.endDate |  | Ending date of the reporting Period | Date (YYYY-MM-DD) | 2026-06-30 |

### 2.5 Mandatory metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------|--------------|--------------|--------------|
| *Provide a value* | *Provide a value or N/A* | *Provide succinct text* | *Provide a value* | *Provide a value* |

### 2.6 Optional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------|--------------|--------------|--------------|
| *Provide a value* | *Provide a value or N/A* | *Provide succinct text* | *Provide a value* | *Provide a value* |

### 2.7 Conditional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------|--------------|--------------|--------------|
| *Provide a value* | *Provide a value or N/A* | *Provide succinct text* | *Provide a value* | *Provide a value* |

### 2.8 Code lists

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

### 2.9 Integrity rules

*Use this section to define integrity or consistency rules that are not fully captured by the
encoding format or schema alone, such as cross-field dependencies, temporal consistency checks,
mutual exclusivity, or conditional combinations of values.*

*Integrity rules may be copied and refined from an attestation description, logical model, or
business-rule specification where available.*

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

| **Data Identifier** | **Attribute identifier** | **Encoding format** |**Reference/Notes** |**Disclosable**|
|-------------------- |--------------------------|---------------------|--------------------|---------------|
| family_name | family_name | string | Section 5.1 of [OIDC] | MUST |

*A similar table should be used for Public Names and for Private Names specific
to the attestation type defined in this document. For
example:*

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Notes** |**Disclosable**|
|---------------------|--------------------------|---------------------|-----------|---------------|
| trust_anchor | trust_anchor | string | The trust anchor defined in Section 5 | MUST NOT |

*The corresponding entry for the "attestation_legal_category" attribute defined
in Section 2.1 SHALL be:*

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Notes** |**Disclosable**|
|---------------------|--------------------------|---------------------|-----------|---------------|
| attestation_legal_category | attestation_legal_category | string | Defined in Attestation Rulebook template |MUST NOT|

Finally, illustrative examples SHALL be included.

[RULEBOOK AUTHOR TO PROVIDE AN EXAMPLE OF THE JWT CLAIM SET USED BY THE PROVIDER]

[RULEBOOK AUTHOR TO PROVIDE AN EXAMPLE OF THE ISSUED SD-JWT (IN base64 ENCODING)]

[RULEBOOK AUTHOR TO PROVIDE AN EXAMPLE OF A HUMAN READABLE VERSION OF THE SD-JWT PAYLOAD
AND A DESCRIPTION OF THE DISCLOSURES INCLUDED IN THE EXAMPLE]

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

## 6 Revocation

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
