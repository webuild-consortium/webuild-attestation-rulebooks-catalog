# WE BUILD Attestation Rulebook Template for attestations of type Power of Attorney
## Abstract

This rulebook provides a common conceptual and operational foundation for the use of Power of Attorney and Power of Representation within the WeBUILD ecosystem. It explains how legal authority can be expressed, issued, presented, and verified in a digital context, enabling trusted business and public-sector processes across organizational and national boundaries.

Power of Attorney refers to a legally granted authority by which an economic operator authorizes another to act on its behalf within a defined scope. Power of Representation dcertifies a specific position or role held by the representative within an organization to operate with unliminted capacity in a given transaction or process, based on law, internal governance, mandate, or delegated authority. In digital wallet-based ecosystems such as EUBW and EUDI, these concepts need to be represented in a machine-readable, verifiable, and selective-disclosure-friendly form so that relying parties can validate both the existence and the limits of the authority.

The rulebook aims to align legal meaning, technical implementation, and operational trust requirements. It supports interoperable issuance and presentation flows, consistent terminology, and reliable validation of representation claims in cross-border use cases such as business-to-government interactions, tax-related procedures, and other regulated transactions. By establishing shared rules and reference patterns, the rulebook helps create a scalable foundation for trustworthy digital representation in the European business wallet environment.

* Author(s):
    * Boris Lingl
    * Sofia Lucas
    * Alexander Manecke
    * Ignacio Ripoll
    * Iris Speiser
    * Marlene Urbschat


| Version | Date | Description |
|---------|------------|------------|
| 0.1 | 2026-06-02 | initial Version |
| 0.2 | 2026-06-30 | added content  |
| 0.3 | 2026-07-06 | Added PoX model    |
| 0.4 | 2026-07-08 | Detailed tables for the attestation elements |
| 0.5 | 2026-07-09 | Detailed tables for the attestation metadata and dimissal of mDoc encoding for the moment |
| 0.55 | 2026-07-14 | Enhanced content |
| 0.6 | 2026-07-14 | Added examples for SD-JWT |
| 0.7 | 2026-07-14 | Added references to rulebook sections within SD-JWT |

**Feedback:**

* <https://github.com/webuild-consortium/BU4/issues/>

## 1 Introduction

### 1.1 Document scope and purpose

#### Scope

This document defines the scope and purpose of the WeBUILD rulebook for the use of **Power of Attorney (PoA)** and **Power of Representation (PoR)** here called **Power of X (PoX)** in digital business and public-sector interactions. It establishes a shared framework for how representation rights are described, issued, presented, verified, and relied upon in interoperable wallet-based environments, particularly in the context of the European Digital Identity Wallet and the European Business Wallet ecosystem.

The scope of this document covers the conceptual, legal, organizational, and technical foundations required to support trustworthy representation of economic operators acting on behalf of other economic operator. It addresses the roles of relevant actors, the structure and meaning of representation mandates, the requirements for verifiable attestations, and the conditions under which relying parties can assess the validity and scope of delegated authority in cross-border and regulated use cases.

The purpose of the rulebook is to create a common understanding among participating stakeholders and to support consistent implementation across pilots and future productive environments. It aims to reduce ambiguity, improve interoperability, and provide a reliable basis for secure and legally meaningful digital representation processes within the WeBUILD framework.This Rulebook specifies semantic, organizational and technical requirements for the digital representation of **Power of X (PoX)** attestations within the WE BUILD ecosystem.

It defines:

- the legal meaning of a digital Power of Attorney (PoA);
- the legal meaning of a digital Power of Representation (PoR);
- the actors participating in its lifecycle;
- the mandatory and optional data elements;
- issuance requirements;
- presentation and verification requirements;
- trust requirements;
- revocation mechanisms;
- encoding requirements for interoperable attestation formats.

The Rulebook applies to Powers of X (PoA, PoR) issued for cross-border business interactions involving legal entities, public administrations and regulated service providers. The attestations of attributes described in this document MUST be supported by an authentic source, as defined in the eIDAS Regulation [CIR 2024/1183]. They shall be issued by a public sector body that is responsible for an authentic source or by a public sector body that is designated by the Member State to issue such attestations of attributes on behalf of the public sector bodies responsible for authentic sources in accordance with Article 45f and with Annex VI of the regulation. The issuer of the electronic attestation of attributes MAY choose not to validate the information with an authentic source in those cases where the subject of the attestation is not included in Annex VI of the eIDAS Regulation. Any attestation not supported by information provided by an authentic source MUST not be qualified according to eIDAS Regulation and ADRXXX.

#### Purpose

The primary objective of this Rulebook is to establish a common interoperable model for representing delegated authority inside the European Digital Identity ecosystem.

The objective of Power or X (PoX) is to provide legally valid and verifiable proof that an economic operator has the capacity to act on behalf of another, with clearly defined terms, scope, duration and limitations, based on the faculties and authority granted to them by holding an organic position within the entity (such as Sole Administrators, Supportive Administrator, Joint Administrator or Board Member) or by having a power of attorney with specific faculties. 

The Rulebook enables organizations to digitally authorize individuals or other legal entities to perform legally binding actions on their behalf in B2B and B2G contecxts.
Typical examples include:

- submitting tax declarations;
- representing an enterprise before public authorities;
- signing legally binding business transactions;
- submitting regulatory filings;
- accessing business platforms;
- performing financial or administrative operations.

The Rulebook ensures that delegated authority can be issued once and reused across multiple relying parties without repeated manual verification.

#### What real-world fact, entitlement, role, status, or capability the attestation expresses

This attestation expresses that the holder (the attorney-in-fact in the case of PoA) has been legally authorized by the granter (the principal) to act on their behalf in specific or general legal, administrative, or business matters; or certifies a specific position or role of the holder within a company, in accordance with the data entered in the official register authorised by each Member State (in the case of PoR). It formally establishes the entitlement to represent the principal before third parties, including government authorities, courts, financial institutions, or business partners. The attestation confirms the capability to make binding declarations, sign documents, submit applications, receive payments, or perform other defined actions within the scope of the granted power.

#### Which issuers, holders, and relying parties are expected to use it

Role	Expected Actors
- Issuers. In EUDI and EUBW context: Qualified Trust Service Providers (QTSPs) issuing digitally signed attestations with QES/QEAA. Economic operators wanting to attest authorizations to act on its behalf (self-issued). The attestation SHALL be issued by actors within the trust framework who are authorised to do so, whether they are a Trust Service Provider that has an agreement with the authentic source responsible for the data, a public sector body responsible for an authentic source, or an organisation acting on its behalf.
- Holders.	The appointed attorney-in-fact (natural or legal person), who may be a family member, legal advisor, company representative, or professional agent (PoA) or a person having a position within the company that entitles unlimited representation capacities (PoR). The holder stores the attestation in their EUBW wallet.
- Relying. Parties	Government agencies (e.g., courts, tax authorities, DPMA), financial institutions, notaries, businesses, or any third party requiring proof of representation authority before accepting actions taken by the holder.
- Authentic Sources. Repository or system, held under the responsibility of a public sector body or private entity, that contains and provides attributes about a natural or legal person or object and that is considered to be a primary source of that information or recognised as authentic in accordance with Union or national law, including administrative practice;


#### Which use case or user journey the attestation supports

Primary Use Cases:

B2B: Authorizing employees or partners to sign contracts, conduct financial transactions, or represent the company in negotiations or get access to services

B2G: Representation before public authorities (e.g., submitting tax reporting, social security matters, ...)

Legal Proceedings: representation against 3rd parties, public sector and other relying parties, accepting service of documents and in most cases directly through personal actions as personal Affair while taking actionb / decisions on behalf of a company or organsation. 


> Example
>
> This attestation enables a relying party (e.a. a tax authority) to verify, in plain language, that the holder (e.g. a tax advisor) is
> authorised to act in a specific project role (e.g. to file a tax declaration on behalf of a company in a another EU member state). 
> It is intended for project operators, service providers, and supervisory relying parties in the WE BUILD ecosystem. The functional description
> and actor terminology can be reused from the corresponding use-case attestation description and
> refined here into rulebook language.
>


#### Business Context

Many European business processes require an individual to act on behalf of an organization in B2B and B2G contexts. Traditionally, such mandates are expressed by paper documents, national electronic registers or proprietary authorization mechanisms.

These approaches suffer from lack of interoperability, manual verification, legal uncertainty across borders, duplicated onboarding procedures and high operational costs.

Digital Powers of Attorney address these challenges by providing verifiable, machine-readable evidence of delegated authority.

#### Objectives

This Rulebook pursues the following objectives:

- establish a common semantic model;
- support cross-border interoperability;
- enable selective disclosure;
- reduce administrative burden;
- improve legal certainty;
- enable automated authorization decisions;
- support reuse across multiple services;
- align with the EUDI Wallet Architecture and Reference Framework.

#### Intended Audience

This Rulebook is intended for:

- Qualified Trust Service Providers;
- Electronic Attestation Providers;
- Authentic Sources;
- Business Register Operators;
- Wallet Providers;
- European Business Wallet Providers;
- Relying Parties;
- Public Administrations;
- solution architects;
- developers implementing WE BUILD pilots.

#### Power of X within WE BUILD

Within the WE BUILD ecosystem, **Power of X (PoX)** is the common semantic model used to describe the authority of a natural or legal person to act on behalf of a Economic Operator in a legally meaningful and verifiable manner.
Rather than defining a separate attestation type, PoX provides a common representation framework for different forms of delegated or inherent authority. It establishes a shared conceptual model that can be specialized according to the legal origin of the authority.

The WE BUILD PoX model currently distinguishes three authority models:

- **Power of Attorney (PoA)** – authority explicitly delegated by a principal through a legally valid mandate defining the scope, duration and limitations of the delegated powers.
- **Power of Representation (PoR)** – authority derived directly from law, company statutes or an official register. The representative acts by virtue of holding an organizational position recorded by an authentic source.
- **Power of Employee (PoE)** – authority granted by an organization to an employee or contractor to perform defined operational activities or access specific services on behalf of the organization. Support for PoE may be specified in future versions of this Rulebook.

> REMARK: As a BU4 Onsite Berlin decission, PoE will **NOT** be covered in MVP Pilot scenarios. 
> It might be covered in MVP+ scenarios.

#### Common Representation Model

In general all PoX attestation will be based on one common approach and the same logical structure.

```text
Representation
│
├── economic_operator_represented (legal_entity_represented)
│
├── proxy
│      │
│      ├── entity_type
│      ├── natural_entity_proxy
│      └── legal_entity_proxy
│
├── authority
│      │
│      ├── proxy_position
│      ├── proxy_power_scope
│      └── proxy_employee_authorisation
│
└── metadata

```

All three authority models share the same semantic foundation and differ only in the legal source from which the authority originates.

Where:

- **Represented Economic Operator** identifies the organization or Legal Entity on whose behalf actions may be performed.
- **Proxy** identifies the economic operator exercising the authority.
- **Authority** describes the legal basis that enables representation.
- **Metadata** contains attestation lifecycle and trust information.

The Authority component is specialized depending on the representation model:

| Authority Model          | Authority Source |
|-----------------         |------------------|
| Power of Representation  | Organizational Position |
| Power of Attorney        | Delegated Mandate |
| Power of Employee        | Employee Authorization |



#### Relationship to pilot cases and other WE BUILD Rulebooks

This Rulebook forms the wider WE BUILD Power of X framework. As one layer, it represents use case scenarios:

| Scenario Number    | Scenario Source / Pilot case      | Link            |
|-----------------    |------------------                 |-----------------|  
| 1a                  | Power of Attorney                 | https://github.com/webuild-consortium/BU4/tree/main/scenarios/1A-PoA-Issuance|
| 1b                  | Power of Representation           | https://github.com/webuild-consortium/BU4/tree/main/scenarios/1B-PoR-Issuance|
| which results in    |                                   |                  |
| 1c                  | get access to a service           | https://github.com/webuild-consortium/BU4/tree/main/scenarios/1C-Service-Access |


| Attestattion type   | Rulebook                          | Link            |
|-----------------    |------------------                 |-----------------|  
| PID                 | rb-pid                            | https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/tree/main/rulebooks/rb-pid                |
| EUCC                | rb-eucc                           | https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/tree/main/rulebooks/rb-pid                |
| Employee            | rb-employee                       | https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/tree/main/rulebooks/rb-employee           |
| tbd                 | rb-                               |                                                                                                                       |


Power of X provides the common semantic foundation for authority-based attestations within WE BUILD. This Rulebook specifies the specialization for **Power of X**. All related specifications are included within this document:

- WE BUILD Attestation Rulebook – Power of Attorney
- WE BUILD Attestation Rulebook – Power of Representation
- WE BUILD Attestation Rulebook - Power of Employee Specification (future work - for transparency but will not be covered)
plus
- WE BUILD Operational Rulebook – Access to Service

```text
Represented Economic Operator 
          │
          ▼
        Proxy
          │
          ▼
      Authority
          │
          ▼
       Metadata
```

```text
Represented Economic Operator with attestation
          │
          ▼
 get access to service 

```

This Rulebooks is expected to share the same core semantic model while specializing the **Authority** component according to their legal basis.

### 1.2 Document structure

