# EntityTemplate

*1 fields · module: Platform & Tenancy · Postgres: `entity_template`*

A single-field stub representing a reusable entity-setup template, referenced by TemplateAudit.

Source: `data-fields/small-miscellaneous-entities.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 1 |
| Fields with a vendor definition | 0 of 1 inventoried |
| Physical tables | `entity_template` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 1 (1 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 16 keys from 4 record types |
| Points at | 1 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 3 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in entity_template

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [PLT-R-014](../rules/PLT-R-014.md) | These are join/marker tables or the export is truncating them; either way, do not model them as one-column tables in the rebuild without a targeted schema-browser capture | Derived |
| [PLT-R-015](../rules/PLT-R-015.md) | A single audit table serves templating across modules; `EntityTemplate` (this module) is the only one of the four whose home object is filed here | Observed |
| [DOC-R-009](../rules/DOC-R-009.md) | Input: `FolderTemplateAudit.EntityTemplateID`, `.FolderEntityTemplateID`, `.BudgetEntityTemplateID`, `.TaskEntityTemplateID` — four `Template ID`-typed columns on one row, plus `CopyFolderStructure` (boolean) and `AppliedDate`. Effect: A si | Observed |

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ProjectEntityID` |  |  | Entity ID | — |  | `entity_template.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

## What points here (16 keys)

| Record type | Via column |
|---|---|
| [BudgetTemplateAudit](BudgetTemplateAudit.md) | `BudgetEntityTemplateID`, `EntityTemplateID`, `FolderEntityTemplateID`, `TaskEntityTemplateID` |
| [FolderTemplateAudit](FolderTemplateAudit.md) | `BudgetEntityTemplateID`, `EntityTemplateID`, `FolderEntityTemplateID`, `TaskEntityTemplateID` |
| [TaskTemplateAudit](TaskTemplateAudit.md) | `BudgetEntityTemplateID`, `EntityTemplateID`, `FolderEntityTemplateID`, `TaskEntityTemplateID` |
| [TemplateAudit](TemplateAudit.md) | `BudgetEntityTemplateID`, `EntityTemplateID`, `FolderEntityTemplateID`, `TaskEntityTemplateID` |
