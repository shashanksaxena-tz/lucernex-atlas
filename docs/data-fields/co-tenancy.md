# CoTenancy — Data Fields

A co-tenancy clause (rent reduction if an anchor tenant vacates) — anchor name, co-tenancy amount/area, and begin date, one of the seven Firm-editable Contract subgroups per 005. 26 Global fields under Contract.

**Table Association:** `CoTenancy` &nbsp;·&nbsp; **Total fields:** 26 (Global: 26, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Amendment | `AmendmentID` | `sTYPE_CONTRACT_AMENDMENT` | Global | No | No |  | Contract / Co Tenancy |
| Anchor Name | `CoTenancyName` | `sTYPE_TEXT` | Global | No | No |  | Contract / Co Tenancy |
| Begin Date | `BeginDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Co Tenancy |
| Building Area Unit | `CodeBuildingAreaUnitID` | `sCODE_BUILDING_AREA_UNIT` | Global | No | No |  | Contract / Co Tenancy |
| Co Tenancy Amount | `CoTenancyAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Co Tenancy |
| Co Tenancy Area | `CoTenancyArea` | `sTYPE_AREA` | Global | No | No |  | Contract / Co Tenancy |
| Co Tenancy ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Co Tenancy |
| Co Tenancy Group | `CodeCoTenancyGroupID` | `sCODE_CO_TENANCY_GROUP` | Global | No | No |  | Contract / Co Tenancy |
| Co Tenancy RecID | `CoTenancyID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Co Tenancy |
| Co Tenancy Type | `CodeCoTenancyTypeID` | `sCODE_CO_TENANCY_TYPE` | Global | No | No |  | Contract / Co Tenancy |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Co Tenancy |
| Covenant | `CovenantID` | `sTYPE_COVENANT` | Global | No | No |  | Contract / Co Tenancy |
| Currency Type | `CodeCurrencyTypeID` | `sCODE_CURRENCY_TYPE` | Global | No | No |  | Contract / Co Tenancy |
| Effective Date | `EffectiveDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Co Tenancy |
| End Date | `EndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Co Tenancy |
| Has Right To Terminate? | `HasRightToTerminate` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Co Tenancy |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Co Tenancy |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Co Tenancy |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Co Tenancy |
| Occupancy Percentage | `OccupancyPercentage` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Co Tenancy |
| Remodel Date | `RemodelDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Co Tenancy |
| Rent Account | `RentAccount` | `sTYPE_TEXT` | Global | No | No |  | Contract / Co Tenancy |
| Rent Reduction Amount | `RentReductionAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Co Tenancy |
| Rent Reduction Percent | `RentReductionPercent` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Co Tenancy |
| Sales | `Sales` | `sTYPE_MONEY` | Global | No | No |  | Contract / Co Tenancy |
| Section | `Section` | `sTYPE_TEXT` | Global | No | No |  | Contract / Co Tenancy |
