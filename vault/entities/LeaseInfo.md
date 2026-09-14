---
title: LeaseInfo
tags: [entity, contracts]
evidence: Derived
---

**`lease_info` · 219 fields · [[module-contracts]]**

The third-largest object in the product and one of the strangest: 219 fields of negotiation history,
with **in-degree 0** and only two foreign keys out.

Nothing points at it and it barely points anywhere. It reads as a wide snapshot of the deal as
negotiated, kept beside the [[Contract]] rather than joined into it.

Worth flagging before any rebuild sizes the contract aggregate: 219 fields is larger than
[[Facility]], [[Location]] or [[Parcel]], and none of the corpus's screens account for it.
