# Expense recovery / CAM

**Stated up front — why 565 fields.** `ExpenseRecovery` is not 565 concepts. It is **63
configuration fields plus a 502-cell computation grid**, and the grid is a clean three-dimensional
cross-product:

```
502  =  9 valuation perspectives  ×  ~19 measures  ×  {Gross, Net}
```

The 9 perspectives are `Reported`, `Approved`, `Budgeted`, their three `Prior`-year counterparts,
and six pairwise variance families (`R−A`, `A−B`, `R−P`, `A−P`, `B−P`, with `%` siblings for the
three vs-Prior families). The ~19 measures are the line items of a CAM reconciliation worksheet.
`Gross` and `Net` are the two exclusion bases.

The grid exists because Lucernex **materialises the entire CAM audit worksheet as columns**. 360 of
the 567 catalog leaves (63%) are typed `sTYPE_MONEY_MATH_OPERATION` (233) or
`sTYPE_PERCENT_MATH_OPERATION` (127) — *"System-calculated … (computed, not directly entered)"* —
so nearly two thirds of the surface is derived. Only ~105 fields are `sTYPE_MONEY` inputs.
**Observed**, `docs/data-fields/expense-recovery.md`.

And the payoff: **Lucernex encoded the CAM waterfall in the UI labels of the computed fields.** The
six-step formula is recoverable exactly, with no inference required. See §3.

---

## 1. The 63 configuration fields — what CAM actually models

These are `ExpenseRecovery`'s own, non-grid fields. Grouped by what they configure.
**Observed** from `_lucernex_objects_summary.txt` + labels from `docs/data-fields/expense-recovery.md`.

### Identity and clause provenance
`ExpenseRecoveryID`, `BOMapClientRecordID`, `ContractID`, `AmendmentID`, `CovenantID`, `Section`,
`RevNumber`, `CreatedByID`, `CreatedDate`, `ModifiedByID`, `ModifiedDate`, `Notes`,
`DocumentIDList`, `BeginDate`, `EndDate`, `CodeCurrencyTypeID`

### Classification — what kind of recovery this is
| Field | Label | Role |
|---|---|---|
| `CodeRecoveryTypeID` | Recovery Type | The recovery model |
| `CodeRecoveryGroupID` | Recovery Group | Grouping |
| `CodeExpenseGroupID` / `CodeExpenseTypeID` | Expense Group / Type | GL + accounting treatment (via `CodeExpenseType`) |
| `CodeCalculationMethodID` | Calculation Method | How the recoverable amount is computed |
| `CodeExpRecBasedOnID` | Exp Rec Based On | The basis (area? sales? occupancy?) |

### Pro-rata share
| Field | Label |
|---|---|
| `CodeProRataShareMethodID` | Pro Rata Share Method |
| `OccupancyAdjustedThreshold` (`sTYPE_PERCENT_MATH_OPERATION`) | **Occupancy Factor** — computed |
| `GrossupRate` (`sTYPE_MONEY`) | Grossup Rate |

Plus the per-perspective `ReportedProRataShareRate`, `ApprovedProRataShareRate`,
`BudgetedProRataShareRate` in the grid, and `ReportedRentableArea` / `ReportedGLA` (and their
Approved/Budgeted twins) — the numerator and denominator of the share.

### Base year (the "expense stop")
`BaseYear(Text)`, `BaseYearAmount(Currency)`, `CodeBaseYearAmountTypeID`

Note `BaseYear` is typed **`Text`**, not a year or a date. **Observed** — a typing hazard.

### Caps
| Field | Label |
|---|---|
| `CodeCapTypeID` | Cap Type |
| `CapPercentage` | Cap Percentage |
| `CapAmountChangePercent` | Cap Amount Per-Period Change (Percent) |
| `CapAmountChangeValue` | Cap Amount Per-Period Change (Value) |
| `IsRecoveryCapEscalationNonCum` | Is Escalation Non-Cumulative |
| `MaximumValue` / `MinimumValue` | Maximum Value / Minimum Value — the outer clamp |

The cap is not a single number. It is a **growing cap**: a starting amount that escalates each
period by either a percentage or a value, cumulatively or not. That is why `CapAmountChangePercent`,
`CapAmountChangeValue` and `IsRecoveryCapEscalationNonCum` all exist together.
**Derived** from labels.

