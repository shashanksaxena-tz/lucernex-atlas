# ACC-R-056 — Amortisation basis: Per Day or Per Period

*Lease Accounting & Payments · Observed*

**- `PER_PERIOD` ⇒ "distributes the amortization equally among periods"; - `PER_DAY` ⇒ "distributes the amortization according to the number of days in the period", i.e. weight each period by `SLPeriod.NumberDays`.**

Three independent switches, one per schedule column. Do not collapse them into one.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | schedule generation |
| What it reads | `Program.SLAssetAmortizeMethod`, `Program.SLCashAmortizeMethod`, `Program.SLExpenseAmortizeMethod` — three independent `sTYPE_TEXT` switches, one per schedule column |
| The test | - `PER_PERIOD` ⇒ "distributes the amortization equally among periods"; - `PER_DAY` ⇒ "distributes the amortization according to the number of days in the period", i.e. weight each period by `SLPeriod.NumberDays` |
| What it writes | `SLPeriod.PeriodAssetAmortizationExpense` (asset switch), `SLPeriod.PeriodCashAmount` (cash switch), `SLPeriod.PeriodExpenseAmount` (expense switch) |
| Scope restriction | ⚠ "This setting impacts only ASC 842 Finance leases." — stated on the asset switch. The cash and expense switches carry no such restriction |
| Rebuild note | three separate switches, not one. A single "amortisation basis" setting in ASG Edge+ would be a behavio |

## The wording it rests on

> distributes the amortization equally among periods

## What it constrains

[Program](../entities/Program.md), [SLPeriod](../entities/SLPeriod.md)

Columns named: `Program.SLAssetAmortizeMethod`, `Program.SLCashAmortizeMethod`, `Program.SLExpenseAmortizeMethod`, `SLPeriod.NumberDays`, `SLPeriod.PeriodAssetAmortizationExpense`, `SLPeriod.PeriodCashAmount`, `SLPeriod.PeriodExpenseAmount`

## Confidence

Observed. The GraphQL enum `GaapAmortizeMode { PER_DAY, PER_PERIOD }` is the API-level name for the value these three columns hold; the columns themselves are typed `Text` in the schema dump, so the enum is the authoritative value list. (Sources: `_xlsx_lucernex_jcrew.txt`; `docs/data-model/graphql-api.md`.)

---

Source: `docs/modules/accounting/rules.md`
