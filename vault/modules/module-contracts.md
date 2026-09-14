---
title: Contracts
tags: [module, contracts, core]
evidence: Observed
---

**55 objects · rules `CON-R-001`…`CON-R-161`** — the largest rule set in the corpus.

Read [[setup-schedule-transaction]] first. It is the module's own stated centrepiece: not five
financial subsystems but **one pattern applied five times**, plus one outlier — and the outlier is
[[cam-waterfall|CAM]].

Entities: [[Contract]] · [[ContractAmendment]] · [[Covenant]] · [[ContractTerm]] · [[KeyDate]] ·
[[SecurityDeposit]] · [[Insurance]] · [[Allowance]] · [[CoTenancy]] · [[Responsibility]] ·
[[LeaseInfo]] · [[ExpenseRecovery]] · [[PercentageRent]] · [[Sales]] · [[SalesExclusionCap]]

Two modules with no folder of their own live here: **Expense Recovery (CAM)** and
**Variable Rent (Percentage / Use-Based) & Sales**.

What it settles:

- [[contract-lifecycle]] — the platform field has three values and the real lifecycle is a
  [[client-drop-down]].
- The [[cam-waterfall]] is recoverable **exactly** from the product's own labels, in six steps.
- **All 1,194 landed Postgres columns are `TEXT`** except 31 `VARCHAR(64)` keys — everything must be
  parsed on ingest ([[rule-CON-R-131]]). That is a direct hazard against ASG Edge+'s Constitution
  §4.4 `BigDecimal` rule.
- **Five independent date axes must coexist**: posting, effective, due, coverage, settlement
  ([[rule-CON-R-103]]).

The module's highest-risk rule is [[rule-CON-R-058]] — percentage-rent tiering, **Inferred**.

Rules: [[rules-contracts]] · [`modules/contracts/`](../../docs/modules/contracts/README.md)
