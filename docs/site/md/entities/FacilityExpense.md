# FacilityExpense

*22 fields · module: Facilities, Locations & Sites · Postgres: `facility_expense`*

A non-recovered operating expense tracked directly against a Facility rather than through a Contract's ExpenseRecovery — actual vs. budgeted amount and description. 21 Global fields under Facility.

Source: `data-fields/facility-expense.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 22 |
| Fields with a vendor definition | 21 of 22 inventoried |
| Physical tables | `facility_expense` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 21 (21 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 6 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in facility_expense

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 21 fields carry a vendor definition

**Observed.** 21 of this record's 22 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: the captures agree

**Observed.** Over the 21 fields both the Data Fields catalogue and the field inventory contain, the two agree on every one. 2 are marked required.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Fields

### Relationships (foreign keys) (4)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AssociatedDocumentID` | Associated Document | The ID of a document associated with this record. | Document ID | Global |  | `facility_expense.AssociatedDocumentID · TEXT` | [Document](Document.md) |
| `FacilityID` | Facility | Select the facility that your record will be associated with from this field. | Facility ID | Global | yes | `facility_expense.FacilityID · TEXT` | [Facility](Facility.md) |
| `FolderID` | Folder | Select the folder where the associated document is located from this field. | Folder ID | Global |  | `facility_expense.FolderID · TEXT` | [Folder](Folder.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `facility_expense.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeExpenseGroupID` | Expense Group | The Expense Group field allows you to associate your record with a pre-configured expense group. Expense groups are used to categorize expense types. | Dropdown (Expense Group Code) | Global |  | `facility_expense.CodeExpenseGroupID · TEXT` | Expense Group Code |
| `CodeExpenseTypeID` | Expense Type | The Expense Type field allows you to associate your record with a pre-configured expense type. Expense Types are used to associate records with lease accounting schedules, AP export numbers, expense accrual accounts, percentage rent accrual accounts, and real estate tax accounts. | Dropdown (Expense Type Code) | Global |  | `facility_expense.CodeExpenseTypeID · TEXT` | Expense Type Code |

### Money (4)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActualAmount` | Actual Amount | Enter the actual amount of the expense in this field. | Currency | Global |  | `facility_expense.ActualAmount · TEXT` |  |
| `BudgetedAmount` | Budgeted Amount | Enter the budgeted amount of the expense in this field. | Currency | Global |  | `facility_expense.BudgetedAmount · TEXT` |  |
| `PlannedAmount` | Planned Amount | Enter the planned amount of the expense in this field. | Currency | Global |  | `facility_expense.PlannedAmount · TEXT` |  |
| `RevisedAmount` | Revised Amount | Enter the revised amount of the expense in this field. | Currency | Global |  | `facility_expense.RevisedAmount · TEXT` |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `FacilityExpenseID` | Facility Expense RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `facility_expense.FacilityExpenseID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (1)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `EffectiveDate` | Effective Date | Enter the effective date of the expense in this field. | Date | Global |  | `facility_expense.EffectiveDate · TEXT` |  |

### Text & notes (4)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BaseName` | File Name | This field displays the file name of the file attached to the record. | Text | Global |  | `facility_expense.BaseName · TEXT` |  |
| `Description` |  | Write a description of the record. | Text | Global |  | `facility_expense.Description · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `facility_expense.Notes · TEXT` |  |
| `ReferenceID` | Reference ID | The reference ID for the facility expense. | Text | Global |  | `facility_expense.ReferenceID · TEXT` |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Facility Expense ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `facility_expense.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `facility_expense.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `facility_expense.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `facility_expense.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `facility_expense.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | `facility_expense.RevNumber · TEXT` |  |
