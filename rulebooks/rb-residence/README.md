# WE BUILD Attestation Rulebook for attestations of type *Certificate of Residence (CoR)*

*This rulebook is derived from the WE BUILD v1 Attestation Rulebook Template and profiles the Certificate of Residence (CoR) attestation guideline for bank account onboarding of natural persons within the WE BUILD Large-Scale Pilot (LSP).*

*This is a working document that holds no legal value and does not reflect any common agreement or position of the co-legislators or of the WE BUILD consortium. It presents a state-of-play of ongoing work and should not be considered final.*

**Authors:**

* \[Uwe Pfizenmaier, IDnow]

**Previous Authors:**

* \[Uwe Pfizenmaier, IDnow (all versions)]

| Version | Date       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 0.1     | 12-02-2026 | Initial conversion from CoR attestation description (WE BUILD LSP) into WE BUILD Rulebook format.                                                                                                                                                                                                                                                                                                                                                                                                            |
| 0.2     | 30-06-2026 | Incorporated validation corrections: added `cryptographically_bound_to` to § 2.4; clarified `resident_address` encoding difference across formats (§ 2.2, § 3.2); qualified IR-03 for optional `resident_state`; strengthened claim-name alignment note in § 3.2; updated trust anchor section with forward-looking production guidance (§ 5); updated compliance table (§ 7).                                                                                                                               |
| 0.3     | 01-07-2026 | Removed `personal_administrative_number` and `tax_identification_number` (§ 2.3) as redundant given mandatory cryptographic binding to the PID (§ 4.4); removed corresponding entries from §§ 3.1/3.2 encoding tables. Upgraded § 4.2 relying-party PID request/verification to SHALL. Retained `family_name`, `given_name`, `birth_date` as mandatory per ARB\_16/17 (subject identity attributes SHALL be included in the attestation itself, independent of PID binding). Updated compliance table (§ 7). |

**Feedback:** \[<uwe.pfizenmaier@idnow.io>]

***

## 1 Introduction

### 1.1 Document scope and purpose

This rulebook defines functional, semantic, and technical requirements for a **Certificate of Residence (CoR)** attestation used in the onboarding of a natural person as a retail banking customer. The attestation is designed for issuance into, and presentation from, a European Digital Identity Wallet (EUDI Wallet) within the WE BUILD Large-Scale Pilot (LSP).

**What the attestation expresses:** The CoR attestation provides structured, verifiable evidence of a natural person's usual place of residence (or, where no fixed residential address exists with legitimate residence in the Union, the postal address at which the person can be reached), bound to their identity.

**Issuers, holders, and relying parties:**

* *Issuers:* Public administrations authorised by Member State national governance frameworks as authentic sources for residential address data (e.g. population registers, civil registries, tax authorities, municipal address registers).
* *Holders:* Natural persons who are customers or prospective customers of obliged entities.
* *Relying parties:* Obliged entities (credit and financial institutions and other entities subject to EU anti-money laundering and counter-terrorist-financing rules) performing Customer Due Diligence (CDD).

**Primary use cases:**

1. Remote or semi-remote opening of a payment or current account for a natural person, where the obliged entity relies on PID and CoR attestations presented from the EUDI Wallet to satisfy identification and residential address verification requirements under AMLR.
2. Periodic review and information update processes (e.g. "KYC refresh").

**Source material:** This rulebook builds on and profiles the generic Certificate of Residence (CoR) attestation guideline developed in earlier large-scale pilots. Where not explicitly amended or extended here, the provisions of that generic CoR guideline remain applicable. Attribute proofing requirements are based on ETSI TS 119 461 v2.1.1 clauses 8.2.6/8.3.6 (trusted register), 8.2.7/8.3.7 (proof of access), and 8.2.8/8.3.8 (documents and attestations).

**Relationship to AMLR:** This profile tailors the attribute set, integrity rules, and usage context to the specific requirements of bank account onboarding for a natural person under Regulation (EU) 2024/1620 (AMLR).

### 1.2 Document structure

* **Chapter 2** defines attestation attributes and metadata in an encoding-independent manner, including code lists (Section 2.8) and integrity rules (Section 2.9).
* **Chapter 3** specifies encoding for SD-JWT VC (primary), ISO/IEC 18013-5 (mdoc), and W3C VCDM v2.0, with illustrative examples.
* **Chapter 4** specifies attestation usage, relying-party obligations, presentation requirements, and device binding.
* **Chapter 5** defines trust anchor provision and verification mechanisms.
* **Chapter 6** defines attestation revocation.
* **Chapter 7** provides compliance information with respect to the ARF and EUDI framework.
* **Chapter 8** lists references.

### 1.3 Key words

This document uses the capitalised key words 'SHALL', 'SHOULD' and 'MAY' as specified in \[RFC 2119], i.e., to indicate requirements, recommendations and options specified in this document. In addition, 'must' (non-capitalised) is used to indicate an external constraint, i.e., a requirement that is not mandated by this document, but, for instance, by an external document (such as AMLR or the ARF). The word 'can' indicates a capability, whereas other words such as 'will', and 'is' or 'are' are intended as statements of fact.

### 1.4 Terminology

This document uses the terminology specified in Annex 1 of the ARF and in the generic CoR attestation guideline. In addition, "obliged entity" is used in the meaning of \[AMLR] to denote credit and financial institutions and other entities subject to EU anti-money laundering and counter-terrorist-financing rules.

***

## 2 Attestation attributes and metadata

### Chapter overview and requirements

This chapter defines all attributes and metadata that a CoR attestation MAY contain, in an encoding-independent manner. Each attribute is classified as mandatory, optional, or conditional. Definitions align with the generic CoR guideline and the AMLR minimum information requirements.

**Requirements applicable to CoR as a QEAA (where applicable):**

* An indication that the attestation has been issued as a QEAA SHALL be included (ARB\_11, Annex V point a of \[European Digital Identity Regulation]).
* Attributes or metadata representing issuer identity and country SHALL be included (ARB\_13, Annex V point b).
* Attributes representing subject identity SHALL be included (ARB\_16, Annex V point c).
* Validity period metadata SHALL be included (ARB\_18, Annex V point e).
* Trust anchor location SHALL be indicated (ARB\_20, Annex V point h).

