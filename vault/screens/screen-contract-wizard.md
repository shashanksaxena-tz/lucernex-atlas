---
title: "The contract creation wizard"
tags: [screen, administration,contracts,layouts]
evidence: Observed
---

`Five SUB layouts — PLIDs 98883–98887`

**The largest previously-identified gap in this corpus**: contract creation appears **nowhere in the
[[navigation-tree]]**, because the 105-screen tree is navigation *within* a record that already
exists. It is built from **sub-page layouts**.

| Step | PLID | Fields | Collects |
|---|---:|---:|---|
| 1 — Contract Summary Setup | 98883 | **35** | identity, parties, and **every critical date** |
| 2 — Contract Terms | 98884 | 10 | renewal options: count, term type, length, rentable area |
| 3 — Covenants | 98885 | 6 | **clones [[Covenant\|covenants]] from a [[contract-template\|template]]** |
| 4 — Responsibilities | 98886 | 6 | **clones [[Responsibility\|responsibilities]] from a template** |
| 5 — Expense Setup | 98887 | 22 | recurring rent/expense with escalation |

Plus `ASG Facility Wizard` (99141, 26 fields) and `ASG Location Wizard` (99142, 23 fields).

Three things that change the rebuild picture:

1. **[[finding-wizard-writes-two-entities]]** — step 1 carries `Facility_OpenDate` and
   `Facility_CloseDate`.
2. **Steps 3 and 4 are template cloning, not data entry** — and **no `ContractTemplate` object exists**
   ([[q-bbw-09-contract-templates]]).
3. **[[finding-computed-fields-render-as-prose]]** — `TermLength` and two `Firm_` date fields render as
   `input[type=hidden]`.

Field naming is `{Entity}_{Column}`, and firm-custom fields are `{Entity}_Firm_{Column}` — step 1 alone
carries **eight** of them, which is a third independent confirmation of
[[finding-firm-fields-are-physical-columns]].

**Live data volumes** (Derived, from select option counts): 2,191 master contracts, 2,141 locations,
2,062 facilities, 151 expense types, 166 currency types.

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
