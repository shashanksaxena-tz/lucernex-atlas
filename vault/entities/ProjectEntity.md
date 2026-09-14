---
title: ProjectEntity
tags: [entity, platform-tenancy, spine, core]
evidence: Observed
---

**`project_entity` · 107 fields · [[module-platform-tenancy]]**

The universal entity supertype. Every ownable thing in the product has a row here, and **161 of 223
objects carry a `ProjectEntityID`** pointing at it — joint first in the schema's in-degree ranking.

- It is **not the tenant key**. [[firm-tenancy|`FirmID`]] is. `ProjectEntityID` is the *intra-tenant
  partition* key, and it must survive database-per-tenant even though `FirmID`'s job is subsumed by
  the database boundary ([[rule-PLT-R-003]]).
- The discriminator is `ProjectEntityTypeName`, and it decides
  [[finding-root-renders-iff-record-exists|whether a navigation root renders at all]].
- The `Entity ID` FK type appears on **163** columns; 161 are literally named `ProjectEntityID`.
- The UI labels it **"General Entity Info"**, which is why a label-based census diff reported it
  missing — see [[caveat-labels-are-tenant-local]].

Nine objects carry its 8-column block as [[subtype-root|subtype roots]]; 161 are
[[entity-scoped-vs-firm-global|entity-scoped]]; 52 sit above it.

A competing candidate exists and is unreconciled: [[Project]] and `ProjectEntity` are both live
candidates for the spine ([[rule-PLT-R-016]]).

See [[entity-spine]] · [`data-model/project-entity.md`](../../docs/data-model/project-entity.md)
