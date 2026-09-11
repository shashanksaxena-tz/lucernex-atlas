# Assets, Equipment & Maintenance — data model

**Stated up front.** Eight objects, 230 fields, and the module splits cleanly into three unrelated
concerns wearing one name: **the asset register** (`Asset`, `AssetHistory`, `CodeAssetCategory`) —
122 of the 230 fields on `Asset` alone, and, non-obviously, **the same lease-accounting engine that
runs a real-estate `Contract` also runs against `Asset` directly** (§4); **the reactive-maintenance
loop** (`ServiceRequest`, `WorkOrder`) — a two-step ticket chain, each step generated from the one
before it by a UI button, and each step is itself an `Issue` variant, not a bespoke ticket type
(§3); and **the parts catalog** (`Part`, `PartPackage`, `PartPackageItem`) — a firm-wide, single-
location inventory list with no attachment to `ServiceRequest`/`WorkOrder` at all; parts actually
*consumed* against a job are tracked one module over, in `projects-capital`, against the underlying
`Issue` (§3.3).

Source: `_lucernex_objects_summary.txt` (**Observed**, field lists reproduced below), cross-checked
against [`../../mindmap/edges.json`](../../mindmap/edges.json) (**Derived** FK resolution) and,
where a per-entity Data Fields catalog exists, [`../../data-fields/`](../../data-fields/) — an
independently captured admin-screen source that in this module **diverges from the schema export
in a load-bearing way** (§3.2).

## 1. The object roster

| Object | PG table | Fields | Role | In/Out | Notes |
|---|---|---:|---|---:|---|
| `Asset` | `asset` | 122 | `entity_scoped` | 13 / 11 | The fixed-asset/ROU-asset/equipment record. Carries a full ASC 842/IFRS 16 classification overlay — see [`equipment-leases.md`](equipment-leases.md). |
| `AssetHistory` | `asset_history` | 13 | `firm_global` *(misclassified — see below)* | 0 / 3 | A point-in-time snapshot of an `Asset`'s financial state before a recalculation. |
| `CodeAssetCategory` | `code_asset_category` | 6 | `firm_global` | 0 / 0 | The asset-category code table — carries `GLNumber`/`SubAccount`/`DNEAmount`, a routing decision, not a plain lookup (§2.3). |
| `Part` | `part` | 16 | `firm_global` | 0 / 2 | A parts-catalog record — cost, manufacturer, reorder levels. No `ProjectEntityID` at all; not scoped to any entity or location. |
| `PartPackage` | `part_package` | 6 | `firm_global` | 0 / 2 | A named kit/bundle header above `PartPackageItem`. |
| `PartPackageItem` | `part_package_item` | 7 | `firm_global` | 0 / 1 | One `Part` line inside a `PartPackage` kit, with its own `Quantity`. |
| `ServiceRequest` | `service_request` | 30 | `entity_scoped` | 0 / 4 | The maintenance ticket — an `Issue` variant (§3.1). |
| `WorkOrder` | `work_order` | 30 | `entity_scoped` | 0 / 7 | The dispatched work resulting from a `ServiceRequest` — also an `Issue` variant (§3.1). |

**`AssetHistory`'s `firm_global` classification is a known false negative, not a real finding about
the object.** [`../../data-model/project-entity.md`](../../data-model/project-entity.md) §2 already
flagged it by name: `AssetHistory.ProjectEntityID` and `.FromProjectEntityID` are typed the **soft**
`Entity` type rather than the hard `Entity ID` type the mechanical role classifier looks for, so it
is scoped to an entity in reality and simply escapes the automated test. `Part`/`PartPackage`/
`PartPackageItem`, by contrast, carry **no `ProjectEntityID` column of any type** — they are
genuinely firm-wide, not a classifier miss. That is a real distinction the rebuild should preserve:
`AssetHistory` needs a tenant/entity scope column; the parts catalog does not.

## 2. `Asset` — the 122-field roster, grouped

**Observed**, full field list in `_lucernex_objects_summary.txt`. Grouped here by function; the
`Notes (Group/Subgroup)` column in [`../../data-fields/asset.md`](../../data-fields/asset.md)
confirms the platform itself groups them the same way, under two subgroups: *Financial Information*
and *General Information*.

