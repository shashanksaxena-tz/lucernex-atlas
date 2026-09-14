---
title: Firm custom fields are physical columns — so adding one is DDL
tags: [finding, tenancy, data-model, core]
evidence: Observed
---

> Tenant custom fields are **not rows in a metadata table**. They are ordinary physical columns named
> `Firm_<Name>`, fully typed. **359 across the schema, 20 objects, 258 on [[Contract]] alone.**

Verified directly against `_lucernex_objects_summary.txt`, and corroborated from two other surfaces:
the [[data-field-catalog|catalog]] scopes them `Firm`, and the
[[screen-contract-wizard|contract wizard]] places them by their literal names
(`Contract_Firm_LeaseAnalyst`, `Contract_Firm_FixturingPeriod`, …).

### The consequence

**Adding a firm custom field is a DDL change against the tenant's table.** A per-firm column on a
shared table is only workable if **each tenant has its own database**.

The estate carries **two contradicting documents both numbered ADR-004** — one specifying
database-per-tenant, one arguing a single shared platform database. They have never been reconciled.
**Lx is direct evidence for the first and against the second**: 258 tenant-specific columns on one
shared `Contract` table cannot coexist with other tenants' columns in a single database without either
a union-of-all-tenants table or per-tenant schemas, and the incumbent chose neither. See
[[hub-and-spoke]].

It also explains something the corpus had recorded without explaining: **[[data-field-catalog|Manage
Data Fields]] is read-only to a firm in both tenants.** You cannot self-service a DDL change. Field
creation is a vendor operation because it has to be.

### On the number

Three sources give 359 (census), 298 (`showGlobal=false` differencing) and 205 (catalog). They measure
different populations and are **unreconciled** — [[q-bbw-22-three-firm-field-counts]]. **The argument
does not rest on the number.** It rests on firm fields being *physical columns at all*, which every
inventory agrees on. Whether it is 205 or 359, adding one is still DDL.

**Knock-on:** `bbw-platform-tables.json` reads `Contract` at 307 fields against the census's 570 —
almost exactly the 258 `Firm_` columns. **Every field count derived from that capture is a lower
bound.**

See [[firm-custom-field]] · [[feature-data-fields]]
