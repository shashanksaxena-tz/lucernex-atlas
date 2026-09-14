# CodeProblem

*4 fields · module: Capital Projects & Scheduling · Postgres: `code_problem`*

Master maintenance-problem-type reference record with a remedy note, linked to an asset category.

Source: `data-fields/code-reference-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 4 |
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

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [PRJ-R-014](../rules/PRJ-R-014.md) | `CodeProblem` or `CodeResponsibleParty` values are needed · (no confirmed attachment point) · Neither table shows an inbound or outbound edge in the 972-edge graph. May be referenced only via `Dropdown`-typed columns this corpus's edge-extr | Observed |

## Fields

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Inactive` |  | Boolean | — |  |  |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ActualLongName` |  | Text | — |  |  |
| `RemedyNote` | Problem Remedy Note | Text | Global |  |  |
| `ShortName` |  | Text | — |  |  |
