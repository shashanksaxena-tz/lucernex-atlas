---
title: The discount-rate table is empty in both tenants
tags: [finding, accounting, blocker, core]
evidence: Observed
---

> **`Manage Discount Rates` reads "No rows to display" at [[tenant-bbw|BBW]] *and* at
> [[tenant-american-freight|American Freight]]**, both on build `26.09.0.113`.

ASC 842 and IFRS 16 both require a discount rate to compute the lease liability. Both tenants run both
standards plus straight-line. **Two independent tenants showing an empty table retires the "this one
happens to be unpopulated" explanation.**

So either the rate reaches the engine by the **per-record override** —
[[Asset]]`.DiscountRateOverride` and its [[SLSummary]] equivalent — **or no schedule in either tenant
has ever actually been calculated.** Both readings matter:

- If the override is the real path, **ASG Edge+ implementing the rate table alone reproduces an engine
  that cannot calculate.**
- If nothing has been calculated, the ASC 842 output this corpus documents has **never been exercised
  against real rates**, and the schedules are structure without arithmetic.

**And it is stranger than a dormant tenant would be.** BBW is not idle: [[screen-job-log|Job Log]]
carries **818 entries**, a real XLSX import, and an **hourly inbound HTTP integration** posting
transaction data ([[q-bbw-19-hourly-integration]]). A tenant with live operational traffic *and* an
empty discount-rate table is harder to explain than an unused one — which makes the override reading
more likely, and raises the question of what the hourly feed is doing if the liability cannot be
discounted.

**This should be put to ASG before the accounting engine is specified.**
[[q-bbw-18-has-any-schedule-been-calculated]]

See [[DiscountRate]] for the seven lookup dimensions — including the **lease-length band**, which
makes it an incremental-borrowing-rate *curve* rather than a scalar, and the **accounting method**,
which means the same lease can discount differently under ASC 842 and IFRS 16.

Screens: [[screen-manage-discount-rates]]
