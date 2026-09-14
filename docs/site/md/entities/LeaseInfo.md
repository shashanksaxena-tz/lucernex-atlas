# LeaseInfo

*219 fields · module: Contracts & Leases · Postgres: `lease_info`*

A negotiation-history snapshot living under the Pro Forma Lease group — it captures the same handful of deal terms (abatement, rent, TI allowance) at multiple negotiation checkpoints (Broker Recommended, Landlord Asking, Final Terms), each as its own field triple. All 218 fields are Global with none in Firm scope, meaning this negotiation-tracking structure is a fixed platform feature ASG has not customized. It exists to preserve what was offered versus what was countered versus what was ultimately agreed, which is otherwise lost once a lease is executed and only the final terms remain on Contract.

Source: `data-fields/lease-info.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 219 |
| Fields with a vendor definition | 15 of 219 inventoried |
| Physical tables | `lease_info` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 218 (218 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 2 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 1 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in lease_info

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 15 fields carry a vendor definition

**Observed.** 15 of this record's 219 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one source in the corpus that explains fields rather than listing them.

### 2 fields marked required

**Observed.** The inventory marks 2 of this record's fields Required. Across the whole inventory that is 606 fields, which independently corroborates the 603 the corpus had derived from the Data Fields catalogue — two sources, arrived at separately, agreeing to within three.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-144](../rules/CON-R-144.md) | The tenant needs a lifecycle status: Contract.Firm_LeaseStatus (a Firm-scope custom code field, with a Firm_LeaseStatusNotes companion) is ASG's own answer, sitting in the same Contract Info sub-group as the platform's status field — not to | Observed |

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ProjectEntityID` |  |  | Entity ID | — |  | `lease_info.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Soft references (11)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CompanyContact1ID` | Company Contact #1 |  | Contact | Global |  | `lease_info.CompanyContact1ID · TEXT` |  |
| `CompanyContact2ID` | Company Contact #2 |  | Contact | Global |  | `lease_info.CompanyContact2ID · TEXT` |  |
| `ConstructionManagerID` | Construction Manager |  | Contact | Global |  | `lease_info.ConstructionManagerID · TEXT` |  |
| `DeveloperManagerID` | Developer Manager |  | Contact | Global |  | `lease_info.DeveloperManagerID · TEXT` |  |
| `LandlordAttorneyID` | Landlord Attorney |  | Contact | Global |  | `lease_info.LandlordAttorneyID · TEXT` |  |
| `LandlordBrokerContactID` | Landlord Broker |  | Contact | Global |  | `lease_info.LandlordBrokerContactID · TEXT` |  |
| `LandlordID` | Landlord Name |  | Contact | Global |  | `lease_info.LandlordID · TEXT` |  |
| `PropertyManagerID` | Property Manager Name |  | Contact | Global |  | `lease_info.PropertyManagerID · TEXT` |  |
| `SubleaseeID` | Sublease Name |  | Contact | Global |  | `lease_info.SubleaseeID · TEXT` |  |
| `TenantAttorneyID` | Tenant Attorney |  | Contact | Global |  | `lease_info.TenantAttorneyID · TEXT` |  |
| `TenantBrokerContactID` | Tenant Broker |  | Contact | Global |  | `lease_info.TenantBrokerContactID · TEXT` |  |

### Coded values (drop-downs) (6)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeBuildingAreaUnitID` | Building Area Unit | Select the units you are using to measure your area from this field. This field should pre-populate with the area unit you selected when creating your contract. | Dropdown (Building Area Unit Code) | Global |  | `lease_info.CodeBuildingAreaUnitID · TEXT` | Building Area Unit Code |
| `CodeBuildingClassID` | Building Class |  | Dropdown (Building Class Code) | Global |  | `lease_info.CodeBuildingClassID · TEXT` | Building Class Code |
| `CodeCurrencyTypeID` | Currency Type | The Currency Type field allows you to select a currency type to be used on a record. | Dropdown (Currency Type Code) | Global |  | `lease_info.CodeCurrencyTypeID · TEXT` | Currency Type Code |
| `CodeLeaseStatusID` | Lease Status |  | Dropdown (Lease Status Code) | Global |  | `lease_info.CodeLeaseStatusID · TEXT` | Lease Status Code |
| `CodeLeaseTypeID` | Lease Type |  | Dropdown (Lease Type Code) | Global |  | `lease_info.CodeLeaseTypeID · TEXT` | Lease Type Code |
| `CodePropertyPrimaryUseID` | Primary Use |  | Dropdown (Property Primary Use Code) | Global |  | `lease_info.CodePropertyPrimaryUseID · TEXT` | Property Primary Use Code |

