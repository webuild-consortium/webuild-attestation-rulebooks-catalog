# WE BUILD Attestation Rulebook for attestations of type *Tax Identification Number (TaxID)*

*This rulebook is derived from the WE BUILD v1 Attestation Rulebook Template and profiles the Tax Identification Number (TaxID) attestation description for natural persons within the WE BUILD Large-Scale Pilot (LSP).*

*This is a working document that holds no legal value and does not reflect any common agreement or position of the co-legislators or of the WE BUILD consortium. It presents a state-of-play of ongoing work and should not be considered final.*

**Author(s):**

* \[Sevastianos Chatzistergos, Greek Ministry of Digital Governance
* Uwe Pfizenmaier, IDnow]

**Previous Authors:**

* \[Sevastianos Chatzistergos, Greek Ministry of Digital Governance (0.1, 0.2, 0.3, 0.4)
* Uwe Pfizenmaier, IDnow (0.2., 0.3, 0.4)]

| Version | Date       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 0.1     | 17-02-2026 | Source TaxID attestation description (WE BUILD LSP).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 0.2     | 30-06-2026 | Conversion into WE BUILD Attestation Rulebook format. Added `attestation_legal_category` (§ 2.5), `cryptographically_bound_to` (§ 2.4); expanded code lists (§ 2.8); added integrity rule IR-03 (§ 2.9); expanded encoding chapters (§§ 3.1–3.2); per-claim SD-JWT disclosability; trust anchor split LSP/production (§ 5); compliance table (§ 7). Open issues flagged inline.                                                                                                                                                                                                |
| 0.3     | 30-06-2026 | Added conditional metadata attribute `trust_anchor_location` (§ 2.7) to close the gap between § 5 (trust anchor requirements) and Chapter 2 (no carrier attribute previously existed for non-qualified EAA). Updated § 2.8 code list, §§ 3.1/3.2 encoding tables, § 5 resolution model, and § 7 compliance table (ARB\_20–21) accordingly. Tightened ARB\_4 and ARB\_5/ARB\_6 compliance wording to reflect open-issue status (OI-01, OI-05).                                                                                                                                  |
| 0.4     | 01-07-2026 | Upgraded § 4.2 relying-party PID request/verification from SHOULD to SHALL, consistent with mandatory cryptographic binding to the PID where device-bound (§ 4.4). Confirmed `family_name`, `given_name`, `birth_date` remain mandatory (§ 2.2) per ARB\_16/17 (subject identity attributes SHALL be included in the attestation itself, independent of PID binding); no attributes removed as redundant, unlike the CoR rulebook's `personal_administrative_number`/`tax_identification_number` (see CoR v0.3), since TaxID carries no such duplicate national-ID attributes. |

**Feedback:** \[<s.chatzistergos@mindigital.gr>; <uwe.pfizenmaier@idnow.io>]

***

> **Open Issues Register**
>
> The following open issues are flagged inline throughout this document and are collected here for visibility:
>
> | ID    | Section          | Description                                                                                                                                                                                                                                      |
> | ----- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
> | OI-01 | §§ 2.1, 3.1, 3.2 | Namespace and attestation type `eu.europa.ec.eudi.taxid.1` is proposed; pending WE BUILD consortium confirmation.                                                                                                                                |
> | OI-02 | §§ 2.2, 3.1, 3.2 | `birth_date` is encoded as `tdate` (datetime) in the source description. ARF PID convention uses `full-date` (date only). Resolution required before finalisation.                                                                               |
> | OI-03 | § 2.5            | `issuing_authority` definition is dual-use: either a name string or an ISO 3166-1 Alpha-2 code. This creates schema ambiguity; a single, unambiguous definition is needed.                                                                       |
> | OI-04 | § 2.3            | `church_tax_ID` is a jurisdiction-specific attribute (primarily Germany). Consortium should decide whether to retain as a general optional attribute or restrict to a jurisdiction-specific extension namespace.                                 |
> | OI-05 | § 3.3            | W3C VCDM encoding not yet defined. Rulebook author to complete before finalisation.                                                                                                                                                              |
> | OI-06 | §§ 3.1, 3.2      | Illustrative encoding examples (mDoc fragment, SD-JWT token) not yet provided. Rulebook author to complete.                                                                                                                                      |
> | OI-07 | § 2.7, § 5       | `trust_anchor_location` resolution protocol (HTTP semantics, expected response format/profile) is referenced but not yet normatively specified; depends on a forthcoming Commission technical specification for non-qualified EAA trust anchors. |

***

## 1 Introduction

### 1.1 Document scope and purpose

This rulebook defines functional, semantic, and technical requirements for a **Tax Identification Number (TaxID)** attestation for natural persons within the WE BUILD Large-Scale Pilot (LSP) and the EUDI Wallet ecosystem.

**What the attestation expresses:** The TaxID attestation provides structured, verifiable evidence of a natural person's tax identification number within a national tax system, bound to their identity. It enables relying parties to verify the official and unique tax identification of an individual within and across EU member states.

**Scope assumption:** Each attestation is associated with a single Tax ID number. Where a natural person holds multiple Tax IDs (e.g. in multiple jurisdictions), each is represented by a separate attestation.

**Issuers, holders, and relying parties:**

* *Issuers:* Primarily National Tax Authorities (the actual issuers of tax identification numbers). The role of authentic source may also be assumed by other government agencies (e.g. social security or public service agencies) that hold Tax ID information, or by third-party services authorised by governments to verify and validate Tax IDs. In countries where no authentic source is capable of providing the information via interoperability, a QTSP may issue a TaxID QEAA after receiving a relevant physical or electronic document providing the required proof.
* *Holders:* Natural persons to whom a Tax ID has been assigned under national law.
* *Relying parties:* Any entity that requires verification of a natural person's tax identification, including obliged entities performing Customer Due Diligence (CDD), financial institutions, public administrations, and other service providers.

**Primary use cases:**

1. Verification of a natural person's tax identity in the context of financial services (e.g. account opening, investment services).
2. Cross-border identification of individuals for tax reporting and information exchange within and across EU member states.
3. Reuse of verified Tax ID data in digital onboarding workflows where a tax number is required.

