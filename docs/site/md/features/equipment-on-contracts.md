# Equipment on Contracts

Equipment as a leased asset on a contract - in scope via ASG Edge+ BRD-13 (Equipment Contracts) and BRD-16 (Contract Equipment Accounting). The maintenance side of the module (service requests and work orders) has no BRD and is out of scope.

## Who it is for

*Derived · fact · source: `docs/features/README.md`*

The teams leasing equipment rather than space — and the accountants, because the same ASC 842 engine runs over both.

## Where it is used

*Observed · fact · source: `docs/data-model/screen-routing.md`*

BBW's fifth navigation root, 32 nodes. It renders only because BBW holds equipment-contract records; American Freight's identical configuration does not render, because it holds none.

## Equipment on 842

*Observed · capability · source: `docs/modules/assets-equipment/equipment-leases.md`*

Equipment leases run on the accounting engine: the classification, summary and period records each carry a nullable foreign key to Asset, so embedded equipment leases are classified and scheduled by the same engine as real estate.

## Request to WorkOrder

*Derived · capability · source: `docs/modules/assets-equipment/README.md`*

Out of scope - no BRD covers maintenance: the loop is request, triage, work order, completion, all variants of the same request record that backs forms. Kept here because it shares the module.

## Equipment Contracts

*Observed · fact · source: `docs/features/equipment-contracts/README.md`*

What the equipment contracts manual settles: BBW's fifth root, all 32 nodes with ids. Contract minus the retail layers; the whole ASC 842 engine kept. No EquipmentContract table exists in any inventory. Biggest open question: Whether it stores in Contract under ProjectEntityTypeName.

## Manual contents

*Observed · fact · source: `docs/features/equipment-contracts/README.md`*

The equipment contracts manual is organised as: The 32 nodes, with ids; The module, rendered — and it rests on a single record; What is dropped, and why it is coherent; Storage: an entity type with no table; Why American Freight does not show it; What this means for ASG Edge+. Read it rather than this node when you need the detail — this is the index.

## Evidence

*Observed · fact · source: `features/equipment-contracts/README.md`*

Written up in features/equipment-contracts/README.md.

## Open questions (8)

*Inferred · group*

8 things nobody has confirmed for this feature. Each one is work somebody has to do before the feature can be rebuilt with confidence; they are carried here rather than resolved by guessing. Click one for the question and the document that raised it.

### Does an Equipment

*Inferred · question · source: `docs/features/equipment-contracts/README.md`*

~~Does an Equipment Contract row live in Contract?~~ Answered: yes, discriminated by ProjectEntityTypeName = 'Equipment Contract' (with a space). The REST EquipmentContract type is an alias over the same rows. Nobody has confirmed this. Recorded in features/equipment-contracts/README.md, under the Equipment on Contracts area. Until it is settled, anything built on the assumption is a guess.

### What are the 32 JSP

*Inferred · question · source: `docs/features/equipment-contracts/README.md`*

What are the 32 JSP routes? Not captured; not joinable from AF. Requested. Nobody has confirmed this. Recorded in features/equipment-contracts/README.md, under the Equipment on Contracts area. Until it is settled, anything built on the assumption is a guess.

### What do the screens

*Inferred · question · source: `docs/features/equipment-contracts/README.md`*

What do the screens actually contain? No Equipment Contract screen has ever been rendered. Screenshots of Summary (41095), Abstract Details (41091), Payment Details (41093), Accounting Details (45607) and ASC 842 Rent Schedule (43782) requested. Nobody has confirmed this. Recorded in features/equipment-contracts/README.md, under the Equipment on Contracts area. Until it is settled, anything built on the assumption is a guess.

### BBW 02 why is Capital

*Inferred · question · source: `docs/features/equipment-contracts/README.md`*

Q-BBW-02 — why is Capital Lease Test dropped but ASC 842 Test kept? The generic/specific reading does not explain it. Likely the legacy FAS 13 test; unconfirmed. Nobody has confirmed this. Recorded in features/equipment-contracts/README.md, under the Equipment on Contracts area. Until it is settled, anything built on the assumption is a guess.

### BBW 12 what is the

*Inferred · question · source: `docs/features/equipment-contracts/README.md`*