* Chapter 2, which describes the attestation attributes and metadata in an
encoding-independent manner.
* Chapter 3, which specifies how the attestation
attributes and metadata are encoded in case the attestation complies with [ISO/IEC
18013-5] and/or [SD-JWT VC] and/or [W3C VCDM v2.0]. Each encoding SHALL be specified in a separate section, or even in a separate chapter. 
> Within our MVP scenarios we will focus on SD-JWT VC, all others are postponed or might be used in MVP+ scenarios)
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

This Rulebook adopts terminology defined by the European Digital Identity Regulation, the Architecture and Reference Framework, ETSI Electronic Attestation specifications and the WE BUILD semantic model.

| Term                | Definition |
|------               |------------|
| Power of Representation (PoR)| This certifies a specific position or role held by the representative of a legal person, in accordance with the data entered in the official register authorised by each Member State. Therefore, this attestation certifies the performance of a position or function by a legal or natural person. For the purposes of this document, a position shall be understood to be an organic post with **unlimited representative capacity**, which may require the concurrence of several proxies of the same category such as Sole Administrators, Supportive Administrator, Joint Administrator or Board Member. |
| Power of Attorney (PoA) | Confirms that an economic operator has granted legal representation authority to the holder, based on the information recorded in an official register approved by each Member State. This attestation therefore verifies that the individual (whether it is a natural person or a Legal Entity) is authorised to act as an attorney-in-fact.|
| Principal           | Entity granting authority. |
| Position            | specific position or role held by the representative of an economic operator, in accordance with the data entered in the official register authorised by each Member State. |
| Attorney-in-Fact    | Entity receiving delegated authority. |
| Holder              | Wallet owner storing the PoR or PoA. |
| Issuer              | Organization issuing the PoR or PoA. |
| Authentic Source    | Source providing legally reliable information. |
| QTSP                | Qualified Trust Service Provider. |
| Relying Party       | Organization verifying the PoR or PoA. |
| Mandate             | Delegated authorization relationship. |
| Scope               | Business activities authorized by the PoR or PoA. |
| Validity            | Time interval during which the PoR or PoA may be exercised. |
| Revocation          | Withdrawal of delegated authority. |
| economic operator   | wider definition which is either a natural person (also soletrader) or a legal entity |


This document uses the terminology specified in Annex 1 of the ARF.

## 2 Attestation attributes and metadata

### Chapter overview and requirements

This chapter defines the semantic model of the **Power of X (PoA, PoR)** attestation independently of any credential encoding format.

Every Power of Attorney SHALL express a legally valid delegation of authority between a **Principal** and a **Position** or an **Attorney-in-Fact**. The attestation SHALL allow a Relying Party to determine:

- who delegated authority;
- who received authority;
- which economic operator is represented;
- which actions are authorized;
- under which legal basis;
- for which validity period;
- under which restrictions;
- whether the mandate remains valid.

The semantic model defined in this chapter SHALL remain independent of the chosen attestation format.

**Requirements for non-qualified EAA**

* An attribute indicating that the attestation is an EAA SHOULD be included (see ARB_12 in [Topic 12]).
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
* Non-qualified EAA MAY be self-issued without the perticipation of an authentic source in the issuance process.

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
* Qualified EAA MUST use the information registered in an authentic source in the issuance process.

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

### 2.1 Introduction

#### Chapter Overview

This chapter defines the semantic model of the **Power of X (PoA, PoR)**  attestation independently of any attestation encoding format.

Every Power of Attorney SHALL express a legally valid delegation of authority between a **Principal** and a **Position** or an **Attorney-in-Fact**. The attestation SHALL allow a Relying Party to determine:

- who delegated authority;
- who received authority;
- which organization is represented;
- which actions are authorized;
- under which legal basis;
- for which validity period;
- under which restrictions;
- whether the mandate remains valid.

The semantic model defined in this chapter SHALL remain independent of the chosen attestation format.

#### 2.1 Overall Semantic Model

A Power of X attestation is composed of four common semantic domains.

```text
Power of X
│
├── Represented Economic Operator (Legal Entity)
├── Proxy
├── Authority
└── Metadata
```

Depending on the selected authority model, the **Authority** domain is represented as:

- Position (Power of Representation)
- Mandate (Power of Attorney)
- Employee Authorization (Power of Employee)

> Remark
>
> The attestation description used here for Power of X (PoA, PoR, PoE) already contain a domain model showing the holder,
> issuer, project, permit, and validity period. Depending on your way of personal information gathering and to make things easier to understand, the following UML diagram
> might help to sort information out easier
>
> <img width="454" height="438" alt="image" src="https://github.com/user-attachments/assets/28ba0189-1722-42ab-b1c4-431a7f1e82ce" />
> 
> If you experience trouble viewing the UML-File please refer directly to our GitGUB Repo
> 
> https://github.com/webuild-consortium/BU4/blob/main/rulebooks/pox_rulebook_uml.png


#### 2.2 Mandatory attributes

The semantic model is organized into four common domains that are shared by all Power of X attestations.

##### Domain 1 – Represented Economic Operator (Legal Entity)

An economic operator that has legal rights and obligations. An economic operator able to transact business, typically registered with a body able to confer legal status such as a national business register. It is able to trade, is legally liable for its actions, accounts, tax affairs etc. It will contain the minimum mandatory information for legal person identification, ensuring identity matching while delegating full company information to the EBW-OID [CIR 2024/2977]

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------|--------------|--------------|--------------|
| *EconomicOperator.EBWOID* | *TBD* | *A unique identifier constructed by the sending Member State in accordance with the technical specifications for the purposes of cross-border identification and which is as persistent as possible in time.* | *String* | *EU-DE-HRB-123456* |
| *EconomicOperator.LegalName* | *TBD* | *The name under which the Legal Entity is legally registered* | *String* | *Mustermann GmbH* |

##### Domain 2 – Proxy

Refers to the identity of an economic operator authorised to act on behalf of the Represented Economic Operator. In the context of the PoX, two possible types of proxy are identified that are mutually exclusive, and the attestation will contain only one of the two options shown below.

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------|--------------|--------------|--------------|
| *Proxy.EntityType* | *TBD* | *Enumeration describing whether the proxy is a Economic Operator or a natural person so that the proxy's identifying information can be interpreted correctly. Values shall be one of the following:•0  = LegalEntityProxy • 1 = NaturalEntityProxy* | *Integer* | *0* |
| *Proxy.Proxy* | *TBD* | *See LegalEntityProxy and NaturalEntityProxy data structuresbelow* | *JSON ENUM* | *See LegalEntityProxy and NaturalEntityProxy data structuresbelow* |

##### Domain 2.1 – Economic Operator Proxy

It will contain the minimum mandatory information for legal person identification, ensuring identity matching while delegating full company information to the EBW-OID [CIR 2024/2977]

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------|--------------|--------------|--------------|
| *LegalEntityProxy.EBWOID* | *TBD* | *A unique identifier constructed by the sending Member State in accordance with the technical specifications for the purposes of cross-border identification and which is as persistent as possible in time.* | *String* | *EU-DE-HRB-123456* |
| *LegalEntityProxy.LegalName* | *TBD* | *The name under which the Economic Operator is legally registered* | *String* | *Mustermann GmbH* |

##### Domain 2.2 – Natural Entity Proxy

It will contain the minimum mandatory information for natural person identification, ensuring identity matching while delegating full person information to the PID [CIR 2024/2977] with any possible modification approved in the context of WeBuild Consorcium, specifically through WP4 PID-EBWOID group.

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------|--------------|--------------|--------------|
| *NaturalEntityProxy.FamilyName* | *TBD* | *Current last name(s) or surname(s) of the user to whom the person identification data relates* | *String* | *Duck* |
| *NaturalEntityProxy.GivenName* | *TBD* | *Current first name(s), including middle name(s) where applicable, of the user to whom the person identification data relates.* | *String* | *Donald* |
| *NaturalEntityProxy. BirthDate* | *TBD* | *Day, month, and year on which the user to whom the person identification data relates was born.* | *date-time or full-date as specified in RFC 3339* | *1990-07-08T10:30:21.000Z* |
| *NaturalEntityProxy.BirthPlace* | *TBD* | *The country as an alpha-2 country code as specified in ISO 3166-1, or the state, province, district, or local area or the municipality, city, town, or village where the user to whom the person identification data relates was born.* | *alpha-2 country code as specified in ISO 3166-1* | *BE* |
| *NaturalEntityProxy.Nationality* | *TBD* | *One or more alpha-2 country codes as specified in ISO 3166-1, representing the nationality of the user to whom the person identification data relates.* | *BE* |

##### Domain 3 – Authority Scope

The Authority domain represents the legal basis enabling representation.

Depending on the attestation type, exactly one Authority specialization SHALL be present.

| Authority Type            | Used by                 | Core Attributes       |
|-----------------          |---                      |---                     |
| Position                  | Power of Representation | position, registration date, cardinality |
| Mandate                   | Power of Attorney       | mandate type, scope, legal basis, validity |
| Employee Authorization    | Power of Employee       | employee role, authorization scope, service access |

The Authority domain is specialized according to the legal origin of the authority while preserving a common representation model.

Three authority models are defined:

| Authority Model            | Purpose                |
|-----------------           |---------               |
| **ProxyPosition**          | Represents authority derived from an organisational position recorded in an authentic source (Power of Representation). |
| **ProxyPowerScope**        | Represents authority explicitly delegated through a legally valid mandate (Power of Attorney). |
| **ProxyEmployeeAuthorisation** | Represents operational authority granted by an organisation to an employee or contractor (Power of Employee). |

Only **one** Authority specialization SHALL be present in a single Power of X attestation.

For this Rulebook, the applicable Authority specialization is **ProxyPowerScope**.

##### Domain 3.1 Common Authority Components

Regardless of the specialization, the Authority domain may reference a common set of reusable semantic components.

| Component          | Purpose                      |
|-----------         |---------                     |
| **Mandator**       | Identifies the person granting the authority where applicable. |
| **Constraints**    | Defines operational or legal limitations associated with the authority. |
| **ServiceAccess**  | Specifies the relying parties or services for which the authority may be exercised. |

These components are reused across multiple authority models to ensure semantic consistency.

##### Domain 3.2 ProxyPosition (Power of Representation | PoR)

This certifies a specific position or role held by the representative of a legal person, in accordance with the data entered in the official register authorised by each Member State.

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------|--------------|--------------|--------------|
| *ProxyPosition.Position* | *TBD* | *In the event that the type of representation is organic / administrative position within the Economic Operator, indicate the type of position held by the proxy in relation to the faculty indicated in the power.* | *String* | *Sole Administrator* |
| *ProxyPosition.InscriptionDate* | *TBD* | *Specific date of the inscription of the faculty in the authentic source that enables the attestation.* | *date-time or full-date as specified in RFC 3339* | *2020-07-08T10:30:21.000Z* |
| *ProxyPosition.IssuingAuthority* | *TBD* | *Name of the authority that is issuing the attestation.* | *String* | *Cleverbase* |
| *ProxyPosition.IssuingAuthorityType* | *TBD* | *Type of authority in accordance with the Trust Framework defined in the scope of eIDAS Regulation (QTSP, PubEAA, NQTSP)* | *Integer* | *0* |
| *ProxyPosition.AuthenticSourceId* | *TBD* | *Identification information with regard the authentic source that has the power and faculties registered.* | *String* | *VATES-E81458556* |
| *ProxyPosition.AuthenticSourceName* | *TBD* | *Name of the authentic source that has the power and faculties registered.* | *String* | *Registro Mercantil de Madrid* |
| *ProxyPosition.IssuingCountry* | *TBD* | *Country where the attestation is being issued.* | *alpha-2 country code as specified in ISO 3166-1* | *ES* |
| *ProxyPosition.EvidenceURI* | *TBD* | *Address for accessing the public document certifying the power of representation.* | *String* | *https://sede.registradores.org/sede/sede-csv-web/csv/20815412F93A6D5B* |
| *ProxyPosition.EvidenceDescription* | *TBD* | *Description of the public document certifying the power of representation.* | *String* | *Business Registry Certification* |
| *ProxyPosition.AssuranceLevel* | *TBD* | *Level of assurance and confidence that should be given to a statement based on the origin of the information. Since this attestation relies on a Business Registry the assurance level is always High.* | *Integer* | *0* |

##### Domain 3.3 ProxyPowerScope (Power of Attorney | PoA )

Representation powers authorise a person or entity to act on behalf of another in legal, administrative, or business matters. Each power has a specific scope that impose a context and limitations to the operations that may be performed by the Proxy.

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------|--------------|--------------|--------------|
| *ProxyPowerScope.Type* | *TBD* | *Establishes the type of power based on the relationship that the proxy has with the company it claims to represent.* | *Integer* | *1* |
| *ProxyPowerScope.GrantDate* | *TBD* | *Specific date of the granting of the faculty in the authentic source that enables the attestation.* | *date-time or full-date as specified in RFC 3339* | *1990-07-08T10:30:21.000Z* |
| *ProxyPowerScope.Limitation* | *TBD* | *Assessment of the existence of limitations on the scope of execution of the power.* | *Boolean* | *FALSE* |
| *ProxyPowerScope.Faculty* | *TBD* | *Represent the inherent capacities that the power enables on the Proxy.* | *Integer* | *5* |
| *ProxyPowerScope.IssuingAuthority* | *TBD* | *Name of the authority that is issuing the attestation.* | *String* | *Cleverbase* |
| *ProxyPowerScope.IssuingAuthorityType* | *TBD* | *Type of authority in accordance with the Trust Framework defined in the scope of eIDAS Regulation (QTSP, PubEAA, NQTSP)* | *Integer* | *0* |
| *ProxyPowerScope.IssuingCountry* | *TBD* | *Country where the attestation is being issued.* | *alpha-2 country code as specified in ISO 3166-1* | *ES* |
| *ProxyPowerScope.AssuranceLevel* | *TBD* | *Level of assurance and confidence that should be given to a statement based on the origin of the information. Since this attestation relies on a Business Registry the assurance level is always High.* | *Integer* | *0* |

