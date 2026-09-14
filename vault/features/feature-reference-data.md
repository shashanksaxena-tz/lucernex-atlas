---
title: Reference data
tags: [feature, reference-data, accounting]
evidence: Observed
---

The five administration tools that maintain the data everything else calculates against — and
**four of the five are completely empty in [[tenant-bbw|BBW]]**.

| Tool | Rows |
|---|---|
| [[screen-manage-cpi-data\|CPI Data]] | **3,683** — one series, `BLS_CWUR0000SA0`, 1932–2019 |
| [[screen-manage-discount-rates\|Discount Rates]] | **0** |
| [[screen-manage-exchange-rates\|Exchange Rates]] | **0** |
| [[screen-manage-fiscal-calendar\|Fiscal Calendar]] | 9 years, **no period detail** |
| [[screen-manage-holiday-calendar\|Holiday Calendar]] | **0** |

The consequential one is **[[finding-discount-rate-table-empty]]** — both tenants run ASC 842, IFRS 16
and straight-line against an empty rate table, confirmed independently on two tenants' screens.

Entities: [[DiscountRate]] · [[EscalationIndex]]

- The CPI grid is **identical in both tenants to five decimal places** — platform-seeded
  [[hub-and-spoke|Hub]] data. It also shows a month `0`, unexplained (*Inferred*: annual average).
- **[[fiscal-period|A fiscal period is not a calendar month]]** — 4-4-5 and 13-period retail years are
  supported, and the calendar **extrapolates** beyond its last defined year.
- **Corrected:** the holiday calendar feeds **project scheduling, not accounting** — its own help text
  says holiday days determine task completion dates.

And a required-ness datapoint from the same screens: **the asterisk appears on list column headers**,
which is what narrowed [[finding-no-layout-level-required]] to its answer.

[`features/reference-data/`](../../docs/features/reference-data/README.md)
