---
title: A fiscal period is not a calendar month
tags: [concept, reference-data, accounting]
evidence: Observed
---

The fiscal calendar ([[screen-manage-fiscal-calendar]]) supports **4-4-5 quarters** and **13 period
slots** with per-period week counts, allowing a 53-week retail year. So a "period" in the accounting
engine is whatever the firm defined, not a month.

And it **extrapolates**. The screen states: *"Computed calendar years will be used for date ranges not
defined below (based on last defined Fiscal Year)."* Ask for a date outside the defined range and you
get an answer, computed — not an error.

At [[tenant-bbw|BBW]] the nine defined years 2022–2030 are plain calendar years with 12 monthly
periods, so the capability is configured off. **The capability being present and unused is the point**:
a rebuild that hard-codes calendar months cannot express a retail client's year, and will silently
disagree with the incumbent the moment one is onboarded.

Dates render `DD/MM/YYYY` on a US tenant, which is worth knowing before reading any date in a capture.

It is one of five financial reference-data screens, **four of which are empty** — see
[[feature-reference-data]] and [[finding-discount-rate-table-empty]].

The [[screen-manage-holiday-calendar|holiday calendar]] is *not* part of this: it feeds project
scheduling, not accounting.

Source: [`features/reference-data/`](../../docs/features/reference-data/README.md)