**Requirements applicable to CoR as a PuB-EAA or non-qualified EAA** follow the corresponding provisions of Annex VII and ARB\_12–ARB\_21 of \[Topic 12] respectively, and SHALL be fulfilled where the CoR attestation is issued under the relevant legal category.

### 2.1 Introduction

The CoR attestation is designed to support AML/CFT CDD obligations. It is used together with a PID attestation: the PID identifies and verifies the natural person customer, while the CoR verifies the customer's residential address and attributes needed for risk assessment.

The CoR attestation may be issued as a **QEAA**, **PuB-EAA**, or **non-qualified EAA**, depending on the issuing authority and Member State governance framework. This rulebook therefore defines the attribute `attestation_legal_category` (Section 2.5), which SHALL have the value `"QEAA"`, `"PuB-EAA"`, or `"non-qualified-EAA"` as appropriate.

The attestation namespace and type identifier is: **`eu.europa.ec.eudi.cor.1`**.

The attribute set is structured in two groups:

1. **General (identity-linking) attributes** — enabling identification of the natural person, aligned with PID attributes (Section 2.2 and 2.3).
2. **Residential address attributes** — enabling proof of the natural person's usual place of residence (Section 2.2).

All `tstr` attributes SHALL have a maximum length of 150 characters. The authorised character set for CoR attestations SHALL be Latin Alphabet No. 1 as specified in ISO/IEC 8859-1. Multiple values per claim are not allowed.

### 2.2 Mandatory attributes

| **Data Identifier**     | **Semantic Reference**           | **Definition**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | **Data type**                    | **Example value**                     |
| ----------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- | ------------------------------------- |
| `family_name`           | ARF PID attribute: `family_name` | Current last name(s) or surname(s) of the User.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | tstr                             | "Mill"                                |
| `given_name`            | ARF PID attribute: `given_name`  | Current first name(s), including middle name(s), of the User.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | tstr                             | "Lyla-Rose"                           |
| `birth_date`            | ARF PID attribute: `birth_date`  | Day, month, and year on which the User was born. If unknown, an approximate date of birth.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | full-date                        | "1972-03-04"                          |
| `birth_place`           | ARF PID attribute: `birth_place` | Place of birth of the User (town/city and country).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | tstr                             | "London"                              |
| `nationality`           | ARF PID attribute: `nationality` | Nationality of the User as an Alpha-2 country code (ISO 3166-1). Where a User has multiple nationalities and the provider attests to all of them, all nationalities MAY be included.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | tstr                             | "BE"                                  |
| `resident_country`      | eIDAS/ARF residence attribute    | Country of the User's usual place of residence as an Alpha-2 country code (ISO 3166-1). Where the User has no fixed residential address with legitimate residence in the Union, this refers to the country of the main postal address at which the person can be reached.                                                                                                                                                                                                                                                                                                                                                                                                                   | tstr                             | "LU"                                  |
| `resident_city`         | eIDAS/ARF residence attribute    | City, town, or locality of the User's usual place of residence. Where the User has no fixed residential address, this refers to the city/town of the postal address at which the person can be reached.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | tstr                             | "Schifflange"                         |
| `resident_postal_code`  | eIDAS/ARF residence attribute    | Postal code of the User's usual place of residence. Where the User has no fixed residential address, this refers to the postal code of the postal address at which the person can be reached.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | tstr                             | "L-3851"                              |
| `resident_street`       | eIDAS/ARF residence attribute    | Street name (thoroughfare) of the User's usual place of residence. Where the User has no fixed residential address, this refers to the street name of the postal address at which the person can be reached.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | tstr                             | "Rue de Kayl"                         |
| `resident_house_number` | eIDAS/ARF residence attribute    | House number, building number, and/or other numeric designator that uniquely identifies the residential building in the relevant street. Where the User has no fixed residential address, this refers to the equivalent number in the postal address at which the person can be reached.                                                                                                                                                                                                                                                                                                                                                                                                    | tstr                             | "2"                                   |
| `resident_address`      | eIDAS/ARF residence attribute    | Complete address of the User's usual place of residence as a single human-readable string, typically combining `resident_street`, `resident_house_number`, `resident_postal_code`, `resident_city`, `resident_state`, and `resident_country`. Where the User has no fixed residential address, this contains the full postal address at which the person can be reached. **Encoding note:** In mdoc (ISO/IEC 18013-5) this attribute is encoded as a flat `tstr`. In SD-JWT VC it is encoded as a nested JSON object with Recursive Disclosures, allowing individual address sub-claims to be selectively disclosed independently. See §§ 3.1 and 3.2 for format-specific encoding details. | tstr (mdoc) / object (SD-JWT VC) | "2 Rue de Kayl L-3851 Schifflange LU" |

### 2.3 Optional attributes

| **Data Identifier** | **Semantic Reference**        | **Definition**                                                                                                                                                                                                                                                                                                                                                                                                                                                     | **Data type** | **Example value**                    |
| ------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------- | ------------------------------------ |
| `resident_state`    | eIDAS/ARF residence attribute | Name or code of the state/province/region of the User's usual place of residence, where applicable (e.g. "Bavaria", "Île-de-France"). Where the User has no fixed residential address, this refers to the corresponding subdivision of the postal address. If the concept of state/region is not used in the national addressing scheme, this attribute SHALL be omitted; issuers SHALL NOT insert artificial placeholders (e.g. 'N/A') or duplicate other fields. | tstr          | "N/A (omitted where not applicable)" |
| `arrival_date`      | N/A                           | Day, month, and year on which the User arrived at the current usual place of residence, if known.                                                                                                                                                                                                                                                                                                                                                                  | full-date     | "2024-11-05"                         |

> **Removed in v0.3 —** **`personal_administrative_number`** **and** **`tax_identification_number`:** These attributes were removed from the CoR attribute set. The CoR attestation is mandatorily cryptographically bound to a PID attestation on the same Wallet Unit (see § 4.4, `cryptographically_bound_to`, § 2.4), and § 4.2 now requires relying parties to always request and verify the PID together with the CoR. The PID is the authoritative, ARF-defined carrier of the User's national identification/administrative number and tax identifier where such attributes are relevant; duplicating them in the CoR would create redundant, potentially inconsistent copies of identity data that is already available, verified, and bound via the PID. Where a relying party's use case requires this information, it SHALL obtain it from the presented PID rather than from the CoR.

