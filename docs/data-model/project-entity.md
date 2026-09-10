# `ProjectEntity` — the spine of the product

**Stated up front.** `ProjectEntity` is not a "project" table. It is the product's **universal
entity supertype**: one row per *thing you can own* — a portfolio, a capital program, a capital
project, a site, a facility, a location, a parcel, a prototype, a lease, an equipment contract.
Every one of those has its own detail table, and **all of them inherit `ProjectEntity`'s identity
column block on a shared key**. Every other object in the product — 161 of 223 — carries a
`ProjectEntityID` foreign key back to it.

That makes `ProjectEntityID` the closest thing Lucernex has to a partition key, and it is
**not the tenant key**. The tenant key is `FirmID`. `ProjectEntityID` partitions *within* a tenant.
For ASG Edge+'s database-per-tenant design this is the important distinction, and §5 works through
what follows from it.

Confidence: **Derived** — every claim below is a mechanical property of the field lists in
`_lucernex_objects_summary.txt`, reproducible by re-running
[`../mindmap/build_graph.py`](../mindmap/build_graph.py). Where corroboration comes from a screen
capture it is marked **Observed** and cited.

## 1. The evidence, in the order it forces the conclusion

### 1.1 `Entity ID` is the FK type for `ProjectEntity`

| Fact | Where |
|---|---|
| `ProjectEntity`'s own `ProjectEntityID` column is typed **`Number`** | The `ProjectEntity` row of the export |
| 161 other objects carry a `ProjectEntityID` column typed **`Entity ID`** | 161 rows of the export |
| No object anywhere is named `Entity` | The 223-object list |
| `Entity ID` appears on 163 columns; 161 of them are literally named `ProjectEntityID` | `build_graph.py` |

A type named after its target table (**Observed**,
[009](../admin/009-related-fields-and-data-model.md)) whose only plausible target has that exact
column as its own key, used on a column of that exact name 161 times, is `ProjectEntity`. The other
two `Entity ID` columns are `BudgetOptionTemplate.BudgetOptionTemplateID` and
`DevelopmentSlot.ProjectPEID`.

Corroboration from an independent capture: [`../data-fields/INDEX.md`](../data-fields/INDEX.md)
documents `sTYPE_PROJECT_ENTITY` as "Lookup reference to a ProjectEntity record", and — critically
— `sTYPE_PORTFOLIO` as **"Lookup reference to a *portfolio-level ProjectEntity* record"**. A
portfolio *is* a ProjectEntity. That single legend line is the first hint that ProjectEntity is a
supertype rather than one entity among many.

### 1.2 Eight other objects inherit `ProjectEntity`'s column block

Nine objects — `Contract`, `Facility`, `Location`, `Parcel`, `Program`, `Prototype`,
`PotentialProject`, `Project`, `BudgetOptionTemplate` — carry this **identical** block of columns,
and no other object carries any of it:

| Column | Type | On `ProjectEntity` | On the nine |
|---|---|---|---|
| `EntityId` | `Number` | ✓ | ✓ |
| `ProjectEntityID` | `Number` — **not** `Entity ID` | ✓ | ✓ |
| `ProjectEntityName` | `Text` | ✓ | ✓ |
| `ProjectEntityTypeName` | `Text` | ✓ | ✓ |
| `ClientEntityID` | `Text` | ✓ | ✓ |
| `EntityEmail` | `Text` | ✓ | ✓ |
| `EntityPhoto` | `Text` | ✓ | ✓ |
| `LinkProjectEntityContactListData` | `Contact` | ✓ | ✓ |

The type is the tell. On a *child* object `ProjectEntityID` is typed `Entity ID` — a foreign key.
On these nine it is typed `Number` — the same as on `ProjectEntity` itself. **They are not
referencing the supertype; they are carrying its key.** That is the signature of table-per-subtype
inheritance on a shared primary key, and the vendor's schema browser reports the joined column set
for each subtype.

The `ProjectEntityTypeName` column is the discriminator.

### 1.3 `ProjectEntity`'s own 107 fields are a union of all the subtypes

Its field list is not project-shaped. It is everything-shaped:

| Group of columns | What it belongs to |
|---|---|
| `FacilityName`, `RentableArea`, `UsableArea`, `GrossArea`, `Frontage`, `Depth` | Facility |
| `LocationID`, `StreetAddress1..4`, `City`, `PostalCode`, `CountryID`, `LatitudeDegrees`, `LongitudeDegrees`, `TimeZone`, `CrossStreet1/2`, `HTMLAddress` | Location |
| `ComplexID`, `PrototypeID`, `DemographicDMAID`, `TradeArea`, `CodeMarketAreaID`, `CodeMarketTypeID`, `CodeDistributionCenterID` | Site selection |
| `ProgramID`, `ProgramName` | Portfolio / Program |
| `PotentialProjectName`, `ProjectName`, `ProjectDescription` | Project pipeline |
| `DesignPhaseStatus`, `ConstructionPhaseStatus`, `PossessionPhaseStatus`, `OperationsPhaseStatus`, `RealEstatePhaseStatus`, `CompletedPhaseStatus`, `CurrentPhaseStatus`, `CurrentMilestone`, `NextMilestone`, `PreviousMilestone` | Lifecycle, common to all |
| `RegionID`, `RootRegionID`, `SubRegionID` | The region hierarchy, common to all |
| `Firm_SalesReportLogo`, `Firm_SalesReportSignature*` | Tenant customisation |

Seven denormalised name columns (`ProjectEntityName`, `FacilityName`, `ProgramName`, `ProjectName`,
`PotentialProjectName`, `PrototypeName`, plus `ProjectEntityTypeName`) sitting on one table is not
how you model a project. It is how you model **"whatever this entity is, here is its display
name"**.

### 1.4 The 11 `IsValidFor*` flags name the subtypes explicitly

`VirtualTemplateBudget`, `VirtualTemplateBudgetOption`, `VirtualTemplateFolder` and
`VirtualTemplateSchedule` each carry the same eleven boolean columns (the first two are out of
scope for the rebuild, but the second two are not — so this evidence survives the scope
exclusion intact):

`IsValidForPortfolio`, `IsValidForCapProgram`, `IsValidForCapProject`, `IsValidForOpenProject`,
`IsValidForPotentialProject`, `IsValidForContract`, `IsValidForEquipContract`, `IsValidForFacility`,
`IsValidForLocation`, `IsValidForParcel`, `IsValidForPrototype`

That is the product asking, for each template, *"which kinds of entity may I be attached to?"* —
a question that only makes sense if all eleven kinds share one attachment mechanism.

### 1.5 The vendor's own tool agrees

**Observed**, [009](../admin/009-related-fields-and-data-model.md): `walkHierarchy.jsp`'s
aggregate-root "Show" dropdown lists

`Portfolio, Capital Program, Prototype, Location, Parcel, Site, Opening Project, Facility,
Capital Project, RE Contract, Equipment Contract, Firm, Firm All Children, All Tables`

Set that beside the `IsValidFor*` list and they are the same enumeration, modulo naming
(`Site` ↔ `PotentialProject`, `Opening Project` ↔ `OpenProject`, `RE Contract` ↔ `Contract`). Two
independently captured sources, one from a JSP admin tool and one from a virtual view's column
names, enumerate the same eleven entity types. `Firm` is the outlier in the walkHierarchy list, and
that is exactly right — the Firm is the tenant, not an entity.

## 2. The three-way split of all 223 objects

| Role | Objects | Fields | Definition |
|---|---:|---:|---|
| `supertype` | 1 | 107 | `ProjectEntity` |
| `subtype_root` | 9 | 1,617 | Carries the supertype column block with `ProjectEntityID` typed `Number` |
| `entity_scoped` | 161 | 4,644 | Carries a `ProjectEntityID` typed `Entity ID` — a hard FK to the spine |
| `firm_global` | 52 | 1,053 | Neither. Lives above the spine. |

### The 9 subtype roots

| Object | Fields | walkHierarchy name | Notes |
|---|---:|---|---|
| `Contract` | 570 | RE Contract / Equipment Contract | The two contract flavours share one table — no `EquipmentContract` object exists. |
| `Program` | 180 | Portfolio / Capital Program | Reached by the `Portfolio ID` type (**Observed** mismatch, [009](../admin/009-related-fields-and-data-model.md)). Self-references via `OrgChartProgramID`. |
| `Parcel` | 154 | Parcel | Self-references via `MasterParcelID`. |
| `Location` | 141 | Location | |
| `Facility` | 133 | Facility | |
| `Prototype` | 113 | Prototype | |
| `Project` | 111 | Capital Project / Opening Project | |
| `PotentialProject` | 108 | Site | |
| `BudgetOptionTemplate` *(out of scope)* | 107 | — | **Does not belong here.** It has no physical table and carries `BudgetTemplateID`; it is a denormalised `ProjectEntity` × `BudgetTemplate` view that happens to match the column signature. Flagged as a false positive of the mechanical test. |

