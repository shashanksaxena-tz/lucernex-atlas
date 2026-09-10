# What actually keys a Contract

**Stated up front.** A Lucernex `Contract` is keyed by **four outward FKs and one self-reference**:
`FacilityID` (the building), `LocationID` (the site), `OrganizationID` (the org whose accounts are
debited), `ProgramID` (the portfolio — note the name/label mismatch), and `MasterContractID`
pointing at another `Contract`. It has **no Vendor FK at all** — that relationship lives one level
down on `PaymentTransaction`. It also carries `ComplexID` and `PrototypeID`.

Three structural facts dominate everything else:

1. **`MasterContractID` is the master-lease/sublease hierarchy**, and it is a plain self-referencing
   FK typed `Contract ID` with no depth constraint, no role discriminator, and no cycle guard.
2. **570 fields across 4 physical tables, 258 of them (45%) tenant custom fields.** `Contract` is
   `contract_admin` + `contract_financial` + `contract_firm` + `contract_firm1`. The Global platform
   schema is ~312 fields; the ASG tenant added 258 more.
3. **`Contract Status Code` holds only three values** — `AI Abstracted`, `Active`, `Inactive` — and
   none of them is a BRD-24 lifecycle stage. Contract status is a **record-state enum**; the
   lifecycle BRD-24 describes is a **real state machine implemented on a different axis entirely**.
   Full answer in [§7](#7-contract-status-vs-the-brd-24-lifecycle--the-answer). *(Live capture,
   2026-09-10.)*

All FK columns and types **Observed** from `_lucernex_objects_summary.txt`, corroborated
independently by [`../../admin/009-related-fields-and-data-model.md`](../../admin/009-related-fields-and-data-model.md)
reading the same rows out of `ShowObjectDetails.jsp`.

---

## 1. The FK columns

| Column | Declared type | UI label | Lucernex's own definition (from 009) |
|---|---|---|---|
| `FacilityID` | `Facility ID` | Facility | *"Select the facility that your entity will be associated with from this field."* |
| `LocationID` | `Location ID` | Location | *"Select the location that your entity will be associated with from this field."* |
| `OrganizationID` | `Organization ID` | Organization | *"Select the organization where payments should be debited from this field."* |
| `MasterContractID` | **`Contract ID`** | Master Contract | *"The Master Contract ID is the contract ID of the master lease in a master lease-sub-lease relationship…"* |
| `ProgramID` | `Portfolio ID` | **Portfolio** | Internal name says Program, label says Portfolio — a naming-legacy mismatch, same relationship |
| `ComplexID` | `Complex ID` | Complex | Shopping-centre / multi-building grouping |
| `PrototypeID` | `Prototype ID` | Prototype | Store prototype |
| `NextAvailableTermID` | `Contract Term ID` | Next Available Term | Points at **this** contract's own next `ContractTerm` — not the master's |
| `BudgetTemplateID` | `Template ID` | | Budget template |
| `RegionID`, `SubRegionID`, `RootRegionID` | `Region ID` | | Three-level region hierarchy |
| `JurisdictionID` | `County ID` | | Tax jurisdiction |
| `IStateProvinceCountryID` | `Country, State, County ID` | | Geography |
| `DemographicDMAID` | `DMA ID` | | Media market |
| `CreatedByID`, `ModifiedByID`, `Firm_LeaseAnalyst` | `Member ID` | | People |

The lease-accounting fields `Contract.DiscountRate(Percentage)` and
`Contract.ComputedSLDiscountRate(Percentage)` are values, not FKs — the `DiscountRate` **object**
(16 fields) is looked up by `CodeAccountingMethodID` + `CodeContractUseID` + geography +
`MinSchedMons`/`MaxSchedMons` term band, and its result is stamped onto the contract. **Derived.**

---

## 2. There is no Vendor FK — and that is deliberate

