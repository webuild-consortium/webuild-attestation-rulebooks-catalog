| Version | Date | Description |
|---------|------------|------------|
| 0.1 | 2026-07-01 | Initial draft of the eInvoice attestation rulebook, derived from the WE BUILD Attestation Rulebook Template v1.1 and the eInvoice Attestation description (v0.5 final draft), aligned with the SC5 eInvoicing scenario specification (Scenario 4 — Direct eInvoicing between Business Wallets). |
| 0.6 | 2026-07-14 | Review draft for SC5 rulebook review meeting. Aligned with the WE BUILD attestation rulebooks catalog conventions: vct pattern `eu.we-build:<slug>:1`, legal category value `EAA`, EBWOID-anchored EAA trust model per rb-base, Chapter 4 issuer/RP obligations referencing the Base Verification rulebook, and Token Status List metadata (`status_list_credential`/`status_list_index`). Attributes, code lists and integrity rules transposed from the eInvoice Attestation description v0.5 into the template structure. |
| 0.7 | 2026-07-15 | Finalised for SC5. Reconciled attribute naming between the attribute tables and the integrity rules (`buyerLegalRegistrationIdentifier`, `invoiceTotalVatAmount`), completed the SD-JWT VC encoding and selective-disclosure table, and completed Chapters 4–7. Open items (payload canonicalization/hash algorithm, LoTE/trust-registry mechanism) flagged inline pending WP4 confirmation. |
| 0.71 | 2026-07-23 | Small corrections: renamed the business lifecycle claim to `invoiceLifecycleStatus` to avoid collision with Token Status List metadata; corrected `attestation_legal_category` to `non-qualified-EAA`; added conditional `precedingInvoiceReference` (EN 16931 BT-25) for corrections, cancellations and credit notes; and explicitly retained the broad supporting-document scope of `evidenceReferences`. |

# WE BUILD Attestation Rulebook for attestations of type *eInvoice*

*This Rulebook is derived from the WE BUILD v1.1 Attestation Rulebook Template (itself derived from
the EUDI attestation rulebook template) and keeps the template's chapter structure. It specifies the
eInvoice attestation used in WE BUILD Use Case SC5 (eInvoicing), Scenario 4 (Direct eInvoicing between
Business Wallets).*

* Author(s):
    * Andreas Abraham, Validated ID
    * Maarten Boender, Sphereon 


| Version | Date | Description |
|---------|------------|------------|
| 0.1 | 2026-07-01 | Initial draft |
| 0.6 | 2026-07-14 | Draft aligned with conventions |
| 0.7 | 2026-07-15 | Finalised |
| 0.71 | 2026-07-23 | Small corrections |



## 1 Introduction

### 1.1 Document scope and purpose

This Rulebook defines the **eInvoice attestation**, an Electronic Attestation of Attributes (EAA) used
within WE BUILD Use Case SC5 (eInvoicing).

In plain language, the eInvoice attestation is a verifiable representation of an invoice exchange
event. It binds the content of a structured electronic invoice (via a payload hash) to a cryptographic
signature associated with the **Supplier's** legal-person identity, so that a **Buyer** — receiving the
attestation directly into its Business Wallet — can verify the integrity of the invoice, the validity
of the Supplier's identity, and, where applicable, the authenticity and validity of any referenced
supporting evidence. In Scenario 4 this exchange is wallet-to-wallet and machine-to-machine, without an
intermediary access point: trust is established cryptographically at the point of exchange rather than
delegated to a network operator.

* **Real-world fact expressed:** that a named Supplier has issued a specific electronic invoice (bound
  by payload hash) to a named Buyer, together with the core invoice header data (amounts, currency,
  VAT, parties) and optional supporting evidence needed to accept and process it.
* **Issuers:** the **Supplier** (the invoice seller), acting as a legal person through its European
  Business Wallet (EBW). The Supplier self-issues the eInvoice attestation for each invoice.
* **Holders:** in the direct wallet-to-wallet flow the attestation is issued by the Supplier's EBW and
  presented to, and then held by, the **Buyer's** EBW.
* **Relying parties:** the **Buyer** (the invoice recipient) verifying the attestation in its Business
  Wallet; and, where the Buyer delegates processing, a third-party software/service provider that
  verifies integrity rules on the Buyer's behalf.
* **Use case / user journey:** SC5 Scenario 4 (Direct eInvoicing between Business Wallets). The
  attestation is issued per invoice, delivered directly from Supplier EBW to Buyer EBW using the
  OID4VP/DCQL profile in a machine-to-machine context, and verified on receipt. This scenario is
  designated **MVP**.
* **Source material:** the eInvoice Attestation description (v0.5 final draft, Maarten Boender) and the
  SC5 Scenario 4 specification (v1.0). Attribute names use **EN 16931** semantic term names in
  `camelCase` style; the invoice payload is bound to the EN 16931 semantic model with Peppol BIS
  Billing 3.0 syntax, with country-specific profiles permitted (see Section 2.8).

### 1.2 Document structure

* Chapter 2 describes the attestation attributes and metadata in an encoding-independent manner.
* Chapter 3 specifies the encoding. For this attestation type, the SD-JWT VC encoding (Section 3.2) is
  normative. ISO/IEC 18013-5 (mdoc) and W3C VCDM encodings are not specified, for the reasons given in
  Sections 3.1 and 3.3.
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

This document uses the terminology specified in Annex 1 of the ARF, supplemented by eInvoicing domain
terminology (Supplier/Seller, Buyer, invoice payload, EN 16931, Peppol BIS Billing 3.0) and WE BUILD
terminology (EBW, EBWOID, WE BUILD LoTL, WE BUILD Trusted List, List of Trusted Entities (LoTE)) as
defined in the SC5 specification and the WP4 Blueprint.

## 2 Attestation attributes and metadata

