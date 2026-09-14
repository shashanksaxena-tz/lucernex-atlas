---
title: Map of findings
tags: [moc]
---

# What was learned

Every finding states its evidence. Where a finding is **Inferred**, it says so and names its
falsifier. Four entries below are **retractions** — things this corpus published and then withdrew.

## The ones that change a rebuild

| Finding | Evidence |
|---|---|
| [[finding-root-renders-iff-record-exists]] — a navigation root appears only if the firm holds a record of that type | **Inferred**, 11-for-11 |
| [[finding-firm-fields-are-physical-columns]] — tenant custom fields are `Firm_` columns, so adding one is DDL | Observed |
| [[finding-no-layout-level-required]] — required-ness has no layout layer | Observed |
| [[finding-publish-then-fork]] — one layout set, copied per tenant, then drifting with no lineage | Derived |
| [[finding-http-200-is-not-success]] — writes return a bulk envelope | Observed |
| [[finding-discount-rate-table-empty]] — both tenants run ASC 842 against an empty rate table | Observed |
| [[finding-lifecycle-has-no-ordering]] — the lifecycle is a drop-down with null `SortOrder` | Observed |
| [[finding-rules-store-labels-not-ids]] — renaming a drop-down value silently breaks rules | Observed |
| [[finding-layouts-over-projections]] — the layout engine must target read models | Observed |
| [[finding-accounting-runs-per-asset]] — the engine runs per asset, not only per lease | Observed |

## Architecture and tenancy

[[finding-platform-seeded-by-id]] · [[finding-tenants-differ-by-one-feature]] ·
[[finding-punch-list-out-of-scope]] · [[finding-no-generic-export]]

## Layouts and navigation

[[finding-form-layouts-are-hidden]] · [[finding-two-files-serve-56-percent]] ·
[[finding-routes-are-not-addressable]]

## Workflow

[[finding-form-workflow-not-1-1]] · [[finding-no-task-step-anywhere]] ·
[[finding-routing-is-to-named-people]] · [[finding-workflow-versioning-is-naming]] ·
[[finding-maker-checker-pairs]]

## Accounting and contracts

[[finding-classification-polarity-inverted]] · [[finding-schedules-are-approved-not-published]] ·
[[finding-engine-is-button-driven]] · [[finding-wizard-writes-two-entities]] ·
[[finding-computed-fields-render-as-prose]]

## Data model

[[finding-fk-graph-undercounts]]

## Retractions, and the pattern behind them

**Four confident readings were published and withdrawn**, and every one of them failed the same way —
a cheap signal was trusted instead of the thing it stood for.

[[finding-no-where-used-precedent]] · [[finding-one-row-can-hide-a-module]] ·
[[method-cheap-signals]] · [[method-fetch-is-not-render]]

← [[00-start-here]] · [[map-of-open-questions]] · [[evidence-labels]]
