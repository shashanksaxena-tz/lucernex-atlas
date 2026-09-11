# ASG Edge+ mapping

**Stated up front.** ASG Edge+ has **nothing** in this space yet — no `Location`, `Facility`,
`Parcel`, `Complex`, `Space`, `Prototype`, or site-selection class exists in either
`ASG-Edgeplus-Configuration-Service` or the legacy monorepo (checked directly, 2026-09-11: no
`class Location`/`class Facility`/`class Parcel`/`class Complex`/`class Space` anywhere in either
codebase's source). The only trace is anticipatory: MDM-01's own decision register lists Location
and Facility as future FK targets *of* Masters, not yet as entities themselves —
`ASG-Edgeplus-Configuration-Service/docs/plans/masters-page-layout/OPEN-DECISIONS.md:483` notes
"masters referenced by Contract, Location, Facility, Asset, Covenant, KeyDate...". **This entire
module must be designed and built**, and the one open architectural conflict it surfaces —
[`../../data-model/project-entity.md`](../../data-model/project-entity.md) §5.2's disputed placement
of `Location` in the Hub — has a concrete answer proposed below.

## 1. What exists today

| ASG Edge+ artefact | What it says | Gap |
|---|---|---|
| `ASG-Edgeplus-Configuration-Service` OPEN-DECISIONS.md:483 | Names `Location` and `Facility` as entities that Masters will need to reference | No `Location`/`Facility` entity itself is defined anywhere in the codebase |
| Workspace index (`ASG/Code/CLAUDE.md`) target architecture | Puts `Location`/`Organization` in the Hub, everything under a Contract in the Spoke | Silent on `Facility`, `Parcel`, `Complex`, `Space`, `Prototype` entirely |
| `ASG-AssetStrategiesGroup-EdgePlus` monorepo | No facility/location domain classes found | Confirms this is greenfield, not a migration |

## 2. Resolving the Location-in-the-Hub conflict

[`../../data-model/project-entity.md`](../../data-model/project-entity.md) §5.2 raised this as the
single biggest open architectural question blocking either service from modelling `Location`: the
workspace index puts `Location` in the shared Hub, but Lucernex's `Location` is a `ProjectEntity`
subtype root, portfolio-scoped, carrying per-tenant operational data.

**This module's evidence resolves it in favour of option (a) from that document: ASG Edge+'s Hub
`Location` and Lucernex's `Location` are different concepts, and the Hub concept needs a narrower
name.** The evidence:

- Lucernex's `Location` is required to belong to exactly one `Program` (Portfolio) — `FAC-R-004`
  — which is per-firm, per-portfolio data. It carries `TaxRate1..4`, `EquipContractTaxRate1..4`,
  `GrossLeaseArea`, `AccountingNumber`, and a link to the operating `Organization`. None of that is
  Hub-shareable across firms; it is exactly the kind of per-tenant operational record
  database-per-tenant is meant to isolate.
- The naming evidence in [`location-vs-facility-vs-site.md`](location-vs-facility-vs-site.md) §2
  point 4 — `Firm_CenterName`, `EDGE_ASGCenterID`, and the live menu's "Complex/Center Details"
  screen — independently suggests ASG's own prior tooling already distinguished a lightweight
  geography/address master from this operational "Center" record.

**Recommendation:** split the Hub's `Location` concept into (1) a thin, genuinely shared
geography/address reference — country/state/postal-code master data, equivalent to Lucernex's
firm-global `StateProvinceCountry`/`Jurisdiction` (already `platform-tenancy` per
[`../../data-model/object-catalog.md`](../../data-model/object-catalog.md), not this module) — and
(2) a per-Portfolio operational "Center" entity matching Lucernex's `Location`, which belongs in the
Spoke alongside `Facility`, `Parcel`, and `Prototype`. This is a naming and scope decision for
whoever owns the Hub/Spoke boundary, not a code change this pass can make.

## 3. What must be built

| Lucernex object | ASG Edge+ status | Priority reasoning |
|---|---|---|
| `Facility`, `Location` | Must build | The two subtype roots every other artefact in this module and `Contract` hang off. Build order: `Location` before `Facility` (`FAC-R-001`). |
| `Parcel` | Must build | Required to attach the property-tax subsystem (`FAC-R-014`) at all; its containment parent is `Location`, not `Facility` (`FAC-R-005`) — a common modelling mistake to avoid. |
| `Complex` | Should build, lower priority | Purely optional grouping (`FAC-R-008`/`FAC-R-009`); nothing else in the module requires it to exist for `Facility`/`Location`/`Parcel` to function. Defer until it is confirmed ASG's live data actually populates it (see `data-model.md` open question 3). |
| `Space`, `Tenant` | Should build alongside Facility | Needed the moment ASG models a multi-tenant building or wants to attach a lease to a specific floor/suite rather than the whole Facility. See [`space-management.md`](space-management.md). |
| `Prototype` | Can defer | A design-template convenience, not load-bearing for any other record in the module (nothing requires a Prototype to exist). Its own Location/Complex/DMA links are themselves unresolved (`FAC-R-019`). |
| `Ownership`, `Parking`, `FacilityExpense`, `ParcelAccess` | Can defer | Straightforward child records once their required parent (`Facility` or `Parcel`) exists; low structural risk, build on demand. |
| `Competitor`, `DMA`, `SiteSurvey`, `DemographicReport`/`Fact`/`StudyArea`/`Results`, `LandPurchaseSummary`/`LinkLandPurchaseInspection` | Deliberately deferred, pending a business decision | The whole demographics/site-selection family (see [`demographics.md`](demographics.md)) has no counterpart in ASG Edge+ and no BRD checked against it in this pass. Do not build speculatively. |

## 4. What should deliberately differ

- **Do not replicate `SiteSurvey`'s fixed 1/3/5-mile bands.** If ASG Edge+ ever builds
  demographics/site-selection, build it on `DemographicStudyArea`'s parameterised radius/drive-time
  pattern instead (`FAC-R-020`). Lucernex itself carries both, unreconciled; a rebuild should not
  inherit that duplication.
- **Do not make `Prototype`'s Location/Complex/DMA relationships administrator-configurable without
  first deciding what they mean.** `FAC-R-019` documents that Lucernex itself never exposes them for
  placement — copying the schema column without copying that restriction (or resolving why it
  exists) would silently add capability nobody asked for.
- **Do not model `Complex` as a required parent of anything.** Every reference to it in Lucernex's
  schema is optional (`FAC-R-008`). Requiring it would be a stricter model than the system being
  replaced.
- **Consider whether ASG Edge+ needs the `Employer`-as-`Tenant`-occupant pattern at all.**
  Lucernex's `Tenant.CompanyID` reuses `Employer` for the occupant company, the same table that
  already stands in for landlord and vendor
  ([`../../admin/009-related-fields-and-data-model.md`](../../admin/009-related-fields-and-data-model.md)).
  That is a deliberate, load-bearing simplification worth keeping if ASG Edge+ builds
  `Space`/`Tenant` at all, rather than inventing a fourth party-role table.

## 5. Decisions blocking a build

1. **The Hub/Spoke placement of `Location` (§2)** — needs sign-off from whoever owns
   `ASG-Edgeplus-Configuration-Service`'s architecture before either `Location` or `Facility` is
   coded, since the tenancy model differs materially between the two placements.
2. **Whether `Complex` is worth building at all** — see `data-model.md`'s open question on whether
   ASG's live tenant even populates it.
3. **Whether the demographics/site-selection family is in scope for any BRD** — a business
   question, explicitly out of this pass's remit.

## Open questions

Carried forward from the other documents in this folder, ranked by how much they block a build
decision:

1. Is `Location` a Hub or Spoke concept — resolved above as a recommendation, but not yet a
   decision anyone has signed off on.
2. Does ASG's live tenant populate `Complex` at all?
3. What does `Facility.UseLocationAddress` do at render time, and does ASG Edge+ need the same
   address-inheritance behaviour?
4. Does any approved BRD require site-selection/demographics functionality?
5. How does a `PotentialProject` ("Site") get promoted into a `Location`/`Facility`, and does ASG
   Edge+ need to model that pipeline at all, or only the post-promotion state?
