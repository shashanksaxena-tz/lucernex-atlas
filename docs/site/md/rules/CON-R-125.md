# CON-R-125 — 10. Suppression and gating

*Contracts & Leases · Observed*

**Any generation or posting: HoldFlag on ExpenseSetup, ExpenseSchedule, ExpenseAccrualSetup, PaymentTransaction or AccrualTransaction is a negative gate at every layer.**

Any generation or posting: HoldFlag on ExpenseSetup, ExpenseSchedule, ExpenseAccrualSetup, PaymentTransaction or AccrualTransaction is a negative gate at every layer.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Any generation or posting |
| Stated as | `HoldFlag` on `ExpenseSetup`, `ExpenseSchedule`, `ExpenseAccrualSetup`, `PaymentTransaction`, `AccrualTransaction` |
| Stated as | Negative gate at every layer |
| Stated as | Suppression |
| Stated as | Observed |

## What it constrains

[ExpenseSetup](../entities/ExpenseSetup.md), [ExpenseSchedule](../entities/ExpenseSchedule.md), [ExpenseAccrualSetup](../entities/ExpenseAccrualSetup.md), [PaymentTransaction](../entities/PaymentTransaction.md), [AccrualTransaction](../entities/AccrualTransaction.md)

---

Source: `docs/modules/contracts/rules.md`