### Money (68)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AdditionalRent1Rate` | Additional Rent #1 Rate |  | Currency | Global |  | `lease_info.AdditionalRent1Rate · TEXT` |  |
| `AdditionalRent2Rate` | Additional Rent #2 Rate |  | Currency | Global |  | `lease_info.AdditionalRent2Rate · TEXT` |  |
| `AdditionalRent3Rate` | Additional Rent #3 Rate |  | Currency | Global |  | `lease_info.AdditionalRent3Rate · TEXT` |  |
| `AdditionalRent4Rate` | Additional Rent #4 Rate |  | Currency | Global |  | `lease_info.AdditionalRent4Rate · TEXT` |  |
| `AnnualRentFixedIncrease` | Annual Rent Fixed Increase |  | Currency | Global |  | `lease_info.AnnualRentFixedIncrease · TEXT` |  |
| `AvgAnnualOccupancyCost` | Avg Annual Occupancy Cost |  | Currency | Global |  | `lease_info.AvgAnnualOccupancyCost · TEXT` |  |
| `AvgBaseRentRate` | Avg Base Rent Rate |  | Currency | Global |  | `lease_info.AvgBaseRentRate · TEXT` |  |
| `AvgGrossRentRate` | Avg Gross Rent Rate |  | Currency | Global |  | `lease_info.AvgGrossRentRate · TEXT` |  |
| `AvgMonthlyOccupancyCost` | Avg Monthly Occupancy Cost |  | Currency | Global |  | `lease_info.AvgMonthlyOccupancyCost · TEXT` |  |
| `AvgTotalCostRate` | Avg Total Cost Rate |  | Currency | Global |  | `lease_info.AvgTotalCostRate · TEXT` |  |
| `BaseRent` | Base Rent |  | Currency | Global |  | `lease_info.BaseRent · TEXT` |  |
| `BrokerRecoRent` | Broker Recommended Rent |  | Currency | Global |  | `lease_info.BrokerRecoRent · TEXT` |  |
| `BrokerRecoTenantImprove` | Broker Recommended TI$ |  | Currency | Global |  | `lease_info.BrokerRecoTenantImprove · TEXT` |  |
| `ConstructionAllowanceLL` | Construction Allowance (Landlord) |  | Currency | Global |  | `lease_info.ConstructionAllowanceLL · TEXT` |  |
| `EstOpxCAMTaxes` | Est Opx CAM Taxes |  | Currency | Global |  | `lease_info.EstOpxCAMTaxes · TEXT` |  |
| `EstRETaxes` | Est RE Taxes |  | Currency | Global |  | `lease_info.EstRETaxes · TEXT` |  |
| `FinalRent` | Final Terms Rent |  | Currency | Global |  | `lease_info.FinalRent · TEXT` |  |
| `FinalTenantImprove` | Final Terms TI$ |  | Currency | Global |  | `lease_info.FinalTenantImprove · TEXT` |  |
| `Furniture` |  |  | Currency | Global |  | `lease_info.Furniture · TEXT` |  |
| `LandlordAskingRent` | Landlord Asking Rent |  | Currency | Global |  | `lease_info.LandlordAskingRent · TEXT` |  |
| `LandlordAskingTenantImprove` | Landlord Asking TI$ |  | Currency | Global |  | `lease_info.LandlordAskingTenantImprove · TEXT` |  |
| `MovingAllowance` | Moving Allowance |  | Currency | Global |  | `lease_info.MovingAllowance · TEXT` |  |
| `NPVAvgAnnualOccupancyCost` | NPV Avg Annual Occupancy Cost |  | Currency | Global |  | `lease_info.NPVAvgAnnualOccupancyCost · TEXT` |  |
| `NPVBaseRentRate` | NPV Base Rent Rate |  | Currency | Global |  | `lease_info.NPVBaseRentRate · TEXT` |  |
| `NPVGrossRentRate` | NPV Gross Rent Rate |  | Currency | Global |  | `lease_info.NPVGrossRentRate · TEXT` |  |
| `NPVOccupancyCost` | NPV Occupancy Cost |  | Currency | Global |  | `lease_info.NPVOccupancyCost · TEXT` |  |
| `NPVTotalOccupancyCostRate` | NPV Total Occupancy Cost Rate |  | Currency | Global |  | `lease_info.NPVTotalOccupancyCostRate · TEXT` |  |
| `NetEffectiveRentAmount` | Net Effective Rent Amount |  | Currency | Global |  | `lease_info.NetEffectiveRentAmount · TEXT` |  |
| `NetEffectiveRentRate` | Net Effective Rent Rate |  | Currency | Global |  | `lease_info.NetEffectiveRentRate · TEXT` |  |
| `OtherLLIncentivesExp1Rate` | Other LL Incentives Exp #1 Rate |  | Currency | Global |  | `lease_info.OtherLLIncentivesExp1Rate · TEXT` |  |
| `OtherLLIncentivesExp2Rate` | Other LL Incentives Exp #2 Rate |  | Currency | Global |  | `lease_info.OtherLLIncentivesExp2Rate · TEXT` |  |
| `OtherLLIncentivesExp3Rate` | Other LL Incentives Exp #3 Rate |  | Currency | Global |  | `lease_info.OtherLLIncentivesExp3Rate · TEXT` |  |
| `OtherLLIncentivesExp4Rate` | Other LL Incentives Exp #4 Rate |  | Currency | Global |  | `lease_info.OtherLLIncentivesExp4Rate · TEXT` |  |
| `OtherMthCosts1Rate` | Other Mth Costs #1 Rate |  | Currency | Global |  | `lease_info.OtherMthCosts1Rate · TEXT` |  |
| `OtherMthCosts2Rate` | Other Mth Costs #2 Rate |  | Currency | Global |  | `lease_info.OtherMthCosts2Rate · TEXT` |  |
| `OtherMthCosts3Rate` | Other Mth Costs #3 Rate |  | Currency | Global |  | `lease_info.OtherMthCosts3Rate · TEXT` |  |
| `OtherMthCosts4Rate` | Other Mth Costs #4 Rate |  | Currency | Global |  | `lease_info.OtherMthCosts4Rate · TEXT` |  |
| `OtherOpxPaidDirectly1Rate` | Other Opx Paid Directly #1 Rate |  | Currency | Global |  | `lease_info.OtherOpxPaidDirectly1Rate · TEXT` |  |
| `OtherOpxPaidDirectly2Rate` | Other Opx Paid Directly #2 Rate |  | Currency | Global |  | `lease_info.OtherOpxPaidDirectly2Rate · TEXT` |  |
| `OtherOpxPaidDirectly3Rate` | Other Opx Paid Directly #3 Rate |  | Currency | Global |  | `lease_info.OtherOpxPaidDirectly3Rate · TEXT` |  |
| `OtherOpxPaidDirectly4Rate` | Other Opx Paid Directly #4 Rate |  | Currency | Global |  | `lease_info.OtherOpxPaidDirectly4Rate · TEXT` |  |
| `OtherProjectCostsCapital1` | Other Project Costs Capital #1 |  | Currency | Global |  | `lease_info.OtherProjectCostsCapital1 · TEXT` |  |
| `OtherProjectCostsCapital2` | Other Project Costs Capital #2 |  | Currency | Global |  | `lease_info.OtherProjectCostsCapital2 · TEXT` |  |
| `OtherProjectCostsCapital3` | Other Project Costs Capital #3 |  | Currency | Global |  | `lease_info.OtherProjectCostsCapital3 · TEXT` |  |
| `OtherProjectCostsCapital4` | Other Project Costs Capital #4 |  | Currency | Global |  | `lease_info.OtherProjectCostsCapital4 · TEXT` |  |
| `OtherProjectCostsCapital5` | Other Project Costs Capital #5 |  | Currency | Global |  | `lease_info.OtherProjectCostsCapital5 · TEXT` |  |
| `OtherProjectCostsExp1` | Other Project Costs Exp #1 |  | Currency | Global |  | `lease_info.OtherProjectCostsExp1 · TEXT` |  |
| `OtherProjectCostsExp2` | Other Project Costs Exp #2 |  | Currency | Global |  | `lease_info.OtherProjectCostsExp2 · TEXT` |  |
| `OtherProjectCostsExp3` | Other Project Costs Exp #3 |  | Currency | Global |  | `lease_info.OtherProjectCostsExp3 · TEXT` |  |
| `OtherProjectCostsExp4` | Other Project Costs Exp #4 |  | Currency | Global |  | `lease_info.OtherProjectCostsExp4 · TEXT` |  |
| `OtherProjectCostsExp5` | Other Project Costs Exp #5 |  | Currency | Global |  | `lease_info.OtherProjectCostsExp5 · TEXT` |  |
| `ParkingReservedCost` | Parking Reserved Cost |  | Currency | Global |  | `lease_info.ParkingReservedCost · TEXT` |  |
| `ParkingUnreservedCost` | Parking Unreserved Cost |  | Currency | Global |  | `lease_info.ParkingUnreservedCost · TEXT` |  |
| `RestorationMakeGoodForNewLoc` | Restoration Make Good For New Loc |  | Currency | Global |  | `lease_info.RestorationMakeGoodForNewLoc · TEXT` |  |
| `SecurityDeposit` | Security Deposit |  | Currency | Global |  | `lease_info.SecurityDeposit · TEXT` |  |
| `SpecialExpCredits1Rate` | Special Exp Credits #1 Rate |  | Currency | Global |  | `lease_info.SpecialExpCredits1Rate · TEXT` |  |
| `SpecialExpCredits2Rate` | Special Exp Credits #2 Rate |  | Currency | Global |  | `lease_info.SpecialExpCredits2Rate · TEXT` |  |
| `SpecialExpCredits3Rate` | Special Exp Credits #3 Rate |  | Currency | Global |  | `lease_info.SpecialExpCredits3Rate · TEXT` |  |
| `SpecialExpCredits4Rate` | Special Exp Credits #4 Rate |  | Currency | Global |  | `lease_info.SpecialExpCredits4Rate · TEXT` |  |
| `SpecialExpCredits5Rate` | Special Exp Credits #5 Rate |  | Currency | Global |  | `lease_info.SpecialExpCredits5Rate · TEXT` |  |
| `SubleaseRent` | Sublease Rent |  | Currency | Global |  | `lease_info.SubleaseRent · TEXT` |  |
| `TenantUtilities` | Tenant Utilities |  | Currency | Global |  | `lease_info.TenantUtilities · TEXT` |  |
| `TotalBaseRentObligation` | Total Base Rent Obligation |  | Currency | Global |  | `lease_info.TotalBaseRentObligation · TEXT` |  |
| `TotalConstructionCost` | Total Construction Cost |  | Currency | Global |  | `lease_info.TotalConstructionCost · TEXT` |  |
| `TotalOccCostWithConstruction` | Total Occupancy Cost With Construction |  | Currency | Global |  | `lease_info.TotalOccCostWithConstruction · TEXT` |  |
| `TotalOccupancyCostOverTerm` | Total Occupancy Cost Over Term |  | Currency | Global |  | `lease_info.TotalOccupancyCostOverTerm · TEXT` |  |
| `TotalOccupancyCostYear1` | Total Occupancy Cost Year #1 |  | Currency | Global |  | `lease_info.TotalOccupancyCostYear1 · TEXT` |  |
| `VoiceAndData` | Voice And Data |  | Currency | Global |  | `lease_info.VoiceAndData · TEXT` |  |

