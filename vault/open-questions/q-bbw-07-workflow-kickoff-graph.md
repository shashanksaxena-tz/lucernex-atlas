---
title: "Q-BBW-07 — What is the full workflow kickoff graph?"
tags: [open-question, workflow]
evidence: Observed
status: open
---

**Workflows chain.** `Implementation Workflow - Document Abstraction` (2401) reports
`Process kicked off by:` = *"(work flow specified as kickoff action in another work flow)"*.

**The corpus did not record that workflows can trigger each other at all.** It matters because it
changes the unit of analysis: a "workflow" in production may be a graph of templates, not one template,
and a rebuild that migrates templates individually loses the chain.

There are **four** kickoff methods, not the three the vendor's own help text names:
`STEP_ACTION`, `PAGE_LAYOUT`, `STATUS_CHANGE`, `TASK` ([[rule-WF-R-014]]). `STATUS_CHANGE` is the
omitted one.

### How to settle it

Cheap — a single sweep. Read `KickOffDescription` and the kickoff action on each of the 13 templates
via `WorkFlowTemplateEdit.jsp?formSubmit=viewBO`, which is a read-only `GET`.

See [[workflow-template]] · [[feature-workflows-forms]]
