* Template version: 1.1, 20-08-2025


# Attestation Rulebook for attestations of type Ultimate Beneficial Owner(s) List (UBO-List)*

*Provide information about the author(s) of this Rulebook in the following form:*

* Author(s): 
    * [Florin Coptil, Robert Bosch GmbH]
    * [...., Deutsche Bank]
* Previous Authors


*Provide versioning information about the Rulebook in the following form:*

| Version | Date       | Description                                                     |
|---------|------------|-----------------------------------------------------------------|
| 0.1     | 13.03.2026 | Initial draft based on the WeBuild design attestations mettings |

*Provide a contact email address and/or a link to an issue tracking system that can be used for
providing feedback, e.g.:* 

**Feedback:**
  *  https://example.com/tracker 

## 1 Introduction

### 1.1 Document scope and purpose

This document is the Ultimate Beneficial Owner Attestation Data Rulebook (referred to as UBO) based on
- The Proposal for the Implementing Act dated 26/11/2025, concerning the “formats for submitting beneficial ownership information”
- Regulation (EU) 2024/1624 of the European Parliament and of the Council of 31 May 2024, on the prevention of the use of the financial system for the purposes of money laundering or terrorist financing
the EU Company Law regulation.

It contains the specific requirements, issuance process, formatting and content of the UBO. This document is created and used by the WEBUILD consortium to provide a common understanding, data schema, format and usage guidlines for the WEBUILD eco system.

This document MAY be used as one of multiple inputs toward a final UBO definition for the EBW ecosystem but that is up so the sole decisision of the EU commission or any other relevant authority with delgated power from the commission.

### 1.2 Document structure
- Chapter 2, Attestation attributes and metadata in an encoding-independent manner.
- Chapter 3, Attestation attributes for the specific encodings [SD-JWT VC] and [W3C VCDM v2.0].
- Chapter 4, Attestation usage.
- Chapter 5, Trust anchors
- Chapter 6, Revocation mechanisms
- Chapter 7, Compliance information

### 1.3 Keywords

This document uses the capitalised keywords 'SHALL', 'SHOULD' and 'MAY' as
specified in [RFC 2119], i.e. to indicate requirements, recommendations and
options specified in this document.

In addition, 'must' (non-capitalised) is used to indicate an external
constraint, i.e. a requirement that is not mandated by this document, but, for
instance, by an external document. The word 'can' indicates a capability,
whereas other words, such as 'will', and 'is' or 'are' are intended as
statements of fact.

### 1.4 Terminology

*It is recommended to use the terminology defined in Annex 1 of ARF. For example,
the following text can be used.* 

This document uses the terminology specified in Annex 1 of the ARF.

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

### 2.1 Introduction


UBO-List (Ultimate Beneficial Owner(s) List)

| **Data Identifier**     | **Definition**                                                      |
|-------------------------|---------------------------------------------------------------------|
| ubo_info                | Information about the beneficial owner(s)                           |
| ubo_residential_address | Information about the residential address of the beneficial owner(s)| 
| ubo_identification      | Information about the identification of the beneficial owner(s)     |
| ubo_stake               | Information about the stake information of the beneficial owner(s)  |

### 2.2 UBO

| **Data Identifier** | **Definition**                                                                                                                                                                                            | Required |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| first name(s)      | Current last name(s) or surname(s) of the beneficial owne                                                                                                                                                   | Yes      | 
| surname(s)       | Current first name(s), including middle name(s) where applicable, of the beneficial owner                                                                                                                   | Yes      |
| birth_date       | The name of a passage or way through from one location to another.                                                                                                                                          | Yes      |
| birth_place      | The country as an alpha-3 country code as specified in ISO 3166-3, or the state, province, district, or local area or the municipality, city, town, or village where the beneficial ownerrelates was born.  | Yes      |
| nationality vs citizenship | A number or sequence that uniquely identifies the locator.                                                                                                                                         | Yes      |

### 2.3 UBO_Residential_Address

| **Data Identifier**       | **Definition**                                                           | Required | Type                          |
|---------------------------|--------------------------------------------------------------------------|----------|-------------------------------|
| residential_street	       | The street where the UBO currently resides or can be contacted           | 	Yes	    | String                        |
| residential_house_number	 | The street number  where the UBO currently resides or can be contacted   | 	Yes     | 	String                       |
| residential_city	         | The city  where the UBO currently resides or can be contacted	           | Yes      | String                        |
| residential_state         | 	The state where the UBO currently resides or can be contacted	          | Yes	     | String                        |
| residential_postal_code 	 | The postal code where the UBO currently resides or can be contacted	     | Yes      | String                        |
| country of residence	     | The country() where the UBO currently resides or can be contacted	       | Yes      | 	Array [ ISO-3166-1 alpha-3]  |

