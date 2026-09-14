# CON-R-049 — 4. Escalations

*Contracts & Leases · Observed*

**Increase/decrease asymmetry: ExpenseSetup.AmountIncreaseCap/AmountDecreaseCap/PercentIncreaseCap/PercentDecreaseCap are a separate, parallel collar to ExpenseEscalation's own min/max, with unspecified precedence between the two.**

Increase/decrease asymmetry: ExpenseSetup.AmountIncreaseCap/AmountDecreaseCap/PercentIncreaseCap/PercentDecreaseCap are a separate, parallel collar to ExpenseEscalation's own min/max, with unspecified precedence between the two.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Increase/decrease asymmetry |
| Stated as | `ExpenseSetup.AmountIncreaseCap`, `AmountDecreaseCap`, `PercentIncreaseCap`, `PercentDecreaseCap` |
| Stated as | Separate caps for upward and downward movement, in addition to `ExpenseEscalation`'s min/max. Precedence unspecified |
| Stated as | Bounded amount |
| Stated as | Observed |

## What it constrains

[ExpenseSetup](../entities/ExpenseSetup.md), [ExpenseEscalation](../entities/ExpenseEscalation.md)

Columns named: `ExpenseSetup.AmountIncreaseCap`

---

Source: `docs/modules/contracts/rules.md`
