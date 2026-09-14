---
title: The layout chain
tags: [concept, layouts]
evidence: Observed
---

Several [[page-layout-concept|layouts]] can point at one navigation node. They are **not a set the
runtime chooses from — they are an ordered sequence**, linked by `PreviousPageLayoutID`.

```
Contract : Abstract Info : Abstract Details
  Contract Abstract Details → Common Area Maintenance → Delivery Requirements
    → Funds and Expenses → Real Estate Taxes

Contract : Payment Info : Percentage Rent
  ASG Contract Percent Rent [LIST] → Percent Rent Schedule [SEP] → Breakpoint Schedule [SEP]
```

**8 of 8** chained pairs share the same navigation parent, and every node with more than one layout
resolves to exactly one chain with a single head.

This corrects a reading that a column name invited. `bbw-layout-engine-tables.json` recorded
`PreviousPageLayoutID` as "a self-reference used for versioning/duplication" — a fair guess from the
name, and wrong. The chains link **semantically distinct layouts in a reading order**. It is one of
the [[method-cheap-signals|cheap-signal failures]] the corpus catalogues.

Two consequences for a rebuild:

- The model is **`(navigation_node, sequence)`** on the layout. Order carries meaning.
- **Chains cross modes.** Two heads are `LIST` layouts followed by `SEP` pages. A rebuild that models
  list and detail layouts as separate populations cannot express this.

What remains open is only presentation — the runtime shows the head and offers the rest through a
layout-selector dropdown, observed on a rendered contract. See [[screen-contract-summary]].

Source: [`tenants/bbw-vs-american-freight.md` §19](../../docs/tenants/bbw-vs-american-freight.md)