**Source material:** This rulebook is derived from the TaxID attestation description (WE BUILD LSP, v0.1, 17-02-2026). Where not explicitly amended or extended here, the provisions of that source description remain applicable.

### 1.2 Document structure

* **Chapter 2** defines attestation attributes and metadata in an encoding-independent manner, including code lists (§ 2.8) and integrity rules (§ 2.9).
* **Chapter 3** specifies encoding for SD-JWT VC (primary), ISO/IEC 18013-5 (mdoc), and W3C VCDM v2.0, with illustrative examples.
* **Chapter 4** specifies attestation usage, relying-party obligations, presentation requirements, and device binding.
* **Chapter 5** defines trust anchor provision and verification mechanisms.
* **Chapter 6** defines attestation revocation.
* **Chapter 7** provides compliance information with respect to the ARF and EUDI framework.
* **Chapter 8** lists references.

### 1.3 Key words

This document uses the capitalised key words 'SHALL', 'SHOULD' and 'MAY' as specified in \[RFC 2119], i.e., to indicate requirements, recommendations and options specified in this document. In addition, 'must' (non-capitalised) is used to indicate an external constraint, i.e., a requirement that is not mandated by this document, but, for instance, by an external document. The word 'can' indicates a capability, whereas other words such as 'will', and 'is' or 'are' are intended as statements of fact.

### 1.4 Terminology

This document uses the terminology specified in Annex 1 of the ARF and in the WE BUILD LSP documentation. Key terms:

* **Tax Identification Number (Tax ID / TaxID):** A unique identifier assigned to a natural person by a national tax authority or equivalent body for purposes of tax administration and identification.
* **National Tax Authority:** The governmental body in a Member State responsible for issuing and administering Tax IDs (e.g. Bundeszentralamt für Steuern in Germany, Direction Générale des Finances Publiques in France).
* **Authentic source:** An authoritative repository or system holding Tax ID information, which may serve as the data source for TaxID attestation issuance.

***

## 2 Attestation attributes and metadata

### Chapter overview and requirements

This chapter defines all attributes and metadata that a TaxID attestation MAY contain, in an encoding-independent manner. Each attribute is classified as mandatory, optional, or conditional. Abstract data types are used; format-specific encoding details are provided in Chapter 3.

**Structure:** The TaxID attestation is a **single flat object** — no nested or composite attribute structures are defined.

**Requirements applicable to TaxID as a QEAA:**

* An indication that the attestation has been issued as a QEAA SHALL be included (ARB\_11, Annex V point a of \[European Digital Identity Regulation]).
* Attributes or metadata representing issuer identity and country SHALL be included (ARB\_13, Annex V point b).
* Attributes representing subject identity SHALL be included (ARB\_16, Annex V point c).
* Validity period metadata SHALL be included (ARB\_18, Annex V point e).
* Trust anchor location SHALL be indicated (ARB\_20, Annex V point h).

**Requirements applicable to TaxID as a PuB-EAA or non-qualified EAA** follow the corresponding provisions of Annex VII and ARB\_12–ARB\_21 of \[Topic 12] respectively.

### 2.1 Introduction

The TaxID attestation is designed to enable relying parties to verify a natural person's tax identity in a machine-readable, privacy-preserving manner. It is used together with, or independently from, a PID attestation, depending on the relying party's requirements.

The TaxID attestation may be issued as a **QEAA**, **PuB-EAA**, or **non-qualified EAA**, depending on the issuing authority and Member State governance framework. This rulebook defines the mandatory metadata attribute `attestation_legal_category` (§ 2.5), which SHALL have the value `"QEAA"`, `"PuB-EAA"`, or `"non-qualified-EAA"` as appropriate.

> **OI-01 — OPEN ISSUE (Namespace):** The attestation namespace and type identifier is proposed as **`eu.europa.ec.eudi.taxid.1`**. This identifier is used throughout this rulebook but is **pending confirmation by the WE BUILD consortium** before this rulebook can be considered final.

All `tstr` / `string` attributes SHALL have a maximum length of 150 characters unless otherwise stated.

### 2.2 Mandatory attributes

*NOTE: If an attribute is indicated as mandatory, this solely means that the Issuer SHALL ensure that the element is present in the attestation. It does not imply that a Relying Party is required to request it, nor that the User cannot refuse to disclose it.*

| **Data Identifier**   | **Semantic Reference**                         | **Definition**                                                                                                                                                                                                   | **Data type** | **Example value** |
| --------------------- | ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ----------------- |
| `tax_number`          | National tax authority (Member State specific) | Character string that enables the tax authority to uniquely assign the User within the national tax system. The format and structure of this string varies per Member State (combination of letters and digits). | string        | `"DE123456789"`   |
| `affiliation_country` | ISO 3166-1                                     | Alpha-2 country code of the User's country of tax residence (i.e. the Member State whose national tax system assigns the `tax_number`).                                                                          | string        | `"DE"`            |
| `family_name`         | ARF PID attribute: `family_name`               | Current last name(s) or surname(s) of the User.                                                                                                                                                                  | string        | `"Müller"`        |
| `given_name`          | ARF PID attribute: `given_name`                | Current first name(s), including middle name(s), of the User.                                                                                                                                                    | string        | `"Hans"`          |
| `birth_date`          | ARF PID attribute: `birth_date`                | Day, month, and year on which the User was born. Expressed as a date (not a datetime). See OI-02 regarding encoding type.                                                                                        | date          | `"1988-08-25"`    |

> **OI-02 — OPEN ISSUE (birth\_date encoding):** The source TaxID description specifies `birth_date` with encoding type `tdate`, which is a CDDL datetime type. ARF PID convention uses `full-date` (date only, tag 1004), which is more appropriate for a date of birth. **The WE BUILD consortium and rulebook author SHOULD resolve this discrepancy and align to** **`full-date`** **for consistency with ARF PID.** Until resolved, implementers SHOULD use `full-date` in conformance with ARF PID conventions. This rulebook adopts `full-date` as the normative encoding in § 3.

### 2.3 Optional attributes

