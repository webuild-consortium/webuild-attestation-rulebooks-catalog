# WE BUILD Attestation Rulebook for attestations of type *Membership Credential*

*This WE BUILD v1 Rulebook specifies the Membership Credential used in the WE BUILD Supply Chain 2
(SC2) MVP scenario "seamless onboarding" piloted by the Data Sharing Initiatives (DSI) DjustConnect
(ILVO), DADS (ITC) and Tritom (Dataspace Europe), and the common agriculture dataspace "Agri-X".*

* Author(s):
    * Ingo Wolf, [Spherity GmbH](https://www.spherity.com)
    * Martin Domajnko, [Lutra Labs d.o.o.](https://lutralabs.io)

| Version | Date       | Description                                                                         |
|---------|------------|-------------------------------------------------------------------------------------|
| 01      | 25.06.2026 | Initial Rulebook derived from the MVP Membership credential attestation description. |
| 02      | 26.08.2026 | consolidated draft                                                                  |
| 03      | 26.08.2026 | BREAKING: `role`/`roles` values changed from bare strings to absolute URIs under `https://w3id.org/ebwv/roles#`; `memberOf` values changed from bare strings to absolute URIs minted per-DSI under the DSI's own domain. See Section 2.8. |
| 04      | 27.08.2026 | `onboardedBy` gains `memberIdentifier`, the platform-local identifier of the **holder** (Section 2.2.2/2.2.4), bridging the EBWOID/EUID to legacy identifiers; code list 2.8 corrected accordingly. Chapter 3 (SD-JWT VC and W3C VCDM) realigned with the Chapter 2 attribute names (`member`, `role`, `termsOfUse`) after drift; holder `legalName` folded into `member`. Disclosability rules made consistent (Section 3.2.2). Use of the credential in data-sharing transactions marked out of scope for the pilot. |
| 05      | 01.09.2026 | Editorial: "SC2" expanded to "Supply Chain 2 (SC2)" on first use; feedback channel now points to the Supply Chain 2 contact points. |
| 06      | 01.09.2026 | BREAKING, aligns the Rulebook with the published European Business Wallet Vocabulary and its JSON-LD context. Reverts entry 03: `role` and `memberOf` values return from absolute URIs to plain terms, since both properties are typed `xsd:string` in the vocabulary and the `https://w3id.org/ebwv/roles#` namespace does not exist — role individuals are published under `https://w3id.org/ebwv#`. Namespace-prefix trust withdrawn accordingly (Section 5), IR-05 added. `onboardedBy.memberIdentifier` refactored to credential-level `evidence` (Section 2.6), recording the identification means used to prove the holder's identity during initial onboarding; `onboardedBy` now describes the onboarding platform only. Identifiers adopt the vocabulary's typed-literal pattern; the Identifier object of entry 04 is withdrawn and `member` uses `legalIdentifier`. Cardinality in compacted and expanded JSON-LD documented (Section 3.3.1). New Section 3.3.2 records the type declarations required for expansion, after a round-trip through a JSON-LD processor showed that the previous credential-level `type` of `Membership` caused `member`, `memberOf`, `role` and `onboardedBy` to be dropped silently; `Membership` now types the credential subject. |
| 07      | 02.09.2026 | The credential subject gains the optional `holderIdentifier` attribute (Section 2.3), derived from the source attestation description (*MVP Membership credential — attestation description*, v1.0, section 1.4.1). It carries the identifier by which the onboarding platform refers to the holder, and is populated only where the value differs from `member.legalIdentifier`. It sits alongside `memberOf` on the credential subject rather than inside `onboardedBy`, because it describes the holder and not the onboarding platform; `onboardedBy` now identifies the onboarding party only. No companion `holderIdentifierType` is defined: the scheme follows from the onboarding platform named in `onboardedBy`, and where it must be stated explicitly the identifier is carried as `evidence`, whose scheme is machine-readable. IR-06 and IR-07 added. The attribute has no property term in the published vocabulary context, so it is recorded among the known expansion gaps in Section 3.3.2. The credential-level `type` now includes `ElectronicAttestationOfAttributes`, which is what brings `attestationLegalCategory` into scope; that attribute previously dropped on expansion and now resolves to the `EAA` individual, closing the gap recorded in entry 06. `attestation_legal_category` moved from the Membership attribute table (Section 2.2) to mandatory metadata (Section 2.5), since it qualifies the attestation rather than the member and is carried at credential level. |
| 08      | 02.09.2026 | BREAKING, follows the European Business Wallet Vocabulary context republished on 2 September 2026. That context retypes `role` and `memberOf` from `xsd:string` to `@id`, so both now carry **absolute IRIs** and expand to node references; the plain terms introduced in entry 06 are withdrawn. Role values are the `DataSpaceRole` individuals under `https://w3id.org/ebwv#`. Verified by expansion: a relative value such as `DataRightsHolder` resolves against the document base, yielding a different IRI for every location a credential is served from. Namespace-prefix trust for `role` is reinstated (Section 5) and a DSI may now mint its own role IRIs without a vocabulary or Rulebook change. The same context adds `holderIdentifier` to the `Membership` type-scoped context, closing the last expansion gap from entry 07; Section 3.3.2 now records full coverage. IR-05 restated in terms of IRI matching. |

**Feedback:**
* Main feedback channel: [GitHub issues](https://github.com/webuild-consortium/eudi-wallet-rulebooks-and-schemas/issues)
* Alternative: contact Supply Chain 2 contact points in WE BUILD.

## 1 Introduction

### 1.1 Document scope and purpose

The Membership Credential expresses that its holder is a member of a specific Data Sharing
Initiative (DSI) or dataspace, which roles the holder has within that DSI or dataspace, and to
which dataspace governance rulebook the holder has conformed. It exists to enable *seamless
onboarding*: common information already presented in a previous onboarding flow is trusted and not
requested again when the holder onboards into a further DSI or the common dataspace.

In plain language, the credential combines all necessary information about the dataspace or DSI
membership into a single attestation held in an EU Business Wallet (EBW), independent of any
dataspace-specific connector technology.

* **Real-world fact expressed:** membership of a DSI or dataspace, the roles held within it
  (e.g. Data Rights Holder, Data Provider, Data Consumer, Operator, Onboarding Service Provider),
  and acceptance of the dataspace governance rulebook.
* **Issuers:** trusted issuers / onboarding service providers (the participating DSIs, or another
  technology partner acting as onboarding service provider). Agri-X is envisaged as a federation of
  DSIs; participants join Agri-X via a DSI or directly via a trusted issuer.
* **Holders:** organisations (legal persons) participating in a DSI or dataspace. The MVP scenario
  is limited to legal persons.
* **Relying parties:** DSI / dataspace platforms and participants that verify membership and roles
  during onboarding. Use during data-sharing transactions is a *potential* future application and
  is **out of scope for this pilot**: a data-transfer flow would likely require the Membership
  Credential to be transformed into a connector-native credential (for instance an EDC / dataspace
  protocol participant credential) rather than presented directly.
* **Use case:** WE BUILD SC2 "seamless onboarding" piloted by DjustConnect (ILVO), DADS (ITC) and
  Tritom (Dataspace Europe), targeting the common agriculture dataspace "Agri-X".
* **Source document:** *MVP Membership credential — attestation description*.

The schema is designed to be re-usable and interoperable with other dataspaces. It is aligned with
the membership credential used within Catena-X; attributes that must remain interoperable with such
operational dataspaces are marked as dataspace-specific (DS-specific) terminology that SHALL NOT be
renamed.

### 1.2 Document structure

* Chapter 2, which describes the attestation attributes and metadata in an
  encoding-independent manner.
* Chapter 3, which specifies how the attestation
  attributes and metadata are encoded in case the attestation complies with [ISO/IEC
  18013-5] and/or [SD-JWT VC] and/or [W3C VCDM v2.0]. Each encoding SHALL be specified in a separate section, or even in a separate chapter.
* Chapter 4, which specifies attestation usage.
* Chapter 5, which defines how trust anchors for attestation verification can be obtained.
* Chapter 6, which defines attestation revocation mechanisms.
* Chapter 7, which provides compliance information.

### 1.3 Key words

This document uses the capitalised key words 'SHALL', 'SHOULD' and 'MAY' as
specified in [RFC 2119], i.e., to indicate requirements, recommendations and
options specified in this document.

In addition, 'must' (non-capitalised) is used to indicate an external
constraint, i.e., a requirement that is not mandated by this document, but, for
instance, by an external document. The word 'can' indicates a capability,
whereas other words, such as 'will', and 'is' or 'are' are intended as
statements of fact.

### 1.4 Terminology

This document uses the terminology specified in Annex 1 of the ARF.

## 2 Attestation attributes and metadata

### Chapter overview and requirements

*This chapter is used for defining all attributes that an
attestation of the defined type may contain. In this section
the attributes SHALL be defined in an encoding-independent manner (see ARB_06 in [Topic 12]).
Each attribute can be mandatory, optional, or conditional
and this SHALL be specified in the corresponding section (see ARB_09 in [Topic 12]).*

*When attributes are defined, referring to attributes that
already exist in a catalogue of attestation attributes
SHOULD be considered (see ARB_07 in [Topic 12]).*

*Where use-case documentation or an attestation description already defines attribute meanings,
logical models, code lists, or integrity constraints, authors SHOULD align terminology with those
sources and may copy and refine that material for this Rulebook.*

*[Topic 12] of Annex 2 of the ARF defines the following High-Level Requirements with
respect to the Attestation Rulebooks:*

**Requirements for QEAA**

* An attribute as meant in Annex V point a)  of the [European Digital Identity Regulation]
  SHALL be included (see ARB_11 in [Topic 12]). See also section 2.1.
* One or more attributes or metadata representing the set of data meant in Annex
  V point b) of the [European Digital Identity Regulation] SHALL be included (see ARB_13 in [Topic 12])
* One or more attributes representing the set of data meant in Annex V point c)  
  of the [European Digital Identity Regulation] SHALL be included (see ARB_16 in [Topic 12]).
