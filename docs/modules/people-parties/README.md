# People & Parties — module overview

**Stated up front.** Ten objects, 301 fields, and one object — `Member` — with **290 foreign keys**
pointing at it, the single most-referenced record in the 223-object schema (second is `ProjectEntity`
at 163; see [`data-model.md`](data-model.md#why-290-foreign-keys-point-at-member)). This module holds
everyone the system knows about: internal `Member` (a real login), external `Person`/`NonMember`
(no login), the company record `Employer` (which is also, relabelled, Vendor/Landlord/Tenant — see
[009](../../admin/009-related-fields-and-data-model.md)), and `Party` (a thin per-contract role
assignment tying a company and/or a person to a lease with a classification).

**The load-bearing finding is [`member-vs-person-vs-party.md`](member-vs-person-vs-party.md):**
`Person`, `NonMember`, and `Member` are not three unrelated record types that happen to share some
column names. An exhaustive field-by-field diff shows `Person` and `NonMember` are **field-for-field
identical — 37 fields, 37 matching types, zero differences** — and `Member` is that same 37-field
block **plus** 44 login/security/approval-specific columns, sharing `PersonID` as a plain-`Number`
identity column across all three, exactly the shared-key signature
[`../../data-model/project-entity.md`](../../data-model/project-entity.md) §1.2 used to prove
`ProjectEntity` is a supertype. **Lucernex has a second supertype, and it is `Person`.**

**Why 290 foreign keys point at `Member`, resolved:** 240 of the 290 (83%) are just the universal
`CreatedByID`/`ModifiedByID` audit-stamp pair present on most objects in the schema (161 objects
carry `ModifiedByID`, 79 carry `CreatedByID`, both pointing at `Member`). The remaining 50 are
genuine business-identity and workflow-routing FKs — approvers, assignees, notifiees, checkout locks,
bid parties, brokers, lease analysts. **Member is the universal "who did this" anchor for the whole
product**, not primarily a business-domain reference. See
[`data-model.md`](data-model.md#why-290-foreign-keys-point-at-member) for the full breakdown.

![`Manage Employers` in BBW: **7,447 rows**, every one `Company Type = Vendor` and `Contact Type = Vendor` on the visible page. Eight of the columns are red-asterisked and required, including `Vendor#` and `Store Number`. Note the `Select Alternate Layout` control at the top right -- the layout-chain picker, appearing on an administration list rather than an end-user screen.](../../assets/screenshots/bbw-admin/35-manage-employers.jpg)

**Derived.** `Employer` is where the counterparty lives, and the grid shows why
[`../contracts/contract-hierarchy.md`](../contracts/contract-hierarchy.md) finds **no `Vendor` FK on
`Contract`**: there is no separate Vendor object to point at. Vendor, Landlord and Tenant are the
same `Employer` record under a relabelled `Contact Type`.

> **The count is the pager's, not the image's.** `Displaying 1 - 15 of 7447` — fifteen rows are on
> screen. These grids scroll internally, so nothing may be read from the visible page about the
> other 7,432.

### Why this module is under-illustrated, deliberately

**The captures exist; most of them cannot be shown.** `Manage Regions/Org Chart`
(`bbw-admin/30-manage-regions-org-chart.jpg`) is the single richest screen in this module — it renders
the whole `Accounting Purposes` portfolio's membership as a job-title-to-person list — and it names
roughly **sixty real individuals**. `Manage Members/Contacts` and `Manage Membership` have the same
problem by construction: they are directories of people.

What can be taken from those screens without naming anyone is the **job-title vocabulary**, which is
the part a rebuild actually needs:

| Observed job titles, `(ASG)BBW` org chart |
|---|
| `Lease Admin Manager`, `Lease Admin`, `Lease Admin Accounting`, `Lease Admin Client`, `Lease Abstractor`, `Outside Attorney`, `Outside Paralegal` |

**Derived, and it connects two modules.** These are `CodeJobTitle` values, and they are exactly the
vocabulary the workflow router resolves against when a step's `ApproverType` is `JOBTITLE`
([`../workflow/routing-and-approvals.md`](../workflow/routing-and-approvals.md)). The split between
`Lease Admin *` (internal) and `Outside *` (external counsel) also shows the org chart carries
**non-employees**, which bears on whether `Member` means "staff" or "anyone with a login".

**Observed, from `Manage Company`.** Three firm-level flags — `Apply Org Chart when creating
Locations`, `… RE Contracts`, `… Equipment Contracts` — are all **`Yes`** in BBW. The org chart is
therefore not a directory; **it is applied at record creation**, which is how membership propagates
to new entities without anyone assigning it.


## Contents

| Document | Answers |
|---|---|
| [`data-model.md`](data-model.md) | All 10 objects, their fields, FK edges, and the `Member` in-degree breakdown. |
| [`member-vs-person-vs-party.md`](member-vs-person-vs-party.md) | **The most important file in this folder.** What each of `Member`, `Person`, `Party`, `Employer`, `NonMember` actually is, the `Person` supertype finding, and the "Contact" soft type that resolves polymorphically across all three individual-person subtypes. |
| [`security-model.md`](security-model.md) | `SecurityLevel`, User Class, Job Title, and how workflow routing resolves a role to an actual person — cross-referencing, not restating, [`../workflow/routing-and-approvals.md`](../workflow/routing-and-approvals.md). |
| [`rules.md`](rules.md) | `PPL-R-001`…`PPL-R-013` in trigger/input/condition/effect/confidence form. |
| [`asg-edgeplus-mapping.md`](asg-edgeplus-mapping.md) | What ASG Edge+ has, must build, should deliberately differ on, and the decisions blocking it. |

## The 10 objects, by role

| Role | Objects |
|---|---|
| **The person supertype family** (shared `PersonID` key) | `Person`, `Member`, `NonMember` |
| **The company record** — also Vendor, also Landlord, also Tenant | `Employer`, `EmployerSite` |
| **Per-contract role assignment** | `Party` |
| **Per-entity contact/vendor rosters** | `LinkProjectEntityContact`, `LinkProjectEntityVendor` |
| **Audit** | `MemberAudit` |
| **Insurance detail on a vendor** | `VendorInsurance` |

## What "Vendor" and "Landlord" and "Tenant" actually are

There is no `Vendor`, `Landlord`, or `Tenant` object in this module — and none anywhere in the
223-object schema. `PaymentTransaction.VendorID` has declared type `Employer ID`
(**Observed**, [009](../../admin/009-related-fields-and-data-model.md)); `LinkProjectEntityContact`
carries a `Landlord_EmployerID` alongside its plain `EmployerID`; `VendorInsurance.VendorID` is also
typed `Employer ID`. **All three business roles are the same underlying `Employer` record**, played
under different names depending on which side of the transaction the schema column sits on. See
[`member-vs-person-vs-party.md`](member-vs-person-vs-party.md#employer--the-company-record-that-plays-three-roles)
for the full evidence.

## Admin entry points

**Observed**, [004](../../admin/004-company-administration.md), under the **Member Administration**
dashboard heading:

| Link | Route | Maps to |
|---|---|---|
| Manage Members/Contacts | `ContactEdit.jsp` | `Person`/`Member`/`NonMember` (the shared identity family) |
| Manage Employer Members | `ManageEmployerMembers.jsp` | `Employer` ↔ `Member`/`Person` linkage |
| Manage Employers | `EmployerEdit.jsp` | `Employer` |
| Manage Vendors | `VendorActivate.jsp` | `Employer`, filtered/flagged `IsVendor` — a separate admin screen for what is, at the data layer, the same table as Manage Employers |
| Manage Membership | `ManageOneMemberManyProjects.jsp` | `LinkMemberProjectEntity` (filed in `../platform-tenancy/`, not here) |
| Manage Security | `SecurityPageAccess.jsp` | `Security`/`UserClassSecurity` (filed in `../platform-tenancy/`, not here) |

None of these six screens has been opened in this pass — the routes are **Observed** from the
dashboard's accessibility tree, but no field grid behind any of them has been captured. That is this
module's largest single evidence gap; see [Open questions](#open-questions).

## Open questions

Ranked by how much they block work.

1. **Does "Manage Vendors" (`VendorActivate.jsp`) apply an `IsVendor`/`IsPreferredVendor` filter over
   `Employer`, or does it write to different columns than "Manage Employers"?** Neither screen has
   been opened. This is the single most direct way to confirm the Vendor-is-Employer reading with a
   live capture rather than schema inference alone.
2. **What determines whether a `Person` row also gets a `Member` row (login) versus a `NonMember`
   row (no login), if both are field-for-field identical to `Person`?** See
   `member-vs-person-vs-party.md`'s open questions — this is the sharpest unresolved question in the
   whole module.
3. **What is the actual value list for `Party.CodePartyTypeID`/`CodePartyGroupID`**, and does it
   overlap with `Employer.CodeContactTypeIDList`/`LinkProjectEntityContact.CodeContactTypeID`? Three
   different "type of party" classifications exist across this module's objects and none has been
   observed populated.
4. **Where does the org chart actually live**, beyond `Member.SupervisorID`? See
   `security-model.md` — the mechanism is schema-clear but the routing semantics
   (`../workflow/routing-and-approvals.md` OQ-22, OQ-23) remain open.
5. **Does `LinkProjectEntityContact`'s `Landlord_EmployerID`/`Landlord_PersonID` pair indicate a
   second, parallel contact record specifically for the landlord side of a lease**, or is it a
   convention for storing an alternate/secondary contact that happens to be named for the landlord
   case? No screen renders this pair.
