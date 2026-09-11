# The CAM recovery waterfall — recovered from the vendor's own field labels

**Stated up front.** Lucernex's expense-recovery calculation does not have to be reverse-engineered.
**The vendor wrote the formulas into the UI labels**, and the View Object Model tool will list every
computed field in the product. The complete CAM waterfall is:

```
Sub Total #1   = Controllable + Non-Controllable − Deductions          (C+NC−D)
Pass-Through   = Sub Total #1 + Admin Fee % + Admin Fee + Additions    (ST1+AF%+AF+A)
Sub Total #2   = Pass-Through − Recoveries                             (PT−R)
Net Pass-Through = Sub Total #2 × Pro Rata Share Rate                  (ST2*PRR)
Net Amount Due = Net Pass-Through − Pre-Paid                           (NPT−PP)
Revised Amount Due = Net Amount Due + Adjustments                      (Net+Adj)
```

Every one of those parenthesised expressions is **literally the field's UI label** in Lucernex.
Confidence: **Observed**.

| Property | Value |
|---|---|
| Source | View Object Model, `/en/admin/ShowObjectDetails.jsp?sqlTableID=&limitFieldFilter=Math` |
| Captured | 2026-09-11, tenant `(ASG)American Freight`, build `26.08.0.46` |
| Exploration mode | Read-only report screen |
| Reproduce | Open the URL above, or filter by table with `sqlTableID=<id>` |

## The vendor's own field classification

The tool classifies every field in the product four ways. Run against **All Tables**:

| Filter | Fields | Share |
|---|---:|---:|
| `All` | **7,047** | — |
| `Editable` | **3,437** | 49% |
| `NonMathComputed` | **1,804** | 26% |
| `Math` | **422** | 6% |

**Derived:** computed fields total **2,226 — 32% of the product**. User-editable is 49%. The
remaining ~19% is neither: keys, audit stamps and system columns.

This **supersedes inference**. [`computed-vs-input-fields.md`](computed-vs-input-fields.md)
classified 666 accounting fields INPUT/COMPUTED by reasoning from type names such as
`sTYPE_MONEY_MATH_OPERATION`. That work was sound and its conclusions hold, but this tool is the
vendor's own answer for **all 7,047 fields** and should be treated as authoritative wherever the two
disagree. It also distinguishes something the type names do not: `Math` (a formula over other
fields) versus `NonMathComputed` (system-derived by other means).

## Where the computation actually lives

The 422 `Math` fields are **not** spread across the product. They sit in nine tables:

| Table | Math fields | Share |
|---|---:|---:|
| **`ExpenseRecovery`** | **379** | **90%** |
| `ExpenseRecoveryItem` | 19 | 4% |
| `ContractFinancialTest` | 13 | 3% |
| `KeyDate` | 4 | |
| `Contract` | 2 | |
| `InvoiceItem` | 2 | |
| `ContractTerm` | 1 | |
| `Scenario` | 1 | |
| `Tenant` | 1 | |

**Nine tenths of every formula in Lucernex is on one table.** `ExpenseRecovery` is the product's
computational centre of gravity, and this is independent confirmation of what
[`setup-schedule-transaction-pattern.md`](setup-schedule-transaction-pattern.md) argued from
structure: **CAM is not an instance of the Clause/Schedule/Transaction pattern — it is a
reconciliation grid.** A grid is what 379 formulas on one row look like.

For the rebuild, the sizing implication is blunt: **expense recovery is not one module among many.
It is the calculation engine.**

## The measurement bases

CAM reconciliation compares four versions of the same figures. The prefixes are consistent
throughout:

| Basis | Meaning |
|---|---|
| **Budgeted** | What the landlord estimated at the start of the year |
| **Reported** | What the landlord's year-end statement claims |
| **Approved** | What the tenant accepted after audit |
| **Prior** | Last period's equivalent, for year-over-year comparison |