### 2.4 Conditional attributes

The following attribute is conditional: it SHALL be present when the CoR attestation is device-bound and cryptographically linked to another attestation on the same Wallet Unit (see § 4.4 and ARB\_28 of \[Topic 12]).

| **Data Identifier**          | **Semantic Reference**    | **Definition**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | **Data type** | **Example value**           |
| ---------------------------- | ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | --------------------------- |
| `cryptographically_bound_to` | ARF ARB\_28 (\[Topic 12]) | Indicates the attestation type or `vct` of the other attestation on the same Wallet Unit to which this CoR attestation is cryptographically bound. When the CoR attestation is bound to a PID, this attribute SHALL be set to `"eu.europa.ec.eudi.pid.1"` (for mdoc) or `"urn:eudi:pid:1"` (for SD-JWT VC). The attribute SHALL be present when device binding is applied and cryptographic binding to the PID is required by the relying party or by Member State governance rules. It SHALL be omitted when the attestation is not device-bound. | tstr          | `"eu.europa.ec.eudi.pid.1"` |

### 2.5 Mandatory metadata

| **Data Identifier**          | **Semantic Reference**                                                           | **Definition**                                                                                                                                                                        | **Data type** | **Example value** |
| ---------------------------- | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ----------------- |
| `attestation_legal_category` | ARF / \[European Digital Identity Regulation] Annex V point a, Annex VII point a | Indicates the legal category of the attestation. SHALL be set to `"QEAA"`, `"PuB-EAA"`, or `"non-qualified-EAA"` depending on the issuer's legal status. Not selectively disclosable. | tstr          | "QEAA"            |
| `issuance_date`              | ARF attestation metadata                                                         | Day, month, and year on which the CoR attestation was issued.                                                                                                                         | full-date     | "2025-01-29"      |
| `issuing_authority`          | ARF attestation metadata                                                         | Name of the authority or body that issued the CoR attestation.                                                                                                                        | tstr          | "CTIE"            |
| `issuing_country`            | ARF attestation metadata                                                         | Issuing country as an Alpha-2 country code as specified in ISO 3166-1.                                                                                                                | tstr          | "LU"              |

### 2.6 Optional metadata

| **Data Identifier** | **Semantic Reference**   | **Definition**                                                           | **Data type** | **Example value** |
| ------------------- | ------------------------ | ------------------------------------------------------------------------ | ------------- | ----------------- |
| `expiry_date`       | ARF attestation metadata | Day, month, and year after which the CoR attestation is no longer valid. | full-date     | "2026-04-03"      |

### 2.7 Conditional metadata

No conditional metadata are defined for this attestation type at this time.

### 2.8 Code lists

| **Field name**               | **Allowed values**                                     | **Meaning**                                                                                                                                                                                       | **Source / vocabulary**                                          | **Notes / extensibility**                                                                                    |
| ---------------------------- | ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `nationality`                | ISO 3166-1 Alpha-2 codes (e.g. `"BE"`, `"DE"`, `"LU"`) | Two-letter country code indicating the nationality of the User. Where a User holds multiple nationalities, each SHOULD be represented as a separate value if the provider attests to all of them. | ISO 3166-1 (International Organization for Standardization)      | The list is normatively defined by ISO 3166; no additional values SHALL be used unless ISO 3166 is extended. |
| `resident_country`           | ISO 3166-1 Alpha-2 codes (e.g. `"DE"`, `"FR"`, `"LU"`) | Two-letter code identifying the country of usual residence or principal postal address.                                                                                                           | ISO 3166-1                                                       | No extension allowed; values not in ISO 3166-1 SHALL NOT be used.                                            |
| `issuing_country`            | ISO 3166-1 Alpha-2 codes                               | Two-letter code identifying the country of the issuing authority.                                                                                                                                 | ISO 3166-1                                                       | No extension allowed.                                                                                        |
| `attestation_legal_category` | `"QEAA"`, `"PuB-EAA"`, `"non-qualified-EAA"`           | Indicates whether the attestation is a Qualified EAA, a Public Body EAA, or a non-qualified EAA, as defined under \[European Digital Identity Regulation].                                        | ARF / \[European Digital Identity Regulation] Annex V, Annex VII | No additional values SHALL be introduced. Value is determined by the legal status of the issuer.             |

### 2.9 Integrity rules

| **Rule ID** | **Rule statement**                                                                                                                                                                                                                                                                                                                                                                                                                                                           | **Why it exists**                                                                             | **Where enforced**                                   | **Verifier / issuer behavior on failure**                                                                                       |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| IR-01       | If `arrival_date` is present, it SHALL be prior to or equal to `issuance_date`.                                                                                                                                                                                                                                                                                                                                                                                              | Ensures temporal consistency — a person cannot have arrived after the attestation was issued. | Issuer business rules; verifier business validation. | Issuer SHALL reject inconsistent dates; verifier SHALL treat the attestation as invalid for the transaction.                    |
| IR-02       | `resident_country`, `resident_street`, `resident_house_number`, and `resident_address` SHALL contain non-empty values, unless an individual element is not applicable in the jurisdiction concerned. In the latter case, the issuer SHALL apply nationally agreed fall-back rules.                                                                                                                                                                                           | AMLR CDD requires a complete, usable address representation.                                  | Issuer business rules; schema validation.            | Issuer SHALL reject attestations with empty mandatory address elements in the absence of an applicable national fall-back rule. |
| IR-03       | `resident_address` SHALL be consistent with the granular `resident_*` elements that are present in the attestation (i.e. it SHOULD be a concatenation that does not contradict `resident_city`, `resident_postal_code`, `resident_street`, `resident_house_number`, and, **where present**, `resident_state`). This rule applies only to attributes that are actually included; the absence of optional attributes such as `resident_state` does not constitute a violation. | Prevents contradictory address representations that could undermine CDD reliability.          | Issuer business rules; verifier business validation. | Verifier SHOULD flag inconsistencies and MAY reject the attestation for CDD purposes if the discrepancy is material.            |
| IR-04       | A postal box or similar descriptor, if used in `resident_address`, SHALL NOT be the only information from which the person's location can be derived for CDD purposes. Where a PO box is involved, the issuer SHOULD also provide at least `resident_country` and `resident_city`, and, where available, `resident_postal_code`.                                                                                                                                             | A PO box alone is insufficient to establish actual place of residence for AMLR CDD.           | Issuer business rules.                               | Issuer SHALL ensure at least `resident_country` and `resident_city` are present alongside any PO-box-based `resident_address`.  |
| IR-05       | If `resident_state` is not used in the national addressing scheme, the issuer SHALL omit this attribute entirely. Issuers SHALL NOT insert artificial placeholders (e.g. `'N/A'`) or duplicate other fields (e.g. city, country) to populate `resident_state`.                                                                                                                                                                                                               | Prevents misleading or spurious data entries in address fields.                               | Issuer business rules.                               | Issuer SHALL omit the field; verifiers encountering a placeholder value SHOULD treat it as absent.                              |