| **Data Identifier** | **Semantic Reference**                         | **Definition**                                                                                                                                                                                                                                                                                                             | **Data type** | **Example value**          |
| ------------------- | ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | -------------------------- |
| `church_tax_ID`     | National tax authority (jurisdiction-specific) | Character string made up of numbers and letters, identifying the User for church tax purposes. This attribute is jurisdiction-specific and primarily applicable in Member States where church tax is levied (e.g. Germany). Issuers in jurisdictions where church tax does not exist SHALL omit this attribute. See OI-04. | string        | `"1234567890"`             |
| `iban`              | ISO 13616                                      | IBAN (International Bank Account Number) registered with the tax authority for the User. Formatted in accordance with ISO 13616. This attribute is sensitive financial data; relying parties SHALL handle it accordingly and SHALL NOT request it unless strictly necessary for the transaction.                           | string        | `"DE89370400440532013000"` |

> **OI-04 — OPEN ISSUE (church\_tax\_ID scope):** `church_tax_ID` is primarily a Germany-specific attribute. The consortium SHOULD decide whether to retain it as a general optional attribute in the common namespace, or relocate it to a jurisdiction-specific domestic namespace (e.g. `eu.europa.ec.eudi.taxid.de.1`). Until resolved, it is retained here as optional.

### 2.4 Conditional attributes

The following attribute is conditional: it SHALL be present when the TaxID attestation is device-bound and cryptographically linked to another attestation on the same Wallet Unit (see § 4.4 and ARB\_28 of \[Topic 12]). It SHALL be omitted when the attestation is not device-bound.

| **Data Identifier**          | **Semantic Reference**    | **Definition**                                                                                                                                                                                                                                                                                                                      | **Data type** | **Example value**           |
| ---------------------------- | ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | --------------------------- |
| `cryptographically_bound_to` | ARF ARB\_28 (\[Topic 12]) | Indicates the attestation type or `vct` of the attestation on the same Wallet Unit to which this TaxID attestation is cryptographically bound. When bound to a PID, this attribute SHALL be set to `"eu.europa.ec.eudi.pid.1"` (mdoc) or `"urn:eudi:pid:1"` (SD-JWT VC). Shall be omitted when the attestation is not device-bound. | string        | `"eu.europa.ec.eudi.pid.1"` |

### 2.5 Mandatory metadata

| **Data Identifier**          | **Semantic Reference**                                                           | **Definition**                                                                                                                                                                                                                                                              | **Data type** | **Example value**                |
| ---------------------------- | -------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | -------------------------------- |
| `attestation_legal_category` | ARF / \[European Digital Identity Regulation] Annex V point a, Annex VII point a | Indicates the legal category of the attestation. SHALL be set to `"QEAA"`, `"PuB-EAA"`, or `"non-qualified-EAA"` depending on the issuer's legal status. Not selectively disclosable (see § 3.2).                                                                           | string        | `"QEAA"`                         |
| `issuance_date`              | ARF attestation metadata                                                         | Date and time on which the TaxID attestation was issued.                                                                                                                                                                                                                    | datetime      | `"2025-03-01T10:00:00Z"`         |
| `issuing_authority`          | ARF attestation metadata                                                         | Name of the administrative authority that issued this TaxID attestation. Where no separate authority is authorised to issue TaxID attestations in the Member State, this field SHALL contain the ISO 3166-1 Alpha-2 country code of the respective Member State. See OI-03. | string        | `"Bundeszentralamt für Steuern"` |
| `issuing_country`            | ARF attestation metadata                                                         | Alpha-2 country code (ISO 3166-1) of the TaxID attestation provider's country or territory.                                                                                                                                                                                 | string        | `"DE"`                           |

> **OI-03 — OPEN ISSUE (issuing\_authority definition):** The current definition is dual-use: either a human-readable name string, or an ISO 3166-1 Alpha-2 country code. This creates schema ambiguity (the field could contain either `"Bundeszentralamt für Steuern"` or `"DE"`). A single, unambiguous definition is needed — either always a name, or always a code, or split into two distinct fields. **The rulebook author SHOULD resolve this before finalisation** and update the attribute definition and code list (§ 2.8) accordingly.

### 2.6 Optional metadata

| **Data Identifier**    | **Semantic Reference**   | **Definition**                                                                                                                                                                                                                          | **Data type** | **Example value**        |
| ---------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ------------------------ |
| `expiry_date`          | ARF attestation metadata | Date and time after which the TaxID attestation is no longer valid. Where present, SHALL be greater than `issuance_date` (see IR-01).                                                                                                   | datetime      | `"2030-03-01T10:00:00Z"` |
| `issuing_jurisdiction` | ISO 3166-2:2020          | Country subdivision code of the jurisdiction that issued the TaxID attestation, as defined in ISO 3166-2:2020 Clause 8. The first part of the code (before the hyphen) SHALL be the same as the value of `issuing_country` (see IR-03). | string        | `"DE-BY"`                |

### 2.7 Conditional metadata

The following metadata attribute is conditional on the attestation's legal category (see § 2.5 `attestation_legal_category` and Chapter 5 Trust anchors).

| **Data Identifier**     | **Semantic Reference**                                                                                  | **Definition**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | **Data type** | **Example value**                                           |
| ----------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------- | ----------------------------------------------------------- |
| `trust_anchor_location` | ARF / \[European Digital Identity Regulation] Annex V point h, Annex VII point h; ARB\_21 (\[Topic 12]) | The URL at which a machine-readable version of the trust anchor to be used for verifying this TaxID attestation can be found or looked up. SHALL be present when `attestation_legal_category` = `"non-qualified-EAA"`, since non-qualified EAA issuers are not listed on an EU Trusted List and therefore require an explicit, attestation-carried pointer to their trust anchor (per ARB\_21). SHALL be omitted when `attestation_legal_category` = `"QEAA"` or `"PuB-EAA"`, since for these categories the trust anchor is obtained from the applicable EU Trusted List as described in Chapter 5, and an attestation-carried URL is not the normative mechanism (per ARB\_20). Not selectively disclosable — see disclosability rationale in § 3.2. | string (URL)  | `"https://trust.example-issuer.eu/anchors/taxid-2026.json"` |

