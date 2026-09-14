---
title: The contract lifecycle
tags: [concept, contracts, core]
evidence: Observed
---

The platform's `Contract Status Code` (`TableType 2094`) carries exactly **three** values —
`Active`, `AI Abstracted`, `Inactive` — in both tenants. None of them is a BRD-24 lifecycle stage, and
that mismatch was an open question for most of this corpus's life.

**It does not have to match, because ASG tracks the lifecycle in a field it defined itself.**
`Lease Status` is a [[client-drop-down]], not a platform table, and at [[tenant-bbw|BBW]] it carries
seven values:

`Open` · `Possession` · `Possession - Paying Rent` · `Closed` · `Closed - Active` ·
`Future Possession` · `Accounting Purposes Only`

| BRD-24 stage | In `Lease Status` |
|---|---|
| Open | `Open` — exact |
| Active | **absent standalone** (only inside the compound `Closed - Active`) |
| Possession | `Possession` — exact |
| Paying Rent | `Possession - Paying Rent` — compound |
| Closed | `Closed` — exact |

Both fields render side by side on a contract record, and **the record's breadcrumb header ends with
the `Lease Status`, not the contract status** — see [[screen-contract-summary]].

**The detail that matters most:** [[finding-lifecycle-has-no-ordering]] — `SortOrder` is null on every
value, so the drop-down renders alphabetically and the sequence exists only as convention in users'
heads. The platform stores no ordering, no transitions, no state machine.

Source: [`tenants/bbw-vs-american-freight.md` §23](../../docs/tenants/bbw-vs-american-freight.md) ·
[`modules/contracts/contract-hierarchy.md`](../../docs/modules/contracts/contract-hierarchy.md)
