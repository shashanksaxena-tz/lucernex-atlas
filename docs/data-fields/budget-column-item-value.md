# BudgetColumnItemValue — Data Fields

The actual dollar value at the intersection of a BudgetLineItem and a BudgetColumn — the individual cell in the budget grid. 20 fields under Budget and Statics.

**Table Association:** `BudgetColumnItemValue` &nbsp;·&nbsp; **Total fields:** 20 (Global: 20, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Budget Column | `BudgetColumnID` | `sTYPE_BUDGET_COLUMN` | Global | Yes | No |  | Budget / Budget Item Value |
| Budget Column ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Budget / Budget Item Value |
| Budget Column Item Value Name | `BudgetColumnItemValueName` | `sTYPE_TEXT` | Global | No | No |  | Budget / Budget Item Value |
| Budget Column Item Value RecID | `BudgetColumnItemValueID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Budget / Budget Item Value |
| Budget Line Item | `BudgetLineItemID` | `sTYPE_BUDGET_LINE_ITEM` | Global | Yes | No |  | Budget / Budget Item Value |
| Budget Option | `BudgetOptionID` | `sTYPE_BUDGET_OPTION` | Global | No | No |  | Budget / Budget Item Value |
| Bypass Locked Check? | `BypassLockedCheck` | `sTYPE_BOOLEAN` | Global | No | No |  | Budget / Budget Item Value |
| Change Reason | `CodeBudgetChangeReasonID` | `sCODE_BUDGET_CHANGE_REASON` | Global | No | No |  | Budget / Budget Item Value |
| Description | `Description` | `sTYPE_TEXTAREA` | Global | No | No |  | Budget / Budget Item Value |
| Item Value | `ItemValue` | `sTYPE_MONEY` | Global | No | No |  | Budget / Budget Item Value |
| Line Item Code | `LineItemCode` | `sTYPE_TEXT` | Global | No | No |  | Budget / Budget Item Value |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Budget / Budget Item Value |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Budget / Budget Item Value |
| Quantity | `Quantity` | `sTYPE_NUMBER` | Global | No | No |  | Budget / Budget Item Value |
| Raw Item Value | `RawItemValue` | `sTYPE_NUMBER` | Global | No | No |  | Budget / Budget Item Value |
| Total Value | `GrandTotalValue` | `sTYPE_MONEY` | Global | No | No |  | Budget / Budget Item Value |
| Unit Cost | `UnitCost` | `sTYPE_MONEY` | Global | No | No |  | Budget / Budget Item Value |
| Units | `CodeBudgetValueUnitsID` | `sCODE_BUDGET_VALUE_UNITS` | Global | No | No |  | Budget / Budget Item Value |
| Budget Comment | `BudgetComment` | `sTYPE_BUDGET_COLUMN_ITEM_COMMENT` | Global | No | No |  | Statics / Layout |
| Budget Value | `BudgetValue` | `sTYPE_BUDGET_COLUMN_ITEM_VALUE` | Global | No | No |  | Statics / Layout |
