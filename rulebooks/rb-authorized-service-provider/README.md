| Version | Date | Description |
|---------|------------|------------|
| 0.1 | 2026-06-01 | Initial draft of the Authorized Service Provider attestation rulebook, derived from the WE BUILD Attestation Rulebook Template v1.1 and aligned with the SC5 eInvoicing scenario specification (Scenarios 2 and 3). |
| 0.6 | 2026-07-14 | Review draft for SC5 rulebook review meeting. Aligned with the WE BUILD attestation rulebooks catalog conventions: vct pattern `eu.we-build:<slug>:1`, legal category value `EAA`, EBWOID-anchored EAA trust model per rb-base, Chapter 4 issuer/RP obligations referencing the Base Verification rulebook, and Token Status List metadata (`status_list_credential`/`status_list_index`). |
| 0.7 | 2026-07-15 | Added issue tracker and cleaned up author list layout |

# WE BUILD Attestation Rulebook for attestations of type *Authorized Service Provider*

*This Rulebook is derived from the WE BUILD v1.1 Attestation Rulebook Template (itself derived from the
EUDI attestation rulebook template) and keeps the template's chapter structure. It specifies the
Authorized Service Provider attestation used in WE BUILD Use Case SC5 (eInvoicing), Scenario 2 (Service
Provider authorization) and Scenario 3 (SP authorization verifiable by a Tax Administration).*

* Author(s):
    * Rune Kjørlaug, Emning AS / OpenPeppol (SC5 co-lead)

**Feedback:**

