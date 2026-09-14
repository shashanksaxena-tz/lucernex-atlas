# VirtualTemplateFolder

*16 fields · module: Documents, Folders & Correspondence · Postgres: `virtual_template_folder`*

Read-only projection of FolderTemplate metadata (name, description, Cap Program/Cap Project applicability), the folder-template counterpart to VirtualTemplateBudget. 15 Global fields under Company Items.

Source: `data-fields/virtual-template-folder.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 16 |
| Catalogued fields | 15 (15 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 1 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 2 |

## What to know before rebuilding this

### A computed projection, not a table

**Observed.** Virtual records are calculated at read time rather than stored. They have no primary key to join on and never appear in Firm scope — a tenant cannot customise a projection the platform generates. Treat this as the shape of a query result, not as a table to migrate.

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [DOC-R-007](../rules/DOC-R-007.md) | Input: `FolderTemplate` has one field (`ProjectEntityID`); `VirtualTemplateFolder` carries `TemplateName`, `Description`, `Notes`, and 11 `IsValidFor*` flags. | Observed |
| [DOC-R-008](../rules/DOC-R-008.md) | Input: The 11 `IsValidFor*` booleans on `VirtualTemplateFolder`, matching the enumeration in `../../data-model/project-entity.md` §1.4. Effect: The same attachability-matrix mechanism used for Forms/Issue types applies to folder templates. | Observed |

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
| `TemplateID` | Folder Template RecID | Number | Global |  |  |

### Flags (11)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `IsValidForCapProgram` | Folder Template Valid for Cap Program? | Boolean | Global |  |  |
| `IsValidForCapProject` | Folder Template Valid for Cap Project? | Boolean | Global |  |  |
| `IsValidForContract` | Folder Template Valid for RE Contract? | Boolean | Global |  |  |
| `IsValidForEquipContract` | Folder Template Valid for Equipment Contract? | Boolean | Global |  |  |
| `IsValidForFacility` | Folder Template Valid for Facility? | Boolean | Global |  |  |
| `IsValidForLocation` | Folder Template Valid for Location? | Boolean | Global |  |  |
| `IsValidForOpenProject` | Folder Template Valid for Open Project? | Boolean | Global |  |  |
| `IsValidForParcel` | Folder Template Valid for Parcel? | Boolean | Global |  |  |
| `IsValidForPortfolio` | Folder Template Valid for Portfolio? | Boolean | Global |  |  |
| `IsValidForPotentialProject` | Folder Template Valid for Potential Project? | Boolean | Global |  |  |
| `IsValidForPrototype` | Folder Template Valid for Prototype? | Boolean | Global |  |  |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Description` | Folder Template Description | Text | Global |  |  |
| `Notes` | Folder Template Notes | Text | Global |  |  |
| `TemplateName` | Folder Template Name | Text | Global |  |  |
