(Template version: 1.1)

# WE BUILD Attestation Rulebook for attestations of type *Ferry Loyalty Card*

*[Based on the WE BUILD Attestation Rulebook Template and the Ferry Loyalty Card Attestation model.]*

* Author(s):
    * Nikos Triantafyllou, UAegean
* Previous Authors
    * N/A

| Version | Date | Description |
|---------|------|-------------|
| 0.1 | 2026-06-01 | Initial draft rulebook for the Ferry Loyalty Card Attestation |
| 0.9 | 2026-06-23 | Draft, ready for review/QA |

**Feedback:**

* Github, portal, email, Slack

## 1 Introduction

### 1.1 Document scope and purpose

This Rulebook defines the *Ferry Loyalty Card Attestation* for use in the European Digital Identity Wallet ecosystem.

The Ferry Loyalty Card Attestation expresses the real-world fact that a natural person is a registered customer of a ferry operator and participates in that operator's loyalty or frequent traveller programme. It proves the existence and validity of a loyalty card issued by, or on behalf of, a ferry operator.

The attestation is intended to be issued by an authentic source, such as a ferry operator or an authorised customer-management or ticketing system acting on behalf of the ferry operator. The Holder is the registered customer to whom the loyalty card applies. Relying Parties include ferry operators, authorised ticketing systems, customer-service systems, booking portals, port services, and other authorised partners that need to verify customer loyalty status or customer identity information for a legitimate service purpose.

In practical terms, the attestation enables a customer to present loyalty-card information through an EUDI Wallet. It can support customer identification, service personalisation, loyalty benefits, journey-related discounts, and reduced reliance on physical loyalty cards or account lookups.

The attestation contains customer, loyalty-card, organisation, and credential metadata. Because it is intended for repeated use across multiple journeys, it is longer-lived than a boarding pass and SHALL support revocation or status checking where operationally required.

### 1.2 Document structure

This Rulebook is structured as follows:

* Chapter 2 describes the attestation attributes and metadata in an encoding-independent manner.
* Chapter 3 specifies how the attestation attributes and metadata are encoded using SD-JWT VC. ISO/IEC 18013-5 and W3C VCDM encodings are not defined in this version of the Rulebook.
* Chapter 4 specifies attestation usage, including presentation and verification expectations.
* Chapter 5 defines how trust anchors for attestation verification can be obtained.
* Chapter 6 defines revocation and expiry mechanisms.
* Chapter 7 provides compliance information.
* Chapter 8 lists references.

### 1.3 Key words

This document uses the capitalised key words 'SHALL', 'SHOULD' and 'MAY' as specified in [RFC 2119], i.e., to indicate requirements, recommendations and options specified in this document.

In addition, 'must' (non-capitalised) is used to indicate an external constraint, i.e., a requirement that is not mandated by this document, but, for instance, by an external document. The word 'can' indicates a capability, whereas other words, such as 'will', and 'is' or 'are' are intended as statements of fact.

### 1.4 Terminology

This document uses the terminology specified in Annex 1 of the ARF.

In addition, the following domain-specific terms are used:

| Term | Meaning |
|------|---------|
| Ferry Loyalty Card Attestation | A Verifiable Credential representing a customer's membership in a ferry operator's loyalty or frequent traveller programme. |
| Ferry operator | The organisation operating ferry services and managing, or authorising the management of, the loyalty programme. |
| Authorised customer-management system | A system authorised by the ferry operator to create, manage, or issue loyalty-card records. |
| Customer | The natural person to whom the loyalty card applies. |
| Loyalty card | A customer identifier or membership record used by a ferry operator to recognise loyalty-programme participation. |
| Loyalty programme | A ferry operator programme used to provide customer identification, service personalisation, benefits, or journey-related offers. |

## 2 Attestation attributes and metadata

### Chapter overview and requirements

This chapter defines the attributes and metadata that a Ferry Loyalty Card Attestation may contain. The attributes are defined in an encoding-independent manner. Each attribute is classified as mandatory, optional, or conditional.

The Ferry Loyalty Card Attestation is a reusable, customer-specific attestation. It is not bound to a single journey. Its attribute set is designed to support customer identification, loyalty-card verification, and controlled disclosure of optional customer information.

### 2.1 Introduction

The Ferry Loyalty Card Attestation is defined as a non-qualified Electronic Attestation of Attributes unless a future version of this Rulebook explicitly defines a qualified or public-sector legal category.

