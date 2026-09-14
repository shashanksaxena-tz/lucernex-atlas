# POR-R-005

*Portfolio & Real-Estate Transactions · Observed*

**A `PotentialProject`, `Program`, `Scenario`, or `RETransaction` needs a deal classification · `PotentialProject.CodeDealTypeID` / `Program.CodeDealTypeID` → `Deal Type Code` (2024); `Scenario.CodeScenarioDealTypeID` / `RETransaction.PreferredScenarioCodeDealTypeID` → `Scenario Deal Type Code`….**

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | A `PotentialProject`, `Program`, `Scenario`, or `RETransaction` needs a deal classification |
| Stated as | `PotentialProject.CodeDealTypeID` / `Program.CodeDealTypeID` → `Deal Type Code` (2024); `Scenario.CodeScenarioDealTypeID` / `RETransaction.PreferredScenarioCodeDealTypeID` → `Scenario Deal Type Code` (2059); `Scenario.CodeScenarioTypeID` → `Scenario Type Code` (2060); `RETransaction.CodeRETransactionStatusID` → `RE Transaction Status Code` (2057) |
| Stated as | Four distinct code tables classify overlapping aspects of one pipeline. Row values were never captured from the live tenant. |
| Stated as | Observed table existence and attachment; unconfirmed contents |

## What it constrains

[PotentialProject](../entities/PotentialProject.md), [Program](../entities/Program.md), [Scenario](../entities/Scenario.md), [RETransaction](../entities/RETransaction.md)

Columns named: `PotentialProject.CodeDealTypeID`, `Program.CodeDealTypeID`, `Scenario.CodeScenarioDealTypeID`, `RETransaction.PreferredScenarioCodeDealTypeID`, `Scenario.CodeScenarioTypeID`, `RETransaction.CodeRETransactionStatusID`

---

Source: `docs/modules/portfolio-transactions/rules.md`
