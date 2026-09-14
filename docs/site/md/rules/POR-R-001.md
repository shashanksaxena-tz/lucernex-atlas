# POR-R-001

*Portfolio & Real-Estate Transactions · Observed*

**A `Contract` needs a fiscal period, discount rate, or ASC 842 threshold · `Contract.ProgramID` · Resolves to `Program`'s policy fields (`SLDiscountRate`, `FairValueThreshold`, `RemainingEconomicLifeThreshold`, `FiscalYearEnd`, FX rate types) before falling back to `Firm`. Full detail in….**

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | A `Contract` needs a fiscal period, discount rate, or ASC 842 threshold |
| Stated as | `Contract.ProgramID` |
| Stated as | Resolves to `Program`'s policy fields (`SLDiscountRate`, `FairValueThreshold`, `RemainingEconomicLifeThreshold`, `FiscalYearEnd`, FX rate types) before falling back to `Firm`. Full detail in `ACC-R-056`…`059` (`../accounting/`). |
| Stated as | Observed |

## What it constrains

[Contract](../entities/Contract.md), [Program](../entities/Program.md), [Firm](../entities/Firm.md)

Columns named: `Contract.ProgramID`

## Rules it cites

[ACC-R-056](ACC-R-056.md)

---

Source: `docs/modules/portfolio-transactions/rules.md`
