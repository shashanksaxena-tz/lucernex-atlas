# How Lucernex actually separates tenants

**Stated up front.** Lucernex has two keys that look like they could be "the tenant," and only one
of them is. `FirmID` is the tenant key — it is the one column that says *which client this row
belongs to*. `ProjectEntityID` is the intra-tenant partition key — it says *which portfolio,
contract, facility, or other owned thing this row is about*, and it says nothing about which firm
that is, because 161 of 223 objects carry `ProjectEntityID` and **none of them also carry
`FirmID`**. This was fully derived in
[`../../data-model/project-entity.md`](../../data-model/project-entity.md) §4 from the field-type
evidence; this document does not re-derive it, only extends it with the one piece of live evidence
`project-entity.md` didn't have — the session JWT's `cluster` claim — and works through what the
combination means for the ASG Edge+ database-per-tenant decision, without deciding it.

## The two keys, restated once for this module's purposes

| Key | Typed as | Lives on | Answers |
|---|---|---|---|
| `FirmID` | `Text` — **not** a declared FK type | `ProjectEntity`, the 9 subtype roots, and 3 config objects (13 objects total) | *Which tenant?* |
| `ProjectEntityID` | `Entity ID` (FK) on 161 children; `Number` (shared key) on the 9 subtypes and `ProjectEntity` itself | 161 `entity_scoped` objects, this module's own `LinkMemberProjectEntity`/`Region`/`AuditColumn`/etc. | *Which owned thing, within some tenant?* |

