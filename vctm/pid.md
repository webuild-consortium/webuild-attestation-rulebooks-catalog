---
vct: urn:euditest:pid:1
background_color: "#003087"
text_color: "#ffffff"
---

# Personal Identification Data (PID)

A verifiable credential that identifies a natural person within the EUDI Wallet ecosystem, as defined in CIR 2024/2977 and the ARF PID Rulebook.

## Claims

- `given_name` "Given Name" (string): Current first name(s), including middle name(s) where applicable [mandatory]
- `family_name` "Family Name" (string): Current last name(s) or surname(s) [mandatory]
- `birthdate` "Date of Birth" (date): Date of birth in ISO 8601 YYYY-MM-DD format [mandatory]
- `place_of_birth` "Place of Birth" (object): Place where the person was born [mandatory]
  - `country` (string): Alpha-2 country code (ISO 3166-1)
  - `region` (string): State, province, district, or local area
  - `locality` (string): Municipality, city, town, or village
- `nationalities` "Nationalities" (array): One or more alpha-2 country codes (ISO 3166-1) [mandatory]
  - (string): Alpha-2 country code
- `address` "Address" (object): Current residence address
  - `formatted` (string): Full mailing address, formatted for display
  - `street_address` (string): Full street address component
  - `house_number` (string): House number including any affix or suffix
  - `locality` (string): City or locality component
  - `region` (string): State, province, prefecture, or region component
  - `postal_code` (string): Zip code or postal code component
  - `country` (string): Country name component
- `birth_family_name` "Family Name at Birth" (string): Last name(s) at the time of birth
- `birth_given_name` "Given Name at Birth" (string): First name(s) at the time of birth
- `sex` "Sex" (number): 0=not known, 1=male, 2=female, 3=other, 4=inter, 5=diverse, 6=open, 9=not applicable
- `email` "Email Address" (string): Electronic mail address
- `phone_number` "Mobile Phone Number" (string): Mobile telephone number in E.164 format
- `picture` "Portrait" (image): Facial image in JPEG format as data URL
- `personal_administrative_number` "Personal Administrative Number" (string): Unique personal administrative number assigned by the PID Provider
- `date_of_expiry` "Expiry Date" (date): Administrative expiry date in ISO 8601 YYYY-MM-DD format [mandatory]
- `date_of_issuance` "Issuance Date" (date): Date when the PID was issued in ISO 8601 YYYY-MM-DD format
- `issuing_authority` "Issuing Authority" (string): Name of the administrative authority that issued the PID [mandatory]
- `issuing_country` "Issuing Country" (string): Alpha-2 country code of the PID Provider's country [mandatory]
- `document_number` "Document Number" (string): Number assigned by the PID Provider
- `issuing_jurisdiction` "Issuing Jurisdiction" (string): Country subdivision code per ISO 3166-2
- `attestation_legal_category` "Attestation Legal Category" (string): Legal category; SHALL be PID [mandatory] [sd=never]
- `trust_anchor` "Trust Anchor" (string): URL of the machine-readable trust anchor for verifying the PID
