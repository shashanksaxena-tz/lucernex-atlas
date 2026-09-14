---
title: The type system
tags: [concept, data-model]
evidence: Derived
---

**315 distinct type strings** across the 7,421 fields, falling into five families. The important
number is that **22.5% of the schema is a typed reference** — 60 FK types (972 fields) plus 229
dropdown types (699 fields) = 1,671 fields.

| Family | Distinct types | Fields | Share |
|---|---:|---:|---:|
| `scalar` | 14 | 5,630 | 75.9% |
| `foreign_key` | 60 | 972 | 13.1% |
| `dropdown` | 229 | 699 | 9.4% |
| [[soft-reference]] | 10 | 118 | 1.6% |
| `other` | 2 | 2 | 0.03% |

**Foreign-key types are named after their target table** — `Contract ID`, `Entity ID`, `Facility ID`.
That is what makes the [[foreign-key-graph|FK graph]] derivable at all. Four type names **lie about
their target**:

| Type | Actually points at |
|---|---|
| `Portfolio ID` | [[Program]] |
| `Employer ID` | [[Employer]] — but the column is usually `VendorID` |
| `Country, State, County ID` | [[StateProvinceCountry]] |
| `County ID` | [[Jurisdiction]] |

Three resolve to **nothing** and point into configuration metadata: `item ID` (56 columns),
`Custom Drop Down ID` (2), `DashboardComponent ID` (2). `item ID` is how you reach
[[PageLayout|page layouts]], which is why they never appear in the object census —
[[Firm]] alone holds 11 of those columns, one per subtype.

`Template ID` (31 fields) is **polymorphic** across 8 template targets — resolved per column name, not
per type.

**Four scalar types cover 60% of the product**: `Text` 1,916, `Currency` 1,207, `Number` 846, `Date`
511. Two traps: `Time` is a **timestamp**, not a clock time (it is what `CreatedDate` uses), and
`Acreage` is the only unit-bearing scalar.

**157 of 229 code lists are used by exactly one field**, and 214 of 229 end in `Code`.

Source: [`data-model/type-system.md`](../../docs/data-model/type-system.md)
