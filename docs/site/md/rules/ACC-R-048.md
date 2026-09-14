# ACC-R-048 — Impairment

*Lease Accounting & Payments · Observed*

**`TotalImpairmentImpact = ImpairmentAmount + PriorAccumulatedAmortizationBalance`, where `PriorAccumulatedAmortizationBalance` is "the Accumulated Amortization Balance of the accounting period prior to the impairment.".**

Total impairment impact is the impairment plus the prior accumulated amortisation balance. Precedence among the three inputs is unresolved.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | an impairment amount is entered |
| What it reads | `SLSummary.ImpairmentAmount` / `ContractFinancialTest.ImpairmentsAmount` / `Asset.ImpairmentOverride` — all three entered as negative numbers |
| What it computes | `TotalImpairmentImpact = ImpairmentAmount + PriorAccumulatedAmortizationBalance`, where `PriorAccumulatedAmortizationBalance` is "the Accumulated Amortization Balance of the accounting period prior to the impairment." |

## The wording it rests on

> the Accumulated Amortization Balance of the accounting period prior to the impairment.

## What it constrains

[SLSummary](../entities/SLSummary.md), [ContractFinancialTest](../entities/ContractFinancialTest.md), [Asset](../entities/Asset.md)

Columns named: `SLSummary.ImpairmentAmount`, `ContractFinancialTest.ImpairmentsAmount`, `Asset.ImpairmentOverride`

## Confidence

Observed for the sign convention and the formula; ⚠ unresolved which of the three inputs wins when more than one is populated

---

Source: `docs/modules/accounting/rules.md`
