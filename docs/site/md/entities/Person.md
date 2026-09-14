# Person

*37 fields · module: People & Parties · Postgres: `person`*

An individual contact record (broker, attorney, property manager) distinct from Employer (the company) and Member (internal user) — billing rates, multiple email/phone slots, and job-title code linkage. 37 Global fields under Company Items.

Source: `data-fields/person.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 37 |
| Catalogued fields | 37 (37 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 4 other records |
| Tenancy position | firm_global |
| Rules that name it | 4 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [PPL-R-001](../rules/PPL-R-001.md) | `Person` and `NonMember` are field-for-field identical (37/37, zero type mismatches); `Member` is that same 37-field block plus 44 login/authorization fields | Derived |
| [PPL-R-002](../rules/PPL-R-002.md) | No `Person ID` FK type exists anywhere in the 60-odd declared FK types | Inferred |
| [PPL-R-003](../rules/PPL-R-003.md) | The existing identity is promoted to carry login/authorization data; it is not deleted and recreated. The exact mechanics (same row extended vs. new row sharing `PersonID`) are open — see `member-vs-person-vs-party.md` open question 1 | Inferred |
| [AST-R-009](../rules/AST-R-009.md) | Input: For each of the three event types, a `Code{X}PartyID` (Responsible Party code), `{X}ResponsiblePersonID` (a `Person` contact), `Code{X}RemedyID` (a Maintenance Remedy code), and `{X}MaximumRemedyDays` (a day count) — twelve fields to | Observed |

## Fields

### Relationships (foreign keys) (3)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `EmployerID` | Employer | Employer ID | Global | yes | [Employer](Employer.md) |
| `IStateProvinceCountryID` | State | Country, State, County ID | Global |  | [StateProvinceCountry](StateProvinceCountry.md) |
| `JurisdictionID` | Jurisdiction | County ID | Global |  | [Jurisdiction](Jurisdiction.md) |

### Coded values (drop-downs) (4)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeContactTypeIDList` | Contact Type List | Dropdown (Contact Type Code) | Global | yes | Contact Type Code |
| `CodeJobFunctionID` | Job Function | Dropdown (Job Function Code) | Global | yes | Job Function Code |
| `CodeJobTitleID` | Job Title | Dropdown (Job Title Code) | Global |  | Job Title Code |
| `CodeJobTitleIDList` | Job Titles | Dropdown (Job Title Code) | Global |  | Job Title Code |

### Money (2)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BillRate1` | Billing Rate #1 | Currency | Global |  |  |
| `BillRate2` | Billing Rate #2 | Currency | Global |  |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `PersonID` | Person RecID | Number | Global |  |  |

### Flags (2)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Inactive` | Is Inactive? | Boolean | Global | yes |  |
| `UseEmployerAddress` | Use Employer Address | Boolean | Global | yes |  |

### Text & notes (22)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `City` |  | Text | Global |  |  |
| `CountryID` | Country | Text | Global |  |  |
| `Description` |  | Text | Global |  |  |
| `Designations` |  | Text | Global |  |  |
| `EMail1` | Email #1 | Text | Global |  |  |
| `EMail2` | Email #2 | Text | Global |  |  |
| `Fax` |  | Text | Global |  |  |
| `FirstName` | First Name | Text | Global | yes |  |
| `LastName` | Last Name | Text | Global | yes |  |
| `MiddleName` | Middle Name | Text | Global |  |  |
| `MobileNumber` | Mobile Number | Text | Global |  |  |
| `Phone` |  | Text | Global |  |  |
| `PhoneExtension` | Phone Extension | Text | Global |  |  |
| `PostalCode` | Postal Code | Text | Global |  |  |
| `StreetAddress1` | Street Address #1 | Text | Global |  |  |
| `StreetAddress2` | Street Address #2 | Text | Global |  |  |
| `StreetAddress3` | Street Address #3 | Text | Global |  |  |
| `StreetAddress4` | Street Address #4 | Text | Global |  |  |
| `Suffix` |  | Text | Global |  |  |
| `Title` |  | Text | Global |  |  |
| `WebSite` | Website | Text | Global |  |  |
| `WirelessEMail` | Wireless Email | Text | Global |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Person ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