> **OI-07 — OPEN ISSUE (trust\_anchor\_location resolution):** This rulebook defines the attribute that *carries* the trust anchor location, but the **resolution protocol** (e.g. HTTPS GET semantics, expected response content-type, and the machine-readable trust anchor format/profile) is not yet normatively specified. This depends on a forthcoming Commission technical specification for non-qualified EAA trust anchors. See § 5 for the interim resolution model.

### 2.8 Code lists

| **Field name**               | **Allowed values**                                            | **Meaning**                                                                                                                                | **Source / vocabulary**                                          | **Notes / extensibility**                                                                                                                                                          |
| ---------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `affiliation_country`        | ISO 3166-1 Alpha-2 codes (e.g. `"DE"`, `"FR"`, `"NL"`)        | Two-letter code identifying the Member State or territory whose national tax system assigns the `tax_number`.                              | ISO 3166-1 (International Organization for Standardization)      | No extension allowed; values not in ISO 3166-1 SHALL NOT be used.                                                                                                                  |
| `issuing_country`            | ISO 3166-1 Alpha-2 codes                                      | Two-letter code identifying the country of the issuing authority.                                                                          | ISO 3166-1                                                       | No extension allowed.                                                                                                                                                              |
| `issuing_jurisdiction`       | ISO 3166-2:2020 subdivision codes (e.g. `"DE-BY"`, `"DE-NW"`) | Country subdivision code. The portion before the hyphen SHALL equal the value of `issuing_country`.                                        | ISO 3166-2:2020, Clause 8                                        | Issuers SHALL only use values defined in ISO 3166-2 for the relevant country. No additional values SHALL be introduced.                                                            |
| `attestation_legal_category` | `"QEAA"`, `"PuB-EAA"`, `"non-qualified-EAA"`                  | Legal category of the attestation as defined under the \[European Digital Identity Regulation].                                            | ARF / \[European Digital Identity Regulation] Annex V, Annex VII | No additional values SHALL be introduced. Value is determined by the legal status of the issuer.                                                                                   |
| `iban`                       | ISO 13616 format (e.g. `"DE89370400440532013000"`)            | IBAN formatted as country code (2 letters) + check digits (2 digits) + BBAN (up to 30 alphanumeric characters), as specified in ISO 13616. | ISO 13616-1:2020 (IBAN standard)                                 | Only valid IBANs SHALL be included. Issuers SHOULD validate the IBAN check digits before issuance.                                                                                 |
| `trust_anchor_location`      | Any well-formed absolute HTTPS URL                            | Location at which a machine-readable trust anchor document can be retrieved.                                                               | ARB\_21 (\[Topic 12]); URL syntax per \[RFC 3986]                | Scheme SHALL be `https`. The resolution protocol and response format are not yet standardised (see OI-07); issuers SHOULD monitor forthcoming Commission technical specifications. |

### 2.9 Integrity rules

| **Rule ID** | **Rule statement**                                                                                                                                                                            | **Why it exists**                                                                                                                                                                                                                                                      | **Where enforced**                                   | **Verifier / issuer behavior on failure**                                                                                                                                                                                                       |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IR-01       | If `expiry_date` is present, it SHALL be strictly greater than `issuance_date`.                                                                                                               | An attestation cannot expire before or at the moment it is issued.                                                                                                                                                                                                     | Issuer business rules; verifier business validation. | Issuer SHALL reject attestations where `expiry_date` ≤ `issuance_date`. Verifier SHALL treat the attestation as invalid.                                                                                                                        |
| IR-02       | `birth_date` SHALL be strictly earlier than `issuance_date`.                                                                                                                                  | A person cannot be issued a TaxID attestation before or on the date of their birth.                                                                                                                                                                                    | Issuer business rules; verifier business validation. | Issuer SHALL reject attestations where `birth_date` ≥ `issuance_date`. Verifier SHOULD treat the attestation as suspect if this rule is violated.                                                                                               |
| IR-03       | If `issuing_jurisdiction` is present, the portion of the code before the hyphen (the country part) SHALL be identical to the value of `issuing_country`.                                      | Ensures jurisdictional consistency: the subdivision code must belong to the same country as the issuer.                                                                                                                                                                | Issuer business rules; schema validation.            | Issuer SHALL reject attestations with a mismatched `issuing_jurisdiction` / `issuing_country` pair. Verifier SHOULD treat a mismatch as an indication of a malformed attestation.                                                               |
| IR-04       | `trust_anchor_location` SHALL be present if and only if `attestation_legal_category` = `"non-qualified-EAA"`. It SHALL be absent when `attestation_legal_category` = `"QEAA"` or `"PuB-EAA"`. | Aligns the trust anchor mechanism with the attestation's legal category: non-qualified EAA requires an explicit pointer (ARB\_21), while QEAA/PuB-EAA resolve trust via the EU Trusted List (ARB\_20) and SHOULD NOT carry a redundant or potentially conflicting URL. | Issuer business rules; schema validation.            | Issuer SHALL reject an attestation where this conditional presence rule is violated. Verifier SHALL treat a non-qualified EAA lacking `trust_anchor_location`, or a QEAA/PuB-EAA carrying one, as non-conformant and SHOULD flag it for review. |

***

## 3 Attestation encoding

### 3.1 ISO/IEC 18013-5-compliant encoding (mdoc)

The TaxID attestation MAY be issued in ISO/IEC 18013-5-compliant mdoc format where proximity presentation (without internet) is required by the deployment context. Issuers and Member States SHALL determine, in accordance with ARB\_02 of \[Topic 12], whether proximity presentation is a required capability for their deployment of the TaxID attestation.

> **OI-01 (reminder):** The document type below is proposed and pending consortium confirmation.

**Document type:** `eu.europa.ec.eudi.taxid.1`

**General encoding rules:**

