# Attestation Rulebook for attestations of type Ultimate Beneficial Owner(s) List (UBO-List)*

* Author(s): 
    * [Florin Coptil, Robert Bosch GmbH]
* Previous Authors

* Reviewer(s):
    * [......, Bundesanzeiger]
    * [......, Deutsche Bank]

| Version | Date       | Description                                                     |
|---------|------------|-----------------------------------------------------------------|
| 0.1     | 13.03.2026 | Initial draft based on the WeBuild design attestations mettings |
| 0.2     | 20.04.2026 | updates in regard to the comments and legislation              |

* Contact:
  <a href="mailto:florin.coptil@bosch.com">Florin Coptil</a>

* Feedback:

## 1 Introduction

### 1.1 Document scope and purpose

The Ultimate Beneficial Owner (UBO) List Attestation identifies and verifies the natural persons who ultimately own or control a legal entity, meeting the fundamental requirement within both Know Your Customer (KYC) and Know Your Supplier (KYS) processes to ensure transparency, prevent financial crime, and fulfill regulatory compliance obligations mandated by the EU Anti-Money Laundering Regulation (AMLR) and related directives.

Understanding who ultimately owns or controls a legal entity is essential to assess the true risk profile of a customer or supplier, detect potential money laundering, terrorism financing, sanctions exposure, or conflicts of interest, and comply with anti-money laundering (AML) and counter-terrorist financing (CTF) regulations. 

**Design Decisions**

This UBO List Attestation Rulebook is based on:
- Proposed Implementing Act dated 26/11/2025 – Formats for submitting beneficial ownership information
- AMLD4, AMLD5, AMLD6 – Anti-Money Laundering Directives (predecessor frameworks)
- Regulation (EU) 2024/1624 (AMLR) – Anti-Money Laundering Regulation, particularly:Article 3(17) – Definition of "beneficial owner"
- Article 60 – Beneficial ownership registers
- Article 62 – Beneficial ownership information requirements
- Articles 20-25 – Customer Due Diligence (CDD) and Enhanced Due Diligence (EDD)

### 1.2 Document structure
This Rulebook is structured as follows:

- Chapter 2 describes the UBO List attestation attributes and metadata in an encoding-independent manner, including the flat-list UBO data model.
- Chapter 3 specifies how the attestation attributes and metadata are encoded:Section 3.1: ISO/IEC 18013-5-compliant encoding (applicability assessment)
- Chapter 4 specifies attestation usage scenarios, Relying Party obligations (including UBO identity verification procedures per AMLR), and integration with KYC/KYS workflows.
- Chapter 5 defines trust anchors and verification mechanisms for issuer authorization, including integration with Transparency Registers.
- Chapter 6 defines revocation mechanisms for the attestation.
- Chapter 7 provides compliance information regarding the EUDI framework, AMLR, AMLD, and applicable data protection laws.

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

*Additional terminology specific to this attestation:*

| Term                                                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 
|---------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ultimate Beneficial Owner (UBO) / Beneficial Owner Per AMLR Article 3(17) | Any natural person who ultimately owns or controls a legal entity or legal arrangement, OR on whose behalf a transaction or activity is being conducted. For legal entities: natural person(s) who ultimately own or control ≥25% of shares/voting rights/ownership interests, or who exercise control through other means. For legal arrangements (trusts, foundations): settlors, trustees, protectors, beneficiaries, and any other natural person exercising ultimate control. |
| UBO List                                                                  | A list of all natural persons meeting the UBO definition for a specific legal entity, calculated by applying the ≥25% threshold and AMLR determination methodologies to the Ownership List and Control List                                                                                                                                                                                                                                                                        |
| Transparency Register / Beneficial Ownership Register                     | National register mandated by AMLR Article 60 where legal entities must submit UBO information, accessible by competent authorities, obliged entities (financial institutions), and (with restrictions) the public                                                                                                                                                                                                                                                                 |
| Determination Methodology                                                 | The calculation method used to identify UBOs, specified by AMLR and the proposed Implementing Act, including: (a) type of ownership (direct, indirect); (b) legal arrangement (settlor, trustee, beneficiary, etc.); (c) nature of control (control through ownership, voting rights, appointment rights, veto rights, distribution of profits, agreements, family relationships, acting in concert, nominee arrangements)                                                         |
| Direct Ownership                                                          | Ownership interest held directly by a natural person in the subject entity, without intermediary entities (per AMLR and Ownership List definition)                                                                                                                                                                                                                                                                                                                                 |
| Indirect Ownership                                                        | Ownership interest held through one or more intermediary legal entities (per AMLR and Ownership List definition)                                                                                                                                                                                                                                                                                                                                                                   |
| Unique Personal Identification Number                                     | A government-assigned number uniquely linked to an individual, independent of any specific ID document, and valid for the person's lifetime (e.g., social security number, national identification number, fiscal code). Where available, this SHALL be included per AMLR Article 62.                                                                                                                                                                                              |
| Person Identification Data (PID)                                          | EUDI Wallet attestation providing verified identity attributes of a natural person (name, birth date, address, nationality), used for UBO identity verification                                                                                                                                                                                                                                                                                                                    |
| KYC                                                                       | Know Your Customer – due diligence process for verifying customer identity and assessing risk in financial relationships, mandated by AMLR Articles 20-25                                                                                                                                                                                                                                                                                                                          |
| KYS                                                                       | Know Your Supplier – due diligence process for verifying supplier credentials, integrity, and risk exposure                                                                                                                                                                                                                                                                                                                                                                        |
| EUCC                                                                      | EU Company Certificate – attestation establishing the legal existence and identity of a legal entity within the EU                                                                                                                                                                                                                                                                                                                                                                 |

