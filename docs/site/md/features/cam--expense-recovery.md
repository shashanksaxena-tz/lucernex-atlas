# CAM & Expense Recovery

Expense recovery - the CAM reconciliation tenants audit and landlords issue. This is the product's computational centre of gravity: 379 of the product's 422 formula fields sit on the single ExpenseRecovery record. The vendor wrote the entire waterfall into the field labels, so the calculation did not have to be reverse-engineered.

## Who it is for

*Derived · fact · source: `docs/features/README.md`*

Lease administrators auditing a landlord's reconciliation, and the analysts who have to defend the number back to the landlord.

## Where it is used

*Observed · fact · source: `docs/data-model/screen-routing.md`*

The expense-recovery grid on the contract. It is a reconciliation grid, not a schedule, and it has no schedule layer behind it.

## The CAM waterfall

*Observed · capability · source: `docs/modules/contracts/cam-waterfall.md`*

Sub Total #1 = Controllable + Non-Controllable - Deductions. Pass-Through = ST1 + Admin Fee % + Admin Fee + Additions. Sub Total #2 = Pass-Through - Recoveries. Net Pass-Through = ST2 x Pro Rata Share Rate. Net Amount Due = NPT - Pre-Paid. Revised = NAD + Adjustments. Every one of those expressions is literally a field label. Observed.

## Grid, not a schedule

*Derived · capability · source: `docs/modules/contracts/setup-schedule-transaction-pattern.md`*

CAM is a reconciliation grid, not a schedule: it has no schedule layer and does not follow the four-layer pattern every other money flow uses. Treating it as an instance of that pattern would be the single most expensive modelling mistake available here. It is a wide grid of stored, precomputed figures.

## Four bases, gross/net

*Observed · capability · source: `View Object Model, ExpenseRecovery field labels`*

Every figure exists as Budgeted, Reported, Approved and Prior, each in Gross and Net form, and five pairwise variances (Approved-Budgeted, Approved-Prior, Budgeted-Prior, Reported-Approved, Reported-Prior) are precomputed for every waterfall line. The table is wide because the variance grid is fully materialised rather than computed on read. A rebuild could store four bases and compute variances on demand - the largest single schema simplification available in this product.

## Occupancy gross-up

*Observed · capability · source: `Vendor field labels, Observed`*

The gross-up provision - recovering as if the centre were fully occupied - applies only on the Approved basis: approved net pass-through multiplies by an Occupancy Factor, every other basis uses only the pro-rata rate. One formula for all bases gets approved amounts wrong on every gross-up lease.

## NoZeroDef: nullable

*Derived · capability · source: `Field-name analysis, CON-R-160`*

Prior periods are nullable by design: every prior-period field carries the suffix NoZeroDef - a prior period that does not exist is unknown, not zero. Zero-defaulting would manufacture 100% variances on every first-year reconciliation. Recovery measures must be nullable, never zero-defaulted.

## Waterfall gaps

*Observed · fact*

Three gaps remain: whether Admin Fee % applies to Sub Total #1 or something narrower; where the Cap clamps (it has variance fields but appears in no labelled formula); and what feeds the Occupancy Factor. All tracked as open questions in the corpus.

## Open questions (77)

*Inferred · group*

77 things nobody has confirmed for this feature. Each one is work somebody has to do before the feature can be rebuilt with confidence; they are carried here rather than resolved by guessing. Click one for the question and the document that raised it.

### What is the value list

*Inferred · question · source: `docs/modules/contracts/asg-edgeplus-mapping.md`*

What is the value list of Project Phase Code, and of the tenant's Firm_LeaseStatus? (§5.1.) Together they settle whether FR-010's five stages already exist in the incumbent in some form. Project Phase Code is not tenant-editable and cannot be read from FirmCodeList.jsp; Firm_LeaseStatus is a Client Drop Down, readable from CustomCodeTableEdit.jsp. Nobody has confirmed this. Recorded in modules/contracts/asg-edgeplus-mapping.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### Does MasterContractID

*Inferred · question · source: `docs/modules/contracts/asg-edgeplus-mapping.md`*