### 2.4 UBO_Identification

| **Data Identifier** | **Definition**                                                                                                                                                                                                              | Required |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
|type of identity document	| A value defining the type of the identity document according to the nationality of the UBO (not the country of the authentic source !) (ex. Passport number / National identity card number / Driver license…) 	            | Yes      |
|identity document number| 	This is the number of identity document, such as passport or national identity document A value assigned to the natural person that is unique among all personal administrative numbers issued by the official government. | 	Yes     |
|identity issuing country| 	The country that issued the identity document (use ISO 3166‑1 alpha‑3 code)	                                                                                                                                               | Yes      |
|identity expiryDate	| The expiration date of the identity document	                                                                                                                                                                               | Yes      |
|unique personal identification number| 	A government-assigned number uniquely linked to the individual, independent of any specific ID document, and valid for the person’s lifetime                                                                               | No       |
|identity revocation link	| The revocation link for identity in case that the unique personal identification is specified                                                                                                                               | 	No      |


### 2.5 UBO_Stake

| **Data Identifier**       | **Definition**                                                                                                                  | Required | Type | 
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------|----------|----|
| determination_methodolog  | Specifies the calculation methodology applied in accordance with the applicable register requirement  (See Codes Section 1.4.2) | 	Yes     |	string|
| ownership_stake	          | The percentage or level of ownership                                                                                            | Yes	     |Percentage|
| ownership_held_date	      | date of which beneficial interest is held                                                                                       | Yes      |	ISO 8601 (YYYY-MM-DD)|


### 2.3 Optional attributes

| **Data Identifier** | **Definition**          | **Data type**     | **Example value** |
|---------------------|-------------------------|-------------------|-------------------|
| *Provide a value*   | *Provide succinct text* | *Provide a value* | *Provide a value* |

### 2.4 Conditional attributes

| **Data Identifier** | **Definition**          | **Data type**     | **Example value** |
|---------------------|-------------------------|-------------------|-------------------|
| *Provide a value*   | *Provide succinct text* | *Provide a value* | *Provide a value* |

### 2.5 Residential address

### 2.5 Mandatory metadata 

| **Data Identifier** | **Definition**          | **Data type**     | **Example value** |
|---------------------|-------------------------|-------------------|-------------------|
| *Provide a value*   | *Provide succinct text* | *Provide a value* | *Provide a value* |

# 3 Attestation encoding 

## 3.1 ISO/IEC 18013-5-compliant encoding 
ISO/IEC 18013-5 (also called mdoc) is out of scope for this rulebook, as offline proximity presentation is not a current requirement for UBO.

### 3.2 SD-JWT VC-based encoding 
The UBO attestation uses the SD-JWT VC format to allow for selective disclosure of company attributes. Selective Disclosure: Claims of UBO SHALL NOT be selectively disclosable to preserve the legally mandated content of the UBO.

The . notation is used to indicate the nesting of attributes.

