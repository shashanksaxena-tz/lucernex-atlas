---
title: PaymentReceipt
tags: [entity, accounting]
evidence: Observed
---

**`payment_receipt` · 21 fields · [[module-accounting]]**

Money received — the inverse of [[PaymentTransaction]]. Relevant because a [[Contract]] can be both
payable and receivable: direction is carried **per clause and per transaction**, never on the contract
([[rule-CON-R-019]]).

**Nothing joins a receipt to the transaction it settles** ([[rule-CON-R-118]]). There is no FK and no
link table, only allocated/unallocated totals. If ASG Edge+ needs cash application, it is building it,
not migrating it.