Eight genuine subtypes, and the walkHierarchy root list is fully accounted for.

### The 52 firm-global objects — the natural Hub

These are the objects with **no** connection to the entity spine. They are almost exactly what you
would put in a shared platform database:

| Category | Objects |
|---|---|
| Tenant & security | `Firm`, `Security`, `UserClassSecurity`, `GlobalProperty` |
| Identity & parties | `Member`, `NonMember`, `Person`, `Organization`, `Employer`, `EmployerSite`, `VendorInsurance` |
| Geography & currency | `StateProvinceCountry`, `Jurisdiction`, `DMA`, `Complex`, `ExchangeRate` |
| Reference code lists | `CodeASC842Schedule`, `CodeIFRS16Schedule`, `CodeSLSchedule`, `CodeExpenseType`, `CodeAssetCategory`, `CodeBudgetColumnStatus` *(out of scope)*, `CodeIssueType`, `CodeProblem`, `CodeResponsibleParty`, `CodeSalesGroup`, `CodeSalesType` |
| Rates & indices | `DiscountRate`, `EscalationIndex`, `HolidaySchedule`, `HolidayDate` |
| Templates | `WorkFlowTemplate`, `WorkFlowTemplateStep`, `ProcessTimelineTemplate`; plus `BudgetColumnType`, `BudgetIndex` *(out of scope)* |
| Parts catalogue | `Part`, `PartPackage`, `PartPackageItem` |
| Configuration | `CustomCodeField`, `ReportGroupAvailableField`, `ReportGroupData` |
| Demographics reference | `DemographicFact`, `DemographicReport`, `DemographicStudyArea` |
| Miscellaneous | `AssetHistory`, `FolderSecurity`, `ReTransScenContact`, and the four firm-global `Virtual*` projections |

Of these 52, **five are out of scope** (`BudgetColumnType`, `BudgetIndex`, `CodeBudgetColumnStatus`,
and two `Virtual*` budget-template views), leaving **47 in-scope Hub candidates**.

One caveat, and it matters: **`AssetHistory` is a false negative.** It carries `ProjectEntityID`
and `FromProjectEntityID` typed with the *soft* `Entity` type rather than the hard `Entity ID`, so
the mechanical test misses it. It is entity-scoped in reality. Anything relying on this
classification should treat the soft `Entity` type as scoping too — that adds 13 more objects.

## 3. Why it is nearly universal

`ProjectEntityID` is on 161 objects because **it is how any record says what it is about.** A
payment, a task, a document, a budget line, an insurance policy, a covenant — each belongs to *some*
entity, and which kind of entity varies. Rather than give every child table a nullable
`FacilityID` + `LocationID` + `ContractID` + `ParcelID` + …, Lucernex gives it one
`ProjectEntityID` and resolves the type through the supertype's `ProjectEntityTypeName`.

This is a **polymorphic association implemented as real inheritance**, and it buys the product three
things that are visible in the corpus:

1. **One attachment mechanism for everything.** Documents, folders, budgets, schedules, workflows
   and tasks attach to *any* entity type through one column. The `IsValidFor*` flags are how a
   template declares which types it accepts.
2. **One page-layout mechanism.** `Firm` carries `ContractSetupPageLayoutID`,
   `FacilitySetupPageLayoutID`, `LocationSetupPageLayoutID`, `ParcelSetupPageLayoutID`,
   `PrototypeSetupPageLayoutID`, `SiteSetupPageLayoutID`, `OpenProjectSetupPageLayoutID`,
   `EquipmentContractSetupPageLayoutID`, `CapProjectSetupPageLayoutID`, `CapProgramSetupPageLayoutID`
   and `PortfolioSetupPageLayoutID` — **one column per subtype**, which is only expressible because
   the subtypes are enumerable and share a root.
3. **One security and audit boundary.** `AuditColumn` carries `ProjectEntityID`;
   `LinkMemberProjectEntity` assigns members to entities. Access control and audit are expressed
   once, against the spine, not per entity type.

## 4. Is `ProjectEntityID` a tenant partition key?

**No — and this is the load-bearing answer for ASG Edge+.**

