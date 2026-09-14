# AcctingAssumptionAdjust

*19 fields · module: Lease Accounting & Payments · Postgres: `accting_assumption_adjust`*

A manual adjustment to lease-accounting assumptions used in ASC 842/IFRS 16 calculations — adjustment percent and annual amount, letting an accountant override a calculated assumption. 18 Global fields under Contract.

Source: `data-fields/accting-assumption-adjust.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 19 |
| Catalogued fields | 18 (18 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 3 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 2 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [ACC-R-020](../rules/ACC-R-020.md) | `SLSummary.NeedsRecalculation := true` | Observed |
| [ACC-R-026](../rules/ACC-R-026.md) | the stated percentage of the amount is allocated to a secondary schedule; the remainder to the primary | Observed |

## Fields

### Relationships (foreign keys) (3)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ContractID` | Contract | Contract ID | Global | yes | [Contract](Contract.md) |
| `ExpenseSetupID` | Expense Setup | Expense Setup ID | Global |  | [ExpenseSetup](ExpenseSetup.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (4)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeASC842ScheduleID` | ASC 842 Schedule | Dropdown (ASC 842 Schedule Type) | Global |  | ASC 842 Schedule Type |
| `CodeFrequencyID` | Frequency | Dropdown (Frequency Code) | Global |  | Frequency Code |
| `CodeIFRS16ScheduleID` | IFRS 16 Schedule | Dropdown (IFRS 16 Schedule Type) | Global |  | IFRS 16 Schedule Type |
| `CodeProrationMethodID` | Proration Method | Dropdown (Proration Method Code) | Global |  | Proration Method Code |

### Money (5)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AnnualAmount` | Annual Amount | Currency | Global | yes |  |
| `FirstPaymentAmount` | First Payment Amount | Currency | Global |  |  |
| `LastPaymentAmount` | Last Payment Amount | Currency | Global |  |  |
| `PaymentAmount` | Payment Amount | Currency | Global | yes |  |
| `PaymentRate` | Payment Rate | Currency | Global |  |  |

### Rates & percentages (2)

Percentage inputs and computed rates.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AdjustmentPercent` | Adjustment Percent | Percentage | Global |  |  |
| `SecondaryRentSchedAllocPercent` | Accounting Assumption Adjustment Secondary Rent Schedule Allocation Percent | Percentage | Global |  |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AcctingAssumptionAdjustID` | Accting Assumption Adjust RecID | Number | Global |  |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BeginDate` | Begin Date | Date | Global | yes |  |
| `EndDate` | End Date | Date | Global | yes |  |

### Text & notes (1)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Notes` |  | Text | Global |  |  |

### Audit & record keeping (1)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Accting Assumption Adjust ClientID | Text | Global | yes |  |
