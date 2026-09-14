---
title: Map of screens
tags: [moc]
---

# Every captured screen

Each note embeds its screenshot with a caption saying **what to notice**, and cites the canonical
path in `code` — the citation that cannot break when the screenshot sets are re-captured.

> **[[caveat-viewport]]** — these are ExtJS viewport apps. A screenshot never shows more rows than the
> viewport held. The JSON captures are authoritative; images illustrate.

## The end-user product

[[screen-main-navigation]] · [[screen-dashboard-home]]

**A contract, as a user sees it** — [[screen-contract-summary]] ·
[[screen-contract-abstract-details]] · [[screen-contract-payment-details]] ·
[[screen-contract-accounting-details]] · [[screen-contract-capital-lease-test]] ·
[[screen-contract-accrual-details]] · [[screen-contract-co-tenancy]] ·
[[screen-asc842-rent-schedule]]

**[[equipment-contract|Equipment Contract]]** *(one record only — [[caveat-one-equipment-contract]])* —
[[screen-eq-details-summary]] · [[screen-eq-abstract-details]] · [[screen-eq-payment-details]] ·
[[screen-eq-accounting-details]]

## Administration — [[feature-administration|all 57 tools]]

**Configuration (14)** — [[screen-manage-data-fields]] · [[screen-manage-page-layouts]] ·
[[screen-manage-page-layout-builder]] · [[screen-conditional-filter-editor]] ·
[[screen-contract-wizard]] · [[screen-manage-forms]] · [[screen-manage-custom-lists]] ·
[[screen-manage-work-flows]] · [[screen-manage-firm-drop-downs]] · [[screen-client-drop-downs]] ·
[[screen-lease-status-values]] · [[screen-manage-top-menu]] · [[screen-manage-firm-dictionary]] ·
[[screen-layout-changes]] · [[screen-manage-folder-templates]] · [[screen-manage-binder-templates]] ·
[[screen-manage-schedule-templates]] · [[screen-manage-milestone-timeline]]

**Master data (8)** — [[screen-manage-company]] · [[screen-manage-portfolios]] ·
[[screen-manage-locations]] · [[screen-manage-facilities]] · [[screen-manage-contracts]] ·
[[screen-manage-complex]] · [[screen-manage-organizations]] · [[screen-manage-parts]]

**People and access (7)** — [[screen-manage-members-contacts]] · [[screen-manage-membership]] ·
[[screen-manage-employers]] · [[screen-manage-employer-members]] · [[screen-manage-vendors]] ·
[[screen-manage-regions]] · [[screen-manage-security]]

**Financial reference data (5)** — *four of the five are empty* —
[[screen-manage-discount-rates]] · [[screen-manage-cpi-data]] · [[screen-manage-exchange-rates]] ·
[[screen-manage-fiscal-calendar]] · [[screen-manage-holiday-calendar]]

**Import, export and jobs (6)** — [[screen-import-data]] ·
[[screen-import-best-practice-templates]] · [[screen-export-configuration]] · [[screen-job-log]] ·
[[screen-report-log]] · [[screen-generate-enterprise-report]]

**Diagnostics and developer tools (7)** — [[screen-view-object-model]] · [[screen-walk-hierarchy]] ·
[[screen-related-fields]] · [[screen-audit-reports]] · [[screen-email-log]] ·
[[screen-restful-docs]] · [[screen-graphql-explorer]] · [[screen-manage-dashboard-reports]]

**Out of scope and vendor-only** — [[screen-budget-and-bidding-tools]] (6) ·
[[screen-lxadmin-tools]] (4) · [[screen-delete-entities]] · [[screen-admin-dashboard]]

## Two screens have no capture, deliberately

[[screen-restful-docs]] renders live credentials; [[screen-delete-entities]] is vendor-only and
destructive. See [[method-omitting-identities]].

## And a route is not a URL

[[finding-routes-are-not-addressable]] — a `fetch`-based audit overstates deep-linkability by more
than 2×. [[method-fetch-is-not-render]].

← [[00-start-here]] · [[map-of-features]]
