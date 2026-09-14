# AlternateRentSchedule

*25 fields · module: Lease Accounting & Payments · Postgres: `alternate_rent_schedule`*

An alternate/contingency rent calculation method available on a contract — alt rent math formula selection and begin date. 24 Global fields under Contract.

Source: `data-fields/alternate-rent-schedule.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 25 |
| Catalogued fields | 24 (24 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 2 keys from 2 record types |
| Points at | 5 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 4 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [ACC-R-055](../rules/ACC-R-055.md) | a hold flag is set on all recurring-expense transactions (resp. percentage-rent transactions) generated during the window | Observed |
| [CON-R-061](../rules/CON-R-061.md) | Offsets are applied: VariableRentOffset and ScheduledOffset, applied via APPLY_OFFSETS, reduce the rent-year obligation. | Observed |
| [CON-R-062](../rules/CON-R-062.md) | Rent already paid is credited: PRPRentDue = PRPTotalRent − SalesPeriodRentPaid − offsets. | Inferred |
| [CON-R-070](../rules/CON-R-070.md) | An AlternateRentSchedule window is active: a substitute rent formula (CodeAltRentMathID, PercentRentRate) replaces the normal one for the window. | Observed |

## Fields

### Relationships (foreign keys) (3)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ContractID` | Contract | Contract ID | Global | yes | [Contract](Contract.md) |
| `ExpenseSetupID` | Expense Setup | Expense Setup ID | Global |  | [ExpenseSetup](ExpenseSetup.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeAltRentMathID` | Alt Rent Math | Dropdown (Alt Rent Math Code) | Global |  | Alt Rent Math Code |
| `CodeSalesGroupID` | Sales Group | Dropdown (Sales Group) | Global |  | Sales Group |

### Money (3)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CapAmount` | Monthly Max Cap(Ceiling) | Currency | Global |  |  |
| `ExpenseReductionAmount` | Expense Reduction Amount | Currency | Global |  |  |
| `FloorAmount` | Monthly Min Cap(Floor) | Currency | Global |  |  |

### Rates & percentages (2)

Percentage inputs and computed rates.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ExpenseReductionPercent` | Expense Reduction Percent | Percentage | Global |  |  |
| `PercentRentRate` | Percent Rent Rate | Percentage | Global |  |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AlternateRentScheduleID` | Alternate Rent Schedule RecID | Number | Global |  |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BeginDate` | Begin Date | Date | Global | yes |  |
| `EndDate` | End Date | Date | Global |  |  |

### Flags (4)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `PRDeductExclusions` | Deduct Exclusions? | Boolean | Global |  |  |
| `SetExpHoldFlag` | Set payments for Recurring Expenses on Hold | Boolean | Global |  |  |
| `SetPRHoldFlag` | Set payments for Percent Rent on Hold | Boolean | Global |  |  |
| `SuspendSL` | Suspend SL? | Boolean | Global |  |  |

### Text & notes (2)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Description` |  | Text | Global |  |  |
| `Notes` |  | Text | Global |  |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Alternate Rent Schedule ClientID | Text | Global | yes |  |
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |

## What points here (2 keys)

| Record type | Via column |
|---|---|
| [PaymentTransaction](PaymentTransaction.md) | `AlternateRentScheduleID` |
| [PaymentTransactionFullImport](PaymentTransactionFullImport.md) | `AlternateRentScheduleID` |
