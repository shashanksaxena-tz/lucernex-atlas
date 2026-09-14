---
title: PageLayoutField
tags: [entity, layouts, core]
evidence: Observed
---

**20 columns over REST · layouts-forms-reporting**

One row per **field placement** on a [[PageLayout]]. Geometry is **three parallel coordinate sets** —
`Edit*`, `View*`, `Header*` — with `-1` meaning "not placed", so one row describes where a field sits
in three different renderings.

`CodeIssueTypeID` on it is what makes a layout a form layout.

**It has exactly 20 columns and none of them is named `IsRequired` or `IsReadOnly`.** That absence was
read as a puzzle for most of this corpus's life, and it turns out to be the design —
[[finding-no-layout-level-required]].

Everything per-placement that *is* configurable lives in `JSONConfigText`, a free-form blob with
**29 distinct keys** observed:

| Key | Placements |
|---|---:|
| `ColumnWidthInList` | 667 |
| `NumberOfDecimals` | 231 |
| `AutoSizeColumnWidthForInitialContent` | 163 |
| `ShowColumnTotal` | 146 |
| `EditModeDefaultValue` | 133 |
| `FieldScript` | 67 |
| **`conditionalFieldsConfig`** | **50** |
| `FieldValidationMinValue` / `MaxValue` | 42 / 29 |
| `rowsPerPage` | 26 |
| **`IncludeInSearch`** | **9** |

Two consequences: [[conditional-field|conditional rules]] are an opaque blob, so Lx **cannot answer
"which layouts use this field"** ([[rule-LAY-R-134]]); and **search participation is configured per
field per placement** — on nine placements in the whole tenant.
