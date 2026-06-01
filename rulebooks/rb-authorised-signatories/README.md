# Attestation Rulebook for attestations of type AuthorisedSignatories Attestation  
* Author(s):
    * [Ricky Lambert, Robert Bosch GmbH]
    * @todo fred contact 
* Previous Authors

* Reviewer(s):
    * [Florin Coptil, Robert Bosch GmbH]
    * [Stephan-A Fuchs, Deutsche Bank]

| Version | Date       | Description                                                      |
|---------|------------|------------------------------------------------------------------|
| 0.1     | 15.05.2026 | Initial draft based on the WeBuild design attestations meetings  |

* Contact:
  <a href="mailto:florin.coptil@bosch.com">Florin Coptil</a>

* Feedback:

---

## 1 Introduction

This attestation addresses the following question:

**Who is authorised to act or sign on behalf of this legal entity?**
An Authorised Signatory Rights is defined as any natural person who is authorised to act on behalf of a legal entity in financial and contractual settings with third parties. It serves as a digital, verifiable list and consists of natural persons having representation powers.

The authority to act on behalf of a legal entity can be derived from two primary sources:
- Statutory Power: Authority based on a direct entry in a national public register (e.g., a Commercial Register).
- Delegated Power: Authority granted via a separate Power of Attorney (PoA) Attestation, which was issued by the company which issued the Authhorized Signatories attestation.
The Authorised Signatory Attestation enables a Relying Party (banks or fintechs) to confidently confirm that a person (the Signatory) has the authority to make binding commitments (i.e. signing a contract). This attestation is mandatory, for example, when opening a bank account. Other use cases may require the same type of attestation.

### 1.1 Document scope and purpose
The Authorised Signatory Attestation records all natural persons who are authorised to act on behalf of a legal entity, providing comprehensive transparency on signatory rights and representation powers. This attestation is a critical component of both Know Your Customer (KYC) and Know Your Supplier (KYS) processes within the EUDI Wallet ecosystem, supporting effective risk management, regulatory compliance, and anti-money laundering (AML) obligations.

Important distinctions:
- An Authorised Signatory does not need to be a registered Legal Representative
- An Authorised Signatory does not need to meet any ownership or control threshold
- A single person MAY hold both statutory and delegated authority simultaneously
Note: This attestation is not a replacement for the Power of Attorney (PoA) Attestation

**Design Decisions**

This Authorised Signatories Rulebook is based on:
- EU Company Certificate (EUCC) framework as the foundational legal identity layer
- Draft RTS on Customer Due Diligence under Article 28(1) of Regulation (EU) 2024/1624
- eIDAS 2.0 / EUDI Wallet framework for digital identity and verifiable attestations
- ISO 8601 for date formatting

### 1.2 Document structure

This Rulebook is structured as follows:

- Chapter 2 describes the attestation attributes and metadata in an encoding-independent manner, including the data model.
- Chapter 3 specifies how the attestation attributes and metadata are encoded: Section 3.2 covers SD-JWT VC-based encoding.
- Chapter 4 specifies attestation usage scenarios, Relying Party obligations, and integration with KYC/KYS workflows.
- Chapter 5 defines trust anchors and verification mechanisms for issuer authorization.
- Chapter 6 defines revocation mechanisms for the attestation.
- Chapter 7 provides compliance information regarding the EUDI framework and applicable data protection laws.
- Chapter 8 provides references to applicable standards and specifications.

### 1.3 Keywords

This document uses the capitalised keywords 'SHALL', 'SHOULD' and 'MAY' as specified in [RFC 2119], i.e. to indicate requirements, recommendations and options specified in this document.

In addition, 'must' (non-capitalised) is used to indicate an external constraint, i.e. a requirement that is not mandated by this document, but, for instance, by an external document. The word 'can' indicates a capability, whereas other words, such as 'will', and 'is' or 'are' are intended as statements of fact.

### 1.4 Terminology

*Additional terminology specific to this attestation:*

