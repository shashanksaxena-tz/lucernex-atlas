# CodeExpenseType

*31 fields · module: Lease Accounting & Payments · Postgres: `code_expense_type`*

Master expense-category configuration — AP export account/tax numbers for up to several slots, defining how each expense type maps to the general ledger on export. 29 Global fields under Contract, despite the 'Code' prefix this is a substantial configuration table rather than a small reference list, so it is kept standalone rather than folded into the small Code/Reference bucket.

Source: `data-fields/code-expense-type.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 31 |
| Catalogued fields | 29 (29 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 1 other records |
| Tenancy position | firm_global |
| Rules that name it | 6 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

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

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeASC842ScheduleID` | ASC 842 Schedule | Dropdown (ASC 842 Schedule Type) | Global |  | ASC 842 Schedule Type |
| `CodeExpenseCategoryID` | Expense Category | Dropdown (Expense Category Code) | Global |  | Expense Category Code |
| `CodeIFRS16ScheduleID` | IFRS 16 Schedule | Dropdown (IFRS 16 Schedule Type) | Global |  | IFRS 16 Schedule Type |
| `CodeSLScheduleID` | Straight-Line Schedule | Dropdown (Straight Line Schedule Type) | Global |  | Straight Line Schedule Type |
| `ParentCodeExpenseGroupID` | Parent Group | Dropdown (Expense Group Code) | Global | yes | Expense Group Code |
| `ParentID` | Parent Expense Group | Dropdown (Expense Group Code) | Global |  | Expense Group Code |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeID` | Expense Type RecID | Number | Global |  |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Inactive` |  | Boolean | — |  |  |

### Text & notes (21)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `APExportBaseNumber` | AP Export Base Number | Text | Global |  |  |
| `APExportPrepaidNumber` | AP Export Prepaid Number | Text | Global |  |  |
| `APExportTax1Number` | AP Export Tax #1 | Text | Global |  |  |
| `APExportTax2Number` | AP Export Tax #2 | Text | Global |  |  |
| `APExportTax3Number` | AP Export Tax #3 | Text | Global |  |  |
| `APExportTax4Number` | AP Export Tax #4 | Text | Global |  |  |
| `ActualLongName` |  | Text | — |  |  |
| `ExpAccrualAcct1Number` | Expense Accrual Acct #1 | Text | Global |  |  |
| `ExpAccrualAcct2Number` | Expense Accrual Acct #2 | Text | Global |  |  |
| `ExpAccrualAcct3Number` | Expense Accrual Acct #3 | Text | Global |  |  |
| `ExpAccrualAcct4Number` | Expense Accrual Acct #4 | Text | Global |  |  |
| `LongDescription` | Description | Text | Global |  |  |
| `PercentRentAccrualAcct1Number` | Percent Rent Accrual Acct #1 | Text | Global |  |  |
| `PercentRentAccrualAcct2Number` | Percent Rent Accrual Acct #2 | Text | Global |  |  |
| `PercentRentAccrualAcct3Number` | Percent Rent Accrual Acct #3 | Text | Global |  |  |
| `PercentRentAccrualAcct4Number` | Percent Rent Accrual Acct #4 | Text | Global |  |  |
| `RETaxAccrualAcct1Number` | RE Tax Accrual Acct #1 | Text | Global |  |  |
| `RETaxAccrualAcct2Number` | RE Tax Accrual Acct #2 | Text | Global |  |  |
| `RETaxAccrualAcct3Number` | RE Tax Accrual Acct #3 | Text | Global |  |  |
| `RETaxAccrualAcct4Number` | RE Tax Accrual Acct #4 | Text | Global |  |  |
| `ShortName` | Name | Text | Global | yes |  |

### Audit & record keeping (2)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