### 2.3 Optional attributes

Optional attributes are grouped according to the common PoX semantic domains.

##### Domain 2.2 – Natural Entity Proxy

It will contain the optional information for natural person identification, ensuring identity matching while delegating full person information to the PID [CIR 2024/2977] with any possible modification approved in the context of WeBuild Consorcium, specifically through WP4 PID-EBWOID group.

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------|--------------|--------------|--------------|
| *NaturalEntityProxy.PersonalAdministrativeNumber* | *TBD* | *A value assigned to the natural person that is unique among all personal administrative numbers issued by the provider of person identification data. Where Member States opt to include this attribute, they shall describe in their electronic identification schemes under which the person identification data is issued, the policy that they apply to the values of this attribute, including, where applicable, specific conditions for the processing of this value.* | *String* | *76590327M* |
| *NaturalEntityProxy.Pseudonym* | *TBD* | *Fictitious or assumed name used by an individual, or online user, to conceal their real identity.* | *String* | *Employee-1234* |

##### Domain 3.2 ProxyPosition (Power of Representation | PoR)

This certifies the optional information regerding a specific position or role held by the representative of a legal person, in accordance with the data entered in the official register authorised by each Member State.

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------|--------------|--------------|--------------|
| *ProxyPosition.ExpirationDate* | *TBD* | *Specific date of expiration Issuanceof the power and the faculty it enables in the Proxy. The absence of this field implies that there is no expiration date.* | *date-time or full-date as specified in RFC 3339* | *2030-07-08T10:30:21.000Z* |
| *ProxyPosition.Cardinality* | *TBD* | *Number of concurrent proxies with the same Position required to carry out the operations referred to in the scope of execution of the operation that is intended to be performed. If not included, it is assumed that only one Proxy is needed to perform the action.* | *Integer* | *3* |
| *ProxyPosition.IssuingRegion* | *TBD* | *Region of a specific country where the attestation is being issued.* | *alpha-2 region code as specified in ISO 3166-2* | *MD* |

##### Domain 3.3 ProxyPowerScope (Power of Attorney | PoA )

This certifies the optional information regerding a specific scope and faculties of a Power of Attorney granted of a legal person, in accordance with the data entered in the official register authorised by each Member State.

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------|--------------|--------------|--------------|
| *ProxyPowerScope.ExpirationDate* | *TBD* | *Specific date of expiration of the power and the faculty it enables in the Proxy. The absence of this field implies that there is no expiration date.* | *date-time or full-date as specified in RFC 3339* | *2030-07-08T10:30:21.000Z* |
| *ProxyPowerScope.Cardinality* | *TBD* | *Number of concurrent proxies with the same faculties required to carry out the operations referred to in the scope of execution of the power. If not included, it is assumed that only one Proxy is needed to perform the action.* | *Integer* | *3* |
| *ProxyPowerScope.Constraints* | *TBD* | *In the cases where the Power is limited in its nature include the constraints. See Power.Constraints data structure. If not included, it is assumed that there are no constraints to be considered.* | *Json Object* | *See Constraints data structures below* |
| *ProxyPowerScope.GeographicalScope* | *TBD* | *Country where the attestation is enabled to be used. Exception is made for the case that the power is usable in the EU will use the labels “EU” that are not conformant with the ISO 3166-1. If not included, it is assumed that there are no limitations in this regard.* | *List of alpha-2 country code as specified in ISO 3166-1* | *DE,ES,NL* |
| *ProxyPowerScope.IssuingRegion* | *TBD* | *Region of a specific country where the attestation is being issued.* | *alpha-2 region code as specified in ISO 3166-2* | *MD* |
| *ProxyPowerScope.Mandator* | *TBD* | *The Mandator is the natural person that holds de PoR or PoA that entitles the empowerment of the subject.* | *Json Object* | *See Mandator data structures below* |
| *ProxyPowerScope.ServiceAccess* | *TBD* | *List of all the (digital) services to which the power holder is entitled to access.* | *Json Object* | *See ServiceAccess data structures below* |
| *ProxyPowerScope.AuthenticSourceId* | *TBD* | *Identification information with regard the authentic source that has the power and faculties registered.* | *String* | *VATES-E81458556* |
| *ProxyPowerScope.AuthenticSourceName* | *TBD* | *Name of the authentic source that has the power and faculties registered.* | *String* | *Registro Mercantil de Madrid* |
| *ProxyPowerScope.EvidenceURI* | *TBD* | *Address for accessing the public document certifying the power of representation.* | *String* | *https://sede.registradores.org/sede/sede-csv-web/csv/20815412F93A6D5B* |
| *ProxyPowerScope.EvidenceDescription* | *TBD* | *Description of the public document certifying the power of representation.* | *String* | *Business Registry Certification* |

##### Domain 3.3.1 Constraints

Operational restrictions on the use of power in accordance with its characteristics.

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------|--------------|--------------|--------------|
| *ProxyPowerScope.Constraint.Type* | *TBD* | *Types of limitations according to a finite list of areas of restriction in the actions of a company's representatives* | *String* | *Operational* |
| *ProxyPowerScope.Constraint.Description* | *TBD* | *Description of the limitations that apply to the exercise of power.* | *String* | *Prohibition to operate after business hours (8:00 to 17:00)* |

##### Domain 3.3.2 Mandator

The Mandator is the natural person that holds de PoR or PoA that entitles the empowerment of the subject. It will contain the minimum mandatory information for natural person identification, ensuring identity matching while delegating full person information to the PID [CIR 2024/2977]

| *ProxyPowerScope.Mandator.FamilyName* | *TBD* | *Current last name(s) or surname(s) of the user to whom the person identification data relates* | *String* | *Duck* |
| *ProxyPowerScope.Mandator.GivenName* | *TBD* | *Current first name(s), including middle name(s) where applicable, of the user to whom the person identification data relates.* | *String* | *Donald* |
| *ProxyPowerScope.Mandator. BirthDate* | *TBD* | *Day, month, and year on which the user to whom the person identification data relates was born.* | *date-time or full-date as specified in RFC 3339* | *1990-07-08T10:30:21.000Z* |
| *ProxyPowerScope.Mandator.BirthPlace* | *TBD* | *The country as an alpha-2 country code as specified in ISO 3166-1, or the state, province, district, or local area or the municipality, city, town, or village where the user to whom the person identification data relates was born.* | *alpha-2 country code as specified in ISO 3166-1* | *BE* |
| *ProxyPowerScope.Mandator.Nationality* | *TBD* | *One or more alpha-2 country codes as specified in ISO 3166-1, representing the nationality of the user to whom the person identification data relates.* | *BE* |

##### Domain 3.3.2 Service Access

Relying parties that provide online services that require some evidence of representation capabilities that enables the user to access an online service and / or operate within its boundaries.

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------|--------------|--------------|--------------|
| *ProxyPosition.ServiceAccess.RelyingPartyName* | *TBD* | *The name under which the Economic Operator is legally registered* | *String* | *Belastingdienst* |
| *ProxyPosition.ServiceAccess.RelyingPartyID* | *TBD* | *A unique identifier constructed by the sending Member State in accordance with the technical specifications for the purposes of cross-border identification and which is as persistent as possible in time.* | *String* | *NL000099998B57* |
| *ProxyPosition.ServiceAccess.RelyingPartyServices* | *TBD* | *List of service IDs or Names that the proxy is entitled to use. The specific semantics shall be provided by the relying party for it to be able to interpret the data* | *String* | *https://www.belastingdienst.nl/service1, https://www.belastingdienst.nl/serive2* |

### 2.4 Conditional attributes

*No conditional atributes in the context of the PoX attestation*

### 2.5 Mandatory metadata

Every attestation SHALL include at least the following metadata.

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------|--------------|--------------|--------------|
| *Serial Number* | *TBD* | *The serial number univocaly identifies an attestation MUST be a positive integer assigned by the Issuer to each attestation.  It MUST be unique for each attestation issued by a given issuer.  Issuers MUST force the serialNumber to be a non-negative integer.* | *Integer* | *1903bce34282776057558af9e9b77e2b* |
| *Signature* | *TBD* | *This field MUST contain the digital signature or seal of the attestation to ensure the identity of the issuer and the integrity of the data* | *Bit String* | *-* |
| *Issuer Key Identifier* | *TBD* | *The issuer key identifier field provides a means of identifying the public key corresponding to the private key used to sign an attestation* | *Integer* | *da723861400697e502f16d69db0401e9e70ca3e8* |
| *Validity* | *TBD* | *The attestation validity period is the time interval during which the CA warrants that it will maintain information about the status of the attestation.  The field is represented as a SEQUENCE of two dates: the date on which the attestation validity period begins (notBefore) and the date on which the attestation validity period ends (notAfter).  Both notBefore and notAfter may be encoded as UTCTime or GeneralizedTime.* | *UTCTime or GeneralizedTime* | *notBefore:1783577425Z, notAfter:1752041425Z* |
| *EAA Revocation List Distribution Points* | *TBD* | *The EAARL distribution points field identifies how EAA Revocation List information is obtained. The EAARL distribution points fild is a SEQUENCE of EAA Revocation List information* | *String Sequence* | *-* |
| *Schema ID* | *TBD* | *Globally unique, dot-separated decimal string based on the schema defined by the Internet Assigned Numbers Authority (IANA) to identify objects, network equipment, and digital protocols* | *String* | *1.3.6.1.7.1.7.2.3* |
| *Schema Version* | *TBD* | *This field describes the version of the encoded attestaions. Implementations SHOULD be prepared to accept any version attestation. At a minimum, conforming implementations MUST recognize version 1 attestations.* | *Integer* | *1* |
| *Schema Location* | *TBD* | *Internet address where information about the schema and the rulebook can be found in a trustworthy manner.* | *String* | *https://eidas.ec.europa.eu/efda/trust-services/browse/schema* |
| *Trust Anchor* | *TBD* | *Authoritative, inherently trusted entity that serves as the starting point for validating a chain of trust.* | *String* | *https://eidas.ec.europa.eu/efda/trust-services/browse/anchor* |

### 2.6 Optional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------|--------------|--------------|--------------|
| *Attestation Policies* | *TBD* | *The attestation policies field contains a sequence of one or more policy information terms, each of which consists of an object identifier (OID) and optional qualifiers.  Optional qualifiers, which MAY be present, are not expected to change the definition of the policy. A certificate policy OID MUST NOT appear more than once in a certificate policies extension.* | *String Sequence* | *1.3.6.1.5.5.7.2.1: https://eaa.provider.org/eaa_policy, 1.3.6.1.5.5.7.2.2: https://eaa.provider.org/privacy_policy, 1.3.6.1.5.5.7.2.3: http://eaa.provider.org/eaa_terms_of_use* |
| *Issuer Information Access* | *TBD* | *The issuer information access field indicates how to access information and services for the issuer of the attestation.  Information and services may include on-line validation services and EAA policy data.* | *String* | *https://eaa.provider.org* |
| *Language* | *TBD* | *Language of display metadata* | *alpha-2 country code as specified in ISO 3166-1* | *DE* |
| *Display Name* | *TBD* | *Human-readable attestation name* | *String* | *Power of Representation* |
| *Logo* | *TBD* | *Issuer or attestation logo* | *Bit String* | *-* |

### 2.7 Conditional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|------------------------|--------------------------|--------------|--------------|--------------|
| *cryptographically_bound_to* | *TBD* | *Required when device-bound attestation are used* | *-* | *-* |
| *qualified_certificate_reference* | *TBD* | *Required for QEAA where applicable* | *-* | *-* |

