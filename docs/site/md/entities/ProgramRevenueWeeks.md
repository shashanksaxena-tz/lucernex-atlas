# ProgramRevenueWeeks

*13 fields · module: Portfolio & Real-Estate Transactions · Postgres: `program_revenue_weeks`*

Weekly revenue-target tracking (filled/unfilled targets and weeks) for a development Program, feeding DevelopmentSlot planning.

Source: `data-fields/small-miscellaneous-entities.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 13 |
| Fields with a vendor definition | 12 of 13 inventoried |
| Physical tables | `program_revenue_weeks` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 14 (14 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 2 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 1 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in program_revenue_weeks

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 12 fields carry a vendor definition

**Observed.** 12 of this record's 13 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one source in the corpus that explains fields rather than listing them.

### 3 fields marked required

**Observed.** The inventory marks 3 of this record's fields Required. Across the whole inventory that is 606 fields, which independently corroborates the 603 the corpus had derived from the Data Fields catalogue — two sources, arrived at separately, agreeing to within three.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [POR-R-007](../rules/POR-R-007.md) | A rollout program needs capacity tracking · `DevelopmentPlan` → `DevelopmentSlot` → `ProgramRevenueWeeks` · Rolls up filled/unfilled slot and week counts per `Program`. No FK connects a `DevelopmentSlot` to the specific `PotentialProject`/` | Derived |

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ProjectEntityID` |  |  | Entity ID | — |  | `program_revenue_weeks.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Quantities (9)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `NumberCurrentFilledSlots` | Current Filled Targets | The number of filled targets. | Number | Global |  | `program_revenue_weeks.NumberCurrentFilledSlots · TEXT` |  |
| `NumberCurrentFilledWeeks` | Current Filled Weeks | The number of filled weeks. | Number | Global |  | `program_revenue_weeks.NumberCurrentFilledWeeks · TEXT` |  |
| `NumberCurrentTotalSlots` | Current Targets | The total number of targets for this set of revenue weeks. | Number | Global |  | `program_revenue_weeks.NumberCurrentTotalSlots · TEXT` |  |
| `NumberCurrentTotalWeeks` | Current Weeks | The total number of revenue weeks. This field's value is equal to the sum of all of the revenue weeks of each target. | Number | Global |  | `program_revenue_weeks.NumberCurrentTotalWeeks · TEXT` |  |
| `NumberCurrentUnfilledSlots` | Current Unfilled Targets | The number of unfilled targets. | Number | Global |  | `program_revenue_weeks.NumberCurrentUnfilledSlots · TEXT` |  |
| `NumberCurrentUnfilledWeeks` | Current Unfilled Weeks | The number of unfilled weeks. | Number | Global |  | `program_revenue_weeks.NumberCurrentUnfilledWeeks · TEXT` |  |
| `NumberOfSlots` | Goal Targets | The number of goal targets. | Number | Global | yes | `program_revenue_weeks.NumberOfSlots · TEXT` |  |
| `ProgramRevenueWeeksID` | Program Revenue Weeks RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `program_revenue_weeks.ProgramRevenueWeeksID · VARCHAR(64) NOT NULL` |  |
| `RevenueWeeks` | Goal Weeks | The number of goal weeks. | Number | Global | yes | `program_revenue_weeks.RevenueWeeks · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Program Revenue Weeks ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `program_revenue_weeks.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `program_revenue_weeks.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `program_revenue_weeks.ModifiedDate · TEXT` |  |