Does MasterContractID drive any financial behaviour? (Rollup, allocation, depth > 1.). Nobody has confirmed this. Recorded in modules/contracts/asg-edgeplus-mapping.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### AccountNumber1 8

*Inferred · question · source: `docs/modules/contracts/asg-edgeplus-mapping.md`*

AccountNumber1..8 — segments or split lines? (CON-R-111.). Nobody has confirmed this. Recorded in modules/contracts/asg-edgeplus-mapping.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### Is Virtual a query a

*Inferred · question · source: `docs/modules/contracts/asg-edgeplus-mapping.md`*

Is Virtual* a query, a view, or a cached table?. Nobody has confirmed this. Recorded in modules/contracts/asg-edgeplus-mapping.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### Contract level vendor

*Inferred · question · source: `docs/modules/contracts/asg-edgeplus-mapping.md`*

Contract-level vendor: option A or B? (§5 — needs an ADR either way.). Nobody has confirmed this. Recorded in modules/contracts/asg-edgeplus-mapping.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### CON R 058 marginal

*Inferred · question · source: `docs/modules/contracts/asg-edgeplus-mapping.md`*

CON-R-058 — marginal band or simple excess for percentage-rent tiers? Does not change the schema, but every percentage-rent number depends on it and it blocks ASG component #22's test corpus. Nobody has confirmed this. Recorded in modules/contracts/asg-edgeplus-mapping.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### CON R 094 CON R 095

*Inferred · question · source: `docs/modules/contracts/asg-edgeplus-mapping.md`*

CON-R-094 / CON-R-095 — where do the CAM cap and base year enter the waterfall? Same: not schema, but blocks the CAM test corpus. Nobody has confirmed this. Recorded in modules/contracts/asg-edgeplus-mapping.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### Which of the 40 code

*Inferred · question · source: `docs/modules/contracts/asg-edgeplus-mapping.md`*

Which of the ~40 code lists are Hub-global and which are firm-overridable? Directly engages the unwritten Hub→Spoke publish/accept mechanism. CodeExpenseType is the hard case: its GL account numbers are unavoidably firm-specific while its accounting-treatment bindings should be global. Nobody has confirmed this. Recorded in modules/contracts/asg-edgeplus-mapping.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### Do the core financial

*Inferred · question · source: `docs/modules/contracts/asg-edgeplus-mapping.md`*

**Do the core financial tables (payment_transaction, expense_setup, expense_schedule, expense_recovery_part*) land as TEXT like the 33 tables in _crossmap.tsv?** None of them appear there. If they do, hazard #1 applies to the whole migration; if they are properly typed, it applies only to the reference tables. Nobody has confirmed this. Recorded in modules/contracts/asg-edgeplus-mapping.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### What exactly is Admin

*Inferred · question · source: `docs/modules/contracts/cam-waterfall.md`*

What exactly is Admin Fee % versus Admin Fee? Both appear as separate addends in the Pass-Through formula, so one is a rate-derived amount and the other a flat fee — but which is which, and does the percentage apply to Sub Total #1 or to something narrower?. Nobody has confirmed this. Recorded in modules/contracts/cam-waterfall.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### Where does the cap

*Inferred · question · source: `docs/modules/contracts/cam-waterfall.md`*

Where does the cap clamp? CapAmount has variance fields at every basis but does not appear in any of the labelled formulas. CON-R-094 flagged this as unresolved and it remains so. Nobody has confirmed this. Recorded in modules/contracts/cam-waterfall.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### What sets

*Inferred · question · source: `docs/modules/contracts/cam-waterfall.md`*

What sets OccupancyAdjustedThreshold? The gross-up factor is computed, so something feeds it — probably an occupancy percentage on the Location or Complex. Nobody has confirmed this. Recorded in modules/contracts/cam-waterfall.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### What are the 1 804

*Inferred · question · source: `docs/modules/contracts/cam-waterfall.md`*

What are the 1,804 NonMathComputed fields, and how do they differ from Math? Capturing that list would complete the classification for the whole product. Nobody has confirmed this. Recorded in modules/contracts/cam-waterfall.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### Are the COREFirmOnly

