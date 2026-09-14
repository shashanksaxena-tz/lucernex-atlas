---
title: "Q-BBW-08 — Configuration error, or deliberate form reuse?"
tags: [open-question, workflow]
evidence: Observed
status: open
---

Two things in `Lease Admin Request`'s eight steps do not line up:

- **Steps 5 and 6 share one form.** Both point at `LAR Finalize Lease Admin Request(Approvers)`, the
  second labelled `(Option)` — the same form presented twice to different approver groups.
- **Step 8, `Client Review of Estoppel`, points at a form named
  `LAR Submit Lease Admin Request(Approvers)`.** The step name and its form name **disagree**.

**Inferred:** form reuse rather than a mistake. But it is Inferred, and it **matters if these
definitions are migrated** — a migration that trusts the naming will wire step 8 to the wrong form, or
a migration that trusts the mapping will carry a mislabelled one forward.

**Form naming is a convention, not a relation.** Forms are prefixed by workflow (`LAR ` for Lease
Admin Request, `IWF ` for the Implementation Workflows) and suffixed `(Approvers)`. **Nothing enforces
it**, which is exactly why the disagreement is possible.

### How to settle it

Open both steps.

See [[finding-maker-checker-pairs]] · [[WorkFlowTemplateStep]]
