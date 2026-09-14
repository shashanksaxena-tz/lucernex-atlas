---
title: Space
tags: [entity, facilities]
evidence: Observed
---

**`space` · 27 fields · [[module-facilities-locations]]**

A leasable space or suite inside a [[Facility]] — the occupancy layer that makes multi-tenant
buildings expressible. A Space must belong to exactly one Facility ([[rule-FAC-R-015]]).

Paired with `Tenant`, which is *not* a separate party object — see [[Employer]], which is the one
table behind landlord, tenant and vendor alike.

See [`space-management.md`](../../docs/modules/facilities-locations/space-management.md)