*Inferred · question · source: `docs/modules/contracts/cam-waterfall.md`*

Are the COREFirmOnly "Duplicate" fields safe to drop in a migration?. Nobody has confirmed this. Recorded in modules/contracts/cam-waterfall.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### Tenant math

*Inferred · question · source: `docs/modules/contracts/cam-waterfall.md`*

Tenant.math_calcTotalCapacity_1 — a headcount calculation on the Tenant record, unrelated to anything else in the corpus. What uses it?. Nobody has confirmed this. Recorded in modules/contracts/cam-waterfall.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### What is the full value

*Inferred · question · source: `docs/modules/contracts/contract-hierarchy.md`*

What is the full value list of Project Phase Code? It is the platform-internal phase enumeration behind the real lifecycle state machine (§7), and it is not among the 207 Firm Drop Downs, so it cannot be read from FirmCodeList.jsp. The six phase-status fields name six phases (Real Estate, Design, Construction, Possession, Operations, Completed) but that is read off field names, not off the enumeration. Try the Contract summary page's phase display, or ShowObjectDetails.jsp for ProcessTimelineTemplate. *Blocks the lifecycle state-machine design.*. Nobody has confirmed this. Recorded in modules/contracts/contract-hierarchy.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### What distinguishes

*Inferred · question · source: `docs/modules/contracts/contract-hierarchy.md`*

**What distinguishes Closed - Active from Closed, and what are the two Accounting Purposes Only values for?** Three of the nine Lease Status values have no BRD-24 counterpart (§7). The accounting-only pair in particular implies contracts measured under ASC 842 while operationally dormant, which changes how SLSummary.IsIncludeInRollForwardReport and Covenant.HoldAmountInSchedLiability should behave. Ask the business, and read the full label of the truncated ninth value. Nobody has confirmed this. Recorded in modules/contracts/contract-hierarchy.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### Is ProcessTimeline

*Inferred · question · source: `docs/modules/contracts/contract-hierarchy.md`*

Is ProcessTimeline actually populated for contracts in this tenant, or only for projects? The machinery exists on ProjectEntity and Contract inherits it, but whether ASG uses milestone timelines on leases is unverified. Open a live contract and look for a Milestones section. Nobody has confirmed this. Recorded in modules/contracts/contract-hierarchy.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### Does anything other

*Inferred · question · source: `docs/modules/contracts/contract-hierarchy.md`*

Does anything other than layout display use MasterContractID? Specifically: does a sublease's rent roll up to its master, do allocations flow across the edge, and is depth > 1 supported? *This is the single highest-priority live-UI check in this document*, because the answer determines whether ASG Edge+'s contract entity needs a hierarchy path, an allocation percentage on the edge, and a cycle guard. Nobody has confirmed this. Recorded in modules/contracts/contract-hierarchy.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### Which field

*Inferred · question · source: `docs/modules/contracts/contract-hierarchy.md`*

Which field distinguishes a master lease from a sublease? CodeAgreementTypeID is the prime candidate; read its members from FirmCodeList.jsp (screen 007). Nobody has confirmed this. Recorded in modules/contracts/contract-hierarchy.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### Is a sublease s

*Inferred · question · source: `docs/modules/contracts/contract-hierarchy.md`*

**Is a sublease's IsReceivable direction genuinely per-clause, or is there a contract-level convention?** Determines whether ASG Edge+ carries direction on the contract or only on money. Nobody has confirmed this. Recorded in modules/contracts/contract-hierarchy.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### Do all four contract

*Inferred · question · source: `docs/modules/contracts/contract-hierarchy.md`*

Do all four contract_* tables always have a row? Determines the migration's join strategy. Nobody has confirmed this. Recorded in modules/contracts/contract-hierarchy.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### Should ASG Edge add a

*Inferred · question · source: `docs/modules/contracts/contract-hierarchy.md`*

Should ASG Edge+ add a contract-level primary vendor that Lx does not have? BRD-24 PJ-12 implies one. If yes, this is a deliberate divergence and needs an ADR. Nobody has confirmed this. Recorded in modules/contracts/contract-hierarchy.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### Are the 120 Financial

