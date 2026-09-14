# NonMember

*37 fields · module: People & Parties · Postgres: `non_member`*

Not covered by the Data Fields catalogue: this record type appears in the 223-object census but has no row in the catalogue of 6,158 configurable fields, so nothing in the corpus explains it in the vendor's own words. What is known is structural — 37 declared fields, filed under People & Parties, 0 foreign keys pointing at it.

Source: `_lucernex_objects_summary.txt`

## At a glance

|  | Value |
|---|---|
| Fields declared | 37 |
| Catalogued fields | not in the catalogue |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 4 other records |
| Tenancy position | firm_global |
| Rules that name it | 3 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [PPL-R-001](../rules/PPL-R-001.md) | `Person` and `NonMember` are field-for-field identical (37/37, zero type mismatches); `Member` is that same 37-field block plus 44 login/authorization fields | Derived |
| [PPL-R-002](../rules/PPL-R-002.md) | No `Person ID` FK type exists anywhere in the 60-odd declared FK types | Inferred |
| [PPL-R-003](../rules/PPL-R-003.md) | The existing identity is promoted to carry login/authorization data; it is not deleted and recreated. The exact mechanics (same row extended vs. new row sharing `PersonID`) are open — see `member-vs-person-vs-party.md` open question 1 | Inferred |

## Fields

### Relationships (foreign keys) (3)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `EmployerID` |  | Employer ID | — |  | [Employer](Employer.md) |
| `IStateProvinceCountryID` |  | Country, State, County ID | — |  | [StateProvinceCountry](StateProvinceCountry.md) |
| `JurisdictionID` |  | County ID | — |  | [Jurisdiction](Jurisdiction.md) |

### Coded values (drop-downs) (4)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeContactTypeIDList` |  | Dropdown (Contact Type Code) | — |  | Contact Type Code |
| `CodeJobFunctionID` |  | Dropdown (Job Function Code) | — |  | Job Function Code |
| `CodeJobTitleID` |  | Dropdown (Job Title Code) | — |  | Job Title Code |
| `CodeJobTitleIDList` |  | Dropdown (Job Title Code) | — |  | Job Title Code |

### Money (2)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BillRate1` |  | Currency | — |  |  |
| `BillRate2` |  | Currency | — |  |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `PersonID` |  | Number | — |  |  |

### Flags (2)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Inactive` |  | Boolean | — |  |  |
| `UseEmployerAddress` |  | Boolean | — |  |  |

### Text & notes (22)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `City` |  | Text | — |  |  |
| `CountryID` |  | Text | — |  |  |
| `Description` |  | Text | — |  |  |
| `Designations` |  | Text | — |  |  |
| `EMail1` |  | Text | — |  |  |
| `EMail2` |  | Text | — |  |  |
| `Fax` |  | Text | — |  |  |
| `FirstName` |  | Text | — |  |  |
| `LastName` |  | Text | — |  |  |
| `MiddleName` |  | Text | — |  |  |
| `MobileNumber` |  | Text | — |  |  |
| `Phone` |  | Text | — |  |  |
| `PhoneExtension` |  | Text | — |  |  |
| `PostalCode` |  | Text | — |  |  |
| `StreetAddress1` |  | Text | — |  |  |
| `StreetAddress2` |  | Text | — |  |  |
| `StreetAddress3` |  | Text | — |  |  |
| `StreetAddress4` |  | Text | — |  |  |
| `Suffix` |  | Text | — |  |  |
| `Title` |  | Text | — |  |  |
| `WebSite` |  | Text | — |  |  |
| `WirelessEMail` |  | Text | — |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` |  | Text | — |  |  |
| `ModifiedByID` |  | Member ID | — |  | [Member](Member.md) |
| `ModifiedDate` |  | Time | — |  |  |
