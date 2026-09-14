---
title: "Q-BBW-19 — What is the hourly inbound integration, and is BBW a training tenant?"
tags: [open-question, integration, risk]
evidence: Observed
status: open
---

[[screen-job-log|Job Log]] shows **`BBW Transaction Update` executing every hour on the half-hour**,
initiated by `Lx Administrator`, each with an `LxHttpMsg…` input and an `LxDataImportLog_…` output —
**an external system posting transaction data over HTTP.**

**Nothing in the corpus recorded this.**

### Why it matters, twice

1. **It changes the risk profile of any future write testing.** A tenant everyone is treating as
   training is receiving live-shaped data hourly.
2. **It sharpens [[q-bbw-18-has-any-schedule-been-calculated]].** A tenant with live operational
   traffic *and* [[finding-discount-rate-table-empty|an empty discount-rate table]] is harder to
   explain than an idle one.

[[tenant-bbw|BBW]] is also substantially populated — 2,191 master contracts, 11,905 documents, 605
assets — which does not read like a training tenant either.

### How to settle it

**Ask ASG.** What is the feed, where does it come from, and is BBW actually a training environment?
