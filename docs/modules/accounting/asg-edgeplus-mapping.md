# Mapping the accounting engine onto ASG Edge+

**Stated up front.** ASG Edge+ already has a *better* target architecture for this module than
Lucernex has: the **Accounting Engine BRD** (`KnowledgeFolder/ProjectProposals/ASG Edge Plus/Source/
_md_cache/ASG_Gen_accounting engine.md`) specifies a single centralised ledger service with idempotent
candidate submission, a `Generated → Approved → Posted → Reversed` lifecycle, immutable posted rows,
period open/close, double-entry validation, and a **Rule Administration UI where the ASC 842
thresholds are versioned, effective-dated, and four-eyes approved**. Lucernex has none of that: its
thresholds are per-contract columns, its schedules are mutable until approved and then permanently
frozen, and its "period close" is a `LastPostedEndDate` watermark. So the mapping is mostly *not*
a port. What must be ported is the **calculation surface** — 230 computed fields, 55 rules, and the
schedule-versioning pattern — into a structure ASG Edge+ has already designed differently.

**The scope is smaller than the schema suggests.** ASG runs **one** of the three standards the engine
supports: the `ASC 842 Schedule Type Code` table holds a single row (`842 Rent`) and the
straight-line and IFRS 16 tables are both empty. So the migration carries one schedule type and one
set of twenty GL slots — not a matrix — and whether ASG Edge+ builds IFRS 16 at all is a business
decision rather than a technical one. That single fact removes more work from the build list than
anything else in this document.

One thing the BRD does **not** yet cover, and the live tenant does: **ASG runs a three-step
`ASC 842 Schedule Review/Approval` workflow** — internal review, ASG approval, then client approval —
before a schedule counts. The BRD's approval governance (§7) covers *transactions*; the review gate
here sits on the *schedule* that produces them, one level up, and it is a two-party sign-off. That is
a build item, not a port, and it is item 12 below.

Three things in ASG Edge+ as it stands today will fight this module, and all three are called out
below: `Money` rounds to 2 decimal places while the Accounting Engine BRD requires 4; there is no
`Rate` primitive for discount rates or FX rates; and the durable-audit ADR blocker (ADR-0020 vs.
ADR-0012) sits directly across the path of an immutable, audited ledger.

*Evidence for the Lucernex side: as cited throughout this folder. Evidence for the ASG Edge+ side:
`ASG_Gen_accounting engine.md`, `16_Contract_Equipment_Accounting_BRD.md`,
`ASG-EdgePlus-Platform/asg-edgeplus-primitives/src/main/java/.../Money.java`, and the workspace
`CLAUDE.md`. All **Observed** in those files. Live-tenant evidence (build `26.08.0.46`, 2026-09-10) is
in `docs/data-model/graphql-api.md` and
`docs/modules/layouts-and-forms/forms-vs-pages-vs-layouts.md`.*

## What already exists in ASG Edge+

| Asset | Where | Relevance |
|---|---|---|
| **Accounting Engine BRD** | `KnowledgeFolder/…/_md_cache/ASG_Gen_accounting engine.md` | The target design. Governs every other module: *"No module may independently post, finalize, modify, or maintain accounting transactions."* |
| **BRD 16 — Contract Accounting (Real Estate & Equipment)** | `KnowledgeFolder/…/Source/16_Contract_Equipment_Accounting_BRD.md` (1,333 lines) | The user-facing ASC 842 module, written against the live Lucernex UI. Its Source-of-Truth list names seven Lucernex screens this folder describes from the schema side. |
| **BRD 23 — Accrual Management** | `KnowledgeFolder/…/_md_cache/23 Accrual Management BRD.md` | Owns `ExpenseAccrualSetup` / `ExpenseAccrualSchedule` / `AccrualTransaction`. Its lifecycle (Calculated, Reviewed, Posted, Adjusted, Reversed) is explicitly subordinated to the engine's. |
| **`Money` domain primitive** | `ASG-EdgePlus-Platform/asg-edgeplus-primitives` | `record Money(BigDecimal amount, Currency currency)`; rejects `double`; throws on cross-currency arithmetic. Constitution §4.4 satisfied — **but see the scale problem below.** |
| **`TenantId`, `Result`** | same module | Tenant discriminator and error-carrying return type. |
| **`asg-edgeplus-starter-identity`** | `ASG-EdgePlus-Platform` | `X-User-Id` / `X-Tenant-Id` / `X-Roles` from the gateway. The accounting service must use it, not add a resource-server config. |

