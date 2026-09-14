# CON-R-131 — 4.1 Typing hazard register (Constitution §4.4)

*Contracts & Leases · Derived*

**Migrating any landed Postgres column: every column across 33 tables is TEXT except 31 VARCHAR(64) primary keys — no numeric, date or boolean column exists; every value must be parsed and validated on ingest.**

Migrating any landed Postgres column: every column across 33 tables is TEXT except 31 VARCHAR(64) primary keys — no numeric, date or boolean column exists; every value must be parsed and validated on ingest.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | 1 |
| Stated as | Every landed Postgres column is `TEXT` — 1,163 of 1,194 cross-mapped columns; the other 31 are `VARCHAR(64)` PKs. No numeric, date or boolean column exists in the landed schema |
| Stated as | All 33 tables in `_crossmap.tsv`, incl. `sales.GrossSalesAmount`, `sales.NetSalesAmount`, `sales.SalesAdjustment1..6` |
| Stated as | Critical |

---

Source: `docs/modules/contracts/asg-edgeplus-mapping.md`
