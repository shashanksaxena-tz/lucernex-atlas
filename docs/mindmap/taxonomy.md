# Module taxonomy and the mind-map hierarchy

**Stated up front.** The 223 objects group into **14 in-scope modules plus one deliberately
excluded catch-all**. Nine of the fourteen come from the module folders already scaffolded under
[`../modules/`](../modules/); five are new, and each is new because the evidence forced it, not for
tidiness. Every object has exactly one primary module — the assignment is asserted in
[`build_graph.py`](build_graph.py) and the build **fails** if any object is unassigned or assigned
twice, so the taxonomy is verified on every run rather than maintained by hand.

> ### Scope exclusion — Cost Management and Budgeting
>
> **This is a deliberate scoping decision made by the user on 2026-09-10, relayed via the team
> lead. It is not an oversight, and it is not a finding about the product.**
>
> `budgets-bidding` has been **withdrawn as a first-class module** and its 26 objects, plus
> `BidderIssue`, are collected into a single catch-all module named
> **`out-of-scope-cost-budget`** (27 objects, 546 fields). Those objects remain in
> [`objects.json`](objects.json), [`edges.json`](edges.json) and
> [`../data-model/object-catalog.md`](../data-model/object-catalog.md) so the census still covers
> all 223 objects and the FK graph stays whole — but they get **one-line purposes only**: no module
> write-up, no hub analysis, no sub-module derivation, and no mind-map depth. The
> `docs/modules/budgets-bidding/` folder is being removed.
>
> In-scope totals are therefore **196 objects and 6,875 fields** across 14 modules.
>
> **Two things a later reader should know.** First, I moved six objects beyond the list the
> instruction named — `CodeBudgetColumnStatus`, `BudgetOption`, `LinkBudgetIndexBLI`,
> `LinkBudgetViewBLI`, `VirtualTemplateBudget`, `VirtualTemplateBudgetOption` — because each is
> unambiguously part of the same Budget object family (a budget status code list, a budget option,
> two budget-line-item join tables, and two budget-template views). Say so if that is wider than
> intended. Second, the *Lucernex* dashboard heading "Cost Management" is broader than the
> exclusion: it also covers `accounting`, `expense-recovery`, `variable-rent` and `property-tax`
> (2,518 fields). Those are lease accounting, CAM reconciliation, turnover rent and property tax —
> core lease-administration capability, not capital cost — so I have **kept them in scope**,
> matching the object list the instruction actually named. Flagged as open question 1 below.

For the mind map itself, §4 proposes an **11-level hierarchy** and checks, level by level, whether
the data can actually populate it. Nine of the eleven populate for every object; two populate for
195 of 223 and the shortfall is stated rather than papered over.

## 1. Evidence for the taxonomy

| Source | Weight | What it gave |
|---|---|---|
| System Administrator Dashboard section headings — Company Administration, Portfolio/Capital Program Administration, Portfolio Administration, Member Administration, Folder Administration, Cost Management, Data/PS Tools | **Observed** ([004](../admin/004-company-administration.md)) | The top-level shape a Lucernex administrator already sees. Every module below names the heading it sits under. |
| `walkHierarchy.jsp` aggregate roots — Portfolio, Capital Program, Prototype, Location, Parcel, Site, Opening Project, Facility, Capital Project, RE Contract, Equipment Contract, Firm | **Observed** ([009](../admin/009-related-fields-and-data-model.md)) | Which objects are roots and which are owned children. Drove the `contracts-leases` / `facilities-locations` / `portfolio-transactions` boundaries. |
| Per-entity explanations for 214 entities | **Derived** ([`../data-fields/INDEX.md`](../data-fields/INDEX.md)) | What each object is for, at the granularity needed to place the 190 objects the dashboard headings do not name. |
| The FK graph itself | **Derived** ([`edges.json`](edges.json)) | Sanity check. A module whose objects mostly point at each other is real; one whose objects all point elsewhere is not. |

**Where the scaffolded folder list changed, and why**

