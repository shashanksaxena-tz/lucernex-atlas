---
title: The AI lease-abstraction pipeline
tags: [concept, integration, contracts]
evidence: Observed
---

Three of the REST API's eleven tags are a **live third-party AI lease-abstraction integration** — 16
operations in total, discovered only from the OpenAPI capture.

| Route | Verbs | What it does |
|---|---|---|
| `/atlas-api/import/{leaseId}` | POST | Fetch one lease from the **Atlas** API and import it |
| `/atlas-api/import/{leaseId}/async` | POST | The same, scheduled asynchronously |
| `/atlas-api/contracts` | GET | List active contracts for *update-existing* import |
| `/adapter-config/{vendorId}/{fileName}` | GET · PUT · DELETE | The vendor's field-mapping config |
| `/adapter-config/firms/{firmId}/{vendorId}/{fileName}` | GET · PUT · DELETE | **Per-firm override** of that mapping |
| `/adapter-config/vendors` | GET | Registered vendor adapter ids |

**The field mapping is tenant-configurable.** A vendor adapter has a default config and a firm can
upload an override — so the AI-extraction-to-Lx field mapping is configuration, per tenant, not code.

**It ties together four observations the corpus had recorded separately with no explanation:** the
`Allow AI Lease Abstraction` entitlement flag on [[Firm]]; BBW's seven `ASG Lease Abstract - *`
layouts that AF lacks; `AI Abstracted` as a value in four status code tables; and `AI Abstracted`
becoming **delete-protected** in build `26.09`. They are one feature — see
[[finding-tenants-differ-by-one-feature]].

That last point **retires the corpus's claim that `AI Abstracted` is "a tenant-added status"**. On
current evidence it is vendor-shipped. *(Inferred — the flag change was observed across builds, not
the value's origin.)*

Whether any of it is in scope for ASG Edge+ is [[q-bbw-17-ai-abstraction-in-scope]], and nobody has
been asked, because nothing in the corpus showed the pipeline existed.

Source: [`tenants/bbw-vs-american-freight.md` §17](../../docs/tenants/bbw-vs-american-freight.md)