| Term                       | Description                                                                                                                                                                       |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Authorised Signatories 	   | Authorised Signatories  Attestation — the attestation type defined in this Rulebook, providing a verifiable list of natural persons authorised to act on behalf of a legal entity |
| Authorised Signatory	      | A natural person who is authorised to act on behalf of a legal entity in financial and contractual settings, either through statutory power or delegated power                    |
| Statutory Power	           | Authority to act on behalf of a legal entity based on a direct entry in a national public register (e.g., Commercial Register)                                                    |
| Delegated Power            | 	Authority to act on behalf of a legal entity granted via a Power of Attorney (PoA) issued by the legal entity                                                                    |
| PoA	                       | Power of Attorney — a separate attestation granting delegated authority to act on behalf of a legal entity                                                                        |
| EUCC	                      | EU Company Certificate — attestation establishing the legal existence and identity of a legal entity within the EU                                                                |
| EUID	                      | European Unique Identifier — the unique identifier assigned to legal entities registered within the EU                                                                            |
| KYC	                       | Know Your Customer — due diligence process for verifying customer identity and assessing risk in financial relationships                                                          |
| KYS	                       | Know Your Supplier — due diligence process for verifying supplier credentials, integrity, and risk exposure                                                                       |
| Relying Party	             | A bank, fintech, or other entity that relies on the ASR to verify the authority of a signatory                                                                                    |
| Representation Type        | 	The nature of the power of representation — either SOLE (one signatory sufficient) or JOINT (multiple signatories required)                                                      |
| ISO 8601	                  | International standard for date and time representations (e.g., YYYY-MM-DD)                                                                                                       |

## 2 Attestation attributes and metadata
The AuthorisedSignatories Attestation  is designed to provide a standardized, verifiable representation of all natural persons authorised to act on behalf of a legal entity. It enables Relying Parties to comprehensively verify signatory authority in financial and contractual settings, supporting effective KYC/KYS processes and regulatory compliance.

### 2.1 Introduction

**Data Model:**
The AuthorisedSignatories Attestation is structured into a root object containing two distinct sub-objects:

```
AuthorisedSignatories Attestation
├── Legal_Entity [1]
│   ├─ Legal_Person    (legal_person_name (M), legal_form_type (M))                                              — mandatory
│   └─ Identifier      (euid (M), lei (O), tax (O))                                                              — mandatory
└── Authorised_Person [1..n]
    ├─ NaturalPerson          (first_name (M), surname (M), date_of_birth (M))                                   — mandatory
    ├─ BirthPlace             (locality (M), country (M), region (O))                                            — mandatory
    ├─ Citizenship            (citizenship(s) [1..n])                                                            — mandatory
    ├─ PersonRole             (role (O), representation_type (M))                                                — mandatory
    └─ NaturalPersonIdentifier (document_type (M), document_number (M), issuing_country (M), expiry_date (M))   — optional
```

**Explanation:**

The `Legal_Entity` object SHALL appear exactly once and contains:
- `Legal_Person` — the official legal name and legal form of the entity issuing the attestation.
- `Identifier` — the EUID (mandatory) and optionally LEI and/or tax registration number.
The `Authorised_Person` object SHALL appear at least once and MAY be repeated for each authorised signatory. Each instance contains:
- `Natural_Person` — the full legal name and date of birth of the signatory.
- `Birth_Place` — the place of birth including at minimum locality and country.
- `Citizenship` — one or more citizenships held by the signatory.
- `Person_Role` — the role within the company (optional) and the representation type (mandatory).
- `NaturalPersonIdentifier` — optional identity document details for enhanced identification.

**Attestation Classification:**

This attestation type MAY be classified as:
- **"EAA"** when self-issued by the legal entity subject to the disclosure.

