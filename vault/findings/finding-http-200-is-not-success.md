---
title: HTTP 200 does not mean the write succeeded
tags: [finding, api, core, trap]
evidence: Observed
---

> **Writes on the [[rest-business-object|generic REST controller]] return `ImportResults` — a bulk
> envelope of `successes[]` and `errors[]`. A write can return HTTP 200 while having failed
> entirely.**

The caller **must** inspect `errors[]`. Any ASG Edge+ integration that treats 2xx as success will
silently lose data.

This is not an edge case in the API design — it is the shape of the whole write surface. The same
generic controller serves all 227 record types, the request body is a recursive `BusinessObject`, and
a contract plus its children can be written in one call. Bulk semantics are the default, so bulk
result semantics come with them.

Two things that follow:

- `synchronous` is **required** on `POST /rest/firm`; `stopOnError` is optional and the UI defaults to
  *stop on first error*. **There is no dry-run parameter.**
- Bulk import **creates parent records implicitly** — importing a [[Facility]] creates its
  [[Location]].

**What is not known** is the full `ImportError` vocabulary, and **whether a partial write is
transactional or leaves a half-created aggregate**. Determining that requires a write, which was out
of scope under the read-only rule — [[q-bbw-15-import-results]].

Auth is out of band: the spec declares **no `securitySchemes`**.

See [[feature-import-export]]
