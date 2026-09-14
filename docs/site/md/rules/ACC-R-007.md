# ACC-R-007 — Test 3: major part of remaining economic life

*Lease Accounting & Payments · Observed*

**`< RemainingEconomicLifeThreshold` ⇒ Pass; otherwise Fail. Default threshold "usually set to 75%".**

Test term divided by remaining life, compared against the threshold. The default threshold comes from the portfolio.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | classification test run |
| What it reads | `TestTermLength`, `RemainingLife`, `CodeRemainingLifeFreqUnitID`, `RemainingEconomicLifeThreshold` |
| The test | `< RemainingEconomicLifeThreshold` ⇒ Pass; otherwise Fail. Default threshold "usually set to 75%" |
| What it computes | `ComputedTestTermLengthToRemainingLife = TestTermLength / RemainingLife` (both normalised to `CodeRemainingLifeFreqUnitID`) |
| What it writes | `ComputedTestTermLengthToRemainingLife` (`sTYPE_PERCENTAGE`), `Test3Result`. - Threshold source ↑ upgraded: the default comes from `Program.RemainingEconomicLifeThreshold` — "Enter the fraction of the economic life of the underlying asset that amounts to a major part of the scheduled accounting period. This value is usually set to 75%. This field is used in the ASC 842 Test." `Contract.RemainingEconomicLifeThreshold` resolves portfolio-level first, then firm-level (ACC-R-004's pattern) |

## The wording it rests on

> . - Output: `ComputedTestTermLengthToRemainingLife` (`sTYPE_PERCENTAGE`), `Test3Result`. - Threshold source ↑ upgraded: the default comes from `Program.RemainingEconomicLifeThreshold` —

## What it constrains

[Program](../entities/Program.md), [Contract](../entities/Contract.md)

Columns named: `Program.RemainingEconomicLifeThreshold`, `Contract.RemainingEconomicLifeThreshold`

## Rules it cites

[ACC-R-004](ACC-R-004.md)

## Confidence

Observed — "The value of this field is the Term Length (based on Test) divided by the Remaining Economic Life. The comparison of this percentage to the Remaining Economic Life Threshold determines the pass / fail value displayed for the Test 3 result."

---

Source: `docs/modules/accounting/rules.md`
