# ACC-R-022 — Accounting method change requires remeasurement

*Lease Accounting & Payments · Observed*

**the schedule must be remeasured.**

Vendor definition of the accounting method field: "If its value is changed, you will need to remeasure your schedule." It states the consequence, not whether the flag is set.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | `SLSummary.CodeAccountingMethodID` is changed |
| What it writes | the schedule must be remeasured |

## The wording it rests on

> If its value is changed, you will need to remeasure your schedule.

## What it constrains

[SLSummary](../entities/SLSummary.md)

Columns named: `SLSummary.CodeAccountingMethodID`

## Confidence

Observed — "If its value is changed, you will need to remeasure your schedule." ⚠ Note this states the consequence, not that `NeedsRecalculation` is set; whether it is, is unconfirmed

---

Source: `docs/modules/accounting/rules.md`