* `tstr`, `uint`, `bstr`, `bool`, `tdate`, and `full-date` are CDDL representation types defined in \[RFC 8610].
* A `tstr` SHALL be encoded in UTF-8 (as specified in \[RFC 8949]) and SHALL support the full Unicode range.
* All `tstr` attributes SHALL have a maximum length of 150 characters.
* `full-date` is encoded as `full-date = #6.1004(tstr)`, where tag 1004 is specified in [RFC 8943]. In accordance with [RFC 8943], a `full-date` attribute SHALL contain a full-date string as specified in \[RFC 3339].
* `tdate` is used for datetime values (`issuance_date`, `expiry_date`). In accordance with [RFC 8949] section 3.4.1, a `tdate` attribute SHALL contain a date-time string as specified in [RFC 3339]. Fractions of seconds SHALL NOT be used; the time-offset SHALL be `"Z"`.
* **`birth_date`** **encoding:** Per OI-02, this rulebook adopts `full-date` for `birth_date` (date only), overriding the source description's `tdate`. Implementers SHALL use `full-date` for `birth_date`.
* Canonical CBOR rules per \[RFC 8949] section 4.2 SHALL apply: integers SHALL be as small as possible; lengths SHALL be as short as possible; indefinite-length items SHALL be definite-length.

**Attribute encoding table:**

| **Data Identifier**          | **Attribute identifier**     | **Encoding format**     | **Namespace**               |
| ---------------------------- | ---------------------------- | ----------------------- | --------------------------- |
| `tax_number`                 | `tax_number`                 | tstr                    | `eu.europa.ec.eudi.taxid.1` |
| `affiliation_country`        | `affiliation_country`        | tstr                    | `eu.europa.ec.eudi.taxid.1` |
| `family_name`                | `family_name`                | tstr                    | `eu.europa.ec.eudi.taxid.1` |
| `given_name`                 | `given_name`                 | tstr                    | `eu.europa.ec.eudi.taxid.1` |
| `birth_date`                 | `birth_date`                 | full-date *(see OI-02)* | `eu.europa.ec.eudi.taxid.1` |
| `church_tax_ID`              | `church_tax_ID`              | tstr                    | `eu.europa.ec.eudi.taxid.1` |
| `iban`                       | `iban`                       | tstr                    | `eu.europa.ec.eudi.taxid.1` |
| `cryptographically_bound_to` | `cryptographically_bound_to` | tstr                    | `eu.europa.ec.eudi.taxid.1` |
| `attestation_legal_category` | `attestation_legal_category` | tstr                    | `eu.europa.ec.eudi.taxid.1` |
| `issuance_date`              | `issuance_date`              | tdate                   | `eu.europa.ec.eudi.taxid.1` |
| `expiry_date`                | `expiry_date`                | tdate                   | `eu.europa.ec.eudi.taxid.1` |
| `issuing_authority`          | `issuing_authority`          | tstr                    | `eu.europa.ec.eudi.taxid.1` |
| `issuing_country`            | `issuing_country`            | tstr                    | `eu.europa.ec.eudi.taxid.1` |
| `issuing_jurisdiction`       | `issuing_jurisdiction`       | tstr                    | `eu.europa.ec.eudi.taxid.1` |
| `trust_anchor_location`      | `trust_anchor_location`      | tstr                    | `eu.europa.ec.eudi.taxid.1` |

> **OI-06 — OPEN ISSUE:** A full or partial mDoc illustrative example SHALL be provided here before finalisation. \[RULEBOOK AUTHOR TO PROVIDE AN EXAMPLE OF FULL OR PARTIAL mDOC OF THE ATTESTATION AND THE ATTRIBUTES AND THEIR VALUES]

### 3.2 SD-JWT VC-based encoding

The TaxID attestation SHALL be issued in SD-JWT VC-compliant format in conformance with the SD-JWT VCs profile specified in \[HAIP] (ARB\_01b of \[Topic 12]). Selective Disclosure SHALL be used.

> **OI-01 (reminder):** The `vct` value below is proposed and pending consortium confirmation.

**Verifiable Credential Type (`vct`):** `eu.europa.ec.eudi.taxid.1`

**General encoding rules:**

* JSON attributes SHALL be encoded as specified in \[RFC 8259].
* Date-only values (`birth_date`) SHALL be encoded as a JSON `string` in ISO 8601 / [RFC 3339] full-date format (e.g. `"1988-08-25"`).
* Datetime values (`issuance_date`, `expiry_date`) SHALL be encoded as a JSON `string` in [RFC 3339] date-time format with UTC offset `"Z"` (e.g. `"2025-03-01T10:00:00Z"`).
* All `string` attributes SHALL have a maximum length of 150 characters.
* The TaxID attestation is a **flat object** — no nested SD-JWT recursive disclosures are required. Each top-level claim is individually selectively disclosable according to the table below.
* Non-disclosable claims (marked MUST NOT) SHALL be included as plain JSON in the JWT payload, not wrapped in SD-JWT disclosure structures. This ensures that metadata cannot be hidden from verifiers.

**Disclosability rationale for non-disclosable claims:** `attestation_legal_category`, `issuance_date`, `issuing_authority`, `issuing_country`, and `cryptographically_bound_to` are attestation integrity and provenance metadata. Hiding them would prevent verifiers from establishing the legal status, currency, and provenance of the attestation — which are prerequisites for valid verification. They are therefore not selectively disclosable.

**IANA-registered / well-known claims:**

| **Data Identifier** | **Attribute identifier** | **Encoding format**             | **Reference / Notes**               | **Disclosable** |
| ------------------- | ------------------------ | ------------------------------- | ----------------------------------- | --------------- |
| `family_name`       | `family_name`            | string                          | Section 5.1 of \[OIDC]              | MUST            |
| `given_name`        | `given_name`             | string                          | Section 5.1 of \[OIDC]              | MUST            |
| `birth_date`        | `birth_date`             | string (full-date, \[RFC 3339]) | See OI-02; date-only format adopted | MUST            |

**Private claim names specific to TaxID attestation type:**

