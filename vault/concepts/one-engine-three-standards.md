---
title: One engine, three standards
tags: [concept, accounting, core]
evidence: Observed
---

ASC 842, IFRS 16 and straight-line are **not three modules**. They are one
[[SLSummary]]/[[SLPeriod]] summary-and-period pair with three mutually exclusive flags —
`IsSLSchedule`, `IsASC842Schedule`, `IsIFRS16Schedule` — recording which standard a schedule was
generated under.

- **Classification is a separate record**, [[ContractFinancialTest]] (93 fields), not a field on the
  contract.
- The three schedule-type [[code-table|code tables]] are **byte-identical** in structure: `ShortName`,
  `ActualLongName`, `Inactive`, `DontAmortizeAssetValue`, and **20 numbered `ExportAcctNNumber` GL
  slots** each.
- **Only one is configured.** `ASC 842 Schedule Type Code` (`2162`) holds exactly **1 row**
  (`842 Rent`); `2161` (straight-line) and `2163` (IFRS 16) are **empty**. IFRS 16 has a screen, a
  schedule type table and a rent-schedule layout — and no configured data anywhere.
- The standard is also a **layout** distinction, not only a data one: `ASG ASC 842 Schedule` (98859)
  and `ASG SL Summary` (98873) declare the *same* primary table.

Two structural facts a rebuild must plan around:

- **[[finding-classification-polarity-inverted]]** — any test *Fail* means Finance lease; all five
  *Pass* means Operating ([[rule-ACC-R-011]]).
- **[[finding-schedules-are-approved-not-published]]** — a generated schedule is a candidate that must
  pass a three-step approval, and approval is irreversible ([[rule-ACC-R-050]]).

And the hole underneath it all: **[[finding-discount-rate-table-empty]]**. Both tenants run all three
standards with an empty rate table.

Source: [`modules/accounting/`](../../docs/modules/accounting/README.md)