## What the live configuration removes from scope

*All **Observed**, 2026-09-10, `FirmCodeEdit.jsp` — `docs/data-model/code-table-registry.md`.*

| Code table | `TableType` | Rows | What it takes off the build |
|---|---:|---:|---|
| ASC 842 Schedule Type | 2162 | **1** (`842 Rent`) | One GL mapping to migrate, not N. One `DontAmortizeAssetValue` value to carry — and it is **unchecked**. |
| Straight Line Schedule Type | 2161 | **0** | The legacy ASC 840 schedule type is unused. Nothing to migrate; do not build the concept. |
| IFRS 16 Schedule Type | 2163 | **0** | IFRS 16 is unconfigured. See the decision below. |

**The IFRS 16 decision, stated plainly.** The incumbent supports IFRS 16 and ASG does not use it.
Building it in ASG Edge+ is therefore a *product* choice about future international leases, not a
parity requirement. If the answer is no, five things drop out of this document: the standard-scoped
accounting dates (differ item 3), the standard-scoped practical expedients (item 4), the standard
dimension on the discount rate (item 5 of the typing section), the sibling-schedule link, and roughly
a fifth of the measurement surface. If the answer is yes, they are all still required — but they are
**greenfield design**, not a port, because there is no working IFRS 16 configuration to copy.
Put this in front of the business before the accounting service is scoped.

**A caveat on `DontAmortizeAssetValue`.** Its only configured value is unchecked, so `ACC-R-030`
cannot be observed behaving anywhere in ASG's data. It stays permanently **Inferred**. Either
implement it from the accounting standard and flag the divergence risk, or leave it out and record
the omission — do not claim parity on it.

## What must be built

Ordered by dependency.

| # | To build | Lucernex source | Notes |
|---:|---|---|---|
| 1 | **Fiscal calendar service** | `FiscalPeriod` (17 fields) | Portfolio-scoped, 12- or 13-period years, 4/5-week periods. Everything downstream indexes on it. The Accounting Engine BRD's period open/close model needs it as its period identity. |
| 2 | **Rate primitive + `DiscountRate` resolution** | `DiscountRate` (16 fields), `Contract.ComputedSLDiscountRate`, `Asset.DiscountRateOverride` | ACC-R-001…004. The BRD wants IBR *"by term tier and effective date"* in the Rule Administration UI — that is `MinSchedMons`/`MaxSchedMons`/`EffectiveThroughDate` generalised. **No `Rate` primitive exists yet.** |
| 3 | **Classification service** | `ContractFinancialTest` (93 fields) | ACC-R-005…019. The five tests, the two computed ratios, locking, propagation. Thresholds move to the Rule Administration UI (versioned, effective-dated) instead of `Contract.FairValueThreshold` / `.RemainingEconomicLifeThreshold`. |
| 4 | **Measurement service** | `ContractFinancialTest` ASC842*/IFRS16* blocks | ACC-R-031…036. ⚠ ACC-R-033 (initial asset balance) is undocumented in Lucernex; ASG Edge+ must derive it from ASC 842-20-30-5 rather than copy it. |
| 5 | **Schedule generation + period ledger** | `SLSummary` (134) / `SLPeriod` (79) | ACC-R-025…030, 037…044. This is the bulk of the work. |
| 6 | **Schedule versioning / remeasurement** | `PriorLastPostedPeriodID`, `Posted*Adj*`, `Inactive`, `Shortened*` | ACC-R-045…049. Maps cleanly onto the BRD's reversal model **if** a remeasurement is expressed as reverse-and-repost rather than as a mutable chain. |
| 7 | **Recalculation dirty-flag engine** | `NeedsRecalculation` + the four audit fields + `RecalcOverrideNotes` | ACC-R-020…024. BRD 16 FR-028/FR-030/FR-031 already require better than Lucernex: report every No→Yes transition, drill from the recalc list into the specific audit events, and clear a flag with a mandatory rationale. |
| 8 | **GL account mapping** | 20 `ExportAcctNNumber` slots on the single `842 Rent` schedule type; 16 more slots on `AccrualTransaction` | ⚠ **Do not port the 20 numbered slots.** The BRD specifies mapping rules keyed on `(transaction type, expense group, expense type, cost center, property/portfolio) → (debit account, credit account)` with double-entry validation. That is strictly better and strictly different. The migration input is now **one row of twenty values**, which makes reverse-engineering the slot semantics a single capture rather than a survey. |
| 9 | **Accrual sub-engine** | `ExpenseAccrualSetup`/`Schedule`, `AccrualTransaction` | ACC-R-052…054. Owned by BRD 23; submits candidates to the engine at `Generated`. |
| 10 | **FX translation** | 12 `SLPeriod` fields, `Contract.IsTranslation`, `ExchangeRate` | ACC-R-043/044. ⚠ One published formula is probably wrong (see [`rules.md`](rules.md) ACC-R-043). |
| 11 | **Roll-forward + maturity disclosures** | 25 + 14 `SLSummary` fields | Derivable from the period ledger; Lucernex stores them, ASG Edge+ probably should not. |
| 12 | ⚠ **Schedule review/approval gate** | The live `ASC 842 Schedule Review/Approval` workflow, its 3 steps and 4 `ASR` form layouts | `ACC-R-060`…`062`. **Not in the Accounting Engine BRD** — §7 governs transaction approval; this governs *schedule* approval, one level up, with two parties. Needs a schedule state machine (`draft → submitted → under review → ASG-approved → client-approved`), a rejection path, and an approval record per step. |
| 13 | **Portfolio-level accounting policy** | `Program`: `SLDiscountRate`, `FairValueThreshold`, `RemainingEconomicLifeThreshold`, `SL{Asset,Cash,Expense}AmortizeMethod`, `SLProrate35As28`, `SLMatchYearEnds`, `FiscalYearEnd`, 14 FX rate types | `ACC-R-056`…`059`. These are exactly the parameters BRD §12 wants in the **Rule Administration UI** — versioned, effective-dated, four-eyes approved. Lucernex has them as bare unversioned columns. |

