# How to read the 223-object census — and what it does not contain

**Stated up front.** `_lucernex_objects_summary.txt` is the corpus's foundation: 223 objects,
7,421 fields, and the source of the foreign-key graph. It is reliable, but it is **not the physical
schema**. It is the *configurable-field surface* — roughly, what Manage Data Fields exposes. Three
consequences follow, and at least three "gaps" recorded elsewhere in this corpus are artefacts of
not knowing this.

**The tell: 18 objects declare exactly one field, `ProjectEntityID`.**

## The 18

| Object | PG table | Reading |
|---|---|---|
| `Region` | `region` | ProjectEntity subtype |
| `CommitteePackage` | `committee_package` | ProjectEntity subtype — **this is "Binders"** |
| `DocumentMarkup` | `document_markup` | ProjectEntity subtype |
| `Notify` | `notify` | ProjectEntity subtype |
| `TaskTemplate` | `task_template` | ProjectEntity subtype |
| `LeaseAudit` | `lease_audit` | ProjectEntity subtype |
| `ScratchPad` | `scratch_pad` | ProjectEntity subtype |
| `IssueSubmittal` | `issue_submittal` | ProjectEntity subtype |
| `FolderTemplate` | `folder_template` | ProjectEntity subtype |
| `EntityTemplate` | `entity_template` | ProjectEntity subtype |
| `BudgetTemplate` | `budget_template` | ProjectEntity subtype *(out of scope)* |
| `AuditTable` | `audit_table` | ProjectEntity subtype |
| `EMailSentLog` | `e_mail_sent_log` | ProjectEntity subtype |
| `LinkBudgetIndexBLI` | `link_budget_index_b_l_i` | **join table** |
| `LinkBudgetViewBLI` | `link_budget_view_b_l_i` | **join table** |
| `LinkPEMemberCodeJobTitle` | `link_p_e_member_code_job_title` | **join table** |
| `LinkRegionManager` | `link_region_manager` | **join table** |
| `LinkTaskDocument` | `link_task_document` | **join table** |

Two distinct cases, and they must be read differently.

### Case 1 — real ProjectEntity subtypes (13 objects)

These genuinely declare nothing of their own. [`project-entity.md`](project-entity.md) establishes
that ProjectEntity is a supertype whose subtypes inherit an identity column block on a shared key.
A subtype that adds no columns of its own is therefore **complete at one field**. Confirmed
independently for `Region` via the View Object Model, which shows the same single field with the
definition *"the Base Entity System Identifier for associated tasks, folders, documents, forms, and
other records"*.

So `Region` is not an empty table. It is the pattern in its purest form.

### Case 2 — join tables (5 objects)

A table named `Link<A><B>` must carry at least two foreign keys or it cannot join anything.
`LinkRegionManager` declaring only `ProjectEntityID` is therefore **evidence of omission, not of
design**. Its `RegionID` and `MemberID` columns exist physically and are simply absent from this
export, because they are not configurable fields.

**Derived:** the census omits columns that are not exposed as Data Fields — join keys, internal
bookkeeping, and anything the platform does not let an administrator place on a layout.

## Three corrections this forces

1. **"No object backs Binders / Committee Packages."** It does: `CommitteePackage`
   (`committee_package`), reached by `CommitteeDocuments/PECommPkg.jsp` from every entity root. It
   is a ProjectEntity subtype, so the census shows one field. *(`CommitteePackageTemplate` also
   exists in the View Object Model's table list but is **absent from the census entirely** — see
   below.)*
2. **"Document markup content is not recoverable."** `DocumentMarkup` is a ProjectEntity subtype;
   its content columns are simply not configurable fields. Absence from the census is not absence
   from the database.
3. **`Region` is not a data gap.** Twelve objects reference it across 34 columns and it declares one
   field, because that is what a column-free subtype looks like.

The general rule: **a one-field object in this census is a statement about the Data Fields catalog,
never about the database.**

## The census is also incomplete by at least one object

`CommitteePackageTemplate` appears in the View Object Model's table picker but **not** in
`_lucernex_objects_summary.txt`. The picker offers 224 entries (223 tables plus "All Tables"), and
the census holds 223 — the counts coincide, so at least one object in the picker is missing from the
census and at least one in the census is absent from the picker.