The attribute `attestation_legal_category` SHALL be included and SHALL have the value `non-qualified-EAA`.

The attestation model consists of the following logical groups:

* customer information;
* loyalty-card information;
* organisation information;
* credential metadata.

The attestation is bound to a single registered customer and a single loyalty-card record issued by a specific ferry operator or authorised operator system. It MAY be presented repeatedly, subject to validity, expiry, and revocation rules.

### 2.2 Mandatory attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---------------------|------------------------|----------------|---------------|-------------------|
| `attestation_legal_category` | ARF Topic 12 / Rulebook legal category indication | Indicates the legal category of the attestation. | string | `non-qualified-EAA` |
| `customer.first_name` | OIDC `given_name` where applicable | Customer given name. | string | `Nikos` |
| `customer.last_name` | OIDC `family_name` where applicable | Customer family name. | string | `Triantafyllou` |
| `loyalty_card.id` | N/A | Unique loyalty-card identifier issued by the ferry operator. | string | `LC-FAST-000123456` |
| `loyalty_card.issue_date` | ISO 8601 date | Date on which the loyalty card was issued. | date | `2026-01-07` |
| `organization.name` | N/A | Legal or operating name of the ferry operator. | string | `Fast Ferries S.A.` |
| `organization.id` | N/A | Ferry operator identifier. | string | `GR-FAST-FERRIES` |
| `organization.country` | ISO 3166-1 alpha-2 recommended | Country of registration or operation of the ferry operator. | string | `GR` |
| `credential.type` | Rulebook-defined credential type | Type of credential represented by the attestation. | string | `FerryLoyaltyCardAttestation` |
| `credential.issuer` | SD-JWT VC / issuer identifier | Issuer of the credential. | string | `https://issuer.example-ferry.gr` |
| `credential.issuance_date` | ISO 8601 date | Date on which the credential was issued. | date | `2026-01-07` |

### 2.3 Optional attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---------------------|------------------------|----------------|---------------|-------------------|
| `customer.nationality` | ISO 3166-1 alpha-2 recommended | Nationality of the customer. | string | `GR` |
| `customer.birth_date` | ISO 8601 date | Customer date of birth. | date | `1985-04-12` |
| `customer.address` | N/A | Customer street address. | string | `1 Example Street` |
| `customer.city` | N/A | City of residence. | string | `Athens` |
| `customer.zip_code` | N/A | Postal code. | string | `10557` |
| `customer.phone` | N/A | Fixed phone number. | string | `+302101234567` |
| `customer.mobile` | N/A | Mobile phone number. | string | `+306901234567` |
| `customer.email` | RFC 5322 | Customer email address. | string | `nikos@example.com` |
| `credential.expiry_date` | ISO 8601 date | Date after which the credential SHALL NOT be accepted. | date | `2028-01-07` |

### 2.4 Conditional attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---------------------|------------------------|----------------|---------------|-------------------|
| `credential.expiry_date` | ISO 8601 date | SHALL be present where the loyalty programme issues cards with a defined expiry date. MAY be omitted where the card remains valid until revoked. | date | `2028-01-07` |
| `customer.birth_date` | ISO 8601 date | SHOULD be present only where age-related checks, age-based benefits, or customer disambiguation require it. | date | `1985-04-12` |
| `customer.email` | RFC 5322 | SHOULD be present only where the customer has consented to share email contact information or where it is required for the specific service interaction. | string | `nikos@example.com` |
| `customer.address`, `customer.city`, `customer.zip_code` | N/A | SHOULD be present only where residency, address-based service rules, billing, or customer-service processes require address information. | string | `Athens` |
| `customer.phone`, `customer.mobile` | N/A | SHOULD be present only where phone contact information is required for the relevant customer interaction. | string | `+306901234567` |

### 2.5 Mandatory metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---------------------|------------------------|----------------|---------------|-------------------|
| `vct` | SD-JWT VC | Verifiable Credential Type identifying this attestation type. | string | `urn:eu.europa.ec.eudi:ferry_loyalty_card:1` |
| `iss` | SD-JWT VC / JWT | Identifier of the issuer of the credential. | string | `https://issuer.example-ferry.gr` |
| `iat` | JWT | Time at which the credential was issued. | integer | `1767787200` |
| `cnf` | SD-JWT VC / JOSE | Confirmation claim binding the credential to key material controlled by the Holder or Wallet Unit, where holder binding is used. | object | `{ "jwk": { ... } }` |
| `status` | SD-JWT VC status mechanism, where used | Status information enabling revocation or suspension checks. SHOULD be used for this reusable attestation type. | object | `{ "status_list": { ... } }` |

