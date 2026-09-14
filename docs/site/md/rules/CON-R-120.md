# CON-R-120 — 9. Payment lifecycle

*Contracts & Leases · Observed*

**An accrual clause is configured: ExpenseAccrualSetup accrues an expense ahead of its billing, using CodeAccrualTypeID, CurrentAnnualExpense/CurrentPeriodExpense, and optionally IsDailyRent + RentableArea.**

An accrual clause is configured: ExpenseAccrualSetup accrues an expense ahead of its billing, using CodeAccrualTypeID, CurrentAnnualExpense/CurrentPeriodExpense, and optionally IsDailyRent + RentableArea.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | An accrual clause is configured |
| Stated as | `ExpenseAccrualSetup.CodeAccrualTypeID`, `.CurrentAnnualExpense`, `.CurrentPeriodExpense`, `.BeginPeriodName`, `.EndPeriodName`, `.IsDailyRent`, `.RentableArea` |
| Stated as | Accrue an expense ahead of its billing (property tax, insurance) |
| Stated as | Accrual clause |
| Stated as | Observed |

## What it constrains

[ExpenseAccrualSetup](../entities/ExpenseAccrualSetup.md)

Columns named: `ExpenseAccrualSetup.CodeAccrualTypeID`

---

Source: `docs/modules/contracts/rules.md`