## 2 Attestation attributes and metadata
The UBO List Attestation is designed to provide a complete, verifiable representation of an entity's ultimate beneficial owners in a standardized digital format compliant with AMLR Article 62 and the proposed Implementing Act (26/11/2025). This attestation consolidates all natural persons meeting the UBO threshold (≥25% ownership/control or exercising ultimate control through other means) into a single, comprehensive attestation.

### 2.1 Introduction
Unlike Ownership List and Control List attestations (which use hierarchical structures with nested ownership/control layers), the UBO List uses a flat list structure where each entry represents a single UBO with all associated attributes:

_Data Model:
````
UBO List
├─ UBO [1...n]   (at least one UBO; typically 1-5 UBOs for most entities)
│   ├─ Personal Identification Attributes (first name, surname, date of birth, citizenship(s))
│   ├─ Birthplace (locality, country)
│   ├─ ResidentialAddress (street, house number, city, state, postal code, country(ies) of residence)
│   ├─ IdentityInformation (type of identity document, document number, issuing country, expiry date, unique personal identification number, revocation link)
│   └─ OwnershipInfo (determination methodology, ownership stake, ownership held date)
````

**Explanation:**
- The UBO List SHALL contain at least one UBO (natural person meeting the UBO definition per AMLR Article 3(17))
- Each UBO is represented as a single flat object (not nested hierarchically)
- All attributes for a UBO are co-located within that UBO object
- The UBO List MAY contain n UBOs (typically 1-5 for most entities; more for complex structures with multiple ≥25% shareholders or control persons)

**Attestation Classification:**

This attestation type MAY be classified as:
- "EAA" when self-issued by the legal entity subject to the UBO disclosure 
- "QEAA" when issued by a national Transparency Register or competent authority which can attest the information in case that a RP require it (ex. Bank in KYC process by cross-check of discrepancy) 


| **Data Identifier**         | **Semantic Reference** | **Definition**                                                       | **Data type** |
|-----------------------------|------------------------|----------------------------------------------------------------------|---------------|
| ubo_personal_identification | ...                    | Information about the beneficial owner(s)                            | Object                                                             |
| ubo_birthplace              | ...                    | Information about the birth place                                    | Object                                    |
| ubo_residential_address     | ...                    | Information about the residential address of the beneficial owner(s) | Object                                    |
| ubo_identification          | ...                    | Information about the identification of the beneficial owner(s)      | Object                                                               |
| ubo_ownership_info          | ...                    | Information about the stake information of the beneficial owner(s)   | Object                                                               |

### 2.2 Mandatory attributes
@TODO Florin still to confirmed with Barth the type (after matching in vocabulary document) 

**UBO Personal Identification Attributes**  

| **Data Identifier**          | **Semantic Reference** | **Definition**                                                                         | **Data type**                       |
|------------------------------|------------------------|----------------------------------------------------------------------------------------|-------------------------------------|
| first_names                  | ...                    |The beneficial owner's first names in full (including all given names and middle names) | String                                                                               |
| surnames                     | ...                    |The beneficial owner's surnames in full (all family names/last names)                   | String                                                                                  |
| date_of_birth                | ...                    |Day, month, and year of birth of the UBO ISO 8601                                       | Date (YYYY-MM-DD)                                                                       |
| citizenships                 | ...                    |Citizenship(s) held by the UBO (one or more nationalities)                              | Array of Strings (ISO 3166-1 alpha-3)                                                   |

**Birthplace Attributes** 

| **Data Identifier**   | **Semantic Reference** | **Definition**                                            | **Data type**                       |
|-----------------------|------------------------|-----------------------------------------------------------|------------------------------|
| birth_place_locality  | ...                    | Locality (city or town) where the natural person was born | String                                               |
| birth_place_country   | ...                    | Country where the natural person was born                 | String (ISO 3166-1 alpha-3)                               |

Note: AMLR Article 62(b) requires "place and full date of birth." This Rulebook interprets "place" as locality + country.

**ResidentialAddress Attributes**

