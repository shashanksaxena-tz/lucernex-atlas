# ACC-R-055 — Alternate-rent hold propagation

*Lease Accounting & Payments · Observed*

**a hold flag is set on all recurring-expense transactions (resp. percentage-rent transactions) generated during the window.**

A hold flag is set on transactions generated during the window.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | rent generation while the contract is in an alternate-rent window |
| What it reads | `AlternateRentSchedule.SetExpHoldFlag`, `.SetPRHoldFlag`, `.BeginDate`, `.EndDate` |
| What it writes | a hold flag is set on all recurring-expense transactions (resp. percentage-rent transactions) generated during the window |

## What it constrains

[AlternateRentSchedule](../entities/AlternateRentSchedule.md), [Program](../entities/Program.md)

Columns named: `AlternateRentSchedule.SetExpHoldFlag`, `AlternateRentSchedule.SuspendSL`

## Confidence

Observed. ⚠ These do not affect the accounting schedule; they are cash-side controls. `AlternateRentSchedule.SuspendSL` — the one field whose name suggests schedule suspension — is documented as "no longer used." --- ## I. Portfolio-level accounting policy (`Program`) *Added 2026-09-10 from the live tenant. `Program` — the object the UI calls Portfolio — is the accounting engine's policy carrier, and round one of this document missed it. It holds the discount rate, both ASC 842 thresholds, three amortisation-basis switches, two proration switches, the fiscal year end, and fourteen FX rate-type selectors. Everything here is Observed from vendor field definitions in `_xlsx_lucernex_jcrew.txt`.*

---

Source: `docs/modules/accounting/rules.md`
