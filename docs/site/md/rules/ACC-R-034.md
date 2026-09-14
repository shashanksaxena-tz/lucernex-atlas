# ACC-R-034 — Balance forward and its split

*Lease Accounting & Payments · Observed*

**``` BalanceForward = InitialAssetBalance − InitialLiabilityBalance BalanceForward = RemeasurementBalanceForward + ProfitAndLossImpact ```.**

BalanceForward = InitialAssetBalance − InitialLiabilityBalance, and it equals RemeasurementBalanceForward + ProfitAndLossImpact.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | schedule creation that carries balances from a prior schedule |
| What it computes | ``` BalanceForward = InitialAssetBalance − InitialLiabilityBalance BalanceForward = RemeasurementBalanceForward + ProfitAndLossImpact ``` |
| What it writes | `BalanceForward`, `RemeasurementBalanceForward` (label "Balance Sheet Impact"), `ProfitAndLossImpact` |

## The wording it rests on

> ), `ProfitAndLossImpact`. - Confidence: Observed for the first identity (

## Confidence

Observed for the first identity ("The difference between the asset and liability balance at the start of your accounting schedule"); Derived for the split, from "the portion of the balance forward that does appear on the balance sheet going forward" and "the portion of the balance forward that will not persist on the balance sheet and is taken as a capital gain or loss."

---

Source: `docs/modules/accounting/rules.md`
