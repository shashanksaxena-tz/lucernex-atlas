# ACC-R-028 — Period row generation

*Lease Accounting & Payments · Derived*

**one `SLPeriod` per fiscal period, carrying `BeginDate`, `EndDate`, `NumberDays`, `FiscalPeriod`, `FiscalPeriodYear`, `CumulativePeriodNumber`.**

One period row per fiscal period between the schedule's begin and end dates, taken from the portfolio's fiscal calendar.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | schedule generation |
| What it reads | `FiscalPeriod` rows for the contract's `ProgramID` covering `SLSummary.BeginDate` … `EndDate` |
| What it computes | one `SLPeriod` per fiscal period, carrying `BeginDate`, `EndDate`, `NumberDays`, `FiscalPeriod`, `FiscalPeriodYear`, `CumulativePeriodNumber` |
| What it writes | N `SLPeriod` rows; `SLSummary.SLTermLength` = "The number of periods in the straight line schedule term." |

## The wording it rests on

> The number of periods in the straight line schedule term.

## What it constrains

[FiscalPeriod](../entities/FiscalPeriod.md), [SLSummary](../entities/SLSummary.md), [SLPeriod](../entities/SLPeriod.md)

Columns named: `SLSummary.BeginDate`, `SLSummary.SLTermLength`, `SLPeriod.FiscalPeriod`

## Confidence

Derived — `FiscalPeriod` is described in `docs/data-fields/INDEX.md` as "the calendar backbone that SLPeriod, ExpenseSchedule, and Sales fiscal-period fields reference", and 12- or 13-period years are documented on `SLPeriod.FiscalPeriod`

---

Source: `docs/modules/accounting/rules.md`
