# CON-R-008 — 1. The Clause / Schedule / Transaction / Projection pattern

*Contracts & Leases · Observed*

**Generation is requested: both ExpenseSetup.ReadyForPaymentFlag and ExpenseSchedule.ReadyForPaymentFlag must be true for the row to generate — the fields are observed, the exact gate semantics are inferred.**

Generation is requested: both ExpenseSetup.ReadyForPaymentFlag and ExpenseSchedule.ReadyForPaymentFlag must be true for the row to generate — the fields are observed, the exact gate semantics are inferred.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Generation is requested |
| Stated as | `ExpenseSetup.ReadyForPaymentFlag`, `ExpenseSchedule.ReadyForPaymentFlag` |
| Stated as | Both must be true for the row to generate |
| Stated as | Gate result |
| Stated as | Observed (fields exist); gate semantics Inferred |

## What it constrains

[ExpenseSetup](../entities/ExpenseSetup.md), [ExpenseSchedule](../entities/ExpenseSchedule.md)

Columns named: `ExpenseSetup.ReadyForPaymentFlag`, `ExpenseSchedule.ReadyForPaymentFlag`

---

Source: `docs/modules/contracts/rules.md`