**This has not been reconciled.** Until it is, treat 223 as approximately right rather than exact.

## Two field counts that do not match

| Source | Fields |
|---|---:|
| `_lucernex_objects_summary.txt` | **7,421** |
| View Object Model, All Tables, filter `All` | **7,047** |

A 374-field difference, unreconciled. **Inferred:** the two tools apply different inclusion rules —
most plausibly around code tables (the View Object Model has a separate `Show Code Tables`
checkbox) or Firm-scope fields. Both numbers are used in this corpus; where precision matters, say
which source a count came from.

## What to trust the census for

| Use | Trust |
|---|---|
| The set of business objects | **High** — cross-checked against the View Object Model picker |
| Field names, types and FK types on substantive objects | **High** — this is its purpose |
| The foreign-key graph between substantive objects | **High** — 972 edges, resolution-scored |
| Field *counts* as physical column counts | **Low** — configurable surface only |
| Join tables' actual keys | **Do not** — use the View Object Model instead |
| Presence or absence of an object's internals | **Do not** — absence means "not configurable" |

## The better tool, when precision matters

`/en/admin/ShowObjectDetails.jsp` (**View Object Model**) is authoritative where the census is not:

- `?sqlTableID=<id>` — one table's full field list with **Required?**, **Type**, **UI Label**,
  **Version Added**, **Maximum Size**, **Definition** (the vendor's own prose) and **Functional
  Field?**
- `&limitFieldFilter=All|Editable|Math|NonMathComputed` — the vendor's own computed-versus-editable
  classification, used in [`../modules/contracts/cam-waterfall.md`](../modules/contracts/cam-waterfall.md)
- `&showVersion=` / `&modifiedVersion=` — **which release added or changed each field**, across
  roughly 75 releases from `7.2` to `26.08.0`

That last one is unexploited and worth a pass: it would date every field in the product, showing
which subsystems are mature and which are recent. The ASC 842 screens already look late from their
layout-id band (see [`screen-routing.md`](screen-routing.md)); this would confirm it field by field.

## Open questions

1. **Reconcile 223 against the View Object Model's 223.** Which object is in each that is not in the
   other?
2. **Reconcile 7,421 against 7,047.** What inclusion rule differs?
3. **Re-derive the join tables' real keys** from the View Object Model, and check whether
   `edges.json` is missing edges as a result. `ServiceRequest` and `WorkOrder` are known to lose
   their `IssueID` relationship this way — the export declares it as untyped `Text`, so the
   mechanical FK parse misses it.
4. **Which of the 153 untyped relationships are real?** *(Now sized — see below.)*

## The foreign-key graph is incomplete, and by roughly how much

`ServiceRequest` and `WorkOrder` are `Issue` variants, but the census declares their `IssueID` as
untyped `Text`, so the mechanical parse that built `edges.json` misses the relationship entirely.

A sweep for the same signature — a column named `*ID` carrying declared type `Text` rather than an
`<Entity> ID` FK type — finds **153 such columns** (excluding `BOMapClientRecordID`, which is a
migration key rather than a join). **Derived.**

| Object | Untyped `*ID` columns |
|---|---:|
| `Contract` | 8 |
| `BudgetOptionTemplate` | 6 *(out of scope)* |
| `ProjectEntity` | 6 |
| `Facility`, `Location`, `Parcel`, `PotentialProject`, `Program`, `Project`, `Prototype` | 5 each |
| `BidPackage`, `BidPackageBreakoutValue` | 3 each |

Against **972** resolved edges, that is up to **14% more relationships than the graph currently
holds** — if they are all genuine joins. Some will not be: a few are probably external reference
numbers that merely look like keys.

**What this means in practice:**

- The interactive atlas's FK graph, `docs/mindmap/edges.json`, and every impact-radius claim derived
  from it are **lower bounds**. A record may point at more than the map shows.
- **It is never an over-count.** Nothing in the graph is spurious; the risk is entirely in what is
  missing.
- **`Contract` has 8 of them**, which matters most — it is the schema-freeze blocker, and eight
  potentially unmapped relationships on the most important record is a real gap to close before
  Week 12.

Resolving them needs the View Object Model per object, which carries the vendor's own `Definition`
prose for each column and would say what each actually references.
