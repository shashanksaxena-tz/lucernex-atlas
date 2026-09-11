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
