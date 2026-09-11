# Platform & Tenancy — mapping to ASG Edge+

**Stated up front.** ASG Edge+'s target architecture already names a Hub (Masters, global Data
Fields, global Page/Sub-Page Layouts, global Drop Downs, global Workflows/Forms, plus the shared
`Location`/`Organization`/User entities) and a per-firm Spoke (Portfolios, Contracts, everything
under a Contract). Lucernex's own `firm_global`/`entity_scoped` split lands on that boundary almost
exactly, with one conflict (`Location`) already flagged in
[`../../data-model/project-entity.md`](../../data-model/project-entity.md) §5.2 and not repeated
here. What this module adds: a concrete list of what the Hub needs from *this* module specifically,
and the two open ADRs blocking a build decision.

## 1. What exists

| ASG Edge+ artefact | Status |
|---|---|
| `ASG-EdgePlus-Platform` | Parent POM, domain primitives, identity starter — builds and tests green |
| `ASG-Edgeplus-Configuration-Service` | Masters (MDM-01) + Page/List Layouts — domain/application/REST done, Masters only |
| `asg-edgeplus-starter-identity` | The JWT contract: only the gateway validates a JWT; downstream services receive `X-User-Id`, `X-Tenant-Id`, `X-Roles` |
| `AbstractRoutingDataSource` reference implementation | Exists, unused, in `ASG-AssetStrategiesGroup-EdgePlus/backend/services/multitenant` |
| Two contradictory ADR-004s | Both exist, unreconciled — see `tenancy-model.md` |

Nothing in the two new repos yet models `Firm`/tenant, `Region`, `UserClassSecurity`, or the
geography master tables. Masters (MDM-01) is the closest existing work, and it is scoped to
data-field/layout masters, not tenant or security plumbing.

## 2. What must be built

| Lucernex evidence | What ASG Edge+ needs |
|---|---|
| `Firm` — one row per tenant, 11 subtype-specific setup-layout columns | A tenant record. **Recommendation, not yet decided:** do not copy the one-column-per-subtype pattern (`PLT-R-004`) — model default-layout-per-entity-type as rows in a lookup table keyed by entity-type code, so onboarding a new entity type is a data change, not a schema migration. |
| `FirmID` typed `Text`, no declared FK type | A tenant identifier that **is** a first-class, strongly-typed reference in the ASG Edge+ domain model, carried via the `X-Tenant-Id` header the gateway already forwards — do not repeat Lucernex's own architectural blind spot here (`PLT-R-002`). |
| `Region`/`LinkRegionManager`, `AssigneeType`'s `REGION1`/`REGION2`/`MARKET` | An org-chart region hierarchy, if role-based workflow routing scoped by region is in scope for ASG Edge+. Note `../workflow/routing-and-approvals.md`'s finding that ASG's own live tenant barely uses this (17 of 19 steps route by named Member) — low priority unless a different ASG client needs it. |
| `Security`/`UserClassSecurity`, the `SecurityLevel` ladder | A field/layout/dashboard-scoped permission model. `DEFAULT/NO_ACCESS/VIEW/EDIT/DELETE` is a clean, small enum worth adopting directly rather than re-designing. |
| `StateProvinceCountry`/`Jurisdiction` | Standard geography reference masters — natural Hub content, no open design question. |
| `ExchangeRate` | A point-in-time currency-rate capture per contract, if multi-currency leases are in scope. |

## 3. What should deliberately differ

| Lucernex pattern | Why ASG Edge+ should not copy it | Deliberate alternative |
|---|---|---|
| `FirmID` as an untyped `Text` column absent from 161 of 223 objects | Structurally invites a missing-`WHERE`-clause cross-tenant leak (`tenancy-model.md`) | Database-per-tenant removes the column (and the risk) entirely — the strongest data-side argument for ADR-004's database-per-tenant reading, independent of whether Lucernex itself works that way |
| `Security` as a materialised-looking shadow of `UserClassSecurity` with no declared physical table | Ambiguous whether it is cached, computed on read, or a reporting artefact — not a pattern worth reproducing as-is | Compute effective permissions in the authorization service at request time or via an explicit, documented cache; don't leave the "is this a table" question open the way Lucernex's export does |
| One `Firm` column per `ProjectEntity` subtype for default layouts | Extensibility cost — a new entity type requires a schema migration | A lookup table keyed by entity-type code, as above |
| Two unreconciled audit mechanisms (`AuditColumn`/`AuditTable` vs. inline `CreatedByID`/`ModifiedByID`, present on different subsets of objects) | Ambiguous authority, and this is literally the same open question as ASG Edge+'s own ADR-0020 (in-transaction audit) vs. the ADR-0012 outbox | Pick one audit mechanism and apply it uniformly; do not let some objects get inline stamps and others get the explicit log the way Lucernex's schema does |

## 4. Decisions blocking a build

1. **Database-per-tenant vs. shared-schema-with-discriminator** — the two ADR-004s. Not settled by
   this corpus; `tenancy-model.md` states what the Lucernex evidence does and does not support.
2. **Is `Location` Hub or Spoke?** Blocks any `Location` modelling in either
   `ASG-Edgeplus-Configuration-Service` or a future contracts service. `project-entity.md` §5.2.
3. **The Hub→Spoke publish/accept/fork mechanism** is not designed yet (per the workspace index), and
   this module surfaces a second concrete need for it: Spoke-side `ProjectEntity`-equivalent rows
   would need read access to Hub-side geography/reference masters (`StateProvinceCountry`,
   `Jurisdiction`, `Complex`, `DMA`) on every read, exactly as `project-entity.md` open question 6
   raises.
4. **Whether ASG Edge+ adopts a region/market org-chart hierarchy at all**, given the live tenant's
   near-total reliance on named-Member routing over role-based routing (cross-reference
   `../workflow/routing-and-approvals.md` OQ-42). This is a scope question for whoever owns workflow
   routing, not a platform-tenancy design question per se, but it determines whether `Region` needs
   to exist in ASG Edge+ at all.
