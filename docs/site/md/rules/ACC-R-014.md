# ACC-R-014 — Propagation of the authoritative result

*Lease Accounting & Payments · Observed*

**take the most recently locked row's `FinalResult`.**

The most recently locked test's verdict propagates to the contract.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | a `ContractFinancialTest` is locked |
| What it reads | all `ContractFinancialTest` rows for the contract with `IsLocked = true` |
| What it computes | take the most recently locked row's `FinalResult` |
| What it writes | `Contract.LatestFinancialTestFinalResult` |

## The wording it rests on

> The final result of the most recently locked ASC 842 test.

## What it constrains

[ContractFinancialTest](../entities/ContractFinancialTest.md), [Contract](../entities/Contract.md)

Columns named: `Contract.LatestFinancialTestFinalResult`

## Confidence

Observed — "The final result of the most recently locked ASC 842 test."

---

Source: `docs/modules/accounting/rules.md`
