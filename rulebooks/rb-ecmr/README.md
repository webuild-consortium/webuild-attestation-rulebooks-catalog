# WE BUILD Attestation Rulebook for eCMR Attestation (mDoc)
## WORK IN PROGRESS - first commit to check github 

**Author(s):**
- Christophe DANNA, WE BUILD Consortium
- OULMAHDI, WE BUILD Consortium
- Eelco, WE BUILD Consortium
XXXXXXXXXXX  tous les gens de l'atelier ******

**Reviewer(s)**
- XXXXXXXXXXXXXXXXXXXXXXXXXXX

**Version History**

| Version | Date | Description |
|----------|----------|-------------|
| 0.1 | 17-07-2026 | Initial draft created from SC1.3 eCMR Attestation Workshop outcomes |

**Feedback: ** 
<mark style="background-color: lightyellow">Assumptions more subject to comments are hightlighted into Lightyellow.</mark> 

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
- Chapter 7 provides compliance information.

### 1.3 Key words

This document uses the capitalised key words `SHALL`, `SHOULD` and `MAY` as
specified in [RFC 2119], i.e., to indicate requirements, recommendations and
options specified in this document.

In addition, 'must' (non-capitalised) is used to indicate an external
constraint, i.e., a requirement that is not mandated by this document, but, for
instance, by an external document. The word 'can' indicates a capability,
whereas other words, such as 'will', and 'is' or 'are' are intended as
statements of fact.

## 1.4 Terminology XXXXXXXXXXXXXXXXX

This document follows terminology defined by:

- EUDI Architecture Reference Framework (ARF);
- eCMR Convention;
- eFTI Regulation;
- WE BUILD Architecture documentation.

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

The attribute `attestation_legal_category` SHALL indicate the legal classification of the attestation. This attestation type is classified as "EAA" within the EBW Wallet ecosystem, as it is typically issued by an eCRM platform and no authentic source is used.

## 2.2 Mandatory attributes
### 2.2.1 Consignment identification 

| Data Identifier |  Definition | Data Type | Example Value |
|----------------|-------------|-----------|---------------|
| consignment_identifier |  Unique identifier of the consignment* | tstr | CMR-2026-000123 |
| ecmr_platform_url |  URL of the originating eCMR platform | URI | https://platform.example.eu/ecmr/CMR-2026-000123 |

<mark style="background-color: lightyellow">* The issuing eCmr platform can freely use whatever content needed to identify the consignment and its eCMR. On purpose, already defined Id fields in UN/CEFACT Electronic Road Consignment Note (eCMR)are not used [UN/CEFACT eCMR].</mark> 


## 2.3 Optional attributes
### 2.4 eFTI information (Unique Information Link)

| Data Identifier |  Definition | Data Type | Example Value |
|----------------|-------------|-----------|---------------|
| efti_dataset_identifier | The unique ID of an eFTI CMDS, assigned by an eFTI platform | String-36 | EFTI-248811 |
| efti_platform_identifier |  The identifier of an eFTI platform | String-17 | EFTI-PLAT-45 |
| efti_gate_identifier |  The identifier of an eFTI gate | String-17 | EFTI-GATE-12 |

Note: at the present time, the naming rule for eftt platform and gate identifiers has not been defined yet by the eFTI technical guidance documents. Exemples are fictionnal.
<mark style="background-color: lightyellow">Question: should the QR Code (image of encoded UIL) be added?</mark> 

### 2.4 Human readbale eCMR
| Data Identifier |  Definition | Data Type | Example Value |
|----------------|-------------|-----------|---------------|
| embedded_ecmr_pdf |  Embedded human-readable eCMR document for offline presentation | actual pdf/a file as base64 string |    |

Note: no embedded transport dataset representation, only a human readable document 

These attributes SHALL be present when offline verification or human-readable presentation is required. Optional in MVP, mandatory in MVP+.

## 2.4 Conditional attributes
### 2.4.1 Parties identification 

| Data Identifier |  Definition | Data Type | Example Value |
|----------------|-------------|-----------|---------------|
| consignor_ebwoid |  ebwoid of the issuing organisation | String | SEBOLREG.123456789 |
| carrier_ebwoid |  ebwoid of the carrier | String | NOFOR.123456789 |
| consigner_ebwoid |  ebwoid of the consignor | String | SEBOLREG.987654321 |

<mark style="background-color: lightyellow">At least One ebwoid SHALL be included in the attestation, depending on the step reached in process.</mark> 

## 2.5 Mandatory metadata

| Data Identifier |  Definition | Data Type | Example Value |
|----------------|-------------|-----------|---------------|
| attestation_legal_category |  Legal category of the attestation | String | non-qualified-EAA |
| issuer_identifier |  Unique issuer identifier | String | WEBUILD-ECMR-PLATFORM |
| issuer_ebwoid |  ebwoid of the issuing organisation | String | EU.ebwoid.12345678 |
| trust_anchor_location |  URL of trust anchor information | URI | https://trust.webuild.eu |
| expiry_date |  Expiration date of the attestation | DateTime | 2026-07-30T00:00:00Z |
| schema_version |  Attestation schema version | String | 1.0 |
| issuance_date |  Timestamp of issuance | datetime | 2026-06-30T10:25:00Z |

