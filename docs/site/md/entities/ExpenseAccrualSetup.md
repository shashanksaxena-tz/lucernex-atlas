# ExpenseAccrualSetup

*31 fields · module: Lease Accounting & Payments · Postgres: `expense_accrual_setup`*

The configuration for accruing an expense ahead of its billing (common for property tax and insurance accrued monthly against an annual bill) — accrual message, area-unit basis, and begin period. 30 Global fields under Contract.

Source: `data-fields/expense-accrual-setup.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 31 |
| Fields with a vendor definition | 30 of 31 inventoried |
| Physical tables | `expense_accrual_setup` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 30 (30 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 7 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 3 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in expense_accrual_setup

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 30 fields carry a vendor definition

**Observed.** 30 of this record's 31 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: 1 disagree of 30 comparable

**Observed.** Over the 30 fields both captures contain, they agree on 29. The exceptions are ContractID. Estate-wide there are 43 such fields and every one runs the same way — catalogue-required, inventory-not — and they are 34 ContractID, 8 ProjectEntityID and 1 ShortName: the owner foreign key. Parenthood is enforced by the application, not by the database.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [ACC-R-052](../rules/ACC-R-052.md) | entering any one of annual amount / period amount / accrual rate auto-populates the other two plus `FirstPaymentAmount` and `LastPaymentAmount`. Rate-based entry requires `RentableArea` to be populated — "If you are not going to use rentabl | Observed |
| [CON-R-120](../rules/CON-R-120.md) | An accrual clause is configured: ExpenseAccrualSetup accrues an expense ahead of its billing, using CodeAccrualTypeID, CurrentAnnualExpense/CurrentPeriodExpense, and optionally IsDailyRent + RentableArea. | Observed |
| [CON-R-125](../rules/CON-R-125.md) | Any generation or posting: HoldFlag on ExpenseSetup, ExpenseSchedule, ExpenseAccrualSetup, PaymentTransaction or AccrualTransaction is a negative gate at every layer. | Observed |

## Fields

### Relationships (foreign keys) (5)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AmendmentID` | Amendment | Select the amendment that the record is associated with from this field. | Contract Amendment ID | Global |  | `expense_accrual_setup.AmendmentID · TEXT` | [ContractAmendment](ContractAmendment.md) |
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global | yes | `expense_accrual_setup.ContractID · TEXT` | [Contract](Contract.md) |
| `CovenantID` | Covenant | Select the covenant that the record is associated with from this field. | Covenant ID | Global |  | `expense_accrual_setup.CovenantID · TEXT` | [Covenant](Covenant.md) |
| `ExpenseSetupID` | Expense Setup | The ExpenseSetupID field is used to associate an expense accrual setup record with an expense setup record. | Expense Setup ID | Global |  | `expense_accrual_setup.ExpenseSetupID · TEXT` | [ExpenseSetup](ExpenseSetup.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `expense_accrual_setup.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (6)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeAccrualTypeID` | Record Type | Select whether this is an accrual, a forecast, or a plan from this field. | Dropdown (Accrual Type Code) | Global | yes | `expense_accrual_setup.CodeAccrualTypeID · TEXT` | Accrual Type Code |
| `CodeBuildingAreaUnitID` | Building Area Unit | Select the units you are using to measure your area from this field. This field should pre-populate with the area unit you selected when creating your contract. | Dropdown (Building Area Unit Code) | Global |  | `expense_accrual_setup.CodeBuildingAreaUnitID · TEXT` | Building Area Unit Code |
| `CodeCurrencyTypeID` | Currency Type | The Currency Type field allows you to select a currency type to be used on a record. | Dropdown (Currency Type Code) | Global |  | `expense_accrual_setup.CodeCurrencyTypeID · TEXT` | Currency Type Code |
| `CodeExpenseCategoryID` | Expense Category | The Expense Category field allows you to associate your record with a pre-configured expense category. Categories are the children of types, and the grandchildren of groups. | Dropdown (Expense Category Code) | Global |  | `expense_accrual_setup.CodeExpenseCategoryID · TEXT` | Expense Category Code |
| `CodeExpenseGroupID` | Expense Group | The Expense Group field allows you to associate your record with a pre-configured expense group. Expense groups are used to categorize expense types. | Dropdown (Expense Group Code) | Global |  | `expense_accrual_setup.CodeExpenseGroupID · TEXT` | Expense Group Code |
| `CodeExpenseTypeID` | Expense Type | The Expense Type field allows you to associate your record with a pre-configured expense type. Expense Types are used to associate records with lease accounting schedules, AP export numbers, expense accrual accounts, percentage rent accrual accounts, and real estate tax accounts. | Dropdown (Expense Type Code) | Global |  | `expense_accrual_setup.CodeExpenseTypeID · TEXT` | Expense Type Code |

### Money (2)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CurrentAnnualExpense` | Current Annual Expense | The sum of annual amounts for your current expense schedule records for a given expense setup record. | Currency | Global |  | `expense_accrual_setup.CurrentAnnualExpense · TEXT` |  |
| `CurrentPeriodExpense` | Current Period Expense | The sum of period amounts for your current expense schedule records for a given expense setup record. | Currency | Global |  | `expense_accrual_setup.CurrentPeriodExpense · TEXT` |  |

### Quantities (2)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ExpenseAccrualSetupID` | Expense Accrual Setup RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `expense_accrual_setup.ExpenseAccrualSetupID · VARCHAR(64) NOT NULL` |  |
| `RentableArea` | Rentable Area | The Rentable Area field must be populated in order for the system to calculate your rate. The system will remember your rentable area and populate this field whenever it is present on a page. If you are not going to use rentable area, do not enter 0. Leave this field blank. | Number | Global |  | `expense_accrual_setup.RentableArea · TEXT` |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BeginDate` | Begin Date | The Begin Date field allows you to select a begin date for the record. | Date | Global |  | `expense_accrual_setup.BeginDate · TEXT` |  |
| `EndDate` | End Date | The End Date field allows you to select an end date for the record. | Date | Global |  | `expense_accrual_setup.EndDate · TEXT` |  |

### Flags (2)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `HoldFlag` | Hold? | This flag is informational-only. Select this check box to mark this expense accrual setup as being on hold. | Boolean | Global |  | `expense_accrual_setup.HoldFlag · TEXT` |  |
| `IsDailyRent` | Daily Rent | Select this check box to indicate that this expense accrual is for daily rent. | Boolean | Global |  | `expense_accrual_setup.IsDailyRent · TEXT` |  |

### Text & notes (6)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AccrualMessage` | Accrual Message | If you'd like to add a message on your accrual, enter the message in this field. | Text | Global |  | `expense_accrual_setup.AccrualMessage · TEXT` |  |
| `BeginPeriodName` | Begin Period / Year | Select the beginning period from this field. | Text | Global |  | `expense_accrual_setup.BeginPeriodName · TEXT` |  |
| `Description` |  | Write a description of the record. | Text | Global |  | `expense_accrual_setup.Description · TEXT` |  |
| `EndPeriodName` | End Period / Year | Select the ending period from this field. | Text | Global |  | `expense_accrual_setup.EndPeriodName · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `expense_accrual_setup.Notes · TEXT` |  |
| `Section` |  | Enter the section of the covenant that pertains to this record in this field. | Text | Global |  | `expense_accrual_setup.Section · TEXT` |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Expense Accrual Setup ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `expense_accrual_setup.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `expense_accrual_setup.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `expense_accrual_setup.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `expense_accrual_setup.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `expense_accrual_setup.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | `expense_accrual_setup.RevNumber · TEXT` |  |
