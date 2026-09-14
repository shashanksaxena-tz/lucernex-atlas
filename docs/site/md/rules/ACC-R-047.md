# ACC-R-047 — Term shortening

*Lease Accounting & Payments · Observed*

**``` ShortenedSchedInitLiabilityBal = initial liability over the remaining periods of the original schedule, restated over the shortened term ShortenedLeaseLiabilityDiff = ShortenedSchedInitLiabilityBal − original.lastPostedPeriod.LiabilityBalance ShortenedTermAssetDiff = −1 × Σ….**

Four formulas, all stated verbatim by the vendor, covering the restated liability and the asset, liability and rent differences.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | early termination / term shortening |
| What it computes | ``` ShortenedSchedInitLiabilityBal = initial liability over the remaining periods of the original schedule, restated over the shortened term ShortenedLeaseLiabilityDiff = ShortenedSchedInitLiabilityBal − original.lastPostedPeriod.LiabilityBalance ShortenedTermAssetDiff = −1 × Σ AssetAmortizationExpense over the remaining periods of the original schedule within the shortened term ShortenedTermRentDiff = new.InitialLiabilityBalance − ShortenedSchedInitLiabilityBal ``` |

## Confidence

Observed, all four stated verbatim

---

Source: `docs/modules/accounting/rules.md`
