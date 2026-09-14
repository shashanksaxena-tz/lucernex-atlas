# BudgetTemplate

*1 fields · module: Budgeting, Cost Tracking & Bidding — OUT OF SCOPE · Postgres: `budget_template`*

Not covered by the Data Fields catalogue: this record type appears in the 223-object census but has no row in the catalogue of 6,158 configurable fields, so nothing in the corpus explains it in the vendor's own words. What is known is structural — 1 declared fields, filed under Budgeting, Cost Tracking & Bidding — OUT OF SCOPE, 14 foreign keys pointing at it.

Source: `_lucernex_objects_summary.txt`

## At a glance

|  | Value |
|---|---|
| Fields declared | 1 |
| Catalogued fields | not in the catalogue |
| Physical tables | 1 |
| Referenced by | 14 keys from 14 record types |
| Points at | 1 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

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

## What points here (14 keys)

| Record type | Via column |
|---|---|
| [BudgetColumn](BudgetColumn.md) | `BudgetTemplateID` |
| [BudgetLineGroup](BudgetLineGroup.md) | `BudgetTemplateID` |
| [BudgetLineItem](BudgetLineItem.md) | `BudgetTemplateID` |
| [BudgetLineLeaf](BudgetLineLeaf.md) | `BudgetTemplateID` |
| [BudgetOptionTemplate](BudgetOptionTemplate.md) | `BudgetTemplateID` |
| [Contract](Contract.md) | `BudgetTemplateID` |
| [Facility](Facility.md) | `BudgetTemplateID` |
| [Location](Location.md) | `BudgetTemplateID` |
| [Parcel](Parcel.md) | `BudgetTemplateID` |
| [PotentialProject](PotentialProject.md) | `BudgetTemplateID` |
| [Program](Program.md) | `BudgetTemplateID` |
| [Project](Project.md) | `BudgetTemplateID` |
| [ProjectEntity](ProjectEntity.md) | `BudgetTemplateID` |
| [Prototype](Prototype.md) | `BudgetTemplateID` |
