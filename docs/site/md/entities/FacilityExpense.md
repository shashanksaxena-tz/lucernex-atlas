# FacilityExpense

*22 fields · module: Facilities, Locations & Sites · Postgres: `facility_expense`*

A non-recovered operating expense tracked directly against a Facility rather than through a Contract's ExpenseRecovery — actual vs. budgeted amount and description. 21 Global fields under Facility.

Source: `data-fields/facility-expense.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 22 |
| Catalogued fields | 21 (21 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 6 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Fields

### Relationships (foreign keys) (4)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AssociatedDocumentID` | Associated Document | Document ID | Global |  | [Document](Document.md) |
| `FacilityID` | Facility | Facility ID | Global | yes | [Facility](Facility.md) |
| `FolderID` | Folder | Folder ID | Global |  | [Folder](Folder.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeExpenseGroupID` | Expense Group | Dropdown (Expense Group Code) | Global |  | Expense Group Code |
| `CodeExpenseTypeID` | Expense Type | Dropdown (Expense Type Code) | Global |  | Expense Type Code |

### Money (4)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ActualAmount` | Actual Amount | Currency | Global |  |  |
| `BudgetedAmount` | Budgeted Amount | Currency | Global |  |  |
| `PlannedAmount` | Planned Amount | Currency | Global |  |  |
| `RevisedAmount` | Revised Amount | Currency | Global |  |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `FacilityExpenseID` | Facility Expense RecID | Number | Global |  |  |

### Dates & timestamps (1)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `EffectiveDate` | Effective Date | Date | Global |  |  |

### Text & notes (4)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BaseName` | File Name | Text | Global |  |  |
| `Description` |  | Text | Global |  |  |
| `Notes` |  | Text | Global |  |  |
| `ReferenceID` | Reference ID | Text | Global |  |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Facility Expense ClientID | Text | Global | yes |  |
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |
