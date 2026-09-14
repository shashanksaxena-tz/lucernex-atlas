---
title: Code tables — the 207 platform drop-downs
tags: [concept, configuration, reference-data, core]
evidence: Observed
---

Every platform drop-down in Lx is a set of rows in one generic editor (`FirmCodeEdit.jsp`),
discriminated by a numeric **`TableType`**. There are **207** of them, and both tenants carry the same
207 with the same ids and names — see [[finding-platform-seeded-by-id]].

- Ids fall in two bands: `2000`–`2190` (**190** tables) and `3000`–`3016` (**17**).
- The **3000 band is behaviour-bearing**. `Expense Type` (`3013`) is the exemplar: `CodeExpenseType`
  carries 31 fields including `CodeSLScheduleID`, `CodeASC842ScheduleID`, `CodeIFRS16ScheduleID` —
  **choosing an expense type is choosing which accounting schedules the money flows into**. A row is a
  routing decision, not a label.
- **The band hypothesis is refuted as a general rule.** Schedule-type tables `2161`–`2163` (24 fields
  each) and `Issue Type` `2035` (19 fields) are 2000-band yet behaviour-bearing, while `Sales Type`
  (`3012`) is a bare lookup. The band is probably a registration-order artefact.
- `2090` is absent from the sequence — inferred retired.
- The value census across all 207 at [[tenant-american-freight|AF]]: **73 populated, 134 empty, 1,140
  values**. Three tables hold 56% of them.

**Deletability is a per-row server-supplied boolean**, `isReadOnlyRecord`, read straight out of the
grid renderer. There is no count, no threshold, no usage lookup — see
[[finding-no-where-used-precedent]], which retracts an earlier and load-bearing inference.

A separate registry, [[client-drop-down|Client Drop Downs]], holds the firm's own tables. The two are
different screens over different stores, not two views of one thing.

Source: [`data-model/code-table-registry.md`](../../docs/data-model/code-table-registry.md) ·
[`features/drop-downs-code-tables/`](../../docs/features/drop-downs-code-tables/README.md)