### 2.6 Optional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---------------------|------------------------|----------------|---------------|-------------------|
| `nbf` | JWT | Time before which the credential MUST NOT be accepted. | integer | `1767787200` |
| `exp` | JWT | Expiration time of the credential, where the credential has a technical expiry timestamp. SHOULD correspond to or not exceed `credential.expiry_date` where that attribute is present. | integer | `1830859200` |
| `jti` | JWT | Unique identifier of the credential instance. | string | `urn:uuid:ec622e9e-23f8-4c1d-9985-5c5b088caa11` |
| `trust_anchor` | ARF Topic 12 | Location or identifier of the machine-readable trust anchor or trust framework entry used to verify issuer authorisation. | string | `https://trust.example.eu/ferry/operators/fast-ferries` |
| `cryptographically_bound_to` | ARF Topic 12 / ARB_28 | Identifier of another attestation type to which this attestation is cryptographically bound, where such binding is used. | string | `urn:eudi:pid:1` |

### 2.7 Conditional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---------------------|------------------------|----------------|---------------|-------------------|
| `exp` | JWT | SHALL be present where the credential has a fixed validity period. SHOULD be present where `credential.expiry_date` is present. | integer | `1830859200` |
| `status` | SD-JWT VC status mechanism, where used | SHALL be present where the issuer supports revocation or suspension. SHOULD be present for reusable loyalty-card attestations. | object | `{ "status_list": { ... } }` |
| `cryptographically_bound_to` | ARF Topic 12 / ARB_28 | SHOULD be present where the loyalty card is required to be presented together with PID or another identity attestation for stronger customer identity matching. | string | `urn:eudi:pid:1` |

### 2.8 Code lists

| **Field name** | **Allowed values** | **Meaning** | **Source / vocabulary** | **Notes / extensibility** |
|----------------|--------------------|-------------|--------------------------|---------------------------|
| `customer.nationality` | ISO 3166-1 country codes | Identifies the nationality of the customer. | ISO 3166-1 | Alpha-2 representation is RECOMMENDED unless the ecosystem profile specifies otherwise. |
| `organization.country` | ISO 3166-1 country codes | Identifies the country of registration or operation of the ferry operator. | ISO 3166-1 | Alpha-2 representation is RECOMMENDED. |
| `loyalty_card.issue_date` | ISO 8601 date | Date on which the loyalty card was issued. | ISO 8601 | Date-only format SHOULD be used. |
| `credential.issuance_date` | ISO 8601 date | Date on which the credential was issued. | ISO 8601 | Date-only format SHOULD be used. |
| `credential.expiry_date` | ISO 8601 date | Date after which the credential SHALL NOT be accepted. | ISO 8601 | Date-only format SHOULD be used. |
| `customer.birth_date` | ISO 8601 date | Customer date of birth. | ISO 8601 | Date-only format SHOULD be used. |
| `customer.email` | Valid email address syntax | Customer email address. | RFC 5322 | Verifiers SHALL NOT request this attribute unless needed for the specific interaction. |
| `attestation_legal_category` | `non-qualified-EAA`, `QEAA`, `PuB-EAA` | Indicates the legal category of the attestation. | ARF Topic 12 / Rulebook template | This Rulebook uses `non-qualified-EAA`. |

### 2.9 Integrity rules

