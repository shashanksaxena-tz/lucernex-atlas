# People & Parties

*In scope for the rebuild*

Everyone the system knows about: internal Members (users), external Persons and Parties, and Employer records — the single table behind landlords, tenants and vendors alike (doc 009).

Stated up front. Ten objects, 301 fields, and one object — Member — with 290 foreign keys pointing at it, the single most-referenced record in the 223-object schema (second is ProjectEntity at 163; see data-model.md). This module holds everyone the system knows about: internal Member (a real login), external Person/NonMember (no login), the company record Employer (which is also, relabelled, Vendor/Landlord/Tenant — see 009), and Party (a thin per-contract role assignment tying a company and/or a person to a lease with a classification).

|  | Count |
|---|---|
| Record types | 10 |
| Fields | 301 |
| Keys in | 309 |
| Keys out | 14 |
| Rules | 13 |

## What was found here

### Member is the most-referenced record, but mostly as an audit stamp

**Derived.** 290 foreign keys point at it — more than ProjectEntity. But 240 of them, 83%, are just the universal CreatedByID / ModifiedByID pair. Only 50 are genuine business references: approvers, assignees, checkout locks, bid parties, brokers. Member is the schema's universal 'who did this' anchor far more than it is a business entity.

### The identity service sits on nearly every write path

**Derived.** Because 161 objects carry ModifiedByID and 79 carry CreatedByID, any write anywhere needs to resolve a member. That argues for a cross-cutting created-by / modified-by mechanism rather than each service reimplementing the stamp, and for identity being cheap to reach.

### There is a second supertype hiding in the schema

**Derived.** Person and NonMember are field-for-field identical — 37 fields, zero differences. Member is Person's 37 plus 44 login and authentication fields. All three share PersonID, typed as a plain Number rather than a declared foreign-key type. It is the same shared-key inheritance pattern ProjectEntity uses, applied to people, and nothing names it.

### The tenant key is not modelled as a relationship

**Observed.** FirmID is typed Text. It is not a declared foreign-key type anywhere in the schema. The one relationship every single row has is the one Lx's own type system declines to model — which is exactly why tenant isolation cannot be enforced by the schema.

### The org chart is a self-reference on Member

**Observed.** Member.SupervisorID points at Member. But workflow's REGION1, REGION2 and MARKET routing does not resolve through any Member column — it goes through ProjectEntity.RegionID / RootRegionID / SubRegionID and LinkRegionManager. Two different hierarchies, and routing uses the geographic one.

### Region is nearly empty and heavily referenced

**Observed.** Twelve objects reference Region across 34 columns, yet Region itself declares a single field. Whatever a region actually stores is not in the schema dump — a genuine gap that needs a targeted capture.

## Record types

| Record type | Postgres table | Fields | Referenced by |
|---|---|---|---|
| [Member](../entities/Member.md) | `member` | 81 | 290 |
| [Employer](../entities/Employer.md) | `employer` | 71 | 40 |
| [NonMember](../entities/NonMember.md) | `non_member` | 37 | 0 |
| [Person](../entities/Person.md) | `person` | 37 | 0 |
| [EmployerSite](../entities/EmployerSite.md) | `employer_site` | 20 | 1 |
| [VendorInsurance](../entities/VendorInsurance.md) | `vendor_insurance` | 15 | 0 |
| [LinkProjectEntityContact](../entities/LinkProjectEntityContact.md) | `link_project_entity_contact` | 12 | 0 |
| [MemberAudit](../entities/MemberAudit.md) | `member_audit` | 12 | 0 |
| [Party](../entities/Party.md) | `party` | 12 | 0 |
| [LinkProjectEntityVendor](../entities/LinkProjectEntityVendor.md) | `link_project_entity_vendor` | 4 | 0 |

## Rules

| Rule | Subject | What it requires | Confidence |
|---|---|---|---|
| [PPL-R-001](../rules/PPL-R-001.md) | `Person` is a supertype; `Member` and `NonMember` are its subtypes on a shared key | `Person` and `NonMember` are field-for-field identical (37/37, zero type mismatches); `Member` is that same 37-field block plus 44 login/authorization fields | Derived |
| [PPL-R-002](../rules/PPL-R-002.md) | No hard FK type references a person directly; `Contact` is the soft, polymorphic type | No `Person ID` FK type exists anywhere in the 60-odd declared FK types | Inferred |
| [PPL-R-003](../rules/PPL-R-003.md) | `ConvertToMember` implies promotion, not replacement | The existing identity is promoted to carry login/authorization data; it is not deleted and recreated. The exact mechanics (same row extended vs. new row sharing `PersonID`) are open — see `member-vs-p | Inferred |
| [PPL-R-004](../rules/PPL-R-004.md) | `Employer` is one table serving three business roles | No `Vendor`, `Landlord`, or `Tenant`-as-counterparty object exists in the 223-object schema | Observed |
| [PPL-R-005](../rules/PPL-R-005.md) | `Party` is a generic, classified role assignment, not an identity record | Both `CompanyID` and `ContactID` are independently nullable | Derived |
| [PPL-R-006](../rules/PPL-R-006.md) | The per-entity contact roster and the per-entity vendor list are separate, differently-shaped joins | Contacts get a typed, richer roster entry; approved vendors get a bare membership list with no role classification at all | Observed |
| [PPL-R-007](../rules/PPL-R-007.md) | 83% of `Member`'s in-degree is the universal audit-stamp pair, not business routing | The identity/user record must be cheaply reachable from nearly every write path in the product for stamping alone, independent of its true business-domain reference count (50 edges) | Derived |
| [PPL-R-008](../rules/PPL-R-008.md) | `MemberAudit` is login/session audit, not field-change audit | This is a distinct audit mechanism from `../platform-tenancy/`'s `AuditColumn` (which logs field-level changes) — `MemberAudit` logs session/security events specifically | Observed |
| [PPL-R-009](../rules/PPL-R-009.md) | A member's routable identity is three independent axes | A person can be selected by class, by title (global or entity-specific), or by reporting-line position, and these three do not have to agree with each other | Observed |
| [PPL-R-010](../rules/PPL-R-010.md) | Per-entity job title can override the member's global default | Differs from `Member.CodeJobTitleID` | Inferred |
| [PPL-R-011](../rules/PPL-R-011.md) | Region/Market routing resolves through the entity, not through any `Member` column | This is a two-hop resolution (entity → region/market → manager), not a direct `Member` attribute lookup | Derived |
| [PPL-R-012](../rules/PPL-R-012.md) | Production routing barely uses any of the above | The rich role-based apparatus this module documents is largely latent in ASG's actual configuration. Treat as lower priority pending the answer to `../workflow/routing-and-approvals.md` OQ-42 (deliber | Observed |
| [PPL-R-013](../rules/PPL-R-013.md) | Approval-amount bands exist on `Member` but are read by no observed workflow field | No `WorkFlowTemplateStep`/`WorkFlowTemplateStepAction` field reads these columns (exhaustive check, `../workflow/step-actions.md`/`routing-and-approvals.md`) | Derived |