*Inferred · question · source: `docs/modules/contracts/contract-hierarchy.md`*

**Are the 120 Financial - Calendar/Fiscal rollups recomputed on write, on read, or on a schedule?** SLSummary's NeedsRecalculation/RecalcTriggerDate suggests a deferred recalculation queue; Contract has no equivalent flag. Nobody has confirmed this. Recorded in modules/contracts/contract-hierarchy.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### What populates

*Inferred · question · source: `docs/modules/contracts/contract-hierarchy.md`*

What populates Contract.ProRataShareRate versus ExpenseRecovery.{persp}ProRataShareRate? A contract-level default with per-recovery overrides is the obvious reading, unconfirmed. Nobody has confirmed this. Recorded in modules/contracts/contract-hierarchy.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### Is ProgramID Portfolio

*Inferred · question · source: `docs/modules/contracts/contract-hierarchy.md`*

Is ProgramID/Portfolio the tenant boundary? FiscalPeriod is keyed by ProgramID, and DiscountRate is too — so the portfolio, not the firm, appears to own the fiscal calendar and the discount-rate table. That has direct bearing on ASG Edge+'s Hub/Spoke tenancy model. Nobody has confirmed this. Recorded in modules/contracts/contract-hierarchy.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### What is the

*Inferred · question · source: `docs/modules/contracts/data-model.md`*

**What is the ProjectEntity supertype's discriminator column, and is ProjectEntityID globally unique across all entity types?** This determines whether ASG Edge+'s payment ledger can be single-table-polymorphic or needs separate ledgers per entity type. *(Check ShowObjectDetails.jsp?sqlTableID= for ProjectEntity.)*. Nobody has confirmed this. Recorded in modules/contracts/data-model.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### What does the 145

*Inferred · question · source: `docs/modules/contracts/data-model.md`*

What does the ~145-field gap between 2,678 and 2,823 consist of? *(Re-run the Manage Data Fields Contract-group export and diff.)*. Nobody has confirmed this. Recorded in modules/contracts/data-model.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### Are the seven weak

*Inferred · question · source: `docs/modules/contracts/data-model.md`*

Are the seven weak (Text-typed) FKs enforced anywhere? If Lx tolerates dangling PaymentTransaction.ExpenseRecoveryID, the migration needs an orphan-handling policy. Nobody has confirmed this. Recorded in modules/contracts/data-model.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### Does Contract s four

*Inferred · question · source: `docs/modules/contracts/data-model.md`*

Does Contract's four-table split imply four separate row lifecycles, or is it one row spread across four tables with a shared PK? *(Check whether contract_firm1 rows can exist without a contract_admin row.)*. Nobody has confirmed this. Recorded in modules/contracts/data-model.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### Do the fourteen 3000

*Inferred · question · source: `docs/modules/contracts/data-model.md`*

**Do the fourteen 3000-band code tables with no modelled object carry anything beyond (ShortName, ActualLongName, Inactive)?** (§8.) Contract Type (3003) and Key Date Type (3006) are the two that would most change this module if they did — the first is a candidate home for the master-lease/sublease role discriminator, the second for the lifecycle key-date taxonomy. Open each in FirmCodeEdit.jsp and count the columns. Nobody has confirmed this. Recorded in modules/contracts/data-model.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### Which of the 33 landed

*Inferred · question · source: `docs/modules/contracts/data-model.md`*

Which of the 33 landed Postgres tables in _crossmap.tsv are the complete set? None of the core financial tables (payment_transaction, expense_setup, expense_schedule, expense_recovery_part*) appear in it — only covenant, sales, usage, allowance, insurance, responsibility, party do. Whether the financial tables land as TEXT too is unverified and is the highest-value single fact still missing. Nobody has confirmed this. Recorded in modules/contracts/data-model.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### Is EscalationIndex

*Inferred · question · source: `docs/modules/contracts/escalations.md`*

Is EscalationIndex.IndexAmount a published index *level* or a *change rate*? (§3.) This single fact determines the CPI formula. Load two consecutive months of a known index and read the values — if they are ~312 and ~313 it is a level; if ~0.03 it is a rate. Nobody has confirmed this. Recorded in modules/contracts/escalations.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### What is the value