| **Rule ID** | **Rule statement** | **Why it exists** | **Where enforced** | **Verifier / issuer behavior on failure** |
|-------------|--------------------|-------------------|--------------------|-------------------------------------------|
| `LC-IR-01` | `loyalty_card.id` MUST be unique per issuer. | Enables unambiguous identification of the loyalty-card record. | Issuer business rules and verifier business validation. | Issuer SHALL prevent duplicate active card identifiers. Verifier MAY reject duplicated identifiers if detected. |
| `LC-IR-02` | If `credential.expiry_date` is present, it MUST be later than `credential.issuance_date`. | Prevents temporally invalid credentials. | Issuer business rules, schema validation, verifier business validation. | Issuer SHALL reject invalid validity periods. Verifier SHALL reject credentials with invalid validity periods. |
| `LC-IR-03` | Expired loyalty cards SHALL NOT be accepted. | Ensures that relying parties do not provide benefits or services based on expired membership. | Verifier freshness checks and business validation. | Verifier SHALL reject the attestation if the credential is expired. |
| `LC-IR-04` | The attestation SHALL refer to a single loyalty-card record and a single issuing organisation. | Prevents ambiguous membership claims. | Issuer business rules and verifier business validation. | Issuer SHALL reject ambiguous source data. Verifier SHALL reject the attestation if issuer or organisation data is inconsistent. |
| `LC-IR-05` | Optional contact and address attributes SHALL be requested and disclosed only where required for the specific service interaction. | Supports data minimisation and selective disclosure. | Wallet presentation policy, verifier request policy, and relying-party business rules. | Verifier SHALL NOT require unnecessary optional attributes. Wallet SHOULD allow the Holder to review and consent to disclosure. |
| `LC-IR-06` | Where identity matching is required, `customer.first_name` and `customer.last_name` SHOULD be compared with PID or another accepted identity source. | Ensures that the presenter is the customer to whom the loyalty card applies. | Relying Party business validation. | Verifier SHOULD reject the transaction where required identity matching fails. |

# 3 Attestation encoding

## 3.1 ISO/IEC 18013-5-compliant encoding

This version of the Rulebook does not define an ISO/IEC 18013-5 mdoc encoding for the Ferry Loyalty Card Attestation.

The Ferry Loyalty Card Attestation defined in this Rulebook is specified for SD-JWT VC-based issuance and presentation. If a future version of this Rulebook defines an ISO/IEC 18013-5-compliant mdoc representation, that version SHALL define a unique document type, namespaces, attribute identifiers, CBOR encoding rules, and illustrative mdoc examples.

## 3.2 SD-JWT VC-based encoding

The Ferry Loyalty Card Attestation SHALL be issued as an SD-JWT VC.

The Verifiable Credential Type (`vct`) for this attestation type is:

```text
urn:eu.europa.ec.eudi:ferry_loyalty_card:1
```

The credential claims defined in this section SHALL follow SD-JWT VC and HAIP conventions where applicable. Claim names are either IANA-registered JWT claims, public names, or private names specific to this attestation type.

For all claims, this Rulebook specifies whether an Attestation Provider MUST, MAY, or MUST NOT make the claim selectively disclosable.

### 3.2.1 IANA-registered and standard JWT / SD-JWT VC claims

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Reference/Notes** | **Disclosable** |
|---------------------|--------------------------|---------------------|---------------------|-----------------|
| `iss` | `iss` | string | JWT issuer identifier. | MUST NOT |
| `iat` | `iat` | integer | Issued-at timestamp. | MUST NOT |
| `nbf` | `nbf` | integer | Not-before timestamp, where used. | MUST NOT |
| `exp` | `exp` | integer | Expiration timestamp, where used. SHOULD correspond to or not exceed `credential.expiry_date` where that attribute is present. | MUST NOT |
| `jti` | `jti` | string | Unique credential instance identifier, where used. | MUST NOT |
| `cnf` | `cnf` | object | Holder binding confirmation claim, where used. | MUST NOT |
| `status` | `status` | object | Status or revocation information, where used. | MUST NOT |
| `vct` | `vct` | string | SD-JWT VC type. Value SHALL be `urn:eu.europa.ec.eudi:ferry_loyalty_card:1`. | MUST NOT |

### 3.2.2 Public or reusable claims

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Reference/Notes** | **Disclosable** |
|---------------------|--------------------------|---------------------|---------------------|-----------------|
| `customer.first_name` | `customer.first_name` | string | Customer given name. May be mapped to OIDC `given_name` in implementations that use OIDC naming conventions. | MUST |
| `customer.last_name` | `customer.last_name` | string | Customer family name. May be mapped to OIDC `family_name` in implementations that use OIDC naming conventions. | MUST |

