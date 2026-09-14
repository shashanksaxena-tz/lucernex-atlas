---
title: "Q-BBW-18 — Has any schedule ever been calculated against a real discount rate?"
tags: [open-question, accounting, blocker]
evidence: Observed
status: open
---

**The most consequential open question in this corpus for the accounting rebuild.**

[[finding-discount-rate-table-empty|The rate table is empty in both tenants]], on the same build,
verified from the screens themselves. Both tenants run ASC 842, IFRS 16 and straight-line.

**So one of two things is true, and they lead to different rebuilds:**

- **The per-record override is the real path** — [[Asset]]`.DiscountRateOverride` and the
  [[SLSummary]] equivalent. In which case **ASG Edge+ implementing the rate table alone reproduces an
  engine that cannot calculate.**
- **Nothing has ever been calculated.** In which case the ASC 842 output this corpus documents has
  never been exercised against real rates, and the schedules are **structure without arithmetic**.

The [[tenant-bbw|live operational traffic]] in BBW — 818 job-log entries, an hourly inbound feed —
makes the first reading more likely, and raises a further question: **what is the hourly feed doing if
the lease liability cannot be discounted?**

### How to settle it

**Ask ASG.** Technically: open a contract with an ASC 842 schedule and check whether
`Asset.DiscountRateOverride` or the `SLSummary` equivalent carry values.

**This should be answered before the accounting engine is specified.**
