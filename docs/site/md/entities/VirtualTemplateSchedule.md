# VirtualTemplateSchedule

*16 fields · module: Capital Projects & Scheduling · Postgres: `virtual_template_schedule`*

Read-only projection of a schedule-template's metadata, completing the Virtual*Template trio alongside VirtualTemplateBudget and VirtualTemplateFolder. 15 Global fields under Company Items.

Source: `data-fields/virtual-template-schedule.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 16 |
| Catalogued fields | 15 (15 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 1 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 1 |

## What to know before rebuilding this

### A computed projection, not a table

**Observed.** Virtual records are calculated at read time rather than stored. They have no primary key to join on and never appear in Firm scope — a tenant cannot customise a projection the platform generates. Treat this as the shape of a query result, not as a table to migrate.

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [PRJ-R-003](../rules/PRJ-R-003.md) | A tenant defines a new Form/Issue type · `CodeIssueType`, `TableType` 2035 · Carries the same 11 `IsValidFor*` entity-attachability flags as `VirtualTemplateSchedule` in this module and every template object in every other module. · Observe | Observed |

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `TemplateID` | Schedule Template RecID | Number | Global |  |  |

### Flags (11)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `IsValidForCapProgram` | Schedule Template Valid for Cap Program? | Boolean | Global |  |  |
| `IsValidForCapProject` | Schedule Template Valid for Cap Project? | Boolean | Global |  |  |
| `IsValidForContract` | Schedule Template Valid for RE Contract? | Boolean | Global |  |  |
| `IsValidForEquipContract` | Schedule Template Valid for Equipment Contract? | Boolean | Global |  |  |
| `IsValidForFacility` | Schedule Template Valid for Facility? | Boolean | Global |  |  |
| `IsValidForLocation` | Schedule Template Valid for Location? | Boolean | Global |  |  |
| `IsValidForOpenProject` | Schedule Template Valid for Open Project? | Boolean | Global |  |  |
| `IsValidForParcel` | Schedule Template Valid for Parcel? | Boolean | Global |  |  |
| `IsValidForPortfolio` | Schedule Template Valid for Portfolio? | Boolean | Global |  |  |
| `IsValidForPotentialProject` | Schedule Template Valid for Potential Project? | Boolean | Global |  |  |
| `IsValidForPrototype` | Schedule Template Valid for Prototype? | Boolean | Global |  |  |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Description` | Schedule Template Description | Text | Global |  |  |
| `Notes` | Schedule Template Notes | Text | Global |  |  |
| `TemplateName` | Schedule Template Name | Text | Global |  |  |
