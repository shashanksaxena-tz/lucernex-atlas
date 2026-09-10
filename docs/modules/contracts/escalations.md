# Escalations

**Stated up front.** Lucernex models escalation as a **single object with two mutually exclusive
drivers and a four-level collar**. `ExpenseEscalation` (28 fields) attaches to an `ExpenseSetup`
and escalates its amount every `EscalationPeriod` periods. The driver is either **fixed**
(`FixedAmount`, or a percentage carried in `EscalationMethod`) or **index-based** (`EscalationIndexID`
→ `EscalationIndex`, with `IndexBaseFactor` and `CPIMultiplier`). The collar is
`PeriodMinPercentage`/`PeriodMaxPercentage` per step and
`LifetimeMinPercentage`/`LifetimeMaxPercentage` across the whole clause, plus an absolute
`CapAmount` and a `StopAmount`.

Crucially, escalation is **not** a schedule generator in its own right. It is an input to the
`ExpenseSchedule` generator. The evidence: `ExpenseSchedule` carries `IsCPI(Boolean)`,
`AdjustmentMethod(Text)`, `CodeAdjustmentMethodID`, and a
`PreviousAnnualAmount`/`AnnualAmount`/`NextAnnualAmount` triple — the escalated step is
materialised onto the schedule row, not held separately. **Observed.**

---

## 1. `ExpenseEscalation` — all 28 fields

**Observed** from `_lucernex_objects_summary.txt`; labels from
`docs/data-fields/expense-escalation.md`.

| Field | Type | Role |
|---|---|---|
| `ExpenseEscalationID` | `Number` | PK |
| `BOMapClientRecordID` | `Text` | Client mapping key |
| `ContractID` | `Contract ID` | Parent |
| `ExpenseSetupID` | `Expense Setup ID` | **The clause it escalates** |
| `ProjectEntityID` | `Entity ID` | Polymorphic root |
| `BeginDate` / `EndDate` | `Date` | Escalation window |
| `EscalationPeriod` | `Number` | How many periods between steps |
| `CodeFrequencyID` | `Dropdown (Frequency Code)` | The period unit |
| `CodeEscalationTypeID` | `Dropdown (Escalation Type Code)` | **The driver selector.** Members unknown. |
| `CodeEscalationCategoryID` / `CodeEscalationGroupID` | `Dropdown` | Classification |
| `EscalationMethod` | `Text` | How the step is computed. **Typed `Text`, not a code — a hazard.** |
| `FixedAmount` | `Currency` | The fixed-driver amount |
| `BaseAmount` | `Currency` | The amount escalation is measured from |
| `BaseYear` | `Text` | The base year label |
| `EscalationIndexID` | `Escalation Index ID` | **The index-driver FK** |
| `IndexBaseFactor` | `Percentage` | The base index reading, as a factor |
| `PeriodMinPercentage` / `PeriodMaxPercentage` | `Percentage` | Per-step collar |
| `LifetimeMinPercentage` / `LifetimeMaxPercentage` | `Percentage` | Whole-clause collar |
| `CapAmount` | `Currency` | Absolute ceiling on the escalated amount |
| `CapPercentage` | `Percentage` | Percentage ceiling |
| `StopAmount` | `Currency` | An expense **stop** — the level above which escalation transfers to the tenant |
| `ModifiedByID` / `ModifiedDate` / `Notes` | | Audit |