### Escrow / estimated payments and true-up
| Field | Label |
|---|---|
| `CurrentEscrowPayment` | Current Escrow Payment |
| `NewEscalationPayment` | New Escalation Payment |
| `ProposedEscalationPayment` (computed) | Proposed Escalation Payment |
| `EscalationPercentage` | Escalation Percentage |
| `EscalationAmountIncrease` (computed) | Escalation Amount Increase |
| `CodeEscalationPaymentMethodID` | Escalation Payment Method |
| `CatchUpNumberOfMonths` | Catch Up Number of Months |
| `CatchUpPaymentAmount` | Catch Up Payment Amount |
| `ProposedCatchUpPaymentAmount` (computed) | Proposed Catch Up Payment Amount |

This is the escrow true-up cycle: the tenant pays a monthly estimate, the landlord reconciles, a
new estimate is proposed, and the shortfall is caught up over N months. The `UPDATE_ESCROW` command
on `Contract` drives it. **Derived.**

### Periodicity
`RecoveryPeriod(Text)`, `NumDaysInRecoveryPeriod` (computed date math),
`RecoveryPeriodDaysNoZeroDef`, `CodePaymentFrequencyID`, `CodeReconciliationFrequencyID`

### Reconciliation lifecycle
`CodeApprovalStatusID` (`sCODE_APPROVAL_STATUS_EXPRECOVERY` — a **dedicated** approval status list
for expense recovery), `DateReceived`, `ReconciledFlag`, `ReconciledDate`, `TenantDueDate`,
`TenantSavingsAmount`

### Exclusions
`RecoveryExclusions(Textarea)` — **free text**. There is no structured exclusion model for expense
recovery, in stark contrast to `SalesExclusion`/`SalesExclusionCap` on the percentage-rent side.
**Observed.** This is a genuine gap in the Lucernex model and ASG Edge+ should not copy it.

### Firm-scope (ASG tenant) additions — 9 fields
`Firm_ExpenseRecoveryStatus`, `Firm_ExpenseRecoveryReviewer`, `Firm_ExpenseRecoveryDueDateProcessed`,
`Firm_ExpenseRecoverySalesTax`, `Firm_ExpenseRecoverySavings`, `Firm_ProRataShare`,
`Firm_ProRataShareAmountPaid`, `Firm_ExpenseRecoveryProRataShareSubtotal` (computed),
`Firm_ExpenseRecoveryProRataShareTotalDue` (computed)

The tenant added its own reviewer, status, savings tracking and a **parallel pro-rata-share
computation**. The last one is telling: the tenant did not trust or could not configure the
platform's pro-rata share, so it built a second one in custom fields. **Observed.**

---

## 2. The Statement Audit grid, decoded

`docs/data-fields/expense-recovery.md` groups the 502 grid fields into **26 sub-groups**, all named
`Contract / Statement Audit - …`. Reading the sub-group names gives the grid's axes directly.
**Observed.**

### Axis 1 — the 9 valuation perspectives

| Perspective | Sub-groups | Fields | What it is |
|---|---|---:|---|
| `Reported` | `Reported (Gross)`, `Reported (Net)`, `Reported (Gross/Net)` | 35 | What the **landlord's statement says** |
| `Approved` | `Approved (Gross)`, `(Net)`, `(Gross/Net)` | 35 | What the **tenant agreed to after audit** |
| `Budgeted` | `Budgeted (Gross)`, `(Net)`, `(Gross/Net)` | 30 | What was **estimated/escrowed** |
| `PriorReported` | `Prior Reported (Gross)`, `(Net)` | 38 | Last year's reported |
| `PriorApproved` | `Prior Approved (Gross)`, `(Net)` | 38 | Last year's approved |
| `PriorBudgeted` | `Prior Budgeted (Gross)`, `(Net)` | 38 | Last year's budgeted |

### Axis 1b — the 6 variance families

