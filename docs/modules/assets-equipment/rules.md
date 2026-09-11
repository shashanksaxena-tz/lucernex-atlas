# Assets, Equipment & Maintenance — rules

`AST-R-001` through `AST-R-016`. Every rule below is derived from the FK graph
([`data-model.md`](data-model.md)), the Data Fields `Required`/`Field Type` columns, or a direct
field-definition quote; none is derived from a live screen capture of this module (no Asset/Service
Request/Work Order screen has been opened yet — see Open Questions in [`README.md`](README.md)), so
confidence tops out at **Derived** except where a vendor field definition is quoted directly.
Evidence discipline per [`../../CONVENTIONS.md`](../../CONVENTIONS.md).

---

### AST-R-001 — An Asset attaches to any `ProjectEntity`, not only to a Facility
**Trigger:** N/A (structural). **Input:** `Asset.ProjectEntityID`, the only entity-scoping column on
`Asset`. **Effect:** There is no hard-typed `FacilityID`/`LocationID` column on `Asset` at all — the
soft, universal `ProjectEntityID` is the sole attachment mechanism, so an Asset can in principle be
scoped to a Facility, a Location, a Portfolio, or any other `ProjectEntity` subtype. **Confidence:**
Observed (exhaustive field-list read, `_lucernex_objects_summary.txt`).

### AST-R-002 — An Asset may carry a second, independent soft pointer
**Input:** `Asset.AssociatedProjectEntityID`, typed the soft `Entity` type (not `Entity ID`).
**Effect:** Distinct from the primary `ProjectEntityID` scope — allows an asset record to reference a
second entity beyond the one it is scoped to. **Confidence:** Inferred — the column's presence and
type are Observed; what a populated value is used for at render time was not captured.

### AST-R-003 — An Asset's equipment lease is a hard, typed FK
**Input:** `Asset.FinancialContractID`, typed `Contract ID`. **Effect:** Ties the asset to the
equipment-flavour `Contract` that finances it, independent of the entity it is physically scoped to.
**Confidence:** Observed ([`../../data-fields/asset.md`](../../data-fields/asset.md)).