[009](../../admin/009-related-fields-and-data-model.md) establishes this at the schema level:
`PaymentTransaction.VendorID` has declared type **`Employer ID`**, not a distinct "Vendor" type.
"Vendor" is a relabelled `Employer`. And `Contract` carries no `EmployerID`, no `VendorID`, nothing.

Where vendor relationships actually live:

| Object | Vendor column | Meaning |
|---|---|---|
| `PaymentTransaction.VendorID` | `Employer ID` | Who this payment goes to |
| `ExpenseSetup.VendorID` | `Employer ID` | The default payee for a recurring clause |
| `ExpenseVendorAllocation.VendorID` + `PaymentPercentage` + `APVendorNumber` | `Employer ID` | Split one clause's payments across several vendors by percentage |
| `ScheduledOffset.VendorID` | `Employer ID` | Who owes the offset credit |
| `LandlordInvoice.EmployerID` | `Employer ID` | Who sent the invoice |
| `SecurityDeposit.PartyID` | `Employer ID` | Who holds the deposit |

**Consequence for ASG Edge+:** a contract's vendor set is a *derived* set, not a stored one, and it
can change per expense clause and per payment. BRD-24's PJ-12 ("Vendor record setup — create or
link a vendor") therefore has to decide whether ASG Edge+ stores a contract-level primary vendor
that Lucernex does not have. If it does, it is a **deliberate divergence** and should be recorded as
one. See [`asg-edgeplus-mapping.md`](asg-edgeplus-mapping.md).

The Manage Data Fields catalog types the same column `sTYPE_VENDOR` while View Object Model types
it `Employer ID` — presentation type vs storage type, exactly as 009 documents. **Observed in both
sources.**

---

## 3. The master-lease / sublease hierarchy

### What the schema says

```
Contract.MasterContractID  →  Contract      (type: Contract ID)
```

That is the entire mechanism. **Observed.** What it does **not** carry:

| Missing | Consequence |
|---|---|
| No role discriminator (`IsSublease`, `IsMasterLease`) | Master vs sub is inferred purely from whether `MasterContractID` is null |
| No depth limit or cycle guard | A→B→C→A is representable |
| No allocation percentage | How much of the master's cost this sublease bears is not on the edge |
| No sublease direction flag | Whether we are subletting **out** (receivable) or subleasing **in** (payable) is not on the contract |

Direction is instead carried per-clause on `ExpenseSetup.IsReceivable(Boolean)` and per-transaction
on `PaymentTransaction.IsReceivable(Boolean)`. So one contract can be simultaneously payable (rent
to the landlord) and receivable (rent from the subtenant) — which is correct for a real sublease,
and is a strong argument that ASG Edge+ should carry direction on the **money**, not on the
contract. **Derived.**

### What Related Fields exposes across the edge

Per [009](../../admin/009-related-fields-and-data-model.md), the Page Layout builder's
**Related Fields → Contract (self)** node exposes only **four fields across two subgroups**:

| Subgroup | Fields |
|---|---|
| Accounting Assumptions | `Contract Discount Rate` |
| Contract Term | `Next Available Term`, `Next Available Term Key Date`, `Remaining Number of Term` |

versus Facility/Location/Organization, which pass through their **complete** native catalogs.
009 reads the narrowing as a deliberate Page-Layout-builder decision, not a data-model limitation —
`MasterContractID`'s schema type is `Contract ID` like any other FK. **Inference, inherited from
009 and labelled there as moderate confidence.**

Practical reading: the only things a sublease is expected to inherit from its master lease on a
layout are the **discount rate** and the **term structure**. That is a strong hint about what
actually matters in a master-lease relationship, and worth testing in the live UI.

### What is not answered anywhere

- Does financial data roll up from sublease to master? (No aggregate field on `Contract` names a
  master or sublease scope.)
- Does an `ExpenseSetup` on a master lease automatically create allocations to its subleases?
  (`ExpenseAllocation` allocates by `OrganizationID`, not by contract.)
