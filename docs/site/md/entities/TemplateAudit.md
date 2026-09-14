# TemplateAudit

*18 fields · module: Platform & Tenancy · Postgres: `template_audit`*

An audit trail of when a BudgetTemplate/EntityTemplate/FolderTemplate was applied to a new project — applied date and whether folder structure was copied. 17 Global fields under Company Items.

Source: `data-fields/template-audit.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 18 |
| Catalogued fields | 17 (17 global, 0 firm) |
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
| [PLT-R-015](../rules/PLT-R-015.md) | A single audit table serves templating across modules; `EntityTemplate` (this module) is the only one of the four whose home object is filed here | Observed |

## Fields

### Relationships (foreign keys) (5)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BudgetEntityTemplateID` | Budget Template | Template ID | Global |  | [EntityTemplate](EntityTemplate.md) |
| `EntityTemplateID` | Entity Template | Template ID | Global | yes | [EntityTemplate](EntityTemplate.md) |
| `FolderEntityTemplateID` | Folder Template | Template ID | Global |  | [EntityTemplate](EntityTemplate.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |
| `TaskEntityTemplateID` | Task Template | Template ID | Global |  | [EntityTemplate](EntityTemplate.md) |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeFolderActionIDList` | Folder Template Action List | Dropdown (Folder Template Action Code) | Global |  | Folder Template Action Code |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `TemplateAuditID` | Template Audit RecID | Number | Global |  |  |

### Dates & timestamps (3)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AppliedDate` | Applied Date | Time | Global | yes |  |
| `ScheduleEndDate` | Schedule End Date | Date | Global |  |  |
| `ScheduleStartDate` | Schedule Start Date | Date | Global |  |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CopyFolderStructure` | Copy Folder Structure? | Boolean | Global |  |  |

### Text & notes (1)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `EntityTemplateTypeName` | Entity Template Type | Text | Global |  |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Template Audit ClientID | Text | Global | yes |  |
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |
