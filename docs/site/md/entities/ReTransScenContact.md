# ReTransScenContact

*28 fields · module: Portfolio & Real-Estate Transactions · Postgres: `re_trans_scen_contact`*

Contact record specific to a real-estate transaction scenario (distinct from LinkReTransScenContact, the join-style variant) — contact type, employer name, email. 28 Global fields under RE Transaction.

Source: `data-fields/re-trans-scen-contact.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 28 |
| Catalogued fields | 28 (28 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 1 keys from 1 record types |
| Points at | 4 other records |
| Tenancy position | firm_global |
| Rules that name it | 0 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `JurisdictionID` | Jurisdiction | County ID | Global |  | [Jurisdiction](Jurisdiction.md) |
| `StateProvinceCountryID` | State Province Country | Country, State, County ID | Global |  | [StateProvinceCountry](StateProvinceCountry.md) |

### Coded values (drop-downs) (3)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeContactTypeID` | Contact Type | Dropdown (Contact Type Code) | Global |  | Contact Type Code |
| `CodeJobFunctionID` | Job Function | Dropdown (Job Function Code) | Global |  | Job Function Code |
| `CodeJobTitleID` | Job Title | Dropdown (Job Title Code) | Global |  | Job Title Code |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ReTransScenContactID` | RE Trans Scen Contact ID | Number | Global |  |  |

### Text & notes (18)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `City` |  | Text | Global |  |  |
| `EMail1` | E Mail #1 | Text | Global |  |  |
| `EmployerName` | Employer Name | Text | Global | yes |  |
| `FirstName` | First Name | Text | Global | yes |  |
| `LastName` | Last Name | Text | Global | yes |  |
| `MiddleName` | Middle Name | Text | Global |  |  |
| `MobileNumber` | Mobile Number | Text | Global |  |  |
| `NameFirstLast` | Name (First Last) | Text | Global |  |  |
| `NameLastFirst` | Name (Last First) | Text | Global |  |  |
| `Notes` |  | Text | Global |  |  |
| `Phone` |  | Text | Global |  |  |
| `PostalCode` | Postal Code | Text | Global |  |  |
| `StreetAddress1` | Street Address #1 | Text | Global |  |  |
| `StreetAddress2` | Street Address #2 | Text | Global |  |  |
| `StreetAddress3` | Street Address #3 | Text | Global |  |  |
| `StreetAddress4` | Street Address #4 | Text | Global |  |  |
| `Suffix` |  | Text | Global |  |  |
| `Title` |  | Text | Global |  |  |

### Audit & record keeping (4)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |

## What points here (1 keys)

| Record type | Via column |
|---|---|
| [LinkReTransScenContact](LinkReTransScenContact.md) | `ReTransScenContactID` |
