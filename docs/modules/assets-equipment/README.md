# Assets, Equipment & Maintenance — module overview

**Stated up front.** This module is three unrelated concerns sharing one dashboard heading
(**Portfolio Administration**): **8 objects, 230 fields.** `Asset` (122 fields, `entity_scoped`) is
the fixed-asset/equipment record and by far the largest object here — and it is **not** a passive
piece of equipment that a lease merely references. It carries its own copy of the ASC 842/IFRS 16
classification-test surface (`FairValueOfAsset`, `DiscountRateOverride`,
`IsAssetTooSpecializedForLessor`, `IsLowAssetValue`, `IsShortTerm`, `HasBuyoutOption`,
`PlanToBuyAtEndOfTerm`, `DoesTitleRevertToTenant`, `InitialAssetBalanceAdjust`,
`InitialLiabilityBalanceAdjust`, `ImpairmentOverride`, `Residual`, `YearsOfDepreciableLife`), and
`ContractFinancialTest`, `SLSummary` and `SLPeriod` — the same tables the accounting module built
around `Contract` — each carry a separate, nullable, direct FK back to `Asset`. **The accounting
engine runs per equipment asset, not only per lease.** Full argument:
[`equipment-leases.md`](equipment-leases.md).

The second concern is the **reactive-maintenance loop**: `ServiceRequest` and `WorkOrder`, a
two-step ticket chain, each step generated from the one before it by a button press
(`Generate Service Request` on `Asset`, `Generate Work Order` on `ServiceRequest`), and — a
non-obvious finding — **each step is itself an `Issue` variant**, exactly like `InvoiceIssue`/
`BidderIssue` elsewhere in the schema, just without the matching name. The schema export itself
declares that link as an untyped `Text` column, so the mechanical FK graph
([`../../mindmap/edges.json`](../../mindmap/edges.json)) misses the relationship entirely; only the
independently-captured admin Data Fields catalog reveals it. See
[`data-model.md`](data-model.md#3-the-maintenance-loop--servicerequest--workorder-and-how-both-relate-to-issue).

The third concern is the **parts catalog** (`Part`, `PartPackage`, `PartPackageItem`) — a firm-wide,
single-location inventory list with no relationship to `ServiceRequest` or `WorkOrder` at all. Actual
parts *consumption* against a maintenance job is tracked one module over, in `projects-capital`,
against the underlying `Issue` (`LinkIssuePart`/`LinkIssuePartOrder`), not against the `WorkOrder`
object.

*Evidence class for this paragraph: **Observed** field lists and FK types from
`_lucernex_objects_summary.txt`, [`../../mindmap/edges.json`](../../mindmap/edges.json), and the
per-entity catalogs in [`../../data-fields/`](../../data-fields/); the accounting-engine connection
and the Issue-variant finding are **Derived** from comparing those sources side by side — see
[`data-model.md`](data-model.md) for the full argument.*

## The module at a glance

| Property | Value |
|---|---|
| Objects | 8 |
| Fields | 230 |
| `entity_scoped` objects | 3 — `Asset`, `ServiceRequest`, `WorkOrder` |
| `firm_global` objects | 5 — `AssetHistory` *(misclassified, see below)*, `CodeAssetCategory`, `Part`, `PartPackage`, `PartPackageItem` |
| Internal FK edges (mechanically resolved) | 1 — `AssetHistory.AssetID → Asset`. Two more relationships exist (`ServiceRequest`/`WorkOrder` → `Issue`, `WorkOrder` → `ServiceRequest`) but are invisible to the mechanical graph — see [`data-model.md`](data-model.md#32-the-schema-export-and-the-admin-data-fields-catalog-disagree-about-the-fk-typing--and-it-hides-the-relationship-from-mechanical-parsing) |
| Outbound cross-module edges | 29, dominated by vendor (`Employer`) and audit (`Member`) roles on `Asset` |
| Inbound cross-module edges | 13, all into `Asset` — from `accounting` (7), `projects-capital` (3), `layouts-forms-reporting` (2), `contracts-leases` (1, `Asset.FinancialContractID`'s reverse) |
| End-user screens (from [003](../../screens/003-main-navigation.md)) | Portfolio "Equipment"; Location "Equipment", "Work Orders"; Facility "Equipment (FF&E)", "Service Requests / Work Orders" |
| Dashboard heading | Portfolio Administration |
| Live tenant volume | 605 `assets` ([`../../data-model/graphql-api.md`](../../data-model/graphql-api.md)) |

**`Asset` is labelled "Equipment" throughout the UI** (`AssetName`'s field label is *Equipment
Name*; the Facility nav group is *Equipment (FF&E)*) — the schema's object name and the product's
own vocabulary diverge consistently, and a rebuild's glossary should record the mapping rather than
force one name to win.

## Where the module attaches

`Asset` has **no hard-typed FK to `Facility`/`Location`** — its only entity-scoping column is the
generic `ProjectEntityID`, meaning it can in principle attach to any `ProjectEntity` subtype, not
only the physical-space objects the "Equipment" screens suggest. Its one hard, typed FK is
`FinancialContractID → Contract` (the equipment lease). `ServiceRequest` and `WorkOrder` are scoped
the same soft way, plus `ServiceRequest.ContractID → Contract` (optionally tying a maintenance ticket
to a specific lease). `CodeAssetCategory`, `Part`, `PartPackage` and `PartPackageItem` carry no
entity scope at all — they are tenant-wide reference/catalog data.

## The maintenance loop

```
Asset ──[Generate Service Request button]──► ServiceRequest ──[Generate Work Order button]──► WorkOrder
  │  (ProjectEntityID + FinancialContractID → Contract)     │  (Required IssueID → Issue,        │  (Required IssueID → Issue,
  │                                                          │   optional ContractID → Contract)  │   optional ServiceRequestID)
  │                                                          │                                     │
  └── ContractFinancialTest / SLSummary / SLPeriod           └── an Issue variant, undeclared      └── an Issue variant, undeclared
      each carry a nullable AssetID (see equipment-leases.md)    as a typed FK in the raw schema        as a typed FK in the raw schema

Issue (from WorkOrder.IssueID) ──► LinkIssuePart (projects-capital) ──► Part
                                    parts actually consumed against the job, tracked here, not on WorkOrder
```

Both generation steps are **user-triggered buttons**, not automatic escalation or a scheduled
sweep — matching the same pattern `../accounting/README.md` documents for `Generate Rent`/`Calculate
Schedule`. Full detail, including the schema-export-vs-admin-catalog divergence that hides the
`Issue` relationship from the mechanical FK graph:
[`data-model.md`](data-model.md#3-the-maintenance-loop--servicerequest--workorder-and-how-both-relate-to-issue).

## How equipment leases relate to the contract-side accounting engine

Answered in full in [`equipment-leases.md`](equipment-leases.md); in short: **`ContractFinancialTest`,
`SLSummary` and `SLPeriod` each carry a nullable `AssetID` alongside their `ContractID`**, so the
same lease-accounting engine `../accounting/README.md` documents for real-estate `Contract` rows can
also classify and schedule **per individual equipment asset** under one equipment `Contract`. `Asset`
supplies its own classification inputs (fair value, residual, discount-rate override, buyout/
title/specialization/low-value flags) in parallel with — and, per an unresolved open question,
possibly in conflict with — `ContractFinancialTest`'s equivalent computed fields. The one confirmed
gap: the `ASC 842 Schedule Review/Approval` workflow that gates whether a schedule counts as
published is attachable to `Portfolio` and `RE Contract` but **not** `Equipment Contract`
([`../accounting/README.md`](../accounting/README.md) finding 6) — equipment-lease schedules appear
to have no observed approval route at all.

## What a rebuild must not get wrong

1. **Do not model equipment-lease classification as a read-only reporting link from `Asset` to a
   contract-level test.** The nullable, parallel FK shape on `ContractFinancialTest`/`SLSummary`/
   `SLPeriod`, plus `Asset`'s own duplicated classification fields, both point to per-asset
   classification as a real capability, not an incidental join. `AST-R-004`.
2. **`RemainingAssetBalance` is magnitude-typed on `Asset`, exactly as on `SLSummary`.** The identical
   `sTYPE_PERCENT_OR_AMOUNT` hazard `../accounting/README.md` flags for the contract-level field
   exists a second time here. `AST-R-006`.
3. **`ServiceRequest` and `WorkOrder` are `Issue` variants**, even though neither is named
   `...Issue` and the schema export declares the link as untyped `Text`. A rebuild's own FK-parsing
   tooling would miss this exactly as `edges.json` did — verify by reading field types, not just
   declared column types. `AST-R-012`.
4. **Parts consumed against a job live on the `Issue`, not the `WorkOrder`.** Building a "parts used"
   report against `WorkOrder` directly will return nothing; the join runs through `Issue`.
   `AST-R-014`.
5. **The parts catalog has no per-location stock.** `QuantityOnHand`/`QuantityOnOrder` are single,
   firm-wide counters. A multi-warehouse rebuild needs a new table Lucernex does not have.
   `AST-R-015`.
6. **`AssetHistory`'s `firm_global` role label is a known classifier miss**, not a real finding — it
   is entity-scoped in practice via a soft-typed `ProjectEntityID`. `AST-R-016`.

## Contents

| Document | Answers |
|---|---|
| [`data-model.md`](data-model.md) | Every object, field roster, the maintenance-loop FK divergence, and the accounting-engine cross-module edges. |
| [`equipment-leases.md`](equipment-leases.md) | **The ASC 842/IFRS 16 angle** — how `Asset` plugs into the same engine `../accounting/` documents for `Contract`, and the one confirmed approval-workflow gap. |
| [`rules.md`](rules.md) | `AST-R-001`…`AST-R-016` — every rule in trigger/input/effect/confidence form. |
| [`asg-edgeplus-mapping.md`](asg-edgeplus-mapping.md) | What exists (nothing), what must be built, what should deliberately differ, and the decisions blocking a build. |

## Open questions

Ranked by how much each blocks a rebuild decision.

1. **Does one equipment `Contract` actually carry more than one `Asset`, each with its own
   `SLSummary`/`ContractFinancialTest` row, in a live tenant?** The schema permits it; nothing
   observed confirms it happens. See [`equipment-leases.md`](equipment-leases.md).
2. **Is there truly no approval workflow for equipment-lease schedules**, or was an existing one
   simply not found in this pass? Blocks whether ASG Edge+ needs a parallel approval path for
   equipment leases.
3. **Which of `Contract`/`ContractFinancialTest`'s impairment field and `Asset.ImpairmentOverride`
   wins when both are populated for the same equipment lease?**
4. **Does `WorkOrder.ServiceRequestID` being optional ever get exercised** in the live tenant — any
   standalone work orders with no parent service request?
5. **Where does a live tenant's `Part` stock actually live if it operates more than one
   warehouse/facility?** Nothing in the schema answers this; not checked against live data.