### 3.2.3 Private claims specific to the Ferry Loyalty Card Attestation

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Notes** | **Disclosable** |
|---------------------|--------------------------|---------------------|-----------|-----------------|
| `attestation_legal_category` | `attestation_legal_category` | string | SHALL be `non-qualified-EAA`. | MUST NOT |
| `customer` | `customer` | object | Customer information object. | MUST NOT |
| `customer.nationality` | `nationality` | string | Nationality of the customer, where disclosed. | MAY |
| `customer.birth_date` | `birth_date` | string | Customer date of birth, formatted as ISO 8601 date. | MAY |
| `customer.address` | `address` | string | Customer street address. | MAY |
| `customer.city` | `city` | string | City of residence. | MAY |
| `customer.zip_code` | `zip_code` | string | Postal code. | MAY |
| `customer.phone` | `phone` | string | Fixed phone number. | MAY |
| `customer.mobile` | `mobile` | string | Mobile phone number. | MAY |
| `customer.email` | `email` | string | Customer email address. | MAY |
| `loyalty_card` | `loyalty_card` | object | Loyalty-card information object. | MUST NOT |
| `loyalty_card.id` | `id` | string | Unique loyalty-card identifier. | MUST |
| `loyalty_card.issue_date` | `issue_date` | string | Date of issuance, formatted as ISO 8601 date. | MUST |
| `organization` | `organization` | object | Issuing ferry operator information object. | MUST NOT |
| `organization.name` | `name` | string | Ferry operator name. | MUST NOT |
| `organization.id` | `id` | string | Ferry operator identifier. | MUST NOT |
| `organization.country` | `country` | string | Country of registration or operation. | MUST NOT |
| `credential` | `credential` | object | Credential metadata object defined by the attestation model. | MUST NOT |
| `credential.type` | `type` | string | Credential type. | MUST NOT |
| `credential.issuer` | `issuer` | string | Issuer of the credential. | MUST NOT |
| `credential.issuance_date` | `issuance_date` | string | Issuance date, formatted as ISO 8601 date. | MUST NOT |
| `credential.expiry_date` | `expiry_date` | string | Expiry date, where present. | MUST NOT |
| `trust_anchor` | `trust_anchor` | string | Location or identifier of the trust anchor or trust framework entry used to verify issuer authorisation, where used. | MUST NOT |
| `cryptographically_bound_to` | `cryptographically_bound_to` | string | Identifier of another attestation type to which this attestation is bound, where used. | MUST NOT |

### 3.2.4 Example JWT claim set

```json
{
  "iss": "https://issuer.example-ferry.gr",
  "iat": 1767787200,
  "nbf": 1767787200,
  "exp": 1830859200,
  "jti": "urn:uuid:ec622e9e-23f8-4c1d-9985-5c5b088caa11",
  "vct": "urn:eu.europa.ec.eudi:ferry_loyalty_card:1",
  "attestation_legal_category": "non-qualified-EAA",
  "customer": {
    "first_name": "Nikos",
    "last_name": "Triantafyllou",
    "nationality": "GR",
    "birth_date": "1985-04-12",
    "city": "Athens",
    "email": "nikos@example.com",
    "mobile": "+306901234567"
  },
  "loyalty_card": {
    "id": "LC-FAST-000123456",
    "issue_date": "2026-01-07"
  },
  "organization": {
    "name": "Fast Ferries S.A.",
    "id": "GR-FAST-FERRIES",
    "country": "GR"
  },
  "credential": {
    "type": "FerryLoyaltyCardAttestation",
    "issuer": "https://issuer.example-ferry.gr",
    "issuance_date": "2026-01-07",
    "expiry_date": "2028-01-07"
  },
  "trust_anchor": "https://trust.example.eu/ferry/operators/fast-ferries",
  "cnf": {
    "jwk": {
      "kty": "EC",
      "crv": "P-256",
      "x": "...",
      "y": "..."
    }
  },
  "status": {
    "status_list": {
      "idx": 12345,
      "uri": "https://issuer.example-ferry.gr/status/loyalty-card-status-list.jwt"
    }
  }
}
```

### 3.2.5 Example issued SD-JWT

The following is a non-normative placeholder example. A production SD-JWT SHALL be generated by the issuer using the applicable signing algorithm, disclosure construction, holder binding, and SD-JWT VC rules.

```text
<issuer-signed-sd-jwt>~<disclosure-1>~<disclosure-2>~<disclosure-n>~<holder-binding-jwt>
```

### 3.2.6 Example human-readable disclosed payload

A verifier that needs only to confirm loyalty-programme participation may receive a presentation disclosing the following claims:

```json
{
  "vct": "urn:eu.europa.ec.eudi:ferry_loyalty_card:1",
  "customer": {
    "first_name": "Nikos",
    "last_name": "Triantafyllou"
  },
  "loyalty_card": {
    "id": "LC-FAST-000123456",
    "issue_date": "2026-01-07"
  },
  "organization": {
    "name": "Fast Ferries S.A.",
    "id": "GR-FAST-FERRIES",
    "country": "GR"
  }
}
```

A verifier that needs contact details for a customer-service interaction MAY request additional selectively disclosable claims such as `customer.email` or `customer.mobile`, provided those claims are necessary for the interaction and the Holder consents to disclosure.

The issuer identity, credential type, expiry time, signature, holder binding proof, status information, and trust anchor information are not treated as selectively disclosable customer attributes and SHALL remain available to the verifier for technical validation.

## 3.3 W3C Verifiable Credentials Data Model-based encoding

This version of the Rulebook does not define a W3C Verifiable Credentials Data Model encoding for the Ferry Loyalty Card Attestation.

If a future version defines a W3C VCDM representation, that version SHALL define the credential context, type, credential subject structure, proof type, selective disclosure mechanism, and presentation requirements.

## 4 Attestation usage

The Ferry Loyalty Card Attestation is intended for verifying a customer's loyalty-programme membership and, where necessary, selected customer information.

Typical usage scenarios include:

* presentation by the customer during online ferry booking;
* presentation at a ticket office or customer-service point;
* verification of loyalty-card membership for customer benefits or discounts;
* customer identification for service personalisation;
* controlled disclosure of optional contact or residency information where required for a specific service interaction;
* repeated presentation across multiple journeys, subject to validity and revocation checks.

A Relying Party receiving the attestation SHALL verify:

* the issuer signature;
* the SD-JWT VC type (`vct`);
* the issuer authorisation to issue Ferry Loyalty Card Attestations;
* the credential validity period, where defined;
* the credential status, where a status mechanism is present;
* holder binding, where used;
* the integrity rules defined in Section 2.9;
* that the loyalty-card and organisation details match the service context.

The Relying Party SHOULD request and verify PID or another accepted identity credential when the service requires stronger customer identity matching. In such cases, the Relying Party SHOULD compare the relevant identity attributes, such as customer name, with the Ferry Loyalty Card Attestation. The Relying Party SHALL apply data minimisation and SHALL request only the attributes required for the specific loyalty or customer-service decision.

The attestation SHOULD be device-bound through holder binding where supported by the EUDI Wallet and the applicable SD-JWT VC profile. The attestation MAY be cryptographically bound to a PID or another accepted identity attestation where the relying-party process requires stronger customer identity matching. Where this binding is used, the metadata attribute `cryptographically_bound_to` SHOULD contain:

```text
urn:eudi:pid:1
```

No payment-specific transactional data is defined by this Rulebook. If the Ferry Loyalty Card Attestation is used as part of a transaction that also involves payment or discounts, payment-related requirements SHALL be defined in a separate payment attestation, payment profile, discount rulebook, or transaction-specific rulebook.

## 5 Trust anchors

A Relying Party SHALL verify that the issuer of the Ferry Loyalty Card Attestation is authorised to issue this attestation type.

For non-qualified EAA deployments, the Relying Party SHOULD obtain trust anchor information through one or more of the following mechanisms:

* a machine-readable trust list or trust registry used by the relevant ecosystem;
* an issuer metadata endpoint published by the ferry operator or authorised customer-management system;
* a trust framework entry managed by the WE BUILD ecosystem or by another authorised governance body;
* a pilot trust list used for controlled interoperability testing.

Where the metadata attribute `trust_anchor` is present, it SHOULD identify the location or registry entry from which the Relying Party can obtain the issuer trust anchor or issuer authorisation information.

The Relying Party SHALL use the trust anchor to verify that:

* the issuer signing key or certificate chains to a trusted authority or registered trust anchor;
* the issuer is authorised to issue the `urn:eu.europa.ec.eudi:ferry_loyalty_card:1` attestation type;
* the issuer metadata or trust framework entry has not expired or been revoked;
* the issuer identity in the credential is consistent with the issuer identity in the trust framework;
* the organisation information disclosed in the credential is consistent with the issuer's authorisation scope.