* [WE BUILD SC5 issue tracker](https://github.com/webuild-consortium/SC5/)

## 1 Introduction

### 1.1 Document scope and purpose

This Rulebook defines the **Authorized Service Provider attestation**, an Electronic Attestation of
Attributes (EAA) used within WE BUILD Use Case SC5 (eInvoicing).

In plain language, the Authorized Service Provider attestation lets a **company** declare, in a
machine-verifiable way, that a named **Service Provider** (Access Point) is authorised to send and/or
receive invoices on the company's behalf. The attestation is issued by the company to its Service
Provider and is presented so that a counterpart Access Point — or, in Scenario 3, a **Tax
Administration** — can verify that the Access Point handling a given invoice is genuinely mandated by
the company it acts for. This closes a trust gap in the 4-corner model: it makes the company→provider
mandate explicit and verifiable rather than assumed from network registration alone.

* **Real-world fact expressed:** that a named company authorises a named Service Provider (Access
  Point) to act for it, for a defined set of operations (send / receive / tax reporting) and validity
  period.
* **Issuers:** the authorising company — a Supplier (**C1**) or a Buyer (**C4**) — acting as a legal
  person through its European Business Wallet (EBW).
* **Holders:** the Service Provider / Access Point (**C2** or **C3**), holding the attestation in its
  wallet.
* **Relying parties:** the counterpart Access Point (**C3** or **C2**); and, in Scenario 3, a **Tax
  Administration** verifying the provider's mandate for tax-reporting purposes.
* **Use case / user journey:** SC5 Scenario 2 (Service Provider authorization), Scenario 3 (mandate
  verifiable by a Tax Administration), and Scenario 5 (Peppol enhancements).
* **Source material:** the SC5 eInvoicing scenario specification (SC5_Introduction.md,
  SC5_Scenario2_ServiceProviderAuthorization.md, SC5_Scenario3_SPAuthorizationTaxAdmin.md). Actor
  terminology (C1–C4, EBW, EBWOID, Access Point) is kept aligned with that specification and with the
  Peppol Interoperability Framework.

### 1.2 Document structure

* Chapter 2 describes the attestation attributes and metadata in an encoding-independent manner.
* Chapter 3 specifies the encoding. The SD-JWT VC encoding (Section 3.2) is normative. ISO/IEC 18013-5
  (mdoc) and W3C VCDM encodings are not specified, for the reasons given in Sections 3.1 and 3.3.
* Chapter 4 specifies attestation usage.
* Chapter 5 defines how trust anchors for verification are obtained.
* Chapter 6 defines the revocation mechanism.
* Chapter 7 provides compliance information.
* Chapter 8 lists references.

### 1.3 Key words

This document uses the capitalised key words 'SHALL', 'SHOULD' and 'MAY' as specified in [RFC 2119],
i.e., to indicate requirements, recommendations and options specified in this document.

In addition, 'must' (non-capitalised) is used to indicate an external constraint, i.e., a requirement
that is not mandated by this document but, for instance, by an external document. The word 'can'
indicates a capability, whereas other words, such as 'will', and 'is' or 'are' are intended as
statements of fact.

### 1.4 Terminology

This document uses the terminology specified in Annex 1 of the ARF, supplemented by Peppol terminology
(C1–C4, Access Point, SMP/SML, Peppol participant identifier) and WE BUILD terminology (EBW, EBWOID,
WE BUILD LoTL, WE BUILD Trusted List) as defined in the SC5 specification and the WP4 Blueprint.

## 2 Attestation attributes and metadata

### Chapter overview and requirements

This chapter defines all attributes and metadata that an Authorized Service Provider attestation may
contain, in an encoding-independent manner (ARB_06 in [Topic 12]). Each attribute is marked mandatory,
optional, or conditional in its section (ARB_09).

**Applicable legal category.** Per the SC5 working assumptions, the Authorized Service Provider
attestation is implemented as a **non-qualified EAA** for the WE BUILD pilot; QEAA escalation is a
post-pilot decision. Where the SC5 specification refers to a "WE BUILD QEAA", this denotes a
technically interoperable, ITB-tested attestation within the pilot trust framework, not an
eIDAS-qualified EAA. The requirements for non-qualified EAA in [Topic 12] therefore apply:

* An attribute indicating that the attestation is an EAA SHOULD be included (ARB_12). See Section 2.1.
* One or more attributes or metadata representing identification data of the issuer SHALL be included
  (ARB_15).
* One or more attributes representing the subject SHOULD be included (ARB_17).
* Attributes or metadata representing the validity period SHOULD be defined (ARB_19).
* Attributes or metadata representing the location of the trust anchor SHOULD be defined (ARB_21); see
  Chapter 5.

### 2.1 Introduction

The Authorized Service Provider attestation expresses a mandate: a company authorises a Service
Provider to act for it in eInvoicing. The design models two parties — the **authorizing company** (C1
or C4, also the technical issuer) and the **authorized service provider** (C2 or C3, the
holder/subject) — together with the set of authorised operations and the validity period.

Per ARB_12 of [Topic 12], this document defines the attribute **`attestation_legal_category`**, which
for this attestation type SHALL have the value **`EAA`**.

**Logical model (informative):**

```
AuthorizedServiceProviderAttestation
├── attestation_legal_category : "EAA"
├── authorizing_company        (the company, C1 or C4 — also the issuer)
│   ├── legal_name
│   ├── legal_id               (EUID / LPID, from the company's EBWOID)
│   └── peppol_id              (Peppol participant identifier)
├── authorized_service_provider (the Access Point, C2 or C3 — the holder/subject)
│   ├── legal_name
│   ├── legal_id               (EUID / LPID)
│   └── peppol_ap_id           (Peppol Access Point identifier)
├── authorization_scope        (array of code list values, see 2.8)
├── authorization_valid_from   (date)
└── authorization_valid_until  (date; see also the exp metadata claim)
```

This model refines the flat claim list in the SC5 specification (issuer_id, issuer_name, subject_id,
subject_name, authorization_date, expiry_date, scope, company_peppol_id, sp_peppol_ap_id) into two
grouped party objects, while preserving the same information content. Note that the authorising party
may be either the Supplier (C1, authorising its sending AP C2) or the Buyer (C4, authorising its
receiving AP C3); the model is symmetric.

Subsections 2.2–2.7 define the attributes and metadata. Section 2.8 documents the scope code list and
Section 2.9 the integrity rules.

### 2.2 Mandatory attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------|--------------|--------------|--------------|
| `authorizing_company.legal_name` | N/A (WE BUILD SC5 domestic namespace) | Registered legal name of the authorising company. | string | `Green Flowers B.V.` |
| `authorizing_company.legal_id` | EUID (Regulation (EU) 2017/1132) | Unique legal-person identifier of the company, sourced from its EBWOID. | string | `NL853746281B01` |
| `authorizing_company.peppol_id` | Peppol Participant Identifier | Peppol participant identifier of the company (scheme::value). | string | `0106:853746281` |
| `authorized_service_provider.legal_name` | N/A (WE BUILD SC5 domestic namespace) | Registered legal name of the Service Provider (the holder). | string | `Banqup N.V.` |
| `authorized_service_provider.legal_id` | EUID (Regulation (EU) 2017/1132) | Unique legal-person identifier of the Service Provider. | string | `BE0890123456` |
| `authorized_service_provider.peppol_ap_id` | Peppol AP Identifier (CN of AP certificate) | Identifier of the Service Provider's Peppol Access Point. | string | `POP000123` |
| `authorization_scope` | N/A (see code list 2.8) | One or more authorised operations. | array of string (enum) | `["peppol:send"]` |
| `authorization_valid_from` | N/A | Date from which the authorization is valid. | full-date (RFC 3339) | `2026-01-01` |

### 2.3 Optional attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------|--------------|--------------|--------------|
| `authorization_valid_until` | N/A | Date until which the authorization is valid (business validity, distinct from the technical `exp` metadata claim). | full-date (RFC 3339) | `2026-12-31` |
| `authorization_reference` | N/A | Company-internal reference for the service agreement underlying the mandate. | string | `SLA-2026-AP-007` |

### 2.4 Conditional attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------|--------------|--------------|--------------|
| `tax_reporting_member_state` | ISO 3166-1 alpha-2 | Member State for which the provider is authorised to perform tax reporting. **Conditional:** SHALL be present if and only if `authorization_scope` contains `vida:tax_report`. | string | `NL` |

### 2.5 Mandatory metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------|--------------|--------------|--------------|
| `attestation_legal_category` | Defined in Section 2.1 | Indicates the legal category of the attestation. | string | `EAA` |
| `vct` | [SD-JWT VC] | Verifiable Credential Type identifier (see Section 3.2). | string | `eu.we-build:authorizedserviceprovider:1` |
| `iss` | [IANA-JWT-Claims] | Issuer identifier (the authorising company's issuing system / EBW). | string (URI) | `https://wallet.greenflowers.example/issuer` |
| `iat` | [IANA-JWT-Claims] | Issuance timestamp. | NumericDate | `1767225600` |
| `exp` | [IANA-JWT-Claims] | Technical expiry timestamp of the attestation. | NumericDate | `1798761600` |
| `status` | [SD-JWT VC] / [Token Status List] | Reference to the Token Status List entry for revocation (see Chapter 6). | object | *(see Chapter 6)* |
| `cnf` | [SD-JWT VC] | Holder key-binding confirmation (proof of possession by the Service Provider's wallet). | object | *(JWK / key reference)* |

### 2.6 Optional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------|--------------|--------------|--------------|
| `cryptographically_bound_to` | ARB_28 / [Topic 12] | vct of another attestation on the same Wallet Unit to which this attestation is cryptographically bound (the Service Provider's EBWOID). RECOMMENDED — see Chapter 4. | string | `uri:eu.ebw.oid.1` |

### 2.7 Conditional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------|--------------|--------------|--------------|
| N/A | N/A | No conditional metadata is defined in v0.1. | N/A | N/A |

### 2.8 Code lists

| **Field name** | **Allowed values** | **Meaning** | **Source / vocabulary** | **Notes / extensibility** |
|----------------|--------------------|-------------|--------------------------|---------------------------|
| `authorization_scope` | `peppol:send` | The provider is authorised to send (transmit) invoices as the company's sending Access Point (C2). | WE BUILD SC5 domestic vocabulary | Used by C1 authorising C2. |
| `authorization_scope` | `peppol:receive` | The provider is authorised to receive invoices as the company's receiving Access Point (C3). | WE BUILD SC5 domestic vocabulary | Used by C4 authorising C3. |
| `authorization_scope` | `vida:tax_report` | The provider is authorised to perform tax-reporting / digital reporting on the company's behalf (Scenario 3). | WE BUILD SC5 domestic vocabulary; aligned with ViDA Digital Reporting Requirements | Requires `tax_reporting_member_state` (Section 2.4). Additional values SHOULD only be introduced if defined consistently across issuers and verifiers and registered in the WE BUILD Attestation Rulebooks catalog. |

### 2.9 Integrity rules

| **Rule ID** | **Rule statement** | **Why it exists** | **Where enforced** | **Verifier / issuer behavior on failure** |
|-------------|--------------------|-------------------|--------------------|-------------------------------------------|
| `IR-ASP-01` | `authorization_valid_from` SHALL NOT be later than `authorization_valid_until` (when present), and both SHALL fall within the `iat`–`exp` window. | Prevents inconsistent or unusable validity periods. | Issuer business rules; verifier business validation. | Issuer SHALL reject; verifier SHALL treat the attestation as invalid. |
| `IR-ASP-02` | If `authorization_scope` contains `vida:tax_report`, then `tax_reporting_member_state` SHALL be present; otherwise it SHALL be absent. | Ensures tax-reporting mandates carry the jurisdiction needed by a Tax Administration relying party (Scenario 3), and that the field is not set spuriously. | Issuer; verifier (Tax Administration) business validation. | Verifier SHALL treat the attestation as invalid for tax-reporting reliance. |
| `IR-ASP-03` | `authorization_scope` SHALL contain at least one value, and SHALL NOT contain both `peppol:send` and `peppol:receive` unless the same provider genuinely acts as both C2 and C3 for the company. | Keeps the mandate explicit and prevents over-broad authorizations. | Issuer business rules. | Issuer SHALL reject an empty or contradictory scope. |
| `IR-ASP-04` | At verification time, the `authorized_service_provider.peppol_ap_id` SHALL match the Access Point actually transmitting/receiving the invoice, and `authorizing_company.peppol_id` SHALL match the corresponding party on the invoice. | Binds the mandate to the specific invoice flow, preventing reuse for an unrelated company/provider pair. | Verifier (counterpart AP, or Tax Administration). | Verifier SHALL reject. |

## 3 Attestation encoding

### 3.1 ISO/IEC 18013-5-compliant encoding

The Authorized Service Provider attestation is presented in automated, online, system-to-system flows
(see Chapter 4). There is no proximity / offline presentation use case (ARB_02). An ISO/IEC 18013-5
(mdoc) encoding is therefore **not specified** in this version.

### 3.2 SD-JWT VC-based encoding

This attestation type SHALL be issued in the [SD-JWT VC]-compliant format and SHALL comply with the
'SD-JWT VCs' profile specified in [HAIP] (ARB_01b).

**Verifiable Credential Type (`vct`):** `eu.we-build:authorizedserviceprovider:1`

*(Proposed value; subject to registration in the WE BUILD Attestation Rulebooks catalog by the WP4
semantics group, ARB_05.)*

For all claims, the table below specifies whether an Attestation Provider MUST, MAY, or MUST NOT make
the claim selectively disclosable (ARB_30). A Type Metadata Document SHOULD be defined for this vct per
Chapter 6 of [SD-JWT VC] (ARB_31).

A JSON Schema for this encoding is published in the catalog at
`data-schemas/sd-jwt/authorized-service-provider-sd-jwt.json`, with sample data at
`data-schemas/sd-jwt/sample-data/authorized-service-provider-sd-jwt-sample.json`.

**Registered / standard claims:**

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Reference/Notes** | **Disclosable** |
|---------------------|--------------------------|---------------------|---------------------|-----------------|
| `iss` | iss | string | [IANA-JWT-Claims] | MUST NOT |
| `iat` | iat | number | [IANA-JWT-Claims] | MUST NOT |
| `exp` | exp | number | [IANA-JWT-Claims] | MUST NOT |
| `vct` | vct | string | [SD-JWT VC] | MUST NOT |
| `status` | status | object | [Token Status List]; Chapter 6 | MUST NOT |
| `cnf` | cnf | object | [SD-JWT VC]; holder binding | MUST NOT |

**Private claims specific to this attestation type:**

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Notes** | **Disclosable** |
|---------------------|--------------------------|---------------------|-----------|-----------------|
| `attestation_legal_category` | attestation_legal_category | string | Section 2.1 | MUST NOT |
| `authorizing_company` | authorizing_company | object | C1 or C4 | MAY |
| `authorized_service_provider` | authorized_service_provider | object | C2 or C3 | MAY |
| `authorization_scope` | authorization_scope | array | Code list 2.8 | MAY |
| `authorization_valid_from` | authorization_valid_from | string (full-date) | | MAY |
| `authorization_valid_until` | authorization_valid_until | string (full-date) | Optional | MAY |
| `tax_reporting_member_state` | tax_reporting_member_state | string | Conditional (2.4) | MAY |
| `authorization_reference` | authorization_reference | string | Optional | MUST — issuer SHALL make selectively disclosable so the provider can withhold the internal reference |
| `cryptographically_bound_to` | cryptographically_bound_to | string | Section 2.6; Chapter 4 | MUST NOT |

**Illustrative JWT claim set (informative, synthetic data):**

```json
{
  "vct": "eu.we-build:authorizedserviceprovider:1",
  "iss": "https://wallet.greenflowers.example/issuer",
  "iat": 1767225600,
  "exp": 1798761600,
  "attestation_legal_category": "EAA",
  "status": { "status_list": { "idx": 87, "uri": "https://status.webuild.example/sc5/authorized_sp" } },
  "cnf": { "jwk": { "kty": "EC", "crv": "P-256", "x": "...", "y": "..." } },
  "authorizing_company": {
    "legal_name": "Green Flowers B.V.",
    "legal_id": "NL853746281B01",
    "peppol_id": "0106:853746281"
  },
  "authorized_service_provider": {
    "legal_name": "Banqup N.V.",
    "legal_id": "BE0890123456",
    "peppol_ap_id": "POP000123"
  },
  "authorization_scope": ["peppol:send", "vida:tax_report"],
  "tax_reporting_member_state": "NL",
  "authorization_valid_from": "2026-01-01",
  "authorization_valid_until": "2026-12-31"
}
```

[RULEBOOK AUTHOR TO PROVIDE AN EXAMPLE OF THE ISSUED SD-JWT IN base64 ENCODING ONCE A REFERENCE
ISSUER IS AVAILABLE]

[RULEBOOK AUTHOR TO PROVIDE A HUMAN-READABLE VERSION OF THE SD-JWT PAYLOAD WITH THE DISCLOSURES,
ONCE THE SELECTIVE-DISCLOSURE STRUCTURE IS FINALISED WITH WP4]

### 3.3 W3C Verifiable Credentials Data Model-based encoding

A W3C VCDM encoding is **not specified** for this attestation type. SD-JWT VC (Section 3.2) is the
single normative encoding for SC5, consistent with the WE BUILD Conformance Specifications.

## 4 Attestation usage

**Primary use cases.** SC5 Scenario 2 (Service Provider authorization), Scenario 3 (mandate verifiable
by a Tax Administration), and Scenario 5 (Peppol enhancements). The Service Provider (C2 or C3) holds
the attestation and presents it — in a machine-to-machine OpenID4VP flow — so that the counterpart
Access Point can confirm the provider is mandated by the company it acts for. In Scenario 3, a Tax
Administration verifies the same attestation (specifically the `vida:tax_report` scope and
`tax_reporting_member_state`) to confirm the provider's authority to report on the company's behalf.

**PID verification (ARB_27).** A relying party **does not** request or verify a PID. Both the holder
(Service Provider) and the authorising party are legal persons; identity assurance is provided by the
EBWOID binding (see Chapter 5), not by a natural-person PID.

**Presentation requirements.** Presentation is online and system-to-system via OpenID4VP, using DCQL
queries as profiled by the WE BUILD Conformance Specification cs-02. No offline / proximity
presentation is supported. Where the relying party is itself an EBW-based system, the Mutual
Identification & Consent Handshake defined in [rb-base — Handshake] SHOULD be applied before
presentation.

**Device binding (ARB_34).** An attestation of this type SHOULD be device-bound to the holder's Wallet
Unit (the Service Provider's wallet), evidenced by the `cnf` claim and verified through key binding at
presentation (base verification step 4.2.8).

**Binding to another attestation (ARB_28).** An attestation of this type SHOULD be cryptographically
bound to the Service Provider's organisational identity attestation (EBWOID) on the same Wallet Unit.
Where present, the binding metadata identifier SHALL be `cryptographically_bound_to`, its value SHALL be
a string containing the bound attestation's vct, and that value SHALL be `uri:eu.ebw.oid.1` (the EBWOID
vct defined in [rb-ebwoid]).

**Transactional data ([Topic 20]).** No payment-authentication transactional data is defined for this
attestation type. The attestation authorises a *mandate*, not an individual payment.

### 4.1 Issuance process

The issuer is the authorising company (C1 or C4), a legal person self-issuing this EAA through its EBW
on the basis of a service agreement with the Service Provider. Issuance uses OpenID4VCI as profiled by
the WE BUILD Conformance Specification cs-01.

The Issuer SHALL implement the base issuer obligations defined in the Base Verification specification:
<https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-base/verifier-base-verification.md#41-issuer-obligations>

In particular, the issuer SHALL include the holder-generated public key (`cnf`) in the payload, SHALL
include its own EBWOID-anchored certificate material in the attestation header (see Chapter 5), and
SHALL populate the `status` metadata (see Chapter 6) in every issued attestation.

### 4.2 Relying Party obligations

When receiving and processing an Authorized Service Provider attestation, the Relying Party (the
counterpart AP, or a Tax Administration in Scenario 3) SHALL perform the following verification
obligations.

#### 4.2.1 – 4.2.8 Base verification process

The Relying Party SHALL perform the base attestation verification process for EAAs as defined in the
Base Verification specification:
<https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-base/verifier-base-verification.md#42-relying-party-obligations>

This covers verification of attestation authenticity and issuer identity via the EBWOID chain
(4.2.2–4.2.4), validity periods (4.2.5), revocation status (4.2.6), wallet integrity via the WUA
(4.2.7), and holder key binding (4.2.8).

#### 4.2.9 Validate attestation-specific integrity rules

In addition to the base verification, the Relying Party SHALL apply the integrity rules IR-ASP-01 to
IR-ASP-04 defined in Section 2.9, and SHALL verify that the requested operation is within
`authorization_scope`. A Tax Administration relying party (Scenario 3) SHALL additionally confirm that
`vida:tax_report` is present and that `tax_reporting_member_state` matches its jurisdiction.

## 5 Trust anchors

This chapter specifies how a Relying Party establishes trust in the issuer of an Authorized Service
Provider attestation. The corresponding verification procedures are steps 4.2.2–4.2.4 of the Base
Verification specification.

The Authorized Service Provider attestation is an **EAA self-issued by a legal entity** (the
authorising company). Authorising companies are not, and cannot practically be, individually registered
on a Trusted List. Trust is therefore established through a cryptographic chain anchored in the
issuer's **EBWOID**, following the common WE BUILD EAA trust model:

* The issuer's EBWOID SHALL be included in the header of every issued Authorized Service Provider
  attestation. During EBWOID issuance, the EBWOID provider verifies that the public key contained in
  the EBWOID is owned by the EBW owner.
* The Relying Party SHALL verify the EBWOID in accordance with [rb-ebwoid] and the Base Verification
  specification. The EBWOID provider's trust anchor is obtained via the WE BUILD trust list
  infrastructure (TLOL) operated under WP4.
* Upon successful verification, the Relying Party obtains: assurance that the EBWOID was issued by an
  authorised provider (and is not self-issued); the verified identity of the issuer, including its
  legal name and EUID; and the public key authorised to verify the attestation signature.
* The Relying Party SHALL then confirm that the verified issuer identity (EUID) matches
  `authorizing_company.legal_id` in the attestation payload.

Authorization of the issuer *as a mandating company* is subsequently determined in accordance with the
Relying Party's internal policies (e.g. the counterpart AP confirming the company is the Peppol
participant on the invoice; a Tax Administration confirming the company is a registered taxpayer in its
jurisdiction), optionally supported by domain-specific trust list services.

## 6 Revocation

An Authorized Service Provider attestation SHALL remain valid only while the underlying mandate is in
effect. The attestation is **revocable** (it is not a short-lived ≤24h attestation; mandates persist
for the duration of a service agreement).

### 6.1 Revocation mechanism

* **Token Status List:** the issuer SHALL maintain an active IETF Token Status List ([Token Status
  List]), aligned with the Attestation Status List mechanism specified by the EU Commission and
  mandated by the WE BUILD ADR on Attestation Revocation.
* **Credential metadata:** the `status` metadata SHALL be populated in every issued attestation with:
  * `status_list_credential` (string, URI) — the URI of the Status List Credential containing the
    status bitstring;
  * `status_list_index` (integer, ≥ 0) — the zero-based index into the status list bitstring for this
    attestation;
  * `status_purpose` (string) — SHALL be `revocation`.
* **Authorized authority:** only the issuing company (the self-issuing legal entity) may modify the
  status list entry.

### 6.2 Revocation triggers and business rules

* **Issuer trigger (obligation):** the authorising company SHALL revoke the attestation without undue
  delay when it changes Service Provider, when the service agreement ends, when the authorised scope
  changes (issuing a replacement attestation), or when the provider's identity data becomes inaccurate.
* **Relying Party action:** a revoked or suspended attestation SHALL be treated as invalid; the
  counterpart AP SHALL reject exchanges relying on it, and a Tax Administration SHALL NOT accept
  reporting mandated by it. The business interpretation of a revocation (e.g. handling of exchanges
  already in flight) is determined by the Relying Party's internal policies.

## 7 Compliance

This Rulebook follows the structure mandated by [Topic 12] of the ARF and the WE BUILD Attestation
Rulebook Template v1.1. The Authorized Service Provider attestation is a **non-qualified EAA** in the
sense of the [European Digital Identity Regulation], implemented within the WE BUILD pilot trust
framework rather than the eIDAS production ecosystem (WP4 Blueprint D4.1 §1.2.1). It uses the SD-JWT VC
format profiled by [HAIP], OpenID4VCI for issuance and OpenID4VP for presentation per the WE BUILD
Conformance Specifications (cs-01, cs-02), and the IETF Token Status List for revocation per the WE
BUILD ADR on Attestation Revocation. The `vida:tax_report` scope and `tax_reporting_member_state`
attribute are designed to align with ViDA Digital Reporting Requirements for Scenario 3; their precise
mapping to a production digital-reporting obligation is out of scope for this pilot version. Escalation
to an eIDAS-qualified EAA (QEAA) is a post-pilot decision.

## 8 References

| **Item Reference** | **Standard name/details** |
|--------------------|---------------------------|
| [European Digital Identity Regulation] | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework |
| [HAIP] | OpenID4VC High Assurance Interoperability Profile, OpenID Foundation, draft-03 |
| [IANA-JWT-Claims] | IANA JSON Web Token Claims Registry. <https://www.iana.org/assignments/jwt/jwt.xhtml> |
| [RFC 2119] | Key words for use in RFCs to Indicate Requirement Levels, S. Bradner, March 1997 |
| [RFC 3339] | Date and Time on the Internet: Timestamps, G. Klyne et al., July 2002 |
| [SD-JWT VC] | SD-JWT-based Verifiable Credentials. <https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/> |
| [Token Status List] | Token Status List, IETF OAuth WG. <https://datatracker.ietf.org/doc/draft-ietf-oauth-status-list/> |
| [OpenID4VCI] | OpenID for Verifiable Credential Issuance, OpenID Foundation |
| [OpenID4VP] | OpenID for Verifiable Presentations, OpenID Foundation |
| [Topic 7] | ARF Annex 2 — Topic 7 — Attestation revocation and revocation checking |
| [Topic 10] | ARF Annex 2 — Topic 10 — Issuing a PID or attestation to a Wallet Unit |
| [Topic 12] | ARF Annex 2 — Topic 12 — Attestation Rulebooks |
| [Topic 20] | ARF Annex 2 — Topic 20 — Strong User authentication for electronic payments |
| [ViDA] | Council Directive amending Directive 2006/112/EC as regards VAT rules for the digital age (Digital Reporting Requirements) |
| [Peppol BIS Billing 3.0] | OpenPeppol Business Interoperability Specification, Billing 3.0 |
| [EN 16931] | European standard on the semantic data model of the core elements of an electronic invoice |
| [EWC RB001] | EWC LPID Rulebook |
| [EWC RB002] | EWC EUCC Rulebook |
| [WP4 Blueprint] | WE BUILD Deliverable D4.1 (trust infrastructure blueprint) |
| [WBCS] | WE BUILD Conformance Specifications, cs-01 (issuance) and cs-02 (presentation) |
| [WE BUILD ADR — Revocation] | WE BUILD Architecture Decision Record on Attestation Revocation |
| [rb-base — Base Verification] | WE BUILD Rulebook for common verification steps for all attestations. <https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-base/verifier-base-verification.md> |
| [rb-base — Handshake] | WE BUILD Rulebook for Mutual Identification & Consent Handshake. <https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-base/holder-authorization-handshake.md> |
| [rb-ebwoid] | WE BUILD EBWOID Rulebook. <https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-ebwoid/README.md> |