| Group | Representative fields | Reading |
|---|---|---|
| Identity & audit | `AssetID`, `AssetName` (label: *Equipment Name*), `ClientNumber` (*Asset Number*), `UUID`, `BOMapClientRecordID`, `CreatedByID`/`CreatedDate`/`ModifiedByID`/`ModifiedDate`/`RevNumber` | Standard record scaffolding. `AssetName`'s UI label is **"Equipment Name"** — the schema says Asset, the UI says Equipment throughout (matches the Facility screen group "Equipment (FF&E)", [003](../../screens/003-main-navigation.md)). |
| Physical description | `AssetSerialNumber`, `AssetBarcodeNumber`, `Make`, `ModelNumber`, `Color`, `Weight`+`CodeWeightUnitID`, `Height`/`Width`/`Depth`/`Floor`+`CodeDimensionUnitID` | Straightforward asset-tag data. |
| Classification | `CodeAssetCategoryID`/`CodeDesc_CodeAssetCategoryID` (two separate FKs to the same code table, §2.3), `CodeAssetDepartmentID`, `CodeAssetGroupID`, `CodeAssetOperationStatusID`, `CodeAssetProductTypeID`, `CodeAssetSuspensionStatusID`, `CodeAssetTypeID` | Six independent classification axes on one record. |
| Vendor roles | `AlternateVendorID`, `InstallerVendorID`, `ManufacturerVendorID`, `PrimaryVendorID`, `SecondaryVendorID`, `SupplierVendorID`, `WarrantyVendorID` — all typed `Employer ID` | Seven distinct vendor *roles* against the same `Employer` table, reusing the landlord/tenant/vendor multiplexing [`../../modules/people-parties/member-vs-person-vs-party.md`](../../modules/people-parties/README.md) documents elsewhere. |
| Warranty & insurance | `WarrantyBeginDate`/`EndDate`/`Number`/`Comments`, `InsurancePolicyNumber`/`Agent`/`Term`+`CodeInsuranceTermUnitID`/`BeginDate`/`EndDate`/`AlertDate`/`TicklerDate` | A full insurance-tracking block on the equipment record itself, independent of the property-level `VendorInsurance` object in `people-parties`. |
| Maintenance SLA (×3, parallel) | `CodeMaintenancePartyID`+`MaintenanceResponsiblePersonID`+`CodeMaintenanceRemedyID`+`MaintenanceMaximumRemedyDays`; the same four-column pattern repeated for **Repair** and **Replacement** | Three independent responsibility/remedy/SLA blocks — who is responsible, which contact to reach, what remedy applies, and how many days it has, once each for routine maintenance, repair, and replacement. See `AST-R-013`. |
| Lifecycle dates | `InstallationDate`, `InServiceDate`, `MoveInDate`, `PurchaseDate`, `DispositionDate` | The physical asset's own lifecycle, independent of the lease's own dates. |
| **ASC 842/IFRS 16 classification overlay** | `FairValueOfAsset`, `DiscountRateOverride`, `IsAssetTooSpecializedForLessor`, `IsLowAssetValue`, `IsShortTerm`, `HasBuyoutOption`, `PlanToBuyAtEndOfTerm`, `DoesTitleRevertToTenant`, `InitialAssetBalanceAdjust`, `InitialLiabilityBalanceAdjust`, `ImpairmentOverride`, `Residual`, `YearsOfDepreciableLife`, `AccountingBeginDate`/`EndDate`, `RemainingAssetBalance`, `RemainingLife`+`CodeRemainingLifeFreqUnitID` | The equipment-lease classification tests, on the equipment record itself, not only on `ContractFinancialTest`. **This is the module's central finding — see [`equipment-leases.md`](equipment-leases.md).** |
| Financial position | `FinancialContractID` (typed `Contract ID`), `PurchasePrice`, `PurchaseOrderNumber`/`Description`/`Reference`, `CurrentAnnualPayment`, `CurrentMonthlyPayment`, `StartingDepreciationCost`, `DepreciationEndDate`, `ReplacementCost`, `AssetSalePrice`, `FinalAssetAmount`+`FinalAssetAllocPercent`+`FinalAssetDate` | The commercial and depreciation surface. `FinancialContractID` is the hard link to the equipment lease (§4). |
| Buttons | `MOVE_ASSET`, `GenerateServiceRequest` (both `sTYPE_SUBMITBUTTON`) | User-triggered actions, not batch jobs — see `AST-R-011`, and the same pattern the accounting module found for `Generate Rent`/`Calculate Schedule`. |

