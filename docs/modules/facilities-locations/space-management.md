# Space Management — `Space` and `Tenant`

**Stated up front.** `Space` is a leasable subdivision of a `Facility` — a floor, suite or room —
and `Tenant` is who occupies one. Both are ordinary `entity_scoped` children (soft `ProjectEntityID`
plus hard typed FKs), not `ProjectEntity` subtype roots — neither appears in
[`../../data-model/project-entity.md`](../../data-model/project-entity.md)'s nine-subtype list, and
neither carries the shared identity block. This is the multi-tenant-building layer sitting one
level below the Facility/Location split documented in
[`location-vs-facility-vs-site.md`](location-vs-facility-vs-site.md).

## 1. `Space` — 27 fields

| Column | Type | Required? | Reading |
|---|---|---|---|
| `FacilityID` | `Facility ID` | **Yes** | A Space always belongs to exactly one Facility. |
| `ContractID` | `Contract ID` | No | A Space may be tied to the lease that occupies it — optional, so a Space can be defined before any lease references it. |
| `ProjectEntityID` | `Entity ID` | — | The generic attachment column, present alongside the two hard FKs above. |
| `SpaceName`, `FloorNumber`, `SuiteNumber`, `RoomNumber` | Text | — | The physical subdivision's identity. |
| `GrossArea`, `RentableArea`, `UsableArea` | Number | — | The same three-way area split used at Facility/Location level, repeated here at the sub-Facility granularity. |
| `TotalHeadCount` | Number | — | Occupancy capacity for this specific space. |
| `CodeSpaceGroupID`, `CodeSpaceStatusID`, `CodeSpaceTypeID`, `CodeSpaceUseID` | Dropdown | — | The same four-way category/status/type/use classification pattern seen on `Facility` and `Location`. |

Source: `_lucernex_objects_summary.txt` and
[`../../data-fields/space.md`](../../data-fields/space.md) (26 of 27 schema fields exposed in the
admin catalog — the closest match of any object in this module, per
[`data-model.md`](data-model.md#5-schema-export-vs-admin-data-fields-catalog--a-real-divergence-and-what-it-means)).
**Observed.**

`003`'s navigation confirms this is a real, named feature: Facility's own group list includes
**`Space Management`** as a distinct entry alongside Details, Demographics, Asset Management,
Facility Expense, Pro Forma Lease and Responsibilities
([003](../../screens/003-main-navigation.md)). No screen inside that group has been opened, so the
actual list/detail rendering of Space Management remains unobserved.

## 2. `Tenant` — 42 fields

| Column | Type | Required? | Reading |
|---|---|---|---|
| `SpaceID` | `Space ID` | **Yes** (Derived — the FK type is present and every Tenant field is scoped around occupying one) | A Tenant occupies exactly one Space. |
| `ContractID` | `Contract ID` | No | The lease under which this occupant sits — a Tenant can exist as a record before/without a Contract link. |
| `CompanyID` | `Employer ID` | No | The occupant company. This is the same `Employer` table that stands in for landlord/tenant/vendor alike ([`../../admin/009-related-fields-and-data-model.md`](../../admin/009-related-fields-and-data-model.md)) — confirming a lease "Tenant" here is not a separate party type, it is an `Employer` playing the tenant role. |
| `OrganizationID` | `Organization ID` | No | The internal operating-company link, same column family as on `Location`. |
| `HeadCount1..4`, `Capacity1..4`, `TotalCapacity`, `math_calcTotalCapacity_1` | Number | — | Four parallel headcount/capacity slots plus a computed total — likely a multi-period or multi-shift capacity tracking pattern (warehouse/DC staffing), not a single static number. **Inferred** — no screen observed to confirm what the four slots represent. |
| `MoveInDate`, `MoveOutDate`, `EffectiveDate` | Date | — | The occupancy period. |

Source: `_lucernex_objects_summary.txt`. **Observed** for all columns; the four-slot
headcount/capacity reading is **Inferred**.

**Domain reading, flagged as Inferred.** The captured tenant is `(ASG)American Freight`
([003](../../screens/003-main-navigation.md), [009](../../admin/009-related-fields-and-data-model.md)) —
a large-format retailer/distribution operator. Four parallel `HeadCount`/`Capacity` slots on a
sub-Facility occupancy record is a plausible fit for tracking staffing across shifts or departments
within one distribution-center space, but this corpus has no screen capture of the `Tenant` record
to confirm it, and the same fields would read equally well as a generic multi-scenario planning
pattern unrelated to that one tenant's business.

## 3. What Space Management is *for*

Putting `Space` and `Tenant` together with their FKs: a `Facility` (building) can be subdivided into
multiple `Space` records (floors/suites), each of which can independently be tied to a `Contract`
(the lease covering that space) and can host a `Tenant` occupant tied to a different `Employer`. This
is the schema's answer to **multi-tenant occupancy inside one building** — a shopping-center anchor
space and three in-line stores inside the same Facility, for example, each its own Space/Tenant/
Contract combination, all children of the one Facility record.

That reading is corroborated structurally: `Complex` (the shopping-center container,
[`location-vs-facility-vs-site.md`](location-vs-facility-vs-site.md)) carries `NumberStores`,
`GLAExcludingAnchors`, `HasFoodCourt`, `NotableTenants` — genuinely multi-tenant-mall vocabulary —
and `Space`/`Tenant` are the row-level mechanism that would populate a "how many stores, how much
area each" answer for a Complex, even though no FK directly connects `Complex` to `Space`.
**Derived**, not directly observed as a join.

## Open questions

1. **What does the Space Management screen list actually render?** Not captured; Facility's own
   group in [003](../../screens/003-main-navigation.md) names it but no screen inside it was opened.
2. **What do the four `HeadCount`/`Capacity` slots on `Tenant` represent?** (§2)
3. **Is there a reporting rollup from `Space`/`Tenant` up to `Complex`'s `NumberStores` and
   `GLAExcludingAnchors` fields**, or are those Complex fields maintained by hand?
