# LeaseInfo

*219 fields · module: Contracts & Leases · Postgres: `lease_info`*

A negotiation-history snapshot living under the Pro Forma Lease group — it captures the same handful of deal terms (abatement, rent, TI allowance) at multiple negotiation checkpoints (Broker Recommended, Landlord Asking, Final Terms), each as its own field triple. All 218 fields are Global with none in Firm scope, meaning this negotiation-tracking structure is a fixed platform feature ASG has not customized. It exists to preserve what was offered versus what was countered versus what was ultimately agreed, which is otherwise lost once a lease is executed and only the final terms remain on Contract.

Source: `data-fields/lease-info.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 219 |
| Catalogued fields | 218 (218 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 2 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 1 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-144](../rules/CON-R-144.md) | The tenant needs a lifecycle status: Contract.Firm_LeaseStatus (a Firm-scope custom code field, with a Firm_LeaseStatusNotes companion) is ASG's own answer, sitting in the same Contract Info sub-group as the platform's status field — not to | Observed |

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Soft references (11)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CompanyContact1ID` | Company Contact #1 | Contact | Global |  |  |
| `CompanyContact2ID` | Company Contact #2 | Contact | Global |  |  |
| `ConstructionManagerID` | Construction Manager | Contact | Global |  |  |
| `DeveloperManagerID` | Developer Manager | Contact | Global |  |  |
| `LandlordAttorneyID` | Landlord Attorney | Contact | Global |  |  |
| `LandlordBrokerContactID` | Landlord Broker | Contact | Global |  |  |
| `LandlordID` | Landlord Name | Contact | Global |  |  |
| `PropertyManagerID` | Property Manager Name | Contact | Global |  |  |
| `SubleaseeID` | Sublease Name | Contact | Global |  |  |
| `TenantAttorneyID` | Tenant Attorney | Contact | Global |  |  |
| `TenantBrokerContactID` | Tenant Broker | Contact | Global |  |  |

### Coded values (drop-downs) (6)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeBuildingAreaUnitID` | Building Area Unit | Dropdown (Building Area Unit Code) | Global |  | Building Area Unit Code |
| `CodeBuildingClassID` | Building Class | Dropdown (Building Class Code) | Global |  | Building Class Code |
| `CodeCurrencyTypeID` | Currency Type | Dropdown (Currency Type Code) | Global |  | Currency Type Code |
| `CodeLeaseStatusID` | Lease Status | Dropdown (Lease Status Code) | Global |  | Lease Status Code |
| `CodeLeaseTypeID` | Lease Type | Dropdown (Lease Type Code) | Global |  | Lease Type Code |
| `CodePropertyPrimaryUseID` | Primary Use | Dropdown (Property Primary Use Code) | Global |  | Property Primary Use Code |

