---
title: "Tenant: (ASG)BBW"
tags: [tenant]
evidence: Observed
---

| Property | Value |
|---|---|
| Tenant | `(ASG)BBW`, `firmID=3159` |
| Build | **`26.09.0.113`** (2026/09/11) |
| Captured | 2026-09-13 |
| Mode | **Read-only.** Every probe a `GET` — [[method-read-only-exploration]] |

The second tenant, read against [[tenant-american-freight|American Freight]] to find out which
documented facts were platform behaviour and which were one tenant's configuration. **It turned out to
refute several.**

| | AF | BBW |
|---|---:|---:|
| Navigation roots / nodes | 4 / 109 | **5 / 141** |
| Page layouts (SEP/SUB/LIST) | 17/31/40 = 88 | 15/32/46 = **93** |
| [[WorkFlowTemplate\|Workflow templates]] | 4 | **13** |
| Workflow steps | 19 | **62** |
| Form types | 4 | **6** |
| Admin tools | **63** | 57 |
| [[code-table\|Firm Drop Downs]] | 207 | 207 — identical |
| Sql tables | 227 | 227 — identical |

**A substantially populated tenant**: 2,191 master contracts, 2,141 locations, 2,062 facilities, 605
assets, 11,905 documents, 151 expense types.

**It is also not idle.** [[screen-job-log|Job Log]] shows 818 entries and an **hourly inbound HTTP
integration** ([[q-bbw-19-hourly-integration]]) — which raises whether "training tenant" is the right
description at all.

### What it added

[[finding-root-renders-iff-record-exists]] · [[finding-form-layouts-are-hidden]] ·
[[finding-form-workflow-not-1-1]] · [[finding-publish-then-fork]] ·
[[finding-lifecycle-has-no-ordering]] · [[finding-http-200-is-not-success]] ·
[[atlas-ai-abstraction]] · [[equipment-contract]] · [[screen-contract-wizard]]

### What it retracted

[[finding-no-where-used-precedent]] · [[layout-chain]] · [[finding-routes-are-not-addressable]] ·
the conditional-fields false negative · the census gap count

See [[tenant-comparison]] for what the two settle between them.

### The caveats

[[caveat-one-equipment-contract]] · [[caveat-viewport]] ·
**no vendor schema export exists for BBW**, so no field-level claim is made for it.

Source: [`tenants/bbw-vs-american-freight.md`](../../docs/tenants/bbw-vs-american-freight.md)