| **Data Identifier**      | **Semantic Reference** | **Definition**                                                                     | **Data type**                          |
|--------------------------|------------------------|------------------------------------------------------------------------------------|----------------------------------------|
| residential_street       | ...                    | The street where the UBO currently resides or can be contacted                     | String                                                                            |
| residential_house_number | ...                    | The house/building number where the UBO currently resides or can be contacted      | String                                                         |
| residential_city         | ...                    | The city where the UBO currently resides or can be contacted                       | String                                                         |
| residential_state        | ...                    | The state, province, or region where the UBO currently resides or can be contacted | String                                                         |
| residential_postal_code  | ...                    | The postal code where the UBO currently resides or can be contacted                | String                                                         |
| countries_of_residence   | ...                    | The country or countries where the UBO currently resides or can be contacted       | Array of Strings (ISO 3166-1 alpha-3)                          |

Note: AMLR Article 62(c) requires "residential address" and (d) requires "country or countries of residence." This Rulebook provides full address breakdown for structured data.

** IdentityInformation Attributes**

| **Data Identifier**       | **Semantic Reference** | **Definition**                                                                                                                                        | **Data type**                          |
|---------------------------|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| type_of_identity_document | ...                    | A value defining the type of the identity document according to the nationality of the UBO (e.g., Passport, National identity card, Driver's license) | String                                                             |
| identity_document_number  | ...                    | The number of the identity document (passport number, national ID number, driver's license number, etc.)                                                 | String                                                                                                                                                |
| identity_issuing_country  | ...                    | The country that issued the identity document (ISO 3166-1 alpha-3 code)                                                                                  | String                                                                                                                                                |
| identity_expiry_date      | ...                    | The expiration date of the identity document ISO 8601                                                                                                    | Date (YYYY-MM-DD)                                                                                                                                     |

**Ownership Attributes**

Each UBO entry SHALL contain an OwnershipInfo nested object with the following mandatory attribute:

| **Data Identifier**       | **Semantic Reference** | **Definition**                                                                                                                                                                              | **Data type**                          |
|---------------------------|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| determination_methodology | ...                    | Specifies the calculation methodology applied in accordance with the AMLR and applicable Transparency Register requirement. This attribute classifies how the UBO was determined. String or | Array of Strings (enumeration) ["Direct ownership", "Control through voting rights"]                                                                                                |
| ownership_stake           | ...                    | The percentage or level of ownership/control held by the UBO (≥25% per AMLR threshold, but may be higher)                                                                                       | Decimal (25.0-100.0)                                                                                                                                                                        |
| ownership_held_date       | ...                    | Date on which the beneficial interest is held (as of when the UBO calculation was performed)                                                                                                    | ISO 8601 Date (YYYY-MM-DD)                                                                                                                                                                  |

Note: A UBO may be identified through multiple determination methodologies simultaneously (e.g., both direct ownership ≥25% AND control through voting rights ≥50%). Therefore, determination_methodology MAY be encoded as an array of strings.

### 2.3 Optional attributes

**UBO Optional Attributes**

| **Data Identifier**                   | **Semantic Reference** | **Definition**                                                                                                                                                                                                                                | **Data type**                          |
|---------------------------------------|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| unique_personal_identification_number | ...                    | A government-assigned number uniquely linked to the individual,independent of any specific ID document, and valid for the person's lifetime (e.g., social security number, national ID, fiscal code). This SHALL be included where available. | String |
| unique_id_number_source               | ...                    | General description of the source of the unique personal identification number (e.g., "Spanish National ID (DNI)", "French Social Security Number", "German Tax ID")                                                                          |String|
| birth_place_region                    | ...                    | Optional additional detail on the region/state where the UBO was born                                                                                                                                                                         |String |

Note: unique_personal_identification_number and unique_id_number_source are optional in this Rulebook because AMLR Article 62(g) states "where available." However, issuers SHOULD include this information whenever it is available, as it significantly enhances identity verification reliability.

#### 2.4 Conditional attributes
No conditional attributes are defined for this attestation type. All attributes are either mandatory or optional as specified above.

#### 2.5 Mandatory metadata

| **Data Identifier**            | **Definition**                                                                                                                                                     | **Data type** |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| issuance_date                  | The date and time when the attestation was issued ISO 8601                                                                                                         | DateTime      |
| expiry_date                    | The date and time when the attestation expires ISO 8601                                                                                                            | DateTime      |
| issuing_entity                 | The identifier of the legal entity that issued the attestation (typically the subject entity itself for self-issued attestations, or the QTSP identifier for QEAA) | String        | 
| attestation_legal_category     | Indicates the legal category of this attestation ("EAA" or "pubEAA"/"QEAA")                                                                                        | String        |
### 2.6 Optional metadata

| **Data Identifier** | **Definition**                                                             | **Data type**                          |
|-----------------------|----------------------------------------------------------------------------|----------------------------------------|
| trust_anchor_url    | URL where the trust anchor for verifying this attestation can be retrieved | URI|
| schema_version      | Version of the schema used                                                 |String |

#### 2.7 Conditional metadata
No conditional metadata elements are defined for this attestation type.

#### 2.8 Value Lists

#### 2.8.1 Type of Identity Document Codes

The type_of_identity_document attribute SHALL use one of the following standardized values:

| **Code**                         | **Definition**      |
|----------------------------------|---------------------------------------------------------------------|
| Passport                         |International travel document issued by a national government|
| National identity card           |National identity card issued by the UBO's country of nationality|
| Driver's license                 |Driver's license (may be used as identity document in some jurisdictions)|
| Residence permit                 |Residence permit or similar document issued by the country of residence (if different from nationality)|
| Other official identity document |Other government-issued identity document accepted for identity verification|

Note: The type of identity document SHOULD correspond to the UBO's nationality (not the country of the authentic source or the subject entity's jurisdiction). Per AMLR, identity documents issued by the UBO's country of nationality are preferred.

### 2.8.2 Determination Methodology Codes
The determination_methodology attribute SHALL use one or more of the following standardized values, aligned with AMLR Article 3(17) and the proposed Implementing Act:

*a) Type of Ownership:*

