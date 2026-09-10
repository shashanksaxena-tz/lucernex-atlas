# LeaseInfo — Data Fields

A negotiation-history snapshot living under the Pro Forma Lease group — it captures the same handful of deal terms (abatement, rent, TI allowance) at multiple negotiation checkpoints (Broker Recommended, Landlord Asking, Final Terms), each as its own field triple. All 218 fields are Global with none in Firm scope, meaning this negotiation-tracking structure is a fixed platform feature ASG has not customized. It exists to preserve what was offered versus what was countered versus what was ultimately agreed, which is otherwise lost once a lease is executed and only the final terms remain on Contract.

**Table Association:** `LeaseInfo` &nbsp;·&nbsp; **Total fields:** 218 (Global: 218, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Broker Recommended Abatement | `BrokerRecoAbatementDays` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Deal History |
| Broker Recommended Rent | `BrokerRecoRent` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Deal History |
| Broker Recommended TI$ | `BrokerRecoTenantImprove` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Deal History |
| Final Terms Abatement | `FinalAbatementDays` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Deal History |
| Final Terms Rent | `FinalRent` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Deal History |
| Final Terms TI$ | `FinalTenantImprove` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Deal History |
| Landlord Asking Abatement | `LandlordAskingAbatementDays` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Deal History |
| Landlord Asking Rent | `LandlordAskingRent` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Deal History |
| Landlord Asking TI$ | `LandlordAskingTenantImprove` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Deal History |
| Amended Commencement Date | `AmendedCommencementDate` | `sTYPE_DATE` | Global | No | No |  | Pro Forma Lease / General Lease Info |
| Building Area Unit | `CodeBuildingAreaUnitID` | `sCODE_BUILDING_AREA_UNIT` | Global | No | No |  | Pro Forma Lease / General Lease Info |
| Commencement Date | `CommencementDate` | `sTYPE_DATE` | Global | No | No |  | Pro Forma Lease / General Lease Info |
| Company Contact #1 | `CompanyContact1ID` | `sTYPE_PERSON` | Global | No | No |  | Pro Forma Lease / General Lease Info |
| Company Contact #2 | `CompanyContact2ID` | `sTYPE_PERSON` | Global | No | No |  | Pro Forma Lease / General Lease Info |
| Currency Type | `CodeCurrencyTypeID` | `sCODE_CURRENCY_TYPE` | Global | No | No |  | Pro Forma Lease / General Lease Info |
| Defined Field #1 | `DefinedField1` | `sTYPE_TEXT` | Global | No | No |  | Pro Forma Lease / General Lease Info |
| Defined Field #2 | `DefinedField2` | `sTYPE_TEXT` | Global | No | No |  | Pro Forma Lease / General Lease Info |
| Defined Field #3 | `DefinedField3` | `sTYPE_TEXT` | Global | No | No |  | Pro Forma Lease / General Lease Info |
| First Full Month | `FirstFullMonth` | `sTYPE_DATE` | Global | No | No |  | Pro Forma Lease / General Lease Info |
| Landlord Address | `LandlordAddress` | `sTYPE_TEXT` | Global | No | No |  | Pro Forma Lease / General Lease Info |
| Landlord Attorney | `LandlordAttorneyID` | `sTYPE_LAWYER` | Global | No | No |  | Pro Forma Lease / General Lease Info |
| Landlord Broker | `LandlordBrokerContactID` | `sTYPE_BROKER` | Global | No | No |  | Pro Forma Lease / General Lease Info |
| Landlord Employer Name | `LandlordEmployerName` | `sTYPE_TEXT` | Global | No | No |  | Pro Forma Lease / General Lease Info |
| Landlord Name | `LandlordID` | `sTYPE_LANDLORD` | Global | No | No |  | Pro Forma Lease / General Lease Info |
| Landlord Phone | `LandlordPhone` | `sTYPE_TEXT` | Global | No | No |  | Pro Forma Lease / General Lease Info |
| Lease ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Pro Forma Lease / General Lease Info |
| Lease Expiration Date | `LeaseExpirationDate` | `sTYPE_DATE` | Global | No | No |  | Pro Forma Lease / General Lease Info |
| Lease RecID | `LeaseInfoID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Pro Forma Lease / General Lease Info |
| Lease Status | `CodeLeaseStatusID` | `sCODE_LEASE_STATUS` | Global | No | No |  | Pro Forma Lease / General Lease Info |
| Lease Term (in Months) | `LeaseTermInMonths` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / General Lease Info |
| Lease Type | `CodeLeaseTypeID` | `sCODE_LEASE_TYPE` | Global | No | No |  | Pro Forma Lease / General Lease Info |
| MSA Code | `MSA` | `sTYPE_TEXT` | Global | No | No |  | Pro Forma Lease / General Lease Info |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Pro Forma Lease / General Lease Info |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Pro Forma Lease / General Lease Info |
| Month to Month | `MonthToMonth` | `sTYPE_BOOLEAN` | Global | No | No |  | Pro Forma Lease / General Lease Info |
| Notes | `Description` | `sTYPE_TEXTAREA` | Global | No | No |  | Pro Forma Lease / General Lease Info |
| Primary Use | `CodePropertyPrimaryUseID` | `sCODE_PROPERTY_PRIMARY_USE` | Global | No | No |  | Pro Forma Lease / General Lease Info |
| Property Manager Name | `PropertyManagerID` | `sTYPE_PROPERTY_MANAGER` | Global | No | No |  | Pro Forma Lease / General Lease Info |
| Remaining Lease Term (in Months) | `RemainingTermInMonths` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / General Lease Info |
| Security Applied To | `SecurityAppliedTo` | `sTYPE_TEXT` | Global | No | No |  | Pro Forma Lease / General Lease Info |
| Security Deposit | `SecurityDeposit` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / General Lease Info |
| Status Changed Date | `LeaseStatusEffectiveDate` | `sTYPE_DATE` | Global | No | No |  | Pro Forma Lease / General Lease Info |
| Sublease End Date | `SubleaseEndDate` | `sTYPE_DATE` | Global | No | No |  | Pro Forma Lease / General Lease Info |
| Sublease Name | `SubleaseeID` | `sTYPE_PERSON` | Global | No | No |  | Pro Forma Lease / General Lease Info |
| Sublease Rent | `SubleaseRent` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / General Lease Info |
| Subleased? | `IsSublease` | `sTYPE_BOOLEAN` | Global | No | No |  | Pro Forma Lease / General Lease Info |
| Tenant Attorney | `TenantAttorneyID` | `sTYPE_LAWYER` | Global | No | No |  | Pro Forma Lease / General Lease Info |
| Tenant Broker | `TenantBrokerContactID` | `sTYPE_BROKER` | Global | No | No |  | Pro Forma Lease / General Lease Info |
| Additional Rent #1 Name | `AdditionalRent1Name` | `sTYPE_TEXT` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Additional Rent #1 Rate | `AdditionalRent1Rate` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Additional Rent #1 Start Date | `AdditionalRent1StartDate` | `sTYPE_DATE` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Additional Rent #1 Start Month | `AdditionalRent1StartMonth` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Additional Rent #1 Start Year | `AdditionalRent1StartYear` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Additional Rent #2 Name | `AdditionalRent2Name` | `sTYPE_TEXT` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Additional Rent #2 Rate | `AdditionalRent2Rate` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Additional Rent #2 Start Date | `AdditionalRent2StartDate` | `sTYPE_DATE` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Additional Rent #2 Start Month | `AdditionalRent2StartMonth` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Additional Rent #2 Start Year | `AdditionalRent2StartYear` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Additional Rent #3 Name | `AdditionalRent3Name` | `sTYPE_TEXT` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Additional Rent #3 Rate | `AdditionalRent3Rate` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Additional Rent #3 Start Date | `AdditionalRent3StartDate` | `sTYPE_DATE` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Additional Rent #3 Start Month | `AdditionalRent3StartMonth` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Additional Rent #3 Start Year | `AdditionalRent3StartYear` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Additional Rent #4 Name | `AdditionalRent4Name` | `sTYPE_TEXT` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Additional Rent #4 Rate | `AdditionalRent4Rate` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Additional Rent #4 Start Date | `AdditionalRent4StartDate` | `sTYPE_DATE` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Additional Rent #4 Start Month | `AdditionalRent4StartMonth` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Additional Rent #4 Start Year | `AdditionalRent4StartYear` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Addon Loss Factor Pctg | `AddonLossFactorPct` | `sTYPE_PERCENTAGE` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Addon Or Loss Factor? | `AddonOrLossFactorFlag` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Annual Rent Fixed Increase | `AnnualRentFixedIncrease` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Annual Rent Pctg Increase | `AnnualRentPctgIncrease` | `sTYPE_PERCENTAGE` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Avg Annual Occupancy Cost | `AvgAnnualOccupancyCost` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Avg Base Rent Rate | `AvgBaseRentRate` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Avg Gross Rent Rate | `AvgGrossRentRate` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Avg Monthly Occupancy Cost | `AvgMonthlyOccupancyCost` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Avg Total Cost Rate | `AvgTotalCostRate` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Base Name | `BaseName` | `sTYPE_TEXT` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Base Rent | `BaseRent` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Base Rent Includes Op X? | `BaseRentIncludesOpXFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Building Class | `CodeBuildingClassID` | `sCODE_BUILDING_CLASS` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Cancellation Options | `CancellationOptions` | `sTYPE_TEXT` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Client Name | `ClientName` | `sTYPE_TEXT` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Computed Commencement Date | `ComputedCommencementDate` | `sTYPE_DATE` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Construction Allowance (Landlord) | `ConstructionAllowanceLL` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Construction Manager | `ConstructionManagerID` | `sTYPE_PERSON` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Corporate Tax Rate | `CorporateTaxRate` | `sTYPE_PERCENTAGE` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Developer Manager | `DeveloperManagerID` | `sTYPE_PERSON` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Discount Rate | `DiscountRate` | `sTYPE_PERCENTAGE` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Est Opx CAM Increase Start Date | `EstOpxCAMIncreaseStartDate` | `sTYPE_DATE` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Est Opx CAM Increase Start Month | `EstOpxCAMIncreaseStartMonth` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Est Opx CAM Increase Start Year | `EstOpxCAMIncreaseStartYear` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Est Opx CAM Pass Thru Start Date | `EstOpxCAMPassThruStartDate` | `sTYPE_DATE` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Est Opx CAM Pass Thru Start Month | `EstOpxCAMPassThruStartMonth` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Est Opx CAM Pass Thru Start Year | `EstOpxCAMPassThruStartYear` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Est Opx CAM Taxes | `EstOpxCAMTaxes` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Est RE Taxes | `EstRETaxes` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Est RE Taxes Increase Start Date | `EstRETaxesIncreaseStartDate` | `sTYPE_DATE` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Est RE Taxes Increase Start Month | `EstRETaxesIncreaseStartMonth` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Est RE Taxes Increase Start Year | `EstRETaxesIncreaseStartYear` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Est RE Taxes Pass Thru Start Date | `EstRETaxesPassThruStartDate` | `sTYPE_DATE` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Est RE Taxes Pass Thru Start Month | `EstRETaxesPassThruStartMonth` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Est RE Taxes Pass Thru Start Year | `EstRETaxesPassThruStartYear` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Est RE Taxes Pct Inc | `EstRETaxesPctInc` | `sTYPE_PERCENTAGE` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Expansion Options | `ExpansionOptions` | `sTYPE_TEXT` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Furniture | `Furniture` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Is Lease Executed? | `IsLeaseExecuted` | `sTYPE_BOOLEAN` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Lease Start Month | `LeaseStartMonth` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Lease Start Year | `LeaseStartYear` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Lease Stop Month | `LeaseStopMonth` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Lease Stop Year | `LeaseStopYear` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Length Term Months | `LengthTermMonths` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Location Name | `LocationName` | `sTYPE_TEXT` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Months Free Rent | `MonthsFreeRent` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Moving Allowance | `MovingAllowance` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| NPV Avg Annual Occupancy Cost | `NPVAvgAnnualOccupancyCost` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| NPV Base Rent Rate | `NPVBaseRentRate` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| NPV Gross Rent Rate | `NPVGrossRentRate` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| NPV Occupancy Cost | `NPVOccupancyCost` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| NPV Total Occupancy Cost Rate | `NPVTotalOccupancyCostRate` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Net Effective Rent Amount | `NetEffectiveRentAmount` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Net Effective Rent Rate | `NetEffectiveRentRate` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Op X Annual Pct Increase | `OpXAnnualPctIncrease` | `sTYPE_PERCENTAGE` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other LL Incentives Exp #1 Date | `OtherLLIncentivesExp1Date` | `sTYPE_DATE` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other LL Incentives Exp #1 Month | `OtherLLIncentivesExp1Month` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other LL Incentives Exp #1 Rate | `OtherLLIncentivesExp1Rate` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other LL Incentives Exp #1 Year | `OtherLLIncentivesExp1Year` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other LL Incentives Exp #2 Date | `OtherLLIncentivesExp2Date` | `sTYPE_DATE` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other LL Incentives Exp #2 Month | `OtherLLIncentivesExp2Month` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other LL Incentives Exp #2 Rate | `OtherLLIncentivesExp2Rate` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other LL Incentives Exp #2 Year | `OtherLLIncentivesExp2Year` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other LL Incentives Exp #3 Date | `OtherLLIncentivesExp3Date` | `sTYPE_DATE` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other LL Incentives Exp #3 Month | `OtherLLIncentivesExp3Month` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other LL Incentives Exp #3 Rate | `OtherLLIncentivesExp3Rate` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other LL Incentives Exp #3 Year | `OtherLLIncentivesExp3Year` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other LL Incentives Exp #4 Date | `OtherLLIncentivesExp4Date` | `sTYPE_DATE` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other LL Incentives Exp #4 Month | `OtherLLIncentivesExp4Month` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other LL Incentives Exp #4 Rate | `OtherLLIncentivesExp4Rate` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other LL Incentives Exp #4 Year | `OtherLLIncentivesExp4Year` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other Mth Costs #1 Pct Inc | `OtherMthCosts1PctInc` | `sTYPE_PERCENTAGE` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other Mth Costs #1 Rate | `OtherMthCosts1Rate` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other Mth Costs #2 Pct Inc | `OtherMthCosts2PctInc` | `sTYPE_PERCENTAGE` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other Mth Costs #2 Rate | `OtherMthCosts2Rate` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other Mth Costs #3 Pct Inc | `OtherMthCosts3PctInc` | `sTYPE_PERCENTAGE` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other Mth Costs #3 Rate | `OtherMthCosts3Rate` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other Mth Costs #4 Pct Inc | `OtherMthCosts4PctInc` | `sTYPE_PERCENTAGE` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other Mth Costs #4 Rate | `OtherMthCosts4Rate` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other Mth Costs Start Date | `OtherMthCostsStartDate` | `sTYPE_DATE` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other Mth Costs Start Month | `OtherMthCostsStartMonth` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other Mth Costs Start Year | `OtherMthCostsStartYear` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other Opx Paid Directly #1 Pct Inc | `OtherOpxPaidDirectly1PctInc` | `sTYPE_PERCENTAGE` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other Opx Paid Directly #1 Rate | `OtherOpxPaidDirectly1Rate` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other Opx Paid Directly #2 Pct Inc | `OtherOpxPaidDirectly2PctInc` | `sTYPE_PERCENTAGE` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other Opx Paid Directly #2 Rate | `OtherOpxPaidDirectly2Rate` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other Opx Paid Directly #3 Pct Inc | `OtherOpxPaidDirectly3PctInc` | `sTYPE_PERCENTAGE` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other Opx Paid Directly #3 Rate | `OtherOpxPaidDirectly3Rate` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other Opx Paid Directly #4 Pct Inc | `OtherOpxPaidDirectly4PctInc` | `sTYPE_PERCENTAGE` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other Opx Paid Directly #4 Rate | `OtherOpxPaidDirectly4Rate` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other Opx Paid Directly Start Date | `OtherOpxPaidDirectlyStartDate` | `sTYPE_DATE` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other Opx Paid Directly Start Month | `OtherOpxPaidDirectlyStartMonth` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other Opx Paid Directly Start Year | `OtherOpxPaidDirectlyStartYear` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other Project Costs Capital #1 | `OtherProjectCostsCapital1` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other Project Costs Capital #2 | `OtherProjectCostsCapital2` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other Project Costs Capital #3 | `OtherProjectCostsCapital3` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other Project Costs Capital #4 | `OtherProjectCostsCapital4` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other Project Costs Capital #5 | `OtherProjectCostsCapital5` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other Project Costs Exp #1 | `OtherProjectCostsExp1` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other Project Costs Exp #2 | `OtherProjectCostsExp2` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other Project Costs Exp #3 | `OtherProjectCostsExp3` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other Project Costs Exp #4 | `OtherProjectCostsExp4` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Other Project Costs Exp #5 | `OtherProjectCostsExp5` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Parking Annual Pct Increase | `ParkingAnnualPctIncrease` | `sTYPE_PERCENTAGE` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Parking Free Months | `ParkingFreeMonths` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Parking Ratio | `ParkingRatio` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Parking Reserved Cost | `ParkingReservedCost` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Parking Reserved Spaces | `ParkingReservedSpaces` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Parking Unreserved Cost | `ParkingUnreservedCost` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Parking Unreserved Spaces | `ParkingUnreservedSpaces` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Preparer Address | `PreparerAddress` | `sTYPE_TEXT` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Preparer Name | `PreparerName` | `sTYPE_TEXT` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Proposal Date | `ProposalDate` | `sTYPE_DATE` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Renewal Options | `RenewalOptions` | `sTYPE_TEXT` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Rent Per Month Or Year? | `RentPerMonthOrYearFlag` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Rentable Area | `RentableArea` | `sTYPE_AREA` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Restoration Make Good For New Loc | `RestorationMakeGoodForNewLoc` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Scenario Name | `ScenarioName` | `sTYPE_TEXT` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Special Exp Credits #1 Date | `SpecialExpCredits1Date` | `sTYPE_DATE` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Special Exp Credits #1 Month | `SpecialExpCredits1Month` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Special Exp Credits #1 Rate | `SpecialExpCredits1Rate` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Special Exp Credits #1 Year | `SpecialExpCredits1Year` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Special Exp Credits #2 Date | `SpecialExpCredits2Date` | `sTYPE_DATE` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Special Exp Credits #2 Month | `SpecialExpCredits2Month` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Special Exp Credits #2 Rate | `SpecialExpCredits2Rate` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Special Exp Credits #2 Year | `SpecialExpCredits2Year` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Special Exp Credits #3 Date | `SpecialExpCredits3Date` | `sTYPE_DATE` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Special Exp Credits #3 Month | `SpecialExpCredits3Month` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Special Exp Credits #3 Rate | `SpecialExpCredits3Rate` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Special Exp Credits #3 Year | `SpecialExpCredits3Year` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Special Exp Credits #4 Date | `SpecialExpCredits4Date` | `sTYPE_DATE` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Special Exp Credits #4 Month | `SpecialExpCredits4Month` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Special Exp Credits #4 Rate | `SpecialExpCredits4Rate` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Special Exp Credits #4 Year | `SpecialExpCredits4Year` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Special Exp Credits #5 Date | `SpecialExpCredits5Date` | `sTYPE_DATE` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Special Exp Credits #5 Month | `SpecialExpCredits5Month` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Special Exp Credits #5 Rate | `SpecialExpCredits5Rate` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Special Exp Credits #5 Year | `SpecialExpCredits5Year` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Tenant Utilities | `TenantUtilities` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Tenant Utility Annual Pct Increase | `TenantUtilAnnualPctIncrease` | `sTYPE_PERCENTAGE` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Total Base Rent Obligation | `TotalBaseRentObligation` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Total Construction Cost | `TotalConstructionCost` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Total Headcount | `TotalHeadcount` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Total Occupancy Cost Over Term | `TotalOccupancyCostOverTerm` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Total Occupancy Cost With Construction | `TotalOccCostWithConstruction` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Total Occupancy Cost Year #1 | `TotalOccupancyCostYear1` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Total Seating Capacity | `TotalSeatingCapacity` | `sTYPE_NUMBER` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Usable Area | `UsableArea` | `sTYPE_AREA` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
| Version | `Version` | `sTYPE_NUMBER` | Global | Yes | No |  | Pro Forma Lease / Lease Analysis |
| Voice And Data | `VoiceAndData` | `sTYPE_MONEY` | Global | No | No |  | Pro Forma Lease / Lease Analysis |
