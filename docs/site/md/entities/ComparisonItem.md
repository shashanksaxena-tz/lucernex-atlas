# ComparisonItem

*9 fields · module: Portfolio & Real-Estate Transactions · Postgres: `comparison_item`*

One line in a competitive/market comparison analysis, with a computed value and expense-group total.

Source: `data-fields/small-miscellaneous-entities.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 9 |
| Fields with a vendor definition | 8 of 9 inventoried |
| Physical tables | `comparison_item` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 8 (8 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 1 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 2 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in comparison_item

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 8 fields carry a vendor definition

**Observed.** 8 of this record's 9 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one source in the corpus that explains fields rather than listing them.

### 2 fields marked required

**Observed.** The inventory marks 2 of this record's fields Required. Across the whole inventory that is 606 fields, which independently corroborates the 603 the corpus had derived from the Data Fields catalogue — two sources, arrived at separately, agreeing to within three.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [RPT-R-031](../rules/RPT-R-031.md) | A Comparison Report's cells live in `ComparisonItem`, one row per scenario column, carrying `ScenarioName`, `ScenarioDate`, `ExpenseGroup`, `Assumptions`, `ComputedValue` and a serialised `XmlData` payload. · Observed · `_lucernex_objects_s | Observed |
| [POR-R-008](../rules/POR-R-008.md) | A user compares competing sites or scenarios · `ComparisonReport` → `ComparisonItem` · `ComparisonItem.ComputedValue`/`ExpenseGroup` hold computed comparison output; `ScenarioName`/`ScenarioDate` are plain text, not FKs — a comparison item  | Observed |

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ProjectEntityID` |  |  | Entity ID | — |  | `comparison_item.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ComparisonItemID` | Comparison Item RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `comparison_item.ComparisonItemID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (1)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ScenarioDate` | Scenario Date | Enter the date of the comparison scenario in this field. | Date | Global |  | `comparison_item.ScenarioDate · TEXT` |  |

### Text & notes (5)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Assumptions` |  | This field is a placeholder that is used to hold assumptions. | Text | Global |  | `comparison_item.Assumptions · TEXT` |  |
| `ComputedValue` | Computed Value | This field is a placeholder that is used when calculating values in a comparison report. | Text | Global |  | `comparison_item.ComputedValue · TEXT` |  |
| `ExpenseGroup` | Expense Group Total | This field is a placeholder that is used to hold expense group totals. | Text | Global |  | `comparison_item.ExpenseGroup · TEXT` |  |
| `ScenarioName` | Scenario Name | Enter the name of the comparison scenario in this field. | Text | Global |  | `comparison_item.ScenarioName · TEXT` |  |
| `XmlData` | Scenario XmlData | This field is used to save data values for a comparison report. | Text | Global | yes | `comparison_item.XmlData · TEXT` |  |

### Audit & record keeping (1)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Comparison Item ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `comparison_item.BOMapClientRecordID · TEXT` |  |
