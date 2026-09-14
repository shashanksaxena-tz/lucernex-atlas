# ReportGroupData

*5 fields · module: Configuration, Layouts, Forms & Reporting · Postgres: `report_group_data`*

Platform metadata for a top-level or subgroup node in this very Data Fields hierarchy — parent group name and firm scoping.

Source: `data-fields/small-miscellaneous-entities.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 5 |
| Fields with a vendor definition | 5 of 5 inventoried |
| Physical tables | `report_group_data` |
| Replication database | `lxr_drp_bbw` |
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

### Lands in report_group_data

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 5 fields carry a vendor definition

**Observed.** 5 of this record's 5 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: the captures agree

**Observed.** Over the 5 fields both the Data Fields catalogue and the field inventory contain, the two agree on every one. 1 are marked required.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [LAY-R-171](../rules/LAY-R-171.md) | The list is a `ReportGroupData` node; its fields are `ReportGroupAvailableField` leaves; | Observed |
| [RPT-R-041](../rules/RPT-R-041.md) | Audit entries are filed under the field registry's group tree — `AuditColumn.GroupID` and `.SubGroupID` both point at `ReportGroupData`. An audit report can therefore be grouped by the same taxonomy as a form or a report. | Observed |
| [PLT-R-005](../rules/PLT-R-005.md) | Tenant-specific configuration and platform-default configuration live in the same table, discriminated by a boolean/text pair, not partitioned physically | Observed |

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ParentReportGroupDataID` | Parent Group Name | The ID of the Parent Group of the field. | item ID | Global |  | `report_group_data.ParentReportGroupDataID · TEXT` | unresolved |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `FirmID` | RGD FirmID | The record's Firm ID. | Number | Global |  | `report_group_data.FirmID · TEXT` |  |

### Text & notes (1)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ReportGroupDataName` | Report Group Name | The ID of the Report Group associated with the field. | Text | Global | yes | `report_group_data.ReportGroupDataName · TEXT` |  |

### Audit & record keeping (2)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CreatedDate` | RGD Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Date | Global |  | `report_group_data.CreatedDate · TEXT` |  |
| `ModifiedDate` | RGD Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Date | Global |  | `report_group_data.ModifiedDate · TEXT` |  |
