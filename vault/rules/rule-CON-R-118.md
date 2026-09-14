---
title: "CON-R-118 — Nothing joins a receipt to the transaction it settles"
tags: [rule, contracts]
evidence: Observed
---

**`CON-R-118`** · [[module-contracts]] · **Observed**

**No foreign key and no link table** connects [[PaymentReceipt]] to [[PaymentTransaction]] — only
allocated and unallocated totals.

**Observed by absence, and recorded as a schema gap.** If ASG Edge+ needs cash application, it is
building it, not migrating it.

See [[rules-contracts]] for the full register.
