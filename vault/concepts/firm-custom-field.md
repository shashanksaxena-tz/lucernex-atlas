---
title: Firm custom fields
tags: [concept, tenancy, data-model, core]
evidence: Observed
---

A tenant's custom fields are **not rows in a metadata table**. They are ordinary physical columns,
named `Firm_<Name>`, fully typed.

| | |
|---|---:|
| `Firm_` columns across the schema (census) | **359** |
| Objects carrying them | **20** |
| …on [[Contract]] alone | **258** of its 570 columns |

Next largest: [[Location]] 10, [[Facility]] 8, [[Covenant]] 7, [[KeyDate]] 7, `AllowanceTransaction` 6,
[[Parcel]] 6. They carry real types — 188 Text, 77 `Dropdown (Custom Field)`, 28 Date, 22 Percentage,
19 Currency, 7 Custom List.

The [[screen-contract-wizard|contract wizard]] places them by their literal names —
`Contract_Firm_LeaseAnalyst`, `Contract_Firm_FixturingPeriod`, `Contract_Firm_BuildoutDuration` — which
is direct confirmation from a third surface.

**The count is contested; the conclusion is not.** Three sources give 359 (census), 298 (a
`showGlobal=false` re-sweep) and 205 ([[data-field-catalog|the catalog]]). They measure different
populations and are unreconciled — [[q-bbw-22-three-firm-field-counts]]. The argument does not rest on
the number: whether it is 205 or 359, **adding one is DDL**. That is
[[finding-firm-fields-are-physical-columns]], and it is the strongest single piece of evidence for
database-per-tenant in this corpus.

Most of them are one thing. **147 of the 205 catalog firm leaves are on [[Contract]] and most are CAM
clauses** — ASG's customisation of Lx is very largely a [[cam-waterfall|CAM]] abstraction.

Source: [`features/data-fields/`](../../docs/features/data-fields/README.md) ·
[`modules/platform-tenancy/udf-registry.md`](../../docs/modules/platform-tenancy/udf-registry.md)
