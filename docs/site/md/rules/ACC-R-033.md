# ACC-R-033 — Initial asset balance

*Lease Accounting & Payments · Inferred*

**not documented. The vendor says only "This is a calculated value which contains the initial value over the asset of the lease.".**

Standard practice is liability + prepaid rent + initial direct costs − lease incentives, and all four fields exist, but the actual formula is not stated. Do not code from the schema alone.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | schedule generation |
| What it reads | `InitialLiabilityBalance`, `InitialDirectCostAmount`, `LeaseIncentiveAmount`, `PreCommencePayAmount`, `DismantlingStorageCostAmount`, `InitialAssetBalanceAdjust` |
| What it computes | not documented. The vendor says only "This is a calculated value which contains the initial value over the asset of the lease." |
| What it writes | `SLSummary.InitialAssetBalance` |

## The wording it rests on

> This is a calculated value which contains the initial value over the asset of the lease.

## What it constrains

[SLSummary](../entities/SLSummary.md)

Columns named: `SLSummary.InitialAssetBalance`

## Confidence

Inferred — the standard ASC 842-20-30-5 build-up is `liability + prepaid + IDC − incentives`, and all four component fields exist on `SLSummary`, but the actual formula is not stated anywhere offline. ⚠ Do not code this from the schema alone

---

Source: `docs/modules/accounting/rules.md`
