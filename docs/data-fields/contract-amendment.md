# ContractAmendment — Data Fields

A formal amendment/modification to an executed lease — amendment group/number/type classification and base-amount change. 19 fields (17 Global, 2 Firm) under Contract.

**Table Association:** `ContractAmendment` &nbsp;·&nbsp; **Total fields:** 19 (Global: 17, Firm: 2)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Amendment Group | `CodeAmendmentGroupID` | `sCODE_AMENDMENT_GROUP` | Global | No | No |  | Contract / Contract Amendment |
| Amendment Number | `AmendmentNumber` | `sTYPE_TEXT` | Global | No | No |  | Contract / Contract Amendment |
| Amendment RecID | `ContractAmendmentID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Contract Amendment |
| Amendment Type | `CodeAmendmentTypeID` | `sCODE_AMENDMENT_TYPE` | Global | No | No |  | Contract / Contract Amendment |
| Base Amount Change | `BaseAmountChange` | `sTYPE_MONEY` | Global | No | No |  | Contract / Contract Amendment |
| Building Area Unit | `CodeBuildingAreaUnitID` | `sCODE_BUILDING_AREA_UNIT` | Global | No | No |  | Contract / Contract Amendment |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Contract Amendment |
| Contract Amendment ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Contract Amendment |
| Contract Use | `CodeContractUseID` | `sCODE_CONTRACT_USE` | Global | No | No |  | Contract / Contract Amendment |
| Description | `Description` | `sTYPE_TEXT` | Global | No | No |  | Contract / Contract Amendment |
| Documents | `DocumentIDList` | `sTYPE_DOCUMENT_LIST` | Global | No | No |  | Contract / Contract Amendment |
| Effective Date | `EffectiveDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Contract Amendment |
| Entry Date | `Firm_AmendmentEntryDate` | `sTYPE_DATE` | Firm | No | No |  | Contract / Contract Amendment |
| Execution Date | `Firm_AmendmentExecutionDate` | `sTYPE_DATE` | Firm | No | No |  | Contract / Contract Amendment |
| Frequency | `CodeFrequencyID` | `sCODE_MONTH_FREQUENCY` | Global | No | No |  | Contract / Contract Amendment |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Contract Amendment |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Contract Amendment |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Contract Amendment |
| Rentable Area Change | `RentableAreaChange` | `sTYPE_AREA` | Global | No | No |  | Contract / Contract Amendment |