### Rates & percentages (16)

Percentage inputs and computed rates.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AddonLossFactorPct` | Addon Loss Factor Pctg |  | Percentage | Global |  | `lease_info.AddonLossFactorPct · TEXT` |  |
| `AnnualRentPctgIncrease` | Annual Rent Pctg Increase |  | Percentage | Global |  | `lease_info.AnnualRentPctgIncrease · TEXT` |  |
| `CorporateTaxRate` | Corporate Tax Rate |  | Percentage | Global |  | `lease_info.CorporateTaxRate · TEXT` |  |
| `DiscountRate` | Discount Rate |  | Percentage | Global |  | `lease_info.DiscountRate · TEXT` |  |
| `EstRETaxesPctInc` | Est RE Taxes Pct Inc |  | Percentage | Global |  | `lease_info.EstRETaxesPctInc · TEXT` |  |
| `OpXAnnualPctIncrease` | Op X Annual Pct Increase |  | Percentage | Global |  | `lease_info.OpXAnnualPctIncrease · TEXT` |  |
| `OtherMthCosts1PctInc` | Other Mth Costs #1 Pct Inc |  | Percentage | Global |  | `lease_info.OtherMthCosts1PctInc · TEXT` |  |
| `OtherMthCosts2PctInc` | Other Mth Costs #2 Pct Inc |  | Percentage | Global |  | `lease_info.OtherMthCosts2PctInc · TEXT` |  |
| `OtherMthCosts3PctInc` | Other Mth Costs #3 Pct Inc |  | Percentage | Global |  | `lease_info.OtherMthCosts3PctInc · TEXT` |  |
| `OtherMthCosts4PctInc` | Other Mth Costs #4 Pct Inc |  | Percentage | Global |  | `lease_info.OtherMthCosts4PctInc · TEXT` |  |
| `OtherOpxPaidDirectly1PctInc` | Other Opx Paid Directly #1 Pct Inc |  | Percentage | Global |  | `lease_info.OtherOpxPaidDirectly1PctInc · TEXT` |  |
| `OtherOpxPaidDirectly2PctInc` | Other Opx Paid Directly #2 Pct Inc |  | Percentage | Global |  | `lease_info.OtherOpxPaidDirectly2PctInc · TEXT` |  |
| `OtherOpxPaidDirectly3PctInc` | Other Opx Paid Directly #3 Pct Inc |  | Percentage | Global |  | `lease_info.OtherOpxPaidDirectly3PctInc · TEXT` |  |
| `OtherOpxPaidDirectly4PctInc` | Other Opx Paid Directly #4 Pct Inc |  | Percentage | Global |  | `lease_info.OtherOpxPaidDirectly4PctInc · TEXT` |  |
| `ParkingAnnualPctIncrease` | Parking Annual Pct Increase |  | Percentage | Global |  | `lease_info.ParkingAnnualPctIncrease · TEXT` |  |
| `TenantUtilAnnualPctIncrease` | Tenant Utility Annual Pct Increase |  | Percentage | Global |  | `lease_info.TenantUtilAnnualPctIncrease · TEXT` |  |

### Quantities (61)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AdditionalRent1StartMonth` | Additional Rent #1 Start Month |  | Number | Global |  | `lease_info.AdditionalRent1StartMonth · TEXT` |  |
| `AdditionalRent1StartYear` | Additional Rent #1 Start Year |  | Number | Global |  | `lease_info.AdditionalRent1StartYear · TEXT` |  |
| `AdditionalRent2StartMonth` | Additional Rent #2 Start Month |  | Number | Global |  | `lease_info.AdditionalRent2StartMonth · TEXT` |  |
| `AdditionalRent2StartYear` | Additional Rent #2 Start Year |  | Number | Global |  | `lease_info.AdditionalRent2StartYear · TEXT` |  |
| `AdditionalRent3StartMonth` | Additional Rent #3 Start Month |  | Number | Global |  | `lease_info.AdditionalRent3StartMonth · TEXT` |  |
| `AdditionalRent3StartYear` | Additional Rent #3 Start Year |  | Number | Global |  | `lease_info.AdditionalRent3StartYear · TEXT` |  |
| `AdditionalRent4StartMonth` | Additional Rent #4 Start Month |  | Number | Global |  | `lease_info.AdditionalRent4StartMonth · TEXT` |  |
| `AdditionalRent4StartYear` | Additional Rent #4 Start Year |  | Number | Global |  | `lease_info.AdditionalRent4StartYear · TEXT` |  |
| `AddonOrLossFactorFlag` | Addon Or Loss Factor? |  | Number | Global |  | `lease_info.AddonOrLossFactorFlag · TEXT` |  |
| `BrokerRecoAbatementDays` | Broker Recommended Abatement |  | Number | Global |  | `lease_info.BrokerRecoAbatementDays · TEXT` |  |
| `EstOpxCAMIncreaseStartMonth` | Est Opx CAM Increase Start Month |  | Number | Global |  | `lease_info.EstOpxCAMIncreaseStartMonth · TEXT` |  |
| `EstOpxCAMIncreaseStartYear` | Est Opx CAM Increase Start Year |  | Number | Global |  | `lease_info.EstOpxCAMIncreaseStartYear · TEXT` |  |
| `EstOpxCAMPassThruStartMonth` | Est Opx CAM Pass Thru Start Month |  | Number | Global |  | `lease_info.EstOpxCAMPassThruStartMonth · TEXT` |  |
| `EstOpxCAMPassThruStartYear` | Est Opx CAM Pass Thru Start Year |  | Number | Global |  | `lease_info.EstOpxCAMPassThruStartYear · TEXT` |  |
| `EstRETaxesIncreaseStartMonth` | Est RE Taxes Increase Start Month |  | Number | Global |  | `lease_info.EstRETaxesIncreaseStartMonth · TEXT` |  |
| `EstRETaxesIncreaseStartYear` | Est RE Taxes Increase Start Year |  | Number | Global |  | `lease_info.EstRETaxesIncreaseStartYear · TEXT` |  |
| `EstRETaxesPassThruStartMonth` | Est RE Taxes Pass Thru Start Month |  | Number | Global |  | `lease_info.EstRETaxesPassThruStartMonth · TEXT` |  |
| `EstRETaxesPassThruStartYear` | Est RE Taxes Pass Thru Start Year |  | Number | Global |  | `lease_info.EstRETaxesPassThruStartYear · TEXT` |  |
| `FinalAbatementDays` | Final Terms Abatement |  | Number | Global |  | `lease_info.FinalAbatementDays · TEXT` |  |
| `LandlordAskingAbatementDays` | Landlord Asking Abatement |  | Number | Global |  | `lease_info.LandlordAskingAbatementDays · TEXT` |  |
| `LeaseInfoID` | Lease RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `lease_info.LeaseInfoID · VARCHAR(64) NOT NULL` |  |
| `LeaseStartMonth` | Lease Start Month |  | Number | Global |  | `lease_info.LeaseStartMonth · TEXT` |  |
| `LeaseStartYear` | Lease Start Year |  | Number | Global |  | `lease_info.LeaseStartYear · TEXT` |  |
| `LeaseStopMonth` | Lease Stop Month |  | Number | Global |  | `lease_info.LeaseStopMonth · TEXT` |  |
| `LeaseStopYear` | Lease Stop Year |  | Number | Global |  | `lease_info.LeaseStopYear · TEXT` |  |
| `LeaseTermInMonths` | Lease Term (in Months) |  | Number | Global |  | `lease_info.LeaseTermInMonths · TEXT` |  |
| `LengthTermMonths` | Length Term Months |  | Number | Global |  | `lease_info.LengthTermMonths · TEXT` |  |
| `MonthsFreeRent` | Months Free Rent |  | Number | Global |  | `lease_info.MonthsFreeRent · TEXT` |  |
| `OtherLLIncentivesExp1Month` | Other LL Incentives Exp #1 Month |  | Number | Global |  | `lease_info.OtherLLIncentivesExp1Month · TEXT` |  |
| `OtherLLIncentivesExp1Year` | Other LL Incentives Exp #1 Year |  | Number | Global |  | `lease_info.OtherLLIncentivesExp1Year · TEXT` |  |
| `OtherLLIncentivesExp2Month` | Other LL Incentives Exp #2 Month |  | Number | Global |  | `lease_info.OtherLLIncentivesExp2Month · TEXT` |  |
| `OtherLLIncentivesExp2Year` | Other LL Incentives Exp #2 Year |  | Number | Global |  | `lease_info.OtherLLIncentivesExp2Year · TEXT` |  |
| `OtherLLIncentivesExp3Month` | Other LL Incentives Exp #3 Month |  | Number | Global |  | `lease_info.OtherLLIncentivesExp3Month · TEXT` |  |
| `OtherLLIncentivesExp3Year` | Other LL Incentives Exp #3 Year |  | Number | Global |  | `lease_info.OtherLLIncentivesExp3Year · TEXT` |  |
| `OtherLLIncentivesExp4Month` | Other LL Incentives Exp #4 Month |  | Number | Global |  | `lease_info.OtherLLIncentivesExp4Month · TEXT` |  |
| `OtherLLIncentivesExp4Year` | Other LL Incentives Exp #4 Year |  | Number | Global |  | `lease_info.OtherLLIncentivesExp4Year · TEXT` |  |
| `OtherMthCostsStartMonth` | Other Mth Costs Start Month |  | Number | Global |  | `lease_info.OtherMthCostsStartMonth · TEXT` |  |
| `OtherMthCostsStartYear` | Other Mth Costs Start Year |  | Number | Global |  | `lease_info.OtherMthCostsStartYear · TEXT` |  |
| `OtherOpxPaidDirectlyStartMonth` | Other Opx Paid Directly Start Month |  | Number | Global |  | `lease_info.OtherOpxPaidDirectlyStartMonth · TEXT` |  |
| `OtherOpxPaidDirectlyStartYear` | Other Opx Paid Directly Start Year |  | Number | Global |  | `lease_info.OtherOpxPaidDirectlyStartYear · TEXT` |  |
| `ParkingFreeMonths` | Parking Free Months |  | Number | Global |  | `lease_info.ParkingFreeMonths · TEXT` |  |
| `ParkingRatio` | Parking Ratio |  | Number | Global |  | `lease_info.ParkingRatio · TEXT` |  |
| `ParkingReservedSpaces` | Parking Reserved Spaces |  | Number | Global |  | `lease_info.ParkingReservedSpaces · TEXT` |  |
| `ParkingUnreservedSpaces` | Parking Unreserved Spaces |  | Number | Global |  | `lease_info.ParkingUnreservedSpaces · TEXT` |  |
| `RemainingTermInMonths` | Remaining Lease Term (in Months) |  | Number | Global |  | `lease_info.RemainingTermInMonths · TEXT` |  |
| `RentPerMonthOrYearFlag` | Rent Per Month Or Year? |  | Number | Global |  | `lease_info.RentPerMonthOrYearFlag · TEXT` |  |
| `RentableArea` | Rentable Area | The Rentable Area field must be populated in order for the system to calculate your rate. The system will remember your rentable area and populate this field whenever it is present on a page. If you are not going to use rentable area, do not enter 0. Leave this field blank. | Number | Global |  | `lease_info.RentableArea · TEXT` |  |
| `SpecialExpCredits1Month` | Special Exp Credits #1 Month |  | Number | Global |  | `lease_info.SpecialExpCredits1Month · TEXT` |  |
| `SpecialExpCredits1Year` | Special Exp Credits #1 Year |  | Number | Global |  | `lease_info.SpecialExpCredits1Year · TEXT` |  |
| `SpecialExpCredits2Month` | Special Exp Credits #2 Month |  | Number | Global |  | `lease_info.SpecialExpCredits2Month · TEXT` |  |
| `SpecialExpCredits2Year` | Special Exp Credits #2 Year |  | Number | Global |  | `lease_info.SpecialExpCredits2Year · TEXT` |  |
| `SpecialExpCredits3Month` | Special Exp Credits #3 Month |  | Number | Global |  | `lease_info.SpecialExpCredits3Month · TEXT` |  |
| `SpecialExpCredits3Year` | Special Exp Credits #3 Year |  | Number | Global |  | `lease_info.SpecialExpCredits3Year · TEXT` |  |
| `SpecialExpCredits4Month` | Special Exp Credits #4 Month |  | Number | Global |  | `lease_info.SpecialExpCredits4Month · TEXT` |  |
| `SpecialExpCredits4Year` | Special Exp Credits #4 Year |  | Number | Global |  | `lease_info.SpecialExpCredits4Year · TEXT` |  |
| `SpecialExpCredits5Month` | Special Exp Credits #5 Month |  | Number | Global |  | `lease_info.SpecialExpCredits5Month · TEXT` |  |
| `SpecialExpCredits5Year` | Special Exp Credits #5 Year |  | Number | Global |  | `lease_info.SpecialExpCredits5Year · TEXT` |  |
| `TotalHeadcount` | Total Headcount |  | Number | Global |  | `lease_info.TotalHeadcount · TEXT` |  |
| `TotalSeatingCapacity` | Total Seating Capacity |  | Number | Global |  | `lease_info.TotalSeatingCapacity · TEXT` |  |
| `UsableArea` | Usable Area | Enter the usable area. | Number | Global |  | `lease_info.UsableArea · TEXT` |  |
| `Version` |  |  | Number | Global | yes | `lease_info.Version · TEXT` |  |

