---
title: Security
tags: [entity, security, platform-tenancy]
evidence: Derived
---

**no physical table · 21 fields · [[module-platform-tenancy]]**

A **computed, read-only shadow** of [[UserClassSecurity]]. The two declare 21 fields each, **identical
name for name**, and only `UserClassSecurity` is editable ([[rule-PLT-R-006]]).

One of the **7 objects in the census with no physical table**.

Anyone reading the schema and finding two identical security tables will assume a modelling error.
It is a projection. See [[security-ladder]].