`Description` is the internal name behind the UI label **"Notes"** — the same relabeling pattern
[`../../data-fields/INDEX.md`](../../data-fields/INDEX.md) documents across the corpus generally.

### 2.1 `RemainingAssetBalance` is magnitude-typed — flagged again, here

**Observed**, field type `sTYPE_PERCENT_OR_AMOUNT`
([`../../data-fields/asset.md`](../../data-fields/asset.md)). Read as a **percentage** at 0–100,
and as **currency** at 100.01 and above; the user may override the platform's guess. This is the
same hazard `docs/modules/accounting/README.md` finding 4 documents for
`SLSummary.SLRemainingAssetBalance` — the identical field-type code appears on `Asset` too, meaning
**the ambiguity exists at both the contract-level schedule and the per-equipment-asset level.** A
rebuild must give this field an explicit, separate percentage column and currency column rather than
one polymorphic one, on both records.

### 2.2 Two `CodeAssetCategoryID` columns, two different UI roles

`Asset` carries **`CodeAssetCategoryID`**, labelled *"Maintenance Category"*, and
**`CodeDesc_CodeAssetCategoryID`**, labelled *"Account #"*
([`../../data-fields/asset.md`](../../data-fields/asset.md)) — two independent foreign keys into
the *same* `CodeAssetCategory` table, one read for maintenance classification and one read for GL
account lookup. **Derived**, and it only makes sense given §2.3: the code table itself carries both
a maintenance-facing label and a GL-facing account number, so the same row can be selected once for
each purpose from the same field's parent record.

### 2.3 `CodeAssetCategory` is a routing decision, not a label

**Observed** — 6 fields: `ShortName`, `ActualLongName`, `Inactive`, plus **`GLNumber`,
`SubAccount`, `DNEAmount`**. This is the same insight
[`../../data-model/code-table-registry.md`](../../data-model/code-table-registry.md) draws for
`CodeExpenseType` (3000-band, "Expense Type"): choosing an Asset Category is choosing a GL routing,
not merely tagging a record with a descriptive category. `DNEAmount` ("Do Not Exceed") on a code
table row, rather than on the `Asset` itself, means a spending ceiling is set **per category**, once,
rather than per asset.

## 3. The maintenance loop — `ServiceRequest` → `WorkOrder`, and how both relate to `Issue`

### 3.1 Both objects are `Issue` variants, generated by a button, not a workflow trigger

**Observed**, both [`../../data-fields/service-request.md`](../../data-fields/service-request.md)
and [`../../data-fields/work-order.md`](../../data-fields/work-order.md): `ServiceRequest.IssueID`
and `WorkOrder.IssueID` are both **Required = Yes**, field type `sTYPE_ISSUE`. That is exactly the
signature [`../../data-model/code-table-registry.md`](../../data-model/code-table-registry.md)
documents for `InvoiceIssue` and `BidderIssue` — a bespoke-named object that is really an `Issue`
row wearing a specific type. `ServiceRequest` and `WorkOrder` follow the identical pattern without
following the identical *naming* convention (neither is called `...Issue`), which is worth flagging
for anyone searching the schema for "the maintenance Issue variant" by name and not finding one.

The generation chain is **user-triggered by a button at each step**, not an automatic cascade:

```
Asset  ──[Generate Service Request button, sTYPE_SUBMITBUTTON]──►  ServiceRequest
ServiceRequest ──[Generate Work Order button, sTYPE_SUBMITBUTTON]──►  WorkOrder
```

**Observed** field-level evidence: `Asset.GenerateServiceRequest` and
`ServiceRequest.GenerateWorkOrder`, both `sTYPE_SUBMITBUTTON`
([`../../data-fields/asset.md`](../../data-fields/asset.md),
[`service-request.md`](../../data-fields/service-request.md)). **Derived:** this is the same
user-triggered-action pattern `docs/modules/accounting/README.md` finding 6 documents for `Generate
Rent`/`Calculate Schedule` — Lucernex's engines are consistently buttons on a record, not batch jobs,
and the maintenance loop is no exception.

### 3.2 The schema export and the admin Data Fields catalog disagree about the FK typing — and it hides the relationship from mechanical parsing

