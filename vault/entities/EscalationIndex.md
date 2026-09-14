---
title: EscalationIndex
tags: [entity, accounting, reference-data]
evidence: Observed
---

**`escalation_index` · 12 fields · [[module-accounting]]**

A named published-index series driving [[ExpenseEscalation]] — CPI and its relatives.

The data behind it is [[screen-manage-cpi-data|Manage CPI Data]], which holds **3,683 rows of exactly
one series** (`BLS_CWUR0000SA0`, years 1932–2019, `Published Date` `12/06/2019` on every row) — and
the grid is **identical in both tenants to five decimal places**, so it is platform-seeded
[[hub-and-spoke|Hub]] data, not tenant data.

The series stops in 2019. Any escalation clause indexed past then has nothing to read.

The escalation stack around it is five code tables — `Escalation Category/Group/Type Code`
(`2165`–`2167`) and `Index Group/Source/Type Code` (`2169`–`2171`) — plus `Cap Type Code` (`2164`).