| Change | Reason |
|---|---|
| `budgets-bidding` **withdrawn** | User scope decision, 2026-09-10 — see the box above. Its objects survive only as the `out-of-scope-cost-budget` catch-all. |
| `accounting` **kept**, but at 38 objects / 1,265 fields it is the largest module | Accepted. Splitting it further would cut through the expense-setup → schedule → accrual → payment chain, which is one dependency run. |
| `contracts` → **`contracts-leases`** | Naming only; "Contract" in Lucernex covers both RE and Equipment contracts. |
| `projects-capital` **kept**, narrowed to delivery (tasks, schedules, issues, change orders) | The *portfolio* half of the original folder had 11 objects and 513 fields of its own and a completely different dependency profile — it became `portfolio-transactions`. |
| **New: `portfolio-transactions`** | `Program`, `PotentialProject`, `RETransaction`, `Scenario`, `ComparisonReport` are deal-pipeline objects with no task/schedule content. The dashboard has a *separate* heading for them ("Portfolio/Capital Program Administration" vs "Portfolio Administration"). |
| **New: `platform-tenancy`** | Nothing in the scaffolded list owned `Firm`, `ProjectEntity`, `Security`, `Region`, `StateProvinceCountry` or the audit tables — yet these absorb **237 inbound FK columns**, more than any other module. A rebuild that has no home for them has no foundation layer. |
| **New: `people-parties`** | Same argument, stronger: **309 inbound columns**, the single most depended-on module in the product, and it had no folder. `Member`, `Employer` and `Person` cannot be a sub-topic of something else. |
| **New: `variable-rent`** | 17 objects and 472 fields of percentage-rent / use-based-rent / sales machinery, including 7 of the 13 `Virtual*` projections. Buried inside `accounting` it would be invisible; it is a distinct retail-lease capability with its own calculation engine. |
| **New: `expense-recovery`** | 3 objects but **618 fields** — 8.3% of the whole product in three tables. CAM reconciliation is a named commercial capability and `ExpenseRecovery` alone is the second-largest object. It cannot be a footnote in `accounting`. |
| **New: `property-tax`** | 6 objects, 163 fields, a self-contained assessment → bill → appeal → award lifecycle with 5 internal edges. Distinct capability. |
| `assets-equipment` **kept**, widened to include maintenance | `ServiceRequest`, `WorkOrder` and the `Part`/`PartPackage` catalogue have no other home and are the reactive-maintenance loop around `Asset`. |
| `layouts-and-forms` + `reporting` → **merged as `layouts-forms-reporting`** | Together they own only **6 objects and 107 fields**. The reason is itself the finding: **Lucernex's configuration layer is not in this business-object model.** Page layouts, data fields, drop-downs and dashboards are referenced by `item ID` / `Custom Drop Down ID` / `DashboardComponent ID` types that resolve to nothing here (see [`../data-model/type-system.md`](../data-model/type-system.md) §2). Two separate modules over 6 objects would overstate what the data supports. |
| `facilities-locations`, `documents-folders`, `workflow` **kept as-is** | Confirmed by the data. |

## 2. The 15 modules

Ordered by field count. Full machine-readable form in [`modules.json`](modules.json).

