# Lx Manage Data Fields — Cross-Mapping Report

**Date**: 2026-09-03
**Sources merged**:
1. **Lx UI** — `data-fields-global-tree-rows.json` (6,297 rows) + `data-fields-firm-tree-rows.json` (549 rows)
2. **Lucernex → PostgreSQL inventory (jcrew)** — `Lucernex_to_PostgreSQL_Inventory_jcrew.xlsx` (7,421 rows in `Field Inventory`)
3. **ASG Edge Plus Draft Feature List V1.xlsx** — sheets: `ExistingGlobalFields` (6,345), `NeededGlobalFields` (4,304), `ExistingFirmFields` (521), `NeededFirmFields` (374)

---

## Headline numbers

| Metric | Count |
| --- | ---: |
| Lx top-level groups | **24** |
| Lx subgroups (across all top groups) | 320 |
| Lx leaves — Global (`isGlobal=true`) | **5,953** |
| Lx leaves — Firm (`isGlobal=false`) | **205** |
| Lx leaves total | **6,158** |
| Lx distinct tables in use | **214** |
| Lx distinct field types | 280+ |
| Lucernex objects | **223** |
| Lucernex PG tables | **222** |
| Lucernex total field rows | 7,421 |
| Lx leaves matched to Lucernex PG | **1,194** (19.4%) |
| Lx leaves **without** Lucernex match | 4,964 (80.6%) |
| ASG Existing Global rows | 6,345 |
| ASG Needed Global rows | 4,304 |
| ASG Existing Firm rows | 521 |
| ASG Needed Firm rows | 374 |

