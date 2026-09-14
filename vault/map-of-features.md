---
title: Map of features
tags: [moc]
---

# The product, by what it does

Twelve feature areas — the product as a user and an administrator meet it. For the same product by
what it *stores*, see [[map-of-entities]].

| Area | The one thing to know |
|---|---|
| [[feature-page-layouts]] | Every screen is a [[page-layout-concept\|layout]] — and there are 135 of them, not 93 |
| [[feature-required-and-validation]] | Three sources of required-ness, and [[finding-no-layout-level-required\|none of them is the layout]] |
| [[feature-workflows-forms]] | A [[form-vs-page\|Form is an Issue Type]], and Form↔Workflow is **not** 1:1 |
| [[feature-data-fields]] | One catalog feeds everything — and [[finding-firm-fields-are-physical-columns\|firm fields are DDL]] |
| [[feature-drop-downs-code-tables]] | 207 platform tables, 73 populated, and delete is a per-row boolean |
| [[feature-equipment-contracts]] | [[Contract]] minus retail, accounting engine kept whole |
| [[feature-security-access]] | Four securable kinds, five levels — and `Default` means *inherit* |
| [[feature-import-export]] | Four inbound paths, and [[finding-http-200-is-not-success\|200 is not success]] |
| [[feature-search-filtering]] | Three unrelated mechanisms; `IncludeInSearch` is set on **9** placements |
| [[feature-custom-lists]] | A Form without the workflow — and the storage does not add up |
| [[feature-reference-data]] | **Four of five tables are empty**, including [[DiscountRate\|the discount rates]] |
| [[feature-administration]] | All 57 tools, classified. A quarter of them are the configuration engine |

## The modules underneath

The features are how the product presents itself. The **modules** are how the domain decomposes:

[[module-accounting]] · [[module-contracts]] · [[module-workflow]] ·
[[module-layouts-and-forms]] · [[module-reporting]] · [[module-facilities-locations]] ·
[[module-platform-tenancy]] · [[module-people-parties]] · [[module-assets-equipment]] ·
[[module-property-tax]] · [[module-documents-folders]] · [[module-portfolio-transactions]] ·
[[module-projects-capital]]

**Two modules have no folder of their own** and are documented inside [[module-contracts]]:
Expense Recovery (CAM) — see [[ExpenseRecovery]] and [[cam-waterfall]] — and Variable Rent &
Sales — see [[PercentageRent]] and [[Sales]].

← [[00-start-here]] · [[map-of-screens]] · [[map-of-rules]]
