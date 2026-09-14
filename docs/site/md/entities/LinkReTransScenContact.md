# LinkReTransScenContact

*33 fields · module: Portfolio & Real-Estate Transactions · Postgres: `link_re_trans_scen_contact`*

A join record linking a real-estate transaction Scenario to a contact (broker, attorney) with contact-type classification and email. 32 Global fields under RE Transaction — despite the Link-style name, at 32 fields it is treated as standalone rather than folded into the small Link bucket.

Source: `data-fields/link-re-trans-scen-contact.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 33 |
| Catalogued fields | 32 (32 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 8 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Fields

### Relationships (foreign keys) (6)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `JurisdictionID` | Jurisdiction | County ID | Global |  | [Jurisdiction](Jurisdiction.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |
| `RETransactionID` | RE Transaction | RE Transaction ID | Global |  | [RETransaction](RETransaction.md) |
| `ReTransScenContactID` | RE Transaction Contact | RE Transaction Contact ID | Global |  | [ReTransScenContact](ReTransScenContact.md) |
| `ScenarioID` | Scenario | Scenario ID | Global |  | [Scenario](Scenario.md) |
| `StateProvinceCountryID` | State Province Country | Country, State, County ID | Global |  | [StateProvinceCountry](StateProvinceCountry.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `PersonID` | Company Contact | Contact | Global |  |  |

### Coded values (drop-downs) (3)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeContactTypeIDList` | Contact Type | Dropdown (Contact Type Code) | Global |  | Contact Type Code |
| `CodeJobTitleID` | Job Title | Dropdown (Job Title Code) | Global |  | Job Title Code |
| `ICodeJobFunctionID` | Job Function | Dropdown (Job Function Code) | Global |  | Job Function Code |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `LinkReTransScenContactID` | RE Transaction Scenario Contact RecID | Number | Global |  |  |

### Text & notes (17)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `City` |  | Text | Global |  |  |
| `EMail1` | E Mail #1 | Text | Global |  |  |
| `EmployerName` | Employer Name | Text | Global |  |  |
| `FirstName` | First Name | Text | Global |  |  |
| `LastName` | Last Name | Text | Global |  |  |
| `MiddleName` | Middle Name | Text | Global |  |  |
| `MobileNumber` | Mobile Number | Text | Global |  |  |
| `NameFirstLast` | Name (First Last) | Text | Global |  |  |
| `NameLastFirst` | Name (Last First) | Text | Global |  |  |
| `Phone` |  | Text | Global |  |  |
| `PostalCode` | Postal Code | Text | Global |  |  |
| `StreetAddress1` | Street Address #1 | Text | Global |  |  |
| `StreetAddress2` | Street Address #2 | Text | Global |  |  |
| `StreetAddress3` | Street Address #3 | Text | Global |  |  |
| `StreetAddress4` | Street Address #4 | Text | Global |  |  |
| `Suffix` |  | Text | Global |  |  |
| `Title` |  | Text | Global |  |  |

### Audit & record keeping (5)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | RE Transaction Scenario Contact ClientID | Text | Global | yes |  |
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
