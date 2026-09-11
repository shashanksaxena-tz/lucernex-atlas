# Reading the two field inventories — neither is the schema

**Stated up front.** This corpus draws on two independent field inventories, and **they disagree,
in both directions, by a lot**. Neither is the physical database schema. Any count taken from one
alone can be wrong, and several conclusions elsewhere in this corpus were reached by trusting one
without checking the other.

| Source | Fields | What it is |
|---|---:|---|
| `_lucernex_objects_summary.txt` — "the census" | **7,421** | The object/field export the FK graph is built from |
| `docs/data-fields/all-fields.csv` — "the catalog" | **6,158** | Everything the Manage Data Fields admin screen exposes |
| View Object Model, `All` filter | **7,047** | The vendor's own per-table field report |

Three tools, three totals, none reconciled.

## The divergence runs both ways

| Object | Census | Catalog | |
|---|---:|---:|---|
| `PotentialProject` | 108 | **0** | census has everything, catalog nothing |
| `BudgetOptionTemplate` | 107 | 0 | |
| `Issue` | 56 | 4 | |
| `Prototype` | 113 | 15 | |
| `Contract` | 570 | 402 | |
| **`Region`** | **1** | **8** | **catalog has more** |
| **`Asset`** | **122** | **126** | **catalog has more** |
| `CommitteePackage` | 1 | 1 | *different* single fields — `ProjectEntityID` vs `CommitteePackageID` |
| `DocumentMarkup` | 1 | 0 | both nearly empty |

**Twelve objects have 20 or more census fields and zero catalog rows**, including
`PaymentTransactionFullImport` (118), `PotentialProject` (108), `NonMember` (37), `TaskGroup` (37)
and `TaskItem` (37).

## A correction

An earlier version of this document claimed the census was "the configurable-field surface, roughly
what Manage Data Fields exposes", and explained the 18 objects that declare only `ProjectEntityID`
as ProjectEntity subtypes that genuinely add no columns.

**That explanation was wrong**, and `Region` disproves it. The census shows `Region` with one field.
The catalog shows **eight**:

| Field | Type | Label |
|---|---|---|
| `RegionName` | Text | Region Name |
| `Description` | Text | Region Description |
| `ParentRegionID` | **Region** | Parent Region |
| `PreviousRegionID` | Region | Previous Region |
| `ManagerIDList` | **Member** | Region Manager Names |
| `MemberIDList` | Member | Region Member Names |
| `ProgramID` | **Program** | Region Program |
| `OperatingStatus` | Operating Status | Operating Status |

So a one-field object in the census means **the census is missing columns for that object**, not
that the object has none. The right rule is the plain one: *check both sources before concluding
anything about an object's shape.*

### What `Region` actually is — answered

The eight fields settle a question three separate documents left open:

- **`ParentRegionID` is self-referencing** — regions nest. That is the `REGION1` / `REGION2`
  hierarchy in `AssigneeType` ([`graphql-api.md`](graphql-api.md)), held on Region itself.
- **`ManagerIDList` is a Member list** — this is how a region resolves to actual people for workflow
  routing, alongside the `LinkRegionManager` join table.
- **`ProgramID` ties a region to a Portfolio**, consistent with the portfolio owning the org
  structure.

`docs/modules/people-parties/` inferred that routing resolves through
`ProjectEntity.RegionID / RootRegionID / SubRegionID` plus `LinkRegionManager`. That stands, and
this adds the missing half: Region carries its own parent pointer and its own manager list.

## What survives the correction

Two conclusions from the earlier version still hold, on other evidence:

1. **`CommitteePackage` exists and backs "Binders."** Both inventories list it, and
   `CommitteeDocuments/PECommPkg.jsp` is its route from every entity root. The claim elsewhere that
   *no object backs Binders* is wrong regardless of which inventory you read. Note the two
   inventories name *different* single fields for it, so neither shows the real table.
2. **The foreign-key graph is a lower bound**, for a reason unaffected by the above — see below.

## The foreign-key graph is incomplete, and by roughly how much

`ServiceRequest` and `WorkOrder` are `Issue` variants, but the census declares their `IssueID` as
untyped `Text`, so the mechanical parse that built `edges.json` never saw the edge.

Sweeping for that signature — a column named `*ID` with declared type `Text` rather than an
`<Entity> ID` FK type — finds **153 columns** (excluding `BOMapClientRecordID`, a migration key
rather than a join). **Derived.**

| Object | Untyped `*ID` columns |
|---|---:|
| `Contract` | 8 |
| `BudgetOptionTemplate` | 6 *(out of scope)* |
| `ProjectEntity` | 6 |
| `Facility`, `Location`, `Parcel`, `PotentialProject`, `Program`, `Project`, `Prototype` | 5 each |
| `BidPackage`, `BidPackageBreakoutValue` | 3 each |

Against **972** resolved edges that is up to **14% more relationships** than the graph holds.

- The atlas's FK graph and every impact-radius claim derived from it are **lower bounds**.
- **It is never an over-count.** Nothing in the graph is spurious; the risk is entirely in omission.
- **`Contract` carries 8**, which matters most — it is the schema-freeze blocker.

## Trust table

| Use | Census | Catalog |
|---|---|---|
| Which business objects exist | **High** | Partial — 12 objects absent entirely |
| Field names and declared FK types | **High** where present | **High** where present |
| Field *counts* | **Low** | **Low** |
| An object's full shape | **No** | **No** — check both, then the View Object Model |
| Join tables' real keys | **No** | **No** |

## The authoritative tool

`/en/admin/ShowObjectDetails.jsp` (**View Object Model**) beats both where precision matters:

- `?sqlTableID=<id>` — one table with **Required?**, **Type**, **UI Label**, **Version Added**,
  **Maximum Size**, the vendor's own **Definition** prose, and **Functional Field?**
- `&limitFieldFilter=All|Editable|Math|NonMathComputed` — the vendor's computed-versus-editable
  classification, used in [`../modules/contracts/cam-waterfall.md`](../modules/contracts/cam-waterfall.md)
- `&showVersion=` / `&modifiedVersion=` — **which release added or changed each field**, across
  ~75 releases from `7.2` to `26.08.0`

That last is unexploited and would date every field in the product.

## Open questions

1. **Reconcile 7,421 / 6,158 / 7,047.** What inclusion rule differs between the three?
2. **Why do 12 objects have census fields but no catalog rows?** `PotentialProject` with 108 and 0 is
   the starkest. A plausible reading is that these are not layout-placeable, but that is **Inferred**.
3. **`CommitteePackageTemplate`** is in the View Object Model picker and absent from the census
   entirely. How many other objects are?
4. **Re-derive join tables' real keys** and rebuild `edges.json` from the View Object Model rather
   than the census.
5. **Which of the 153 untyped `*ID` columns are genuine joins?** Some will be external reference
   numbers that merely look like keys.
