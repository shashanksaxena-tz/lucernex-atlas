# The site pipeline — how a `PotentialProject` becomes a `Facility`

**Stated up front.** The schema names the pipeline but does not show its mechanism. **Best answer:
Site (`PotentialProject`) → Project (`Project`, typed `Opening Project`) → Facility, in two
distinct steps, each configured by its own dedicated page layout on `Program` — but only the
*second* step (`Project` → `Facility`) is backed by an actual, admin-labelled foreign key.** The
first step (`PotentialProject` → `Project`) is unconfirmed: no column anywhere in the 7,421-field
schema links a `Project` back to the `PotentialProject` it came from. **Confidence: Derived for the
sequence and the second step; genuinely Inferred/unconfirmed for the first step and the copy
mechanism.** This is honestly the corpus's ceiling on this question — it does not settle further.

## 1. The evidence, in the order it forces the conclusion

### 1.1 `PotentialProject` is an island — no inbound FK, no admin exposure

`PotentialProject` ("Site" in the `walkHierarchy` enumeration,
[`project-entity.md`](../../data-model/project-entity.md) §1.5) is a `ProjectEntity` subtype root
with 108 raw schema fields. Two facts bracket it:

| Fact | Evidence |
|---|---|
| **Zero objects anywhere in the 972-edge graph carry a foreign key pointing at `PotentialProject`.** | `docs/mindmap/edges.json`, filtered for `target_object == "PotentialProject"` — empty. **Observed.** |
| **Zero rows for `PotentialProject` exist in the Manage Data Fields admin catalog**, out of 6,158 total leaves. | `grep -c "^PotentialProject," docs/data-fields/all-fields.csv` → `0`. **Observed.** |

Both facts together mean: nothing in the schema *shows its work* when a Site stops being a Site.
There is no `PotentialProjectID` column on any other object, no `IsPromoted` flag, no status value
captured, and no admin-configurable field an implementer could point to as "the one that changes."
Compare this to `Prototype`'s partial admin-exposure gap
([`../facilities-locations/README.md`](../facilities-locations/README.md) finding 7) — this is the
same shape of gap, but total rather than partial.

### 1.2 `Program` carries two page-layout fields that name a two-step conversion, and only two

A full-text search for `ToProject`, `ToFacility`, `ToLocation`, `ToPotential`, `Promote`, and
`Convert` across every field name in `_lucernex_objects_summary.txt` returns exactly two hits,
**both on `Program`, and on no other object**:

```
SiteToProjectSetupLayoutID       (item ID)
ProjectToFacilitySetupLayoutID   (item ID)
```

Contrast this with the eleven ordinary `<Subtype>SetupPageLayoutID` columns on `Program`
(`ContractSetupPageLayoutID`, `FacilitySetupPageLayoutID`, …) and the matching eleven on `Firm`
([`project-entity.md`](../../data-model/project-entity.md) §3) — each of those names *one* subtype's
own detail-page layout. These two name a *transition between two subtypes*, and their pairing —
`Site → Project`, then `Project → Facility` — is exactly the two hops needed to connect
`PotentialProject` to `Facility`. **Observed** field names; **Derived** that they represent a
sequential, two-step pipeline rather than two independent, unrelated layouts.

**Why a page layout, and not a workflow or a status flag?** The GraphQL `KickOffMethod` enum
declares `PAGE_LAYOUT` as one of four ways a workflow can be triggered
([`graphql-api.md`](../../data-model/graphql-api.md)) — "from a page layout, i.e. a button placed on
a form." A `*SetupLayoutID` column pointing at a layout that itself hosts a business-action button
is consistent with the whole platform's own trigger vocabulary. **Inferred** — no screen was
captured showing either layout's actual buttons.

### 1.3 `Project.FacilityID` is a real, admin-labelled, optional FK — the second step is confirmed

`Project` (the schema object behind both "Capital Project" and "Opening Project" — see §3) carries
`FacilityID`, typed `Facility ID`. This is not a hypothesis from the raw dump alone: the Manage Data
Fields admin catalog exposes it, labelled by the vendor itself:

| Label | Internal Name | Type | Required |
|---|---|---|---|
| **Related Project Facility** | `FacilityID` | `sTYPE_FACILITY` | **No** |

*(`docs/data-fields/all-fields.csv`, `Project` rows — **Observed**.)*

