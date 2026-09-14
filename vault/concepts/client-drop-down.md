---
title: Client drop-downs — the firm's own tables
tags: [concept, configuration, reference-data]
evidence: Observed
---

Distinct from the 207 platform [[code-table|code tables]]. `Client Drop Downs`
(`/en/admin/CustomCodeTableEdit.jsp`) is the firm's own registry, with full create/edit/delete —
**38 tables at [[tenant-bbw|BBW]]**, 27 at [[tenant-american-freight|American Freight]]. Every row
offers `edit | delete`; none is protected.

Two of the 38 carry more weight than the rest:

- **`Lease Status`** (`CustomCodeTableID 7727`) is where the [[contract-lifecycle|contract lifecycle
  actually lives]] — seven values at BBW, nine as read at AF, against the platform field's three.
- **`Lease Admin Request Type`**, 13 values, is the driver behind **44 of 54**
  [[conditional-field|conditional-field]] clauses in the tenant. The conditional engine's principal
  driver is a firm-defined drop-down, not a platform one.

Two negatives worth having:

- All 38 have `ParentCustomCodeTableID` empty, so the **dependent/cascading drop-down capability
  exists and is used nowhere**. The machinery is there — [[CustomCodeField]] carries
  `ParentCustomCodeFieldID` and `ParentCustomCodeTableID` — and no tenant uses it.
- Names collide with the platform registry. A platform `Lease Status Code` (`2043`) exists too, with
  exactly one value (`Expired`). Two different things, one name.

Client drop-down values expose an **audit log** with Old Value / New Value / Field / Action / Item ID
columns — see [[audit-trail]].

Source: [`admin/007-firm-and-client-drop-downs.md`](../../docs/admin/007-firm-and-client-drop-downs.md)