* One or more attributes or metadata representing the set of data meant in Annex V point e)
  of the [European Digital Identity Regulation] SHALL be included (see ARB_18 in [Topic 12]).
* One or more attributes or metadata representing the location meant in Annex V point h)
  of the [European Digital Identity Regulation] SHALL be included. This location SHALL
  indicate at least the URL at which a machine-readable version of the trust anchor to be
  used for verifying the QEAA can be found or looked up (see ARB_20 in [Topic 12]).

**Requirements for PuB-EAA**

* An attribute as meant in  Annex VII point a) of the [European Digital Identity Regulation]
  SHALL be included (see ARB_11 in [Topic 12]). See also section 2.1.
* One or more attributes or metadata representing the set of data meant in Annex
  VII point b) of the [European Digital Identity Regulation] SHALL be included (see ARB_14 in [Topic 12]).
* One or more attributes representing the set of data meant in Annex VII point c)
  of the [European Digital Identity Regulation] SHALL be included (see ARB_16 in [Topic 12]).
* One or more attributes or metadata representing the set of data meant in Annex VII point e)
  of the [European Digital Identity Regulation] SHALL be included (see ARB_18 in [Topic 12]).
* one or more attributes or metadata representing the location meant in Annex VII point h)
  of the [European Digital Identity Regulation] SHALL be included. This location SHALL
  indicate at least the URL at which a machine-readable version of the qualified
  certificate that signed the PuB-EAA can be found or looked up. (see ARB_20 in [Topic 12])

**Requirements for non-qualified EAA**

* An attribute indicating that the attestation is an EAA should be included (see ARB_12 in [Topic 12]).
  See also section 2.1.
* One or more attributes or metadata representing the set of data meant in Annex
  V point b) of the [European Digital Identity Regulation] SHALL be included (see ARB_15 in [Topic 12]).
* One or more attributes representing the set of data meant in Annex V point c) of the
  [European Digital Identity Regulation] SHOULD be included (see ARB_17 in [Topic 12])
* One or more attributes representing the set of data meant in Annex V point e) of
  the [European Digital Identity Regulation] SHOULD be defined (see ARB_19 in [Topic 12]).
* One or more attributes or metadata representing the location at which a machine-readable
  version of the trust anchor to be used for verifying the EAA can be found or
  looked up SHOULD be defined. What this location indicates precisely is dependent
  on the nature of the mechanism used for distributing trust anchors, detailed in section
  5 (see ARB_21 in [Topic 12])

### 2.1 Introduction

