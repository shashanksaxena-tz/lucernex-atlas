---
title: Contract
tags: [entity, contracts, subtype-root, core]
evidence: Observed
---

**`contract_admin` + `contract_financial` + `contract_firm` + `contract_firm1` · 570 fields ·
[[module-contracts]]**

The lease header, and the centre of gravity of the whole schema: the **largest object** (7.7% of all
fields), a [[subtype-root]], third in in-degree (**61 objects, 62 columns** point at it), and the
owner of 39 navigation screens.

- **Vertically partitioned across four physical tables.** Two of them are the
  [[firm-custom-field|firm-custom]] halves: **258 of its 570 columns are `Firm_`-prefixed**, a 55:45
  global-to-firm split.
- `MasterContractID` is a self-reference — the master/sub and sublease pattern, mirrored exactly by
  `Parcel.MasterParcelID` ([[rule-FAC-R-011]]).
- It attaches to [[Facility]] and [[Location]] **independently** — neither forces traversal through
  the other ([[rule-FAC-R-012]]).
- **120 denormalised rollup fields can go stale.** Unlike [[SLSummary]] it has **no
  `NeedsRecalculation`** flag ([[rule-CON-R-026]]).
- It still carries the ASC 840 "Cap Lease Test" as `Test1Result`…`Test5bResult`, alongside the newer
  [[ContractFinancialTest]].
- Only **7** of its 307 admin-catalog columns are required, none of them a business fact
  ([[required-ness]]).

An [[equipment-contract|equipment lease]] is a `Contract` row with
`ProjectEntityTypeName = 'Equipment Contract'`. There is no separate table.

The lifecycle is not on this record in any useful form — see [[contract-lifecycle]].

Screens: [[screen-contract-summary]] · [[screen-contract-abstract-details]] ·
[[screen-contract-wizard]] · [[screen-manage-contracts]]