### Dates & timestamps (27)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AdditionalRent1StartDate` | Additional Rent #1 Start Date |  | Date | Global |  | `lease_info.AdditionalRent1StartDate · TEXT` |  |
| `AdditionalRent2StartDate` | Additional Rent #2 Start Date |  | Date | Global |  | `lease_info.AdditionalRent2StartDate · TEXT` |  |
| `AdditionalRent3StartDate` | Additional Rent #3 Start Date |  | Date | Global |  | `lease_info.AdditionalRent3StartDate · TEXT` |  |
| `AdditionalRent4StartDate` | Additional Rent #4 Start Date |  | Date | Global |  | `lease_info.AdditionalRent4StartDate · TEXT` |  |
| `AmendedCommencementDate` | Amended Commencement Date |  | Date | Global |  | `lease_info.AmendedCommencementDate · TEXT` |  |
| `CommencementDate` | Commencement Date | The date when the first term for the lease started. The Commencement Date and the Expiration Date must be populated in order to use the term wizard when setting up a lease. | Date | Global |  | `lease_info.CommencementDate · TEXT` |  |
| `ComputedCommencementDate` | Computed Commencement Date |  | Date | Global |  | `lease_info.ComputedCommencementDate · TEXT` |  |
| `EstOpxCAMIncreaseStartDate` | Est Opx CAM Increase Start Date |  | Date | Global |  | `lease_info.EstOpxCAMIncreaseStartDate · TEXT` |  |
| `EstOpxCAMPassThruStartDate` | Est Opx CAM Pass Thru Start Date |  | Date | Global |  | `lease_info.EstOpxCAMPassThruStartDate · TEXT` |  |
| `EstRETaxesIncreaseStartDate` | Est RE Taxes Increase Start Date |  | Date | Global |  | `lease_info.EstRETaxesIncreaseStartDate · TEXT` |  |
| `EstRETaxesPassThruStartDate` | Est RE Taxes Pass Thru Start Date |  | Date | Global |  | `lease_info.EstRETaxesPassThruStartDate · TEXT` |  |
| `FirstFullMonth` | First Full Month |  | Date | Global |  | `lease_info.FirstFullMonth · TEXT` |  |
| `LeaseExpirationDate` | Lease Expiration Date | The current expiration date of the lease (excluding options). The Commencement Date and the Expiration Date must be populated in order to use the term wizard when setting up a lease. A Lease Expiration Alert will be sent out nightly during the Notice Period until the Expiration Date passes or you act upon an option. | Date | Global |  | `lease_info.LeaseExpirationDate · TEXT` |  |
| `LeaseStatusEffectiveDate` | Status Changed Date |  | Date | Global |  | `lease_info.LeaseStatusEffectiveDate · TEXT` |  |
| `OtherLLIncentivesExp1Date` | Other LL Incentives Exp #1 Date |  | Date | Global |  | `lease_info.OtherLLIncentivesExp1Date · TEXT` |  |
| `OtherLLIncentivesExp2Date` | Other LL Incentives Exp #2 Date |  | Date | Global |  | `lease_info.OtherLLIncentivesExp2Date · TEXT` |  |
| `OtherLLIncentivesExp3Date` | Other LL Incentives Exp #3 Date |  | Date | Global |  | `lease_info.OtherLLIncentivesExp3Date · TEXT` |  |
| `OtherLLIncentivesExp4Date` | Other LL Incentives Exp #4 Date |  | Date | Global |  | `lease_info.OtherLLIncentivesExp4Date · TEXT` |  |
| `OtherMthCostsStartDate` | Other Mth Costs Start Date |  | Date | Global |  | `lease_info.OtherMthCostsStartDate · TEXT` |  |
| `OtherOpxPaidDirectlyStartDate` | Other Opx Paid Directly Start Date |  | Date | Global |  | `lease_info.OtherOpxPaidDirectlyStartDate · TEXT` |  |
| `ProposalDate` | Proposal Date |  | Date | Global |  | `lease_info.ProposalDate · TEXT` |  |
| `SpecialExpCredits1Date` | Special Exp Credits #1 Date |  | Date | Global |  | `lease_info.SpecialExpCredits1Date · TEXT` |  |
| `SpecialExpCredits2Date` | Special Exp Credits #2 Date |  | Date | Global |  | `lease_info.SpecialExpCredits2Date · TEXT` |  |
| `SpecialExpCredits3Date` | Special Exp Credits #3 Date |  | Date | Global |  | `lease_info.SpecialExpCredits3Date · TEXT` |  |
| `SpecialExpCredits4Date` | Special Exp Credits #4 Date |  | Date | Global |  | `lease_info.SpecialExpCredits4Date · TEXT` |  |
| `SpecialExpCredits5Date` | Special Exp Credits #5 Date |  | Date | Global |  | `lease_info.SpecialExpCredits5Date · TEXT` |  |
| `SubleaseEndDate` | Sublease End Date |  | Date | Global |  | `lease_info.SubleaseEndDate · TEXT` |  |

