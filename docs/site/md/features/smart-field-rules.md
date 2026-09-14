# Smart Field Rules

The conditional display engine - fields and whole sections that appear, hide or become required based on rules. The rule engine closest to what ASG Edge+ calls a rule engine: every field can carry one rule set, read as a sentence: [Show | Show and Require | Hide] this field when [all | any] of these rules match.

## Who it is for

*Derived · fact · source: `docs/features/README.md`*

Configuration administrators, working inside the layout editor. No developer is involved, which is the point of the feature and the risk in it.

## Where it is used

*Observed · fact · source: `docs/data-model/screen-routing.md`*

The conditional-rule editor inside a page layout's field properties.

## Flat, deliberately

*Observed · capability · source: `docs/modules/layouts-and-forms/conditional-fields.md`*

A flat engine, deliberately: no nesting, no mixed AND/OR. A rule set is one flat list evaluated all-or-any. That keeps every rule explicable to a business user and indexable by a machine.

## Typed operators

*Observed · capability · source: `Live capture, conditional filter editor`*

Operators depend on the driver's type: list fields get is-in / is-not-in; numbers get the six comparisons; checkboxes get selected / not selected; all get is-specified / is-not-specified. Text and date fields can never drive a rule at all - a deliberate constraint.

## Cross-entity drivers

*Observed · capability · source: `Live capture, conditional filter editor`*

Rules cross record boundaries: a lease layout offers 85 candidate driver fields drawn from four records - lease 65, entity 9, building 7, site 4. A lease field can be hidden because of a value on its site record.

## Opaque JSON storage

*Derived · capability · source: `docs/modules/layouts-and-forms/conditional-fields.md`*

Rules are stored as an opaque JSON blob, one per target field. Cheap to write, impossible to query: the product cannot answer 'which layouts depend on this drop-down?'. Storing predicates as rows instead would give the rebuild a Where-Used answer for free.

## Evidence

*Observed · fact · source: `docs/assets/screenshots/`*

2 screen captures on disk, under docs/assets/screenshots/conditional-fields — the screens themselves, not a description of them. First few: conditional-filter-editor-contract-header.jpg, conditional-filter-standalone-no-host.jpg.

![conditional-filter-editor-contract-header.jpg](../../assets/screenshots/conditional-fields/conditional-filter-editor-contract-header.jpg)
![conditional-filter-standalone-no-host.jpg](../../assets/screenshots/conditional-fields/conditional-filter-standalone-no-host.jpg)
