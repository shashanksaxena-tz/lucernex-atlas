# FiscalPeriod

*17 fields · module: Lease Accounting & Payments · Postgres: `fiscal_period`*

The fiscal calendar definition — begin/end date and days-in-period per named fiscal period, the calendar backbone that SLPeriod, ExpenseSchedule, and Sales fiscal-period fields reference. 16 Global fields under Company Items.

Source: `data-fields/fiscal-period.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 17 |
| Fields with a vendor definition | 16 of 17 inventoried |
| Physical tables | `fiscal_period` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 16 (16 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 3 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 3 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in fiscal_period

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 16 fields carry a vendor definition

**Observed.** 16 of this record's 17 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: the captures agree

**Observed.** Over the 16 fields both the Data Fields catalogue and the field inventory contain, the two agree on every one. 6 are marked required.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [ACC-R-028](../rules/ACC-R-028.md) | one `SLPeriod` per fiscal period, carrying `BeginDate`, `EndDate`, `NumberDays`, `FiscalPeriod`, `FiscalPeriodYear`, `CumulativePeriodNumber` | Derived |
| [CON-R-023](../rules/CON-R-023.md) | Determining the fiscal calendar: the calendar is owned by Contract.ProgramID (the portfolio), not by the firm. | Observed |
| [CON-R-024](../rules/CON-R-024.md) | A retail fiscal period is used: periods may be 4 or 5 weeks (retail 4-5-4), not calendar months, per FiscalPeriod.Is4or5WeekPeriod. | Observed |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ProgramID` | Portfolio | Select the Portfolio that the record belongs to from this field. | Portfolio ID | Global |  | `fiscal_period.ProgramID · TEXT` | [Program](Program.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `fiscal_period.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `MatchingCalendarMonth` | Matching Calendar Month | The calendar month that this fiscal period overlaps with. | Dropdown | Global |  | `fiscal_period.MatchingCalendarMonth · TEXT` |  |

### Quantities (7)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `FiscalPeriodID` | Fiscal Period RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `fiscal_period.FiscalPeriodID · VARCHAR(64) NOT NULL` |  |
| `MatchingCalendarYear` | Matching Calendar Year | The calendar year that this fiscal period overlaps with. | Number | Global |  | `fiscal_period.MatchingCalendarYear · TEXT` |  |
| `NumberDaysInPeriod` | Days In Period | Calculates how many days are in the period. | Number | Global |  | `fiscal_period.NumberDaysInPeriod · TEXT` |  |
| `NumberWeeksInPeriod` | Weeks In Period | Calculates how many weeks are in the period. | Number | Global |  | `fiscal_period.NumberWeeksInPeriod · TEXT` |  |
| `Period` |  | The period number. | Number | Global | yes | `fiscal_period.Period · TEXT` |  |
| `Quarter` |  | The quarter number. | Number | Global | yes | `fiscal_period.Quarter · TEXT` |  |
| `Year` |  | The fiscal year. | Number | Global | yes | `fiscal_period.Year · TEXT` |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BeginDate` | Begin Date | The Begin Date field allows you to select a begin date for the record. | Date | Global | yes | `fiscal_period.BeginDate · TEXT` |  |
| `EndDate` | End Date | The End Date field allows you to select an end date for the record. | Date | Global | yes | `fiscal_period.EndDate · TEXT` |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Is4or5WeekPeriod` | Is 4 or 5 Week Period? | This field determines how many weeks are in the fiscal period. It has two potential values: 4 weeks or 5 weeks. | Boolean | Global |  | `fiscal_period.Is4or5WeekPeriod · TEXT` |  |

### Text & notes (1)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `FiscalPeriodName` | Fiscal Period Name | This field is not implemented. | Text | Global |  | `fiscal_period.FiscalPeriodName · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Fiscal Period ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `fiscal_period.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `fiscal_period.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `fiscal_period.ModifiedDate · TEXT` |  |