## 2.6 Optional metadata

None

## 2.7 Conditional metadata

None

## 2.8 Code lists

| Field Name | Allowed Values | Meaning | Source |
|------------|----------------|---------|---------|
| attestation_legal_category | "non-qualified-EAA" | Legal classification of the attestation | EUDI Framework |
| presentation_mode | online, offline, hybrid | Verification mode | WE BUILD |
| embedded_document_type | PDF, eCMR-XML, eFTI | Embedded evidence format | WE BUILD |

## 2.9 Integrity rules (to be completed)

| Rule ID | Rule Statement |
|----------|----------------|
| IR-01 | |
| IR-02 | |
| IR-03 ||
| IR-04 ||
| IR-05 ||
| IR-06 ||

# 3 Attestation encoding

## 3.1 ISO/IEC 18013-5 compliant encoding

The eCMR Attestation SHALL be issued exclusively as an ISO/IEC 18013-5 compliant mDoc. This format supports:

- Device-to-device proximity presentation;
- Offline verification;
- Integration within the EUDI Wallet ecosystem;
- Embedded transport evidence;
- Selective disclosure mechanisms. 

docType `eu.webuild.ecmr.attestation.1`
Namespace `eu.webuild.ecmr.attestation.1`

## Attributes

| Attribute Identifier | Data type | Encoding Format |
|-----------------|----------------------|-----------------|
| attestation_legal_category | string | UTF-8 |

``` To be completed```

## Illustrative example (to be done)

```json
{
  "docType": "eu.webuild.ecmr.attestation.1",
  "namespace": "eu.webuild.ecmr.attestation.1",
  "attestation_legal_category": "non-qualified-EAA",
  "consignment_identifier": "CMR-2026-000123",
  "ecmr_platform_url": "https://platform.example.eu/ecmr/CMR-2026-000123",
  "issuer_ebwoid": "EU.ebwoid.12345678",
  "carrier_ebwoid": "EU.ebwoid.87654321",
  "consigner_ebwoid": "EU.ebwoid.11223344",
  "issuance_timestamp": "2026-06-30T10:25:00Z",
  "document_hash": "SHA256:4F2C9B...",
  "embedded_ecmr_pdf": "<binary object>"
}
```

## Selective disclosure

Selective disclosure SHOULD be supported for:

- XXXXX
- 
- eFTI XXX-related references.

Mandatory verification attributes SHALL always be available to relying parties.

# 4 Attestation usage XXXXXXXspecifies attestation usage scenarios, ISSUING  & Relying Party obligations XXXXXXXXXXXXXXX to be filled with the scenario 

The eCMR Attestation SHALL support:

- Roadside inspections;
- Cross-border transport verification;
- Compliance controls;
- Logistics interoperability services;
- Future eFTI exchange scenarios. 

The holder SHALL present the attestation through EUDI Wallet presentation protocols.

The relying party SHALL:

1. Verify the issuer signature.
2. Verify the trust chain.
3. Verify all ebwoid identifiers.
4. Verify the validity period.
5. Verify document integrity evidence.
6. Validate embedded transport evidence when present. 

The attestation SHALL support:

- Device-to-device presentation;
- Device-to-verifier presentation;
- Offline inspection scenarios. 

The attestation SHOULD be non-device-bound to ensure operational flexibility for transport activities.

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

Trust anchor distribution mechanisms remain subject to final validation by the WE BUILD Architecture Group. 

# 6 Revocation

The preferred operational model is based on short-lived attestations. 

For longer validity periods, implementations SHOULD support:

- Attestation Status Lists;
- Revocation List mechanisms defined by future EUDI technical specifications.


# 7 Compliance

This rulebook aligns with:

- Regulation (EU) 2024/1183;
- EUDI Architecture Reference Framework;
- WE BUILD Architecture principles;
- eCMR operational requirements;
- eFTI interoperability objectives. 

The attestation provides:

- Trusted business identification;
- Legal and technical identity binding;
- Online and offline presentation capabilities;
- Human-readable transport documentation support;
- Integrity protection for transport data. 

# 8 References

| Reference | Description |
|------------|-------------|
| Regulation (EU) 2024/1183 | European Digital Identity Regulation |
| ISO/IEC 18013-5 | Mobile Driving Licence (mDoc) Standard |
| EUDI ARF | European Digital Identity Architecture Reference Framework |
| eFTI Regulation | Electronic Freight Transport Information Regulation |
| SD-JWT VC | Verifiable Credentials Specification |
| W3C VCDM | Verifiable Credentials Data Model |
| WE BUILD SC1.3 Workshop | eCMR Attestation Workshop Outcomes |
| WE BUILD Architecture ADR | QEAA Attestation and QERD Documents |
| [UN/CEFACT eCMR] | Electronic Consignment Note Specification https://unece.org/trade/documents/2024/12/standards/ecmr-d24a |

