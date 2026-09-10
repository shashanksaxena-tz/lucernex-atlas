# Allowance — Data Fields

A tenant-improvement or other landlord allowance on a lease — allowance type/group classification and begin date. 21 fields (17 Global, 4 Firm) under Contract; one of the entities the user specifically named, and its Firm extension (Firm_AllowCostPSF per 005's representative examples) shows ASG tracks a cost-per-square-foot calculation the base platform doesn't.

**Table Association:** `Allowance` &nbsp;·&nbsp; **Total fields:** 21 (Global: 17, Firm: 4)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Allowance ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Allowance |
| Allowance Group | `CodeAllowanceGroupID` | `sCODE_ALLOWANCE_GROUP` | Global | No | No |  | Contract / Allowance |
| Allowance RecID | `AllowanceID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Allowance |
| Allowance Type | `CodeAllowanceTypeID` | `sCODE_ALLOWANCE_TYPE` | Global | No | No |  | Contract / Allowance |
| Amendment | `AmendmentID` | `sTYPE_CONTRACT_AMENDMENT` | Global | No | No |  | Contract / Allowance |
| Begin Date | `BeginDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Allowance |
| Building Area Unit | `CodeBuildingAreaUnitID` | `sCODE_BUILDING_AREA_UNIT` | Global | No | No |  | Contract / Allowance |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Allowance |
| Cost PSF | `Firm_AllowCostPSF` | `sTYPE_MONEY_MATH_OPERATION` | Firm | No | No |  | Contract / Allowance |
| Covenant | `CovenantID` | `sTYPE_COVENANT` | Global | No | No |  | Contract / Allowance |
| Currency Type | `CodeCurrencyTypeID` | `sCODE_CURRENCY_TYPE` | Global | No | No |  | Contract / Allowance |
| Document | `Firm_AllowanceDocument` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Allowance |
| End Date | `EndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Allowance |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Allowance |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Allowance |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Allowance |
| Page | `Firm_AllowancePage` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Allowance |
| Rentable Area | `RentableArea` | `sTYPE_AREA` | Global | No | No |  | Contract / Allowance |
| Section | `Section` | `sTYPE_TEXT` | Global | No | No |  | Contract / Allowance |
| Total Amount | `TotalAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Allowance |
| Test | `math_Test_0` | `sTYPE_MATH_OPERATION` | Firm | No | No |  | Contract / Contract Term |
