---
title: Equipment contracts
tags: [feature, equipment, contracts]
evidence: Observed
---

Concept: [[equipment-contract]]. Caveat: [[caveat-one-equipment-contract]].

Root `PageLayoutID 41087` — **5 groups, 26 leaf screens, 32 nodes**, ids in the platform-seeded band
and in neither tenant's layout registry.

- **24 of 26 screens are name-identical to a [[Contract]] screen**; 2 are renames
  (`Recurring Payments`, `Equipment Contract Reports`). **No new screen kind.**
- **No `EquipmentContract` table exists** — not in the 223-object census, the 227-table picker, or the
  25 refused tables. `GET /rest/businessObject/EquipmentContract` returns 2,017 links to the same
  [[Contract]] records: an alias. `EquipContract` 400s.
- **All 32 nodes carry zero [[PageLayoutField]] rows.** The whole module renders from platform
  defaults; nothing has been configured.
- [[tenant-american-freight|AF]] carries the entire menu structure (id `41087`, 64 nodes) and
  `Allow Equipment Contracts? = Yes`, and **does not render it** — which is how
  [[finding-root-renders-iff-record-exists]] was finally arrived at, after page access was tested
  across all ten user classes and ruled out too.

Screens: [[screen-eq-details-summary]] · [[screen-eq-abstract-details]] ·
[[screen-eq-payment-details]] · [[screen-eq-accounting-details]]

Open: [[q-bbw-02-capital-lease-test]] · [[q-bbw-05-equipment-contract-type]]

[`features/equipment-contracts/`](../../docs/features/equipment-contracts/README.md)
