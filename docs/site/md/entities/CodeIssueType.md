# CodeIssueType

*19 fields · module: Capital Projects & Scheduling · Postgres: `code_issue_type`*

Not covered by the Data Fields catalogue: this record type appears in the 223-object census but has no row in the catalogue of 6,158 configurable fields, so no document describes the record as a whole. What is known is structural — 19 declared fields, filed under Capital Projects & Scheduling, 0 foreign keys pointing at it.

Source: `_lucernex_objects_summary.txt`

## At a glance

|  | Value |
|---|---|
| Fields declared | 19 |
| Fields with a vendor definition | 0 of 19 inventoried |
| Physical tables | `code_issue_type` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | not in the catalogue |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 0 other records |
| Tenancy position | firm_global |
| Rules that name it | 4 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### No typed relationships either way

**Derived.** Nothing holds a typed foreign key into this record and it declares none out. Either it is joined by a soft reference the census cannot see, or it is genuinely standalone — worth settling before anything is built on it.

### Lands in code_issue_type

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [WF-R-006](../rules/WF-R-006.md) | A form type is marked as workflow-driving · `CodeIssueType.IsWorkFlow` · true · Forms of this type participate in the workflow engine rather than standing alone · Inferred — no vendor help text for this column | Inferred |
| [LAY-R-160](../rules/LAY-R-160.md) | A Form Type is a `CodeIssueType` row. Lx's schema names the dropdown that selects one `Dropdown (Form Type)`. | Observed |
| [LAY-R-162](../rules/LAY-R-162.md) | A Form Type declares which entity types it may be raised against, via eleven `IsValidFor<Entity>` flags (Portfolio, CapProgram, CapProject, OpenProject, PotentialProject, Prototype, Parcel, Facility, Location, Contract, EquipContract). · Ob | Observed |
| [PRJ-R-003](../rules/PRJ-R-003.md) | A tenant defines a new Form/Issue type · `CodeIssueType`, `TableType` 2035 · Carries the same 11 `IsValidFor*` entity-attachability flags as `VirtualTemplateSchedule` in this module and every template object in every other module. · Observe | Observed |

## Fields

### Flags (16)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AllowReply` |  |  | Boolean | — |  | `code_issue_type.AllowReply · TEXT` |  |
| `AutoClose` |  |  | Boolean | — |  | `code_issue_type.AutoClose · TEXT` |  |
| `Inactive` |  |  | Boolean | — |  | `code_issue_type.Inactive · TEXT` |  |
| `IsSequencePerFirm` |  |  | Boolean | — |  | `code_issue_type.IsSequencePerFirm · TEXT` |  |
| `IsValidForCapProgram` |  |  | Boolean | — |  | `code_issue_type.IsValidForCapProgram · TEXT` |  |
| `IsValidForCapProject` |  |  | Boolean | — |  | `code_issue_type.IsValidForCapProject · TEXT` |  |
| `IsValidForContract` |  |  | Boolean | — |  | `code_issue_type.IsValidForContract · TEXT` |  |
| `IsValidForEquipContract` |  |  | Boolean | — |  | `code_issue_type.IsValidForEquipContract · TEXT` |  |
| `IsValidForFacility` |  |  | Boolean | — |  | `code_issue_type.IsValidForFacility · TEXT` |  |
| `IsValidForLocation` |  |  | Boolean | — |  | `code_issue_type.IsValidForLocation · TEXT` |  |
| `IsValidForOpenProject` |  |  | Boolean | — |  | `code_issue_type.IsValidForOpenProject · TEXT` |  |
| `IsValidForParcel` |  |  | Boolean | — |  | `code_issue_type.IsValidForParcel · TEXT` |  |
| `IsValidForPortfolio` |  |  | Boolean | — |  | `code_issue_type.IsValidForPortfolio · TEXT` |  |
| `IsValidForPotentialProject` |  |  | Boolean | — |  | `code_issue_type.IsValidForPotentialProject · TEXT` |  |
| `IsValidForPrototype` |  |  | Boolean | — |  | `code_issue_type.IsValidForPrototype · TEXT` |  |
| `IsWorkFlow` |  |  | Boolean | — |  | `code_issue_type.IsWorkFlow · TEXT` |  |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActualLongName` | Description |  | Text | — |  | `code_issue_type.ActualLongName · TEXT` |  |
| `SequencePrefix` |  |  | Text | — |  | `code_issue_type.SequencePrefix · TEXT` |  |
| `ShortName` | Name |  | Text | — |  | `code_issue_type.ShortName · TEXT` |  |
