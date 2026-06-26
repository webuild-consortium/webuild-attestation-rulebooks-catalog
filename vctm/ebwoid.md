---
vct: urn:eu:ebw:oid:1
background_color: "#003087"
text_color: "#ffffff"
formats:
  - "sd-jwt"
  - "w3c"
---

# European Business Wallet – Owner Identification Data (EBW-OID)

A verifiable credential that uniquely identifies an EBW owner (economic operator or public sector body) within the European Business Wallets ecosystem. Issued as a Pub-EAA or QEAA in accordance with the European Digital Identity Regulation and the EBW proposal (COM 2025/838).

## Claims

- `id` "Business Identifier" (string): EUID where available, otherwise a similar constructed unique per-issuer identifier [mandatory] [sd=never]
- `name` "Legal Name" (string): Official name of the EBW owner (economic operator or public sector body) [mandatory] [sd=never]
- `attestation_legal_category` "Attestation Legal Category" (string): Legal category of the attestation; QEAA or PUB-EAA [mandatory] [sd=never]
- `date_of_expiry` "Expiry Date" (date): Administrative expiry date in ISO 8601 YYYY-MM-DD format [sd=never]
- `issuing_authority` "Issuing Authority" (string): Name of the administrative authority that issued the EBW-OID [mandatory] [sd=never]
- `issuing_country` "Issuing Country" (string): Alpha-2 country code of the provider's country or territory [mandatory] [sd=never]
- `trust_anchor` "Trust Anchor" (string): URL of the machine-readable trust anchor for verifying the EBW-OID [sd=never]
