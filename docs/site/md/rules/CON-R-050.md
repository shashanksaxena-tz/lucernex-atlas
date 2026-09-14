# CON-R-050 — Step 0 — the two buckets (``)

*Contracts & Leases · Observed*

**A percentage-rent period is projected: two independent date windows are produced — ReportingBucket{Begin,End,Due}Date and BillingBucket{Begin,End,Due}Date.**

A percentage-rent period is projected: two independent date windows are produced — ReportingBucket{Begin,End,Due}Date and BillingBucket{Begin,End,Due}Date.

``` ReportingBucketBeginDate / EndDate / DueDate ← CodeReportingFrequencyID + PeriodReportDueDays BillingBucketBeginDate / EndDate / DueDate ← CodeBillingFrequencyID + PeriodPaymentDueDays BillingBucketCapAmount / BillingBucketFloorAmount ← PercentageRent.CapAmount / FloorAmount, scaled to CodeCapFrequencyID ``` The reporting bucket also carries its own sales totals — `ReportingBucketGrossSalesAmount`, `ReportingBucketNetSalesAmount` — separate from the billing bucket's. Observed.

---

Source: `docs/modules/contracts/percentage-rent.md`
