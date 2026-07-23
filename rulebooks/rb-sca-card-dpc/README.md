(Template version: 1.1)

# WE BUILD Attestation Rulebook for attestations of type *SCA-Card (DPC)*

*[Based on the WE BUILD attestation description: https://portal.webuildconsortium.eu/group/wp3-technology-standards/files?mid=7109&fid%5B0%5D=6880&fid%5B1%5D=7094]*

*[The data model of this attestation is derived from the EMVCo specification "EMV Digital Payment Credential (DPC) - Card Credential & Display Meta-Data"]*

* Author(s):
    * Tomasz Błachowicz, Mastercard

| Version | Date | Description |
|---------|------------|------------|
| 0.1 | 2026-07-13 | Initial version derived from EMV DPC Card Credential & Display Meta-Data |

**Feedback:**

* Github, portal, email, Slack

## 1 Introduction

### 1.1 Document scope and purpose

SCA-Card (DPC) specifies the card-level SUA attestation described in [TS12] published by the European
Commission. The attestation represents a digitised payment card as a verifiable credential, called a
Digital Payment Credential (DPC), and is used for payment authentication with multi-factor
authentication in remote commerce. It supports both authentication of a card already known to the
merchant (for example a token on file or a recognised returning consumer) and credential discovery
with card selection in the Wallet, which enables the authenticated guest checkout scenario.

The attestation follows the data minimisation principle: the signed payload identifies the payment
instrument through opaque identifiers only and never contains the PAN or fragments of it. All
presentation-oriented card data, such as the last four digits, card art, and branding, travels in a
separate unsigned display meta-data object defined in this document.

In this document we specify attributes, allowed formats, and processing rules for this attestation.
The data model is derived from the EMVCo Digital Payment Credential specification [EMV-DPC] and adapted
to the WE BUILD SCA attestation family. Co-badged cards, which [EMV-DPC] supports through a per-badge
credential model, are out of scope for WE BUILD; see Section 2.1.

### 1.2 Document structure

* Chapter 2, which describes the attestation attributes and metadata in an encoding-independent manner.
* Chapter 3, which specifies how the attestation attributes and metadata are encoded in case the attestation
  complies with [SD-JWT VC].
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

Please note that terms credential and attestation are interchangeable for the purpose of this document.

## 2 Attestation attributes and metadata

### 2.1 Introduction

SCA-Card (DPC) is a simple attestation type with only top-level attributes, all of which are selectively
disclosable. The attestation payload is intentionally minimal: it identifies the credential instance, the
payment network, and optionally the digitised card through an opaque token reference. It never contains
the PAN, the card BIN, or the last four digits; those are display-only data carried in the unsigned
display meta-data object described in Section 2.9.

Unlike the other attestations of the WE BUILD SCA family, SCA-Card (DPC) does not define a `sub` claim.
The EMVCo source model has no subject identifier; the `credential_id` attribute identifies the credential
instance and plays that role.

Co-badged cards, cards that participate in more than one payment network, are out of scope for the
WE BUILD profile of this attestation: WE BUILD supports SCA-Card (DPC) for single-network cards only,
and each attestation identifies exactly one payment network. The EMVCo source specification [EMV-DPC]
defines a per-badge credential model for co-badged cards; that model MAY be adopted in a future version
of this Rulebook.

This document defines the attribute `attestation_legal_category` which SHALL have the value
`"non-qualified-EAA"`.

### 2.2 Mandatory attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---|---|---|---|---|
| credential_id | N/A | Unique identifier of this specific credential instance. The value is issuer-specific and must uniquely identify the credential within the issuer's namespace. It SHOULD be generated using a collision-resistant mechanism (e.g., UUID). The `credential_id` identifies the credential artefact itself rather than the underlying payment card. | string | urn:uuid:9f2b7a2e-3b74-4a0d-9b1a-0e6a91f5d2c8 |
| network | N/A | Payment network or scheme associated with the credential, as a single string value. Each attestation is issued for exactly one network. Co-badged cards are out of scope; see Section 2.1. | string | mastercard |

### 2.3 Optional attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---|---|---|---|---|
| card_id | N/A | Opaque identifier of the digitised payment instrument for which this attestation is issued, specific to this attestation's network, typically the token or card reference provisioned by that network's token service provider. The value is issuer-specific and MUST NOT reveal sensitive card data such as the full PAN. | string | mc-8c3f2d1a |

### 2.4 Mandatory metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---|---|---|---|---|
| iss | https://www.rfc-editor.org/info/rfc7519/#section-4.1.1 | Issuer URL identifying the attestation provider | string (URI) | https://issuer.bank.example |
| iat | https://www.rfc-editor.org/info/rfc7519/#section-4.1.6 | Unix timestamp designating the time when the attestation was issued | integer (Long) | 1772195095 |
| exp | https://www.rfc-editor.org/info/rfc7519/#section-4.1.4 | Unix timestamp denoting the technical validity expiration of the attestation | integer (Long) | 1835267095 |
| vct | Section 3.2.1 of [SD-JWT VC] | Denotes type of attestation; SHALL be an issuer-specific URL extending the WE BUILD base VCT | string (URI) | https://issuer.bank.example/credentials/sca/card-dpc/1.0 |
| cnf | https://www.rfc-editor.org/info/rfc7800 | Object containing the JWK of the holder's public key (device binding). Each credential instance SHALL have its own unique holder binding key pair; see Section 2.7. | JSON Object | `{"jwk": {"kty":"EC","crv":"P-256",...}}` |

### 2.5 Conditional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---|---|---|---|---|
| nbf | https://www.rfc-editor.org/info/rfc7519/#section-4.1.5 | Unix timestamp denoting the first time the attestation may be used. Conditionally mandatory when `nbf` and `iat` differ. | integer (Long) | 1772195095 |

### 2.6 Code lists

| **Field name** | **Allowed values** | **Meaning** | **Source / vocabulary** | **Notes / extensibility** |
|----------------|--------------------|-------------|--------------------------|---------------------------|
| `network` | Open list of lower-case payment network identifiers, e.g. `mastercard`, `maestro`, `visa` | Identifies the payment network that can route a transaction for this attestation | [EMV-DPC] logical credential model | New values MAY be introduced when they are used consistently across issuer, Wallet, and verifier implementations. The value SHALL equal the `network_branding.network` value in the accompanying display meta-data (see Section 2.7, IR-04). |

### 2.7 Integrity rules

| **Rule ID** | **Rule statement** | **Why it exists** | **Where enforced** | **Verifier / issuer behavior on failure** |
|---|---|---|---|---|
| IR-01 | `card_id` MUST NOT reveal sensitive card data such as the full PAN or fragments of it | Data minimisation; prevents exposure of card data to verifiers and intermediaries | Issuer | Issuer SHALL NOT issue the attestation; a Verifier detecting PAN data SHOULD reject the presentation and report the issuer |
| IR-02 | `network` SHALL be single-valued; the attestation SHALL identify exactly one payment network | Gives DCQL native value matching and makes the network-to-token association unambiguous | Issuer, schema validation | Issuer fails to issue the attestation |
| IR-03 | Each credential instance SHALL have its own unique holder binding key pair; keys SHALL NOT be shared across credential instances | Prevents a verifier from correlating attestations of the same holder or card through a shared public key | Issuer, Wallet | Wallet SHALL reject a credential whose binding key it has seen in another credential |
| IR-04 | `network_branding.network` in the display meta-data SHALL equal the `network` claim of the attestation it accompanies | Keeps the rendered network branding consistent with the signed claim | Issuer, Wallet | Wallet SHALL treat the display meta-data as invalid and fall back to the `network` claim value |

### 2.8 VCT rules

For SCA-Card (DPC) the proposed base VCT is: `https://webuildconsortium.eu/sca/sca-card-dpc/1.0`

This base type has claims `"extends"` and `"extends#integrity"` that point to the base SCA VCT type
`https://webuildconsortium.eu/sca/1.0`.

Actual SCA-Card (DPC) attestations issued by a credential issuer carry an issuer-specific VCT URL such
as `https://issuer.bank.example/credentials/sca/card-dpc/1.0` and their metadata contains claims
`"extends"` and `"extends#integrity"` pointing to the base SCA-Card (DPC) type
`https://webuildconsortium.eu/sca/sca-card-dpc/1.0`.

Versioning of VCT types SHALL follow an `x.y` version model where:
- `x` is the major version - introduces breaking changes (removing claims from metadata, renaming or
  repurposing claims in transaction data).
- `y` is the minor version - introduces backward-compatible changes (adding elements, adding display claims,
  adding languages).

With this mechanism, integrity checks remain in place and the need for re-issuance of credentials across all
wallets is minimised.

The attribute set and semantics of this attestation type are derived from the EMVCo Digital Payment
Credential type `com.emvco.dpc.card` defined in [EMV-DPC]. Within the WE BUILD pilot, the WE BUILD VCT
hierarchy above is used as the type identifier; the EMVCo identifier is referenced for semantic alignment
only.

### 2.9 Display meta-data

Each SCA-Card (DPC) attestation is delivered together with an unsigned display meta-data object that
defines how the Wallet presents the card to the User, both in the card representation in the Wallet and
on the payment sheet. Providing this data with the attestation enables consistent, issuer-controlled
rendering without reliance on out-of-band branding repositories. The object carries the following fields
within its top-level `card` object:

| **Field** | **Meaning** | **Display intent** |
|---|---|---|
| `type` | Card product type: code `CREDIT`, `DEBIT`, or `PREPAID`, with an optional human-readable label | Product-type caption; the label MAY be localised |
| `last_four` | Last four digits of the PAN | User recognition of the card in Wallet and checkout interfaces; display-only, never a verifiable claim |
| `alias` | User-facing card name (e.g. "Platinum Credit Card") | Primary card title; MAY be localised |
| `card_art` | Card artwork images with `DEFAULT`, `LIGHT`, and `DARK` theme variants | Card visual in the Wallet and on the payment sheet |
| `issuer` | Issuer branding (name, logo) with optional country, website, and support contacts | Issuer identity and customer-support entry points |
| `co_branding` | Optional co-brand partner branding (e.g. airline or retailer) | Secondary brand rendered alongside the card |
| `network_branding` | Name and logo of this attestation's network; exactly one per attestation | Network logo on the card visual |

Image resources referenced by `image_url` attributes MAY be provided either as externally hosted HTTPS
URLs or as embedded Data URLs as defined in [RFC 2397]. Image arrays SHALL contain at least one image;
when only a single image is provided, its `theme` value SHALL be `DEFAULT`, indicating that the image is
suitable for any UI theme.

The display meta-data object:

* is NOT part of the signed attestation and carries no issuer signature;
* is transported in the `display` array of the OpenID4VCI credential response, enabling the Wallet to
  render the issued attestation with full visual fidelity, and MAY additionally be provided in the
  credential offer, enabling the User to recognise the card and give informed consent before issuance;
* is never presented to a Verifier. This is guaranteed structurally: the object is not a claim in the
  signed credential and display meta-data is not part of an OpenID4VP presentation.

Wallet behaviour for rendering this data is specified in Chapter 4 (Wallet display handling).

The table above defines field semantics only; the authoritative definition of the object's structure
(data types, patterns, enumerations, and required fields) is the machine-readable JSON Schema published
in this catalogue at
[`data-schemas/display/sca-card-dpc-display-meta.schema.json`](../../data-schemas/display/sca-card-dpc-display-meta.schema.json),
with a sample at
[`data-schemas/display/sample-data/sca-card-dpc-display-meta-sample.json`](../../data-schemas/display/sample-data/sca-card-dpc-display-meta-sample.json).

# 3 Attestation encoding

## 3.1 ISO/IEC 18013-5-compliant encoding

This encoding is not supported for this attestation type. SCA-Card (DPC) SHALL be issued exclusively in
the SD-JWT VC format specified in Section 3.2. Presentation when the Wallet Unit and the Relying Party
are in proximity without using the internet is not required for this attestation type (see ARB_02 in
[Topic 12]): all supported use cases are online remote-commerce flows.

## 3.2 SD-JWT VC-based encoding

The SCA-Card (DPC) attestation supports the SD-JWT VC format as specified in [SD-JWT VC], compliant with
the [HAIP] profile.

**VCT (Verifiable Credential Type):** `https://issuer.bank.example/credentials/sca/card-dpc/1.0`
(issuer-specific; MUST extend `https://webuildconsortium.eu/sca/sca-card-dpc/1.0` via `"extends"` and
`"extends#integrity"` claims in VCT metadata)

The machine-readable JSON Schema of the resolved claim set is published in this catalogue at
[`data-schemas/sd-jwt/sca-card-dpc-sd-jwt.json`](../../data-schemas/sd-jwt/sca-card-dpc-sd-jwt.json),
with a sample at
[`data-schemas/sd-jwt/sample-data/sca-card-dpc-sd-jwt-sample.json`](../../data-schemas/sd-jwt/sample-data/sca-card-dpc-sd-jwt-sample.json).

**IANA-registered JWT claims (not selectively disclosable):**

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Reference/Notes** | **Disclosable** |
|---|---|---|---|---|
| iss | iss | string (URI) | [RFC 7519] §4.1.1 | MUST NOT |
| iat | iat | integer (NumericDate) | [RFC 7519] §4.1.6 | MUST NOT |
| exp | exp | integer (NumericDate) | [RFC 7519] §4.1.4 | MUST NOT |
| nbf | nbf | integer (NumericDate) | [RFC 7519] §4.1.5 - conditionally mandatory when `nbf` differs from `iat` | MUST NOT |

**Private claim names and SD-JWT-specific claims:**

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Notes** | **Disclosable** |
|---|---|---|---|---|
| vct | vct | string (URI) | Denotes attestation type; SHALL be an issuer-specific URL extending the WE BUILD base VCT | MUST NOT |
| cnf | cnf | JSON Object | JWK of holder's public key (device binding); see [RFC 7800]. Unique per credential instance (IR-03). | MUST NOT |
| attestation_legal_category | attestation_legal_category | string | SHALL be `"non-qualified-EAA"` | MUST NOT |
| credential_id | credential_id | string | Unique identifier of the credential instance | MUST |
| network | network | string | Single payment network identifier | MUST |
| card_id | card_id | string | Opaque per-network token reference; MUST NOT reveal PAN data | MUST |

**Example JWT claim set (provider-side, before issuing SD-JWT):**

```json
{
  "vct": "https://issuer.bank.example/credentials/sca/card-dpc/1.0",
  "vct#integrity": "sha256-Cp5VgPMqzU7cphGIL0aRy54scWhTiBFB1FJYDLyO94w=",
  "extends": "https://webuildconsortium.eu/sca/sca-card-dpc/1.0",
  "extends#integrity": "sha256-gV1X+E7n79QEHEt9AI0VY3ZbNefHhZloJhpaHoYFqKM=",
  "iss": "https://issuer.bank.example",
  "iat": 1772195095,
  "exp": 1835267095,
  "cnf": {
    "jwk": {
      "kty": "EC",
      "crv": "P-256",
      "x": "f83OJ3D2xF4wK2Yp6tK2vNhbbX6YsJhBKt3vnDnNQfQ",
      "y": "x_FEzRu9w4J6v7P3cu6UytzszbmWzxubUANe0yoyl9A"
    }
  },
  "attestation_legal_category": "non-qualified-EAA",
  "_sd_alg": "sha-256",
  "_sd": [
    "X9yH4uRPd0rFgCnMq7LwKp3jZoStViEa2bDNcOIkT8s",
    "mBpQ1vYeKrDnCjHaWgFxZ5tSoUilNcT3LdR7yEhAP94",
    "kL8nJpFaOcQrBdVwXgY2eIhCmT5ZsU1RoPN6yDK7WHv"
  ]
}
```

**Example issued SD-JWT (compact serialization, abbreviated):**

```
eyJhbGciOiJFUzI1NiIsInR5cCI6ImRjK3NkLWp3dCIsImtpZCI6Imlzc3Vlci1rZXktMSJ9
.
eyJpc3MiOiJodHRwczovL2lzc3Vlci5iYW5rLmV4YW1wbGUiLCJpYXQiOjE3NzIxOTUwOTUs
ImV4cCI6MTgzNTI2NzA5NSwidmN0IjoiaHR0cHM6Ly9pc3N1ZXIuYmFuay5leGFtcGxlL2Ny
ZWRlbnRpYWxzL3NjYS9jYXJkLWRwYy8xLjAiLCJjbmYiOnsiandrIjp7Imt0eSI6IkVDIn19
LCJhdHRlc3RhdGlvbl9sZWdhbF9jYXRlZ29yeSI6Im5vbi1xdWFsaWZpZWQtRUFBIiwiX3Nk
X2FsZyI6InNoYS0yNTYiLCJfc2QiOlsiLi4uIl19
.
<issuer-signature>
~WyI8c2FsdC0xPiIsImNyZWRlbnRpYWxfaWQiLCJ1cm46dXVpZDo5ZjJiN2EyZS0uLi4iXQ
~WyI8c2FsdC0yPiIsIm5ldHdvcmsiLCJtYXN0ZXJjYXJkIl0
~WyI8c2FsdC0zPiIsImNhcmRfaWQiLCJtYy04YzNmMmQxYSJd
```

**Human-readable SD-JWT payload and disclosure descriptions:**

Non-selectively-disclosable claims (always present in the JWT body):

| Claim | Value |
|---|---|
| `iss` | `https://issuer.bank.example` |
| `iat` | `1772195095` (2026-02-27T12:24:55Z) |
| `exp` | `1835267095` (2028-02-27T12:24:55Z) |
| `vct` | `https://issuer.bank.example/credentials/sca/card-dpc/1.0` |
| `cnf` | `{jwk: {kty: "EC", crv: "P-256", ...}}` |
| `attestation_legal_category` | `non-qualified-EAA` |

Selectively-disclosable claims (each disclosure encoded as `[<salt>, <claim_name>, <claim_value>]`
base64url per [SD-JWT VC]):

| Disclosure # | Claim | Value |
|---|---|---|
| ~0 | `credential_id` | `urn:uuid:9f2b7a2e-3b74-4a0d-9b1a-0e6a91f5d2c8` |
| ~1 | `network` | `mastercard` |
| ~2 | `card_id` | `mc-8c3f2d1a` |

## 3.3 W3C Verifiable Credentials Data Model-based encoding

This encoding is not supported for this attestation type. The attestation SHALL be issued exclusively
in the SD-JWT VC format.

## 4 Attestation usage

SCA-Card (DPC) is designed for the 3-party model in remote commerce: the credential issuer and the
verifier are in different organisations. The verifying side is typically a merchant, PSP, or a payment
system component acting on their behalf. Integration of DPC presentations into payment system rails,
for example EMVCo Secure Remote Commerce (Click to Pay), is defined by the respective payment system
specifications and is out of scope of this Rulebook.

**Primary use cases:**

1. **Payment authentication with a known credential:** The verifier already holds a reference to the
   digitised card (e.g. token on file or recognised returning consumer) and requests a presentation of
   the specific attestation, typically by `credential_id`.
2. **Authenticated guest checkout with credential discovery:** The verifier does not know the card. The
   presentation request filters by supported networks, the User selects a card in the Wallet, and the
   disclosed `card_id` gives the verifier the network token reference needed to route the transaction.

Both use cases provide multi-factor authentication through device biometrics or PIN plus the
device-bound key, supporting PSD2 Strong Customer Authentication. SCA-Card (DPC) is exclusively used in
presentation scenarios where transaction data is present in the presentation request.

**Relying Party obligations:**

* The Relying Party SHALL verify the issuer signature and the `cnf` key binding (KB-JWT) before
  accepting the attestation.
* The Relying Party SHALL verify that presented transaction data is bound to the attestation as
  specified in [Topic 20] and [TS12] ("sign what you see": the Wallet incorporates the payment details
  shown to the User into the data signed by the device-bound key).
* Verification of a PID alongside this attestation is not required.

**Presentation requirements:**

* SCA-Card (DPC) SHALL be presented online using OID4VP; presentation MAY be invoked through the W3C
  Digital Credentials API.
* Transaction data MUST be present in all presentation requests (see [Topic 20]).
* The Wallet SHOULD respect VC metadata published by the Issuer at the VCT metadata endpoint.

**Wallet requirements (normative):**

* The Wallet SHALL present each matched attestation as a single card on the payment sheet.
* The Wallet SHALL return exactly one attestation, the selected card's, as the response to the
  credential query, with the key binding mechanism binding it to the transaction data.

**Wallet display handling (normative):**

* The Wallet SHOULD render the card in the Wallet UI and on the payment sheet using the display
  meta-data delivered at issuance (Section 2.9), without relying on out-of-band branding repositories.
* For themed images (`card_art` and branding logos), the Wallet SHOULD select the image variant matching
  the active UI theme and SHALL fall back to the `DEFAULT` variant when no theme-specific image is
  provided.
* The Wallet SHALL support image resources provided as externally hosted HTTPS URLs as well as embedded
  Data URLs per [RFC 2397].
* When retrieving externally hosted images, the Wallet SHOULD take measures to prevent unintended
  disclosure of User information, for example by avoiding transmission of identifying headers or by
  using privacy-preserving fetch mechanisms.

**Device binding:**

* This attestation SHALL be device-bound (ARB_34 in [Topic 12]).
* The device binding key SHALL be attested at AVA_VAN.4 or higher.
* Each credential instance SHALL have its own unique binding key pair (IR-03).
* The attestation MAY be cryptographically bound to the holder's PID. If so, `cryptographically_bound_to`
  SHALL carry the value `"urn:eudi:pid:1"`.
  Note that such binding weakens the unlinkability property provided by per-instance keys and SHOULD be
  avoided unless required by the deployment.

### 4.1 Issuance lifecycle

Issuer of SCA-Card (DPC) is - for the purpose of WE BUILD - the card issuer or an entity issuing
credentials on its behalf (the Credential Issuer in [EMV-DPC] terms).

Before issuance, the Issuer SHALL check Wallet eligibility:

* Wallet provider is trusted for this purpose via a trust list.
* Wallet Unit is in operational state with valid WUA/WIA and PID.
* Wallet Unit has an eligible WSCD available at AVA_VAN.4 or higher.
* The user identified by this Wallet Unit is the same user authenticated into the issuer's environment.

When issuing the attestation, the Issuer SHALL:

* Use a sender-constrained token (DPoP) to ensure that only the requesting Wallet may receive the issued
  credential.
* Ensure that the attestation is device-bound with sufficient secure storage (AVA_VAN.4 or higher).
* Deliver the display meta-data object (Section 2.9) in the `display` array of the credential response,
  and MAY additionally include it in the credential offer to support user recognition before issuance.

After receiving the attestation, the Wallet SHOULD notify the Issuer of successful acceptance.

### 4.2 Presentation lifecycle

SCA-Card (DPC) SHOULD be presented when the presentation request comes from a verifier participating in
a payment transaction, with payment transaction data attached as described in [TS12].

The following DCQL examples illustrate the two selection patterns in an OpenID4VP request. A Wallet
SHALL treat an attestation as matching a requested VCT value when its `vct` claim or any type in its
`extends` chain equals that value.

**Query by Credential ID** (known-card scenario): requests a specific attestation and disclosure of
`credential_id` and `network`.

```json
{
  "credentials": [
    {
      "id": "dpc",
      "format": "dc+sd-jwt",
      "meta": {
        "vct_values": ["https://webuildconsortium.eu/sca/sca-card-dpc/1.0"]
      },
      "claims": [
        { "path": ["credential_id"], "values": ["urn:uuid:9f2b7a2e-3b74-4a0d-9b1a-0e6a91f5d2c8"] },
        { "path": ["network"] }
      ]
    }
  ]
}
```

**Query by supported network** (guest checkout): filters on the `network` claim. Because every
attestation carries a single-valued `network` claim, this uses standard DCQL `values` semantics. The
Wallet shows each matching card once; after the User selects a card, the Wallet presents exactly one
attestation and discloses only the requested attributes.

```json
{
  "credentials": [
    {
      "id": "dpc",
      "format": "dc+sd-jwt",
      "meta": {
        "vct_values": ["https://webuildconsortium.eu/sca/sca-card-dpc/1.0"]
      },
      "claims": [
        { "path": ["network"], "values": ["mastercard", "visa"] },
        { "path": ["credential_id"] },
        { "path": ["card_id"] }
      ]
    }
  ]
}
```

## 5 Trust anchors

SCA-Card (DPC) is a non-qualified EAA. The trust anchor mechanism for this attestation type is **TBD**
and will be defined in a future version of this Rulebook. This includes the mechanism through which
Relying Parties obtain the trust anchor used to verify the attestation and the mechanism through which
they establish that an Issuer is authorized to issue this attestation type, for example a
sector-specific issuer accreditation scheme such as an EMVCo-operated issuer root programme discussed
in [EMV-DPC]-related work.

## 6 Revocation

SCA-Card (DPC) attestations are **long-lived** by definition: the attestation is provisioned once and
remains valid for an extended period, typically aligned with the lifecycle of the underlying digitised
card. The validity period is expressed through the `exp` metadata.

The revocation mechanism for this attestation type is **TBD** and will be defined in a future version
of this Rulebook.

## 7 Compliance

This Rulebook is aligned with the following specifications:

* **[European Digital Identity Regulation]** (Regulation (EU) 2024/1183) - This is a non-qualified EAA.
  Attributes and metadata satisfy the requirements of Annex V points b), c), and e) as applicable
  (ARB_15, ARB_17, ARB_19).