Note what is **absent**: no `AmendmentID`, no `CovenantID`, no `Section`, no `RevNumber`. By the
[layer discriminator test](setup-schedule-transaction-pattern.md#2-how-to-tell-which-layer-a-record-is-in--the-discriminator-test),
`ExpenseEscalation` is **not** a clause record — it is a *modifier attached to* the
`ExpenseSetup` clause. That is why it lives in the same layer as `ExpenseAllocation` and
`ExpenseVendorAllocation`, both of which are also `ExpenseSetupID`-scoped modifiers. **Derived.**

---

## 2. Fixed escalation

Driver fields: `FixedAmount`, `BaseAmount`, `EscalationMethod`, `EscalationPeriod`, `CodeFrequencyID`.

```
every EscalationPeriod × CodeFrequencyID:
    newAmount = f(BaseAmount or currentAmount, FixedAmount, EscalationMethod)
```

`EscalationMethod(Text)` is the discriminator between the plausible forms — add a flat amount, add
a percentage, set to a new amount, compound — but it is **free text**, which means Lucernex
either constrains it in the UI or tolerates arbitrary strings. **Observed** that it is `Text`;
the value space is unknown and is open question 2.

The corresponding materialisation on `ExpenseSchedule` is explicit and readable:

| `ExpenseSchedule` field | Role |
|---|---|
| `PreviousAnnualAmount` / `AnnualAmount` / `NextAnnualAmount` | The escalation step, visible on one row |
| `PreviousPaymentAmount` / `PaymentAmount` / `NextPaymentAmount` | Same, at payment granularity |
| `AdjustmentMethod(Text)` + `CodeAdjustmentMethodID` | Which method produced this row's amount |
| `PreviousExpenseScheduleID` / `NextExpenseScheduleID` | The linked list of steps |
| `FirstPaymentAmount` / `LastPaymentAmount` | Stub proration at the ends |

**This is the cleanest thing in the whole engine and ASG Edge+ should copy it directly:** an
escalating schedule is a doubly-linked list of period rows, each of which knows its own amount and
both neighbours' amounts. It makes an escalation auditable on a single row.

---

## 3. Index-based escalation (CPI)

### `EscalationIndex` — 12 fields, one published reading

| Field | Type | Role |
|---|---|---|
| `EscalationIndexID` | `Number` | PK |
| `EscalationIndexName` | `Text` | e.g. "CPI-U US City Average" |
| `CodeIndexTypeID` | `Dropdown (Index Type Code)` | CPI, RPI, PPI, … |
| `CodeIndexSourceID` | `Dropdown (Index Source Code)` | Publisher (BLS, ONS, …) |
| `CodeIndexGroupID` | `Dropdown (Index Group Code)` | Grouping |
| `IndexAmount` | **`Percentage`** | **The reading itself** |
| `PeriodMonth` / `PeriodYear` | `Number` | Which month the reading is for |
| `EffectiveDate` | `Date` | When it applies from |
| `BOMapClientRecordID`, `ModifiedByID`, `ModifiedDate` | | |

**`EscalationIndex` is contract-agnostic** — it has no `ContractID`. It is a shared reference series
loaded once per tenant and referenced by every escalation clause. The `IMPORT_CPI_DATA` command
(on `ProjectEntity`, i.e. a batch operation) loads it. **Observed.**

**`IndexAmount` is typed `Percentage`, not a raw index level.** That is unexpected — CPI is
normally published as a level (e.g. 312.332), not a percentage. Two readings:

| Reading | Consequence |
|---|---|
| (a) Lucernex stores the published **level** in a field cosmetically typed `Percentage` | `IndexBaseFactor` holds the base-period level and the escalation is `IndexAmount / IndexBaseFactor` |
| (b) Lucernex stores the year-over-year **change rate** | `IndexBaseFactor` is a dampening multiplier and the escalation is `IndexAmount × IndexBaseFactor` |

Reading (a) fits the name `IndexBaseFactor` and the standard lease formula. **Inferred, and this is
open question 1 — it must be confirmed before any CPI code is written.**

### Application

```
─ inputs ─────────────────────────────────────────────────────────────
  IndexAmount        from EscalationIndex, for the period matching this step
  IndexBaseFactor    from ExpenseEscalation — the base-period index reading
  CPIMultiplier      from ExpenseSetup (Number) — a fractional application factor
  IsCPICompounding   from ExpenseSetup (Boolean) — compound vs simple
  CodeCPIIndexID     from ExpenseSetup (Dropdown (CPI Index Code)) — which index

─ step ───────────────────────────────────────────────────────────────
  rawChange   = (IndexAmount / IndexBaseFactor) − 1          [reading (a)]
  applied     = rawChange × CPIMultiplier
  collared    = clamp(applied, PeriodMinPercentage, PeriodMaxPercentage)
  newAmount   = baseFor(IsCPICompounding) × (1 + collared)
  newAmount   = min(newAmount, CapAmount)
  cumulative  = clamp(cumulativeChange, LifetimeMinPercentage, LifetimeMaxPercentage)
```

`baseFor(IsCPICompounding)`: the **current** amount when compounding, the **`BaseAmount`** when not.
That is the entire meaning of `ExpenseSetup.IsCPICompounding(Boolean)`. **Derived.**

The whole formula is **Inferred** — the fields exist and this is the standard lease CPI mechanic,
but no screen was opened. `CON-R-040`…`CON-R-047` in [`rules.md`](rules.md) carry the same
confidence labels.

### CPI fields living on `ExpenseSetup` rather than `ExpenseEscalation`

This is a real split and easy to miss:

| Field | On | Type |
|---|---|---|
| `CodeCPIIndexID` | **`ExpenseSetup`** | `Dropdown (CPI Index Code)` |
| `CPIMultiplier` | **`ExpenseSetup`** | `Number` |
| `CPINotes` | **`ExpenseSetup`** | `Text` |
| `IsCPICompounding` | **`ExpenseSetup`** | `Boolean` |
| `Firm_CPIIncrease` | **`ExpenseSetup`** (Firm scope) | `Boolean` |
| `EscalationIndexID` | `ExpenseEscalation` | `Escalation Index ID` |
| `IndexBaseFactor` | `ExpenseEscalation` | `Percentage` |
| `IsCPI` | **`ExpenseSchedule`** | `Boolean` |
| `IsCPI` | **`VirtualExpenseForecastPeriod`** | `Boolean` |

So a CPI clause is configured across **three** objects, and the "is this row CPI-driven?" flag is
carried down onto both the schedule and the forecast. `CodeCPIIndexID` on `ExpenseSetup` and
`EscalationIndexID` on `ExpenseEscalation` appear to be **two ways of naming the same index** —
one a dropdown code, one an FK. **Observed** that both exist; whether they are redundant or serve
different purposes (e.g. dropdown selects the *series*, FK selects the *reading*) is open
question 3.

### The `CPI_ADJUSTMENTS` command

`Contract` exposes `CPI_ADJUSTMENTS` (label *"CPI Adjustments"*) as a `sTYPE_SUBMITBUTTON`, and
`ProjectEntity` exposes `IMPORT_CPI_DATA` (*"Import CPI Data"*). Together: load the index series in
bulk, then apply it per contract. **Observed.** Whether `CPI_ADJUSTMENTS` rewrites existing
`ExpenseSchedule` rows in place or generates new ones is open question 4 — it determines whether a
retroactive CPI restatement is a schedule mutation or a new schedule generation with a
`GENERATE_RETRO_PAYMENT` catch-up.

---

## 4. The four-level collar

Escalation is bounded at four independent levels. All **Observed**.

| Level | Fields | Applies to |
|---|---|---|
| **Per step, percentage** | `PeriodMinPercentage`, `PeriodMaxPercentage` | The change in one escalation step |
| **Lifetime, percentage** | `LifetimeMinPercentage`, `LifetimeMaxPercentage` | Cumulative change over the whole clause |
| **Absolute ceiling** | `CapAmount`, `CapPercentage` | The escalated amount itself |
| **Expense stop** | `StopAmount` | The threshold above which the cost transfers |

And on `ExpenseSetup`, a **separate, parallel** collar for the setup's own amount:

```
ExpenseSetup.AmountIncreaseCap(Currency)     ExpenseSetup.AmountDecreaseCap(Currency)
ExpenseSetup.PercentIncreaseCap(Percentage)  ExpenseSetup.PercentDecreaseCap(Percentage)
```

Note the **asymmetry**: `ExpenseSetup` has separate increase and decrease caps (a CPI clause that
falls should not reduce rent below a floor), while `ExpenseEscalation` uses min/max pairs. Both sets
exist simultaneously and their precedence is unspecified — open question 5.

A third parallel set exists for **forecasting** on both `ExpenseSetup` and `ExpenseAccrualSchedule`:

```
ForecastCapPercent / ForecastGrowthPercent / ForecastAdjustment
PlanCapPercent     / PlanGrowthPercent     / PlanAdjustment
```

i.e. planning and forecasting use their **own** assumed growth rates, independent of the contractual
escalation. `ExpenseSetup.IncludeInPlanForecast(Boolean)`, `CodePlanForecastBasedOnID` and
`CodePlanForecastGroupID` gate it, and `VirtualExpenseForecastPeriod` materialises the result with
`PeriodExpense` vs `AdjustedPeriodExpense`. **Observed.** ASG Edge+ must keep contractual
escalation and forecast growth as **separate** concepts; conflating them is a common rebuild error.

---

## 5. Recovery escalation is a different mechanism

`ExpenseRecovery` has its own escalation fields and does **not** use `ExpenseEscalation`:

| Field | Role |
|---|---|
| `EscalationPercentage` | The rate |
| `EscalationAmountIncrease` (computed) | The resulting increase |
| `CodeEscalationPaymentMethodID` | How the increase is collected |
| `NewEscalationPayment` / `ProposedEscalationPayment` (computed) | The revised escrow payment |
| `CapAmountChangePercent` / `CapAmountChangeValue` | **The cap itself escalates** |
| `IsRecoveryCapEscalationNonCum` | Cumulative or not |

So there are **two escalation engines**: one that escalates a fixed expense amount
(`ExpenseEscalation`), and one that escalates a recovery **cap** and its escrow payment
(`ExpenseRecovery`). **Observed.** They share no fields and no FK. ASG Edge+ needs both, and should
name them distinctly rather than trying to unify them.

---

## 6. Escalation on the contract term side

`ContractTerm` carries no escalation of its own, but the **Contract Terms Wizard** does:

```
ContractTermWizard_TermLength(Number)              — length of the term in years
ContractTermWizard_OptionNumber(Number)            — number of options
ContractTermWizard_TermCoverageBeginDate(Date)     — first coverage begin
GenerateContractTerms(sTYPE_SUBMITBUTTON)          — the generator
```

and the **Expense Setup Wizard** carries the escalation authoring UI:

```
ExpenseSetupWizard_StartDate / _EndDate / _EffectiveDates
ExpenseSetupWizard_StartingAmout(Money)            [sic — typo in the platform]
ExpenseSetupWizard_FindStartingAmout(Checkbox)     [sic]
ExpenseSetupWizard_AmountType(Text)
ExpenseSetupWizard_TypeOfEscalation(sTYPE_EXPENSE_ESCALTION_TYPE)   [sic]
ExpenseSetupWizard_EscalateEvery(Number)           — years between steps
ExpenseSetupWizard_EscalateAmountRate(Money)       — the step size
GenerateExpenseSetup(sTYPE_SUBMITBUTTON)           — the generator
```

**Observed**, `docs/data-fields/expense-setup.md` / `contract-term.md`. This is the *authoring*
surface: an analyst states "start at $X on date D, escalate every N years by Y", presses Generate,
and the platform materialises `ExpenseSetup` + `ExpenseEscalation` + the whole `ExpenseSchedule`.
`_FindStartingAmout` ("Find Starting Amount") implies the wizard can work **backwards** from a
known later amount to derive the start — a genuinely useful feature for abstracting a lease
mid-term. **Inferred** from the label.

Three platform typos (`StartingAmout`, `FindStartingAmout`, `ESCALTION`) are preserved verbatim
here because they are the literal internal names a migration must match.

---

## Open questions

Ranked by impact.

1. **Is `EscalationIndex.IndexAmount` a published index *level* or a *change rate*?** (§3.) This
   single fact determines the CPI formula. Load two consecutive months of a known index and read
   the values — if they are ~312 and ~313 it is a level; if ~0.03 it is a rate.
2. **What is the value space of `ExpenseEscalation.EscalationMethod(Text)`?** It is the fixed-driver
   discriminator and it is free text. Query distinct values, or read the UI dropdown that populates
   it.
3. **`ExpenseSetup.CodeCPIIndexID` vs `ExpenseEscalation.EscalationIndexID` — redundant or
   complementary?** Two paths to the same index series.
4. **Does `CPI_ADJUSTMENTS` rewrite `ExpenseSchedule` rows in place or generate new ones?**
   Determines the retroactive-restatement model.
5. **Precedence between `ExpenseSetup`'s increase/decrease caps and `ExpenseEscalation`'s
   period/lifetime collar.** Both apply to the same amount; which binds first?
6. **What are the members of `Dropdown (Escalation Type Code)`, `(Escalation Category Code)`,
   `(Escalation Group Code)`, `(Index Type Code)`, `(Index Source Code)`, `(CPI Index Code)`,
   `(Adjustment Method Code)`, `(Escalation Payment Method)`?** Eight code lists, all readable from
   `FirmCodeList.jsp` (screen 007).
7. **Does `StopAmount` behave as an expense stop (tenant pays the excess) or as a hard ceiling?**
   The name says stop; `CapAmount` already covers ceiling, which supports the stop reading — but it
   is unconfirmed.
8. **Is `ExpenseEscalation` one row per clause or one row per step?** `BeginDate`/`EndDate` +
   `EscalationPeriod` reads as one row per clause driving many steps, but a per-step model would
   also fit. Check whether a 10-year lease with annual escalation has 1 or 10 rows.
