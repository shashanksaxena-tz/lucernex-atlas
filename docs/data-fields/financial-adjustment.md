# FinancialAdjustment — Data Fields

A manual dollar adjustment to an Asset's or Contract's financial position — accounting adjustment type and amount. 18 Global fields under Contract.

**Table Association:** `FinancialAdjustment` &nbsp;·&nbsp; **Total fields:** 18 (Global: 18, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Accounting Adjustment Type | `CodeAccountingAdjustmentTypeID` | `sCODE_ACCOUNTING_ADJUSTMENT_TYPE` | Global | No | No |  | Contract / Financial Adjustment |
| Amount | `Amount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial Adjustment |
| Asset | `AssetID` | `sTYPE_ASSET` | Global | Yes | No |  | Contract / Financial Adjustment |
| Asset Associated Entity | `AssetAssociatedProjectEntityID` | `sTYPE_MIXEDENTITY` | Global | No | No |  | Contract / Financial Adjustment |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Financial Adjustment |
| Covenant | `CovenantID` | `sTYPE_COVENANT` | Global | No | No |  | Contract / Financial Adjustment |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Financial Adjustment |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Financial Adjustment |
| Effective Date | `EffectiveDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Financial Adjustment |
| Financial Adjustment ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Financial Adjustment |
| Financial Adjustment RecID | `FinancialAdjustmentID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Financial Adjustment |
| Financial Adjustment Status | `CodeFinancialAdjustmentStatusID` | `sCODE_FINANCIAL_ADJUSTMENT_STATUS` | Global | No | No |  | Contract / Financial Adjustment |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Financial Adjustment |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Financial Adjustment |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Financial Adjustment |
| Portion Guaranteed By 3rd Party | `ThirdPartyRVGAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial Adjustment |
| Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Financial Adjustment |
| Total Residual Value Guarantee | `TotalRVGAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial Adjustment |