### Money (68)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AdditionalRent1Rate` | Additional Rent #1 Rate | Currency | Global |  |  |
| `AdditionalRent2Rate` | Additional Rent #2 Rate | Currency | Global |  |  |
| `AdditionalRent3Rate` | Additional Rent #3 Rate | Currency | Global |  |  |
| `AdditionalRent4Rate` | Additional Rent #4 Rate | Currency | Global |  |  |
| `AnnualRentFixedIncrease` | Annual Rent Fixed Increase | Currency | Global |  |  |
| `AvgAnnualOccupancyCost` | Avg Annual Occupancy Cost | Currency | Global |  |  |
| `AvgBaseRentRate` | Avg Base Rent Rate | Currency | Global |  |  |
| `AvgGrossRentRate` | Avg Gross Rent Rate | Currency | Global |  |  |
| `AvgMonthlyOccupancyCost` | Avg Monthly Occupancy Cost | Currency | Global |  |  |
| `AvgTotalCostRate` | Avg Total Cost Rate | Currency | Global |  |  |
| `BaseRent` | Base Rent | Currency | Global |  |  |
| `BrokerRecoRent` | Broker Recommended Rent | Currency | Global |  |  |
| `BrokerRecoTenantImprove` | Broker Recommended TI$ | Currency | Global |  |  |
| `ConstructionAllowanceLL` | Construction Allowance (Landlord) | Currency | Global |  |  |
| `EstOpxCAMTaxes` | Est Opx CAM Taxes | Currency | Global |  |  |
| `EstRETaxes` | Est RE Taxes | Currency | Global |  |  |
| `FinalRent` | Final Terms Rent | Currency | Global |  |  |
| `FinalTenantImprove` | Final Terms TI$ | Currency | Global |  |  |
| `Furniture` |  | Currency | Global |  |  |
| `LandlordAskingRent` | Landlord Asking Rent | Currency | Global |  |  |
| `LandlordAskingTenantImprove` | Landlord Asking TI$ | Currency | Global |  |  |
| `MovingAllowance` | Moving Allowance | Currency | Global |  |  |
| `NPVAvgAnnualOccupancyCost` | NPV Avg Annual Occupancy Cost | Currency | Global |  |  |
| `NPVBaseRentRate` | NPV Base Rent Rate | Currency | Global |  |  |
| `NPVGrossRentRate` | NPV Gross Rent Rate | Currency | Global |  |  |
| `NPVOccupancyCost` | NPV Occupancy Cost | Currency | Global |  |  |
| `NPVTotalOccupancyCostRate` | NPV Total Occupancy Cost Rate | Currency | Global |  |  |
| `NetEffectiveRentAmount` | Net Effective Rent Amount | Currency | Global |  |  |
| `NetEffectiveRentRate` | Net Effective Rent Rate | Currency | Global |  |  |
| `OtherLLIncentivesExp1Rate` | Other LL Incentives Exp #1 Rate | Currency | Global |  |  |
| `OtherLLIncentivesExp2Rate` | Other LL Incentives Exp #2 Rate | Currency | Global |  |  |
| `OtherLLIncentivesExp3Rate` | Other LL Incentives Exp #3 Rate | Currency | Global |  |  |
| `OtherLLIncentivesExp4Rate` | Other LL Incentives Exp #4 Rate | Currency | Global |  |  |
| `OtherMthCosts1Rate` | Other Mth Costs #1 Rate | Currency | Global |  |  |
| `OtherMthCosts2Rate` | Other Mth Costs #2 Rate | Currency | Global |  |  |
| `OtherMthCosts3Rate` | Other Mth Costs #3 Rate | Currency | Global |  |  |
| `OtherMthCosts4Rate` | Other Mth Costs #4 Rate | Currency | Global |  |  |
| `OtherOpxPaidDirectly1Rate` | Other Opx Paid Directly #1 Rate | Currency | Global |  |  |
| `OtherOpxPaidDirectly2Rate` | Other Opx Paid Directly #2 Rate | Currency | Global |  |  |
| `OtherOpxPaidDirectly3Rate` | Other Opx Paid Directly #3 Rate | Currency | Global |  |  |
| `OtherOpxPaidDirectly4Rate` | Other Opx Paid Directly #4 Rate | Currency | Global |  |  |
| `OtherProjectCostsCapital1` | Other Project Costs Capital #1 | Currency | Global |  |  |
| `OtherProjectCostsCapital2` | Other Project Costs Capital #2 | Currency | Global |  |  |
| `OtherProjectCostsCapital3` | Other Project Costs Capital #3 | Currency | Global |  |  |
| `OtherProjectCostsCapital4` | Other Project Costs Capital #4 | Currency | Global |  |  |
| `OtherProjectCostsCapital5` | Other Project Costs Capital #5 | Currency | Global |  |  |
| `OtherProjectCostsExp1` | Other Project Costs Exp #1 | Currency | Global |  |  |
| `OtherProjectCostsExp2` | Other Project Costs Exp #2 | Currency | Global |  |  |
| `OtherProjectCostsExp3` | Other Project Costs Exp #3 | Currency | Global |  |  |
| `OtherProjectCostsExp4` | Other Project Costs Exp #4 | Currency | Global |  |  |
| `OtherProjectCostsExp5` | Other Project Costs Exp #5 | Currency | Global |  |  |
| `ParkingReservedCost` | Parking Reserved Cost | Currency | Global |  |  |
| `ParkingUnreservedCost` | Parking Unreserved Cost | Currency | Global |  |  |
| `RestorationMakeGoodForNewLoc` | Restoration Make Good For New Loc | Currency | Global |  |  |
| `SecurityDeposit` | Security Deposit | Currency | Global |  |  |
| `SpecialExpCredits1Rate` | Special Exp Credits #1 Rate | Currency | Global |  |  |
| `SpecialExpCredits2Rate` | Special Exp Credits #2 Rate | Currency | Global |  |  |
| `SpecialExpCredits3Rate` | Special Exp Credits #3 Rate | Currency | Global |  |  |
| `SpecialExpCredits4Rate` | Special Exp Credits #4 Rate | Currency | Global |  |  |
| `SpecialExpCredits5Rate` | Special Exp Credits #5 Rate | Currency | Global |  |  |
| `SubleaseRent` | Sublease Rent | Currency | Global |  |  |
| `TenantUtilities` | Tenant Utilities | Currency | Global |  |  |
| `TotalBaseRentObligation` | Total Base Rent Obligation | Currency | Global |  |  |
| `TotalConstructionCost` | Total Construction Cost | Currency | Global |  |  |
| `TotalOccCostWithConstruction` | Total Occupancy Cost With Construction | Currency | Global |  |  |
| `TotalOccupancyCostOverTerm` | Total Occupancy Cost Over Term | Currency | Global |  |  |
| `TotalOccupancyCostYear1` | Total Occupancy Cost Year #1 | Currency | Global |  |  |
| `VoiceAndData` | Voice And Data | Currency | Global |  |  |

