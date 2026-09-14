# ComparisonReport

*4 fields · module: Portfolio & Real-Estate Transactions · Postgres: `comparison_report`*

A saved competitive-comparison report with its own assigned page layout.

Source: `data-fields/small-miscellaneous-entities.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 4 |
| Catalogued fields | 3 (3 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 1 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 2 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [RPT-R-030](../rules/RPT-R-030.md) | A Comparison Report is a first-class record (`ComparisonReport`) that still delegates its rendering to a `PageLayout` (`PageLayoutID`, required). Even the bespoke report types run on the generic layout engine. | Observed |
| [POR-R-008](../rules/POR-R-008.md) | A user compares competing sites or scenarios · `ComparisonReport` → `ComparisonItem` · `ComparisonItem.ComputedValue`/`ExpenseGroup` hold computed comparison output; `ScenarioName`/`ScenarioDate` are plain text, not FKs — a comparison item  | Observed |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `PageLayoutID` | Comparison Report Layout | item ID | Global | yes | unresolved |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ComparisonReportID` | Comparison Report RecID | Number | Global |  |  |

### Audit & record keeping (1)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Comparison Report ClientID | Text | Global | yes |  |
