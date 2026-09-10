# DiscountRate — Data Fields

A named discount-rate configuration (by country and accounting method) used in NPV/present-value calculations across ContractFinancialTest and ProFormaBudget. 16 Global fields under Company Items.

**Table Association:** `DiscountRate` &nbsp;·&nbsp; **Total fields:** 16 (Global: 16, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Accounting Method | `CodeAccountingMethodID` | `sCODE_ACCOUNTING_METHOD` | Global | No | No |  | Company Items / Discount Rate |
| Contract Use | `CodeContractUseID` | `sCODE_CONTRACT_USE` | Global | No | No |  | Company Items / Discount Rate |
| Country | `CountryID` | `sTYPE_COUNTRY_ONLY` | Global | No | No |  | Company Items / Discount Rate |
| Country List | `CountryIDList` | `sTYPE_COUNTRY_ONLY` | Global | No | No |  | Company Items / Discount Rate |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Discount Rate |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Company Items / Discount Rate |
| Discount Rate | `DiscountRate` | `sTYPE_PERCENTAGE` | Global | Yes | No |  | Company Items / Discount Rate |
| Effective End Date | `EffectiveThroughDate` | `sTYPE_DATE` | Global | Yes | No |  | Company Items / Discount Rate |
| Maximum Schedule Length (months) | `MaxSchedMons` | `sTYPE_NUMBER` | Global | Yes | No |  | Company Items / Discount Rate |
| Minimum Schedule Length (months) | `MinSchedMons` | `sTYPE_NUMBER` | Global | Yes | No |  | Company Items / Discount Rate |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Discount Rate |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Company Items / Discount Rate |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Company Items / Discount Rate |
| Program | `ProgramID` | `sTYPE_PROGRAM` | Global | No | No |  | Company Items / Discount Rate |
| Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Discount Rate |
| State Province | `StateProvinceIDList` | `sTYPE_STATE_PROVINCE_LIST` | Global | No | No |  | Company Items / Discount Rate |
