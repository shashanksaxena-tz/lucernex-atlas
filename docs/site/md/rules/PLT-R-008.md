# PLT-R-008 — Region is a three-level hierarchy resolved by `RegionID`/`RootRegionID`/`SubRegionID`

*Platform & Tenancy · Derived*

**The routing rule names a region-scoped principal category (see `../workflow/routing-and-approvals.md` §2, Dimension 2).**

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | Workflow routing with `AssigneeType = REGION1 \| REGION2 \| MARKET` |
| What it reads | `ProjectEntity.RegionID`, `RootRegionID`, `SubRegionID`, `CodeMarketAreaID`, `CodeMarketTypeID` |
| The test | The routing rule names a region-scoped principal category (see `../workflow/routing-and-approvals.md` §2, Dimension 2) |
| What it writes | The scope resolves against this three-column region hierarchy on the entity, not against a separate routing table. `Region` itself declares almost none of this shape directly — see `PLT-R-009` |

## What it constrains

[ProjectEntity](../entities/ProjectEntity.md), [Region](../entities/Region.md)

Columns named: `ProjectEntity.RegionID`

## Rules it cites

[PLT-R-009](PLT-R-009.md)

## Confidence

Derived — cross-module reconciliation between this module's schema and `../workflow/routing-and-approvals.md`

---

Source: `docs/modules/platform-tenancy/rules.md`