| Prefix | Sub-group | Fields | Comparison | Has `%` sibling? |
|---|---|---:|---|---|
| `RAVariance` | `Reported-Approved Variance (Gross/Net)` | 36 | Reported − Approved | **No** |
| `ABVariance` | `Approved-Budgeted Variance (Gross/Net)` | 36 | Approved − Budgeted | **No** |
| `RPVariance` + `RPVariancePct` | `Reported-Prior Variance (…)` + ` % (…)` | 72 | Reported − Prior Reported | Yes |
| `APVariance` + `APVariancePct` | `Approved-Prior Variance (…)` + ` % (…)` | 72 | Approved − Prior Approved | Yes |
| `BPVariance` + `BPVariancePct` | `Budgeted-Prior Variance (…)` + ` % (…)` | 72 | Budgeted − Prior Budgeted | Yes |

**The asymmetry is real and worth noting:** the three *year-over-year* comparisons carry percentage
variances; the two *within-year* comparisons (`R−A`, `A−B`) carry only absolute variances at the
header level. At the **line-item** level, `ExpenseRecoveryItem` carries **both** Amount and Percent
for all five (`RAVarianceAmount`/`RAVariancePercent`, `ABVariance…`, `RPVariance…`, `APVariance…`,
`BPVariance…`). **Observed.** Reading: percentage swing year-over-year is the audit trigger;
percentage swing against the landlord's own claim is only meaningful per line item. **Inferred.**

### Axis 2 — the ~19 measures

| Measure | Gross/Net split? | Role in the waterfall |
|---|---|---|
| `ControllableExpenses` | Yes | Input |
| `NonControllableExpenses` | Yes | Input |
| `Deductions` | Yes | Input |
| `SubTotal1` | Yes | **Computed** — step 1 |
| `AdminFeePercentage` | Gross/Net (single on current-year) | Input rate |
| `AdminFeePercentageAmount` | Yes | **Computed** — the rate applied |
| `AdministrationFees` | Yes | Input — a flat admin fee |
| `Additions` | Yes | Input |
| `PassThrough` | Yes | **Computed** — step 2 |
| `Recoveries` | Yes | Input — amounts recovered from others |
| `SubTotal2` | Yes | **Computed** — step 3 |
| `ProRataShareRate` | Gross/Net (single on current-year) | Input rate |
| `NetPassThrough` | Yes | **Computed** — step 4 |
| `NetPassThroughCOREFirmOnly` | Yes | A duplicate of `NetPassThrough`, label *"Duplicate"* — present on Reported/Approved/Prior only |
| `PrePaidAmount` | Gross/Net (single on current-year) | Input — escrow already paid |
| `NetAmountDue` | Yes | **Computed** — step 5 |
| `AdjustmentAmount` | Single | Manual adjustment (Reported/Approved only) |
| `RevisedNetAmountDue` | Yes | **Computed** — step 6 (Reported/Approved only) |
| `CapAmount` | Gross/Net (single on current-year) | The cap |
| `RentableArea` | Gross/Net (single on current-year) | Share numerator |
| `GLA` | Gross/Net (single on current-year) | Gross Leasable Area — share denominator |

The `(Gross/Net)` sub-groups hold the measures that have **no** gross/net split on the current-year
perspectives (7 for Reported, 7 for Approved, 6 for Budgeted): `AdjustmentAmount`,
`AdminFeePercentage`, `CapAmountNoZeroDef`, `GLA`, `PrePaidAmount`, `ProRataShareRate`,
`RentableArea`. The `Prior` perspectives split even these — `PriorReportedGLAGross` /
`PriorReportedGLANet` both exist — which is why `Prior*` has 38 fields against Reported's 35.
**Observed.**

### Axis 3 — Gross vs Net

Every measure exists twice: `…Gross` and `…Net`. The meaning is **Inferred**: `Gross` is the
landlord's total before contractual exclusions, `Net` after. The presence of both on every measure —
including `GLA` and `RentableArea` — is consistent with the "gross-up" concept, where an
under-occupied building's variable expenses are grossed up to a notional occupancy (see
`GrossupRate` and `OccupancyAdjustedThreshold` in §1). **This reading is not confirmed** and is
open question 1.

### The `NoZeroDef` suffix