| Module | Dashboard heading | Objects | Fields | Internal edges | Out | In | What it is |
|---|---|---:|---:|---:|---:|---:|---|
| `accounting` | Cost Management | 38 | 1,265 | 23 | 146 | 1 | ASC 842 / IFRS 16 / straight-line schedules, expense setups and their generated schedules, accruals, escalation indices, and the payment/invoice ledger. |
| `contracts-leases` | Portfolio Administration | 14 | 1,166 | 29 | 48 | 67 | The `Contract` aggregate root and the lease terms hanging off it: amendments, terms, key dates, covenants, co-tenancy, insurance, security deposits, responsibilities, allowances. |
| `facilities-locations` | Portfolio Administration | 20 | 918 | 23 | 82 | 34 | The physical estate and the site-selection data around it: `Facility`, `Location`, `Complex`, `Parcel`, `Space`, `Parking`, plus prototypes, demographics and site surveys. |
| `expense-recovery` | Cost Management | 3 | 618 | 0 | 13 | 0 | Landlord operating-expense recovery and CAM reconciliation. |
| `portfolio-transactions` | Portfolio/Capital Program Administration | 11 | 513 | 12 | 66 | 10 | The portfolio/capital-program container above projects, plus deal pipeline: potential projects, RE transactions, scenarios, comparison reporting. |
| `variable-rent` | Cost Management | 17 | 472 | 1 | 44 | 2 | Retail turnover rent: reported sales and usage, breakpoints, exclusions and caps, and the virtual period projections that price them. |
| `projects-capital` | Portfolio/Capital Program Administration | 23 | 376 | 11 | 62 | 8 | Project delivery: task/schedule networks with predecessors and holiday calendars, process timelines, change orders, and the issue/RFI loop. |
| `platform-tenancy` | Company Administration / Data-PS Tools | 21 | 385 | 28 | 34 | **237** | The tenant/partition spine and cross-cutting plumbing: `Firm`, `ProjectEntity`, geography and currency reference data, security, audit scaffolding. |
| `people-parties` | Member Administration | 10 | 301 | 22 | 14 | **309** | Internal Members, external Persons and Parties, and `Employer` — the single table behind landlords, tenants and vendors alike. |
| `workflow` | Company Administration | 9 | 262 | 15 | 44 | 0 | Template-driven approval routing: templates and their steps/actions, instantiated workflows, per-step approvers and assignees. |
| `assets-equipment` | Portfolio Administration | 8 | 230 | 1 | 29 | 13 | The asset register and the reactive-maintenance loop: service requests, work orders, parts catalogue. |
| `property-tax` | Cost Management | 6 | 163 | 5 | 28 | 2 | Assessment, bill, appeal and award tracking for real-property tax. |
| `layouts-forms-reporting` | Company Administration / Data-PS Tools | 6 | 107 | 3 | 13 | 2 | The configurable presentation layer's *business-object footprint only*: custom lists and extension parts, custom code fields, questions, report group metadata. |
| `documents-folders` | Folder Administration | 10 | 99 | 2 | 20 | 16 | Document storage with a templated folder tree and per-folder security, plus the inbound/outbound e-mail log. |
| **In-scope total** | | **196** | **6,875** | **175** | | |
| ~~`out-of-scope-cost-budget`~~ | ~~Cost Management~~ | ~~27~~ | ~~546~~ | ~~23~~ | ~~71~~ | ~~13~~ | **Excluded by user decision — see the box at the top. Listed for completeness only.** |
| **Census total** | | **223** | **7,421** | **198** | **714** | **714** | |

### Layering, read off the dependency matrix

| Layer | Modules | Evidence |
|---|---|---|
| **Foundation** — depended on by everything, depends on almost nothing | `people-parties` (309 in / 14 out), `platform-tenancy` (237 in / 34 out) | Build first. |
| **Core domain** — bidirectional | `contracts-leases` (67 in / 48 out), `facilities-locations` (34 in / 82 out), `documents-folders` (16 in / 20 out), `assets-equipment` (13 in / 29 out) | Build second. |
| **Terminal consumers** — nothing points at them | `workflow` (0 in), `expense-recovery` (0 in), `accounting` (1 in), `variable-rent` (2 in), `property-tax` (2 in), `layouts-forms-reporting` (2 in) | Safely extractable as independent services; build last. |

`workflow` and `expense-recovery` having **exactly zero inbound edges** is the cleanest extraction
signal in the whole graph.

### Secondary memberships

Cross-cutting objects also carry secondary modules in [`objects.json`](objects.json) —
`Contract` appears in `accounting`, `variable-rent`, `expense-recovery` and `property-tax`;
`ProjectEntity` in all 13 other in-scope modules; `Member`, `Employer`, `Facility`, `Location`,
`Document`, `WorkFlow`, `ExpenseSetup`, `Covenant`, `Asset`, `Program`, `Task`, `Sales` and
`PaymentTransaction` likewise. No object carries `out-of-scope-cost-budget` as a secondary
module. Primary membership is what the mind map nests
by; secondary membership is what a "where else does this appear" cross-link uses.

## 3. Sub-modules

Level 3 of the mind map needs a sub-module between Module and Entity. It is **derived
mechanically**, not hand-authored, from four properties already in `objects.json`:

| Sub-module | Rule | Example (in `contracts-leases`) |
|---|---|---|
| **Aggregate root** | `pe_scope == "subtype_root"` or in-degree ≥ 5 | `Contract` |
| **Owned children** | `entity_scoped`, in-degree 0, not `Link*`/`Code*`/`Virtual*` | `KeyDate`, `SecurityDeposit`, `Insurance`, `CoTenancy` |
| **Reference / code lists** | name starts `Code`, or `firm_global` with in-degree > 0 | `CodeSLSchedule` |
| **Join tables** | name starts `Link` | `LinkReceiptTransaction` |
| **Computed projections** | name starts `Virtual`, or no `pg_table` | `VirtualPercentageRentPeriod` |
| **Integration projections** | name ends `FullImport` | `PaymentTransactionFullImport` |

