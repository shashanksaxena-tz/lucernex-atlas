# ACC-R-045 — Schedule supersession

*Lease Accounting & Payments · Observed*

**``` new.PriorLastPostedPeriodID := old.SLSummaryID new.PostedEndDate := old.LastPostedEndDate new.PostedInitAssetAdj := new.InitialAssetBalance − old.AssetBalance(as of PostedEndDate) new.PostedInitLiabilityAdj := new.InitialLiabilityBalance − old.LiabilityBalance(as of PostedEndDate)….**

Creating a replacement schedule links it to its predecessor, copies the posted cut-off date, computes four adjustment figures, and marks the predecessor inactive.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | a replacement `SLSummary` is created for a contract |
| What it writes | ``` new.PriorLastPostedPeriodID := old.SLSummaryID new.PostedEndDate := old.LastPostedEndDate new.PostedInitAssetAdj := new.InitialAssetBalance − old.AssetBalance(as of PostedEndDate) new.PostedInitLiabilityAdj := new.InitialLiabilityBalance − old.LiabilityBalance(as of PostedEndDate) new.PostedAssetAdjustment := new.AssetBalance − old.lastPostedAssetBalance new.PostedLiabilityAdjustment := new.LiabilityBalance − old.lastPostedLiabilityBalance old.Inactive := true old.InactiveDate := today ``` |

## What it constrains

[SLSummary](../entities/SLSummary.md)

## Confidence

Observed for every one of the six field definitions; Derived that they occur together as one transaction

---

Source: `docs/modules/accounting/rules.md`