- Is `MasterContractID` used for anything other than layout display?

All three are open questions. Given ADR-0008 freezes the schema at Week 12, **these are the highest-
priority live-UI checks in this document.**

---

## 4. `walkHierarchy.jsp`'s composition tree — what a Contract owns

Per [009](../../admin/009-related-fields-and-data-model.md), Lucernex's own
`walkHierarchy.jsp` → `RE Contract` → `Schema` view renders **~70 tables nested under `'Contract'`
as owned children** — `PaymentTransaction, PaymentReceipt, Covenant, ContractTerm → KeyDate,
ContractAmendment, Sales, SecurityDeposit, Space, Responsibility, WorkFlow, …` — and, critically,
**`Facility`, `Location` and `Organization` do not appear anywhere in that tree.** They are separate
aggregate roots in the tool's own top-level dropdown. **Observed** (in 009).

That draws the line ASG Edge+ needs:

| Relationship kind | Lucernex representation | UI surface | ASG Edge+ implication |
|---|---|---|---|
| **Owned one-to-many child** | Nested under `Contract` in `walkHierarchy` | **List Layouts** (embedded grid) | Same aggregate, same transaction boundary, cascade delete |
| **Referenced many-to-one lookup** | Separate aggregate root | **Related Fields** (joined lookup) | Different aggregate, FK only, no cascade |

`MasterContractID` is the awkward case: it is a **reference** to another instance of the **same**
aggregate root. It is not in the composition tree (a contract does not own its master), and Contract
does appear in its own Related Fields list — so Lucernex treats it as a lookup. **Derived** from
009's evidence.

---

## 5. `Contract`'s physical shape: 570 fields, 4 tables, 45% tenant custom

```
Contract → contract_admin, contract_financial, contract_firm, contract_firm1
```

**Observed** in `_lucernex_objects_summary.txt`.

| Scope | Fields | % |
|---|---:|---:|
| Global (platform) | 312 | 55% |
| Firm (`Firm_*` prefix, tenant custom) | 258 | 45% |

[009](../../admin/009-related-fields-and-data-model.md) reports reading a **307-field** Contract
schema out of `ShowObjectDetails.jsp` with the `Global Fields` radio set. 312 − 307 = 5. The two
numbers agree to within rounding of how computed and button pseudo-fields are counted. **Derived**,
and it is a useful cross-check that both sources describe the same object.