The decisive fact, from `project-entity.md` §4: **`FirmID` is typed `Text`, not a first-class FK
type.** Lucernex's own schema declares dozens of `<Entity> ID` types — `Facility ID`, `Contract
ID`, `Employer ID`, `Member ID` — each one a first-class reference the type system understands. It
declares no `Firm ID` type. The one relationship every single row in a multi-tenant product
ultimately has — *which tenant do I belong to* — is the one relationship Lucernex's own type system
does not model as a relationship at all. Tenant identity is present in the data but architecturally
invisible in the schema.

## The `cluster` JWT claim — the one piece of live evidence

**Observed**, [`../../data-model/graphql-api.md`](../../data-model/graphql-api.md): the session
JWT minted for the GraphQL Explorer carries a `cluster` claim shaped `<host>:<tenant-schema>`,
alongside `firmname` (the tenant identifier, in plain text, riding in the same token). **Inferred**:
the `host:tenant` shape is consistent with the request being routed to a tenant-specific database or
schema keyed off a value carried in the token — the same shape of idea as ASG Edge+'s own planned
`AbstractRoutingDataSource` Hub/Spoke routing (an unused reference implementation already sitting in
`ASG-AssetStrategiesGroup-EdgePlus/backend/services/multitenant`, per the workspace index).

**What this does and does not prove.** It proves Lucernex's runtime has *some* concept of routing a
session to a physical location keyed by tenant. It does **not** prove database-per-tenant at the SQL
level, and it does not contradict a shared-schema-with-`FirmID`-discriminator reading either:
`cluster` could equally be a sharding/replica-routing detail sitting in front of a single shared
schema where `FirmID` still does the real isolation work. The static schema export
(`_lucernex_objects_summary.txt`) cannot distinguish the two — it shows one set of table definitions,
which is exactly what you'd see in *either* architecture (one schema replicated per tenant database,
or one schema shared and discriminated by `FirmID`). **This is the single open question this
document cannot close**, and it is exactly the question the ASG estate's own two contradictory
ADR-004s disagree on.

## What Lucernex's data model settles, independent of that question

Whichever way Lucernex itself is built, the **shape of tenant-scoping in the data it exposes** is
settled and is useful regardless:

1. **Isolation is one join deep, everywhere.** No child object carries `FirmID`. A `PaymentTransaction`
   does not know its firm; it knows its `ProjectEntityID`, and only the `ProjectEntity` row knows
   `FirmID`. Every tenant-scoped query in the product is, structurally, "join to `ProjectEntity`,
   filter on `FirmID`" — or would be, if `FirmID` were queryable as a real FK, which it is not.
   (`project-entity.md` §4, **Derived**.)
2. **`ProjectEntityID` does not go away under database-per-tenant.** It is not a tenant-scoping
   mechanism competing with `FirmID` — it is the partition *within* a tenant's data (which portfolio,
   which contract), and access control (`LinkMemberProjectEntity`) and audit
   (`AuditColumn.ProjectEntityID`) are both expressed against it, not against `FirmID`. A
   database-per-tenant Spoke still needs it for exactly the same reasons Lucernex does.
3. **The Hub/Spoke boundary is legible in the `firm_global`/`entity_scoped` split**, with one
   disputed object. `project-entity.md` §5.1 works this out in full — 47 in-scope `firm_global`
   objects are clean Hub candidates, the 161 `entity_scoped` objects are clean Spoke candidates, and
   `Location` is the one object that reads as Spoke-shaped (a `ProjectEntity` subtype with 141 fields
   of address/lifecycle data) while the ASG Edge+ workspace index currently places it in the Hub.
   This module inherits that conflict without adding new evidence to it — see
   [`README.md`](README.md#open-questions) item 3's sibling in `project-entity.md`.

## What this means for the two ADR-004s

The ASG estate carries two documents both numbered ADR-004 that disagree about tenancy:
`KnowledgeFolder/asg-edge-plus-kb/decisions/ADR-004-multi-tenancy-database-per-tenant.md` (accepted,
specifies database-per-tenant, rejects schema-per-tenant and row-level isolation for SOC 2/SOX
reasons) and `ASG-Edgeplus-Configuration-Service/.vault/decisions/0004-multi-tenant-defense-in-depth.md`
(argues for one shared platform database). **This document takes no side.** What the Lucernex
evidence actually supports:

- **In favour of database-per-tenant:** the children's total lack of a queryable `FirmID` means a
  shared-schema, row-level-discriminator design is exactly the pattern that makes a missing
  `WHERE FirmID = ?` clause a silent cross-tenant leak — the one thing `FirmID` being typed `Text`
  rather than a real FK makes structurally easy to get wrong. Database-per-tenant removes the
  discriminator (and the risk of forgetting it) entirely, because every row in a Spoke database is
  that firm's by construction. That argument is made in full in `project-entity.md` §5.3 and is not
  repeated here.
- **Not decided by anything in this corpus:** whether Lucernex *itself* is built database-per-tenant
  (the `cluster` claim is suggestive, not proof), and therefore whether Lucernex is precedent for the
  choice or merely compatible evidence either way.
- **A genuine simplification, either way:** tenant-custom columns (`Firm_*` — 258 of `Contract`'s 570
  fields) are physically merged into the shared tables today. Database-per-tenant makes that
  legitimate rather than a code smell, because the table is already scoped to one firm.
  `project-entity.md` §5.3 makes this point in full; it is the strongest single piece of *design*
  evidence (as opposed to *precedent* evidence) in favour of the choice, and it is independent of
  what Lucernex itself does internally.

## Open questions

Ranked by how much each blocks the ASG Edge+ tenancy decision.

1. **Is Lucernex itself database-per-tenant, schema-per-tenant, or row-discriminated by `FirmID`?**
   The `cluster` JWT claim is the only lead. Nothing short of a second training tenant (to compare
   `cluster` values and infer whether they point at different physical databases) or a vendor
   architecture document would settle this from outside.
2. **Does `Location` belong in the ASG Edge+ Hub or the Spoke?** Restated from `project-entity.md`
   §5.2 because it is this module's own open conflict, not a new one — `Location` is filed under
   `facilities-locations`, not here, but the Hub/Spoke boundary this module is meant to encode
   depends on resolving it.
3. **Is `FirmID`'s absence from the 161 `entity_scoped` children a deliberate design (tenant
   isolation belongs one layer up, at the entity spine) or an artefact of the export missing an
   implicit tenant column enforced elsewhere** (e.g., a database-level row-security policy not
   visible in a schema dump)? If the latter, the "isolation is one join deep" reading in this
   document would be an underestimate of how seriously Lucernex treats it internally.
4. **Does the Hub→Spoke publish/accept/fork mechanism the ASG Edge+ workspace index flags as
   unwritten have a Lucernex precedent?** `ProjectEntity` points at firm-global reference data
   (`Complex`, `DMA`, `StateProvinceCountry`) from what would be Spoke-side rows under either ADR-004
   reading — meaning a Spoke database needs read access to Hub reference data on every entity read,
   which is exactly the mechanism the workspace index says is not yet designed. This is a concrete,
   evidenced case for that design problem, not a new finding — `project-entity.md`'s own open
   question 6 raises it first.