### 2.8 Code lists
| **Field name** | **Allowed values** | **Meaning** | **Source / vocabulary** | **Notes / extensibility** |
|----------------|--------------------|-------------|--------------------------|---------------------------|
| *`Proxy.EntityType`* | *`0`,`1`* | *`0:LegalEntityProxy` - minimum mandatory information for legal person identification, ensuring identity matching while delegating full company information to the EBW-OID [CIR 2024/2977],`1:NaturalEntityProxy`- minimum mandatory information for natural person identification, ensuring identity matching while delegating full person information to the PID [CIR 2024/2977] with any possible modification approved in the context of WeBuild Consortium, specifically through WP4 PID-EBWOID group.* | *ISA Business Core Vocabullary* | *There are no extensions allowed for this field* |
| *`ProxyPosition.Position`* | *`Sole Administrator`, `Supportive Administrator`, `Joint Administrator`, `Board Member`* | *`Sole Administrator`: An individual who is granted exclusive authority to manage, represent, and legally bind an organization. The Sole Administrator exercises all executive powers independently, without requiring approval or participation from any other administrator, `Supportive Administrator`: An administrator whose authority is exercised in support of another authorized administrator. A Supportive Administrator may perform delegated administrative functions or participate in decision-making but does not normally possess independent authority to bind the organization unless expressly authorized by applicable governance rules or delegation, `Joint Administrator`: An administrator who shares executive authority with one or more other administrators. Actions requiring joint administration are valid only when performed collectively in accordance with the organization's governing documents, typically requiring the approval or signatures of all, or a specified number of, Joint Administrators., `Board Member`: An individual appointed or elected to serve on the organization's board of directors or equivalent governing body. A Board Member participates in corporate governance by establishing strategic direction, overseeing management, approving significant decisions, and fulfilling fiduciary duties, but does not necessarily possess executive or representative authority unless separately appointed to an executive administrative role* | *ISA Business Core Vocabullary* | *There are no extensions allowed for this field* |
| *ProxyPosition.AssuranceLevel* | *`0`,`1`,`2`* | *`0:High` - assurance level high SHALL refer to an electronic identification means, which provides a higher degree of confidence in the claimed or asserted identity of a person than electronic identification means with the assurance level substantial, and is characterised with reference to technical specifications, standards and procedures related thereto, including technical controls, the purpose of which is to prevent misuse or alteration of the identity,`1:Substantial` - assurance level substantial SHALL refer to an electronic identification means, which provides a substantial degree of confidence in the claimed or asserted identity of a person, and is characterised with reference to technical specifications, standards and procedures related thereto, including technical controls, the purpose of which is to decrease substantially the risk of misuse or alteration of the identity,`2:Low` - assurance level low SHAL refer to an electronic identification means, which provides a limited degree of confidence in the claimed or asserted identity of a person, and is characterised with reference to technical specifications, standards and procedures related thereto, including technical controls, the purpose of which is to decrease the risk of misuse or alteration of the identity* | *eIDAS Regulatioon* | *There are no extensions allowed for this field* |
| *ProxyPowerScope.AssuranceLevel* | *`0`,`1`,`2`* | *`0:High` - assurance level high SHALL refer to an electronic identification means, which provides a higher degree of confidence in the claimed or asserted identity of a person than electronic identification means with the assurance level substantial, and is characterised with reference to technical specifications, standards and procedures related thereto, including technical controls, the purpose of which is to prevent misuse or alteration of the identity,`1:Substantial` - assurance level substantial SHALL refer to an electronic identification means, which provides a substantial degree of confidence in the claimed or asserted identity of a person, and is characterised with reference to technical specifications, standards and procedures related thereto, including technical controls, the purpose of which is to decrease substantially the risk of misuse or alteration of the identity,`2:Low` - assurance level low SHAL refer to an electronic identification means, which provides a limited degree of confidence in the claimed or asserted identity of a person, and is characterised with reference to technical specifications, standards and procedures related thereto, including technical controls, the purpose of which is to decrease the risk of misuse or alteration of the identity* | *eIDAS Regulatioon* | *There are no extensions allowed for this field* |
| *ProxyPosition.IssuingAuthorityType* | *`0`,`1`,`2`* | *`0:QEAA`,`1:PubEAA`,`2:EAA`* | *eIDAS Regulatioon* | *There are no extensions allowed for this field* |
| *ProxyPowerScope.IssuingAuthorityType* | *`0`,`1`,`2`* | *`0:QEAA`,`1:PubEAA`,`2:EAA`* | *eIDAS Regulatioon* | *There are no extensions allowed for this field* |
| *ProxyPowerScope.Type* | *`0`,`1`,`2`* | *`0:Organic Representation` - Directors or board members authorized by company bylaws to represent a business,`1:Voluntary Representation` - Authorized by an individual or company to a third party (attorney-in-fact) for specific or general,`2:Apud Acta` - A type of representation granted via personal or electronic appearance before a public body* | *ISA Business Core Vocabullary* | *There are no extensions allowed for this field* |
| *ProxyPowerScope.Limitation* | *`0 or False`, `1 or True`* | *`0 or False` - Unlimited, `1 or True` - Limited* | *-* | *There are no extensions allowed for this field* |
| *ProxyPowerScope.Faculty* | *`GENERAL`,`TAX`, `PROCUREMENT`, `CONTRACT`, `FINANCIAL`, `BANKING`, `LEGAL`, `DATA`, `OTHER`* | *`GENERAL`: General Power of Attorney,`TAX`: Tax representation, `PROCUREMENT`: Procurement authority, `CONTRACT`: Contract signature, `FINANCIAL`: Financial transactions, `BANKING`: Banking authority, `LEGAL`: Legal representation, `DATA`: Trusted Data Sharing for Data Spaces, `OTHER`: Other delegation* | *-* | *This is an initial list based on Usecases within WeBuild consortium. Extensions MAY be adopted by the usecases based on their specifications* |
| *ProxyPowerScope.Constraint.Type* | *`Economic`, `Operational`, `Other`* | *`Economic`: Economic limiting factors that modify the exercise of the power, such as the value of an acquisition, the value of an asset on which a transaction is being carried out, etc, `Operational`: reflects restrictions that must be taken into account when considering the execution of power, such as the concurrence of preconditions for certain operations, etc, `Other`: Any type of restriction that does not fit into the above categories* | *-* | *This is an initial list based on Usecases within WeBuild consortium. Extensions MAY be adopted by the usecases based on their specifications* |

### 2.9 Integrity rules

| **Rule ID** | **Rule statement** | **Why it exists** | **Where enforced** | **Verifier / issuer behavior on failure** |
|-------------|--------------------|-------------------|--------------------|-------------------------------------------|
| *IR-01* | *PoA and PoR attesttions SHALL include all mandatory attributes and MAY include any number of optional attributes* | *The attestations have to be complete so there is consistency and reliability in their use* | *Issuance / Verification* | *Abort issuance / Reject attestation* |
| *IR-02* | *`RepresentedEconomicOperator` SHALL exist only once in the attestation.* | *It is core that we know the identity of the economic operator that is being represented* | *Issuance / Verification* | *Abort issuance / Reject attestation* |
| *IR-03* | *`Proxy` SHALL exist only once in the attestation* | *It is core that we know the identity of the economic operator that is being acting on behalf of a company / economic operator.* | *Issuance / Verification* | *Abort issuance / Reject attestation* |
| *IR-04* | *`Proxy` SHAL contain either a Economic Operator Proxy or a Natural Entity Proxy in a mutually exclusive fashion* | *Ensure that there is just one representative / attorney included in the attestation* | *Issuance / Verification* | *Abort issuance / Reject attestation* |
| *IR-05* | *PoA and PoR attesttions SHALL include either a `ProxyPosition` or a `ProxyPowerScope` data structure* | *A PoX attestation can either be a PoA, specified through `ProxyPowerScope` data structure, or a PoR, specified through `ProxyPosition` data structure, not being possible to be simultaneously a PoA and PoR* | *Issuance / Verification* | *Abort issuance / Reject attestation* |
| *IR-06* | *When issuing a QEAA the issuer MUST be verified against authentic sources either directly by the qualified trust service provider or by means of designated intermediaries recognised at national level in accordance with Union or national law for the purpose of secure exchange of attested attributes between identity or attestation of attributes’ service providers and relying parties* | *The information contained in QEAA must be accurate and reliable so the relying parties can trust them* | *Issuance / Verification* | *Abort issuance / Reject attestation* |
| *IR-07* | *On QEAA for `ProxyPosition` the fields `AuthenticSourceId` and `AuthenticSourceName` SHALL be included despite being optional* | *There is a need to keep the chain to the Authentic Sources* | *Issuance / Verification* | *Abort issuance / Reject attestation* |
| *IR-08* | *On QEAA for `ProxyPowerScope` the fields `AuthenticSourceId` and `AuthenticSourceName` SHALL be included despite being optional* | *There is a need to keep the chain to the Authentic Sources* | *Issuance / Verification* | *Abort issuance / Reject attestation* |
| *IR-09* | *On QEAA for `ProxyPosition` the fields `EvidenceURI` and `EvidenceDescription` SHALL be included despite being optional* | *There is a need to keep the chain to the Authentic Sources' information* | *Issuance / Verification* | *Abort issuance / Reject attestation* |
| *IR-10* | *On QEAA for `ProxyPowerScope` the fields `EvidenceURI` and `EvidenceDescription` SHALL be included despite being optional* | *There is a need to keep the chain to the Authentic Sources' information* | *Issuance / Verification* | *Abort issuance / Reject attestation* |
| *IR-11* | *All data elements that depend on 'code lists' as defined in the current rulebook SHALL use those values* | *Need for a common data shcema to ensure interoperability* | *Issuance / Verification* | *Abort issuance / Reject attestation* |
| *IR-12* | *When `ProxyPowerScope` indicates that the PoA has resctrictions (`ProxyPowerScope.Limitation = 1 or True`) either the value `ProxyPowerScope.Faculty` or `ProxyPowerScope.ServiceAccess` SHALL exist* | *When there are limitations to the capacity of acting on behalf of the company is of vital importance to let the relying parties know which are the specific limitations.* | *Issuance / Verification* | *Abort issuance / Reject attestation* |
| *IR-13* | *In the `validity` attribute in the attestation's metadata the value `notBefore` SHALL precede `notAfter`* | *The attestation needts to be valid within an specific timeframe* | *Verification* | *Reject attestation* |
| *IR-14* | *Revoked attestations SHALL NOT be accepted by a Relying Party* | *Powers of Attorney and Powers of Representation need to be current and valid to generate legally binding actions* | *Verification* | *Reject attestation* |
| *IR-15* | *Expired attestations SHALL NOT be accepted by a Relying Party* | *Powers of Attorney and Powers of Representation need to be current and valid to generate legally binding actions* | *Verification* | *Reject attestation* |
| *IR-16* | *Issuer SHALL be trusted according to Section 5* | *There needs to be a correlation with the trust framework defined in the eIDAS regulation* | *-* | *-* |
| *IR-17* | *Attestation signature SHALL validate successfully* | *Integrity of the attestation as well as the binding with the trust anchor is vital to mantain trustworthiness in the ecosystem* | *Verification* | *Reject attestation* |
| *IR-18* | *A mandate SHALL NOT authorize actions outside its defined scope* | *Based on business rules a Proxy is authorized to do a limited set of acctions according to risk and operational requirements* | *Verification* | *Reject action* |
| *IR-19* | *Every attestation SHALL reference exactly one issuing authority* | *Operationaly there can not be a binding with more than one authority* | *Verification* | *Reject attestation* |
| *IR-20* | *Every attestation SHALL contain exactly one unique attestation identifier* | *We need to ensure attestation uniqueness across the ecosystem* | *Issuance / Verification* | *Abort issuance / Reject attestation* |

# 3 Attestation encoding

## 3.1 ISO/IEC 18013-5-compliant encoding

> ISO/IEC 18013-5-compliant Verifiable Credentials are not part of PoX attestations priority within WE BUILD, as we concentrate mainly on SD/JWT, mDoc for proximity use cased will be developed if and when needed

### 3.2 SD-JWT VC-based encoding

### 3.2.1 Human-readable Payload Example

> PERSONAS & ROLES used in examples
> 
> Bianca (Beratung) is our tax advisor to whom PoA is granted
> 
> Hans Schreiner GmbH is our company who grants PoA
> 
> Hans (Schreiner) is our sole shareholder and managing director of Hans Schreiner GmbH


##### 3.2.1.1 Canonical Information Model
*** DRAFT STATUS ***

```json
{
  "model": {
    "name": "WE BUILD Power of X Canonical Information Model",
    "version": "7.0.0",
    "namespace": "https://credentials.webuild.eu/power-of-x/v7",
    "credential_profile": "SD-JWT VC",
    "status": "working-draft",
    "source": "WE BUILD Rulebook Chapter 2"
  },
  "credential": {
    "vct": "https://credentials.webuild.eu/power-of-x/v7",
    "type": "",
    "legal_category": ""
  },
  "represented_economic_operator": {
    "identifier": {
      "scheme": "",
      "value": ""
    },
    "legal_name": ""
  },
  "proxy": {
    "entity_type": "",
    "legal_entity_proxy": {
      "identifier": {
        "scheme": "",
        "value": ""
      },
      "legal_name": ""
    },
    "natural_entity_proxy": {
      "family_name": "",
      "given_name": "",
      "birth_date": "",
      "birth_place": "",
      "nationality": [],
      "personal_administrative_number": "",
      "pseudonym": ""
    }
  },
  "authority": {
    "authority_source": "",
    "proxy_position": {
      "position": "",
      "inscription_date": "",
      "expiration_date": "",
      "cardinality": 1,
      "issuing_authority": {
        "name": "",
        "type": "",
        "country": "",
        "region": ""
      },
      "authentic_source": {
        "id": "",
        "name": ""
      },
      "evidence": {
        "uri": "",
        "description": ""
      },
      "assurance_level": ""
    },
    "proxy_power_scope": {
      "type": "",
      "grant_date": "",
      "expiration_date": "",
      "limitation": false,
      "faculty": [],
      "cardinality": 1,
      "constraints": [],
      "geographical_scope": [],
      "mandator": {
        "family_name": "",
        "given_name": "",
        "birth_date": "",
        "birth_place": "",
        "nationality": []
      },
      "service_access": [
        {
          "relying_party_name": "",
          "relying_party_id": "",
          "relying_party_services": []
        }
      ],
      "issuing_authority": {
        "name": "",
        "type": "",
        "country": "",
        "region": ""
      },
      "authentic_source": {
        "id": "",
        "name": ""
      },
      "evidence": {
        "uri": "",
        "description": ""
      },
      "assurance_level": ""
    },
    "proxy_employee_authorisation": {}
  },
  "credential_metadata": {
    "issuer": {
      "iss": "",
      "issuer_key_identifier": ""
    },
    "validity": {
      "iat": "",
      "not_before": "",
      "not_after": ""
    },
    "status": {
      "serial_number": "",
      "status_endpoint": "",
      "revocation_distribution_points": []
    },
    "binding": {
      "cryptographically_bound_to": "",
      "cnf": {}
    },
    "trust": {
      "trust_anchor": "",
      "qualified_certificate_reference": ""
    },
    "schema": {
      "id": "",
      "version": "7.0.0",
      "location": ""
    },
    "display": {
      "language": "en",
      "name": "WE BUILD Power of X",
      "logo": ""
    },
    "policies": []
  }
}

```


