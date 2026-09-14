# ACC-R-031 — Initial liability balance

*Lease Accounting & Payments · Observed*

**`InitialLiabilityBalance = Σ PVOfPeriodCashAmount`.**

Sum the present value of every period's cash payment across the life of the lease.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | schedule generation |
| What it reads | `SLPeriod.PVOfPeriodCashAmount` for every period |
| What it computes | `InitialLiabilityBalance = Σ PVOfPeriodCashAmount` |
| What it writes | `SLSummary.InitialLiabilityBalance`, `SLPeriod.InitialLiabilityBalance` |

## The wording it rests on

> This is the total of all of the Period Payment Present Values over the life of the lease.

## What it constrains

[SLPeriod](../entities/SLPeriod.md), [SLSummary](../entities/SLSummary.md)

Columns named: `SLPeriod.PVOfPeriodCashAmount`, `SLSummary.InitialLiabilityBalance`, `SLPeriod.InitialLiabilityBalance`

## Confidence

Observed — "This is the total of all of the Period Payment Present Values over the life of the lease."

---

Source: `docs/modules/accounting/rules.md`
