# ASG Edge+ mapping

**Stated up front.** ASG Edge+ has **nothing** in this space yet — no `Program`/`Portfolio`,
`PotentialProject`, `RETransaction`, or `Scenario` class exists anywhere in
`ASG-Edgeplus-Configuration-Service`, `ASG-EdgePlus-Platform`, or the legacy monorepo (checked
directly, 2026-09-11: no source match for any of those class names outside `node_modules` noise).
This is greenfield, and this module surfaces one concrete Hub/Spoke consequence the other modules'
mapping documents did not: **`Program` is not just a container to place in the Spoke — it is where
the tenant's accounting policy, fiscal calendar, and per-subtype page-layout registry all live at
once**, which means whichever service owns "Portfolio" in ASG Edge+ inherits configuration surface
that today is split across three different BRDs' worth of concerns (accounting, layouts, real
estate).

## 1. What exists today

| ASG Edge+ artefact | What it says | Gap |
|---|---|---|
| Workspace index (`ASG/Code/CLAUDE.md`) target architecture | Puts Portfolios in the Spoke, alongside Contracts and everything beneath a Contract | Silent on whether the Portfolio's *configuration* fields (discount rate, fiscal year end, layout overrides) travel with it or live separately |
| `ASG-Edgeplus-Configuration-Service` OPEN-DECISIONS.md | Names Masters, Page Layouts; does not mention Portfolio, Program, or a deal pipeline anywhere | No entity, no decision record, no open question touching this module exists yet |
| `docs/data-model/project-entity.md` §5.1 | Classifies `Program` as `subtype_root`, Spoke-side, alongside `Contract` | Consistent with the workspace index — no conflict here, unlike `Location` |

Unlike [`../facilities-locations/`](../facilities-locations/), this module raises **no** Hub/Spoke
placement conflict — `Program` and `PotentialProject` are cleanly Spoke-side by every reading in
this corpus. What it raises instead is a **scope** question: how much of `Program`'s 180 fields is
"Portfolio" versus "accounting configuration" versus "layout configuration," and whether ASG Edge+
should keep that bundling or split it.

## 2. Should ASG Edge+ keep Lucernex's bundling of policy onto the Portfolio record?

**Recommendation: no — split it, but keep the resolution chain.** Lucernex bundles three
independent concerns onto one 180-field table:

1. **Portfolio identity and rollups** — name, description, region, counts of child entities.
2. **Accounting policy** — discount rate, ASC 842 thresholds, amortisation bases, FX rate types,
   fiscal year end. This is genuinely a different bounded context
   ([`../accounting/asg-edgeplus-mapping.md`](../accounting/asg-edgeplus-mapping.md) already argues
   for a **Rule Administration UI** with versioned, effective-dated, four-eyes-approved parameters —
   the opposite of bare unversioned columns on a Portfolio row).
3. **Layout configuration** — 17 `*SetupPageLayoutID`/`*MapSetupLayoutID` columns, which is
   PAGE-LAYOUTS-01's problem space, not Portfolio's.

Lucernex's single-table design is a **legacy convenience**, not a pattern worth reproducing: a
schema change to how layouts are registered (PAGE-LAYOUTS-01) should not require touching the same
table a schema change to accounting policy touches (the accounting engine). ASG Edge+ should keep
the *resolution semantics* — Contract → Portfolio → Firm for accounting policy; tenant-wide default
overridable per-Portfolio for layouts — while storing each concern in the service/aggregate that
actually owns it. This is a genuine "should deliberately differ," not a gap to fill by copying.

## 3. The site-pipeline question is an open decision, not a build task

