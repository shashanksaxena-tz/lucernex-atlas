---
title: Virtual projections
tags: [concept, data-model, accounting]
evidence: Derived
---

Thirteen objects named `Virtual*` are **computed projections — views or generated result sets, not
persisted tables**. The test is decisive:

| Test | `Virtual*` (13) | Every other object |
|---|---|---|
| Has a `<ObjectName>ID` primary key | **0 of 13** | 147 of 210 do |
| Has any audit column | **0 of 13** | 173 of 210 do |
| Has `BOMapClientRecordID` | **0 of 13** | 141 of 210 do |

A persisted table has a key and a modification stamp. Not one of these has either.

Three shapes:

- **Period expansion (7)** — [[VirtualSalesPeriod]] (66 fields), `VirtualUsagePeriod` (66),
  [[VirtualPercentageRentPeriod]] (38), `VirtualUseBasedRentPeriod` (23), `VirtualPRAccrualPeriod` (20),
  `VirtualExpenseForecastPeriod` (20), `VirtualExpAccrualForecastPeriod` (13). Always `ContractID` plus
  a period window plus computed amounts. **246 fields of pure calculation output** — reading them as
  schema would be a serious mistake.
- **Aggregate (2)** — `VirtualPRPAggregate`, `VirtualUBRPAggregate`.
- **Template applicability (4)** — `VirtualTemplateBudget`, `VirtualTemplateBudgetOption`,
  `VirtualTemplateFolder`, `VirtualTemplateSchedule`, each carrying the same 11 `IsValidFor*` flags as
  [[CodeIssueType]].

The corpus treated them as internal machinery until two of them turned up as the **primary table of
user-facing screens** — see [[finding-layouts-over-projections]]. That makes them a direct constraint
on the layout engine, and raises [[q-bbw-11-virtual-layout-writable]].

Source: [`data-model/foreign-key-graph.md`](../../docs/data-model/foreign-key-graph.md)
