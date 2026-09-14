# PRJ-R-009

*Capital Projects & Scheduling · Observed*

**A part is consumed or ordered against a work-order `Issue` · `LinkIssuePart` (cost, labor hours, serial number) vs. `LinkIssuePartOrder` (quantity ordered/received, `CodePartOrderStatusID`) · Two distinct records — one for parts actually used, one for parts on order — both attached to the same….**

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | A part is consumed or ordered against a work-order `Issue` |
| Stated as | `LinkIssuePart` (cost, labor hours, serial number) vs. `LinkIssuePartOrder` (quantity ordered/received, `CodePartOrderStatusID`) |
| Stated as | Two distinct records — one for parts actually used, one for parts on order — both attached to the same `Issue` via `IssueID`. |
| Stated as | Observed |

## What it constrains

[Issue](../entities/Issue.md), [LinkIssuePart](../entities/LinkIssuePart.md), [LinkIssuePartOrder](../entities/LinkIssuePartOrder.md)

---

Source: `docs/modules/projects-capital/rules.md`