*Inferred · question · source: `docs/modules/contracts/escalations.md`*

What is the value space of ExpenseEscalation.EscalationMethod(Text)? It is the fixed-driver discriminator and it is free text. Query distinct values, or read the UI dropdown that populates it. Nobody has confirmed this. Recorded in modules/contracts/escalations.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### ExpenseSetup

*Inferred · question · source: `docs/modules/contracts/escalations.md`*

**ExpenseSetup.CodeCPIIndexID vs ExpenseEscalation.EscalationIndexID — redundant or complementary?** Two paths to the same index series. Nobody has confirmed this. Recorded in modules/contracts/escalations.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### Does CPI ADJUSTMENTS

*Inferred · question · source: `docs/modules/contracts/escalations.md`*

Does CPI_ADJUSTMENTS rewrite ExpenseSchedule rows in place or generate new ones? Determines the retroactive-restatement model. Nobody has confirmed this. Recorded in modules/contracts/escalations.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### Precedence between

*Inferred · question · source: `docs/modules/contracts/escalations.md`*

**Precedence between ExpenseSetup's increase/decrease caps and ExpenseEscalation's period/lifetime collar.** Both apply to the same amount; which binds first?. Nobody has confirmed this. Recorded in modules/contracts/escalations.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### What are the members

*Inferred · question · source: `docs/modules/contracts/escalations.md`*

**What are the members of Dropdown (Escalation Type Code), (Escalation Category Code), (Escalation Group Code), (Index Type Code), (Index Source Code), (CPI Index Code), (Adjustment Method Code), (Escalation Payment Method)?** Eight code lists, all readable from FirmCodeList.jsp (screen 007). Nobody has confirmed this. Recorded in modules/contracts/escalations.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### Does StopAmount behave

*Inferred · question · source: `docs/modules/contracts/escalations.md`*

Does StopAmount behave as an expense stop (tenant pays the excess) or as a hard ceiling? The name says stop; CapAmount already covers ceiling, which supports the stop reading — but it is unconfirmed. Nobody has confirmed this. Recorded in modules/contracts/escalations.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### Is ExpenseEscalation

*Inferred · question · source: `docs/modules/contracts/escalations.md`*

Is ExpenseEscalation one row per clause or one row per step? BeginDate/EndDate + EscalationPeriod reads as one row per clause driving many steps, but a per-step model would also fit. Check whether a 10-year lease with annual escalation has 1 or 10 rows. Nobody has confirmed this. Recorded in modules/contracts/escalations.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### What exactly

*Inferred · question · source: `docs/modules/contracts/expense-recovery-cam.md`*

What exactly distinguishes Gross from Net on every measure? Gross-up basis, pre/post exclusions, or something else? Nothing in the corpus names it. Open a recovery record in the UI with both populated and read the on-screen section headers. Nobody has confirmed this. Recorded in modules/contracts/expense-recovery-cam.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### Where in the waterfall

*Inferred · question · source: `docs/modules/contracts/expense-recovery-cam.md`*

Where in the waterfall is the cap applied — to C, to ST1, or to NAD? The labels stop short of showing it. Enter a recovery with a cap below ST1 and read which computed field changes. *This changes every capped CAM number.*. Nobody has confirmed this. Recorded in modules/contracts/expense-recovery-cam.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### Where does

*Inferred · question · source: `docs/modules/contracts/expense-recovery-cam.md`*

Where does BaseYearAmount enter the waterfall? Same test: set a base-year amount and see which computed measure moves. Nobody has confirmed this. Recorded in modules/contracts/expense-recovery-cam.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### What are the members

*Inferred · question · source: `docs/modules/contracts/expense-recovery-cam.md`*

**What are the members of Dropdown (Recovery Type Code), (Calculation Method), (Exp Rec Based On), (Pro Rata Share Method), (Cap Type), (Base Year Amount Type)?** Six code lists whose members define the model's variant space. All readable from FirmCodeList.jsp (screen 007). Nobody has confirmed this. Recorded in modules/contracts/expense-recovery-cam.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### Why does

