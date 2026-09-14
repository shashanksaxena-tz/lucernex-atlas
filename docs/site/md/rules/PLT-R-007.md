# PLT-R-007 — A permission grant targets exactly one of four surfaces

*Platform & Tenancy · Observed*

**The grant is scoped to a whole page layout, a single field-registry leaf, a field-registry subtree, or a dashboard component — never more than one kind at a time, and the level (`SecurityLevelByteValue`) is one of `DEFAULT | NO_ACCESS | VIEW | EDIT | DELETE`.**

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | A `UserClassSecurity` row is created |
| What it reads | `PageLayoutID`, `ReportGroupAvailableFieldID`, `ReportGroupDataID`/`RootReportGroupDataID`/ `SubReportGroupDataID`, `DashboardComponentID` |
| What it writes | The grant is scoped to a whole page layout, a single field-registry leaf, a field-registry subtree, or a dashboard component — never more than one kind at a time, and the level (`SecurityLevelByteValue`) is one of `DEFAULT \| NO_ACCESS \| VIEW \| EDIT \| DELETE` |

## What it constrains

[UserClassSecurity](../entities/UserClassSecurity.md)

## Confidence

Observed — `../../data-model/graphql-api.md` (`SecurityLevel` enum), Derived granularity claim from the column set. ## Org-chart and geography

---

Source: `docs/modules/platform-tenancy/rules.md`