| Question | Answer | Evidence |
|---|---|---|
| Does `ProjectEntityID` identify the tenant? | No | `ProjectEntity` itself carries `FirmID(Text)`. The tenant key is `FirmID`. |
| Does `ProjectEntityID` partition data *within* a tenant? | Yes | 161 objects scope every row to one entity; access is granted per entity via `LinkMemberProjectEntity` and `ProjectEntity.ManagerIDList`. |
| Is a portfolio a `ProjectEntity`? | Yes | `sTYPE_PORTFOLIO` = "portfolio-level ProjectEntity record" ([`../data-fields/INDEX.md`](../data-fields/INDEX.md)); `IsValidForPortfolio`; `Portfolio ID` → `Program`. |
| Is `FirmID` on the child objects too? | **No** | `FirmID` appears on exactly 13 objects: `ProjectEntity`, all nine subtype roots, and the three configuration objects `GlobalProperty`, `ReportGroupAvailableField`, `ReportGroupData`. **Not one of the 161 `entity_scoped` children carries it.** They reach the tenant *through* the spine. |
| Is `FirmID` even a typed FK? | No | It is typed `Text`, not `Firm ID`. There is no `Firm ID` FK type in the 60. The tenant key is the one reference in the product that the type system does not model. |

That last row is the one to sit with. In Lucernex, a `PaymentTransaction` does not know which firm
it belongs to. It knows its `ProjectEntityID`, and the `ProjectEntity` knows its `FirmID`. **Tenant
isolation is one join deep on every single query in the product.**

## 5. What this means for ASG Edge+

### 5.1 The Hub/Spoke boundary is already drawn in the data

ASG Edge+'s target shape (per `ASG-Edgeplus-Configuration-Service`'s workspace index) is a Hub of
Masters, global Data Fields, global Layouts, Drop Downs, Workflows/Forms and the shared
`Location`/`Organization`/User entities, with a per-firm Spoke holding Portfolios, Contracts and
everything beneath a Contract. Lucernex's own `firm_global` / `entity_scoped` split maps onto that
almost cleanly:

| ASG Edge+ intent | Lucernex evidence | Fit |
|---|---|---|
| Hub holds Masters and reference data | The 11 `Code*` tables, `StateProvinceCountry`, `Jurisdiction`, `ExchangeRate`, `DiscountRate`, `EscalationIndex`, `HolidaySchedule` are all `firm_global` | **Clean** |
| Hub holds User management | `Member`, `NonMember`, `Person`, `Organization`, `Security`, `UserClassSecurity` are all `firm_global` | **Clean** |
| Hub holds global Workflows/Forms templates | `WorkFlowTemplate`, `WorkFlowTemplateStep`, `ProcessTimelineTemplate` are `firm_global`; the *instances* (`WorkFlow`, `WorkFlowStep`) are `entity_scoped` | **Clean, and instructive** — the template/instance split lands exactly on the Hub/Spoke line |
| Hub holds `Location` and `Organization` | `Organization` is `firm_global` ✓ — but **`Location` is a `subtype_root`**, deep inside the entity spine, with 141 fields and a `ProjectEntity` identity | **Conflict — see 5.2** |
| Spoke holds Portfolios, Contracts and their children | `Program` (Portfolio), `Contract` and the 161 `entity_scoped` objects | **Clean** |

### 5.2 The conflict worth raising now

The workspace index puts **`Location` in the Hub**. Lucernex puts `Location` in the entity spine —
it is a `ProjectEntity` subtype with its own 141-field detail table, an address, a region hierarchy
and a lifecycle. It cannot be Hub-global and also be a portfolio-partitioned entity carrying
per-firm operational data.

This is a real design question, not a documentation error. Either:

- **(a)** ASG Edge+'s `Location` is a narrower concept than Lucernex's — a master address/geography
  record — and Lucernex's `Location` maps to something Spoke-side; or
- **(b)** `Location` genuinely belongs in the Spoke and the Hub definition needs amending.

Nothing in this corpus decides it. It should be decided before either service models `Location`.

### 5.3 Consequences for database-per-tenant