### AST-R-004 — Asset carries its own ASC 842/IFRS 16 classification overlay, parallel to Contract's
**Input:** The 13-field block enumerated in [`data-model.md`](data-model.md#2-asset--the-122-field-roster-grouped)
and detailed in [`equipment-leases.md`](equipment-leases.md). **Effect:** Equipment-lease
classification can run per asset, using asset-supplied inputs, rather than only at the contract
level. **Confidence:** Observed (field presence); the precedence between this overlay and
`ContractFinancialTest`'s equivalent fields is Inferred and unresolved — see
[`equipment-leases.md`](equipment-leases.md) open questions.

### AST-R-005 — `Asset.AccountingBeginDate`/`AccountingEndDate` override the derived accounting window
**Input:** The two override fields. **Effect:** When populated, replace the accounting window that
would otherwise be derived from the asset's `ExpenseSchedule` rows. **Confidence:** Observed —
vendor field-definition text quoted in
[`equipment-leases.md`](equipment-leases.md#3-assets-own-date-fields-override-the-contracts-when-populated).

### AST-R-006 — `RemainingAssetBalance` is magnitude-typed on Asset, exactly as on SLSummary
**Input:** `Asset.RemainingAssetBalance`, field type `sTYPE_PERCENT_OR_AMOUNT`. **Effect:** A value
0–100 is read as a percentage; ≥ 100.01 is read as currency; the user may override the platform's
guess. **Confidence:** Observed ([`../../data-fields/asset.md`](../../data-fields/asset.md)),
corroborating the identical hazard [`../accounting/README.md`](../accounting/README.md) finding 4
documents for `SLSummary.SLRemainingAssetBalance`.

### AST-R-007 — Two independent code-table lookups on Asset resolve to the same table, for different UI roles
**Input:** `Asset.CodeAssetCategoryID` (labelled *Maintenance Category*) and
`Asset.CodeDesc_CodeAssetCategoryID` (labelled *Account #*), both FKs to `CodeAssetCategory`.
**Effect:** The same code table serves a maintenance-classification role and a GL-account-lookup
role from the same parent record, via two separate columns. **Confidence:** Observed
([`../../data-fields/asset.md`](../../data-fields/asset.md)).

### AST-R-008 — An Asset Category code-table row is a GL routing decision, not a plain label
**Input:** `CodeAssetCategory.GLNumber`, `.SubAccount`, `.DNEAmount`, alongside `ShortName`/
`ActualLongName`/`Inactive`. **Effect:** Selecting an asset category also selects a GL account, a
sub-account, and a per-category spending ceiling (`DNEAmount`, "Do Not Exceed"). **Confidence:**
Observed (field list), corroborating the same pattern
[`../../data-model/code-table-registry.md`](../../data-model/code-table-registry.md) documents for
`CodeExpenseType`.

### AST-R-009 — Asset carries three parallel maintenance-SLA blocks: Maintenance, Repair, Replacement
**Input:** For each of the three event types, a `Code{X}PartyID` (Responsible Party code),
`{X}ResponsiblePersonID` (a `Person` contact), `Code{X}RemedyID` (a Maintenance Remedy code), and
`{X}MaximumRemedyDays` (a day count) — twelve fields total, four per event type. **Effect:** Each
event type has an independently configurable responsible party, a named contact, a remedy
classification, and an SLA day count. **Confidence:** Observed (exhaustive field-list read,
`_lucernex_objects_summary.txt`).

### AST-R-010 — Asset's vendor roles reuse Employer, seven ways
**Input:** `AlternateVendorID`, `InstallerVendorID`, `ManufacturerVendorID`, `PrimaryVendorID`,
`SecondaryVendorID`, `SupplierVendorID`, `WarrantyVendorID` — all typed `Employer ID`. **Effect:**
Seven distinct roles against the same company table, matching the landlord/tenant/vendor
multiplexing [`../../modules/people-parties/README.md`](../../modules/people-parties/README.md)
documents for `Employer` generally. **Confidence:** Observed
([`../../data-fields/asset.md`](../../data-fields/asset.md)).

### AST-R-011 — The maintenance loop is generated by buttons, not an automatic cascade
**Input:** `Asset.GenerateServiceRequest` and `ServiceRequest.GenerateWorkOrder`, both
`sTYPE_SUBMITBUTTON`. **Effect:** A `ServiceRequest` is created from an `Asset`, and a `WorkOrder`
from a `ServiceRequest`, only when a user presses the corresponding button — never automatically on
a schedule or threshold. **Confidence:** Observed
([`../../data-fields/asset.md`](../../data-fields/asset.md),
[`service-request.md`](../../data-fields/service-request.md)), matching the same user-triggered
pattern [`../accounting/README.md`](../accounting/README.md) finding 6 documents for `Generate
Rent`/`Calculate Schedule`.

### AST-R-012 — ServiceRequest and WorkOrder are each themselves `Issue` variants
**Input:** `ServiceRequest.IssueID` and `WorkOrder.IssueID`, both `Required = Yes`, field type
`sTYPE_ISSUE`. **Effect:** Each row of `ServiceRequest`/`WorkOrder` is paired 1:1 with an underlying
`Issue` record, exactly as `InvoiceIssue`/`BidderIssue` are documented to be in
[`../../data-model/code-table-registry.md`](../../data-model/code-table-registry.md) — without
following that pattern's naming convention. **Confidence:** Observed (both Data Fields catalogs);
the schema export itself declares both columns type `Text`, not a typed FK — see
[`data-model.md`](data-model.md#32-the-schema-export-and-the-admin-data-fields-catalog-disagree-about-the-fk-typing--and-it-hides-the-relationship-from-mechanical-parsing)
for the divergence this causes.

### AST-R-013 — WorkOrder's link to ServiceRequest is optional, unlike its link to Issue
**Input:** `WorkOrder.ServiceRequestID`, field type `sTYPE_SERVICE_REQUEST`, `Required = No`.
**Effect:** A `WorkOrder` can exist with no parent `ServiceRequest`, even though the UI's normal
generation path (`AST-R-011`) always produces one from a `ServiceRequest`. **Confidence:** Observed
([`../../data-fields/work-order.md`](../../data-fields/work-order.md)).

### AST-R-014 — Parts consumed against a job are recorded against the Issue, not the WorkOrder
**Input:** `LinkIssuePart.IssueID` + `.AssetID` (typed `Equipment ID`) + `.PartID` + `.Quantity` +
`.CostPerPart` + `.TotalCost` + `.SerialNumber` — an object in the `projects-capital` module, not
this one. **Effect:** The practical path from a `WorkOrder` to the parts it used runs
`WorkOrder → Issue (via WorkOrder.IssueID) → LinkIssuePart (via LinkIssuePart.IssueID)`; nothing in
`Part`, `PartPackage`, or `PartPackageItem` points at `ServiceRequest`, `WorkOrder`, or `Issue` at
all. **Confidence:** Derived (exhaustive read of both objects' field lists;
[`data-model.md`](data-model.md#33-parts-are-consumed-against-the-issue-not-against-the-workorder-object)).

### AST-R-015 — The parts catalog carries no per-location stock
**Input:** `Part.QuantityOnHand`, `.QuantityOnOrder`, `.ParLevel`, `.OrderToLevel` — single counters
on the catalog record, with no `FacilityID`/warehouse column anywhere in this module. **Effect:** A
tenant with parts stocked at multiple locations has one firm-wide count per part, not one per
location. **Confidence:** Derived (exhaustive field-list read,
[`../../data-fields/part.md`](../../data-fields/part.md)).

### AST-R-016 — `AssetHistory` is entity-scoped in practice despite its mechanical `firm_global` label
**Input:** `AssetHistory.ProjectEntityID` and `.FromProjectEntityID`, both typed the soft `Entity`
type rather than the hard `Entity ID` type. **Effect:** The object behaves as an entity-scoped
snapshot of an `Asset`'s state, but escapes the mechanical role classifier that looks only for the
hard FK type. **Confidence:** Derived, corroborating
[`../../data-model/project-entity.md`](../../data-model/project-entity.md) §2's own naming of this
exact object as a false negative.