| **Code**            | **Definition**      |
|---------------------|---------------------------------------------------------------------|
| Direct ownership    |The UBO holds ≥25% of shares, voting rights, or ownership interests directly in the subject entity, without intermediary entities UBO owns 30% of shares directly|
| Indirect ownership   |The UBO holds ≥25% of shares, voting rights, or ownership interests indirectly through one or more intermediary legal entities UBO owns 100% of Parent Co., which owns 40% of Subject Entity → UBO has 40% indirect ownership|

*b) Legal Arrangement (for trusts, foundations, and similar structures):*

| **Code**          | **Definition**      |
|-------------------|---------------------------------------------------------------------|
| Settlor           |The UBO is the settlor (creator) of a trust or similar legal arrangement UBO established a trust that owns 50% of the entity|
| Trustee           |The UBO is the trustee of a trust or similar legal arrangement UBO acts as trustee of a trust owning 60% of the entity|
| Beneficiary       |The UBO is a beneficiary of a trust or similar legal arrangement UBO is beneficiary of a trust owning 35% of the entity|
| Object of a power |The UBO is the object of a power in a legal arrangement UBO is object of a power of appointment in a trust|
| Default taker     |The UBO is the default taker (residual beneficiary) of a legal arrangement UBO is default taker if primary beneficiaries disclaim|
| Protector         |The UBO is the protector of a trust or similar legal arrangement UBO acts as protector with powers to appoint/remove trustees|
| Other             |person exercising ultimate control over legal arrangement Any other natural person exercising ultimate control over the legal arrangement (direct, indirect, or by other means, including through a chain of control or ownership) UBO has contractual control over trust decisions despite not being settlor/trustee/beneficiary|

*c) Nature of Control (for control through means other than ownership percentage):*

