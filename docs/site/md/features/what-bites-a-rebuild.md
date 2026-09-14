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

## Punch List is out

*Observed · fact · source: `docs/data-model/object-catalog.md`*

Punch List is out of scope. The four Punch List tables belong to construction management, which the approved BRDs assign to a different product. They stay in the census so impact analysis is never silently wrong at the boundary, and are documented nowhere else.