Q-BBW-12 — what is the second gate on the root? UserClassSecurity.PageLayoutID is now the predicted mechanism (see above). Confirming it needs /en/admin/SecurityPageAccess.jsp read with a real user class selected. Nobody has confirmed this. Recorded in features/equipment-contracts/README.md, under the Equipment on Contracts area. Until it is settled, anything built on the assumption is a guess.

### Which layouts serve

*Inferred · question · source: `docs/features/equipment-contracts/README.md`*

Which layouts serve these screens? No BBW firm layout attaches to any Equipment Contract navigation node, so the screens must be rendered by platform layouts — which are not listed in Manage Page Layouts and whose field content is therefore unreadable by the route used for the 93 firm layouts. This is the same blind spot described in ../page-layouts/. Nobody has confirmed this. Recorded in features/equipment-contracts/README.md, under the Equipment on Contracts area. Until it is settled, anything built on the assumption is a guess.

### Is Asset linked to an

*Inferred · question · source: `docs/features/equipment-contracts/README.md`*

~~Is Asset linked to an Equipment Contract, and how?~~ Answered: an embedded Equipment grid on the Summary screen, with the asset pointing back at the contract, and the ASC 842 flags Is Short Term / Is Low Asset Value shown as grid columns. Nobody has confirmed this. Recorded in features/equipment-contracts/README.md, under the Equipment on Contracts area. Until it is settled, anything built on the assumption is a guess.

### What does the module

*Inferred · question · source: `docs/features/equipment-contracts/README.md`*

What does the module look like with real data? Everything observed rests on one record, itself barely populated. The range of the module is unknown. Nobody has confirmed this. Recorded in features/equipment-contracts/README.md, under the Equipment on Contracts area. Until it is settled, anything built on the assumption is a guess.

## Rules (16)

*Derived · group*

Every numbered rule the docs corpus records for this feature, named by a short summary. Click one: the panel opens with its ID, the full statement, and a link to the complete rule page.

### An Asset attaches to — [AST-R-001](../rules/AST-R-001.md)

*Observed · rule · source: `docs/modules/assets-equipment/rules.md`*

**Trigger: N/A (structural). Input: `Asset.ProjectEntityID`, the only entity-scoping column on `Asset`.**

### An Asset may carry a — [AST-R-002](../rules/AST-R-002.md)

*Inferred · rule · source: `docs/modules/assets-equipment/rules.md`*

**Input: `Asset.AssociatedProjectEntityID`, typed the soft `Entity` type (not `Entity ID`). Effect: Distinct from the primary `ProjectEntityID` scope — allows an asset record to reference a second entity beyond the one it is scoped to.**

### An Asset s equipment — [AST-R-003](../rules/AST-R-003.md)

*Observed · rule · source: `docs/modules/assets-equipment/rules.md`*

**Input: `Asset.FinancialContractID`, typed `Contract ID`. Effect: Ties the asset to the equipment-flavour `Contract` that finances it, independent of the entity it is physically scoped to.**

### Asset carries its — [AST-R-004](../rules/AST-R-004.md)

*Observed · rule · source: `docs/modules/assets-equipment/rules.md`*

**Input: The 13-field block enumerated in `data-model.md` and detailed in `equipment-leases.md`. Effect: Equipment-lease classification can run per asset, using asset-supplied inputs, rather than only at the contract level.**

### Asset — [AST-R-005](../rules/AST-R-005.md)

*Derived · rule · source: `docs/modules/assets-equipment/rules.md`*

**Input: The two override fields. Effect: When populated, replace the accounting window that would otherwise be derived from the asset's `ExpenseSchedule` rows.**

### AST-R-006 — [AST-R-006](../rules/AST-R-006.md)

*Observed · rule · source: `docs/modules/assets-equipment/rules.md`*

**Input: `Asset.RemainingAssetBalance`, field type `sTYPE_PERCENT_OR_AMOUNT`. Effect: A value 0–100 is read as a percentage;.**

### Two independent code — [AST-R-007](../rules/AST-R-007.md)

*Observed · rule · source: `docs/modules/assets-equipment/rules.md`*

