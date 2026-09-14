# Leases & Contracts

The lease record is the centre of the product: 570 fields across four physical tables, and 62 other record types point at it. Payment processing, percentage rent and ASC 842 accounting all sit downstream of it, which is why its schema freeze gates them.

## Who it is for

*Derived · fact · source: `docs/features/README.md`*

Lease administrators and abstractors — the people who read an executed lease and turn it into data. Everything else in the product reads what they enter.

## Where it is used

*Observed · fact · source: `docs/data-model/screen-routing.md`*

The contract record: 15 SEP page layouts and the sub-page sections beneath them, reached from the Contracts navigation root.

## Co-tenancy clauses

*Observed · capability · source: `data-fields/co-tenancy.md, modules/contracts/percentage-rent.md`*

A retail clause family with its own 26-field record: anchor name, co-tenancy group and type, occupancy percentage, rent reduction amount and percent, and a right-to-terminate flag, linked to the lease and to a covenant record, with two code tables governing clause kinds. The record is fully tabulated in the corpus; how Lx evaluates the clause - what triggers the occupancy test, how the reduction applies, what termination unlocks - is documented only in outline and stands as an open analysis item. ASG Edge+ BRD-29.

## The 4-layer pattern

*Derived · capability · source: `docs/modules/contracts/setup-schedule-transaction-pattern.md`*

Every money flow is modelled as four layers: Clause (the negotiated term), Schedule (the calculated run of amounts), Transaction (an executed payment or charge) and Projection (future expectation). Rent, escalations and most financial terms follow it. CAM is the one exception - see its own feature.

## Lifecycle in data

*Observed · capability · source: `docs/data-model/code-table-registry.md`*

The lease lifecycle lives in tenant-editable data, not schema: nine states - Open, Future Possession, Possession, Paying Rent, Active, two Closed variants and two Accounting Purposes Only variants - sit in a tenant-authored list. Anyone with drop-down rights can add a tenth. The platform's own three-value status field means something different, and both are required on the same form.

## Self-parenting leases

*Observed · capability · source: `_lucernex_objects_summary.txt`*

A lease can be its own parent: the master-contract field points back at leases, carrying the master-lease and sublease hierarchy.

## Asymmetric relations

*Observed · capability · source: `Live screen capture, screen 014`*

Relationships read differently from each side: from a lease, the building is a single related record; from the building, leases appear as an embedded child list. The product models the one-to-many direction differently from the many-to-one - a rebuild should pick one convention.

## Vendor = Employer

*Observed · capability · source: `_crossmap.tsv`*

The payee ('Vendor') is a relabelled Employer: the payment's vendor field is declared as an Employer ID. The lease itself has no vendor foreign key at all - the payee relationship lives on the payment, not the lease.

## Evidence

*Observed · fact · source: `docs/assets/screenshots/`*

23 screen captures on disk, under docs/assets/screenshots/end-user, docs/assets/screenshots/bbw-enduser — the screens themselves, not a description of them. First few: asc842-rent-schedule.jpg, contract-summary-rendered.jpg, expense-setup-with-vendor-allocations.jpg, generate-payments-dialog.jpg, payment-transactions-empty.jpg, ct-01-contract.jpg.

![asc842-rent-schedule.jpg](../../assets/screenshots/end-user/asc842-rent-schedule.jpg)
![contract-summary-rendered.jpg](../../assets/screenshots/end-user/contract-summary-rendered.jpg)
![expense-setup-with-vendor-allocations.jpg](../../assets/screenshots/end-user/expense-setup-with-vendor-allocations.jpg)
![generate-payments-dialog.jpg](../../assets/screenshots/end-user/generate-payments-dialog.jpg)
![payment-transactions-empty.jpg](../../assets/screenshots/end-user/payment-transactions-empty.jpg)
![ct-01-contract.jpg](../../assets/screenshots/bbw-enduser/ct-01-contract.jpg)
![ct-02-details.jpg](../../assets/screenshots/bbw-enduser/ct-02-details.jpg)
![ct-03-summary.jpg](../../assets/screenshots/bbw-enduser/ct-03-summary.jpg)
![ct-04-abstract-info.jpg](../../assets/screenshots/bbw-enduser/ct-04-abstract-info.jpg)
![ct-05-abstract-details.jpg](../../assets/screenshots/bbw-enduser/ct-05-abstract-details.jpg)
![ct-12-co-tenancy.jpg](../../assets/screenshots/bbw-enduser/ct-12-co-tenancy.jpg)
![ct-13-payment-info.jpg](../../assets/screenshots/bbw-enduser/ct-13-payment-info.jpg)
![ct-14-payment-details.jpg](../../assets/screenshots/bbw-enduser/ct-14-payment-details.jpg)
![ct-26-accounting-info.jpg](../../assets/screenshots/bbw-enduser/ct-26-accounting-info.jpg)
![ct-27-accounting-details.jpg](../../assets/screenshots/bbw-enduser/ct-27-accounting-details.jpg)
![ct-28-capital-lease-test.jpg](../../assets/screenshots/bbw-enduser/ct-28-capital-lease-test.jpg)
![ct-32-accrual-info.jpg](../../assets/screenshots/bbw-enduser/ct-32-accrual-info.jpg)
![ct-33-accrual-details.jpg](../../assets/screenshots/bbw-enduser/ct-33-accrual-details.jpg)
![ct-36-percentage-rent-accruals.jpg](../../assets/screenshots/bbw-enduser/ct-36-percentage-rent-accruals.jpg)
![eq-01-details-summary.jpg](../../assets/screenshots/bbw-enduser/eq-01-details-summary.jpg)
![eq-02-abstract-details.jpg](../../assets/screenshots/bbw-enduser/eq-02-abstract-details.jpg)
![eq-03-payment-details.jpg](../../assets/screenshots/bbw-enduser/eq-03-payment-details.jpg)
![eq-04-accounting-details.jpg](../../assets/screenshots/bbw-enduser/eq-04-accounting-details.jpg)

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

## Rules (161)

*Derived · group*

Every numbered rule the docs corpus records for this feature, named by a short summary. Click one: the panel opens with its ID, the full statement, and a link to the complete rule page.

### 1 The Clause — [CON-R-001](../rules/CON-R-001.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Classifying any financial record by its field set: if it carries both AmendmentID and Section, it is an L0 clause record.**

|  |  |
|---|---|
| Stated as | Classifying any financial record |
| Stated as | The record's field set |
| Stated as | If it carries both `AmendmentID` and `Section`, it is an L0 clause record |
| Stated as | `layer = CLAUSE` |
| Stated as | Observed |

### 1 The Clause — [CON-R-002](../rules/CON-R-002.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Classifying any financial record: if it carries an FK to an L0 object and ProcessedFlag, it is an L1 schedule row.**

|  |  |
|---|---|
| Stated as | Classifying any financial record |
| Stated as | The record's field set |
| Stated as | If it carries an FK to an L0 object and `ProcessedFlag`, it is an L1 schedule row |
| Stated as | `layer = SCHEDULE` |
| Stated as | Observed |

### 1 The Clause — [CON-R-003](../rules/CON-R-003.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Classifying any financial record: if it carries PostingDate and GL account slots and a counterparty FK, it is an L2 transaction.**

|  |  |
|---|---|
| Stated as | Classifying any financial record |
| Stated as | The record's field set |
| Stated as | If it carries `PostingDate` and GL account slots and a counterparty FK, it is an L2 transaction |
| Stated as | `layer = TRANSACTION` |
| Stated as | Observed |

### 1 The Clause — [CON-R-004](../rules/CON-R-004.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Classifying any financial record by its object name and field set: if the name is prefixed Virtual and it has no RevNumber/ModifiedByID/Firm-scope field, it is an L3 projection.**

|  |  |
|---|---|
| Stated as | Classifying any financial record |
| Stated as | The object name and field set |
| Stated as | If the name is prefixed `Virtual` and it has no `RevNumber`/`ModifiedByID`/Firm-scope field, it is an L3 projection |
| Stated as | `layer = PROJECTION` |
| Stated as | Observed |

### 1 The Clause — [CON-R-005](../rules/CON-R-005.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**An L0 clause is created or edited: its validity window is its own BeginDate..EndDate; a new RevNumber supersedes the prior revision.**

|  |  |
|---|---|
| Stated as | An L0 clause is created or edited |
| Stated as | `AmendmentID`, `BeginDate`, `EndDate`, `RevNumber` |
| Stated as | A clause's validity window is its own `BeginDate`..`EndDate`; a new `RevNumber` supersedes the prior revision |
| Stated as | Effective clause version for a date |
| Stated as | Derived |

### 1 The Clause — [CON-R-006](../rules/CON-R-006.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Operator invokes a generator command on the L0 clause and its modifiers: the generator materialises L1 rows spanning the clause window.**

|  |  |
|---|---|
| Stated as | Operator invokes a generator command |
| Stated as | The L0 clause + its modifiers |
| Stated as | The generator materialises L1 rows spanning the clause window |
| Stated as | N × L1 rows |
| Stated as | Observed (commands exist as `sTYPE_SUBMITBUTTON`) |

### 1 The Clause — [CON-R-007](../rules/CON-R-007.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**Operator invokes GENERATE_RENT (or a sibling): generate L2 transactions from every eligible L1 row where ProcessedFlag is false; set ProcessedFlag = true, ProcessedDate = now.**

|  |  |
|---|---|
| Stated as | Operator invokes `GENERATE_RENT` (or a sibling) |
| Stated as | L1 rows where `ProcessedFlag = false` |
| Stated as | Generate L2 transactions from each eligible row; set `ProcessedFlag = true`, `ProcessedDate = now` |
| Stated as | N × L2 rows |
| Stated as | Derived |

### 1 The Clause — [CON-R-008](../rules/CON-R-008.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Generation is requested: both ExpenseSetup.ReadyForPaymentFlag and ExpenseSchedule.ReadyForPaymentFlag must be true for the row to generate — the fields are observed, the exact gate semantics are inferred.**

|  |  |
|---|---|
| Stated as | Generation is requested |
| Stated as | `ExpenseSetup.ReadyForPaymentFlag`, `ExpenseSchedule.ReadyForPaymentFlag` |
| Stated as | Both must be true for the row to generate |
| Stated as | Gate result |
| Stated as | Observed (fields exist); gate semantics Inferred |

### 1 The Clause — [CON-R-009](../rules/CON-R-009.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Generation is requested: any HoldFlag = true anywhere in the L0→L1→L2 chain suppresses the row — though whether it prevents generation or merely marks the generated row held is unconfirmed.**

|  |  |
|---|---|
| Stated as | Generation is requested |
| Stated as | `HoldFlag` at L0, L1 and L2 |
| Stated as | Any `HoldFlag = true` in the chain suppresses the row |
| Stated as | Suppression |
| Stated as | Observed (fields); propagation Inferred |

### 1 The Clause — [CON-R-010](../rules/CON-R-010.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**Correcting generated output: the supported path is DELETE_PAYMENTS then GENERATE_RENT, not editing a posted transaction in place.**

|  |  |
|---|---|
| Stated as | Correcting generated output |
| Stated as | `DELETE_PAYMENTS`, then `GENERATE_RENT` |
| Stated as | The supported correction path is delete-then-regenerate, not in-place edit |
| Stated as | Rebuilt L2 set |
| Stated as | Derived |

### 1 The Clause — [CON-R-011](../rules/CON-R-011.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**An L2 row has left the system: a row carrying ExportBatchNumber, CheckNumber or CheckDate has been exported/settled — treat it as an immutability candidate, though enforcement is unverified.**

|  |  |
|---|---|
| Stated as | An L2 row has left the system |
| Stated as | `ExportBatchNumber`, `CheckNumber`, `CheckDate` |
| Stated as | A row carrying any of these has been exported/settled |
| Stated as | Immutability candidate |
| Stated as | Observed (fields); enforcement unverified |

### 1 The Clause — [CON-R-012](../rules/CON-R-012.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Reading an L3 projection: projections are computed, not authored; a tenant cannot customise them because no Firm-scope fields exist on any Virtual* object.**

|  |  |
|---|---|
| Stated as | Reading an L3 projection |
| Stated as | The L0 clause + L1 rows + reported facts |
| Stated as | Projections are computed, not authored; a tenant cannot customise them (no Firm-scope fields exist on any `Virtual*` object) |
| Stated as | Projection rows |
| Stated as | Observed |

### 1 The Clause — [CON-R-013](../rules/CON-R-013.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**An escalation step is materialised: L1 rows form a doubly-linked list; each row carries PreviousAnnualAmount/AnnualAmount/NextAnnualAmount.**

|  |  |
|---|---|
| Stated as | An escalation step is materialised |
| Stated as | `PreviousExpenseScheduleID`, `NextExpenseScheduleID` |
| Stated as | L1 rows form a doubly-linked list; each row carries `PreviousAnnualAmount`/`AnnualAmount`/`NextAnnualAmount` |
| Stated as | Auditable step chain |
| Stated as | Observed |

### 1 The Clause — [CON-R-014](../rules/CON-R-014.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**An L2 row is written: every transaction records SourceEntityTable and CodeSourceEntityID — which generator produced it.**

|  |  |
|---|---|
| Stated as | An L2 row is written |
| Stated as | `SourceEntityTable`, `CodeSourceEntityID` |
| Stated as | Every transaction records which generator produced it |
| Stated as | Provenance |
| Stated as | Observed |

### 2 Contract identity — [CON-R-015](../rules/CON-R-015.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**A contract is created: FacilityID, LocationID, OrganizationID and ProgramID key the contract to building, site, debiting org and portfolio.**

|  |  |
|---|---|
| Stated as | A contract is created |
| Stated as | `FacilityID`, `LocationID`, `OrganizationID`, `ProgramID` |
| Stated as | These four FKs key the contract to building, site, debiting org and portfolio |
| Stated as | Contract keys |
| Stated as | Observed |

### 2 Contract identity — [CON-R-016](../rules/CON-R-016.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**A contract is created: OrganizationID is 'where payments should be debited' in Lx's own field definition — it determines the GL debit side.**

