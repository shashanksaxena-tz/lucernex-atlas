# RecalcOverrideNotes

*7 fields · module: Lease Accounting & Payments · Postgres: `recalc_override_notes`*

A free-text note explaining why a financial recalculation was manually overridden — an audit-style justification field.

Source: `data-fields/small-miscellaneous-entities.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 7 |
| Fields with a vendor definition | 0 of 7 inventoried |
| Physical tables | `recalc_override_notes` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 6 (6 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 1 keys from 1 record types |
| Points at | 4 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 1 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in recalc_override_notes

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 2 fields marked required

**Observed.** The inventory marks 2 of this record's fields Required. Across the whole inventory that is 606 fields, which independently corroborates the 603 the corpus had derived from the Data Fields catalogue — two sources, arrived at separately, agreeing to within three.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [ACC-R-024](../rules/ACC-R-024.md) | a `RecalcOverrideNotes` row linked by `SLSummaryID`; the id appended to `SLSummary.RecalcOverrideNotesIDList` | Derived |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ProjectEntityID` |  |  | Entity ID | — |  | `recalc_override_notes.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `SLSummaryID` | Straight Line Summary |  | Straight-Line Schedule ID | Global | yes | `recalc_override_notes.SLSummaryID · TEXT` | [SLSummary](SLSummary.md) |

### Text & notes (1)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Notes` | Override Note |  | Text | Global | yes | `recalc_override_notes.Notes · TEXT` |  |

### Audit & record keeping (4)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CreatedByID` | Created By |  | Member ID | Global |  | `recalc_override_notes.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Date of entry |  | Time | Global |  | `recalc_override_notes.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By |  | Member ID | Global |  | `recalc_override_notes.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date |  | Time | Global |  | `recalc_override_notes.ModifiedDate · TEXT` |  |

## What points here (1 keys)

| Record type | Via column |
|---|---|
| [SLSummary](SLSummary.md) | `RecalcOverrideNotesIDList` |
