# ASG Edge+ mapping

**Stated up front.** ASG Edge+ has **nothing** in this space yet — no `Task`, `Schedule`, `Issue`,
or Gantt/CPM-adjacent class exists anywhere in `ASG-Edgeplus-Configuration-Service`,
`ASG-EdgePlus-Platform`, or the legacy monorepo (checked directly, 2026-09-11; the only matches are
unrelated build-tooling and skill-documentation files, not domain code). This is greenfield, and
this module's central finding changes the shape of the build: **the schema strongly suggests one
physical schedule-row concept (`TaskGroup`) is reused, unmodified, by three completely different
callers** — capital-project delivery, real-estate deal steps, and workflow kickoff triggers. A
rebuild gets real leverage only if it makes that reuse deliberate rather than accidental.

## 1. What exists today

| ASG Edge+ artefact | What it says | Gap |
|---|---|---|
| Workspace index (`ASG/Code/CLAUDE.md`) target architecture | Silent on scheduling/task management entirely — not named as Hub or Spoke | No placement decision has been made either way |
| `docs/data-model/project-entity.md` §2 | Classifies none of this module's 23 objects as `subtype_root` — they are all `entity_scoped` or `firm_global` | Consistent: this module has no aggregate root of its own; it is a capability every `ProjectEntity` consumes |

Unlike `portfolio-transactions` or `facilities-locations`, this module raises **no** Hub/Spoke
placement conflict — it has no subtype root to place. The open question is architectural in a
different sense: **should ASG Edge+ build one shared scheduling capability, or let each consuming
module (Contracts, Capital Projects, Workflow) build its own?**

## 2. The reuse argument, made concrete

Three unrelated callers in Lucernex's schema all resolve the ambiguous `Task/Group ID` FK type to
the same table (`PRJ-R-001`, [`scheduling.md`](scheduling.md)):

- `RETransaction`/`Scenario` (`portfolio-transactions`) — a real-estate deal's step schedule.
- `WorkFlow`/`WorkFlowStep` (`workflow`) — a workflow's kickoff trigger and per-step task.
- This module's own `TaskTemplate`/`TaskTemplateAudit` — capital-project delivery schedules.

**Recommendation: build one scheduling capability — tasks, predecessors, calendars — as a shared
service or shared domain module (per the workspace `CLAUDE.md`'s own test: "would changing this
force two services to deploy together?" — if the answer for a scheduling primitive is no, it can be
a shared library; if the schedule needs to be queried/joined across service boundaries routinely, it
argues for a dedicated Scheduling service that Contracts, Capital Projects, and Workflow all call).**
Do **not** let each of those three modules invent its own task/date/predecessor model — that is
exactly the trap [`code-table-registry.md`](../../data-model/code-table-registry.md) already warned
about for request-shaped features ("Lease Admin Requests, Rent Payment approvals, invoice disputes
and bid questions" all needing separate workflow engines if built independently). Scheduling is the
same shape of risk.

## 3. What must be built

| Lucernex object | ASG Edge+ status | Priority reasoning |
|---|---|---|
| `TaskGroup` (as the single real schedule-row concept — see §2 and `PRJ-R-001`) | Must build first | Everything else in this module, plus `portfolio-transactions`'s deal-step scheduling and `workflow`'s task-triggered kickoffs, depends on it existing. Do not build `Task`/`TaskItem` as separate aggregates without first confirming (via a live Lucernex query, if ever available) whether they are truly distinct. |
| `TaskPredecessor` | Must build alongside | The dependency network is what makes a schedule a CPM schedule rather than a flat list; without it there is no critical path, no "push this date and see what moves." |
| `HolidaySchedule` / `HolidayDate` | Must build alongside | Working-day calculation is meaningless without a calendar; needed the moment duration math is real. |
| `ProcessTimeline` / `ProcessTimelineTemplate` | Should build, as a genuinely separate capability | Do not conflate with the task schedule — it is deliberately simpler (no hierarchy, no dependency graph) and serves a different need: coarse milestone tracking on *any* entity, including ones with no capital-project schedule at all. |
| `Issue` (this module's non-form uses: RFI, change-order thread, parts request) | Must build if `layouts-and-forms`' "Issue" model is adopted | Should be the *same* `Issue`/ticket aggregate that module already recommends for Forms — not a second one. |
| `ChangeOrder` | Should build alongside capital-project delivery | Straightforward child record once `Issue` and the (out-of-scope) Purchase Order/budget subsystem exist. |
| `LinkTaskByCodeMember` / `LinkTaskMember` | Should build alongside `TaskGroup` | Two assignment mechanisms (by role, by named person) mirror the `AssigneeType` enum (`JOB_TITLE` vs. specific member) already established for workflow routing — reuse that same routing vocabulary rather than inventing a parallel one for tasks. |
| `LinkIssuePart` / `LinkIssuePartOrder` | Can defer | Depends on the (out-of-scope) parts/asset-maintenance subsystem being in scope at all. |
| `CodeProblem`, `CodeResponsibleParty` | Can defer | No confirmed attachment point in the corpus (`PRJ-R-014`); build only if a live capture confirms they are used. |

## 4. What should deliberately differ

- **Do not build three schedule-row tables where Lucernex's evidence suggests one.** If ASG Edge+
  needs a genuine distinction between "a task" and "a task acting as a phase header," model it as a
  discriminator field (Lucernex's own `IsTaskGroup` shows the platform already had this exact field
  available and arguably should have used it instead of exporting three table names) — not three
  aggregates with drift risk between them.
- **Do not merge the WBS hierarchy and the CPM dependency network into one relationship.** Lucernex
  keeps `ParentTaskID` and `TaskPredecessor` genuinely separate; a rebuild that tries to derive one
  from the other will break the ordinary case where a task's schedule predecessor sits in a
  different WBS branch than its parent.
- **Enforce acyclicity on the predecessor graph at the database or application layer, explicitly.**
  Lucernex's schema gives no evidence this is enforced anywhere (`scheduling.md` open question 2) —
  an unconstrained predecessor graph is a genuine correctness risk (`CPM` computation on a cyclic
  graph does not terminate) and should not be inherited silently.
- **Reuse the same `Issue`/ticket model this schedule feeds RFIs and change orders into** as the one
  `layouts-and-forms` recommends for Forms — Lucernex already runs both through the same table
  (`code-table-registry.md`); a rebuild that splits them loses that leverage for nothing.

## 5. Decisions blocking a build

1. **Is `TaskGroup` one shared Scheduling capability that Contracts, Capital Projects, and Workflow
   all call, or does each module get its own?** (§2) This is the single highest-leverage
   architectural decision in this module and should be made before any of the three consuming
   modules starts building task/schedule fields of its own.
2. **Are `Task`/`TaskGroup`/`TaskItem` genuinely three tables in Lucernex, or one?** Affects how
   confidently the "build one aggregate" recommendation can be stated; currently a strong inference,
   not a certainty.
3. **Does ASG Edge+ need the `ProcessTimeline` milestone layer as a separate capability from the
   task schedule**, or is a coarser view over the same `TaskGroup` data sufficient? A scoping
   question, not a technical blocker.

## Open questions

Carried forward from [`README.md`](README.md#open-questions) and
[`scheduling.md`](scheduling.md#open-questions).
