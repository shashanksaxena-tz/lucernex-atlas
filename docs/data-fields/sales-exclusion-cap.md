# SalesExclusionCap — Data Fields

A cap limiting how much sales can be excluded from percentage-rent calculation (e.g., online/catalog sales exclusions) — cap amount/percent and begin date. 22 Global fields under Contract.

**Table Association:** `SalesExclusionCap` &nbsp;·&nbsp; **Total fields:** 22 (Global: 22, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Begin Date | `BeginDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Sales Exclusion Cap |
| Cap Amount | `CapAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales Exclusion Cap |
| Cap Percent | `CapPercent` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Sales Exclusion Cap |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Sales Exclusion Cap |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Sales Exclusion Cap |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Sales Exclusion Cap |
| Currency Type | `CodeCurrencyTypeID` | `sCODE_CURRENCY_TYPE` | Global | No | No |  | Contract / Sales Exclusion Cap |
| End Date | `EndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Sales Exclusion Cap |
| Exclusion Cap | `CodeExclusionCapID` | `sCODE_EXCLUSION_CAP` | Global | Yes | No |  | Contract / Sales Exclusion Cap |
| Exclusion Cap ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Sales Exclusion Cap |
| Exclusion Cap RecID | `SalesExclusionCapID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Sales Exclusion Cap |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Sales Exclusion Cap |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Sales Exclusion Cap |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Sales Exclusion Cap |
| PRP Computed Cap Amount | `PRPComputedCapAmount` | `sTYPE_NUMBER` | Global | No | No |  | Contract / Sales Exclusion Cap |
| PRP Excess Excluded Amount | `PRPExcessExcludedAmount` | `sTYPE_NUMBER` | Global | No | No |  | Contract / Sales Exclusion Cap |
| PRP Gross Excluded Amount | `PRPGrossExcludedAmount` | `sTYPE_NUMBER` | Global | No | No |  | Contract / Sales Exclusion Cap |
| PRP Gross Sales Amount | `PRPGrossSalesAmount` | `sTYPE_NUMBER` | Global | No | No |  | Contract / Sales Exclusion Cap |
| PRP Net Excluded Amount | `PRPNetExcludedAmount` | `sTYPE_NUMBER` | Global | No | No |  | Contract / Sales Exclusion Cap |
| Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Sales Exclusion Cap |
| SP Excluded Amount | `SPExcludedAmount` | `sTYPE_NUMBER` | Global | No | No |  | Contract / Sales Exclusion Cap |
| Sales Group | `CodeSalesGroupID` | `sCODE_SALES_GROUP` | Global | No | No |  | Contract / Sales Exclusion Cap |