*Inferred · question · source: `docs/modules/contracts/expense-recovery-cam.md`*

Why does NetPassThroughCOREFirmOnly exist, labelled *"Duplicate"*? It appears on Reported/Approved/Prior but not Budgeted, and not in any variance family. A legacy or firm-specific parallel calculation. Nobody has confirmed this. Recorded in modules/contracts/expense-recovery-cam.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### Is NoZeroDef really no

*Inferred · question · source: `docs/modules/contracts/expense-recovery-cam.md`*

Is NoZeroDef really "no zero default"? Confirm by leaving a measure blank and checking whether the variance renders blank or as a 100% swing. Nobody has confirmed this. Recorded in modules/contracts/expense-recovery-cam.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### Does ExpenseRecovery

*Inferred · question · source: `docs/modules/contracts/expense-recovery-cam.md`*

**Does ExpenseRecovery have a *per-period* row, or one row per contract per recovery category?** BeginDate/EndDate + RecoveryPeriod(Text) + the Prior* perspectives suggest one row per recovery period, with Prior* denormalised from the previous row. Confirm by listing recovery records for a multi-year contract. **This determines whether ASG Edge+ needs a period key on the recovery entity.**. Nobody has confirmed this. Recorded in modules/contracts/expense-recovery-cam.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### How are the four

*Inferred · question · source: `docs/modules/contracts/expense-recovery-cam.md`*

How are the four expense_recovery_part1..4 tables keyed and joined? They share ExpenseRecoveryID (which appears four times in the field export), but whether all four rows are always created is unknown. Nobody has confirmed this. Recorded in modules/contracts/expense-recovery-cam.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### How is a

*Inferred · question · source: `docs/modules/contracts/payment-lifecycle.md`*

How is a PaymentReceipt matched to the PaymentTransactions it settles? There is no FK and no link table. Only AmountAllocated/AmountNotAllocated on each side and the RECONCILE_RECEIPT command. Open a receipt in the UI and see what the reconcile screen joins on. *This is a genuine schema gap — ASG Edge+ should add an explicit allocation table.*. Nobody has confirmed this. Recorded in modules/contracts/payment-lifecycle.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### Where do

*Inferred · question · source: `docs/modules/contracts/payment-lifecycle.md`*

**Where do AccountNumber1..8 come from, and are they eight segments of one account or eight split-coding lines?** docs/data-fields/payment-transaction.md says split coding; Organization also carries Account Number #1–8, suggesting segments. Read one posted transaction's eight values against its organization's eight. *This is the core of the GL export.*. Nobody has confirmed this. Recorded in modules/contracts/payment-lifecycle.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### Precedence between

*Inferred · question · source: `docs/modules/contracts/payment-lifecycle.md`*

Precedence between ExpenseSchedule.TaxAmount1..4 and CalculatedTaxAmount1..4. Which one reaches PaymentTransaction.TaxAmount1..4?. Nobody has confirmed this. Recorded in modules/contracts/payment-lifecycle.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### What is the base date

*Inferred · question · source: `docs/modules/contracts/payment-lifecycle.md`*

What is the base date for the first aging ladder (AgingAmountForMonth1..3)? Invoice date or effective date? The second ladder is explicitly due-date-based. Nobody has confirmed this. Recorded in modules/contracts/payment-lifecycle.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### Is there any FX rate

*Inferred · question · source: `docs/modules/contracts/payment-lifecycle.md`*

Is there any FX rate on the payment path? CodeCheckCurrencyTypeID differs from CodeCurrencyTypeID but no rate or gain/loss field exists on PaymentTransaction, while SLPeriod has a full translation apparatus. Confirm whether cross-currency settlement is actually supported or merely representable. Nobody has confirmed this. Recorded in modules/contracts/payment-lifecycle.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### Does DELETE PAYMENTS

*Inferred · question · source: `docs/modules/contracts/payment-lifecycle.md`*

Does DELETE_PAYMENTS refuse rows carrying ExportBatchNumber or CheckNumber? Determines whether "exported" is a hard immutability boundary. Nobody has confirmed this. Recorded in modules/contracts/payment-lifecycle.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### What are the members

