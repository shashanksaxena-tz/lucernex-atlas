---
title: Hub and Spoke — why this corpus exists
tags: [concept, architecture, asg-edgeplus]
evidence: Derived
---

ASG Edge+'s target architecture is a **Hub** of shared configuration and a per-firm **Spoke**
database holding that firm's records. Much of what this vault records is evidence about which
surfaces belong where — and about a publish mechanism that has never been specified.

What the two-tenant comparison converts from assumption into evidence:

| Layer | Evidence | Belongs in |
|---|---|---|
| Navigation tree and its `PageLayoutID`s | 109/109 identical ids | **Hub** — seeded |
| [[code-table\|Code-table registry]] (207 `TableType`s) | 207/207 identical ids | **Hub** — the *registry* is fixed |
| Code-table **values** | differ per tenant | **Spoke** — firms populate them |
| [[page-layout-concept\|Page layouts]] | 0 shared ids, **80 shared names**, 0 table mismatches | **Spoke, but [[publish-and-fork\|published from one template set then forked]]** |
| The 227-table schema | identical in both tenants | **Hub** |
| [[equipment-contract\|Equipment Contract]] root | present at BBW, absent at AF | gated by data, not entitlement — [[finding-root-renders-iff-record-exists]] |

The single strongest input is **[[finding-firm-fields-are-physical-columns]]**: 258 tenant-specific
columns on one shared [[Contract]] table cannot coexist with other tenants' columns in a single
database without either a union-of-all-tenants table or per-tenant schemas, and the incumbent chose
neither. The estate carries **two contradictory documents both numbered ADR-004**, one specifying
database-per-tenant and one arguing a shared platform database; they have never been reconciled. Lx is
direct evidence for the former.

And [[three-publish-tiers]] is the closest prior art anywhere for the Hub→Spoke *"never more than one
version behind"* rule — already implemented by the vendor, at the tier ASG does not use.

Source: [`tenants/bbw-vs-american-freight.md` §9, §16, §20](../../docs/tenants/bbw-vs-american-freight.md)
