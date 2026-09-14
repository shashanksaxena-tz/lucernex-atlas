# CodeResponsibleParty

*4 fields · module: Capital Projects & Scheduling · Postgres: `code_responsible_party`*

A single-field master value for the responsible-party code list used on Responsibility records.

Source: `data-fields/code-reference-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 4 |
| Fields with a vendor definition | 0 of 4 inventoried |
| Physical tables | `code_responsible_party` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 1 (1 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 0 other records |
| Tenancy position | firm_global |
| Rules that name it | 1 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### No typed relationships either way

**Derived.** Nothing holds a typed foreign key into this record and it declares none out. Either it is joined by a soft reference the census cannot see, or it is genuinely standalone — worth settling before anything is built on it.

### Lands in code_responsible_party

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [PRJ-R-014](../rules/PRJ-R-014.md) | `CodeProblem` or `CodeResponsibleParty` values are needed · (no confirmed attachment point) · Neither table shows an inbound or outbound edge in the 972-edge graph. May be referenced only via `Dropdown`-typed columns this corpus's edge-extr | Observed |

## Fields

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeResponsiblePartySystemID` | Responsible Party Value |  | Dropdown (Responsible Party System Code) | Global |  | `code_responsible_party.CodeResponsiblePartySystemID · TEXT` | Responsible Party System Code |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Inactive` |  |  | Boolean | — |  | `code_responsible_party.Inactive · TEXT` |  |

### Text & notes (2)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActualLongName` | Description |  | Text | — |  | `code_responsible_party.ActualLongName · TEXT` |  |
| `ShortName` | Name |  | Text | — |  | `code_responsible_party.ShortName · TEXT` |  |