| **Code**                                             | **Definition**      |
|------------------------------------------------------|---------------------------------------------------------------------|
| Control through ownership                            |Control exercised through ownership of shares/capital (overlaps with "Direct ownership" / "Indirect ownership" but emphasizes control aspect) UBO owns 51% of shares, giving control|
| Control through voting rights                        |Control exercised through voting rights that exceed ownership percentage (e.g., special shares with enhanced voting rights) UBO owns 10% of shares but holds "Class A" shares with 60% of voting rights|
| Control through right of appointments                |Control exercised through the right to appoint or remove directors, senior management, or other key decision-makers UBO has contractual right to appoint majority of board members|
| Control through veto rights                          |Control exercised through veto rights over major corporate decisions (e.g., M&A, capital increases, dissolution) UBO has contractual veto rights over all major decisions per shareholder agreement|
| Control through distribution of profits              |Control exercised through the right to control the distribution of profits (e.g., special dividend rights) UBO has contractual right to determine dividend policy|
| Control through formal or informal agreements        |Control exercised through formal agreements (e.g., shareholders' agreements, management agreements) or informal arrangements UBO controls the entity via a shareholders' agreement granting operational control|
| Control through relationships between family members |Control exercised through coordinated action among family members (acting in concert) UBO and family members collectively control 60% of voting rights via family council|
| Control through acting in concert                    |Control exercised through acting in concert with other shareholders or stakeholders UBO and other shareholders have voting agreement to act in concert, giving collective control|
| Control through nominee arrangements                 |Control exercised through nominee shareholders, nominee directors, or other nominee arrangements where the UBO is the beneficial controller behind the nominee UBO controls the entity through nominee shareholders holding shares on UBO's behalf|

Note: Multiple determination methodologies MAY apply to a single UBO. For example, a UBO may be identified through:
"Direct ownership" (30% direct shareholding) AND
"Control through voting rights" (50% voting rights via special shares) AND
"Control through right of appointments" (contractual right to appoint CEO)

In such cases, determination_methodology SHOULD be encoded as an array containing all applicable codes._


### 2.9 Integrity Rules

The following integrity rules **SHALL** be enforced:

*   The `UBO List` **SHALL** contain at least one `UBO` object.
*   Each `UBO` object **SHALL** contain `first_names`, `surnames`, `date_of_birth`, `citizenships`, `birth_place_locality`, `birth_place_country`, `residential_street`, `residential_house_number`, `residential_city`, `residential_postal_code`, `countries_of_residence`, `type_of_identity_document`, `identity_document_number`, `identity_issuing_country`, `identity_expiry_date`, and `ownership_info`.
*   `date_of_birth` **SHALL** be a valid ISO 8601 date (YYYY-MM-DD).
*   `citizenships` **SHALL** be an array of valid ISO 3166-1 alpha-3 country codes.
*   `birth_place_country` **SHALL** be a valid ISO 3166-1 alpha-3 country code.
*   `countries_of_residence` **SHALL** be an array of valid ISO 3166-1 alpha-3 country codes.
*   `identity_expiry_date` **SHALL** be a valid ISO 8601 date (YYYY-MM-DD).
*   `ownership_stake` **SHALL** be a decimal number between 25.0 and 100.0, inclusive.
*   `ownership_held_date` **SHALL** be a valid ISO 8601 date (YYYY-MM-DD).
*   `type_of_identity_document` **SHALL** be one of the values defined in Section 2.8.1.
*   Each element in `determination_methodology` **SHALL** be one of the values defined in Section 2.8.2.
*   `unique_personal_identification_number` and `unique_id_number_source` **SHALL** only be present if the information is available.
*   Each attribute **SHALL** appear at most once within its scope (e.g., within a `UBO` object or `OwnershipInfo` object).
*   `issuance_date` and `expiry_date` **SHALL** be valid ISO 8601 DateTimes.
*   `issuance_date` **SHALL** be in the past.
*   `expiry_date` **SHALL** be in the future relative to the `issuance_date`.
*   `attestation_legal_category` **SHALL** be one of "EAA" or  "QEAA".
*   If `trust_anchor_url` is present, it **SHALL** be a valid URI.
*   If `schema_version` is present, it **SHALL** be a non-empty string.

## 3 Attestation encoding

### 3.1 ISO/IEC 18013-5-compliant encoding

ISO/IEC 18013-5 (also called mdoc) is out of scope for this Rulebook, as offline proximity presentation is not a current requirement for the UBO List attestation.

### 3.2 SD-JWT VC-based encoding

The UBO List attestation uses the SD-JWT VC format to allow for selective disclosure of UBO attributes.

**Selective Disclosure:** Top-level claims (e.g., `ubos`, containing the array of UBO objects) **SHALL** be individually selectively disclosable, enabling a legal entity to disclose only the attributes requested by a Relying Party. Attributes nested within a `UBO` object (e.g., `first_names`, `date_of_birth`, `ownership_stake`) **MAY** be individually selectively disclosable as per the attribute encoding table.

The `.` notation is used to indicate the nesting of attributes.

**Verifiable Credential Type (`vct`):** `vct: eu.we-build.ubolist.1`

#### 3.2.1 Attribute Encoding Table

| **Data Identifier**                           | **Attribute identifier**                               | **Encoding format**                     | **Reference/Notes**                                                                                                                                                                        | **Disclosable** |
| :-------------------------------------------- | :----------------------------------------------------- | :-------------------------------------- |:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| :-------------- |
| ubos                                          | `ubos`                                                 | Array [UBO]                             | Array of UBO objects; **SHALL** contain at least one UBO.                                                                                                                                  | MUST            |
| ubo_personal_identification.first_names       | `ubos[n].first_names`                                  | String                                  | The beneficial owner's first names in full (including all given names and middle names)                                                                                                    | MUST            |
| ubo_personal_identification.surnames          | `ubos[n].surnames`                                     | String                                  | The beneficial owner's surnames in full (all family names/last names)                                                                                                                      | MUST            |
| ubo_personal_identification.date_of_birth     | `ubos[n].date_of_birth`                                | String (ISO 8601 YYYY-MM-DD)            | Day, month, and year of birth of the UBO                                                                                                                                                   | MUST            |
| ubo_personal_identification.citizenships      | `ubos[n].citizenships`                                 | Array of Strings (ISO 3166-1 alpha-3)   | Citizenship(s) held by the UBO (one or more nationalities)                                                                                                                                 | MUST            |
| ubo_birthplace.birth_place_locality           | `ubos[n].birth_place_locality`                         | String                                  | Locality (city or town) where the natural person was born                                                                                                                                  | MUST            |
| ubo_birthplace.birth_place_country            | `ubos[n].birth_place_country`                          | String (ISO 3166-1 alpha-3)             | Country where the natural person was born                                                                                                                                                  | MUST            |
| ubo_birthplace.birth_place_region             | `ubos[n].birth_place_region`                           | String                                  | Optional additional detail on the region/state where the UBO was born                                                                                                                      | MAY             |
| ubo_residential_address.residential_street      | `ubos[n].residential_street`                           | String                                  | The street where the UBO currently resides or can be contacted                                                                                                                             | MUST            |
| ubo_residential_address.residential_house_number | `ubos[n].residential_house_number`                   | String                                  | The house/building number where the UBO currently resides or can be contacted                                                                                                              | MUST            |
| ubo_residential_address.residential_city      | `ubos[n].residential_city`                             | String                                  | The city where the UBO currently resides or can be contacted                                                                                                                               | MUST            |
| ubo_residential_address.residential_state     | `ubos[n].residential_state`                            | String                                  | The state, province, or region where the UBO currently resides or can be contacted                                                                                                         | MAY             |
| ubo_residential_address.residential_postal_code | `ubos[n].residential_postal_code`                    | String                                  | The postal code where the UBO currently resides or can be contacted                                                                                                                        | MUST            |
| ubo_residential_address.countries_of_residence | `ubos[n].countries_of_residence`                     | Array of Strings (ISO 3166-1 alpha-3)   | The country or countries where the UBO currently resides or can be contacted                                                                                                               | MUST            |
| ubo_identification.type_of_identity_document  | `ubos[n].type_of_identity_document`                    | String                                  | A value defining the type of the identity document according to the nationality of the UBO (e.g., Passport, National identity card, Driver's license)                                      | MUST            |
| ubo_identification.identity_document_number   | `ubos[n].identity_document_number`                     | String                                  | The number of the identity document (passport number, national ID number, driver's license number, etc.)                                                                                   | MUST            |
| ubo_identification.identity_issuing_country   | `ubos[n].identity_issuing_country`                     | String (ISO 3166-1 alpha-3)             | The country that issued the identity document                                                                                                                                              | MUST            |
| ubo_identification.identity_expiry_date       | `ubos[n].identity_expiry_date`                         | String (ISO 8601 YYYY-MM-DD)            | The expiration date of the identity document                                                                                                                                               | MUST            |
| ubo_identification.unique_personal_identification_number | `ubos[n].unique_personal_identification_number` | String                                  | A government-assigned number uniquely linked to the individual, independent of any specific ID document, and valid for the person's lifetime. Included where available.                    | MAY             |
| ubo_identification.unique_id_number_source    | `ubos[n].unique_id_number_source`                      | String                                  | General description of the source of the unique personal identification number (e.g., "Spanish National ID (DNI)", "French Social Security Number"). Included where available.             | MAY             |
| ubo_ownership_info.determination_methodology  | `ubos[n].ownership_info.determination_methodology`     | Array of Strings (enumeration)          | Specifies the calculation methodology applied (e.g., "Direct ownership", "Control through voting rights"). **SHALL** use codes from Section 2.8.2.                                         | MUST            |
| ubo_ownership_info.ownership_stake            | `ubos[n].ownership_info.ownership_stake`               | Decimal (25.0-100.0)                    | The percentage or level of ownership/control held by the UBO (≥25% per AMLR threshold, but may be higher)                                                                                  | MUST            |
| ubo_ownership_info.ownership_held_date        | `ubos[n].ownership_info.ownership_held_date`           | String (ISO 8601 YYYY-MM-DD)            | Date on which the beneficial interest is held (as of when the UBO calculation was performed)                                                                                               | MUST            |
| issuance_date                                 | `iat`                                                  | Number (Unix timestamp)                 | The date and time when the attestation was issued (ISO 8601); RFC 7519 / Section 2.5                                                                                                       | MUST NOT        |
| expiry_date                                   | `exp`                                                  | Number (Unix timestamp)                 | The date and time when the attestation expires (ISO 8601); RFC 7519 / Section 2.5                                                                                                          | MUST NOT        |
| issuing_entity                                | `iss`                                                  | String (URI or DID)                     | The identifier of the legal entity that issued the attestation (typically the subject entity itself for self-issued attestations, or the QTSP identifier for QEAA). RFC 7519 / Section 2.5 | MUST NOT        |
| attestation_legal_category                    | `attestation_legal_category`                           | String                                  | One of `EAA` or `QEAA` as defined by eIDAS 2                                                                                                                                               | MUST NOT        |
| schema_version                                | `schema_version`                                       | String                                  | Version of the schema used for this attestation.                                                                                                                                           | MAY             |
| trust_anchor_url                              | `trust_anchor_url`                                     | URI                                     | URL where the trust anchor for verifying this attestation can be retrieved.                                                                                                                | MAY             |

**Notes:**

*   **MUST**: The claim **SHALL** be selectively disclosable — the holder **MAY** choose to disclose or withhold this claim when presenting the credential to a Relying Party.
*   **MAY**: The claim **MAY** be selectively disclosable if the issuer supports it, but the holder can choose to disclose or withhold.
*   **MUST NOT**: The claim **SHALL NOT** be selectively disclosable — it is always present in plain text in the JWT header/payload and cannot be withheld by the holder, as it is required for credential verification and trust establishment.
*   `iat`, `exp`, and `iss` follow RFC 7519 standard JWT claim naming conventions.

#### 3.2.2 Status Claim

For SD-JWT VC-compliant UBO List attestations, the attestation **MUST** include a `status` claim if the technical validity period is greater than 24 hours. This claim enables Relying Parties to determine if a credential has been revoked via a status list mechanism, as specified in SD-JWT VC.

The `status` claim **SHALL** be a JSON object with the following members:

*   `type` (string): **SHALL** be `"status-list"`.
*   `status_list_credential` (string, URI): The URI of the Status List Credential document that contains the status bitstring.
*   `status_list_index` (integer, >= 0): The zero-based index into the status list bitstring that corresponds to this credential.
*   `status_purpose` (string): **SHALL** be `"revocation"` for this attestation.

**Example:**

```json
{
  "status": {
 "type": "status-list",
 "status_list_credential": "https://issuer.example.com/status/ubolist/2025",
 "status_list_index": 456,
 "status_purpose": "revocation"
  }
}
```

#### 3.2.3 Example Payload
The following is a non-normative example of a UBO List SD-JWT VC payload:

```
{
  "vct": "eu.we-build.ubolist.1",
  "iss": "https://issuer.example.com",
  "iat": 1673875200,
  "exp": 1705411200,
  "attestation_legal_category": "EAA",
  "schema_version": "1.0",
  "ubos": [
 {
   "first_names": "John",
   "surnames": "Doe",
   "date_of_birth": "1980-05-15",
   "citizenships": ["DEU"],
   "birth_place_locality": "Berlin",
   "birth_place_country": "DEU",
   "birth_place_region": "Berlin",
   "residential_street": "Main Street",
   "residential_house_number": "10",
   "residential_city": "Berlin",
   "residential_state": "Berlin",
   "residential_postal_code": "10115",
   "countries_of_residence": ["DEU"],
   "type_of_identity_document": "National identity card",
   "identity_document_number": "123456789",
   "identity_issuing_country": "DEU",
   "identity_expiry_date": "2030-12-31",
   "unique_personal_identification_number": "DE1234567890123",
   "unique_id_number_source": "German Tax ID",
   "ownership_info": {
     "determination_methodology": ["Direct ownership", "Control through voting rights"],
     "ownership_stake": 35.5,
     "ownership_held_date": "2024-01-01"
   }
 },
 {
   "first_names": "Jane",
   "surnames": "Smith",
   "date_of_birth": "1975-11-20",
   "citizenships": ["FRA"],
   "birth_place_locality": "Paris",
   "birth_place_country": "FRA",
   "residential_street": "Rue de la Paix",
   "residential_house_number": "5",
   "residential_city": "Paris",
   "residential_postal_code": "75002",
   "countries_of_residence": ["FRA"],
   "type_of_identity_document": "Passport",
   "identity_document_number": "ABC987654",
   "identity_issuing_country": "FRA",
   "identity_expiry_date": "2028-06-30",
   "ownership_info": {
     "determination_methodology": ["Indirect ownership"],
     "ownership_stake": 28.0,
     "ownership_held_date": "2023-07-15"
   }
 }
  ],
  "status": {
 "type": "status-list",
 "status_list_credential": "https://issuer.example.com/status/ubolist/2025",
 "status_list_index": 456,
 "status_purpose": "revocation"
  }
}
```
Sample payloads are provided under ../data-schemas/sd-jwt-vc/sample-data/ubolist-sd-jwt-sample.json

#### 3.3 W3C Verifiable Credentials Data Model-based encoding
@TODO — To be discussed: which stakeholders will support this format and which use cases require it.        

## 4 Attestation usage

The UBO List Attestation serves the core AML/CTF compliance requirement of identifying ultimate beneficial owners across European financial and business ecosystems:

*Primary use cases:*
- Bank KYC for Corporate Account Opening (per AMLR Articles 20-25)
- Supplier Onboarding (KYS with UBO Transparency)
- Regulatory Submission for company to Transparency Register  ( Proposed Implementing Act dated 26/11/2025)
- Regulatory Reporting for company (Transparency Register Cross-Reference)
- Ongoing Monitoring (AMLR Article 25)

### 4.1. Issuance process ###

**Issuance Flow:**

*Calculation and Issuance:*
- The legal entity calculates its UBO list by:Applying the ≥25% threshold to the Ownership List (identifying natural persons with ≥25% direct or indirect ownership)
- Analyzing the Control List for natural persons exercising ultimate control through other means (even if ownership <25%)
- Applying AMLR determination methodologies (direct ownership, indirect ownership, legal arrangement roles, nature of control)
- The legal entity self-issues the UBO List Attestation into its Company Wallet OR a QTSP issues the UBO List Attestation to the company's wallet (as a QEAA), certifying the UBO calculation
- Classification: "EAA" (self-issued) or "QEAA (Transparency Reqister/QTSP issued)

### 4.2 Relying Party Obligations ###
When receiving and processing the attestation, a Relying Party SHALL:

A reference to rb-attestation-core verification should be made
### 4.2.1- 4.2.4 - Base verication process

This block should be removed when the core-verification is available
````

The first 4 steps are basic verification - similar for all attestations:
### 4.2.1 Verify Cryptographic Integrity ###
- Validate the digital signature over the attestation using the issuer's public key
- For SD-JWT VC: Verify JWT signature and validate all disclosed claims
### 4.2.2 Validate Issuer ###

@TODO Werner
- Issuer Authentification
- Issuer Identification
- Issuer  Authorization
  - Verify that the issuer is authorized to issue Payment Terms Attestations
  - Check the issuer's credentials against the appropriate trust framework (see Chapter 5)
  - For "EAA": Confirm issuer authorization mechanisms

### 4.2.3 Holder Related check ###
- Revocation status check
  - Query the designated revocation/status mechanism (Cap 6)
  - Treat revoked or suspended attestations as invalid
  - @TODO Forin Check Handle indeterminate status according to organizational risk policy

- Check Temporal Validity ####
  - Validate issuanceDate / iat to ensure the attestation was issued in the past
  - Validate expirationDate / exp to ensure the attestation has not expired
  - Consider attestation age in relation to business risk (e.g., payment terms updated recently vs. stale data)

### 4.2.4  Holder Wallet Related check ###
#### 4.2.4.1.Device binding  ####
@TODO Werner
- avoid copy & reply
- WUA check
````

#### 4.2.5 Validate Integrity Rules ####
- Verify that at least one UBO is present
- Verify that all AMLR Article 62 mandatory attributes are present for each UBO
- Verify that each UBO has at least one determination_methodology

#### 4.2.6 UseCaseSpecific: Cross-Reference with Ownership and Control Lists (AMLR Article 60) ###
AMLR compliance requires independent verification of UBO calculations.

*RPs SHALL:*
- Request Ownership List and Control List in addition to UBO List
- Perform Independent UBO Calculation:Apply ≥25% threshold to Ownership List → Identify natural persons with ≥25% total ownership
- Analyze Control List for natural persons exercising ultimate control (even if <25% ownership)
- Apply AMLR determination methodologies 
- Cross-Check Against Presented UBO List:
  - Compare UBO data: Verify that all independently calculated UBOs appear in the presented UBO List
  - Compare determination methodologies: Verify consistency
  - Compare ownership stakes (if disclosed)
- Discrepancy Handling*
  - If UBOs are missing from presented list → notify entity to recalculate and update
  - If extra UBOs appear in presented list (not in calculated list) → request justification or evidence
  - If discrepancies relate to Transparency Register submission → report to register authority per AMLR Article 60
  - If discrepancies cannot be resolved -> risk cases: apply enhanced due diligence or decline relationship

#### 4.2.7 UseCaseSpecific: UBO Identity Verification (AMLR Article 21 Procedure) ####
For each UBO in the UBO List Attestation, the RP SHALL perform identity verification following this hierarchical procedure:

@TODO Florin Specify the process 

**Step 1: PID-Based Verification (Preferred Method)**
- Request PID Attestation from the UBO (via EUDI Wallet)
- Cross-Check PID Against UBO List :identification & other attributes
- Check PID revocation status via the PID's revocation mechanism
- Validate PID expiry date

**Step 2: non-PID Based Verification ( e.g., mdoc for driver's license, future passport mdoc))**
- Request presentation of identity document attestation
- Cross-Check data against UBO List :identification & other attributes

**Step 3: Identity Document Verification (PoA)**
- Request presentation of identity document attestation (PoA)
- Cross-Check data against UBO List :identification & other attributes

**Step 4: Manual/physical verification (in-person or certified copy)**
- Manual/physical identity document verification (in-person or certified copy)

**Step 5: Unique Personal Identification Number Verification (if available)**
- Check if unique_personal_identification_number is available in UBO List
- If available:Use the unique ID number for identity verification
- Cross-reference with national ID databases (where legally permitted and accessible to RPs)
- Verify unique_id_number_source to understand the number's origin (e.g., Spanish DNI, German Tax ID, French Social Security Number)

## 5 Trust anchors

### 5.1 Trust Model for UBO List Attestations

**For "EAA" - Self-Issued Attestations:**

*The trust model relies on:*
- EUCC prerequisite: The subject entity has a valid EUCC establishing its legal identity
- Cross-verification: RPs independently verify UBO calculations by comparing against Ownership List and Control List
- Transparency Register cross-reference: RPs may cross-check against national Transparency Register submissions

**For "QEAA" Issued Attestations (QEAA):**

*The trust model follows the standard eIDAS trust framework:*
- Certificate Chain Verification: RP verifies the Issuer certificate chain to an eIDAS Trust List trust anchor
- QEAA" Authorization: RP confirms the Issuer is authorized to issue UBO List Attestations ("QEAA")
- Enhanced Assurance: "QEAA" issued UBO Lists provide higher assurance because the QTSP independently verifies the UBO calculation against source data (Ownership/Control Lists, company register data)

### 5.2 Trust Anchor Location Metadata
UBO List Attestations SHOULD include the trust_anchor_url metadata attribute (see Section 2.6).
@Florin -> trust topic 

## 6 Revocation
Details on the revocation mechanisms and processes for UBO List attestations will be completed in a future version of this Rulebook. This will cover how Relying Parties can check the revocation status of an attestation.
@Florin -> revocation  topic

## 7 References
This chapter will be completed in a future version of this Rulebook to include specific references relevant to UBO List attestations.

## 7 Compliance
This chapter will be completed in a future version of this Rulebook.

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
| [SD-JWT VC]	                            | SD-JWT-based Verifiable Credentials (SD-JWT VC). Available: https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/, version draft-ietf-oauth-sd-jwt-vc-09|
