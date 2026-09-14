# ContractTerm

*26 fields · module: Contracts & Leases · Postgres: `contract_term`*

One renewal/extension term option on a lease — average rent per area unit and area-unit basis, linked to Amendment and Covenant, appearing under both Contract and Wizard (the guided lease-entry flow). 29 fields (26 Global, 3 Firm).

Source: `data-fields/contract-term.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 26 |
| Catalogued fields | 29 (26 global, 3 firm) |
| Physical tables | 1 |
| Referenced by | 5 keys from 5 record types |
| Points at | 5 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 4 |

## What to know before rebuilding this

### 3 tenant custom columns

**Observed.** This record carries 3 physical Firm_-prefixed columns — tenant custom fields are real columns, not rows in a value store, so adding one is a DDL change. That is direct evidence for database-per-tenant and against a shared schema.

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### 3 catalogued Firm-scope fields

**Observed.** Of 29 catalogued fields on this record, 3 are Firm scope — defined by this tenant rather than shipped by the platform. Firm-scope definitions are RGAF rows carrying IsGlobal, FirmID and IsClientExtensionField.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [ACC-R-016](../rules/ACC-R-016.md) | - `TermLength = ExpireDate − CommenceDate` (the contractual term); - `LikelyTermLength` = length through the last term marked Likely on `Abstract Info > Terms`; - `LastLikelyOptionDate` = end date of the last likely term; - `TestTermLength` | Observed |
| [CON-R-028](../rules/CON-R-028.md) | A contract term option is created: the Terms Wizard generates N ContractTerm rows of a stated length from a stated start. | Observed |
| [CON-R-029](../rules/CON-R-029.md) | Accruing over an option term: only terms flagged IncludeTermForAccruals participate in accrual schedules. | Observed |
| [CON-R-128](../rules/CON-R-128.md) | Accrual scope: only ContractTerm rows flagged IncludeTermForAccruals are accrued. | Observed |

## Fields

### Relationships (foreign keys) (4)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AmendmentID` | Amendment | Contract Amendment ID | Global |  | [ContractAmendment](ContractAmendment.md) |
| `ContractID` | Contract | Contract ID | Global | yes | [Contract](Contract.md) |
| `CovenantID` | Covenant | Covenant ID | Global |  | [Covenant](Covenant.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (3)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeBuildingAreaUnitID` | Building Area Unit | Dropdown (Building Area Unit Code) | Global |  | Building Area Unit Code |
| `CodeTermStatusID` | Term Status | Dropdown (Term Status Code) | Global |  | Term Status Code |
| `CodeTermTypeID` | Term Type | Dropdown (Term Type Code) | Global |  | Term Type Code |

### Money (1)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AvgRentPerAreaUnit` | Average Rent Per Area Unit | Currency | Global |  |  |

### Quantities (4)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ContractTermID` | Term RecID | Number | Global |  |  |
| `Firm_OptionRentPSF` | Option Rent PSF | Number | Firm |  |  |
| `LengthOfTerm` | Length | Number | Global |  |  |
| `RentableArea` | Rentable Area | Number | Global |  |  |

### Dates & timestamps (4)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BeginDate` | Coverage Period Begin Date | Date | Global |  |  |
| `EndDate` | Coverage Period End Date | Date | Global |  |  |
| `PaymentBeginDate` | Payment Begin Date | Date | Global |  |  |
| `PaymentEndDate` | Payment End Date | Date | Global |  |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `IncludeTermForAccruals` | Include Term For Accruals? | Boolean | Global |  |  |

### Text & notes (6)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ClientNumber` | Client Number | Text | Global |  |  |
| `Description` |  | Text | Global |  |  |
| `Firm_TermDocument` | Document | Text | Firm |  |  |
| `Firm_TermPage` | Page | Text | Firm |  |  |
| `Notes` |  | Text | Global |  |  |
| `Section` |  | Text | Global |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Term ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |

## What points here (5 keys)

| Record type | Via column |
|---|---|
| [Contract](Contract.md) | `NextAvailableTermID` |
| [ExpenseSchedule](ExpenseSchedule.md) | `ContractTermID` |
| [KeyDate](KeyDate.md) | `ContractTermID` |
| [RETransaction](RETransaction.md) | `KickoffContractTermID` |
| [Scenario](Scenario.md) | `ContractTermID` |
