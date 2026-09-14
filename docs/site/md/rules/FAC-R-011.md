# FAC-R-011 — A Parcel may subdivide from another Parcel

*Facilities, Locations & Sites · Observed*

**Input: `Parcel.MasterParcelID` (self-reference, typed `Parcel ID`). Effect: Mirrors `Contract.MasterContractID`'s master/sub pattern exactly — a parcel of land can be split, with each resulting parcel pointing back at the original.**

Input: `Parcel.MasterParcelID` (self-reference, typed `Parcel ID`). Effect: Mirrors `Contract.MasterContractID`'s master/sub pattern exactly — a parcel of land can be split, with each resulting parcel pointing back at the original. Confidence: Observed (self-reference column present; cross-referenced against the identical master/sub pattern on `Contract` in `../../data-model/foreign-key-graph.md` §2).

## What it constrains

[Parcel](../entities/Parcel.md), [Contract](../entities/Contract.md)

Columns named: `Parcel.MasterParcelID`, `Contract.MasterContractID`

## Confidence

Observed (self-reference column present; cross-referenced against the identical master/sub pattern on `Contract` in `../../data-model/foreign-key-graph.md` §2)

---

Source: `docs/modules/facilities-locations/rules.md`
