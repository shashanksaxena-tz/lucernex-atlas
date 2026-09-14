# Asset

*122 fields · module: Assets, Equipment & Maintenance · Postgres: `asset`*

The fixed-asset/ROU-asset record tied to a lease or equipment contract — accounting begin/end dates, discount rate overrides, depreciation dates, sale price, and current payment amounts. 126 fields, entirely Global, spanning Equipment/Assets, Statics, and Summary Information, reflecting that an Asset is simultaneously an accounting construct (depreciation, discount rate), a physical-equipment record, and a portfolio summary line.

Source: `data-fields/asset.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 122 |
| Catalogued fields | 126 (126 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 14 keys from 13 record types |
| Points at | 11 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 14 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

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

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AlternateVendorID` | Alternate Vendor | Employer ID | Global |  | [Employer](Employer.md) |
| `FinancialContractID` | Financial Contract | Contract ID | Global |  | [Contract](Contract.md) |
| `InstallerVendorID` | Installer | Employer ID | Global |  | [Employer](Employer.md) |
| `ManufacturerVendorID` | Manufacturer | Employer ID | Global |  | [Employer](Employer.md) |
| `PrimaryVendorID` | Primary Vendor | Employer ID | Global |  | [Employer](Employer.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |
| `SecondaryVendorID` | Secondary Vendor | Employer ID | Global |  | [Employer](Employer.md) |
| `SupplierVendorID` | Supplier | Employer ID | Global |  | [Employer](Employer.md) |
| `WarrantyVendorID` | Warranty Vendor | Employer ID | Global |  | [Employer](Employer.md) |

### Soft references (4)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AssociatedProjectEntityID` | Associated Entity | Entity | Global |  |  |
| `MaintenanceResponsiblePersonID` | Maintenance Responsible Contact | Contact | Global |  |  |
| `RepairResponsiblePersonID` | Repair Responsible Contact | Contact | Global |  |  |
| `ReplacementResponsiblePersonID` | Replacement Responsible Contact | Contact | Global |  |  |

### Coded values (drop-downs) (21)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeAccountingMethodOverrideID` | Accounting Method Override | Dropdown (Accounting Method Code) | Global |  | Accounting Method Code |
| `CodeAssetCategoryID` | Maintenance Category | Dropdown (Asset Category Code) | Global |  | Asset Category Code |
| `CodeAssetDepartmentID` | Asset Department | Dropdown (Asset Department Code) | Global |  | Asset Department Code |
| `CodeAssetGroupID` | Asset Group | Dropdown (Asset Group Code) | Global |  | Asset Group Code |
| `CodeAssetOperationStatusID` | Asset Operation Status | Dropdown (Asset Operation Status Code) | Global |  | Asset Operation Status Code |
| `CodeAssetProductTypeID` | Asset Product Type | Dropdown (Asset Product Type Code) | Global |  | Asset Product Type Code |
| `CodeAssetSuspensionStatusID` | Asset Suspension Status | Dropdown (Asset Suspension Status Code) | Global |  | Asset Suspension Status Code |
| `CodeAssetTypeID` | Asset Type | Dropdown (Asset Type Code) | Global |  | Asset Type Code |
| `CodeCompoundingFrequencyID` | Compounding Frequency | Dropdown (Frequency Code) | Global |  | Frequency Code |
| `CodeDesc_CodeAssetCategoryID` | Account # | Dropdown (Asset Category Code) | Global |  | Asset Category Code |
| `CodeDimensionUnitID` | Dimension Unit | Dropdown (Measurement Unit Code) | Global |  | Measurement Unit Code |
| `CodeInsuranceTermUnitID` | Insurance Term Unit | Dropdown (Time Unit Code) | Global |  | Time Unit Code |
| `CodeMaintenancePartyID` | Maintenance Responsible Party | Dropdown (Responsible Party) | Global |  | Responsible Party |
| `CodeMaintenanceRemedyID` | Maintenance Remedy Allowed | Dropdown (Maintenance Remedy Code) | Global |  | Maintenance Remedy Code |
| `CodePMFrequencyUnitID` | PM Frequency | Dropdown (Frequency Unit Code) | Global |  | Frequency Unit Code |
| `CodeRemainingLifeFreqUnitID` | Remaining Life Freq Unit | Dropdown (Frequency Unit Code) | Global |  | Frequency Unit Code |
| `CodeRepairPartyID` | Repair Responsible Party | Dropdown (Responsible Party) | Global |  | Responsible Party |
| `CodeRepairRemedyID` | Repair Remedy Allowed | Dropdown (Maintenance Remedy Code) | Global |  | Maintenance Remedy Code |
| `CodeReplacementPartyID` | Replacement Responsible Party | Dropdown (Responsible Party) | Global |  | Responsible Party |
| `CodeReplacementRemedyID` | Replacement Remedy Allowed | Dropdown (Maintenance Remedy Code) | Global |  | Maintenance Remedy Code |
| `CodeWeightUnitID` | Weight Unit | Dropdown (Weight Unit Code) | Global |  | Weight Unit Code |

### Money (12)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AssetSalePrice` | Asset Sale Price | Currency | Global |  |  |
| `CurrentAnnualPayment` | Current Annual Payment | Currency | Global |  |  |
| `CurrentMonthlyPayment` | Current Monthly Payment | Currency | Global |  |  |
| `FairValueOfAsset` | Fair Value Of Asset | Currency | Global |  |  |
| `FinalAssetAmount` | Final Asset Amount | Currency | Global |  |  |
| `ImpairmentOverride` | Impairment Override Amount | Currency | Global |  |  |
| `InitialAssetBalanceAdjust` | Initial Asset Balance Adjustment | Currency | Global |  |  |
| `InitialLiabilityBalanceAdjust` | Initial Liability Balance Adjustment | Currency | Global |  |  |
| `PurchasePrice` | Purchase Price | Currency | Global |  |  |
| `ReplacementCost` | Replacement Cost | Currency | Global |  |  |
| `Residual` |  | Currency | Global |  |  |
| `StartingDepreciationCost` | Starting Depreciation Cost | Currency | Global |  |  |

### Rates & percentages (4)

Percentage inputs and computed rates.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DiscountRateOverride` | Discount Rate Override | Percentage | Global |  |  |
| `FinalAssetAllocPercent` | Final Asset Amount Allocation Percentage | Percentage | Global |  |  |
| `FirstYearBonusDepreciation` | First Year Bonus Depreciation | Percentage | Global |  |  |
| `PortionOfAssetControlled` | Portion Of Asset Controlled | Percentage | Global |  |  |

### Quantities (13)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AssetID` | Asset RecID | Number | Global |  |  |
| `Depth` |  | Number | Global |  |  |
| `Height` |  | Number | Global |  |  |
| `InsuranceTerm` | Insurance Term | Number | Global |  |  |
| `LOAMonths` | LOA Months | Number | Global |  |  |
| `MaintenanceMaximumRemedyDays` | Maintenance Remedy Time | Number | Global |  |  |
| `PMPeriod` | PM Period | Number | Global |  |  |
| `RemainingLife` | Remaining Life | Number | Global |  |  |
| `RepairMaximumRemedyDays` | Repair Remedy Time | Number | Global |  |  |
| `ReplacementMaximumRemedyDays` | Replacement Remedy Time | Number | Global |  |  |
| `Weight` |  | Number | Global |  |  |
| `Width` |  | Number | Global |  |  |
| `YearsOfDepreciableLife` | Years Of Depreciable Life | Number | Global |  |  |

### Dates & timestamps (19)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AccountingBeginDate` | Accounting Begin Date | Date | Global |  |  |
| `AccountingEndDate` | Accounting End Date | Date | Global |  |  |
| `DepreciationEndDate` | Depreciation End Date | Date | Global |  |  |
| `DispositionDate` | Disposition Date | Date | Global |  |  |
| `FinalAssetDate` | Final Asset Amount Date | Date | Global |  |  |
| `InServiceDate` | In-Service Date | Date | Global |  |  |
| `InstallationDate` | Installation Date | Date | Global |  |  |
| `InsuranceAlertDate` | Insurance Alert Date | Date | Global |  |  |
| `InsuranceBeginDate` | Insurance Begin Date | Date | Global |  |  |
| `InsuranceEndDate` | Insurance End Date | Date | Global |  |  |
| `InsuranceTicklerDate` | Insurance Tickler Date | Date | Global |  |  |
| `MoveInDate` | Move In Date | Date | Global |  |  |
| `PaymentsBeginDate` | Payments Begin Date | Date | Global |  |  |
| `PaymentsEndDate` | Payments End Date | Date | Global |  |  |
| `PurchaseDate` | Purchase Date | Date | Global |  |  |
| `UCCExpirationDate` | UCC Expiration Date | Date | Global |  |  |
| `UCCFileDate` | UCC File Date | Date | Global |  |  |
| `WarrantyBeginDate` | Warranty Begin Date | Date | Global |  |  |
| `WarrantyEndDate` | Warranty End Date | Date | Global |  |  |

### Flags (7)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DoesTitleRevertToTenant` | Does Ownership Revert To Tenant? | Boolean | Global |  |  |
| `HasBuyoutOption` | Has Buyout Option? | Boolean | Global |  |  |
| `IsAssetTooSpecializedForLessor` | Is Asset Too Specialized For Lessor? | Boolean | Global |  |  |
| `IsLowAssetValue` | Is Low Asset Value | Boolean | Global |  |  |
| `IsShortTerm` | Is Short Term | Boolean | Global |  |  |
| `MonthToMonth` | Month To Month? | Boolean | Global |  |  |
| `PlanToBuyAtEndOfTerm` | Plan To Buy At End Of Term? | Boolean | Global |  |  |

### Text & notes (25)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AssetBarcodeNumber` | Asset Barcode Number | Text | Global |  |  |
| `AssetName` | Equipment Name | Text | Global | yes |  |
| `AssetSerialNumber` | Asset Serial # | Text | Global |  |  |
| `BaseProvider` | System of Record | Text | Global |  |  |
| `ClientNumber` | Asset Number | Text | Global |  |  |
| `Color` |  | Text | Global |  |  |
| `Description` | Notes | Text | Global |  |  |
| `ExpectedLife` | Expected Life | Text | Global |  |  |
| `FairValueSource` | Fair Value Source | Text | Global |  |  |
| `Floor` |  | Text | Global |  |  |
| `InsuranceAgent` | Insurance Agent | Text | Global |  |  |
| `InsurancePolicyNumber` | Insurance Policy Number | Text | Global |  |  |
| `IntegrationAssetStatus` | Integration Asset Status | Text | Global |  |  |
| `LeaseSection` | Lease Section | Text | Global |  |  |
| `LocationDetails` | Location Details | Text | Global |  |  |
| `Make` |  | Text | Global |  |  |
| `ModelNumber` | Model # | Text | Global |  |  |
| `PurchaseOrderDescrption` | Purchase Order Descrption | Text | Global |  |  |
| `PurchaseOrderNumber` | Purchase Order Number | Text | Global |  |  |
| `PurchaseOrderReference` | Purchase Order Reference | Text | Global |  |  |
| `ResponsibilityID` | Contract Responsibility | Text | Global |  |  |
| `SalesPersonName` | Sales Person Name | Text | Global |  |  |
| `VendorPONumber` | Vendor PO Number | Text | Global |  |  |
| `WarrantyComments` | Warranty Comments | Text | Global |  |  |
| `WarrantyNumber` | Warranty Number | Text | Global |  |  |

### Audit & record keeping (7)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Asset ClientID | Text | Global | yes |  |
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |
| `UUID` | Asset UUID | Text | Global |  |  |

### Other (1)

Everything that did not fall into a named group.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `RemainingAssetBalance` | Remaining Asset Balance | Percent or Currency | Global |  |  |

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