### Chapter overview and requirements

This chapter defines all attributes and metadata that an eInvoice attestation may contain, in an
encoding-independent manner (ARB_06 in [Topic 12]). Each attribute is marked mandatory, optional, or
conditional in its section (ARB_09). Attribute names follow the EN 16931 semantic term names in
`camelCase` style. The `NOTE` from [RFC 8610]-style descriptions applies: an attribute marked mandatory
means the Issuer SHALL ensure the element is present in the attestation; it does not imply that a
Relying Party must request it, nor that a User cannot refuse to release it.

**Applicable legal category.** Per the SC5 working assumptions, the eInvoice attestation is implemented
as a **non-qualified EAA** for the WE BUILD pilot; QEAA escalation (which would require QTSP
involvement) is a post-pilot decision. Where the SC5 specification refers to a "WE BUILD QEAA", this
denotes a technically interoperable, ITB-tested attestation within the pilot trust framework, not an
eIDAS-qualified EAA. The requirements for non-qualified EAA in [Topic 12] therefore apply:

* An attribute indicating that the attestation is an EAA SHOULD be included (ARB_12). See Section 2.1.
* One or more attributes or metadata representing identification data of the issuer (the Supplier)
  SHALL be included (ARB_15).
* One or more attributes representing the subject SHOULD be included (ARB_17).
* Attributes or metadata representing the validity period SHOULD be defined (ARB_19).
* Attributes or metadata representing the location of the trust anchor SHOULD be defined (ARB_21); see
  Chapter 5.

### 2.1 Introduction

The eInvoice attestation is modelled as **one object** representing a single invoice exchange event. It
binds to an external structured invoice payload (EN 16931 / Peppol BIS) via `invoicePayloadHash`, and
carries the core invoice header data needed for verification and acceptance (parties, amounts,
currency, VAT). It may include one or more optional `evidenceReferences` that integrity-bind supporting
business documents (e.g., purchase order, delivery note, contract or acceptance evidence), and optional
grouped `paymentInstructions` and `taxSubtotal` containers. In this version, `evidenceReferences`
deliberately retains this broad supporting-document scope, including evidence used for invoice acceptance
or dispute resolution. It is not used for correction-chain linking; `precedingInvoiceReference` serves
that separate purpose.

Per ARB_12 of [Topic 12], this document defines the attribute **`attestation_legal_category`**. Because
this Rulebook profiles a non-qualified EAA for the WE BUILD pilot, the attribute SHALL have the exact
value **`non-qualified-EAA`**.

**Logical model (informative):**

```
eInvoiceAttestation
├── attestation_legal_category : "non-qualified-EAA"
├── invoicePayloadHash                 (integrity anchor to the canonicalized invoice payload)
├── invoiceFormat                      (optional; EN 16931 default, may be country-specific)
├── invoiceNumber
├── issueDate
├── seller                             (Supplier — the issuer)
│   ├── sellerLegalRegistrationIdentifier   (EUCC/LPID identity reference)
│   ├── sellerRegistrationName
│   ├── sellerVatIdentifier
│   └── sellerCountry
├── buyer                              (Buyer — the relying party; optional identity fields)
│   ├── buyerLegalRegistrationIdentifier    (optional; EUCC/LPID identity reference)
│   ├── buyerVatIdentifier
│   ├── buyerCountry
│   └── BuyerElectronicAddress
├── amountDueForPayment
├── invoiceTotalVatAmount
├── InvoiceCurrencyCode
├── taxSubtotal[]                      (optional container; VAT breakdown, one entry per tax code)
│   ├── taxCategoryCode
│   ├── taxableAmount
│   ├── taxPercent
│   ├── taxAmount
│   └── taxExemptionReasonCode         (optional)
├── paymentInstructions                (optional container)
│   ├── paymentMeansCode
│   ├── paymentMeansText               (optional)
│   ├── paymentAccountIdentifier
│   └── paymentCardPAN                 (optional)
├── evidenceReferences[]               (optional array; supporting business documents)
│   └── evidenceReferencesType
├── precedingInvoiceReference          (conditional; required for non-active lifecycle states)
└── invoiceLifecycleStatus             (optional; defaults to active when omitted)
```

This model preserves the information content of the eInvoice Attestation description v0.5 while grouping
the seller and buyer fields for readability. The grouping is informative; the normative encoding
(Chapter 3) follows the flat/`camelCase` identifiers used in the attribute tables below.

Subsections 2.2–2.7 define the attributes and metadata. Section 2.8 documents the code lists and
Section 2.9 the integrity rules.

### 2.2 Mandatory attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------|--------------|--------------|--------------|
| `invoicePayloadHash` | N/A (WE BUILD SC5 domestic namespace) | Hash of the canonicalized invoice payload as defined by the rulebook (see IR-EI-03). Binds the attestation to the external structured invoice. | tstr | `sha256:9f2c…a1` |
| `invoiceNumber` | EN 16931 BT-1 (Invoice number) | Invoice identifier, unique for the Supplier within the agreed duplicate-detection window. | tstr | `INV-2026-000123` |
| `issueDate` | EN 16931 BT-2 (Invoice issue date) | Invoice issue date (ISO 8601 / RFC 3339 full-date). | tstr | `2026-07-15` |
| `sellerLegalRegistrationIdentifier` | EN 16931 BT-30 (Seller legal registration identifier) | Reference to the Supplier's Legal Person identity (e.g., EUCC/LPID identifier reference). | tstr | `NL853746281B01` |
| `sellerRegistrationName` | EN 16931 BT-27 (Seller name) | The registered legal name of the Supplier. | tstr | `Green Flowers B.V.` |
| `sellerVatIdentifier` | EN 16931 BT-31 (Seller VAT identifier) | The VAT / tax registration identifier of the Supplier. | tstr | `NL853746281B01` |
| `sellerCountry` | EN 16931 BT-40 (Seller country code) | The country code of the Supplier (ISO 3166-1 alpha-2). | tstr | `NL` |
| `amountDueForPayment` | EN 16931 BT-115 (Amount due for payment) | Total payable amount as per the chosen binding rules (EN 16931 / BIS). | tstr | `1210.00` |
| `invoiceTotalVatAmount` | EN 16931 BT-110 (Invoice total VAT amount) | The total VAT amount for this invoice. | tstr | `210.00` |
| `InvoiceCurrencyCode` | EN 16931 BT-5 (Invoice currency code) | Invoice currency code (ISO 4217). | tstr | `EUR` |

