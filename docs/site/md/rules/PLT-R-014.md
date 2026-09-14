# PLT-R-014 — Single-field objects rely entirely on a join or virtual pattern for content

*Platform & Tenancy · Derived*

**These are join/marker tables or the export is truncating them; either way, do not model them as one-column tables in the rebuild without a targeted schema-browser capture.**

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | Any attempt to fully specify `EntityTemplate`, `MapClientSchedule`'s peers, `Notify`, `ScratchPad`, `AuditTable`, `Region`, `LinkPEMemberCodeJobTitle`, or `LinkRegionManager` from this export alone |
| What it reads | Each declares ≤1 stored field (`MapClientSchedule` is the exception at 10) |
| What it writes | These are join/marker tables or the export is truncating them; either way, do not model them as one-column tables in the rebuild without a targeted schema-browser capture |

## What it constrains

[EntityTemplate](../entities/EntityTemplate.md), [MapClientSchedule](../entities/MapClientSchedule.md), [Notify](../entities/Notify.md), [ScratchPad](../entities/ScratchPad.md), [AuditTable](../entities/AuditTable.md), [Region](../entities/Region.md), [LinkPEMemberCodeJobTitle](../entities/LinkPEMemberCodeJobTitle.md), [LinkRegionManager](../entities/LinkRegionManager.md)

## Confidence

Derived — `object-catalog.md`'s "18 one-field objects" note

---

Source: `docs/modules/platform-tenancy/rules.md`
