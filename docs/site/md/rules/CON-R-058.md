# CON-R-058 — Step 4 — the eight tiers (``, `CON-R-059`)

*Contracts & Leases · Derived*

**A percentage-rent period is tiered: PRPSalesPastBreakpoint_N is computed for each of 8 tiers from PRPBreakpointAmount1..8 (or BreakpointCount1..8 under UseCountBasedRate) — assumed to be a marginal band reading, though a simple-excess reading is also grammatically possible.**

A percentage-rent period is tiered: PRPSalesPastBreakpoint_N is computed for each of 8 tiers from PRPBreakpointAmount1..8 (or BreakpointCount1..8 under UseCountBasedRate) — assumed to be a marginal band reading, though a simple-excess reading is also grammatically possible.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Reading |
| Stated as | Formula |
| Stated as | Consequence |
| Stated as | (a) marginal band (assumed) |
| Stated as | `clamp(PRPSalesAmount, BP_N, BP_{N+1}) − BP_N`, with `BP_9 = ∞` |
| Stated as | Σ of tier rents is the standard tiered result; rates are marginal |

---

Source: `docs/modules/contracts/percentage-rent.md`