**Input: `Asset.CodeAssetCategoryID` (labelled Maintenance Category) and `Asset.CodeDesc_CodeAssetCategoryID` (labelled Account #), both FKs to `CodeAssetCategory`. Effect: The same code table serves a maintenance-classification role and a GL-account-lookup role from the same parent record, via two….**

### An Asset Category — [AST-R-008](../rules/AST-R-008.md)

*Observed · rule · source: `docs/modules/assets-equipment/rules.md`*

**Input: `CodeAssetCategory.GLNumber`, `.SubAccount`, `.DNEAmount`, alongside `ShortName`/ `ActualLongName`/`Inactive`. Effect: Selecting an asset category also selects a GL account, a sub-account, and a per-category spending ceiling (`DNEAmount`, "Do Not Exceed").**

### Asset carries three — [AST-R-009](../rules/AST-R-009.md)

*Observed · rule · source: `docs/modules/assets-equipment/rules.md`*

**Input: For each of the three event types, a `Code{X}PartyID` (Responsible Party code), `{X}ResponsiblePersonID` (a `Person` contact), `Code{X}RemedyID` (a Maintenance Remedy code), and `{X}MaximumRemedyDays` (a day count) — twelve fields total, four per event type. Effect: Each event type has an….**

### Asset s vendor roles — [AST-R-010](../rules/AST-R-010.md)

*Observed · rule · source: `docs/modules/assets-equipment/rules.md`*

**Input: `AlternateVendorID`, `InstallerVendorID`, `ManufacturerVendorID`, `PrimaryVendorID`, `SecondaryVendorID`, `SupplierVendorID`, `WarrantyVendorID` — all typed `Employer ID`. Effect: Seven distinct roles against the same company table, matching the landlord/tenant/vendor multiplexing….**

### The maintenance loop — [AST-R-011](../rules/AST-R-011.md)

*Observed · rule · source: `docs/modules/assets-equipment/rules.md`*

**Input: `Asset.GenerateServiceRequest` and `ServiceRequest.GenerateWorkOrder`, both `sTYPE_SUBMITBUTTON`. Effect: A `ServiceRequest` is created from an `Asset`, and a `WorkOrder` from a `ServiceRequest`, only when a user presses the corresponding button — never automatically on a schedule or….**

### ServiceRequest and — [AST-R-012](../rules/AST-R-012.md)

*Observed · rule · source: `docs/modules/assets-equipment/rules.md`*

**Input: `ServiceRequest.IssueID` and `WorkOrder.IssueID`, both `Required = Yes`, field type `sTYPE_ISSUE`. Effect: Each row of `ServiceRequest`/`WorkOrder` is paired 1:1 with an underlying `Issue` record, exactly as `InvoiceIssue`/`BidderIssue` are documented to be in….**

### WorkOrder s link to — [AST-R-013](../rules/AST-R-013.md)

*Observed · rule · source: `docs/modules/assets-equipment/rules.md`*

**Input: `WorkOrder.ServiceRequestID`, field type `sTYPE_SERVICE_REQUEST`, `Required = No`. Effect: A `WorkOrder` can exist with no parent `ServiceRequest`, even though the UI's normal generation path (`AST-R-011`) always produces one from a `ServiceRequest`.**

### Parts consumed — [AST-R-014](../rules/AST-R-014.md)

*Derived · rule · source: `docs/modules/assets-equipment/rules.md`*

**Input: `LinkIssuePart.IssueID` + `.AssetID` (typed `Equipment ID`) + `.PartID` + `.Quantity` + `.CostPerPart` + `.TotalCost` + `.SerialNumber` — an object in the `projects-capital` module, not this one. Effect: The practical path from a `WorkOrder` to the parts it used runs `WorkOrder → Issue (via….**

### The parts catalog — [AST-R-015](../rules/AST-R-015.md)

*Derived · rule · source: `docs/modules/assets-equipment/rules.md`*

**Input: `Part.QuantityOnHand`, `.QuantityOnOrder`, `.ParLevel`, `.OrderToLevel` — single counters on the catalog record, with no `FacilityID`/warehouse column anywhere in this module. Effect: A tenant with parts stocked at multiple locations has one firm-wide count per part, not one per location.**

### AssetHistory is — [AST-R-016](../rules/AST-R-016.md)

*Derived · rule · source: `docs/modules/assets-equipment/rules.md`*

**Input: `AssetHistory.ProjectEntityID` and `.FromProjectEntityID`, both typed the soft `Entity` type rather than the hard `Entity ID` type. Effect: The object behaves as an entity-scoped snapshot of an `Asset`'s state, but escapes the mechanical role classifier that looks only for the hard FK type.**
