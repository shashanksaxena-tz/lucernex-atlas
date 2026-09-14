# ReportGroupData

*5 fields · module: Configuration, Layouts, Forms & Reporting · Postgres: `report_group_data`*

Platform metadata for a top-level or subgroup node in this very Data Fields hierarchy — parent group name and firm scoping.

Source: `data-fields/small-miscellaneous-entities.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 5 |
| Catalogued fields | 5 (5 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 0 other records |
| Tenancy position | firm_global |
| Rules that name it | 3 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### No typed relationships either way

**Derived.** Nothing holds a typed foreign key into this record and it declares none out. Either it is joined by a soft reference the census cannot see, or it is genuinely standalone — worth settling before anything is built on it.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [LAY-R-171](../rules/LAY-R-171.md) | The list is a `ReportGroupData` node; its fields are `ReportGroupAvailableField` leaves; | Observed |
| [RPT-R-041](../rules/RPT-R-041.md) | Audit entries are filed under the field registry's group tree — `AuditColumn.GroupID` and `.SubGroupID` both point at `ReportGroupData`. An audit report can therefore be grouped by the same taxonomy as a form or a report. | Observed |
| [PLT-R-005](../rules/PLT-R-005.md) | Tenant-specific configuration and platform-default configuration live in the same table, discriminated by a boolean/text pair, not partitioned physically | Observed |

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ParentReportGroupDataID` | Parent Group Name | item ID | Global |  | unresolved |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `FirmID` | RGD FirmID | Number | Global |  |  |

### Text & notes (1)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ReportGroupDataName` | Report Group Name | Text | Global | yes |  |

### Audit & record keeping (2)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CreatedDate` | RGD Created Date | Date | Global |  |  |
| `ModifiedDate` | RGD Modified Date | Date | Global |  |  |
