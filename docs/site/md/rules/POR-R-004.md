# POR-R-004

*Portfolio & Real-Estate Transactions · Observed*

**A `Scenario` reaches `Contract` · `Scenario.ContractID` · One-way, optional link. `Contract` carries no reciprocal `ScenarioID`/`RETransactionID` column — a signed lease cannot be traced back to the deal that produced it via FK.**

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | A `Scenario` reaches `Contract` |
| Stated as | `Scenario.ContractID` |
| Stated as | One-way, optional link. `Contract` carries no reciprocal `ScenarioID`/`RETransactionID` column — a signed lease cannot be traced back to the deal that produced it via FK. |
| Stated as | Observed |

## What it constrains

[Scenario](../entities/Scenario.md), [Contract](../entities/Contract.md)

Columns named: `Scenario.ContractID`

---

Source: `docs/modules/portfolio-transactions/rules.md`
