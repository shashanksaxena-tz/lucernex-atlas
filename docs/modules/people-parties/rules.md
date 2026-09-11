# People & Parties — rules

`PPL-R-001` … `PPL-R-013`. Format: trigger / input / condition / effect / confidence.

## Identity

### PPL-R-001 — `Person` is a supertype; `Member` and `NonMember` are its subtypes on a shared key
- **Trigger:** Any read or write that treats `Member`, `Person`, or `NonMember` as unrelated tables.
- **Input:** `PersonID`, typed `Number` (not a declared FK type) on all three objects.
- **Condition:** `Person` and `NonMember` are field-for-field identical (37/37, zero type
  mismatches); `Member` is that same 37-field block plus 44 login/authorization fields.
- **Effect:** All three share one identity key space. A rebuild should model one identity aggregate
  with an optional login/authorization extension, not three tables.
- **Confidence:** Derived — exhaustive field diff, `member-vs-person-vs-party.md`.

### PPL-R-002 — No hard FK type references a person directly; `Contact` is the soft, polymorphic type
- **Trigger:** Any column that needs to reference "a person" from another object.
- **Input:** 12 columns across the schema declared type `Contact` (`Employer.AccountRepPersonID`,
  `Party.ContactID`, `LinkProjectEntityContact.PersonID`/`Landlord_PersonID`, `ProjectEntity.
  LinkProjectEntityContactListData` on all 9 spine roots, and others).
- **Condition:** No `Person ID` FK type exists anywhere in the 60-odd declared FK types.
- **Effect:** A field typed `Contact` may resolve to a `Person`, `Member`, or `NonMember` row
  interchangeably. Model it as a polymorphic reference into the identity aggregate, not as an FK to
  a single physical table.
- **Confidence:** Inferred — consistent with PPL-R-001 and with `project-entity.md`'s precedent for
  soft types (`Entity`, and `FirmID`'s missing FK type), but not directly observed resolving live.

### PPL-R-003 — `ConvertToMember` implies promotion, not replacement
- **Trigger:** A `Person`/`NonMember` is granted system login.
- **Input:** `Member.ConvertToMember` (Boolean).
- **Condition:** —
- **Effect:** The existing identity is promoted to carry login/authorization data; it is not deleted
  and recreated. The exact mechanics (same row extended vs. new row sharing `PersonID`) are open —
  see `member-vs-person-vs-party.md` open question 1.
- **Confidence:** Inferred from the field name alone.

## Companies and roles

### PPL-R-004 — `Employer` is one table serving three business roles
- **Trigger:** Any process that treats Vendor, Landlord, or Tenant-as-counterparty as separate
  entities.
- **Input:** `PaymentTransaction.VendorID` (type `Employer ID`), `LinkProjectEntityContact.
  Landlord_EmployerID`, `Employer.Is*Vendor` flags.
- **Condition:** No `Vendor`, `Landlord`, or `Tenant`-as-counterparty object exists in the 223-object
  schema.
- **Effect:** All three business roles resolve to one `Employer` row. A rebuild should not create
  separate entities that then require manual synchronisation.
- **Confidence:** Observed — [009](../../admin/009-related-fields-and-data-model.md), this module's
  field export.

### PPL-R-005 — `Party` is a generic, classified role assignment, not an identity record
- **Trigger:** A role needs recording against a Contract that doesn't fit the standing roster
  (`LinkProjectEntityContact`) or a direct `Employer` relationship elsewhere on `Contract`.
- **Input:** `Party.CompanyID` (nullable `Employer ID`), `Party.ContactID` (nullable `Contact`, soft),
  `CodePartyGroupID`/`CodePartyTypeID`, `PrimaryFlag`.
- **Condition:** Both `CompanyID` and `ContactID` are independently nullable.
- **Effect:** A `Party` row can name a company, a person, or (in principle) both, classified by type
  — the escape hatch for a role that isn't one of the platform's named relationships.
- **Confidence:** Derived — field shape only, no live capture of populated rows.

### PPL-R-006 — The per-entity contact roster and the per-entity vendor list are separate, differently-shaped joins
- **Trigger:** Listing "who is associated with this entity."
- **Input:** `LinkProjectEntityContact` (12 fields, classified by `CodeContactTypeID`, carries a
  parallel `Landlord_*` pair) vs. `LinkProjectEntityVendor` (4 fields, unclassified — just
  `ProjectEntityID` + `VendorID`).
- **Condition:** —
- **Effect:** Contacts get a typed, richer roster entry; approved vendors get a bare membership list
  with no role classification at all.
- **Confidence:** Observed, this module's field export.

## Audit and identity load

### PPL-R-007 — 83% of `Member`'s in-degree is the universal audit-stamp pair, not business routing
- **Trigger:** Any capacity-planning or service-boundary decision involving the identity service.
- **Input:** 290 FK edges target `Member`; 240 of them are `CreatedByID`/`ModifiedByID`.
- **Condition:** —
- **Effect:** The identity/user record must be cheaply reachable from nearly every write path in the
  product for stamping alone, independent of its true business-domain reference count (50 edges).
- **Confidence:** Derived — exhaustive edge-count analysis, `data-model.md`.

### PPL-R-008 — `MemberAudit` is login/session audit, not field-change audit
- **Trigger:** A member logs in, is impersonated (support access), or performs an audited action.
- **Input:** `MemberAudit.CodeMemberActionID`, `AuditDate`, `ImpersonatingMemberID`, `SrcIP`,
  `UserAgent`.
- **Condition:** —
- **Effect:** This is a distinct audit mechanism from `../platform-tenancy/`'s `AuditColumn` (which
  logs field-level changes) — `MemberAudit` logs session/security events specifically.