##### 3.2.1.2 JSON Schema 
*** DRAFT STATUS ***

```json

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://schemas.webuild.eu/power-of-x/power_of_x.schema.v1.json",
  "title": "WE BUILD Power of X Credential",
  "description": "JSON Schema derived from Canonical Model V7",
  "type": "object",
  "required": [
    "vct",
    "credential",
    "represented_economic_operator",
    "proxy",
    "authority",
    "credential_metadata"
  ],
  "properties": {
    "vct": {
      "type": "string",
      "format": "uri"
    },
    "credential": {
      "type": "object",
      "required": [
        "type",
        "legal_category"
      ],
      "properties": {
        "type": {
          "type": "string",
          "enum": [
            "power_of_attorney",
            "power_of_representation",
            "power_of_employee"
          ]
        },
        "legal_category": {
          "type": "string",
          "enum": [
            "QEAA",
            "PubEAA",
            "non-qualified-EAA"
          ]
        }
      }
    },
    "represented_economic_operator": {
      "type": "object",
      "required": [
        "identifier",
        "legal_name"
      ],
      "properties": {
        "identifier": {
          "type": "object",
          "required": [
            "scheme",
            "value"
          ],
          "properties": {
            "scheme": {
              "const": "EBWOID"
            },
            "value": {
              "type": "string"
            }
          }
        },
        "legal_name": {
          "type": "string"
        }
      }
    },
    "proxy": {
      "type": "object",
      "required": [
        "entity_type"
      ],
      "properties": {
        "entity_type": {
          "type": "string",
          "enum": [
            "natural_entity",
            "legal_entity"
          ]
        },
        "legal_entity_proxy": {
          "type": "object"
        },
        "natural_entity_proxy": {
          "type": "object"
        }
      }
    },
    "authority": {
      "type": "object",
      "required": [
        "authority_source"
      ],
      "properties": {
        "authority_source": {
          "type": "string",
          "enum": [
            "proxy_position",
            "proxy_power_scope",
            "proxy_employee_authorisation"
          ]
        },
        "proxy_position": {
          "type": "object"
        },
        "proxy_power_scope": {
          "type": "object"
        },
        "proxy_employee_authorisation": {
          "type": "object"
        }
      }
    },
    "credential_metadata": {
      "type": "object",
      "properties": {
        "issuer": {
          "type": "object"
        },
        "validity": {
          "type": "object"
        },
        "status": {
          "type": "object"
        },
        "binding": {
          "type": "object"
        },
        "trust": {
          "type": "object"
        },
        "schema": {
          "type": "object"
        },
        "display": {
          "type": "object"
        },
        "policies": {
          "type": "array"
        }
      }
    }
  },
  "allOf": [
    {
      "oneOf": [
        {
          "properties": {
            "authority": {
              "properties": {
                "authority_source": {
                  "const": "proxy_position"
                }
              }
            }
          }
        },
        {
          "properties": {
            "authority": {
              "properties": {
                "authority_source": {
                  "const": "proxy_power_scope"
                }
              }
            }
          }
        },
        {
          "properties": {
            "authority": {
              "properties": {
                "authority_source": {
                  "const": "proxy_employee_authorisation"
                }
              }
            }
          }
        }
      ]
    }
  ]
}

```


##### 3.2.1.3 Specification Bundle with reference to section 2
*** DRAFT We BUILD Power of X spec with reference to rulebook sections ***

```json
{
  "specification": {
    "name": "WE BUILD Power of X Specification Bundle",
    "version": "4.0.0",
    "status": "working-draft",
    "namespace": "https://credentials.webuild.eu/power-of-x/v7",
    "based_on": [
      "WE BUILD Rulebook Chapter 2",
      "WE BUILD Rulebook Chapter 3",
      "Canonical Model V7"
    ]
  },
  "domains": {
    "represented_economic_operator": {
      "rulebook": "2.2 Domain 1",
      "required": true,
      "attributes": [
        "identifier",
        "legal_name"
      ]
    },
    "proxy": {
      "rulebook": "2.2 Domain 2",
      "required": true,
      "attributes": [
        "entity_type",
        "natural_entity_proxy",
        "legal_entity_proxy"
      ]
    },
    "authority": {
      "rulebook": "2.2 Domain 3",
      "required": true,
      "attributes": [
        "proxy_position",
        "proxy_power_scope",
        "proxy_employee_authorisation"
      ]
    },
    "credential_metadata": {
      "rulebook": "2.5-2.7",
      "required": true
    }
  },
  "attribute_catalog": {
    "represented_economic_operator.identifier": {
      "datatype": "Identifier",
      "cardinality": "1",
      "rulebook": "2.2 Domain 1"
    },
    "represented_economic_operator.legal_name": {
      "datatype": "string",
      "cardinality": "1",
      "rulebook": "2.2 Domain 1"
    },
    "proxy.entity_type": {
      "datatype": "enum",
      "cardinality": "1",
      "rulebook": "2.2 Domain 2"
    },
    "authority.authority_source": {
      "datatype": "enum",
      "cardinality": "1",
      "rulebook": "2.2 Domain 3"
    },
    "credential_metadata.validity": {
      "datatype": "object",
      "cardinality": "1",
      "rulebook": "2.5"
    }
  },
  "code_lists": {
    "entity_type": [
      "natural_entity",
      "legal_entity"
    ],
    "authority_source": [
      "proxy_position",
      "proxy_power_scope",
      "proxy_employee_authorisation"
    ],
    "legal_category": [
      "QEAA",
      "PubEAA",
      "non-qualified-EAA"
    ],
    "assurance_level": [
      "HIGH",
      "SUBSTANTIAL",
      "LOW"
    ]
  },
  "integrity_rules": [
    {
      "id": "IR-01",
      "rule": "Mandatory domains SHALL be present."
    },
    {
      "id": "IR-02",
      "rule": "Exactly one represented economic operator SHALL exist."
    },
    {
      "id": "IR-03",
      "rule": "Exactly one proxy SHALL exist."
    },
    {
      "id": "IR-04",
      "rule": "Proxy SHALL be either natural entity or Economic Operator."
    },
    {
      "id": "IR-05",
      "rule": "Exactly one authority source SHALL be present."
    }
  ],
  "artifacts": {
    "canonical_model": "available",
    "json_schema": "available",
    "type_metadata": "available",
    "poa_example": "planned",
    "por_example": "planned",
    "mapping": "planned"
  },
  "changelog": [
    {
      "version": "4.0.0",
      "changes": [
        "Added attribute catalog",
        "Added rulebook references at attribute level",
        "Prepared normative model for JSON Schema generation"
      ]
    }
  ]
}
```


##### 3.2.1.4 SD-JWT VC Type Metadata 
*** DRAFT We BUILD Power of X metadata spec with reference to rulebook sections ***

```json
{
  "vct": "https://credentials.webuild.eu/power-of-x/v7",
  "name": "WE BUILD Power of X",
  "description": "Type Metadata for WE BUILD Power of X credentials",
  "extends": null,
  "display": [
    {
      "lang": "en",
      "name": "WE BUILD Power of X",
      "description": "Power of Attorney, Power of Representation and Power of Employee"
    }
  ],
  "schema_uri": "https://schemas.webuild.eu/power-of-x/power_of_x.schema.v1.json",
  "cryptographic_binding_methods_supported": [
    "jwk",
    "cose_key"
  ],
  "credential_signing_alg_values_supported": [
    "ES256",
    "EdDSA"
  ],
  "hash_alg_values_supported": [
    "sha-256"
  ],
  "claims": [
    {
      "path": [
        "credential",
        "type"
      ],
      "mandatory": true,
      "sd": "never",
      "value_type": "string"
    },
    {
      "path": [
        "credential",
        "legal_category"
      ],
      "mandatory": true,
      "sd": "never",
      "value_type": "string"
    },
    {
      "path": [
        "represented_economic_operator",
        "identifier",
        "value"
      ],
      "mandatory": true,
      "sd": "allowed",
      "value_type": "string"
    },
    {
      "path": [
        "represented_economic_operator",
        "legal_name"
      ],
      "mandatory": true,
      "sd": "allowed",
      "value_type": "string"
    },
    {
      "path": [
        "proxy",
        "entity_type"
      ],
      "mandatory": true,
      "sd": "never",
      "value_type": "string"
    },
    {
      "path": [
        "proxy",
        "natural_entity_proxy"
      ],
      "mandatory": false,
      "sd": "allowed",
      "value_type": "object"
    },
    {
      "path": [
        "proxy",
        "legal_entity_proxy"
      ],
      "mandatory": false,
      "sd": "allowed",
      "value_type": "object"
    },
    {
      "path": [
        "authority",
        "authority_source"
      ],
      "mandatory": true,
      "sd": "never",
      "value_type": "string"
    },
    {
      "path": [
        "authority",
        "proxy_position"
      ],
      "mandatory": false,
      "sd": "allowed",
      "value_type": "object"
    },
    {
      "path": [
        "authority",
        "proxy_power_scope"
      ],
      "mandatory": false,
      "sd": "allowed",
      "value_type": "object"
    },
    {
      "path": [
        "authority",
        "proxy_employee_authorisation"
      ],
      "mandatory": false,
      "sd": "allowed",
      "value_type": "object"
    },
    {
      "path": [
        "credential_metadata"
      ],
      "mandatory": true,
      "sd": "never",
      "value_type": "object"
    }
  ]
}
```

##### 3.2.1.5 Canonical Reference Credential PoA
*** DRAFT CANONICAL REFERENCE EXAMPLE PoA ***

```json
{
  "vct": "https://credentials.webuild.eu/power-of-x/v7",
  "credential": {
    "type": "power_of_attorney",
    "legal_category": "QEAA"
  },
  "represented_economic_operator": {
    "identifier": {
      "scheme": "EBWOID",
      "value": "EU-DE-HRB-123456"
    },
    "legal_name": "Hans Schreiner GmbH"
  },
  "proxy": {
    "entity_type": "natural_entity",
    "natural_entity_proxy": {
      "family_name": "Beratung (Counselor)",
      "given_name": "Bianca",
      "birth_date": "1987-04-11",
      "birth_place": "Nuremberg",
      "nationality": [
        "DE"
      ],
      "personal_administrative_number": "PID-DE-123456789",
      "pseudonym": "TaxAdvisor01"
    }
  },
  "authority": {
    "authority_source": "proxy_power_scope",
    "proxy_power_scope": {
      "type": "voluntary_representation",
      "grant_date": "2026-07-01",
      "expiration_date": "2027-07-01",
      "limitation": true,
      "faculty": [
        "TAX",
        "FINANCIAL"
      ],
      "cardinality": 1,
      "constraints": [
        {
          "type": "Operational",
          "description": "Tax filings only"
        },
        {
          "type": "Economic",
          "description": "Maximum transaction amount EUR 100000"
        }
      ],
      "geographical_scope": [
        "DE",
        "AT",
        "NL"
      ],
      "mandator": {
        "family_name": "Schreiner",
        "given_name": "Hans",
        "birth_date": "1975-02-18",
        "birth_place": "Nuremberg",
        "nationality": [
          "DE"
        ]
      },
      "service_access": [
        {
          "relying_party_name": "DATEV",
          "relying_party_id": "DE-DATEV",
          "relying_party_services": [
            "Tax Filing",
            "VAT Declaration"
          ]
        },
        {
          "relying_party_name": "German Tax Authority",
          "relying_party_id": "DE-FIN",
          "relying_party_services": [
            "Corporate Tax",
            "Income Tax"
          ]
        }
      ],
      "issuing_authority": {
        "name": "WE BUILD QTSP",
        "type": "QEAA",
        "country": "DE",
        "region": "BY"
      },
      "authentic_source": {
        "id": "DE-BR-001",
        "name": "German Business Register"
      },
      "evidence": {
        "uri": "https://example.org/evidence/4711",
        "description": "Notarial Power of Attorney"
      },
      "assurance_level": "HIGH"
    }
  },
  "credential_metadata": {
    "issuer": {
      "iss": "https://issuer.webuild.eu",
      "issuer_key_identifier": "kid-001"
    },
    "validity": {
      "iat": "2026-07-14T10:00:00Z",
      "not_before": "2026-07-14T10:00:00Z",
      "not_after": "2027-07-01T00:00:00Z"
    },
    "status": {
      "serial_number": "POX-2026-000001",
      "status_endpoint": "https://status.webuild.eu/pox",
      "revocation_distribution_points": [
        "https://status.webuild.eu/pox/rl"
      ]
    },
    "binding": {
      "cryptographically_bound_to": "urn:eudi:pid:1",
      "cnf": {
        "jwk": {
          "kty": "EC",
          "crv": "P-256",
          "alg": "ES256"
        }
      }
    },
    "trust": {
      "trust_anchor": "https://eidas.ec.europa.eu",
      "qualified_certificate_reference": "QC-DE-12345"
    },
    "schema": {
      "id": "https://schemas.webuild.eu/power-of-x/v7",
      "version": "7.0.0",
      "location": "https://schemas.webuild.eu/power-of-x"
    },
    "display": {
      "language": "en",
      "name": "WE BUILD Power of X",
      "description": "Normative Reference Credential"
    },
    "policies": [
      "https://webuild.eu/policies/pox"
    ],
    "references": {
      "rulebook": "Chapter 2",
      "canonical_model": "V7",
      "json_schema": "power_of_x.schema.v1.json",
      "type_metadata": "power_of_x.type_metadata.v1.json"
    }
  }
}

```

