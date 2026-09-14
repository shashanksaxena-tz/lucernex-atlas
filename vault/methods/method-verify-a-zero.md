---
title: "Method: verify a zero three ways"
tags: [method, meta]
evidence: Observed
---

A **false zero** is the obvious failure mode when an entire finding rests on one count being zero —
and [[finding-root-renders-iff-record-exists]] rests on
[[tenant-american-freight|American Freight]] holding **zero** Equipment Contracts.

It was verified three independent ways:

1. **The type scan** — `GET /rest/businessObject/Contract/details?fields=ProjectEntityTypeName&$top=5000`,
   counted format-agnostically because BBW answered JSON on one call and XML on another.
2. **The dedicated endpoint** — `GET /rest/businessObject/EquipmentContract` returns `HTTP 200` with
   zero rows, against `HTTP 400 unknown objectType` for `Site`, `Equipment` and `OpeningProject`.
   **Not-provisioned and not-populated are distinguishable**, and this proves AF is the latter — which
   also eliminated type registration as the candidate gate.
3. **A spelling control** — `Equipment%20Contract` returns `400 unknown objectType`, proving the
   no-space form is the right one and the zero is real rather than a typo.

**[[fiql|FIQL was deliberately not used]]**: a malformed or unmatched filter returns `{}`, which is
exactly the shape of a correct empty result.

The general form: **a zero from one method is a hypothesis. A zero from three methods, one of which
distinguishes "absent" from "unregistered", is evidence.**

See [[method-cheap-signals]]
