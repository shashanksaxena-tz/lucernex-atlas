# FolderTemplateAudit

*18 fields · module: Documents, Folders & Correspondence · Postgres: `folder_template_audit`*

Not covered by the Data Fields catalogue: this record type appears in the 223-object census but has no row in the catalogue of 6,158 configurable fields, so nothing in the corpus explains it in the vendor's own words. What is known is structural — 18 declared fields, filed under Documents, Folders & Correspondence, 0 foreign keys pointing at it.

Source: `_lucernex_objects_summary.txt`

## At a glance

|  | Value |
|---|---|
| Fields declared | 18 |
| Catalogued fields | not in the catalogue |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 7 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 1 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [DOC-R-009](../rules/DOC-R-009.md) | Input: `FolderTemplateAudit.EntityTemplateID`, `.FolderEntityTemplateID`, `.BudgetEntityTemplateID`, `.TaskEntityTemplateID` — four `Template ID`-typed columns on one row, plus `CopyFolderStructure` (boolean) and `AppliedDate`. Effect: A si | Observed |

## Fields

### Relationships (foreign keys) (5)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BudgetEntityTemplateID` |  | Template ID | — |  | [EntityTemplate](EntityTemplate.md) |
| `EntityTemplateID` |  | Template ID | — |  | [EntityTemplate](EntityTemplate.md) |
| `FolderEntityTemplateID` |  | Template ID | — |  | [EntityTemplate](EntityTemplate.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |
| `TaskEntityTemplateID` |  | Template ID | — |  | [EntityTemplate](EntityTemplate.md) |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeFolderActionIDList` |  | Dropdown (Folder Template Action Code) | — |  | Folder Template Action Code |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `TemplateAuditID` |  | Number | — |  |  |

### Dates & timestamps (3)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AppliedDate` |  | Time | — |  |  |
| `ScheduleEndDate` |  | Date | — |  |  |
| `ScheduleStartDate` |  | Date | — |  |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CopyFolderStructure` |  | Boolean | — |  |  |

### Text & notes (1)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `EntityTemplateTypeName` |  | Text | — |  |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` |  | Text | — |  |  |
| `CreatedByID` |  | Member ID | — |  | [Member](Member.md) |
| `CreatedDate` |  | Time | — |  |  |
| `ModifiedByID` |  | Member ID | — |  | [Member](Member.md) |
| `ModifiedDate` |  | Time | — |  |  |
| `RevNumber` |  | Number | — |  |  |
