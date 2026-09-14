# CON-R-032 — 3. Recurring expense: setup and schedule

*Contracts & Leases · Derived*

**Determining billing frequency: CodeFrequencyID, NumberOfPayments and PaymentDueDay drive the number and spacing of ExpenseSchedule rows.**

Determining billing frequency: CodeFrequencyID, NumberOfPayments and PaymentDueDay drive the number and spacing of ExpenseSchedule rows.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Determining billing frequency |
| Stated as | `ExpenseSetup.CodeFrequencyID`, `NumberOfPayments`, `PaymentDueDay` |
| Stated as | Drives the number and spacing of `ExpenseSchedule` rows |
| Stated as | Period grid |
| Stated as | Derived |

## What it constrains

[ExpenseSetup](../entities/ExpenseSetup.md), [ExpenseSchedule](../entities/ExpenseSchedule.md)

Columns named: `ExpenseSetup.CodeFrequencyID`

---

Source: `docs/modules/contracts/rules.md`
