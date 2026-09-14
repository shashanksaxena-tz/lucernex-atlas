# POR-R-012

*Portfolio & Real-Estate Transactions · Derived*

**A Site is promoted toward becoming an operating asset · `Program.SiteToProjectSetupLayoutID`, then `Program.ProjectToFacilitySetupLayoutID` · Names a two-step conversion pipeline (Site → Project → Facility). The second step is corroborated by a real FK (`Project.FacilityID`, admin-labelled "Related….**

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | A Site is promoted toward becoming an operating asset |
| Stated as | `Program.SiteToProjectSetupLayoutID`, then `Program.ProjectToFacilitySetupLayoutID` |
| Stated as | Names a two-step conversion pipeline (Site → Project → Facility). The second step is corroborated by a real FK (`Project.FacilityID`, admin-labelled "Related Project Facility", optional); the first step has no FK corroboration at all. |
| Stated as | Derived (naming + partial FK); Inferred (full mechanism) — see `site-pipeline.md` |

## What it constrains

[Program](../entities/Program.md), [Project](../entities/Project.md)

Columns named: `Program.SiteToProjectSetupLayoutID`, `Program.ProjectToFacilitySetupLayoutID`, `Project.FacilityID`

---

Source: `docs/modules/portfolio-transactions/rules.md`
