# CON-R-119 — 9. Payment lifecycle

*Contracts & Leases · Observed*

**An accrual is posted: AccrualTransaction carries PeriodAmount, PeriodBeginDate/EndDate, PeriodNumber/Year and PostingDate, with its own GL slots, driven by GENERATE_ACCRUALS.**

An accrual is posted: AccrualTransaction carries PeriodAmount, PeriodBeginDate/EndDate, PeriodNumber/Year and PostingDate, with its own GL slots, driven by GENERATE_ACCRUALS.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | An accrual is posted |
| Stated as | `AccrualTransaction.PeriodAmount`, `.PeriodBeginDate`, `.PeriodEndDate`, `.PeriodNumber`, `.PeriodYear`, `.PostingDate`, `GENERATE_ACCRUALS` |
| Stated as | Period-scoped accrual with its own GL slots |
| Stated as | Accrual posting |
| Stated as | Observed |

## What it constrains

[AccrualTransaction](../entities/AccrualTransaction.md)

Columns named: `AccrualTransaction.PeriodAmount`

---

Source: `docs/modules/contracts/rules.md`