That is a genuine, optional, forward-pointing link from a `Project` to an existing `Facility`. It is
the one piece of this whole pipeline with a real column behind it, and it is enough on its own to
say: **a `Project` can name the `Facility` it is building, expanding, or associated with, and the
vendor's own label calls that relationship exactly what it looks like.** `Project.LocationID`
(typed `Location ID`) also exists in the raw schema export but is **not** exposed in the admin
catalog at all — present in the physical schema, invisible to a tenant admin, same asymmetry
pattern as `PotentialProject` itself. **Observed** for both columns' existence; **Derived** for the
significance of one being admin-exposed and the other not.

### 1.4 `Project.ProjectType`'s own label confirms the discriminator `project-entity.md` could only infer

[`project-entity.md`](../../data-model/project-entity.md) §6 (open question 4) flagged that
"Capital Program vs. Portfolio both mapping to `Program`" and "RE Contract vs. Equipment Contract
both mapping to `Contract`" needed confirming, not assuming — the same question applies to
`Project`/"Capital Project"/"Opening Project". The admin catalog settles the `Project` half
directly:

| Label | Internal Name | Type | Required |
|---|---|---|---|
| **Opening Project or Capital Project** | `ProjectType` | `sTYPE_TEXT` | **Yes** |

*(`docs/data-fields/all-fields.csv` — **Observed**.)* The vendor's own field label states the two
values in plain English. **This is the first of `project-entity.md`'s four unresolved subtype-name
questions to get a direct, textual confirmation** rather than an inference from the `IsValidFor*`
flags or the `walkHierarchy` dropdown.

Corroborating this from a second, independent angle: `Program` carries separate rollup counters
`TotalOpeningProjects` and `TotalCapitalProjects` (alongside `TotalSites`, `TotalFacilities`,
`TotalProjects`, and seven more) — the platform counts these as two distinct populations at the
portfolio level, not one. **Observed**, `_lucernex_objects_summary.txt`.

**Reading `ProjectType`'s two values against the pipeline:** an "Opening Project" is the natural
reading of *the project of opening a new store* — the phase immediately after a Site is selected,
before the store exists as an operating `Facility`. A "Capital Project" is the natural reading of
*capital work on a facility that already exists* — a remodel, an expansion, a capital improvement.
That split lines up cleanly with `SiteToProjectSetupLayoutID` (Site becomes an *Opening* Project)
and a separate life for Capital Projects that never touch `PotentialProject` at all. **Inferred** —
plausible from field naming and rollup structure, not confirmed by any screen showing
`ProjectType`'s actual stored values.

## 2. What is and is not confirmed, stated plainly

| Link in the chain | Confirmed by a hard FK? | Confirmed by anything else? |
|---|---|---|
| `PotentialProject` → `Project` | **No.** No column on `Project` is typed `Site ID` or `PotentialProject ID`; `Project.PotentialProjectName` is a plain `Text` denormalised display field, part of the shared `ProjectEntity` union block ([`project-entity.md`](../../data-model/project-entity.md) §1.3), not a pointer. | The `SiteToProjectSetupLayoutID` field name on `Program`, and nothing else. |
| `Project` → `Facility` | **Yes.** `Project.FacilityID`, admin-labelled "Related Project Facility", optional. | The `ProjectToFacilitySetupLayoutID` field name on `Program`, corroborating from the config side. |
| `PotentialProject` → `Location` | **No direct evidence either way in this pass.** `PotentialProject.LocationID` exists (required parent per the raw schema; not admin-exposed to confirm required/optional), but nothing shows it being *set* as part of a promotion — it may simply be the Location the Site is proposed *at*, evaluated before any Facility exists there. | None. |
| `PotentialProject` → `Facility` directly (no `Project` in between) | **No evidence for or against.** The two-layout naming implies a `Project` in between, but nothing rules out a direct promotion for simple cases. | None. |

## 3. Capital projects vs. contracts — the other half of the brief's question

`Project` and `Contract` are both `ProjectEntity` subtype roots (570 fields on `Contract`, 111 on
`Project`), both carry budgets, schedules ([`Task`/`TaskGroup`/`TaskItem`](../projects-capital/scheduling.md) —
`projects-capital`) and workflows, and both can reference a `Facility` (`Project.FacilityID`,
`Contract.FacilityID` — [`../facilities-locations/README.md`](../facilities-locations/README.md)).
**They are not the same kind of thing and nothing forces one through the other:**

- **`Project` models the work of creating, opening, or capitally improving a physical asset.**
  Its field vocabulary is construction-and-milestone shaped: `ConstructionPhaseStatus`,
  `DesignPhaseStatus`, `PossessionPhaseStatus`, `CurrentMilestone`/`NextMilestone`/
  `PreviousMilestone`, `CodeConstructionTypeID`. Its financial engine is
  `Task`/`TaskGroup`/`TaskItem` scheduling plus the (out-of-scope) budget subsystem, not the
  accounting engine.