### 2.3 Optional attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------|--------------|--------------|--------------|
| `invoiceFormat` | N/A (see code list 2.8) | Identifier of the invoice representation / profile used for the payload. EN 16931 is the default; may be country-specific. | tstr | `EN16931` |
| `buyerLegalRegistrationIdentifier` | EN 16931 BT-47 (Buyer legal registration identifier) | Reference to the Buyer's Legal Person identity (e.g., EUCC/LPID identifier reference). | tstr | `FR59120680088` |
| `buyerVatIdentifier` | EN 16931 BT-48 (Buyer VAT identifier) | The VAT / tax registration identifier of the Buyer. | tstr | `FR59120680088` |
| `buyerCountry` | EN 16931 BT-55 (Buyer country code) | The country code of the Buyer (ISO 3166-1 alpha-2). | tstr | `FR` |
| `BuyerElectronicAddress` | EN 16931 BT-49 (Buyer electronic address) | Address/endpoint identifier for delivery/receipt handling. | tstr | `0009:FR59120680088` |
| `paymentInstructions` | EN 16931 BG-16 (Payment instructions) | Group for all payment-related information. See Section 2.4 for its members. | container | *(see 2.4)* |
| `taxSubtotal` | EN 16931 BG-23 (VAT breakdown) | VAT breakdown group (one or more entries per tax code/rate). See Section 2.4 for its members. | container (array) | *(see 2.4)* |
| `evidenceReferences` | N/A (see code list 2.8) | Optional references to supporting evidence items. See Section 2.4 for member typing and Section 2.8 for supported forms. | array | *(see 2.4 / 2.8)* |
| `invoiceLifecycleStatus` | N/A (see code list 2.8) | Business lifecycle status for corrections, cancellations and credit notes. If omitted, the lifecycle status SHALL be interpreted as `active`. | tstr | `active` |

### 2.4 Conditional attributes

*This section defines both standalone conditional attributes and members of optional containers/arrays.
For container members, presence and obligation are conditional on the presence of their parent group: if
the parent group is present, members marked "M (within group)" SHALL be present and members marked
"O (within group)" MAY be present.*

**Standalone lifecycle attribute** (conditional on `invoiceLifecycleStatus`):

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------|--------------|--------------|--------------|
| `precedingInvoiceReference` | EN 16931 BT-25 (Preceding Invoice reference) | Identifier of the original or preceding invoice to which a correction, cancellation or credit note relates. It SHALL be present when `invoiceLifecycleStatus` is `corrected`, `cancelled` or `credited`, and MAY be omitted when the lifecycle status is `active` or omitted. The reference SHALL allow the verifier to identify the corresponding preceding eInvoice attestation within the Supplier's invoice context. | tstr | `INV-2026-000123` |

**`taxSubtotal` container members** (conditional on `taxSubtotal` being present):

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------|--------------|--------------|--------------|
| `taxSubtotal.taxCategoryCode` | EN 16931 BT-118 (VAT category code) — M within group | VAT category code (the Code). | tstr | `S` |
| `taxSubtotal.taxableAmount` | EN 16931 BT-116 (VAT category taxable amount) — M within group | Sum of net amounts for this VAT category/rate (the Base). | tstr | `1000.00` |
| `taxSubtotal.taxPercent` | EN 16931 BT-119 (VAT category rate) — M within group | The VAT percentage (the Rate). | tstr | `21` |
| `taxSubtotal.taxAmount` | EN 16931 BT-117 (VAT category tax amount) — M within group | Total VAT calculated for this specific subtotal (the Tax). | tstr | `210.00` |
| `taxSubtotal.taxExemptionReasonCode` | EN 16931 BT-121 (VAT exemption reason code) — O within group | A standardized code for the exemption. | tstr | `VATEX-EU-AE` |

**`paymentInstructions` container members** (conditional on `paymentInstructions` being present):

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------|--------------|--------------|--------------|
| `paymentInstructions.paymentMeansCode` | EN 16931 BT-81 (Payment means type code); see code list 2.8 — M within group | A code representing the payment method (e.g., 30 for Credit transfer). | tstr | `30` |
| `paymentInstructions.paymentMeansText` | EN 16931 BT-82 (Payment means text) — O within group | A text description of the payment method (e.g., IBAN, VISA, MC). | tstr | `SEPA Credit Transfer` |
| `paymentInstructions.paymentAccountIdentifier` | EN 16931 BT-84 (Payment account identifier) — M within group | Payment account identifier (IBAN or other bank account number). | tstr | `NL91ABNA0417164300` |
| `paymentInstructions.paymentCardPAN` | EN 16931 BT-87 (Card PAN) — O within group | Payment card primary account number (masked or full credit/debit card PAN). | tstr | `**** **** **** 1234` |

**`evidenceReferences` array members** (conditional on `evidenceReferences` being present):

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------|--------------|--------------|--------------|
| `evidenceReferencesType` | N/A (see code list 2.8) — M within group | The type of the referenced evidence item. | tstr | `purchase_order` |

