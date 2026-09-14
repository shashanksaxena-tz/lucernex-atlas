---
title: The lease-accounting engine runs per asset, not only per lease
tags: [finding, accounting, assets, core]
evidence: Observed
---

[[ContractFinancialTest]], [[SLSummary]] and [[SLPeriod]] **each carry a nullable foreign key straight
to [[Asset]]**. So a schedule can be measured against an equipment asset, not only against a
[[Contract]].

That was the schema-side evidence. [[tenant-bbw|BBW]] then showed the same thing **from the front**:
the [[equipment-contract|Equipment Contract]] root exposes it as a first-class navigation root with 26
screens, keeping the **entire** ASC 842 / IFRS 16 / straight-line engine and dropping every
retail-property layer. **Confirmed by construction.**

[[Asset]] also carries **its own 13-field classification overlay**, parallel to [[Contract]]'s
([[rule-AST-R-004]]), and `Asset.AccountingBeginDate`/`EndDate` **override** the window derived from
[[ExpenseSchedule]] rows ([[rule-AST-R-005]]).

> **Which overlay wins when both the Contract's and the Asset's are populated is Inferred and
> unresolved.** That is a real gap for a rebuild: it decides the classification of every
> equipment lease.

For ASG Edge+ the consequence is scoping. If the accounting engine is built as *"schedules hang off
contracts"*, equipment leases will not fit, and the incumbent's own product line shows they are
expected to.

See [[one-engine-three-standards]] · [[module-assets-equipment]]
