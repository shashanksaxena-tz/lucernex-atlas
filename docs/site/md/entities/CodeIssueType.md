# CodeIssueType

*19 fields · module: Capital Projects & Scheduling · Postgres: `code_issue_type`*

Not covered by the Data Fields catalogue: this record type appears in the 223-object census but has no row in the catalogue of 6,158 configurable fields, so nothing in the corpus explains it in the vendor's own words. What is known is structural — 19 declared fields, filed under Capital Projects & Scheduling, 0 foreign keys pointing at it.

Source: `_lucernex_objects_summary.txt`

## At a glance

|  | Value |
|---|---|
| Fields declared | 19 |
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

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AllowReply` |  | Boolean | — |  |  |
| `AutoClose` |  | Boolean | — |  |  |
| `Inactive` |  | Boolean | — |  |  |
| `IsSequencePerFirm` |  | Boolean | — |  |  |
| `IsValidForCapProgram` |  | Boolean | — |  |  |
| `IsValidForCapProject` |  | Boolean | — |  |  |
| `IsValidForContract` |  | Boolean | — |  |  |
| `IsValidForEquipContract` |  | Boolean | — |  |  |
| `IsValidForFacility` |  | Boolean | — |  |  |
| `IsValidForLocation` |  | Boolean | — |  |  |
| `IsValidForOpenProject` |  | Boolean | — |  |  |
| `IsValidForParcel` |  | Boolean | — |  |  |
| `IsValidForPortfolio` |  | Boolean | — |  |  |
| `IsValidForPotentialProject` |  | Boolean | — |  |  |
| `IsValidForPrototype` |  | Boolean | — |  |  |
| `IsWorkFlow` |  | Boolean | — |  |  |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ActualLongName` |  | Text | — |  |  |
| `SequencePrefix` |  | Text | — |  |  |
| `ShortName` |  | Text | — |  |  |
