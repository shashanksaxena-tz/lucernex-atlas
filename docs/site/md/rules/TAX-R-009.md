# TAX-R-009 — Property tax is explicitly a recoverable (CAM) expense, not merely an expense

*Property Tax · Observed*

**Input: `PropertyTaxSummary.CodeRecoveryGroupID`/`.CodeRecoveryTypeID`. Effect: Ties this module directly into the CAM/expense-recovery engine (`../accounting/README.md`'s "out of scope but adjacent" list) — a tax summary is not just billed, it is (at least potentially) passed through to tenants….**

Input: `PropertyTaxSummary.CodeRecoveryGroupID`/`.CodeRecoveryTypeID`. Effect: Ties this module directly into the CAM/expense-recovery engine (`../accounting/README.md`'s "out of scope but adjacent" list) — a tax summary is not just billed, it is (at least potentially) passed through to tenants under a recovery group/type classification. Confidence: Observed (field presence); the recovery mechanism itself is out of this module's scope to document further.

## The wording it rests on

> out of scope but adjacent

## What it constrains

[PropertyTaxSummary](../entities/PropertyTaxSummary.md)

Columns named: `PropertyTaxSummary.CodeRecoveryGroupID`

## Confidence

Observed (field presence); the recovery mechanism itself is out of this module's scope to document further

---

Source: `docs/modules/property-tax/rules.md`
