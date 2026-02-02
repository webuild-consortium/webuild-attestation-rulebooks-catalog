* Template version: 1.1, 20-08-2025


# Attestation Rulebook for attestations of type European Company Certificate (EUCC)

*Provide information about the author(s) of this Rulebook in the following form:*

* Author(s):
    <!-- Usage help: (Name LastName, Affiliation) -->
  * Jonas Toennis , [Brønnøysund Registry Center](https://www.brreg.no)

* Previous Authors
     <!-- Usage help: (Name LastName, Affiliation) -->
    * [celiacouson](https://github.com/celiacouson), Unknown Affiliation

*Provide versioning information about the Rulebook in the following form:*

| Version          | Date               | Description                                      |
|------------------|--------------------|--------------------------------------------------|
| 01                | 12.01.2025         | Initial Draft based on the previous [work of EWC ](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md) |

**Feedback:**
Main feedback channel: [GitHub issues](https://github.com/webuild-consortium/eudi-wallet-rulebooks-and-schemas/issues)
Alternative: Contact Business usecase 2 contact points in WE BUILD.

## 1 Introduction

### 1.1 Document scope and purpose

This document is the EU Company Certificate Data Rulebook (referred to as EUCC) based on
the [EU Company Law regulation](https://eur-lex.europa.eu/eli/dir/2025/25/oj/eng). It contains the specific requirements, issuance process, formatting and content of the EUCC. 
This document is created and used by the WEBUILD consortium to provide a common understanding, data schema, format and usage guidlines for the WEBUILD eco system. 

This document MAY be used as one of multiple innputs toward a final EUCC definition for the EBW ecosystem but that is up so the sole decisision of the EU commission or any other relevant authority with delgated power from the commission.

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

This document uses terminology specified in [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/eli/reg/2024/1183/oj/eng).

In addition to the attributes definition necessary to understand the data schema, it’s important to understand:

| Term                 | Definition in WE BUILD Context                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Natural person       | an individual human being who has legal rights and obligations. Unlike a legal person (which refers to an organization or entity), a natural person is a human with the capacity to engage in legal relationships, enter into contracts, own property, and be subject to legal actions. Natural persons are distinct from artificial entities (like corporations or governments). In legal terms, a natural person is someone who exists as a human being, as opposed to a corporate or fictional entity.                                                                                                                                                                                                                                                                                           | 
| Legal person         | an entity that has legal rights and obligations, similar to a natural person (an individual). It is an organization or group recognized by law as having the capacity to enter into contracts, sue, and be sued, and own property. Legal persons are distinct from the individuals who may own, manage, or be part of them. Examples of legal persons include Corporations, Government agencies, public entities (that are granted legal recognition to act on behalf of the state), Nonprofit organizations A legal person exists as a separate legal entity, meaning it can perform legal actions in its own name, distinct from the actions of its members.                                                                                                                                      | 
| Legal entity         | an organization or structure that is recognized by law as having legal rights and responsibilities distinct from those of its members or owners. A legal entity can enter into contracts, own property, incur debts, and be held liable for legal actions in its own name. Legal entities include various forms of organizations such as Corporations, Limited liability companies (LLCs), Nonprofit organizations, Partnerships The key characteristic of a legal entity is that it has its own legal existence, allowing it to perform actions independently of the individuals who are involved with it.                                                                                                                                                                                         |
 | Legal representative | Natural or legal person authorized to act on behalf of another person or organization in legal matters. This person has the legal authority to represent the interests of the entity, such as a company, in dealings with other parties, including signing contracts, making decisions, and appearing in legal proceedings. For businesses, a legal representative can be a director, officer, or another person designated by the company’s governing body (like the board of directors) to represent the company in legal matters. In the case of individuals, a legal representative might include a guardian, power of attorney holder, or someone with similar legal authority to act on behalf of the person.                                                                                 |
 | Signatory rights     | the authority or power granted to an individual or entity to legally bind an organization or company by signing contracts, agreements, or other formal documents. This authority can be granted to a specific person, such as an executive, director, or authorized representative, and can be either individual (where one person alone can sign) or joint (where multiple individuals are required to sign together). Signatory rights are important because they ensure that any commitments made by the organization are legally valid and enforceable. The terms and scope of signatory rights are usually outlined in the organization's internal governance documents, such as its bylaws, and can vary based on the level of responsibility and the nature of the agreements being signed.  | 


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

#TODO: 


### 2.2 Mandatory attributes

| **Data Identifier**        | **Definition**                                                                                                                                                    |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| attestation_legal_category | One of EAA, Pub-EAA or QEAA                                                                                                                                       |
| legal_person_name          | Official current legal person name as registered in the business register.                                                                                        |
| legal_person_id            | Unique ID for the legal person in the EUID structure.                                                                                                             |
| legal_form_type            | Legal form of the company.                                                                                                                                        |
| registration_member_state  | The member state where the company is registered (Alpha-2 country code).                                                                                          |
| registered_address         | The official address of the company as registered by public authority. See [section 2.5](#25-Address)                                                             |
| registration_date          | Date of company registration.                                                                                                                                     |
| legal_person_status        | Status of the company as defined in national law.       #TODO: Can we limit this to the BRIS accepted groups for a better international representative aproach ?  |
| legal_person_activity      | Main activity of the company (NACE).                                                                                                                              |
| legal_representative       | Information about the natural og legal person(s) authorized to represent the company. See [section 2.4](#24-conditional-attributes). At least one is required.    |


### 2.3 Optional attributes

| **Data Identifier**   | **Definition**                                                                                                            |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------|
| share_capital         | Amount of the subscribed capital with currency. Currency code used of the capital subscribed, as defined in ISO 4217:2015 |
| legal_person_duration | Endpoint of the legal duration of the company, if it is of a limited timespan. Given as date following ISO 8601        |
| digital_contact_point | Correspondence address of the company, such as electronic mail and/or website                                             |



### 2.4 Conditional attributes

If a Natural Person is representative of a legal person, the following attributes SHALL be included:

| **Data Identifier** | **Definition**                                                                      |
|---------------------|-------------------------------------------------------------------------------------|
| full_name           | Full name of the natural person representing the company.                           |
| date_of_birth       | Date of birth of the natural person representing the company.                       |
| nationality         | OPTIONAL: Nationality of the natural person representing the company.               |
| signatory_rule      | Information on whether the representative can engage the company alone or jointly.  | 



If a Legal Person is representative of a legal person, the following attributes SHALL be included:

| **Data Identifier** | **Definition**                                                                     |
|---------------------|------------------------------------------------------------------------------------|
| name                | Details about the legal person representing the company.                           |
| id                  | Unique ID for the legal person in the EUID structure.                              |
| legal_form_type     | Legal form of the legal person representing the company.                           |
| signatory_rule      | Information on whether the representative can engage the company alone or jointly. | 

A combination of natural and legal persons can be legal representatives of a legal person.

### 2.5 Address
There is currently no open standard for addresses. As such, the definitions from EWC for company addresses are re-used.

| **Data Identifier** | **Definition**                                                                  | Required |
|---------------------|---------------------------------------------------------------------------------|----------|
| full_address        | Complete address of the company, written as a string, separated by semicolons.  | Yes      | 
| care_of             | Used when the address is at the address of another person or legal person.      | No       |
| thorough_fare       | The name of a passage or way through from one location to another.              | No       |
| locator_designator  | A number or sequence that uniquely identifies the locator.                      | No       |
| post_code           | The code created and maintained for postal purposes.                            | No       |
| post_name           | A name identifying a subdivision of addresses (e.g., city).                     | No       |
| post_office_box     | A location designator for a postal delivery point at a post office.             | No       |
| locator_name        | Proper noun(s) applied to the real-world entity.                                | No       |
| admin_unit_level_1  | The uppermost administrative unit (typically country).                          | No       |
| admin_unit_level_2  | Secondary level/region (typically county or state).                             | No       |


### 2.6 Mandatory metadata 

| **Data Identifier**  | **Definition**                                                                                                                                                                                           |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| expiry_date          | Date (and if possible time) when the attestation will expire. Does not need to be an atribute and can be covered by credentialformat metadata, such as for example the "exp" field on the sd-jwt format. |
| issuing_authority    | Name of the administrative authority that issued the eucc, or the ISO 3166 alpha-2 country code of the respective Member State if there is no separate authority entitled to issue the EUCC.             |
| issuing_country      | Alpha-2 country code, as specified in ISO 3166-1, of the country or territory of the provider of the person identification data.                                                                         |

### 2.8 Conditional metadata 

| **Data Identifier**  | **Definition**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| location_status      | The location of validity status information on the person identification data where the providers of person identification data revoke person identification data. This attribute is required when the the time validity time periode of the attestation exceeds 24 hours.                                                                                                                                                                                                                                                            |
| trust_anchor         | This attribute indicates at least the URL at which a machine-readable version of the trust anchor to be used for verifying the EUCC can be found or looked up. *Note: This attribute corresponds to the location meant in Annex V point h) or Annex VII point h) of the [European Digital Identity Regulation], which is mandatory for QEAAs. This  Rulebook adds this as an optional attribute for EUCCs as well, so EUCC Providers are able to ensure that EUCCs can be validated by Relying Parties in the same manner as QEAAs.   |



# 3 Attestation encoding 

## 3.1 ISO/IEC 18013-5-compliant encoding 

ISO/IEC 18013-5 (also called mdoc) is out of scope for this rulebook, as offline proximity presentation is not a current requirement for EUCC.

### 3.2 SD-JWT VC-based encoding 

The EUCC attestation uses the SD-JWT VC format to allow for selective disclosure of company attributes.
Selective Disclosure: Claims of EUCC SHALL NOT be selectively disclosable to preserve the legally mandated content of the EUCC.


The . notation is used to indicate the nesting of attributes.


**Verifiable Credential Type (`vct`):** `uri:eu.eudi.eucc.1`


| **Data Identifier**                                | **Attribute identifier**                          | **Encoding format** | **Reference/Notes**                                                        |
|----------------------------------------------------|---------------------------------------------------|---------------------|----------------------------------------------------------------------------|
| attestation_legal_category                         | attestation_legal_category                        | string              | One of EAA, Pub-EAA, QEAA as defined by eIDAS 2                            |
| issuing_authority                                  | iss                                               | string              | RFC 7519 / Section 2.6                                                     |
| expiry_date                                        | exp                                               | number              | RFC 7519 / Section 2.6 (Unix timestamp)                                    |
| issuing_country                                    | issuing_country                                   | string              | ISO 3166-1 alpha-2                                                         |
| legal_person_name                                  | legal_person_name                                 | string              | Official current legal person name as registered in the business register. |
| legal_person_id                                    | legal_person_id                                   | string              | EUID                                                                       |
| legal_form_type                                    | legal_form_type                                   | string              | Legal form of the company.                                                 |
| registration_member_state                          | registration_member_state                         | string              | The member state where the company is registered (Alpha-2 country code).   |
| registration_date                                  | registration_date                                 | string              | ISO 8601 (YYYY-MM-DD)                                                      |
| legal_person_status                                | legal_person_status                               | string              |                                                                            |
| legal_person_activity                              | legal_person_activity                             | object              | The NACE code describing the main activity                                 |
| legal_person_activity.code                         | legal_person_activity.code                        | string              |                                                                            |
| legal_person_activity.description                  | legal_person_activity.description                 | string              |                                                                            |
| legal_person_duration                              | legal_person_duration                             | date                | Given as date following ISO 8601                                           |
| registered_address                                 | registered_address                                | object              | See section 2.5 for structure                                              |
| registered_address.full_address                    | registered_address.full_address                   | string              |                                                                            |
| registered_address.care_of                         | registered_address.care_of                        | string              |                                                                            |
| registered_address.thorough_fare                   | registered_address.thorough_fare                  | string              |                                                                            |
| registered_address.locator_designator              | registered_address.locator_designator             | string              |                                                                            |
| registered_address.post_code                       | registered_address.post_code                      | string              |                                                                            |
| registered_address.post_name                       | registered_address.post_name                      | string              |                                                                            |
| registered_address.post_office_box                 | registered_address.post_office_box                | string              |                                                                            |
| registered_address.locator_name                    | registered_address.locator_name                   | string              |                                                                            |
| registered_address.admin_unit_level_1              | registered_address.admin_unit_level_1             | string              |                                                                            |
| registered_address.admin_unit_level_2              | registered_address.admin_unit_level_2             | string              |                                                                            |
| legal_representative                               | legal_representative                              | array               | Array of natural/legal persons                                             |
| legal_representative.legal_person                  | legal_representative.legal_person                 | object              |                                                                            |
| legal_representative.legal_person.name             | legal_representative.legal_person.name            | string              |                                                                            |
| legal_representative.legal_person.id               | legal_representative.legal_person.id              | string              |                                                                            |
| legal_representative.legal_person.formtype         | legal_representative.legal_person.formtype        | string              |                                                                            |
| legal_representative.legal_person.signatory_rule   | legal_representative.legal_person.signatory_rule  | string              |                                                                            |
| legal_representative.natural_person                | legal_representative.natural_person               | object              |                                                                            |
| legal_representative.natural_person.full_name      | legal_representative.natural_person.full_name     | string              |                                                                            |
| legal_representative.natural_person.date_of_birth  | legal_representative.natural_person.date_of_birth | string              |                                                                            |
| legal_representative.natural_person.nationality    | legal_representative.natural_person.nationality   | string              |                                                                            |
| legal_representative.natural_person.signatory_rule | legal_representative.natural_person               | string              |                                                                            |
| share_capital                                      | share_capital                                     | object              |                                                                            |
| share_capital.amount                               | share_capital.amount                              | string              |                                                                            |
| share_capital.currency                             | share_capital.currency                            | string              |                                                                            |
| digital_contact_point                              | digital_contact_point                             | object              |                                                                            |
| digital_contact_point.website                      | digital_contact_point.website                     | string              |                                                                            |
| digital_contact_point.email                        | digital_contact_point.email                       | string              |                                                                            |
| location_status                                    | status                                            | object              | See chapter [3.2.3](#321-attribute-status)                                 |


#### 3.2.1 Attribute status
For SD-JWT VC-compliant EUCCs, the EUCC MUST include a status claim if the technical validity period is greater than 24 hours. This claim enables Relying Parties to determine if a credential has been revoked via a status list mechanism, as specified in [SD-JWT VC](https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/12/).

The status claim SHALL be a JSON object with the following members:

* 'type' (string): SHALL be "status-list".
* 'status_list_credential' (string, URI): The URI of the Status List Credential document that contains the status bitstring.
* 'status_list_index' (integer, >= 0): The zero-based index into the status list bitstring that corresponds to this credential.
* 'status_purpose' (string): SHALL be "revocation" for this PID.

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

#### 3.2.3 Example Payload 
Sample payloads provided under `../data-schemas/sd-jwt-vc/sample-data/ds004-eucc-sd-jwt-sample.json`



### 3.3 W3C Verifiable Credentials Data Model-based encoding
*If the attestation type supports the format specified in W3C Verifiable Credentials 
Data Model, then in this section the corresponding encoding of attributes and 
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

The EUCC is intended to be used as a standardised, machine-verifiable proof of a company’s incorporation and registered company information, to be presented by a Wallet User to an RP in cross-border and domestic contexts.

Typical scenarios include, but are not limited to:

- **Cross-border business onboarding (B2B)**: sharing official company registration data during supplier/customer onboarding, procurement qualification, or partner due diligence.
- **Public administration procedures (G2B)**: providing evidence of registration and company attributes when applying for permits, registrations, notifications, or access to public services.
- **Financial and regulated services**: supporting organisational onboarding steps where official company data is required (e.g., account opening or contractual setup), where the RP needs a reliable, registry-backed set of company attributes.
- **Replacement/supplement of national extracts**: substituting ad-hoc sharing of national registry extracts (often requiring translation) with a harmonised EUCC attestation.

The EUCC is **not** intended to be used as a standalone authentication mechanism to log into a company register or to replace processes that legally require a natural person to act and be authenticated in their own right.

**Note:** The EUCC includes information about legal representation (e.g., legal representatives and signatory rules). This supports business decisions but does not, by itself, prove that the current presenter is one of those representatives unless the RP also performs an appropriate binding to the presenter (typically via PID and/or additional authorisation evidence outside the scope of this rulebook).

**Note:** The EUCC is intended for **online, remote presentation** using EUDI Wallet-compatible presentation protocols.


### 4.1 Issuance of the EUCC

* The Issuer of the EUCC SHALL be the company register or an authority appointed by the company register to issue EUCCs on their behalf. 
* The Issuance SHALL be based on up to date, authoritive data from the authorative source as defined by ????? #TODO
* The EUCC SHALL be key bound to the wallet, IF the wallet belongs to the company that the EUCC is issued for.
* If the EUCC is issued to a wallet that is not owned by the company that the EUCC is issued for, the EUCC SHALL NOT be  key bound to the wallet.
* The EUCC SHALL be issued in a format that is compatible with the EUDI Wallet ecosystem (e.g., **OpenID4VP** profiles adopted by the ecosystem).
* To recive an EUCC with keybinding, the application shall ensure that the wallet is owned by the company that the EUCC is issued for through presentation, and matching of key material of the European busesiness wallet owner identifaction data (OID). **Note** If bulk issued to the same wallet, the authorisation process of the OID process SHOULD be considered sufficent for reciept of an EUCC with keybinding in the same transaction. 

### 4.5 Relying Party obligations when processing an EUCC

Beyond protocol-level checks, an RP processing an EUCC presentation **SHALL** perform at least the following controls:

1. **Verify authenticity and integrity**
    - Verify the EUCC cryptographic protections (signature/seal chain validation as applicable for the legal category).
    - Verify that the issuer is authorised to issue EUCCs according to the trust anchor mechanism defined in this rulebook (see Chapter 5).

2. **Verify time validity / freshness**
    - Verify the EUCC is within its validity period (e.g., using `exp` in SD-JWT VC).

3. **Check revocation / status (where applicable)**
    - Where the EUCC validity exceeds 24 hours and a status mechanism is provided, the RP **SHALL** check the EUCC validity status using the mechanism defined in Chapter 6.

4. **Process according to purpose limitation**
    - RPs **SHOULD** request and process the EUCC only when needed for the specific transaction, and only for the purpose of the transaction, in line with applicable legal requirements.


EUCC presentation may involve **transactional data** exchanged as part of the presentation protocol. The following transactional data elements are relevant for EUCC usage:

- **Relying Party request parameters**, including the requested credential type(s) and any policy constraints (e.g., requirement to include PID alongside EUCC).
- **Challenge/nonce and session identifiers** used to prevent replay and bind the presentation to a specific session.
- **Presentation timestamp** (implicit or explicit), to support auditability and freshness validation.
- **Relying Party identification information** presented to the Wallet Unit (e.g., RP name, domain, certificate details), to support user transparency and consent decisions.

The specific protocol artefacts and parameter names depend on the adopted OpenID4VP profile(s). This rulebook does not prescribe additional EUCC-specific transactional data beyond what is required by the underlying presentation protocol(s).


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








 
