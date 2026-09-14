# VirtualTemplateBudget

*17 fields · module: Budgeting, Cost Tracking & Bidding — OUT OF SCOPE · Postgres: `virtual_template_budget`*

Near-identical structure to VirtualTemplateBudgetOption; the two likely back two different UI pickers (a single-select field vs. an option list) over the same underlying budget template metadata. 16 Global fields under Company Items.

Source: `data-fields/virtual-template-budget.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 17 |
| Fields with a vendor definition | 16 of 17 inventoried |
| Physical tables | `virtual_template_budget` |
| Replication database | `lxr_drp_bbw` |
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

### Lands in virtual_template_budget

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 16 fields carry a vendor definition

**Observed.** 16 of this record's 17 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one source in the corpus that explains fields rather than listing them.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

### Out of scope by decision

**Observed.** Its module is excluded from the rebuild. It stays in the census so impact analysis through the relationship graph is never silently wrong at the boundary, but nothing here is being built.

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ProjectEntityID` |  |  | Entity ID | — |  | `virtual_template_budget.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `TemplateID` | Budget Template RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `virtual_template_budget.TemplateID · TEXT` |  |

### Flags (12)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `IsValidForCapProgram` | Budget Template Valid for Cap Program? | This check box indicates that this record type is valid for a program / capital program. | Boolean | Global |  | `virtual_template_budget.IsValidForCapProgram · TEXT` |  |
| `IsValidForCapProject` | Budget Template Valid for Cap Project? | This check box indicates that this record type is valid for a capital project. | Boolean | Global |  | `virtual_template_budget.IsValidForCapProject · TEXT` |  |
| `IsValidForContract` | Budget Template Valid for RE Contract? | This check box indicates that this record type is valid for a contract. | Boolean | Global |  | `virtual_template_budget.IsValidForContract · TEXT` |  |
| `IsValidForEquipContract` | Budget Template Valid for Equipment Contract? | This check box indicates that this record type is valid for an equipment contract. | Boolean | Global |  | `virtual_template_budget.IsValidForEquipContract · TEXT` |  |
| `IsValidForFacility` | Budget Template Valid for Facility? | This check box indicates that this record type is valid for a facility. | Boolean | Global |  | `virtual_template_budget.IsValidForFacility · TEXT` |  |
| `IsValidForLocation` | Budget Template Valid for Location? | This check box indicates that this record type is valid for a location. | Boolean | Global |  | `virtual_template_budget.IsValidForLocation · TEXT` |  |
| `IsValidForOpenProject` | Budget Template Valid for Open Project? | This check box indicates that this record type is valid for a project / opening project. | Boolean | Global |  | `virtual_template_budget.IsValidForOpenProject · TEXT` |  |
| `IsValidForParcel` | Budget Template Valid for Parcel? | This check box indicates that this record type is valid for a parcel. | Boolean | Global |  | `virtual_template_budget.IsValidForParcel · TEXT` |  |
| `IsValidForPortfolio` | Budget Template Valid for Portfolio? | This check box indicates that this record type is valid for a portfolio. | Boolean | Global |  | `virtual_template_budget.IsValidForPortfolio · TEXT` |  |
| `IsValidForPotentialProject` | Budget Template Valid for Potential Project? | This check box indicates that this record type is valid for a site / potential project. | Boolean | Global |  | `virtual_template_budget.IsValidForPotentialProject · TEXT` |  |
| `IsValidForPrototype` | Budget Template Valid for Prototype? | This check box indicates that this record type is valid for a prototype. | Boolean | Global |  | `virtual_template_budget.IsValidForPrototype · TEXT` |  |
| `LockAllBudgetGroups` | Lock All Budget Groups | Indicates if the budget groups for the template are locked. | Boolean | Global |  | `virtual_template_budget.LockAllBudgetGroups · TEXT` |  |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Description` | Budget Template Description | The description of the budget template. | Text | Global |  | `virtual_template_budget.Description · TEXT` |  |
| `Notes` | Budget Template Notes | Add any notes about the record. | Text | Global |  | `virtual_template_budget.Notes · TEXT` |  |
| `TemplateName` | Budget Template Name | The name of the budget template. | Text | Global |  | `virtual_template_budget.TemplateName · TEXT` |  |