The Membership Credential is a **non-qualified EAA**. This document defines the attribute
[attestationLegalCategory](https://w3id.org/ebwv#attestationLegalCategory) which SHALL have the value `EAA`.
It qualifies the attestation as a whole rather than the member, and is therefore carried at
credential level, outside the credential subject; in the W3C VCDM encoding the credential-level
`type` SHALL include
[ElectronicAttestationOfAttributes](https://w3id.org/ebwv#ElectronicAttestationOfAttributes), which
is what defines the attribute. See Section 3.3.2.

The credential describes the member (the `CredentialSubject`) together with the dataspace
governance rulebook the member conforms to (`termsOfUse`), the roles the member has within the
DSI or dataspace (`role`), and the platform through which the member was onboarded
(`onboardedBy`). Separately, at credential level, `evidence` records the identification means by
which the holder's identity was proven during the initial onboarding process.

**Logical model.** The Membership Credential is structured as follows:

* The credential subject is identified by `id` (a UUID, may change) and `member`, an object of type
  [EconomicOperator](https://w3id.org/ebwv#EconomicOperator) carrying the stable identifier of the
  holder in `legalIdentifier`; for the MVP this re-uses the EUID from the EUBWOID of that economic
  operator.
* `memberOf` names the DSI or dataspace the membership is for.
* `role` is an array of roles the holder has within that DSI or dataspace. The membership and its
  set of roles share the same lifecycle: a change of roles requires re-issuance of the credential.
* `termsOfUse` is an object of type [GovernanceRulebook](https://w3id.org/ebwv#GovernanceRulebook) referencing the accepted dataspace governance rulebook (URL,
  version, SHA-256 hash, and acceptance datetime).
* `holderIdentifier` optionally carries the identifier by which the onboarding platform refers to
  the holder, where that differs from `member.legalIdentifier`. It sits alongside `memberOf` on the
  credential subject, because it describes the holder rather than the platform.
* `onboardedBy` is an object of type [Platform](https://w3id.org/ebwv#Platform) identifying the
  onboarding party: the platform's identifier (`platformId`) and commercial `name`, and the
  `operator` — the economic operator hosting and running the platform.
* `evidence` records the identification means used to prove the holder's identity during the
  initial onboarding process, for example the VAT identifier presented in a paper-based onboarding
  flow. It is credential metadata about the issuance, not an attribute of the subject, and is
  therefore carried at credential level rather than inside the credential subject (Section 2.6).

Note that `evidence` describes how **the holder** was identified, whereas `onboardedBy` describes
the platform and the organisation that performed the onboarding. Keeping the two apart is
deliberate: an identifier recorded as evidence belongs to the holder, never to the platform
operator. As a side effect, `evidence` also bridges the EU-level identifier in
`member.legalIdentifier` to a legacy or platform-local identifier of the same holder, which may not
be recognisable or interoperable outside the onboarding platform; see IR-03 and IR-04 for the
limits on that use.

Standard credential metadata (issuer, issuance time, expiry, status) follows from the chosen VC
format and is documented in Chapter 3 rather than as attributes here. Each Membership Credential
has its own unique identifier.

**DS-specific terminology.** Attributes marked `(*)` below (`id`, `member`, `memberOf`) keep their
names for cross-dataspace interoperability (e.g. with Catena-X) and SHALL NOT be renamed. For
extensibility purposes the JSON Schema definition allows additional properties in the `onboardedBy`
data type definition.

*Subsections 2.2 - 2.7 define the attributes and metadata in an encoding-independent manner. Code
lists are in Section 2.8 and integrity rules in Section 2.9. The structured objects `termsOfUse`
and `onboardedBy` are defined as sub-tables in Section 2.2; `evidence` is defined in Section 2.6.*

### 2.2 Mandatory attributes of object [Membership](https://w3id.org/ebwv#Membership)

| **Data Identifier**          | **Semantic Reference**                                                     | **Definition**                                                                                                                                                                                                                                                                | **Data type**                                                              | **Example value**                     |
|------------------------------|----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|---------------------------------------|
| `id` (*)                     | @id                                                                        | UUID of the credential subject. May change, in contrast to `member.legalIdentifier` which is a persistent, stable identifier. Name kept for cross-dataspace interoperability.                                                                                            | UUID                                                                       | `did:web:example.com:participant:123` |
| `member` (*)                 | [member](https://w3id.org/ebwv#member)                                     | The holder, as an economic operator carrying the stable identifier that uniquely identifies it. For the MVP this re-uses the EUID (part of the EUBWOID); scope is legal persons only. Name kept for cross-dataspace interoperability. Object, see table below.                 | [EconomicOperator](https://w3id.org/ebwv#EconomicOperator)                 | *see 2.2.3*                           |
| `memberOf` (*)               | [memberOf](https://w3id.org/ebwv#memberOf)                                 | The DSI or dataspace the holder is a member of. Within a DSI/DS all issued membership credentials use the same value. The value is an absolute IRI registered in code list 2.8, matched by exact IRI comparison. Name kept for cross-dataspace interoperability.               | URL                                                                        | `https://agri-x.eu`                              |
| `role`                       | [role](https://w3id.org/ebwv#role)                                         | The roles the holder has within the DSI or dataspace. A member may have multiple roles; the set of roles shares the membership lifecycle. Each value is an absolute IRI from code list 2.8. See also Section 3.3.1 on cardinality.        | array of IRIs                                                              | `["https://w3id.org/ebwv#DataProvider"]` |
| `termsOfUse`                 | [termsOfUse](https://www.w3.org/2018/credentials#termsOfUse)               | Dataspace governance rulebook information. Object, see table below.                                                                                                                                                                                                           | [GovernanceRulebook](https://w3id.org/ebwv#GovernanceRulebook)             | *see 2.2.1*                           |
| `onboardedBy`                | [onboardedBy](https://w3id.org/ebwv#onboardedBy)                           | The platform through which the holder was onboarded into the DSI or dataspace: the platform itself and the economic operator hosting it. Object, see table below.                                                                                                             | [Platform](https://w3id.org/ebwv#Platform)                                 | *see 2.2.2*                           |

#### 2.2.1 `termsOfUse` object of type [GovernanceRulebook](https://w3id.org/ebwv#GovernanceRulebook)

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Optionality** | **Example value** |
|---------------------|------------------------|----------------|---------------|-----------------|-------------------|
| `url`               | N/A                    | Reference to the online dataspace governance rulebook for the given DSI or DS. | string (URI) | M | `https://agri-x.eu/rulebook` |
| `version`           | N/A                    | Version of the online rulebook at the time of acceptance. | string | M | `1.2` |
| `hash`              | N/A                    | SHA-256 hash of the rulebook, for quick comparison. | string (SHA-256 hash) | M | `9f86d081...` |
| `acceptedAt`        | N/A                    | Datetime when the rulebook was accepted. May differ from issuance time in an outbound flow where a credential is issued to an existing member based on a previously completed onboarding flow. | datetime | O | `2026-06-01T10:00:00Z` |

#### 2.2.2 `onboardedBy` object of type [Platform](https://w3id.org/ebwv#Platform)

This object identifies **the onboarding party**: which platform performed the onboarding and which
legal entity hosts it. Example reading: *"DjustConnect, a platform hosted by ILVO, onboarded farmer
XYZ."*

Identifiers of the **holder** are not carried here. The identifier by which the onboarding platform
refers to the holder is `holderIdentifier` at credential-subject level (Section 2.3), and the
identification means used to prove the holder's identity is `evidence` at credential level
(Section 2.6). The only identifier in this object, `operator.identifier`, belongs to the
organisation hosting the platform.

| **Data Identifier** | **Semantic Reference**                                     | **Definition**                                                             | **Data type**                                              | **Optionality** | **Example value**         |
|---------------------|------------------------------------------------------------|------------------------------------------------------------------------------|------------------------------------------------------------|-----------------|---------------------------|
| `platformId`          | [platformId](https://w3id.org/ebwv#platformId)             | DID identifying the platform through which the holder was onboarded.         | string (URI)                                               | M               | `did:web:djustconnect.be` |
| `name`                | [name](https://w3id.org/ebwv#name)                         | Commercial name of the platform (DSI or onboarding partner).                 | string                                                     | M               | `DjustConnect`            |
| `operator`            | [operator](https://w3id.org/ebwv#operator)                 | The economic operator hosting and running the platform. Object, see 2.2.3.   | [EconomicOperator](https://w3id.org/ebwv#EconomicOperator) | M               | *see 2.2.3*               |

#### 2.2.3 [EconomicOperator](https://w3id.org/ebwv#EconomicOperator) object

Used by `member` (the holder) and by `onboardedBy.operator` (the organisation hosting the
onboarding platform). Identifier values follow the European Business Wallet Vocabulary pattern for
identifiers: a typed literal whose datatype is the identifier scheme. See Section 2.8.

| **Data Identifier** | **Semantic Reference**                                 | **Definition**                                                                                                                                                                                        | **Data type**    | **Optionality** | **Example value**                                    |
|---------------------|--------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|-----------------|------------------------------------------------------|
| `legalName`         | [legalName](https://w3id.org/ebwv#legalName)           | Official legal name of the economic operator. For `member`, see integrity rule IR-02.                                                                                                                 | string           | M               | `Farm Example BV`                                    |
| `legalIdentifier`   | [legalIdentifier](https://w3id.org/ebwv#legalIdentifier) | The stable, EU-level identifier of the economic operator. Used by `member`: for the MVP the EUID taken from the holder's EUBWOID. Scheme SHALL be `Euid` or `PublicSectorBodyId` (range of the property). | typed literal    | M for `member`  | `{"@type":"Euid","@value":"BEEUID0123456789"}`       |
| `identifier`        | [identifier](https://w3id.org/ebwv#identifier)         | A further identifier of the economic operator, in any scheme from code list 2.8. Used by `onboardedBy.operator` to identify the organisation hosting the platform.                                     | typed literal    | M for `operator`| `{"@type":"VatId","@value":"BE0848278827"}`          |

### 2.3 Optional attributes

This attribute belongs to the [Membership](https://w3id.org/ebwv#Membership) credential subject,
alongside the mandatory attributes of Section 2.2. It describes **the holder**, not the onboarding
platform, and is optional: an issuer populates it only where the onboarding platform holds an
identifier for the holder other than the one in `member.legalIdentifier`.

| **Data Identifier**    | **Semantic Reference**                                                               | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------------------------------------------------------------------|----------------|---------------|-------------------|
| `holderIdentifier`     | [holderIdentifier](https://w3id.org/ebwv#holderIdentifier) | Stable and unique identifier used within the DSI or dataspace to refer to the holder. To be specified only where it differs from `member.legalIdentifier`. Supports platforms whose own identifier for a data partner is not recognisable or interoperable at EU level. See IR-06, IR-07. | string | `BE0123456789` |

The scheme of the value is not stated by a separate attribute. It follows from the onboarding
platform, which `onboardedBy` identifies (Section 2.2.2): a Relying Party that knows the platform
knows which identifier that platform issues. Where the scheme has to be stated explicitly and
machine-readably, `evidence` carries it as the datatype of a typed literal (Section 2.6.1).

The holder's official name is carried by `member.legalName` (Section 2.2.3).

*Relationship to `evidence` (Section 2.6). The two are distinct and may both be present.
`holderIdentifier` is the identifier the onboarding platform uses operationally to refer to the
holder — the value that appears in that platform's own APIs and records. `evidence` records the
identification means by which the holder's identity was **proven** at onboarding. In practice a
platform will often use the same value for both, for instance a VAT identifier that was both
checked during onboarding and used as the platform's reference thereafter. Where an issuer has only
one of the two facts, it SHOULD populate only the corresponding attribute rather than duplicating
the value into both.*

### 2.5 Mandatory metadata

*Standard VC metadata (issuer, issuance time, expiry, status, credential `id`) is provided by the
chosen VC format and specified per encoding in Chapter 3. This Rulebook defines one additional
mandatory metadata attribute.*

| **Data Identifier**          | **Semantic Reference**                                                     | **Definition**                                                                                                                                                                                                                                             | **Data type**                                                              | **Example value**                |
|------------------------------|----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|----------------------------------|
| `attestation_legal_category` | [attestationLegalCategory](https://w3id.org/ebwv#attestationLegalCategory) | Indication that the attestation is a non-qualified EAA (per ARB_12). Qualifies the attestation as a whole, not the member, and is therefore carried at credential level rather than in the credential subject. SHALL be `EAA`. See Sections 2.1 and 3.3.2. | [AttestationLegalCategory](https://w3id.org/ebwv#AttestationLegalCategory) | [EAA](https://w3id.org/ebwv#EAA) |

### 2.6 Optional metadata

| **Data Identifier** | **Semantic Reference**                                            | **Definition**                                                                                                                                                                                          | **Data type**      | **Example value** |
|---------------------|-------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|-------------------|
| `evidence`          | [evidence](https://www.w3.org/2018/credentials#evidence)          | The identification means used to prove the identity of the holder during the initial onboarding process. Metadata about the issuance, carried at credential level. Object or array of objects, see 2.6.1. | array of objects   | *see 2.6.1*       |

#### 2.6.1 `evidence` attribute

Each `evidence` entry records one identification means presented by, or verified for, the holder
during the initial onboarding process — for example the VAT identifier checked in a paper-based
onboarding flow. `evidence` is optional; where the onboarding platform holds such a record, the
issuer SHOULD include it.

| **Data Identifier** | **Semantic Reference**                         | **Definition**                                                                                                                                                                            | **Data type**  | **Optionality** | **Example value**                            |
|---------------------|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|-----------------|----------------------------------------------|
| `type`              | @type                                          | The evidence entry describes the holder as an economic operator identified by the means used at onboarding. SHALL be `EconomicOperator`; see Section 3.3.2 for why this declaration is required. | class name     | M in W3C VCDM; omitted in SD-JWT VC | `EconomicOperator`                          |
| `identifier`        | [identifier](https://w3id.org/ebwv#identifier) | The identification means: the identifier by which the holder's identity was proven, as a typed literal whose datatype is the identifier scheme. Where no scheme from code list 2.8 applies, an untyped string. | typed literal  | M               | `{"@type":"VatId","@value":"BE0123456789"}` |

`evidence` describes the **holder**. It SHALL NOT be used to carry an identifier of the onboarding
platform or of its operator; those belong in `onboardedBy` (Section 2.2.2). See IR-03 and IR-04.


### 2.7 Conditional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------|--------------|--------------|--------------|
| N/A | N/A | N/A | N/A | N/A |

### 2.8 Code lists

The following code lists apply to attributes defined in Section 2. Lists are kept fit-for-pilot:
they cover the minimal set needed by the three participating DSIs and are not exhaustive.

**`memberOf`** — fixes the DSI or dataspace the holder is a member of. The value is agreed at the
governance level of the DSI or dataspace itself and registered in the code list below, as a URL
under that DSI's or dataspace's own domain. Uniqueness therefore rests on domain ownership, and two
DSIs cannot collide by independently choosing the same label.

The [memberOf](https://w3id.org/ebwv#memberOf) property is typed `@id` in the European Business
Wallet Vocabulary, so the value is an **absolute IRI** and expands to a node reference,
`{"@id": "https://agri-x.eu"}`. A Relying Party matches it by exact IRI comparison. The value need
not dereference to anything, and a Relying Party SHALL NOT depend on it resolving. A relative value
SHALL NOT be used: it would be resolved against the document base, so the same credential would
yield different IRIs depending on where it was retrieved from. A new DSI or dataspace SHALL
register its IRI in this code list before issuing.

| **Field name** | **Value** | **Meaning** | **Source / vocabulary** | 
|----------------|--------------------|-------------|--------------------------|
| `memberOf` | `https://agri-x.eu` | The common agriculture dataspace (federation level). | WE BUILD SC2 use case | 
| `memberOf` | `https://dih-agrifood.com/` | DSI operated by ITC. | WE BUILD SC2 use case | 
| `memberOf` | `https://djustconnect.be` | DSI operated by ILVO. | WE BUILD SC2 use case | 
| `memberOf` | `https://www.dataspace.fi/` | DSI operated by DataSpace Europe Oy. | WE BUILD SC2 use case | 

**`role`** — roles a member can have. A member may have multiple roles in one credential. Based on
the common roles agreed across the piloting DSIs, treating Agri-X as a federation of DSIs.

The [role](https://w3id.org/ebwv#role) property is typed `@id` in the European Business Wallet
Vocabulary, so each value is an **absolute IRI** and expands to a node reference. The values below
are the `DataSpaceRole` individuals published in that vocabulary, under the
`https://w3id.org/ebwv#` namespace. A relative value such as `DataRightsHolder` SHALL NOT be used:
it would be resolved against the document base, so the same credential would yield different role
IRIs depending on where it was retrieved from.

| **Field name** | **Value (absolute IRI)** | **Meaning** | **Source / vocabulary** |
|-----------|--------------------|-------------|--------------------------|
| `role` | `https://w3id.org/ebwv#DataRightsHolder` | Owns the rights to the data (e.g. farmers) and can consent to data being shared from a data provider to a data consumer. | WE BUILD SC2 use case |
| `role` | `https://w3id.org/ebwv#DataProvider` | Partner that enables sharing data, e.g. via an API. | WE BUILD SC2 use case |
| `role` | `https://w3id.org/ebwv#DataConsumer` | Partner that wants to use data, e.g. by calling an API. | WE BUILD SC2 use case |
| `role` | `https://w3id.org/ebwv#Operator` | Partner providing DSSC building-block services (identity management, consent management, logging, …). | WE BUILD SC2 use case (custom role part of DADS) |
| `role` | `https://w3id.org/ebwv#OnboardingServiceProvider` | Partner that onboards members into Agri-X; may be a DSI or another technology partner. | WE BUILD SC2 use case (role part of Catena-X) |

Because values are IRIs, a DSI MAY mint an additional role under a namespace it owns without any
change to this Rulebook, to the JSON Schema, or to the vocabulary context, and a Relying Party MAY
trust roles by namespace prefix rather than enumerating each value. Roles minted outside
`https://w3id.org/ebwv#` are governed by the minting DSI's own trust framework; see Section 5. New
roles intended for common use across the piloting DSIs SHOULD still be published as `DataSpaceRole`
individuals by the WE BUILD Semantics work group and registered here.

**Identifier schemes** — the datatype of an identifier typed literal, wherever one appears:
`member.legalIdentifier`, `onboardedBy.operator.identifier` and `evidence.identifier`. The
European Business Wallet Vocabulary publishes these as named individuals used as datatypes, in the
pattern `{"@type": "VatId", "@value": "…"}`.

| **Field name** | **Scheme** | **Meaning** | **Source / vocabulary** | **Notes** |
|-----------------------------------------|--------------------|-------------|--------------------------|---------------------------|
| `@type` | `Euid` | The unique identifier attributed in accordance with Article 9 of EBW, taken from the holder's EUBWOID. The expected scheme of `member.legalIdentifier` in the MVP. | [European Business Wallet Vocabulary v0.1], `rb-ebwoid` | In range of `legalIdentifier` |
| `@type` | `PublicSectorBodyId` | Identifier of a public sector body. | [European Business Wallet Vocabulary v0.1] | In range of `legalIdentifier` |
| `@type` | `VatId` | VAT identifier. Used by DjustConnect and Tritom as an identification means during onboarding. | [European Business Wallet Vocabulary v0.1] | |
| `@type` | `Lei`, `Eori`, `Tin`, `Iban`, `Bic`, `PeppolId`, `GlobalLocationNumber`, `ClearingNumber`, `Excise` | Further schemes published by the vocabulary, available where applicable. | [European Business Wallet Vocabulary v0.1] | Not used in the MVP |

*Not every identification means in the pilot has a published scheme. The KMG-MID used by the DADS
platform (unique farm id issued by the Slovenian Ministry of Agriculture) and any purely
platform-specific identifier have no individual in the vocabulary. Until one is published, such a
value SHALL be carried as an untyped string — `"identifier": "1234567"` — which is valid and
expands correctly but does not record the scheme. Publishing `KmgMid`, a generic `PlatformSpecific`
scheme, and an `OnboardingEvidence` class is the recommended vocabulary addition.*

*No code list applies to `holderIdentifier` (Section 2.3). Its scheme is not stated by a separate
attribute: it follows from the onboarding platform identified by `onboardedBy`. Where the scheme
has to be stated explicitly, the identifier is carried as `evidence` instead, using the schemes in
the table above.*

A common code list distinguishing Legal Person from Natural Person identifiers is being prepared by
the WE BUILD Semantics work group. It is not required for this version: the MVP scenario pilots
legal persons only. Values will be added once provided.

### 2.9 Integrity rules

| **Rule ID** | **Rule statement**                                                                                                                  | **Why it exists** | **Where enforced** | **Verifier / issuer behavior on failure** |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------|-------------------|--------------------|-------------------------------------------|
| `IR-01` | If `termsOfUse.acceptedAt` is present, its value SHALL be a datetime less than or equal to the issuance datetime of the credential. | Acceptance of the rulebook cannot logically occur after the credential was issued; supports outbound flows where acceptance happened during an earlier onboarding. | Issuer business rules, schema validation, and verifier business validation. | Issuer SHALL reject the value; verifier SHALL treat `termsOfUse` as invalid. |
| `IR-02` | If the member is a Legal Person, `member.legalName` SHOULD carry the official name as registered.                                   | Improves readability and identification of legal-person holders. | Issuer business rules. | Issuer SHOULD populate `member.legalName`; verifier MAY warn if absent. |
| `IR-03` | Every `evidence` entry SHALL record an identification means by which the identity of the holder — the legal person identified by `member` — was proven during the initial onboarding process. `evidence` SHALL NOT carry an identifier of the onboarding platform or of its operator. | Evidence is about proofing the holder. Recording the platform operator's own identifier there would misidentify the holder, which is the failure this separation exists to prevent. | Issuer business rules and verifier business validation. | Issuer SHALL NOT issue the credential; verifier SHALL treat the credential as inconsistent. |
| `IR-04` | A Relying Party SHALL NOT treat an `evidence` identifier as an authoritative identifier of the holder. `member.legalIdentifier` is authoritative. | An identification means may be a legacy or platform-local identifier with no recognition or interoperability outside the onboarding platform, and it records how proofing was done rather than who the holder is at EU level. | Verifier business validation. | Verifier MAY use the value only to reconcile the holder against its own legacy records, never as the basis of identification. |
| `IR-05` | `role` and `memberOf` values SHALL be absolute IRIs. A Relying Party SHALL match them by exact IRI comparison against code list 2.8, or for `role` by namespace prefix where its policy permits, and SHALL ignore any value it does not recognise. | A relative value is resolved against the document base, so the same credential would yield different IRIs depending on where it was retrieved from. Inferring authorisation from an unrecognised value would grant access on an unverifiable claim. | Verifier business validation. | Verifier SHALL disregard the unrecognised value and SHALL NOT treat it as conferring any role or membership. |
| `IR-06` | If `holderIdentifier` is present, it SHALL identify the same legal person as `member`, and SHALL be populated only where its value differs from `member.legalIdentifier`. | It is the same holder under the onboarding platform's own scheme, not a second subject. Repeating a value already carried by `member.legalIdentifier` adds no information and risks the two drifting apart. | Issuer business rules and verifier business validation. | Issuer SHALL NOT issue the credential; verifier SHALL treat the credential as inconsistent. |
| `IR-07` | A Relying Party SHALL NOT treat `holderIdentifier` as an authoritative identifier of the holder. `member.legalIdentifier` is authoritative. | The value is the onboarding platform's operational reference for the holder and may have no recognition or interoperability outside that platform. | Verifier business validation. | Verifier MAY use the value only to reconcile the holder against its own records, never as the basis of identification. |

# 3 Attestation encoding

## 3.1 ISO/IEC 18013-5-compliant encoding

*Not applicable for this version.* The Membership Credential is used in online onboarding flows;
no proximity / offline presentation requirement applies (ARB_02). The primary
format is W3C VCDM (JSON-LD), see Section 3.3, with SD-JWT VC considered as an additional flow
(Section 3.2). No ISO/IEC 18013-5 mdoc document type is defined.

## 3.2 SD-JWT VC-based encoding

*Considered as an additional flow (not the primary format for the MVP).* The Membership Credential
MAY additionally be piloted as an SD-JWT VC. If issued in this format, attestations
SHALL comply with the 'SD-JWT VCs' profile specified in [HAIP] (ARB_01b). This Rulebook follows
the catalog baseline of [HAIP] draft-03 and [SD-JWT VC] draft-ietf-oauth-sd-jwt-vc-09.

**Verifiable Credential Type (`vct`):** `eu.we-build.ds-membership.1`

The issued SD-JWT VC SHALL use the JOSE `typ` header value required by [SD-JWT VC]. For draft -09,
this value is `dc+sd-jwt`.

### 3.2.1 IANA-registered and standard JWT / SD-JWT VC claims

The following claims are standard JWT or SD-JWT VC claims.

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Reference / Notes** | **Disclosable** |
|---------------------|--------------------------|---------------------|-----------------------|-----------------|
| `iss` | `iss` | string (HTTPS URL) | Issuer identifier. | MUST NOT |
| `iat` | `iat` | NumericDate | Issued-at timestamp. | MUST NOT |
| `nbf` | `nbf` | NumericDate | Not-before timestamp, where used. | MUST NOT |
| `exp` | `exp` | NumericDate | Expiration timestamp. | MUST NOT |
| `jti` | `jti` | string | Unique credential instance identifier. | MUST NOT |
| `vct` | `vct` | string | SHALL be `eu.we-build.ds-membership.1`. | MUST NOT |
| `status` | `status` | JSON object | Status-list revocation information. See Section 3.2.3. | MUST NOT |
| `cnf` | `cnf` | JSON object | Holder binding confirmation claim, where used. | MUST NOT |

### 3.2.2 Private names specific to the Membership Credential

The following private claims map to the attributes defined in Chapter 2. Claim names are identical
to the Chapter 2 data identifiers; the two SHALL be kept in step.

| **Data Identifier**                       | **Attribute identifier** | **Encoding format** | **Reference / Notes** | **Optionality** | **Disclosable** |
|-------------------------------------------|--------------------------|---------------------|-----------------------|-----------------|-----------------|
| `attestationLegalCategory`                | `attestation_legal_category` | string | SHALL be `EAA`. Credential-level metadata, see Section 2.5. | M | MUST NOT |
| `id`                                      | `id` | string (DID) | DID of the credential subject. | M | MUST |
| `member`                                  | `member` | JSON object | The holder as an economic operator. See Section 2.2.3. | M | MUST |
| `member.legalName`                        | `member.legalName` | string | Official name of the holder. See IR-02. | M | MUST |
| `member.legalIdentifier`                  | `member.legalIdentifier` | JSON object | Stable, EU-level identifier of the holder. See Section 2.2.3. | M | MUST |
| `member.legalIdentifier.scheme`           | `member.legalIdentifier.scheme` | string | Identifier scheme; `Euid` in the MVP. See code list 2.8. | M | MUST |
| `member.legalIdentifier.value`            | `member.legalIdentifier.value` | string | Identifier value. For the MVP this re-uses the EUID from the EUBWOID. | M | MUST |
| `memberOf`                                | `memberOf` | string (absolute IRI, see code list 2.8) | DSI or dataspace membership value. | M | MUST |
| `holderIdentifier`                        | `holderIdentifier` | string | Identifier used within the DSI or dataspace to refer to **the holder**, where it differs from `member.legalIdentifier`. See IR-06, IR-07. | O | MUST |
| `role`                                    | `role` | array of strings (absolute IRIs, see code list 2.8) | Non-empty array of role values. | M | MUST (per element) |
| `termsOfUse`                              | `termsOfUse` | JSON object | Dataspace governance rulebook information. See Section 2.2.1. | M | MUST |
| `termsOfUse.url`                          | `termsOfUse.url` | string (URI) | Reference to the online dataspace governance rulebook. | M | MUST |
| `termsOfUse.version`                      | `termsOfUse.version` | string | Version of the online rulebook at the time of acceptance. | M | MUST |
| `termsOfUse.hash`                         | `termsOfUse.hash` | string (SHA-256 hash) | SHA-256 hash of the rulebook, represented as 64 hexadecimal characters. | M | MUST |
| `termsOfUse.acceptedAt`                   | `termsOfUse.acceptedAt` | string (date-time) | Datetime when the rulebook was accepted, where present. See IR-01. | O | MUST |
| `onboardedBy`                             | `onboardedBy` | JSON object | The platform through which the holder was onboarded. See Section 2.2.2. | M | MUST |
| `onboardedBy.platformId`                  | `onboardedBy.platformId` | string (DID) | DID identifying the onboarding platform. | M | MUST |
| `onboardedBy.name`                        | `onboardedBy.name` | string | Commercial name of the onboarding platform. | M | MUST |
| `onboardedBy.operator`                    | `onboardedBy.operator` | JSON object | Economic operator hosting the platform. See Section 2.2.3. | M | MUST |
| `onboardedBy.operator.legalName`          | `onboardedBy.operator.legalName` | string | Legal name of the organisation hosting the platform. | M | MUST |
| `onboardedBy.operator.identifier`         | `onboardedBy.operator.identifier` | JSON object | Identifier of that organisation, as `scheme` and `value`. See Section 2.2.3. | M | MUST |
| `evidence`                                | `evidence` | array of JSON objects | Identification means used to prove the holder's identity during initial onboarding. Credential-level metadata, see Section 2.6.1 and IR-03, IR-04. | O | MUST |
| `evidence[].identifier`                   | `evidence[].identifier` | JSON object | The identification means, as `scheme` and `value`. Where no scheme from code list 2.8 applies, a plain string. | M within an entry | MUST |

**Identifier representation in this encoding.** SD-JWT VC is not JSON-LD, so an identifier is
encoded as a plain JSON object with `scheme` and `value` members — for example
`{"scheme": "VatId", "value": "BE0123456789"}`. This is the SD-JWT VC form of the typed literal
described in Section 2.2.3; the W3C VCDM encoding uses the JSON-LD form
`{"@type": "VatId", "@value": "BE0123456789"}` (Section 3.3). Both carry the same scheme and value,
and the scheme is drawn from the same code list 2.8. Where no published scheme applies, the
identifier is a plain string in both encodings.

**Reading the Disclosable column.** `MUST` means the issuer SHALL make the claim selectively
disclosable; `MAY` means the issuer MAY do so; `MUST NOT` means the claim SHALL remain in the
always-visible signed payload.

Disclosability is independent of whether an attribute is mandatory in the credential. Optionality
governs what the *issuer* SHALL include when issuing; disclosability governs what the *holder* may
withhold when presenting. All subject attributes are therefore selectively disclosable, including
the mandatory ones: a Relying Party enforces the set it needs through its presentation request and
rejects a presentation that omits any of them, so disclosability costs the Relying Party nothing
while leaving the holder in control of everything beyond that set. The claims marked `MUST NOT` are
exactly those required to process or validate the credential itself, which no presentation can
omit.

**Granularity for structured attributes.** Where an attribute is an object or an array, the
following applies:

* Members of `termsOfUse`, `member`, `onboardedBy` and their nested objects SHALL be individually
  disclosable (structured/recursive selective disclosure), so that a holder can present, for
  example, `termsOfUse.hash` and `termsOfUse.version` without disclosing
  `termsOfUse.acceptedAt`, which is onboarding-date metadata a Relying Party rarely needs.
* Elements of `role` SHALL be individually disclosable, so that a holder with several roles can
  present only the role or roles the Relying Party's policy requires.
* Elements of `evidence` SHALL be individually disclosable. Evidence reveals how the holder was
  identity-proofed and carries an identifier that may correlate the holder across services, so a
  holder SHOULD be able to withhold it entirely or disclose a single entry.

Note that the granularity, not the requirement, is what depends on the data type: `MUST` applies
uniformly to `memberOf`, `role` and `termsOfUse` alike, since all three are part of the atomic set
a Relying Party uses to decide whether to accept the credential. The distinction between a string,
an array of strings and an object determines only *how* selective disclosure is applied to each.

### 3.2.3 Status Claim

The Membership Credential is revocable (Chapter 6). Therefore, an SD-JWT VC-compliant
Membership Credential SHALL include a `status` claim unless a future profile explicitly
defines a short-lived, non-revocable variant.

The `status` claim SHALL use the status-list mechanism used by the other SD-JWT VC rulebooks in
this catalog. It SHALL be a JSON object with the following members:

* `type` (string): SHALL be `"status-list"`.
* `status_list_credential` (string, URI): URI of the Status List Credential that contains the
  status bitstring.
* `status_list_index` (integer, >= 0): zero-based index into the status list bitstring for this
  credential.
* `status_purpose` (string): SHALL be `"revocation"` for this attestation.

Example:

```json
{
  "status": {
    "type": "status-list",
    "status_list_credential": "https://djustconnect.be/status/membership/1",
    "status_list_index": 42,
    "status_purpose": "revocation"
  }
}
```

### 3.2.4 Example Payload

The following non-normative example shows the JWT claim set before SD-JWT processing.

```json
{
  "iss": "https://djustconnect.be",
  "iat": 1782205200,
  "nbf": 1782205200,
  "exp": 1813741200,
  "jti": "urn:uuid:8d6f0e3c-1c2a-4e2b-9f1a-1234567890ab",
  "vct": "eu.we-build.ds-membership.1",
  "attestation_legal_category": "EAA",
  "id": "did:web:example.com:participant:123",
  "member": {
    "legalName": "Farm Example BV",
    "legalIdentifier": {
      "scheme": "Euid",
      "value": "BEEUID0123456789"
    }
  },
  "memberOf": "https://agri-x.eu",
  "holderIdentifier": "BE0123456789",
  "role": ["https://w3id.org/ebwv#DataRightsHolder", "https://w3id.org/ebwv#DataProvider"],
  "termsOfUse": {
    "url": "https://agri-x.eu/rulebook",
    "version": "1.2",
    "hash": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
    "acceptedAt": "2026-06-20T14:30:00Z"
  },
  "onboardedBy": {
    "platformId": "did:web:djustconnect.be",
    "name": "DjustConnect",
    "operator": {
      "legalName": "Instituut voor Landbouw-, Visserij- en Voedingsonderzoek (ILVO)",
      "identifier": {
        "scheme": "VatId",
        "value": "BE0848278827"
      }
    }
  },
  "evidence": [
    {
      "identifier": {
        "scheme": "VatId",
        "value": "BE0123456789"
      }
    }
  ],
  "status": {
    "type": "status-list",
    "status_list_credential": "https://djustconnect.be/status/membership/1",
    "status_list_index": 42,
    "status_purpose": "revocation"
  },
  "cnf": {
    "jwk": {
      "kty": "EC",
      "crv": "P-256",
      "x": "...",
      "y": "..."
    }
  }
}
```

Note the distinct roles of the VAT identifiers. `onboardedBy.operator.identifier` is the VAT-ID of
ILVO, the organisation hosting the DjustConnect platform. `holderIdentifier` is the VAT-ID by which
DjustConnect refers to the holder, Farm Example BV, in its own communication.
`evidence[0].identifier` is the VAT-ID that was used to prove that holder's identity during initial
onboarding. The latter two carry the same value here, as they commonly will; `member` identifies the
same legal person at EU level by its EUID.

The SD-JWT VC JSON Schema and sample payload are published at:

* `data-schemas/sd-jwt/ds-membership-sd-jwt.json`
* `data-schemas/sd-jwt/sample-data/ds-membership-sd-jwt-sample.json`

## 3.3 W3C Verifiable Credentials Data Model-based encoding

**This is the primary format for the MVP.** The Membership Credential is a non-qualified EAA, which
is the only legal category permitted to use the W3C VCDM format (ARB_01a). W3C VCDM (JSON-LD) is
chosen for semantic interoperability with the dataspaces domain and because it supports selective
disclosure via ZKP.

The credential subject carries the attributes defined in Chapter 2. Standard VCDM metadata is used
for the credential envelope: `issuer`, `validFrom`, `validUntil`, `credentialStatus`, and the
credential `id` (unique per credential).
The credential subject is modeled by the [Membership](https://w3id.org/ebwv#Membership) class 

**`evidence` is credential-level, not part of the credential subject.** The W3C VCDM v2 context
defines [evidence](https://www.w3.org/2018/credentials#evidence) inside the type-scoped context of
`VerifiableCredential`. It is therefore only defined as a member of the credential itself. Placing
it inside `credentialSubject`, whose type is `Membership`, leaves the term undefined; since the VCDM
v2 context is `@protected` and sets no `@vocab`, that is an expansion failure rather than a silent
omission. This placement is also the semantically correct one: evidence records how the issuer
verified the holder's identity, which is a statement about the issuance, not an attribute of the
subject.

`evidence` is optional, but where the onboarding platform holds a record of the identification
means used, the issuer SHOULD include it: it is what allows a Relying Party operating a legacy
system to reconcile the holder against its existing records. It SHALL NOT be confused with
`onboardedBy.operator.identifier`, which identifies the organisation hosting the platform. See
IR-03 and IR-04.


**Illustrative example (informative):**

```json
{
  "@context": [
    "https://www.w3.org/ns/credentials/v2",
    "https://w3id.org/ebwv/v0.1"
  ],
  "type": ["VerifiableCredential","ElectronicAttestationOfAttributes"],
  "id": "urn:uuid:8d6f0e3c-1c2a-4e2b-9f1a-1234567890ab",
  "issuer": "did:web:djustconnect.be",
  "validFrom": "2026-06-23T09:00:00Z",
  "validUntil": "2027-06-23T09:00:00Z",
  "attestationLegalCategory": "EAA",
  "credentialStatus": {
    "id": "https://djustconnect.be/status/membership#42",
    "type": "BitstringStatusListEntry"
  },
  "evidence": [
    {
      "type": "EconomicOperator",
      "identifier": { "@type": "VatId", "@value": "BE0123456789" }
    }
  ],
  "credentialSubject": {
    "id": "urn:uuid:650805cd-8abf-4f2d-bc23-9552511c7e01",
    "type": "Membership",
    "member": {
      "type": "EconomicOperator",
      "legalName": "Farm Example BV",
      "legalIdentifier": { "@type": "Euid", "@value": "BEEUID0123456789" }
    },
    "memberOf": "https://agri-x.eu",
    "holderIdentifier": "BE0123456789",
      "role": ["https://w3id.org/ebwv#DataRightsHolder", "https://w3id.org/ebwv#DataProvider"],
    "termsOfUse": {
      "type":"GovernanceRulebook",
      "url": "https://agri-x.eu/rulebook",
      "version": "1.2",
      "hash": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
      "acceptedAt": "2026-06-20T14:30:00Z" 
    },
    "onboardedBy": {
      "type": "Platform",
      "platformId": "did:web:djustconnect.be",
      "name": "DjustConnect",
      "operator": {
        "type": "EconomicOperator",
        "legalName": "Instituut voor Landbouw-, Visserij- en Voedingsonderzoek (ILVO)",
        "identifier": { "@type": "VatId", "@value": "BE0848278827" }
      }
    }
  }
}
```

This example reads: *"DjustConnect, a platform hosted by ILVO, onboarded Farm Example BV — proven
during onboarding by VAT-ID BE0123456789 and identified at EU level by EUID BEEUID0123456789 — into
Agri-X as a Data Rights Holder and Data Provider."* The VAT-ID under `operator.identifier` belongs
to ILVO; the VAT-ID under `evidence` is the identification means used for the holder.

Expanding this example makes three things explicit. `role` and `memberOf` become **node
references** — `{"@id": "https://w3id.org/ebwv#DataProvider"}`, `{"@id": "https://agri-x.eu"}` —
because the vocabulary types both properties `@id` (Section 2.8). This is why their values are
absolute IRIs: a relative value would be resolved against the document base, producing a different
IRI for every location the credential is served from. `holderIdentifier`, by contrast, is typed
`xsd:string` and expands as a plain literal. Identifiers expand as **typed literals** carrying
their scheme as the datatype IRI, for example
`{"@value": "BE0123456789", "@type": "https://w3id.org/ebwv#VatId"}`. And
`attestationLegalCategory` expands to a node reference, `{"@id": "https://w3id.org/ebwv#EAA"}`,
because the vocabulary types it `@vocab`. Section 3.3.2 sets out the type declarations this
depends on.

### 3.3.2 Type declarations required for expansion

The European Business Wallet Vocabulary context defines almost all of its properties inside
**type-scoped contexts**, not at the top level. Only `description`, `issuer`, `name` and
`termsOfUse` are defined globally. A property is therefore undefined — and, since the context sets
no `@vocab`, **silently dropped on expansion** — unless the enclosing object declares the type that
scopes it. Issuers SHALL declare the following types, and verifiers SHOULD reject a credential in
which an expected attribute does not survive expansion:

| Object | `type` that SHALL be declared | Properties it brings into scope |
|---|---|---|
| the credential | `VerifiableCredential` and `ElectronicAttestationOfAttributes` | `attestationLegalCategory`; `evidence` and the other VCDM envelope terms come from `VerifiableCredential` |
| `credentialSubject` | `Membership` | `member`, `memberOf`, `role`, `onboardedBy` |
| `credentialSubject.member`, `onboardedBy.operator`, each `evidence` entry | `EconomicOperator` | `legalName`, `legalIdentifier`, `identifier` |
| `credentialSubject.onboardedBy` | `Platform` | `platformId`, `operator` |
| `credentialSubject.termsOfUse` | `GovernanceRulebook` | `url`, `version`, `hash`, `acceptedAt` |

Three consequences worth stating plainly:

* **`ElectronicAttestationOfAttributes` SHALL appear in the credential-level `type`.** It is what
  brings `attestationLegalCategory` into scope; without it the attribute required by Section 2.1 is
  dropped on expansion. The vocabulary types that property `@type: @vocab` with a nested context
  mapping `EAA`, `QEAA` and `Pub-EAA` to their individuals, so the value expands to a node
  reference — `{"@id": "https://w3id.org/ebwv#EAA"}` — rather than a string literal. That nested
  context also sets `"@vocab": "ebwv:INVALID_VALUE:"`, so a value outside the three published
  categories expands to a visibly invalid IRI instead of being silently dropped.

* **`Membership` types the credential subject, not the credential.** The credential-level `type`
  is `["VerifiableCredential", "ElectronicAttestationOfAttributes"]`, neither of which is
  `Membership`. `Membership` is declared a subclass of `CredentialSubject` in the
  vocabulary, and putting it in the credential-level `type` array leaves every Membership property
  undefined inside `credentialSubject`, so `member`, `memberOf`, `role` and `onboardedBy` are all
  dropped on expansion without any error being raised.
* **Each `evidence` entry is typed `EconomicOperator`.** The `identifier` property is scoped to that
  type, and the entry does describe the holder as an economic operator identified by the means used
  at onboarding, so the typing is both necessary and semantically correct. It also satisfies the
  domain of [identifier](https://w3id.org/ebwv#identifier).

**Coverage.** Every attribute defined by this Rulebook now has a property term in the European
Business Wallet Vocabulary context, and the illustrative example in Section 3.3 expands without
loss. This was verified against the context published on 2 September 2026, which added
`holderIdentifier` to the `Membership` type-scoped context.

Because that context sets no `@vocab`, an attribute with no term is **silently dropped on
expansion** rather than raising an error. Issuers and verifiers SHOULD therefore treat a successful
expansion as something to check rather than assume: a Relying Party SHALL NOT infer the absence of
an attribute from an expanded document alone without confirming that its context set defines the
corresponding term.

*Proof type: an EU-approved Data Integrity proof / VC-JOSE-COSE securing mechanism SHALL be used.
[PROOF TYPE TO BE FIXED once the WE BUILD profile selects it; e.g. a Data Integrity ECDSA proof to
support ZKP-based selective disclosure.]*

## 4 Attestation usage

The Membership Credential is used in the WE BUILD SC2 "seamless onboarding" scenario. Its use case
in this pilot is:

* **Onboarding into a DSI or into Agri-X.** The holder presents the EUBWOID to identify their
  organisation, accepts the applicable dataspace governance rulebook, and receives a Membership
  Credential reflecting their membership and roles. Information already presented during a previous
  onboarding flow is trusted and not requested again. Where the onboarding platform holds a
  identification means used to prove the holder's identity, it is recorded in `evidence`, so that a
  later Relying Party can reconcile the holder with its own legacy records.

**Potential future use, out of scope for this pilot.** Verifying membership and roles during
data-sharing transactions between participants of a DSI or dataspace is a plausible further
application, but it is not piloted in the MVP and is not specified by this Rulebook. Direct
presentation of the Membership Credential inside a data-transfer flow is not assumed: such a flow
would most likely require the credential to be transformed into a connector-native credential (for
instance an EDC / dataspace protocol participant credential) first. Any statement about
data-sharing use elsewhere in this document is to be read in that light.

**PID verification.** The holder is a legal person identified via the EUBWOID/EUID, not via a PID.
A Relying Party therefore does not need to request and verify a PID (ARB_27) for this attestation
in the MVP scenario.

**Relying Party obligations.** A Relying Party SHALL verify the issuer signature/proof, check
credential validity (`validFrom`/`validUntil`) and revocation status (Section 6), and confirm the
issuer is an authorised onboarding service provider for the relevant `memberOf` value (Section 5).
Where rulebook conformance matters, the Relying Party MAY compare `termsOfUse.hash` /
`termsOfUse.version` against the expected rulebook. A Relying Party MAY additionally use
`evidence` to reconcile the holder with its own legacy records, subject to IR-04. It SHALL match
`role` and `memberOf` as exact, case-sensitive strings per IR-05.

**Presentation requirements.** Presentation is online. The primary format is W3C VCDM (JSON-LD)
presented via OpenID4VP; an SD-JWT VC flow may be piloted additionally. No proximity/offline
presentation is required.

**Device binding.**  The attestation is bound to an
organisation (legal person) held in an EU Business Wallet rather than to a natural person's device;
the MVP does not require cryptographic binding to a PID. The `cryptographically_bound_to` attribute
(ARB_28) is therefore not included. If a future scenario requires binding to the EUBWOID, add
`cryptographically_bound_to` as optional metadata in Section 2.6 with the corresponding attestation
type / `vct` value.

**Transactional data.** No transactional data (per [Topic 20]) is defined for this attestation; it
is not used for strong user authentication of electronic payments.

## 5 Trust anchors

**This Rulebook (non-qualified EAA):** the trust anchor is the public key of the issuing onboarding
service provider, resolvable from the issuer DID (`issuer` in the VCDM credential, e.g. a `did:web`
document). A Relying Party obtains the trust anchor by resolving that DID and verifies the
credential proof against it. Authorisation of an issuer to issue Membership Credentials for a given
`memberOf` value is governed by the WE BUILD / dataspace trust framework (WP4).

**memberOf vocabulary governance.** `memberOf` values are absolute IRIs registered in code list 2.8
by the governance level of the owning DSI or dataspace, under that DSI's or dataspace's own domain.
A Relying Party SHALL match `memberOf` by exact IRI comparison and confirm WP4 authorisation of the
issuer for that specific value (IR-05). Domain ownership makes the values globally unique. Prefix
matching does not apply, since each value identifies a distinct DSI or dataspace rather than a term
in a shared vocabulary, and a Relying Party SHALL NOT depend on the IRI dereferencing. Registering
the value in code list 2.8 before issuing remains a governance obligation, not a convenience.

**Role vocabulary governance.** `role` values are absolute IRIs. Those registered in code list 2.8
are the `DataSpaceRole` individuals published by the WE BUILD Semantics work group under
`https://w3id.org/ebwv#`, independently of this Rulebook's own versioning. Because the vocabulary
types `role` as `@id`, a Relying Party MAY trust roles by namespace prefix rather than an
exact-match list, so that new individuals published under that namespace do not require a Relying
Party policy change. A DSI MAY likewise mint role IRIs under a namespace it owns without a change
to this Rulebook or to the vocabulary context; such values SHALL be governed by that DSI's own
trust framework, and a Relying Party SHALL ignore any role IRI it does not recognise (IR-05).

## 6 Revocation

The Membership Credential is **revocable**. Membership and the associated set of
roles share a single lifecycle: adding, changing, or removing a role requires re-issuance of the
credential and revocation of the superseded one. The credential carries a `credentialStatus` entry
(see the Section 3.3 example) used to publish status.


## 7 Compliance

The Membership Credential is defined as a **non-qualified EAA** under the [European Digital Identity
Regulation]:

* It includes an attribute indicating it is an EAA (`attestation_legal_category` = `EAA`,
  Sections 2.1 and 2.5), per ARB_12.
* It carries attributes about the holder (`member.legalIdentifier`, `member.legalName`, `memberOf`,
  `role`) per ARB_15 / ARB_17 (Annex V points b and c).
* The W3C VCDM (JSON-LD) format is used, which is permitted only for non-qualified EAA (ARB_01a).
* The trust-anchor location is provided via the issuer DID (Section 5), per ARB_21 / ARB_26.
* Revocation is addressed in Section 6, per [Topic 7].


## 8 References

| **Item Reference** | **Standard name/details**|
|--------------------|---------------------------|
| [European Business Wallet Vocabulary v0.1] | WE BUILD Semantics work group, European Business Wallet Vocabulary, version 0.1 |
| [European Digital Identity Regulation] | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework |
| [HAIP] | Yasuda, K. *et al,* OpenID4VC High Assurance Interoperability Profile, OpenId Foundation, Version draft-03 |
| [IANA-JWT-Claims] | IANA JSON Web Token Claims Registry. Available: <https://www.iana.org/assignments/jwt/jwt.xhtml> |
| [ISO/IEC 18013-5] |  ISO/IEC 18013-5, Personal identification --- ISO-compliant driving licence - Part 5: Mobile driving licence (mDL) application, First edition, 2021-09 |
| [OIDC] | Sakimura, N. et al., "OpenID Connect Core 1.0", OpenID Foundation. Available: <https://openid.net/specs/openid-connect-core-1_0.html> |
| [RFC 3339] | RFC 3339  - Date and Time on the Internet: Timestamps, G. Klyne et al., July 2002 |
| [RFC 8610] | RFC 8610  - Concise Data Definition Language (CDDL): A Notational Convention to Express Concise Binary Object Representation (CBOR) and JSON Data Structures, H. Birkholz et al., June 2019 |
| [RFC 8943] | RFC 8943  - Concise Binary Object Representation (CBOR) Tags for Date, M. Jones et al., November 2020 |
| [RFC 8949] | RFC 8949 - Concise Binary Object Representation (CBOR), C. Bormann et al., December 2020 |
| [SD-JWT VC] |  SD-JWT-based Verifiable Credentials (SD-JWT VC). Available: <https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/>, version draft-ietf-oauth-sd-jwt-vc-09  |
| [Topic 7] | ARF Annex 2 - Topic 7 - Attestation revocation and revocation checking Available: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a237-topic-7-attestation-revocation-and-revocation-checking>|
| [Topic 10] | ARF Annex 2 - Topic 10 - Issuing a PID or attestation to a Wallet Unit: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a2310-topic-10-issuing-a-pid-or-attestation-to-a-wallet-unit>|
| [Topic 12] | ARF Annex 2 - Topic 12 - Attestation Rulebooks, Available: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a2312-topic-12-attestation-rulebooks>|
| [Topic 20] | ARF Annex 2 - Strong User authentication for electronic payments, Available: <https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-2/annex-2-high-level-requirements/#a2320-topic-20-strong-user-authentication-for-electronic-payments>|
| [W3C VCDM v2.0] | Sporny, M. *et al,* Verifiable Credentials Data Model v2.0, W3C Recommendation.  |