| **Data Identifier** | **Semantic Reference** | **Definition**                                         | **Data type**                         |
|---------------------|------------------------|--------------------------------------------------------|---------------------------------------|
| legal_person        | ...                    | Information about the legal person                     | Object                                |
| legal_identifier    | ...                    | Information about the legal person identifier          | Object                                |
| natural_person      | ...                    | Information about the natural persion                  | Object                                |
| birth_place         | ...                    | Information about the birth place                      | Object                                |
| citizenship         | ...                    | Citizenship(s) held by the person  (one or more nationalities) | Array of Strings (ISO 3166-1 alpha-3) |
| person_role         | ...                    | Information about the natural person role              | Object                                |
| residence_address   | ...                    | Information about the residential address of the person | Object                                |
| identification      | ...                    | Information about the identification of the person     | Object                                |


### 2.2 Mandatory attributes

The AuthorisedSignatories Attestation is designed to provide a standardized, verifiable representation of all natural persons authorised to act on behalf of a legal entity. It enables Relying Parties to comprehensively verify signatory authority in financial and contractual settings, supporting effective KYC/KYS processes and regulatory compliance.

**LegalPerson Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                                                                                 | **Data type** |
|---------------------|------------------------|----------------------------------------------------------------------------------------------------------------|---------------|
| legal_person_name   | --                     | The complete official name of the legal entity which exercises control over this entity                        | String        |
| legal_form_type     | --                     | The legal form of the controlling legal entity (e.g., SA, GmbH, Ltd, BV)                                       | String        |

**NaturalPerson Attributes**

| **Data Identifier**        | **Semantic Reference** | **Definition**                                                       | **Data type**                       |
|----------------------------|------------------------|----------------------------------------------------------------------|-------------------------------------|
| first_name                 | ...                    | The first names in full (including all given names and middle names) | String                              |
| surname                    | ...                    | The surnames in full (all family names/last names)                   | String                              |
| date_of_birth              | ...                    | Day, month, and year of birth of the person ISO 8601                 | Date (YYYY-MM-DD)                   |

**Birthplace Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                            | **Data type**                |
|---------------------|------------------------|-----------------------------------------------------------|------------------------------|
| locality            | ...                    | Locality (city or town) where the natural person was born | String                       |
| country             | ...                    | Country where the natural person was born                 | String (ISO 3166-1 alpha-3)  |



**Citizenship Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                            | **Data type**                |
|---------------------|------------------------|-----------------------------------------------------------|------------------------------|
| citizenship 	       | ...	                 |The nationality or nationalities of the authorised person (one or more) 	|Array of Strings (ISO 3166-1 alpha-3)|

**PersonRole Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                            | **Data type**                |
|---------------------|------------------------|-----------------------------------------------------------|------------------------------|
|representation_type	|...	|The nature of the power of representation. SHALL be one of the values defined in Section 2.8.1	|String ("SOLE" | "JOINT") |

### 2.3 Optional attributes

**LegalPersonIdentifier Optional Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                             | **Data type** |
|---------------------|------------------------|--------------------------------------------|---------------|
| euid                | --                     | EUID per ISO 3166-1 alpha-2                | String        |
| lei                 | --                     | Legal Entity Identifier (LEI) per ISO 1744 | String        | 
| tax                 | --                     | National company registration number       | String        |

**ResidenceAddress Optional Attributes**

| **Data Identifier** | **Semantic Reference**  | **Definition**                                                         | **Data type** |
|---------------------|-------------------------|------------------------------------------------------------------------|---------------|
| address             | --                      | The street address where the controller currently resides              | String        |
| locality            | --                      | The city where the controller currently resides d                      | String        |
| postal_code         | --                      | The postal or ZIP code of the controller's address                     | String        |
| region              | --                      | The state, province, or region of the controller's address             | String        |                                            
| country             | --                      | ISO 3166-1 alpha-3 country code where the controller currently resides | String        | 

**PersonRole Optional Attributes**

| **Data Identifier** | **Semantic Reference** | **Definition**                                            | **Data type**                |
|---------------------|------------------------|-----------------------------------------------------------|------------------------------|
| role	               |...	|	The role of the authorised person within the company (e.g., CEO, CFO, Director)	|String  |


