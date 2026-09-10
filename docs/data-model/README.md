# Data model — the Lucernex object graph

**Stated up front.** Lucernex/LxRetail is **223 business objects and 7,421 fields** resting on a
single universal spine: **`ProjectEntity`**. 161 of the 223 objects carry a `ProjectEntityID`
column typed `Entity ID` — a hard foreign key to `ProjectEntity`. Nine more (`Contract`,
`Facility`, `Location`, `Parcel`, `Program`, `Prototype`, `PotentialProject`, `Project`,
`BudgetOptionTemplate`) are **subtype extension tables** that inherit `ProjectEntity`'s own column
block on a shared key. Only **52** objects sit outside the spine entirely, and those are exactly
the tenant-global ones: `Firm`, `Member`, `Employer`, `Person`, the `Code*` reference lists and the
geography/currency tables. That 52 / 171 split is a ready-made **Hub / Spoke boundary** for ASG
Edge+ — see [`project-entity.md`](project-entity.md), which treats this as the central question.

The relational reading is not inferred from naming. Lucernex's field-type system has **first-class
foreign-key types named after their target table** (`Contract ID`, `Facility ID`, `Employer ID`,
`Entity ID`, …), directly visible in the vendor's own View Object Model admin tool — **Observed**,
[`../admin/009-related-fields-and-data-model.md`](../admin/009-related-fields-and-data-model.md).
This corpus's whole edge inventory is derived from that type column.

## The numbers

All figures below are produced by [`../mindmap/build_graph.py`](../mindmap/build_graph.py) from
`_lucernex_objects_summary.txt`. **Derived.** Re-run with `python3 docs/mindmap/build_graph.py`.

| Measure | Value |
|---|---:|
| Objects | 223 |
| Fields (declared, and independently re-counted from the parse) | 7,421 / 7,421 |
| Distinct field types | 315 |
| Physical PG tables named | 222 across 216 objects (7 objects name none; 2 objects name 4 each) |
| FK-typed columns | 972 |
| — resolving to one of the 223 objects | 912 |
| — unresolved (`item ID`, `Custom Drop Down ID`, `DashboardComponent ID`) | 60 |
| Self-referencing FK columns | 13 |
| Distinct object→object edges (excluding self-loops) | 701 |
| Objects with in-degree 0 | 167 |
| Modules in the taxonomy | 14 in scope + 1 excluded |
| **In-scope census** (excluding Budgeting/Bid/Cost, see below) | **196 objects / 6,875 fields** |

## Scope

**Cost Management and Budgeting are out of scope** by user decision (2026-09-10). The 27
Budget / Bid / Cost Tracking objects (546 fields) remain in the census, in `objects.json`,
`edges.json` and [`object-catalog.md`](object-catalog.md) — so the FK graph is whole and the
degrees are honest — but they are collected into a single catch-all module
`out-of-scope-cost-budget` and carry a one-line purpose only: no module write-up, no hub analysis,
no mind-map depth. Rationale and the two caveats worth checking are in
[`../mindmap/taxonomy.md`](../mindmap/taxonomy.md).

The boundary is cheap: only **13 FK columns** cross from in-scope objects into that module, 9 of
them the same `BudgetTemplateID` column repeated once per entity subtype
([`foreign-key-graph.md`](foreign-key-graph.md) §3.1).

## Documents

| File | What it answers |
|---|---|
| [`object-catalog.md`](object-catalog.md) | All 223 objects: physical table(s), field count, module, spine role, degree, one-line purpose. |
| [`foreign-key-graph.md`](foreign-key-graph.md) | The 972-column edge inventory, target resolution and confidence, the hubs, the in-degree-0 set, and the module dependency matrix. |
| [`project-entity.md`](project-entity.md) | What `ProjectEntity` actually is, why it is on almost everything, and what that means for ASG Edge+ database-per-tenant. |
| [`type-system.md`](type-system.md) | The complete 315-type vocabulary grouped into five families, with per-type field and object counts. |
| [`graphql-api.md`](graphql-api.md) | (Sibling capture, different author.) Lucernex's introspectable GraphQL schema — 490 types, 617 root query fields. A **more authoritative** source than this object export where the two overlap; the object export's advantage is that it carries the physical `PG TABLE` names and the human-readable FK type labels, which the GraphQL schema does not. Cross-checking the two is the highest-value next step. |
| [`../mindmap/taxonomy.md`](../mindmap/taxonomy.md) | The 15-module taxonomy, its evidence, and the 11-level mind-map hierarchy with a populate-check per level. |
| [`../mindmap/objects.json`](../mindmap/objects.json) / [`edges.json`](../mindmap/edges.json) / [`modules.json`](../mindmap/modules.json) | Machine-readable form of everything above. |

## Confidence

| Claim | Label | Source |
|---|---|---|
| `<Entity> ID` types are genuine typed FK columns | **Observed** | [009](../admin/009-related-fields-and-data-model.md), Lucernex View Object Model |
| Object, table, field-count and type figures | **Derived** | `build_graph.py` over `_lucernex_objects_summary.txt` |
| Which object a given FK type points at | **Derived** where the type name matches an object name; **Inferred** for the 11 aliased types — each edge in `edges.json` carries its own `resolution` and `rationale` |
| `ProjectEntity` is a supertype with subtype extension tables | **Derived** — from the column-block signature, see [`project-entity.md`](project-entity.md) |
| The `Virtual*` family are computed projections, not tables | **Derived** — no PK and no audit column on any of the 13 |
| Module boundaries | **Inferred**, anchored on Observed dashboard headings — see [`../mindmap/taxonomy.md`](../mindmap/taxonomy.md) |

## Open questions

1. What is the `item ID` type's actual target table? 56 columns carry it; 54 are named
   `*PageLayoutID` / `*LayoutID` / `*ReportGroupDataID` and the remaining two are `AuditColumn`'s
   `GroupID` / `SubGroupID` — i.e. **all 56 point at configuration metadata that lives outside
   these 223 business objects**. Confirming the physical target needs a `ShowObjectDetails.jsp`
   pass over a layout-carrying table (`Firm` carries 11 of them).
2. `walkHierarchy.jsp` lists `Site`, `Opening Project`, `Capital Program`, `Capital Project` and
   `Equipment Contract` as aggregate roots, but no object of those names exists in the export.
   The `IsValidFor*` flags on `VirtualTemplateBudget` enumerate the same 11 names. Are these
   `ProjectEntityTypeName` discriminator values over shared tables, or separate tables absent from
   this export? See [`project-entity.md`](project-entity.md) §4.
3. Only 33 of 223 objects have a populated `LucObject` in `_crossmap.tsv`; the remaining join has
   to go through `LeafTable`, which covers 195. The 28 objects with neither have no Manage Data
   Fields catalog entry at all — are they genuinely not user-configurable, or was the capture
   incomplete?
4. `Contract` names four physical tables but repeats `ContractID` only three times, while
   `ExpenseRecovery` names four and repeats `ExpenseRecoveryID` four times. Is `contract_firm1`
   keyed differently, or is this an export artefact?
5. **Does the GraphQL schema in [`graphql-api.md`](graphql-api.md) agree with this graph?** It
   reports 490 types against these 223 objects. Reconciling the two would settle several open
   questions at once — in particular `ProjectEntityTypeName`'s value set, whether `Site` /
   `Opening Project` / `Equipment Contract` are separate types, and what `item ID` points at.
