---
title: "Method: read-only exploration, and what it costs"
tags: [method, meta]
evidence: Observed
---

Both tenants were explored **strictly read-only**. No record, layout, drop-down, workflow or rule was
created, edited, saved or deleted; no `Save` button was clicked; every probe was a `GET`.

That discipline is why several questions in [[map-of-open-questions]] are *open rather than answered*,
and it is worth naming which ones, because they are not gaps in the method — they are the price of it:

| Open question | Why read-only blocks it |
|---|---|
| [[q-bbw-03-task-step]] | Observing a Task step's behaviour requires **creating** one |
| [[q-bbw-15-import-results]] | Determining whether a partial write is transactional requires **a write** |
| [[q-bbw-11-virtual-layout-writable]] | Answerable by inspection, but proving it requires an attempted save |

Two more limits, stated plainly rather than worked around:

- **`Export Schema` would yield the complete physical schema in one file.** It is a download and needs
  explicit approval. It has not been run.
- **Nothing in [[tenant-bbw|BBW]] comes from a vendor schema export** — there is no BBW equivalent of
  `_lucernex_objects_summary.txt` — so **no field-level or table-level claim is made for that tenant**.

The capture itself ran in two passes: the first ended when two MCP instances contended for one Chrome
profile; the second recovered the session from the persisted browser profile.

See [[method-omitting-identities]] · [[tenant-bbw]]
