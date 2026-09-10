# BudgetColumn — Data Fields

One column within a capital project budget (e.g., 'Original Budget', 'Approved Change Orders') — status, type, and an 'Allow UI Edit?' flag, the representative example walked through in 005's own documentation. 20 Global fields under Budget.

**Table Association:** `BudgetColumn` &nbsp;·&nbsp; **Total fields:** 20 (Global: 20, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Allow UI Edit? | `AllowUIEdit` | `sTYPE_BOOLEAN` | Global | No | No |  | Budget / Budget Column |
| Bid Package | `BidPackageID` | `sTYPE_BID_PACKAGE` | Global | No | No |  | Budget / Budget Column |
| Budget Column ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Budget / Budget Column |
| Budget Column Name | `BudgetColumnName` | `sTYPE_TEXT` | Global | No | No |  | Budget / Budget Column |
| Budget Column RecID | `BudgetColumnID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Budget / Budget Column |
| Budget Column Status | `CodeBudgetColumnStatusID` | `sCODE_BUDGET_COLUMN_STATUS` | Global | Yes | No |  | Budget / Budget Column |
| Budget Column Type | `BudgetColumnTypeID` | `sTYPE_BUDGET_COLUMN_TYPE` | Global | Yes | No |  | Budget / Budget Column |
| Budget Template | `BudgetTemplateID` | `sTYPE_BUDGET_TEMPLATE` | Global | Yes | No |  | Budget / Budget Column |
| Created By Member | `CreatedByMemberID` | `sTYPE_MEMBER` | Global | Yes | No |  | Budget / Budget Column |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Budget / Budget Column |
| Description | `Description` | `sTYPE_TEXTAREA` | Global | No | No |  | Budget / Budget Column |
| Initialized From Budget Column | `InitializedFromBudgetColumnID` | `sTYPE_BUDGET_COLUMN` | Global | No | No |  | Budget / Budget Column |
| Is Inactive? | `Inactive` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Budget / Budget Column |
| Is Locked? | `IsLocked` | `sTYPE_BOOLEAN` | Global | No | No |  | Budget / Budget Column |
| Is Selected? | `IsSelected` | `sTYPE_BOOLEAN` | Global | No | No |  | Budget / Budget Column |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Budget / Budget Column |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Budget / Budget Column |
| Sealed Bid Number | `SealedBidNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Budget / Budget Column |
| Sequence Number | `SequenceNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | Yes | No |  | Budget / Budget Column |
| Third Party Vendor | `ThirdPartyVendorID` | `sTYPE_EMPLOYER` | Global | No | No |  | Budget / Budget Column |
