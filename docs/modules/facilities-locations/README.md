# Facilities, Locations & Sites — module overview

**Stated up front.** This module is the physical real-estate register: **20 objects, 918 fields**,
built around four independently-ownable `ProjectEntity` subtype roots — `Facility`, `Location`,
`Parcel`, `Prototype` — plus a shared optional container (`Complex`), a sub-Facility occupancy layer
(`Space`/`Tenant`), and a site-selection/demographics family with no ASG Edge+ counterpart today.
**The central finding: `Location` is the retail site/"Center"; `Facility` is the building on it.**
A Location can hold more than one Facility; a Facility belongs to exactly one Location
(`Facility.LocationID` is required; `Location` has no reverse pointer at all). `Complex` is an
optional physical grouping *above* both — a shopping-mall/campus record that a Location, Facility,
Parcel or Prototype may join, itself parentless. `Parcel`'s mandatory containment parent is the
**Location**, not the Facility, and it is the sole attachment point for the entire property-tax
subsystem. `Prototype` is not a place at all — a reusable design template a Facility can be built
from. **"Site" is not one of this module's objects** — it is `PotentialProject`, which lives in
`portfolio-transactions`, the pre-development pipeline before any of the above exists. Full argument
in [`location-vs-facility-vs-site.md`](location-vs-facility-vs-site.md).

*Evidence class for this paragraph: **Observed** FK types and required/optional flags from
`_lucernex_objects_summary.txt` and the per-entity Data Fields catalogs
([`../../data-fields/`](../../data-fields/)); the containment reading is **Derived** from that FK
direction, corroborated independently by two unrelated sources — a field-naming convention
(`EDGE_ASGCenterID`, `Firm_CenterName`) and a live menu label ("Complex/Center Details") — cited in
full in [`location-vs-facility-vs-site.md`](location-vs-facility-vs-site.md).*

## The module at a glance

