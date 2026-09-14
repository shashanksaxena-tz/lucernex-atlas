---
title: Reporting
tags: [module, reporting]
evidence: Derived
---

**49 rules, `RPT-R-001`…`RPT-R-077`** (non-contiguous; `034` and `035` are **retired and must not be
reused**; `070`–`077` are ASG Edge+ requirements, not Lx rules).

**There is no report engine separate from the page engine.** A report is a [[PageLayout]] row with
`IsReport = true` ([[rule-RPT-R-001]]) — and that claim rested on a table the schema viewer refuses,
until it was recovered over [[rest-business-object|REST]].

Four absences define most of the rebuild: **no report table, no schedule table, no run-history table,
no subscription table, no chart table.** [[PageLayout]] records a single most-recent run stamp.

What it does settle:

- Report columns draw from the **same [[data-field-catalog|field registry]]** as forms — the vendor's
  own FK type is named `Report/Form Field ID` ([[rule-RPT-R-010]]).
- Output format is a **required property of the definition** (`OutputType`), not a run-time choice
  ([[rule-RPT-R-003]]).
- Filters and groupings are the same [[PageLayoutFilter]] row, so reporting is **pivot-shaped**
  ([[rule-RPT-R-023]]).
- **Dashboard tiles are secured by title string, not record id** — renaming a tile breaks its grants
  ([[rule-RPT-R-051]]).
- [[virtual-projection|`Virtual*`]] objects let reports select calculated period series unmaterialised
  ([[rule-RPT-R-036]]).

GraphQL has 490 types and **no layout, report, chart or rule type at all** — layouts and reports
**cannot** be migrated through the data API.

Rules: [[rules-reporting]] · [`modules/reporting/`](../../docs/modules/reporting/README.md)
