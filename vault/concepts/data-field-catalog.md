---
title: The data field catalog
tags: [concept, configuration, core]
evidence: Observed
---

One catalog feeds every configuration surface in the product. The layout builder's *Available Fields*
palette, the report column picker and the form field picker are all the same tree.

- **6,158 leaves across 214 entities.** `Global` scope 5,953, `Firm` scope **205**. 637 leaves marked
  `Required`; **0** marked `ReadOnly`; 448 distinct field-type codes.
- The definitions are rows in [[ReportGroupAvailableField]] (27 columns), keyed by `IsGlobal` +
  `FirmID` + `IsClientExtensionField`, plus `IsRequired`, `IsReadOnly`, `IsFunctional`.
- The vendor's own FK type is named **`Report/Form Field ID`** — the schema says in its own words
  that report fields and form fields are one catalog ([[rule-RPT-R-010]]).
- `ReadOnly = No` on all 6,158 leaves is **not an error**. Read-only is `View` in
  [[security-ladder|Field Security]], which measures a different question.

**Manage Data Fields is read-only to a firm in both tenants.** That looked like a product decision
until [[finding-firm-fields-are-physical-columns]] explained it: you cannot self-service a DDL change.

**Three inventories disagree and none is the physical schema** — census 223 objects / 7,421 fields,
picker 227 tables / 6,487 fields, catalog 214 entities / 6,158 leaves, union 254 tables. Never quote
one as authoritative; see [`reading-the-census.md`](../../docs/data-model/reading-the-census.md) and
[[q-bbw-22-three-firm-field-counts]].

Source: [`features/data-fields/`](../../docs/features/data-fields/README.md) ·
[`admin/005-manage-data-fields.md`](../../docs/admin/005-manage-data-fields.md)
