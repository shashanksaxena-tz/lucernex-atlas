# FiscalPeriod

*17 fields · module: Lease Accounting & Payments · Postgres: `fiscal_period`*

The fiscal calendar definition — begin/end date and days-in-period per named fiscal period, the calendar backbone that SLPeriod, ExpenseSchedule, and Sales fiscal-period fields reference. 16 Global fields under Company Items.

Source: `data-fields/fiscal-period.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 17 |
| Catalogued fields | 16 (16 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 3 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 3 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [ACC-R-028](../rules/ACC-R-028.md) | one `SLPeriod` per fiscal period, carrying `BeginDate`, `EndDate`, `NumberDays`, `FiscalPeriod`, `FiscalPeriodYear`, `CumulativePeriodNumber` | Derived |
| [CON-R-023](../rules/CON-R-023.md) | Determining the fiscal calendar: the calendar is owned by Contract.ProgramID (the portfolio), not by the firm. | Observed |
| [CON-R-024](../rules/CON-R-024.md) | A retail fiscal period is used: periods may be 4 or 5 weeks (retail 4-5-4), not calendar months, per FiscalPeriod.Is4or5WeekPeriod. | Observed |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ProgramID` | Portfolio | Portfolio ID | Global |  | [Program](Program.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `MatchingCalendarMonth` | Matching Calendar Month | Dropdown | Global |  |  |

### Quantities (7)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `FiscalPeriodID` | Fiscal Period RecID | Number | Global |  |  |
| `MatchingCalendarYear` | Matching Calendar Year | Number | Global |  |  |
| `NumberDaysInPeriod` | Days In Period | Number | Global |  |  |
| `NumberWeeksInPeriod` | Weeks In Period | Number | Global |  |  |
| `Period` |  | Number | Global | yes |  |
| `Quarter` |  | Number | Global | yes |  |
| `Year` |  | Number | Global | yes |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BeginDate` | Begin Date | Date | Global | yes |  |
| `EndDate` | End Date | Date | Global | yes |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Is4or5WeekPeriod` | Is 4 or 5 Week Period? | Boolean | Global |  |  |

### Text & notes (1)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `FiscalPeriodName` | Fiscal Period Name | Text | Global |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Fiscal Period ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
