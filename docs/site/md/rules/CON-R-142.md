# CON-R-142 — 12. Contract status and lifecycle

*Contracts & Leases · Derived*

**A contract advances through its process: ProcessTimelineTemplate forms a linked list of phase-bound milestone templates, instantiated per entity as ProcessTimeline rows with their own status/percent-complete/date-triple fields — the real state machine underneath the derived display text.**

A contract advances through its process: ProcessTimelineTemplate forms a linked list of phase-bound milestone templates, instantiated per entity as ProcessTimeline rows with their own status/percent-complete/date-triple fields — the real state machine underneath the derived display text.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | A contract advances through its process |
| Stated as | `ProcessTimelineTemplate.CodeProjectPhaseID`, `.InProcessPhaseStatus`, `.CompletedPhaseStatus`, `.PreviousProcessTimelineID`; `ProcessTimeline.CodeTaskStatusID`, `.PercentComplete`, Original/Projected/Actual date triples |
| Stated as | A linked list of phase-bound milestone templates, instantiated per entity, each declaring the status text for its in-progress and completed states. This is the real state machine |
| Stated as | `CurrentPhaseStatus`, `CurrentMilestone`, `NextMilestone`, `PreviousMilestone` (all `Text`, derived display) |
| Stated as | Observed fields; Derived mechanism |

## What it constrains

[ProcessTimelineTemplate](../entities/ProcessTimelineTemplate.md), [ProcessTimeline](../entities/ProcessTimeline.md)

Columns named: `ProcessTimelineTemplate.CodeProjectPhaseID`, `ProcessTimeline.CodeTaskStatusID`

---

Source: `docs/modules/contracts/rules.md`
