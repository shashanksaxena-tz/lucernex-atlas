# ACC-R-051 — Posting state and the closed cut-line

*Lease Accounting & Payments · Observed*

**`SLSummary.LastPostedDate` = begin date of the last posted period; `LastPostedEndDate` = its end date; `LastBalancePosted` = "the asset minus the liability as of the last posted period"; `LastPostedBalanceSheetImpact` = "the portion of the last posted balance that is to remain on the balance sheet.".**

The last posted period's end date is the boundary all remeasurement deltas are taken against.

## Stated for a rule engine

|  |  |
|---|---|
| What it reads | `SLPeriod.RecordStatus` ∈ {posted, not posted, mixed}; `SLPeriod.PostedDate` |
| What it writes | `SLSummary.LastPostedDate` = begin date of the last posted period; `LastPostedEndDate` = its end date; `LastBalancePosted` = "the asset minus the liability as of the last posted period"; `LastPostedBalanceSheetImpact` = "the portion of the last posted balance that is to remain on the balance sheet." |

## The wording it rests on

> the asset minus the liability as of the last posted period

## What it constrains

[SLPeriod](../entities/SLPeriod.md), [SLSummary](../entities/SLSummary.md)

Columns named: `SLPeriod.RecordStatus`, `SLPeriod.PostedDate`, `SLSummary.LastPostedDate`

## Rules it cites

[ACC-R-045](ACC-R-045.md)

## Confidence

Observed for every definition; Derived that `LastPostedEndDate` is the closed/open boundary against which ACC-R-045 measures its deltas

---

Source: `docs/modules/accounting/rules.md`
