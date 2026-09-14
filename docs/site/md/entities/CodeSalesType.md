# CodeSalesType

*3 fields · module: Variable Rent (Percentage / Use-Based) & Sales · Postgres: `code_sales_type`*

Master reference record for sales-type classification, with a flag to omit a type from sales-group totals.

Source: `data-fields/code-reference-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 3 |
| Fields with a vendor definition | 0 of 3 inventoried |
| Physical tables | `code_sales_type` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 2 (2 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 0 other records |
| Tenancy position | firm_global |
| Rules that name it | 0 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### No typed relationships either way

**Derived.** Nothing holds a typed foreign key into this record and it declares none out. Either it is joined by a soft reference the census cannot see, or it is genuinely standalone — worth settling before anything is built on it.

### Lands in code_sales_type

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### Required: the two captures disagree

**Observed.** The field inventory marks 0 of this record's fields required; the Data Fields catalogue marks 2; 0 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

## Fields

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Inactive` |  |  | Boolean | — |  | `code_sales_type.Inactive · TEXT` |  |

### Text & notes (2)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActualLongName` | Description |  | Text | — |  | `code_sales_type.ActualLongName · TEXT` |  |
| `ShortName` | Name |  | Text | — |  | `code_sales_type.ShortName · TEXT` |  |
