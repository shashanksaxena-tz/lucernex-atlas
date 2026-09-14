# Assets, Equipment & Maintenance

*In scope for the rebuild*

The asset register and the reactive-maintenance loop: service requests, work orders and the parts catalogue that feeds them.

Stated up front. This module is three unrelated concerns sharing one dashboard heading (Portfolio Administration): 8 objects, 230 fields. Asset (122 fields, entity_scoped) is the fixed-asset/equipment record and by far the largest object here — and it is not a passive piece of equipment that a lease merely references. It carries its own copy of the ASC 842/IFRS 16 classification-test surface (FairValueOfAsset, DiscountRateOverride, IsAssetTooSpecializedForLessor, IsLowAssetValue, IsShortTerm, HasBuyoutOption, PlanToBuyAtEndOfTerm, DoesTitleRevertToTenant, InitialAssetBalanceAdjust, InitialLiabilityBalanceAdjust, ImpairmentOverride, Residual, YearsOfDepreciableLife), and ContractFinancialTest, SLSummary and SLPeriod — the same tables the accounting module built around Contract — each carry a separate, nullable, direct FK back to Asset. The accounting engine runs per equipment asset, not only per lease. Full argument: equipment-leases.md.

|  | Count |
|---|---|
| Record types | 8 |
| Fields | 230 |
| Keys in | 13 |
| Keys out | 29 |
| Rules | 16 |

## Record types

| Record type | Postgres table | Fields | Referenced by |
|---|---|---|---|
| [Asset](../entities/Asset.md) | `asset` | 122 | 14 |
| [ServiceRequest](../entities/ServiceRequest.md) | `service_request` | 30 | 0 |
| [WorkOrder](../entities/WorkOrder.md) | `work_order` | 30 | 0 |
| [Part](../entities/Part.md) | `part` | 16 | 0 |
| [AssetHistory](../entities/AssetHistory.md) | `asset_history` | 13 | 0 |
| [PartPackageItem](../entities/PartPackageItem.md) | `part_package_item` | 7 | 0 |
| [CodeAssetCategory](../entities/CodeAssetCategory.md) | `code_asset_category` | 6 | 0 |
| [PartPackage](../entities/PartPackage.md) | `part_package` | 6 | 0 |

## Rules

