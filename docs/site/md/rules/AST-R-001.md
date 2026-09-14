# AST-R-001 — An Asset attaches to any `ProjectEntity`, not only to a Facility

*Assets, Equipment & Maintenance · Observed*

**Trigger: N/A (structural). Input: `Asset.ProjectEntityID`, the only entity-scoping column on `Asset`.**

Trigger: N/A (structural). Input: `Asset.ProjectEntityID`, the only entity-scoping column on `Asset`. Effect: There is no hard-typed `FacilityID`/`LocationID` column on `Asset` at all — the soft, universal `ProjectEntityID` is the sole attachment mechanism, so an Asset can in principle be scoped to a Facility, a Location, a Portfolio, or any other `ProjectEntity` subtype. Confidence: Observed (exhaustive field-list read, `_lucernex_objects_summary.txt`).

## What it constrains

[Asset](../entities/Asset.md), [ProjectEntity](../entities/ProjectEntity.md)

Columns named: `Asset.ProjectEntityID`

## Confidence

Observed (exhaustive field-list read, `_lucernex_objects_summary.txt`)

---

Source: `docs/modules/assets-equipment/rules.md`
