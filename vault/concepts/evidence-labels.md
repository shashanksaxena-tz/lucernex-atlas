---
title: Observed, Derived, Inferred
tags: [concept, method, meta]
---

Every claim in this vault and in [`docs/`](../../docs/CONVENTIONS.md) carries one of three labels.
They are load-bearing, not decoration — this corpus is the input to a rebuild, and a wrong "fact" here
becomes a wrong line of code later.

| Label | Means |
|---|---|
| **Observed** | Seen directly in the UI or in a data export. Cite the route, screenshot path, or source file. |
| **Derived** | Computed from observed data — counting rows in a capture, joining two captures. |
| **Inferred** | Domain reasoning, naming convention, or analogy. **Not confirmed.** |

Two rules that come with them:

- **Never restate an inference as a fact downstream.** If note B cites note A, it inherits A's label.
- **Where a question could not be answered, it becomes an [[map-of-open-questions|open question]]
  rather than a guess.** Open questions are output, not failure.

The discipline has already earned itself several times. Four confident readings in this project were
retracted, and every one of them was Inferred material that had been quietly promoted —
[[finding-no-where-used-precedent]], [[layout-chain]], the census gap count, and the conditional-field
false negative. The pattern behind all four is catalogued at [[method-cheap-signals]].

In this vault, a note whose claims sit at several confidence levels carries the **weakest** label in
frontmatter and labels each claim in the body.
