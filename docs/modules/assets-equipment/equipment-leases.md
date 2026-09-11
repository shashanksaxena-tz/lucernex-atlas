# Equipment leases — how `Asset` plugs into the ASC 842 / IFRS 16 engine

**Stated up front.** `Asset` is not a passive equipment record that a lease happens to reference. It
carries its own copy of the classification-test surface — `FairValueOfAsset`,
`DiscountRateOverride`, `IsAssetTooSpecializedForLessor`, `IsLowAssetValue`, `IsShortTerm`,
`HasBuyoutOption`, `PlanToBuyAtEndOfTerm`, `DoesTitleRevertToTenant`, `InitialAssetBalanceAdjust`,
`InitialLiabilityBalanceAdjust`, `ImpairmentOverride`, `Residual`, `YearsOfDepreciableLife` — and
`ContractFinancialTest`, `SLSummary` and `SLPeriod` each carry a **separate, nullable, direct FK to
`Asset`** alongside their FK to `Contract`
([`data-model.md`](data-model.md#4-asset-in-the-accounting-engine--the-cross-module-edges-that-matter-most)).
**One equipment lease can classify and schedule at the level of an individual piece of equipment,
not only at the level of the contract that covers it.** That is the accommodation the schema makes
for an equipment lease bundling several distinct assets — a fleet of trucks, a set of forklifts —
each of which may fail or pass the ASC 842 five-part test differently even though they share one
`Contract`. `docs/modules/accounting/README.md` documents the engine from the `Contract` side; this
file documents the same engine from the `Asset` side and does not restate what it already
established about the tests themselves.

## 1. The FK shape, and what it implies

**Observed**, [`../../mindmap/edges.json`](../../mindmap/edges.json) and
[`../accounting/data-model.md`](../accounting/data-model.md):

| Record | FK to `Contract` | FK to `Asset` |
|---|---|---|
| `ContractFinancialTest` | `ContractID`, required | `AssetID`, **nullable** |
| `SLSummary` | `ContractID`, required | `AssetID`, **nullable** |
| `SLPeriod` | `ContractID` (via `SLSummary`) | `AssetID`, **nullable** |
| `FinancialAdjustment` | `ContractID` | `AssetID` |
| `ExpenseAllocation`, `ExpenseSchedule`, `PaymentTransaction` | `ContractID`-adjacent | `AssetID` |

`AssetID` being **nullable, not required**, on the classification/schedule tables is the load-bearing
detail: it means the same table shape serves both a real-estate lease (no `Asset`, `AssetID` null)
and an equipment lease (an `Asset` populated, possibly one row per asset under the one `Contract`).
**Derived** — this is a mechanical reading of the nullability, not a confirmed behaviour; no live
record was captured showing more than one `SLSummary` under a single equipment `Contract`, so
whether the platform actually *generates* one schedule per asset, or one schedule for the contract
with `AssetID` merely recording which asset it happens to concern, is not settled. See Open
Questions.

`Asset.FinancialContractID` is the return path: typed `Contract ID`
([`../../data-fields/asset.md`](../../data-fields/asset.md)), it is how the asset knows which
equipment contract it belongs to, independent of and complementary to the `SLSummary`/
`ContractFinancialTest` rows that may separately point back at the same asset.

## 2. Two classification surfaces, not one

`Contract`/`ContractFinancialTest` and `Asset` each carry their own overlapping set of ASC 842 input
fields:

| Concept | On `ContractFinancialTest` (per `../accounting/asc-842.md`) | On `Asset` |
|---|---|---|
| Impairment | `ImpairmentsAmount` | `ImpairmentOverride` |
| Fair value | *(part of the PV/aggregate-value calc)* | `FairValueOfAsset`, `FairValueSource` |
| Residual value | — | `Residual` |
| Discount rate | *(via `Contract.ComputedSLDiscountRate`)* | `DiscountRateOverride` |
| Bargain purchase / buyout | `ContainsBargainPurchaseOption` (legacy Cap Lease Test, on `Contract`) | `HasBuyoutOption`, `PlanToBuyAtEndOfTerm` |
| Title transfer | `DoesTitleRevertToTenant` (also on the legacy Cap Lease Test) | `DoesTitleRevertToTenant` — **the identical field name, on a different table** |
| Specialized-asset test | — | `IsAssetTooSpecializedForLessor` |
| Low-value / short-term practical expedients | — | `IsLowAssetValue`, `IsShortTerm` |
| Initial balances | `ASC842InitialAssetBalance`/`IFRS16InitialAssetBalance` | `InitialAssetBalanceAdjust`, `InitialLiabilityBalanceAdjust` — named as **adjustments**, not the balances themselves |
| Depreciable life | — | `YearsOfDepreciableLife` |

**Derived**, from the naming: the `Asset`-level fields read as **inputs and overrides feeding the
per-asset test**, while `ContractFinancialTest`'s fields are the **computed result** of running that
test (both ASC 842 and IFRS 16 in parallel, per `../accounting/asc-842.md` §"the measurement
surface"). `DoesTitleRevertToTenant` existing verbatim on both `Contract` (as part of the legacy Cap
Lease Test, per `../accounting/asc-842.md` §"the legacy Cap Lease Test") and on `Asset` is the
clearest single piece of evidence that the equipment-lease classification test is meant to run
*per asset*, using asset-level facts, even though the identically-named question exists at the
contract level for real-estate leases. **No screen was captured to confirm which one wins when both
are populated for the same equipment lease** — the same "which impairment input wins" open question
`../accounting/asc-842.md` already raises for `SLSummary`/`ContractFinancialTest`/`Asset` together
now has a specific, concrete third input to add to that unresolved list.

## 3. `Asset`'s own date fields override the contract's, when populated

**Observed**, vendor field definition text quoted directly in
[`../accounting/asc-842.md`](../accounting/asc-842.md#12-what-drives-the-accounting-window)
(cited here, not restated as new): *"[`Asset.AccountingBeginDate`/`AccountingEndDate`] change the
dates that the test and rent schedules will be run for. If you do not enter override dates, the
test and schedules will run based on the dates of the expense schedules for the asset."* The default
path derives the accounting window from `ExpenseSchedule` rows tied to the asset; populating the two
override fields on `Asset` replaces that derivation outright. This is the one piece of the engine's
control flow the vendor's own help text states explicitly rather than leaving to field-name
inference.

## 4. The one gap: no approval route

**Observed**, [`../accounting/README.md`](../accounting/README.md) finding 6 and
[`../accounting/asc-842.md`](../accounting/asc-842.md)'s "what a rebuild must not miss" list:
the live tenant runs a three-step `ASC 842 Schedule Review/Approval` workflow — Initial Review →
Approve (ASG) → Approve (Client) — before `SLSummary.IsApproved` is set, and that workflow's form
type is attachable to `Portfolio` and `RE Contract`, **but not `Equipment Contract`.** Equipment
leases produce `ContractFinancialTest`/`SLSummary` rows exactly as real-estate leases do (§1), yet
have **no observed route through the approval gate** that governs whether a schedule counts as
published rather than a draft. Whether this is a genuine gap in the tenant's configuration, a
workflow type this pass simply did not find, or a deliberate design choice (equipment leases are
lower-value and don't warrant the same three-party sign-off) is unresolved. This is the most
consequential open question this file raises for a rebuild: copying the engine without copying an
equivalent gate for equipment would silently publish equipment-lease schedules that a real-estate
lease of equal complexity would have blocked.

## 5. What this means for ASG Edge+

- **Do not model equipment-lease classification as "the same `Contract`-level test, just with
  `Asset` as a foreign key for reporting."** The nullable, parallel FK shape and the duplicated
  field surface both point to classification running *per asset*, with the asset supplying its own
  inputs (fair value, residual, discount-rate override, buyout/title/specialization/low-value flags)
  independently of whatever the contract-level test would compute for a real-estate lease.
- **Decide explicitly whether an approval gate applies to equipment schedules.** Section 4's gap is
  a real design question, not a documentation oversight — silently omitting it would be a regression
  if ASG's business process actually requires equipment schedules to be reviewed, and an unnecessary
  addition if it does not.
- **Resolve the impairment-precedence question once, for both leases types.** `Contract`-level
  (`../accounting/asc-842.md`), and now `Asset`-level, impairment overrides both exist with no
  documented precedence. A rebuild should pick one authoritative source rather than inherit three
  competing inputs.
- **Carry `RemainingAssetBalance`'s magnitude-typing hazard into the rebuild's fix, not just the
  contract-level `SLSummary.SLRemainingAssetBalance`.** The identical `sTYPE_PERCENT_OR_AMOUNT` field
  type sits on `Asset` too ([`data-model.md`](data-model.md#21-remainingassetbalance-is-magnitude-typed--flagged-again-here)); whatever
  percentage/currency split the accounting module's mapping proposes must apply to both fields, not
  only the one already flagged.

## Open questions

Ranked by how much each blocks a rebuild decision.

1. **Does one equipment `Contract` actually carry more than one `Asset`, each with its own
   `SLSummary`/`ContractFinancialTest` row, in a live tenant?** The schema permits it; nothing in
   this pass observed it happening. This is the single fact that would confirm or refute the whole
   "classification runs per asset" reading.
2. **Is there truly no approval workflow for equipment-lease schedules, or was an existing one simply
   not found?** (§4) Blocks any rebuild decision about whether to build a parallel approval path for
   equipment.
3. **Which of `Contract`/`ContractFinancialTest`'s impairment field and `Asset.ImpairmentOverride`
   wins when both are populated for the same equipment lease?**
4. **What does `Asset.DoesTitleRevertToTenant` actually drive**, given the same-named field exists
   independently on `Contract` for the legacy Cap Lease Test — are they read together, or is the
   `Asset`-level one the one that matters for equipment specifically?
5. **Does `RemainingAssetBalance` on `Asset` ever disagree with the same-named/typed field on
   `SLSummary` for the same asset**, and if so which one is authoritative?
