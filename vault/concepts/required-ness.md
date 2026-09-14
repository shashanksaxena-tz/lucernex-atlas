---
title: Required-ness
tags: [concept, validation, core]
evidence: Observed
---

There is no single "required" flag. There are three layers, only two of them storage, and a fourth
that is never used.

| Layer | What it expresses | Where |
|---|---|---|
| Schema `required` | `NOT NULL` at storage | the column |
| Catalog `Required` | *the user must supply this when creating the record* — additionally covers **parent linkage** | [[ReportGroupAvailableField]] |
| Conditional `showAndRequire` | required *only when* a rule matches | `PageLayoutField.JSONConfigText` — **used zero times** |

**The first two are not one flag twice.** On the correct denominator they agree on **5,650 of 5,694**
fields (99.2%) and disagree on **44 in both directions**: 42 catalogue-Yes/schema-No cases are all
owner foreign keys (`ContractID` on 34 tables, `ProjectEntityID` on 8), and 2 reverse cases are
[[ProjectEntity]] audit columns. Neither is a subset of the other. A rebuild needs both — `NOT NULL`
cannot express *"you must pick a parent Contract when creating an Allowance"*.

**And there is no fourth layer.** The red asterisk in the builder is
[[finding-no-layout-level-required|schema-required, rendered at paint time]]. `DisplayOption1` /
`DisplayOption2` were the last standing candidate and are eliminated: no single bit covers the
asterisked set, and what the bits actually track is **data type**.

A separate, fifth thing does exist and is not required-ness: per-placement **validation** —
`FieldValidationMinValue` on 42 placements, `FieldValidationMaxValue` on 29, `EditModeDefaultValue`
on 133, `FieldScript` on 67.

For scale: [[Contract]] has 307 columns and requires **7**, none of them a business fact.

Source: [`features/required-and-validation/`](../../docs/features/required-and-validation/README.md)
