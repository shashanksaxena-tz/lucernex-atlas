---
title: Conditional rules store display labels, not ids
tags: [finding, layouts, rules, trap]
evidence: Observed
---

> **`crtVal1` holds the *rendered text* of the driver's [[code-table]] value — `"Estoppel"`,
> `"New Lease"`, `"Yes"` — not its `CodeXxxID`.**

**Renaming a drop-down value silently breaks every [[conditional-field|conditional rule]] referencing
it.** Nothing warns, nothing fails loudly; the rule simply stops matching.

It is worse than a generic referential-integrity gap, because the principal driver in
[[tenant-bbw|BBW]] — `Issue.LAR_RequestType`, behind **44 of 54** criteria clauses — is a
**firm-defined [[client-drop-down]]**, which anyone with drop-down rights can rename. The safeguard
and the hazard are in the same person's hands.

**This is a defect to design out, not to reproduce.** ASG Edge+ should store the id and resolve the
label at render time.

Compounding it: because the rules are stored as **an opaque JSON blob** in
[[PageLayoutField]]`.JSONConfigText` rather than as normalised rows, Lx **cannot answer "which layouts
depend on this field"** ([[rule-LAY-R-134]]). So the breakage is not even discoverable by query.

A second instance of the same pattern lives in reporting: **dashboard tiles are secured by title
string, not record id**, so renaming a tile breaks its grants ([[rule-RPT-R-051]]).

See [[conditional-field]]