Every figure exists in **Gross** and **Net** variants — hence the `…Gross` / `…Net` suffix pairs
throughout.

### The variance matrix

Five pairwise comparisons are precomputed, each as both an absolute amount and a percentage:

| Prefix | Comparison |
|---|---|
| `ABVariance…` | Approved − Budgeted |
| `APVariance…` | Approved − Prior |
| `BPVariance…` | Budgeted − Prior |
| `RAVariance…` | Reported − Approved |
| `RPVariance…` | Reported − Prior |

with `…PctVariance…` forms for the percentage version. Each variance is computed for **every line in
the waterfall** — Controllable Expenses, Non-Controllable Expenses, Deductions, Additions, Admin
Fee, Admin Fee %, Cap Amount, Recoveries, Pre-Paid Amount, Pro Rata Share Rate, GLA, Rentable Area,
Sub Total #1, Sub Total #2, Pass-Through, Net Pass-Through, Net Amount Due.

**Derived:** 5 comparisons × ~17 measures × {amount, percent} × {Gross, Net} is most of the 379.
The table is wide because the variance grid is fully materialised rather than computed on read.

**This is a deliberate design choice with a clear rebuild consequence.** Lucernex precomputes and
stores every variance. A rebuild could compute them on demand from four stored bases and carry ~20
columns instead of ~379. That is the single largest schema simplification available anywhere in this
product — but it trades storage for compute on a screen accountants use interactively, so it is a
decision to make deliberately, not an obvious win.

## Two details that matter

### `NoZeroDef` — nullable by design

Every `Prior*` field carries the suffix `NoZeroDef`: `PriorApprovedSubTotal1GrossNoZeroDef`,
`PriorBudgetedNetAmountDueNetNoZeroDef`, and so on.

**Derived:** "no zero default" — these columns are **nullable rather than zero-defaulted**, because
a prior period that does not exist is *unknown*, not *zero*. Defaulting it to zero would produce
spurious 100% variances on every first-year reconciliation.

This is exactly the hazard `CON-R-137` predicted, and the field naming confirms the vendor hit it
and fixed it. **ASG Edge+ must model recovery measures as nullable `BigDecimal`, never
zero-defaulted.**

### Occupancy gross-up

`OccupancyAdjustedThreshold`, labelled **"Occupancy Factor"**, and the `Approved` variant of net
pass-through uses a different formula from the rest:

```
Approved Net Pass-Through (ST2*PRS*Occ)     ← includes occupancy
other bases      Net Pass-Through (ST2*PRR) ← does not
```

**Observed.** The approved figure multiplies by an occupancy factor where the others multiply only
by the pro-rata rate. That is the **gross-up** provision — where a landlord may recover as if the
centre were fully occupied. It applies only on the approved basis, which is where a tenant's auditor
would insist on it.

A rebuild that models one `netPassThrough` formula for all four bases will get approved amounts
wrong on every lease with a gross-up clause.

### Fields the vendor marks `Duplicate`

`ApprovedNetPassThroughCOREFirmOnlyGross`, `PriorReportedNetPassThroughCOREFirmOnlyNetNoZeroDef` and
their siblings carry the label suffix **"Duplicate"** and the internal marker `COREFirmOnly`.

**Inferred:** a parallel set maintained for a specific customer or migration, retained for
compatibility. Do not migrate them without asking; they are candidates for deliberate omission.

## The rest of the Math fields

Outside recovery, the formula set is small and worth knowing in full:

