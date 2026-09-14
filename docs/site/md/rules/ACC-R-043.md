# ACC-R-043 — Currency translation

*Lease Accounting & Payments · Observed*

**``` AssetTranslationAdjustment = AssetBalance[n] + AssetAmortizationExpense[n] − AssetBalance[n−1] LiabilityTranslationAdjustment = AssetBalance[n] + (Payment[n] − Interest[n]) − AssetBalance[n−1] CumulativeTranslationAdjustment = AssetTranslationAdjustment[n] − LiabilityTranslationAdjustment[n]….**

Four published formulas covering asset, liability, cumulative translation adjustment and liability FX impact.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | FX impact calculated on the Rent Schedule page for a contract with `Contract.IsTranslation = true` |
| What it computes | ``` AssetTranslationAdjustment = AssetBalance[n] + AssetAmortizationExpense[n] − AssetBalance[n−1] LiabilityTranslationAdjustment = AssetBalance[n] + (Payment[n] − Interest[n]) − AssetBalance[n−1] CumulativeTranslationAdjustment = AssetTranslationAdjustment[n] − LiabilityTranslationAdjustment[n] LiabilityFXImpact = (FXrate[n] − FXrate[initial]) × LiabilityBalance[n] ``` |

## Confidence

Observed — all four formulas are printed verbatim in the vendor definitions. ⚠ The `LiabilityTranslationAdjustment` formula as published references the asset balance twice and never the liability balance; it is very likely a documentation error. Do not implement as written

---

Source: `docs/modules/accounting/rules.md`