***

## 3 Attestation encoding

### 3.1 ISO/IEC 18013-5-compliant encoding (mdoc)

The CoR attestation MAY be issued in ISO/IEC 18013-5-compliant mdoc format where proximity presentation (without internet) is required by the deployment context. Member States and issuers SHALL determine, in accordance with ARB\_02 of \[Topic 12], whether proximity presentation is a required capability for their deployment of the CoR attestation.

**Document type:** `eu.europa.ec.eudi.cor.1`

**General encoding rules:**

* `tstr`, `uint`, `bstr`, `bool`, and `tdate` are CDDL representation types defined in \[RFC 8610].
* A `tstr` SHALL be encoded in UTF-8 (as specified in \[RFC 8949]) and SHALL support the full Unicode range within the Latin Alphabet No. 1 (ISO/IEC 8859-1) character set constraint for CoR.
* All attributes with encoding type `tstr` SHALL have a maximum length of 150 characters.
* `full-date` is encoded as `full-date = #6.1004(tstr)`, where tag 1004 is specified in \[RFC 8943].
* In accordance with [RFC 8949] section 3.4.1, a `tdate` attribute SHALL contain a date-time string as specified in \[RFC 3339].
* Fractions of seconds SHALL NOT be used; local offsets from UTC SHALL NOT be used; the time-offset SHALL be `"Z"`.
* **`resident_address`** **encoding (mdoc):** In ISO/IEC 18013-5-compliant mdoc, `resident_address` is encoded as a flat `tstr` containing the full address as a human-readable string. This differs from the SD-JWT VC encoding where it is a nested JSON object with Recursive Disclosures (see § 3.2). Issuers SHALL ensure that the string value in mdoc is consistent with the granular `resident_*` fields per IR-03.

**Attribute encoding table:**

| **Data Identifier**          | **Attribute identifier**     | **Encoding format**                                                         | **Namespace**             |
| ---------------------------- | ---------------------------- | --------------------------------------------------------------------------- | ------------------------- |
| `family_name`                | `family_name`                | tstr                                                                        | `eu.europa.ec.eudi.cor.1` |
| `given_name`                 | `given_name`                 | tstr                                                                        | `eu.europa.ec.eudi.cor.1` |
| `birth_date`                 | `birth_date`                 | full-date                                                                   | `eu.europa.ec.eudi.cor.1` |
| `birth_place`                | `birth_place`                | tstr                                                                        | `eu.europa.ec.eudi.cor.1` |
| `nationality`                | `nationality`                | tstr                                                                        | `eu.europa.ec.eudi.cor.1` |
| `resident_country`           | `resident_country`           | tstr                                                                        | `eu.europa.ec.eudi.cor.1` |
| `resident_state`             | `resident_state`             | tstr                                                                        | `eu.europa.ec.eudi.cor.1` |
| `resident_city`              | `resident_city`              | tstr                                                                        | `eu.europa.ec.eudi.cor.1` |
| `resident_postal_code`       | `resident_postal_code`       | tstr                                                                        | `eu.europa.ec.eudi.cor.1` |
| `resident_street`            | `resident_street`            | tstr                                                                        | `eu.europa.ec.eudi.cor.1` |
| `resident_house_number`      | `resident_house_number`      | tstr                                                                        | `eu.europa.ec.eudi.cor.1` |
| `resident_address`           | `resident_address`           | tstr (flat human-readable string; see encoding note in § 3.1 general rules) | `eu.europa.ec.eudi.cor.1` |
| `arrival_date`               | `arrival_date`               | full-date                                                                   | `eu.europa.ec.eudi.cor.1` |
| `attestation_legal_category` | `attestation_legal_category` | tstr                                                                        | `eu.europa.ec.eudi.cor.1` |
| `issuance_date`              | `issuance_date`              | full-date                                                                   | `eu.europa.ec.eudi.cor.1` |
| `expiry_date`                | `expiry_date`                | full-date                                                                   | `eu.europa.ec.eudi.cor.1` |
| `issuing_authority`          | `issuing_authority`          | tstr                                                                        | `eu.europa.ec.eudi.cor.1` |
| `issuing_country`            | `issuing_country`            | tstr                                                                        | `eu.europa.ec.eudi.cor.1` |

\[RULEBOOK AUTHOR TO PROVIDE AN EXAMPLE OF FULL OR PARTIAL mDOC OF THE ATTESTATION]

### 3.2 SD-JWT VC-based encoding

The CoR attestation SHALL be issued in SD-JWT VC-compliant format in conformance with the SD-JWT VCs profile specified in \[HAIP] (ARB\_01b of \[Topic 12]). Selective Disclosure SHALL be used (see Section 4).

**Verifiable Credential Type (`vct`):** `eu.europa.ec.eudi.cor.1`

**General encoding rules:**

* JSON attributes SHALL be encoded as specified in \[RFC 8259].
* `full-date` values SHALL conform to \[RFC 3339] full-date format.
* All `string` attributes SHALL have a maximum length of 150 characters.
* **`resident_address`** **encoding (SD-JWT VC):** In SD-JWT VC, `resident_address` is encoded as a **nested JSON object** with Recursive Disclosures, enabling individual address sub-claims (`resident_street`, `resident_house_number`, `resident_postal_code`, `resident_city`, `resident_state`, `resident_country`) to be selectively disclosed independently. This differs from the mdoc encoding where `resident_address` is a flat `tstr` (see § 3.1). Issuers SHALL ensure consistency between the nested sub-claims and the flat `resident_address` value per IR-03.