### Flags (4)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BaseRentIncludesOpXFlag` | Base Rent Includes Op X? |  | Boolean | Global |  | `lease_info.BaseRentIncludesOpXFlag · TEXT` |  |
| `IsLeaseExecuted` | Is Lease Executed? |  | Boolean | Global |  | `lease_info.IsLeaseExecuted · TEXT` |  |
| `IsSublease` | Subleased? |  | Boolean | Global |  | `lease_info.IsSublease · TEXT` |  |
| `MonthToMonth` | Month to Month |  | Boolean | Global |  | `lease_info.MonthToMonth · TEXT` |  |

### Text & notes (22)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AdditionalRent1Name` | Additional Rent #1 Name |  | Text | Global |  | `lease_info.AdditionalRent1Name · TEXT` |  |
| `AdditionalRent2Name` | Additional Rent #2 Name |  | Text | Global |  | `lease_info.AdditionalRent2Name · TEXT` |  |
| `AdditionalRent3Name` | Additional Rent #3 Name |  | Text | Global |  | `lease_info.AdditionalRent3Name · TEXT` |  |
| `AdditionalRent4Name` | Additional Rent #4 Name |  | Text | Global |  | `lease_info.AdditionalRent4Name · TEXT` |  |
| `BaseName` | Base Name | This field displays the file name of the file attached to the record. | Text | Global |  | `lease_info.BaseName · TEXT` |  |
| `CancellationOptions` | Cancellation Options |  | Text | Global |  | `lease_info.CancellationOptions · TEXT` |  |
| `ClientName` | Client Name |  | Text | Global |  | `lease_info.ClientName · TEXT` |  |
| `DefinedField1` | Defined Field #1 | This field is a reserved space for client fields. | Text | Global |  | `lease_info.DefinedField1 · TEXT` |  |
| `DefinedField2` | Defined Field #2 | This field is a reserved space for client fields. | Text | Global |  | `lease_info.DefinedField2 · TEXT` |  |
| `DefinedField3` | Defined Field #3 | This field is a reserved space for client fields. | Text | Global |  | `lease_info.DefinedField3 · TEXT` |  |
| `Description` | Notes | Write a description of the record. | Text | Global |  | `lease_info.Description · TEXT` |  |
| `ExpansionOptions` | Expansion Options |  | Text | Global |  | `lease_info.ExpansionOptions · TEXT` |  |
| `LandlordAddress` | Landlord Address |  | Text | Global |  | `lease_info.LandlordAddress · TEXT` |  |
| `LandlordEmployerName` | Landlord Employer Name |  | Text | Global |  | `lease_info.LandlordEmployerName · TEXT` |  |
| `LandlordPhone` | Landlord Phone |  | Text | Global |  | `lease_info.LandlordPhone · TEXT` |  |
| `LocationName` | Location Name |  | Text | Global |  | `lease_info.LocationName · TEXT` |  |
| `MSA` | MSA Code |  | Text | Global |  | `lease_info.MSA · TEXT` |  |
| `PreparerAddress` | Preparer Address |  | Text | Global |  | `lease_info.PreparerAddress · TEXT` |  |
| `PreparerName` | Preparer Name |  | Text | Global |  | `lease_info.PreparerName · TEXT` |  |
| `RenewalOptions` | Renewal Options |  | Text | Global |  | `lease_info.RenewalOptions · TEXT` |  |
| `ScenarioName` | Scenario Name |  | Text | Global |  | `lease_info.ScenarioName · TEXT` |  |
| `SecurityAppliedTo` | Security Applied To |  | Text | Global |  | `lease_info.SecurityAppliedTo · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Lease ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `lease_info.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `lease_info.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `lease_info.ModifiedDate · TEXT` |  |
