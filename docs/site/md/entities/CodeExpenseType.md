# CodeExpenseType

*31 fields · module: Lease Accounting & Payments · Postgres: `code_expense_type`*

Master expense-category configuration — AP export account/tax numbers for up to several slots, defining how each expense type maps to the general ledger on export. 29 Global fields under Contract, despite the 'Code' prefix this is a substantial configuration table rather than a small reference list, so it is kept standalone rather than folded into the small Code/Reference bucket.

Source: `data-fields/code-expense-type.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 31 |
| Fields with a vendor definition | 27 of 31 inventoried |
| Physical tables | `code_expense_type` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 29 (29 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 1 other records |
| Tenancy position | firm_global |
| Rules that name it | 6 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### Lands in code_expense_type

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 27 fields carry a vendor definition

**Observed.** 27 of this record's 31 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: 1 disagree of 29 comparable

**Observed.** Over the 29 fields both captures contain, they agree on 28. The exceptions are ShortName. Estate-wide there are 43 such fields and every one runs the same way — catalogue-required, inventory-not — and they are 34 ContractID, 8 ProjectEntityID and 1 ShortName: the owner foreign key. Parenthood is enforced by the application, not by the database.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [ACC-R-020](../rules/ACC-R-020.md) | `SLSummary.NeedsRecalculation := true` | Observed |
| [ACC-R-025](../rules/ACC-R-025.md) | each period cash flow is routed to the schedule type its expense type designates for the standard being generated | Derived |
| [CON-R-109](../rules/CON-R-109.md) | An expense type is chosen: CodeExpenseTypeID selects both the GL account set and the accounting treatment (CodeASC842ScheduleID, CodeIFRS16ScheduleID, CodeSLScheduleID) in one action. | Observed |
| [CON-R-111](../rules/CON-R-111.md) | Eight-segment coding is applied: AccountNumber1..8 exists on PaymentTransaction/AccrualTransaction but not on CodeExpenseType; whether these are 8 segments of one account or 8 split-coding lines is unresolved. | Inferred |
| [AST-R-008](../rules/AST-R-008.md) | Input: `CodeAssetCategory.GLNumber`, `.SubAccount`, `.DNEAmount`, alongside `ShortName`/ `ActualLongName`/`Inactive`. Effect: Selecting an asset category also selects a GL account, a sub-account, and a per-category spending ceiling (`DNEAmo | Observed |
| [TAX-R-008](../rules/TAX-R-008.md) | Input: `PropertyTaxSummary.CodeExpenseGroupID`/`.CodeExpenseTypeID`, `PropertyTaxAppeal.CodeExpenseGroupID`/`.CodeExpenseTypeID`. Effect: Selecting an expense type/group on a property-tax record is a GL-routing decision, identical in mechan | Observed |

## Fields

### Coded values (drop-downs) (6)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeASC842ScheduleID` | ASC 842 Schedule | The ASC 842 Schedule field is where you select the ASC 842 schedule you want to associate with a record. This field is functional, and changing its value on the Accounting Assumptions page, the Covenants page, or the Recurring Expenses page will set the Recalc? flag to YES. | Dropdown (ASC 842 Schedule Type) | Global |  | `code_expense_type.CodeASC842ScheduleID · TEXT` | ASC 842 Schedule Type |
| `CodeExpenseCategoryID` | Expense Category | This setting links this expense type to a particular expense category. | Dropdown (Expense Category Code) | Global |  | `code_expense_type.CodeExpenseCategoryID · TEXT` | Expense Category Code |
| `CodeIFRS16ScheduleID` | IFRS 16 Schedule | The IFRS 16 Schedule field is where you select the IFRS 16 schedule you want to associate with a record. This field is functional, and changing its value on the Accounting Assumptions page, the Covenants page, or the Recurring Expenses page will set the Recalc? flag to YES. | Dropdown (IFRS 16 Schedule Type) | Global |  | `code_expense_type.CodeIFRS16ScheduleID · TEXT` | IFRS 16 Schedule Type |
| `CodeSLScheduleID` | Straight-Line Schedule | The Straight-Line Schedule field is where you select the Straight Line schedule you want to associate with a record. | Dropdown (Straight Line Schedule Type) | Global |  | `code_expense_type.CodeSLScheduleID · TEXT` | Straight Line Schedule Type |
| `ParentCodeExpenseGroupID` | Parent Group | Select the expense group that this expense type should be associated with. Groups are parents to types. | Dropdown (Expense Group Code) | Global | yes | `code_expense_type.ParentCodeExpenseGroupID · TEXT` | Expense Group Code |
| `ParentID` | Parent Expense Group |  | Dropdown (Expense Group Code) | Global |  | `code_expense_type.ParentID · TEXT` | Expense Group Code |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeID` | Expense Type RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `code_expense_type.CodeID · TEXT` |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Inactive` |  |  | Boolean | — |  | `code_expense_type.Inactive · TEXT` |  |

