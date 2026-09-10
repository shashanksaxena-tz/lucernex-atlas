# Asset — Data Fields

The fixed-asset/ROU-asset record tied to a lease or equipment contract — accounting begin/end dates, discount rate overrides, depreciation dates, sale price, and current payment amounts. 126 fields, entirely Global, spanning Equipment/Assets, Statics, and Summary Information, reflecting that an Asset is simultaneously an accounting construct (depreciation, discount rate), a physical-equipment record, and a portfolio summary line.

**Table Association:** `Asset` &nbsp;·&nbsp; **Total fields:** 126 (Global: 126, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Accounting Begin Date | `AccountingBeginDate` | `sTYPE_DATE` | Global | No | No |  | Equipment/Assets / Financial Information |
| Accounting End Date | `AccountingEndDate` | `sTYPE_DATE` | Global | No | No |  | Equipment/Assets / Financial Information |
| Accounting Method Override | `CodeAccountingMethodOverrideID` | `sCODE_ACCOUNTING_METHOD` | Global | No | No |  | Equipment/Assets / Financial Information |
| Asset Sale Price | `AssetSalePrice` | `sTYPE_MONEY` | Global | No | No |  | Equipment/Assets / Financial Information |
| Compounding Frequency | `CodeCompoundingFrequencyID` | `sCODE_MONTH_FREQUENCY` | Global | No | No |  | Equipment/Assets / Financial Information |
| Current Annual Payment | `CurrentAnnualPayment` | `sTYPE_MONEY` | Global | No | No |  | Equipment/Assets / Financial Information |
| Current Monthly Payment | `CurrentMonthlyPayment` | `sTYPE_MONEY` | Global | No | No |  | Equipment/Assets / Financial Information |
| Depreciation End Date | `DepreciationEndDate` | `sTYPE_DATE` | Global | No | No |  | Equipment/Assets / Financial Information |
| Discount Rate Override | `DiscountRateOverride` | `sTYPE_PERCENTAGE` | Global | No | No |  | Equipment/Assets / Financial Information |
| Disposition Date | `DispositionDate` | `sTYPE_DATE` | Global | No | No |  | Equipment/Assets / Financial Information |
| Does Ownership Revert To Tenant? | `DoesTitleRevertToTenant` | `sTYPE_CHECKBOX` | Global | No | No |  | Equipment/Assets / Financial Information |
| Fair Value Of Asset | `FairValueOfAsset` | `sTYPE_MONEY` | Global | No | No |  | Equipment/Assets / Financial Information |
| Fair Value Source | `FairValueSource` | `sTYPE_TEXT` | Global | No | No |  | Equipment/Assets / Financial Information |
| Final Asset Amount | `FinalAssetAmount` | `sTYPE_MONEY` | Global | No | No |  | Equipment/Assets / Financial Information |
| Final Asset Amount Allocation Percentage | `FinalAssetAllocPercent` | `sTYPE_PERCENTAGE` | Global | No | No |  | Equipment/Assets / Financial Information |
| Final Asset Amount Date | `FinalAssetDate` | `sTYPE_DATE` | Global | No | No |  | Equipment/Assets / Financial Information |
| Financial Contract | `FinancialContractID` | `sTYPE_EQUIPMENT_CONTRACT` | Global | No | No |  | Equipment/Assets / Financial Information |
| Has Buyout Option? | `HasBuyoutOption` | `sTYPE_CHECKBOX` | Global | No | No |  | Equipment/Assets / Financial Information |
| Impairment Override Amount | `ImpairmentOverride` | `sTYPE_MONEY` | Global | No | No |  | Equipment/Assets / Financial Information |
| Initial Asset Balance Adjustment | `InitialAssetBalanceAdjust` | `sTYPE_MONEY` | Global | No | No |  | Equipment/Assets / Financial Information |
| Initial Liability Balance Adjustment | `InitialLiabilityBalanceAdjust` | `sTYPE_MONEY` | Global | No | No |  | Equipment/Assets / Financial Information |
| Is Asset Too Specialized For Lessor? | `IsAssetTooSpecializedForLessor` | `sTYPE_CHECKBOX` | Global | No | No |  | Equipment/Assets / Financial Information |
| Month To Month? | `MonthToMonth` | `sTYPE_CHECKBOX` | Global | No | No |  | Equipment/Assets / Financial Information |
| Payments Begin Date | `PaymentsBeginDate` | `sTYPE_DATE` | Global | No | No |  | Equipment/Assets / Financial Information |
| Payments End Date | `PaymentsEndDate` | `sTYPE_DATE` | Global | No | No |  | Equipment/Assets / Financial Information |
| Plan To Buy At End Of Term? | `PlanToBuyAtEndOfTerm` | `sTYPE_CHECKBOX` | Global | No | No |  | Equipment/Assets / Financial Information |
| Portion Of Asset Controlled | `PortionOfAssetControlled` | `sTYPE_PERCENTAGE` | Global | No | No |  | Equipment/Assets / Financial Information |
| Purchase Date | `PurchaseDate` | `sTYPE_DATE` | Global | No | No |  | Equipment/Assets / Financial Information |
| Purchase Order Descrption | `PurchaseOrderDescrption` | `sTYPE_TEXTAREA` | Global | No | No |  | Equipment/Assets / Financial Information |
| Purchase Order Number | `PurchaseOrderNumber` | `sTYPE_TEXT` | Global | No | No |  | Equipment/Assets / Financial Information |
| Purchase Order Reference | `PurchaseOrderReference` | `sTYPE_TEXT` | Global | No | No |  | Equipment/Assets / Financial Information |
| Purchase Price | `PurchasePrice` | `sTYPE_MONEY` | Global | No | No |  | Equipment/Assets / Financial Information |
| Remaining Asset Balance | `RemainingAssetBalance` | `sTYPE_PERCENT_OR_AMOUNT` | Global | No | No |  | Equipment/Assets / Financial Information |
| Remaining Life | `RemainingLife` | `sTYPE_NUMBER` | Global | No | No |  | Equipment/Assets / Financial Information |
| Remaining Life Freq Unit | `CodeRemainingLifeFreqUnitID` | `sCODE_FREQUENCY_UNIT` | Global | No | No |  | Equipment/Assets / Financial Information |
| Residual | `Residual` | `sTYPE_MONEY` | Global | No | No |  | Equipment/Assets / Financial Information |
| Starting Depreciation Cost | `StartingDepreciationCost` | `sTYPE_MONEY` | Global | No | No |  | Equipment/Assets / Financial Information |
| Years Of Depreciable Life | `YearsOfDepreciableLife` | `sTYPE_NUMBER` | Global | No | No |  | Equipment/Assets / Financial Information |
| Account # | `CodeDesc_CodeAssetCategoryID` | `sCODE_ASSET_CATEGORY` | Global | No | No |  | Equipment/Assets / General Information |
| Alternate Vendor | `AlternateVendorID` | `sTYPE_VENDOR` | Global | No | No |  | Equipment/Assets / General Information |
| Asset Barcode Number | `AssetBarcodeNumber` | `sTYPE_TEXT` | Global | No | No |  | Equipment/Assets / General Information |
| Asset ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Equipment/Assets / General Information |
| Asset Department | `CodeAssetDepartmentID` | `sCODE_ASSET_DEPARTMENT` | Global | No | No |  | Equipment/Assets / General Information |
| Asset Group | `CodeAssetGroupID` | `sCODE_ASSET_GROUP` | Global | No | No |  | Equipment/Assets / General Information |
| Asset Number | `ClientNumber` | `sTYPE_TEXT` | Global | No | No |  | Equipment/Assets / General Information |
| Asset Operation Status | `CodeAssetOperationStatusID` | `sCODE_ASSET_OPERATION_STATUS` | Global | No | No |  | Equipment/Assets / General Information |
| Asset Product Type | `CodeAssetProductTypeID` | `sCODE_ASSET_PRODUCT_TYPE` | Global | No | No |  | Equipment/Assets / General Information |
| Asset RecID | `AssetID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Equipment/Assets / General Information |
| Asset Serial # | `AssetSerialNumber` | `sTYPE_TEXT` | Global | No | No |  | Equipment/Assets / General Information |
| Asset Suspension Status | `CodeAssetSuspensionStatusID` | `sCODE_ASSET_SUSPENSION_STATUS` | Global | No | No |  | Equipment/Assets / General Information |
| Asset Type | `CodeAssetTypeID` | `sCODE_ASSET_TYPE` | Global | No | No |  | Equipment/Assets / General Information |
| Asset UUID | `UUID` | `sTYPE_TEXT` | Global | No | No |  | Equipment/Assets / General Information |
| Associated Entity | `AssociatedProjectEntityID` | `sTYPE_MIXEDENTITY` | Global | No | No |  | Equipment/Assets / General Information |
| Color | `Color` | `sTYPE_TEXT` | Global | No | No |  | Equipment/Assets / General Information |
| Contract Responsibility | `ResponsibilityID` | `sTYPE_RESPONSIBILITY` | Global | No | No |  | Equipment/Assets / General Information |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Equipment/Assets / General Information |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Equipment/Assets / General Information |
| Depth | `Depth` | `sTYPE_NUMBER` | Global | No | No |  | Equipment/Assets / General Information |
| Dimension Unit | `CodeDimensionUnitID` | `sCODE_MEASUREMENT_UNIT` | Global | No | No |  | Equipment/Assets / General Information |
| Equipment Name | `AssetName` | `sTYPE_TEXT` | Global | Yes | No |  | Equipment/Assets / General Information |
| Expected Life | `ExpectedLife` | `sTYPE_TEXTAREA` | Global | No | No |  | Equipment/Assets / General Information |
| First Year Bonus Depreciation | `FirstYearBonusDepreciation` | `sTYPE_PERCENTAGE` | Global | No | No |  | Equipment/Assets / General Information |
| Floor | `Floor` | `sTYPE_TEXT` | Global | No | No |  | Equipment/Assets / General Information |
| Generate Service Request | `GenerateServiceRequest` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Equipment/Assets / General Information |
| Height | `Height` | `sTYPE_NUMBER` | Global | No | No |  | Equipment/Assets / General Information |
| In-Service Date | `InServiceDate` | `sTYPE_DATE` | Global | No | No |  | Equipment/Assets / General Information |
| Installation Date | `InstallationDate` | `sTYPE_DATE` | Global | No | No |  | Equipment/Assets / General Information |
| Installer | `InstallerVendorID` | `sTYPE_VENDOR` | Global | No | No |  | Equipment/Assets / General Information |
| Insurance Agent | `InsuranceAgent` | `sTYPE_TEXT` | Global | No | No |  | Equipment/Assets / General Information |
| Insurance Alert Date | `InsuranceAlertDate` | `sTYPE_DATE` | Global | No | No |  | Equipment/Assets / General Information |
| Insurance Begin Date | `InsuranceBeginDate` | `sTYPE_DATE` | Global | No | No |  | Equipment/Assets / General Information |
| Insurance End Date | `InsuranceEndDate` | `sTYPE_DATE` | Global | No | No |  | Equipment/Assets / General Information |
| Insurance Policy Number | `InsurancePolicyNumber` | `sTYPE_TEXT` | Global | No | No |  | Equipment/Assets / General Information |
| Insurance Term | `InsuranceTerm` | `sTYPE_NUMBER` | Global | No | No |  | Equipment/Assets / General Information |
| Insurance Term Unit | `CodeInsuranceTermUnitID` | `sCODE_TIME_UNIT` | Global | No | No |  | Equipment/Assets / General Information |
| Insurance Tickler Date | `InsuranceTicklerDate` | `sTYPE_DATE` | Global | No | No |  | Equipment/Assets / General Information |
| Integration Asset Status | `IntegrationAssetStatus` | `sTYPE_TEXT` | Global | No | No |  | Equipment/Assets / General Information |
| Is Low Asset Value | `IsLowAssetValue` | `sTYPE_NULL_CHECKBOX` | Global | No | No |  | Equipment/Assets / General Information |
| Is Short Term | `IsShortTerm` | `sTYPE_NULL_CHECKBOX` | Global | No | No |  | Equipment/Assets / General Information |
| LOA Months | `LOAMonths` | `sTYPE_NUMBER` | Global | No | No |  | Equipment/Assets / General Information |
| Lease Section | `LeaseSection` | `sTYPE_TEXT` | Global | No | No |  | Equipment/Assets / General Information |
| Location Details | `LocationDetails` | `sTYPE_TEXTAREA` | Global | No | No |  | Equipment/Assets / General Information |
| Maintenance Category | `CodeAssetCategoryID` | `sCODE_ASSET_CATEGORY` | Global | No | No |  | Equipment/Assets / General Information |
| Maintenance Remedy Allowed | `CodeMaintenanceRemedyID` | `sCODE_MAINTENANCE_REMEDY` | Global | No | No |  | Equipment/Assets / General Information |
| Maintenance Remedy Time | `MaintenanceMaximumRemedyDays` | `sTYPE_NUMBER` | Global | No | No |  | Equipment/Assets / General Information |
| Maintenance Responsible Contact | `MaintenanceResponsiblePersonID` | `sTYPE_PERSON` | Global | No | No |  | Equipment/Assets / General Information |
| Maintenance Responsible Party | `CodeMaintenancePartyID` | `sCODE_RESPONSIBLE_PARTY` | Global | No | No |  | Equipment/Assets / General Information |
| Make | `Make` | `sTYPE_TEXT` | Global | No | No |  | Equipment/Assets / General Information |
| Manufacturer | `ManufacturerVendorID` | `sTYPE_VENDOR` | Global | No | No |  | Equipment/Assets / General Information |
| Model # | `ModelNumber` | `sTYPE_TEXT` | Global | No | No |  | Equipment/Assets / General Information |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Equipment/Assets / General Information |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Equipment/Assets / General Information |
| Move In Date | `MoveInDate` | `sTYPE_DATE` | Global | No | No |  | Equipment/Assets / General Information |
| Notes | `Description` | `sTYPE_TEXTAREA` | Global | No | No |  | Equipment/Assets / General Information |
| PM Frequency | `CodePMFrequencyUnitID` | `sCODE_FREQUENCY_UNIT` | Global | No | No |  | Equipment/Assets / General Information |
| PM Period | `PMPeriod` | `sTYPE_NUMBER` | Global | No | No |  | Equipment/Assets / General Information |
| Primary Vendor | `PrimaryVendorID` | `sTYPE_VENDOR` | Global | No | No |  | Equipment/Assets / General Information |
| Repair Remedy Allowed | `CodeRepairRemedyID` | `sCODE_MAINTENANCE_REMEDY` | Global | No | No |  | Equipment/Assets / General Information |
| Repair Remedy Time | `RepairMaximumRemedyDays` | `sTYPE_NUMBER` | Global | No | No |  | Equipment/Assets / General Information |
| Repair Responsible Contact | `RepairResponsiblePersonID` | `sTYPE_PERSON` | Global | No | No |  | Equipment/Assets / General Information |
| Repair Responsible Party | `CodeRepairPartyID` | `sCODE_RESPONSIBLE_PARTY` | Global | No | No |  | Equipment/Assets / General Information |
| Replacement Cost | `ReplacementCost` | `sTYPE_MONEY` | Global | No | No |  | Equipment/Assets / General Information |
| Replacement Remedy Allowed | `CodeReplacementRemedyID` | `sCODE_MAINTENANCE_REMEDY` | Global | No | No |  | Equipment/Assets / General Information |
| Replacement Remedy Time | `ReplacementMaximumRemedyDays` | `sTYPE_NUMBER` | Global | No | No |  | Equipment/Assets / General Information |
| Replacement Responsible Contact | `ReplacementResponsiblePersonID` | `sTYPE_PERSON` | Global | No | No |  | Equipment/Assets / General Information |
| Replacement Responsible Party | `CodeReplacementPartyID` | `sCODE_RESPONSIBLE_PARTY` | Global | No | No |  | Equipment/Assets / General Information |
| Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Equipment/Assets / General Information |
| Sales Person Name | `SalesPersonName` | `sTYPE_TEXT` | Global | No | No |  | Equipment/Assets / General Information |
| Secondary Vendor | `SecondaryVendorID` | `sTYPE_VENDOR` | Global | No | No |  | Equipment/Assets / General Information |
| Supplier | `SupplierVendorID` | `sTYPE_VENDOR` | Global | No | No |  | Equipment/Assets / General Information |
| System of Record | `BaseProvider` | `sTYPE_VALUES_PROVIDER` | Global | No | No |  | Equipment/Assets / General Information |
| UCC Expiration Date | `UCCExpirationDate` | `sTYPE_DATE` | Global | No | No |  | Equipment/Assets / General Information |
| UCC File Date | `UCCFileDate` | `sTYPE_DATE` | Global | No | No |  | Equipment/Assets / General Information |
| Vendor PO Number | `VendorPONumber` | `sTYPE_TEXT` | Global | No | No |  | Equipment/Assets / General Information |
| Warranty Begin Date | `WarrantyBeginDate` | `sTYPE_DATE` | Global | No | No |  | Equipment/Assets / General Information |
| Warranty Comments | `WarrantyComments` | `sTYPE_TEXTAREA` | Global | No | No |  | Equipment/Assets / General Information |
| Warranty End Date | `WarrantyEndDate` | `sTYPE_DATE` | Global | No | No |  | Equipment/Assets / General Information |
| Warranty Number | `WarrantyNumber` | `sTYPE_TEXT` | Global | No | No |  | Equipment/Assets / General Information |
| Warranty Vendor | `WarrantyVendorID` | `sTYPE_VENDOR` | Global | No | No |  | Equipment/Assets / General Information |
| Weight | `Weight` | `sTYPE_NUMBER` | Global | No | No |  | Equipment/Assets / General Information |
| Weight Unit | `CodeWeightUnitID` | `sCODE_WEIGHT_UNIT` | Global | No | No |  | Equipment/Assets / General Information |
| Width | `Width` | `sTYPE_NUMBER` | Global | No | No |  | Equipment/Assets / General Information |
| Personal Prop Tax Description | `PersonalPropTaxDescription` | `sTYPE_TEXTAREA` | Global | No | No |  | Statics / Hidden |
| Personal Prop Tax Frequency | `CodePersonalPropTaxFrequencyID` | `sCODE_MONTH_FREQUENCY` | Global | No | No |  | Statics / Hidden |
| Personal Prop Tax Rate | `PersonalPropTaxRate` | `sTYPE_PERCENTAGE` | Global | No | No |  | Statics / Hidden |
| Move Asset | `MOVE_ASSET` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
