---
title: "Q-BBW-17 — Is AI lease abstraction in scope for ASG Edge+?"
tags: [open-question, integration, scope, business]
evidence: Observed
status: open
---

**A business question, not a technical one — and nobody has been asked, because nothing in the corpus
showed the pipeline existed.**

[[atlas-ai-abstraction|A live Atlas integration]] runs in [[tenant-bbw|BBW]]: 16 REST operations, with
**per-firm configurable field mapping**. And [[finding-tenants-differ-by-one-feature|BBW's entire
layout advantage over AF serves it]].

**No BRD reviewed so far mentions it.**

### What hangs on the answer

Roughly seven layouts (`ASG Lease Abstract - *`), a status value (`AI Abstracted`), a [[Firm]]
entitlement flag, two `Implementation Workflow` templates, and a third-party integration — **in or
out**.

It also bears directly on **BRD-24**. The corpus records that the Lease Admin Request workflow's step
2 is *"Abstract Lease Document"*, and [[finding-maker-checker-pairs|two Implementation Workflows]]
cover document and financial abstraction. **A production AI pipeline sits underneath that workflow, so
the BRD's abstraction path is not purely human.**

### How to settle it

Raise it. The answer determines whether the rebuild reproduces the integration, replaces it, or drops
it.
