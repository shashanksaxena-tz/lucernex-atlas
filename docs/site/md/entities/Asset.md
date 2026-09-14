# Asset

*122 fields · module: Assets, Equipment & Maintenance · Postgres: `asset`*

The fixed-asset/ROU-asset record tied to a lease or equipment contract — accounting begin/end dates, discount rate overrides, depreciation dates, sale price, and current payment amounts. 126 fields, entirely Global, spanning Equipment/Assets, Statics, and Summary Information, reflecting that an Asset is simultaneously an accounting construct (depreciation, discount rate), a physical-equipment record, and a portfolio summary line.

Source: `data-fields/asset.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 122 |
| Fields with a vendor definition | 117 of 122 inventoried |
| Physical tables | `asset` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 126 (126 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 14 keys from 13 record types |
| Points at | 11 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 14 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in asset

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 117 fields carry a vendor definition

**Observed.** 117 of this record's 122 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one source in the corpus that explains fields rather than listing them.

### 2 fields marked required

**Observed.** The inventory marks 2 of this record's fields Required. Across the whole inventory that is 606 fields, which independently corroborates the 603 the corpus had derived from the Data Fields catalogue — two sources, arrived at separately, agreeing to within three.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [ACC-R-003](../rules/ACC-R-003.md) | if populated, it supersedes ACC-R-001/002 for that asset | Observed |
| [ACC-R-012](../rules/ACC-R-012.md) | if populated, the override supersedes the computed `CodeAccountingMethodID` | Derived |
| [ACC-R-018](../rules/ACC-R-018.md) | if the override dates are populated they set the test/schedule window; otherwise the window comes from the expense schedule dates | Observed |
| [ACC-R-032](../rules/ACC-R-032.md) | discount the cash payment from the period it is made back to the accounting begin date | Observed |
| [ACC-R-048](../rules/ACC-R-048.md) | `TotalImpairmentImpact = ImpairmentAmount + PriorAccumulatedAmortizationBalance`, where `PriorAccumulatedAmortizationBalance` is "the Accumulated Amortization Balance of the accounting period prior to the impairment." | Observed |
| [ACC-R-061](../rules/ACC-R-061.md) | the form type declares attachability as a Boolean per entity kind. For this form type, only `Portfolio` = Yes and `RE Contract` = Yes; `Capital Program`, `Prototype`, `Location`, `Parcel`, `Site`, `Project`, `Facility`, `Capital Project` an | Observed |
| [ACC-R-062](../rules/ACC-R-062.md) | all three ASC 842 steps use `Member` — a named approver, resolved at configuration time rather than by org-chart position | Observed |
| [AST-R-001](../rules/AST-R-001.md) | Trigger: N/A (structural). Input: `Asset.ProjectEntityID`, the only entity-scoping column on `Asset`. | Observed |
| [AST-R-002](../rules/AST-R-002.md) | Input: `Asset.AssociatedProjectEntityID`, typed the soft `Entity` type (not `Entity ID`). Effect: Distinct from the primary `ProjectEntityID` scope — allows an asset record to reference a second entity beyond the one it is scoped to. | Inferred |
| [AST-R-003](../rules/AST-R-003.md) | Input: `Asset.FinancialContractID`, typed `Contract ID`. Effect: Ties the asset to the equipment-flavour `Contract` that finances it, independent of the entity it is physically scoped to. | Observed |
| [AST-R-006](../rules/AST-R-006.md) | Input: `Asset.RemainingAssetBalance`, field type `sTYPE_PERCENT_OR_AMOUNT`. Effect: A value 0–100 is read as a percentage; | Observed |
| [AST-R-007](../rules/AST-R-007.md) | Input: `Asset.CodeAssetCategoryID` (labelled Maintenance Category) and `Asset.CodeDesc_CodeAssetCategoryID` (labelled Account #), both FKs to `CodeAssetCategory`. Effect: The same code table serves a maintenance-classification role and a GL | Observed |
| [AST-R-011](../rules/AST-R-011.md) | Input: `Asset.GenerateServiceRequest` and `ServiceRequest.GenerateWorkOrder`, both `sTYPE_SUBMITBUTTON`. Effect: A `ServiceRequest` is created from an `Asset`, and a `WorkOrder` from a `ServiceRequest`, only when a user presses the correspo | Observed |
| [AST-R-016](../rules/AST-R-016.md) | Input: `AssetHistory.ProjectEntityID` and `.FromProjectEntityID`, both typed the soft `Entity` type rather than the hard `Entity ID` type. Effect: The object behaves as an entity-scoped snapshot of an `Asset`'s state, but escapes the mechan | Derived |

## Fields

### Relationships (foreign keys) (9)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AlternateVendorID` | Alternate Vendor | Select the alternate vendor associated with the asset from this field. | Employer ID | Global |  | `asset.AlternateVendorID · TEXT` | [Employer](Employer.md) |
| `FinancialContractID` | Financial Contract | Select the associated equipment contract from this field. | Contract ID | Global |  | `asset.FinancialContractID · TEXT` | [Contract](Contract.md) |
| `InstallerVendorID` | Installer | Select the vendor who installed the asset from this field. | Employer ID | Global |  | `asset.InstallerVendorID · TEXT` | [Employer](Employer.md) |
| `ManufacturerVendorID` | Manufacturer | Select the manufacturer from this field. | Employer ID | Global |  | `asset.ManufacturerVendorID · TEXT` | [Employer](Employer.md) |
| `PrimaryVendorID` | Primary Vendor | Select the primary vendor from this field. | Employer ID | Global |  | `asset.PrimaryVendorID · TEXT` | [Employer](Employer.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `asset.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `SecondaryVendorID` | Secondary Vendor | Select the secondary vendor from this field. | Employer ID | Global |  | `asset.SecondaryVendorID · TEXT` | [Employer](Employer.md) |
| `SupplierVendorID` | Supplier | Select the supplier of the asset from this field. | Employer ID | Global |  | `asset.SupplierVendorID · TEXT` | [Employer](Employer.md) |
| `WarrantyVendorID` | Warranty Vendor | Select the warranty provider from this field. | Employer ID | Global |  | `asset.WarrantyVendorID · TEXT` | [Employer](Employer.md) |

### Soft references (4)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AssociatedProjectEntityID` | Associated Entity | The value that appears in the Associated Entity field is the equipment contract associated with the asset. | Entity | Global |  | `asset.AssociatedProjectEntityID · TEXT` |  |
| `MaintenanceResponsiblePersonID` | Maintenance Responsible Contact | Select the person responsible for maintenance from this field. | Contact | Global |  | `asset.MaintenanceResponsiblePersonID · TEXT` |  |
| `RepairResponsiblePersonID` | Repair Responsible Contact | Select the person responsible for repairs from this field. | Contact | Global |  | `asset.RepairResponsiblePersonID · TEXT` |  |
| `ReplacementResponsiblePersonID` | Replacement Responsible Contact | Select the person responsible for replacements from this field. | Contact | Global |  | `asset.ReplacementResponsiblePersonID · TEXT` |  |

### Coded values (drop-downs) (21)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeAccountingMethodOverrideID` | Accounting Method Override | If you want to override the accounting method for your asset, select the accounting method you want to use from this field. | Dropdown (Accounting Method Code) | Global |  | `asset.CodeAccountingMethodOverrideID · TEXT` | Accounting Method Code |
| `CodeAssetCategoryID` | Maintenance Category | Select the maintenance category of the asset from this field. | Dropdown (Asset Category Code) | Global |  | `asset.CodeAssetCategoryID · TEXT` | Asset Category Code |
| `CodeAssetDepartmentID` | Asset Department | Select the asset department from this field. | Dropdown (Asset Department Code) | Global |  | `asset.CodeAssetDepartmentID · TEXT` | Asset Department Code |
| `CodeAssetGroupID` | Asset Group | The asset group is the first level of categorization for assets. Groups are the parents of types. | Dropdown (Asset Group Code) | Global |  | `asset.CodeAssetGroupID · TEXT` | Asset Group Code |
| `CodeAssetOperationStatusID` | Asset Operation Status | Select the operational status of the asset from this field. | Dropdown (Asset Operation Status Code) | Global |  | `asset.CodeAssetOperationStatusID · TEXT` | Asset Operation Status Code |
| `CodeAssetProductTypeID` | Asset Product Type | Select the asset product type from this field. | Dropdown (Asset Product Type Code) | Global |  | `asset.CodeAssetProductTypeID · TEXT` | Asset Product Type Code |
| `CodeAssetSuspensionStatusID` | Asset Suspension Status | Select the asset suspension status from this field. | Dropdown (Asset Suspension Status Code) | Global |  | `asset.CodeAssetSuspensionStatusID · TEXT` | Asset Suspension Status Code |
| `CodeAssetTypeID` | Asset Type | The asset group is the second level of categorization for assets. Types are the children of groups. | Dropdown (Asset Type Code) | Global |  | `asset.CodeAssetTypeID · TEXT` | Asset Type Code |
| `CodeCompoundingFrequencyID` | Compounding Frequency | Select the compounding frequency from this field. | Dropdown (Frequency Code) | Global |  | `asset.CodeCompoundingFrequencyID · TEXT` | Frequency Code |
| `CodeDesc_CodeAssetCategoryID` | Account # | This field displays the name of the asset category. | Dropdown (Asset Category Code) | Global |  | `asset.CodeDesc_CodeAssetCategoryID · TEXT` | Asset Category Code |
| `CodeDimensionUnitID` | Dimension Unit | Select the dimension unit from this field. | Dropdown (Measurement Unit Code) | Global |  | `asset.CodeDimensionUnitID · TEXT` | Measurement Unit Code |
| `CodeInsuranceTermUnitID` | Insurance Term Unit | Select a term unit from this field. A term unit could be days, weeks, months, or years. | Dropdown (Time Unit Code) | Global |  | `asset.CodeInsuranceTermUnitID · TEXT` | Time Unit Code |
| `CodeMaintenancePartyID` | Maintenance Responsible Party | Select the party responsible for preventative maintenance from this field. | Dropdown (Responsible Party) | Global |  | `asset.CodeMaintenancePartyID · TEXT` | Responsible Party |
| `CodeMaintenanceRemedyID` | Maintenance Remedy Allowed | Select the preventative maintenance allowed from this field. | Dropdown (Maintenance Remedy Code) | Global |  | `asset.CodeMaintenanceRemedyID · TEXT` | Maintenance Remedy Code |
| `CodePMFrequencyUnitID` | PM Frequency | Select the frequency of preventative maintenance from this field. | Dropdown (Frequency Unit Code) | Global |  | `asset.CodePMFrequencyUnitID · TEXT` | Frequency Unit Code |
| `CodeRemainingLifeFreqUnitID` | Remaining Life Freq Unit | Select the unit used to measure the remaining economic life of the asset from this field. Example units include days, weeks, months, and years. | Dropdown (Frequency Unit Code) | Global |  | `asset.CodeRemainingLifeFreqUnitID · TEXT` | Frequency Unit Code |
| `CodeRepairPartyID` | Repair Responsible Party | Select the party responsible for repairs from this field. | Dropdown (Responsible Party) | Global |  | `asset.CodeRepairPartyID · TEXT` | Responsible Party |
| `CodeRepairRemedyID` | Repair Remedy Allowed | Select the repairs allowed from this field. | Dropdown (Maintenance Remedy Code) | Global |  | `asset.CodeRepairRemedyID · TEXT` | Maintenance Remedy Code |
| `CodeReplacementPartyID` | Replacement Responsible Party | Select the party responsible for replacing this asset from this field. | Dropdown (Responsible Party) | Global |  | `asset.CodeReplacementPartyID · TEXT` | Responsible Party |
| `CodeReplacementRemedyID` | Replacement Remedy Allowed | Select the replacements allowed from this field. | Dropdown (Maintenance Remedy Code) | Global |  | `asset.CodeReplacementRemedyID · TEXT` | Maintenance Remedy Code |
| `CodeWeightUnitID` | Weight Unit | Select the weight measurement unit from this field. | Dropdown (Weight Unit Code) | Global |  | `asset.CodeWeightUnitID · TEXT` | Weight Unit Code |

### Money (12)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AssetSalePrice` | Asset Sale Price | Enter the sale price of the asset in this field. | Currency | Global |  | `asset.AssetSalePrice · TEXT` |  |
| `CurrentAnnualPayment` | Current Annual Payment | Calculates your current annual payment for the asset. | Currency | Global |  | `asset.CurrentAnnualPayment · TEXT` |  |
| `CurrentMonthlyPayment` | Current Monthly Payment | Calculates your current monthly payment for the asset. | Currency | Global |  | `asset.CurrentMonthlyPayment · TEXT` |  |
| `FairValueOfAsset` | Fair Value Of Asset | Enter the fair value of the asset into this field. FASB 842.10.20 defines fair value as the price that would be received to sell an asset or paid to transfer a liability in an orderly transaction between market participants at the measurement date. | Currency | Global |  | `asset.FairValueOfAsset · TEXT` |  |
| `FinalAssetAmount` | Final Asset Amount |  | Currency | Global |  | `asset.FinalAssetAmount · TEXT` |  |
| `ImpairmentOverride` | Impairment Override Amount | Enter any deductions related to the diminished value of the asset as a negative number. | Currency | Global |  | `asset.ImpairmentOverride · TEXT` |  |
| `InitialAssetBalanceAdjust` | Initial Asset Balance Adjustment | Enter any adjustments to the initial asset balance in this field. | Currency | Global |  | `asset.InitialAssetBalanceAdjust · TEXT` |  |
| `InitialLiabilityBalanceAdjust` | Initial Liability Balance Adjustment | Enter any adjustments to the initial liability balance in this field. | Currency | Global |  | `asset.InitialLiabilityBalanceAdjust · TEXT` |  |
| `PurchasePrice` | Purchase Price | Enter the purchase price in this field. | Currency | Global |  | `asset.PurchasePrice · TEXT` |  |
| `ReplacementCost` | Replacement Cost | Enter the replacement cost in this field. | Currency | Global |  | `asset.ReplacementCost · TEXT` |  |
| `Residual` |  | Enter the estimated value of the asset at the end of the lease. | Currency | Global |  | `asset.Residual · TEXT` |  |
| `StartingDepreciationCost` | Starting Depreciation Cost | If the asset will depreciate at a different rate within the first year, enter a flag for indicating additional first year depreciation, or enter the first year depreciation amount in this field. | Currency | Global |  | `asset.StartingDepreciationCost · TEXT` |  |

### Rates & percentages (4)

Percentage inputs and computed rates.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DiscountRateOverride` | Discount Rate Override | If this equipment uses a different discount rate, enter the discount rate in this field. The discount rate is also known as the Interest Rate or the Internal Borrower Rate (IBR). | Percentage | Global |  | `asset.DiscountRateOverride · TEXT` |  |
| `FinalAssetAllocPercent` | Final Asset Amount Allocation Percentage |  | Percentage | Global |  | `asset.FinalAssetAllocPercent · TEXT` |  |
| `FirstYearBonusDepreciation` | First Year Bonus Depreciation | If the asset will depreciate at a different rate within the first year, enter a flag for indicating additional first year depreciation, or enter the first year depreciation amount in this field. | Percentage | Global |  | `asset.FirstYearBonusDepreciation · TEXT` |  |
| `PortionOfAssetControlled` | Portion Of Asset Controlled | Enter the portion of the asset you control in this field. | Percentage | Global |  | `asset.PortionOfAssetControlled · TEXT` |  |

### Quantities (13)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AssetID` | Asset RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `asset.AssetID · VARCHAR(64) NOT NULL` |  |
| `Depth` |  | Enter the depth of the asset in this field. | Number | Global |  | `asset.Depth · TEXT` |  |
| `Height` |  | Enter the height of the asset in this field. | Number | Global |  | `asset.Height · TEXT` |  |
| `InsuranceTerm` | Insurance Term | Enter the insurance term in this field. This value should be a numerical value that is paired with a term unit. A term unit could be days, weeks, months, or years. | Number | Global |  | `asset.InsuranceTerm · TEXT` |  |
| `LOAMonths` | LOA Months | Enter the life of the asset in months in this field. | Number | Global |  | `asset.LOAMonths · TEXT` |  |
| `MaintenanceMaximumRemedyDays` | Maintenance Remedy Time | Enter the maximum number of days allowed after a preventative maintenance request has been made. | Number | Global |  | `asset.MaintenanceMaximumRemedyDays · TEXT` |  |
| `PMPeriod` | PM Period | Enter the preventative maintenance period in this field. | Number | Global |  | `asset.PMPeriod · TEXT` |  |
| `RemainingLife` | Remaining Life | Enter the numerical value of the remaining economic life of the asset in this field. | Number | Global |  | `asset.RemainingLife · TEXT` |  |
| `RepairMaximumRemedyDays` | Repair Remedy Time | Enter the maximum number of days allowed after a repair request has been made. | Number | Global |  | `asset.RepairMaximumRemedyDays · TEXT` |  |
| `ReplacementMaximumRemedyDays` | Replacement Remedy Time | Enter the maximum number of days allowed after a replacement request has been made. | Number | Global |  | `asset.ReplacementMaximumRemedyDays · TEXT` |  |
| `Weight` |  | Enter the asset weight in this field. | Number | Global |  | `asset.Weight · TEXT` |  |
| `Width` |  | Enter the asset width in this field. | Number | Global |  | `asset.Width · TEXT` |  |
| `YearsOfDepreciableLife` | Years Of Depreciable Life | Enter the number of years the asset will be usable in this field. | Number | Global |  | `asset.YearsOfDepreciableLife · TEXT` |  |

### Dates & timestamps (19)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AccountingBeginDate` | Accounting Begin Date | If applicable, enter the accounting begin date override in this field. The purpose of this field is to change the dates that the test and rent schedules will be run for. If you do not enter override dates, the test and schedules will run based on the dates of the expense schedules for the asset. | Date | Global |  | `asset.AccountingBeginDate · TEXT` |  |
| `AccountingEndDate` | Accounting End Date | If applicable, enter the accounting begin date override in this field. The purpose of this field is to change the dates that the test and rent schedules will be run for. If you do not enter override dates, the test and schedules will run based on the dates of the expense schedules for the asset. | Date | Global |  | `asset.AccountingEndDate · TEXT` |  |
| `DepreciationEndDate` | Depreciation End Date | Enter the depreciation end date in this field. | Date | Global |  | `asset.DepreciationEndDate · TEXT` |  |
| `DispositionDate` | Disposition Date | Enter the date the asset was sold in this field. | Date | Global |  | `asset.DispositionDate · TEXT` |  |
| `FinalAssetDate` | Final Asset Amount Date |  | Date | Global |  | `asset.FinalAssetDate · TEXT` |  |
| `InServiceDate` | In-Service Date | Enter the date this asset was brought into service in this field. | Date | Global |  | `asset.InServiceDate · TEXT` |  |
| `InstallationDate` | Installation Date | Enter the asset installation date in this field. | Date | Global |  | `asset.InstallationDate · TEXT` |  |
| `InsuranceAlertDate` | Insurance Alert Date | Enter the insurance alert date for the asset in this field. | Date | Global |  | `asset.InsuranceAlertDate · TEXT` |  |
| `InsuranceBeginDate` | Insurance Begin Date | Enter the begin date of the insurance policy in this field. | Date | Global |  | `asset.InsuranceBeginDate · TEXT` |  |
| `InsuranceEndDate` | Insurance End Date | Enter the end date of the insurance policy in this field. | Date | Global |  | `asset.InsuranceEndDate · TEXT` |  |
| `InsuranceTicklerDate` | Insurance Tickler Date | Enter a tickler date in this field. A tickler is a date a certain amount of time prior to something becoming due. Clients often use these dates in reports. | Date | Global |  | `asset.InsuranceTicklerDate · TEXT` |  |
| `MoveInDate` | Move In Date | Enter the installation date of the asset in this field. | Date | Global |  | `asset.MoveInDate · TEXT` |  |
| `PaymentsBeginDate` | Payments Begin Date | The payment begin date for the asset. | Date | Global |  | `asset.PaymentsBeginDate · TEXT` |  |
| `PaymentsEndDate` | Payments End Date | The payment end date for the asset. | Date | Global |  | `asset.PaymentsEndDate · TEXT` |  |
| `PurchaseDate` | Purchase Date | Enter the purchase date of the asset in this field. | Date | Global |  | `asset.PurchaseDate · TEXT` |  |
| `UCCExpirationDate` | UCC Expiration Date | Enter the date when the UCC filing was originally going to expire in this field. | Date | Global |  | `asset.UCCExpirationDate · TEXT` |  |
| `UCCFileDate` | UCC File Date | Enter the origination date of the UCC filing in this field. | Date | Global |  | `asset.UCCFileDate · TEXT` |  |
| `WarrantyBeginDate` | Warranty Begin Date | Enter the warranty begin date in this field. | Date | Global |  | `asset.WarrantyBeginDate · TEXT` |  |
| `WarrantyEndDate` | Warranty End Date | Enter the warranty end date in this field. | Date | Global |  | `asset.WarrantyEndDate · TEXT` |  |

### Flags (7)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DoesTitleRevertToTenant` | Does Ownership Revert To Tenant? | Select this check box if the ownership of the asset reverts to the tenant at the termination of the lease term. | Boolean | Global |  | `asset.DoesTitleRevertToTenant · TEXT` |  |
| `HasBuyoutOption` | Has Buyout Option? | Select this check box if you have the option to buy the asset at the end of the lease term. | Boolean | Global |  | `asset.HasBuyoutOption · TEXT` |  |
| `IsAssetTooSpecializedForLessor` | Is Asset Too Specialized For Lessor? | Select this check box if the asset has a specialized use, such that the lessor will have no alternative use for it. | Boolean | Global |  | `asset.IsAssetTooSpecializedForLessor · TEXT` |  |
| `IsLowAssetValue` | Is Low Asset Value | Select this check box if the asset is low value. | Boolean | Global |  | `asset.IsLowAssetValue · TEXT` |  |
| `IsShortTerm` | Is Short Term | Select this check box if this asset is short-term. | Boolean | Global |  | `asset.IsShortTerm · TEXT` |  |
| `MonthToMonth` | Month To Month? | If the equipment payment is going to be month-to-month, select this check box. | Boolean | Global |  | `asset.MonthToMonth · TEXT` |  |
| `PlanToBuyAtEndOfTerm` | Plan To Buy At End Of Term? | Select this check box if you plan to buy the asset at the end of the lease term. | Boolean | Global |  | `asset.PlanToBuyAtEndOfTerm · TEXT` |  |

### Text & notes (25)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AssetBarcodeNumber` | Asset Barcode Number | Enter the asset barcode number in this field. | Text | Global |  | `asset.AssetBarcodeNumber · TEXT` |  |
| `AssetName` | Equipment Name | Enter the asset name in this field. | Text | Global | yes | `asset.AssetName · TEXT` |  |
| `AssetSerialNumber` | Asset Serial # | Enter the asset serial number in this field. | Text | Global |  | `asset.AssetSerialNumber · TEXT` |  |
| `BaseProvider` | System of Record | This field is used to fetch a record value from another Accruent software. | Text | Global |  | `asset.BaseProvider · TEXT` |  |
| `ClientNumber` | Asset Number | Enter the asset number in this field. | Text | Global |  | `asset.ClientNumber · TEXT` |  |
| `Color` |  | Enter the asset's color in this field. | Text | Global |  | `asset.Color · TEXT` |  |
| `Description` | Notes | Write a description of the record. | Text | Global |  | `asset.Description · TEXT` |  |
| `ExpectedLife` | Expected Life | Enter any notes about the expected life in this field. | Text | Global |  | `asset.ExpectedLife · TEXT` |  |
| `FairValueSource` | Fair Value Source | Enter the name of the person who assessed the fair value of the asset in this field. | Text | Global |  | `asset.FairValueSource · TEXT` |  |
| `Floor` |  | Enter the floor where the asset is located in this field. | Text | Global |  | `asset.Floor · TEXT` |  |
| `InsuranceAgent` | Insurance Agent | Enter the name of the insurance agent in this field. | Text | Global |  | `asset.InsuranceAgent · TEXT` |  |
| `InsurancePolicyNumber` | Insurance Policy Number | Enter the insurance policy number for the asset in this field. | Text | Global |  | `asset.InsurancePolicyNumber · TEXT` |  |
| `IntegrationAssetStatus` | Integration Asset Status | The status of an asset that has been included in an integration between two Accruent products. For example, this field could be used to capture the status of an asset that is shared between Siterra and Lx. | Text | Global |  | `asset.IntegrationAssetStatus · TEXT` |  |
| `LeaseSection` | Lease Section | This field can be used to capture the section of the lease the asset is referenced in. | Text | Global |  | `asset.LeaseSection · TEXT` |  |
| `LocationDetails` | Location Details | Enter any additional information about the location of the asset in this field. | Text | Global |  | `asset.LocationDetails · TEXT` |  |
| `Make` |  | Enter the brand of the asset in this field. | Text | Global |  | `asset.Make · TEXT` |  |
| `ModelNumber` | Model # | Enter the model number in this field. | Text | Global |  | `asset.ModelNumber · TEXT` |  |
| `PurchaseOrderDescrption` | Purchase Order Descrption | Enter a description of the purchase order for the asset in this field. | Text | Global |  | `asset.PurchaseOrderDescrption · TEXT` |  |
| `PurchaseOrderNumber` | Purchase Order Number | Enter the purchase order number in this field. | Text | Global |  | `asset.PurchaseOrderNumber · TEXT` |  |
| `PurchaseOrderReference` | Purchase Order Reference | Enter any reference number for the purchase order for the asset in this field. | Text | Global |  | `asset.PurchaseOrderReference · TEXT` |  |
| `ResponsibilityID` | Contract Responsibility | Select the contract the asset should be associated with from this field. | Text | Global |  | `asset.ResponsibilityID · TEXT` |  |
| `SalesPersonName` | Sales Person Name | Enter the name of the salesperson who assisted with the purchase order in this field. | Text | Global |  | `asset.SalesPersonName · TEXT` |  |
| `VendorPONumber` | Vendor PO Number | Enter the vendor purchase order number in this field. | Text | Global |  | `asset.VendorPONumber · TEXT` |  |
| `WarrantyComments` | Warranty Comments | Enter any comments about the warranty in this field. | Text | Global |  | `asset.WarrantyComments · TEXT` |  |
| `WarrantyNumber` | Warranty Number | Enter the warranty number in this field. | Text | Global |  | `asset.WarrantyNumber · TEXT` |  |

### Audit & record keeping (7)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Asset ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `asset.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `asset.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `asset.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `asset.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `asset.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | `asset.RevNumber · TEXT` |  |
| `UUID` | Asset UUID | This field captures a unique identifier associated with your record. This identifier is used if you are using an integration with other Accruent products. | Text | Global |  | `asset.UUID · TEXT` |  |

### Other (1)

Everything that did not fall into a named group.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `RemainingAssetBalance` | Remaining Asset Balance |  | Percent or Currency | Global |  | `asset.RemainingAssetBalance · TEXT` |  |

## What points here (14 keys)

| Record type | Via column |
|---|---|
| [Issue](Issue.md) | `EquipmentID`, `EquipmentIDList` |
| [AssetHistory](AssetHistory.md) | `AssetID` |
| [CLRExtensionPart](CLRExtensionPart.md) | `AssetID` |
| [ClientListRow](ClientListRow.md) | `AssetID` |
| [ContractFinancialTest](ContractFinancialTest.md) | `AssetID` |
| [ExpenseAllocation](ExpenseAllocation.md) | `AssetID` |
| [ExpenseSchedule](ExpenseSchedule.md) | `AssetID` |
| [FinancialAdjustment](FinancialAdjustment.md) | `AssetID` |
| [LinkIssuePart](LinkIssuePart.md) | `AssetID` |
| [PaymentTransaction](PaymentTransaction.md) | `AssetID` |
| [PaymentTransactionFullImport](PaymentTransactionFullImport.md) | `AssetID` |
| [SLPeriod](SLPeriod.md) | `AssetID` |
| [SLSummary](SLSummary.md) | `AssetID` |
