# ACC-R-030 — Suppress ROU asset amortization

*Lease Accounting & Payments · Inferred*

**if true, no asset amortization is recognised for schedules of this type.**

If the flag is set, no asset amortisation is recognised. Inferred from the field name — the only rule in the module resting on naming alone, and now known to be inert in production.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | schedule generation |
| What it reads | the schedule type's `DontAmortizeAssetValue` (Boolean) |
| The test | if true, no asset amortization is recognised for schedules of this type |
| What it writes | `SLPeriod.PeriodAssetAmortizationExpense` suppressed |

## What it constrains

[SLPeriod](../entities/SLPeriod.md)

Columns named: `SLPeriod.PeriodAssetAmortizationExpense`

## Confidence

Inferred — the field is the only behavioural switch on the three code tables and its name is unambiguous, but it has no vendor definition. - ⚠ Inert in this tenant. The only configured schedule type, `842 Rent`, has `Don't Amortize Asset Value` unchecked, and the other two schedule-type tables are empty. The flag therefore has no observable effect on any ASG data, so this rule cannot be validated here and stays permanently Inferred until a vendor answer or a tenant that sets it. Observed, 2026-09-10. --- ## E. Measurement

---

Source: `docs/modules/accounting/rules.md`