##### 3.2.1.6 SD-JWT VC Reference Credential PoA
*** DRAFT FULL EXAMPLE PoA ***

```json
{
  "iss": "https://issuer.webuild.eu",
  "vct": "https://credentials.webuild.eu/power-of-x/v7",
  "iat": 1784023200,
  "nbf": 1784023200,
  "exp": 1815559200,
  "jti": "urn:uuid:11111111-1111-1111-1111-111111111111",
  "status": {
    "status_list": "https://status.webuild.eu/statuslists/pox/1",
    "status_index": 41
  },
  "cnf": {
    "jwk": {
      "kty": "EC",
      "crv": "P-256",
      "alg": "ES256"
    }
  },
  "credential": {
    "type": "power_of_attorney",
    "legal_category": "QEAA"
  },
  "represented_economic_operator": {
    "identifier": {
      "scheme": "EBWOID",
      "value": "EU-DE-HRB-123456"
    },
    "legal_name": "Hans Schreiner GmbH"
  },
  "proxy": {
    "entity_type": "natural_entity",
    "natural_entity_proxy": {
      "family_name": "Beratung (Counselor)",
      "given_name": "Bianca",
      "birth_date": "1987-04-11",
      "birth_place": "Nuremberg",
      "nationality": [
        "DE"
      ],
      "personal_administrative_number": "PID-DE-123456789",
      "pseudonym": "TaxAdvisor01"
    }
  },
  "authority": {
    "authority_source": "proxy_power_scope",
    "proxy_power_scope": {
      "type": "voluntary_representation",
      "grant_date": "2026-07-01",
      "expiration_date": "2027-07-01",
      "limitation": true,
      "faculty": [
        "TAX",
        "FINANCIAL"
      ],
      "cardinality": 1,
      "constraints": [
        {
          "type": "Operational",
          "description": "Tax filings only"
        },
        {
          "type": "Economic",
          "description": "Maximum transaction amount EUR 100000"
        }
      ],
      "geographical_scope": [
        "DE",
        "AT",
        "NL"
      ],
      "mandator": {
        "family_name": "Schreiner",
        "given_name": "Hans",
        "birth_date": "1975-02-18",
        "birth_place": "Nuremberg",
        "nationality": [
          "DE"
        ]
      },
      "service_access": [
        {
          "relying_party_name": "DATEV",
          "relying_party_services": [
            "Tax Filing",
            "VAT Declaration"
          ]
        },
        {
          "relying_party_name": "German Tax Authority",
          "relying_party_services": [
            "Corporate Tax",
            "Income Tax"
          ]
        }
      ],
      "issuing_authority": {
        "name": "WE BUILD QTSP",
        "type": "QEAA",
        "country": "DE",
        "region": "BY"
      },
      "authentic_source": {
        "id": "DE-BR-001",
        "name": "German Business Register"
      },
      "evidence": {
        "uri": "https://example.org/evidence/4711",
        "description": "Notarial Power of Attorney"
      },
      "assurance_level": "HIGH"
    }
  },
  "credential_metadata": {
    "schema": {
      "id": "https://schemas.webuild.eu/power-of-x/v7",
      "version": "7.0.0"
    },
    "display": {
      "language": "en",
      "name": "WE BUILD Power of Attorney"
    },
    "policies": [
      "https://webuild.eu/policies/pox"
    ]
  },
  "_sd_alg": "sha-256",
  "_sd": [
    "<digest:represented_economic_operator.identifier>",
    "<digest:represented_economic_operator.legal_name>",
    "<digest:proxy.natural_entity_proxy.family_name>",
    "<digest:proxy.natural_entity_proxy.given_name>",
    "<digest:authority.proxy_power_scope>",
    "<digest:authority.proxy_power_scope.mandator>",
    "<digest:authority.proxy_power_scope.service_access>"
  ]
}

```



#### 3.2.1.7 Canonical Reference Credential PoR
*** DRAFT CANONICAL REFERENCE EXAMPLE PoR ***

```json
{
  "vct": "https://credentials.webuild.eu/power-of-x/v7",
  "credential": {
    "type": "power_of_representation",
    "legal_category": "QEAA"
  },
  "represented_economic_operator": {
    "identifier": {
      "scheme": "EBWOID",
      "value": "EU-DE-HRB-123456"
    },
    "legal_name": "Hans Schreiner GmbH"
  },
  "proxy": {
    "entity_type": "natural_entity",
    "natural_entity_proxy": {
      "family_name": "Schreiner",
      "given_name": "Hans",
      "birth_date": "1975-02-18",
      "birth_place": "Nuremberg",
      "nationality": [
        "DE"
      ]
    }
  },
  "authority": {
    "authority_source": "proxy_position",
    "proxy_position": {
      "position": "Sole Administrator",
      "inscription_date": "2024-01-15",
      "expiration_date": "",
      "cardinality": 1,
      "issuing_authority": {
        "name": "WE BUILD QTSP",
        "type": "QEAA",
        "country": "DE",
        "region": "BY"
      },
      "authentic_source": {
        "id": "DE-BR-001",
        "name": "German Business Register"
      },
      "evidence": {
        "uri": "https://example.org/register/123456",
        "description": "Commercial Register Extract"
      },
      "assurance_level": "HIGH"
    }
  },
  "credential_metadata": {
    "issuer": {
      "iss": "https://issuer.webuild.eu",
      "issuer_key_identifier": "kid-001"
    },
    "validity": {
      "iat": "2026-07-14T10:00:00Z",
      "not_before": "2026-07-14T10:00:00Z",
      "not_after": "2027-07-01T00:00:00Z"
    },
    "status": {
      "serial_number": "POX-2026-000001",
      "status_endpoint": "https://status.webuild.eu/pox",
      "revocation_distribution_points": [
        "https://status.webuild.eu/pox/rl"
      ]
    },
    "binding": {
      "cryptographically_bound_to": "urn:eudi:pid:1",
      "cnf": {
        "jwk": {
          "kty": "EC",
          "crv": "P-256",
          "alg": "ES256"
        }
      }
    },
    "trust": {
      "trust_anchor": "https://eidas.ec.europa.eu",
      "qualified_certificate_reference": "QC-DE-12345"
    },
    "schema": {
      "id": "https://schemas.webuild.eu/power-of-x/v7",
      "version": "7.0.0",
      "location": "https://schemas.webuild.eu/power-of-x"
    },
    "display": {
      "language": "en",
      "name": "WE BUILD Power of X",
      "description": "Normative Reference Credential"
    },
    "policies": [
      "https://webuild.eu/policies/pox"
    ],
    "references": {
      "rulebook": "Chapter 2",
      "canonical_model": "V7",
      "json_schema": "power_of_x.schema.v1.json",
      "type_metadata": "power_of_x.type_metadata.v1.json"
    }
  }
}

```

##### 3.2.1.8 SD-JWT VC Reference Credential PoR
*** DRAFT FULL EXAMPLE PoR ***
```json
{
  "iss": "https://issuer.webuild.eu",
  "vct": "https://credentials.webuild.eu/power-of-x/v7",
  "iat": 1784023200,
  "nbf": 1784023200,
  "exp": 1815559200,
  "jti": "urn:uuid:22222222-2222-2222-2222-222222222222",
  "status": {
    "status_list": "https://status.webuild.eu/statuslists/pox/1",
    "status_index": 42
  },
  "cnf": {
    "jwk": {
      "kty": "EC",
      "crv": "P-256",
      "alg": "ES256"
    }
  },
  "credential": {
    "type": "power_of_representation",
    "legal_category": "QEAA"
  },
  "represented_economic_operator": {
    "identifier": {
      "scheme": "EBWOID",
      "value": "EU-DE-HRB-123456"
    },
    "legal_name": "Hans Schreiner GmbH"
  },
  "proxy": {
    "entity_type": "natural_entity",
    "natural_entity_proxy": {
      "family_name": "Schreiner",
      "given_name": "Hans",
      "birth_date": "1975-02-18",
      "birth_place": "Nuremberg",
      "nationality": [
        "DE"
      ]
    }
  },
  "authority": {
    "authority_source": "proxy_position",
    "proxy_position": {
      "position": "Sole Administrator",
      "inscription_date": "2024-01-15",
      "expiration_date": "",
      "cardinality": 1,
      "issuing_authority": {
        "name": "WE BUILD QTSP",
        "type": "QEAA",
        "country": "DE",
        "region": "BY"
      },
      "authentic_source": {
        "id": "DE-BR-001",
        "name": "German Business Register"
      },
      "evidence": {
        "uri": "https://example.org/register/123456",
        "description": "Commercial Register Extract"
      },
      "assurance_level": "HIGH"
    }
  },
  "credential_metadata": {
    "schema": {
      "id": "https://schemas.webuild.eu/power-of-x/v7",
      "version": "7.0.0"
    },
    "display": {
      "language": "en",
      "name": "WE BUILD Power of Representation"
    },
    "policies": [
      "https://webuild.eu/policies/pox"
    ]
  },
  "_sd_alg": "sha-256",
  "_sd": [
    "<digest:represented_economic_operator.identifier>",
    "<digest:represented_economic_operator.legal_name>",
    "<digest:proxy.natural_entity_proxy.family_name>",
    "<digest:proxy.natural_entity_proxy.given_name>",
    "<digest:authority.proxy_position>"
  ]
}

```



### 3.3.2 Mandatory JWT Claims

| Claim | Description | Selectively Disclosable |
|-------|-------------|-------------------------|
| iss | Issuer. | NO |
| sub | Holder. | NO |
| iat | Issuance time. | NO |
| exp | Expiration time. | NO |
| vct | Credential type. | NO |


> NOTE
> The Canonical Information Model separates business metadata from transport metadata.
> Standard JWT claims (iss, sub, iat, exp, jti, cnf, status) remain top-level
> SD-JWT VC claims, whereas business-related metadata are represented inside
> credential_metadata.



### 3.3.3 Private Claims

| Claim | Type | Selectively Disclosable |
|-------|------|-------------------------|
| poa_id | string | YES |
| principal | object | YES |
| representative | object | YES |
| represented_entity | object | YES |
| mandate | object | YES |
| legal_basis | string | YES |
| scope | array | YES |
| restrictions | object | YES |
| jurisdiction | string | YES |






### 3.3.5 Selective Disclosure Policy

The following claims SHOULD be selectively disclosable:

- representative details;
- scope;
- restrictions;
- jurisdiction;
- professional registration;
- financial limits.

The following claims SHALL NOT be selectively disclosable:

- issuer;
- credential identifier;
- credential type;
- expiration;
- issue date;
- credential status.

### 3.3 W3C Verifiable Credentials Data Model-based encoding

> W3C Verifiable Credentials are not part of PoX attestations within WE BUILD, as we concentrate mainly on SD/JWT (mdoc for proximity use cased where applicable) 

## 3.4 Encoding Consistency Rules

| Rule  | Description |
|------ |-------------|
| EC-01 | Every credential SHALL contain one unique identifier. |
| EC-02 | Every credential SHALL identify exactly one Principal. |
| EC-03 | Every credential SHALL identify exactly one Attorney-in-Fact. |
| EC-04 | Every credential SHALL identify one represented organization. |
| EC-05 | Credential semantics SHALL remain identical across encodings. |
| EC-06 | Every credential SHALL contain validity information. |
| EC-07 | Every credential SHALL reference credential status information. |
| EC-08 | Every credential SHALL support cryptographic verification. |

## 3.5 Selective Disclosure Requirements

Power of Attorney credentials contain legally sensitive information. Issuers SHOULD maximize use of selective disclosure mechanisms. A Holder SHOULD disclose only those attributes required by the transaction.

## 3.6 Privacy Considerations

Issuers SHALL apply the principle of data minimization. Wallets SHALL support selective disclosure where supported by the credential format. Relying Parties SHALL request only attributes necessary for the requested transaction.

## 3.7 Encoding Interoperability

A Power of Attorney issued in one supported encoding SHALL be semantically equivalent to the same credential issued in another encoding.

Wallets MAY internally convert between supported encodings provided that no semantic information is lost, cryptographic integrity is preserved, issuer authenticity remains verifiable and selective disclosure policies remain enforceable.

# 4 Attestation Usage

| Usecase | Description            | PID / LPID verification through RP needed    | device bound and cryptographically bound to another type of attestation on the same Wallet Unit   |   
|---      |----                    | ---                                          | ---             |
| 1a       | A person (e.g. a tax advisor) uses the business wallet (EUBW), authenticated via EUDIW/PID, to obtain a PoA attestation issued by a QTSP/issuer from an authentic source — to later act on behalf of a company cross-border | SHALL  | MAY   |   
| 1b       | A person (e.g. a company person) uses the business wallet (EUBW), authenticated via EUDIW/PID, to obtain a PoR attestation issued by a QTSP/issuer from an authentic source — to later act on behalf of a company cross-border | SHALL  | MAY  |   
| 1c       | A person (e.g. a tax advisor) uses the business wallet (EUBW), authenticated via EUDIW/PID, to obtain a PoA attestation issued by a QTSP/issuer from an authentic source — to later act on behalf of a company cross-border | SHOULD | MAY |   

