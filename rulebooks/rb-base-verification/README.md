# Rulebook for base-verification of the attestation  

*Provide information about the author(s) of this Rulebook in the following form:*

* Author(s):
  * [Folkendt Werner , Robert Bosch GmbH]
* 
* Reviewer(s):
  * [Florin Coptil, Robert Bosch GmbH]
  * [ .... ] 

*Provide versioning information about the Rulebook in the following form:*

| Version | Date       | Description                                                     |
|---------|------------|-----------------------------------------------------------------|
| 0.1     | 06.05.2026 | Initial draft based on the WeBuild design attestations mettings |

*Provide a contact email address and/or a link to an issue tracking system that can be used for
providing feedback, e.g.:*
Contact: 

**Feedback:**

## Intro
When a Relying Party (RP) receives an attestation, the immediate challenge is to determine whether the information it contains can be genuinely trusted. This document establishes the essential verification processes that an RP SHALL implement to ensure the integrity and authenticity of attestation data. These foundational checks, elaborated in Chapter 4.2, serve as the universal starting point for evaluating any attestation. Beyond the technical validation, RPs are also obligated to scrutinize the attestation's issuance process. This dual-pronged approach – verifying both the attestation's content and its creation – is critical for establishing confidence and clarifying liability within the attestation ecosystem. While the initial steps provide a common baseline, more intricate attestations may necessitate additional verification measures.

## 4.2 Relying Party Obligations ##

### 4.2.1 Verify Cryptographic Integrity ###
- Validate the digital signature over the attestation using the issuer's public key
- For SD-JWT VC: Verify JWT signature and validate all disclosed claims
### 4.2.2 Validate Issuer ###

#### 4.2.2.1 Authentification ####
- Verification of the certifications  in the chain

#### 4.2.2.2 Identification ####
- Verification of the intermediate certifications in the chain against TLOL and TLOL - historie

#### 4.2.2.3 Authorization ####
- Verify that the issuer is authorized to issue Payment Terms Attestations
- Check the issuer's credentials against the appropriate trust framework (see Chapter 5)
- For "EAA": Confirm issuer authorization mechanisms

### 4.2.3 Holder Wallet Related check ###
#### 4.2.3.1.Device binding  ####
- Check copy & reply
#### 4.2.3.1.WUA check ####
- Check WUA

### 4.2.4 Holder Related check ###
#### 4.2.4.1. Revocation status check ####
- Query the designated revocation/status mechanism (Cap 6)
- Treat revoked or suspended attestations as invalid
- Handle the status according to organizational risk policy

#### 4.2.4.2. Check Temporal Validity ####
- Validate issuanceDate / iat to ensure the attestation was issued in the past
- Validate expirationDate / exp to ensure the attestation has not expired
- Consider attestation age in relation to business risk 