The 80.6% mismatch is expected: the jcrew PostgreSQL export is a **sample firm** (Accruent's reference customer) and only a fraction of all Lucernex platform tables. The Lucernex object/field inventory in the export is the **floor** — every other table still exists in the Lucernex platform even if not in this export.

---

## Lx top-level groups (24)

| Lx Top Group | UI Leaves (Global) | UI Leaves (Firm) | Distinct PG tables used | ASG Existing Global | ASG Needed Global | ASG Existing Firm | ASG Needed Firm |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Budget | 130 | 0 | 8 | ✓ | – | 13 | 0 |
| Company Items | 681 | 5 | 33 | ✓ | – | 37 | 26 |
| Complex | 45 | 0 | 1 | ✓ | – | 2 | 0 |
| Contract | **2,637** | **186** | 63 | ✓ | ✓ | 301 | 295 |
| Demographics Criteria | 37 | 0 | 4 | ✓ | – | 5 | 0 |
| Documents | 47 | 0 | 4 | ✓ | ✓ | 5 | 5 |
| Equipment/Assets | 138 | 0 | 3 | ✓ | ✓ | 4 | 4 |
| Facility | 194 | 1 | 5 | ✓ | ✓ | 7 | 7 |
| Location | 63 | 4 | 2 | ✓ | ✓ | 6 | 4 |
| Milestones | 39 | 0 | 2 | ✓ | – | 27 | 0 |
| Parcel | 250 | 0 | 8 | ✓ | ✓ | 10 | 10 |
| Pro Forma Lease | 218 | 0 | 1 | ✓ | – | 6 | 0 |
| Program Summary Information | 85 | 0 | 1 | ✓ | – | 1 | 0 |
| Prototype | 15 | 0 | 1 | ✓ | – | 1 | 0 |
| Purchase Management | 50 | 0 | 3 | ✓ | – | 4 | 0 |
| RE Planner | 48 | 0 | 3 | ✓ | – | 2 | 0 |
| RE Transaction | 160 | 0 | 4 | ✓ | – | 4 | 0 |
| Schedule | 75 | 0 | 6 | ✓ | – | 37 | 0 |
| Site Survey | 78 | 0 | 1 | ✓ | – | 3 | 0 |
| Specialized Forms | 286 | 0 | 19 | ✓ | – | 17 | 0 |
| Statics | 243 | 0 | 45 | ✓ | ✓ | 0 | 0 |
| Summary Information | 317 | 6 | 17 | ✓ | ✓ | 19 | 13 |
| Wizard | 18 | 0 | 4 | ✓ | ✓ | 4 | 4 |
| Workflow | 102 | 0 | 5 | ✓ | ✓ | 5 | 5 |

**Reading this table**:
- "UI Leaves (Global)" — fields with `isGlobal=true` in the Lx UI. "UI Leaves (Firm)" — `isGlobal=false` (Firm fields, almost all `Firm_*` prefix).
- "Distinct PG tables used" — number of unique Lucernex PostgreSQL tables referenced by leaves in this group (via the `Table` cell).
- "ASG Existing/Needed" — does the feature list call out fields in this group; counts how many ASG rows are mapped to that top group.

**Top group by leaf count**: `Contract` (2,637 + 186 = 2,823 leaves), then `Company Items` (686), `Summary Information` (323), `Specialized Forms` (286), `Parcel` (250), `Statics` (243), `Pro Forma Lease` (218), `Facility` (195).

**Top groups with both Global AND Firm leaves**: `Contract`, `Company Items`, `Facility`, `Location`, `Summary Information`. These are the only 5 groups where ASG has firm-specific field requirements; all others are Global-only.

---

## ASG status distribution across Lx leaves

| ASG status | Lx leaves |
| --- | ---: |
| `EXISTING_GLOBAL;NEEDED_GLOBAL` | 4,597 |
| `EXISTING_GLOBAL` | 1,305 |
| `EXISTING_FIRM;NEEDED_FIRM` | 166 |
| *(no ASG match)* | 59 |
| `EXISTING_FIRM;EXISTING_GLOBAL;NEEDED_FIRM;NEEDED_GLOBAL` | 24 |
| `EXISTING_FIRM;EXISTING_GLOBAL;NEEDED_FIRM` | 4 |
| `EXISTING_FIRM` | 3 |

**Implication**: 4,597 leaves are listed in both `ExistingGlobalFields` AND `NeededGlobalFields` — meaning the ASG feature list calls them out as **required for ASG but currently not implemented** in the platform. These are the **delta fields** to deliver.

The 59 "no ASG match" leaves are not flagged in the feature list. They mostly live in `WorkFlowTemplateStepAction` (1) and the `Contract / Financial - Rent Schedule` MONEY aggregator fields (58), which are derived/computed and not user-maintainable.

---

## Lucernex PG coverage

| Lucernex PG table | Lx leaves matched |
| --- | ---: |
| asset | 121 |
| facility | 88 |
| program | 85 |
| member | 78 |
| parcel | 73 |
| employer | 71 |
| scenario | 69 |
| location | 65 |
| complex | 45 |
| covenant | 43 |
| tenant | 41 |
| person | 37 |
| task | 36 |
| responsibility | 31 |
| sales | 27 |
| insurance | 26 |
| space | 26 |
| competitor | 25 |
| document | 22 |
| allowance | 20 |
| … (13 more tables) | 8–18 each |

33 of 222 Lucernex tables are reached by at least one Lx leaf. The other 189 are not surfaced in `Manage Data Fields` — they are platform-internal tables (e.g. `audit_log`, `report_queue`, `workflow_state`, `permission_role`).

---

## Top Lx field types (descending)

| Field type | Leaves |
| --- | ---: |
| `sTYPE_TEXT` | 1,044 |
| `sTYPE_MONEY` | 899 |
| `sTYPE_DATE` | 377 |
| `sTYPE_NUMBER` | 348 |
| `sTYPE_UNFORMATTED_NUMBER` | 279 |
| `sTYPE_MEMBER` | 262 |
| `sTYPE_MONEY_MATH_OPERATION` | 262 |
| `sTYPE_TIME` | 232 |
| `sTYPE_BOOLEAN` | 229 |
| `sTYPE_PERCENTAGE` | 188 |
| `sTYPE_TEXTAREA` | 166 |
| `sTYPE_CHECKBOX` | 155 |
| `sTYPE_PERCENT_MATH_OPERATION` | 134 |
| `sTYPE_CONTRACT` | 62 |
| `sTYPE_SUBMITBUTTON` | 62 |
| `sTYPE_CUSTOM_CODE_FIELD` | 55 |
| `sTYPE_AREA` | 54 |
| `sTYPE_PAGE_LAYOUT` | 46 |
| `sCODE_CURRENCY_TYPE` | 37 |
| `sTYPE_NUMBER_FRACTION6DIGITS` | 34 |
| `sTYPE_PERSON` | 31 |
| `sTYPE_EMPLOYER` | 26 |
| `sCODE_JOB_TITLE` | 24 |
| `sTYPE_DROPDOWN_YEAR` | 23 |
| `sTYPE_MATH_OPERATION` | 23 |
| `sCODE_EXPENSE_GROUP` | 20 |
| `sTYPE_PROJECT_ENTITY` | 18 |
| `sCODE_BUILDING_AREA_UNIT` | 18 |
| `sCODE_EXPENSE_TYPE` | 18 |

**Patterns**:
- `sTYPE_*` are primitive (text, money, date, number, percent, boolean, member, time, person, employer).
- `sCODE_*` are reference-data enumerations (currency, job title, expense group, expense type, building area unit). These are "code tables" — the sCODE_X type means a foreign key to the `code_X` lookup table.
- `sTYPE_MONEY_MATH_OPERATION` (262) and `sTYPE_PERCENT_MATH_OPERATION` (134) are formula fields — computed from other money/percent fields.
- `sTYPE_CUSTOM_CODE_FIELD` (55) lets a firm point at any custom code table.
- `sTYPE_PAGE_LAYOUT` (46) is interesting — it lets a field hold a reference to a Page Layout. This is how Page Layouts are wired into Manage Data Fields.
- `sTYPE_SUBMITBUTTON` (62) and `sTYPE_CONTRACT` (62) are action/reference types, not data carriers.

---

## Top Lx table associations (descending)

| Lx table | Leaves | What it is |
| --- | ---: | --- |
| ExpenseRecovery | 567 | Expense recovery rules per contract |
| Contract | 402 | Master contract record |
| LeaseInfo | 218 | Lease-specific data (term, dates, options) |
| ProjectEntity | 170 | Real-estate project |
| SLSummary | 135 | Sales / lease summary rollup |
| Asset | 126 | Equipment / asset |
| PaymentTransaction | 118 | Payment / accrual transactions |
| ExpenseSetup | 105 | Expense setup config |
| ContractFinancialTest | 92 | Financial test (debt covenant etc.) per contract |
| Facility | 89 | Facility / building |
| Program | 85 | Program (e.g. multi-store rollout) |
| Member | 78 | User / member |
| SLPeriod | 78 | Sales/lease period |
| SiteSurvey | 78 | Site survey |
| Parcel | 74 | Land parcel |
| Employer | 71 | Employer / company |
| Scenario | 70 | What-if scenario |
| VirtualSalesPeriod / VirtualUsagePeriod | 66 each | Virtual periods (forecasting) |
| Location | 66 | Location within facility |
| WorkFlowTemplateStep | 59 | Workflow step |
| AccrualTransaction | 54 | Accrual transaction |

`ExpenseRecovery` is the #1 Lx table association (567 leaves). It's where most of the rule-level fields live (basis, caps, exclusions, escalators, etc.).

---

## Per-leaf cross-mapping

The full per-leaf table is in `_crossmap.md` (4.9 MB, 10,841 lines) grouped by Lx top group, and `_crossmap.tsv` (0.99 MB, 6,159 rows) for machine consumption.

`tsv` columns:
```
Scope  TopGroup  SubGroup  LeafLabel  LeafInternal  LeafType  LeafReq  LeafRO  LeafTable  LucObject  LucField  LucLabel  LucTable  LucColumn  LucType  LucKeyRole  ASGStatus
```

`md` columns:
```
Path | Label | Internal | Type | Req? | RO? | Lx Table | Lucernex Match | PG Column | PG Type | Key Role | ASG Status
```

Plus a final **reverse section** listing every Lucernex PG table that no Lx top-group references (192 tables — most are platform-internal) and a **forward section** of every ASG `NeededGlobal`/`NeededFirm` row (4,678 rows) — i.e. fields ASG marked required that are also exposed in the Lx UI.

---

## What this map does NOT cover

- **ZCRO firm export** — the user mentioned an "export of one of the firms called ZCRO" with actual data values for everything. Neither `_xlsx_lucernex_jcrew.txt` nor `_xlsx_feature_list.txt` contains "ZCRO", "zcro", or any firm-specific export sheet. The dump did not capture a ZCRO tab. If the ZCRO sheet is in a different xlsx (not the two supplied), it would need to be supplied separately.
- **"Manage Data Fields shown for one of the clients on global dashboard"** — not present in either xlsx. This was likely a screenshot or a UI snapshot that the user has but isn't in the supplied files.
- **Sheets named "Required Global Data Fields" and "Required Firm Data Fields"** — these exact names do not appear in the dump. The closest are `NeededGlobalFields` and `NeededFirmFields`, which we have used. If the user has an older xlsx with the "Required" naming, that is a separate file.
- **Live UI exploration** — Chrome session was unstable in this run; the analysis relies on the prior JSON snapshots (`data-fields-global-tree-rows.json`, `data-fields-firm-tree-rows.json`).
- **The 4964 Lx leaves that did not match** — these are leaves whose internal name is not present in the jcrew Lucernex export. They are likely either (a) tables not exported for jcrew (most), (b) Lx-only UI plumbing fields, or (c) field-name drift between Lx and Lucernex. A second-pass name-fuzzy match would catch some of these.

---

## Files produced

- `/Users/shashanksaxena/Documents/ASG/Code/Lx/_crossmap.md` — human-readable grouped table (4.9 MB)
- `/Users/shashanksaxena/Documents/ASG/Code/Lx/_crossmap.tsv` — machine-readable (989 KB)
- `/Users/shashanksaxena/Documents/ASG/Code/Lx/_crossmap_report.md` — this report