| Property | Value |
|---|---|
| Objects | 20 |
| Fields | 918 |
| `ProjectEntity` subtype roots in this module | 4 of 9 — `Facility`, `Location`, `Parcel`, `Prototype` |
| Firm-global reference objects | 6 — `Complex`, `DMA`, `DemographicReport`, `DemographicFact`, `DemographicStudyArea` (+`Region`, out of module) |
| Entity-scoped children | 10 |
| Internal FK edges | 23 |
| Inbound cross-module edges | 34 (from 7 distinct source objects — see [`data-model.md`](data-model.md#31-inbound-34-columns-but-only-7-distinct-source-objects)) |
| Outbound cross-module edges | 82 |
| End-user screens (from [003](../../screens/003-main-navigation.md)) | Facility 16, Location 12 |
| Dashboard heading | Portfolio Administration |

## The containment hierarchy

```
                    Program (Portfolio)
                   /   |    |    \
             Location Facility Parcel Prototype     ← all four required to belong to a Program
                 \      |      /   |
                  \     |     /    |
                   Complex (optional, shared, parentless)
                        |
         Location ──required──▶ Facility ──required──▶ Space ──required──▶ Tenant
                                    │                       │
         Location ──required──▶ Parcel ◀──optional──── Facility
                                    │
                          PropertyTax* (6 objects, property-tax module)

         Contract ─┬─optional,direct──▶ Facility
                    └─optional,direct──▶ Location        (not forced through one another — FAC-R-012)
```

Full FK-by-FK evidence and a Mermaid ER diagram: [`data-model.md`](data-model.md#6-the-containment-diagram).

**Two-parent and no-parent cases, stated explicitly** (per
[`location-vs-facility-vs-site.md`](location-vs-facility-vs-site.md) §4): `Parcel` can carry up to
five simultaneous optional parents at once (`Facility`, `Contract`, `Complex`, `Prototype`,
`Organization`) on top of its required `Location`/`Program` — the most cross-linked object in the
module. `Complex` has none — it sits at the top of the physical axis with zero outbound FKs of its
own.

## Which four are `ProjectEntity` subtypes, and why it matters

`Facility`, `Location`, `Parcel` and `Prototype` are 4 of the 9 subtype roots identified in
[`../../data-model/project-entity.md`](../../data-model/project-entity.md) — each carries the
supertype's shared identity block on a shared key (`ProjectEntityID` typed `Number`, not `Entity
ID`), which is what buys every one of them, for free, the universal tab strip
[003](../../screens/003-main-navigation.md) observed on every entity root: `Summary`,
`Members/Contacts`, `Forms`, `Work Flow`, `Documents`, `Binders`, plus `Schedule`/`Budget` where
applicable. **Building any of the four as an unrelated aggregate means building those six
capabilities again, once per entity — the same warning `project-entity.md` gives for the product as
a whole.** `Space`, `Tenant`, and every other object in this module are ordinary `entity_scoped`
children, not subtypes — they attach via a soft `ProjectEntityID` plus, in most cases, a hard FK to
their real parent.

## The Facility ↔ Contract relationship

**Asymmetric by cardinality, and the UI reflects it correctly on both sides** — this module's
half of the finding [009](../../admin/009-related-fields-and-data-model.md) already established
from the Contract side. `Contract.FacilityID` and `Contract.LocationID` are both present, both
optional, and independent of one another (`FAC-R-012`) — a lease is not forced to reach a Location
by first going through a Facility. From the other direction, `Facility`'s own Related Fields sidebar
never offers `Contract` as a lookup at all; the Facility Summary layout instead embeds an **"ASG
Contract List (One to Many List)"** child grid (`FAC-R-013`). Two structurally independent tools —
the Page Layout builder's sidebar contents and the routing/screen evidence — agree on the same
asymmetry.

## Space Management, briefly

A `Facility` can be subdivided into `Space` records (floor/suite/room), each optionally tied to the
`Contract` covering it, each able to host a `Tenant` occupant linked to a different `Employer`. This
is the schema's mechanism for multi-tenant buildings — a shopping-center anchor plus several in-line
stores inside one `Facility`, each its own Space/Tenant/Contract combination. Full detail:
[`space-management.md`](space-management.md).

## Demographics & site selection, briefly

Nine objects split into a reusable reference layer (`DMA`, `DemographicStudyArea`,
`DemographicReport`, `DemographicFact` — all firm-global) and a per-site evaluation layer
(`Competitor`, `SiteSurvey`, `DemographicResults`, `LandPurchaseSummary`,
`LinkLandPurchaseInspection` — all soft-attached via `ProjectEntityID`). This family has **no
counterpart anywhere in ASG Edge+ today**, and it carries its own internal redundancy —
`SiteSurvey`'s fixed 1/3/5-mile bands versus `DemographicStudyArea`'s configurable radius — that a
rebuild should resolve rather than reproduce. Full detail: [`demographics.md`](demographics.md).

## Contents

| Document | Answers |
|---|---|
| [`data-model.md`](data-model.md) | Every object, field count, role classification, the full 23-edge internal FK graph, the cross-module inbound/outbound edges, and the schema-vs-admin-catalog divergence. |
| [`location-vs-facility-vs-site.md`](location-vs-facility-vs-site.md) | **The central question of this module** — what each of Location/Facility/Complex/Parcel/Prototype actually is, worked out from the FK graph and corroborated two independent ways. |
| [`space-management.md`](space-management.md) | `Space` and `Tenant` — the sub-Facility occupancy layer. |
| [`demographics.md`](demographics.md) | The site-selection/demographics family, its reusable-vs-per-site split, and its internal redundancy. |
| [`rules.md`](rules.md) | `FAC-R-001`…`FAC-R-020` — every rule in trigger/input/effect/confidence form. |
| [`asg-edgeplus-mapping.md`](asg-edgeplus-mapping.md) | What exists (nothing), what must be built, what should deliberately differ, and — concretely — how this module's evidence resolves the open Hub/Spoke `Location` conflict raised in `project-entity.md`. |

## What a rebuild must not get wrong

1. **`Location` is the site/"Center"; `Facility` is the building on it — not the other way round,
   and not synonyms.** `Facility.LocationID` is required; `Location` carries no reverse pointer.
   `FAC-R-001`, `FAC-R-002`.
2. **A Parcel's real parent is the Location, not the Facility.** `Parcel.LocationID` is required;
   `Parcel.FacilityID` is optional. A rebuild that nests Parcel under Facility will misrepresent
   every parcel of land that has no building on it yet. `FAC-R-005`.
3. **"Site" is `PotentialProject`, a different module, not a sixth member of this hierarchy.**
   Confirmed absent from this module's object list and cross-checked against
   [`../../data-model/project-entity.md`](../../data-model/project-entity.md) §2.
4. **`Complex` is optional everywhere and required nowhere.** Do not model it as a mandatory parent
   of Location/Facility/Parcel/Prototype. `FAC-R-008`, `FAC-R-009`.
5. **Property tax attaches only to `Parcel`.** All six `PropertyTax*` objects FK to `Parcel` alone —
   never `Facility`, never `Contract`. `FAC-R-014`.
6. **Contract reaches Facility and Location independently, and the reverse is a child grid, not a
   lookup.** `FAC-R-012`, `FAC-R-013`.
7. **`Prototype`'s Location/Complex/DMA columns exist in the schema but are not exposed as
   admin-configurable Data Fields**, unlike the identical columns on `Facility`/`Location`/`Parcel`.
   Whatever mechanism actually sets them was not captured. `FAC-R-019`.
8. **The demographics family has two independent, unreconciled ways to define a trade area** —
   `SiteSurvey`'s fixed mile-bands and `DemographicStudyArea`'s configurable radius. Do not build
   both. `FAC-R-020`.

## Open questions

Ranked by how much each blocks a rebuild decision.

1. **Is `Location` a Hub or a Spoke concept in ASG Edge+?** This module's evidence — per-Portfolio
   scoping, tax rates, an `Organization` link — argues for Spoke, with only a thin geography/address
   master staying in the Hub. See [`asg-edgeplus-mapping.md`](asg-edgeplus-mapping.md) §2 for the
   full argument. Not yet signed off by whoever owns the Hub/Spoke boundary.
2. **What does `Facility.UseLocationAddress = true` actually render?** No `Summary` screen for
   either entity has been captured yet.
3. **Does ASG's live tenant have any populated `Complex` records at all**, or is it vendor capability
   never exercised — the same kind of gap the accounting module found for IFRS 16?
4. **How does a `PotentialProject` ("Site") get promoted into a real `Location`/`Facility`?** Not
   captured anywhere; the single biggest open question connecting this module to
   `portfolio-transactions`.
5. **Which specific `ProjectEntity` type do the soft-attached children (`SiteSurvey`,
   `LandPurchaseSummary`, `Ownership`, `DemographicResults`) actually point at in a live record?**
   The schema permits any subtype; no screen confirms which one is used in practice.
6. **Does any approved BRD require site-selection/demographics functionality in ASG Edge+ at all?**
   Not checked in this pass — a business question, not a technical one.
7. **What does the Space Management screen list actually render**, and is there a reporting rollup
   from `Space`/`Tenant` up to `Complex`'s `NumberStores`/`GLAExcludingAnchors` fields, or are those
   maintained by hand?