29 grid fields end in `NoZeroDef` (e.g. `ApprovedCapAmountNoZeroDef`,
`PriorReportedNetAmountDueGrossNoZeroDef`, `RecoveryPeriodDaysNoZeroDef`). Reading: *"no zero
default"* — a variant of the field that returns null/blank rather than `0` when unset, so that a
genuine zero is distinguishable from an unentered value. **Inferred** from the name; the pattern
appears only on measures that participate in variance arithmetic, which supports the reading (a
`0` default would produce a spurious 100% variance). **For ASG Edge+ this is a strong argument for
nullable `BigDecimal` rather than a zero default on every recovery measure.**

---

## 3. The CAM waterfall — recovered exactly from the field labels

This is the highest-value single finding in the module. Lucernex put the formula in the UI label of
every computed field. **Observed**, `docs/data-fields/expense-recovery.md`.

| Label as it appears in Lucernex | Internal name |
|---|---|
| `Reported Sub Total #1 (C+NC-D)` | `ReportedSubTotal1Gross` / `…Net` |
| `Reported Pass-Through (ST1+AF%+AF+A)` | `ReportedPassThroughGross` / `…Net` |
| `Reported Sub Total #2 (PT-R)` | `ReportedSubTotal2Gross` / `…Net` |
| `Reported Net Pass-Through (ST2*PRR)` | `ReportedNetPassThroughGross` / `…Net` |
| `Reported Net Amount Due (NPT-PP)` | `ReportedNetAmountDueGross` / `…Net` |
| `Reported Revised Amount Due (Net+Adj)` | `ReportedRevisedNetAmountDueGross` / `…Net` |

The identical labels appear on the `Approved`, `Budgeted`, `Prior*` and all six variance
perspectives — 9 perspectives running the identical six-step waterfall.

### The waterfall, expanded

```
── inputs ───────────────────────────────────────────────────────────────
  C    = ControllableExpenses            (landlord's controllable operating costs)
  NC   = NonControllableExpenses         (taxes, insurance, utilities — uncapped)
  D    = Deductions                      (contractually excluded costs)
  AF%  = AdminFeePercentage              (rate)
  AF   = AdministrationFees              (flat fee)
  A    = Additions
  R    = Recoveries                      (amounts recovered from other tenants/sources)
  PRR  = ProRataShareRate                (this tenant's share)
  PP   = PrePaidAmount                   (escrow already paid)
  Adj  = AdjustmentAmount                (manual)

── step 1 ── the recoverable pool
  ST1  = C + NC − D                                            [CON-R-080]

── step 2 ── add the landlord's fees
  AF%amt = ST1 × AF%          → AdminFeePercentageAmount       [CON-R-081]
  PT     = ST1 + AF%amt + AF + A                               [CON-R-082]

── step 3 ── net off what was recovered elsewhere
  ST2  = PT − R                                                [CON-R-083]

── step 4 ── this tenant's share
  NPT  = ST2 × PRR                                             [CON-R-084]

── step 5 ── credit the escrow
  NAD  = NPT − PP                                              [CON-R-085]

── step 6 ── manual adjustment
  RNAD = NAD + Adj                                             [CON-R-086]
```

**Confidence:** steps 1, 3, 4, 5, 6 are **Observed** — the formula is literally in the label. Step 2
is **Observed** for the composition (`ST1+AF%+AF+A`) and **Derived** for `AF%amt = ST1 × AF%` (the
label `Admin Fee Percentage Amount` next to a rate field `Admin Fee Percentage` in a formula that
adds `AF%` as an amount leaves no other reading).

### Where the cap enters

The waterfall as labelled does **not** show the cap. `CapAmount` sits alongside as a separate
measure per perspective, and §1's cap configuration (`CodeCapTypeID`, `CapPercentage`,
`CapAmountChangePercent/Value`, `IsRecoveryCapEscalationNonCum`, `MaximumValue`/`MinimumValue`)
defines how it grows. **Where in the waterfall the clamp is applied is not observable from the
field names** — it could clamp `C` (controllable only, the common lease formulation), `ST1`, or
`NAD`. This is open question 2 and it materially changes the arithmetic. The strong prior is
**controllables only** — that is why `ControllableExpenses` and `NonControllableExpenses` are
separate measures at all. **Inferred, unconfirmed.**

### Base year

