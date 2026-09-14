# POR-R-008

*Portfolio & Real-Estate Transactions · Observed*

**A user compares competing sites or scenarios · `ComparisonReport` → `ComparisonItem` · `ComparisonItem.ComputedValue`/`ExpenseGroup` hold computed comparison output; `ScenarioName`/`ScenarioDate` are plain text, not FKs — a comparison item does not hard-link to the `Scenario` row it summarises.**

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | A user compares competing sites or scenarios |
| Stated as | `ComparisonReport` → `ComparisonItem` |
| Stated as | `ComparisonItem.ComputedValue`/`ExpenseGroup` hold computed comparison output; `ScenarioName`/`ScenarioDate` are plain text, not FKs — a comparison item does not hard-link to the `Scenario` row it summarises. |
| Stated as | Observed structure; Inferred usage |

## What it constrains

[ComparisonReport](../entities/ComparisonReport.md), [ComparisonItem](../entities/ComparisonItem.md), [Scenario](../entities/Scenario.md)

Columns named: `ComparisonItem.ComputedValue`

---

Source: `docs/modules/portfolio-transactions/rules.md`
