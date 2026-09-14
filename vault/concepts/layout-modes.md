---
title: SEP, SUB, LIST — the three layout modes
tags: [concept, layouts]
evidence: Observed
---

The layout administrator (`SummaryEntityPageLayoutEdit.jsp`) takes `mode={SEP,SUB,LIST}`, and the
mode decides what a [[page-layout-concept|layout]] is for.

| Mode | Is | Count at [[tenant-bbw|BBW]] | Count at [[tenant-american-freight|AF]] |
|---|---|---:|---:|
| `SEP` | Summary Page — a top-level destination | 15 | 17 |
| `SUB` | Sub-page — a titled section embedded in a parent | 32 | 31 |
| `LIST` | Grid of child records | 46 | 40 |
| | **total** | **93** | **88** |

**93 is not the real total.** `mode=ISSUE` and `mode=FORM` silently fall back to `SEP`, which is why
**42 form layouts** never appear in the registry at all — they are reachable only through Issue Types.
The true layout total is **135**. That mattered: a conditional-fields sweep over the 93 concluded the
feature was unused, and the feature actually lives almost entirely on the 42. See
[[finding-form-layouts-are-hidden]].

**Sub-pages are not navigable (Observed).** All 32 `SUB` layouts return no `ParentPageLayoutID`,
against 15 of 15 for `SEP` and 19 of 46 for `LIST`. They attach to a parent; they are composition
units.

The runtime renderers mirror the split: `PForm.jsp` serves detail, `PLForm.jsp` serves lists, and
between them they serve [[finding-two-files-serve-56-percent|56% of all routed screens]].

The tenant also holds **1,647 `PageLayout` rows** against these 135 — see [[q-bbw-23-1647-layouts]].

Source: [`features/page-layouts/`](../../docs/features/page-layouts/README.md) ·
[`admin/008-manage-page-layouts.md`](../../docs/admin/008-manage-page-layouts.md)