| Table | Field | Label |
|---|---|---|
| `ContractFinancialTest` | `ASC842InitialAssetBalance` | ASC 842 Initial Asset Balance |
| | `ASC842InitialLiabilityBalance` | ASC 842 Initial Liability Balance |
| | `ASC842NetLeaseLiabilityBalance` | ASC 842 Net Lease Liability Balance |
| | `IFRS16InitialAssetBalance` / `…Liability…` / `…NetLease…` | the IFRS 16 trio |
| | `FairValueControlled`, `ThresholdFairValueControlled` | fair-value test inputs |
| | `InitLiabilityBalToThreshFairValueCtrld` | **the 90% test ratio** |
| | `PVOfFinancialTermsWithAdjustments` | PV of payments |
| | `LikelyTermLength`, `TestTermLength`, `TermLength` | three different term lengths |
| `Contract` | `TermLength` | the "5 years 16 days" value seen on screen 014 |
| `KeyDate` | `ActionPeriod`, `FirstNoticePeriod`, `NoticePeriod`, `LengthOfTerm` | option-notice windows |
| `ContractTerm` | `LengthOfTerm` | |
| `InvoiceItem` | `InvoiceAmount`, `TotalAmount` | |
| `Scenario` | `NewTermLength` | |
| `Tenant` | `math_calcTotalCapacity_1` | calcTotalHeadcount |

**`InitLiabilityBalToThreshFairValueCtrld` is the ASC 842 classification test made explicit** —
initial liability balance as a percentage of threshold fair value. That is the "substantially all of
the fair value" criterion, computed. [`asc-842.md`](../accounting/asc-842.md) inferred the tests from
field names; here is the one that is actually a formula.

**Three distinct term lengths** on `ContractFinancialTest` — `TermLength`, `TestTermLength`,
`LikelyTermLength` — is worth flagging: the term used for classification is not necessarily the
contractual term, because reasonably-certain renewal options extend it. A rebuild needs all three.

## Rules

| ID | Rule | Confidence |
|---|---|---|
| `CON-R-153` | `Sub Total #1 = Controllable + Non-Controllable − Deductions`. | Observed |
| `CON-R-154` | `Pass-Through = Sub Total #1 + Admin Fee % amount + Admin Fee + Additions`. | Observed |
| `CON-R-155` | `Sub Total #2 = Pass-Through − Recoveries`. | Observed |
| `CON-R-156` | `Net Pass-Through = Sub Total #2 × Pro Rata Share Rate`, **except on the Approved basis**, where it is `Sub Total #2 × Pro Rata Share × Occupancy Factor`. | Observed |
| `CON-R-157` | `Net Amount Due = Net Pass-Through − Pre-Paid Amount`. | Observed |
| `CON-R-158` | `Revised Amount Due = Net Amount Due + Adjustments`. | Observed |
| `CON-R-159` | Four measurement bases exist — Budgeted, Reported, Approved, Prior — each in Gross and Net form, and five pairwise variances are materialised for every waterfall line. | Observed |
| `CON-R-160` | Prior-period measures are nullable, never zero-defaulted (`NoZeroDef`). A missing prior period is unknown, not zero. | Observed |
| `CON-R-161` | 2,226 of 7,047 fields (32%) are computed; 3,437 (49%) are user-editable. 90% of all formula fields are on `ExpenseRecovery`. | Observed |

## Open questions

1. **What exactly is `Admin Fee %` versus `Admin Fee`?** Both appear as separate addends in the
   Pass-Through formula, so one is a rate-derived amount and the other a flat fee — but which is
   which, and does the percentage apply to Sub Total #1 or to something narrower?
2. **Where does the cap clamp?** `CapAmount` has variance fields at every basis but does not appear
   in any of the labelled formulas. `CON-R-094` flagged this as unresolved and it remains so.
3. **What sets `OccupancyAdjustedThreshold`?** The gross-up factor is computed, so something feeds
   it — probably an occupancy percentage on the Location or Complex.
4. **What are the 1,804 `NonMathComputed` fields**, and how do they differ from `Math`? Capturing
   that list would complete the classification for the whole product.
5. **Are the `COREFirmOnly` "Duplicate" fields safe to drop** in a migration?
6. **`Tenant.math_calcTotalCapacity_1`** — a headcount calculation on the Tenant record, unrelated to
   anything else in the corpus. What uses it?