### Rates & percentages (16)

Percentage inputs and computed rates.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AddonLossFactorPct` | Addon Loss Factor Pctg | Percentage | Global |  |  |
| `AnnualRentPctgIncrease` | Annual Rent Pctg Increase | Percentage | Global |  |  |
| `CorporateTaxRate` | Corporate Tax Rate | Percentage | Global |  |  |
| `DiscountRate` | Discount Rate | Percentage | Global |  |  |
| `EstRETaxesPctInc` | Est RE Taxes Pct Inc | Percentage | Global |  |  |
| `OpXAnnualPctIncrease` | Op X Annual Pct Increase | Percentage | Global |  |  |
| `OtherMthCosts1PctInc` | Other Mth Costs #1 Pct Inc | Percentage | Global |  |  |
| `OtherMthCosts2PctInc` | Other Mth Costs #2 Pct Inc | Percentage | Global |  |  |
| `OtherMthCosts3PctInc` | Other Mth Costs #3 Pct Inc | Percentage | Global |  |  |
| `OtherMthCosts4PctInc` | Other Mth Costs #4 Pct Inc | Percentage | Global |  |  |
| `OtherOpxPaidDirectly1PctInc` | Other Opx Paid Directly #1 Pct Inc | Percentage | Global |  |  |
| `OtherOpxPaidDirectly2PctInc` | Other Opx Paid Directly #2 Pct Inc | Percentage | Global |  |  |
| `OtherOpxPaidDirectly3PctInc` | Other Opx Paid Directly #3 Pct Inc | Percentage | Global |  |  |
| `OtherOpxPaidDirectly4PctInc` | Other Opx Paid Directly #4 Pct Inc | Percentage | Global |  |  |
| `ParkingAnnualPctIncrease` | Parking Annual Pct Increase | Percentage | Global |  |  |
| `TenantUtilAnnualPctIncrease` | Tenant Utility Annual Pct Increase | Percentage | Global |  |  |

### Quantities (61)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AdditionalRent1StartMonth` | Additional Rent #1 Start Month | Number | Global |  |  |
| `AdditionalRent1StartYear` | Additional Rent #1 Start Year | Number | Global |  |  |
| `AdditionalRent2StartMonth` | Additional Rent #2 Start Month | Number | Global |  |  |
| `AdditionalRent2StartYear` | Additional Rent #2 Start Year | Number | Global |  |  |
| `AdditionalRent3StartMonth` | Additional Rent #3 Start Month | Number | Global |  |  |
| `AdditionalRent3StartYear` | Additional Rent #3 Start Year | Number | Global |  |  |
| `AdditionalRent4StartMonth` | Additional Rent #4 Start Month | Number | Global |  |  |
| `AdditionalRent4StartYear` | Additional Rent #4 Start Year | Number | Global |  |  |
| `AddonOrLossFactorFlag` | Addon Or Loss Factor? | Number | Global |  |  |
| `BrokerRecoAbatementDays` | Broker Recommended Abatement | Number | Global |  |  |
| `EstOpxCAMIncreaseStartMonth` | Est Opx CAM Increase Start Month | Number | Global |  |  |
| `EstOpxCAMIncreaseStartYear` | Est Opx CAM Increase Start Year | Number | Global |  |  |
| `EstOpxCAMPassThruStartMonth` | Est Opx CAM Pass Thru Start Month | Number | Global |  |  |
| `EstOpxCAMPassThruStartYear` | Est Opx CAM Pass Thru Start Year | Number | Global |  |  |
| `EstRETaxesIncreaseStartMonth` | Est RE Taxes Increase Start Month | Number | Global |  |  |
| `EstRETaxesIncreaseStartYear` | Est RE Taxes Increase Start Year | Number | Global |  |  |
| `EstRETaxesPassThruStartMonth` | Est RE Taxes Pass Thru Start Month | Number | Global |  |  |
| `EstRETaxesPassThruStartYear` | Est RE Taxes Pass Thru Start Year | Number | Global |  |  |
| `FinalAbatementDays` | Final Terms Abatement | Number | Global |  |  |
| `LandlordAskingAbatementDays` | Landlord Asking Abatement | Number | Global |  |  |
| `LeaseInfoID` | Lease RecID | Number | Global |  |  |
| `LeaseStartMonth` | Lease Start Month | Number | Global |  |  |
| `LeaseStartYear` | Lease Start Year | Number | Global |  |  |
| `LeaseStopMonth` | Lease Stop Month | Number | Global |  |  |
| `LeaseStopYear` | Lease Stop Year | Number | Global |  |  |
| `LeaseTermInMonths` | Lease Term (in Months) | Number | Global |  |  |
| `LengthTermMonths` | Length Term Months | Number | Global |  |  |
| `MonthsFreeRent` | Months Free Rent | Number | Global |  |  |
| `OtherLLIncentivesExp1Month` | Other LL Incentives Exp #1 Month | Number | Global |  |  |
| `OtherLLIncentivesExp1Year` | Other LL Incentives Exp #1 Year | Number | Global |  |  |
| `OtherLLIncentivesExp2Month` | Other LL Incentives Exp #2 Month | Number | Global |  |  |
| `OtherLLIncentivesExp2Year` | Other LL Incentives Exp #2 Year | Number | Global |  |  |
| `OtherLLIncentivesExp3Month` | Other LL Incentives Exp #3 Month | Number | Global |  |  |
| `OtherLLIncentivesExp3Year` | Other LL Incentives Exp #3 Year | Number | Global |  |  |
| `OtherLLIncentivesExp4Month` | Other LL Incentives Exp #4 Month | Number | Global |  |  |
| `OtherLLIncentivesExp4Year` | Other LL Incentives Exp #4 Year | Number | Global |  |  |
| `OtherMthCostsStartMonth` | Other Mth Costs Start Month | Number | Global |  |  |
| `OtherMthCostsStartYear` | Other Mth Costs Start Year | Number | Global |  |  |
| `OtherOpxPaidDirectlyStartMonth` | Other Opx Paid Directly Start Month | Number | Global |  |  |
| `OtherOpxPaidDirectlyStartYear` | Other Opx Paid Directly Start Year | Number | Global |  |  |
| `ParkingFreeMonths` | Parking Free Months | Number | Global |  |  |
| `ParkingRatio` | Parking Ratio | Number | Global |  |  |
| `ParkingReservedSpaces` | Parking Reserved Spaces | Number | Global |  |  |
| `ParkingUnreservedSpaces` | Parking Unreserved Spaces | Number | Global |  |  |
| `RemainingTermInMonths` | Remaining Lease Term (in Months) | Number | Global |  |  |
| `RentPerMonthOrYearFlag` | Rent Per Month Or Year? | Number | Global |  |  |
| `RentableArea` | Rentable Area | Number | Global |  |  |
| `SpecialExpCredits1Month` | Special Exp Credits #1 Month | Number | Global |  |  |
| `SpecialExpCredits1Year` | Special Exp Credits #1 Year | Number | Global |  |  |
| `SpecialExpCredits2Month` | Special Exp Credits #2 Month | Number | Global |  |  |
| `SpecialExpCredits2Year` | Special Exp Credits #2 Year | Number | Global |  |  |
| `SpecialExpCredits3Month` | Special Exp Credits #3 Month | Number | Global |  |  |
| `SpecialExpCredits3Year` | Special Exp Credits #3 Year | Number | Global |  |  |
| `SpecialExpCredits4Month` | Special Exp Credits #4 Month | Number | Global |  |  |
| `SpecialExpCredits4Year` | Special Exp Credits #4 Year | Number | Global |  |  |
| `SpecialExpCredits5Month` | Special Exp Credits #5 Month | Number | Global |  |  |
| `SpecialExpCredits5Year` | Special Exp Credits #5 Year | Number | Global |  |  |
| `TotalHeadcount` | Total Headcount | Number | Global |  |  |
| `TotalSeatingCapacity` | Total Seating Capacity | Number | Global |  |  |
| `UsableArea` | Usable Area | Number | Global |  |  |
| `Version` |  | Number | Global | yes |  |

