# POR-R-009

*Portfolio & Real-Estate Transactions · Inferred*

**Notification/routing needs to walk the org chart · `Program.OrgChartProgramID` (self-reference) + `LinkRegionManager` (member-to-region assignment) · Two independent hierarchies exist: the `Region` chain and the `Program` self-reference (a Portfolio rolling into a parent Portfolio). Neither is the….**

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Notification/routing needs to walk the org chart |
| Stated as | `Program.OrgChartProgramID` (self-reference) + `LinkRegionManager` (member-to-region assignment) |
| Stated as | Two independent hierarchies exist: the `Region` chain and the `Program` self-reference (a Portfolio rolling into a parent Portfolio). Neither is the `OrgChart` screen's data source, which was never opened. |
| Stated as | Inferred |

## What it constrains

[Program](../entities/Program.md), [LinkRegionManager](../entities/LinkRegionManager.md), [Region](../entities/Region.md)

Columns named: `Program.OrgChartProgramID`

---

Source: `docs/modules/portfolio-transactions/rules.md`
