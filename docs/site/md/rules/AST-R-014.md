# AST-R-014 — Parts consumed against a job are recorded against the Issue, not the WorkOrder

*Assets, Equipment & Maintenance · Derived*

**Input: `LinkIssuePart.IssueID` + `.AssetID` (typed `Equipment ID`) + `.PartID` + `.Quantity` + `.CostPerPart` + `.TotalCost` + `.SerialNumber` — an object in the `projects-capital` module, not this one. Effect: The practical path from a `WorkOrder` to the parts it used runs `WorkOrder → Issue (via….**

Input: `LinkIssuePart.IssueID` + `.AssetID` (typed `Equipment ID`) + `.PartID` + `.Quantity` + `.CostPerPart` + `.TotalCost` + `.SerialNumber` — an object in the `projects-capital` module, not this one. Effect: The practical path from a `WorkOrder` to the parts it used runs `WorkOrder → Issue (via WorkOrder.IssueID) → LinkIssuePart (via LinkIssuePart.IssueID)`; nothing in `Part`, `PartPackage`, or `PartPackageItem` points at `ServiceRequest`, `WorkOrder`, or `Issue` at all. Confidence: Derived (exhaustive read of both objects' field lists; `data-model.md`).

## What it constrains

[LinkIssuePart](../entities/LinkIssuePart.md), [WorkOrder](../entities/WorkOrder.md), [Part](../entities/Part.md), [PartPackage](../entities/PartPackage.md), [PartPackageItem](../entities/PartPackageItem.md), [ServiceRequest](../entities/ServiceRequest.md), [Issue](../entities/Issue.md)

Columns named: `LinkIssuePart.IssueID`

## Confidence

Derived (exhaustive read of both objects' field lists; `data-model.md`)

---

Source: `docs/modules/assets-equipment/rules.md`
