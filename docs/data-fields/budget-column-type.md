# BudgetColumnType — Data Fields

The template defining what a Budget Column represents (multi-select allowed, one-instance-only, editable) — configuration metadata one level above the individual BudgetColumn records. 34 Global fields under Budget and Statics.

**Table Association:** `BudgetColumnType` &nbsp;·&nbsp; **Total fields:** 34 (Global: 34, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Allow Multi Select? | `AllowMultiSelect` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Budget / Budget Type Configuration |
| Allow One Instance? | `AllowOneInstance` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Budget / Budget Type Configuration |
| Budget Column Type ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Budget / Budget Type Configuration |
| Budget Column Type RecID | `BudgetColumnTypeID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Budget / Budget Type Configuration |
| Budget Editable? | `AllowUIEditForBudgetColumn` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Budget / Budget Type Configuration |
| Budget View | `BudgetViewID` | `sTYPE_BUDGET_VIEW` | Global | No | No |  | Budget / Budget Type Configuration |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Budget / Budget Type Configuration |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Budget / Budget Type Configuration |
| Default Status | `CodeStatusDefaultID` | `sCODE_BUDGET_COLUMN_STATUS` | Global | No | No |  | Budget / Budget Type Configuration |
| Description | `Description` | `sTYPE_TEXTAREA` | Global | No | No |  | Budget / Budget Type Configuration |
| Is Bid Template | `IsBidTemplate` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Budget / Budget Type Configuration |
| Is For Bid Leveling? | `IsForBidLeveling` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Budget / Budget Type Configuration |
| Is For Bidding? | `IsForBidding` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Budget / Budget Type Configuration |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Budget / Budget Type Configuration |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Budget / Budget Type Configuration |
| Name | `BudgetColumnTypeName` | `sTYPE_TEXT` | Global | Yes | No |  | Budget / Budget Type Configuration |
| Report Group Available Field | `ReportGroupAvailableFieldID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Budget / Budget Type Configuration |
| Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Budget / Budget Type Configuration |
| Status | `CodeStatusSelectedID` | `sCODE_BUDGET_COLUMN_STATUS` | Global | Yes | No |  | Budget / Budget Type Configuration |
| Use this Budget View for Edit Control | `EditControllerID` | `sTYPE_BUDGET_VIEW` | Global | No | No |  | Budget / Budget Type Configuration |
| Valid For Capital Program? | `IsValidForCapProgram` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Budget / Budget Type Configuration |
| Valid For Capital Project? | `IsValidForCapProject` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Budget / Budget Type Configuration |
| Valid For Equipment Contract? | `IsValidForEquipContract` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Budget / Budget Type Configuration |
| Valid For Facility? | `IsValidForFacility` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Budget / Budget Type Configuration |
| Valid For Location? | `IsValidForLocation` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Budget / Budget Type Configuration |
| Valid For Opening Project? | `IsValidForOpenProject` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Budget / Budget Type Configuration |
| Valid For Parcel? | `IsValidForParcel` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Budget / Budget Type Configuration |
| Valid For Portfolio? | `IsValidForPortfolio` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Budget / Budget Type Configuration |
| Valid For Prototype? | `IsValidForPrototype` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Budget / Budget Type Configuration |
| Valid For RE Contract? | `IsValidForContract` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Budget / Budget Type Configuration |
| Valid For Site? | `IsValidForPotentialProject` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Budget / Budget Type Configuration |
| Bidding Budget Column Type to be Leveled | `BiddingBCTForLevelingID` | `sTYPE_BUDGET_COLUMN_TYPE` | Global | No | No |  | Statics / Hidden |
| Code Status Default Name For Create | `CodeStatusDefaultNameForCreate` | `sTYPE_TEXT` | Global | No | No |  | Statics / Hidden |
| Code Status Selected Name For Create | `CodeStatusSelectedNameForCreate` | `sTYPE_TEXT` | Global | No | No |  | Statics / Hidden |
