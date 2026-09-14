# CON-R-060 — Step 5 — cap and floor (``)

*Contracts & Leases · Derived*

**Cap and floor are applied: PRPCapFloorAdjustedRent = clamp(PRPBreakpointRent, BillingBucketFloorAmount, BillingBucketCapAmount).**

Cap and floor are applied: PRPCapFloorAdjustedRent = clamp(PRPBreakpointRent, BillingBucketFloorAmount, BillingBucketCapAmount).

``` PRPCapFloorAdjustedRent = clamp(PRPBreakpointRent, BillingBucketFloorAmount, BillingBucketCapAmount) ``` `BillingBucketCapAmount` / `BillingBucketFloorAmount` are the clause's `CapAmount`/`FloorAmount` resolved into this specific billing bucket, scaled per `CodeCapFrequencyID`. Derived — the field names carry both the "BillingBucket" prefix and the Cap/Floor role, and `CodeCapFrequencyID` exists precisely to make the scaling explicit.

---

Source: `docs/modules/contracts/percentage-rent.md`
