# User-defined fields, from the tenant-configuration angle

**Stated up front.** [`../reporting/report-field-registry.md`](../reporting/report-field-registry.md)
already establishes, with five independent pieces of evidence, that Lucernex has **exactly one**
field registry — `ReportGroupAvailableField` (RGAF) plus its grouping tree `ReportGroupData` (RGD) —
serving Manage Data Fields, Page Layouts, filters, Custom Lists, field-level security, and the audit
trail alike. This document does not re-derive that; it exists because RGAF/RGD are filed under the
`layouts-forms-reporting` module in the object taxonomy, not this one, yet the registry's
**Global/Firm split is itself a tenant-configuration mechanism** — the exact kind of thing a
"Platform & Tenancy" module is responsible for describing — and this module's own
`UserClassSecurity` object is a direct consumer of the registry's tree. That is the connection this
document draws.

## The mechanism, in one sentence

`RGAF.IsGlobal` (boolean) + `RGAF.FirmID` (text) make Global-vs-Firm a **column on one shared
table**, not a second schema or a separate registry — a tenant customises the product by adding rows
to the same table the platform's own fields live in, scoped to their `FirmID`. **Observed**,
`report-field-registry.md`. This is architecturally the same idea `tenancy-model.md` describes for
business data: one shared structure, a tenant-scoping column, no separate physical space per tenant.

## Why this module cites it rather than owns it

| What lives where | Object | Module |
|---|---|---|
| The field registry itself | `ReportGroupAvailableField`, `ReportGroupData` | `layouts-forms-reporting` |
| The Firm-scoped generic settings store (a sibling mechanism, not the same table) | `GlobalProperty` | **`platform-tenancy`** (this module) |
| The field-level security grant that *reads* the registry's tree | `UserClassSecurity` (real table), `Security` (its computed shadow) | **`platform-tenancy`** (this module) |

`UserClassSecurity.ReportGroupAvailableFieldID` + `ReportGroupDataID` + `RootReportGroupDataID` +
`SubReportGroupDataID` (**Observed**, this module's own field export) is a direct FK into the
registry's leaf-and-tree structure. **Derived**: a permission grant in this module is always *either*
a whole page layout, *or* one specific registry leaf, *or* one whole registry subtree — the same
three-level granularity (group → subgroup → leaf) that `report-field-registry.md` measured
behaviourally in [005](../../admin/005-manage-data-fields.md) (24 groups, 320 subgroups, 5,953
Global + 205 Firm leaves). Field-level security in this module and the field registry in
`layouts-forms-reporting` are, structurally, the same tree walked for two different purposes.

`GlobalProperty` (`FirmID`, `GlobalPropertySectionID`, `PropertyKey`, `PropertyValue`) is a second,
independent Firm-scoped key/value store — **not** the same mechanism as RGAF's `IsGlobal`/`FirmID`
split, because it has no leaf-field typing, no page-layout binding, and no security grant surface.
**Derived**, from the field shape alone: where RGAF/RGD model a typed, placeable, securable field,
`GlobalProperty` models an untyped setting. Both are Firm-scoped extension points; only one is a
user-defined *field*.

## What this means for the ASG Edge+ Hub/Spoke split

`RGAF`/`RGD` are `firm_global` objects (per `project-entity.md` §2's classification), which puts the
field registry itself in the Hub — a single, tenant-partitioned-by-column table of field definitions,
not a per-Spoke copy. That is consistent with `tenancy-model.md`'s reading of Lucernex's general
posture: shared structure, `FirmID`-scoped rows, not physical separation. If ASG Edge+ commits to
database-per-tenant Spokes (the open question in `tenancy-model.md`), the field registry — and by
extension `UserClassSecurity`'s grants against it — would need to live in the Hub and be readable
from every Spoke, which is the same "Spoke needs Hub read access" mechanism `tenancy-model.md` open
question 4 already flags as undesigned. This document adds one more concrete consumer to that list;
it does not resolve it.

## Open questions

1. **Does `UserClassSecurity`'s three-column tree pointer (`ReportGroupDataID` /
   `RootReportGroupDataID` / `SubReportGroupDataID`) ever disagree with RGAF's own two-FK denormalised
   path** (`ReportGroupDataID` + `ParentReportGroupDataID`, per `report-field-registry.md`)? Both
   describe "where in the tree" but use different column names and, in `UserClassSecurity`'s case, a
   third level. Unresolved without a live capture of a populated security grant.
2. **Is `GlobalProperty` used anywhere a rebuild needs to reproduce**, or is it dead platform
   scaffolding? No screen in this corpus renders it directly.