| **Data Identifier**                                    | **Attribute identifier**                                                                                                                                                                                                    | **Encoding format** | **Reference/Notes**                                                                                                                                                                                                        |
|--------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ubo                                                    	| ubo                                             	        |Array 	|List of beneficial owners|
| ubo_first name(s)                                      	| ubo_first name(s)                                      	|String	|the beneficial owner’s first names in full;|
| ubo_surname(s)                                         	| ubo_surname(s)                                         	|String	|beneficial owner’s surnames in full;|
| ubo_date of birth                                      	| ubo_date of birth                                      	|String	|Day, month, and year of birth of natural person|
| ubo_citizenship(s)                                     	| ubo_citizenship(s)                                     	||Array	|Citizenship(s) held by the UBO.|
| ubo_birthplace                                         	| ubo_birthplace                                         	|String||
| ubo_birthplace_locality                                	| ubo_birthplace_locality                                	|String	|locality where the natural person was born.|
| ubo_birthplace_country                                 	| ubo_birthplace_country                                 	|String	|Country where the natural person was born.|
| ubo_residential_address                                	| ubo_residential_address                                	|Object||
| ubo_residential_address_street                         	| ubo_residential_address_street                         	|String	|The street where the UBO currently resides or can be contacted|
| ubo_residential_address_house_number	                   | ubo_residential_address_house_number	                    |String	|The street number where the UBO currently resides or can be contacted|
| ubo_residential_address_city	                           | ubo_residential_address_city	                            |String	|The city where the UBO currently resides or can be contacted|
| ubo_residential_address_state                          	| ubo_residential_address_state                          	|String	|The state where the UBO currently resides or can be contacted|
| ubo_residential_address_postal_code 	                   | ubo_residential_address_postal_code 	                    |String	|The postal code where the UBO currently resides or can be contacted|
| ubo_residential_address_country                        	| ubo_residential_address_country                        	|Array	|The country() where the UBO currently resides or can be contacted|
| ubo_identification                                      	| ubo_identification                                      	|Object||
| ubo_identification_type	                                | ubo_identification_type	                                |String	|the type of the identity document|
| ubo_identification_document_number              	       | ubo_identification_document_number              	        ||String|	document number|
| ubo_identification_issuing_country              	       | ubo_identification_issuing_country              	        |String	|issuing country|
| ubo_identification_expiredate	                          | ubo_identification_expiredate	                            |String	|expire date for the identification document|
| ubo_identification_unique_personal_identification_number 	| ubo_identification_unique_personal_identification_number 	|String	|unique personal identification nr|
| ubo_identification _revocation link	                    | ubo_identification _revocation link	                    |String	|the revocation link for the identification nr (optional)|
| ubo_stake                                              	| ubo_stake                                              	|Object||
| ubo_stake_determination_methodology                     	| ubo_stake_determination_methodology                     	|Array	|the calculation methodology applied|
| ubo_stake_ownership_stake	                              | ubo_stake_ownership_stake	                                |String	|The percentage or level of ownership|
| ubo_stake_ownership_held_date	                          | ubo_stake_ownership_held_date	                            |String	|date of which beneficial interest is held|


For SD-JWT VC-compliant UBOs, the EUCC MUST include a status claim if the technical validity period is greater than 24 hours. This claim enables Relying Parties to determine if a credential has been revoked via a status list mechanism, as specified in SD-JWT VC.

The status claim SHALL be a JSON object with the following members:

'type' (string): SHALL be "status-list".
'status_list_credential' (string, URI): The URI of the Status List Credential document that contains the status bitstring.
'status_list_index' (integer, >= 0): The zero-based index into the status list bitstring that corresponds to this credential.
'status_purpose' (string): SHALL be "revocation" for this PID.
Example:

{
"status": {
"type": "status-list",
"status_list_credential": "https://issuer.example.com/status/1",
"status_list_index": 42,
"status_purpose": "revocation"
}
}
3.2.3 Example Payload
Sample payloads provided under ../data-schemas/sd-jwt-vc/sample-data/ds010-ubo-sd-jwt-sample.json

### 3.3 W3C Verifiable Credentials Data Model-based encoding

@TODO
to be discussed who will support here and which use case need the format ?

## 4 Attestation usage
*Briefly describe the primary use cases or scenarios for which this attestation 
type is intended*

*Additionally, in this section it SHOULD be specified whether a Relying Party receiving the attestation
must request and verify a PID (see ARB_27 in [Topic 12]). Also, beyond PID verification, 
it SHOULD be defined what other key obligations a Relying Party has when processing 
this attestation type (e.g. signature verification, freshness checks)*

*Furthermore, provide potential presentation requirements, e.g. are there specific 
requirements for how this attestation must be presented (e.g. online, offline, specific protocols)?*

*Finally, in this section information about potential transactional data
SHALL be defined (see [Topic 20] of Annex 2 of the ARF).*

## 5 Trust anchors

*Mechanisms for the provision of a trust anchor that SHALL
be used for the verification of an attestation SHALL be defined in this section.*

*It is noted that the ARF specifies the following for QEAAs and Pub-EAAs*

> To do this for [...] QEAAs the Relying Party Instance uses a trust anchor of 
the Provider obtained from a Trusted List. Note that the PID Provider or QEAA 
Provider may use an intermediate signing certificate to sign the PID or 
 attestation and use the trust anchor to sign the signing certificate, instead 
of signing the PID or attestation directly with the trust anchor.

> For PuB-EAAs, the Relying Party Instance verifies a PuB-EAA by first 
verifying the signature of the PuB-EAA Provider over the PuB-EAA, using the 
PuB-EAA Provider certificate issued by a QTSP. Subsequently, the Relying Party 
Instance verifies the signature over this certificate, using the corresponding 
trust anchor from the QTSP Trusted List. Note that both the PuB-EAA Provider 
and the QTSP may use an intermediate signing certificate. All other things 
being equal, the verification of a PuB-EAA will therefore involve one or more 
extra certificates, compared to the verification of a PID or QEAA.

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








 
