# ASG Edge+ mapping

**Stated up front.** ASG Edge+ has **nothing** in this space yet. Neither
`ASG-Edgeplus-Configuration-Service` nor the legacy monorepo defines an `Asset`, `ServiceRequest`,
`WorkOrder`, or parts-catalog class, and the workspace index (`ASG/Code/CLAUDE.md`) does not mention
equipment or maintenance at all. This module must be designed from evidence alone, and the one
decision that most changes its shape is not a UI question but an accounting one: **does ASG Edge+
need per-asset ASC 842/IFRS 16 classification, or is contract-level classification enough for every
lease ASG actually carries?** Lucernex's schema is built for the former; a rebuild that only ever
sees real-estate leases can defer most of this module's accounting surface.

## 1. What exists today

| ASG Edge+ artefact | What it says | Gap |
|---|---|---|
| `ASG-Edgeplus-Configuration-Service` OPEN-DECISIONS.md | Lists `Asset` among masters referenced by Contract/Location/Facility/Covenant/KeyDate | No `Asset` entity, no maintenance or parts model, defined anywhere |
| `ASG-EdgePlus-Platform` domain primitives | None found for equipment, service requests, or work orders | Confirms greenfield |
| Workspace index target architecture | Silent on this module entirely | No stated Hub/Spoke placement for `Asset` to check against |

## 2. What must be built

| Lucernex object | ASG Edge+ status | Priority reasoning |
|---|---|---|
| `Asset` | Must build if ASG carries any equipment leases | It is the only object in this module that other engines (accounting, GL export) depend on. If ASG's business is real-estate-only, this can be deferred entirely — see the open question below. |
| `CodeAssetCategory` | Must build alongside `Asset` | Two independent lookups on `Asset` resolve to it (`AST-R-007`), and it carries GL routing (`AST-R-008`) — it is Masters data, sized for MDM-01, not a plain enum. |
| `ServiceRequest`, `WorkOrder` | Should build if the maintenance loop is in scope | Straightforward two-step ticket chain once `Issue`/workflow infrastructure exists (see `../../modules/workflow/`); no accounting dependency. |
| `Part`, `PartPackage`, `PartPackageItem` | Can defer | Firm-wide catalog with no per-location stock and no link to the maintenance loop in this schema (`AST-R-015`); low structural risk, build on demand. |
| Per-asset classification/schedule rows (the `Asset`-nullable FK on `ContractFinancialTest`/`SLSummary`/`SLPeriod`) | **Decision required before building** | This is not a small feature — it changes the cardinality of the accounting engine's core tables from one-per-contract to potentially many-per-contract. See §3. |

## 3. The central decision: does the accounting engine need a per-asset dimension at all?

[`equipment-leases.md`](equipment-leases.md) establishes that Lucernex's `ContractFinancialTest`,
`SLSummary` and `SLPeriod` each carry a nullable `AssetID`, meaning classification and scheduling can
run once per contract *or* once per asset under a contract. Building this into ASG Edge+'s accounting
engine from day one — even if unused — adds a real dimension to every query and every GL export path
in that engine. **Recommendation: do not build the per-asset dimension until ASG confirms it
services equipment leases with more than one asset per contract.** If every equipment lease ASG
carries covers exactly one asset, a 1:1 `Contract`↔`Asset` relationship is sufficient and the
nullable, many-per-contract shape can be deferred indefinitely without losing anything observable
today.

## 4. What should deliberately differ

- **Give `Asset`'s classification overlay one authoritative precedence rule against
  `ContractFinancialTest`'s, decided at design time.** Lucernex ships with the conflict unresolved
  (`AST-R-004`, [`equipment-leases.md`](equipment-leases.md) §2) — a rebuild should not inherit two
  competing sources of truth for the same fact.
- **Split `RemainingAssetBalance` into an explicit percentage field and an explicit currency field**,
  on both `Asset` and the accounting engine's schedule table, rather than reproducing the
  magnitude-typed `sTYPE_PERCENT_OR_AMOUNT` pattern. `AST-R-006`.
- **Decide the equipment-lease approval workflow deliberately, not by omission.** If ASG Edge+
  requires review/approval for real-estate lease schedules, an equal or explicitly lesser bar should
  be set for equipment schedules — Lucernex's own gap (§ `../accounting/README.md` finding 6) should
  not be treated as a template to copy.
- **Model `ServiceRequest`/`WorkOrder` as genuine `Issue`/workflow instances from the start**, not as
  bespoke ticket tables with a look-alike shape. Lucernex's own schema declares the link as untyped
  `Text`, which is almost certainly an implementation shortcut rather than a deliberate design —
  ASG Edge+ should type the relationship properly. `AST-R-012`.
- **If multi-warehouse parts inventory is ever needed, add a location-scoped stock table.** Lucernex
  has none (`AST-R-015`); do not assume the incumbent's single firm-wide counter is a design worth
  keeping.

## 5. Decisions blocking a build

1. **Does ASG carry any equipment lease covering more than one distinct asset?** (§3) Changes the
   accounting engine's core cardinality if yes.
2. **Is the maintenance loop (`ServiceRequest`/`WorkOrder`/`Part`) in scope for ASG Edge+ at all**, or
   is it a Lucernex capability ASG has never operationally used? Not checked against any approved
   BRD in this pass — a business question.
3. **What approval process, if any, should gate an equipment-lease schedule** before it counts as
   published, given Lucernex itself appears to have none?

## Open questions

Carried forward from the other documents in this folder, ranked by how much each blocks a build
decision.

1. Does one equipment `Contract` actually carry more than one `Asset` with independent schedules in
   a live Lucernex tenant? Directly decides §3.
2. Is there truly no approval workflow for equipment schedules in Lucernex, or was one simply not
   found?
3. Which impairment input — contract-level, test-level, or asset-level — is authoritative?
4. Does any approved BRD require the maintenance loop (`ServiceRequest`/`WorkOrder`/`Part`) at all?
5. Does ASG operate more than one warehouse/parts-stock location, which would make Lucernex's
   firm-wide parts counters insufficient to migrate as-is?