- **Confidence:** Observed, field export.

## Security and routing (owned jointly with `platform-tenancy` and `workflow`)

### PPL-R-009 — A member's routable identity is three independent axes
- **Trigger:** Any workflow, task, or notification routing rule.
- **Input:** `Member.CodeUserClassID`, `Member.CodeJobTitleID` (default) /
  `LinkMemberProjectEntity.CodeJobTitleIDList`/`AssignedCodeJobTitleIDList` (per-entity override),
  `Member.SupervisorID` (org chart).
- **Condition:** —
- **Effect:** A person can be selected by class, by title (global or entity-specific), or by
  reporting-line position, and these three do not have to agree with each other.
- **Confidence:** Observed — `security-model.md`, cross-referencing
  `../workflow/routing-and-approvals.md` §2 without re-deriving it.

### PPL-R-010 — Per-entity job title can override the member's global default
- **Trigger:** Job-Title-based routing evaluated in the context of a specific entity.
- **Input:** `LinkMemberProjectEntity.AssignedCodeJobTitleIDList`.
- **Condition:** Differs from `Member.CodeJobTitleID`.
- **Effect:** The entity-scoped assignment takes precedence for routing purposes on that entity —
  **Inferred** from the column's own definition text (*"the job titles that override the member's
  default job title"*), not confirmed by a live capture. See `../workflow/routing-and-approvals.md`
  OQ-24.
- **Confidence:** Inferred.

### PPL-R-011 — Region/Market routing resolves through the entity, not through any `Member` column
- **Trigger:** `AssigneeType = REGION1 | REGION2 | MARKET`.
- **Input:** `ProjectEntity.RegionID`/`RootRegionID`/`SubRegionID`/`CodeMarketAreaID`/
  `CodeMarketTypeID` (in `../platform-tenancy/`), then `LinkRegionManager` to find the responsible
  member.
- **Condition:** —
- **Effect:** This is a two-hop resolution (entity → region/market → manager), not a direct `Member`
  attribute lookup.
- **Confidence:** Derived — `security-model.md`.

### PPL-R-012 — Production routing barely uses any of the above
- **Trigger:** Prioritising which routing axes a rebuild must support on day one.
- **Input:** 17 of 19 live workflow steps route by named `Member`; 1 by Job Title; 1 by Ad Hoc; 0 by
  User Class, Org Chart level, or Region/Market.
- **Condition:** —
- **Effect:** The rich role-based apparatus this module documents is largely latent in ASG's actual
  configuration. Treat as lower priority pending the answer to
  `../workflow/routing-and-approvals.md` OQ-42 (deliberate policy vs. workaround for the "all-for-one"
  overload).
- **Confidence:** Observed, `../workflow/routing-and-approvals.md`.

### PPL-R-013 — Approval-amount bands exist on `Member` but are read by no observed workflow field
- **Trigger:** Any attempt to implement amount-banded approval routing (route high-value payments to
  a different approver than low-value ones).
- **Input:** `Member.PaymentApprovalMinAmount`/`MaxAmount`, `RecurringApprovalMinAmount`/`MaxAmount`,
  and the two `Equip*` pairs.
- **Condition:** No `WorkFlowTemplateStep`/`WorkFlowTemplateStepAction` field reads these columns
  (exhaustive check, `../workflow/step-actions.md`/`routing-and-approvals.md`).
- **Effect:** These fields may be vestigial, may be read by application logic outside the schema
  dump, or may be populated but unused in the live tenant. Do not assume amount-banded routing works
  end-to-end without confirming a live step reads them.
- **Confidence:** Derived — `../workflow/routing-and-approvals.md` OQ-19, carried here because the
  fields themselves are this module's own.
