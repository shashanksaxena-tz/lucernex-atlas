# ACC-R-019 — Covenant-sourced measurement adjustments

*Lease Accounting & Payments · Observed*

**the covenant amount is pulled into the accounting assumptions and the accounting schedule only if `CodeAccountingAdjustmentTypeID` ∈ {`Purchase Option`, `Cancellation Option`, `Residual Value Guarantee`}.**

Only the three named adjustment types flow into the accounting.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | classification test or schedule creation |
| What it reads | `Covenant.CovenantAmount`, `Covenant.CodeAccountingAdjustmentTypeID`, `Covenant.TotalRVGAmount`, `Covenant.ThirdPartyRVGAmount` |
| The test | the covenant amount is pulled into the accounting assumptions and the accounting schedule only if `CodeAccountingAdjustmentTypeID` ∈ {`Purchase Option`, `Cancellation Option`, `Residual Value Guarantee`} |
| What it writes | `ContractFinancialTest.PurchaseOptionAmount` / `.CancellationOptionAmount` / `.ResidualValueGuarantees`, and the same three fields on `SLSummary` |

## The wording it rests on

> This amount will be pulled into your accounting assumptions and accounting schedule if the covenant has one of three accounting adjustment types: Purchase Option, Cancellation Option, or Residual Value guarantee.

## What it constrains

[Covenant](../entities/Covenant.md), [ContractFinancialTest](../entities/ContractFinancialTest.md), [SLSummary](../entities/SLSummary.md)

Columns named: `Covenant.CovenantAmount`, `Covenant.CodeAccountingAdjustmentTypeID`, `Covenant.TotalRVGAmount`, `Covenant.ThirdPartyRVGAmount`, `ContractFinancialTest.PurchaseOptionAmount`

## Confidence

Observed — "This amount will be pulled into your accounting assumptions and accounting schedule if the covenant has one of three accounting adjustment types: Purchase Option, Cancellation Option, or Residual Value guarantee." --- ## C. Recalculation triggers

---

Source: `docs/modules/accounting/rules.md`
