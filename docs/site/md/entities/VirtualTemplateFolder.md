# VirtualTemplateFolder

*16 fields · module: Documents, Folders & Correspondence · Postgres: `virtual_template_folder`*

Read-only projection of FolderTemplate metadata (name, description, Cap Program/Cap Project applicability), the folder-template counterpart to VirtualTemplateBudget. 15 Global fields under Company Items.

Source: `data-fields/virtual-template-folder.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 16 |
| Fields with a vendor definition | 15 of 16 inventoried |
| Physical tables | `virtual_template_folder` |
| Replication database | `lxr_drp_bbw` |
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

### Lands in virtual_template_folder

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 15 fields carry a vendor definition

**Observed.** 15 of this record's 16 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [DOC-R-007](../rules/DOC-R-007.md) | Input: `FolderTemplate` has one field (`ProjectEntityID`); `VirtualTemplateFolder` carries `TemplateName`, `Description`, `Notes`, and 11 `IsValidFor*` flags. | Observed |
| [DOC-R-008](../rules/DOC-R-008.md) | Input: The 11 `IsValidFor*` booleans on `VirtualTemplateFolder`, matching the enumeration in `../../data-model/project-entity.md` §1.4. Effect: The same attachability-matrix mechanism used for Forms/Issue types applies to folder templates. | Observed |

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ProjectEntityID` |  |  | Entity ID | — |  | `virtual_template_folder.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `TemplateID` | Folder Template RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `virtual_template_folder.TemplateID · TEXT` |  |

### Flags (11)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `IsValidForCapProgram` | Folder Template Valid for Cap Program? | The name of the schedule template. | Boolean | Global |  | `virtual_template_folder.IsValidForCapProgram · TEXT` |  |
| `IsValidForCapProject` | Folder Template Valid for Cap Project? | This check box indicates that this record type is valid for a capital project. | Boolean | Global |  | `virtual_template_folder.IsValidForCapProject · TEXT` |  |
| `IsValidForContract` | Folder Template Valid for RE Contract? | This check box indicates that this record type is valid for a contract. | Boolean | Global |  | `virtual_template_folder.IsValidForContract · TEXT` |  |
| `IsValidForEquipContract` | Folder Template Valid for Equipment Contract? | This check box indicates that this record type is valid for an equipment contract. | Boolean | Global |  | `virtual_template_folder.IsValidForEquipContract · TEXT` |  |
| `IsValidForFacility` | Folder Template Valid for Facility? | This check box indicates that this record type is valid for a facility. | Boolean | Global |  | `virtual_template_folder.IsValidForFacility · TEXT` |  |
| `IsValidForLocation` | Folder Template Valid for Location? | This check box indicates that this record type is valid for a location. | Boolean | Global |  | `virtual_template_folder.IsValidForLocation · TEXT` |  |
| `IsValidForOpenProject` | Folder Template Valid for Open Project? | This check box indicates that this record type is valid for a project / opening project. | Boolean | Global |  | `virtual_template_folder.IsValidForOpenProject · TEXT` |  |
| `IsValidForParcel` | Folder Template Valid for Parcel? | This check box indicates that this record type is valid for a parcel. | Boolean | Global |  | `virtual_template_folder.IsValidForParcel · TEXT` |  |
| `IsValidForPortfolio` | Folder Template Valid for Portfolio? | This check box indicates that this record type is valid for a portfolio. | Boolean | Global |  | `virtual_template_folder.IsValidForPortfolio · TEXT` |  |
| `IsValidForPotentialProject` | Folder Template Valid for Potential Project? | This check box indicates that this record type is valid for a site / potential project. | Boolean | Global |  | `virtual_template_folder.IsValidForPotentialProject · TEXT` |  |
| `IsValidForPrototype` | Folder Template Valid for Prototype? | This check box indicates that this record type is valid for a prototype. | Boolean | Global |  | `virtual_template_folder.IsValidForPrototype · TEXT` |  |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Description` | Folder Template Description | The description of the folder template. | Text | Global |  | `virtual_template_folder.Description · TEXT` |  |
| `Notes` | Folder Template Notes | Add any notes about the record. | Text | Global |  | `virtual_template_folder.Notes · TEXT` |  |
| `TemplateName` | Folder Template Name | The name of the folder template. | Text | Global |  | `virtual_template_folder.TemplateName · TEXT` |  |
