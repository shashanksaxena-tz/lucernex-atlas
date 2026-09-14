---
title: Required-ness has no layout-level layer
tags: [finding, validation, layouts, core]
evidence: Observed
---

> **The builder's red asterisk is schema-required, rendered at paint time. There is no layout-level
> required layer at all.**

The clean test is the [[screen-manage-discount-rates|discount-rate list layout]] (`PageLayoutID
88572`), whose grid has four asterisked columns against six plain ones **on a single layout**:

| Column | Asterisked | Schema `required` |
|---|:--:|:--:|
| `DiscountRate` · `EffectiveThroughDate` · `MinSchedMons` · `MaxSchedMons` | ✳ | **Yes** |
| `Country` · `State / Province` · `Portfolio` · `Accounting Method` · `Use Type` · `Notes` | — | No |

The [[DiscountRate]] table has **exactly four** required columns and they are **exactly the four** the
builder marks. **4 of 4 and 6 of 6, no exception in either direction.**

`DisplayOption1`/`DisplayOption2` — the last standing candidate — is eliminated, and the bit pattern
shows why it was never going to work: bit 3 is set on `EffectiveThroughDate` and `DiscountRate` but
**not** the two Length fields; bits 14+27 on the Lengths and `DiscountRate` but **not** the date.
**No single bit covers the asterisked set.** What the bits track is **data type**.

**What this means for ASG Edge+:** do not build a per-placement required flag. The absence of an
`IsRequired` column on [[PageLayoutField]], noted repeatedly in this corpus as a puzzle, **is the
design, not an omission**.

### The counterexample, and how it closed

`docs/admin/008` reported `Contract Status` and `Location` painted red in the layout builder when
neither is schema-required on [[Contract]]. **On the rendered end-user screen neither is marked
required** ([[screen-eq-details-summary]]). **The builder's red text is an editor affordance that does
not reach the end user.**

### A method failure worth recording

The test three separate parties designed **could never have worked**. Layout `98927` was chosen on the
assumption it placed `Contract Status`, `Location` and `Master Contract`. **It does not** — its 22
placements are `Notes`, six action buttons, five Sub Edit Forms and six section headers. **Nobody
checked the layout contained the fields before building a comparison around them.** See
[[method-cheap-signals]].

See [[required-ness]] · [[feature-required-and-validation]]