**IANA-registered / well-known claims:**

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Reference / Notes**  | **Disclosable** |
| ------------------- | ------------------------ | ------------------- | ---------------------- | --------------- |
| `family_name`       | `family_name`            | string              | Section 5.1 of \[OIDC] | MUST            |
| `given_name`        | `given_name`             | string              | Section 5.1 of \[OIDC] | MUST            |
| `birth_date`        | `birth_date`             | string (full-date)  | \[RFC 3339]            | MUST            |

**Private claim names specific to CoR attestation type:**

| **Data Identifier**          | **Attribute identifier**     | **Encoding format** | **Notes**                                                                                                                                                                                                                                                                                    | **Disclosable** |
| ---------------------------- | ---------------------------- | ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| `birth_place`                | `birth_place`                | string              | Place of birth                                                                                                                                                                                                                                                                               | MUST            |
| `nationality`                | `nationality`                | string              | ISO 3166-1 Alpha-2                                                                                                                                                                                                                                                                           | MUST            |
| `resident_country`           | `resident_country`           | string              | ISO 3166-1 Alpha-2                                                                                                                                                                                                                                                                           | MUST            |
| `resident_state`             | `resident_state`             | string              | Omit if not applicable in jurisdiction                                                                                                                                                                                                                                                       | MUST            |
| `resident_city`              | `resident_city`              | string              | <br />                                                                                                                                                                                                                                                                                       | MUST            |
| `resident_postal_code`       | `resident_postal_code`       | string              | <br />                                                                                                                                                                                                                                                                                       | MUST            |
| `resident_street`            | `resident_street`            | string              | <br />                                                                                                                                                                                                                                                                                       | MUST            |
| `resident_house_number`      | `resident_house_number`      | string              | <br />                                                                                                                                                                                                                                                                                       | MUST            |
| `resident_address`           | `resident_address`           | object              | Nested SD-JWT object with Recursive Disclosures (see Section 4); contains `resident_street`, `resident_house_number`, `resident_postal_code`, `resident_city`, `resident_state`, `resident_country`, and `resident_address` (full string) as individually selectively disclosable sub-claims | MUST            |
| `arrival_date`               | `arrival_date`               | string (full-date)  | \[RFC 3339]                                                                                                                                                                                                                                                                                  | MUST            |
| `attestation_legal_category` | `attestation_legal_category` | string              | Defined in WE BUILD Rulebook template; value: `"QEAA"`, `"PuB-EAA"`, or `"non-qualified-EAA"`                                                                                                                                                                                                | MUST NOT        |
| `issuance_date`              | `issuance_date`              | string (full-date)  | Attestation metadata                                                                                                                                                                                                                                                                         | MUST NOT        |
| `expiry_date`                | `expiry_date`                | string (full-date)  | Attestation metadata                                                                                                                                                                                                                                                                         | MUST NOT        |
| `issuing_authority`          | `issuing_authority`          | string              | Attestation metadata                                                                                                                                                                                                                                                                         | MUST NOT        |
| `issuing_country`            | `issuing_country`            | string              | ISO 3166-1 Alpha-2; attestation metadata                                                                                                                                                                                                                                                     | MUST NOT        |

**Example — JWT Claim Set (issuer payload):**

```json
{
  "vct": "eu.europa.ec.eudi.cor.1",
  "iss": "https://ctie.etat.lu",
  "issuing_authority": "CTIE",
  "issuing_country": "LU",
  "attestation_legal_category": "QEAA",
  "iat": 1738147797,
  "exp": 1738183797,
  "nbf": 1738148097,
  "_sd_alg": "sha-256",
  "_sd": [
    "G22coLkZdH6gGqWHlgbYXp8K194YREJwpVdfxk8IBFc",
    "3CEVLuh0JiwrS_5ERgn2lYohk_g-G6Yu_VfcAQDG9xg",
    "ZeKw7C-JDLv_0S_khqhJM7GLJPM_v6MA2KLillGGmEk",
    "MMp6Y6XpR4mv3YEUZVFB969mMTTIapFk60DYih0zsmQ",
    "6y1MJKyX0LEjD1zK-VOQrDj3_VH7yNBraXmofT2okjk",
    "NE2gFqsj27enkQ4ahcHKMPtqXv2y8Q_vGf30J0N5XBg",
    "-eMdNZWQi2JluPKSE4B2ODCeIrIT46h-mq1NjOrDNN0",
    "ad0vpVyDzLaLhB8nRbqIq8iTnMqq7GfCnFnu4VMUfnA",
    "dRNEYSBhXeG-lK7VLDkvCMwmMkq4aW-LcaUOGoox2-M",
    "V9Pc6SDxByKaH9ES2ABDRUKj8jVtHfwVaZRDDb1-CTI",
    "wdxxiUyZjrS_iN8nFfRHBfoejwJN7ClfPX38JUSuFaw"
  ],
  "cnf": {
    "jwk": {
      "crv": "P-256",
      "kty": "EC",
      "x": "wUuP2OlwHefeE-Y16Wj7PHAzZ0JAQyevqWMfd5-KmKY",
      "y": "YW-b8O3Uk3NUrk9oZpAT1laPeAgiNQwDcotWiwBFQ6E"
    }
  }
}
```

**Example — Disclosures included in the example token:**

