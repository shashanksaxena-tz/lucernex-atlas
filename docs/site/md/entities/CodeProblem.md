# CodeProblem

*4 fields · module: Capital Projects & Scheduling · Postgres: `code_problem`*

Master maintenance-problem-type reference record with a remedy note, linked to an asset category.

Source: `data-fields/code-reference-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 4 |
| Fields with a vendor definition | 1 of 4 inventoried |
| Physical tables | `code_problem` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 2 (2 global, 0 firm) |
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

### Lands in code_problem

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 1 field carry a vendor definition

**Observed.** 1 of this record's 4 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 0 of this record's fields required; the Data Fields catalogue marks 1; 0 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [PRJ-R-014](../rules/PRJ-R-014.md) | `CodeProblem` or `CodeResponsibleParty` values are needed · (no confirmed attachment point) · Neither table shows an inbound or outbound edge in the 972-edge graph. May be referenced only via `Dropdown`-typed columns this corpus's edge-extr | Observed |

## Fields

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Inactive` |  |  | Boolean | — |  | `code_problem.Inactive · TEXT` |  |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActualLongName` | Description |  | Text | — |  | `code_problem.ActualLongName · TEXT` |  |
| `RemedyNote` | Problem Remedy Note | Enter any notes about the remedy to the problem. | Text | Global |  | `code_problem.RemedyNote · TEXT` |  |
| `ShortName` | Name |  | Text | — |  | `code_problem.ShortName · TEXT` |  |
