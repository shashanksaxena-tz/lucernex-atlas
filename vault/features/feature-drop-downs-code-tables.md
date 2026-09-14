---
title: Drop-downs and code tables
tags: [feature, configuration, reference-data]
evidence: Observed
---

Concepts: [[code-table]] · [[client-drop-down]]

**207 platform tables, identical ids and names in both tenants.** The value census at
[[tenant-american-freight|AF]]: **73 populated, 134 empty (65%), 1,140 values — 154 protected, 986
deletable**.

**Three tables hold 56% of all values**: `Recovery Item Type` (`3016`) 314, `Market Area` (`2049`)
213, `Expense Type` (`3013`) 107.

The feature's main finding is a **retraction**: [[finding-no-where-used-precedent]]. Delete is gated
by a server-supplied per-row `isReadOnlyRecord` boolean read straight from the `EditDeleteLink`
renderer — **no count, no threshold, no usage lookup anywhere in the render path**. So Lx is **no
precedent for Where-Used**, and ASG Edge+'s `D-07` and `MST-015` stand as decided.

**The flag moved between builds.** `AI Abstracted` had delete on `26.08.0.46` and not on
`26.09.0.113` — same tenant, three days later — which is also one quarter of
[[atlas-ai-abstraction|the AI pipeline finding]].

Two small negatives with teeth: only **1 of 1,140** values is marked `Inactive`, and two tables render
no `Inactive` column at all. And the **cascading drop-down capability exists and is used nowhere** —
see [[CustomCodeField]].

The [[contract-lifecycle]] turns out to live here, in a [[client-drop-down]].

Screens: [[screen-manage-firm-drop-downs]] · [[screen-client-drop-downs]]

[`features/drop-downs-code-tables/`](../../docs/features/drop-downs-code-tables/README.md)