*Inferred · question · source: `docs/modules/contracts/payment-lifecycle.md`*

What are the members of Dropdown (Source Entity Code)? The complete list of generators that can write to the ledger. Nobody has confirmed this. Recorded in modules/contracts/payment-lifecycle.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### Are ExpenseAllocation

*Inferred · question · source: `docs/modules/contracts/payment-lifecycle.md`*

**Are ExpenseAllocation (by OrganizationID, AllocationPercentage) and ExpenseVendorAllocation (by VendorID, PaymentPercentage) applied at generation time (producing N transactions) or at export time (producing N GL lines from one transaction)?** Changes the cardinality of the ledger. Nobody has confirmed this. Recorded in modules/contracts/payment-lifecycle.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### What are the members

*Inferred · question · source: `docs/modules/contracts/percentage-rent.md`*

What are the members of Dropdown (Percentage Rent Type Code)? This is the calculation variant selector and the single largest unknown in the whole clause. Readable from Manage Firm Drop Downs / Client Drop Downs (screen 007 route, FirmCodeList.jsp). Nobody has confirmed this. Recorded in modules/contracts/percentage-rent.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### Marginal band or

*Inferred · question · source: `docs/modules/contracts/percentage-rent.md`*

Marginal band or simple excess for PRPSalesPastBreakpoint_N? (§4 step 4.) Enter a two-tier breakpoint, post sales above both thresholds, and read the eight Rent Due #N values on the Sales Period list. Every percentage-rent number in a rebuilt system depends on this. Nobody has confirmed this. Recorded in modules/contracts/percentage-rent.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### What is the numerator

*Inferred · question · source: `docs/modules/contracts/percentage-rent.md`*

What is the numerator in naturalBreakpoint = minimumRent / NaturalBreakpointRate? Contract.CurrentAnnualBaseRent, the base-rent ExpenseSetup sum, or the period's ExpenseSchedule.AnnualAmount? Compare a natural-breakpoint contract's derived PRPBreakpointAmount1 against each candidate. Nobody has confirmed this. Recorded in modules/contracts/percentage-rent.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

### Are the Firm Sales

*Inferred · question · source: `docs/modules/contracts/percentage-rent.md`*

Are the Firm_*Sales* exclusion families on Contract documentary or functional? (§6.) Check whether a contract with Firm_EmployeeSalesAllowable set but no SalesExclusion row still excludes employee sales. Nobody has confirmed this. Recorded in modules/contracts/percentage-rent.md, under the Contracts & Leases area. Until it is settled, anything built on the assumption is a guess.

## Rules (9)

*Derived · group*

Every numbered rule the docs corpus records for this feature, named by a short summary. Click one: the panel opens with its ID, the full statement, and a link to the complete rule page.

### 14 The CAM recovery — [CON-R-153](../rules/CON-R-153.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**A recovery period is calculated · Controllable, Non-Controllable, Deductions · `Sub Total #1 = C + NC − D` · `SubTotal1{Gross,Net}` · Observed.**

|  |  |
|---|---|
| Stated as | A recovery period is calculated |
| Stated as | Controllable, Non-Controllable, Deductions |
| Stated as | `Sub Total #1 = C + NC − D` |
| Stated as | `SubTotal1{Gross,Net}` |
| Stated as | Observed |

### 14 The CAM recovery — [CON-R-154](../rules/CON-R-154.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Sub Total #1 is known · Admin Fee % amount, Admin Fee, Additions · `Pass-Through = ST1 + AF% + AF + A` · `PassThrough{Gross,Net}` · Observed.**

|  |  |
|---|---|
| Stated as | Sub Total #1 is known |
| Stated as | Admin Fee % amount, Admin Fee, Additions |
| Stated as | `Pass-Through = ST1 + AF% + AF + A` |
| Stated as | `PassThrough{Gross,Net}` |
| Stated as | Observed |

### 14 The CAM recovery — [CON-R-155](../rules/CON-R-155.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Pass-Through is known · Recoveries · `Sub Total #2 = PT − R` · `SubTotal2{Gross,Net}` · Observed.**