Across all 223 objects that partitions into 97 owned children, 26 roots/standalones, 18 join
tables, 13 computed projections, 11 code lists and 2 integration projections among the in-degree-0
set alone — so every in-scope module gets a populated, non-trivial level 3. **Sub-modules are not
derived for `out-of-scope-cost-budget`**: that module terminates the tree at level 2 and its
objects are reachable only through the catalog.

## 4. The mind-map hierarchy — 11 levels, and whether the data reaches each one

Requested: 9–10 levels. The data supports **11**, with an honest caveat on two of them.

| # | Level | Distinct nodes | Source | Populates? |
|---:|---|---:|---|---|
| 1 | **Product** | 1 | LxRetail / Lucernex IWMS | ✅ |
| 2 | **Module** | 14 (+1 excluded) | [`modules.json`](modules.json) | ✅ all 223 objects assigned, verified by assertion in `build_graph.py`. The mind map renders the 14 in-scope modules; `out-of-scope-cost-budget` is either omitted or shown as a single collapsed, visually-muted node with no children. |
| 3 | **Sub-module** | 6 per module (max) | derived, §3 | ✅ mechanical from `objects.json`, for in-scope modules only |
| 4 | **Entity** | 196 in scope (223 in the census) | [`objects.json`](objects.json) | ✅ |
| 5 | **Physical table** | 196 in scope (222 in the census) | `PG TABLE` column | ⚠️ **216 of 223** — 7 objects name no table (a finding, not a gap: see [`../data-model/foreign-key-graph.md`](../data-model/foreign-key-graph.md) §6). `Contract` and `ExpenseRecovery` fan out to 4 each. |
| 6 | **Field group** | 24 | `_crossmap.tsv` `TopGroup`, joined on `LeafTable` | ⚠️ **195 of 223** objects have a Manage Data Fields catalog entry. The other 28 collapse level 6–7 and attach their fields directly to level 4. |
| 7 | **Field sub-group** | 314 group/sub-group pairs | `_crossmap.tsv` `SubGroup` | ⚠️ same 195-object coverage |
| 8 | **Field** | 6,875 in scope (7,421 in the census) | `objects.json` `fields[]` | ✅ every field of every object, parsed count == declared count on all 223 |
| 9 | **Type** | 315 | `objects.json` `fields[].type` | ✅ |
| 10 | **Type family / binding** | 5 families; 60 FK targets; 229 code lists | `type_family` + `edges.json` | ✅ — and this level is where the mind map becomes a *graph*: an FK field's level-10 node is a **link back to a level-4 entity**, and a dropdown field's is a link to a code list. |
| 11 | **Constraint / evidence** | 4 flags + key role | `all-fields.csv` (`Required`, `ReadOnly`, `Scope`, `Default`) and `_crossmap.tsv` `LucKeyRole` (`Primary key`, `Foreign key (ID reference)`, `Client identifier`, `Incremental watermark`, `Audit`) | ⚠️ `Required`/`ReadOnly`/`Scope`/`Default` populate for the 6,158 Manage-Data-Fields leaves; `LucKeyRole` for 372 fields only. Every level-8 node still gets an **evidence** child (source file + confidence label) even where the flags are absent. |

### Worked path, end to end

Every node below is a real value in the source data, not an illustration:

```
LxRetail                                            (1  Product)
└─ Contracts & Leases                               (2  Module — 14 objects / 1,166 fields)
   └─ Aggregate root                                (3  Sub-module — derived, §3)
      └─ Contract                                   (4  Entity — 570 fields, in-degree 61)
         └─ contract_admin                          (5  Table — 1 of 4)
            └─ Contract                             (6  Field group — _crossmap.tsv TopGroup)
               └─ Contract Info                     (7  Sub-group — _crossmap.tsv SubGroup)
                  └─ FacilityID                     (8  Field)
                     └─ Facility ID                 (9  Type — from the objects export)
                        └─ foreign_key → Facility   (10 Family/binding — cross-link to level 4)
                           └─ sTYPE_FACILITY · Required No · ReadOnly No · Global
                              · Observed, docs/admin/009
                                                    (11 Constraint/evidence)
```

Note that levels 9 and 11 draw the *same* field from two independently captured sources — the
objects export types it `Facility ID`, the Data Fields catalog types it `sTYPE_FACILITY` — which is
exactly the corroboration [009](../admin/009-related-fields-and-data-model.md) §3 relies on.
Whether `contract_admin` is the physical table holding `FacilityID` is **not** established: the
export names four tables for `Contract` but does not say which column lives in which.

