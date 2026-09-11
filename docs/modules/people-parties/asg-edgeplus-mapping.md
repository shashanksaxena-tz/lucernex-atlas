# People & Parties — mapping to ASG Edge+

**Stated up front.** ASG Edge+'s target architecture already names "User management" as Hub content,
alongside the shared `Location`/`Organization` entities. This module's evidence supports that
placement strongly — `Person`/`Member`/`NonMember`/`Employer` are all `firm_global` in Lucernex's own
spine classification (`../../data-model/project-entity.md` §2) — and adds a specific, load-bearing
design constraint the workspace index does not yet capture: the identity record's in-degree is
dominated by audit-stamping, not business reference, which should shape how the Hub's user service
is designed to scale.

## 1. What exists

`ASG-Edgeplus-User-Service` is already extracted and running — "Users, companies, auth lifecycle" per
the workspace index — and is the closest existing analogue to this module. Its actual data model
relative to the `Person`/`Member`/`NonMember`/`Employer`/`Party` split documented here has not been
compared in this pass; that comparison is the natural next step and is listed under Decisions below.

## 2. What must be built (or confirmed already built)

| Lucernex evidence | What ASG Edge+ needs |
|---|---|
| `Person`/`Member`/`NonMember` sharing one identity key | One identity aggregate with an optional login/authorization extension (`PPL-R-001`). If `ASG-Edgeplus-User-Service` already models "user" as a single table with a nullable credentials sub-object, this module's finding **confirms** that design rather than requiring new work — worth an explicit check. |
| `Employer` serving Vendor/Landlord/Tenant-counterparty under one table | One company/counterparty record, not three (`PPL-R-004`). |
| `Party`'s generic (company, person, role-type) triple | A generic role-assignment concept on Contract, if ASG Edge+ needs to record roles that don't fit a named relationship (broker, attorney, guarantor). Low priority unless a specific BRD calls for it — no live capture in this corpus shows `Party` populated. |
| `Member.CodeUserClassID`/`CodeJobTitleID`/`SupervisorID` as the three routing axes | Already covered by `../workflow/`'s mapping for the routing *engine*; this module's contribution is that the *person record itself* must carry all three, queryable, for routing to work at all. |
| The audit-stamp load on the identity record (`PPL-R-007`) | A cross-cutting `createdBy`/`modifiedBy` mechanism at the platform/base-entity level (e.g. a JPA `@MappedSuperclass` or auditing aspect resolving `X-User-Id` from the gateway-forwarded header), not something every service or aggregate re-implements per-object the way Lucernex's 162 objects each carry their own inline stamp columns. |

## 3. What should deliberately differ

| Lucernex pattern | Why ASG Edge+ should not copy it | Deliberate alternative |
|---|---|---|
| `NonMember` as a field-for-field duplicate of `Person` with no distinguishing columns of its own | Two physically identical tables serving (apparently) the same purpose is either dead weight or an unexplained design choice — not worth reproducing until the open question in `member-vs-person-vs-party.md` is resolved | Model "has no login" as a nullable/absent credentials sub-object on the single identity aggregate, per `PPL-R-001`, rather than as a second table |
| A second, unexplained credential pair (`AnySiteLoginName`/`AnySitePassword`) alongside the primary one | Ambiguous purpose; risks becoming a second, less-audited authentication path if copied blindly | If external/vendor-portal login is needed, model it as an explicit, separately-scoped credential type on the same identity aggregate — not a silently parallel field pair |
| `Employer.IsVendor`/`IsPreferredVendor`/`IsREContractVendor`/`IsEquipContractVendor` as boolean flags | Adding a new counterparty role means adding a new boolean column, the same extensibility cost `../platform-tenancy/rules.md#plt-r-004` flags for `Firm`'s setup-layout columns | A role/classification join (counterparty ↔ role-type) that doesn't require a schema change per new role |
| Four separate numbered approval-amount-band pairs on `Member` (`Payment`/`Recurring` × `Min`/`Max`, doubled for `Equip*`), apparently unread by any workflow field | Dead or orphaned configuration surface is a maintenance hazard and a false signal to future engineers that amount-banded routing works | If amount-banded approval routing is wanted (a real, named gap in Lucernex per `PPL-R-013`), design it as an explicit routing rule input, verified end-to-end, rather than copying fields whose consumer cannot be found in this schema |

## 4. Decisions blocking a build

1. **Compare `ASG-Edgeplus-User-Service`'s actual schema against the `Person`/`Member`/`NonMember`
   split documented here.** If the service already collapses these into one identity table, this
   module's finding is confirmation, not new scope. If it mirrors Lucernex's three-table split, this
   module's evidence argues for consolidating before more code is built on top of it.
2. **Does ASG Edge+ need a `NonMember`-equivalent concept at all** — i.e., a record for "a known
   person with no system access" — or is that better modelled as simply a `Person`/`Contact` row with
   no associated `User` credential? This module's evidence favours the latter (`PPL-R-001`,
   `PPL-R-003`) but the decision belongs to whoever owns the identity/user service.
3. **Should `Employer` remain in the Hub as a single shared counterparty record**, given ASG Edge+'s
   database-per-tenant Spoke design means each firm's vendor/landlord list is presumably firm-specific
   data, not shared platform reference data? Lucernex's `Employer` being `firm_global` in its own
   spine classification does not automatically mean "shared across ASG Edge+ tenants" — it means "not
   scoped by `ProjectEntityID` within one Lucernex tenant." Whether ASG Edge+'s per-firm Spoke should
   own its own `Employer`-equivalent table (most likely, since each ASG client has its own vendors and
   landlords) is a modelling question this module's evidence does not by itself resolve, and is worth
   flagging explicitly so `firm_global` is not misread as "Hub-shared across ASG Edge+ tenants."
4. **Is the `Party` concept worth building at all**, given no live capture in this corpus shows it
   populated? Low-cost to defer; revisit if a specific BRD names a role that doesn't fit
   `Employer`/`Person`/`LinkProjectEntityContact`.
