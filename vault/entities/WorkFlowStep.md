---
title: WorkFlowStep
tags: [entity, workflow]
evidence: Observed
---

**`work_flow_step` · 47 fields · [[module-workflow]]**

The runtime instance of one [[workflow-step|step]], with computed alert, warn and due dates.

**20 configuration fields are copied from [[WorkFlowTemplateStep]] at instantiation**
([[rule-WF-R-024]]) — and the other 35 template fields are **read live**, so editing a template
changes workflows already running ([[rule-WF-R-013]]). That hybrid snapshot/live-read split is the
module's stated hazard.

`CodeLastActionStatusID` is **the engine's only field-write capability** ([[rule-WF-R-055]]). A
workflow cannot set any other field on any record.

It has a staging twin, `WFStepFullImport` (47 fields) — one of only two such twins in the schema.
