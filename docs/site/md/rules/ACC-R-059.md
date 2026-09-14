# ACC-R-059 — Per-column FX rate-type selection

*Lease Accounting & Payments · Observed*

**the `Sub` variant applies to "contracts in need of translation", the plain variant to "contracts in need of revaluation" — selected per contract by `Contract.IsTranslation` (`ACC-R-044`).**

The rate type is chosen per schedule column at portfolio level, not once per firm.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | currency conversion of a schedule column |
| What it reads | fourteen `Program` code fields — seven schedule columns × two modes: |
| The test | the `Sub` variant applies to "contracts in need of translation", the plain variant to "contracts in need of revaluation" — selected per contract by `Contract.IsTranslation` (`ACC-R-044`) |
| What it writes | the exchange rate applied to each `SLPeriod` `*Translated` column |
| Rebuild note | this partly answers the `ACC-R-044` open question. The Translation-vs-Revaluation mapping referenced by `Contract.IsTranslation` is portfolio-scoped and column-by-column, not a single firm-wide toggle. The `Exchange Rate Type Code` values themselves are still unknown. --- ## J. The ASC 842 approval workflow *Added 2026-09-10 from the live tenant. The full capture is in `docs/modules/layouts-and-forms/forms-vs-pages-vs-layouts.md`.* |

## The wording it rests on

> contracts in need of translation

## What it constrains

[Program](../entities/Program.md), [Contract](../entities/Contract.md), [SLPeriod](../entities/SLPeriod.md)

Columns named: `Contract.IsTranslation`

## Rules it cites

[ACC-R-044](ACC-R-044.md)

## Confidence

Observed, all fourteen definitions

---

Source: `docs/modules/accounting/rules.md`
