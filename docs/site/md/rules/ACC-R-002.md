# ACC-R-002 — Contract-level discount rate override

*Lease Accounting & Payments · Inferred*

**if `Contract.DiscountRate` is populated it is the rate used; otherwise `ComputedSLDiscountRate`.**

A rate typed directly on the contract is used ahead of the resolved default. The precedence is not stated by the vendor.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | schedule generation or classification test |
| What it reads | `Contract.DiscountRate` (INPUT), `Contract.ComputedSLDiscountRate` (COMPUTED) |
| The test | if `Contract.DiscountRate` is populated it is the rate used; otherwise `ComputedSLDiscountRate` |
| What it writes | `SLSummary.DiscountRate`, `ContractFinancialTest.DiscountRate` |

## What it constrains

[Contract](../entities/Contract.md), [SLSummary](../entities/SLSummary.md), [ContractFinancialTest](../entities/ContractFinancialTest.md)

Columns named: `Contract.DiscountRate`, `Contract.ComputedSLDiscountRate`, `SLSummary.DiscountRate`, `ContractFinancialTest.DiscountRate`

## Confidence

Inferred — the two fields coexist and `ComputedSLDiscountRate` is explicitly the default, but no vendor text states the precedence

---

Source: `docs/modules/accounting/rules.md`