|  |  |
|---|---|
| Stated as | Pass-Through is known |
| Stated as | Recoveries |
| Stated as | `Sub Total #2 = PT − R` |
| Stated as | `SubTotal2{Gross,Net}` |
| Stated as | Observed |

### 14 The CAM recovery — [CON-R-156](../rules/CON-R-156.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Sub Total #2 is known · Pro Rata Share Rate; Occupancy Factor · `Net Pass-Through = ST2 × PRR` on Budgeted/Reported/Prior, but `ST2 × PRS × Occ` on Approved — the gross-up provision · `NetPassThrough{Gross,Net}` · Observed.**

|  |  |
|---|---|
| Stated as | Sub Total #2 is known |
| Stated as | Pro Rata Share Rate; Occupancy Factor |
| Stated as | `Net Pass-Through = ST2 × PRR` on Budgeted/Reported/Prior, but `ST2 × PRS × Occ` on Approved — the gross-up provision |
| Stated as | `NetPassThrough{Gross,Net}` |
| Stated as | Observed |

### 14 The CAM recovery — [CON-R-157](../rules/CON-R-157.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Net Pass-Through is known · Pre-Paid Amount · `Net Amount Due = NPT − PP` · `NetAmountDue{Gross,Net}` · Observed.**

|  |  |
|---|---|
| Stated as | Net Pass-Through is known |
| Stated as | Pre-Paid Amount |
| Stated as | `Net Amount Due = NPT − PP` |
| Stated as | `NetAmountDue{Gross,Net}` |
| Stated as | Observed |

### 14 The CAM recovery — [CON-R-158](../rules/CON-R-158.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Net Amount Due is known · Adjustments · `Revised Amount Due = Net + Adj` · `RevisedNetAmountDue{Gross,Net}` · Observed.**

|  |  |
|---|---|
| Stated as | Net Amount Due is known |
| Stated as | Adjustments |
| Stated as | `Revised Amount Due = Net + Adj` |
| Stated as | `RevisedNetAmountDue{Gross,Net}` |
| Stated as | Observed |

### 14 The CAM recovery — [CON-R-159](../rules/CON-R-159.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Any recovery figure is stored · — · Four bases (Budgeted, Reported, Approved, Prior) × {Gross, Net}, with five pairwise variances (A-B, A-P, B-P, R-A, R-P) materialised as both amount and percentage for every waterfall line · ~379 stored columns · Observed.**

|  |  |
|---|---|
| Stated as | Any recovery figure is stored |
| Stated as | — |
| Stated as | Four bases (Budgeted, Reported, Approved, Prior) × {Gross, Net}, with five pairwise variances (A-B, A-P, B-P, R-A, R-P) materialised as both amount and percentage for every waterfall line |
| Stated as | ~379 stored columns |
| Stated as | Observed |

### 14 The CAM recovery — [CON-R-160](../rules/CON-R-160.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**A prior-period measure is absent · `…NoZeroDef` columns · Prior measures are nullable, never zero-defaulted — a missing prior period is unknown, not zero, or every first-year reconciliation reports spurious 100% variances · Nullable `BigDecimal` · Observed.**

|  |  |
|---|---|
| Stated as | A prior-period measure is absent |
| Stated as | `…NoZeroDef` columns |
| Stated as | Prior measures are nullable, never zero-defaulted — a missing prior period is unknown, not zero, or every first-year reconciliation reports spurious 100% variances |
| Stated as | Nullable `BigDecimal` |
| Stated as | Observed |

### 14 The CAM recovery — [CON-R-161](../rules/CON-R-161.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Classifying any field · View Object Model filters · Of 7,047 fields: 3,437 editable (49%), 1,804 non-math computed (26%), 422 math (6%). 90% of all formula fields live on `ExpenseRecovery` · Field classification · Observed.**

|  |  |
|---|---|
| Stated as | Classifying any field |
| Stated as | View Object Model filters |
| Stated as | Of 7,047 fields: 3,437 editable (49%), 1,804 non-math computed (26%), 422 math (6%). 90% of all formula fields live on `ExpenseRecovery` |
| Stated as | Field classification |
| Stated as | Observed |
