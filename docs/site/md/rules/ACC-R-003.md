# ACC-R-003 — Asset-level discount rate override

*Lease Accounting & Payments · Observed*

**if populated, it supersedes ACC-R-001/002 for that asset.**

An equipment asset may carry its own rate, which supersedes both.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | schedule generation for an equipment lease |
| What it reads | `Asset.DiscountRateOverride` (`sTYPE_PERCENTAGE`) |
| The test | if populated, it supersedes ACC-R-001/002 for that asset |
| What it writes | the rate used in the asset's schedule |

## The wording it rests on

> If this equipment uses a different discount rate, enter the discount rate in this field.

## What it constrains

[Asset](../entities/Asset.md)

Columns named: `Asset.DiscountRateOverride`

## Rules it cites

[ACC-R-001](ACC-R-001.md)

## Confidence

Observed — "If this equipment uses a different discount rate, enter the discount rate in this field."

---

Source: `docs/modules/accounting/rules.md`