## What should deliberately differ

| # | Lucernex does | ASG Edge+ should | Why |
|---:|---|---|---|
| 1 | Stores classification thresholds as **per-contract columns** (`Contract.FairValueThreshold`, `.RemainingEconomicLifeThreshold`), resolved portfolio→firm at read time | Hold them in the **Rule Administration UI**: versioned, effective-dated, four-eyes approved, and *"shall not retroactively affect transactions that were already Posted under the prior parameter value"* | Accounting Engine BRD §12. A per-contract column cannot express an effective-dated policy change, which is exactly what a threshold change is. |
| 2 | Three independent Booleans (`IsSLSchedule`, `IsASC842Schedule`, `IsIFRS16Schedule`) with no uniqueness constraint | **One `reportingStandard` enum** with a uniqueness constraint on `(contract, standard, active)` | Nothing in Lucernex prevents two of the flags being true, or two active schedules of the same standard. |
| 3 | Reuses `Topic842BeginDate` / `Topic842EndDate` for the IFRS 16 measurement | **Standard-scoped accounting windows** — *only if IFRS 16 is in scope* | An entity that adopted IFRS 16 in 2019 and ASC 842 in 2022 cannot express both dates in one pair. See [`ifrs-16.md`](ifrs-16.md#what-a-rebuild-must-add-that-lucernex-does-not-have). Contingent on the IFRS 16 decision above. |
| 4 | One `IsShortTerm` / `IsLowAssetValue` checkbox shared across both standards, and undocumented as to effect | **Standard-scoped, policy-driven practical-expedient elections** with a low-value threshold from the Rule Administration UI (BRD §12 lists *"low-value asset thresholds per tenant"*) | ASC 842 has no low-value expedient; IFRS 16 does. One checkbox cannot express both policies. Contingent on the IFRS 16 decision above; if IFRS 16 is out of scope, only the ASC 842 short-term expedient is needed. |
| 5 | Approval is **irreversible with no back door except an `lxadmin` JSP** | Reversal by **reversing entry**, never by un-approval | Accounting Engine BRD §10. Removes the need for a `SLDemoTweaks.jsp` equivalent entirely. |
| 6 | `sTYPE_PERCENT_OR_AMOUNT` — the unit is guessed from the value's magnitude | **Two columns, or one column plus an explicit unit discriminator** | See the hazard table below. This is the worst single typing decision in the Lucernex schema. |
| 7 | 20 numbered, unnamed GL export slots per schedule type, denormalized onto every period row | **Named mapping rules** with double-entry validation at posting time | Accounting Engine BRD §8. |
| 8 | Multi-valued relationships in delimited `TEXT` columns (`AssociatedExpenseSetupIDs`, `RecalcOverrideNotesIDList`, `NeedsRecalcModifiedByMemberIDList`) | **Join tables** | Standard normalization; the Lucernex delimiter is not even documented. |
| 9 | Stores 39 aggregate disclosure fields on `SLSummary` (roll-forward + maturity) that duplicate `SLPeriod` sums | **Derive at read time**, or materialise deliberately with a documented refresh trigger | 25 of the 39 have no vendor definition at all — they are the least-understood block in the module, and storing an undocumented aggregate is how it stays undocumented. |
| 10 | Carries dead fields for years (`SuspendSL`, four `Ratio*`, four `*Renewal*`, `CodeAssetTypeTestID`, `SectionNumber`, `DateRange`, `AdjustmentPercent`, `FiscalPeriodName`) | **Migrate the data for audit; do not implement the fields** | 15 DEAD fields are enumerated in [`computed-vs-input-fields.md`](computed-vs-input-fields.md#the-15-dead-fields). |
| 11 | Keeps the ASC 840 Cap Lease Test live on `contract_admin` alongside the ASC 842 test | **Migrate as historical read-only data**; do not implement the logic | Two different five-test structures with different Test 4 arithmetic and a 5a/5b split. Confirm with ASG that no report reads it. |
| 12 | `AlternateRentSchedule.SetExpHoldFlag` / `.SetPRHoldFlag` set an inert `HoldFlag` on generated transactions | Express as a **transaction lifecycle state**, not a flag | Every `HoldFlag` in the Lucernex module is documented as *"informational-only"*, which means the hold is enforced by convention, not by the system. |
| 13 | Approval is a single Boolean (`SLSummary.IsApproved`) with the review process held entirely in a separate workflow engine | **One schedule state machine**, with the review steps as states on the schedule itself | The five real states are `draft / submitted / under review / ASG-approved / client-approved`; Lucernex can represent only the last. Splitting the state across `SLSummary` and a workflow instance is why there is no rejection path and no re-open path. |
| 14 | The review workflow cannot be raised against an `Equipment Contract`, although equipment leases produce ASC 842 schedules | **One approval path for both** real-estate and equipment schedules | `ACC-R-061`. Either Lucernex's equipment schedules bypass the gate or they are approved at portfolio level; neither is a design to copy. |
| 15 | Three separate amortisation-basis switches (`SLAssetAmortizeMethod`, `SLCashAmortizeMethod`, `SLExpenseAmortizeMethod`), each `Text` | **Keep all three**, but as a typed enum, effective-dated in the Rule Administration UI | Tempting to collapse to one. Don't: they are independently set, and the asset one carries a scope restriction the other two do not (*"only ASC 842 Finance leases"*). |

## Typing hazards — Constitution §4.4 and beyond

Constitution §4.4 forbids `double` in financial code and requires JSON numeric attributes to be stored
as strings and parsed. This module makes that harder than usual, for five specific reasons.

### 1. `Money` scales to 2 decimal places; the BRD requires 4

`ASG-EdgePlus-Platform`'s `Money` record does:

```java
amount = amount.setScale(currency.getDefaultFractionDigits(), RoundingMode.HALF_EVEN);
```

For USD that is **scale 2**. The Accounting Engine BRD §15 states: *"All currency fields shall use
BigDecimal precision with a minimum of four decimal places to prevent rounding errors in financial
calculations."* These are in direct conflict, and the conflict bites exactly here: an amortization
schedule computes per-period amounts by dividing a total across N periods, and rounding each
intermediate to cents accumulates a visible drift over a 120-period lease.

**Recommendation**: keep `Money` at presentation scale for balances that are *reported*, and
introduce a separate calculation type (or a `Money.ofScale(int)` factory) at scale ≥ 4 for
intermediate schedule arithmetic, with an explicit rounding-and-plug step at the end of each period.
This is a decision for the Platform repo, not for the accounting service, and it blocks item 5 in the
build list.

### 2. There is no `Rate` primitive

`Money` is the only financial primitive in `asg-edgeplus-primitives`. This module needs at least
three more numeric kinds, each with a different scale:

| Kind | Lucernex evidence | Scale needed |
|---|---|---|
| Discount rate / IBR | `sTYPE_PERCENTAGE`, `Percentage`, max size **999999** | 6 significant digits; e.g. `4.375000%` |
| FX conversion rate | `SLPeriod.ConversionRateAverage`, `.ConversionRateMonthEnd` — `sTYPE_NUMBER_FRACTION6DIGITS` | **6 decimal places**, explicitly |
| Threshold percentage | `FairValueThreshold` (90%), `RemainingEconomicLifeThreshold` (75%), `PortionOfAssetControlled` | 6 significant digits |

Modelling a discount rate as `BigDecimal` alone loses the "this is a rate, not an amount" distinction
and invites the classic 0.04375-vs-4.375 unit bug across a service boundary.

### 3. ⚠ `Percent or Currency` — the value carries no unit

`SLSummary.SLRemainingAssetBalance` and `Asset.RemainingAssetBalance` are Lucernex type
`Percent or Currency` / `sTYPE_PERCENT_OR_AMOUNT`, declared max size `2147483647`. The vendor
documents the behaviour exactly:

> *"There are two option buttons: Currency and Percentage. If you enter a value between 0-100, the
> system will default the option button setting to Percentage. If you enter a value of 100.01 or
> above, the system will default the option button setting to Currency. **You can override the
> default option button setting.**"*

Because the override is possible, **the stored number cannot be interpreted without the option-button
state**, and the object dump contains no column holding that state. A migration that guesses by
magnitude will silently misread every record where a user overrode the default — for example a
`50` that means $50, not 50%.

Both fields govern how much ROU asset remains after the schedule end date on a **finance** lease, so a
misread produces a wrong balance sheet, not a cosmetic error.

**Recommendation**: model as `RemainingAssetBalance(BigDecimal value, Unit unit)` where `Unit ∈
{PERCENT, CURRENCY}`, and treat every migrated Lucernex row whose value is in `[0, 100]` as
**requiring manual confirmation** rather than auto-assigning `PERCENT`. Raise it as a migration
open question, not an implementation detail.

### 4. Every non-key source column is `TEXT`

Of the 7,069 typed columns in the jcrew PostgreSQL export, 6,882 are `TEXT`; the remaining 187 are
`VARCHAR(64) NOT NULL` and are all primary keys. There is no numeric typing to inherit and no
database-level guarantee that any currency column contains a number.

⚠ **But the all-`TEXT` columns are a persistence-layer artefact, not the vendor's design intent.**
The live GraphQL API declares a 10-value canonical type system —
`BOOLEAN COMPUTED DATE DATETIME FK FLOAT INTEGER MONEY PERCENTAGE STRING` — in which **`MONEY` and
`PERCENTAGE` are distinct from `FLOAT`**, and it publishes **`BigDecimal` as a scalar**. Accruent
independently reached ASG Edge+ Constitution §4.4's conclusion: money is not a float. *(Observed,
`docs/data-model/graphql-api.md`.)*

Two consequences:

1. **§4.4 is not an ASG idiosyncrasy to defend** — it is the same call the incumbent vendor made. Use
   that when the rule is questioned.
2. **The migration should read the GraphQL API, not the Postgres export, wherever it can.** The API
   returns `BigDecimal`; the export returns `TEXT`. One of those two sources preserves the type and
   the other throws it away. Every migrated
value must be parsed, and a parse failure is a data-quality finding to be reported, not an exception
to swallow. This aligns with Constitution §4.4's "stored as strings and parsed" rule — but note the
rule was written for JSON attributes, and here it applies to the *entire* source dataset.

Declared bounds, for sizing: `Currency` max `999999999999999` (15 digits, scale undeclared —
`BigDecimal(19,4)` covers it); `Percentage` max `999999`; `Number` variously `99`, `9999`, or
`2147483647`. The "2-Digit Number" and "5-Digit Number" labels are display hints, not constraints —
both declare max `2147483647`.

### 5. Three-state vs. two-state Booleans of the same name

`Asset.IsShortTerm` and `Asset.IsLowAssetValue` are `sTYPE_NULL_CHECKBOX` (true / false / **unset**).
`Contract.IsShortTerm` and `Contract.IsLowAssetValue` are `sTYPE_CHECKBOX` (true / false). Modelling
both as primitive `boolean` destroys the asset-level "unset" state, which is almost certainly
"inherit from the contract". Use `Boolean` (nullable) on the asset side and document the inheritance
rule explicitly — Lucernex does not.

## Architecture placement

*Evidence class: **Inferred** — applying the workspace `CLAUDE.md` architecture rules to this module.*

| Question | Answer | Basis |
|---|---|---|
| Which service owns the ledger? | A new **Accounting service**, not Configuration-Service | The Accounting Engine BRD makes it *"an internal platform service — the financial backbone"* with an exclusive write path. Configuration-Service owns Masters and Layouts. |
| Hub or Spoke? | **Spoke** for `SLSummary` / `SLPeriod` / `ContractFinancialTest` / accruals — they hang off Contract, which is Spoke. **Hub** for `DiscountRate`, the three schedule-type code tables, `CodeExpenseType`, `FiscalPeriod`, and the Rule Administration parameters | Workspace `CLAUDE.md`: the Spoke holds "Portfolios, Contracts, and everything under a Contract"; the Hub holds Masters, global Drop Downs, and shared entities. |
| Shared domain types with Contract-Service? | **No.** Share contracts via events | `java-architecture` SKILL §7.7 / workspace `CLAUDE.md`: *"No shared domain library across services."* The accounting engine consumes contract and expense data by event, not by importing a `Contract` class. |
| JWT validation? | **No.** Use `asg-edgeplus-starter-identity` | Only the gateway validates JWTs. |
| Money precision decision? | **Platform repo** (`asg-edgeplus-primitives`) | It would force two services to change together if it lived in the accounting service — which is exactly the test in `ASG-EdgePlus-Platform`'s README. |

⚠ **Note the ADR-004 conflict.** `KnowledgeFolder/asg-edge-plus-kb/decisions/ADR-004-multi-tenancy-database-per-tenant.md`
specifies database-per-tenant; `ASG-Edgeplus-Configuration-Service/.vault/decisions/0004-multi-tenant-defense-in-depth.md`
specifies one shared platform database. The two have never been reconciled. The accounting ledger is
the single most SOX-sensitive dataset in the product, so this module should not be designed until the
conflict is resolved — and it argues strongly for the database-per-tenant reading.

## Blocking decisions

| # | Blocker | Blocks | Owner |
|---:|---|---|---|
| 1 | **ADR superseding ADR-0020** (in-transaction audit vs. the ADR-0012 outbox, still a `NoOpOutboxPublisher`) | The engine's §14 audit-logging requirement — *every* candidate submission, status transition, approval and reversal must be durably logged. A `NoOp` publisher cannot carry a SOX audit trail. | Architecture |
| 2 | **`Money` scale: 2 or ≥4?** | Build item 5 (schedule generation). Cannot start amortization arithmetic without resolving it. | Platform repo |
| 3 | **ADR-004 reconciliation** (database-per-tenant vs. shared) | The ledger's physical design. | Architecture |
| 3b | **⚠ Is IFRS 16 in scope for ASG Edge+?** The incumbent supports it and ASG does not use it. | Roughly a fifth of the measurement surface, plus differ items 3 and 4 and the discount-rate standard dimension. | **Business / Product** |
| 3c | **Are Accounting Method, Accounting Adjustment Type, Accrual Type, Proration Method, Frequency and Frequency Unit tenant-configurable or fixed?** None is among the 207 Firm Drop Downs, unlike the schedule types. | Whether they are Masters rows or hard-coded enums — a Configuration-Service scoping question. | Architecture / MDM-01 |
| 4 | **Is the Cap Lease Test in scope at all?** | Whether ~28 `contract_admin` columns migrate as data-only or not at all. | ASG / Product |
| 5 | **Do `IsShortTerm` / `IsLowAssetValue` gate anything in Lucernex?** | Whether the practical-expedient logic is a port or a greenfield build. | Live-UI check |
| 6 | **`Schedule Creation Reason Code` values** | The schedule-versioning design — whether a recalculation creates a new `SLSummary` or updates in place. | Live-UI check |
| 7 | **The initial-asset-balance formula (ACC-R-033)** | Build item 4. Undocumented in Lucernex; must be specified from the standard and confirmed against a live schedule. | Accounting SME |
| 8 | **(new) Does the schedule review gate belong in the Accounting Engine or in a general workflow service?** The BRD's §7 approval governance is transaction-scoped; this gate is schedule-scoped and two-party. | Build item 12 — the whole schedule state machine. | Architecture / Product |
| 9 | **(new) How are equipment-lease schedules approved?** `ACC-R-061` — the Lucernex form type excludes `Equipment Contract`. | Whether ASG Edge+ builds one approval path or two. | ASG / Product |

## Open questions

Ranked by how much they block the ASG Edge+ build. Items marked **(UI)** are things a browser session
can answer directly.

1. **What is the initial-asset-balance formula?** **(UI)** Open a schedule with known IDC, incentive
   and prepaid values and back it out. Blocks the measurement service.
2. **Does `Money` become scale-4, or does the accounting service get its own calculation type?**
   Blocks schedule generation. Platform decision, not a Lucernex question.
3. **How does the ASG Edge+ reversal model express a lease remeasurement?** Lucernex creates a
   successor `SLSummary` with six delta fields and inactivates the predecessor; the BRD's model is
   reverse-and-repost. These are reconcilable, but the reconciliation has not been written down.
4. **`Schedule Creation Reason Code` values.** **(UI)** `Admin > Manage Firm Drop Downs`.
5. **Which `ExportAcctNNumber` slot is which GL concept in the jcrew tenant?** **(UI)** Needed to map
   legacy exports onto the BRD's named debit/credit mapping rules.
6. **Is `SLRemainingAssetBalance`'s Percent/Currency option-button state persisted anywhere?** **(UI)**
   If not, the migration of that field is lossy and needs a manual review pass.
7. **Where do `Admin > Manage Company > Financial Settings` live?** **(UI)** Both the
   Short-Term/Long-Term Liability Calculation Method and the Translation/Revaluation mapping are
   there, and neither has a home in the object model.
8. **Does BRD 16 already answer any of the ASC 842 open questions in [`asc-842.md`](asc-842.md)?**
   Its 1,333 lines were sampled, not read end to end, for this document. A full read against
   [`rules.md`](rules.md) is the cheapest next step and needs no browser. BRD 16's FR-019 already
   names an "Approved?" checkbox and a "Recalc?" indicator at schedule level, and FR-028/030/031
   already specify recalc-flag reportability, audit drilldown and clear-with-rationale — so some of
   this is specified. Whether it specifies the *three-step, two-party* gate is the question.
8b. **(new) What does each `ASR` form layout collect?** **(UI)** Four layouts — `Submit`,
   `Initial Review`, `Approve (ASG)`, `Approve (Client)` — define the approval record ASG Edge+ must
   reproduce. None has been opened.
8c. **(new) Does the GraphQL schema expose the canonical `FieldType` per field?** **(UI)** If it does,
   one introspection query verifies all 666 rows of
   [`computed-vs-input-fields.md`](computed-vs-input-fields.md) against the vendor's own
   classification — cheaper and more reliable than any other check in this folder.
8d. **(new) What are the `Exchange Rate Type Code` values?** **(UI)** Fourteen `Program` columns
   select from it (`ACC-R-059`) and none of the values is available offline.
8e. **(new) What are the twenty `ExportAcctNNumber` values on `842 Rent`?** **(UI)** One row at
   `FirmCodeEdit.jsp?TableType=2162`. This is the input to the BRD's named debit/credit mapping
   rules, and it is now a single capture.
8f. **(new) Are there `SLSummary` rows with `IsSLSchedule` or `IsIFRS16Schedule` true?** Both
   schedule-type tables are empty, so any such row is an orphan still carrying balances. A migration
   blocker if any exist.
8g. **(new) Does `AI Abstracted` on `Contract Status Code` (2094) affect the accounting engine?**
   ASG has a tenant-added contract status recording that a lease was abstracted by AI. It is upstream
   of this module, but if AI-abstracted contracts feed schedules on a different confidence footing,
   the accounting engine needs to know. **Observed** in the registry; the accounting consequence is
   unexamined.
9. **Is the Cap Lease Test read by any live ASG report?** **(UI / ASG)**
10. **Does ASG report under IFRS 16 at all?** If not, items 3 and 4 in "what should deliberately
    differ" drop to low priority and the IFRS 16 surface migrates as dormant schema.

---

**Registration note.** `docs/CONVENTIONS.md` requires every new document to be registered in
`docs/INDEX.md`. This folder was written under an instruction not to modify anything outside
`docs/modules/accounting/`, so `docs/INDEX.md` has **not** been updated. It currently has no
`## Modules` section; one is needed, pointing at this folder's `README.md` (which indexes the other
seven files).
