# AST-R-013 — WorkOrder's link to ServiceRequest is optional, unlike its link to Issue

*Assets, Equipment & Maintenance · Observed*

**Input: `WorkOrder.ServiceRequestID`, field type `sTYPE_SERVICE_REQUEST`, `Required = No`. Effect: A `WorkOrder` can exist with no parent `ServiceRequest`, even though the UI's normal generation path (`AST-R-011`) always produces one from a `ServiceRequest`.**

Input: `WorkOrder.ServiceRequestID`, field type `sTYPE_SERVICE_REQUEST`, `Required = No`. Effect: A `WorkOrder` can exist with no parent `ServiceRequest`, even though the UI's normal generation path (`AST-R-011`) always produces one from a `ServiceRequest`. Confidence: Observed (`../../data-fields/work-order.md`).

## What it constrains

[WorkOrder](../entities/WorkOrder.md), [ServiceRequest](../entities/ServiceRequest.md)

Columns named: `WorkOrder.ServiceRequestID`

## Rules it cites

[AST-R-011](AST-R-011.md)

## Confidence

Observed (`../../data-fields/work-order.md`)

---

Source: `docs/modules/assets-equipment/rules.md`
