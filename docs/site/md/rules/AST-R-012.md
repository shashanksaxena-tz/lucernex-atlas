# AST-R-012 — ServiceRequest and WorkOrder are each themselves `Issue` variants

*Assets, Equipment & Maintenance · Observed*

**Input: `ServiceRequest.IssueID` and `WorkOrder.IssueID`, both `Required = Yes`, field type `sTYPE_ISSUE`. Effect: Each row of `ServiceRequest`/`WorkOrder` is paired 1:1 with an underlying `Issue` record, exactly as `InvoiceIssue`/`BidderIssue` are documented to be in….**

Input: `ServiceRequest.IssueID` and `WorkOrder.IssueID`, both `Required = Yes`, field type `sTYPE_ISSUE`. Effect: Each row of `ServiceRequest`/`WorkOrder` is paired 1:1 with an underlying `Issue` record, exactly as `InvoiceIssue`/`BidderIssue` are documented to be in `../../data-model/code-table-registry.md` — without following that pattern's naming convention. Confidence: Observed (both Data Fields catalogs); the schema export itself declares both columns type `Text`, not a typed FK — see `data-model.md` for the divergence this causes.

## What it constrains

[ServiceRequest](../entities/ServiceRequest.md), [WorkOrder](../entities/WorkOrder.md), [Issue](../entities/Issue.md), [InvoiceIssue](../entities/InvoiceIssue.md), [BidderIssue](../entities/BidderIssue.md)

Columns named: `ServiceRequest.IssueID`, `WorkOrder.IssueID`

## Confidence

Observed (both Data Fields catalogs); the schema export itself declares both columns type `Text`, not a typed FK — see `data-model.md` for the divergence this causes

---

Source: `docs/modules/assets-equipment/rules.md`