For detailed scenario description please review https://github.com/webuild-consortium/BU4/blob/main/scenarios/

#### Usecase 1a A person action on behalf of an organisation with PoA

#### Usecase 1b A person action on behalf of an organisation with PoR

#### Usecase 1c A person action on behalf of an organisation with PoA, PoR accessing a service 

## 4.1 Purpose

This chapter specifies how a Power of Attorney attestation SHALL be used within the WE BUILD ecosystem throughout its operational lifecycle.

The lifecycle comprises four principal phases:

1. issuance;
2. storage;
3. presentation;
4. verification.

Each phase SHALL preserve the legal meaning, integrity and trustworthiness of the delegated authority.

## 4.2 Operational Lifecycle

``` 
Principal
  |
  ▼
Grant of Authority
  |
  ▼
Authentic Source / Supporting Evidence
  |
  ▼
Issuer (QTSP / EAA Provider)
  |
  ▼
Attestation Issuance
  |
  ▼
Wallet Storage
  |
  ▼
Presentation
  |
  ▼
Verification
  |
  ▼
Authorization Decision
  |
  ▼
Revocation / Expiration
```

The lifecycle SHALL terminate immediately when the attestation expires, is revoked, or the underlying mandate ceases to exist.

## 4.3 Typical Business Use Cases

A Power of Attorney and Power of Representation MAY be used in cross-border business interactions including:

- tax declaration submission;
- customs declarations;
- company registration;
- public procurement;
- banking procedures;
- access to regulated business platforms;
- contract execution;
- representation before supervisory authorities;
- financial reporting;
- legal representation.

The Relying Party SHALL evaluate whether the presented mandate authorizes the requested business transaction.

## 4.4 Presentation Requirements

Presentation SHALL occur through a wallet supporting one of the attestation formats specified in Chapter 3.

Presentation MAY be performed online, cross-device, same-device or in proximity where supported by ISO/IEC 18013-5.

Wallets SHALL support user consent prior to disclosure. Wallets SHOULD support selective disclosure whenever technically possible.

## 4.5 Holder Obligations

Before presenting a Power of Attorney or Power of Representation, the Holder SHALL:

- verify that the attestation is still valid;
- verify that the requested transaction falls within the mandate scope;
- consent to disclosure;
- protect private cryptographic keys.

The Holder SHOULD minimize disclosure of unnecessary attributes. The Holder SHALL NOT modify the attestation.

## 4.6 Relying Party Obligations

Before accepting a Power of Attorney, the Relying Party SHALL verify:

- the identity of the presenting Holder;
- attestation integrity;
- issuer trust;
- attestation status;
- scope;
- validity period;
- restrictions.

Where required by applicable legislation, a PID SHALL be requested and verified. Malformed attestations SHALL be rejected.

## 4.7 Authorization Decision

After successful verification, the Relying Party MAY authorize the requested transaction. Authorization SHALL depend upon attestation validity, issuer trust, business policy, legal requirements and mandate scope.

Possession of a valid attestaion SHALL NOT automatically imply authorization. Business-specific policies MAY impose additional conditions.

## 4.8 PID Binding

Where national legislation requires personal identification, the PoA SHALL be cryptographically or logically bound to a Personal Identification Data attestation.

The Relying Party SHALL verify that the PID identifies the presenting individual and that the Attorney-in-Fact referenced by the PoA corresponds to the PID Holder.

## 4.9 Device Binding

A Power of Attorney MAY be device-bound or non-device-bound. Where device binding is implemented, the attestation SHALL contain the metadata attribute `cryptographically_bound_to`.

The recommended value is:

```text
urn:eudi:pid:1
```

where the attestation is bound to a Personal Identification Data attestation.

## 4.10 Transaction Data

Presentation MAY include transaction-specific information such as requested service, relying party identifier, requested authorization scope, requested signature level, requested attributes, transaction identifier and timestamp.

Transaction data SHALL NOT become part of the attestation itself.

## 4.11 Privacy Requirements

The following privacy principles SHALL apply:

- data minimization;
- selective disclosure;
- user consent;
- purpose limitation;
- privacy-preserving audit logging.

## 4.12 Error Handling

| Error                | Relying Party Behaviour |
|-------               |--------------------------|
| Attestation revoked   | Reject. |
| Attestation expired   | Reject. |
| Invalid signature    | Reject. |
| Unknown issuer       | Reject. |
| Missing mandatory attributes | Reject. |
| PID mismatch         | Reject. |
| Scope mismatch       | Reject. |
| Trust chain failure  | Reject. |
| Attestation malformed | Reject. |

Appropriate error information MAY be presented to the Holder. Detailed trust validation errors SHOULD NOT expose sensitive security information.

## 4.13 Cross-Border Recognition

Power of Attorney and Power of Representation attestations are intended for cross-border use. Participating Relying Parties SHOULD recognize attestations issued by trusted issuers located in other Member States where the applicable trust anchor is recognized, attestations validation succeeds and no legal restriction prohibits acceptance.

## 4.14 Operational Recommendations

Issuers MUST automate revocation and synchronize mandate changes with authentic sources.

Issuers MAY issue short-lived attestation whenever needed.

Wallet Providers SHOULD support offline presentation where applicable, selective disclosure and attestation status updates.

Relying Parties SHOULD cache trust anchors, perform online status checks whenever possible, log authorization decisions and apply the principle of least privilege.

## 4.15 Conformance

An implementation claiming conformance with this Rulebook SHALL implement attestation presentation, issuer trust verification, signature validation, attestation status verification, validity checks, mandate scope evaluation and authorization decision processing.

Selective disclosure support is RECOMMENDED. Offline presentation support is OPTIONAL unless explicitly required by the applicable deployment profile.

## 5 Trust anchors

## 5.1 Purpose

This chapter defines the trust framework applicable to Power of Attorney attestations issued and verified within the WE BUILD ecosystem.

Its objective is to ensure that every Relying Party can establish a consistent level of trust in the issuer, the credential and the underlying delegation of authority.

## 5.2 Trust Model

```text
European Digital Identity Framework
  |
  ▼
European Trusted Lists (eIDAS)
  |
  ▼
Qualified Trust Service Providers
  |
  ▼
QEAA / PubEAA / EAA Provider
  |
  ▼
Power of X (PoA, PoR) Attestation
  |
  ▼
Holder Wallet
  |
  ▼
Relying Party
```

Each trust layer SHALL validate the integrity of the previous layer. Failure of any trust layer SHALL invalidate the Attestation.

## 5.3 Trust Anchors

| Attestation Type  | Trust Anchor |
|------------------ |-------------|
| QEAA              | eIDAS Trusted List. |
| Pub-EAA           | Qualified Certificate issued by a QTSP. |
| EAA               | Organizational trust anchor defined by WE BUILD governance. |

The trust anchor SHALL be machine-readable.

## 5.4 Qualified Electronic Attestations

For Qualified Electronic Attestations of Attributes, the Relying Party SHALL obtain the issuer certificate, validate the certificate chain, verify the Qualified Trust Service Provider, verify the Qualified Certificate and verify the attestation signature.

Trust SHALL ultimately terminate at a trust anchor contained within the applicable European Trusted List.

## 5.5 Public Electronic Attestations

Where a Public Electronic Attestation is used, the issuing public authority SHALL possess a qualified certificate, the certificate SHALL be verifiable through a Qualified Trust Service Provider and the QTSP SHALL be discoverable through the European Trusted Lists.

## 5.6 Non-qualified Electronic Attestations

For non-qualified Electronic Attestations, the trust framework SHALL be explicitly defined by the applicable governance framework. Acceptable trust mechanisms include organizational PKI, sector-specific trust frameworks, national trust registries and WE BUILD trusted issuer registries.

The issuer SHALL publish issuer identifier, public verification key, metadata endpoint and status endpoint.

## 5.7 Trust Anchor Distribution

Trust anchors SHALL be distributed through secure and authoritative mechanisms such as European Trusted Lists, Trusted List APIs, Organizational Trust Registries, Federation Metadata Services or signed Trust Lists.

Unsigned trust anchor distribution SHALL NOT be used.

## 5.8 Issuer Authentication

Before issuing a Power of Attorney, an Issuer SHALL authenticate itself towards the applicable trust infrastructure.

The following information SHALL be available:

- issuer identifier;
- certificate chain;
- public verification keys;
- attestation metadata endpoint;
- revocation endpoint.

## 5.9 Trust Verification by the Relying Party

| Verification Step       | Requirement |
|-------------------      |-------------|
| Attestation signature    | SHALL |
| Issuer certificate      | SHALL |
| Trust chain             | SHALL |
| Attestation status       | SHALL |
| Validity period         | SHALL |
| Issuer authorization    | SHALL |
| Attestation schema       | SHOULD |
| Metadata integrity      | SHOULD |

Failure of any mandatory verification SHALL result in rejection of the attestation.

## 5.10 Trust Validation Process

```text
Receive attestation
  |
  ▼
Verify Signature
  |
  ▼
Validate Certificate Chain
  |
  ▼
Resolve Trust Anchor
  |
  ▼
Validate Trust Anchor
  |
  ▼
Check attestation Status
  |
  ▼
Validate Business Rules
  |
  ▼
Authorize Transaction
```

The order MAY vary provided that equivalent security guarantees are achieved.

## 5.11 Authentic Sources

Where issuance of a Power of Attorney or Power of Representation depends on information obtained from an Authentic Source, the Issuer SHALL ensure that the Authentic Source is authoritative for the relevant information, the retrieved information is current at the time of issuance, the information has not been altered during transmission and access to the Authentic Source is appropriately authenticated and authorized.

Examples include Business Registers, Population Registers, Tax Registers, Professional Registers, Court Registers and National Mandate Registers.

## 5.12 Trust in Supporting Evidence

A Power of Attorney MAY be based upon additional supporting evidence such as notarized documents, court decisions, organizational resolutions, shareholder resolutions, employment contracts or professional licenses.

Where such evidence contributes to the issuance decision, the Issuer SHOULD maintain auditable references to that evidence. The evidence itself SHOULD NOT be embedded within the attestation.

## 5.13 Cross-Border Trust

A Relying Party SHOULD recognize issuers established in other Member States provided that the issuer is trusted, the applicable trust anchor is recognized, attestation validation succeeds and no national legal restrictions prohibit acceptance.

This Rulebook does not override national legislation governing legal recognition of mandates.

## 5.14 Trust Metadata

| Metadata          |    Purpose |
|----------         |---------|
| Issuer Identifier | Unique issuer identification. |
| Issuer Name       | Human-readable issuer. |
| Attestation Types  | Supported attestation types. |
| Public Keys       | Signature verification. |
| Metadata Endpoint | Attestation metadata. |
| Status Endpoint   | Revocation and suspension. |
| Terms of Use      | Issuer policy. |
| Contact Information | Operational support. |

Metadata SHOULD be signed by the issuing authority.

## 5.15 Trust Failure Handling

| Event                | Action |
|-------               |--------|
| Unknown issuer       | Reject. |
| Invalid certificate  | Reject. |
| Invalid signature    | Reject. |
| Revoked certificate  | Reject. |
| Missing trust anchor | Reject. |
| Trust anchor not recognized | Reject. |
| Attestation revoked   | Reject. |
| Attestation expired   | Reject. |

The Relying Party SHOULD log trust failures for audit purposes.

## 5.16 Trust Governance

The governance of trusted issuers SHALL be defined by the WE BUILD Trust Framework. The framework SHOULD define issuer onboarding procedures, trust anchor publication, issuer suspension, issuer removal, key rollover procedures, certificate renewal and incident handling.

## 5.17 Conformance Requirements

An implementation claiming conformance with this Rulebook SHALL support issuer trust verification, certificate path validation, attestation signature verification, trust anchor resolution and attestation status verification.

Implementations SHOULD additionally support automatic trust anchor updates, metadata validation, key rollover handling and federated trust discovery.

Attestation lifespan defined in `validity` attribute SHALL NOT exceed the lifespan of the trust anchor.

## 6 Revocation

## 6.1 Purpose

This chapter specifies mechanisms governing suspension, revocation and expiration of a Power of Attorney and Power of Representation attestation.

The objective is to ensure that delegated authority cannot be exercised after it has ceased to be legally valid. Within this rulebook both short-lived and long-lived attestation are permited and therefore revocation provitions SHALL be established.

## 6.2 Atestation Lifecycle

```text
Draft
  |
  ▼
Issued
  |
  ▼
Active
  |
  | 
  |
  ▼
Revoked
  |
  ▼
Expired
```

A attestation SHALL NOT return to the Active state after it has been revoked.

## 6.3 Expiration

Expiration occurs automatically when the validity period defined by the attestation ends. No explicit revocation is required after expiration. A Relying Party SHALL reject every expired attestation.

## 6.4 Revocation

Revocation permanently terminates the legal validity of a Power of Attorney before its scheduled expiration. Revocation SHALL occur whenever the delegated authority no longer exists.

Once revoked, the attestation SHALL NOT be accepted by any conformant Relying Party.