| Salt                     | Claim name                             | Value                                                          |
| ------------------------ | -------------------------------------- | -------------------------------------------------------------- |
| `_uI5Hy3yyjZLaORsgcBdlA` | `family_name`                          | "Mill"                                                         |
| `qt70iZ9lWAZwSH8m_0nXdA` | `given_name`                           | "Lyla-Rose"                                                    |
| `lxg3lbBA6KLiiKRg5iV3Gg` | `birth_date`                           | "1972-03-04"                                                   |
| `Coc7wXcV1bbpb06dSTDf9g` | `birth_place`                          | "London"                                                       |
| `HsR2WuXFitJBt1f5r0kTLA` | `nationality`                          | "BE"                                                           |
| `OEKDEAnqnuz8sxfmNMZvzw` | `issuance_date`                        | "2025-01-29"                                                   |
| `lfZohb1eaqKxi_zD21hwVA` | `arrival_date`                         | "2024-11-05"                                                   |
| `bWdYchYa616Um1LYyPKlzw` | `issuing_authority`                    | "CTIE"                                                         |
| `ZoOcf7tL1M2nYqw3i8QlHg` | `issuing_country`                      | "LU"                                                           |
| `k7BhU8n7KY1QR7MTbXNu7A` | `residence_address`                    | `{"_sd": [...]}` (nested SD object with recursive disclosures) |
| `1pcpt9V7WdDBsLc6Dg-T4A` | `thoroughfare` (= `resident_street`)   | "Rue de Kayl"                                                  |
| `Gj6pzTgndOecSArhx9kvZg` | `post_code` (= `resident_postal_code`) | "L-3851"                                                       |
| `BCW4wycy-LaClG3oM20ZWQ` | `post_name` (= `resident_city`)        | "Schifflange"                                                  |
| `zdk0DOV2_XVRzGaIrF5elw` | `admin_unit_L1` (= `resident_country`) | "LU"                                                           |
| `Ii3lJ5cvv3mZcD21vtFf-w` | `full_address` (= `resident_address`)  | "2 Rue de Kayl L-3851 Schifflange LU"                          |
| `bdoc-MYdOK14JWi1ez36jQ` | `gender`                               | 0                                                              |

> **Note — claim name alignment (OPEN ISSUE):** The claim identifiers used in the example above (e.g. `thoroughfare`, `post_code`, `post_name`, `admin_unit_L1`, `full_address`) reflect naming conventions from the source WE BUILD pilot example and **do not match** the normative attribute identifiers defined in Section 2 (e.g. `resident_street`, `resident_postal_code`, `resident_city`, `resident_country`, `resident_address`). Conforming implementations SHALL use the normative identifiers from Section 2. The WE BUILD consortium SHOULD resolve this alignment in the next revision of the generic CoR guideline and update the examples in this rulebook accordingly. Until resolved, issuers using the pilot naming convention SHOULD document the mapping explicitly in their system documentation.

**Example — Full issued SD-JWT VP Token (base64url-encoded):**

```
eyJ0eXAiOiJ2YytzZC1qd3QiLCJhbGciOiJFUzI1NiJ9.eyJfc2QiOlsiRzIyY29Ma1pkSDZnR3FXSGxnYllYcDhL
MTk0WVJFSndwVmRmeGs4SUJGYyIsIjNDRVZMdWgwSml3clNfNUVSZ24ybFlvaGtfZy1HNll1X1ZmY0FRREc5eGci
LCJaZUt3N0MtSkRMdl8wU19raHFoSk03R0xKUE1fdjZNQTJLTGlsbEdHbUVrIiwiTU1wNlk2WHBSNG12M1lFVVpW
RkI5NjltTVRUSWFwRms2MERZaWgwenNtUSIsIjZ5MU1KS3lYMExFakQxekstVk9RckRqM19WSDd5TkJyYVhtb2ZU
Mm9ramsiLCJORTJnRnFzajI3ZW5rUTRhaGNIS01QdHFYdjJ5OFFfdkdmMzBKME41WEJnIiwiLWVNZE5aV1FpMkps
dVBLU0U0QjJPRENlSXJJVDQ2aC1tcTFOak9yRE5OMCIsImFkMHZwVnlEekxhTGhCOG5SYnFJcThpVG5NcXE3R2ZD
bkZudTRWTVVmbkEiLCJkUk5FWVNCaFhlRy1sSzdWTERrdkNNd21Na3E0YVctTGNhVU9Hb294Mi1NIiwid2R4eGlV
eVpqclNfaU44bkZmUkhCZm9landKTjdDbGZQWDM4SlVTdUZhdyIsIlY5UGM2U0R4QnlLYUg5RVMyQUJEUlVLajhq
VnRIZndWYVpSRERiMS1DVEkiXSwi...
[full token as provided in source document]
```

### 3.3 W3C Verifiable Credentials Data Model-based encoding

The CoR attestation MAY be issued in W3C VCDM v2.0-compliant format. Note that, per ARB\_01a of \[Topic 12], only a **non-qualified EAA** can use this format.

\[RULEBOOK AUTHOR TO PROVIDE HUMAN-READABLE EXAMPLE OF THE ISSUED ATTESTATION IN W3C VCDM FORMAT]

\[RULEBOOK AUTHOR TO PROVIDE AN EXAMPLE OF THE PROOF TYPE]

Tables analogous to those in Section 3.2 SHALL be defined, referencing documents approved by an EU standardisation body or the European Digital Identity Cooperation Group as required by ARB\_04 of \[Topic 12].

***

## 4 Attestation usage

### 4.1 Primary use cases

1. **Bank account onboarding:** Remote or semi-remote opening of a payment or current account for a natural person, where the obliged entity relies on PID and CoR attestations presented from the EUDI Wallet to satisfy AMLR CDD identification and residential address verification requirements.
2. **KYC refresh:** Periodic review and update of residential address information, enabled by re-issuance of the CoR attestation when the customer updates their address and obtains a newly issued attestation.

### 4.2 Relying party obligations

* Relying parties (obliged entities) SHALL request and verify a PID attestation alongside the CoR attestation (see ARB\_27 of \[Topic 12]). Since the CoR attestation no longer independently carries `personal_administrative_number` or `tax_identification_number` (removed in v0.3; see § 2.3 rationale), and its identity attributes are cryptographically bound to the PID (§ 4.4), the PID SHALL always be requested and verified together with the CoR to establish the natural person's full identity context. The PID is used to identify and verify the natural person customer (e.g. name, date and place of birth, and, where applicable, national identification/tax numbers); the CoR attestation verifies the residential address.
* Obliged entities remain responsible for determining whether the CoR issuer constitutes an acceptable and sufficiently reliable source for CDD, taking into account their risk-based approach and applicable supervisory expectations.
* The CoR attestation does not replace the obliged entity's responsibility to perform ongoing monitoring or to keep customer information up to date.
* Relying parties SHALL verify the attestation signature and check the validity period metadata (issuance date and, where present, expiry date).
* CoR attestation attributes SHALL be released only in a VP Token, as specified in \[OpenID4VP].

