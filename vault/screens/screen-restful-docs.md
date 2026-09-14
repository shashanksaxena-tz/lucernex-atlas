---
title: "RESTful WebService Docs"
tags: [screen, administration,api,diagnostics]
evidence: Observed
---

`/en/test/RESTful.jsp`

> **One of only two of the 57 admin tools with no screenshot in this corpus — deliberately. The page
> renders live Basic and JWT Bearer credentials for copy.** No token was read, captured or recorded at
> any point. See [[method-omitting-identities]].

An interactive generator embedding stock Swagger UI pointed at **`/rest/api-docs/swagger`**, which
serves the complete **OpenAPI 3.0.1** document — **141 paths, 160 operations: 104 GET, 40 POST, 7 PUT,
9 DELETE**.

**Fetching the spec directly makes the generator unnecessary**, which is how the capture was done
structure-only.

This screen closed the corpus's third-ranked open blocker: **[[rest-business-object|REST is fully
CRUD, and it is the write path]]**. It also unlocked the 25 tables
[[screen-view-object-model|the schema viewer refuses]].

The other tool with no screenshot is [[screen-delete-entities]].

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