### Dates & timestamps (27)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AdditionalRent1StartDate` | Additional Rent #1 Start Date | Date | Global |  |  |
| `AdditionalRent2StartDate` | Additional Rent #2 Start Date | Date | Global |  |  |
| `AdditionalRent3StartDate` | Additional Rent #3 Start Date | Date | Global |  |  |
| `AdditionalRent4StartDate` | Additional Rent #4 Start Date | Date | Global |  |  |
| `AmendedCommencementDate` | Amended Commencement Date | Date | Global |  |  |
| `CommencementDate` | Commencement Date | Date | Global |  |  |
| `ComputedCommencementDate` | Computed Commencement Date | Date | Global |  |  |
| `EstOpxCAMIncreaseStartDate` | Est Opx CAM Increase Start Date | Date | Global |  |  |
| `EstOpxCAMPassThruStartDate` | Est Opx CAM Pass Thru Start Date | Date | Global |  |  |
| `EstRETaxesIncreaseStartDate` | Est RE Taxes Increase Start Date | Date | Global |  |  |
| `EstRETaxesPassThruStartDate` | Est RE Taxes Pass Thru Start Date | Date | Global |  |  |
| `FirstFullMonth` | First Full Month | Date | Global |  |  |
| `LeaseExpirationDate` | Lease Expiration Date | Date | Global |  |  |
| `LeaseStatusEffectiveDate` | Status Changed Date | Date | Global |  |  |
| `OtherLLIncentivesExp1Date` | Other LL Incentives Exp #1 Date | Date | Global |  |  |
| `OtherLLIncentivesExp2Date` | Other LL Incentives Exp #2 Date | Date | Global |  |  |
| `OtherLLIncentivesExp3Date` | Other LL Incentives Exp #3 Date | Date | Global |  |  |
| `OtherLLIncentivesExp4Date` | Other LL Incentives Exp #4 Date | Date | Global |  |  |
| `OtherMthCostsStartDate` | Other Mth Costs Start Date | Date | Global |  |  |
| `OtherOpxPaidDirectlyStartDate` | Other Opx Paid Directly Start Date | Date | Global |  |  |
| `ProposalDate` | Proposal Date | Date | Global |  |  |
| `SpecialExpCredits1Date` | Special Exp Credits #1 Date | Date | Global |  |  |
| `SpecialExpCredits2Date` | Special Exp Credits #2 Date | Date | Global |  |  |
| `SpecialExpCredits3Date` | Special Exp Credits #3 Date | Date | Global |  |  |
| `SpecialExpCredits4Date` | Special Exp Credits #4 Date | Date | Global |  |  |
| `SpecialExpCredits5Date` | Special Exp Credits #5 Date | Date | Global |  |  |
| `SubleaseEndDate` | Sublease End Date | Date | Global |  |  |

