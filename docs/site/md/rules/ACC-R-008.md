# ACC-R-008 — Test 3 override: commencement near end of economic life

*Lease Accounting & Payments · Observed*

**`IsLeaseNearEnd = true` ⇒ `Test3Result := Pass`, unconditionally.**

The 'lease is near end' tick box forces a Pass unconditionally.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | after ACC-R-007 |
| What it reads | `IsLeaseNearEnd` (`sTYPE_CHECKBOX`) |
| The test | `IsLeaseNearEnd = true` ⇒ `Test3Result := Pass`, unconditionally |
| What it writes | `Test3Result` |

## The wording it rests on

> If this check box is selected, Test 3's outcome will change to Pass regardless of whether the value the Test Term Length to Remaining Life field is greater than the Remaining Economic Life Threshold field.

## Rules it cites

[ACC-R-007](ACC-R-007.md)

## Confidence

Observed — "If this check box is selected, Test 3's outcome will change to Pass regardless of whether the value the Test Term Length to Remaining Life field is greater than the Remaining Economic Life Threshold field."

---

Source: `docs/modules/accounting/rules.md`