[`site-pipeline.md`](site-pipeline.md) could not confirm the mechanism connecting
`PotentialProject` → `Project` → `Facility`. Before ASG Edge+ builds any of `PotentialProject`
("Site"), `RETransaction`, or `Scenario`, **someone needs to decide what "promotion" means as a
domain event** — a new aggregate created and the old one archived, a state transition on one
long-lived aggregate, or a manual re-entry workflow with no system-enforced link at all. Lucernex's
own schema does not answer this (§2 of `site-pipeline.md`), so ASG Edge+ cannot infer it either; it
has to be designed fresh, informed by — but not copied from — Lucernex's apparent choice to leave no
FK trail.

## 4. What must be built, if this module is in scope

| Lucernex object | ASG Edge+ status | Priority reasoning |
|---|---|---|
| `Program` (Portfolio) | Must build | Every other Spoke-side subtype root in every other module resolves its tenant-policy defaults through it (`POR-R-001`). Build before `Facility`/`Location`/`Contract` if the accounting engine's Contract → Portfolio → Firm resolution chain is to work at all. |
| `PotentialProject` ("Site") | Build only once §3's promotion-mechanism decision is made | Building it without deciding the promotion contract risks reproducing Lucernex's own dead end — a Site with no way to trace what it became. |
| `RETransaction`, `Scenario` | Build alongside `PotentialProject` | Neither is independently useful; they exist to evaluate a Site. Keep the one real asymmetry (`Scenario.ContractID` forward-only, `POR-R-004`) rather than adding a reverse link Lucernex itself never built — or deliberately improve on it, as a scoped decision, not an oversight. |
| `DevelopmentPlan`/`DevelopmentSlot`/`ProgramRevenueWeeks` | Can defer | Rollout capacity planning, not required for a single-site deal to progress; also not connected to the deal pipeline by any FK in Lucernex (`POR-R-007`) — its own value is unclear without confirming real usage. |
| `ComparisonReport`/`ComparisonItem` | Can defer | Reporting convenience over Scenarios; no other record depends on it existing. |
| `LinkReTransScenContact`, `ReTransScenContact` | Build alongside `RETransaction`/`Scenario` if broker/attorney contact tracking is in scope | Low structural risk, standard child-record shape. |

## 5. What should deliberately differ

- **Do not bundle accounting policy and layout configuration onto the Portfolio aggregate** (§2).
  Keep the Contract → Portfolio → Firm *resolution semantics*; move the *storage* to the owning
  service.
- **Decide the site-promotion mechanism explicitly before building `PotentialProject`** (§3), rather
  than discovering — as this corpus did — that the legacy system never left evidence of its own
  mechanism.
- **If ASG Edge+ builds the deal pipeline, consider adding the reverse link Lucernex never built** —
  `Contract` → `Scenario`/`RETransaction` — so a signed lease can be traced back to the deal that
  produced it. This is a genuine improvement opportunity, not a parity requirement.
- **Do not build three separate "deal type" code tables (`POR-R-005`) without confirming they are
  used distinctly.** Lucernex's schema carries `Deal Type Code`, `Scenario Type Code`, and
  `Scenario Deal Type Code` as separate tables attached to different objects, but their row values
  were never captured — collapsing them prematurely risks losing a real distinction; keeping all
  three without evidence risks building unused complexity. Confirm with ASG's business stakeholders
  before either committing.

## 6. Decisions blocking a build

1. **What does "Site promoted to Project/Facility" mean as a domain event?** (§3) Blocks
   `PotentialProject` entirely.
2. **Should Portfolio-level accounting/layout policy be split out of the Portfolio aggregate, or
   kept bundled for schema-migration simplicity?** (§2) Blocks `Program`'s field-level design.
3. **Are all three deal-type code tables actually distinct in ASG's business process, or is one or
   more vestigial?** Business question, not resolvable from this corpus.
4. **Does any approved BRD require the rollout-capacity-planning family
   (`DevelopmentPlan`/`DevelopmentSlot`/`ProgramRevenueWeeks`) at all?** Not checked in this pass.

## Open questions

Carried forward from [`README.md`](README.md#open-questions) and [`site-pipeline.md`](site-pipeline.md#open-questions).
