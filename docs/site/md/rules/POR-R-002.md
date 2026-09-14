# POR-R-002

*Portfolio & Real-Estate Transactions · Inferred*

**Workflow routing needs a `REGION1`/`REGION2` assignee · `Program.RegionID` / `RootRegionID` / `SubRegionID` → `Region` · Resolves an org-chart position through the region hierarchy. `MARKET` resolves through `CodeMarketAreaID` instead, a different code table.**

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Workflow routing needs a `REGION1`/`REGION2` assignee |
| Stated as | `Program.RegionID` / `RootRegionID` / `SubRegionID` → `Region` |
| Stated as | Resolves an org-chart position through the region hierarchy. `MARKET` resolves through `CodeMarketAreaID` instead, a different code table. |
| Stated as | Inferred — no screen confirms the exact level mapping |

## What it constrains

[Program](../entities/Program.md), [Region](../entities/Region.md)

Columns named: `Program.RegionID`

---

Source: `docs/modules/portfolio-transactions/rules.md`
