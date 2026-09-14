---
title: "Q-BBW-12 — Why does the Equipment Contract root not render at AF?"
tags: [open-question, navigation, answered]
evidence: Inferred
status: answered-inferred
---

**Answered:** [[finding-root-renders-iff-record-exists]]. A root renders **iff** the firm holds ≥1
record of that `ProjectEntityTypeName`. [[tenant-bbw|BBW]] has exactly one equipment contract and
renders it; [[tenant-american-freight|AF]] has zero and does not. The rule also explains the
[[Program]] anomaly, which is what makes it the answer rather than a coincidence.

**It is kept open as a question because the answer is Inferred.**

It is an **11-for-11 correlation across two tenants, not a reading of the server's rendering code.**

### The falsifier

> A tenant with the entitlement on, the type registered, page access granted and **zero rows** that
> *still* renders the root.

### To settle the mechanism rather than the correlation

Find the render-time filter in the menu-tree build.

### What was eliminated on the way

Build version · the [[Firm]] entitlement flag · the seeded menu structure ·
[[security-ladder|per-user-class page access]] (granted 8 of 10) · type registration
([[method-verify-a-zero]]).

The trap that killed the previous three-gate model: **`Default` in the security matrix means
*inherit*, not *granted***.
