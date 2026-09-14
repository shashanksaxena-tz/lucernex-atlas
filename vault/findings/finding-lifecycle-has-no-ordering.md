---
title: The contract lifecycle is a drop-down with no stored ordering
tags: [finding, contracts, core]
evidence: Observed
---

The [[contract-lifecycle]] lives in `Lease Status`, a **firm-defined [[client-drop-down]]**
(`CustomCodeTableID 7727`) with seven values at [[tenant-bbw|BBW]] — not in the platform's
three-value `Contract Status Code`.

> **`SortOrder` is null on every value, so the drop-down renders alphabetically.**

The sequence `Open → Possession → Paying Rent → Closed` exists **only as convention in users' heads**.
The platform stores **no ordering, no transitions, and no state machine.**

**A rebuild that models this as an ordered state machine is adding structure the source system does
not have** — which may well be the right thing to do, but it is a **decision, not a migration**, and
it needs stating as such.

Four of BRD-24's five stages are present, one only as a compound (`Closed - Active`), plus two stages
the BRD does not name (`Future Possession`, `Accounting Purposes Only`). **Close to the BRD, not
identical with it** — and the tenant's real lifecycle is the one in production, so this belongs in
front of whoever owns BRD-24.

Anyone with drop-down rights can add an eighth value or rename `Active` tomorrow.

Open: [[q-bbw-20-lease-status]] ·
Source: [`tenants/bbw-vs-american-freight.md` §23](../../docs/tenants/bbw-vs-american-freight.md)