| Rule | Subject | What it requires | Confidence |
|---|---|---|---|
| [AST-R-001](../rules/AST-R-001.md) | An Asset attaches to any `ProjectEntity`, not only to a Facility | Trigger: N/A (structural). Input: `Asset.ProjectEntityID`, the only entity-scoping column on `Asset`. | Observed |
| [AST-R-002](../rules/AST-R-002.md) | An Asset may carry a second, independent soft pointer | Input: `Asset.AssociatedProjectEntityID`, typed the soft `Entity` type (not `Entity ID`). Effect: Distinct from the primary `ProjectEntityID` scope — allows an asset record to reference a second entit | Inferred |
| [AST-R-003](../rules/AST-R-003.md) | An Asset's equipment lease is a hard, typed FK | Input: `Asset.FinancialContractID`, typed `Contract ID`. Effect: Ties the asset to the equipment-flavour `Contract` that finances it, independent of the entity it is physically scoped to. | Observed |
| [AST-R-004](../rules/AST-R-004.md) | Asset carries its own ASC 842/IFRS 16 classification overlay, parallel to Contract's | Input: The 13-field block enumerated in `data-model.md` and detailed in `equipment-leases.md`. Effect: Equipment-lease classification can run per asset, using asset-supplied inputs, rather than only a | Observed |
| [AST-R-005](../rules/AST-R-005.md) | `Asset.AccountingBeginDate`/`AccountingEndDate` override the derived accounting window | Input: The two override fields. Effect: When populated, replace the accounting window that would otherwise be derived from the asset's `ExpenseSchedule` rows. | Derived |
| [AST-R-006](../rules/AST-R-006.md) | `RemainingAssetBalance` is magnitude-typed on Asset, exactly as on SLSummary | Input: `Asset.RemainingAssetBalance`, field type `sTYPE_PERCENT_OR_AMOUNT`. Effect: A value 0–100 is read as a percentage; | Observed |
| [AST-R-007](../rules/AST-R-007.md) | Two independent code-table lookups on Asset resolve to the same table, for different UI roles | Input: `Asset.CodeAssetCategoryID` (labelled Maintenance Category) and `Asset.CodeDesc_CodeAssetCategoryID` (labelled Account #), both FKs to `CodeAssetCategory`. Effect: The same code table serves a  | Observed |
| [AST-R-008](../rules/AST-R-008.md) | An Asset Category code-table row is a GL routing decision, not a plain label | Input: `CodeAssetCategory.GLNumber`, `.SubAccount`, `.DNEAmount`, alongside `ShortName`/ `ActualLongName`/`Inactive`. Effect: Selecting an asset category also selects a GL account, a sub-account, and  | Observed |
| [AST-R-009](../rules/AST-R-009.md) | Asset carries three parallel maintenance-SLA blocks: Maintenance, Repair, Replacement | Input: For each of the three event types, a `Code{X}PartyID` (Responsible Party code), `{X}ResponsiblePersonID` (a `Person` contact), `Code{X}RemedyID` (a Maintenance Remedy code), and `{X}MaximumReme | Observed |
| [AST-R-010](../rules/AST-R-010.md) | Asset's vendor roles reuse Employer, seven ways | Input: `AlternateVendorID`, `InstallerVendorID`, `ManufacturerVendorID`, `PrimaryVendorID`, `SecondaryVendorID`, `SupplierVendorID`, `WarrantyVendorID` — all typed `Employer ID`. Effect: Seven distinc | Observed |
| [AST-R-011](../rules/AST-R-011.md) | The maintenance loop is generated by buttons, not an automatic cascade | Input: `Asset.GenerateServiceRequest` and `ServiceRequest.GenerateWorkOrder`, both `sTYPE_SUBMITBUTTON`. Effect: A `ServiceRequest` is created from an `Asset`, and a `WorkOrder` from a `ServiceRequest | Observed |
| [AST-R-012](../rules/AST-R-012.md) | ServiceRequest and WorkOrder are each themselves `Issue` variants | Input: `ServiceRequest.IssueID` and `WorkOrder.IssueID`, both `Required = Yes`, field type `sTYPE_ISSUE`. Effect: Each row of `ServiceRequest`/`WorkOrder` is paired 1:1 with an underlying `Issue` reco | Observed |
| [AST-R-013](../rules/AST-R-013.md) | WorkOrder's link to ServiceRequest is optional, unlike its link to Issue | Input: `WorkOrder.ServiceRequestID`, field type `sTYPE_SERVICE_REQUEST`, `Required = No`. Effect: A `WorkOrder` can exist with no parent `ServiceRequest`, even though the UI's normal generation path ( | Observed |
| [AST-R-014](../rules/AST-R-014.md) | Parts consumed against a job are recorded against the Issue, not the WorkOrder | Input: `LinkIssuePart.IssueID` + `.AssetID` (typed `Equipment ID`) + `.PartID` + `.Quantity` + `.CostPerPart` + `.TotalCost` + `.SerialNumber` — an object in the `projects-capital` module, not this on | Derived |
| [AST-R-015](../rules/AST-R-015.md) | The parts catalog carries no per-location stock | Input: `Part.QuantityOnHand`, `.QuantityOnOrder`, `.ParLevel`, `.OrderToLevel` — single counters on the catalog record, with no `FacilityID`/warehouse column anywhere in this module. Effect: A tenant  | Derived |
| [AST-R-016](../rules/AST-R-016.md) | `AssetHistory` is entity-scoped in practice despite its mechanical `firm_global` label | Input: `AssetHistory.ProjectEntityID` and `.FromProjectEntityID`, both typed the soft `Entity` type rather than the hard `Entity ID` type. Effect: The object behaves as an entity-scoped snapshot of an | Derived |