### Flags (4)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BaseRentIncludesOpXFlag` | Base Rent Includes Op X? | Boolean | Global |  |  |
| `IsLeaseExecuted` | Is Lease Executed? | Boolean | Global |  |  |
| `IsSublease` | Subleased? | Boolean | Global |  |  |
| `MonthToMonth` | Month to Month | Boolean | Global |  |  |

### Text & notes (22)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AdditionalRent1Name` | Additional Rent #1 Name | Text | Global |  |  |
| `AdditionalRent2Name` | Additional Rent #2 Name | Text | Global |  |  |
| `AdditionalRent3Name` | Additional Rent #3 Name | Text | Global |  |  |
| `AdditionalRent4Name` | Additional Rent #4 Name | Text | Global |  |  |
| `BaseName` | Base Name | Text | Global |  |  |
| `CancellationOptions` | Cancellation Options | Text | Global |  |  |
| `ClientName` | Client Name | Text | Global |  |  |
| `DefinedField1` | Defined Field #1 | Text | Global |  |  |
| `DefinedField2` | Defined Field #2 | Text | Global |  |  |
| `DefinedField3` | Defined Field #3 | Text | Global |  |  |
| `Description` | Notes | Text | Global |  |  |
| `ExpansionOptions` | Expansion Options | Text | Global |  |  |
| `LandlordAddress` | Landlord Address | Text | Global |  |  |
| `LandlordEmployerName` | Landlord Employer Name | Text | Global |  |  |
| `LandlordPhone` | Landlord Phone | Text | Global |  |  |
| `LocationName` | Location Name | Text | Global |  |  |
| `MSA` | MSA Code | Text | Global |  |  |
| `PreparerAddress` | Preparer Address | Text | Global |  |  |
| `PreparerName` | Preparer Name | Text | Global |  |  |
| `RenewalOptions` | Renewal Options | Text | Global |  |  |
| `ScenarioName` | Scenario Name | Text | Global |  |  |
| `SecurityAppliedTo` | Security Applied To | Text | Global |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Lease ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