Once revoked, the attestation SHALL NOT regain it's valid status.

## 6.5 Suspension

Some jurisdictions permit temporary suspension of delegated authority. Where supported, suspension SHALL indicate that the mandate temporarily cannot be exercised. During suspension the attestation SHALL be treated as invalid.

## 6.6 Revocation Triggers

| Event                         | Revocation Requirement |
|-------                        |------------------------|
| Principal withdraws mandate   | SHALL |
| Mandate expires by law        | SHALL |
| Company dissolved             | SHALL |
| Representative leaves organization | SHALL |
| Representative dies           | SHALL |
| Fraud detected                | SHALL |
| Attestation compromised        | SHALL |
| Issuer error                  | SHALL |
| Court decision                | SHALL |
| Administrative decision       | SHALL |
| Authentic Source updated      | SHOULD |
| Organizational restructuring  | MAY |

## 6.7 Authorized Revocation Actors

Only authorized entities SHALL revoke a attestation. Examples include the Issuer, Qualified Trust Service Provider, Principal, Competent Public Authority, Court and Authentic Source Operator.

The revocation authority SHALL be defined by applicable legislation.

## 6.8 Revocation Mechanisms

| Mechanism                   | Description |
|-----------                  |-------------|
| Status List                 | Attestation status lookup. |
| Revocation List             | Published revocation entries. |
| Online Status API           | Real-time validation. |
| OCSP-like service           | Online status protocol. |
| Short-lived Attestation      | Revocation avoided through short lifetime. |

Implementations SHOULD support real-time status verification whenever technically feasible.

## 6.9 Atestation Status Values

| Status                   | Meaning |
|--------                  |---------|
| active                   | Attestation currently valid. |
| revoked                  | Permanently invalid. |
| expired                  | Validity period ended. |
| unknown                  | Status unavailable. |

Relying Parties SHALL reject every attestation except those having status `active`.

## 6.10 Status Verification

Before accepting a attestation, the Relying Party SHALL verify attestation identifier, current status, validity period and issuer status.

Status verification SHOULD occur online. Where offline verification is necessary, locally cached status information MAY be used if permitted by deployment policy.

## 6.11 Revocation Service

Each issuer SHALL publish a status service. The service SHALL support attestation lookup, status retrieval and timestamp of latest update. The endpoint SHALL be identified within the attestation metadata.

## 6.12 Short-Lived Attestation

Issuers MAY issue short-lived attestation. A attestation is considered short-lived where its validity period does not exceed 24 hours.

For short-lived attestations, explicit revocation MAY be omitted and expiration SHALL replace revocation.

## 6.13 Revocation Processing

```text
Revocation Event
  |
  ▼
Issuer validates request
  |
  ▼
Attestation status updated
  |
  ▼
Status service updated
  |
  ▼
Wallet notified (optional)
  |
  ▼
Future presentations rejected
```

## 6.14 Wallet Behaviour

Wallets SHOULD periodically synchronize attestation status. Wallets SHOULD notify the Holder whenever a attestation has been revoked, suspended or approaches expiration.

Wallets SHALL prevent accidental presentation of revoked attestation. Wallets MAY retain revoked attestation for historical audit purposes provided they are clearly marked as invalid.

## 6.15 Relying Party Behaviour

Whenever a revoked attestation is presented, the Relying Party SHALL terminate validation, deny authorization, inform the Holder that the attestation is no longer valid and record the failed authorization event.

Business processes SHALL NOT continue using revoked attestation.

## 6.16 Audit Requirements

Issuers SHOULD maintain an auditable record of issuance, suspension, revocation and expiration. Audit records SHOULD contain credential identifier, timestamp, responsible authority, reason for revocation and evidence reference.

Audit records SHALL be protected against unauthorized modification.

## 6.17 Revocation Reasons

| Code | Description |
|------|-------------|
| PRIVILEGE_WITHDRAWN | Mandate withdrawn. |
| ORGANIZATION_DISSOLVED | Company dissolved. |
| EMPLOYMENT_TERMINATED | Representative left organization. |
| COURT_ORDER | Judicial decision. |
| FRAUD | Fraud detected. |
| ADMINISTRATIVE_DECISION | Administrative action. |
| ATTESTATION_COMPROMISED | Attestation compromised. |
| TECHNICAL_ERROR | Issuance error. |
| SUPERSEDED | Replaced by newer attestation. |

These reason codes SHOULD be machine-readable.

## 6.18 Revocation Notifications

Issuers MAY notify the Holder, Principal, Wallet Provider, Relying Parties or organizational administrators. Notification SHALL NOT replace status verification.

## 6.19 Conformance Requirements

An implementation claiming conformance with this Rulebook SHALL support attestation expiration, attestation revocation, status verification, revocation endpoint publication and rejection of revoked attestations.

Implementations SHOULD additionally support suspension, real-time status updates, revocation notifications and audit logging.

## 6.20 Operational Recommendations

Issuers SHOULD revoke attestations immediately after legal authority ceases, automate synchronization with Authentic Sources and minimize delay between legal revocation and technical revocation.

Wallet Providers SHOULD synchronize status frequently and prevent presentation of invalid attestations.

Relying Parties SHOULD perform status verification for every presentation, avoid long-term caching of attestation status and maintain audit logs for authorization decisions.

## 7 Compliance

*In this section explicitly state how this specific rulebook complies with the
general EUDI framework, ARF, and relevant regulations*

[RULEBOOK AUTHOR TO DEFINE]

## 7.1 Purpose

This chapter specifies compliance requirements applicable to implementations of the WE BUILD Power of Attorney Rulebook.

Its purpose is to ensure that all participating ecosystem actors implement interoperable, secure and legally reliable Power of Attorney credentials.

Compliance with this Rulebook SHALL be assessed independently from national legislation. Where national law imposes additional requirements, such requirements SHALL take precedence.

## 7.2 Relationship to the European Digital Identity Framework

This Rulebook has been developed in accordance with objectives of the European Digital Identity Framework. In particular, it aligns with:

- Regulation (EU) 2024/1183;
- Architecture and Reference Framework https://eudi.dev/2.9.0/;
- Annex 2 – Topic 12, Attestation Rulebooks;
- Annex 2 – Topic 7, Revocation;
- Annex 2 – Topic 10, Issuance;
- applicable ETSI trust service specifications.

This Rulebook SHALL be interpreted consistently with those documents.

## 7.3 Compliance Objectives

Implementations conforming to this Rulebook SHALL support interoperable issuance, presentation, verification, revocation, cross-border recognition and selective disclosure where supported by the chosen encoding.

## 7.4 Issuer Compliance

An Issuer claiming compliance with this Rulebook SHALL:

- issue attestations according to the semantic model defined in Chapter 2;
- use one of the encoding formats defined in Chapter 3;
- implement the trust framework defined in Chapter 5;
- implement revocation mechanisms defined in Chapter 6;
- issue globally unique attestation identifiers;
- maintain issuer metadata;
- publish attestation status information.

Where Qualified Electronic Attestations are issued, the Issuer SHALL comply with applicable eIDAS requirements.

## 7.5 Wallet Compliance

Wallet implementations SHALL support secure attestation storage, secure attestation presentation, user consent, cryptographic verification, selective disclosure where supported and attestation lifecycle management.

Wallets SHOULD additionally support offline presentation where applicable, automatic status synchronization, Holder notifications and attestation backup and recovery according to applicable security policies.

## 7.6 Relying Party Compliance

| Verification | Requirement |
|--------------|-------------|
| Signature verification | SHALL |
| Trust chain validation | SHALL |
| Issuer verification | SHALL |
| Attestation status verification | SHALL |
| Validity period verification | SHALL |
| Scope verification | SHALL |
| Business policy verification | SHALL |

Failure of any mandatory verification SHALL result in rejection of the attestation.

## 7.7 Holder Compliance

The Holder SHALL protect private cryptographic keys, prevent unauthorized attestation disclosure, present attestation only with informed consent and notify the Issuer where compromise is suspected.

The Holder SHOULD regularly synchronize attestation status and remove obsolete attestations where appropriate.

## 7.8 Semantic Compliance

Implementations SHALL preserve the semantic meaning of every attribute defined in Chapter 2. Encoding transformations SHALL NOT alter legal meaning, business interpretation, delegated authority, validity or scope.

Semantic interoperability SHALL take precedence over implementation-specific optimizations.

## 7.9 Privacy Compliance

Implementations SHALL comply with applicable European data protection legislation.

The following principles SHALL apply:

- data minimization;
- purpose limitation;
- user consent;
- confidentiality;
- integrity;
- accountability.

Selective disclosure SHOULD be supported whenever technically feasible. Relying Parties SHALL request only attributes necessary for the requested transaction.

## 7.10 Security Compliance

Every implementation SHALL support cryptographic attestation signatures, issuer authentication, secure communication, integrity protection, replay protection and attestation status verification.

Private keys SHALL remain under the exclusive control of their legitimate owner.

## 7.11 Interoperability Compliance

Conformant implementations SHALL support interoperability across Member States, Wallet Providers, Issuers, Relying Parties and Trust Service Providers.

Interoperability SHALL include common semantics, compatible attestation encodings, standardized verification procedures and standardized trust mechanisms.

## 7.12 Conformance Levels

| Level | Description |
|-------|-------------|
| Level 1 | Semantic Compliance. |
| Level 2 | Encoding Compliance. |
| Level 3 | Trust Compliance. |
| Level 4 | Operational Compliance. |
| Level 5 | Cross-border Compliance. |

Organizations SHOULD aim to satisfy all five levels.

## 7.13 Future Compatibility

Future revisions of this Rulebook SHALL strive to maintain backward compatibility. Breaking changes SHOULD only be introduced where required by legislation, ARF revisions or security reasons.

Version identifiers SHALL clearly distinguish incompatible releases.

## 7.14 Governance

Maintenance of this Rulebook SHOULD be performed through the WE BUILD governance process. Governance responsibilities include publication of new versions, management of semantic changes, coordination with WP4 Semantics, alignment with ETSI and alignment with future EUDI Architecture and Reference Framework revisions.

## 7.15 Conformance Statement

An implementation claiming compliance with the WE BUILD Power of Attorney Rulebook SHALL demonstrate that it satisfies all mandatory requirements identified by the keyword **SHALL** throughout this document.

Requirements expressed using **SHOULD** are considered recommendations supporting interoperability and operational best practices. Requirements expressed using **MAY** identify optional capabilities.

Conformance SHALL be evaluated over the complete attestation lifecycle, including issuance, storage, presentation, verification, revocation and expiration.

Only implementations satisfying all mandatory requirements may claim compliance with this Rulebook.

## 7.16 Summary

This Rulebook establishes a common semantic, operational and technical foundation for interoperable digital Powers of Attorney within the WE BUILD ecosystem.

By combining common semantics, interoperable attestation formats, trusted issuance, standardized verification, robust revocation mechanisms and cross-border trust, the Rulebook enables legally reliable delegation of authority throughout the European Digital Identity ecosystem and provides a foundation for future European Business Wallet services.

## 8 References

| **Item Reference** | **Standard name/details**|
|--------------------|---------------------------|
| [European Digital Identity Regulation] | [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183) of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework |
| EU ARF  | https://eudi.dev/2.9.0/ |
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

| Item Reference | Standard name / details |
|----------------|-------------------------|
| [European Digital Identity Regulation] | Regulation (EU) 2024/1183 of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework. |
| [ARF] | European Digital Identity Wallet Architecture and Reference Framework. |
| [Topic 7] | ARF Annex 2 – Topic 7 – Attestation revocation and revocation checking. |
| [Topic 10] | ARF Annex 2 – Topic 10 – Issuing a PID or attestation to a Wallet Unit. |
| [Topic 12] | ARF Annex 2 – Topic 12 – Attestation Rulebooks. |
| [Topic 20] | ARF Annex 2 – Topic 20 – Strong User Authentication for electronic payments. |
| [ISO/IEC 18013-5] | ISO/IEC 18013-5, Personal identification – ISO-compliant driving licence – Part 5: Mobile driving licence application. |
| [SD-JWT VC] | SD-JWT-based Verifiable Credentials. |
| [W3C VCDM v2.0] | W3C Verifiable Credentials Data Model v2.0. |
| [HAIP] | OpenID4VC High Assurance Interoperability Profile. |
| [OpenID4VCI] | OpenID for Verifiable Credential Issuance. |
| [OpenID4VP] | OpenID for Verifiable Presentations. |
| [OIDC] | OpenID Connect Core 1.0. |
| [RFC 2119] | Key words for use in RFCs to Indicate Requirement Levels. |
| [RFC 3339] | Date and Time on the Internet: Timestamps. |
| [RFC 7519] | JSON Web Token. |
| [RFC 8610] | Concise Data Definition Language. |
| [RFC 8943] | Concise Binary Object Representation Tags for Date. |
| [RFC 8949] | Concise Binary Object Representation. |
| [ETSI TS 119 471] | Policy and security requirements for trust service providers issuing electronic attestations of attributes. |
| [ETSI TR 119 476] | Analysis of selective disclosure and related trust service concepts. |
| [ETSI TS 119 412-6] | Certificate Profiles; Part 6: Qualified certificate profiles for electronic attestations. |
| [WE BUILD Scenario 1A] | BU4 Scenario 1A – Issuance of a Power of Attorney Attestation. |
| [WE BUILD Rulebook Template] | WE BUILD Attestation Rulebook Template for attestations of type Power of Attorney. |
