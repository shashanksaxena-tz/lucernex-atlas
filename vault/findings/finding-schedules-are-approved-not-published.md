---
title: Schedules are approved, not published — and approval is irreversible
tags: [finding, accounting, workflow]
evidence: Observed
---

A generated accounting schedule is **a candidate, not an output**. It must pass a three-step
`ASC 842 Schedule Review/Approval` workflow — review, ASG approve, client approve — before it counts
([[rule-ACC-R-060]]).

> **"Once approved, it cannot be un-approved."** ([[rule-ACC-R-050]])

The workflow is the terminus. There is no reversal path, so a wrong approval is corrected by
generating a new schedule, not by undoing the old one — consistent with the module's general
**delete-and-regenerate** posture ([[rule-CON-R-010]]).

That has two direct consequences for a rebuild:

- **The approval state is part of the accounting record**, not workflow metadata that can live
  elsewhere. [[SLSummary]] carries it.
- **Recalculation is flagged, not automatic.** Changing a schedule type on Assumptions, Covenants or
  Recurring Expenses sets `NeedsRecalculation` ([[rule-ACC-R-020]]) — the engine marks itself stale
  and waits for a human to press the button ([[finding-engine-is-button-driven]]).

[[Contract]]'s 120 denormalised rollup fields have **no equivalent staleness flag**
([[rule-CON-R-026]]), so the discipline is applied in one place and not the other.

See [[one-engine-three-standards]] · [[workflow-template]]
