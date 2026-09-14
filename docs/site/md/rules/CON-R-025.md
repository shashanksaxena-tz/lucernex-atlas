# CON-R-025 — 2. Contract identity and hierarchy

*Contracts & Leases · Observed*

**Computing rent rollups: 120 denormalised sTYPE_MONEY fields on Contract cross {Calendar,Fiscal}×{Base,Total}×{with,without tax}×{period buckets}.**

Computing rent rollups: 120 denormalised sTYPE_MONEY fields on Contract cross {Calendar,Fiscal}×{Base,Total}×{with,without tax}×{period buckets}.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Computing rent rollups |
| Stated as | `ExpenseSchedule` rows |
| Stated as | 120 denormalised `sTYPE_MONEY` fields on `Contract` across `{Calendar, Fiscal} × {Base, Total} × {with, without tax} × {Aggregate, Current Annual/Monthly/Period, Next, 3rd–6th, Beyond 5th/6th, Remaining Obligation, Q1–Q4}` |
| Stated as | Precomputed rollups |
| Stated as | Observed |

## What it constrains

[ExpenseSchedule](../entities/ExpenseSchedule.md), [Contract](../entities/Contract.md)

---

Source: `docs/modules/contracts/rules.md`
