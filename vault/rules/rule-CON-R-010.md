---
title: "CON-R-010 — Delete and regenerate, never edit in place"
tags: [rule, contracts]
evidence: Derived
---

**`CON-R-010`** · [[module-contracts]] · **Derived**

The supported correction path for generated output is **delete-then-regenerate**, not in-place
editing.

Which means a rebuild that offers editable generated rows is offering something the incumbent's users
have been trained not to expect — and something the [[finding-engine-is-button-driven|generator]]
would overwrite.

See [[rules-contracts]] for the full register.
