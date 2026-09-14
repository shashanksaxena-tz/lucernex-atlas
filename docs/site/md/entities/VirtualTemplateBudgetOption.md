# VirtualTemplateBudgetOption

*17 fields · module: Budgeting, Cost Tracking & Bidding — OUT OF SCOPE · Postgres: `virtual_template_budget_option`*

Read-only projection of a budget template's metadata (name, description, notes, and Cap Program/Cap Project applicability flags) surfaced for selection during project setup, distinct from the persisted BudgetLineItem/BudgetColumn records it configures. 16 Global fields under Company Items.

Source: `data-fields/virtual-template-budget-option.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 17 |
| Catalogued fields | 16 (16 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 1 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### A computed projection, not a table

**Observed.** Virtual records are calculated at read time rather than stored. They have no primary key to join on and never appear in Firm scope — a tenant cannot customise a projection the platform generates. Treat this as the shape of a query result, not as a table to migrate.

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Out of scope by decision

**Observed.** Its module is excluded from the rebuild. It stays in the census so impact analysis through the relationship graph is never silently wrong at the boundary, but nothing here is being built.

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
| `TemplateID` | Budget Template RecID | Number | Global |  |  |

### Flags (12)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `IsValidForCapProgram` | Budget Template Valid for Cap Program? | Boolean | Global |  |  |
| `IsValidForCapProject` | Budget Template Valid for Cap Project? | Boolean | Global |  |  |
| `IsValidForContract` | Budget Template Valid for RE Contract? | Boolean | Global |  |  |
| `IsValidForEquipContract` | Budget Template Valid for Equipment Contract? | Boolean | Global |  |  |
| `IsValidForFacility` | Budget Template Valid for Facility? | Boolean | Global |  |  |
| `IsValidForLocation` | Budget Template Valid for Location? | Boolean | Global |  |  |
| `IsValidForOpenProject` | Budget Template Valid for Open Project? | Boolean | Global |  |  |
| `IsValidForParcel` | Budget Template Valid for Parcel? | Boolean | Global |  |  |
| `IsValidForPortfolio` | Budget Template Valid for Portfolio? | Boolean | Global |  |  |
| `IsValidForPotentialProject` | Budget Template Valid for Potential Project? | Boolean | Global |  |  |
| `IsValidForPrototype` | Budget Template Valid for Prototype? | Boolean | Global |  |  |
| `LockAllBudgetGroups` | Lock All Budget Groups | Boolean | Global |  |  |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Description` | Budget Template Description | Text | Global |  |  |
| `Notes` | Budget Template Notes | Text | Global |  |  |
| `TemplateName` | Budget Template Name | Text | Global |  |  |
