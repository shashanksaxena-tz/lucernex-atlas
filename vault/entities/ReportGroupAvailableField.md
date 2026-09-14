---
title: ReportGroupAvailableField
tags: [entity, layouts, reporting, configuration, core]
evidence: Observed
---

**`report_group_available_field` · 27 fields · layouts-forms-reporting**

The **field definition registry** — the store behind [[data-field-catalog|Manage Data Fields]], and
the single catalog every configuration surface draws from.

- Scope is `IsGlobal` + [[firm-tenancy|`FirmID`]] + **`IsClientExtensionField`**, alongside
  `IsRequired`, `IsReadOnly` and `IsFunctional`.
- Its `IsRequired` is the **second** of the three [[required-ness]] layers, and it is **not** a
  duplicate of the schema's: it additionally expresses parent linkage, and the two disagree on 44
  fields in both directions.
- The vendor's own FK type pointing at it is named **`Report/Form Field ID`** — the schema states in
  its own words that report fields and form fields are one catalog ([[rule-RPT-R-010]]).

In-degree 4, out-degree **0**. It is one of only 13 objects carrying `FirmID` directly.

Screens: [[screen-manage-data-fields]]
