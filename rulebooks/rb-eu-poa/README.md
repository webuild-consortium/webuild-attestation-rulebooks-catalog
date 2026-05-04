* Template version: 1.1, 08-04-2026


# Attestation Rulebook for attestations of type EU Power of Attorney (EU PoA)

* Author(s):
    * Erwin Nieuwlaar, [KVK](https://kvk.nl)
    * Astrid Verhallen, [Infogreffe](https://www.infogreffe.fr/)


| Version          | Date               | Description                                      |
|------------------|--------------------|--------------------------------------------------|
| 0.1              | 09-04-2026         | Initial Draft based on the EUDI/WE BUILD rulebook template and [EU PoA description](https://portal.webuildconsortium.eu/group/bu2-create-company-branch/files?mid=7066&fid%5B0%5D=56&fid%5B1%5D=58&fid%5B2%5D=6220&fid%5B3%5D=6620)    |

**Feedback:**
Main feedback channel: [GitHub issues](https://github.com/webuild-consortium/eudi-wallet-rulebooks-and-schemas/issues)

## 1 Introduction

### 1.1 Document scope and purpose

This attestation represents a legally valid Power of Attorney (EU PoA) issued within the European Union.
It embodies:

- The identification of a principal (natural person acting on behalf of a legal entity)
- The identification and registration details of the company
- The designation of an attorney (delegate)
- The defined scope of representation
- The validity period
- The applicable law
- The signing details
- A reference to the EU Company Certificate (EUCC) if applicable

This attestation enables a relying party to verify that an attorney (delegate) has been granted specific powers of representation by a principal acting on behalf of a legal entity. The specific powers are limited to 6: the formation of companies; changes to the instrument of constitution of companies and the statutes if contained in a separate instrument; registration and closure of branches of the company; all legal transactions regarding cross-border conversions involving the company; all legal transactions regarding cross-border mergers involving the company; and all legal transactions regarding cross-border divisions involving the company. The EU PoA complements the EU Company Certificate (EUCC) by providing granular delegation information beyond the company's registered legal representatives.

### 1.2 Document structure

- Chapter 2, Attestation attributes and metadata in an encoding-independent manner.
- Chapter 3, Attestation attributes for the specific encoding [SD-JWT VC].
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

In addition to the attributes definition necessary to understand the data schema, it is important to understand:

| Term                 | Definition in WE BUILD Context                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Principal            | A natural person who acts on behalf of a legal entity and grants authority to an attorney (delegate) through a Power of Attorney.                                                                                                                                                                                                                                                                                                                              |
| Attorney (Delegate)  | A natural person designated by the principal to act on behalf of the legal entity within the defined scope of representation.                                                                                                                                                                                                                                                                                                                                  |
| Power of Attorney    | A legal instrument by which one person (the principal) authorises another person (the attorney) to act on their behalf in specified legal or business matters.                                                                                                                                                                                                                                                                                                 |
| Scope of Representation | The defined set of powers and authorities granted to the attorney under the Power of Attorney.                                                                                                                                                                                                                                                                                                                                                              |

## 2 Attestation attributes and metadata

*This section is used for defining all attributes that an
attestation of the defined type may contain. In this section
the attributes SHALL be defined in an encoding-independent manner (see ARB_06 in [Topic 12]).
Each attribute can be mandatory, optional, or conditional,
and it SHALL be specified in the corresponding section (see ARB_09 in [Topic 12]).*

*When attributes are defined, referring to attributes that
already exist in a catalogue of attestation attributes
SHOULD be considered (see ARB_07 in [Topic 12]).*

### 2.1 Introduction

The EU Power of Attorney attestation SHALL be represented as a single flat object.

The attestation attributes are defined in the sections below. The attribute identifiers SHALL be used in requests and responses. There SHALL be at most one attribute with the same attribute identifier in each attestation.

The optionality column specifies whether the presence of the attribute in an attestation is mandatory (M) or optional (O).

NOTE: If an attribute is indicated as mandatory, this solely means that the Issuer SHALL ensure that this element is present in the attestation. It does not imply that a Relying Party is required to request such an attribute when interacting with the Wallet Instance. Neither does it imply that the User cannot refuse to release a mandatory attribute if requested.

The encoding format column indicates how the data elements SHALL be encoded, using the CDDL representation types defined in [RFC 8610].

### 2.2 Mandatory attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------|--------------|--------------|--------------|
| attestation_legal_category | TBD | One of EAA, Pub-EAA or QEAA | string | QEAA |
| date_of_execution | TBD | Date the PoA was executed | string (date) | 2026-01-15 |
| euid_reference | TBD | EUID reference | string | NLNHR.12345678 |
| principal_full_name | TBD | Legal full name of the principal | string | Frouke Janssen |
| principal_date_of_birth | TBD | Date of birth of the principal | string (date) | 1980-03-22 |
| company_statutory_full_name | TBD | Registered legal name of the company | string | FictiveCo B.V. |
| company_business_register_name | TBD | Name of the business register | string | Kamer van Koophandel |
| company_jurisdiction | TBD | Country of incorporation | string | NL |
| attorney_full_name | TBD | Legal full name of the attorney | string | Maria Schmidt |
| scope_of_representation_powers | TBD | Granted powers | array\<string\> | ["The formation of companies", "Registration and closure of branches of the Company"] |
| validity_period_valid_from | TBD | Start date of validity | string (date) | 2026-01-15 |
| validity_period_valid_until | TBD | End date of validity | string (date) | 2027-01-15 |
| applicable_law_jurisdiction | TBD | Governing Member State law | string | NL |
| signing_place | TBD | Place of signing | string | Hardenberg |
| signing_date | TBD | Date of signing | string (date) | 2026-01-15 |

### 2.3 Optional attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------|--------------|--------------|--------------|
| principal_identification_document_kind | TBD | Type of ID document of the principal | string | passport |
| principal_identification_document_number | TBD | ID document number of the principal | string | NZ1234567 |
| principal_place_of_birth | TBD | Place of birth of the principal | string | Utrecht |
| principal_full_address | TBD | Residential address of the principal | string | Herengracht 100, 1015 AA Amsterdam, Netherlands |
| company_business_register_location | TBD | Location of the business register | string | The Hague |
| company_kind_of_legal_entity | TBD | Legal form (e.g. GmbH, SARL, SA) | string | B.V. |
| company_registered_office | TBD | Registered office address | string | Keizersgracht 200, 1016 DW Amsterdam, Netherlands |
| attorney_date_of_birth | TBD | Date of birth of the attorney | string (date) | 1985-07-10 |
| attorney_identification_document_kind | TBD | Type of ID document of the attorney | string | national_id_card |
| attorney_identification_document_number | TBD | ID document number of the attorney | string | DE9876543 |
| attorney_place_of_birth | TBD | Place of birth of the attorney | string | Groningen |
| attorney_full_address | TBD | Residential address of the attorney | string | Friesestraatweg 3157, 7772CP Groningen, Netherlands |
| scope_of_representation_power_of_substitution | TBD | Whether substitution is allowed | string | not_allowed |

### 2.4 Conditional attributes

No conditional attributes are defined for this attestation.

### 2.5 Mandatory metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------|--------------|--------------|--------------|
| expiry_date | TBD | Date (and if possible time) when the attestation will expire. Does not need to be an attribute and can be covered by credential format metadata, such as for example the "exp" field on the SD-JWT format (TBD if we can remove this attribute and use the "exp" field only). | date | 2027-01-15 |
| issuing_authority | TBD | Name of the administrative authority that issued the EU PoA, or the ISO 3166 alpha-2 country code of the respective Member State if there is no separate authority entitled to issue the EU PoA. | string | Kamer van Koophandel |
| issuing_country | TBD | Alpha-2 country code, as specified in ISO 3166-1, of the country or territory of the provider of the attestation. | string | NL |

### 2.6 Optional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------|--------------|--------------|--------------|
| location_status | TBD | The location of validity status information where the providers revoke attestations. This attribute is required when the validity time period of the attestation exceeds 24 hours. | string | https://issuer.example.com/status/1 |
| trust_anchor | TBD | This attribute indicates at least the URL at which a machine-readable version of the trust anchor to be used for verifying the EU PoA can be found or looked up. | string | https://issuer.example.com/trust-anchor |

### 2.7 Conditional metadata

No conditional metadata are defined for this attestation.

### 2.8 Code lists

| **Field name** | **Allowed values** | **Meaning** | **Source / vocabulary** | **Notes / extensibility** |
|----------------|--------------------|-------------|--------------------------|---------------------------|
| `principal_identification_document_kind` / `attorney_identification_document_kind` | `passport`, `national_id_card`, `residence_permit`, `driving_license` | Type of identification document presented by the principal or attorney | EU PoA attestation definition |  |
| `scope_of_representation_power_of_substitution` | `allowed`, `not_allowed`, `limited` | Whether the attorney may delegate the granted powers to a third party | EU PoA attestation definition | If `limited`, additional limitation details MUST be included in `scope_of_representation_powers` |
| `scope_of_representation_powers` | `The formation of companies`, `Changes to the instrument of constitution of companies and the statutes if contained in a separate instrument`, `Registration and closure of branches of the Company`, `All legal transactions regarding cross-border conversions involving the Company`, `All legal transactions regarding cross border mergers involving the Company`, `All legal transactions regarding cross border divisions involving the Company` | The specific powers granted to the attorney | EU PoA attestation definition |  |

### 2.9 Integrity rules

| **Rule ID** | **Rule statement** | **Why it exists** | **Where enforced** | **Verifier / issuer behavior on failure** |
|-------------|--------------------|-------------------|--------------------|-------------------------------------------|
| `IR-01` | `validity_period_valid_until` MUST be later than `validity_period_valid_from`. | Prevents nonsensical validity periods where the PoA would expire before it becomes effective. | Issuer business rules, schema validation, and verifier business validation. | Issuer SHALL reject the PoA; verifier SHALL treat the attestation as invalid. |
| `IR-02` | `date_of_execution` MUST be equal to or earlier than `validity_period_valid_from`. | Ensures the PoA was executed before or on the date it becomes effective. A PoA cannot take effect before it was executed. | Issuer business rules, schema validation, and verifier business validation. | Issuer SHALL reject the PoA; verifier SHALL treat the attestation as invalid. |
| `IR-03` | The principal must have legal authority to act on behalf of the company. | Prevents invalid delegation chains where a person without authority grants powers to an attorney. | Issuer business rules (verified during issuance). | Issuer SHALL reject issuance if principal authority cannot be established. |
| `IR-04` | If `scope_of_representation_power_of_substitution` = `limited`, additional limitation details MUST be included in `scope_of_representation_powers`. | Ensures that when substitution is restricted, the exact limitations are clearly specified and verifiable. | Issuer business rules and schema validation. | Issuer SHALL reject the PoA if limitation details are missing; verifier SHALL treat the scope as ambiguous and request clarification. |

# 3 Attestation encoding

## 3.1 ISO/IEC 18013-5-compliant encoding

ISO/IEC 18013-5 (also called mdoc) is not currently included in this rulebook. Should a use case arise that requires offline proximity presentation for the EU PoA, support for this standard may be added in a future version.

### 3.2 SD-JWT VC-based encoding

The EU PoA attestation uses the SD-JWT VC format to allow for selective disclosure of PoA attributes.

**Verifiable Credential Type (`vct`):** `uri:eu.eudi.eu-poa.1`

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Reference/Notes** | **Disclosable** |
|---------------------|--------------------------|---------------------|---------------------|-----------------|
| attestation_legal_category | attestation_legal_category | string | One of EAA, Pub-EAA, QEAA as defined by eIDAS 2 | MUST NOT |
| issuing_authority | iss | string | RFC 7519 / Section 2.5 | MUST NOT |
| expiry_date | exp | number | RFC 7519 / Section 2.5 (Unix timestamp) | MUST NOT |
| issuing_country | issuing_country | string | ISO 3166-1 alpha-2 | MUST NOT |
| date_of_execution | date_of_execution | string | ISO 8601 (YYYY-MM-DD) | MUST |
| euid_reference | euid_reference | string | EUID | MUST |
| principal_full_name | principal_full_name | string | | MUST |
| principal_date_of_birth | principal_date_of_birth | string | ISO 8601 (YYYY-MM-DD) | MUST |
| principal_identification_document_kind | principal_identification_document_kind | string | See code list in Section 2.8 | MUST |
| principal_identification_document_number | principal_identification_document_number | string | | MUST |
| principal_place_of_birth | principal_place_of_birth | string | | MUST |
| principal_full_address | principal_full_address | string | | MUST |
| company_statutory_full_name | company_statutory_full_name | string | | MUST |
| company_business_register_name | company_business_register_name | string | | MUST |
| company_business_register_location | company_business_register_location | string | | MUST |
| company_kind_of_legal_entity | company_kind_of_legal_entity | string | | MUST |
| company_jurisdiction | company_jurisdiction | string | ISO 3166-1 alpha-2 | MUST |
| company_registered_office | company_registered_office | string | | MUST |
| attorney_full_name | attorney_full_name | string | | MUST |
| attorney_date_of_birth | attorney_date_of_birth | string | ISO 8601 (YYYY-MM-DD) | MUST |
| attorney_identification_document_kind | attorney_identification_document_kind | string | See code list in Section 2.8 | MUST |
| attorney_identification_document_number | attorney_identification_document_number | string | | MUST |
| attorney_place_of_birth | attorney_place_of_birth | string | | MUST |
| attorney_full_address | attorney_full_address | string | | MUST |
| scope_of_representation_powers | scope_of_representation_powers | array\<string\> | See code list in Section 2.8 | MUST |
| scope_of_representation_power_of_substitution | scope_of_representation_power_of_substitution | string | See code list in Section 2.8 | MUST |
| validity_period_valid_from | validity_period_valid_from | string | ISO 8601 (YYYY-MM-DD) | MUST NOT |
| validity_period_valid_until | validity_period_valid_until | string | ISO 8601 (YYYY-MM-DD) | MUST NOT |
| applicable_law_jurisdiction | applicable_law_jurisdiction | string | ISO 3166-1 alpha-2 | MUST |
| signing_place | signing_place | string | | MUST |
| signing_date | signing_date | string | ISO 8601 (YYYY-MM-DD) | MUST |

#TODO: Provide an example of the issued SD-JWT (in Base64 encoding).


## 4 Attestation usage

#TODO: *Briefly describe the primary use cases or scenarios for which this attestation type is intended.*


## 5 Trust anchors

#TODO

Mechanisms for the provision of a trust anchor that SHALL
be used for the verification of an attestation SHALL be defined in this section.

It is noted that the ARF specifies the following for QEAAs and Pub-EAAs

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



## 6 Revocation

#TODO

(Refer to [Topic 7] of the ARF for a list of High-Level Requirements related to Revocation)

In this section information about the revocation mechanism used SHALL be defined.

For PID, QEAA, or PuB-EAA it SHALL be defined whether only short-lived attestations
will be used, having a validity period of 24 hours or less, such that revocation
will never be necessary, or that the attestations are revocable.

For revocable attestations it SHALL be defined which of the following methods must be implemented:
* Use an Attestation Status List mechanism.
* Use an Attestation Revocation List mechanism.

## 7 Compliance

#TODO

## 8 References

| **Item Reference** | **Standard name/details**|
|--------------------|---------------------------|
| [European Digital Identity Regulation] | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework |
| [ISO/IEC 18013-5] |  ISO/IEC 18013-5, Personal identification --- ISO-compliant driving licence - Part 5: Mobile driving licence (mDL) application, First edition, 2021-09 |
| [RFC 3339] | RFC 3339  - Date and Time on the Internet: Timestamps, G. Klyne et al., July 2002 |
| [RFC 8610] | RFC 8610  - Concise Data Definition Language (CDDL): A Notational Convention to Express Concise Binary Object Representation (CBOR) and JSON Data Structures, H. Birkholz et al., June 2019 |
| [RFC 8943] | RFC 8943  - Concise Binary Object Representation (CBOR) Tags for Date, M. Jones et al., November 2020 |
| [RFC 8949] | RFC 8949 - Concise Binary Object Representation (CBOR), C. Bormann et al., December 2020 |
| [SD-JWT VC] |  SD-JWT-based Verifiable Credentials (SD-JWT VC). Available: <https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/>, version draft-ietf-oauth-sd-jwt-vc-09  |
| [Topic 7] | ARF Annex 2 - Topic 7 - Attestation revocation and revocation checking Available: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a237-topic-7-attestation-revocation-and-revocation-checking>|
| [Topic 12] | ARF Annex 2 - Topic 12 - Attestation Rulebooks, Available: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a2312-topic-12-attestation-rulebooks>|