**Observed, and this is the module's second load-bearing finding.** In
`_lucernex_objects_summary.txt`, both `ServiceRequest.IssueID` and `WorkOrder.IssueID` are declared
type **`Text`**, not an `Entity Type ID`. `WorkOrder.ServiceRequestID` is likewise declared `Text`,
not `Service Request ID`. Yet the independently-captured admin Data Fields catalog shows all three
as typed lookups — `sTYPE_ISSUE` (Required) and `sTYPE_SERVICE_REQUEST` (not required) respectively.

This is the same category of divergence
[`../facilities-locations/data-model.md`](../facilities-locations/data-model.md) §5 found for
`Prototype`'s `Location`/`Complex`/`DMA` columns, but in the **opposite direction**: there, the
schema had the FK and the admin catalog didn't expose it; here, the *admin catalog* is the one that
shows the true relationship, and the raw schema export undercounts it. **Consequence:**
[`../../mindmap/edges.json`](../../mindmap/edges.json), built mechanically from the schema export's
typed columns, contains **no edge at all** from `ServiceRequest`/`WorkOrder` to `Issue`, and none
from `WorkOrder` to `ServiceRequest` — the entire relationship this section documents is invisible
to the automated FK graph and was only found by reading the two sources side by side. Any tool built
against `edges.json` alone will miss it.

**`WorkOrder.ServiceRequestID` is optional** (`Required = No`) even though the UI's normal path
always generates a `WorkOrder` from a `ServiceRequest` — meaning the schema permits a standalone
`WorkOrder` with no parent ticket, which the generation button does not exercise but which the data
model does not forbid.

### 3.3 Parts are consumed against the `Issue`, not against the `WorkOrder` object

**Observed**, `_lucernex_objects_summary.txt`: `LinkIssuePart` (13 fields: `IssueID`, `PartID`,
`AssetID` typed `Equipment ID`, `Quantity`, `CostPerPart`, `TotalCost`, `SerialNumber`) and
`LinkIssuePartOrder` (16 fields: `IssueID`, `PartID`, `QuantityOrdered`/`QuantityReceived`,
`VendorID`, `NeedByDate`, `CodePartOrderStatusID`) both key off **`IssueID`**, not `WorkOrderID`.
Both objects belong to the `projects-capital` module
([`../../mindmap/modules.json`](../../mindmap/modules.json)), not this one.

**Derived:** since `WorkOrder.IssueID` ties a `WorkOrder` 1:1 to an `Issue` (§3.1), the practical
path from "what parts did this work order use" runs `WorkOrder → Issue → LinkIssuePart → Part`, not
through any column on `WorkOrder` or `Part` directly. `LinkIssuePart` records actual consumption
(with its own cost/quantity/serial-number capture — a second, per-use record of `Part.Cost`, not a
read of it); `LinkIssuePartOrder` is the separate reorder/procurement record, complete with its own
vendor and receiving fields, which duplicates rather than reuses `Part.QuantityOnOrder`. Nothing in
`Part`, `PartPackage`, or `PartPackageItem` (this module) points at `ServiceRequest`, `WorkOrder`, or
`Issue` at all — the parts *catalog* and the parts *consumption* record are cleanly separated, and
only the catalog lives in this module.

### 3.4 The parts catalog has no per-location stock

**Derived**, exhaustive read of [`Part`](../../data-fields/part.md)'s 16 fields:
`QuantityOnHand`/`QuantityOnOrder`/`ParLevel`/`OrderToLevel` are single counters on the `Part`
record itself — there is no `Facility`/warehouse-scoped stock row anywhere in this module's object
list. A tenant with parts stocked at multiple locations has one number, firm-wide, not one per
location. A rebuild that needs multi-warehouse inventory will need a new join table Lucernex does
not have.

## 4. `Asset` in the accounting engine — the cross-module edges that matter most

**Observed**, [`../../mindmap/edges.json`](../../mindmap/edges.json):

