# Scenario — Data Fields

A deal/transaction scenario under RE Transaction — comparative what-if terms (Broker Commission, Capital Required, Annual Total Rent) for a prospective site or renewal being evaluated before commitment, plus site demographic fields (Average HH Income, Block) inherited from the site-selection process. 70 Global fields; Scenario sits upstream of Contract in the deal lifecycle, modeling terms under negotiation rather than terms in force.

**Table Association:** `Scenario` &nbsp;·&nbsp; **Total fields:** 70 (Global: 70, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Active Deal Step(s) | `ActiveDealStepTaskIDList` | `sTYPE_TASK` | Global | No | No |  | RE Transaction / Scenario Info |
| Additional Terms | `AdditionalTerms` | `sTYPE_NUMBER` | Global | No | No |  | RE Transaction / Scenario Info |
| Amendment | `AmendmentID` | `sTYPE_CONTRACT_AMENDMENT` | Global | No | No |  | RE Transaction / Scenario Info |
| Annual Total Rent | `AnnualTotalRent` | `sTYPE_MONEY` | Global | No | No |  | RE Transaction / Scenario Info |
| Average HH Income | `AverageHHIncome` | `sTYPE_MONEY` | Global | No | No |  | RE Transaction / Scenario Info |
| Block | `Block` | `sTYPE_TEXT` | Global | No | No |  | RE Transaction / Scenario Info |
| Broker Commission | `BrokerCommission` | `sTYPE_PERCENTAGE` | Global | No | No |  | RE Transaction / Scenario Info |
| Building Area Unit | `CodeBuildingAreaUnitID` | `sCODE_BUILDING_AREA_UNIT` | Global | No | No |  | RE Transaction / Scenario Info |
| Capital Required | `CapitalRequired` | `sTYPE_MONEY` | Global | No | No |  | RE Transaction / Scenario Info |
| Close Days | `CloseDays` | `sTYPE_NUMBER` | Global | No | No |  | RE Transaction / Scenario Info |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | No | No |  | RE Transaction / Scenario Info |
| Contract Key Date | `KeyDateID` | `sTYPE_KEY_DATE` | Global | No | No |  | RE Transaction / Scenario Info |
| Contract Term | `ContractTermID` | `sTYPE_CONTRACT_TERM` | Global | No | No |  | RE Transaction / Scenario Info |
| Covenant | `CovenantID` | `sTYPE_COVENANT` | Global | No | No |  | RE Transaction / Scenario Info |
| Covenant Category | `CodeCovenantCategoryID` | `sCODE_COVENANT_CATEGORY` | Global | No | No |  | RE Transaction / Scenario Info |
| Covenant Group | `CodeCovenantGroupID` | `sCODE_COVENANT_GROUP` | Global | No | No |  | RE Transaction / Scenario Info |
| Covenant Status | `CodeCovenantStatusID` | `sCODE_COVENANT_STATUS` | Global | No | No |  | RE Transaction / Scenario Info |
| Covenant Type | `CodeCovenantTypeID` | `sCODE_COVENANT_TYPE` | Global | No | No |  | RE Transaction / Scenario Info |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | RE Transaction / Scenario Info |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | RE Transaction / Scenario Info |
| Currency | `CodeCurrencyTypeID` | `sCODE_CURRENCY_TYPE` | Global | No | No |  | RE Transaction / Scenario Info |
| Deal Schedule | `DealSchedule` | `sTYPE_TASK` | Global | No | No |  | RE Transaction / Scenario Info |
| Deal Steps | `DealStepSchedule` | `sTYPE_MINISCHEDULE` | Global | No | No |  | RE Transaction / Scenario Info |
| Decision Date | `DecisionDate` | `sTYPE_DATE` | Global | No | No |  | RE Transaction / Scenario Info |
| Decision Status | `CodeDecisionStatusID` | `sCODE_DECISION_STATUS` | Global | No | No |  | RE Transaction / Scenario Info |
| Deposit | `Deposit` | `sTYPE_MONEY` | Global | No | No |  | RE Transaction / Scenario Info |
| Discount Rate | `DiscountRate` | `sTYPE_PERCENTAGE` | Global | No | No |  | RE Transaction / Scenario Info |
| Documents | `DocumentIDList` | `sTYPE_DOCUMENT_LIST` | Global | No | No |  | RE Transaction / Scenario Info |
| Due Diligence Days | `DueDiligenceDays` | `sTYPE_NUMBER` | Global | No | No |  | RE Transaction / Scenario Info |
| End Date | `EndDate` | `sTYPE_DATE` | Global | No | No |  | RE Transaction / Scenario Info |
| Full Address | `HTMLAddress` | `sTYPE_TEXT` | Global | No | No |  | RE Transaction / Scenario Info |
| Lot | `Lot` | `sTYPE_TEXT` | Global | No | No |  | RE Transaction / Scenario Info |
| Major Tenants | `MajorTenants` | `sTYPE_TEXT` | Global | No | No |  | RE Transaction / Scenario Info |
| Market | `CodeMarketAreaID` | `sCODE_MARKET_AREA` | Global | No | No |  | RE Transaction / Scenario Info |
| Median HH Income | `MedianHHIncome` | `sTYPE_MONEY` | Global | No | No |  | RE Transaction / Scenario Info |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | RE Transaction / Scenario Info |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | RE Transaction / Scenario Info |
| New Term End Date | `NewTermEndDate` | `sTYPE_DATE` | Global | No | No |  | RE Transaction / Scenario Info |
| New Term Length | `NewTermLength` | `sTYPE_DATE_MATH_OPERATION` | Global | No | No |  | RE Transaction / Scenario Info |
| New Term Start Date | `NewTermStartDate` | `sTYPE_DATE` | Global | No | No |  | RE Transaction / Scenario Info |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | RE Transaction / Scenario Info |
| Notice Begin Date | `NoticeBeginDate` | `sTYPE_DATE` | Global | No | No |  | RE Transaction / Scenario Info |
| Notice End Date | `NoticeEndDate` | `sTYPE_DATE` | Global | No | No |  | RE Transaction / Scenario Info |
| Operating Costs CAM | `OperatingCostsCAM` | `sTYPE_MONEY` | Global | No | No |  | RE Transaction / Scenario Info |
| Original Lease Start Date | `OriginalLeaseStartDate` | `sTYPE_DATE` | Global | No | No |  | RE Transaction / Scenario Info |
| Parking Ratio | `ParkingRatio` | `sTYPE_NUMBER_FRACTION6DIGITS` | Global | No | No |  | RE Transaction / Scenario Info |
| Parking Spaces | `ParkingSpaces` | `sTYPE_NUMBER` | Global | No | No |  | RE Transaction / Scenario Info |
| Population 5yr Growth | `Population5yrGrowth` | `sTYPE_PERCENTAGE` | Global | No | No |  | RE Transaction / Scenario Info |
| Pro Rata Share Rate | `ProRataShareRate` | `sTYPE_PERCENTAGE` | Global | No | No |  | RE Transaction / Scenario Info |
| Property Type | `CodePropertyTypeID` | `sCODE_PROPERTY_TYPE` | Global | No | No |  | RE Transaction / Scenario Info |
| Proposed Commencement Date | `ProposedCommencementDate` | `sTYPE_DATE` | Global | No | No |  | RE Transaction / Scenario Info |
| Proposed Term Length | `ProposedTermLength` | `sTYPE_NUMBER` | Global | No | No |  | RE Transaction / Scenario Info |
| RE Transaction | `RETransactionID` | `sTYPE_RE_TRANSACTION` | Global | Yes | No |  | RE Transaction / Scenario Info |
| Re Taxes Per Area Unit | `ReTaxesPerAreaUnit` | `sTYPE_MONEY` | Global | No | No |  | RE Transaction / Scenario Info |
| Related Entity | `ProjectEntityID` | `sTYPE_PROJECT_ENTITY` | Global | Yes | No |  | RE Transaction / Scenario Info |
| Rentable Area | `RentableArea` | `sTYPE_AREA` | Global | No | No |  | RE Transaction / Scenario Info |
| Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | RE Transaction / Scenario Info |
| Risk Class | `RiskClass` | `sTYPE_TEXT` | Global | No | No |  | RE Transaction / Scenario Info |
| Scenario ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | RE Transaction / Scenario Info |
| Scenario Deal Type | `CodeScenarioDealTypeID` | `sCODE_SCENARIO_DEAL_TYPE` | Global | Yes | No |  | RE Transaction / Scenario Info |
| Scenario Name | `ScenarioName` | `sTYPE_TEXT` | Global | Yes | No |  | RE Transaction / Scenario Info |
| Scenario RecID | `ScenarioID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | RE Transaction / Scenario Info |
| Scenario Type | `CodeScenarioTypeID` | `sCODE_SCENARIO_TYPE` | Global | No | No |  | RE Transaction / Scenario Info |
| TI Allowance | `TIAllowance` | `sTYPE_MONEY` | Global | No | No |  | RE Transaction / Scenario Info |
| TI Per Area Unit | `TiPerAreaUnit` | `sTYPE_MONEY` | Global | No | No |  | RE Transaction / Scenario Info |
| Term Client Number | `ClientNumber` | `sTYPE_TEXT` | Global | No | No |  | RE Transaction / Scenario Info |
| Term Status | `CodeTermStatusID` | `sCODE_TERM_STATUS` | Global | No | No |  | RE Transaction / Scenario Info |
| Term Type | `CodeTermTypeID` | `sCODE_TERM_TYPE` | Global | No | No |  | RE Transaction / Scenario Info |
| Total Population | `TotalPopulation` | `sTYPE_NUMBER` | Global | No | No |  | RE Transaction / Scenario Info |
| Trade Area Competitors | `TradeAreaCompetitors` | `sTYPE_TEXT` | Global | No | No |  | RE Transaction / Scenario Info |
