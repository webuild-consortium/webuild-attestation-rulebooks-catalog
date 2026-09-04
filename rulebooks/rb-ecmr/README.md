# WE BUILD SC1 Attestation Rulebook for eCMR Attestation (mDoc)

**Author(s):**
- Christophe DANNA, IN Groupe
- Mohamed OULMAHDI, IN Groupe
- Heiti MERING, Digilogistika Keskus

**Reviewer(s)**
- [to be added] when passing to V0.7 

**Version History**

| Version | Date | Description |
|----------|----------|-------------|
| 0.1 | 15-07-2026 | Initial draft created from SC1.3 eCMR Attestation Workshop outcomes |
| 0.6 | 21-07-2026 | (co)Leads review. Structural consistency, terminology, and cross-references between attribute tables and the illustrative encoding example. Not a substantive review of the trust/revocation model. |
| 1.0 | 03-09-2026 | MVP version, updates with optional fields will be done for MVP+ |


# 1 Introduction

## 1.1 Document scope and purpose

The eCMR Attestation is a verifiable electronic attestation designed to provide trusted, portable and interoperable evidence of an Electronic Consignment Note (eCMR) within the EUDI Wallet ecosystem. The attestation is issued by a trusted eCMR platform and enables transport stakeholders and competent authorities to verify the authenticity, integrity and provenance of transport information. The eCMR attestation issued to a company and presented by the driver with its EBW is a multi-purposes attestation: 
-	Link to eCMR, used to give access only to the right consignment data (MVP);
-	The document itself for offline presentation by the driver (PDF, MVP+);
-	eFTI QR Code for roadside checks by authorities (via eFTI network, MVP+).


The attestation expresses the existence of a valid eCMR and establishes a trusted link between:

- The transport consignment;
- The issuing eCMR platform;
- The identified business parties involved in the transport operation;
- The evidence document associated with the transport operation.

The attestation supports:

- Roadside inspections;
- Cross-border freight transport operations;
- Logistics ecosystem interoperability;
- Future eFTI integration scenarios;
- Both online and offline (MVP+) verification processes. 

The primary actors are:

| Role | Description |
|--------|-------------|
| Issuer | Trusted eCMR platform |
| Holder | Driver, carrier representative or authorised business wallet holder |
| Relying Party | Logistics stakeholders (MVP) and roadside authorities (MVP+) |

## 1.2 Document structure

This Rulebook is structured as follows:

- Chapter 2 describes the attestation attributes and metadata in an encoding-independent manner.
- Chapter 3 specifies how the attestation attributes and metadata are encoded and complies with  ISO/IEC 18013-5 (mdoc). 
- Chapter 4 specifies attestation usage scenarios and obligations.
- Chapter 5 defines trust anchors and verification mechanisms for issuer authorization.
- Chapter 6 defines attestation revocation mechanisms.
- Chapter 7 provides reference information.

### 1.3 Key words

This document uses the capitalised key words `SHALL`, `SHOULD` and `MAY` as
specified in [RFC 2119], i.e., to indicate requirements, recommendations and
options specified in this document.

In addition, 'must' (non-capitalised) is used to indicate an external
constraint, i.e., a requirement that is not mandated by this document, but, for
instance, by an external document. The word 'can' indicates a capability,
whereas other words, such as 'will', and 'is' or 'are' are intended as
statements of fact.

## 1.4 Terminology 

Additional terms used in this document:

| Term | Definition |
|--------|-----------|
| EBWOID | European Business Wallet Owner Identifier |
| Business Wallet | Wallet associated with a legal entity |
| eCMR Platform | Platform managing electronic consignment records |
| Consignment | Transport operation represented by an eCMR |
| CMDS | Consignment Movement DataSet -> the consignment XML data |
| Roadside Check | Verification procedure performed by enforcement authorities |

# 2 Attestation attributes and metadata

## 2.1 Introduction

The eCMR Attestation SHALL be issued exclusively as an ISO/IEC 18013-5 compliant mDoc. The workshop concluded that mDoc is the preferred format because it supports proximity presentation, offline verification and compatibility with EUDI Wallet requirements. 

The attestation provides:

- Identification of a specific transport consignment;
- Trusted identification of involved business parties through EBWOIDs;
- Integrity protection of transport information;
- Support for both online and offline verification scenarios;
- Support for human-readable document presentation when required by national regulations. 

The attribute `attestation_legal_category` SHALL indicate the legal classification of the attestation. This attestation type is classified as "EAA" within the EBW Wallet ecosystem, as it is typically issued by an eCMR platform and no authentic source is used.

All attributes and metadate SHALL be disclosable.

