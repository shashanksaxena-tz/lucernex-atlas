---
title: Data fields
tags: [feature, configuration, core]
evidence: Observed
---

Concepts: [[data-field-catalog]] · [[firm-custom-field]]
Entity: [[ReportGroupAvailableField]]

**6,158 leaves across 214 entities** — `Global` 5,953, `Firm` **205**, 637 `Required`, **0**
`ReadOnly`, 448 field-type codes. The layout builder's *Available Fields* palette is this same tree.

The headline is **[[finding-firm-fields-are-physical-columns]]**: firm custom fields are ordinary
`Firm_`-prefixed columns, **359 across 20 objects by the census, 258 on [[Contract]] alone**. So
adding one is DDL — direct evidence for database-per-tenant.

A **retraction** sits in this feature's history and is worth knowing about: an earlier sweep concluded
*"0 of 205 firm fields exist as a physical column"*, and that came from running the capture with
`showGlobal=true`. The corrected `showGlobal=false` re-sweep returns 6,785 fields, **298 firm-scope,
296 with the `Firm_` prefix**, and `Contract` at 477 columns. See [[method-cheap-signals]].

**Firm fields concentrate almost entirely in one place**: [[Contract]] 147 of 205 (72%), [[KeyDate]]
10, [[ExpenseRecovery]] 9, [[Covenant]] 7 — and most of the Contract ones are
[[cam-waterfall|CAM]] clauses. **ASG's customisation of Lx is very largely a CAM abstraction.**

**Three inventories disagree and none is the physical schema** — census 223 objects / 7,421 fields;
picker 227 tables / 6,487 fields; catalog 214 entities / 6,158 leaves; **union 254**. See
[[q-bbw-22-three-firm-field-counts]] and
[`reading-the-census.md`](../../docs/data-model/reading-the-census.md).

Screens: [[screen-manage-data-fields]]
