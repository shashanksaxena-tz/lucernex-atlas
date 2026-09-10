# ExpenseRecoveryItem — Data Fields

The line-item detail underneath ExpenseRecovery — one record per actual-vs-budget variance calculation (A-B, A-P, B-P Variance Amount/Percent), admin fee, and approved pro rata share, used during CAM reconciliation to compare what a tenant was billed against what was approved. 46 Global fields under Contract; naming convention (A=Actual, B=Budget, P=Prior, based on context) mirrors standard CAM reconciliation worksheet columns.

**Table Association:** `ExpenseRecoveryItem` &nbsp;·&nbsp; **Total fields:** 46 (Global: 46, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| A-B Variance Amount | `ABVarianceAmount` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Expense Recovery Item |
| A-B Variance Percent | `ABVariancePercent` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Expense Recovery Item |
| A-P Variance Amount | `APVarianceAmount` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Expense Recovery Item |
| A-P Variance Percent | `APVariancePercent` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Expense Recovery Item |
| Admin Fee Amount | `ApprovedAdminFeeAmtNoZeroDef` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Recovery Item |
| Admin Fee Percentage | `ApprovedAdminFeePrcntNoZeroDef` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Expense Recovery Item |
| Approval Status | `CodeApprovalStatusID` | `sCODE_APPROVAL_STATUS_EXPRECOVERY` | Global | No | No |  | Contract / Expense Recovery Item |
| Approved Amount | `ApprovedAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Recovery Item |
| Approved Pro Rata Share Rate | `ApprovedProRataShareRate` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Expense Recovery Item |
| B-P Variance Amount | `BPVarianceAmount` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Expense Recovery Item |
| B-P Variance Percent | `BPVariancePercent` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Expense Recovery Item |
| Budgeted Amount | `BudgetedAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Recovery Item |
| Budgeted Amount Gross | `BudgetedAmountGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Expense Recovery Item |
| Budgeted Amount Net | `BudgetedAmountNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Expense Recovery Item |
| Budgeted Pro Rata Share Rate | `BudgetedProRataShareRate` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Expense Recovery Item |
| Cap Amount | `ApprovedCapAmountNoZeroDef` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Recovery Item |
| Cap Percentage | `ApprovedCapPercentNoZeroDef` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Expense Recovery Item |
| Computed Admin Fee | `ComputedApprovedAdminFeeNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Expense Recovery Item |
| Computed Approved Cap | `ComputedApprovedCapNoZeroDef` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Expense Recovery Item |
| Computed Total Approved Amount | `ComputedApprovedTotalAmount` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Expense Recovery Item |
| Computed Total Approved Amount Gross | `ComputedApprovedTotalAmountGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Expense Recovery Item |
| Computed Total Approved Amount Net | `ComputedApprovedTotalAmountNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Expense Recovery Item |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Expense Recovery Item |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Expense Recovery Item |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Expense Recovery Item |
| Expense Recovery | `ExpenseRecoveryID` | `sTYPE_EXPENSE_RECOVERY` | Global | Yes | No |  | Contract / Expense Recovery Item |
| Expense Recovery Item ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Expense Recovery Item |
| Expense Recovery Item RecID | `ExpenseRecoveryItemID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Expense Recovery Item |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Expense Recovery Item |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Expense Recovery Item |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Expense Recovery Item |
| Prior Approved Amount | `PriorApprovedAmountNoZeroDef` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Recovery Item |
| Prior Budgeted Amount | `PriorBudgetedAmountNoZeroDef` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Recovery Item |
| Prior Reported Amount | `PriorReportedAmountNoZeroDef` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Recovery Item |
| R-A Variance Amount | `RAVarianceAmount` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Expense Recovery Item |
| R-A Variance Percent | `RAVariancePercent` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Expense Recovery Item |
| R-P Variance Amount | `RPVarianceAmount` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Expense Recovery Item |
| R-P Variance Percent | `RPVariancePercent` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Expense Recovery Item |
| Recovery Item Group | `CodeRecoveryItemGroupID` | `sCODE_RECOVERY_ITEM_GROUP` | Global | No | No |  | Contract / Expense Recovery Item |
| Recovery Item Type | `CodeRecoveryItemTypeID` | `sCODE_RECOVERY_ITEM_TYPE` | Global | No | No |  | Contract / Expense Recovery Item |
| Recovery Section | `CodeRecoverySectionID` | `sCODE_RECOVERY_SECTION` | Global | Yes | No |  | Contract / Expense Recovery Item |
| Reported Amount | `ReportedAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Recovery Item |
| Reported Amount Gross | `ReportedAmountGross` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Expense Recovery Item |
| Reported Amount Net | `ReportedAmountNet` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Expense Recovery Item |
| Reported Pro Rata Share Rate | `ReportedProRataShareRate` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Expense Recovery Item |
| Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Expense Recovery Item |
