---
title: Start here
tags: [moc, entry-point]
evidence: Observed
---

# Start here

This vault is a **graph** of the Lx product — the incumbent lease-accounting and property-management
system that ASG Edge+ is being rebuilt from. Every note is small and about one thing. Follow the
links; the shape of the product emerges from the shape of the graph.

> The long-form reference corpus lives in [`docs/`](../docs/INDEX.md). This vault does not replace it.
> `docs/` is read top to bottom; the vault is wandered. Where a note states a fact, it names the
> document the fact came from.

## What Lx is, in six sentences

Lx is a multi-tenant IWMS. The tenant is a **[[firm-tenancy|firm]]**. Everything a firm owns —
a portfolio, a site, a building, a lease — is a row in a universal supertype called
[[ProjectEntity]], and the nine [[subtype-root|subtype roots]] hanging off it are the only things
that can appear as a top-level navigation root. Almost the entire user interface is *configuration*:
a screen is a [[page-layout-concept|page layout]], a drop-down is a [[code-table|code table]], a
request form is an [[form-vs-page|Issue Type]], and the fields on all of them come from one shared
[[data-field-catalog|field catalog]]. The financial engines follow one repeated shape —
[[setup-schedule-transaction|clause, schedule, transaction, projection]] — and the ASC 842, IFRS 16
and straight-line standards are [[one-engine-three-standards|one engine with three flags]]. What a
tenant sees is decided less by entitlement than by [[finding-root-renders-iff-record-exists|whether
it holds a record of that type]].

## Four ways in

| If you want | Start at |
|---|---|
| The product by **what it does** | [[map-of-features]] |
| The product by **what it stores** | [[map-of-entities]] · [[entity-spine]] |
| **What was learned** — the conclusions | [[map-of-findings]] |
| **What is still unknown** | [[map-of-open-questions]] |
| **What two tenants settle between them** | [[tenant-comparison]] |

Also: [[map-of-screens]] (every captured screen, with its screenshot), [[map-of-rules]] (the numbered
business rules), [[map-of-concepts]].

## Read these five first

1. [[finding-root-renders-iff-record-exists]] — a navigation root appears only if the firm holds at
   least one record of that type. Four other explanations were eliminated first.
2. [[finding-firm-fields-are-physical-columns]] — tenant custom fields are real `Firm_` columns, so
   adding one is DDL. This is the strongest single argument for database-per-tenant.
3. [[finding-no-layout-level-required]] — required-ness has no layout layer; the builder's asterisk
   is the schema, rendered at paint time.
4. [[finding-publish-then-fork]] — configuration is copied into each tenant and then drifts, with
   nothing recording where it came from.
5. [[finding-http-200-is-not-success]] — REST writes return a bulk envelope, so a 200 can mean total
   failure.

## The three caveats that travel with everything here

- **[[caveat-viewport]]** — these are ExtJS viewport apps. A screenshot never shows more rows than
  the viewport held. The JSON captures are authoritative; the images illustrate.
- **[[caveat-one-equipment-contract]]** — BBW holds exactly **one** Equipment Contract, so those
  screens show one record's population, not the module's range.
- **[[caveat-labels-are-tenant-local]]** — a firm can overwrite every field label tenant-wide, so
  any UI label recorded anywhere may be local to that tenant. Internal names are the only safe
  identifier.

And one discipline: every claim here carries an [[evidence-labels|evidence label]] — Observed,
Derived or Inferred. They are not decoration. A wrong "fact" here becomes a wrong line of code later.

## No real names

Screenshots and captures contain the names of ASG staff — approvers, lease analysts, members. **No
note in this vault records a real individual.** Where the source recorded an approver, this vault
records only a count. See [[method-omitting-identities]].
