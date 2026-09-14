# ACC-R-009 — Test 4: substantially all of fair value

*Lease Accounting & Payments · Observed*

**`InitialLiabilityBalance > ThresholdFairValueControlled` ⇒ Fail. Default threshold "usually set to 90%".**

Fair value times the portion controlled times the threshold gives the benchmark; a liability above it fails. Which liability figure is used is ambiguous.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | classification test run |
| What it reads | `FairValueOfAsset`, `PortionOfAssetControlled`, `FairValueThreshold`, an initial liability balance |
| The test | `InitialLiabilityBalance > ThresholdFairValueControlled` ⇒ Fail. Default threshold "usually set to 90%" |
| What it computes | ``` FairValueControlled = FairValueOfAsset × PortionOfAssetControlled ThresholdFairValueControlled = FairValueControlled × FairValueThreshold InitLiabilityBalToThreshFairValueCtrld = InitialLiabilityBalance ÷ ThresholdFairValueControlled ``` |
| What it writes | `FairValueControlled`, `ThresholdFairValueControlled`, `InitLiabilityBalToThreshFairValueCtrld`, `Test4Result`. - Threshold source ↑ upgraded: the default comes from `Program.FairValueThreshold` — "Enter the fraction of the fair value of the underlying asset that you would like to test against to determine whether to treat this lease as a financing- / purchase-type lease or an operating lease. This value is usually set to 90%. This field is used in the ASC 842 Test." This is also the first Observed statement that the fair-value test is what decides finance vs. operating |

## The wording it rests on

> . - Output: `FairValueControlled`, `ThresholdFairValueControlled`, `InitLiabilityBalToThreshFairValueCtrld`, `Test4Result`. - Threshold source ↑ upgraded: the default comes from `Program.FairValueThreshold` —

## What it constrains

[Program](../entities/Program.md)

Columns named: `Program.FairValueThreshold`

## Confidence

Observed for all three formulas and the fail condition. ⚠ Which initial liabi

---

Source: `docs/modules/accounting/rules.md`
