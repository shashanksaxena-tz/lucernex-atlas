# ACC-R-054 — Accrual transaction immutability

*Lease Accounting & Payments · Observed*

**"Warning - once you mark a transaction as processed, you cannot change it.".**

Processed accrual transactions are frozen.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | `AccrualTransaction.ProcessedFlag := true` |
| The test | "Warning - once you mark a transaction as processed, you cannot change it." |

## The wording it rests on

> Warning - once you mark a transaction as processed, you cannot change it.

## Confidence

Observed

---

Source: `docs/modules/accounting/rules.md`
