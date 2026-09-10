# BudgetLineItem — Data Fields

One line item within a budget template — alert threshold, category code, and template linkage; the line-item layer beneath BudgetColumn/BudgetColumnType. 25 Global fields under Budget.

**Table Association:** `BudgetLineItem` &nbsp;·&nbsp; **Total fields:** 25 (Global: 25, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Alert Enabled | `AlertEnabled` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Budget / Budget Line Item |
| Budget Line Item ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Budget / Budget Line Item |
| Budget Line Item Name | `BudgetLineItemName` | `sTYPE_TEXT` | Global | Yes | No |  | Budget / Budget Line Item |
| Budget Line Item RecID | `BudgetLineItemID` | `sTYPE_BUDGET_LINE_ITEM` | Global | No | No |  | Budget / Budget Line Item |
| Budget Template ID | `BudgetTemplateID` | `sTYPE_BUDGET_TEMPLATE` | Global | No | No |  | Budget / Budget Line Item |
| CSI Code | `CodeCSIID` | `sCODE_CSI` | Global | No | No |  | Budget / Budget Line Item |
| Category Code | `CategoryCode` | `sTYPE_TEXT` | Global | No | No |  | Budget / Budget Line Item |
| Computed Sequence Number | `ComputedSequenceNumber` | `sTYPE_NUMBER` | Global | No | No |  | Budget / Budget Line Item |
| Default Amount | `DefaultAmount` | `sTYPE_MONEY` | Global | No | No |  | Budget / Budget Line Item |
| Defined Field #1 | `DefinedField1` | `sTYPE_TEXT` | Global | No | No |  | Budget / Budget Line Item |
| Defined Field #2 | `DefinedField2` | `sTYPE_TEXT` | Global | No | No |  | Budget / Budget Line Item |
| Description | `Description` | `sTYPE_TEXTAREA` | Global | No | No |  | Budget / Budget Line Item |
| Is Budget Line Item Group | `IsBudgetLineItemGroup` | `sTYPE_NUMBER` | Global | Yes | No |  | Budget / Budget Line Item |
| Is Group? | `IsGroup` | `sTYPE_BOOLEAN` | Global | No | No |  | Budget / Budget Line Item |
| Is Ordered? | `IsOrdered` | `sTYPE_BOOLEAN` | Global | No | No |  | Budget / Budget Line Item |
| Line Item Code | `LineItemCode` | `sTYPE_TEXT` | Global | Yes | No |  | Budget / Budget Line Item |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Budget / Budget Line Item |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Budget / Budget Line Item |
| Order Record Name | `OrderRecordName` | `sTYPE_TEXT` | Global | No | No |  | Budget / Budget Line Item |
| Order Record Type | `OrderRecordType` | `sTYPE_TEXT` | Global | No | No |  | Budget / Budget Line Item |
| Overrun Percent | `OverrunPercent` | `sTYPE_PERCENTAGE` | Global | No | No |  | Budget / Budget Line Item |
| Parent Budget Line Item | `ParentBudgetLineItemID` | `sTYPE_BUDGET_LINE_ITEM` | Global | No | No |  | Budget / Budget Line Item |
| Parent ID | `ParentID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Budget / Budget Line Item |
| Previous Budget Line Item | `PreviousBudgetLineItemID` | `sTYPE_BUDGET_LINE_ITEM` | Global | No | No |  | Budget / Budget Line Item |
| Previous ID | `PreviousID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Budget / Budget Line Item |
