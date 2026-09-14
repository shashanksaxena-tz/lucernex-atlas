# PPL-R-011 — Region/Market routing resolves through the entity, not through any `Member` column

*People & Parties · Derived*

**This is a two-hop resolution (entity → region/market → manager), not a direct `Member` attribute lookup.**

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | `AssigneeType = REGION1 \| REGION2 \| MARKET` |
| What it reads | `ProjectEntity.RegionID`/`RootRegionID`/`SubRegionID`/`CodeMarketAreaID`/ `CodeMarketTypeID` (in `../platform-tenancy/`), then `LinkRegionManager` to find the responsible member |
| What it writes | This is a two-hop resolution (entity → region/market → manager), not a direct `Member` attribute lookup |

## What it constrains

[ProjectEntity](../entities/ProjectEntity.md), [LinkRegionManager](../entities/LinkRegionManager.md), [Member](../entities/Member.md)

Columns named: `ProjectEntity.RegionID`

## Confidence

Derived — `security-model.md`

---

Source: `docs/modules/people-parties/rules.md`
