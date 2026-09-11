# `Member` vs `Person` vs `Party` vs `Employer` vs `Contact`

**Stated up front.** Lucernex has exactly **two** identity supertypes in the whole product, not one.
[`../../data-model/project-entity.md`](../../data-model/project-entity.md) found the first —
`ProjectEntity` — from a mechanical signature: a shared identity column typed `Number` on both the
supertype and its subtypes, versus a hard `Entity ID` FK type everywhere else. Applying the
**identical test** to this module's objects finds a second one: `Person` is a supertype, and
`Member` and `NonMember` are its subtypes, sharing `PersonID` as a plain-`Number` key exactly the
way `Contract`/`Facility`/etc. share `ProjectEntityID` with `ProjectEntity`. `Party` and `Employer`
are not part of this family — `Party` is a thin per-contract role assignment, and `Employer` is the
separate *company* supertype (of exactly one shape — it has no subtypes of its own, only three
business names). `Contact` is not an object anywhere in the 223-object schema; it is a **soft FK
type** that resolves polymorphically across `Person`, `Member`, and `NonMember` — evidence, not
inference, is below.

## The evidence: an exhaustive field-by-field diff

Method: extract every field name and declared type for `Person`, `NonMember`, and `Member` from
`_lucernex_objects_summary.txt` and compare as sets. **Derived**, fully reproducible.

| Comparison | Result |
|---|---|
| `Person` fields (37) vs. `NonMember` fields (37) | **Identical — 37/37 names match, 0 type mismatches.** |
| `Person` fields (37) vs. `Member`'s matching subset | **All 37 of `Person`'s fields appear in `Member`, same types.** |
| `Member`'s remaining fields | **44 fields that appear on `Member` and nowhere else in this family** — see below. |

