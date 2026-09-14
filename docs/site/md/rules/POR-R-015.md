# POR-R-015

*Portfolio & Real-Estate Transactions · Derived*

**A `Scenario`'s deal type needs comparing against its parent transaction's preference · `Scenario.CodeScenarioDealTypeID` vs. `RETransaction.PreferredScenarioCodeDealTypeID` · Both draw from the same code table (`Scenario Deal Type Code`, 2059) but are independent fields — nothing in the schema….**

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | A `Scenario`'s deal type needs comparing against its parent transaction's preference |
| Stated as | `Scenario.CodeScenarioDealTypeID` vs. `RETransaction.PreferredScenarioCodeDealTypeID` |
| Stated as | Both draw from the same code table (`Scenario Deal Type Code`, 2059) but are independent fields — nothing in the schema enforces they match. |
| Stated as | Derived |

## What it constrains

[Scenario](../entities/Scenario.md), [RETransaction](../entities/RETransaction.md)

Columns named: `Scenario.CodeScenarioDealTypeID`, `RETransaction.PreferredScenarioCodeDealTypeID`

---

Source: `docs/modules/portfolio-transactions/rules.md`