### Text & notes (21)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `APExportBaseNumber` | AP Export Base Number | Enter the account number for your expenses. | Text | Global |  | `code_expense_type.APExportBaseNumber · TEXT` |  |
| `APExportPrepaidNumber` | AP Export Prepaid Number | Enter the account number for your prepaid expenses (if applicable). | Text | Global |  | `code_expense_type.APExportPrepaidNumber · TEXT` |  |
| `APExportTax1Number` | AP Export Tax #1 | Enter the account number for your accounts payable export taxes. | Text | Global |  | `code_expense_type.APExportTax1Number · TEXT` |  |
| `APExportTax2Number` | AP Export Tax #2 | Enter the account number for your accounts payable export taxes. | Text | Global |  | `code_expense_type.APExportTax2Number · TEXT` |  |
| `APExportTax3Number` | AP Export Tax #3 | Enter the account number for your accounts payable export taxes. | Text | Global |  | `code_expense_type.APExportTax3Number · TEXT` |  |
| `APExportTax4Number` | AP Export Tax #4 | Enter the account number for your accounts payable export taxes. | Text | Global |  | `code_expense_type.APExportTax4Number · TEXT` |  |
| `ActualLongName` | Description |  | Text | — |  | `code_expense_type.ActualLongName · TEXT` |  |
| `ExpAccrualAcct1Number` | Expense Accrual Acct #1 | Enter the account number for your expense accruals. | Text | Global |  | `code_expense_type.ExpAccrualAcct1Number · TEXT` |  |
| `ExpAccrualAcct2Number` | Expense Accrual Acct #2 | Enter the account number for your expense accruals. | Text | Global |  | `code_expense_type.ExpAccrualAcct2Number · TEXT` |  |
| `ExpAccrualAcct3Number` | Expense Accrual Acct #3 | Enter the account number for your expense accruals. | Text | Global |  | `code_expense_type.ExpAccrualAcct3Number · TEXT` |  |
| `ExpAccrualAcct4Number` | Expense Accrual Acct #4 | Enter the account number for your expense accruals. | Text | Global |  | `code_expense_type.ExpAccrualAcct4Number · TEXT` |  |
| `LongDescription` | Description | Write a description of the record. | Text | Global |  | `code_expense_type.LongDescription · TEXT` |  |
| `PercentRentAccrualAcct1Number` | Percent Rent Accrual Acct #1 | Enter the account number for your percent rent accruals. | Text | Global |  | `code_expense_type.PercentRentAccrualAcct1Number · TEXT` |  |
| `PercentRentAccrualAcct2Number` | Percent Rent Accrual Acct #2 | Enter the account number for your percent rent accruals. | Text | Global |  | `code_expense_type.PercentRentAccrualAcct2Number · TEXT` |  |
| `PercentRentAccrualAcct3Number` | Percent Rent Accrual Acct #3 | Enter the account number for your percent rent accruals. | Text | Global |  | `code_expense_type.PercentRentAccrualAcct3Number · TEXT` |  |
| `PercentRentAccrualAcct4Number` | Percent Rent Accrual Acct #4 | Enter the account number for your percent rent accruals. | Text | Global |  | `code_expense_type.PercentRentAccrualAcct4Number · TEXT` |  |
| `RETaxAccrualAcct1Number` | RE Tax Accrual Acct #1 | Enter the account number for your real estate tax accruals. | Text | Global |  | `code_expense_type.RETaxAccrualAcct1Number · TEXT` |  |
| `RETaxAccrualAcct2Number` | RE Tax Accrual Acct #2 | Enter the account number for your real estate tax accruals. | Text | Global |  | `code_expense_type.RETaxAccrualAcct2Number · TEXT` |  |
| `RETaxAccrualAcct3Number` | RE Tax Accrual Acct #3 | Enter the account number for your real estate tax accruals. | Text | Global |  | `code_expense_type.RETaxAccrualAcct3Number · TEXT` |  |
| `RETaxAccrualAcct4Number` | RE Tax Accrual Acct #4 | Enter the account number for your real estate tax accruals. | Text | Global |  | `code_expense_type.RETaxAccrualAcct4Number · TEXT` |  |
| `ShortName` | Name |  | Text | Global | yes | `code_expense_type.ShortName · TEXT` |  |

### Audit & record keeping (2)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `code_expense_type.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `code_expense_type.ModifiedDate · TEXT` |  |