| **Data Identifier**          | **Attribute identifier**     | **Encoding format**            | **Notes**                                                                                                        | **Disclosable** |
| ---------------------------- | ---------------------------- | ------------------------------ | ---------------------------------------------------------------------------------------------------------------- | --------------- |
| `tax_number`                 | `tax_number`                 | string                         | Core identity attribute; Member State-specific format                                                            | MUST            |
| `affiliation_country`        | `affiliation_country`        | string                         | ISO 3166-1 Alpha-2                                                                                               | MUST            |
| `church_tax_ID`              | `church_tax_ID`              | string                         | Jurisdiction-specific (see OI-04); omit if not applicable                                                        | MUST            |
| `iban`                       | `iban`                       | string                         | ISO 13616; sensitive financial data — relying parties SHALL NOT request unless strictly necessary                | MUST            |
| `issuing_jurisdiction`       | `issuing_jurisdiction`       | string                         | ISO 3166-2:2020 subdivision code; optional metadata                                                              | MUST            |
| `attestation_legal_category` | `attestation_legal_category` | string                         | Value: `"QEAA"`, `"PuB-EAA"`, or `"non-qualified-EAA"`                                                           | MUST NOT        |
| `issuance_date`              | `issuance_date`              | string (datetime, \[RFC 3339]) | Attestation metadata                                                                                             | MUST NOT        |
| `expiry_date`                | `expiry_date`                | string (datetime, \[RFC 3339]) | Attestation metadata                                                                                             | MUST NOT        |
| `issuing_authority`          | `issuing_authority`          | string                         | Attestation metadata; see OI-03                                                                                  | MUST NOT        |
| `issuing_country`            | `issuing_country`            | string                         | ISO 3166-1 Alpha-2; attestation metadata                                                                         | MUST NOT        |
| `cryptographically_bound_to` | `cryptographically_bound_to` | string                         | Conditional; omit if not device-bound                                                                            | MUST NOT        |
| `trust_anchor_location`      | `trust_anchor_location`      | string                         | Conditional per IR-04; present only when `attestation_legal_category` = `"non-qualified-EAA"` (see § 2.7, OI-07) | MUST NOT        |

> **OI-06 (reminder):** The following examples SHALL be completed by the rulebook author before finalisation.

\[RULEBOOK AUTHOR TO PROVIDE AN EXAMPLE OF THE JWT CLAIM SET USED BY THE PROVIDER]

\[RULEBOOK AUTHOR TO PROVIDE AN EXAMPLE OF THE ISSUED SD-JWT (IN base64url ENCODING)]

\[RULEBOOK AUTHOR TO PROVIDE A HUMAN-READABLE VERSION OF THE SD-JWT PAYLOAD AND A DESCRIPTION OF THE DISCLOSURES INCLUDED IN THE EXAMPLE]

### 3.3 W3C Verifiable Credentials Data Model-based encoding

The TaxID attestation MAY be issued in W3C VCDM v2.0-compliant format. Note that, per ARB\_01a of \[Topic 12], only a **non-qualified EAA** can use this format.

> **OI-05 — OPEN ISSUE:** W3C VCDM encoding is not yet defined for this attestation type. \[RULEBOOK AUTHOR TO PROVIDE HUMAN-READABLE EXAMPLE OF THE ISSUED ATTESTATION IN W3C VCDM FORMAT AND AN EXAMPLE OF THE PROOF TYPE]

Tables analogous to those in § 3.2 SHALL be defined, referencing documents approved by an EU standardisation body or the European Digital Identity Cooperation Group as required by ARB\_04 of \[Topic 12].

***

## 4 Attestation usage

### 4.1 Primary use cases

1. **Financial services onboarding:** Verification of a natural person's tax identification in the context of account opening, investment services, or other regulated financial services where a Tax ID is required.
2. **Cross-border tax information exchange:** Identification of individuals for tax reporting and information exchange across EU member states, in support of DAC (Directive on Administrative Cooperation) or FATCA-equivalent processes.
3. **Digital onboarding:** Reuse of a verified TaxID attestation in workflows that require a tax number, avoiding re-verification at each service provider.

### 4.2 Relying party obligations

* Relying parties SHALL request and verify a PID attestation alongside the TaxID attestation (see ARB\_27 of \[Topic 12]). Where the TaxID attestation is cryptographically bound to a PID on the same Wallet Unit (§ 4.4), the PID SHALL always be requested and verified together with the TaxID to establish the natural person's full identity context; the PID is used to identify and verify the natural person customer (e.g. name, date and place of birth), while the TaxID attestation verifies the tax identification number itself.
* Relying parties SHALL verify the attestation signature and check that `issuance_date` is in the past and, where present, that `expiry_date` has not been exceeded.
* Relying parties SHALL NOT request `iban` unless it is strictly necessary for the specific transaction and lawful under applicable data protection rules.
* Relying parties SHALL ensure that `tax_number` is used only for the stated tax-identification purpose and is not repurposed as a general identifier.
* Relying parties are responsible for determining whether the issuer constitutes an acceptable and sufficiently reliable source for their specific use case, taking into account their risk-based approach and applicable legal requirements.
* TaxID attestation attributes SHALL be released only in a VP Token, as specified in \[OpenID4VP].

### 4.3 Presentation requirements

* **Selective Disclosure** SHALL be used for the TaxID attestation (ARF section 5.3).
* The TaxID attestation is designed primarily for **remote (online) presentation**. Proximity presentation (offline) is not required by default but MAY be supported by mdoc-capable issuers where Member State governance frameworks require it.
* Relying parties SHOULD request only the minimum set of attributes necessary for the transaction (data minimisation principle).

### 4.4 Device binding

The TaxID attestation SHOULD be **device-bound** to the EUDI Wallet Unit of the holder (ARB\_34 of \[Topic 12]). Where device binding is applied and cryptographic binding to the PID is required, the conditional attribute `cryptographically_bound_to` (defined in § 2.4) SHALL be present and SHALL be set to:

* `"eu.europa.ec.eudi.pid.1"` for ISO/IEC 18013-5 (mdoc) attestations; or
* `"urn:eudi:pid:1"` for SD-JWT VC attestations.

Where the TaxID attestation is not device-bound, the `cryptographically_bound_to` attribute SHALL be omitted.

### 4.5 Transactional data

No transactional data requirements are defined for this attestation type at this time. \[See Topic 20 of Annex 2 of the ARF for High-Level Requirements related to strong user authentication for electronic payments.]

***

## 5 Trust anchors

