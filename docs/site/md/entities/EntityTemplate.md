# EntityTemplate

*1 fields · module: Platform & Tenancy · Postgres: `entity_template`*

A single-field stub representing a reusable entity-setup template, referenced by TemplateAudit.

Source: `data-fields/small-miscellaneous-entities.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 1 |
| Catalogued fields | 1 (1 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 16 keys from 4 record types |
| Points at | 1 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 3 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [PLT-R-014](../rules/PLT-R-014.md) | These are join/marker tables or the export is truncating them; either way, do not model them as one-column tables in the rebuild without a targeted schema-browser capture | Derived |
| [PLT-R-015](../rules/PLT-R-015.md) | A single audit table serves templating across modules; `EntityTemplate` (this module) is the only one of the four whose home object is filed here | Observed |
| [DOC-R-009](../rules/DOC-R-009.md) | Input: `FolderTemplateAudit.EntityTemplateID`, `.FolderEntityTemplateID`, `.BudgetEntityTemplateID`, `.TaskEntityTemplateID` — four `Template ID`-typed columns on one row, plus `CopyFolderStructure` (boolean) and `AppliedDate`. Effect: A si | Observed |

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

## What points here (16 keys)

| Record type | Via column |
|---|---|
| [BudgetTemplateAudit](BudgetTemplateAudit.md) | `BudgetEntityTemplateID`, `EntityTemplateID`, `FolderEntityTemplateID`, `TaskEntityTemplateID` |
| [FolderTemplateAudit](FolderTemplateAudit.md) | `BudgetEntityTemplateID`, `EntityTemplateID`, `FolderEntityTemplateID`, `TaskEntityTemplateID` |
| [TaskTemplateAudit](TaskTemplateAudit.md) | `BudgetEntityTemplateID`, `EntityTemplateID`, `FolderEntityTemplateID`, `TaskEntityTemplateID` |
| [TemplateAudit](TemplateAudit.md) | `BudgetEntityTemplateID`, `EntityTemplateID`, `FolderEntityTemplateID`, `TaskEntityTemplateID` |