| Source.Column | Target | Module | Cardinality |
|---|---|---|---|
| `Asset.FinancialContractID` | `Contract` | contracts-leases | N:1, the equipment lease itself |
| `ContractFinancialTest.AssetID` | `Asset` | contracts-leases | N:1, nullable |
| `SLSummary.AssetID` | `Asset` | accounting | N:1, nullable |
| `SLPeriod.AssetID` | `Asset` | accounting | N:1, nullable |
| `FinancialAdjustment.AssetID` | `Asset` | accounting | N:1, nullable |
| `ExpenseAllocation.AssetID` | `Asset` | accounting | N:1 |
| `ExpenseSchedule.AssetID` | `Asset` | accounting | N:1 |
| `PaymentTransaction.AssetID` / `PaymentTransactionFullImport.AssetID` | `Asset` | accounting | N:1 |
| `Issue.EquipmentID` / `.EquipmentIDList` | `Asset` | projects-capital | N:1 / 1:N, typed `Equipment ID` |
| `LinkIssuePart.AssetID` | `Asset` | projects-capital | N:1, typed `Equipment ID` |
| `AssetHistory.AssetID` | `Asset` | assets-equipment (internal) | N:1, typed `Equipment ID` |
| `CLRExtensionPart.AssetID`, `ClientListRow.AssetID` | `Asset` | layouts-forms-reporting | N:1 |

**This is the module's single most important structural fact.** `ContractFinancialTest`,
`SLSummary` and `SLPeriod` — the classification-test and schedule tables the accounting module built
around `Contract` — all carry a **separate, nullable, direct FK to `Asset`.** The same engine that
produces a contract-level ASC 842 schedule also runs *per-asset*, which is exactly what an equipment
lease covering several distinct pieces of equipment under one `Contract` requires: one `Contract`,
several `Asset` rows, and (potentially) several independent `SLSummary`/`ContractFinancialTest` rows,
one per asset, each nullable back to a specific `Asset` rather than only to the `Contract` as a
whole. Full argument and consequences: [`equipment-leases.md`](equipment-leases.md).

## 5. Confidence summary

| Claim | Label |
|---|---|
| `Asset` carries a full ASC 842/IFRS 16 classification overlay, separate from `ContractFinancialTest`'s | **Observed** — field list, `_lucernex_objects_summary.txt` |
| `ServiceRequest`/`WorkOrder` are `Issue` variants | **Observed** (`Required=Yes`, `sTYPE_ISSUE`, both Data Fields catalogs) |
| The schema export undercounts the `Issue`/`ServiceRequest`/`WorkOrder` relationship | **Derived** — direct comparison of the two sources |
| Parts consumption is tracked against `Issue`, not `WorkOrder` | **Derived** — `LinkIssuePart`/`LinkIssuePartOrder` key off `IssueID`, no column in this module's objects points at either |
| The generation chain is button-triggered, not automatic | **Observed** — `sTYPE_SUBMITBUTTON` fields on `Asset` and `ServiceRequest` |
| `AssetHistory`'s `firm_global` role label is a classifier false negative | **Derived**, corroborating [`../../data-model/project-entity.md`](../../data-model/project-entity.md) §2 |
| `RemainingAssetBalance` is magnitude-typed on `Asset` as well as `SLSummary` | **Observed** — identical `sTYPE_PERCENT_OR_AMOUNT` field type on both |
| `Asset.FinancialContractID`, `ContractFinancialTest.AssetID`, `SLSummary.AssetID`, `SLPeriod.AssetID` all connect the equipment record directly into the lease-accounting engine | **Observed**, `edges.json` |

## Open questions

1. **Can one `Contract` (equipment flavour) carry more than one `Asset`, each with its own
   `SLSummary`/`ContractFinancialTest` row?** The nullable, independent FK shape supports it; no
   screen or live record was captured to confirm it actually happens. See
   [`equipment-leases.md`](equipment-leases.md) open questions.
2. **What resolves the conflict when both `Asset`'s own classification fields (e.g.
   `ImpairmentOverride`) and `ContractFinancialTest`'s equivalent field are populated for the same
   asset?** `docs/modules/accounting/asc-842.md` open question 8 already raises this for
   `Contract`-level impairment; it applies identically here, one level down.
3. **Where does a live tenant's `Part` stock actually live if the tenant has more than one
   warehouse/facility?** Nothing in the schema answers this (§3.4).
4. **Does `WorkOrder.ServiceRequestID` being optional ever get exercised** — i.e., do any live
   `WorkOrder` rows exist with no parent `ServiceRequest`? Not checked against the live tenant's 605
   `assets` or any maintenance data in this pass.