## 2.2 Mandatory attributes
### 2.2.1 Consignment identification 

| Data Identifier |  Definition | Data Type | Example Value |
|----------------|-------------|-----------|---------------|
| consignment_identifier |  Unique identifier of the consignment* | string | CMR-2026-000123 |
| ecmr_platform_url |  URL of the originating eCMR platform | URI | https://platform.example.eu/ecmr/CMR-2026-000123 |


* The issuing eCMR platform can freely use whatever content needed to identify the consignment and its eCMR. On purpose, already defined Id fields in UN/CEFACT Electronic Road Consignment Note (eCMR)are not used [UN/CEFACT eCMR].

## 2.3 Optional attributes

Optional attributes are the eFTI Information and a human readable eCMR (MVP+).

### 2.3.1 eFTI information (MVP+)

eFTI Unique Information Link.

| Data Identifier |  Definition | Data Type | Example Value |
|----------------|-------------|-----------|---------------|
| efti_dataset_identifier | The unique ID of an eFTI CMDS, assigned by an eFTI platform | String-36 | EFTI-248811 |
| efti_platform_identifier |  The identifier of an eFTI platform | String-17 | EFTI-PLAT-45 |
| efti_gate_identifier |  The identifier of an eFTI gate | String-17 | EFTI-GATE-12 |

Note1: at the present time, the naming rule for eFTI platform and gate identifiers has not been defined yet by the eFTI technical guidance documents. Examples are fictional.

Note2: Other fields might be considered whith MVP+ scenario and added later if needed.
- QR Code image could be added later if needed.
- XML MMT file (base64).

### 2.3.2 Human readable eCMR (MVP+)
| Data Identifier |  Definition | Data Type | Example Value |
|----------------|-------------|-----------|---------------|
| embedded_ecmr_pdf |  Embedded human-readable eCMR document for offline presentation | actual pdf/a file as base64 string |    |

Note: no embedded transport dataset representation, only a human readable document 

These attributes must be present when offline verification or human-readable presentation is required. Optional in MVP, mandatory in MVP+.

## 2.4 Conditional attributes
### 2.4.1 Parties identification (MVP)

| Data Identifier |  Definition | Data Type | Example Value |
|----------------|-------------|-----------|---------------|
| consignor_ebwoid |  ebwoid of the issuing organisation | String | SEBOLREG.123456789 |
| carrier_ebwoid |  ebwoid of the carrier | String | NOFOR.123456789 |
| consignee_ebwoid |  ebwoid of the consignor | String | SEBOLREG.987654321 |

Note: At least One ebwoid SHALL be included in the attestation, depending on the step reached in process.

## 2.5 Mandatory metadata (MVP)

| Data Identifier |  Definition | Data Type | Example Value |
|----------------|-------------|-----------|---------------|
| attestation_legal_category |  Legal category of the attestation | String | non-qualified-EAA |
| issuer_ebwoid |  ebwoid of the issuing organisation | String | EU.ebwoid.12345678 |
| trust_anchor_url |  URL of trust anchor information | URI | https://trust.webuild.eu |
| expiry_date |  Expiration date of the attestation | DateTime | 2026-07-30T00:00:00Z |
| attestation_scheme |  Attestation schema | String | TBD |
| issuance_date |  Timestamp of issuance | datetime | 2026-06-30T10:25:00Z |

## 2.6 Optional metadata

None

## 2.7 Conditional metadata

None

## 2.8 Code lists

| Field Name | Allowed Values | Meaning | Source |
|------------|----------------|---------|---------|
| attestation_legal_category | "non-qualified-EAA" | Legal classification of the attestation | EUDI Framework |

## 2.9 Integrity rules

| Rule ID | Rule Statement |
|----------|----------------|
| IR-01 | A mandatory string attribute SHALL be a non-empty string |
| IR-02 | datetime SHALL be ISO 8601 compliant |

# 3 Attestation encoding

## 3.1 ISO/IEC 18013-5 compliant encoding

The eCMR Attestation SHALL be issued exclusively as an ISO/IEC 18013-5 compliant mDoc. This format supports:

- Device-to-device proximity presentation;
- Offline verification;
- Integration within the EUDI Wallet ecosystem;
- Embedded transport evidence;
- Selective disclosure mechanisms. 

docType `"eu.webuildconsortium.ecmr.attestation.V1`

Namespace `"eu.webuildconsortium.ecmr.attestation.V1`

### Illustrative example