**NaturalPersonIdentifier Optional Attributes**

| **Data Identifier**  | **Semantic Reference** | **Definition**                                                                                                                                        | **Data type**                          |
|----------------------|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| document_type        | ...                    | A value defining the type of the identity document according to the nationality of the UBO (e.g., Passport, National identity card, Driver's license) | String                                                             |
| document_number      | ...                    | The number of the identity document (passport number, national ID number, driver's license number, etc.)                                                 | String                                                                                                                                                |
| issuing_country      | ...                    | The country that issued the identity document (ISO 3166-1 alpha-3 code)                                                                                  | String                                                                                                                                                |
| document_expiry_date | ...                    | The expiration date of the identity document ISO 8601                                                                                                    | Date (YYYY-MM-DD)                                                                                                                                     |

### 2.4 Conditional attributes

No conditional attributes are defined for this attestation type. All attributes are either mandatory or optional as specified above.

### 2.5 Mandatory metadata

| **Data Identifier**          | **Definition**                                                                                                                                                | **Data type**   |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| issuance_date                | The date and time when the attestation was issued (ISO 8601)                                                                                                  | DateTime        |
| expiry_date                  | The date and time when the attestation expires (ISO 8601)                                                                                                     | DateTime        |
| issuing_entity               | The identifier of the legal entity that issued the attestation (typically the subject entity itself for self-issued attestations, or the QTSP identifier for QEAA) | String          |
| attestation_legal_category   | Indicates the legal category of this attestation ("EAA" )                                                                                   | String          |
### 2.6 Optional metadata

| **Data Identifier** | **Definition**                                                             | **Data type** |
|---------------------|----------------------------------------------------------------------------|---------------|
| trust_anchor_url    | URL where the trust anchor for verifying this attestation can be retrieved | URI           |
| schema_version      | Version of the schema used                                                 | String        |

### 2.7 Conditional metadata

No conditional metadata elements are defined for this attestation type.

### 2.8 Value Lists

## 3 Attestation encoding

### 3.1 ISO/IEC 18013-5-compliant encoding

ISO/IEC 18013-5 (also called mdoc) is out of scope for this Rulebook, as offline proximity presentation is not a current requirement for the CompanyInfo attestation.

### 3.2 SD-JWT VC-based encoding

The AuthorisedSignatoreies attestation uses the SD-JWT VC format to allow for selective disclosure of signatory attributes.
Selective Disclosure: Top-level claims (legal_entity, authorised_persons) SHALL be individually selectively disclosable, enabling a legal entity to disclose only the attributes requested by a Relying Party.

The . notation is used to indicate the nesting of attributes.

**Verifiable Credential Type (`vct`):** `vct: eu.we-build.authorisedsignatories.1`

#### 3.2.1 Attribute Encoding Table
| **Data Identifier**                                              | **Attribute identifier**                               | **Encoding format**                                                                                                                                      | **Reference/Notes**                                                              | **Disclosable**                                                                 |
|------------------------------------------------------------------|--------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| **Legal Entity**                                                 |                                                        |                                                                                                                                                          |                                                                                  |                                                                                 |				
| legal_person_name	                                               | legal_entity.legal_person.legal_person_name	           | String	                                                                                                                                                  | The complete official legal name of the company	                                 | MUST                                                                            |
| legal_form_type	                                                 | legal_entity.legal_person.legal_form_type	             | String	                                                                                                                                                  | Legal form of the company (e.g., GmbH, S.A., Ltd.)	                              | MUST                                                                            |
| euid	                                                            | legal_entity.identifier.euid                           | 	Stringv	EUID per Directive (EU) 2017/1132; mandatory                                                                                                    | 	MUST                                                                            |
| lei	                                                             | legal_entity.identifier.lei	                           | String (20 characters)	LEI per ISO 17442; optional	                                                                                                      | MUST                                                                             |
| tax 	                                                            | legal_entity.identifier.tax                            | 	String	                                                                                                                                                 | National tax or registration number; optional 	                                  | MUST                                                                            |
| **Authorised Person**                                            |                                                        |                                                                                                                                                          |                                                                                  |                                                                                 |				
| authorised_persons	                                              | authorised_persons	                                    | Array [AuthorisedPerson]	Array of authorised person objects in the AuthorisedSignatories Attestation; SHALL contain at least one entry	MUST              
| **NaturalPerson**                                                |                                                        |                                                                                                                                                          |                                                                                  |                                                                                 |				
| first_name                                                       | 	authorised_persons[n].natural_person.first_name       | 	String	                                                                                                                                                 | Full first name(s) of the authorised person per Art. 2 RTS	                      | MUST                                                                            |
| surname	                                                         | authorised_persons[n].natural_person.surname           | 	String	                                                                                                                                                 | Full surname(s) of the authorised person per Art. 2 RTS	                         | MUST                                                                            |
| date_of_birth	                                                   | authorised_persons[n].natural_person.date_of_birth     | 	String                                                                                                                                                  | (ISO 8601 YYYY-MM-DD)	Date of birth of the authorised person	                    | MUST                                                                            |
| **BirthPlace**                                                   |                                                        |                                                                                                                                                          |                                                                                  |                                                                                 |				
| birth_place.locality	vauthorised_persons[n].birth_place.locality | 	String                                                | 	Locality (city or town) where the authorised person was born	                                                                                           | MUST                                                                             |
| birth_place.country	                                             | authorised_persons[n].birth_place.country              | 	String (ISO 3166-1 alpha-3)                                                                                                                             | 	Country where the authorised person was born, per Art. 4 RTS                    | 	MUST                                                                           |
| birth_place.region	authorised_persons[n].birth_place.region      | 	String	                                               | Optional region or state of birth                                                                                                                        | 	MAY                                                                             
| Citizenship**                                                    |                                                        |                                                                                                                                                          |                                                                                  |                                                                                 |				
| citizenship	authorised_persons[n].citizenship                    | 	Array of Strings (ISO 3166-1 alpha-3)                 | 	Nationality or nationalities of the authorised person                                                                                                   | 	MUST                                                                            |
| **PersonRole**                                                   |                                                        |                                                                                                                                                          |                                                                                  |                                                                                 |				
| person_role.representation_type                                  | 	authorised_persons[n].person_role.representation_type | 	String ("SOLE"                                                                                                                              "JOINT")    |  	The nature of the power of representation; SHALL use codes from Section 2.8.1	 |MUST    |
| person_role.role	                                                | authorised_persons[n].person_role.role	                | String	                                                                                                                                                  | The role of the authorised person within the company (e.g., CEO, CFO); optional	 | MUST                                                                            |
| **NaturalPersonIdentifier**                                      |                                                        |                                                                                                                                                          |                                                                                  |                                                                                 |				
| identifier.document_type                                         | 	authorised_persons[n].identifier.document_type	       | String	                                                                                                                                                  | Type of identity document; SHALL use codes from Section 2.8.2; optional          | 	MAY                                                                            |
| identifier.document_number                                       | 	authorised_persons[n].identifier.document_number	     | String	                                                                                                                                                  | The number of the identity document; optional	                                   | MAY                                                                             |
| identifier.issuing_country                                       | 	authorised_persons[n].identifier.issuing_country	     | String (ISO 3166-1 alpha-3)	                                                                                                                             | Country that issued the identity document; optional	                             | MAY                                                                             |
| identifier.document_expiry_date                                  | 	authorised_persons[n].identifier.document_expiry_date | 	String (ISO 8601 YYYY-MM-DD)                                                                                                                            | 	Expiration date of the identity document; optional	                             | MAY                                                                             |
| **Metadata**                                                     |                                                        |                                                                                                                                                          |                                                                                  |                                                                                 |				
| issuance_date	                                                   | iat	                                                   | Number (Unix timestamp)                                                                                                                                  | 	Date and time when the attestation was issued; RFC 7519                         | 	MUST NOT                                                                       |           
| expiry_date	                                                     | exp	                                                   | Number (Unix timestamp)                                                                                                                                  | 	Date and time when the attestation expires; RFC 7519                            | 	MUST NOT                                                                       |                
| issuing_entity                                                   | 	iss	                                                  | String (URI or DID)	                                                                                                                                     | Identifier of the entity that issued the attestation; RFC 7519	                  | MUST NOT                                                                        |       
| attestation_legal_category	                                      | attestation_legal_category	                            | String	One of EAA or QEAA as defined by eIDAS 2                                                                                                          |                                                                                  | 	MUST NOT                                                                       |       
| schema_version                                                   | 	schema_version                                        | 	String	                                                                                                                                                 | Version of the schema used for this attestation	                                 | MAY                                                                             |                            
| trust_anchor_url	                                                | trust_anchor_url	                                      | URI	                                                                                                                                                     | URL where the trust anchor for verifying this attestation can be retrieved 	     | MAY                                                                             |

**Notes:**

- **MUST**: The claim SHALL be selectively disclosable — the holder MAY choose to disclose or
  withhold this claim when presenting the credential to a Relying Party.
- **MUST NOT**: The claim SHALL NOT be selectively disclosable — it is always present in plain
  text in the JWT header/payload and cannot be withheld by the holder, as it is required for
  credential verification and trust establishment.
- `iat`, `exp`, and `iss` follow RFC 7519 standard JWT claim naming conventions.
- The `NaturalPersonIdentifier` group of attributes is marked as MAY disclosable as a unit — if any attribute within the group is disclosed, all four SHALL be disclosed together.

#### 3.2.2 Status Claim
For SD-JWT VC-compliant AuthorisedSignatories Attestations, the attestation MUST include a status claim if the technical validity period is greater than 24 hours. This claim enables Relying Parties to determine if a credential has been revoked via a status list mechanism, as specified in SD-JWT VC.

The `status` claim SHALL be a JSON object with the following members:

- `type` (string): SHALL be `"status-list"`.
- `status_list_credential` (string, URI): The URI of the Status List Credential document that contains the status bitstring.
- `status_list_index` (integer, >= 0): The zero-based index into the status list bitstring that corresponds to this credential.
- `status_purpose` (string): SHALL be `"revocation"` for this attestation.

Example:

```json
{
  "status": {
    "type": "status-list",
    "status_list_credential": "https://issuer.example.com/status/authorisedsignatory/2025",
    "status_list_index": 789,
    "status_purpose": "revocation"
  }
}
```
### 3.2.3 Example Payload

The following is a non-normative example of a CompanyInfo SD-JWT VC payload:
```
{
  {
  "vct": "eu.we-build.authorisedsignatory.1",
  "attestation_legal_category": "EAA",
  "iss": "did:example:legal-entity-456",
  "iat": 1746000000,
  "exp": 1777536000,
  "jti": "asr-attestation-20260515-001",
  "legal_entity": {
    "legal_person": {
      "legal_person_name": "Example GmbH",
      "legal_form_type": "GmbH"
    },
    "identifier": {
      "euid": "DE-HRB-123456",
      "lei": "5493001KJTIIGC8Y1R12",
      "tax": "DE123456789"
    }
  },
  "authorised_persons": [
    {
      "natural_person": {
        "first_name": "Maria Anna",
        "surname": "Müller",
        "date_of_birth": "1982-07-14"
      },
      "birth_place": {
        "locality": "Munich",
        "country": "DEU",
        "region": "Bavaria"
      },
      "citizenship": ["DEU"],
      "person_role": {
        "representation_type": "SOLE",
        "role": "CEO"
      },
      "identifier": {
        "document_type": "Passport",
        "document_number": "C01X00T47",
        "issuing_country": "DEU",
        "document_expiry_date": "2031-03-20"
      }
    },
    {
      "natural_person": {
        "first_name": "Jean",
        "surname": "Dupont",
        "date_of_birth": "1975-11-30"
      },
      "birth_place": {
        "locality": "Paris",
        "country": "FRA"
      },
      "citizenship": ["FRA", "BEL"],
      "person_role": {
        "representation_type": "JOINT",
        "role": "CFO"
      }
    }
  ],
  "status": {
    "type": "status-list",
    "status_list_credential": "https://example.com/status/authorisedsignatory-list-1",
    "status_list_index": 789,
    "status_purpose": "revocation"
  },
  "trust_anchor_url": "https://trust.webuildconsortium.eu/anchors/eidas-tl",
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
Sample payloads are provided under ../data-schemas/sd-jwt/sample-data/company-info-sd-jwt-sample.json

### 3.3 W3C Verifiable Credentials Data Model-based encoding

@TODO — To be discussed: which stakeholders will support this format and which use cases require it.

## 4 Attestation usage
### 4.1. Issuance process ###

### 4.2 Relying Party Obligations
When receiving and processing an attestation, the Relying Party SHALL perform the following verification obligations.
### 4.2.1 – 4.2.8 Base Verification Process
The Relying Party SHALL perform the base attestation verification process as defined in the Base Verification specification:
https://github.com/flo0x/webuild-attestations/blob/main/rulebooks/rb-base/verifier-base-verification.md#42-relying-party-obligations
### 4.2.9 Validate Integrity Rules
Validation of integrity and policy rules will be specified in a future version of this Rulebook.

## 5 Trust anchors
This chapter will be completed in a future version of this Rulebook.

## 6 Revocation
This chapter will be completed in a future version of this Rulebook.

## 7 References
This chapter will be completed in a future version of this Rulebook.

## 8 References
| **Item Reference**                     | **Standard name/details**                                                                                                                                                                                                                                                                           |
|----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [European Digital Identity Regulation] | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework                            |
| [HAIP]                                 |Yasuda, K. et al, OpenID4VC High Assurance Interoperability Profile, OpenId Foundation, Version draft-03|
| [IANA-JWT-Claims]                      | IANA JSON Web Token Claims Registry. Available: https://www.iana.org/assignments/jwt/jwt.xhtml|
| [ISO/IEC 18013-5]                      | ISO/IEC 18013-5, Personal identification — ISO-compliant driving licence - Part 5: Mobile driving licence (mDL) application, First edition, 2021-09|
| [ISO 4217]                             | ISO 4217 — Currency codes. Available: https://www.iso.org/iso-4217-currency-codes.html|
| [ISO 8601]                             | ISO 8601 — Date and time format. Available: https://www.iso.org/iso-8601-date-and-time-format.html|
| [OIDC]                                 |Sakimura, N. et al., "OpenID Connect Core 1.0", OpenID Foundation. Available: https://openid.net/specs/openid-connect-core-1_0.html|
| [RFC 2119]                             | RFC 2119 — Key words for use in RFCs to Indicate Requirement Levels, S. Bradner, March 1997|
| [RFC 3339]                             |RFC 3339 — Date and Time on the Internet: Timestamps, G. Klyne et al., July 2002|
| [RFC 8610]                             |RFC 8610 — Concise Data Definition Language (CDDL): A Notational Convention to Express Concise Binary Object Representation (CBOR) and JSON Data Structures, H. Birkholz et al., June 2019|
| [RFC 8943]                             |RFC 8943 — Concise Binary Object Representation (CBOR) Tags for Date, M. Jones et al., November 2020|
| [RFC 8949]                             |RFC 8949 — Concise Binary Object Representation (CBOR), C. Bormann et al., December 2020|
| [SD-JWT VC]                            | SD-JWT-based Verifiable Credentials (SD-JWT VC). Available: https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/, version draft-ietf-oauth-sd-jwt-vc-09|
| [Topic 7]                              |ARF Annex 2 - Topic 7 - Attestation revocation and revocation checking. Available: https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a237-topic-7-attestation-revocation-and-revocation-checking|
