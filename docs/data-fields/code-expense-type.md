# CodeExpenseType — Data Fields

Master expense-category configuration — AP export account/tax numbers for up to several slots, defining how each expense type maps to the general ledger on export. 29 Global fields under Contract, despite the 'Code' prefix this is a substantial configuration table rather than a small reference list, so it is kept standalone rather than folded into the small Code/Reference bucket.

**Table Association:** `CodeExpenseType` &nbsp;·&nbsp; **Total fields:** 29 (Global: 29, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| AP Export Base Number | `APExportBaseNumber` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Type |
| AP Export Prepaid Number | `APExportPrepaidNumber` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Type |
| AP Export Tax #1 | `APExportTax1Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Type |
| AP Export Tax #2 | `APExportTax2Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Type |
| AP Export Tax #3 | `APExportTax3Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Type |
| AP Export Tax #4 | `APExportTax4Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Type |
| ASC 842 Schedule | `CodeASC842ScheduleID` | `sCODE_ASC842_SCHEDULE` | Global | No | No |  | Contract / Expense Type |
| Description | `LongDescription` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Type |
| Expense Accrual Acct #1 | `ExpAccrualAcct1Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Type |
| Expense Accrual Acct #2 | `ExpAccrualAcct2Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Type |
| Expense Accrual Acct #3 | `ExpAccrualAcct3Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Type |
| Expense Accrual Acct #4 | `ExpAccrualAcct4Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Type |
| Expense Category | `CodeExpenseCategoryID` | `sCODE_EXPENSE_CATEGORY` | Global | No | No |  | Contract / Expense Type |
| Expense Type RecID | `CodeID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Expense Type |
| IFRS 16 Schedule | `CodeIFRS16ScheduleID` | `sCODE_IFRS16_SCHEDULE` | Global | No | No |  | Contract / Expense Type |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Expense Type |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Expense Type |
| Name | `ShortName` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Expense Type |
| Parent Expense Group | `ParentID` | `sCODE_EXPENSE_GROUP` | Global | No | No |  | Contract / Expense Type |
| Parent Group | `ParentCodeExpenseGroupID` | `sCODE_EXPENSE_GROUP` | Global | Yes | No |  | Contract / Expense Type |
| Percent Rent Accrual Acct #1 | `PercentRentAccrualAcct1Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Type |
| Percent Rent Accrual Acct #2 | `PercentRentAccrualAcct2Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Type |
| Percent Rent Accrual Acct #3 | `PercentRentAccrualAcct3Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Type |
| Percent Rent Accrual Acct #4 | `PercentRentAccrualAcct4Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Type |
| RE Tax Accrual Acct #1 | `RETaxAccrualAcct1Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Type |
| RE Tax Accrual Acct #2 | `RETaxAccrualAcct2Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Type |
| RE Tax Accrual Acct #3 | `RETaxAccrualAcct3Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Type |
| RE Tax Accrual Acct #4 | `RETaxAccrualAcct4Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Type |
| Straight-Line Schedule | `CodeSLScheduleID` | `sCODE_SL_SCHEDULE` | Global | No | No |  | Contract / Expense Type |