For **QEAA and PuB-EAA** TaxID attestations, relying parties SHALL obtain the trust anchor from the applicable EU Trusted List, in conformance with ARB\_20 of \[Topic 12] and the ARF. Issuers MAY use an intermediate signing certificate, with the trust anchor signing the intermediate certificate. For these legal categories, the conditional attribute `trust_anchor_location` (§ 2.7) SHALL be omitted; the EU Trusted List is the sole normative trust anchor mechanism.

For **non-qualified EAA** TaxID attestations, the location of the machine-readable trust anchor SHALL be indicated via the `trust_anchor_location` attestation metadata attribute (§ 2.7), in conformance with ARB\_21 of \[Topic 12]. Relying parties SHALL use this location to retrieve and verify the trust anchor.

**Resolution model for** **`trust_anchor_location`** **(interim):** Until a Commission technical specification for non-qualified EAA trust anchors is finalised, relying parties SHOULD resolve `trust_anchor_location` as follows:

1. Perform an HTTPS GET request against the URL given in `trust_anchor_location`.
2. Expect a machine-readable response (profile to be confirmed — candidates include a JWK Set per \[RFC 7517] or an X.509 certificate bundle).
3. Validate that the resolved trust anchor corresponds to the key or certificate used to sign the attestation before accepting it as trusted.

This interim model is provisional (see OI-07) and SHALL be superseded once the Commission specification referenced by ARB\_21 is published.

**WE BUILD LSP context (current):** In the current WE BUILD Large-Scale Pilot (LSP) deployment, a formal trusted issuer list mechanism is **out of scope**. Participating TaxID Attestation Providers and Relying Parties are assumed to be familiar with the TaxID attestation guideline and with the list of participating issuers. Where a TaxID attestation is issued as a non-qualified EAA within the LSP, `trust_anchor_location` SHOULD still be populated to enable forward compatibility with the resolution model above, even though resolution is not currently enforced by pilot participants.

**Production / cross-border deployments (future):** Future versions of this rulebook MUST replace the above with a concrete trust anchor mechanism aligned with:

* The EU Trusted List framework established pursuant to \[2015/1505];
* ARF Chapter 6.2 and \[HLR] Topic 31 part H (trusted list of issuers);
* The technical specifications for trust anchor distribution defined by the European Digital Identity Cooperation Group, including the final resolution protocol for `trust_anchor_location` (OI-07).

Signing (issuer signing attestation, verifier signing request) SHALL be implemented in conformance with applicable technical specifications. Specific cryptographic algorithms and elliptic curves SHALL be determined in accordance with those specifications once finalised. Holder/device binding SHALL conform to the applicable SD-JWT VC or mdoc specification.

***

## 6 Revocation

Per \[Topic 7] of Annex 2 of the ARF:

In the current WE BUILD LSP deployment, **revocation is out of scope**. Wallet instances and TaxID attestations are assumed not to be revoked during the pilot. Future deployments targeting production or cross-border use SHOULD define a revocation mechanism in conformance with one of the following methods (as applicable at the time of that deployment):

* An Attestation Status List mechanism included in a Technical Specification specified by the Commission.
* An Attestation Revocation List mechanism included in a Technical Specification specified by the Commission.

Where the TaxID attestation has a short validity period (24 hours or less), revocation is not required.

Note: The presence of an optional `expiry_date` attribute enables time-limited issuance, which reduces the need for active revocation. Issuers SHOULD set an appropriate `expiry_date` that reflects the expected validity of the tax identification data and the renewal cycle of the issuing authority.

***

## 7 Compliance

This rulebook addresses compliance with the High-Level Requirements of \[Topic 12] of Annex 2 of the ARF. The table below maps each relevant ARB requirement to its coverage in this rulebook.

| **Requirement**                                                                                     | **ARF Reference**        | **Coverage in this Rulebook**                                                                                                                                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| At least one standardised format SHALL be specified.                                                | ARB\_1                   | § 3: SD-JWT VC (primary), mdoc (§ 3.1), and W3C VCDM v2.0 (§ 3.3, pending) all addressed.                                                                                                                                                                                                       |
| Proximity (offline) presentation requirement SHALL be analysed; if needed, mdoc SHALL be specified. | ARB\_2                   | §§ 3.1 and 4.3: proximity presentation analysed; mdoc MAY be used where required by Member State governance. Not mandated by default.                                                                                                                                                           |
| SD-JWT VC format SHALL be specified if required.                                                    | ARB\_3                   | § 3.2: SD-JWT VC is the primary encoding; conformance with \[HAIP] required.                                                                                                                                                                                                                    |
| W3C VCDM MAY be specified for non-qualified EAA.                                                    | ARB\_4                   | § 3.3: framework reserved for non-qualified EAA use; encoding not yet specified (OI-05 — open).                                                                                                                                                                                                 |
| A unique attestation/document type SHALL be defined.                                                | ARB\_5                   | §§ 2.1, 3.1, 3.2: `eu.europa.ec.eudi.taxid.1` proposed for both mdoc and SD-JWT VC; **pending consortium confirmation (OI-01 — open)**.                                                                                                                                                         |
| Attributes SHALL be defined in an encoding-independent manner within a unique namespace.            | ARB\_6, ARB\_6a, ARB\_6b | Chapter 2: all attributes encoding-independent. Namespace `eu.europa.ec.eudi.taxid.1` proposed in § 2.1; **subject to OI-01 resolution**. Claim names conform to IANA, Public Name, or Private Name requirements.                                                                               |
| Existing attribute conventions and catalogues SHOULD be considered.                                 | ARB\_7                   | §§ 2.2–2.3: PID-aligned attributes (`family_name`, `given_name`, `birth_date`) reuse ARF PID definitions.                                                                                                                                                                                       |
| `attestation_legal_category` SHALL be defined.                                                      | ARB\_11 / ARB\_12        | §§ 2.1, 2.5, 3.1, 3.2: `attestation_legal_category` defined; value `"QEAA"`, `"PuB-EAA"`, or `"non-qualified-EAA"`. Not selectively disclosable.                                                                                                                                                |
| Issuer identity and country metadata SHALL be included.                                             | ARB\_13–ARB\_15          | § 2.5: `issuing_authority` (see OI-03) and `issuing_country` defined as mandatory metadata.                                                                                                                                                                                                     |
| Subject identity attributes SHALL be included.                                                      | ARB\_16–ARB\_17          | § 2.2: `family_name`, `given_name`, `birth_date` defined as mandatory attributes.                                                                                                                                                                                                               |
| Validity period metadata SHALL be included.                                                         | ARB\_18–ARB\_19          | §§ 2.5/2.6: `issuance_date` (mandatory) and `expiry_date` (optional) defined.                                                                                                                                                                                                                   |
| Trust anchor location SHALL be indicated.                                                           | ARB\_20–ARB\_21          | § 5: trust anchor via EU Trusted List for QEAA/PuB-EAA (`trust_anchor_location` omitted, IR-04). For non-qualified EAA, `trust_anchor_location` (§ 2.7) carries the machine-readable trust anchor URL; interim resolution model defined in § 5 pending Commission specification (OI-07 — open). |
| PID verification requirement SHALL/SHOULD be specified.                                             | ARB\_27                  | § 4.2: relying parties SHOULD request and verify PID alongside TaxID where identity verification is required.                                                                                                                                                                                   |
| Device binding and cryptographic binding specification.                                             | ARB\_28, ARB\_34         | § 4.4: device binding SHOULD be applied; `cryptographically_bound_to` defined as conditional attribute in § 2.4 with values `"eu.europa.ec.eudi.pid.1"` (mdoc) / `"urn:eudi:pid:1"` (SD-JWT VC). Omitted when not device-bound.                                                                 |
| Selective disclosure specification SHALL be provided.                                               | ARB\_30, ARB\_31         | §§ 3.2 and 4.3: per-claim SD-JWT disclosability specified; non-disclosable metadata rationale provided. Flat object — no recursive disclosures required.                                                                                                                                        |