### 4.3 Presentation requirements

* **Selective Disclosure** SHALL be used for the CoR attestation (ARF section 5.3).
* **SD-JWT with Recursive Disclosures** SHOULD be used for the `resident_address` object, enabling individual address sub-claims to be selectively disclosed.
* The CoR attestation is designed primarily for **remote (online) presentation**. Proximity presentation (offline) is not required by default but MAY be supported by mdoc-capable issuers where Member State governance frameworks require it.

### 4.4 Device binding

The CoR attestation SHOULD be **device-bound** to the EUDI Wallet Unit of the holder. Where device binding is applied, the attestation SHALL be cryptographically bound to the PID attestation on the same Wallet Unit (ARB\_28 of \[Topic 12]). When such binding is required, the conditional attribute `cryptographically_bound_to` (defined in § 2.4) SHALL be present in the attestation and SHALL be set to:

* `"eu.europa.ec.eudi.pid.1"` for ISO/IEC 18013-5 (mdoc) attestations; or
* `"urn:eudi:pid:1"` for SD-JWT VC attestations.

Where the CoR attestation is not device-bound, the `cryptographically_bound_to` attribute SHALL be omitted.

### 4.5 Transactional data

No transactional data requirements are defined for this attestation type at this time. \[See Topic 20 of Annex 2 of the ARF for High-Level Requirements related to transactional data.]

***

## 5 Trust anchors

For **QEAA and PuB-EAA** CoR attestations, relying parties SHALL obtain the trust anchor from the applicable EU Trusted List, in conformance with ARB\_20 of \[Topic 12] and the ARF. Issuers MAY use an intermediate signing certificate, with the trust anchor signing the intermediate certificate.

For **non-qualified EAA** CoR attestations, the location of the machine-readable trust anchor SHALL be indicated in the attestation metadata (per ARB\_21 of \[Topic 12]). Relying parties SHOULD use this location to retrieve and verify the trust anchor.

**WE BUILD LSP context (current):** In the current WE BUILD Large-Scale Pilot (LSP) deployment, a formal trusted issuer list mechanism is **out of scope**. Participating CoR Attestation Providers and Relying Parties are assumed to be familiar with the CoR attestation guideline and with the list of participating issuers.

**Production / cross-border deployments (future):** Future versions of this rulebook MUST replace the above with a concrete trust anchor mechanism aligned with:

* The EU Trusted List framework established pursuant to \[2015/1505];
* ARF Chapter 6.2 and \[HLR] Topic 31 part H (trusted list of issuers);
* The technical specifications for trust anchor distribution defined by the European Digital Identity Cooperation Group.

Signing (issuer signing attestation, verifier signing request) SHALL be implemented in conformance with \[POTENTIAL D2.2] SD-JWT VC specification. Specific cryptographic algorithms and elliptic curves SHALL be determined in accordance with applicable technical specifications once finalised; holder/device binding SHALL also conform to \[POTENTIAL D2.2].

***

## 6 Revocation

Per \[Topic 7] of Annex 2 of the ARF:

In the current WE BUILD LSP deployment, **revocation is out of scope**. Wallet instances and CoR attestations are assumed not to be revoked during the pilot. Future deployments targeting production or cross-border use SHOULD define a revocation mechanism in conformance with one of the following methods (as applicable at the time of that deployment):

* An Attestation Status List mechanism included in a Technical Specification specified by the Commission.
* An Attestation Revocation List mechanism included in a Technical Specification specified by the Commission.

Where the CoR attestation has a short validity period (24 hours or less), revocation is not required.

***

## 7 Compliance

This rulebook addresses compliance with the High-Level Requirements of \[Topic 12] of Annex 2 of the ARF, as summarised in the table below (derived from the compliance annex of the source CoR attestation guideline).

| **Requirement**                                                                                     | **ARF Reference**        | **Coverage in this Rulebook**                                                                                                                                                                                                                                                                               |
| --------------------------------------------------------------------------------------------------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| At least one standardised format SHALL be specified.                                                | ARB\_1                   | Section 3: SD-JWT VC (primary), mdoc, W3C VCDM v2.0 all addressed.                                                                                                                                                                                                                                          |
| Proximity (offline) presentation requirement SHALL be analysed; if needed, mdoc SHALL be specified. | ARB\_2                   | Section 3.1 and Section 4.3: proximity presentation analysed; mdoc MAY be used where required by Member State governance. Not mandated by default.                                                                                                                                                          |
| SD-JWT VC format SHALL be specified if required.                                                    | ARB\_3                   | Section 3.2: SD-JWT VC is the primary encoding; conformance with \[HAIP] required.                                                                                                                                                                                                                          |
| W3C VCDM MAY be specified for non-qualified EAA.                                                    | ARB\_4                   | Section 3.3: W3C VCDM addressed for non-qualified EAA use only.                                                                                                                                                                                                                                             |
| A unique attestation/document type SHALL be defined.                                                | ARB\_5                   | Sections 3.1 and 3.2: `eu.europa.ec.eudi.cor.1` defined for both mdoc and SD-JWT VC.                                                                                                                                                                                                                        |
| Attributes SHALL be defined in an encoding-independent manner and within a unique namespace.        | ARB\_6, ARB\_6a, ARB\_6b | Chapter 2: all attributes encoding-independent. Namespace `eu.europa.ec.eudi.cor.1` defined in Section 2.1. Claim names conform to IANA, Public Name, or Private Name requirements.                                                                                                                         |
| Existing attribute conventions and catalogues SHOULD be considered.                                 | ARB\_7                   | Section 2.2/2.3: PID-aligned attributes reuse ARF PID definitions; eIDAS address attributes reused where available.                                                                                                                                                                                         |
| `attestation_legal_category` SHALL be defined.                                                      | ARB\_11 / ARB\_12        | Sections 2.1, 2.5, 3.1, 3.2: `attestation_legal_category` defined and set to `"QEAA"`, `"PuB-EAA"`, or `"non-qualified-EAA"`. Not selectively disclosable.                                                                                                                                                  |
| Issuer identity and country metadata SHALL be included.                                             | ARB\_13–ARB\_15          | Section 2.5: `issuing_authority` and `issuing_country` defined as mandatory metadata.                                                                                                                                                                                                                       |
| Subject identity attributes SHALL be included.                                                      | ARB\_16–ARB\_17          | Sections 2.2/2.3: `family_name`, `given_name`, `birth_date`, `birth_place`, `nationality` defined. `personal_administrative_number` and `tax_identification_number` removed in v0.3 as redundant with the mandatorily-bound PID (§ 4.2 now requires PID to always be requested/verified alongside the CoR). |
| Validity period metadata SHALL be included.                                                         | ARB\_18–ARB\_19          | Sections 2.5/2.6: `issuance_date` (mandatory) and `expiry_date` (optional) defined.                                                                                                                                                                                                                         |
| Trust anchor location SHALL be indicated.                                                           | ARB\_20–ARB\_21          | Chapter 5: trust anchor via EU Trusted List for QEAA/PuB-EAA; metadata location for non-qualified EAA.                                                                                                                                                                                                      |
| PID verification requirement SHALL/SHOULD be specified.                                             | ARB\_27                  | Section 4.2: relying parties SHALL request and verify PID alongside CoR.                                                                                                                                                                                                                                    |
| Device binding and cryptographic binding specification.                                             | ARB\_28, ARB\_34         | Section 4.4: device binding SHOULD be applied; `cryptographically_bound_to` defined as conditional attribute in § 2.4 with values `"eu.europa.ec.eudi.pid.1"` (mdoc) / `"urn:eudi:pid:1"` (SD-JWT VC).                                                                                                      |
| Selective disclosure specification SHALL be provided.                                               | ARB\_30, ARB\_31         | Sections 3.2 and 4.3: SD requirements specified per claim; recursive disclosure for `resident_address`.                                                                                                                                                                                                     |