|  |  |
|---|---|
| Stated as | A contract is created |
| Stated as | `OrganizationID` |
| Stated as | The organization is "where payments should be debited" — it determines the GL debit side |
| Stated as | GL routing |
| Stated as | Observed (Lx's own field definition, via 009) |

### 2 Contract identity — [CON-R-017](../rules/CON-R-017.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**A sublease is created: MasterContractID points at the master lease's ContractID; null means not a sublease.**

|  |  |
|---|---|
| Stated as | A sublease is created |
| Stated as | `MasterContractID` |
| Stated as | Points at the master lease's `ContractID`. Null ⇒ not a sublease |
| Stated as | Hierarchy edge |
| Stated as | Observed |

### 2 Contract identity — [CON-R-018](../rules/CON-R-018.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Traversing MasterContractID: no depth limit, no cycle guard, no role discriminator and no allocation percentage exist on the edge — the hierarchy is structurally unconstrained.**

|  |  |
|---|---|
| Stated as | Traversing `MasterContractID` |
| Stated as | The edge |
| Stated as | No depth limit, no cycle guard, no role discriminator and no allocation percentage exist on the edge |
| Stated as | Hierarchy is unconstrained |
| Stated as | Observed (by absence) |

### 2 Contract identity — [CON-R-019](../rules/CON-R-019.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Determining payable vs receivable: direction is carried on ExpenseSetup.IsReceivable and PaymentTransaction.IsReceivable, not on the contract, so one contract can be both.**

|  |  |
|---|---|
| Stated as | Determining payable vs receivable |
| Stated as | `ExpenseSetup.IsReceivable`, `PaymentTransaction.IsReceivable` |
| Stated as | Direction is carried per-clause and per-transaction, not on the contract. One contract may be both |
| Stated as | Money direction |
| Stated as | Observed |

### 2 Contract identity — [CON-R-020](../rules/CON-R-020.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**Resolving a contract's vendors: Contract has no vendor FK; the set is derived from PaymentTransaction.VendorID, ExpenseSetup.VendorID, ExpenseVendorAllocation.VendorID, ScheduledOffset.VendorID, LandlordInvoice.EmployerID and SecurityDeposit.PartyID.**

|  |  |
|---|---|
| Stated as | Resolving a contract's vendors |
| Stated as | `PaymentTransaction.VendorID`, `ExpenseSetup.VendorID`, `ExpenseVendorAllocation.VendorID`, `ScheduledOffset.VendorID`, `LandlordInvoice.EmployerID`, `SecurityDeposit.PartyID` |
| Stated as | `Contract` has no vendor FK; the set is derived from children |
| Stated as | Derived vendor set |
| Stated as | Observed |

### 2 Contract identity — [CON-R-021](../rules/CON-R-021.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Resolving a 'Vendor': VendorID's declared type is Employer ID — Vendor is a relabelled Employer, not a distinct entity.**

|  |  |
|---|---|
| Stated as | Resolving a "Vendor" |
| Stated as | `VendorID` declared type |
| Stated as | `Vendor` is a relabelled `Employer`; `VendorID` has declared type `Employer ID` |
| Stated as | Employer record |
| Stated as | Observed (009) |

### 2 Contract identity — [CON-R-022](../rules/CON-R-022.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**Determining the discount rate: look up DiscountRate by accounting method + contract use + geography + a min/max-scheduled-months band, and stamp it onto Contract.DiscountRate.**

|  |  |
|---|---|
| Stated as | Determining the discount rate |
| Stated as | `CodeAccountingMethodID`, `CodeContractUseID`, geography, schedule length |
| Stated as | Look up `DiscountRate` by method + use + country/state + `MinSchedMons`..`MaxSchedMons` band; stamp onto `Contract.DiscountRate` |
| Stated as | Discount rate |
| Stated as | Derived |

### 2 Contract identity — [CON-R-023](../rules/CON-R-023.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Determining the fiscal calendar: the calendar is owned by Contract.ProgramID (the portfolio), not by the firm.**

|  |  |
|---|---|
| Stated as | Determining the fiscal calendar |
| Stated as | `Contract.ProgramID` → `FiscalPeriod.ProgramID` |
| Stated as | The fiscal calendar is owned by the portfolio, not the firm |
| Stated as | Period definitions |
| Stated as | Observed |

### 2 Contract identity — [CON-R-024](../rules/CON-R-024.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**A retail fiscal period is used: periods may be 4 or 5 weeks (retail 4-5-4), not calendar months, per FiscalPeriod.Is4or5WeekPeriod.**

|  |  |
|---|---|
| Stated as | A retail fiscal period is used |
| Stated as | `FiscalPeriod.Is4or5WeekPeriod`, `NumberWeeksInPeriod`, `NumberDaysInPeriod` |
| Stated as | Periods may be 4 or 5 weeks (retail 4-5-4), not calendar months |
| Stated as | Period length |
| Stated as | Observed |

### 2 Contract identity — [CON-R-025](../rules/CON-R-025.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Computing rent rollups: 120 denormalised sTYPE_MONEY fields on Contract cross {Calendar,Fiscal}×{Base,Total}×{with,without tax}×{period buckets}.**

|  |  |
|---|---|
| Stated as | Computing rent rollups |
| Stated as | `ExpenseSchedule` rows |
| Stated as | 120 denormalised `sTYPE_MONEY` fields on `Contract` across `{Calendar, Fiscal} × {Base, Total} × {with, without tax} × {Aggregate, Current Annual/Monthly/Period, Next, 3rd–6th, Beyond 5th/6th, Remaining Obligation, Q1–Q4}` |
| Stated as | Precomputed rollups |
| Stated as | Observed |

### 2 Contract identity — [CON-R-026](../rules/CON-R-026.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**Any rollup is read: the rollups are denormalised and can be stale — Contract carries no recalculation flag equivalent to SLSummary's.**

|  |  |
|---|---|
| Stated as | Any rollup is read |
| Stated as | — |
| Stated as | The rollups are denormalised and can be stale; `SLSummary` has explicit `NeedsRecalculation`/`RecalcTriggerDate`, `Contract` has no equivalent |
| Stated as | Staleness risk |
| Stated as | Derived |

### 2 Contract identity — [CON-R-027](../rules/CON-R-027.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**Applying contract-level tax: four parallel tax components; each ExpenseSetup opts in per component, producing CalculatedTaxRate1..4 on the schedule.**

|  |  |
|---|---|
| Stated as | Applying contract-level tax |
| Stated as | `Contract.ContractTaxRate1..4`, `ExpenseSetup.ApplyTax1..4Flag` |
| Stated as | Four parallel tax components; each expense clause opts in per component |
| Stated as | `CalculatedTaxRate1..4` on the schedule |
| Stated as | Derived |

### 2 Contract identity — [CON-R-028](../rules/CON-R-028.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**A contract term option is created: the Terms Wizard generates N ContractTerm rows of a stated length from a stated start.**

|  |  |
|---|---|
| Stated as | A contract term option is created |
| Stated as | `ContractTermWizard_TermLength`, `_OptionNumber`, `_TermCoverageBeginDate`, `GenerateContractTerms` |
| Stated as | Generates N `ContractTerm` rows of the stated length from the stated start |
| Stated as | N × `ContractTerm` |
| Stated as | Observed |

### 2 Contract identity — [CON-R-029](../rules/CON-R-029.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Accruing over an option term: only terms flagged IncludeTermForAccruals participate in accrual schedules.**

|  |  |
|---|---|
| Stated as | Accruing over an option term |
| Stated as | `ContractTerm.IncludeTermForAccruals` |
| Stated as | Only terms flagged true participate in accrual schedules |
| Stated as | Accrual scope |
| Stated as | Observed |

### 3 Recurring expense — [CON-R-030](../rules/CON-R-030.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Authoring a recurring expense through the wizard: the wizard's start date, end date, starting amount, amount type and escalation settings materialise ExpenseSetup + ExpenseEscalation + the full ExpenseSchedule in one action.**

|  |  |
|---|---|
| Stated as | Authoring a recurring expense |
| Stated as | `ExpenseSetupWizard_StartDate`, `_EndDate`, `_StartingAmout`, `_AmountType`, `_TypeOfEscalation`, `_EscalateEvery`, `_EscalateAmountRate`, `GenerateExpenseSetup` |
| Stated as | The wizard materialises `ExpenseSetup` + `ExpenseEscalation` + the full `ExpenseSchedule` |
| Stated as | Clause + schedule |
| Stated as | Observed |

### 3 Recurring expense — [CON-R-031](../rules/CON-R-031.md)

*Inferred · rule · source: `docs/modules/contracts/rules.md`*

**The wizard's 'Find Starting Amount' checkbox is set: work backwards from a known later amount and the escalation rule to derive the starting amount — useful for abstracting a lease mid-term.**

|  |  |
|---|---|
| Stated as | `ExpenseSetupWizard_FindStartingAmout = true` |
| Stated as | A known later amount + the escalation rule |
| Stated as | Work backwards to derive the starting amount |
| Stated as | Starting amount |
| Stated as | Inferred (from the label "Find Starting Amount") |

### 3 Recurring expense — [CON-R-032](../rules/CON-R-032.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**Determining billing frequency: CodeFrequencyID, NumberOfPayments and PaymentDueDay drive the number and spacing of ExpenseSchedule rows.**

|  |  |
|---|---|
| Stated as | Determining billing frequency |
| Stated as | `ExpenseSetup.CodeFrequencyID`, `NumberOfPayments`, `PaymentDueDay` |
| Stated as | Drives the number and spacing of `ExpenseSchedule` rows |
| Stated as | Period grid |
| Stated as | Derived |

### 3 Recurring expense — [CON-R-033](../rules/CON-R-033.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**The clause is flagged IsCustomPaymentCoverage: the same ExpenseSetup record supports annual, quarterly or semi-annual coverage without a schema change, via explicit month-and-day markers per frequency.**

|  |  |
|---|---|
| Stated as | `ExpenseSetup.IsCustomPaymentCoverage = true` |
| Stated as | `CoverageBeginAnnual`, `CoverageBeginQ1..Q4`, `CoverageBeginSemiAnnual1..2`, `PaymentDueAnnual`, `PaymentDueQ1..Q4`, `PaymentDueSemiAnnual1..2` |
| Stated as | The same setup record supports annual, quarterly or semi-annual coverage without schema change; explicit month-and-day markers per frequency |
| Stated as | Coverage/due grid |
| Stated as | Observed |

### 3 Recurring expense — [CON-R-034](../rules/CON-R-034.md)

*Inferred · rule · source: `docs/modules/contracts/rules.md`*

**The clause is flagged IsPayArrears: payment is due after the coverage period rather than in advance.**

|  |  |
|---|---|
| Stated as | `ExpenseSetup.IsPayArrears = true` |
| Stated as | The coverage window |
| Stated as | Payment is due after the coverage period rather than in advance |
| Stated as | Due-date shift |
| Stated as | Inferred (from the label "Pay in Arrears?") |

### 3 Recurring expense — [CON-R-035](../rules/CON-R-035.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**The clause is flagged IsDailyRent: the period amount is the daily rate multiplied by the day count in the period, rather than a fixed period amount.**

|  |  |
|---|---|
| Stated as | `ExpenseSetup.IsDailyRent = true` |
| Stated as | `ExpenseSchedule.DailyRentRate`, period day count |
| Stated as | Amount = daily rate × days in period, rather than a fixed period amount |
| Stated as | Period amount |
| Stated as | Derived |

### 3 Recurring expense — [CON-R-036](../rules/CON-R-036.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**A partial first or last period occurs: CodeProrationMethodID governs it, and the schedule's own FirstPaymentAmount / LastPaymentAmount carry the prorated stub amounts.**

|  |  |
|---|---|
| Stated as | A partial first or last period |
| Stated as | `CodeProrationMethodID`, `ExpenseSchedule.FirstPaymentAmount`, `LastPaymentAmount` |
| Stated as | Stub periods carry their own prorated amounts |
| Stated as | Stub amounts |
| Stated as | Observed |

### 3 Recurring expense — [CON-R-037](../rules/CON-R-037.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**CalculateScheduleAmounts is invoked: the schedule's amounts are recomputed in place from the clause, its escalation and its tax configuration.**

|  |  |
|---|---|
| Stated as | `CalculateScheduleAmounts` is invoked |
| Stated as | The `ExpenseSetup` + its escalation + tax config |
| Stated as | Recomputes the schedule's amounts in place |
| Stated as | Updated L1 rows |
| Stated as | Observed |

### 3 Recurring expense — [CON-R-038](../rules/CON-R-038.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**An expense is split across organizations: ExpenseAllocation apportions one clause across organizations by percentage.**

|  |  |
|---|---|
| Stated as | Splitting an expense across orgs |
| Stated as | `ExpenseAllocation.OrganizationID`, `.AllocationPercentage`, `.ExpenseSetupID` |
| Stated as | Allocates one clause across organizations by percentage |
| Stated as | Allocation set |
| Stated as | Observed |

### 3 Recurring expense — [CON-R-039](../rules/CON-R-039.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**An expense is split across vendors: ExpenseVendorAllocation apportions one clause's payments across vendors by percentage; CHANGE_EXPENSE_ALLOCATION_VENDOR rewrites it.**

|  |  |
|---|---|
| Stated as | Splitting an expense across vendors |
| Stated as | `ExpenseVendorAllocation.VendorID`, `.PaymentPercentage`, `.APVendorNumber`, `.ExpenseSetupID` |
| Stated as | Allocates one clause's payments across vendors by percentage; `CHANGE_EXPENSE_ALLOCATION_VENDOR` rewrites it |
| Stated as | Vendor allocation set |
| Stated as | Observed |

### 4 Escalations — [CON-R-040](../rules/CON-R-040.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**An escalation step falls due: a step occurs every EscalationPeriod × CodeFrequencyID units inside the clause's BeginDate..EndDate window.**

|  |  |
|---|---|
| Stated as | An escalation step falls due |
| Stated as | `ExpenseEscalation.EscalationPeriod`, `CodeFrequencyID`, `BeginDate`, `EndDate` |
| Stated as | A step occurs every `EscalationPeriod` × frequency units inside the window |
| Stated as | Step dates |
| Stated as | Derived |

### 4 Escalations — [CON-R-041](../rules/CON-R-041.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**The driver is fixed: new amount = f(base or current amount, FixedAmount, EscalationMethod) — but EscalationMethod is free text, so its value space is unknown.**

|  |  |
|---|---|
| Stated as | The driver is fixed |
| Stated as | `CodeEscalationTypeID`, `EscalationMethod(Text)`, `FixedAmount`, `BaseAmount` |
| Stated as | New amount = f(base or current, `FixedAmount`, `EscalationMethod`). `EscalationMethod` is free text — its value space is unknown |
| Stated as | New amount |
| Stated as | Observed (fields); formula Inferred |

### 4 Escalations — [CON-R-042](../rules/CON-R-042.md)

*Inferred · rule · source: `docs/modules/contracts/rules.md`*

**The driver is index-based: rawChange = (IndexAmount / IndexBaseFactor) − 1 — assumes IndexAmount is a level, which is unconfirmed.**

|  |  |
|---|---|
| Stated as | The driver is index-based |
| Stated as | `EscalationIndexID` → `EscalationIndex.IndexAmount`, `IndexBaseFactor` |
| Stated as | `rawChange = (IndexAmount / IndexBaseFactor) − 1` |
| Stated as | Raw index change |
| Stated as | Inferred — depends on whether `IndexAmount` is a level or a rate (open) |

### 4 Escalations — [CON-R-043](../rules/CON-R-043.md)

*Inferred · rule · source: `docs/modules/contracts/rules.md`*

**An index change is applied: applied = rawChange × ExpenseSetup.CPIMultiplier.**

|  |  |
|---|---|
| Stated as | An index change is applied |
| Stated as | `ExpenseSetup.CPIMultiplier` |
| Stated as | `applied = rawChange × CPIMultiplier` |
| Stated as | Applied change |
| Stated as | Inferred |

### 4 Escalations — [CON-R-044](../rules/CON-R-044.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**A per-step collar exists: collared = clamp(applied, PeriodMinPercentage, PeriodMaxPercentage).**

|  |  |
|---|---|
| Stated as | A per-step collar exists |
| Stated as | `PeriodMinPercentage`, `PeriodMaxPercentage` |
| Stated as | `collared = clamp(applied, min, max)` |
| Stated as | Collared change |
| Stated as | Derived |

### 4 Escalations — [CON-R-045](../rules/CON-R-045.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**ExpenseSetup.IsCPICompounding is set: true escalates from the current amount; false escalates from BaseAmount.**

|  |  |
|---|---|
| Stated as | `ExpenseSetup.IsCPICompounding` |
| Stated as | The flag |
| Stated as | `true` ⇒ escalate from the current amount; `false` ⇒ from `BaseAmount` |
| Stated as | Escalation base |
| Stated as | Derived |

### 4 Escalations — [CON-R-046](../rules/CON-R-046.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**A lifetime collar exists: cumulative change across all steps is clamped by LifetimeMinPercentage/LifetimeMaxPercentage.**

|  |  |
|---|---|
| Stated as | A lifetime collar exists |
| Stated as | `LifetimeMinPercentage`, `LifetimeMaxPercentage` |
| Stated as | Cumulative change across all steps is clamped |
| Stated as | Cumulative bound |
| Stated as | Derived |

### 4 Escalations — [CON-R-047](../rules/CON-R-047.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**An absolute ceiling exists: CapAmount/CapPercentage cap the escalated amount absolutely; order versus the collar above is unknown.**

|  |  |
|---|---|
| Stated as | An absolute ceiling exists |
| Stated as | `CapAmount`, `CapPercentage` |
| Stated as | The escalated amount is capped absolutely |
| Stated as | Capped amount |
| Stated as | Observed (fields); order vs collar unknown |

### 4 Escalations — [CON-R-048](../rules/CON-R-048.md)

*Inferred · rule · source: `docs/modules/contracts/rules.md`*

**An expense stop exists: cost above StopAmount transfers to the tenant rather than continuing to escalate.**

|  |  |
|---|---|
| Stated as | An expense stop exists |
| Stated as | `StopAmount` |
| Stated as | Cost above `StopAmount` transfers rather than escalating |
| Stated as | Stop behaviour |
| Stated as | Inferred |

### 4 Escalations — [CON-R-049](../rules/CON-R-049.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Increase/decrease asymmetry: ExpenseSetup.AmountIncreaseCap/AmountDecreaseCap/PercentIncreaseCap/PercentDecreaseCap are a separate, parallel collar to ExpenseEscalation's own min/max, with unspecified precedence between the two.**

|  |  |
|---|---|
| Stated as | Increase/decrease asymmetry |
| Stated as | `ExpenseSetup.AmountIncreaseCap`, `AmountDecreaseCap`, `PercentIncreaseCap`, `PercentDecreaseCap` |
| Stated as | Separate caps for upward and downward movement, in addition to `ExpenseEscalation`'s min/max. Precedence unspecified |
| Stated as | Bounded amount |
| Stated as | Observed |

### Step 0 the two — [CON-R-050](../rules/CON-R-050.md)

*Observed · rule · source: `docs/modules/contracts/percentage-rent.md`*

**A percentage-rent period is projected: two independent date windows are produced — ReportingBucket{Begin,End,Due}Date and BillingBucket{Begin,End,Due}Date.**

### Step 1 gross sales — [CON-R-051](../rules/CON-R-051.md)

*Observed · rule · source: `docs/modules/contracts/percentage-rent.md`*

**Sales are reported: GrossSalesPeriodAmount sums Sales.GrossSalesAmount over the sales period; GrossSalesPeriodCount does the same for unit counts.**

### Step 2 exclusions — [CON-R-052](../rules/CON-R-052.md)

*Derived · rule · source: `docs/modules/contracts/percentage-rent.md`*

**An exclusion applies: rawExcluded = salesOfType × SalesExclusion.ExclusionRate.**

|  |  |
|---|---|
| Stated as | `SalesExclusionCap` field |
| Stated as | Meaning |
| Stated as | `PRPGrossSalesAmount` |
| Stated as | Gross sales in the percentage-rent period, for the cap's percentage basis |
| Stated as | `PRPGrossExcludedAmount` |
| Stated as | Σ of raw excluded amounts in this cap group, before the cap |

### 5 Percentage rent — [CON-R-053](../rules/CON-R-053.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**Exclusions share a cap group (ExclusionGroupCapID): PRPGrossExcludedAmount sums the raw excluded amounts within the group, before the cap.**

|  |  |
|---|---|
| Stated as | Exclusions share a cap group |
| Stated as | `SalesExclusion.ExclusionGroupCapID` → `SalesExclusionCap` |
| Stated as | `PRPGrossExcludedAmount = Σ rawExcluded` in the group |
| Stated as | Pre-cap total |
| Stated as | Derived |

### 5 Percentage rent — [CON-R-054](../rules/CON-R-054.md)

*Inferred · rule · source: `docs/modules/contracts/rules.md`*

**A cap group is evaluated: PRPComputedCapAmount = min(CapAmount, PRPGrossSalesAmount × CapPercent) — the effective cap, whichever binds first.**

|  |  |
|---|---|
| Stated as | A cap group is evaluated |
| Stated as | `SalesExclusionCap.CapAmount`, `.CapPercent`, `.PRPGrossSalesAmount` |
| Stated as | `PRPComputedCapAmount = min(CapAmount, PRPGrossSalesAmount × CapPercent)` |
| Stated as | Effective cap |
| Stated as | Inferred |

### 5 Percentage rent — [CON-R-055](../rules/CON-R-055.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**The cap is applied: PRPNetExcludedAmount = min(gross, cap); PRPExcessExcludedAmount = gross − net — and the platform stores both numbers, which is what makes the min() reading solid rather than speculative.**

|  |  |
|---|---|
| Stated as | The cap is applied |
| Stated as | `PRPGrossExcludedAmount`, `PRPComputedCapAmount` |
| Stated as | `PRPNetExcludedAmount = min(gross, cap)`; `PRPExcessExcludedAmount = gross − net` |
| Stated as | Allowed / disallowed exclusion |
| Stated as | Derived (both fields exist as separate stored values) |

### 5 Percentage rent — [CON-R-056](../rules/CON-R-056.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**Net sales are computed: NetSalesPeriodAmount = GrossSalesPeriodAmount − ExcludedSalesPeriodAmount.**

|  |  |
|---|---|
| Stated as | Net sales are computed |
| Stated as | Gross sales, `ExcludedSalesPeriodAmount` |
| Stated as | `NetSalesPeriodAmount = GrossSalesPeriodAmount − ExcludedSalesPeriodAmount`; likewise counts |
| Stated as | Net sales |
| Stated as | Derived |

### 5 Percentage rent — [CON-R-057](../rules/CON-R-057.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**Sales periods roll into a rent period: PRPSalesAmount sums NetSalesPeriodAmount over every sales period inside the billing bucket.**

|  |  |
|---|---|
| Stated as | Sales periods roll into a rent period |
| Stated as | Net sales per sales period, `BillingBucket{Begin,End}Date` |
| Stated as | `PRPSalesAmount = Σ NetSalesPeriodAmount` inside the billing bucket |
| Stated as | Rent-period sales |
| Stated as | Derived |

### Step 4 the eight — [CON-R-058](../rules/CON-R-058.md)

*Derived · rule · source: `docs/modules/contracts/percentage-rent.md`*

**A percentage-rent period is tiered: PRPSalesPastBreakpoint_N is computed for each of 8 tiers from PRPBreakpointAmount1..8 (or BreakpointCount1..8 under UseCountBasedRate) — assumed to be a marginal band reading, though a simple-excess reading is also grammatically possible.**

|  |  |
|---|---|
| Stated as | Reading |
| Stated as | Formula |
| Stated as | Consequence |
| Stated as | (a) marginal band (assumed) |
| Stated as | `clamp(PRPSalesAmount, BP_N, BP_{N+1}) − BP_N`, with `BP_9 = ∞` |
| Stated as | Σ of tier rents is the standard tiered result; rates are marginal |

### 5 Percentage rent — [CON-R-059](../rules/CON-R-059.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**Tier rent is computed: PRPBreakpointRentDue_N = past_N × rate_N; PRPBreakpointRent = the sum across all eight tiers.**

|  |  |
|---|---|
| Stated as | Tier rent is computed |
| Stated as | `PRPSalesPastBreakpoint_N`, `PRPBreakpointRate_N` |
| Stated as | `PRPBreakpointRentDue_N = past_N × rate_N`; `PRPBreakpointRent = Σ` |
| Stated as | Tier rent |
| Stated as | Derived |

### Step 5 cap and floor — [CON-R-060](../rules/CON-R-060.md)

*Derived · rule · source: `docs/modules/contracts/percentage-rent.md`*

**Cap and floor are applied: PRPCapFloorAdjustedRent = clamp(PRPBreakpointRent, BillingBucketFloorAmount, BillingBucketCapAmount).**

### Step 6 offsets — [CON-R-061](../rules/CON-R-061.md)

*Observed · rule · source: `docs/modules/contracts/percentage-rent.md`*

**Offsets are applied: VariableRentOffset and ScheduledOffset, applied via APPLY_OFFSETS, reduce the rent-year obligation.**

|  |  |
|---|---|
| Stated as | Field |
| Stated as | Role |
| Stated as | `RentYearBeginDate` / `RentYearEndDate` |
| Stated as | The rent year, per `RentYearStartMonth` |
| Stated as | `RentYearHasAltRent(Boolean)` |
| Stated as | An `AlternateRentSchedule` window overlaps this rent year |

### Step 7 rent due and — [CON-R-062](../rules/CON-R-062.md)

*Inferred · rule · source: `docs/modules/contracts/percentage-rent.md`*

**Rent already paid is credited: PRPRentDue = PRPTotalRent − SalesPeriodRentPaid − offsets.**

|  |  |
|---|---|
| Stated as | Computed |
| Stated as | Posted |
| Stated as | `AccrualAmountThisPeriod` |
| Stated as | `PostedAccrualAmountThisPeriod` |
| Stated as | `AccrualAmountPriorPeriods` |
| Stated as | `PostedAccrualAmountPriorPeriods` |

### 5 Percentage rent — [CON-R-063](../rules/CON-R-063.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**Percentage rent is billed: a PaymentTransaction carrying PercentageRentID is generated for PRPRentDue.**

|  |  |
|---|---|
| Stated as | Percentage rent is billed |
| Stated as | `PRPRentDue`, `PercentageRent.CodeExpenseTypeID`/`CodeExpenseGroupID` |
| Stated as | A `PaymentTransaction` carrying `PercentageRentID` is generated |
| Stated as | L2 row |
| Stated as | Derived |

### 5 Percentage rent — [CON-R-064](../rules/CON-R-064.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**NaturalBreakpointFlag is set: naturalBreakpoint = annualMinimumRent / NaturalBreakpointRate — see the breakpoint entity above for why the numerator is unresolved.**

|  |  |
|---|---|
| Stated as | `NaturalBreakpointFlag = true` |
| Stated as | `NaturalBreakpointRate`, the contract's annual minimum rent |
| Stated as | `naturalBreakpoint = annualMinimumRent / NaturalBreakpointRate`. The numerator source is unconfirmed |
| Stated as | Derived tier-1 threshold |
| Stated as | Inferred |

### 5 Percentage rent — [CON-R-065](../rules/CON-R-065.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**A natural breakpoint is derived: the configured rate and the effective rate are stored separately as the derivation's own audit trail.**

|  |  |
|---|---|
| Stated as | A natural breakpoint is derived |
| Stated as | `ConfiguredBreakpointRate1` vs `BreakpointRate1` on `VirtualPercentageRentPeriod` |
| Stated as | The configured rate and the effective rate are stored separately as the derivation's audit trail |
| Stated as | Audit pair |
| Stated as | Observed |

### 5 Percentage rent — [CON-R-066](../rules/CON-R-066.md)

*Inferred · rule · source: `docs/modules/contracts/rules.md`*

**UseTrailing12MonthSales is set: replace the bucket sum with a rolling 12-month sum, scaled by TrailingSalesMultiplier for a partial history.**

|  |  |
|---|---|
| Stated as | `UseTrailing12MonthSales = true` |
| Stated as | `TrailingSalesMultiplier`, rolling 12-month sales |
| Stated as | Replace the bucket sum with a rolling 12-month window, scaled by the multiplier for partial history |
| Stated as | Trailing sales |
| Stated as | Inferred |

### 5 Percentage rent — [CON-R-067](../rules/CON-R-067.md)

*Inferred · rule · source: `docs/modules/contracts/rules.md`*

**AnnualizeRent is set: scale a partial period's sales up to a full year, tier it, then scale the resulting rent back down.**

|  |  |
|---|---|
| Stated as | `AnnualizeRent = true` |
| Stated as | Partial-period sales, period length |
| Stated as | Scale sales to a full year, tier, then scale the rent back |
| Stated as | Annualised rent |
| Stated as | Inferred |

### 5 Percentage rent — [CON-R-068](../rules/CON-R-068.md)

*Inferred · rule · source: `docs/modules/contracts/rules.md`*

**CumulativeFlag is set: accumulate year-to-date sales and rent, crediting rent already billed, instead of treating each period independently.**

|  |  |
|---|---|
| Stated as | `CumulativeFlag = true` |
| Stated as | Year-to-date sales and rent billed |
| Stated as | Accumulate YTD and credit rent already billed rather than treating each period independently |
| Stated as | Cumulative rent |
| Stated as | Inferred |

### 5 Percentage rent — [CON-R-069](../rules/CON-R-069.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**A percentage-rent clause is flagged ExtFinalPeriodToLeaseExpDt: the final period extends to lease expiry instead of truncating at the usual period boundary.**

|  |  |
|---|---|
| Stated as | `ExtFinalPeriodToLeaseExpDt = true` |
| Stated as | `Contract.ExpireDate` |
| Stated as | The final percentage-rent period extends to lease expiry rather than truncating at the period boundary |
| Stated as | Final period end |
| Stated as | Observed (label) |

### 6 Alternate rent and — [CON-R-070](../rules/CON-R-070.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**An AlternateRentSchedule window is active: a substitute rent formula (CodeAltRentMathID, PercentRentRate) replaces the normal one for the window.**

|  |  |
|---|---|
| Stated as | An `AlternateRentSchedule` window is active |
| Stated as | `BeginDate`, `EndDate`, `CodeAltRentMathID`, `PercentRentRate` |
| Stated as | A substitute rent formula replaces the normal one for the window |
| Stated as | Alternate rent |
| Stated as | Observed |

### 6 Alternate rent and — [CON-R-071](../rules/CON-R-071.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Alternate rent begins: SetExpHoldFlag, SetPRHoldFlag and SuspendSL hold the expense schedule, hold percentage rent, and suspend straight-line accounting — though what releases the holds afterward is not observed.**

|  |  |
|---|---|
| Stated as | Alternate rent begins |
| Stated as | `SetExpHoldFlag`, `SetPRHoldFlag`, `SuspendSL` |
| Stated as | Holds the expense schedule, holds percentage rent, suspends straight-line accounting |
| Stated as | Three suppressions |
| Stated as | Observed (fields); release mechanism unknown |

### 6 Alternate rent and — [CON-R-072](../rules/CON-R-072.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**A payment is generated under alternate rent: PreAltRentInvoiceAmount records what would have been invoiced without the concession.**

|  |  |
|---|---|
| Stated as | A payment is generated under alternate rent |
| Stated as | `PaymentTransaction.InAlternateRent`, `.AlternateRentScheduleID`, `.PreAltRentInvoiceAmount` |
| Stated as | Records what would have been invoiced without the concession |
| Stated as | Concession audit trail |
| Stated as | Observed |

### 6 Alternate rent and — [CON-R-073](../rules/CON-R-073.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Alternate rent applies: ExpenseReductionAmount / ExpenseReductionPercent reduce the fixed expense side as well as the variable side.**

|  |  |
|---|---|
| Stated as | Alternate rent reduces expenses |
| Stated as | `ExpenseReductionAmount`, `ExpenseReductionPercent` |
| Stated as | Reduces the fixed expense side as well as the variable |
| Stated as | Reduced expense |
| Stated as | Observed |

### 6 Alternate rent and — [CON-R-074](../rules/CON-R-074.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**PRDeductExclusions is set: governs whether sales exclusions still apply under the alternate-rent formula.**

|  |  |
|---|---|
| Stated as | `PRDeductExclusions` is set |
| Stated as | The flag |
| Stated as | Determines whether sales exclusions still apply under alternate rent |
| Stated as | Exclusion behaviour |
| Stated as | Observed (field); semantics Inferred |

### 6 Alternate rent and — [CON-R-075](../rules/CON-R-075.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**A VariableRentOffset applies: percentage rent is reduced by amounts paid in a named expense group/type, subject to its own cap.**

|  |  |
|---|---|
| Stated as | A `VariableRentOffset` applies |
| Stated as | `CodeOffsetGroupID`, `CodeOffsetTypeID`, `CodePRAggregateExpGroupID`, `CodePRAggregateExpTypeID`, `FixedOffsetAmount`, `CapAmount`, `CapPercent` |
| Stated as | Reduce percentage rent by amounts paid in a named expense group/type, subject to its own cap |
| Stated as | Offset amount |
| Stated as | Derived |

### 6 Alternate rent and — [CON-R-076](../rules/CON-R-076.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**A ScheduledOffset is drawn down: a landlord credit (TotalAmount, CapAmountPerMonth) is drawn down over time against named expense group/types, via APPLY_OFFSETS.**

|  |  |
|---|---|
| Stated as | A `ScheduledOffset` is drawn down |
| Stated as | `TotalAmount`, `CapAmountPerMonth`, `CapPercent`, `AmountAllocated`, `AmountNotAllocated`, `LinkSchedOffsetExpGrpType`, `APPLY_OFFSETS` |
| Stated as | A landlord credit is drawn down over time, capped per month, against named expense group/types |
| Stated as | Draw-down |
| Stated as | Derived |

### 7 Use based rent — [CON-R-077](../rules/CON-R-077.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**Usage-based rent is computed: structurally identical to the percentage-rent tiering with Sales→Usage and PRP→UBRP; the tier value is a unit cost, not a percentage rate.**

|  |  |
|---|---|
| Stated as | Usage-based rent is computed |
| Stated as | `Usage.UsageCount`, `.UsageShare`, `UseBasedRentBreakpoint.BreakpointCount1..8`, `.BreakpointCost1..8` |
| Stated as | Structurally identical to `CON-R-050`…`CON-R-063` with `Sales`→`Usage` and `PRP`→`UBRP`. Tier value is a unit cost, not a percentage rate |
| Stated as | `UBRPRentDue`, `UBRPTotalRent` |
| Stated as | Derived (field-for-field mirror confirmed) |

### 7 Use based rent — [CON-R-078](../rules/CON-R-078.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Unit rates are stored: usage unit costs carry 6 decimal places (sTYPE_NUMBER_FRACTION6DIGITS); usage counts carry 5 — precision loss here is a direct Constitution §4.4 violation if implemented with floating point.**

|  |  |
|---|---|
| Stated as | Unit rates are stored |
| Stated as | `sTYPE_NUMBER_FRACTION6DIGITS`, `5-Digit Number` |
| Stated as | Usage unit costs carry 6 decimal places; usage counts 5. Precision loss here is a direct §4.4 violation |
| Stated as | Precision requirement |
| Stated as | Observed |

### 7 Use based rent — [CON-R-079](../rules/CON-R-079.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**A use-rent model is selected: CodeUseRentModelTypeID selects the variant; its members are unknown.**

|  |  |
|---|---|
| Stated as | A use-rent model is selected |
| Stated as | `CodeUseRentModelTypeID` |
| Stated as | Selects the usage rent variant. Members unknown |
| Stated as | Model variant |
| Stated as | Observed |

### The waterfall — [CON-R-080](../rules/CON-R-080.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**A recovery statement is valued: ST1 = C + NC − D — the recoverable pool, literally labelled 'Sub Total #1 (C+NC-D)'.**

|  |  |
|---|---|
| Stated as | A recovery statement is valued |
| Stated as | `{P}ControllableExpenses{G/N}`, `{P}NonControllableExpenses{G/N}`, `{P}Deductions{G/N}` |
| Stated as | `ST1 = C + NC − D` |
| Stated as | `{P}SubTotal1{G/N}` |
| Stated as | Observed — label `Sub Total #1 (C+NC-D)` |

### The waterfall — [CON-R-081](../rules/CON-R-081.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**An admin-fee rate exists: AdminFeePercentageAmount = SubTotal1 × AdminFeePercentage.**

|  |  |
|---|---|
| Stated as | An admin-fee rate exists |
| Stated as | `{P}SubTotal1`, `{P}AdminFeePercentage` |
| Stated as | `AF%amt = ST1 × AF%` |
| Stated as | `{P}AdminFeePercentageAmount{G/N}` |
| Stated as | Derived |

### The waterfall — [CON-R-082](../rules/CON-R-082.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Fees and additions are added: PassThrough = ST1 + AF%amt + AdministrationFees + Additions — labelled 'Pass-Through (ST1+AF%+AF+A)'.**

|  |  |
|---|---|
| Stated as | Fees and additions are added |
| Stated as | `ST1`, `AF%amt`, `{P}AdministrationFees`, `{P}Additions` |
| Stated as | `PT = ST1 + AF%amt + AF + A` |
| Stated as | `{P}PassThrough{G/N}` |
| Stated as | Observed — label `Pass-Through (ST1+AF%+AF+A)` |

### The waterfall — [CON-R-083](../rules/CON-R-083.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Other recoveries are netted: SubTotal2 = PassThrough − Recoveries — labelled 'Sub Total #2 (PT-R)'.**

|  |  |
|---|---|
| Stated as | Other recoveries are netted |
| Stated as | `PT`, `{P}Recoveries{G/N}` |
| Stated as | `ST2 = PT − R` |
| Stated as | `{P}SubTotal2{G/N}` |
| Stated as | Observed — label `Sub Total #2 (PT-R)` |

### The waterfall — [CON-R-084](../rules/CON-R-084.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**The tenant's share is taken: NetPassThrough = SubTotal2 × ProRataShareRate — labelled 'Net Pass-Through (ST2*PRR)'.**

|  |  |
|---|---|
| Stated as | The tenant's share is taken |
| Stated as | `ST2`, `{P}ProRataShareRate` |
| Stated as | `NPT = ST2 × PRR` |
| Stated as | `{P}NetPassThrough{G/N}` |
| Stated as | Observed — label `Net Pass-Through (ST2*PRR)` |

### The waterfall — [CON-R-085](../rules/CON-R-085.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Escrow already paid is credited: NetAmountDue = NetPassThrough − PrePaidAmount — labelled 'Net Amount Due (NPT-PP)'.**

|  |  |
|---|---|
| Stated as | Escrow is credited |
| Stated as | `NPT`, `{P}PrePaidAmount` |
| Stated as | `NAD = NPT − PP` |
| Stated as | `{P}NetAmountDue{G/N}` |
| Stated as | Observed — label `Net Amount Due (NPT-PP)` |

### The waterfall — [CON-R-086](../rules/CON-R-086.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**A manual adjustment is made: RevisedNetAmountDue = NetAmountDue + AdjustmentAmount — labelled 'Revised Amount Due (Net+Adj)', the final figure billed.**

|  |  |
|---|---|
| Stated as | A manual adjustment is made |
| Stated as | `NAD`, `{P}AdjustmentAmount` |
| Stated as | `RNAD = NAD + Adj` |
| Stated as | `{P}RevisedNetAmountDue{G/N}` |
| Stated as | Observed — label `Revised Amount Due (Net+Adj)` |

### Grid structure and — [CON-R-087](../rules/CON-R-087.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**A recovery record is stored: 565 fields = 63 configuration fields + a 502-cell grid, where the grid is 9 perspectives × roughly 19 measures × {Gross, Net}.**

|  |  |
|---|---|
| Stated as | A recovery record is stored |
| Stated as | — |
| Stated as | 565 fields = 63 configuration + 502 grid, where grid = 9 perspectives × ~19 measures × {Gross, Net} |
| Stated as | Grid shape |
| Stated as | Derived |

### Grid structure and — [CON-R-088](../rules/CON-R-088.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**A within-year variance is computed: RAVariance = Reported − Approved, for both Gross and Net, at 36 fields.**

|  |  |
|---|---|
| Stated as | A within-year variance is computed |
| Stated as | `Reported*`, `Approved*` |
| Stated as | `RAVariance{M}{G/N} = Reported{M} − Approved{M}` |
| Stated as | 36 fields |
| Stated as | Derived |

### Grid structure and — [CON-R-089](../rules/CON-R-089.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**A within-year variance is computed: ABVariance = Approved − Budgeted, for both Gross and Net.**

|  |  |
|---|---|
| Stated as | A within-year variance is computed |
| Stated as | `Approved*`, `Budgeted*` |
| Stated as | `ABVariance{M}{G/N} = Approved{M} − Budgeted{M}` |
| Stated as | 36 fields |
| Stated as | Derived |

### Grid structure and — [CON-R-090](../rules/CON-R-090.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**A year-over-year variance is computed: {P}PVariance = {P} − Prior{P} for Reported, Approved and Budgeted, each with a percentage sibling.**

|  |  |
|---|---|
| Stated as | A year-over-year variance is computed |
| Stated as | `{P}`, `Prior{P}` |
| Stated as | `{P}PVariance{M}{G/N} = {P}{M} − Prior{P}{M}`, and `{P}PVariancePct` as the percentage form. Applies to R, A and B |
| Stated as | 6 × 36 fields |
| Stated as | Derived |

### Grid structure and — [CON-R-091](../rules/CON-R-091.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Variance families are enumerated: only the three year-over-year families carry a percentage sibling at the header; at the line-item level all five families carry both amount and percent — an asymmetry that says percentage swing year-over-year is the audit trigger, while percentage swing against the….**

|  |  |
|---|---|
| Stated as | Variance families are enumerated |
| Stated as | — |
| Stated as | Only the three year-over-year families carry `%` siblings at the header; at the line item all five carry both Amount and Percent |
| Stated as | Asymmetry |
| Stated as | Observed |

### Grid structure and — [CON-R-092](../rules/CON-R-092.md)

*Inferred · rule · source: `docs/modules/contracts/rules.md`*

**A measure is unset: fields suffixed NoZeroDef return null/blank rather than 0.**

|  |  |
|---|---|
| Stated as | A measure is unset |
| Stated as | Fields suffixed `NoZeroDef` |
| Stated as | Return null/blank rather than 0, so a genuine zero is distinguishable from unentered — preventing spurious 100% variances |
| Stated as | Nullable semantics |
| Stated as | Inferred (from the name) |

### Grid structure and — [CON-R-093](../rules/CON-R-093.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**A recovery cap applies: the cap grows period over period by a percentage or a value, cumulatively or not.**

|  |  |
|---|---|
| Stated as | A recovery cap applies |
| Stated as | `CodeCapTypeID`, `CapPercentage`, `CapAmountChangePercent`, `CapAmountChangeValue`, `IsRecoveryCapEscalationNonCum` |
| Stated as | The cap is a growing cap: a starting amount escalating per period by a percentage or a value, cumulatively or not |
| Stated as | Effective cap |
| Stated as | Derived |

### Grid structure and — [CON-R-094](../rules/CON-R-094.md)

*Inferred · rule · source: `docs/modules/contracts/rules.md`*

**The cap is applied to the waterfall: where in the sequence the clamp lands is not observable; the strong prior is controllables only.**

|  |  |
|---|---|
| Stated as | The cap is applied to the waterfall |
| Stated as | The cap, the waterfall |
| Stated as | Where in the waterfall the clamp lands is not observable. Strong prior: controllables only (`C`), which is why C and NC are separate measures |
| Stated as | Clamp point |
| Stated as | Inferred — unresolved |

### Grid structure and — [CON-R-095](../rules/CON-R-095.md)

*Inferred · rule · source: `docs/modules/contracts/rules.md`*

**A base year applies: an expense stop subtracts the base-year level; where it enters the waterfall is unobserved.**

|  |  |
|---|---|
| Stated as | A base year applies |
| Stated as | `BaseYear(Text)`, `BaseYearAmount`, `CodeBaseYearAmountTypeID` |
| Stated as | An expense stop subtracts the base-year level. Where it enters the waterfall is unobserved |
| Stated as | Base-year adjustment |
| Stated as | Inferred — unresolved |

### Grid structure and — [CON-R-096](../rules/CON-R-096.md)

*Inferred · rule · source: `docs/modules/contracts/rules.md`*

**A gross-up applies: variable expenses are grossed up to a notional occupancy using GrossupRate and OccupancyAdjustedThreshold.**

|  |  |
|---|---|
| Stated as | A gross-up applies |
| Stated as | `GrossupRate`, `OccupancyAdjustedThreshold` (computed Occupancy Factor) |
| Stated as | Variable expenses are grossed up to a notional occupancy |
| Stated as | Grossed-up expense |
| Stated as | Inferred |

### Grid structure and — [CON-R-097](../rules/CON-R-097.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**Escrow is trued up: reconcile the current escrow payment, propose a new estimate, and spread any shortfall over CatchUpNumberOfMonths.**

|  |  |
|---|---|
| Stated as | Escrow is trued up |
| Stated as | `CurrentEscrowPayment`, `EscalationPercentage`, `NewEscalationPayment`, `ProposedEscalationPayment`, `CatchUpNumberOfMonths`, `CatchUpPaymentAmount`, `ProposedCatchUpPaymentAmount`, `UPDATE_ESCROW` |
| Stated as | Reconcile, propose a new estimate, spread the shortfall over N months |
| Stated as | New escrow + catch-up |
| Stated as | Derived |

### Grid structure and — [CON-R-098](../rules/CON-R-098.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Recovery exclusions are recorded: RecoveryExclusions is a free-text textarea; there is no structured exclusion model for expense recovery at all.**

|  |  |
|---|---|
| Stated as | Recovery exclusions are recorded |
| Stated as | `RecoveryExclusions(Textarea)` |
| Stated as | Free text only. There is no structured exclusion model for expense recovery |
| Stated as | Unstructured |
| Stated as | Observed |

### Grid structure and — [CON-R-099](../rules/CON-R-099.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**A recovery is settled: ReconciledFlag, ReconciledDate, TenantDueDate and TenantSavingsAmount record the audit outcome.**

|  |  |
|---|---|
| Stated as | A recovery is settled |
| Stated as | `ReconciledFlag`, `ReconciledDate`, `TenantDueDate`, `TenantSavingsAmount`, `RECONCILE` |
| Stated as | The audit outcome, including what the audit saved the tenant |
| Stated as | Settlement |
| Stated as | Observed |

### Line item level — [CON-R-100](../rules/CON-R-100.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**A recovery line item is valued: the same Reported/Approved/Budgeted/Prior perspectives exist at line-item cardinality.**

|  |  |
|---|---|
| Stated as | A recovery line item is valued |
| Stated as | `ReportedAmount{,Gross,Net}`, `ApprovedAmount`, `BudgetedAmount{,Gross,Net}`, `Prior*AmountNoZeroDef` |
| Stated as | Same perspectives as the header, at line-item cardinality |
| Stated as | Item values |
| Stated as | Observed |

### Line item level — [CON-R-101](../rules/CON-R-101.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**A line item's approved total is computed: ComputedApprovedTotalAmount applies its own admin fee and cap per line item, not only at the header.**

|  |  |
|---|---|
| Stated as | A line item's approved total is computed |
| Stated as | `ApprovedAmount`, `ApprovedAdminFeeAmtNoZeroDef`, `ApprovedAdminFeePrcntNoZeroDef`, `ApprovedCapAmountNoZeroDef`, `ApprovedCapPercentNoZeroDef` |
| Stated as | `ComputedApprovedTotalAmount{,Gross,Net}` — admin fee and cap apply per line item, not only at the header |
| Stated as | Item total |
| Stated as | Derived |

### Line item level — [CON-R-102](../rules/CON-R-102.md)

*Inferred · rule · source: `docs/modules/contracts/rules.md`*

**A landlord statement is ingested: ExpenseRecoveryItemMapping maps a free-text statement line (InvoiceLineItemName, JSONConfigText) to a structured recovery item.**

|  |  |
|---|---|
| Stated as | A landlord statement is ingested |
| Stated as | `ExpenseRecoveryItemMapping.InvoiceLineItemName`, `.DocumentID`, `.JSONConfigText` |
| Stated as | Maps a free-text statement line to a structured `ExpenseRecoveryItem` |
| Stated as | Item mapping |
| Stated as | Inferred |

### 9 Payment lifecycle — [CON-R-103](../rules/CON-R-103.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**A payment is posted: five independent date axes must be simultaneously representable: GL period, economic effect, cash due, service coverage, settlement.**

|  |  |
|---|---|
| Stated as | A payment is posted |
| Stated as | `PostingDate`, `EffectiveDate`, `DueDate`, `BillingDate`, `CoverageBeginDate`, `CoverageEndDate`, `InvoiceDate`, `CheckDate` |
| Stated as | Five independent date axes must be representable simultaneously: GL period, economic effect, cash due, service coverage, settlement |
| Stated as | Date model |
| Stated as | Observed |

### 9 Payment lifecycle — [CON-R-104](../rules/CON-R-104.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Direction is determined: IsReceivable lets one ledger serve both payables and receivables.**

|  |  |
|---|---|
| Stated as | Direction is determined |
| Stated as | `IsReceivable` |
| Stated as | One ledger serves payables and receivables |
| Stated as | Direction |
| Stated as | Observed |

### 9 Payment lifecycle — [CON-R-105](../rules/CON-R-105.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**A credit is issued: CreditFlag plus AppliedToPayTranID points a credit transaction at the transaction it offsets.**

|  |  |
|---|---|
| Stated as | A credit is issued |
| Stated as | `CreditFlag`, `AppliedToPayTranID` |
| Stated as | A credit transaction points at the transaction it offsets |
| Stated as | Credit application |
| Stated as | Observed |

### 9 Payment lifecycle — [CON-R-106](../rules/CON-R-106.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Tax is applied: four parallel tax components, with TaxesIncludedFlag saying whether they sit inside TotalAmount or are additional to it.**

|  |  |
|---|---|
| Stated as | Tax is applied |
| Stated as | `TaxAmount1..4`, `TaxesIncludedFlag` |
| Stated as | Four parallel tax components; the flag says whether they are inside or additional to `TotalAmount` |
| Stated as | Tax treatment |
| Stated as | Observed |

### 9 Payment lifecycle — [CON-R-107](../rules/CON-R-107.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Aging is computed: AgingAmountForMonth1..3 and AgingAmountRemainder bucket from the invoice/effective date — the base date itself is inferred, not confirmed.**

|  |  |
|---|---|
| Stated as | Aging is computed |
| Stated as | `AgingAmountForMonth1..3`, `AgingAmountRemainder` |
| Stated as | Buckets 0-30 / 31-60 / 61-90 / 90+ from the invoice/effective date |
| Stated as | Aging ladder A |
| Stated as | Observed (labels); base date Inferred |

### 9 Payment lifecycle — [CON-R-108](../rules/CON-R-108.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Due-date aging is computed: DueDateAgingAmountForMonth1..3 and its remainder use the same buckets measured from DueDate.**

|  |  |
|---|---|
| Stated as | Due-date aging is computed |
| Stated as | `DueDateAgingAmountForMonth1..3`, `DueDateAgingAmountRemainder` |
| Stated as | The same buckets measured from `DueDate` |
| Stated as | Aging ladder B |
| Stated as | Observed |

### 9 Payment lifecycle — [CON-R-109](../rules/CON-R-109.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**An expense type is chosen: CodeExpenseTypeID selects both the GL account set and the accounting treatment (CodeASC842ScheduleID, CodeIFRS16ScheduleID, CodeSLScheduleID) in one action.**

|  |  |
|---|---|
| Stated as | An expense type is chosen |
| Stated as | `CodeExpenseTypeID` → `CodeExpenseType` |
| Stated as | Selects both the GL account set and the accounting treatment (`CodeASC842ScheduleID`, `CodeIFRS16ScheduleID`, `CodeSLScheduleID`) |
| Stated as | GL + treatment |
| Stated as | Observed |

### 9 Payment lifecycle — [CON-R-110](../rules/CON-R-110.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**A transaction is posted: all twenty account numbers from CodeExpenseType are snapshotted onto the transaction row, not looked up again at export time.**

|  |  |
|---|---|
| Stated as | A transaction is posted |
| Stated as | `CodeExpenseType.APExportBase/Prepaid/Tax1..4Number`, `.ExpAccrualAcct1..4Number`, `.PercentRentAccrualAcct1..4Number`, `.RETaxAccrualAcct1..4Number` |
| Stated as | The account numbers are snapshotted onto the transaction row, not looked up at export |
| Stated as | Frozen GL coding |
| Stated as | Derived |

### 9 Payment lifecycle — [CON-R-111](../rules/CON-R-111.md)

*Inferred · rule · source: `docs/modules/contracts/rules.md`*

**Eight-segment coding is applied: AccountNumber1..8 exists on PaymentTransaction/AccrualTransaction but not on CodeExpenseType; whether these are 8 segments of one account or 8 split-coding lines is unresolved.**

|  |  |
|---|---|
| Stated as | Eight-segment coding is applied |
| Stated as | `AccountNumber1..8` |
| Stated as | Present on `PaymentTransaction` and `AccrualTransaction`, absent from `CodeExpenseType`; `Organization` carries `Account Number #1–8`. Whether these are 8 segments of one account or 8 split-coding lines is unresolved |
| Stated as | Account string |
| Stated as | Inferred — unresolved |

### 9 Payment lifecycle — [CON-R-112](../rules/CON-R-112.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**A batch is exported: ExportBatchNumber is set when the row leaves for AP.**

|  |  |
|---|---|
| Stated as | A batch is exported |
| Stated as | `ExportBatchNumber` |
| Stated as | Set when the row leaves for AP |
| Stated as | Export marker |
| Stated as | Observed |

### 9 Payment lifecycle — [CON-R-113](../rules/CON-R-113.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**AP settles a payment: CheckNumber/CheckDate/CheckAmount/CodeCheckCurrencyTypeID are written back — check currency may differ from transaction currency with no FX rate field to reconcile the two.**

|  |  |
|---|---|
| Stated as | AP settles a payment |
| Stated as | `CheckNumber`, `CheckDate`, `CheckAmount`, `CodeCheckCurrencyTypeID` |
| Stated as | Settlement details written back. Check currency may differ from transaction currency, with no FX rate field on the transaction |
| Stated as | Settlement |
| Stated as | Observed |

### 9 Payment lifecycle — [CON-R-114](../rules/CON-R-114.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**A landlord invoice is imported: IMPORT_INVOICE extracts VendorName/Address/TaxID and CustomerName/Address/TaxID as text, kept alongside the resolved EmployerID.**

|  |  |
|---|---|
| Stated as | A landlord invoice is imported |
| Stated as | `IMPORT_INVOICE`, `LandlordInvoice.VendorName/Address/TaxID`, `CustomerName/Address/TaxID` |
| Stated as | Extracted values are kept as `Text` alongside the resolved `EmployerID` FK |
| Stated as | Invoice + extraction record |
| Stated as | Derived |

### 9 Payment lifecycle — [CON-R-115](../rules/CON-R-115.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**An invoice line is matched to a payment: LinkLandlordInvPaymentTxn allocates AllocationAmount/AllocationDate between LandlordInvoiceItemID and PaymentTransactionID.**

|  |  |
|---|---|
| Stated as | An invoice line is matched to a payment |
| Stated as | `LinkLandlordInvPaymentTxn.LandlordInvoiceItemID`, `.PaymentTransactionID`, `.AllocationAmount`, `.AllocationDate` |
| Stated as | Many-to-many allocation |
| Stated as | Match |
| Stated as | Observed |

### 9 Payment lifecycle — [CON-R-116](../rules/CON-R-116.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**A match has a difference: VarianceAmount and VarianceReason are stored on the join itself, alongside ReconciliationStatus.**

|  |  |
|---|---|
| Stated as | A match has a difference |
| Stated as | `LinkLandlordInvPaymentTxn.VarianceAmount`, `.VarianceReason`, `.ReconciliationStatus` |
| Stated as | The variance and its explanation are stored on the join |
| Stated as | Explained variance |
| Stated as | Observed |

### 9 Payment lifecycle — [CON-R-117](../rules/CON-R-117.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**A payment is fully matched: PaymentTransaction.IsInvoiceReconciled is set when the three-way match completes.**

|  |  |
|---|---|
| Stated as | A payment is fully matched |
| Stated as | `PaymentTransaction.IsInvoiceReconciled` |
| Stated as | Set when the three-way match completes |
| Stated as | Reconciled flag |
| Stated as | Observed |

### 9 Payment lifecycle — [CON-R-118](../rules/CON-R-118.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Money is received: there is no FK or link table from PaymentReceipt to PaymentTransaction — only allocated/unallocated totals on each side.**

|  |  |
|---|---|
| Stated as | Money is received |
| Stated as | `PaymentReceipt.ReceivedAmount`, `.AmountAllocated`, `.AmountNotAllocated`, `RECONCILE_RECEIPT` |
| Stated as | There is no FK or link table from `PaymentReceipt` to `PaymentTransaction` — only allocated/unallocated totals on each side |
| Stated as | Receipt allocation |
| Stated as | Observed (by absence) — schema gap |

### 9 Payment lifecycle — [CON-R-119](../rules/CON-R-119.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**An accrual is posted: AccrualTransaction carries PeriodAmount, PeriodBeginDate/EndDate, PeriodNumber/Year and PostingDate, with its own GL slots, driven by GENERATE_ACCRUALS.**

|  |  |
|---|---|
| Stated as | An accrual is posted |
| Stated as | `AccrualTransaction.PeriodAmount`, `.PeriodBeginDate`, `.PeriodEndDate`, `.PeriodNumber`, `.PeriodYear`, `.PostingDate`, `GENERATE_ACCRUALS` |
| Stated as | Period-scoped accrual with its own GL slots |
| Stated as | Accrual posting |
| Stated as | Observed |

### 9 Payment lifecycle — [CON-R-120](../rules/CON-R-120.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**An accrual clause is configured: ExpenseAccrualSetup accrues an expense ahead of its billing, using CodeAccrualTypeID, CurrentAnnualExpense/CurrentPeriodExpense, and optionally IsDailyRent + RentableArea.**

|  |  |
|---|---|
| Stated as | An accrual clause is configured |
| Stated as | `ExpenseAccrualSetup.CodeAccrualTypeID`, `.CurrentAnnualExpense`, `.CurrentPeriodExpense`, `.BeginPeriodName`, `.EndPeriodName`, `.IsDailyRent`, `.RentableArea` |
| Stated as | Accrue an expense ahead of its billing (property tax, insurance) |
| Stated as | Accrual clause |
| Stated as | Observed |

### 9 Payment lifecycle — [CON-R-121](../rules/CON-R-121.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**An accrual schedule is generated: period-by-period accrual amounts are produced from AccrualRate/DailyAccrualRate, with the same daily-rate support as recurring expense.**

|  |  |
|---|---|
| Stated as | An accrual schedule is generated |
| Stated as | `ExpenseAccrualSchedule.AccrualRate`, `.DailyAccrualRate`, `.PeriodAmount`, `.AnnualAmount`, `.BeginPeriod/Year`, `.EndPeriod/Year` |
| Stated as | Period-by-period accrual amounts, with daily-rate support |
| Stated as | L1 accrual rows |
| Stated as | Observed |

### 9 Payment lifecycle — [CON-R-122](../rules/CON-R-122.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Accruals are forecast: ForecastCapPercent/ForecastGrowthPercent/ForecastAdjustment and their Plan* twins grow the accrual independently of the contract's own escalation.**

|  |  |
|---|---|
| Stated as | Accruals are forecast |
| Stated as | `ExpenseAccrualSchedule.ForecastCapPercent`, `.ForecastGrowthPercent`, `.ForecastAdjustment`, `.PlanCapPercent`, `.PlanGrowthPercent`, `.PlanAdjustment` |
| Stated as | Planning/forecast growth is independent of contractual escalation |
| Stated as | Forecast amounts |
| Stated as | Observed |

### 9 Payment lifecycle — [CON-R-123](../rules/CON-R-123.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Percentage-rent accrual is reconciled: VirtualPRAccrualPeriod's computed AccrualAmount{ThisPeriod,PriorPeriods,Total} is displayed next to the PostedAccrualAmount{...} that was actually posted, with IsPosted as the flag.**

|  |  |
|---|---|
| Stated as | Percentage-rent accrual is reconciled |
| Stated as | `VirtualPRAccrualPeriod.AccrualAmount{ThisPeriod,PriorPeriods,Total}` vs `PostedAccrualAmount{…}`, `IsPosted` |
| Stated as | Recomputed accrual is displayed against what was actually posted |
| Stated as | Reconciliation pair |
| Stated as | Observed |

### 9 Payment lifecycle — [CON-R-124](../rules/CON-R-124.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Bulk payments are imported: PaymentTransactionFullImport mirrors PaymentTransaction's 118 fields with no backing table of its own.**

|  |  |
|---|---|
| Stated as | Bulk payments are imported |
| Stated as | `PaymentTransactionFullImport` (118 fields, no PG table) |
| Stated as | A field-for-field staging mirror of `PaymentTransaction` |
| Stated as | Import buffer |
| Stated as | Observed |

### 10 Suppression and — [CON-R-125](../rules/CON-R-125.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Any generation or posting: HoldFlag on ExpenseSetup, ExpenseSchedule, ExpenseAccrualSetup, PaymentTransaction or AccrualTransaction is a negative gate at every layer.**

|  |  |
|---|---|
| Stated as | Any generation or posting |
| Stated as | `HoldFlag` on `ExpenseSetup`, `ExpenseSchedule`, `ExpenseAccrualSetup`, `PaymentTransaction`, `AccrualTransaction` |
| Stated as | Negative gate at every layer |
| Stated as | Suppression |
| Stated as | Observed |

### 10 Suppression and — [CON-R-126](../rules/CON-R-126.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Any generation: ReadyForPaymentFlag on ExpenseSetup and ExpenseSchedule is a positive gate — both must be true.**

|  |  |
|---|---|
| Stated as | Any generation |
| Stated as | `ReadyForPaymentFlag` on `ExpenseSetup`, `ExpenseSchedule` |
| Stated as | Positive gate — must be true |
| Stated as | Permission |
| Stated as | Observed |

### 10 Suppression and — [CON-R-127](../rules/CON-R-127.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Forecast inclusion: only ExpenseSetup rows flagged IncludeInPlanForecast appear in VirtualExpenseForecastPeriod.**

|  |  |
|---|---|
| Stated as | Forecast inclusion |
| Stated as | `ExpenseSetup.IncludeInPlanForecast`, `CodePlanForecastBasedOnID`, `CodePlanForecastGroupID` |
| Stated as | Only flagged clauses appear in `VirtualExpenseForecastPeriod` |
| Stated as | Forecast scope |
| Stated as | Observed |

### 10 Suppression and — [CON-R-128](../rules/CON-R-128.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Accrual scope: only ContractTerm rows flagged IncludeTermForAccruals are accrued.**

|  |  |
|---|---|
| Stated as | Accrual scope |
| Stated as | `ContractTerm.IncludeTermForAccruals` |
| Stated as | Only flagged option terms are accrued |
| Stated as | Accrual scope |
| Stated as | Observed |

### 10 Suppression and — [CON-R-129](../rules/CON-R-129.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Liability scope: Covenant.HoldAmountInSchedLiability excludes a covenant amount from the ASC 842 scheduled liability.**

|  |  |
|---|---|
| Stated as | Liability scope |
| Stated as | `Covenant.HoldAmountInSchedLiability` |
| Stated as | Excludes a covenant amount from the ASC 842 scheduled liability |
| Stated as | Liability scope |
| Stated as | Observed |

### 10 Suppression and — [CON-R-130](../rules/CON-R-130.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Disclosure scope: SLSummary.IsIncludeInRollForwardReport controls inclusion in the roll-forward disclosure.**

|  |  |
|---|---|
| Stated as | Disclosure scope |
| Stated as | `SLSummary.IsIncludeInRollForwardReport` |
| Stated as | Controls inclusion in the roll-forward disclosure |
| Stated as | Report scope |
| Stated as | Observed |

### 4 1 Typing hazard — [CON-R-131](../rules/CON-R-131.md)

*Derived · rule · source: `docs/modules/contracts/asg-edgeplus-mapping.md`*

**Migrating any landed Postgres column: every column across 33 tables is TEXT except 31 VARCHAR(64) primary keys — no numeric, date or boolean column exists; every value must be parsed and validated on ingest.**

|  |  |
|---|---|
| Stated as | 1 |
| Stated as | Every landed Postgres column is `TEXT` — 1,163 of 1,194 cross-mapped columns; the other 31 are `VARCHAR(64)` PKs. No numeric, date or boolean column exists in the landed schema |
| Stated as | All 33 tables in `_crossmap.tsv`, incl. `sales.GrossSalesAmount`, `sales.NetSalesAmount`, `sales.SalesAdjustment1..6` |
| Stated as | Critical |

### 11 Typing and — [CON-R-132](../rules/CON-R-132.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Migrating PaymentTransaction: parse AmountInvoiced and AmountReceived to BigDecimal and reconcile them against InvoiceAmount and PaymentReceipt.ReceivedAmount.**

|  |  |
|---|---|
| Stated as | Migrating `PaymentTransaction` |
| Stated as | `AmountInvoiced(Text)`, `AmountReceived(Text)` |
| Stated as | Two money fields on the central ledger are declared `Text` while their siblings are `Currency` |
| Stated as | Parse to `BigDecimal`; reconcile against `InvoiceAmount` and `PaymentReceipt.ReceivedAmount` |
| Stated as | Observed |

### 11 Typing and — [CON-R-133](../rules/CON-R-133.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Migrating LandlordInvoiceItem: money, date and boolean are all stored as text on this reconciliation grid; replace the seven PayTrans* mirror fields with a join.**

|  |  |
|---|---|
| Stated as | Migrating `LandlordInvoiceItem` |
| Stated as | `PayTransTotalAmount(Text)`, `LinkAmountAllocated(Text)`, `PayTransEffectiveDate(Text)`, `PayTransIsReceivable(Text)` |
| Stated as | Money, date and boolean all stored as text on a reconciliation grid |
| Stated as | Replace the seven `PayTrans*` mirror fields with a join |
| Stated as | Observed |

### 11 Typing and — [CON-R-134](../rules/CON-R-134.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Migrating any parent-child edge: seven FKs are declared Text rather than typed, though the target's proper FK type exists elsewhere in the same schema; model them as real FKs with an orphan-handling policy.**

|  |  |
|---|---|
| Stated as | Migrating any parent-child edge |
| Stated as | Seven `Text`-typed FKs (`PaymentTransaction.ExpenseRecoveryID`, `.ScheduledOffsetID`, `ExpenseSchedule.Previous/NextExpenseScheduleID`, `ExpenseAccrualSchedule.ExpenseAccrualSetupID`, `AccrualTransaction.ExpenseAccrualSetupID`, `ExpenseRecoveryItem.ExpenseRecoveryID`, `LandlordInvoiceItem.LandlordInvoiceID`, `LinkLandlordInvPaymentTxn.LandlordInvoiceItemID`) |
| Stated as | Declared `Text` rather than a typed FK, though the target's FK type exists elsewhere |
| Stated as | Model as real FKs; define an orphan-handling policy |
| Stated as | Observed |

### 11 Typing and — [CON-R-135](../rules/CON-R-135.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Any usage-based rent arithmetic: 6-decimal precision is required on unit rates; use BigDecimal with explicit scale and rounding mode, never a binary float.**

|  |  |
|---|---|
| Stated as | Any usage-based rent arithmetic |
| Stated as | `sTYPE_NUMBER_FRACTION6DIGITS` unit rates × large usage counts |
| Stated as | 6-decimal precision is required; binary floating point loses money here |
| Stated as | `BigDecimal` with explicit scale and rounding mode |
| Stated as | Observed |

### 11 Typing and — [CON-R-136](../rules/CON-R-136.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Any percentage arithmetic: sTYPE_PERCENTAGE fields multiply money in the pro-rata, breakpoint and CPI paths; store as BigDecimal and fix the scale and rounding policy at every multiplication step.**

|  |  |
|---|---|
| Stated as | Any percentage arithmetic |
| Stated as | `sTYPE_PERCENTAGE` fields (188 catalog-wide) used as multipliers in `CON-R-059`, `CON-R-084`, `CON-R-042` |
| Stated as | Rates multiply money in the pro-rata share, breakpoint and CPI paths |
| Stated as | Store as `BigDecimal`; fix scale and rounding at each step; never `double` |
| Stated as | Observed hazard, Judgement on remedy |

### 11 Typing and — [CON-R-137](../rules/CON-R-137.md)

*Inferred · rule · source: `docs/modules/contracts/rules.md`*

**Any recovery measure is unset: for the rebuild, model recovery measures as nullable BigDecimal, never zero-defaulted — a zero default silently produces spurious 100% variances.**

|  |  |
|---|---|
| Stated as | Any recovery measure is unset |
| Stated as | `NoZeroDef`-suffixed fields |
| Stated as | A zero default produces spurious 100% variances |
| Stated as | Model recovery measures as nullable `BigDecimal`, not zero-defaulted |
| Stated as | Inferred |

### 12 Contract status — [CON-R-138](../rules/CON-R-138.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**A contract's status is set: CodeContractStatusID resolves to exactly one of three values — AI Abstracted, Active, Inactive — and none is a BRD-24 lifecycle stage.**

|  |  |
|---|---|
| Stated as | A contract's status is set |
| Stated as | `CodeContractStatusID` → `Contract Status Code` (2094) |
| Stated as | The enum has exactly three values: `AI Abstracted`, `Active`, `Inactive`. None is a BRD-24 lifecycle stage |
| Stated as | Record state |
| Stated as | Observed |

### 12 Contract status — [CON-R-139](../rules/CON-R-139.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**A status value is deleted: Active carries no delete action — the platform protects at least one seeded value as system-required.**

|  |  |
|---|---|
| Stated as | A status value is deleted |
| Stated as | Row actions on `Contract Status Code` |
| Stated as | `Active` carries no delete action — the platform protects at least one seeded value as system-required |
| Stated as | Deletion refused |
| Stated as | Observed |

### 12 Contract status — [CON-R-140](../rules/CON-R-140.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Recording how a contract was abstracted: provenance (AI-abstracted or not) is encoded as a state value, so a contract can be AI-abstracted and active at once — the two axes are conflated in this one field.**

|  |  |
|---|---|
| Stated as | Recording how a contract was abstracted |
| Stated as | `CodeContractStatusID = AI Abstracted` |
| Stated as | The tenant encodes provenance as a state value. A contract can be AI-abstracted and active, so the two axes are conflated |
| Stated as | Provenance (mis-)recorded as state |
| Stated as | Observed value; Derived reading |

### 12 Contract status — [CON-R-141](../rules/CON-R-141.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**Determining a contract's lifecycle stage: the stage is derived from date fields (ActualStartDate/OpenYear, StatusEffectiveDate, PossessionBeginDate/EndDate, PaymentsBeginDate/EndDate, ExpireDate/ActualEndDate/IsDead/Inactive) rather than stored directly in any enum.**

|  |  |
|---|---|
| Stated as | Determining a contract's lifecycle stage |
| Stated as | `ActualStartDate`/`OpenYear` (Open), `StatusEffectiveDate` (Active), `PossessionBeginDate`/`PossessionEndDate` (Possession), `PaymentsBeginDate`/`PaymentsEndDate` (Paying Rent), `ExpireDate`/`ActualEndDate`/`IsDead`/`Inactive` (Closed) |
| Stated as | Lx derives stage from dates rather than storing it. No enum holds BRD-24's five stages |
| Stated as | Derived stage |
| Stated as | Derived |

### 12 Contract status — [CON-R-142](../rules/CON-R-142.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**A contract advances through its process: ProcessTimelineTemplate forms a linked list of phase-bound milestone templates, instantiated per entity as ProcessTimeline rows with their own status/percent-complete/date-triple fields — the real state machine underneath the derived display text.**

|  |  |
|---|---|
| Stated as | A contract advances through its process |
| Stated as | `ProcessTimelineTemplate.CodeProjectPhaseID`, `.InProcessPhaseStatus`, `.CompletedPhaseStatus`, `.PreviousProcessTimelineID`; `ProcessTimeline.CodeTaskStatusID`, `.PercentComplete`, Original/Projected/Actual date triples |
| Stated as | A linked list of phase-bound milestone templates, instantiated per entity, each declaring the status text for its in-progress and completed states. This is the real state machine |
| Stated as | `CurrentPhaseStatus`, `CurrentMilestone`, `NextMilestone`, `PreviousMilestone` (all `Text`, derived display) |
| Stated as | Observed fields; Derived mechanism |

### 12 Contract status — [CON-R-143](../rules/CON-R-143.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Resolving the phase enumeration: Project Phase Code is used by 11 objects but is not among the 207 Firm Drop Downs — an engine-governed enumeration, not a tenant-configurable one.**

|  |  |
|---|---|
| Stated as | Resolving the phase enumeration |
| Stated as | `Project Phase Code` |
| Stated as | Not among the 207 Firm Drop Downs, yet used by 11 objects. A platform-internal enumeration not exposed for tenant editing — the same pattern as `Work Flow Status Code` |
| Stated as | Engine-governed, not configurable |
| Stated as | Observed (presence in the object export, absence from the registry) |

### 12 Contract status — [CON-R-144](../rules/CON-R-144.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**The tenant needs a lifecycle status: Contract.Firm_LeaseStatus (a Firm-scope custom code field, with a Firm_LeaseStatusNotes companion) is ASG's own answer, sitting in the same Contract Info sub-group as the platform's status field — not to be confused with the platform's own Lease Status Code….**

|  |  |
|---|---|
| Stated as | The tenant needs a lifecycle status |
| Stated as | `Contract.Firm_LeaseStatus` (`sTYPE_CUSTOM_CODE_FIELD`, Firm) + `Firm_LeaseStatusNotes` |
| Stated as | ASG added its own contract-status field in the same `Contract / Contract Info` sub-group as the platform's. Do not confuse with `LeaseInfo.CodeLeaseStatusID` (`Lease Status Code` 2043), which is used by exactly one object and that object has no `ContractID` column |
| Stated as | Tenant-authored lifecycle |
| Stated as | Observed |

### 13 Rent generation — [CON-R-145](../rules/CON-R-145.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**A user invokes `Generate Rent` · `ExpenseSchedule` rows for the contract · Generation reads the Schedule layer, not the Setup layer · A contract with Expense Setups but an empty Expense Schedule generates nothing · Derived.**

|  |  |
|---|---|
| Stated as | A user invokes `Generate Rent` |
| Stated as | `ExpenseSchedule` rows for the contract |
| Stated as | Generation reads the Schedule layer, not the Setup layer |
| Stated as | A contract with Expense Setups but an empty Expense Schedule generates nothing |
| Stated as | Derived |

### 13 Rent generation — [CON-R-146](../rules/CON-R-146.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**The Generate Payments dialog opens · Period (month + year), Posting Date, Batch Date · A batch number is minted as `RNT<yyyymmdd>-<sequence>` · The run is identified by that batch number · Observed.**

|  |  |
|---|---|
| Stated as | The Generate Payments dialog opens |
| Stated as | Period (month + year), Posting Date, Batch Date |
| Stated as | A batch number is minted as `RNT<yyyymmdd>-<sequence>` |
| Stated as | The run is identified by that batch number |
| Stated as | Observed |

### 13 Rent generation — [CON-R-147](../rules/CON-R-147.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**A user selects a generation scope · `Generate Option` · One of `Single Contract`, `Payables — All Contracts`, `Receivables — All Contracts`, `All Contracts` · Three of the four run across every contract in scope; payables and receivables are separately runnable · Observed.**

|  |  |
|---|---|
| Stated as | A user selects a generation scope |
| Stated as | `Generate Option` |
| Stated as | One of `Single Contract`, `Payables — All Contracts`, `Receivables — All Contracts`, `All Contracts` |
| Stated as | Three of the four run across every contract in scope; payables and receivables are separately runnable |
| Stated as | Observed |

### 13 Rent generation — [CON-R-148](../rules/CON-R-148.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**A transaction is generated · Expense type, period, proration method · Description is `<MNEMONIC> MM/YYYY`, or `<MNEMONIC> - PRS <from>-<to>` when prorated · The row records how it was computed. Mnemonics observed: `BRNT`, `RET`, `CAM - PRS`, `CAM - FIXED`, `INS`, `INS - PRS`, `ELEC`, `UTIL`, `WTR`,….**

|  |  |
|---|---|
| Stated as | A transaction is generated |
| Stated as | Expense type, period, proration method |
| Stated as | Description is `<MNEMONIC> MM/YYYY`, or `<MNEMONIC> - PRS <from>-<to>` when prorated |
| Stated as | The row records how it was computed. Mnemonics observed: `BRNT`, `RET`, `CAM - PRS`, `CAM - FIXED`, `INS`, `INS - PRS`, `ELEC`, `UTIL`, `WTR`, `MISC` |
| Stated as | Observed |

### 13 Rent generation — [CON-R-149](../rules/CON-R-149.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**A transaction is generated · `invoiceAmount`, `primaryTax`, `APExportTax1..4Number` · `totalAmount` = `invoiceAmount` + tax · Up to four tax components are carried per transaction · Observed.**

|  |  |
|---|---|
| Stated as | A transaction is generated |
| Stated as | `invoiceAmount`, `primaryTax`, `APExportTax1..4Number` |
| Stated as | `totalAmount` = `invoiceAmount` + tax |
| Stated as | Up to four tax components are carried per transaction |
| Stated as | Observed |

### 13 Rent generation — [CON-R-150](../rules/CON-R-150.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**A transaction is generated · — · In this tenant every generated row arrives `processedFlag = true` and approval status `Approved` · Whether that is tenant configuration or engine behaviour is unresolved · Observed / Inferred.**

|  |  |
|---|---|
| Stated as | A transaction is generated |
| Stated as | — |
| Stated as | In this tenant every generated row arrives `processedFlag = true` and approval status `Approved` |
| Stated as | Whether that is tenant configuration or engine behaviour is unresolved |
| Stated as | Observed / Inferred |

### 13 Rent generation — [CON-R-151](../rules/CON-R-151.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**A transaction is generated · `exportBatchNumber` · Generation does not set it — null on every row sampled · GL export is a separate, later stage from generation · Derived.**

|  |  |
|---|---|
| Stated as | A transaction is generated |
| Stated as | `exportBatchNumber` |
| Stated as | Generation does not set it — null on every row sampled |
| Stated as | GL export is a separate, later stage from generation |
| Stated as | Derived |

### 13 Rent generation — [CON-R-152](../rules/CON-R-152.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**An Expense Setup is generated from · `ExpenseVendorAllocation` rows, each with a `Payment Percentage` and its own begin/end dates · One setup fans out to one transaction per allocation · The vendor split can change mid-term · Observed.**

|  |  |
|---|---|
| Stated as | An Expense Setup is generated from |
| Stated as | `ExpenseVendorAllocation` rows, each with a `Payment Percentage` and its own begin/end dates |
| Stated as | One setup fans out to one transaction per allocation |
| Stated as | The vendor split can change mid-term |
| Stated as | Observed |

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