Example for MVP scenario (mandatory fields only). See clarification about MVP and MVP+ scenarios in section [1.1 Document scope and purpose ](#1.1-Document-scope-and-purpose).


```json
{
  "docType": "eu.webuildconsortium.ecmr.attestation.V1",
  "issuerSigned": {
    "namespaces": {
      "eu.webuild.ecmr.attestation.1": [
        {"elementIdentifier": "attestation_legal_category", "elementValue": "non-qualified-EAA"},
        {"elementIdentifier": "trust_anchor_url", "elementValue": ""},
        {"elementIdentifier": "attestation_scheme", "elementValue": "TBD"},
        {"elementIdentifier": "consignment_identifier", "elementValue": "CMR-2026-000123"},
        {"elementIdentifier": "ecmr_platform_url", "elementValue": "https://platform.example.eu/ecmr/CMR-2026-000123"},
        {"elementIdentifier": "issuer_ebwoid", "elementValue": "EU.ebwoid.12345678"},
        {"elementIdentifier": "carrier_ebwoid", "elementValue": "EU.ebwoid.87654321"},
        {"elementIdentifier": "consignor_ebwoid", "elementValue": "EU.ebwoid.11223344"},
        {"elementIdentifier": "consignee_ebwoid", "elementValue": "EU.ebwoid.11789463"},
        {"elementIdentifier": "expiry_date", "elementValue": "2026-07-30T00:00:00Z"},
        {"elementIdentifier": "issuance_date", "elementValue": "2026-06-30T10:25:00Z"}
      ]     
    }    
}
```

## 3.2 SD-JWT VC-based encoding

 SD-JWT is out of scope for this rulebook, as offline proximity is required.

# 4 Attestation usage 
## 4.1. Issuance process
The eCMR attestation is issued and managed by an eCMR platform throughout the transport lifecycle. 
- The platform creates the initial eCMR and generates a unique identifier linked to the consignment. 
- Pickup and delivery activities are initiated and managed through the platform using Business Wallet authentication. 
- The eCMR platform issues updated eCMR version. 
- The eCMR platform revoke the older eCMR Attestation when a new version is issued.

## 4.2 Relying Party process (MVP+)
The relying party, typically a competent authority, receives the eCMR attestation presented through the Business Wallet.
Where available, the relying party extracts the eFTI UIL from the eCMR attestation. 
The UIL is used to submit a query through the national eFTI Gate to locate the authoritative dataset. 
In offline situations, verification may rely solely on the wallet-based presentation

# 5 Trust anchors

The trust model relies on:

- Trusted eCMR platform issuers;
- Business Wallet identities;
- ebwoid-based legal entity identification;
- Cryptographically signed attestations. 

Each participating organisation SHALL possess a Business Wallet containing an ebwoid identifying both its legal and technical identity. 

The trust chain SHALL enable verification of:

1. The attestation signature.
2. The issuing eCMR platform.
3. The identified legal entity.
4. The associated trust anchor. 

For EAAs, trust is established through a cryptographic chain anchored in the Electronic Business Wallet Owner Identity Document (EBWOID). The EBWOID SHALL be included in the header of every EAA. During EBWOID issuance, the EBWOID provider verifies that the public key contained in the EBWOID is owned by the Electronic Business Wallet (EBW) owner.

The Relying Party (eCMR Platform) SHALL verify the EBWOID. Upon successful verification, the Relying Party obtains:

- assurance that the EBWOID was issued by an authorized provider and is not self-issued;
- the verified identity of the issuer, including its name and EUID (or another globally unique EBW owner identifier); and
- the public key authorized to verify the EAA signature.

# 6 Revocation

A balance between security and usability must be found:
- Short-lived (24 hours) needs re-issuance / renewal by the issuer. ECMR lifecycle is much longer than one day. 
- Status List or revocation List requires internet access to retrieve trusted lists. 
Maintaining a cached copy of the trusted list and revocation information, updated regularly, may enable offline verification (MVP+).

The eCmr Platform (self-issuing entity) SHALL immediately update or revoke its EAA eCMR Attestation when a new version is issued. Nonetheless, the expiracy date SHALL always be set, especially when the eCMR is not the final one.

Note: WeBuild IETF Token Status List SHOULD be used to perform revocation checks to validate credentials.

# 7 References

| Reference | Description |
|------------|-------------|
| Regulation (EU) 2024/1183 | European Digital Identity Regulation |
| ISO/IEC 18013-5 | Mobile Driving Licence (mDoc) Standard |
| ISO 8601	| International standard for date and time representations |
| EUDI ARF | European Digital Identity Architecture Reference Framework |
| eFTI Regulation | Electronic Freight Transport Information Regulation |
| [UN/CEFACT eCMR] | Electronic Consignment Note Specification https://unece.org/trade/documents/2024/12/standards/ecmr-d24a |



