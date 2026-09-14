# BudgetTemplate

*1 fields · module: Budgeting, Cost Tracking & Bidding — OUT OF SCOPE · Postgres: `budget_template`*

Not covered by the Data Fields catalogue: this record type appears in the 223-object census but has no row in the catalogue of 6,158 configurable fields, so no document describes the record as a whole. What is known is structural — 1 declared fields, filed under Budgeting, Cost Tracking & Bidding — OUT OF SCOPE, 14 foreign keys pointing at it.

Source: `_lucernex_objects_summary.txt`

## At a glance

|  | Value |
|---|---|
| Fields declared | 1 |
| Fields with a vendor definition | 0 of 1 inventoried |
| Physical tables | `budget_template` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | not in the catalogue |
| Physical tables | 1 |
| Referenced by | 14 keys from 14 record types |
| Points at | 1 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in budget_template

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

### Out of scope by decision

**Observed.** Its module is excluded from the rebuild. It stays in the census so impact analysis through the relationship graph is never silently wrong at the boundary, but nothing here is being built.

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ProjectEntityID` |  |  | Entity ID | — |  | `budget_template.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

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