***

## 8 References

| **Item Reference**                      | **Standard name / details**                                                                                                                                                                                                                                               |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \[European Digital Identity Regulation] | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework  |
| \[AMLR]                                 | Regulation (EU) 2024/1620 of the European Parliament and of the Council of 31 May 2024 establishing the Authority for Anti-Money Laundering and Countering the Financing of Terrorism and amending Regulations (EU) No 1093/2010, (EU) No 1094/2010 and (EU) No 1095/2010 |
| \[ARF]                                  | The Common Union Toolbox for a Coordinated Approach Towards a European Digital Identity Framework – The European Digital Identity Wallet Architecture and Reference Framework, Version 1.4.0                                                                              |
| \[HLR]                                  | ARF Annex 2 – High Level Requirements                                                                                                                                                                                                                                     |
| \[Topic 7]                              | ARF Annex 2 – Topic 7 – Attestation revocation and revocation checking                                                                                                                                                                                                    |
| \[Topic 10]                             | ARF Annex 2 – Topic 10 – Issuing a PID or attestation to a Wallet Unit                                                                                                                                                                                                    |
| \[Topic 12]                             | ARF Annex 2 – Topic 12 – Attestation Rulebooks                                                                                                                                                                                                                            |
| \[Topic 20]                             | ARF Annex 2 – Topic 20 – Strong User authentication for electronic payments                                                                                                                                                                                               |
| \[2015/1505]                            | Commission Implementing Decision (EU) 2015/1505 of 8 September 2015 laying down technical specifications and formats relating to trusted lists pursuant to Article 22(5) of Regulation (EU) No 910/2014                                                                   |
| \[EBA CP/2025/04]                       | European Banking Authority (EBA) Consultation Paper EBA/CP/2025/04, 6 March 2025                                                                                                                                                                                          |
| \[ETSI TS 119 461]                      | ETSI TS 119 461 v2.1.1 — Attribute proofing: clauses 8.2.6/8.3.6 (trusted register), 8.2.7/8.3.7 (proof of access), 8.2.8/8.3.8 (documents and attestations)                                                                                                              |
| \[HAIP]                                 | Yasuda, K. et al., OpenID4VC High Assurance Interoperability Profile, OpenID Foundation, Version draft-03                                                                                                                                                                 |
| \[IANA-JWT-Claims]                      | IANA JSON Web Token Claims Registry                                                                                                                                                                                                                                       |
| \[ISO/IEC 18013-5]                      | ISO/IEC 18013-5, Personal identification — ISO-compliant driving licence — Part 5: Mobile driving licence (mDL) application, First edition, 2021-09                                                                                                                       |
| \[OIDC]                                 | Sakimura, N. et al., "OpenID Connect Core 1.0", OpenID Foundation                                                                                                                                                                                                         |
| \[OpenID4VP]                            | OpenID for Verifiable Presentations specification                                                                                                                                                                                                                         |
| \[POTENTIAL D2.2]                       | POTENTIAL deliverable D2.2 – API Definition and Integration                                                                                                                                                                                                               |
| \[RFC 2119]                             | RFC 2119 – Key words for use in RFCs to Indicate Requirement Levels, S. Bradner, March 1997                                                                                                                                                                               |
| \[RFC 3339]                             | RFC 3339 – Date and Time on the Internet: Timestamps, G. Klyne et al., July 2002                                                                                                                                                                                          |
| \[RFC 8259]                             | RFC 8259 – The JavaScript Object Notation (JSON) Data Interchange Format, T. Bray, Ed., December 2017                                                                                                                                                                     |
| \[RFC 8610]                             | RFC 8610 – Concise Data Definition Language (CDDL), H. Birkholz et al., June 2019                                                                                                                                                                                         |
| \[RFC 8943]                             | RFC 8943 – CBOR Tags for Date, M. Jones et al., November 2020                                                                                                                                                                                                             |
| \[RFC 8949]                             | RFC 8949 – Concise Binary Object Representation (CBOR), C. Bormann et al., December 2020                                                                                                                                                                                  |
| \[SD-JWT VC]                            | SD-JWT-based Verifiable Credentials (SD-JWT VC), version draft-ietf-oauth-sd-jwt-vc-09                                                                                                                                                                                    |
| \[W3C VCDM v2.0]                        | Sporny, M. et al., Verifiable Credentials Data Model v2.0, W3C Recommendation                                                                                                                                                                                             |

