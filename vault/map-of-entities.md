---
title: Map of entities
tags: [moc, data-model]
---

# The product, by what it stores

**223 record types, 7,421 fields, 972 foreign keys.** Notes here are named with the **real object
name**, because those are technical identifiers and not branding.

Start with [[entity-spine]] — everything below hangs off it.

## The spine

[[ProjectEntity]] — the universal supertype, 107 fields, referenced by 161 objects.

**The nine [[subtype-root|subtype roots]]**, the only things that can be a navigation root:
[[Contract]] 570 · [[Program]] 180 · [[Parcel]] 154 · [[Location]] 141 · [[Facility]] 133 ·
[[Prototype]] 113 · [[Project]] 111 · [[PotentialProject]] 108 · *(`BudgetOptionTemplate`, a false
positive)*

## Contract and its children

[[ContractAmendment]] · [[Covenant]] · [[ContractTerm]] · [[ContractFinancialTest]] · [[KeyDate]] ·
[[SecurityDeposit]] · [[Insurance]] · [[Allowance]] · [[CoTenancy]] · [[Responsibility]] ·
[[LeaseInfo]]

## Money

**Accounting** — [[SLSummary]] · [[SLPeriod]] · [[AccrualTransaction]] · [[PaymentTransaction]] ·
[[PaymentReceipt]] · [[DiscountRate]] · [[EscalationIndex]]

**Expense recovery and schedules** — [[ExpenseRecovery]] (565 fields) · [[ExpenseSetup]] ·
[[ExpenseSchedule]] · [[ExpenseAccrualSchedule]] · [[ExpenseEscalation]]

**Variable rent** — [[PercentageRent]] · [[Sales]] · [[SalesExclusionCap]]

## Property

[[Complex]] · [[Space]] · [[DMA]] ·
**Tax** — [[PropertyTaxSummary]] · [[PropertyTaxAssessment]] · [[PropertyTaxBill]] ·
[[PropertyTaxAppeal]]

## Assets

[[Asset]] · [[AssetHistory]]

## People and parties

[[Member]] · [[Person]] · [[NonMember]] · [[Employer]] · [[Organization]] ·
[[LinkMemberProjectEntity]]

## Workflow and requests

[[WorkFlow]] · [[WorkFlowStep]] · [[WorkFlowStepApprover]] · [[WorkFlowTemplate]] ·
[[WorkFlowTemplateStep]] · [[WorkFlowTemplateStepAction]] · [[Issue]] · [[CodeIssueType]]

## Documents, tasks, deals

[[Document]] · [[Folder]] · [[Task]] · [[TaskGroup]] · [[TaskItem]] · [[RETransaction]] ·
[[Scenario]]

## Configuration — which mostly is not in the census

[[PageLayout]] · [[PageLayoutField]] · [[PageLayoutFilter]] · [[ReportGroupAvailableField]] ·
[[CustomCodeField]] · [[CodeExpenseType]] · [[ClientListRow]]

> **[[PageLayout]] and its family are absent from the 223-object census** — the schema viewer refuses
> them. They were recovered over [[rest-business-object|REST]]. See [[q-bbw-13-census-gap]].

## Platform

[[Firm]] · [[StateProvinceCountry]] · [[Jurisdiction]] · [[Region]] · [[Security]] ·
[[UserClassSecurity]]

## Computed projections — not tables

[[VirtualPercentageRentPeriod]] · [[VirtualSalesPeriod]] — see [[virtual-projection]], and
[[finding-layouts-over-projections]] for why they matter more than "internal machinery" suggests.

## Reading the graph

[[foreign-key-graph]] · [[type-system]] · [[soft-reference]] · [[finding-fk-graph-undercounts]]

← [[00-start-here]] · [[map-of-concepts]] · [[map-of-features]]
