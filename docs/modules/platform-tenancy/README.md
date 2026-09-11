# Platform & Tenancy — module overview

**Stated up front.** This module is not one thing in Lucernex's own admin taxonomy — it is the
assembled scaffolding a multi-tenant, entity-polymorphic product needs underneath every other
module: the tenant record (`Firm`), the universal entity spine (`ProjectEntity`, fully derived in
[`../../data-model/project-entity.md`](../../data-model/project-entity.md) and cited, not repeated,
throughout this folder), the permission ladder (`Security`/`UserClassSecurity`), shared geography
(`StateProvinceCountry`/`Jurisdiction`), currency (`ExchangeRate`), the org-chart region hierarchy
(`Region`), the per-entity roster join (`LinkMemberProjectEntity`), and a handful of audit and
stub tables. 21 objects, 385 fields, captured 2026-09-10 from `_lucernex_objects_summary.txt` and
the GraphQL schema, tenant `(ASG)American Freight`, build `26.08.0.46`.

**The load-bearing finding is [`tenancy-model.md`](tenancy-model.md):** `FirmID` is the tenant key
and `ProjectEntityID` is not — it is the intra-tenant partition key. That distinction, established
in `project-entity.md` §4 and extended here with the GraphQL JWT's `cluster` claim, is the one this
whole module exists to carry forward into the ASG Edge+ Hub/Spoke and database-per-tenant design.

**The second finding is mechanical, not architectural: `Security` is a computed shadow of
`UserClassSecurity`.** The two objects declare **21 fields each, identical name-for-name** —
`Security` has no physical table (**Observed**, `_lucernex_objects_summary.txt`, table column
blank) while `UserClassSecurity` does. One is the editable permission grant; the other is its live,
read-only projection. **Derived** from an exhaustive field-list diff (this document's own working,
reproducible against the raw export).

**The third finding is what the corpus does *not* explain: `Region` carries one declared field and
is referenced from 12 other objects across 34 columns** (`RegionID`, `RootRegionID`, `SubRegionID`
repeated on the same rows) — the schema dump barely describes the table that the workflow engine's
`REGION1`/`REGION2`/`MARKET` routing scopes ultimately resolve against. See
[`tenancy-model.md`](tenancy-model.md#the-org-chart-region-hierarchy) and
[`rules.md`](rules.md#plt-r-006).

## Contents

| Document | Answers |
|---|---|
| [`data-model.md`](data-model.md) | All 21 objects, their fields, their FK edges in and out, and where this module's boundary with `people-parties` and the entity spine actually sits. |
| [`tenancy-model.md`](tenancy-model.md) | **The most important file in this folder.** `FirmID` vs `ProjectEntityID`, the `cluster` JWT claim, and what Lucernex's own architecture does and does not settle about the ASG Edge+ database-per-tenant question. |
| [`udf-registry.md`](udf-registry.md) | How tenant-specific field customization (`Firm_*` columns, the `IsGlobal`/`FirmID` split) sits inside this module's tenant model — cross-referencing, not restating, [`../reporting/report-field-registry.md`](../reporting/report-field-registry.md). |
| [`rules.md`](rules.md) | `PLT-R-001`…`PLT-R-016` in trigger/input/condition/effect/confidence form. |
| [`asg-edgeplus-mapping.md`](asg-edgeplus-mapping.md) | What ASG Edge+ has, must build, should deliberately differ on, and the decisions blocking it. |

## The 21 objects, by role

| Role | Objects |
|---|---|
| **The tenant record** | `Firm` |
| **The entity spine** | `ProjectEntity` (supertype — full treatment in `project-entity.md`, not repeated here) |
| **The disputed second "project" concept** | `Project` — see [`data-model.md`](data-model.md#project-vs-projectentity) |
| **Permission ladder** | `Security` (computed), `UserClassSecurity` (the real table) |
| **Geography** | `StateProvinceCountry`, `Jurisdiction` |
| **Currency** | `ExchangeRate` |
| **Org-chart hierarchy** | `Region`, `LinkRegionManager` |
| **Entity roster / roles** | `LinkMemberProjectEntity`, `LinkPEMemberCodeJobTitle` |
| **Company hierarchy above Employer** | `Organization` — see the boundary note below |
| **Audit scaffolding** | `AuditColumn`, `AuditTable`, `TemplateAudit` |
| **Generic config store** | `GlobalProperty` |
| **Thin stubs (≤1 declared field)** | `EntityTemplate`, `MapClientSchedule`, `Notify`, `ScratchPad` |

### A boundary note: `Organization` reads like a party, but the taxonomy files it here

`Organization` — "a broader organizational entity (parent company, franchise group) above
`Employer`" (`object-catalog.md`) — is thematically closer to `people-parties`' identity family than
to tenant plumbing, and `project-entity.md` §2 groups it under "Identity & parties" in its own
firm-global inventory. The module taxonomy ([`../../mindmap/modules.json`](../../mindmap/modules.json))
nonetheless assigns it to `platform-tenancy`, not `people-parties`. Both readings have evidence:
`Contract.OrganizationID` (type `Organization ID`) is *"the organization where payments should be
debited from"* ([009](../../admin/009-related-fields-and-data-model.md)) — a banking/AP-routing
role, which is what earns it a seat here rather than beside `Employer`/`Person`/`Member` in
`../people-parties/`. Treat the module boundary as a filing convenience, not a claim that
`Organization` is architecturally unlike `Employer`.

## What this module is not

It is not a Lucernex-native "Platform" module — there is no `Manage Platform` admin screen. It is
this documentation set's own assembly of the objects that (a) have no `ProjectEntityID` and sit
above the entity spine (`firm_global`, per `project-entity.md` §2), and (b) are not more naturally
grouped with people, geography-as-a-feature, or any of the other 13 modules. `Firm` and
`ProjectEntity` are the two objects that make this module load-bearing rather than a junk drawer;
the rest is scaffolding those two need.

## Open questions

1. **Does `Security` ever diverge from `UserClassSecurity`**, or is the projection always a pure
   mirror? No screen renders `Security` directly (`ShowObjectDetails.jsp` shows it has no physical
   table) — confirming it requires reading the live effective-permission API response for a member
   and diffing it against their `UserClassSecurity` grants.
2. **What does `Region` actually store beyond its one declared column?** 12 referencing objects and
   34 columns depend on a table the export describes almost not at all. A `ShowObjectDetails.jsp`
   pass on `Region` specifically (not yet done — see `object-catalog.md` open question 1) would
   settle this and directly unblocks `AssigneeType`'s `REGION1`/`REGION2` reading.
3. **Is `Project` a legacy predecessor of `ProjectEntity`, a lightweight cross-system reference id,
   or something else entirely?** Unresolved in `object-catalog.md` open question 2 and inherited here
   unchanged — both objects are `subtype_root`-shaped and this module owns both.
4. **What is `EntityTemplate` actually a template *of***, given `TemplateAudit` references separate
   `BudgetEntityTemplateID`/`FolderEntityTemplateID`/`TaskEntityTemplateID` columns that don't
   obviously map to it? See [`data-model.md`](data-model.md#the-template-family).
5. **Does the vendor's own tenant model use physical database-per-tenant, or is `FirmID` a row-level
   discriminator over one shared schema?** The `cluster` JWT claim (`host:tenant`) is the only
   evidence pointing either way, and it's inferential. See
   [`tenancy-model.md`](tenancy-model.md#open-questions) — this is the single highest-leverage
   question for the ASG Edge+ architecture decision this folder feeds.
