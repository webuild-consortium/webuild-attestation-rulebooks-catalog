# Rulebook for mutual authentification   

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
Overall Interaction Overview
The following diagram illustrates the overall flow of the mutual authentication scenario and highlights where base-verification steps are triggered:
```mermaid
    sequenceDiagram
    autonumber
    box Holder
    participant HW as Buyer Wallet (Holder Wallet)
    end
    box Relying Party
    participant SP as Seller Portal (RP Portal)
    participant SW as Seller Wallet (RP Wallet)
    participant SIS as Seller Internal System
    end
    box EBWOID Provider
    participant OR as EBWOID Revoc. Serv.
    end
    box Trust Registry
    participant TLOL as TLOL
    end
    box Wallet Provider
    participant WR as WUA Revocation Service
    end
    SP->>SW: Request EBWOID + Attestation (EAA) from Business Partner 
    SW->>SW: Prepare Authorization Request
    SW->>HW: Authorization Request (client_id, request_uri, state)
    HW->>SW: GET Request Object (wallet_metadata, wallet_nonce, state)
    SW->>SW: Generate VerifierInfo + Request Object (JWT)
    SW->>HW: Return signed/encrypted Request Object

    rect rgb(255, 240, 200)
        Note over HW,TLOL: RP Identity Validation (Base Verification Steps 4.2.1–4.2.3)
        HW->>HW: 4.2.1 Verify Cryptographic Integrity
        HW->>TLOL: 4.2.2 Validate Issuer (Auth, Ident, Authz)
        TLOL-->>HW: Trust status confirmed
        HW->>OR: 4.2.4.1 Revocation Status Check
        OR-->>HW: Status returned
        HW->>WR: 4.2.3.2 WUA Check
        WR-->>HW: WUA status confirmed
    end

    HW->>HW: Match DCQL queries, check authorization
    HW->>HW: Create Verifiable Presentations (EBWOID + EAA)
    HW->>SW: POST Authorization Response (vp_token)

    rect rgb(200, 240, 255)
        Note over SW,WR: Holder EBWOID + EAA Validation (Base Verification Steps repeated)
        SW->>SW: Holder EBWOID validation (same steps 4.2.1–4.2.4)
        SW->>SW: Verify EAA data integrity, issuer, revocation
    end

    SW->>SIS: Requested certificate available and verified
```