Two structural notes for whoever builds the artifact:

1. **Level 10 makes it a graph, not a tree.** 701 distinct object→object edges connect level-10
   nodes back to level-4 nodes. The mind map should render these as cross-links, not duplicate
   subtrees, or `Member` and `ProjectEntity` will each appear 161 times.
2. **Levels 6–7 are optional.** When an object has no Data Fields catalog entry, collapse straight
   from level 5 to level 8 rather than inventing a group. Do not fabricate a "General" bucket — the
   absence is itself information (see [`../data-model/object-catalog.md`](../data-model/object-catalog.md)
   open question 3).

### Node counts per level (for sizing the artifact)

| Level | Nodes if fully expanded (in scope) |
|---:|---:|
| 1–3 | ~100 |
| 4 | 196 |
| 5 | 196 |
| 6–7 | ~330 |
| 8 | 6,875 |
| 9–10 | ~610 (shared, not per-field) |
| 11 | ~6,875 evidence nodes + key-role nodes |

Levels 9–11 must be **shared/deduplicated nodes**, not per-field children, or the tree exceeds
20,000 nodes. Rendering level 8 lazily (expand-on-demand per entity) keeps the initial tree under
850 nodes.

## 5. Files

| File | Contents |
|---|---|
| [`build_graph.py`](build_graph.py) | The parser. Re-runnable: `python3 docs/mindmap/build_graph.py`. Asserts declared field count == parsed field count, and that the module taxonomy covers all 223 objects exactly once. |
| [`objects.json`](objects.json) | 223 records: name, `pg_table`(s), field counts, every field with parsed name/type/type-family, primary + secondary modules, `pe_scope`, in/out degree. |
| [`edges.json`](edges.json) | 972 records, one per FK-typed column: source object/column, declared type, target phrase, resolved target, `target_kind`, `resolution`, `rationale`, self-reference flag, source/target module. |
| [`modules.json`](modules.json) | 15 records: title, description, dashboard heading, object list, field count, internal/in/out edge counts, `depends_on` and `depended_on_by` maps. |

## Open questions

Ranked.

1. **Does the exclusion extend past the Budget/Bid/Cost object families?** The instruction named
   "Cost Management and Budgeting", and Lucernex's *own* Cost Management dashboard heading also
   covers `accounting` (1,265 fields), `expense-recovery` (618), `variable-rent` (472) and
   `property-tax` (163) — 2,518 fields, more than four times the excluded set. I read those as
   core lease administration and **kept them in scope**, matching the object list the instruction
   actually enumerated. Confirm before any of them is built or dropped; getting this wrong in
   either direction is expensive.
2. **`layouts-forms-reporting` has only 6 objects because the configuration model is not in this
   export.** Page layouts, data fields, drop-downs and dashboards are referenced by
   `item ID` / `Custom Drop Down ID` / `DashboardComponent ID` types that resolve to nothing.
   Since PAGE-LAYOUTS-01 and MDM-01 are live ASG Edge+ threads, that second model needs its own
   capture — this taxonomy cannot substitute for it.
3. **Is `accounting` one module or three?** At 38 objects and 1,265 fields it is the largest, and it
   contains three chains that barely touch: expense setup → schedule → accrual; payment/receipt
   ledger; landlord invoicing. Splitting is defensible; this taxonomy did not, because the FK graph
   shows 23 internal edges holding them together.
4. **Where does `ProcessTimeline` belong?** Placed in `projects-capital`, but `INDEX.md` describes
   it as attached to a `Location` *or* a `ProjectEntity` and spanning the Location and Milestones
   groups. It may be a third milestone mechanism cutting across modules rather than a member of one.
5. **Are `Complex` and `DMA` really `facilities-locations`?** Both are `firm_global` reference data
   that `ProjectEntity` points at, which by the Hub/Spoke reading of
   [`../data-model/project-entity.md`](../data-model/project-entity.md) §5 makes them Hub objects —
   arguably `platform-tenancy`. Placed by domain meaning, not by scope.
6. **Should `variable-rent`'s 7 `Virtual*` projections be entities in the mind map at all?** They
   are calculation output, not schema. Rendering them as siblings of `Sales` and `PercentageRent`
   may mislead. An alternative is a distinct visual treatment for the `computed projection`
   sub-module.
