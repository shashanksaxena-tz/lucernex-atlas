# What bites a rebuild

The findings that cut across every feature, and that a delivery plan gets wrong if it reads only the schema. Each one was established in a named document and is repeated here because filing it under a single feature would hide it from the features it also governs.

## Data gates the roots

*Observed · fact · source: `docs/features/security-access/README.md`*

Navigation roots are gated by data, not by permission. A navigation root renders if and only if the firm holds at least one record of that ProjectEntityTypeName. Four other candidate gates — user-class page security, the action-verb list, field-level security and the firm feature flags — were each tested and eliminated: all three security gates are open at American Freight and the Equipment Contract root still does not render.

## No layout-level required

*Observed · fact · source: `docs/features/required-and-validation/README.md`*

Required-ness has no layout-level layer. The red asterisk a user sees in the builder is the schema-required flag rendered at paint time, not a per-placement setting stored against the layout. Show and Require exists as a conditional action and is used zero times in either tenant.

## Layouts are a sequence

*Observed · fact · source: `docs/features/page-layouts/README.md`*

PreviousPageLayoutID is a sequence pointer. Layouts attached to one navigation node form an ordered chain through PreviousPageLayoutID, and the chains cross SEP and LIST modes. It is a sequence, not a parent link — the parent link is ParentPageLayoutID, which is a separate column.

## 135 layouts, not 93

*Observed · fact · source: `docs/features/page-layouts/README.md`*

135 layouts, not 93. Manage Page Layouts lists 93 rows, but 42 further form layouts are reachable only through Issue Types. The real layout population is 135.

## Rules in opaque JSON

*Observed · fact · source: `docs/modules/layouts-and-forms/conditional-fields.md`*

Conditional field rules live in JSONConfigText. Conditional display rules are stored as an opaque JSON blob in PageLayoutField.JSONConfigText. Eight layouts carry 50 such records. The comparison value crtVal1 stores the display label, not the underlying id — so a rule breaks silently when somebody renames a drop-down value.

## Custom fields are DDL

*Observed · fact · source: `docs/features/data-fields/README.md`*

Firm custom fields are physical columns. A firm custom field is a physical Firm_-prefixed column on the table, not a row in a value store. Adding one is a DDL change. That is direct evidence for database-per-tenant and against a shared schema.

## Three publish tiers

*Derived · fact · source: `docs/tenants/bbw-vs-american-freight.md`*

Configuration publishes along three tiers. Configuration moves platform to firm to firm, and only the vendor's own tier is versioned. Import clones the configuration and discards its lineage, so a tenant cannot be told which version of a template it is running.

## 200 is not success

*Observed · fact · source: `docs/data-model/rest-api.md`*

HTTP 200 does not mean the write succeeded. The REST surface is fully CRUD, but writes return an ImportResults envelope: the transport status is 200 while the envelope reports the failure. Any client must read the envelope, not the status code.

## No Equipment table

*Observed · fact · source: `docs/features/equipment-contracts/README.md`*

EquipmentContract has no table. There is no EquipmentContract table in any inventory. Equipment contracts are Contract rows discriminated by ProjectEntityTypeName = "Equipment Contract" — with a space in the value.

## Discount rates empty

*Observed · fact · source: `docs/features/reference-data/README.md`*

The discount-rate table is empty in both tenants. The reference table that should supply the ASC 842 discount rate holds zero rows in both captured tenants, while the accounting engine runs. Where the rate actually comes from is unresolved, and it blocks the accounting rebuild.

## Versions are a suffix

*Observed · fact · source: `docs/features/workflows-forms/README.md`*

Workflow versioning is a naming convention, not a feature. The live template is the unsuffixed one. A v1 or v2 suffix marks a superseded template, not a successive version, and the fact that it was archived is recorded only as free text in the grid's Description column — "Archived and replaced with new workflow on 10.02.25". There is no version field, so nothing can order them. This settles which Lease Admin Request is live, and the same holds for Lucernex Change Request.

## Fields are documented

*Observed · fact · source: `docs/data-model/pg/bbw-field-inventory.csv`*

6,091 fields carry the vendor's own definition. The field inventory explains what nearly every field is FOR, in the vendor's words — not what it is called or how it is typed, which is all the other readings give. Six thousand of the 7,421 fields in the census now resolve to a definition, and every field node in the schema map leads with it. Read the provenance note before citing it alongside the census: it is the same export, read more sharply — not a second witness.

## One export, two readings

*Observed · fact · source: `docs/data-model/pg/bbw-field-inventory.csv`*

The inventory and the object census are the same source. 222 of 223 objects and 7,273 of roughly 7,400 fields are common to both, with the same Firm_ names present and the same CRL_ names absent. The field inventory is a sharper reading of the export the object census already came from, not an independent corroboration of it. Treating it as a second witness is how one silence becomes two confident citations — so where the two agree, that is one fact stated twice.

## Required: two answers

*Observed · fact · source: `docs/data-model/pg/bbw-field-inventory.csv`*

The two captures of required-ness disagree on 213 fields. The Data Fields catalogue marks 637 fields required; the field inventory marks 606; only 515 appear in both. 122 are required according to the catalogue alone and 91 according to the inventory alone. These two genuinely are separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is evidence, not noise, and it echoes the column-flag versus catalogue-flag split that already disagreed on 44 fields. A rebuild that adopts one capture drops the other's obligations silently.

## Custom lists differ

*Observed · fact · source: `docs/features/custom-lists/README.md`*

The Firm_ precedent does not extend to custom lists. CRL_, OpEx and LAR_ prefixes appear zero times in all 7,368 inventory rows, and ClientListRow's 24 columns carry no prefix at all. The custom-lists analysis had argued that custom-list values are probably real columns on the strength of the Firm_ precedent. The inventory confirms that precedent at column level and shows ClientListRow demonstrably not following it, so the analogy is weaker, not stronger. Only a REST deep-serialise of one custom-list row can settle it: every offline artefact traces back to the one export that omits these fields.

## Replica is not schema

*Observed · fact · source: `docs/data-model/pg/bbw-field-inventory.csv`*

Replication coverage is not the product's schema. The inventory's PG Table Status column splits 69 tables "Created — holds data" against 150 "Not created yet". That describes the coverage of one replication loader targeting one database, lxr_drp_bbw — not the size of Lx's schema. The tell is project_entity: 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it cannot be empty. The loader simply does not produce it. Read that column as loader coverage, never as a statement about the product.

## Punch List is out

*Observed · fact · source: `docs/data-model/object-catalog.md`*

Punch List is out of scope. The four Punch List tables belong to construction management, which the approved BRDs assign to a different product. They stay in the census so impact analysis is never silently wrong at the boundary, and are documented nowhere else.