***

## 8 References

| **Item Reference**                      | **Standard name / details**                                                                                                                                                                                                                                              |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| \[European Digital Identity Regulation] | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework |
| \[ARF]                                  | The Common Union Toolbox for a Coordinated Approach Towards a European Digital Identity Framework – The European Digital Identity Wallet Architecture and Reference Framework, Version 1.4.0                                                                             |
| \[HLR]                                  | ARF Annex 2 – High Level Requirements                                                                                                                                                                                                                                    |
| \[Topic 7]                              | ARF Annex 2 – Topic 7 – Attestation revocation and revocation checking                                                                                                                                                                                                   |
| \[Topic 10]                             | ARF Annex 2 – Topic 10 – Issuing a PID or attestation to a Wallet Unit                                                                                                                                                                                                   |
| \[Topic 12]                             | ARF Annex 2 – Topic 12 – Attestation Rulebooks                                                                                                                                                                                                                           |
| \[Topic 20]                             | ARF Annex 2 – Topic 20 – Strong User authentication for electronic payments                                                                                                                                                                                              |
| \[2015/1505]                            | Commission Implementing Decision (EU) 2015/1505 of 8 September 2015 laying down technical specifications and formats relating to trusted lists pursuant to Article 22(5) of Regulation (EU) No 910/2014                                                                  |
| \[HAIP]                                 | Yasuda, K. et al., OpenID4VC High Assurance Interoperability Profile, OpenID Foundation, Version draft-03                                                                                                                                                                |
| \[IANA-JWT-Claims]                      | IANA JSON Web Token Claims Registry                                                                                                                                                                                                                                      |
| \[ISO/IEC 18013-5]                      | ISO/IEC 18013-5, Personal identification — ISO-compliant driving licence — Part 5: Mobile driving licence (mDL) application, First edition, 2021-09                                                                                                                      |
| \[ISO 3166-1]                           | ISO 3166-1, Codes for the representation of names of countries and their subdivisions — Part 1: Country codes                                                                                                                                                            |
| \[ISO 3166-2]                           | ISO 3166-2:2020, Codes for the representation of names of countries and their subdivisions — Part 2: Country subdivision codes, Clause 8                                                                                                                                 |
| \[ISO 13616]                            | ISO 13616-1:2020, Financial services — International bank account number (IBAN)                                                                                                                                                                                          |
| \[OIDC]                                 | Sakimura, N. et al., "OpenID Connect Core 1.0", OpenID Foundation                                                                                                                                                                                                        |
| \[OpenID4VP]                            | OpenID for Verifiable Presentations specification                                                                                                                                                                                                                        |
| \[RFC 2119]                             | RFC 2119 – Key words for use in RFCs to Indicate Requirement Levels, S. Bradner, March 1997                                                                                                                                                                              |
| \[RFC 3339]                             | RFC 3339 – Date and Time on the Internet: Timestamps, G. Klyne et al., July 2002                                                                                                                                                                                         |
| \[RFC 3986]                             | RFC 3986 – Uniform Resource Identifier (URI): Generic Syntax, T. Berners-Lee et al., January 2005                                                                                                                                                                        |
| \[RFC 7517]                             | RFC 7517 – JSON Web Key (JWK), M. Jones, May 2015                                                                                                                                                                                                                        |
| \[RFC 8259]                             | RFC 8259 – The JavaScript Object Notation (JSON) Data Interchange Format, T. Bray, Ed., December 2017                                                                                                                                                                    |
| \[RFC 8610]                             | RFC 8610 – Concise Data Definition Language (CDDL), H. Birkholz et al., June 2019                                                                                                                                                                                        |
| \[RFC 8943]                             | RFC 8943 – CBOR Tags for Date, M. Jones et al., November 2020                                                                                                                                                                                                            |
| \[RFC 8949]                             | RFC 8949 – Concise Binary Object Representation (CBOR), C. Bormann et al., December 2020                                                                                                                                                                                 |
| \[SD-JWT VC]                            | SD-JWT-based Verifiable Credentials (SD-JWT VC), version draft-ietf-oauth-sd-jwt-vc-09                                                                                                                                                                                   |
| \[W3C VCDM v2.0]                        | Sporny, M. et al., Verifiable Credentials Data Model v2.0, W3C Recommendation                                                                                                                                                                                            |