Similarly, `BaseYear` / `BaseYearAmount` / `CodeBaseYearAmountTypeID` do not appear in the labelled
waterfall. A base-year "stop" normally subtracts the base-year expense level before the share is
applied. Most likely it modifies `ST1` or `ST2`. **Inferred, unconfirmed** — open question 3.

---

## 4. `ExpenseRecoveryItem` — the line-item layer

47 fields. One row per recovery **line item** (a single expense category on the landlord's
statement). Its shape mirrors the header grid but at a much lower cardinality — because the header
grid has to be a fixed set of columns, while items are rows.

| Group | Fields |
|---|---|
| Identity | `ExpenseRecoveryItemID`, `ExpenseRecoveryID` *(typed `Text` — weak FK)*, `ContractID`, `ProjectEntityID`, `BOMapClientRecordID`, `RevNumber`, `CreatedBy/Date`, `ModifiedBy/Date`, `Notes` |
| Classification | `CodeRecoveryItemGroupID`, `CodeRecoveryItemTypeID`, `CodeRecoverySectionID`, `CodeApprovalStatusID` |
| Reported | `ReportedAmount`, `ReportedAmountGross`, `ReportedAmountNet`, `ReportedProRataShareRate` |
| Approved | `ApprovedAmount`, `ApprovedProRataShareRate`, `ApprovedAdminFeeAmtNoZeroDef`, `ApprovedAdminFeePrcntNoZeroDef`, `ApprovedCapAmountNoZeroDef`, `ApprovedCapPercentNoZeroDef` |
| Budgeted | `BudgetedAmount`, `BudgetedAmountGross`, `BudgetedAmountNet`, `BudgetedProRataShareRate` |
| Prior | `PriorApprovedAmountNoZeroDef`, `PriorBudgetedAmountNoZeroDef`, `PriorReportedAmountNoZeroDef` |
| Computed | `ComputedApprovedAdminFeeNoZeroDef`, `ComputedApprovedCapNoZeroDef`, `ComputedApprovedTotalAmount`, `ComputedApprovedTotalAmountGross`, `ComputedApprovedTotalAmountNet` |
| Variances (all 5, Amount **and** Percent) | `RAVariance…`, `ABVariance…`, `RPVariance…`, `APVariance…`, `BPVariance…` |

`ComputedApprovedTotalAmount` = the item's approved amount after its own admin fee and cap are
applied — i.e. **the cap and admin fee also exist per line item**, not just at the header. That is
the correct place for them (leases cap specific categories), and it strengthens the "cap applies to
controllables" reading. **Observed** field names; **Derived** interpretation.

### `ExpenseRecoveryItemMapping` (6 fields)

`ContractID`, `ProjectEntityID`, `ExpenseRecoveryItemID(Text)`, `DocumentID(Document ID)`,
`InvoiceLineItemName(Text)`, `JSONConfigText(Text)`.

Maps a free-text line description on a scanned landlord statement to a structured recovery item,
with an extraction config blob. **Inferred** purpose. This is the document-ingestion bridge for
CAM statements and is a genuinely useful pattern for ASG Edge+.

---

## 5. What the ASG tenant added on top: 91 Firm fields on `Contract`

Two `Contract` sub-groups are **100% Firm scope** — every field is a tenant custom field, not
platform functionality. **Observed** from `docs/data-fields/contract.md`.

| Sub-group | Fields | Scope |
|---|---:|---|
| `Contract / Common Area Maintenance` | 47 | **100% Firm** |
| `Contract / Real Estate Taxes` | 44 | **100% Firm** |

These are the **lease abstract**, not the engine. Sample of the CAM family:

```
Firm_CAMAdministrativeYN / …FeePercent / …FeeDefinition / …FeeExclusionsYN
Firm_CAMLeaseTermCapYN / …CapPercent / …CapType / …CapExclusions / …CapTextReference / …CapComment
Firm_CAMStartingCapYN / …CapAmountPSF / …CapMonthly / …CapStatus / …CapExclusionsYN / …CapTextReference
Firm_CAMFixedYN / …FixedIncreasePercent / …FixedStatus / …FixedText / …FixedComment
Firm_CAMFloorPercent, Firm_CAMInitialFixedMO, Firm_CAMInitialFixedPSF
Firm_CAMDateofFirstIncrease, Firm_CAMMonthofIncrease
Firm_CAMExclusionsYN / …ExclusionsReference
Firm_CAMNoDuplicationofCostsLanguageYN / …Reference
Firm_CAMAuditRightsYN / …Reference, Firm_CAMNumberofYearsAuditable
Firm_CAMStatementsDue / …DueReference, Firm_CAMStatementsBindingLanguageYN / …Reference
Firm_CAMContributionsYN / …Reference, Firm_CAMPRShare / …Status
Firm_CAMDocument / Firm_CAMPage / Firm_CAMSection / Firm_CAMNotes / Firm_CAMComment
```

