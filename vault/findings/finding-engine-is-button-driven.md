---
title: The accounting engine is user-triggered, not batch
tags: [finding, accounting, contracts]
evidence: Observed
---

**`Generate Rent` and `Calculate Schedule` are buttons on a record**, not scheduled jobs. So are
`Generate Payments`, `Approve Payments`, `Extend Contracts` and `Generate Service Request` /
`Generate Work Order` ([[rule-AST-R-011]]).

They are [[action-buttons|placeable, securable verbs]] — placed on a
[[page-layout-concept|layout]] like a field, and secured as one of the 70 named verbs on the Actions
tab of [[security-ladder|Manage Security]].

**Confirmed from the other side**: [[screen-job-log|Job Log]] records `Generate Payments` as a
**user-initiated** job among its 818 entries, alongside `Data Import` and `Scheduled Report`.

Two consequences worth carrying into a rebuild:

- **Nothing recalculates on its own.** [[SLSummary]] sets `NeedsRecalculation` and waits
  ([[finding-schedules-are-approved-not-published]]).
- **The supported correction path is delete-then-regenerate**, not editing generated output
  ([[rule-CON-R-010]]). Regeneration is a user action too.

A rebuild that models the engine as a nightly batch changes the operating model, whether or not it
changes the arithmetic — and the incumbent's users are trained on a button.

See [[setup-schedule-transaction]]
