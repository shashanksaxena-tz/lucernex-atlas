---
title: What the two tenants settle between them
tags: [tenant, architecture, moc]
evidence: Derived
---

Reading [[tenant-bbw|BBW]] against [[tenant-american-freight|American Freight]] turned several
assumptions into evidence, and several confident claims into retractions. This note is the index.

### Same ids ⇒ platform-seeded

[[finding-platform-seeded-by-id]] — 109/109 navigation nodes, 207/207 code tables, 227/227 sql tables.
**Same names could be coincidence; same primary keys cannot.**

### Same names, different ids ⇒ published then forked

[[finding-publish-then-fork]] — 80 layouts shared by name, **zero** by id, offsets clustered
`+2626…+2677`. And the [[publish-and-fork|product names the mechanism itself]].

### Different names, no pattern ⇒ tenant-authored

[[WorkFlowTemplate|Workflow templates]]. 4 against 13, only 2 shared names, no id-offset block.

### The three models, side by side

| Model | Applies to | Signature |
|---|---|---|
| Platform-seeded and shared | navigation, the table catalog | identical ids |
| Published, then forked | [[page-layout-concept\|layouts]], [[code-table]] values | matching names, disjoint ids |
| Tenant-authored | [[workflow-template\|workflows]] | names differ, no pattern |

**A rebuild needs all three, and needs to know which surface is which.** Treating a
published-then-forked surface as tenant-authored loses the template; treating it as platform-seeded
loses the fork. See [[hub-and-spoke]].

### And the difference itself

The two tenants differ by **one feature**, not by drift —
[[finding-tenants-differ-by-one-feature]] — and that feature is visible at all only because
[[finding-root-renders-iff-record-exists|one row exists]].

### What the second tenant refuted

[[finding-form-workflow-not-1-1]] · [[finding-no-where-used-precedent]] ·
[[finding-form-layouts-are-hidden]] · [[finding-punch-list-out-of-scope]]