Wallet Units MAY also use the same trust framework information during issuance to determine whether the provider is authorised to issue this attestation type.

## 6 Revocation

The Ferry Loyalty Card Attestation is intended for repeated use and is typically longer-lived than a boarding pass.

The credential SHALL be considered invalid when:

* the `credential.expiry_date` has been reached, where present;
* the technical expiry timestamp `exp` has been reached, where present;
* the credential has been revoked or suspended by the issuer;
* the underlying loyalty-card record has been cancelled, replaced, closed, or otherwise invalidated.

Revocation SHOULD be supported for this attestation type because loyalty-card status may change before the declared expiry date.

Revocation MAY be handled by one or more of the following mechanisms:

* an attestation status list mechanism, where supported;
* an attestation revocation list mechanism, where supported;
* backend verification by the ferry operator or authorised customer-management system;
* short or medium validity periods combined with re-issuance, where appropriate for the operational model.

If a status or revocation mechanism is included in the credential, the Relying Party SHALL check the status before accepting the attestation, unless offline operating rules explicitly allow deferred status checking.

If a loyalty card is cancelled, replaced, or suspended, the issuer SHOULD revoke or suspend the attestation or ensure that backend verification detects the invalid state.

## 7 Compliance

This Rulebook is designed to align with the EUDI Wallet architectural approach for Electronic Attestations of Attributes and with the Attestation Rulebook structure defined in the ARF.

The Rulebook supports the following compliance objectives:

* it defines the attestation purpose and scope;
* it defines mandatory, optional, and conditional attributes in an encoding-independent manner;
* it defines a legal category indication through `attestation_legal_category`;
* it defines an SD-JWT VC `vct` value for the attestation type;
* it defines issuer, validity, and status metadata needed for verification;
* it defines code lists and integrity rules required for consistent interpretation;
* it defines how trust anchors can be obtained and used;
* it defines expiry and revocation expectations;
* it supports selective disclosure and data minimisation;
* it recognises the reusable nature of the loyalty-card attestation and therefore recommends status or revocation support.

This Rulebook does not define a qualified EAA or public-sector EAA profile. It also does not define ISO/IEC 18013-5 mdoc or W3C VCDM encodings in this version.

## 8 References

| **Item Reference** | **Standard name/details** |
|--------------------|---------------------------|
| [European Digital Identity Regulation] | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework |
| [HAIP] | Yasuda, K. *et al,* OpenID4VC High Assurance Interoperability Profile, OpenID Foundation |
| [IANA-JWT-Claims] | IANA JSON Web Token Claims Registry. Available: <https://www.iana.org/assignments/jwt/jwt.xhtml> |
| [ISO/IEC 18013-5] | ISO/IEC 18013-5, Personal identification --- ISO-compliant driving licence - Part 5: Mobile driving licence application |
| [OIDC] | Sakimura, N. et al., OpenID Connect Core 1.0, OpenID Foundation. Available: <https://openid.net/specs/openid-connect-core-1_0.html> |
| [RFC 2119] | RFC 2119 - Key words for use in RFCs to Indicate Requirement Levels, S. Bradner, March 1997 |
| [RFC 3339] | RFC 3339 - Date and Time on the Internet: Timestamps, G. Klyne et al., July 2002 |
| [RFC 5322] | RFC 5322 - Internet Message Format, P. Resnick, October 2008 |
| [RFC 8610] | RFC 8610 - Concise Data Definition Language (CDDL): A Notational Convention to Express Concise Binary Object Representation, H. Birkholz et al., June 2019 |
| [RFC 8943] | RFC 8943 - Concise Binary Object Representation (CBOR) Tags for Date, M. Jones et al., November 2020 |
| [RFC 8949] | RFC 8949 - Concise Data Definition Language / CBOR-related references used by the template |
| [SD-JWT VC] | SD-JWT-based Verifiable Credentials. Available: <https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/> |
| [Topic 7] | ARF Annex 2 - Topic 7 - Attestation revocation and revocation checking |
| [Topic 10] | ARF Annex 2 - Topic 10 - Issuing a PID or attestation to a Wallet Unit |
| [Topic 12] | ARF Annex 2 - Topic 12 - Attestation Rulebooks |
| [Topic 20] | ARF Annex 2 - Strong User authentication for electronic payments |
| [W3C VCDM v2.0] | Verifiable Credentials Data Model v2.0, W3C Recommendation |
