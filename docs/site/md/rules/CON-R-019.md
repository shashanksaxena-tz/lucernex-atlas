# CON-R-019 — 2. Contract identity and hierarchy

*Contracts & Leases · Observed*

**Determining payable vs receivable: direction is carried on ExpenseSetup.IsReceivable and PaymentTransaction.IsReceivable, not on the contract, so one contract can be both.**

Determining payable vs receivable: direction is carried on ExpenseSetup.IsReceivable and PaymentTransaction.IsReceivable, not on the contract, so one contract can be both.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Determining payable vs receivable |
| Stated as | `ExpenseSetup.IsReceivable`, `PaymentTransaction.IsReceivable` |
| Stated as | Direction is carried per-clause and per-transaction, not on the contract. One contract may be both |
| Stated as | Money direction |
| Stated as | Observed |

## What it constrains

[ExpenseSetup](../entities/ExpenseSetup.md), [PaymentTransaction](../entities/PaymentTransaction.md)

Columns named: `ExpenseSetup.IsReceivable`, `PaymentTransaction.IsReceivable`

---

Source: `docs/modules/contracts/rules.md`
