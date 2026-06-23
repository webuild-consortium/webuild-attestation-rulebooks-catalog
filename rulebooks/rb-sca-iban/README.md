(Template version: 1.1)

# WE BUILD Attestation Rulebook Template for attestations of type *SCA-IBAN*

*[Based on the WE BUILD attestation description: https://portal.webuildconsortium.eu/group/wp3-technology-standards/files?mid=6883&fid%5B0%5D=6880&fid%5B1%5D=7094]*

* Author(s):
    * Filip Hladký, Bank iD CZ, filip@bankid.cz
    * Stefan Kauhaus, Visa, kauhauss@visa.com

| Version          | Date               | Description                                      |
|------------------|--------------------|--------------------------------------------------|
| 0.1              | 2026-06-01         | Initial version based on attestation description |
| 0.9 | 2026-06-23 | Draft, ready for review/QA |

**Feedback:**

* Github, portal, email, Slack

## 1 Introduction

### 1.1 Document scope and purpose

SCA-IBAN attestation specifies Account level SUA attestation described in TS12 published by European Commission.
SCA-IBAN attestation represents User and their account, and it is used in 3rd party Payment initiation with
PISP-captured SCA.

More over SCA-IBAN may be used in the same scenarios as SCA-user, that is using EUDI Wallet for authentication
and risk operation authorization in their online banking or banking mobile application.
In this document we specify attributes, allowed formats, and processing rules for this attestation.
We also specify SD-JWT metadata for SD-JWT credential format since those metadata are critical for correct
processing of presentation requests with attached transaction data.

Attestation rulebook is aligned with ETSI TS 119 472-1.

### 1.2 Document structure

* Chapter 2, which describes the attestation attributes and metadata in an encoding-independent manner.
* Chapter 3, which specifies how the attestation attributes and metadata are encoded in case the attestation complies with [ISO/IEC 18013-5] and/or [SD-JWT VC].
* Chapter 4, which specifies attestation usage.
* Chapter 5, which defines how trust anchors for attestation verification can be obtained.
* Chapter 6, which defines attestation revocation mechanisms.
* Chapter 7, which provides compliance information.

### 1.3 Key words

This document uses the capitalised key words 'SHALL', 'SHOULD' and 'MAY' as specified in [RFC 2119], i.e.,
to indicate requirements, recommendations, and options specified in this document.

In addition, 'must' (non-capitalised) is used to indicate an external constraint, i.e., a requirement that
is not mandated by this document, but, for instance, by an external document. The word 'can' indicates a
capability, whereas other words, such as 'will', and 'is' or 'are' are intended as statements of fact.

### 1.4 Terminology

This document uses the terminology specified in Annex 1 of the ARF.

Please note that terms credential and attestation are interchangeable for purpose of this document.

## 2 Attestation attributes and metadata

### 2.1 Introduction

SCA-IBAN is a simple attestation type with only top-level attributes, some of which are selectively disclosable.
It is designed to support various use cases in Banking, most importantly SCA in Open Banking for both ASPSP and
PISP-captured scenarios. In addition, SCA-IBAN is designed to support authentication and user confirmation in
banking applications.

Attestation is based on TS12 requirements which are refined for WE BUILD.

Unlike SCA-User, SCA-IBAN does support selective disclosure.

This document defines the attribute `attestation_legal_category` which SHALL have the value `"QEAA"`,
`"PuB-EAA"`, or `"non-qualified-EAA"`.

### 2.2 Mandatory attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---|---|---|---|---|
| sub | https://www.rfc-editor.org/info/rfc7519/#section-4.1.2 | Random unique value identifying attestation subject in authentic source. Usage of UUID or prefixed UUID is recommended. | String | urn:uuid:123e4567-e89b-12d3-a456-426614174000 |
| masked_iban | | Masked IBAN where first 4 and last 4 characters are unmasked | String | CZ55***********8745 |

### 2.3 Optional attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---|---|---|---|---|
| iban | N/A | Full IBAN number | string | CZ5508000000001234567899 |
| national_bank_code | | National bank code | string | 0300 |
| bic | | BIC of bank | string | CEKOCZPP |
| scheme_identifier | | Proprietary scheme identifier for routing purposes. May be multivalued. | string or array of string | bancomat |
| display_name | | Friendly name of account for display/distinguishing purposes | string | My current account |
| currency | | ISO 4217 currency code; may be an array for multicurrency accounts | string or array of string | EUR |

### 2.4 Mandatory metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---|---|---|---|---|
| iss | https://www.rfc-editor.org/info/rfc7519/#section-4.1.1 | Issuer URL identifying the attestation provider | string (URI) | https://issuer.bank.cz |
| iat | https://www.rfc-editor.org/info/rfc7519/#section-4.1.6 | Unix timestamp designating the time when the attestation was issued | integer (Long) | 1748736000 |
| exp | https://www.rfc-editor.org/info/rfc7519/#section-4.1.4 | Unix timestamp denoting the technical validity expiration of the attestation | integer (Long) | 1751328000 |
| vct | Section 3.2.1 of [SD-JWT VC] | Denotes type of attestation; SHALL be an issuer-specific URL extending the WE BUILD base VCT | string (URI) | https://issuer.bank.cz/credentials/sca/iban/1.0 |
| cnf | https://www.rfc-editor.org/info/rfc7800 | Object containing the JWK of the holder's public key (device binding) | JSON Object | `{"jwk": {"kty":"EC","crv":"P-256",...}}` |

### 2.5 Conditional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---|---|---|---|---|
| nbf | https://www.rfc-editor.org/info/rfc7519/#section-4.1.5 | Unix timestamp denoting the first time the attestation may be used. Conditionally mandatory when `nbf` and `iat` differ. | integer (Long) | 1748822400 |
| aud | https://www.rfc-editor.org/info/rfc7519/#section-4.1.3 | Audience of this attestation; SHALL be URL(s) of RPs allowed for the 2-party model. Not evaluated when attestation is used for payment. | string or array of string | https://pisp.example.eu |
| status_list | https://www.ietf.org/archive/id/draft-ietf-oauth-status-list-17.html | Status list object for revocation checking | JSON Object | `{"idx": 0, "uri": "https://issuer.bank.cz/statuslists/1"}` |

### 2.6 Code lists

This attestation does not use any code lists.

### 2.7 Integrity rules

| **Rule ID** | **Rule statement** | **Why it exists** | **Where enforced** | **Verifier / issuer behavior on failure** |
|---|---|---|---|---|
| IR-01 | `masked_iban` SHALL be derived from the full IBAN | Ensures integrity and non-repudiation of payment | Issuer | Issuer fails to issue attestation |
| IR-02 | `national_bank_code` in the full IBAN MUST match `national_bank_code` in the attestation | Ensures integrity and non-repudiation of payment | Issuer | Issuer fails to issue attestation |

### 2.8 VCT rules

For SCA-IBAN the proposed base VCT is: `https://webuildconsortium.eu/sca/sca-iban/1.0`

This base type has claims `"extends"` and `"extends#integrity"` that point to the base VCT type
`https://webuildconsortium.eu/sca/1.0`.

Actual SCA-IBAN attestations issued by a bank carry an issuer-specific VCT URL such as
`"https://issuer.bank.cz/credentials/sca/iban/1.0"` and their metadata contains claims `"extends"`
and `"extends#integrity"` pointing to the base SCA-IBAN type
`https://webuildconsortium.eu/sca/sca-iban/1.0`.

Versioning of VCT types SHALL follow an `x.y` version model where:
- `x` is the major version — introduces breaking changes (removing claims from metadata, renaming or
  repurposing claims in transaction data).
- `y` is the minor version — introduces backward-compatible changes (adding elements, adding display claims,
  adding languages).

With this mechanism, integrity checks remain in place and the need for re-issuance of credentials across all
wallets is minimised.

# 3 Attestation encoding

## 3.1 ISO/IEC 18013-5-compliant encoding

The SCA-IBAN attestation supports the mdoc format specified in ISO/IEC 18013-5.

**Document type:** `eu.webuildconsortium.sca.iban.1`

**Encoding conventions:**

* `tstr`, `uint`, `bstr`, `bool`, and `tdate` are CDDL representation types defined in [RFC 8610].
    * `tstr` SHALL be encoded in UTF-8 and SHALL support the full Unicode range (per [RFC 8949]).
    * All `tstr` attributes SHALL have a maximum length of 150 characters.
    * `full-date` is defined as `full-date = #6.1004(tstr)` where tag 1004 is specified in [RFC 8943].
    * A `tdate` attribute SHALL contain a date-time string as specified in [RFC 3339] (per [RFC 8949] §3.4.1).
    * A `full-date` attribute SHALL contain a full-date string as specified in [RFC 3339] (per [RFC 8943]).
    * Fractions of seconds SHALL NOT be used.
    * A local offset from UTC SHALL NOT be used; the time-offset SHALL be `"Z"`.
    * The following canonical CBOR rules (per [RFC 8949] §4.2) SHALL be implemented:
        * Integers (major types 0 and 1) SHALL be as small as possible.
        * The expression of the length in a `bstr`, `tstr`, array, or map SHALL be as short as possible.
        * Indefinite-length items SHALL be made into definite-length items.

**Attribute encoding table:**

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Namespace** |
|---|---|---|---|
| sub | sub | tstr | eu.webuildconsortium.sca.iban.1 |
| masked_iban | masked_iban | tstr | eu.webuildconsortium.sca.iban.1 |
| iban | iban | tstr | eu.webuildconsortium.sca.iban.1 |
| national_bank_code | national_bank_code | tstr | eu.webuildconsortium.sca.iban.1 |
| bic | bic | tstr | eu.webuildconsortium.sca.iban.1 |
| scheme_identifier | scheme_identifier | tstr / array of tstr | eu.webuildconsortium.sca.iban.1 |
| display_name | display_name | tstr | eu.webuildconsortium.sca.iban.1 |
| currency | currency | tstr / array of tstr | eu.webuildconsortium.sca.iban.1 |
| attestation_legal_category | attestation_legal_category | tstr | eu.webuildconsortium.sca.iban.1 |

**Example mdoc (CBOR diagnostic notation):**

```cbor
{
  "version": "1.0",
  "documents": [{
    "docType": "eu.webuildconsortium.sca.iban.1",
    "issuerSigned": {
      "nameSpaces": {
        "eu.webuildconsortium.sca.iban.1": [
          { "digestID": 1, "random": h'a1b2c3d4', "elementIdentifier": "sub",
            "elementValue": "urn:uuid:123e4567-e89b-12d3-a456-426614174000" },
          { "digestID": 2, "random": h'e5f6a7b8', "elementIdentifier": "masked_iban",
            "elementValue": "CZ55***********7899" },
          { "digestID": 3, "random": h'c9d0e1f2', "elementIdentifier": "iban",
            "elementValue": "CZ5508000000001234567899" },
          { "digestID": 4, "random": h'a3b4c5d6', "elementIdentifier": "national_bank_code",
            "elementValue": "0800" },
          { "digestID": 5, "random": h'e7f8a9b0', "elementIdentifier": "bic",
            "elementValue": "GIBACZPX" },
          { "digestID": 6, "random": h'c1d2e3f4', "elementIdentifier": "currency",
            "elementValue": "CZK" },
          { "digestID": 7, "random": h'a5b6c7d8', "elementIdentifier": "attestation_legal_category",
            "elementValue": "non-qualified-EAA" }
        ]
      },
      "issuerAuth": << IssuerAuth COSE_Sign1 structure >>
    }
  }],
  "status": 0
}
```

Attribute values in the example:

| Attribute | Value                                         |
|---|-----------------------------------------------|
| sub | urn:uuid:123e4567-e89b-12d3-a456-426614174000 |
| masked_iban | CZ55***********7899                           |
| iban | CZ5508000000001234567899                      |
| national_bank_code | 0800                                          |
| bic | GIBACZPX                                      |
| currency | CZK                                           |
| attestation_legal_category | non-qualified-EAA                                           |

## 3.2 SD-JWT VC-based encoding

The SCA-IBAN attestation supports the SD-JWT VC format as specified in [SD-JWT VC], compliant with the [HAIP] profile.

**VCT (Verifiable Credential Type):** `https://issuer.bank.cz/credentials/sca/iban/1.0`
(issuer-specific; MUST extend `https://webuildconsortium.eu/sca/sca-iban/1.0` via `"extends"` and
`"extends#integrity"` claims in VCT metadata)

**IANA-registered JWT claims (not selectively disclosable):**

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Reference/Notes** | **Disclosable** |
|---|---|---|---|---|
| iss | iss | string (URI) | [RFC 7519] §4.1.1 | MUST NOT |
| iat | iat | integer (NumericDate) | [RFC 7519] §4.1.6 | MUST NOT |
| exp | exp | integer (NumericDate) | [RFC 7519] §4.1.4 | MUST NOT |
| nbf | nbf | integer (NumericDate) | [RFC 7519] §4.1.5 — conditionally mandatory when `nbf` differs from `iat` | MUST NOT |
| aud | aud | string or array | [RFC 7519] §4.1.3 — optional; not evaluated for payment use case | MUST NOT |
| sub | sub | string | [RFC 7519] §4.1.2 — UUID or prefixed UUID identifying the holder | MUST NOT |

**Private claim names and SD-JWT-specific claims:**

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Notes** | **Disclosable** |
|---|---|---|---|---|
| vct | vct | string (URI) | Denotes attestation type; SHALL be an issuer-specific URL extending the WE BUILD base VCT | MUST NOT |
| cnf | cnf | JSON Object | JWK of holder's public key (device binding); see [RFC 7800] | MUST NOT |
| status_list | status_list | JSON Object | Status list reference per draft-ietf-oauth-status-list-17; optional | MUST NOT |
| attestation_legal_category | attestation_legal_category | string | SHALL be `"QEAA"`, `"PuB-EAA"`, or `"non-qualified-EAA"` | MUST NOT |
| masked_iban | masked_iban | string | First 4 and last 4 characters unmasked; e.g. `CZ55***********8745` | MUST |
| iban | iban | string | Full IBAN number | MUST |
| national_bank_code | national_bank_code | string | National bank code; e.g. `"0800"` | MUST |
| bic | bic | string | BIC of issuing bank; e.g. `"GIBACZPX"` | MUST |
| scheme_identifier | scheme_identifier | string or array | Proprietary scheme identifier for routing; may be multivalued | MUST |
| display_name | display_name | string | Friendly account name for display purposes | MUST |
| currency | currency | string or array | ISO 4217 currency code(s); e.g. `"EUR"` or `["EUR","CZK"]` | MUST |

**Example JWT claim set (provider-side, before issuing SD-JWT):**

```json
{
  "iss": "https://issuer.bank.cz",
  "iat": 1748736000,
  "exp": 1751328000,
  "vct": "https://issuer.bank.cz/credentials/sca/iban/1.0",
  "vct#integrity": "sha256-abc123def456...",
  "extends": "https://webuildconsortium.eu/sca/sca-iban/1.0",
  "extends#integrity": "sha256-def456abc123...",
  "sub": "urn:uuid:123e4567-e89b-12d3-a456-426614174000",
  "cnf": {
    "jwk": {
      "kty": "EC",
      "crv": "P-256",
      "x": "TCAER19Zvu3OHF4j4W4vfSVoHIP1ILilDls7vCeGemc",
      "y": "ZxjiWWbZMQGHVWKVQ4hbSIirsVfuecCE6t4jT9F2HZQ"
    }
  },
  "attestation_legal_category": ""non-qualified-EAA"",
  "status_list": {
    "idx": 12,
    "uri": "https://issuer.bank.cz/statuslists/1"
  },
  "_sd_alg": "sha-256",
  "_sd": [
    "X9yH4uRPd0rFgCnMq7LwKp3jZoStViEa2bDNcOIkT8s",
    "mBpQ1vYeKrDnCjHaWgFxZ5tSoUilNcT3LdR7yEhAP94",
    "kL8nJpFaOcQrBdVwXgY2eIhCmT5ZsU1RoPN6yDK7WHv",
    "eA3hKpNdRqWmXvZcY7tJfOiSgBL1Uo2nCu6DrsP8FT4",
    "vT5cY2RdXoNpKfHaQ9gBmJwLe6PiUs3Cn1rODkA7ZI8",
    "qZ4bW7MdPlJnFhR3aOeKvGcT9XoA6sU2Ct1YiDB5Np8",
    "dR6xK3WoMvCfQpHnL2bY5ZjA9Ts4PuN1gOe7iBSUDa0"
  ]
}
```

**Example issued SD-JWT (compact serialization):**

```
eyJhbGciOiJFUzI1NiIsInR5cCI6InZjK3NkLWp3dCIsImtpZCI6Imlzc3Vlci1rZXktMSJ9
.
eyJpc3MiOiJodHRwczovL2lzc3Vlci5iYW5rLmN6IiwiaWF0IjoxNzQ4NzM2MDAwLCJleHAiOj
E3NTEzMjgwMDAsInZjdCI6Imh0dHBzOi8vaXNzdWVyLmJhbmsuY3ovY3JlZGVudGlhbHMvc2Nh
L2liYW4vMS4wIiwidmN0I2ludGVncml0eSI6InNoYTI1Ni1hYmMxMjMuLi4iLCJzdWIiOiJ1cm4
6dXVpZDoxMjNlNDU2Ny1lODliLTEyZDMtYTQ1Ni00MjY2MTQxNzQwMDAiLCJjbmYiOnsiandri
jp7Imt0eSI6IkVDIiwiY3J2IjoiUC0yNTYiLCJ4IjoiVENBRVIxOVp2dTNPSEY0ajRXNHZmU1Zv
SElQMUlMaWxEbHM3dkNlR2VtYyIsInkiOiJaeGppV1diWk1RR0hWV0tWUTRoYlNJaXJzVmZ1
ZWNDRTZ0NGpUOUYySFpRIn19fSwiYXR0ZXN0YXRpb25fbGVnYWxfY2F0ZWdvcnkiOiJRRUFBIiw
iX3NkX2FsZyI6InNoYS0yNTYiLCJfc2QiOlsiLi4uIl19
.
<issuer-signature>
~WyJyYW5kb20xIiwibWFza2VkX2liYW4iLCJDWjU1KioqKioqKioqKio4NzQ1Il0
~WyJyYW5kb20yIiwiaWJhbiIsIkNaNTUwODAwMDAwMDAwMTIzNDU2Nzg5OSJd
~WyJyYW5kb20zIiwibmF0aW9uYWxfYmFua19jb2RlIiwiMDgwMCJd
~WyJyYW5kb200IiwiYmljIiwiR0lCQUNaUFgifQ
~WyJyYW5kb201IiwiY3VycmVuY3kiLCJDWksiXQ
```

**Human-readable SD-JWT payload and disclosure descriptions:**

Non-selectively-disclosable claims (always present in JWT body):

| Claim | Value |
|---|---|
| `iss` | `https://issuer.bank.cz` |
| `iat` | `1748736000` (2025-05-31T00:00:00Z) |
| `exp` | `1751328000` (2025-06-30T00:00:00Z) |
| `vct` | `https://issuer.bank.cz/credentials/sca/iban/1.0` |
| `sub` | `urn:uuid:123e4567-e89b-12d3-a456-426614174000` |
| `cnf` | `{jwk: {kty: "EC", crv: "P-256", ...}}` |
| `attestation_legal_category` | `"non-qualified-EAA"` |
| `status_list` | `{idx: 12, uri: "https://issuer.bank.cz/statuslists/1"}` |

Selectively-disclosable claims (each disclosure encoded as `[<salt>, <claim_name>, <claim_value>]`
base64url per [SD-JWT VC] §5):

| Disclosure # | Claim | Value |
|---|---|---|
| ~0 | `masked_iban` | `CZ55***********7899` |
| ~1 | `iban` | `CZ5508000000001234567899` |
| ~2 | `national_bank_code` | `0800` |
| ~3 | `bic` | `GIBACZPX` |
| ~4 | `currency` | `CZK` |

## 4 Attestation usage

SCA-IBAN is primarily designed for the 3-party model where the issuer and verifier are in different organisations.
The verifier (Relying Party) is typically a PISP or Merchant acting as a PISP, which captures SCA via the Wallet
and forwards it to the ASPSP with the payment.

**Primary use cases:**

1. **PISP-captured SCA for payment initiation (primary):** The Wallet presents the SCA-IBAN attestation with
   transaction data to a PISP, which forwards it to the ASPSP. Processing of transaction data follows [TS12].
2. **ASPSP-captured SCA (2-party model):** The issuing bank may allow SCA-IBAN to be used directly in its own
   mobile/web banking application, subject to VC metadata permission. Same rules as for SCA-User apply.
3. **User authentication and operation authorization** in the issuing bank's banking applications.

SCA-IBAN is exclusively used in presentation scenarios where transaction data is present in the presentation request.

**Relying Party obligations:**

* The Relying Party SHALL verify the issuer signature and the `cnf` key binding before accepting the attestation.
* The Relying Party SHALL check the `status_list` claim if present to verify that the attestation has not been revoked.
* The Relying Party SHALL verify that presented transaction data is bound to the attestation as specified in [Topic 20] and [TS12].
* The Relying Party SHOULD verify that the `aud` claim, if present, includes the RP's own identifier.
* Verification of a PID alongside this attestation is not required.

**Presentation requirements:**

* SCA-IBAN SHALL be presented online using OID4VP.
* Transaction data MUST be present in all payment-initiation presentation requests (see [Topic 20]).
* In the SD-JWT encoding, the Wallet SHOULD respect VC metadata published by the Issuer at the VCT metadata endpoint.

**Device binding:**

* This attestation SHALL be device-bound (ARB_34 in [Topic 12]).
* The device binding key SHALL be attested at AVA_VAN.4 or higher.
* The attestation MAY be cryptographically bound to the holder's PID. If so, `cryptographically_bound_to`
  SHALL carry the value `"eu.europa.ec.eudi.pid.1"` (ISO/IEC 18013-5) or `"urn:eudi:pid:1"` (SD-JWT VC).

### 4.1 Issuance lifecycle

Issuer of SCA-IBAN is — for the purpose of WE BUILD — a Bank acting as ASPSP in PSD2.

Before issuance, the Bank SHALL check Wallet eligibility:

* Wallet provider is trusted for this purpose via a trust list.
* Wallet Unit is in operational state with valid WUA/WIA and PID.
* Wallet Unit has an eligible WSCD available at AVA_VAN.4 or higher.
* The user identified by this Wallet Unit is the same user authenticated via 2FA into the banking environment.

Eligibility checks MAY be performed by:

* Requesting WUA and WIA and validating the signing certificate and key attestations.
* Requesting a PID and matching its attributes with the authenticated user's data.

When issuing the attestation, the Issuer SHALL:

* Use a sender-constrained token (DPoP) to ensure that only the requesting Wallet may receive the issued credential.
* Provide means to refresh the attestation (i.e., refresh tokens).
* Ensure that the attestation is device-bound with sufficient secure storage (AVA_VAN.4 or higher).
* Include or publish information about allowed verifiers; the `aud` claim MAY be used for this purpose.

Deferred issuance is not recommended — the user is in the loop and banks should be able to process the issuance
request online.

After receiving the attestation, the Wallet SHOULD notify the Issuer of successful acceptance.

### 4.2 Presentation lifecycle

SCA-IBAN SHOULD be presented when the presentation request comes from a Verifier acting as a PISP in the PSD2
scheme with payment transaction data as described in [TS12].

## 5 Trust anchors

Trust anchor mechanisms depend on the legal categorisation of the attestation:

* **QEAA:** The Relying Party obtains the Issuer's trust anchor from the applicable EU Trusted List and uses it
  to verify the attestation or signing certificate chain. Intermediate certificates are permitted.
* **PuB-EAA:** The Relying Party first verifies the Issuer's signature using the PuB-EAA Provider certificate
  issued by a QTSP, then verifies that certificate against the QTSP Trusted List.
* **non-qualified EAA:** The Issuer SHALL publish a machine-readable trust anchor at a URL referenced in the
  `vct` metadata document. Relying Parties SHALL use this URL to retrieve the trust anchor and verify issuer
  authorization.

In all cases, the Issuer MAY use intermediate signing certificates. The trust anchor SHALL be the root certificate
on the applicable Trusted List.

## 6 Revocation

SCA-IBAN attestations are intended to be **short-lived** (validity period ≤ 24 hours for active payment use)
combined with a token refresh mechanism at the Issuer.

For attestations with a validity period exceeding 24 hours, the Issuer SHALL implement revocation using the
**Attestation Status List** mechanism referenced in the `status_list` claim, in accordance with the Technical
Specification to be specified by the Commission (currently tracked as
[draft-ietf-oauth-status-list-17](https://www.ietf.org/archive/id/draft-ietf-oauth-status-list-17.html)).

Relying Parties SHALL check the `status_list` reference when present and reject attestations whose status
indicates revocation or suspension.

## 7 Compliance

This Rulebook is aligned with the following specifications:

* **[European Digital Identity Regulation]** (Regulation (EU) 2024/1183) — Attestation attributes and metadata
  satisfy the requirements of Annex V (QEAA) and Annex VII (PuB-EAA) as applicable.
* **ARF [Topic 12]** — All ARB_ requirements referenced in the template have been addressed:
  ARB_01b, ARB_02, ARB_05, ARB_06, ARB_06a, ARB_06b, ARB_07, ARB_09, ARB_10, ARB_11–ARB_21,
  ARB_26–ARB_31, ARB_34.
* **ETSI TS 119 472-1** — The Rulebook structure and attestation lifecycle follow this standard.
* **[TS12]** — Attribute definitions and transaction data processing align with TS12 published by the
  European Commission.
* **[HAIP]** — The SD-JWT VC encoding complies with the OpenID4VC High Assurance Interoperability Profile.
* **[ISO/IEC 18013-5]** — The mdoc encoding follows the ISO mobile document standard.

## 8 References

| **Item Reference** | **Standard name/details** |
|---|---|
| [European Digital Identity Regulation] | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework |
| [HAIP] | Yasuda, K. *et al,* OpenID4VC High Assurance Interoperability Profile, OpenId Foundation, Version draft-03 |
| [IANA-JWT-Claims] | IANA JSON Web Token Claims Registry. Available: <https://www.iana.org/assignments/jwt/jwt.xhtml> |
| [ISO/IEC 18013-5] | ISO/IEC 18013-5, Personal identification — ISO-compliant driving licence - Part 5: Mobile driving licence (mDL) application, First edition, 2021-09 |
| [OIDC] | Sakimura, N. et al., "OpenID Connect Core 1.0", OpenID Foundation. Available: <https://openid.net/specs/openid-connect-core-1_0.html> |
| [RFC 2119] | RFC 2119 - Key words for use in RFCs to Indicate Requirement Levels, S. Bradner, March 1997 |
| [RFC 3339] | RFC 3339 - Date and Time on the Internet: Timestamps, G. Klyne et al., July 2002 |
| [RFC 7519] | RFC 7519 - JSON Web Token (JWT), M. Jones et al., May 2015 |
| [RFC 7800] | RFC 7800 - Proof-of-Possession Key Semantics for JSON Web Tokens (JWTs), M. Jones et al., April 2016 |
| [RFC 8610] | RFC 8610 - Concise Data Definition Language (CDDL), H. Birkholz et al., June 2019 |
| [RFC 8943] | RFC 8943 - Concise Binary Object Representation (CBOR) Tags for Date, M. Jones et al., November 2020 |
| [RFC 8949] | RFC 8949 - Concise Binary Object Representation (CBOR), C. Bormann et al., December 2020 |
| [SD-JWT VC] | SD-JWT-based Verifiable Credentials (SD-JWT VC). Available: <https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/>, version draft-ietf-oauth-sd-jwt-vc-09 |
| [Topic 7] | ARF Annex 2 - Topic 7 - Attestation revocation and revocation checking Available: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a237-topic-7-attestation-revocation-and-revocation-checking> |
| [Topic 10] | ARF Annex 2 - Topic 10 - Issuing a PID or attestation to a Wallet Unit: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a2310-topic-10-issuing-a-pid-or-attestation-to-a-wallet-unit> |
| [Topic 12] | ARF Annex 2 - Topic 12 - Attestation Rulebooks, Available: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a2312-topic-12-attestation-rulebooks> |
| [Topic 20] | ARF Annex 2 - Strong User authentication for electronic payments, Available: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a2320-topic-20-strong-user-authentication-for-electronic-payments> |
| [TS12] | TS12 - Electronic Payments SCA Implementation with Wallet, European Commission. Available: <https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts12-electronic-payments-SCA-implementation-with-wallet.md> |
