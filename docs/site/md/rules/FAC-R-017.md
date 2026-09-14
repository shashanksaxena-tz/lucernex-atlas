# FAC-R-017 — A Tenant must belong to exactly one Space

*Facilities, Locations & Sites · Derived*

**Input: `Tenant.SpaceID`, typed `Space ID`. Confidence: Derived — the FK type is declared and every `Tenant` field (headcount, capacity, move-in/out dates) is scoped around occupying one space;.**

Input: `Tenant.SpaceID`, typed `Space ID`. Confidence: Derived — the FK type is declared and every `Tenant` field (headcount, capacity, move-in/out dates) is scoped around occupying one space; the Data Fields catalog for `Tenant` was not captured separately to confirm the `Required` flag directly.

## What it constrains

[Tenant](../entities/Tenant.md)

Columns named: `Tenant.SpaceID`

## Confidence

Derived — the FK type is declared and every `Tenant` field (headcount, capacity, move-in/out dates) is scoped around occupying one space; the Data Fields catalog for `Tenant` was not captured separately to confirm the `Required` flag directly

---

Source: `docs/modules/facilities-locations/rules.md`