The four-table split is **semantic**, not mechanical (unlike `ExpenseRecovery`'s `part1..4`):
administrative fields, financial fields, and **two** tables of tenant custom fields — implying the
tenant custom surface itself outgrew one table. Whether all four rows always exist for a contract is
an open question.

### The 97 Contract sub-groups, and which are tenant-only

Full table in [`data-model.md` §7](data-model.md#7-the-contract-sub-group-taxonomy-2678-fields-across-97-sub-groups).
The ones that are **100% Firm scope** — i.e. exist only because this tenant built them:

| Sub-group | Fields | What it is |
|---|---:|---|
| `Contract / Common Area Maintenance` | 47 | The **CAM lease abstract** — `Firm_CAM*` |
| `Contract / Real Estate Taxes` | 44 | The **RE-tax lease abstract** — `Firm_RET*` |
| `Contract / Ongoing Co Tenancy` | 13 | `Firm_ONCOT*` |
| `Contract / Opening Co Tenancy` | 9 | `Firm_OPCOT*` |
| `Contract / Delivery Requirements` | 8 | |
| `Contract / Custom Lists` | 5 | `Firm_OperatingExpenses`, `Firm_SavingsLog` |

**121 fields of pure lease abstract, none of it platform functionality.** This is the finding that
should shape ASG Edge+'s contract schema more than any other: the platform models *what to compute*,
and the tenant had to build *what the lease says* on the side. See
[`expense-recovery-cam.md` §5](expense-recovery-cam.md#5-what-the-asg-tenant-added-on-top-91-firm-fields-on-contract).

### The Global rollup surface: 120 denormalised rent fields

`Contract` carries four sub-groups of pre-computed rent rollups, all Global, all
`sTYPE_MONEY`:

| Sub-group | Fields |
|---:|---|
| `Financial - Calendar` | 34 |
| `Financial - Calendar w/ Tax` | 30 |
| `Financial - Fiscal` | 28 |
| `Financial - Fiscal w/ Tax` | 28 |

The shape is a four-dimensional cross-product:

```
{ Aggregate, Current Annual, Current Monthly, Current Period, Next Year,
  Third Year, Fourth Year, Fifth Year, Sixth Year, Beyond Fifth Year,
  Beyond Sixth Year, Remaining Obligation, Q1..Q4 }
×  { Base Rent, Total Rent }
×  { Calendar, Fiscal }
×  { with tax, without tax }
```

e.g. `CurrentFiscalYearQ3TotalRentWithTax`, `BeyondSixthYearBaseRent`,
`RemainingFiscalObligationTotalRentWithTax`, `AggregateNNNBaseRentNPV`. **Observed.**

These are **denormalised rollups of `ExpenseSchedule`** kept on the contract row so a portfolio list
can sort and filter by them without aggregating. `AggregateNNNBaseRentNPV(Currency)` and
`ComputedSLDiscountRate` show even NPV is precomputed. `Contract.CurrentStraightLineAssetBalance`
and `.CurrentStraightLineLiabilityBalance` do the same for the ASC 842 balances.

**ASG Edge+ should not copy this.** 120 denormalised money columns on the aggregate root is a
staleness and recomputation-cost problem, and the `NeedsRecalculation` / `RecalcTriggerDate` /
`NeedsRecalcModifiedByMemberIDList` machinery on `SLSummary` shows Lucernex already has to manage
exactly that. A materialised projection with an explicit refresh is the right shape. **Judgement,
not observation.**

### `Firm_` custom fields that are computed

Three tenant custom fields are typed `sTYPE_MONEY_MATH_OPERATION`:
`ExpenseSetup.Firm_TotalCurrentMonthlyRent`,
`ExpenseRecovery.Firm_ExpenseRecoveryProRataShareSubtotal`,
`ExpenseRecovery.Firm_ExpenseRecoveryProRataShareTotalDue`.

So the tenant custom-field system supports **user-defined computed fields**, not just data entry.
That is a significant platform capability with direct bearing on the ASG Edge+ Data Fields design,
and it is documented in the layouts-and-forms module's territory rather than here. **Observed.**

---

## 6. Contract-level financial classification

| Field | Type | Role |
|---|---|---|
| `CodeContractTypeID` / `CodeContractGroupID` / `CodeContractCategoryID` / `CodeContractUseID` | `Dropdown` | The four-way classification |
| `CodeAgreementTypeID` | `Dropdown (Agreement Type Code)` | Lease / sublease / licence / easement etc. — **the most likely home of a sublease role discriminator** |
| `CodeHoldingInterestID` | `Dropdown (Holding Interest Code)` | Owned / leased / managed |
| `CodeDealTypeID` | `Dropdown (Deal Type Code)` | |
| `CodeAssetClassID` | `Dropdown (Asset Class Code)` | |
| `CodeContractStatusID` + `StatusEffectiveDate` | `Dropdown` + `Date` | Lifecycle status |
| `CodeProrationMethodID` | `Dropdown (Proration Method Code)` | Default proration for the whole contract |
| `CodeBuildingAreaUnitID` | `Dropdown (Building Area Unit Code)` | sq ft / sq m |
| `CodeCurrencyTypeID` | `Dropdown (Currency Type Code)` | Contract currency |
| `ContractTaxRate1..4` | `Percentage` | Four contract-level tax rates, applied per `ExpenseSetup.ApplyTax1..4Flag` |
| `RentableArea`, `UsableArea`, `GrossArea`, `LeasedLandArea`, `ProjectLandArea`, `Frontage`, `Depth` | `Number` / `Acreage` | The area basis for PSF rents and pro-rata shares |
| `ProRataShareRate` | `Percentage` | The contract-level default share |
| `PaymentRate` | `Percentage` | |
| `TermLength`, `RemainingNumberOfTerms`, `RemainingLife` | `Number` | Term arithmetic |
| `IsShortTerm`, `MonthToMonth`, `Inactive`, `IsDead`, `IsTranslation`, `IsLowAssetValue` | `Boolean` | |
| `InAlternateRent` | `Boolean` | Currently under an alternate-rent regime |

**`CodeAgreementTypeID` is the field to check first** when looking for the master/sublease role
discriminator that `MasterContractID` lacks.

### The date axes

```
OriginalStartDate / OriginalEndDate       — as originally executed
BaselineStartDate / BaselineEndDate       — the baseline for variance
ActualStartDate / ActualEndDate           — as actually happened
ExpectedEndDate, ExpireDate               — projected end
CommenceDate, ExecuteDate, ObligationDate — legal milestones
PossessionBeginDate / PossessionEndDate   — possession
PaymentsBeginDate / PaymentsEndDate       — the paying window
SlotEndDate, LastLikelyOptionDate, DaysToExpiration
```

Eleven date pairs. `PaymentsBeginDate`/`PaymentsEndDate` being separate from
`CommenceDate`/`ExpireDate` is what makes rent-free periods and post-expiry holdover representable.
**Observed.** This maps directly onto BRD-24's PJ-10/PJ-11 (store opens; critical dates
recalibrated) and FR-010's status lifecycle *Open → Active → Possession → Paying Rent → Closed*.

### The ASC 842 classification test fields (accounting module territory)

`Contract / Cap Lease Test` (28 Global fields) holds the lease-classification inputs:
`FMVOfBuilding`, `FMVOfLand`, `FMVSource`, `FairValueThreshold`, `RemainingEconomicLifeThreshold`,
`RemainingLife`, `RatioLeaseAutoRenewToFMV`, `RatioLeaseBargainRenewToFMV`,
`RatioTermAutoRenewToLife`, `RatioTermBargainRenewToLife`, `AutomaticRenewalOption`,
`AutomaticRenewalInLease`, `BargainRenewalOption`, `BargainRenewalInLease`,
`ContainsBargainPurchaseOption`, `DoesTitleRevertToTenant`, `IsLowAssetValue`,
`Test1Result`…`Test5bResult`, `LatestFinancialTestFinalResult`, `FinalResult`, `FinancialModel`.

Five numbered tests with a `5a`/`5b` split — the ASC 842 / IFRS 16 classification criteria. Results
are stored as **`Text`**, not as an enum. Detail belongs to the **accounting** module; noted here
because the fields live on `Contract` and are therefore inside the Week-12 freeze.

---

## 7. Contract status vs the BRD-24 lifecycle — **the answer**

**Stated up front.** Lucernex carries **two status fields on a contract, side by side, both
required**, and they are different concepts:

| Field | Scope | Values | What it is |
|---|---|---|---|
| `CodeContractStatusID` | **Global** (platform) | **3** — `AI Abstracted`, `Active`, `Inactive` | A coarse **record state**: is this row live, retired, or machine-abstracted |
| `Firm_LeaseStatus` | **Firm** (tenant Client Drop Down) | **9** — Open, Future Possession, Possession, Possession - Paying Rent, Active, Closed - Active, Closed, Accounting Purposes Only, Accounting Purposes Only: Close… | The **operational lifecycle**. This is BRD-24's state machine, expanded from five states to nine |

So the answer to "3-value enum or real state machine?" is **both, on two axes that must not be
merged** — and the state machine is **real, stored, and already in production**, just not where the
schema freeze would naturally look for it. Critically, it is **tenant data, not platform schema**:
nine states a rebuild would model as an enum are rows in a customer-editable drop-down.

Both status fields are **Observed**. The 3-value platform table and the 9-value tenant drop-down were
captured live on 2026-09-10 — see
[`../../data-model/code-table-registry.md`](../../data-model/code-table-registry.md#the-contract-lifecycle--resolved),
which also records that the `ASG Contract Summary` layout (`PageLayoutID=96289`) marks **both**
fields required. This section adds what the schema shows underneath.

### What the field inventory adds

Four things the live capture does not show, all **Observed** in `_lucernex_objects_summary.txt` and
`docs/data-fields/contract.md`.

**1. `Firm_LeaseStatus` is a `Contract` column, and it has a notes companion.**

```
Contract.Firm_LeaseStatus       sTYPE_CUSTOM_CODE_FIELD   Firm scope   Contract / Contract Info
Contract.Firm_LeaseStatusNotes  sTYPE_TEXT                Firm scope   Contract / Contract Info
```

It sits in the **same sub-group** as the platform's own `CodeContractStatusID`. A tenant does not
duplicate a platform field in the same sub-group unless the platform field cannot express what they
need. The `Notes` companion says transitions carry a free-text justification today — which is
FR-029's "who, what, when, why" being done by hand, in a text box.

**2. The platform's own `Lease Status Code` (2043) is a red herring — and the schema says why.**
It is used by **exactly one object in the entire 223-object export: `LeaseInfo`** (219 fields,
`CodeLeaseStatusID` + `LeaseStatusEffectiveDate`). And `LeaseInfo` is keyed by `ProjectEntityID`
with **no `ContractID` column at all**. It is a separate lease-abstract record, not the contract's
status — which is consistent with the live capture finding 2043 holds a single value, `Expired`.
The tenant did not extend the platform table; it built a same-named Client Drop Down beside it.

**3. BRD-24's stage names also exist as date fields on `Contract`.** Every one of them:

| Lease Status value | Corroborating date field(s) on `Contract` | Group |
|---|---|---|
| `Open` | `ActualStartDate`, `OpenYear` | Contract Dates / Contract Info |
| `Future Possession` → `Possession` | `PossessionBeginDate` / `PossessionEndDate`, `Firm_OriginalPossessionDate` | Contract Dates |
| `Possession - Paying Rent` | `PaymentsBeginDate` / `PaymentsEndDate` | Contract Dates |
| `Active` | `CommenceDate`, `ObligationDate`, `StatusEffectiveDate` | Contract Dates |
| `Closed` | `ExpireDate`, `ActualEndDate`, `Inactive`, `IsDead` | Contract Dates / Contract Info |

`PaymentsBeginDate`/`PaymentsEndDate` existing separately from `CommenceDate`/`ExpireDate` is
exactly what makes `Possession - Paying Rent` distinguishable from `Possession`. **Derived.** The
dates are the *evidence* for each state; the drop-down value is the *assertion*. Today nothing links
them — an analyst can set `Firm_LeaseStatus = Possession - Paying Rent` with `PaymentsBeginDate`
empty and nothing objects.

**4. There is a *third*, platform-internal state machine underneath, on `ProjectEntity`.**
Contract inherits a full phase apparatus from the polymorphic supertype
([§4](#4-walkhierarchyjsps-composition-tree--what-a-contract-owns)) — all twelve fields exist
identically on `Contract` and `ProjectEntity`:

```
CurrentCodeProjectPhaseID(Dropdown (Project Phase Code))
RealEstatePhaseStatus(Text)   DesignPhaseStatus(Text)      ConstructionPhaseStatus(Text)
PossessionPhaseStatus(Text)   OperationsPhaseStatus(Text)  CompletedPhaseStatus(Text)
CurrentPhaseStatus(Text)
PreviousMilestone(Text)  CurrentMilestone(Text)  NextMilestone(Text)  MilestoneTimeline(Text)
```

Six named phases, one of which — **Possession** — matches a Lease Status value by name. And
**`Project Phase Code` is not among the 207 Firm Drop Downs**: absent from the registry's full
catalogue while used by eleven objects (`Contract`, `Facility`, `Location`, `Parcel`, `Program`,
`Project`, `ProjectEntity`, `PotentialProject`, `Prototype`, `BudgetOptionTemplate`,
`ProcessTimelineTemplate`). That is the same pattern the registry infers for `Work Flow Status
Code` — a platform-internal enumeration governing engine behaviour rather than presentation.
**Observed** (presence in the object export, absence from the registry).

The phases are driven by a template. `ProcessTimelineTemplate` (10 fields):

| Field | Role |
|---|---|
| `CodeProjectPhaseID` | Which phase this milestone belongs to |
| `ProcessTimelineTemplateName`, `DefaultTaskName` | The milestone |
| `InProcessPhaseStatus(Text)` | The phase-status text to display **while in progress** |
| `CompletedPhaseStatus(Text)` | The phase-status text to display **when done** |
| `PreviousProcessTimelineID(Text)` | **A linked list — the milestone ordering** |
| `AlwaysShowInSummary(Boolean)` | Display |

and `ProcessTimeline` (31 fields) is the per-entity instance: `TaskName`, `CodeTaskStatusID`,
`PercentComplete`, `Assignee_MemberID`, Original/Projected/Actual start-end-duration triples,
`DaysAheadOfSchedule`, `RemainingDays`. `Contract.CurrentPhaseStatus` / `CurrentMilestone` /
`NextMilestone` / `PreviousMilestone` are `Text` **derived display fields** computed from those
instances. **Observed** fields; **Derived** mechanism.

### Three state machines, none of them connected

| # | Mechanism | Where | Configurable by | Governs |
|---|---|---|---|---|
| 1 | `CodeContractStatusID` — 3 values, `Active` undeletable | `Contract`, Global | Platform (values are Firm-editable, the table is not) | Record state |
| 2 | `Firm_LeaseStatus` — 9 values | `Contract`, Firm | **Any user with drop-down rights** | Operational lifecycle |
| 3 | `Project Phase Code` + `ProcessTimelineTemplate` → `ProcessTimeline` | `ProjectEntity`, inherited | Not tenant-editable | Process/milestone progress |

Nothing observed links (2) to (3), or either to the date fields. Three parallel notions of "where is
this contract up to", maintained independently. **Derived** — and it is the strongest argument for
ASG Edge+ modelling this deliberately rather than inheriting it.

### Verdict

| Axis | Keep as | Note |
|---|---|---|
| **Record state** | A small platform-seeded enum with protected values (`Active` is undeletable in Lucernex, and ASG Edge+'s `D-07` / `DeactivationPolicy` question applies directly) | **Split `AI Abstracted` out** into a separate `abstractionSource` field — it is provenance, not state. A contract can be AI-abstracted *and* active |
| **Lifecycle stage** | An explicit **stored** state machine, seeded with the nine observed values | Decide deliberately whether it stays tenant-editable. Nine states with legal transitions between them is not a drop-down |
| **Process progress** | Optional; only if ASG uses milestone timelines on leases (unverified — open question 3) | Keep separate from lifecycle |

The design recommendation is to **bind the assertion to its evidence**: store the state, and record
the date field and actor that justified each transition. That gives FR-029's audit requirement
somewhere structural to attach, replacing today's `Firm_LeaseStatusNotes` free-text box.

Two things to ask the business about:

- **The two `Accounting Purposes Only` values** have no BRD-24 counterpart. They read as contracts
  carried for ASC 842 measurement while operationally dormant — which the accounting engine must
  treat differently, and which interacts with `Covenant.HoldAmountInSchedLiability` and
  `SLSummary.IsIncludeInRollForwardReport`.
- **`Closed - Active`** is a state pair the BRD does not have, and its name inverts the record-state
  vocabulary. Worth confirming what distinguishes it from `Closed`.

Raised as a blocking item in
[`asg-edgeplus-mapping.md` §5.1](asg-edgeplus-mapping.md#51-blocking--contract-status-is-not-the-contract-lifecycle).

---

## Open questions

Ranked by impact on the frozen schema.

1. **What is the full value list of `Project Phase Code`?** It is the platform-internal phase
   enumeration behind the real lifecycle state machine ([§7](#7-contract-status-vs-the-brd-24-lifecycle--the-answer)),
   and it is **not** among the 207 Firm Drop Downs, so it cannot be read from `FirmCodeList.jsp`.
   The six phase-status fields name six phases (Real Estate, Design, Construction, Possession,
   Operations, Completed) but that is read off field names, not off the enumeration. Try the
   Contract summary page's phase display, or `ShowObjectDetails.jsp` for `ProcessTimelineTemplate`.
   *Blocks the lifecycle state-machine design.*
2. **What distinguishes `Closed - Active` from `Closed`, and what are the two
   `Accounting Purposes Only` values for?** Three of the nine Lease Status values have no BRD-24
   counterpart ([§7](#7-contract-status-vs-the-brd-24-lifecycle--the-answer)). The accounting-only
   pair in particular implies contracts measured under ASC 842 while operationally dormant, which
   changes how `SLSummary.IsIncludeInRollForwardReport` and
   `Covenant.HoldAmountInSchedLiability` should behave. Ask the business, and read the full label of
   the truncated ninth value.
3. **Is `ProcessTimeline` actually populated for contracts in this tenant, or only for projects?**
   The machinery exists on `ProjectEntity` and Contract inherits it, but whether ASG uses milestone
   timelines on leases is unverified. Open a live contract and look for a Milestones section.
4. **Does anything other than layout display use `MasterContractID`?** Specifically: does a
   sublease's rent roll up to its master, do allocations flow across the edge, and is depth > 1
   supported? *This is the single highest-priority live-UI check in this document*, because the
   answer determines whether ASG Edge+'s contract entity needs a hierarchy path, an allocation
   percentage on the edge, and a cycle guard.
5. **Which field distinguishes a master lease from a sublease?** `CodeAgreementTypeID` is the prime
   candidate; read its members from `FirmCodeList.jsp` (screen 007).
6. **Is a sublease's `IsReceivable` direction genuinely per-clause, or is there a contract-level
   convention?** Determines whether ASG Edge+ carries direction on the contract or only on money.
7. **Do all four `contract_*` tables always have a row?** Determines the migration's join strategy.
8. **Should ASG Edge+ add a contract-level primary vendor that Lucernex does not have?** BRD-24
   PJ-12 implies one. If yes, this is a deliberate divergence and needs an ADR.
9. **Are the 120 `Financial - Calendar/Fiscal` rollups recomputed on write, on read, or on a
   schedule?** `SLSummary`'s `NeedsRecalculation`/`RecalcTriggerDate` suggests a deferred
   recalculation queue; `Contract` has no equivalent flag.
10. **What populates `Contract.ProRataShareRate` versus `ExpenseRecovery.{persp}ProRataShareRate`?**
   A contract-level default with per-recovery overrides is the obvious reading, unconfirmed.
11. **Is `ProgramID`/Portfolio the tenant boundary?** `FiscalPeriod` is keyed by `ProgramID`, and
   `DiscountRate` is too — so the portfolio, not the firm, appears to own the fiscal calendar and
   the discount-rate table. That has direct bearing on ASG Edge+'s Hub/Spoke tenancy model.
