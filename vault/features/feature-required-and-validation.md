---
title: Required and validation
tags: [feature, validation, core]
evidence: Observed
---

How Lx decides a field must be filled — and the answer is **not one flag**. See [[required-ness]].

- Column flag and catalog flag agree on **5,650 of 5,694** jointly observable fields (**99.2%**) and
  **disagree on 44, in both directions**. Neither is a subset of the other.
- **603 of 6,487** fields (9.3%) carry the column required flag. `BOMapClientRecordID` is required on
  **133 of 202** tables — which is how it was confirmed as the upsert key.
- [[PageLayoutField]] has exactly **20 columns and none named `IsRequired` or `IsReadOnly`**.
- `showAndRequire` is used **0 of 50** times; `hide` **0**; all 50 are `show`.
- **[[finding-no-layout-level-required]]** closes it: the asterisk is schema-required, rendered at
  paint time. `DisplayOption1`/`DisplayOption2` — the last standing candidate — is eliminated, and
  what the bits actually track is **data type**.

A distinct fifth mechanism does exist and is **validation, not required-ness**:
`FieldValidationMinValue` (42 placements), `FieldValidationMaxValue` (29), `EditModeDefaultValue`
(133), `FieldScript` (67).

And **read-only is `View` in [[security-ladder|Field Security]]**, not a field property — which is why
the catalog's uniform `ReadOnly = No` across 6,158 leaves is correct rather than anomalous.

Scale: [[Contract]] has 307 columns and requires **7**, none a business fact.

[`features/required-and-validation/`](../../docs/features/required-and-validation/README.md)
