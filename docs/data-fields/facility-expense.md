# FacilityExpense — Data Fields

A non-recovered operating expense tracked directly against a Facility rather than through a Contract's ExpenseRecovery — actual vs. budgeted amount and description. 21 Global fields under Facility.

**Table Association:** `FacilityExpense` &nbsp;·&nbsp; **Total fields:** 21 (Global: 21, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Actual Amount | `ActualAmount` | `sTYPE_MONEY` | Global | No | No |  | Facility / Expense |
| Associated Document | `AssociatedDocumentID` | `sTYPE_DOCUMENT` | Global | No | No |  | Facility / Expense |
| Budgeted Amount | `BudgetedAmount` | `sTYPE_MONEY` | Global | No | No |  | Facility / Expense |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Facility / Expense |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Facility / Expense |
| Description | `Description` | `sTYPE_TEXT` | Global | No | No |  | Facility / Expense |
| Effective Date | `EffectiveDate` | `sTYPE_DATE` | Global | No | No |  | Facility / Expense |
| Expense Group | `CodeExpenseGroupID` | `sCODE_EXPENSE_GROUP` | Global | No | No |  | Facility / Expense |
| Expense Type | `CodeExpenseTypeID` | `sCODE_EXPENSE_TYPE` | Global | No | No |  | Facility / Expense |
| Facility | `FacilityID` | `sTYPE_FACILITY` | Global | Yes | No |  | Facility / Expense |
| Facility Expense ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Facility / Expense |
| Facility Expense RecID | `FacilityExpenseID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Facility / Expense |
| File Name | `BaseName` | `sTYPE_TEXT` | Global | No | No |  | Facility / Expense |
| Folder | `FolderID` | `sTYPE_DOCUMENT` | Global | No | No |  | Facility / Expense |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Facility / Expense |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Facility / Expense |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Facility / Expense |
| Planned Amount | `PlannedAmount` | `sTYPE_MONEY` | Global | No | No |  | Facility / Expense |
| Reference ID | `ReferenceID` | `sTYPE_TEXTAREA` | Global | No | No |  | Facility / Expense |
| Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Facility / Expense |
| Revised Amount | `RevisedAmount` | `sTYPE_MONEY` | Global | No | No |  | Facility / Expense |