`PersonID` itself is declared `Number` on all three objects — **not** a foreign-key type. This is
the exact test `project-entity.md` §1.2 used: *"On a child object `ProjectEntityID` is typed `Entity
ID` — a foreign key. On [the subtypes] it is typed `Number` — the same as on `ProjectEntity` itself.
They are not referencing the supertype; they are carrying its key."* The same reasoning applies here
verbatim, and it is reinforced by a negative check: **no `Person ID` FK type exists anywhere in the
schema.** Every other object that needs to reference "a person" uses a different, soft type —
`Contact` — never a hard `Person ID` (see [§3](#3-contact-is-a-soft-polymorphic-type-not-an-object)).
That absence is the same signature `project-entity.md` found for `FirmID` (no `Firm ID` type exists
either): the true supertype's own key is never expressed as a first-class reference type, because
nothing needs to distinguish *which* subtype it points at when addressed generically.

### The shared 37-field block (on `Person`, `NonMember`, and `Member` alike)

`BOMapClientRecordID`, `BillRate1`, `BillRate2`, `City`, `CodeContactTypeIDList`,
`CodeJobFunctionID`, `CodeJobTitleID`, `CodeJobTitleIDList`, `CountryID`, `Description`,
`Designations`, `EMail1`, `EMail2`, `EmployerID`, `Fax`, `FirstName`, `IStateProvinceCountryID`,
`Inactive`, `JurisdictionID`, `LastName`, `MiddleName`, `MobileNumber`, `ModifiedByID`,
`ModifiedDate`, `PersonID`, `Phone`, `PhoneExtension`, `PostalCode`, `StreetAddress1..4`, `Suffix`,
`Title`, `UseEmployerAddress`, `WebSite`, `WirelessEMail`.

This is "an individual" in full: name, contact channels, address, job title/function, and a link to
an `Employer` (**the individual's employer**, e.g. which vendor company they work for — distinct
from `Party.CompanyID`, which is a role on a specific contract). **Observed.**

### `Member`'s 44 additional fields — what login turns a Person into

`AcceptEULA`, `AlwaysSpellCheck`, `AnySiteLoginName`, `AnySitePassword`, `CodeAnalyticsRoleID`,
`CodeApprovalCurrencyTypeID`, `CodeApprovalStatusID`, `CodeEquipApprovalStatusID`,
`CodeLockOutReasonID`, `CodeUserClassID`, `ColorScheme`, `ConvertToMember`, `Country`, `CreatedDate`,
`DatePattern`, `EmployerInactive`, `EquipPaymentApprovalMaxAmount`, `EquipPaymentApprovalMinAmount`,
`EquipRecurringApprovalMaxAmount`, `EquipRecurringApprovalMinAmount`, `HtmlPersonAddress`,
`IsAdministrator`, `IsExemptFromPWDExpiration`, `IsLucernexAdministrator`, `IsMasterMember`,
`IsMasterPerson`, `IsUnassignedWorkFlowApprover`, `IsViewPrivateIssueAllowed`, `Language`,
`LastLoginDate`, `LoginName`, `MemberID`, `MemberNameFirstLast`, `MemberPhoto`, `NumberPattern`,
`Password`, `PaymentApprovalMaxAmount`, `PaymentApprovalMinAmount`, `PersonNameLastFirst`,
`RecurringApprovalMaxAmount`, `RecurringApprovalMinAmount`, `StateProvinceCountryID`, `SupervisorID`,
`TimeZone`.

Four groups, all **Derived** from the column names: (1) login credentials (`LoginName`, `Password`,
`AnySiteLoginName`/`AnySitePassword` — a *second* credential pair, purpose unconfirmed, see
[Open questions](#open-questions)); (2) authorization (`CodeUserClassID`, `IsAdministrator`,
`IsLucernexAdministrator`, `IsMasterMember`); (3) the four numbered approval-amount-band pairs
(`Payment`/`Recurring` × `Min`/`Max`, plus the `Equip*` doubles) that
[`../workflow/routing-and-approvals.md` OQ-19](../workflow/routing-and-approvals.md#open-questions)
already flagged as populated on `Member` but read by no observed workflow field; (4) session/UI
preference (`ColorScheme`, `DatePattern`, `NumberPattern`, `TimeZone`, `Language`). **`ConvertToMember`
is the single most direct piece of evidence for the whole reading in this document** — its name
states outright that a record can be *converted into* a Member, implying the base identity predates
the login.

## 1. `Person` — the base identity

**Person** is the supertype: an individual contact record with no login and no organisational
authority — a broker, attorney, or property manager (per `../../data-model/`
[`INDEX.md`](../../data-fields/INDEX.md)'s existing, and here confirmed, reading). Every field on it
also exists, unchanged, on `Member` and `NonMember`.

## 2. `Member` and `NonMember` — the two subtypes, and what actually distinguishes them

`Member` = `Person`'s 37 fields + 44 login/authorization/preference fields. **This is exactly the
`ProjectEntity`-style table-per-subtype pattern**, with one structural difference worth flagging:
`ProjectEntity`'s own field list is a *union* of all its subtypes' distinguishing fields (`project-
entity.md` §1.3); `Person`'s field list is **not** a union — it holds only the common base, and
`Member` alone carries the extension. Both are legitimate variants of shared-key inheritance; this
module's version is the narrower, cleaner one (a true base + one meaningfully-extended subtype),
where `ProjectEntity`'s is a denormalised union of eight subtypes onto one table.

`NonMember` is the puzzle. **Its field list is identical to `Person`'s down to the type on every
column — it adds nothing.** `object-catalog.md`'s existing purpose line for `NonMember` — *"External,
non-licensed user record — a portal/vendor login that is not a `Member`"* (marked `_(Inferred)_`) —
**is not supported by the field list** and should be revised. A record with no `LoginName`,
`Password`, or any credential column cannot itself be "a portal login." The evidence instead
supports a narrower, more literal reading: **`NonMember` marks that a given individual is known to
the system as a person, without ever having been promoted to `Member`.** Whether `NonMember` is a
separate physical row from the corresponding `Person` row (sharing `PersonID`), or is instead a
view/filter over `Person` rows that have no matching `Member` row, cannot be settled from the field
list alone — both readings are consistent with everything observed. See
[Open questions](#open-questions).

## 3. `Contact` is a soft, polymorphic type — not an object

No object named `Contact` exists in the 223-object schema. Instead, **12 columns across the schema**
are declared with the type literal `Contact` (rather than a hard `<Entity> ID` type):
`Employer.AccountRepPersonID`, `Party.ContactID`, `LinkProjectEntityContact.PersonID`,
`LinkProjectEntityContact.Landlord_PersonID`, `ProjectEntity.LinkProjectEntityContactListData` (and
its mirror on the other 8 subtype roots — see `project-entity.md` §1.2), and others. **Derived**,
exhaustive grep of the raw export.

This is architecturally the same move `project-entity.md` documented for the soft `Entity` type on
`AssetHistory` (§2, "a false negative... the mechanical test misses it") and for `FirmID` having no
declared FK type at all: **Lucernex uses an untyped/soft-typed reference exactly where a single
column must be able to point at more than one physical table.** `Contact` is the natural reading —
a column typed `Contact` can resolve to a `Person`, a `Member`, or a `NonMember` row, because all
three share the same `PersonID` key space. This is **Inferred**, not directly observed (no screen in
this corpus shows a `Contact`-typed field being placed and resolved live), but it is the only reading
consistent with (a) the shared-key evidence in §0 above, (b) the complete absence of a `Person ID`
hard type, and (c) the precedent `project-entity.md` already established for exactly this kind of
soft type on the other supertype.

## `Employer` — the company record that plays three roles

**Employer** (71 fields, `firm_global`, no subtypes) is a separate supertype family from `Person` —
it has its own primary key (`EmployerID`, typed `Number`, referenced elsewhere as the hard FK type
`Employer ID`) and none of the `Person`-family fields. It is the vendor/landlord/tenant company
record, evidenced three ways:

| Business role | Schema evidence | Source |
|---|---|---|
| **Vendor** | `PaymentTransaction.VendorID` declared type `Employer ID`; `VendorInsurance.VendorID` likewise; `Employer.IsVendor`, `IsPreferredVendor`, `IsEquipContractVendor`, `IsREContractVendor` booleans | **Observed**, [009](../../admin/009-related-fields-and-data-model.md); this module's own field export |
| **Landlord** | `LinkProjectEntityContact.Landlord_EmployerID` — a second `Employer ID` column on the same join row as the plain `EmployerID` | **Observed**, this module's field export |
| **Tenant** *(sub-lease/landlord context, not the ASG Edge+ "tenant" meaning)* | The `Tenant` object exists separately (`facilities-locations` module, sub-occupant under a `Facility`) and is **not** the same concept — flagged here only to avoid confusion, since this module's `Employer` also covers the counterparty-company sense of "tenant" in a master-lease/sub-lease `Party` row | **Inferred** from `Party.CompanyID(Employer ID)` and the co-tenancy/sub-lease vocabulary elsewhere in the schema |

`Employer` additionally carries `EmployerSite` (a specific branch/site of a multi-location vendor) and
`VendorInsurance` (the vendor's actual insurance policy, distinct from `Insurance` — the lease's
*required*-coverage terms, in `contracts-leases`).

## `Party` — a thin, per-contract role assignment, not an identity record

**Party** (12 fields) is not part of the identity family at all — it has no `PersonID` and no
`EmployerID` as its own key, and every field on it exists to classify a role:

| Field | Type | Role |
|---|---|---|
| `CompanyID` | `Employer ID` | The company side of the role (may be null) |
| `ContactID` | `Contact` (soft) | The individual side of the role (may be null) — resolves to `Person`/`Member`/`NonMember` |
| `ContractID` | `Contract ID` | The contract this role applies to |
| `ProjectEntityID` | `Entity ID` | The entity this role applies to (broader than just `Contract`) |
| `CodePartyGroupID` / `CodePartyTypeID` | Dropdowns | The classification — *"used where the role doesn't fit `Employer` or `Person` specifically"* (`object-catalog.md`) |
| `PrimaryFlag` | Boolean | Marks the primary party of that type on the contract |

**Derived**: `Party` is the escape hatch for a contract-specific role that is neither a full
`LinkProjectEntityContact` roster entry nor an `Employer` counterparty relationship elsewhere on
`Contract` — a generic (company, person, role-type) triple scoped to one contract.

## The full picture

```
                    ┌───────────────────────────────────────┐
                    │  Person  (37 fields — the base row)     │
                    │  FirstName, LastName, EMail1/2,         │
                    │  EmployerID, CodeJobTitleID, address …  │
                    │  PersonID (Number — the shared key)     │
                    └───────────────┬─────────────────────────┘
                                    │ same PersonID
              ┌─────────────────────┼─────────────────────┐
              │                                            │
     NonMember (37 = Person, exactly —              Member (81 = Person's 37
     no distinguishing fields of its own;             + 44 login/authorization/
     "known but never promoted to Member")            approval/preference fields)

  Soft type "Contact" resolves to any of the three above, wherever a column
  needs to reference "a person" without committing to which kind:
    Employer.AccountRepPersonID · Party.ContactID · LinkProjectEntityContact.PersonID/Landlord_PersonID
    · ProjectEntity.LinkProjectEntityContactListData (and the 8 other subtype roots)

  Employer (71 fields — a separate supertype: the company)
    ├── EmployerID (Number, own key; referenced elsewhere as hard type "Employer ID")
    ├── plays "Vendor" via PaymentTransaction.VendorID, VendorInsurance.VendorID, Is*Vendor flags
    ├── plays "Landlord" via LinkProjectEntityContact.Landlord_EmployerID
    ├── EmployerSite (1:N — a vendor's branch offices)
    └── VendorInsurance (1:N — the vendor's own policy detail)

  Party (12 fields — per-Contract role assignment, not an identity record)
    ├── CompanyID  (Employer ID)  — the company side, nullable
    ├── ContactID  (Contact, soft) — the person side, nullable
    ├── ContractID (Contract ID)
    └── CodePartyGroupID / CodePartyTypeID — the classification
```

## Why this matters for a rebuild

1. **Model one identity aggregate, not three.** `Member` and `NonMember` should be a single table
   with a nullable credential/authorization sub-object, not two separate tables — reproducing the
   Lucernex split would mean carrying a genuinely empty subtype (`NonMember`) as a first-class
   concept.
2. **Do not model `Contact` as a table.** Anywhere a Lucernex field is typed `Contact`, the ASG Edge+
   equivalent is a polymorphic reference into the identity aggregate above (whichever of
   Member-with-login or Member-without-login the target row is), the same design decision
   `project-entity.md` §5.3 already flags for the `ProjectEntity` supertype question generally.
3. **`Employer` is genuinely one company record used under three business labels.** A rebuild that
   creates separate `Vendor`, `Landlord`, and `Tenant`(-as-counterparty) entities would need to keep
   them in sync by hand; Lucernex's own design avoids that by not having them.
4. **`Party` is a pattern, not a special case.** It is the generic "this company-or-person plays this
   classified role on this contract" record — worth keeping as a genuinely separate, thin join
   concept distinct from both the identity aggregate and the per-entity roster
   (`LinkProjectEntityContact`).

## Open questions

Ranked by how much they block the identity model a rebuild would need.

1. **Is `NonMember` a physically separate row from its corresponding `Person` row, or a
   filtered/computed view of `Person` rows with no `Member` counterpart?** The field-for-field
   identity is consistent with either. Settling it requires a live capture of `ManageOneMemberMany
   Projects.jsp` or `ContactEdit.jsp` showing whether converting a `NonMember` to a `Member`
   preserves or replaces the underlying row.
2. **What are `AnySiteLoginName`/`AnySitePassword` on `Member`, and how do they differ from
   `LoginName`/`Password`?** A second credential pair on the same object is unexplained — possibly an
   external/vendor-portal login distinct from the internal one, which would bear directly on how
   `EnableVendorCollaboration` (`../workflow/routing-and-approvals.md` §9) actually authenticates
   external members.
3. **Does `CodeContactTypeIDList` on `Person`/`Member`/`NonMember` (the individual's own contact-type
   tags) share a value list with `LinkProjectEntityContact.CodeContactTypeID` (the per-entity
   roster's classification) and `Party.CodePartyTypeID`?** Three independent classification columns
   for "what kind of contact/party is this" exist across this module and none has been observed
   populated with real values.
4. **Does "Manage Vendors" write to different `Employer` columns than "Manage Employers"?** Would
   directly confirm or refine the Vendor-is-Employer reading with a live capture. See
   `README.md`'s open questions.
5. **Is `Party.ProjectEntityID` ever populated for a non-`Contract` entity type**, given `Party` also
   carries a direct `ContractID`? If `Party` is only ever used against Contracts in practice, the
   `ProjectEntityID` column may be vestigial generality rather than active polymorphism.