* **ARF [Topic 12]** - All ARB_ requirements applicable to non-qualified EAA have been addressed:
  ARB_01b, ARB_02, ARB_05, ARB_06, ARB_06a, ARB_06b, ARB_07, ARB_09, ARB_10, ARB_12, ARB_15, ARB_17,
  ARB_19, ARB_21, ARB_26, ARB_27, ARB_30, ARB_31, ARB_34.
* **ETSI TS 119 472-1** - The Rulebook structure and attestation lifecycle follow this standard.
* **[TS12]** - Attribute definitions and transaction data processing align with TS12 published by the
  European Commission.
* **[EMV-DPC]** - The logical credential model, disclosable attribute set, and display meta-data model
  are derived from the EMVCo Digital Payment Credential specification, adapted to WE BUILD
  type identifiers and metadata claims as described in Section 2.8. The source specification's co-badged
  card handling is out of scope for WE BUILD (see Section 2.1).
* **[HAIP]** - The SD-JWT VC encoding complies with the OpenID4VC High Assurance Interoperability
  Profile.

## 8 References

| **Item Reference** | **Standard name/details** |
|---|---|
| [EMV-DPC] | EMV Digital Payment Credential Specification - Schema Framework, EMVCo, and its DPC Card Credential & Display Meta-Data schema. Draft under review; no public URL at the time of writing. |
| [European Digital Identity Regulation] | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework |
| [HAIP] | Yasuda, K. *et al,* OpenID4VC High Assurance Interoperability Profile, OpenId Foundation, Version draft-03 |
| [IANA-JWT-Claims] | IANA JSON Web Token Claims Registry. Available: <https://www.iana.org/assignments/jwt/jwt.xhtml> |
| [OpenID4VCI] | Lodderstedt, T. *et al,* OpenID for Verifiable Credential Issuance, OpenID Foundation. Available: <https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html> |
| [OpenID4VP] | Terbu, O. *et al,* OpenID for Verifiable Presentations, OpenID Foundation (includes the Digital Credentials Query Language, DCQL). Available: <https://openid.net/specs/openid-4-verifiable-presentations-1_0.html> |
| [RFC 2119] | RFC 2119 - Key words for use in RFCs to Indicate Requirement Levels, S. Bradner, March 1997 |
| [RFC 2397] | RFC 2397 - The "data" URL scheme, L. Masinter, August 1998 |
| [RFC 7519] | RFC 7519 - JSON Web Token (JWT), M. Jones et al., May 2015 |
| [RFC 7800] | RFC 7800 - Proof-of-Possession Key Semantics for JSON Web Tokens (JWTs), M. Jones et al., April 2016 |
| [SD-JWT VC] | SD-JWT-based Verifiable Credentials (SD-JWT VC). Available: <https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/> |
| [Topic 7] | ARF Annex 2 - Topic 7 - Attestation revocation and revocation checking Available: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a237-topic-7-attestation-revocation-and-revocation-checking> |
| [Topic 10] | ARF Annex 2 - Topic 10 - Issuing a PID or attestation to a Wallet Unit: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a2310-topic-10-issuing-a-pid-or-attestation-to-a-wallet-unit> |
| [Topic 12] | ARF Annex 2 - Topic 12 - Attestation Rulebooks, Available: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a2312-topic-12-attestation-rulebooks> |
| [Topic 20] | ARF Annex 2 - Strong User authentication for electronic payments, Available: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a2320-topic-20-strong-user-authentication-for-electronic-payments> |
| [TS12] | TS12 - Electronic Payments SCA Implementation with Wallet, European Commission. Available: <https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts12-electronic-payments-SCA-implementation-with-wallet.md> |
| [W3C Digital Credentials API] | W3C Digital Credentials, W3C Working Draft. Available: <https://www.w3.org/TR/digital-credentials/> |
