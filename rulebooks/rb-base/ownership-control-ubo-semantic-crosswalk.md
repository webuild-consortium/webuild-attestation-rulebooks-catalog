# Semantic crosswalk for the Ownership, Control and UBO attestations

This document is the shared semantic reference for the three beneficial-ownership
attestations in this catalogue:

- [`rb-ownership`](../rb-ownership/README.md) — `eu.we-build:ownership:1`
- [`rb-control`](../rb-control/README.md) — `eu.we-build:control:1`
- [`rb-ubo`](../rb-ubo/README.md) — `eu.we-build:ubo:1`

It exists because those three rulebooks describe one subject — who owns and controls a
legal entity — in three separate code lists, and because the Semantic Reference column
of each needs somewhere to point. It is **non-normative**. Nothing here overrides a
rulebook; where a rulebook and this document disagree, the rulebook wins and this
document should be corrected.

It is a reference document, not a rulebook, and so does not follow the eleven-chapter
template. It sits in `rb-base` alongside the other material shared between rulebooks.

## Contents

- [1 Namespaces](#1-namespaces)
- [2 How the two vocabularies divide the subject](#2-how-the-two-vocabularies-divide-the-subject)
- [3 Identity and address attributes](#3-identity-and-address-attributes)
- [4 Interest and control code lists](#4-interest-and-control-code-lists)
  - [4.1 `rb-ownership` `interests.type`](#41-rb-ownership-intereststype)
  - [4.2 `rb-control` `controls.type`](#42-rb-control-controlstype)
  - [4.3 `rb-ubo` `justification.threshold_met`](#43-rb-ubo-justificationthreshold_met)
  - [4.4 Directness, share and economic rights](#44-directness-share-and-economic-rights)
  - [4.5 BODS codes no rulebook uses](#45-bods-codes-no-rulebook-uses)
- [5 Evidence and provenance](#5-evidence-and-provenance)
- [6 The EBW beneficial-ownership module](#6-the-ebw-beneficial-ownership-module)
- [7 Open questions](#7-open-questions)
- [8 References](#8-references)

## 1 Namespaces

| Prefix | Namespace | Vocabulary |
| --- | --- | --- |
| `ebwv:` | `https://w3id.org/ebwv#` | European Business Wallet Vocabulary, published by the WE BUILD WP4 semantics group |
| `bods:` | `https://vocab.openownership.org/terms#` | Beneficial Ownership Data Standard RDF Vocabulary 0.4.0, published by Open Ownership |
| `codes:` | `https://standard.openownership.org/codelists#` | BODS code list values |
| `dcterms:` | `http://purl.org/dc/terms/` | Dublin Core terms, already used in this catalogue by `rb-company-info` |

Every IRI used in this document and in the Semantic Reference columns of the three
rulebooks was checked against the published `ebwv` Turtle at
`https://w3id.org/ebwv` and the published BODS Turtle at
`https://vocab.openownership.org/terms/bods-vocabulary-0.4.0.ttl`. Where no term
exists in either vocabulary, this document says so rather than inventing one.

## 2 How the two vocabularies divide the subject

`ebwv` and BODS both now cover beneficial ownership, but they are not competing: they
model different stages of the same work.

**BODS is a declaration model.** Its unit is the statement: an immutable, dated,
attributed claim that some person or entity holds some interest in some entity. A BODS
dataset is an append-only log of such claims, each carrying its own source and
provenance, from which any number of conclusions can be drawn. BODS deliberately
embeds **no** definition of 'beneficial owner'; `bods:beneficialOwnershipOrControl` is
a flag an individual publisher sets according to whichever definition it operates
under. That is what lets one dataset serve jurisdictions with different thresholds.

**The `ebwv` beneficial-ownership module is a determination model.** Its unit is the
analysis: `ebwv:BeneficialOwnership` holds the result of running a focus entity's
ownership graph through several named calculation methods — `ebwv:standard`,
`ebwv:accG10`, `ebwv:accG25`, `ebwv:dom10`, `ebwv:dom25` and `ebwv:cdd` — each of which
yields an `ebwv:BeneficialOwnershipVariant` grouping the owners it finds by the basis of
determination. Those methods and thresholds are drawn from German `GwG` and
Transparenzregister practice, as the term definitions themselves state.

The three attestations sit between the two. They carry *declared* facts, like BODS,
about *interests*, but they are consumed to support a *determination*, like `ebwv`.
That is why both vocabularies appear in their Semantic Reference columns: `ebwv:` for
the identity, address and determination attributes it already defines, `bods:` for the
interest structure it does not.

The practical consequence worth keeping in view: an attestation whose ownership claims
are losslessly BODS-mappable can be submitted to a beneficial-ownership register under
AMLR Articles 60 and 62, and can be cross-checked against register data coming back the
other way, without a bespoke transformation per member state.

## 3 Identity and address attributes

These map cleanly and are the same in all three rulebooks. `ebwv` is preferred here,
per EW-DM-12-010, which requires attributes to be reused from the catalogued vocabulary
where one exists. The BODS column is given for round-tripping.

| Rulebook attribute | `ebwv` | BODS | Note |
| --- | --- | --- | --- |
| `type` = `"Person"` | [`ebwv:NaturalPerson`](https://w3id.org/ebwv#NaturalPerson) | [`bods:Person`](https://vocab.openownership.org/terms#Person) | Discriminator; the class is the semantics, not the string |
| `type` = `"Entity"` | [`ebwv:LegalPerson`](https://w3id.org/ebwv#LegalPerson) | [`bods:Entity`](https://vocab.openownership.org/terms#Entity) | |
| `person.first_name` | [`ebwv:givenName`](https://w3id.org/ebwv#givenName) | [`bods:givenName`](https://vocab.openownership.org/terms#givenName) | |
| `person.surname` | [`ebwv:familyName`](https://w3id.org/ebwv#familyName) | [`bods:familyName`](https://vocab.openownership.org/terms#familyName) | |
| `person.birth_date` | [`ebwv:dateOfBirth`](https://w3id.org/ebwv#dateOfBirth) | [`bods:birthDate`](https://vocab.openownership.org/terms#birthDate) | |
| `birth_place.locality` | [`ebwv:placeOfBirth`](https://w3id.org/ebwv#placeOfBirth) | [`bods:placeOfBirth`](https://vocab.openownership.org/terms#placeOfBirth) | |
| `birth_place.country` | [`ebwv:countryOfBirth`](https://w3id.org/ebwv#countryOfBirth) | [`bods:placeOfBirth`](https://vocab.openownership.org/terms#placeOfBirth) | BODS carries country inside the address object |
| `citizenship` | [`ebwv:citizenship`](https://w3id.org/ebwv#citizenship) | [`bods:nationality`](https://vocab.openownership.org/terms#nationality) | |
| `residential_address` | [`ebwv:domicile`](https://w3id.org/ebwv#domicile) | [`bods:Residence`](https://vocab.openownership.org/terms#Residence) | BODS types the address rather than the property |
| `contact_address` | [`ebwv:temporaryAddress`](https://w3id.org/ebwv#temporaryAddress) | [`bods:Service`](https://vocab.openownership.org/terms#Service) | |
| `entity.name` | [`ebwv:legalName`](https://w3id.org/ebwv#legalName) | [`bods:name`](https://vocab.openownership.org/terms#name) | |
| `entity.legal_form` | [`ebwv:legalForm`](https://w3id.org/ebwv#legalForm) | — | See [Q-BO-11](#q-bo-11) on `form` versus `legal_form` |
| `entity.category` | — | [`bods:entityType`](https://vocab.openownership.org/terms#entityType) | `legal_entity` → [`codes:RegisteredEntity`](https://standard.openownership.org/codelists#RegisteredEntity); `legal_arrangement` → [`codes:Arrangement`](https://standard.openownership.org/codelists#Arrangement), subtype [`codes:Trust`](https://standard.openownership.org/codelists#Trust) |
| `entity.identifier` | [`ebwv:identifier`](https://w3id.org/ebwv#identifier) | [`bods:identifier`](https://vocab.openownership.org/terms#identifier) | |
| `entity.identifier.euid` | [`ebwv:Euid`](https://w3id.org/ebwv#Euid) | [`bods:scheme`](https://vocab.openownership.org/terms#scheme) | |
| `entity.identifier.lei` | [`ebwv:Lei`](https://w3id.org/ebwv#Lei) | [`bods:scheme`](https://vocab.openownership.org/terms#scheme) | BODS scheme code `XI-LEI` from org-id.guide |
| `entity.identifier.tax` | [`ebwv:Tin`](https://w3id.org/ebwv#Tin) | [`bods:scheme`](https://vocab.openownership.org/terms#scheme) | |
| `person_identifier.document_number` | — | [`bods:idString`](https://vocab.openownership.org/terms#idString) | |
| `person_identifier.document_type` + `issuing_country` | — | [`bods:scheme`](https://vocab.openownership.org/terms#scheme) | BODS composes the two into one scheme token, `{ISO 3166-1 alpha-3}-{PASSPORT\|TAXID\|IDCARD}`, e.g. `DEU-PASSPORT`. See [Q-BO-09](#q-bo-09) |
| `person_unique_identifier.identifier_unique` | — | [`bods:idString`](https://vocab.openownership.org/terms#idString) | |
| `person_unique_identifier.identifier_issuing_authority` | — | [`bods:schemeName`](https://vocab.openownership.org/terms#schemeName) | |

Address sub-fields, in all three rulebooks:

| Rulebook attribute | `ebwv` |
| --- | --- |
| `street` | [`ebwv:thoroughfare`](https://w3id.org/ebwv#thoroughfare) |
| `house_number` | [`ebwv:locatorDesignator`](https://w3id.org/ebwv#locatorDesignator) |
| `locality` | [`ebwv:postName`](https://w3id.org/ebwv#postName) |
| `region` | [`ebwv:adminUnitL2`](https://w3id.org/ebwv#adminUnitL2) |
| `postal_code` | [`ebwv:postCode`](https://w3id.org/ebwv#postCode) |
| `country` | [`ebwv:adminUnitL1`](https://w3id.org/ebwv#adminUnitL1) |

Two cautions on reuse. [`ebwv:jurisdiction`](https://w3id.org/ebwv#jurisdiction) has
`rdfs:domain` `ebwv:EconomicOperator` and three other non-person classes, so it fits
`entity.jurisdiction` but not the owner-level or person-level `jurisdiction` field;
`ebwv:citizenship` or the country of `ebwv:domicile` is the correct term for a natural
person. [`ebwv:startDate`](https://w3id.org/ebwv#startDate) has domain
`ebwv:PeriodOfTime`, so it does not fit `effective_date` on an interest;
[`bods:startDate`](https://vocab.openownership.org/terms#startDate), whose domain is
`bods:Interest`, does.

## 4 Interest and control code lists

This is where the three rulebooks diverge from each other. Each has invented its own
enumeration for the same concept — the nature of an ownership or control interest —
and the three do not share spelling, granularity or scope:

| Rulebook | Attribute | Codes | Style |
| --- | --- | --- | --- |
| `rb-ownership` | `interests.type` | 15 | `camelCase`, 13 of them taken verbatim from BODS |
| `rb-control` | `controls.type` | 10 | `snake_case`, none matching BODS |
| `rb-ubo` | `justification.threshold_met` | 20 | `snake_case`, conflating three separate dimensions |

In BODS all three are one closed code list of 23 values, carried on
[`bods:interest`](https://vocab.openownership.org/terms#interest), with directness and
magnitude held in separate fields alongside it. The sections below map each rulebook's
list onto it.

### 4.1 `rb-ownership` `interests.type`

Thirteen of the fifteen codes in section 4.4.5 are BODS v0.4 `interestType` codes,
spelled identically. They need no translation, only an IRI.

| `rb-ownership` code | BODS IRI | Fit |
| --- | --- | --- |
| `shareholding` | [`bods:Shareholding`](https://vocab.openownership.org/terms#Shareholding) | exact |
| `votingRights` | [`bods:VotingRights`](https://vocab.openownership.org/terms#VotingRights) | exact |
| `appointmentOfBoard` | [`bods:AppointmentOfBoard`](https://vocab.openownership.org/terms#AppointmentOfBoard) | exact |
| `otherInfluenceOrControl` | [`bods:OtherInfluenceOrControl`](https://vocab.openownership.org/terms#OtherInfluenceOrControl) | exact |
| `seniorManagingOfficial` | [`bods:SeniorManagingOfficial`](https://vocab.openownership.org/terms#SeniorManagingOfficial) | exact |
| `settlor` | [`bods:Settlor`](https://vocab.openownership.org/terms#Settlor) | exact |
| `trustee` | [`bods:Trustee`](https://vocab.openownership.org/terms#Trustee) | exact |
| `protector` | [`bods:Protector`](https://vocab.openownership.org/terms#Protector) | exact |
| `beneficiaryOfLegalArrangement` | [`bods:BeneficiaryOfLegalArrangement`](https://vocab.openownership.org/terms#BeneficiaryOfLegalArrangement) | exact |
| `rightsGrantedByContract` | [`bods:RightsGrantedByContract`](https://vocab.openownership.org/terms#RightsGrantedByContract) | exact |
| `conditionalRightsGrantedByContract` | [`bods:ConditionalRightsGrantedByContract`](https://vocab.openownership.org/terms#ConditionalRightsGrantedByContract) | exact |
| `controlViaCompanyRulesOrArticles` | [`bods:ControlViaCompanyRulesOrArticles`](https://vocab.openownership.org/terms#ControlViaCompanyRulesOrArticles) | exact |
| `controlByLegalFramework` | [`bods:ControlByLegalFramework`](https://vocab.openownership.org/terms#ControlByLegalFramework) | exact |
| `nomineeShareholding` | [`bods:Nominee`](https://vocab.openownership.org/terms#Nominee) + [`bods:Nominator`](https://vocab.openownership.org/terms#Nominator) | **lossy** — see below |
| `economicBeneficiary` | [`bods:RightsToProfitOrIncome`](https://vocab.openownership.org/terms#RightsToProfitOrIncome) or [`bods:EnjoymentAndUseOfAssets`](https://vocab.openownership.org/terms#EnjoymentAndUseOfAssets) | **approximate** — see [Q-BO-04](#q-bo-04) |

`nomineeShareholding` is a single code covering both sides of a nominee arrangement.
BODS v0.4 split these into `nominee`, the party holding on another's behalf, and
`nominator`, the party instructing them — a distinction the rulebook's own section 3.1
already draws in prose, where it defines both `nominee_shareholder` and `nominator` and
then maps both to `interests[].type: nomineeShareholding`. As written, an owner recorded
as `nomineeShareholding` cannot be read as one or the other. See [Q-BO-03](#q-bo-03).

### 4.2 `rb-control` `controls.type`

This list shares no spelling with BODS, and three of its ten codes collapse onto a
single BODS value while two others duplicate each other.

| `rb-control` code | BODS IRI | Fit |
| --- | --- | --- |
| `voting_rights` | [`bods:VotingRights`](https://vocab.openownership.org/terms#VotingRights) | exact, different spelling |
| `appointment_rights` | [`bods:AppointmentOfBoard`](https://vocab.openownership.org/terms#AppointmentOfBoard) | exact, different spelling |
| `board` | [`bods:AppointmentOfBoard`](https://vocab.openownership.org/terms#AppointmentOfBoard) | **duplicates `appointment_rights`** — both are defined in section 4.4.3 as the right to appoint or remove board members |
| `contractual` | [`bods:RightsGrantedByContract`](https://vocab.openownership.org/terms#RightsGrantedByContract) | exact, different spelling |
| `agreements` | [`bods:ControlViaCompanyRulesOrArticles`](https://vocab.openownership.org/terms#ControlViaCompanyRulesOrArticles) or [`bods:RightsGrantedByContract`](https://vocab.openownership.org/terms#RightsGrantedByContract) | **one-to-many** — the definition spans articles of association and contracts, which BODS separates |
| `profit_distribution` | [`bods:RightsToProfitOrIncome`](https://vocab.openownership.org/terms#RightsToProfitOrIncome) | close |
| `nominee` | [`bods:Nominee`](https://vocab.openownership.org/terms#Nominee) + [`bods:Nominator`](https://vocab.openownership.org/terms#Nominator) | **lossy**, as in 4.1 |
| `dominance` | [`bods:OtherInfluenceOrControl`](https://vocab.openownership.org/terms#OtherInfluenceOrControl) | collapses |
| `veto` | [`bods:OtherInfluenceOrControl`](https://vocab.openownership.org/terms#OtherInfluenceOrControl) | collapses |
| `other_means_of_control` | [`bods:OtherInfluenceOrControl`](https://vocab.openownership.org/terms#OtherInfluenceOrControl) | collapses |

The more consequential finding is an absence. Section 3.1 of `rb-control` names five
roles as the ones a `Person` controller holds — `seniorManagingOfficial`,
`boardMember`, `boardChair`, `nominee` and `nominator` — but `controls.type` in section
4.4.3 has no code for the first three. The section 3.1 table resolves
`seniorManagingOfficial` to `controls.type: voting_rights`, and `boardMember` and
`boardChair` to `controls.type: board`. Neither is sound: a senior managing official
exercises control through employment, not through voting shares, and board membership is
not the right to appoint the board. BODS has had distinct codes for all three since
v0.3 — [`bods:SeniorManagingOfficial`](https://vocab.openownership.org/terms#SeniorManagingOfficial),
[`bods:BoardMember`](https://vocab.openownership.org/terms#BoardMember) and
[`bods:BoardChair`](https://vocab.openownership.org/terms#BoardChair). See
[Q-BO-02](#q-bo-02).

Section 3.1 also maps `settlor`, `trustee` and `protector` to `controls.type:
agreements`, losing the distinction between the three trust roles that `rb-ownership`
and `rb-ubo` both keep, and that BODS carries as separate codes.

### 4.3 `rb-ubo` `justification.threshold_met`

The twenty codes in section 4.4.2 are not a single enumeration. They multiply together
three dimensions that BODS, and `rb-ownership`, keep in separate fields:

1. the **nature** of the interest — `bods:interest` type;
2. how **directly** it is held — [`bods:directOrIndirect`](https://vocab.openownership.org/terms#directOrIndirect);
3. the **magnitude** against a threshold — [`bods:shareExact`](https://vocab.openownership.org/terms#shareExact) or [`bods:shareMinimum`](https://vocab.openownership.org/terms#shareMinimum).

That is why groups (a) and (b) each spend three codes on what is one interest type
crossed with three directness values, and why the list is simultaneously long and
unable to express, for instance, indirect control through a veto right.

| `threshold_met` code | BODS equivalent |
| --- | --- |
| `ownership_25_plus` | `bods:Shareholding` + `bods:shareMinimum` 25 + `bods:beneficialOwnershipOrControl` true |
| `ownership_direct` | `bods:Shareholding` + [`codes:Direct`](https://standard.openownership.org/codelists#Direct) |
| `ownership_indirect` | `bods:Shareholding` + [`codes:Indirect`](https://standard.openownership.org/codelists#Indirect) |
| `control_voting_25_plus` | `bods:VotingRights` + `bods:shareMinimum` 25 |
| `control_voting_direct` | `bods:VotingRights` + `codes:Direct` |
| `control_voting_indirect` | `bods:VotingRights` + `codes:Indirect` |
| `control_management` | [`bods:SeniorManagingOfficial`](https://vocab.openownership.org/terms#SeniorManagingOfficial) or [`bods:AppointmentOfBoard`](https://vocab.openownership.org/terms#AppointmentOfBoard) |
| `control_veto` | `bods:OtherInfluenceOrControl` |
| `control_contractual` | [`bods:RightsGrantedByContract`](https://vocab.openownership.org/terms#RightsGrantedByContract) |
| `control_family_relationships` | `bods:OtherInfluenceOrControl` |
| `control_acting_in_concert` | `bods:OtherInfluenceOrControl` |
| `control_nominee` | [`bods:Nominator`](https://vocab.openownership.org/terms#Nominator) — the UBO behind a nominee is the nominator |
| `control_other_means` | `bods:OtherInfluenceOrControl` |
| `arrangement_settlor` | [`bods:Settlor`](https://vocab.openownership.org/terms#Settlor) |
| `arrangement_trustee` | [`bods:Trustee`](https://vocab.openownership.org/terms#Trustee) |
| `arrangement_beneficiary` | [`bods:BeneficiaryOfLegalArrangement`](https://vocab.openownership.org/terms#BeneficiaryOfLegalArrangement) |
| `arrangement_protector` | [`bods:Protector`](https://vocab.openownership.org/terms#Protector) |
| `arrangement_other_control` | `bods:OtherInfluenceOrControl` |
| `arrangement_object_of_power` | **no BODS code** — see [Q-BO-05](#q-bo-05) |
| `arrangement_default_taker` | **no BODS code** — see [Q-BO-05](#q-bo-05) |

### 4.4 Directness, share and economic rights

| Rulebook attribute | BODS | `ebwv` |
| --- | --- | --- |
| `interests.level` / `controls.level` | [`bods:directOrIndirect`](https://vocab.openownership.org/terms#directOrIndirect) | [`ebwv:isDirectParticipation`](https://w3id.org/ebwv#isDirectParticipation) |
| `level` = `direct` | [`codes:Direct`](https://standard.openownership.org/codelists#Direct) | `ebwv:isDirectParticipation` true |
| `level` = `indirect` | [`codes:Indirect`](https://standard.openownership.org/codelists#Indirect) | `ebwv:isDirectParticipation` false |
| `level` = `unknown` | [`codes:Unknown`](https://standard.openownership.org/codelists#Unknown) | — |
| `level` = `joint` | **no equivalent in either** — see [Q-BO-06](#q-bo-06) | — |
| `interests.percentage` | [`bods:shareExact`](https://vocab.openownership.org/terms#shareExact) | [`ebwv:relativeShare`](https://w3id.org/ebwv#relativeShare) |
| `controls.voting_percentage`, `justification.voting_rights_percentage` | `bods:shareExact` on a `bods:VotingRights` interest | [`ebwv:relativeVotingRights`](https://w3id.org/ebwv#relativeVotingRights) |
| `justification.ownership_percentage` | `bods:shareExact` on a `bods:Shareholding` interest | [`ebwv:relativeShare`](https://w3id.org/ebwv#relativeShare) |
| `interests.quantity` | — | [`ebwv:absoluteShare`](https://w3id.org/ebwv#absoluteShare) is a monetary amount, not a unit count |
| `interests.rights` = `dividend_rights` | [`bods:RightsToProfitOrIncome`](https://vocab.openownership.org/terms#RightsToProfitOrIncome) | — |
| `interests.rights` = `liquidation_rights` | [`bods:RightsToSurplusAssetsOnDissolution`](https://vocab.openownership.org/terms#RightsToSurplusAssetsOnDissolution) | — |
| `effective_date` | [`bods:startDate`](https://vocab.openownership.org/terms#startDate) | — |
| `justification.control_details`, `controls.other_details` | — | [`ebwv:otherControlReason`](https://w3id.org/ebwv#otherControlReason) |
| `controls.basis` | **no equivalent** — see [Q-BO-08](#q-bo-08) | partially [`ebwv:otherControlReason`](https://w3id.org/ebwv#otherControlReason) |

Note the modelling difference on economic rights: BODS treats a right to dividends or
to surplus on dissolution as an **interest type** in its own right, because such a
right can exist without any shareholding. All three rulebooks instead treat `rights` as
a mandatory array hanging off every interest, which forces an answer even where the
question does not arise — see [Q-BO-07](#q-bo-07).

### 4.5 BODS codes no rulebook uses

Ten of the 23 BODS codes appear in none of the three rulebooks. Most are unremarkable,
but two are load-bearing for AMLR:

| BODS code | Why it matters here |
| --- | --- |
| [`bods:UnknownInterest`](https://vocab.openownership.org/terms#UnknownInterest) | An interest is known to exist but its nature is not known. Currently expressible only as `level: unknown`, which says something different |
| [`bods:UnpublishedInterest`](https://vocab.openownership.org/terms#UnpublishedInterest) | The nature of the interest is known but is deliberately withheld, for instance under an AMLR Article 61 exemption or a protection regime |
| [`bods:BoardMember`](https://vocab.openownership.org/terms#BoardMember), [`bods:BoardChair`](https://vocab.openownership.org/terms#BoardChair) | Named as `Person` controller roles by `rb-control` section 3.1 with no code to carry them |
| [`bods:Nominee`](https://vocab.openownership.org/terms#Nominee), [`bods:Nominator`](https://vocab.openownership.org/terms#Nominator) | Both sides of a nominee arrangement, currently collapsed |
| [`bods:RightsToSurplusAssetsOnDissolution`](https://vocab.openownership.org/terms#RightsToSurplusAssetsOnDissolution), [`bods:RightsToProfitOrIncome`](https://vocab.openownership.org/terms#RightsToProfitOrIncome), [`bods:RightToProfitOrIncomeFromAssets`](https://vocab.openownership.org/terms#RightToProfitOrIncomeFromAssets), [`bods:EnjoymentAndUseOfAssets`](https://vocab.openownership.org/terms#EnjoymentAndUseOfAssets) | The economic-rights family, carried as `rights` rather than as interest types |

Alongside these, BODS carries a closed `unspecifiedReason` list for the case where a
party cannot be named at all:
[`codes:NoBeneficialOwners`](https://standard.openownership.org/codelists#NoBeneficialOwners),
[`codes:SubjectExemptFromDisclosure`](https://standard.openownership.org/codelists#SubjectExemptFromDisclosure),
[`codes:InterestedPartyExemptFromDisclosure`](https://standard.openownership.org/codelists#InterestedPartyExemptFromDisclosure),
[`codes:InformationUnknownToPublisher`](https://standard.openownership.org/codelists#InformationUnknownToPublisher)
and three more. All three rulebooks currently require at least one `Person` owner or
controller — `rb-ownership` IR-02, `rb-control` IR-02 — with no way to state that there
is legitimately none, or that the information is withheld. See [Q-BO-01](#q-bo-01).

## 5 Evidence and provenance

| Rulebook attribute | `ebwv` | BODS |
| --- | --- | --- |
| `evidence` / `source` object | [`ebwv:EvidenceData`](https://w3id.org/ebwv#EvidenceData) | [`bods:source`](https://vocab.openownership.org/terms#source) |
| `evidence[n].id` | — | — (use [`dcterms:identifier`](http://purl.org/dc/terms/identifier), as `rb-company-info` does) |
| `evidence[n].url` | — | [`bods:url`](https://vocab.openownership.org/terms#url) |
| `evidence[n].type` = `officialRegister` | — | [`bods:OfficialRegister`](https://vocab.openownership.org/terms#OfficialRegister) |
| `evidence[n].type` = `selfDeclaration` | — | [`bods:SelfDeclaration`](https://vocab.openownership.org/terms#SelfDeclaration) |
| `evidence[n].type` = `thirdPartyVerification` | — | [`bods:ThirdParty`](https://vocab.openownership.org/terms#ThirdParty) + [`bods:Verified`](https://vocab.openownership.org/terms#Verified) |
| `evidence[n].type` = `trustDeed`, `shareholderAgreement`, `articlesOfAssociation`, `governanceChart` | — | no BODS source type; BODS types the *kind* of source, not the document |
| `rb-ubo` `source.type` = `TransparencyRegister` | [`ebwv:TransparencyRegisterEntry`](https://w3id.org/ebwv#TransparencyRegisterEntry) | [`bods:OfficialRegister`](https://vocab.openownership.org/terms#OfficialRegister) |

BODS `source.type` is an **array** of four values describing how the claim was obtained;
the rulebooks' `evidence[n].type` is a single string mixing that question with the
document's genre. The two are compatible in the direction rulebook → BODS but not back.

The `rb-ownership` and `rb-control` evidence lists differ from the `rb-ubo` list in both
spelling and membership — `officialRegister` against `CommercialRegister`,
`selfDeclaration` against `AMLOfficerDeclaration`, and so on — for no reason apparent
from the documents. See [Q-BO-10](#q-bo-10).

## 6 The EBW beneficial-ownership module

The `ebwv` vocabulary now carries a full beneficial-ownership module that none of the
three rulebooks reference. It is worth knowing what is already there:

| `ebwv` term | Holds |
| --- | --- |
| [`ebwv:BeneficialOwnership`](https://w3id.org/ebwv#BeneficialOwnership) | The whole analysis for a focus entity, across all calculation methods |
| [`ebwv:BeneficialOwnershipVariant`](https://w3id.org/ebwv#BeneficialOwnershipVariant) | The owners found under one method, grouped by basis of determination |
| [`ebwv:BeneficialOwner`](https://w3id.org/ebwv#BeneficialOwner) | One owner, with direct and total capital and voting shares, a high-risk flag and an other-control reason |
| [`ebwv:capitalBeneficialOwner`](https://w3id.org/ebwv#capitalBeneficialOwner) | Determined on capital — maps to `bods:Shareholding` + `bods:beneficialOwnershipOrControl` |
| [`ebwv:votingRightsBeneficialOwner`](https://w3id.org/ebwv#votingRightsBeneficialOwner) | Determined on voting rights — maps to `bods:VotingRights` + the same flag |
| [`ebwv:otherControlBeneficialOwner`](https://w3id.org/ebwv#otherControlBeneficialOwner) | Determined on comparable control — maps to `bods:OtherInfluenceOrControl` |
| [`ebwv:fictitiousBeneficialOwner`](https://w3id.org/ebwv#fictitiousBeneficialOwner) | The `GwG` fallback to legal representatives — closest BODS code is `bods:SeniorManagingOfficial` |
| [`ebwv:ShareInFocus`](https://w3id.org/ebwv#ShareInFocus), [`ebwv:shareInFocusAlongBranch`](https://w3id.org/ebwv#shareInFocusAlongBranch), [`ebwv:shareInFocusTotal`](https://w3id.org/ebwv#shareInFocusTotal) | A holder's share in the focus entity, per ownership branch and in total |
| [`ebwv:interestType`](https://w3id.org/ebwv#interestType), [`ebwv:interestScope`](https://w3id.org/ebwv#interestScope) | Type and scope of a natural person's economic interest, on a transparency register entry |

Two observations that bear on the rulebooks.

First, `ebwv:shareInFocusAlongBranch` and `ebwv:shareInFocusTotal` are exactly the
distinction the three rulebooks lack. All three record an indirect holding as a single
percentage with no statement of the path it runs through; `rb-ownership` lists
intermediate entities in the same flat `owner[]` array as the ultimate owners, with
nothing linking an owner to the intermediary it holds through. The non-normative example
payload in `rb-ownership` section 5.1.3 shows the consequence: `Holding GmbH` holds 30%
at `level: indirect`, and the document gives no way to say indirect *through what*. BODS
carries the path as an explicit edge — each link is its own relationship statement with
its own `bods:subject` and `bods:interestedParty` — which is what makes a chain
traversable. See [Q-BO-12](#q-bo-12).

Second, `ebwv:interestType` is declared as a plain `xsd:string` with no enumeration,
while all three rulebooks and BODS enumerate the same concept. If the rulebooks are to
point their `interests.type` column at an `ebwv` term, that term needs a code list; the
BODS 23-value list is one candidate for it.

A question the semantics group is better placed than this document to answer:
`ebwv:accG10`, `ebwv:accG25`, `ebwv:dom10` and `ebwv:dom25` carry 10% thresholds and the
accumulation and domination methods of German `GwG` practice, and
`ebwv:fictitiousBeneficialOwner` is a `GwG` construct. AMLR 2024/1624 harmonises the
threshold at 25% and replaces the notional-owner fallback with senior managing
officials. All three rulebooks name AMLR, not `GwG`, as their regulatory basis. See
[Q-BO-13](#q-bo-13).

## 7 Open questions

Numbering continues from the semantic intake submission for this use case, filed as
`webuild-consortium/wp4-semantics-group` PR #59.

<a name="q-bo-01"></a>
**Q-BO-01 — no beneficial owners, and withheld owners.** `rb-ownership` IR-02 and
`rb-control` IR-02 require at least one `Person` entry. How should an issuer attest that
an entity legitimately has no beneficial owner, or that an owner is exempt from
disclosure? BODS answers with its `unspecifiedReason` list. Without an equivalent, the
rules make a compliant attestation impossible for those cases.

<a name="q-bo-02"></a>
**Q-BO-02 — `rb-control` cannot express its own `Person` roles.** Section 3.1 names
`seniorManagingOfficial`, `boardMember` and `boardChair`; section 4.4.3 has no code for
any of them. Should `controls.type` gain the three BODS codes, and the section 3.1
mappings be corrected?

<a name="q-bo-03"></a>
**Q-BO-03 — nominee and nominator.** Should the single `nomineeShareholding` and
`nominee` codes be split into the two BODS v0.4 codes, so that the distinction section
3.1 of both rulebooks already draws in prose is representable in data?

<a name="q-bo-04"></a>
**Q-BO-04 — `economicBeneficiary`.** This is one of two `rb-ownership` codes with no
BODS counterpart. Is it intended as a right to profit or income
(`bods:RightsToProfitOrIncome`), as use and enjoyment of assets
(`bods:EnjoymentAndUseOfAssets`), or as something else? If the former, the BODS code
would do and the local code could be retired.

<a name="q-bo-05"></a>
**Q-BO-05 — object of a power, and default taker.** These two `rb-ubo` trust roles have
no BODS code. They are real roles in common-law arrangements, and appear in the UK
Companies House register. Open Ownership accepts feature requests against the standard;
if WE BUILD needs them, they are worth proposing upstream rather than keeping local.

<a name="q-bo-06"></a>
**Q-BO-06 — `level: joint`.** All three rulebooks offer `joint` alongside `direct` and
`indirect`. BODS treats joint holding as several interests, or as acting in concert
under `otherInfluenceOrControl`, because jointness is not a degree of directness: a
jointly held interest is still either direct or indirect. Is `joint` meant to be a
fourth value of the same axis, or a separate flag?

<a name="q-bo-07"></a>
**Q-BO-07 — mandatory quantities on interests where they do not apply.**
`rb-ownership` makes `interests.percentage`, `interests.quantity` and `interests.rights`
all mandatory, and `rb-control` makes `controls.rights` mandatory, for every interest
including `trustee`, `protector` and `settlor`. The rulebook's own example payload in
section 5.1.3 shows the result: a family trust recorded as
`beneficiaryOfLegalArrangement` with `"quantity": 0`, a value that is not true but is
required. BODS makes `share` optional per interest for this reason. Should these become
conditional on the interest type?

Separately, `rb-control` section 3.2 lists `controls.voting_percentage` as mandatory
while the encoding table in section 5.1.1 marks it optional, `MAY`. The two should
agree.

<a name="q-bo-08"></a>
**Q-BO-08 — `controls.basis`.** `controls.basis` has no counterpart in either
vocabulary, and overlaps `controls.type` substantially: `shareholding` as a basis
against `voting_rights` as a type, `contractual` in both lists. Is `basis` carrying
information `type` does not?

<a name="q-bo-09"></a>
**Q-BO-09 — identity document scheme tokens.** `rb-ubo` carries `document_type` and
`issuing_country` separately; BODS composes them into one `scheme` token,
`{alpha-3}-{PASSPORT|TAXID|IDCARD}`. The rulebook's `RESIDENCE_PERMIT` and
`DRIVING_LICENSE` have no BODS token. Mapping is mechanical in the
rulebook → BODS direction; is the reverse needed?

<a name="q-bo-10"></a>
**Q-BO-10 — three evidence code lists.** `rb-ownership` and `rb-control` share a
seven-value list; `rb-ubo` has a different ten-value list with different spelling.
Should the three converge?

<a name="q-bo-11"></a>
**Q-BO-11 — `form` and `legal_form`.** `rb-ownership` and `rb-control` both carry
`entity.form`, a nine-value local list, and `entity.legal_form`, free text, as separate
mandatory attributes. `ebwv:legalForm` covers the concept once. This was already raised
on PR #197. Can one of the two go?

<a name="q-bo-12"></a>
**Q-BO-12 — the ownership path.** An indirect holding is recorded as a percentage with
no statement of which intermediate entity it runs through, even where that entity is
listed elsewhere in the same `owner[]` array. `rb-ubo` section 3.1 derives its UBO list
by applying the 25% threshold to the Ownership and Control lists, which only works if
the path is traversable. Should an interest reference the intermediary it is held
through, as `ebwv:shareInFocusAlongBranch` and BODS relationship statements both do?

<a name="q-bo-13"></a>
**Q-BO-13 — `GwG` methods under an AMLR basis.** The `ebwv` beneficial-ownership module
encodes German `GwG` calculation methods and 10% thresholds, and a notional-owner
fallback that AMLR does not have. The three rulebooks name AMLR as their basis. Which
governs where they differ, and should the rulebooks reference the `ebwv` module at all
until that is settled?

<a name="q-bo-14"></a>
**Q-BO-14 — the AMLR citation in `rb-ubo`.** `rb-ubo` section 1 and section 4.4.2 both
cite AMLR Article 3(17) as the definition of beneficial owner, and quote three limbs:
holding 25% or more of the units in a collective investment undertaking, the ability to
define or influence its investment policy, and controlling its activities through other
means. Those three limbs are the collective-investment-undertaking test in **Article
61**, which operates as a derogation from Articles 51 and 58(1); Article 3 is the
definitions article. As cited, the rulebook appears to apply a CIU-specific test as the
general definition of a UBO. Please confirm the intended citation.

## 8 References

| Item | Details |
| --- | --- |
| [BODS] | Beneficial Ownership Data Standard, version 0.4. Open Ownership. https://standard.openownership.org/en/0.4.0/ |
| [BODS-RDF] | BODS RDF Vocabulary 0.4.0. https://vocab.openownership.org/ — Turtle at https://vocab.openownership.org/terms/bods-vocabulary-0.4.0.ttl |
| [BODS-CODES] | BODS code lists, authoritative CSVs. https://github.com/openownership/data-standard/tree/0.4.0/schema/codelists |
| [BODS-MODEL] | The BODS data model. https://standard.openownership.org/en/main/primer/datamodel.html |
| [EBWV] | European Business Wallet Vocabulary. https://w3id.org/ebwv |
| [AMLR 2024/1624] | Regulation (EU) 2024/1624 on the prevention of the use of the financial system for the purposes of money laundering or terrorist financing |
| [WP4-58] | Proposal to use the BODS RDF Vocabulary as the semantic backbone for the ownership, control and UBO terms. https://github.com/webuild-consortium/wp4-semantics-group/issues/58 |
| [WP4-59] | Semantic intake submission for the Ownership, Control and UBO use case. https://github.com/webuild-consortium/wp4-semantics-group/pull/59 |