| Lucernex property | Consequence for ASG Edge+ |
|---|---|
| Children carry no `FirmID` — tenant is reached via `ProjectEntity` | **Database-per-tenant removes this join entirely.** Every row in a Spoke database is that firm's by construction. This is a genuine simplification the rebuild gets for free, and it is the strongest data-side argument for ADR-004's database-per-tenant choice. |
| `ProjectEntityID` is still needed *within* a tenant | Do **not** drop it. It is the intra-tenant partition — the portfolio/entity a record belongs to — and the access-control unit (`LinkMemberProjectEntity`). Database-per-tenant replaces `FirmID`, not `ProjectEntityID`. |
| The supertype is real inheritance, not a discriminator column | ASG Edge+ must decide explicitly: shared-key table-per-subtype (Lucernex's choice), single-table with a discriminator, or independent aggregates with no shared root. Choosing "independent aggregates" is defensible but silently costs the three capabilities in §3 — universal attachment, per-subtype layout binding, and one security boundary. Those are exactly PAGE-LAYOUTS-01's and MDM-01's problem space. |
| 161 objects carry `ProjectEntityID`; 8 real subtypes; 52 firm-global objects | A concrete first-cut Hub/Spoke inventory. The 52 are Hub candidates; the remaining 171 are Spoke; `Location` is the disputed one. |
| Tenant-custom columns (`Firm_*`) are physically merged into shared tables — 258 of `Contract`'s 570 | Database-per-tenant makes this *legitimate* rather than a smell, because the table is already that firm's. It is a point in favour of the target architecture, and a reason ASG Edge+ should not copy the current `Configuration-Service` shared-platform-database reading of `0004-multi-tenant-defense-in-depth.md`. |

## 6. Confidence summary

| Claim | Label |
|---|---|
| `Entity ID` is the FK type for `ProjectEntity` | **Derived**, high — 161/163 columns literally named `ProjectEntityID`, and `ProjectEntity`'s own key is typed `Number` |
| Eight objects are shared-key subtypes of `ProjectEntity` | **Derived**, high — identical 8-column block, `ProjectEntityID` typed `Number` not `Entity ID`, no other object carries any of it |
| `ProjectEntityTypeName` is the discriminator | **Inferred** — the name and the eleven `IsValidFor*` flags are consistent with it; no screen was captured showing its values |
| The eleven entity types | **Observed** (walkHierarchy dropdown, [009](../admin/009-related-fields-and-data-model.md)) corroborated by **Derived** (`IsValidFor*` columns) |
| `FirmID` is the tenant key, `ProjectEntityID` is not | **Derived** — `FirmID` is on `ProjectEntity`, the nine subtype roots and three configuration objects, and on none of the 161 children |
| `BudgetOptionTemplate` is a false-positive subtype | **Inferred** — no physical table, carries `BudgetTemplateID`, no plausible entity semantics |
| The Hub/Spoke mapping in §5.1 | **Inferred** — a proposal, not a finding |

## Open questions

Ranked by how much they block work.

1. **Does `Location` belong in the ASG Edge+ Hub or the Spoke?** (§5.2) Blocks any `Location`
   modelling in either service. Lucernex's answer and the workspace index's answer disagree.
2. **What are `ProjectEntityTypeName`'s actual values?** The eleven types are inferred from two
   indirect sources. A single `walkHierarchy.jsp` "All Values For" pass, or a
   `ShowObjectDetails.jsp` read of `ProjectEntity`, would confirm the enumeration directly — and
   this enumeration is the backbone of the whole subtype model.
3. **Is the subtype relationship a shared primary key, or a separate FK?** The export shows both
   `EntityId` and `ProjectEntityID` as `Number` on every subtype root. Two numeric identity columns
   is unusual and unexplained; one of them may be the real shared key and the other a legacy or
   display id. This determines how ASG Edge+ would model the inheritance if it chose to.
4. **Where do `Site`, `Opening Project`, `Capital Program`, `Capital Project` and
   `Equipment Contract` live physically?** They are named as aggregate roots and as `IsValidFor*`
   flags, but no object bears those names. Best reading: they are `ProjectEntityTypeName` values
   over `PotentialProject`, `Project`, `Program` and `Contract` — but "Capital Program vs Portfolio
   both mapping to `Program`" and "RE Contract vs Equipment Contract both mapping to `Contract`"
   needs confirming, not assuming.
5. **Do the 13 objects using the soft `Entity` type (e.g. `AssetHistory`) count as entity-scoped?**
   They behave as if they do; the mechanical classification misses them because their column is
   typed `Entity`, not `Entity ID`.
6. **Is `ProjectEntity` itself firm-scoped or shared?** It carries `FirmID`, which says firm-scoped.
   But `Complex`, `DMA` and `StateProvinceCountry` — which `ProjectEntity` points *at* — are
   firm-global. A Spoke database would therefore need read access to Hub reference data on every
   entity read. That is the Hub→Spoke publish/accept mechanism the workspace index flags as not yet
   written down, and this is a concrete case for it.
