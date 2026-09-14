# ACC-R-018 — Asset-level accounting date override (equipment leases)

*Lease Accounting & Payments · Observed*

**if the override dates are populated they set the test/schedule window; otherwise the window comes from the expense schedule dates.**

On an equipment lease, asset-level override dates set the window; if blank, the asset's expense schedule dates do.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | test or schedule run for an `Asset` |
| What it reads | `Asset.AccountingBeginDate`, `Asset.AccountingEndDate`, the asset's expense schedules |
| The test | if the override dates are populated they set the test/schedule window; otherwise the window comes from the expense schedule dates |

## The wording it rests on

> If you do not enter override dates, the test and schedules will run based on the dates of the expense schedules for the asset.

## What it constrains

[Asset](../entities/Asset.md)

Columns named: `Asset.AccountingBeginDate`, `Asset.AccountingEndDate`

## Confidence

Observed — "If you do not enter override dates, the test and schedules will run based on the dates of the expense schedules for the asset."

---

Source: `docs/modules/accounting/rules.md`