and the RE-tax family: `Firm_RETAdministrativeFeePercent`, `Firm_RETFloorPercent`,
`Firm_RETLeaseTermCapPercent`, `Firm_RETStartingCapAmount`, `Firm_RETInitialEstimateMonthly`,
`Firm_RETLandlordtoProvideTaxBillsYN`, `Firm_RETTaxesFor`, `Firm_TaxLink1/2`, `Firm_TaxWebsite1/2`.

**The pattern is unmistakable and it is the key insight for ASG Edge+.** Every field comes in a
`…YN` (does the lease contain this provision?) + a value + a `…Reference`/`…TextReference`/
`Document`/`Page`/`Section` (where in the lease does it say so?) + a `…Comment`/`…Status`. That is
a **lease-abstract schema**, distinct from the recovery **engine** schema. The tenant built it in
custom fields because the platform has no first-class place for "what the lease says about CAM" as
opposed to "what we're going to compute".

ASG Edge+ should model these as **two separate things**: an *abstracted clause* (provision present?
where? what does it say? who verified it?) and a *computation configuration* derived from it. That
is exactly what BRD-24's PJ-04 (initial financial abstraction) → PJ-06 (deep contract abstraction)
split already implies (`docs/contracts-explained.html`).

---

## 6. Reconciliation against payments

There is no `ExpenseRecoverySchedule`. The recovery header is settled through the payment layer:

```
ExpenseRecovery ──(ExpenseRecoveryID, typed Text)──▶ PaymentTransaction
LandlordInvoice ──▶ LandlordInvoiceItem ──┐
                                          ├── LinkLandlordInvPaymentTxn ──▶ PaymentTransaction
                                          │      AllocationAmount, AllocationDate,
                                          │      VarianceAmount, VarianceReason,
                                          │      ReconciliationStatus
```

The `RECONCILE` command on `Contract` drives it; `ReconciledFlag` / `ReconciledDate` /
`TenantDueDate` / `TenantSavingsAmount` on `ExpenseRecovery` record the outcome.
`TenantSavingsAmount` — what the audit saved the tenant — is the business KPI of the whole module,
and the ASG tenant added `Firm_ExpenseRecoverySavings` and a `Firm_SavingsLog(Custom List)` on
`Contract` alongside it. **Observed.**

See [`payment-lifecycle.md`](payment-lifecycle.md) for the full three-way match.

---

## 7. What the 565 fields actually cover — the enumeration

Answering the brief's question directly:

