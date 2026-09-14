# ProcessTimelineTemplate

*10 fields · module: Capital Projects & Scheduling · Postgres: `process_timeline_template`*

A reusable milestone/phase template that ProcessTimeline instances are created from, with default phase-status labels.

Source: `data-fields/small-miscellaneous-entities.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 10 |
| Fields with a vendor definition | 10 of 10 inventoried |
| Physical tables | `process_timeline_template` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 10 (10 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 1 other records |
| Tenancy position | firm_global |
| Rules that name it | 2 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### Lands in process_timeline_template

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 10 fields carry a vendor definition

**Observed.** 10 of this record's 10 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: the captures agree

**Observed.** Over the 10 fields both the Data Fields catalogue and the field inventory contain, the two agree on every one. 5 are marked required.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-142](../rules/CON-R-142.md) | A contract advances through its process: ProcessTimelineTemplate forms a linked list of phase-bound milestone templates, instantiated per entity as ProcessTimeline rows with their own status/percent-complete/date-triple fields — the real st | Derived |
| [PRJ-R-002](../rules/PRJ-R-002.md) | An entity needs milestone/phase tracking (`CurrentMilestone`/`NextMilestone`/`PreviousMilestone` on the `ProjectEntity` union block) · `ProcessTimeline` → `ProcessTimelineTemplate` · Produces a flat, non-networked milestone list — no hierar | Observed |

## Fields

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeProjectPhaseID` | Project Phase | Select the project phase that this milestone belongs to from this field. The project phase corresponds with key dates on your project. You may have multiple milestones that share the same phase. | Dropdown (Project Phase Code) | Global | yes | `process_timeline_template.CodeProjectPhaseID · TEXT` | Project Phase Code |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ProcessTimelineTemplateID` | Milestone Template RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `process_timeline_template.ProcessTimelineTemplateID · VARCHAR(64) NOT NULL` |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AlwaysShowInSummary` | Always Show in Summary? | If this milestone is a summary item, select this check box. Milestones that have this check box selected will appear in the default view of the Milestone Timeline section of your Summary page, even if the milestone has been completed. | Boolean | Global | yes | `process_timeline_template.AlwaysShowInSummary · TEXT` |  |

### Text & notes (5)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CompletedPhaseStatus` | Completed Phase Status | Enter the status the entity should have after the milestone is completed in this field. | Text | Global | yes | `process_timeline_template.CompletedPhaseStatus · TEXT` |  |
| `DefaultTaskName` | Default Task Name | Select the schedule task whose completion triggers this milestone from this field. | Text | Global |  | `process_timeline_template.DefaultTaskName · TEXT` |  |
| `InProcessPhaseStatus` | In Process Phase Status | Enter the status the entity should have prior to the milestone being completed in this field. | Text | Global | yes | `process_timeline_template.InProcessPhaseStatus · TEXT` |  |
| `PreviousProcessTimelineID` | Previous Milestone Template | The ID of the milestone that precedes this milestone. | Text | Global |  | `process_timeline_template.PreviousProcessTimelineID · TEXT` |  |
| `ProcessTimelineTemplateName` | Milestone Template Name | Enter the name of the milestone in this field. | Text | Global | yes | `process_timeline_template.ProcessTimelineTemplateName · TEXT` |  |

### Audit & record keeping (2)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ModifiedByID` | Milestone Template Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `process_timeline_template.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Milestone Template Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `process_timeline_template.ModifiedDate · TEXT` |  |
