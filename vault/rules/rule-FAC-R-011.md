---
title: "FAC-R-011 — Parcel and Contract share a master/sub pattern"
tags: [rule, facilities-locations]
evidence: Observed
---

**`FAC-R-011`** · [[module-facilities-locations]] · **Observed**

`Parcel.MasterParcelID` mirrors `Contract.MasterContractID` **exactly** — the same self-referencing
master/sub shape on two unrelated [[subtype-root|subtype roots]]. See [[Parcel]] · [[Contract]].

See [[rules-facilities-locations]] for the full register.