| Concept | Covered? | Where |
|---|---|---|
| **Pro-rata shares** | Yes | `CodeProRataShareMethodID`, `{Reported,Approved,Budgeted}ProRataShareRate`, `…RentableArea`, `…GLA` |
| **Caps** | Yes, as a *growing* cap | `CodeCapTypeID`, `CapPercentage`, `CapAmountChangePercent/Value`, `IsRecoveryCapEscalationNonCum`, `{persp}CapAmount…`, plus per-item `ApprovedCapAmountNoZeroDef`/`ApprovedCapPercentNoZeroDef` |
| **Floors** | Partially | `MinimumValue` / `MaximumValue` at the header; `Firm_CAMFloorPercent` / `Firm_RETFloorPercent` in the abstract. No per-perspective floor measure. |
| **Gross-ups** | Yes | `GrossupRate`, `OccupancyAdjustedThreshold` (Occupancy Factor, computed), and the Gross/Net axis across the whole grid |
| **Admin fees** | Yes, two kinds | `AdminFeePercentage` (rate) + `AdminFeePercentageAmount` (computed) **and** `AdministrationFees` (flat), per perspective and per item |
| **Exclusions** | **Weakly** — free text only | `RecoveryExclusions(Textarea)`. Structured exclusions exist only in the ASG tenant's `Firm_CAM*ExclusionsYN`/`…Reference` abstract fields. **This is the model's biggest gap.** |
| **Base years** | Yes | `BaseYear(Text)`, `BaseYearAmount`, `CodeBaseYearAmountTypeID` |
| **Escrow / estimates / true-up** | Yes | `CurrentEscrowPayment`, `New/Proposed EscalationPayment`, `EscalationPercentage`, `CatchUp*`, `PrePaidAmount` measure, `UPDATE_ESCROW` command |
| **Audit / statement reconciliation** | Yes — this *is* the 502-cell grid | The 26 `Statement Audit - …` sub-groups |
| **Controllable vs non-controllable split** | Yes | `ControllableExpenses` / `NonControllableExpenses` measures |
| **Prior-year comparison** | Yes | Three `Prior*` perspectives + three `*PVariance` families with `%` |
| **Line-item detail** | Yes | `ExpenseRecoveryItem` (47) |
| **Statement document ingestion** | Yes | `ExpenseRecoveryItemMapping`, `DocumentIDList`, `IMPORT_INVOICE` |
| **Approval workflow** | Yes | `CodeApprovalStatusID` (`sCODE_APPROVAL_STATUS_EXPRECOVERY`), `Firm_ExpenseRecoveryReviewer`, `Firm_ExpenseRecoveryStatus` |
| **Vendor allocation** | Yes, but on the expense side | `ExpenseVendorAllocation` (16) — `PaymentPercentage` per `VendorID` per `ExpenseSetupID` |
| **Multi-org allocation** | Yes | `ExpenseAllocation` (15) — `AllocationPercentage` per `OrganizationID` per `ExpenseSetupID` |
| **Sales-tax on recovery** | Firm only | `Firm_ExpenseRecoverySalesTax` |
| **Cap-ex amortisation in CAM** | **No** | No field for amortising a capital replacement across the recovery period |
| **Anchor/major-tenant deductions** | **No structured model** | Only `Deductions` as a lump measure and `Recoveries` as an offset |

---

## Open questions

Ranked by impact on the frozen schema.

1. **What exactly distinguishes `Gross` from `Net` on every measure?** Gross-up basis, pre/post
   exclusions, or something else? Nothing in the corpus names it. Open a recovery record in the UI
   with both populated and read the on-screen section headers.
2. **Where in the waterfall is the cap applied — to `C`, to `ST1`, or to `NAD`?** The labels stop
   short of showing it. Enter a recovery with a cap below `ST1` and read which computed field
   changes. *This changes every capped CAM number.*
3. **Where does `BaseYearAmount` enter the waterfall?** Same test: set a base-year amount and see
   which computed measure moves.
4. **What are the members of `Dropdown (Recovery Type Code)`, `(Calculation Method)`,
   `(Exp Rec Based On)`, `(Pro Rata Share Method)`, `(Cap Type)`, `(Base Year Amount Type)`?**
   Six code lists whose members define the model's variant space. All readable from
   `FirmCodeList.jsp` (screen 007).
5. **Why does `NetPassThroughCOREFirmOnly` exist, labelled *"Duplicate"*?** It appears on
   Reported/Approved/Prior but not Budgeted, and not in any variance family. A legacy or
   firm-specific parallel calculation.
6. **Is `NoZeroDef` really "no zero default"?** Confirm by leaving a measure blank and checking
   whether the variance renders blank or as a 100% swing.
7. **Does `ExpenseRecovery` have a *per-period* row, or one row per contract per recovery
   category?** `BeginDate`/`EndDate` + `RecoveryPeriod(Text)` + the `Prior*` perspectives suggest
   one row per recovery **period**, with `Prior*` denormalised from the previous row. Confirm by
   listing recovery records for a multi-year contract. **This determines whether ASG Edge+ needs a
   period key on the recovery entity.**
8. **How are the four `expense_recovery_part1..4` tables keyed and joined?** They share
   `ExpenseRecoveryID` (which appears four times in the field export), but whether all four rows
   are always created is unknown.
