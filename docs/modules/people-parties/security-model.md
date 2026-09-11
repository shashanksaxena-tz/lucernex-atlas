# Security model — how a role resolves to an actual person

**Stated up front.** This module owns the people; `../platform-tenancy/` owns the permission ladder
(`Security`/`UserClassSecurity`) and `../workflow/routing-and-approvals.md` owns the full
reconciliation of how a routing rule picks a principal. This document is the seam between the three:
what `Member` itself carries that makes role-based resolution possible, and it deliberately does
**not** restate the routing mechanics already fully worked out in
[`../workflow/routing-and-approvals.md`](../workflow/routing-and-approvals.md) — it cites that
document's conclusions and adds only what belongs to the person record itself.

## The three axes a `Member` can be selected by

| Axis | Column(s) on `Member` | Cardinality |
|---|---|---|
| **User Class** | `CodeUserClassID` | One per Member |
| **Job Title** | `CodeJobTitleID` (own/default) vs. `LinkMemberProjectEntity.CodeJobTitleIDList`/`AssignedCodeJobTitleIDList` (per-entity, possibly overridden) | One global, many possible per-entity |
| **Org chart position** | `SupervisorID` (self-referencing `Member ID`) | A tree, walked 1–3 levels or to the root |

**Observed**, this module's field export. The GraphQL `MemberNotifyType` enum
(`ORGCHART_ALL, ORGCHART_LEV1, ORGCHART_LEV2, ORGCHART_LEV3, ORGCHART_MKT, USERCLASS, JOBTITLE,
MEMBERID`) is the authoritative statement of these axes plus a fourth (direct member id) and is
fully reconciled against the competing vendor-help and legacy-column vocabularies in
[`../workflow/routing-and-approvals.md` §2](../workflow/routing-and-approvals.md#2-three-competing-routing-vocabularies-reconciled)
— not repeated here.

## `SecurityLevel` — the permission ladder itself

`SecurityLevel: [DEFAULT, NO_ACCESS, VIEW, EDIT, DELETE]` (**Observed**,
[`../../data-model/graphql-api.md`](../../data-model/graphql-api.md)) is applied per
`(CodeUserClassID, <field | layout | dashboard component>)` pair on `../platform-tenancy/`'s
`UserClassSecurity` object — the mechanics are in
[`../platform-tenancy/data-model.md`](../platform-tenancy/data-model.md#security-is-a-computed-shadow-of-userclasssecurity)
and are not repeated here. What belongs in *this* module: `CodeUserClassID` is a column on `Member`
itself, so a person's effective permission is `UserClassSecurity` rows filtered by their own
`CodeUserClassID` — this module supplies the "who," `platform-tenancy` supplies the "what they can
do."

## Job Title: global default vs. per-entity assignment

`Member.CodeJobTitleID` is the person's own default job title. On a specific entity, that default can
be **overridden**: `LinkMemberProjectEntity.CodeJobTitleIDList` (the titles currently configured for
this member on this entity) sits beside `AssignedCodeJobTitleIDList` (titles that override the
member's default), both typed `Dropdown (Job Title Code)`. **Observed**, this module's field export
and [`../workflow/routing-and-approvals.md` §4](../workflow/routing-and-approvals.md#4-the-entity-roster--how-a-job-title-becomes-a-person).
**Derived** (restating that document's own reading, not re-deriving it): a person can hold a role on
one contract that they do not hold globally, which is exactly what "by Job Title" routing depends on
resolving correctly and is exactly why `../workflow/routing-and-approvals.md` OQ-24 remains open.

Vendor help text (**Observed**, cited in full in `routing-and-approvals.md` §3) is unambiguous about
why this matters: *"The Job Title is used when auto-assigning things like tasks, work flow steps, and
notifications."* Job Title is not a display label in this product; it is a routing key.

## The org chart: `Member.SupervisorID`

`Member.SupervisorID`, typed `Member ID`, self-referencing, **is** the org chart (**Observed**). It
is walked to bound depths by the routing enums (`ORGCHART_LEV1`…`LEV3`, plus `ORGCHART_ALL` and
`ORGCHART_MKT`) — three explicit levels, not an arbitrary tree walk. From whom the hops are counted
(the initiator? the entity's manager?) is unresolved; that is
[`../workflow/routing-and-approvals.md` OQ-22](../workflow/routing-and-approvals.md#open-questions),
inherited here without new evidence.

Two candidate anchors for "manager," both living partly in this module:

| Candidate | Object | Column |
|---|---|---|
| Per-entity manager flag | `../platform-tenancy/`'s `LinkMemberProjectEntity` | `IsManager` |
| Denormalised manager list on the entity | `ProjectEntity` (`../platform-tenancy/`) | `ManagerIDList` |
| Direct supervisor | **This module's** `Member` | `SupervisorID` |

Which of the three the `DaysUntilAlert*` escalation path actually reads is
`../workflow/routing-and-approvals.md` OQ-23 — unresolved, and this module's field list does not add
new evidence toward it.

## `REGION1`/`REGION2`/`MARKET` — resolved on the entity, not on the person

Region- and market-scoped routing (`AssigneeType`'s `REGION1`, `REGION2`, `MARKET` values) resolves
against **the entity being routed on** (`ProjectEntity.RegionID`/`RootRegionID`/`SubRegionID`,
`CodeMarketAreaID`/`CodeMarketTypeID`), not against any column on `Member`. `Member` has no region or
market column of its own. **Derived**: this means region/market routing is really "find the entity's
region/market, then find the member(s) responsible for that region/market" via
`../platform-tenancy/`'s `LinkRegionManager` — a two-hop resolution, not a direct member attribute.
Full mechanics: [`../platform-tenancy/rules.md#plt-r-008`](../platform-tenancy/rules.md#plt-r-008--region-is-a-three-level-hierarchy-resolved-by-regionidrootregionidsubregionid).

## What the live tenant actually does

**Observed**, `../workflow/routing-and-approvals.md`: of 19 configured workflow steps, **17 route by
named `Member`**, one by Job Title, one by Ad Hoc. **None** of the live tenant's routing exercises
User Class, Org Chart level, or Region/Market. The rich role-based apparatus this document and
`platform-tenancy` describe is, in ASG's actual production configuration, almost entirely latent.
That is itself the load-bearing operational fact for a rebuild's prioritisation — see
`../workflow/routing-and-approvals.md` OQ-42 for the open question of whether that's deliberate
policy or a workaround for the "all-for-one" role-routing overload
(`../workflow/README.md`'s known-defect #4).

## Open questions

1. **`IsUnassignedWorkFlowApprover` and `UnassignedApproverID`** (the latter on
   `WorkFlowTemplateStep`, in `../workflow/`) are stated dead in the vendor help text — *"a
   placeholder for an upcoming feature"* (**Observed**, `routing-and-approvals.md` §5). Confirm this
   is still true in the current build before assuming any approver-vacancy handling exists.
2. **Does `Member.CodeAnalyticsRoleID` gate anything security-relevant**, or is it purely a reporting
   classification? No screen in this corpus renders it.
3. **Is `EmployerInactive` on `Member` a cached copy of `Employer.Inactive`**, kept for fast filtering
   of external members whose employer has since been deactivated? **Inferred** from the name; not
   directly observed.
