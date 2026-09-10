# SalesExclusion — Data Fields

An individual excluded sales category feeding into a SalesExclusionCap total. 18 Global fields under Contract.

**Table Association:** `SalesExclusion` &nbsp;·&nbsp; **Total fields:** 18 (Global: 18, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Begin Date | `BeginDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Sales Exclusion |
| Cap Amount | `CapAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales Exclusion |
| Cap Percent | `CapPercent` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Sales Exclusion |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Sales Exclusion |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Sales Exclusion |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Sales Exclusion |
| Currency Type | `CodeCurrencyTypeID` | `sCODE_CURRENCY_TYPE` | Global | No | No |  | Contract / Sales Exclusion |
| End Date | `EndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Sales Exclusion |
| Exclusion ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Sales Exclusion |
| Exclusion Group Cap | `ExclusionGroupCapID` | `sTYPE_SALES_EXCLUSION_CAP` | Global | No | No |  | Contract / Sales Exclusion |
| Exclusion Rate | `ExclusionRate` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Sales Exclusion |
| Exclusion RecID | `SalesExclusionID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Sales Exclusion |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Sales Exclusion |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Sales Exclusion |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Sales Exclusion |
| Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Sales Exclusion |
| Sales Group | `CodeSalesGroupID` | `sCODE_SALES_GROUP` | Global | No | No |  | Contract / Sales Exclusion |
| Sales Type | `CodeSalesTypeID` | `sCODE_SALES_TYPE` | Global | No | No |  | Contract / Sales Exclusion |
