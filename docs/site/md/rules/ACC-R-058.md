# ACC-R-058 — Fiscal / calendar year-end matching

*Lease Accounting & Payments · Observed*

**"This field determines if the program allows for matching of fiscal/calendar year rent.".**

The switch exists and is named; what matching does is inferred, not documented.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | schedule generation and the fiscal-year rollups |
| What it reads | `Program.SLMatchYearEnds` (`Boolean`), `Program.FiscalYearEnd` (`Date` — month and day) |
| The test | "This field determines if the program allows for matching of fiscal/calendar year rent." |

## The wording it rests on

> This field determines if the program allows for matching of fiscal/calendar year rent.

## What it constrains

[Program](../entities/Program.md), [SLSummary](../entities/SLSummary.md), [Contract](../entities/Contract.md)

Columns named: `Program.SLMatchYearEnds`, `Program.FiscalYearEnd`

## Confidence

Observed that the switch exists and what it is named; ⚠ Inferred as to what "matching" does. It is the only setting that could reconcile `SLSummary`'s two parallel rollup families (`Contract`'s `FiscalYear` block against its `CalendarYear` block). Confirm before building

---

Source: `docs/modules/accounting/rules.md`
