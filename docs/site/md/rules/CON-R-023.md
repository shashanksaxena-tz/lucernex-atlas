# CON-R-023 — 2. Contract identity and hierarchy

*Contracts & Leases · Observed*

**Determining the fiscal calendar: the calendar is owned by Contract.ProgramID (the portfolio), not by the firm.**

Determining the fiscal calendar: the calendar is owned by Contract.ProgramID (the portfolio), not by the firm.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Determining the fiscal calendar |
| Stated as | `Contract.ProgramID` → `FiscalPeriod.ProgramID` |
| Stated as | The fiscal calendar is owned by the portfolio, not the firm |
| Stated as | Period definitions |
| Stated as | Observed |

## What it constrains

[Contract](../entities/Contract.md), [FiscalPeriod](../entities/FiscalPeriod.md)

Columns named: `Contract.ProgramID`, `FiscalPeriod.ProgramID`

---

Source: `docs/modules/contracts/rules.md`
