# ProcessTimelineTemplate

*10 fields · module: Capital Projects & Scheduling · Postgres: `process_timeline_template`*

A reusable milestone/phase template that ProcessTimeline instances are created from, with default phase-status labels.

Source: `data-fields/small-miscellaneous-entities.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 10 |
| Catalogued fields | 10 (10 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 1 other records |
| Tenancy position | firm_global |
| Rules that name it | 2 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-142](../rules/CON-R-142.md) | A contract advances through its process: ProcessTimelineTemplate forms a linked list of phase-bound milestone templates, instantiated per entity as ProcessTimeline rows with their own status/percent-complete/date-triple fields — the real st | Derived |
| [PRJ-R-002](../rules/PRJ-R-002.md) | An entity needs milestone/phase tracking (`CurrentMilestone`/`NextMilestone`/`PreviousMilestone` on the `ProjectEntity` union block) · `ProcessTimeline` → `ProcessTimelineTemplate` · Produces a flat, non-networked milestone list — no hierar | Observed |

## Fields

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeProjectPhaseID` | Project Phase | Dropdown (Project Phase Code) | Global | yes | Project Phase Code |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ProcessTimelineTemplateID` | Milestone Template RecID | Number | Global |  |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AlwaysShowInSummary` | Always Show in Summary? | Boolean | Global | yes |  |

### Text & notes (5)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CompletedPhaseStatus` | Completed Phase Status | Text | Global | yes |  |
| `DefaultTaskName` | Default Task Name | Text | Global |  |  |
| `InProcessPhaseStatus` | In Process Phase Status | Text | Global | yes |  |
| `PreviousProcessTimelineID` | Previous Milestone Template | Text | Global |  |  |
| `ProcessTimelineTemplateName` | Milestone Template Name | Text | Global | yes |  |

### Audit & record keeping (2)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ModifiedByID` | Milestone Template Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Milestone Template Modified Date | Time | Global |  |  |