- **`Contract` models the legal right to occupy or use a `Facility`/`Location`/piece of
  `Equipment`.** Its financial engine is the ASC 842/IFRS 16/straight-line accounting engine
  ([`../accounting/`](../accounting/)), entirely separate from `Project`'s budget/schedule surface.
- **A single physical store's lifecycle plausibly touches both, sequentially, not simultaneously**:
  evaluate the site (`PotentialProject`) → build it out (`Project`) → operate it under a lease
  (`Contract`). But `Contract.ProjectID` does not exist as a column, and `Project.FacilityID` points
  at the *building*, not at a lease — there is no schema-level requirement that a `Project` and a
  `Contract` ever reference each other directly.

**Note on where `Project` actually lives:** [`modules.json`](../../mindmap/modules.json) classifies
`Project` under `platform-tenancy`, not `portfolio-transactions` or `projects-capital` — almost
certainly because the automated classifier that built the module map grouped it with `ProjectEntity`
itself (both start `Project*` and neither has many distinguishing internal edges). This document and
[`../projects-capital/README.md`](../projects-capital/README.md) both treat `Project` as
load-bearing evidence regardless of which folder's object list contains it, because the two-step
pipeline this file describes cannot be explained without it.

**`projects` returns 0 rows in the live tenant** ([`graphql-api.md`](../../data-model/graphql-api.md)),
so nothing about `Project`'s behaviour — including whether the site pipeline is ever actually
exercised — can be confirmed against real data. Every claim in this document is schema-level only.

## 4. Confidence summary

| Claim | Label |
|---|---|
| `PotentialProject` has zero inbound FKs and zero Manage Data Fields exposure | **Observed** |
| `SiteToProjectSetupLayoutID` and `ProjectToFacilitySetupLayoutID` are the only two conversion-named fields in the schema, both on `Program` | **Observed** |
| These two fields represent one sequential pipeline, Site → Project → Facility | **Derived** — the naming pairs cleanly and no competing reading fits both fields at once |
| `Project.FacilityID` ("Related Project Facility") is a genuine, optional link from Project to Facility | **Observed** |
| `ProjectType` = "Opening Project or Capital Project" confirms the two-value discriminator | **Observed** (vendor's own field label) |
| "Opening Project" is the site-to-store phase; "Capital Project" is post-occupancy capital work | **Inferred** |
| The `PotentialProject` → `Project` step is unconfirmed by any FK | **Observed** (absence) — the honest state of the evidence |
| The actual copy/promotion mechanism (new row? same `ProjectEntityID` row re-typed? manual re-entry?) | **Not determined by this corpus.** Genuinely open. |

## Open questions

Ranked by how much each blocks a rebuild decision.

1. **What actually happens when a Site is promoted?** Does the platform create a brand-new `Project`
   row and copy matching fields across (address, region, DMA, prototype), or does it reuse the same
   `ProjectEntityID` and simply attach a new `Project` detail row to it, retiring the
   `PotentialProject` one — which the shared-key subtype model
   ([`project-entity.md`](../../data-model/project-entity.md) §1.2) would make structurally possible?
   The two mechanisms have very different implications for how ASG Edge+ should model the
   transition. Nothing in this corpus decides it.
2. **Does `PotentialProject.LocationID` get set as part of promotion, or is it set at Site-creation
   time to say which existing Location the Site is being evaluated at?** Both readings are
   consistent with the schema; only a screen capture of the Site-creation form would settle it.
3. **What do `SiteToProjectSetupLayoutID` and `ProjectToFacilitySetupLayoutID` actually render?**
   Opening either page layout in `Manage Page Layouts` would show whether it hosts a conversion
   button, and what fields it carries — the single most valuable next capture for this question.
4. **Can a `PotentialProject` be promoted directly to a `Facility`, skipping `Project`?** The
   two-layout-field evidence implies the two-step path is the normal one; nothing rules out a direct
   path for simpler deployments.
5. **Are `LandPurchaseSummary`, `SiteSurvey`, `Ownership` and `DemographicResults` (all
   `facilities-locations` objects, soft-attached via `ProjectEntityID`) actually attached to a
   `PotentialProject` in a live record**, and if so, do they transfer to the `Project`/`Facility` on
   promotion, or stay behind? [`../facilities-locations/demographics.md`](../facilities-locations/demographics.md)
   flags the same open question from its side.