*NOTE Each `evidenceReferences` entry carries the supporting business evidence itself in one of the
supported forms defined in Section 2.8 (inline PDF/UBL as BASE64, or a publicly accessible URI plus
hash). Its scope intentionally includes purchase orders, delivery notes, contracts and acceptance
evidence, including evidence used for invoice acceptance or dispute resolution. It SHALL NOT be used as
the correction-chain reference to the original invoice; that role is fulfilled by
`precedingInvoiceReference`. The `dueDate` attribute referenced in integrity rule IR-EI-05 is reserved
for a future profile and is not defined in this version.*

### 2.5 Mandatory metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------|--------------|--------------|--------------|
| `attestation_legal_category` | Defined in Section 2.1 | Indicates the legal category of the attestation. | string | `non-qualified-EAA` |
| `vct` | [SD-JWT VC] | Verifiable Credential Type identifier (see Section 3.2). | string | `eu.we-build:einvoice:1` |
| `iss` | [IANA-JWT-Claims] | Issuer identifier (the Supplier's issuing system / EBW). | string (URI) | `https://wallet.greenflowers.example/issuer` |
| `iat` | [IANA-JWT-Claims] | Issuance timestamp. | NumericDate | `1768435200` |
| `exp` | [IANA-JWT-Claims] | Technical expiry timestamp of the attestation. | NumericDate | `1800057600` |
| `status` (metadata) | [SD-JWT VC] / [Token Status List] | Reference to the Token Status List entry for revocation (see Chapter 6). Distinct from the business `invoiceLifecycleStatus` attribute in Section 2.3. | object | *(see Chapter 6)* |
| `cnf` | [SD-JWT VC] | Holder key-binding confirmation (proof of possession by the Supplier's EBW at issuance). | object | *(JWK / key reference)* |

### 2.6 Optional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------|--------------|--------------|--------------|
| `cryptographically_bound_to` | ARB_28 / [Topic 12] | vct of another attestation on the same Wallet Unit to which this attestation is cryptographically bound (the Supplier's EBWOID). RECOMMENDED — see Chapter 4. | string | `uri:eu.ebw.oid.1` |

### 2.7 Conditional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------|--------------|--------------|--------------|
| N/A | N/A | No conditional metadata is defined in this version. | N/A | N/A |

### 2.8 Code lists

| **Field name** | **Allowed values** | **Meaning** | **Source / vocabulary** | **Notes / extensibility** |
|----------------|--------------------|-------------|--------------------------|---------------------------|
| `invoiceFormat` | `EN16931` (default); country-specific profiles e.g. `ZUGFeRD`, `INSBOUW` | Identifies the invoice representation/profile used for the payload. | EN 16931; national CIUS/profiles | EN 16931 is assumed as the default but can be country-specific. WP4 Semantic WG to confirm the controlled set. |
| `paymentInstructions.paymentMeansCode` | `30`, `48`, `49`, `58` | Payment method: `30` Credit transfer (bank transfer buyer→seller); `48` Bank card (debit/credit card); `49` Direct debit (debited from customer's bank account); `58` SEPA credit transfer (SEPA-compliant credit transfer). | UNTDED 4461 (UNCL 4461) code list | Provides machine-readable payment method identification for automated processing by banks and tax authorities. Additional UNCL 4461 codes MAY be used if agreed across issuer and verifier implementations. |
| `evidenceReferences` | Inline `PDF as BASE64`; inline `UBL as BASE64`; `URI identifier + hash` | Supported forms for carrying/referencing a supporting business evidence item. | WE BUILD SC5 domestic vocabulary | Broad scope is intentional: purchase-order, delivery, contractual and acceptance/dispute evidence are supported. This field SHALL NOT be used for correction-chain linking. If a URI form is used, the link MUST be publicly accessible (rationale: no standard authorization mechanism exists for protected URIs). |
| `evidenceReferencesType` | `purchase_order`, `delivery_note`, `contract`, `acceptance_evidence`, `other` | The type of the referenced supporting evidence. | WE BUILD SC5 domestic vocabulary | Extensible only if new values are defined consistently across issuers and verifiers and registered in the WE BUILD Attestation Rulebooks catalog. |
| `invoiceLifecycleStatus` | `active`, `corrected`, `cancelled`, `credited` | Business lifecycle status of the invoice for corrections, cancellations and credit notes. | WE BUILD SC5 domestic vocabulary | If omitted, the value is interpreted as `active`. State transitions SHALL follow IR-EI-09. Values other than `active` require `precedingInvoiceReference`. |
| `taxSubtotal.taxCategoryCode` | e.g. `S` (standard), `Z` (zero rated), `E` (exempt), `AE` (reverse charge), `G`, `O`, `K` | VAT category code. | UNCL 5305 (EN 16931 code list) | Use the EN 16931-aligned subset of UNCL 5305. |

### 2.9 Integrity rules

*NOTE Two naming inconsistencies in the source description v0.5 have been reconciled here to match the
attribute tables in Sections 2.2–2.4: `buyerRegistrationIdentifier` → `buyerLegalRegistrationIdentifier`,
and `totalTaxAmount` → `invoiceTotalVatAmount`.*

| **Rule ID** | **Rule statement** | **Why it exists** | **Where enforced** | **Verifier / issuer behavior on failure** |
|-------------|--------------------|-------------------|--------------------|-------------------------------------------|
| `IR-EI-01` | The attestation SHALL be valid only if the Supplier's Wallet Unit is bound to a valid legal-entity attestation (e.g., EUCC or equivalent), and the Buyer identity in the invoice matches the receiving Wallet's legal-entity identity. | Ensures both parties are identified legal persons and that the invoice is addressed to the receiving wallet. | Issuer binding (EBWOID, Chapter 5); verifier identity match. | Verifier SHALL treat the attestation as invalid and reject/quarantine the invoice. |
| `IR-EI-02` | The attestation SHALL be valid only if the Supplier's signing key is trusted and valid at verification time (not expired/revoked/suspended) and the signature verifies. | Guarantees authenticity and integrity of the attestation. | Verifier (base verification 4.2.2–4.2.6). | Verifier SHALL reject. |
| `IR-EI-03` | `invoicePayloadHash` SHALL equal the hash of the canonicalized invoice payload, using the rulebook-defined canonicalization method and hash algorithm. | Binds the attestation to the exact invoice content and detects tampering. | Issuer at issuance; verifier recomputes on receipt. | Verifier SHALL reject/quarantine on mismatch. *[OPEN — canonicalization method and hash algorithm to be confirmed by WP4 Architecture WG.]* |
| `IR-EI-04` | `invoiceNumber` SHALL be present and unique for the Supplier within the Relying Party's duplicate-detection window; duplicates SHALL trigger reject or quarantine per Relying Party policy. | Prevents duplicate/replayed invoices. | Verifier business validation. | Verifier SHALL reject or quarantine per policy. |
| `IR-EI-05` | `issueDate` SHALL be present and not unreasonably in the future (allow clock-skew tolerance). If `dueDate` is present (in a future profile), it SHALL be ≥ `issueDate`. | Ensures temporal plausibility and consistency of dates. | Verifier business validation. | Verifier SHALL reject/quarantine. |
| `IR-EI-06` | `sellerLegalRegistrationIdentifier` and (when present) `buyerLegalRegistrationIdentifier` SHALL match the corresponding identities in the invoice payload; mismatches invalidate the attestation. | Ensures the attestation parties and the payload parties are the same. | Verifier cross-check against payload. | Verifier SHALL treat the attestation as invalid. |
| `IR-EI-07` | If `taxSubtotal` is used, `invoiceTotalVatAmount` SHALL strictly equal the sum of all `taxSubtotal.taxAmount` values. | Guarantees internal arithmetic consistency of VAT amounts. | Issuer; verifier arithmetic check. | Verifier SHALL reject/quarantine. |
| `IR-EI-08` | Any referenced or embedded evidence SHALL be integrity-bound and, where applicable, valid at verification time (status/expiry/revocation). | Ensures supporting evidence cannot be substituted or tampered with. | Verifier evidence verification (see Section 4.2.9). | Verifier SHALL reject/quarantine the affected evidence and apply policy. |
| `IR-EI-09` | If `invoiceLifecycleStatus` is `corrected`, `cancelled` or `credited`, `precedingInvoiceReference` SHALL be present and SHALL identify the original or preceding invoice and its corresponding eInvoice attestation. Only rulebook-defined lifecycle values and state transitions (see code list 2.8) SHALL be used. | Maintains an auditable, well-formed correction lifecycle and makes the original invoice reference machine-verifiable. | Issuer business rules; verifier reference and state validation. | Verifier SHALL reject an invalid lifecycle value, invalid transition, missing reference or unresolvable preceding invoice/attestation reference. |

## 3 Attestation encoding

### 3.1 ISO/IEC 18013-5-compliant encoding

The eInvoice attestation is presented in automated, online, system-to-system (wallet-to-wallet) flows
between European Business Wallets (see Chapter 4 and SC5 Scenario 4). There is no proximity / offline
presentation use case (ARB_02). An ISO/IEC 18013-5 (mdoc) encoding is therefore **not specified** in
this version. If a future use case requires proximity presentation, a document type and mdoc encoding
would be added here.

### 3.2 SD-JWT VC-based encoding

This attestation type SHALL be issued in the [SD-JWT VC]-compliant format and SHALL comply with the
'SD-JWT VCs' profile specified in [HAIP] (ARB_01b).

**Verifiable Credential Type (`vct`):** `eu.we-build:einvoice:1`

*(Proposed value; subject to registration in the WE BUILD Attestation Rulebooks catalog by the WP4
semantics group, ARB_05.)*

For all claims, the tables below specify whether an Attestation Provider MUST, MAY, or MUST NOT make the
claim selectively disclosable (ARB_30). A Type Metadata Document SHOULD be defined for this vct per
Chapter 6 of [SD-JWT VC] (ARB_31).

Encoding conventions: `tstr` attributes are encoded as JSON strings; monetary and percentage values are
carried as strings (as in the source description) to preserve exact decimal representation; dates use
RFC 3339 full-date strings; `taxSubtotal` and `evidenceReferences` are JSON arrays of objects; and
`paymentInstructions` is a JSON object.

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
| `invoicePayloadHash` | invoicePayloadHash | string | Integrity anchor; SHALL always be present for verification | MUST NOT |
| `invoiceFormat` | invoiceFormat | string | Code list 2.8 | MAY |
| `invoiceNumber` | invoiceNumber | string | Mandatory (2.2) | MAY |
| `issueDate` | issueDate | string (full-date) | Mandatory (2.2) | MAY |
| `sellerLegalRegistrationIdentifier` | sellerLegalRegistrationIdentifier | string | Mandatory (2.2) | MAY |
| `sellerRegistrationName` | sellerRegistrationName | string | Mandatory (2.2) | MAY |
| `sellerVatIdentifier` | sellerVatIdentifier | string | Mandatory (2.2) | MAY |
| `sellerCountry` | sellerCountry | string | Mandatory (2.2) | MAY |
| `buyerLegalRegistrationIdentifier` | buyerLegalRegistrationIdentifier | string | Optional (2.3) | MAY |
| `buyerVatIdentifier` | buyerVatIdentifier | string | Optional (2.3) | MAY |
| `buyerCountry` | buyerCountry | string | Optional (2.3) | MAY |
| `BuyerElectronicAddress` | BuyerElectronicAddress | string | Optional (2.3) | MAY |
| `amountDueForPayment` | amountDueForPayment | string | Mandatory (2.2) | MAY |
| `invoiceTotalVatAmount` | invoiceTotalVatAmount | string | Mandatory (2.2) | MAY |
| `InvoiceCurrencyCode` | InvoiceCurrencyCode | string | Mandatory (2.2) | MAY |
| `taxSubtotal` | taxSubtotal | array | Members in 2.4 | MAY |
| `paymentInstructions` | paymentInstructions | object | Members in 2.4; sensitive payment data | MUST — issuer SHALL make selectively disclosable so payment details can be withheld where not required |
| `evidenceReferences` | evidenceReferences | array | Members in 2.4; forms and scope in 2.8 | MAY |
| `precedingInvoiceReference` | precedingInvoiceReference | string | Conditional lifecycle reference (2.4); required by IR-EI-09 for non-active lifecycle states | MUST NOT |
| `invoiceLifecycleStatus` | invoiceLifecycleStatus | string | Business lifecycle (2.3); distinct from registered `status` metadata; defaults to `active` when omitted | MUST NOT |
| `cryptographically_bound_to` | cryptographically_bound_to | string | Section 2.6; Chapter 4 | MUST NOT |

**Illustrative JWT claim set (informative, synthetic data):**

```json
{
  "vct": "eu.we-build:einvoice:1",
  "iss": "https://wallet.greenflowers.example/issuer",
  "iat": 1768435200,
  "exp": 1800057600,
  "attestation_legal_category": "non-qualified-EAA",
  "status": { "status_list": { "idx": 128, "uri": "https://status.webuild.example/sc5/einvoice" } },
  "cnf": { "jwk": { "kty": "EC", "crv": "P-256", "x": "...", "y": "..." } },
  "invoicePayloadHash": "sha256:9f2c8b1e7d43a0c5f6e9b2d1a4c7e0f3b6d9a2c5e8f1b4d7a0c3e6f9b2d5a8c1",
  "invoiceFormat": "EN16931",
  "invoiceNumber": "INV-2026-000123",
  "issueDate": "2026-07-15",
  "sellerLegalRegistrationIdentifier": "NL853746281B01",
  "sellerRegistrationName": "Green Flowers B.V.",
  "sellerVatIdentifier": "NL853746281B01",
  "sellerCountry": "NL",
  "buyerLegalRegistrationIdentifier": "FR59120680088",
  "buyerVatIdentifier": "FR59120680088",
  "buyerCountry": "FR",
  "BuyerElectronicAddress": "0009:FR59120680088",
  "amountDueForPayment": "1210.00",
  "invoiceTotalVatAmount": "210.00",
  "InvoiceCurrencyCode": "EUR",
  "taxSubtotal": [
    {
      "taxCategoryCode": "S",
      "taxableAmount": "1000.00",
      "taxPercent": "21",
      "taxAmount": "210.00"
    }
  ],
  "paymentInstructions": {
    "paymentMeansCode": "58",
    "paymentMeansText": "SEPA Credit Transfer",
    "paymentAccountIdentifier": "NL91ABNA0417164300"
  },
  "evidenceReferences": [
    { "evidenceReferencesType": "purchase_order" }
  ],
  "invoiceLifecycleStatus": "active"
}
```

[RULEBOOK AUTHOR TO PROVIDE AN EXAMPLE OF THE ISSUED SD-JWT IN base64 ENCODING ONCE A REFERENCE
ISSUER IS AVAILABLE]

[RULEBOOK AUTHOR TO PROVIDE A HUMAN-READABLE VERSION OF THE SD-JWT PAYLOAD WITH THE DISCLOSURES,
ONCE THE SELECTIVE-DISCLOSURE STRUCTURE IS FINALISED WITH WP4]

### 3.3 W3C Verifiable Credentials Data Model-based encoding

A W3C VCDM encoding is **not specified** for this attestation type. SD-JWT VC (Section 3.2) is the
single normative encoding for SC5, consistent with the WE BUILD Conformance Specifications. (Note that
only a non-qualified EAA may use the VCDM format, ARB_01a; this attestation is a non-qualified EAA, so a
VCDM encoding could be added in future if an interoperability need arises.)

## 4 Attestation usage

**Primary use case.** SC5 Scenario 4 (Direct eInvoicing between Business Wallets). The Supplier's EBW
issues and signs the eInvoice attestation and presents it directly to the Buyer's EBW endpoint using
the OID4VP/DCQL profile in a machine-to-machine context, having resolved the Buyer's wallet endpoint via
the List of Trusted Entities (LoTE), as specified in [ETSI TS 119 602]. The Buyer's EBW verifies the
attestation, recomputes the payload hash, and accepts, rejects, or quarantines the invoice.

**PID verification (ARB_27).** A Relying Party (the Buyer) **does not** request or verify a PID. Both
Supplier and Buyer are legal persons; identity assurance is provided by the EBWOID / legal-entity
binding (see Chapter 5), not by a natural-person PID.

**Presentation requirements.** Presentation is online and system-to-system via OpenID4VP, using DCQL
queries as profiled by the WE BUILD Conformance Specification cs-02, in a machine-to-machine context. In
the supplier-initiated flow, the Supplier's wallet first fetches a fresh Presentation Request (OID4VP
Request Object — DCQL constraints, nonce, audience, expiry, correlation identifier, submission endpoint)
from the Buyer's endpoint, then submits the eInvoice attestation (and invoice payload / optional
evidence) as the OID4VP response. No offline / proximity presentation is supported. The upcoming
Implementing Acts may additionally require a (Q)ERDS-based delivery track for stronger delivery evidence;
this is out of scope for the MVP but noted as a possible additional pilot track.

**Device binding (ARB_34).** An attestation of this type SHOULD be device-bound to the issuing/holding
Wallet Unit, evidenced by the `cnf` claim and verified through key binding at presentation (base
verification step 4.2.8).

**Binding to another attestation (ARB_28).** An attestation of this type SHOULD be cryptographically
bound to the Supplier's organisational identity attestation (EBWOID) on the same Wallet Unit. Where
present, the binding metadata identifier SHALL be `cryptographically_bound_to`, its value SHALL be a
string containing the bound attestation's vct, and that value SHALL be `uri:eu.ebw.oid.1` (the EBWOID
vct defined in [rb-ebwoid]).

**Transactional data ([Topic 20]).** No payment-authentication transactional data is defined for this
attestation type. Although the invoice carries payment information (`paymentInstructions`), the eInvoice
attestation records an *invoice exchange event*; it does not authorise an individual electronic payment,
so the strong-user-authentication transactional-data mechanism of [Topic 20] does not apply.

### 4.1 Issuance process

The issuer is the Supplier, a legal person self-issuing this EAA through its EBW for each invoice, on
the basis of an invoice payload prepared by its ERP (canonicalized, with `invoicePayloadHash` computed
per the agreed rulebook). Issuance uses OpenID4VCI as profiled by the WE BUILD Conformance Specification
cs-01.

The Issuer SHALL implement the base issuer obligations defined in the Base Verification specification:
<https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-base/verifier-base-verification.md#41-issuer-obligations>

In particular, the issuer SHALL include the holder-generated public key (`cnf`) in the payload, SHALL
include its own EBWOID-anchored certificate material in the attestation header (see Chapter 5), SHALL
populate the `status` metadata (see Chapter 6) in every issued attestation, and SHALL ensure
`invoicePayloadHash` is computed over the canonicalized payload per IR-EI-03.

### 4.2 Relying Party obligations

When receiving and processing an eInvoice attestation, the Relying Party (the Buyer, or a delegated
third-party processor) SHALL perform the following verification obligations.

#### 4.2.1 – 4.2.8 Base verification process

The Relying Party SHALL perform the base attestation verification process for EAAs as defined in the
Base Verification specification:
<https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-base/verifier-base-verification.md#42-relying-party-obligations>

This covers verification of attestation authenticity and issuer identity via the EBWOID chain
(4.2.2–4.2.4), validity periods (4.2.5), revocation status (4.2.6) — including checking the Supplier's
authorization status against the Status Service — wallet integrity via the WUA (4.2.7), and holder key
binding (4.2.8).

#### 4.2.9 Validate attestation-specific integrity rules

In addition to the base verification, the Relying Party SHALL apply the integrity rules IR-EI-01 to
IR-EI-09 defined in Section 2.9. In particular, the Relying Party SHALL: recompute `invoicePayloadHash`
over the received invoice payload and confirm it matches (IR-EI-03); confirm that the invoice's buyer
field matches the receiving Wallet's own identity (IR-EI-01); verify VAT arithmetic consistency
(IR-EI-07); and, where `evidenceReferences` are present, retrieve the referenced artefacts and verify
their integrity and validity (IR-EI-08); and validate `invoiceLifecycleStatus` together with
`precedingInvoiceReference` for corrections, cancellations and credit notes (IR-EI-09). If all checks
pass, the Buyer's Wallet accepts the invoice and
stores the attestation for audit; if any check fails, it rejects or quarantines the invoice with an
error code. In both cases an optional status message MAY be returned to the Supplier's Wallet.

## 5 Trust anchors

This chapter specifies how a Relying Party establishes trust in the issuer of an eInvoice attestation.
The corresponding verification procedures are steps 4.2.2–4.2.4 of the Base Verification specification.

The eInvoice attestation is an **EAA self-issued by a legal entity** (the Supplier). Suppliers are not,
and cannot practically be, individually registered on a Trusted List. Trust is therefore established
through a cryptographic chain anchored in the issuer's **EBWOID**, following the common WE BUILD EAA
trust model:

* The issuer's EBWOID SHALL be included in the header of every issued eInvoice attestation. During
  EBWOID issuance, the EBWOID provider verifies that the public key contained in the EBWOID is owned by
  the EBW owner.
* The Relying Party SHALL verify the EBWOID in accordance with [rb-ebwoid] and the Base Verification
  specification. The EBWOID provider's trust anchor is obtained via the WE BUILD trust list
  infrastructure (TLOL) operated under WP4.
* Upon successful verification, the Relying Party obtains: assurance that the EBWOID was issued by an
  authorised provider (and is not self-issued); the verified identity of the issuer, including its
  legal name and EUID; and the public key authorised to verify the attestation signature.
* The Relying Party SHALL then confirm that the verified issuer identity (EUID) matches
  `sellerLegalRegistrationIdentifier` in the attestation payload (IR-EI-06).

For endpoint discovery and issuer-metadata resolution, the WE BUILD **List of Trusted Entities (LoTE)**
per [ETSI TS 119 602] is used (the EC's proposed European Digital Directory (EDD) may serve this role).
*[OPEN — the trust anchor mechanism for LPID and signing keys (registry vs federation vs QTSP signals)
is not in scope of SC5 but is a dependency; it will be based on [ETSI TS 119 602]. WP4 Trust Registry
Infrastructure WG to confirm.]*

## 6 Revocation

An eInvoice attestation records an invoice exchange event, and SHALL support revocation so that an
issued attestation can be invalidated where necessary (e.g., an invoice issued in error). The
attestation is **revocable**; it is not a short-lived (≤24h) attestation.

### 6.1 Revocation mechanism

* **Token Status List:** the issuer SHALL maintain an active IETF Token Status List ([Token Status
  List]), aligned with the Attestation Status List mechanism specified by the EU Commission and mandated
  by the WE BUILD ADR on Attestation Revocation.
* **Credential metadata:** the `status` metadata SHALL be populated in every issued attestation with:
  * `status_list_credential` (string, URI) — the URI of the Status List Credential containing the status
    bitstring;
  * `status_list_index` (integer, ≥ 0) — the zero-based index into the status list bitstring for this
    attestation.
* **Authorized authority:** only the issuing Supplier (the self-issuing legal entity) may modify the
  status list entry.

### 6.2 Relationship between revocation and `invoiceLifecycleStatus`

Cryptographic revocation (via the registered Token Status List `status` metadata, Section 6.1) is distinct
from the business-level `invoiceLifecycleStatus` attribute (`active`/`corrected`/`cancelled`/`credited`,
Section 2.3). `invoiceLifecycleStatus` and the correction/credit-note lifecycle (IR-EI-09) express the
accounting state of the invoice, while Token Status List revocation expresses the cryptographic validity
of the attestation. An issuer correcting or cancelling an invoice SHOULD issue a new attestation with the
appropriate `invoiceLifecycleStatus` value and a `precedingInvoiceReference` identifying the original or
preceding invoice. The issuer SHALL revoke the superseded attestation via the Token Status List where it
should no longer be relied upon.

### 6.3 Revocation triggers and business rules

* **Issuer trigger (obligation):** the Supplier SHALL revoke the attestation without undue delay when
  the invoice is cancelled or replaced, or when the attestation was issued in error or contains
  inaccurate identity data.
* **Relying Party action:** a revoked or suspended attestation SHALL be treated as invalid; the Buyer
  SHALL reject or quarantine an invoice relying on it. The business interpretation of a revocation (e.g.
  handling of invoices already accepted) is determined by the Relying Party's internal policies.

## 7 Compliance

This Rulebook follows the structure mandated by [Topic 12] of the ARF and the WE BUILD Attestation
Rulebook Template v1.1. The eInvoice attestation is a **non-qualified EAA** in the sense of the
[European Digital Identity Regulation], implemented within the WE BUILD pilot trust framework rather
than the eIDAS production ecosystem (WP4 Blueprint D4.1 §1.2.1). It uses the SD-JWT VC format profiled
by [HAIP], OpenID4VCI for issuance and OpenID4VP/DCQL for presentation per the WE BUILD Conformance
Specifications (cs-01, cs-02), and the IETF Token Status List for revocation per the WE BUILD ADR on
Attestation Revocation. The invoice payload is bound to the [EN 16931] semantic model with [Peppol BIS
Billing 3.0] syntax (country-specific profiles permitted), consistent with ViDA-relevant guidance where
applicable. Escalation to an eIDAS-qualified EAA (QEAA), and any associated QTSP involvement, is a
post-pilot decision and out of scope for this version. Open dependencies (payload canonicalization and
hash strategy; the LPID/signing-key trust anchor mechanism) are tracked with WP4 and noted inline in
Sections 2.9 and 5.

## 8 References

| **Item Reference** | **Standard name/details** |
|--------------------|---------------------------|
| [European Digital Identity Regulation] | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework |
| [HAIP] | OpenID4VC High Assurance Interoperability Profile, OpenID Foundation, draft-03 |
| [IANA-JWT-Claims] | IANA JSON Web Token Claims Registry. <https://www.iana.org/assignments/jwt/jwt.xhtml> |
| [RFC 2119] | Key words for use in RFCs to Indicate Requirement Levels, S. Bradner, March 1997 |
| [RFC 3339] | Date and Time on the Internet: Timestamps, G. Klyne et al., July 2002 |
| [RFC 8610] | Concise Data Definition Language (CDDL), H. Birkholz et al., June 2019 |
| [SD-JWT VC] | SD-JWT-based Verifiable Credentials. <https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/> |
| [Token Status List] | Token Status List, IETF OAuth WG. <https://datatracker.ietf.org/doc/draft-ietf-oauth-status-list/> |
| [OpenID4VCI] | OpenID for Verifiable Credential Issuance, OpenID Foundation |
| [OpenID4VP] | OpenID for Verifiable Presentations, OpenID Foundation |
| [ETSI TS 119 602] | ETSI TS 119 602 — Trusted Lists / List of Trusted Entities (LoTE). <https://www.etsi.org/deliver/etsi_TS/119600_119699/119602/01.01.01_60/> |
| [Topic 7] | ARF Annex 2 — Topic 7 — Attestation revocation and revocation checking |
| [Topic 10] | ARF Annex 2 — Topic 10 — Issuing a PID or attestation to a Wallet Unit |
| [Topic 12] | ARF Annex 2 — Topic 12 — Attestation Rulebooks |
| [Topic 20] | ARF Annex 2 — Topic 20 — Strong User authentication for electronic payments |
| [EN 16931] | European standard on the semantic data model of the core elements of an electronic invoice |
| [Peppol BIS Billing 3.0] | OpenPeppol Business Interoperability Specification, Billing 3.0 |
| [UNCL 4461] | UNTDED 4461 (UN/CEFACT) Payment means code list |
| [UNCL 5305] | UN/CEFACT Duty/tax/fee category code list (VAT category codes) |
| [ViDA] | Council Directive amending Directive 2006/112/EC as regards VAT rules for the digital age (Digital Reporting Requirements) |
| [EWC RB001] | EWC LPID Rulebook |
| [EWC RB002] | EWC EUCC Rulebook |
| [WP4 Blueprint] | WE BUILD Deliverable D4.1 (trust infrastructure blueprint) |
| [WBCS] | WE BUILD Conformance Specifications, cs-01 (issuance) and cs-02 (presentation) |
| [WE BUILD ADR — Revocation] | WE BUILD Architecture Decision Record on Attestation Revocation |
| [rb-base — Base Verification] | WE BUILD Rulebook for common verification steps for all attestations. <https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-base/verifier-base-verification.md> |
| [rb-base — Handshake] | WE BUILD Rulebook for Mutual Identification & Consent Handshake. <https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-base/holder-authorization-handshake.md> |
| [rb-ebwoid] | WE BUILD EBWOID Rulebook. <https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/rb-ebwoid/README.md> |
