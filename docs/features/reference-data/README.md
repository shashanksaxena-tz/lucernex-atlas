# Reference data — discount rates, CPI, exchange rates, and the two calendars

**Stated up front.** Five administration tools maintain the reference data the rest of the product
calculates against. Four of the five are **completely empty in `(ASG)BBW)`**, and the fifth holds
**3,683 rows of one US government index**. That distribution is the finding: ASG's tenants run
lease accounting on **a single CPI series and nothing else**.

| Tool | Route | Rows in BBW | Feeds |
|---|---|---:|---|
| Manage CPI Data | `/en/admin/ManageCPIData.jsp` | **3,683** — *identical in AF* | Index-based rent and expense escalations |
| Manage Discount Rates | `/en/admin/ManageDiscountRates.jsp` | **0** — *also 0 in AF* | ASC 842 / IFRS 16 present-value calculation |
| Manage Exchange Rates | `/en/admin/ManageCurrencyRates.jsp` | **0** | Multi-currency contracts |
| Manage Fiscal Calendar | `/en/admin/ManageFiscalPeriod.jsp` | **9 years**, no period detail | Fiscal-period accounting |
| Manage Holiday Calendar | `/en/admin/ManageHolidayCalendar.jsp` | **0** | **Project scheduling — not accounting** |

**The empty discount-rate table is the one to act on.** ASC 842 and IFRS 16 both require a discount
rate to compute the lease liability, both tenants run both, and the table the product provides for
that purpose has **no rows in either tenant**. The rate must therefore be reaching the engine some other way — the
per-record `DiscountRateOverride` on `Asset` and the equivalent on `SLSummary` are the candidates
([`../../modules/accounting/`](../../modules/accounting/)). Confirming which matters, because a
rebuild that implements the rate table and not the override reproduces an engine that cannot
calculate anything.

**Observed** from the admin screenshots, `(ASG)BBW`, build `26.09.0.113`, captured 2026-09-13:
`bbw-admin/` items 24, 25, 26, 31,
32. American Freight equivalents are items 25, 26, 27, 32, 33 in
`af-admin/`. Read-only; nothing was added, edited or deleted.

---

## Manage CPI Data — 3,683 rows, one index

**Observed**
(`bbw-admin/26-manage-cpi-data.jpg`).

| | |
|---|---|
| Columns | `Actions`, **`CPI Index *`**, **`Year *`**, **`Month *`**, **`CPI Value *`**, `Published Date` |
| Filter | A single control — *"With a CPI Index of `<Any>`"* |
| Paging | *"Displaying 1 - 15 of 3683"*, with a **Rows per page** control |
| Action | `Add CPI…` |
| Index observed | **`BLS_CWUR0000SA0`** — the only value present |
| Year range observed | **1932 to 2019** |

![`Manage CPI Data`. The only populated reference table of the five -- 3,683 rows, but the footer reads `Displaying 1 - 15 of 3683`, so the grid is showing one page and the row count comes from the pager, not from what is visible. One index, `BLS_CWUR0000SA0`, across every row on the page.](../../assets/screenshots/bbw-admin/26-manage-cpi-data.jpg)


**Derived.** `BLS_CWUR0000SA0` is the US Bureau of Labor Statistics series for **CPI-W, US city
average, all items, not seasonally adjusted**. Nearly nine decades of monthly values are loaded,
which is far more history than any live lease needs — so this is a **bulk vendor or ASG data load**,
not hand entry. At roughly 12 rows a year for 88 years plus extras, 3,683 is consistent with one
series fully populated.

**Observed, and unexplained.** The 2019 rows show months `3`, `2`, `1` and **`0`**. **Inferred:**
month `0` is an annual or average entry rather than a calendar month. Not confirmed.

**Observed.** All four data columns are required — `CPI Index`, `Year`, `Month` **and `CPI Value`**.
A fifth column, `Published Date`, is not required and reads `12/06/2019` on every row seen.

> An earlier revision of this document recorded `CPI Value` as *not* required and inferred from that
> that the asterisks might mark the composite key rather than mandatory input. **That was wrong** —
> the BBW screenshot is cropped at the right edge and the `*` was simply outside the frame. The
> American Freight capture showed the full grid, with `CPI Value *` asterisked. The
> key-versus-required speculation is withdrawn. *(That AF capture is part of a set being re-taken, so
> it is not linked here.)*

### The same data in both tenants

**Observed.** American Freight's CPI grid is **identical** to BBW's: the same index
`BLS_CWUR0000SA0`, the same **3,683** rows, the same values to five decimal places, and the same
`Published Date` of `12/06/2019` on every row.

**Derived.** Two independently forked tenants do not arrive at 3,683 byte-identical rows by hand.
**CPI data is platform-seeded**, loaded by Accruent and shared, exactly like navigation (109/109
identical), the code-table registry (207/207) and the sql-table catalogue (227/227). It belongs in
the **Hub**, not the Spoke.

**Derived.** The uniform `Published Date` of `12/06/2019` dates the load and explains the 2019
cut-off: the series has not been refreshed in roughly seven years. **Any escalation clause indexed
after 2019 cannot compute from this table.** That is either a training-tenant staleness or a real
operational gap, and it is worth asking ASG which.

**Derived.** A single index means **escalation clauses in these tenants are all US CPI-W**. A rebuild
needs the index to be a first-class dimension — the screen is built for many — but ASG's actual data
needs exactly one.

---

## Manage Discount Rates — the empty table that matters

**Observed**
(`bbw-admin/25-manage-discount-rates.jpg`).
*"No rows to display."*

| | |
|---|---|
| Filter row | `Effective Date`, `Length (In Months)`, `Country`, `State / Province`, `Portfolio`, `Accounting Method`, `Use Type` |
| Columns | `Actions`, **`Effective End Date *`**, **`Length Month (min) *`**, **`Length Month (max) *`**, **`Discount Rate *`**, `Country`, `State / Province`, `Portfolio`, `Accounting Method`, `Use Type` |
| Action | `Add Discount Rate…` |

![`Manage Discount Rates`, empty -- `No rows to display`, `No items to display` in the pager, so this is a genuine zero and not a viewport artefact. The seven-control filter row above the grid is the lookup key in miniature: effective date, lease-length band, country, state, portfolio, accounting method, use type. The ASC 842 engine runs in this tenant against this empty table.](../../assets/screenshots/bbw-admin/25-manage-discount-rates.jpg)


**Derived — the lookup key, read off the columns.** A discount rate is selected by **seven
dimensions**: effective date range, a **lease-length band** (`Length Month min`–`max`), country,
state/province, portfolio, **accounting method**, and **use type**. That is a considerably richer
model than "one rate per tenant":

- The **length band** is the incremental-borrowing-rate curve — a 5-year lease and a 20-year lease
  discount differently, which is exactly what ASC 842 expects.
- **`Accounting Method`** as a dimension means the **same lease can carry different rates under ASC
  842 and IFRS 16** — consistent with [`../../modules/accounting/`](../../modules/accounting/), where
  one engine serves three standards selected by flags on `SLSummary`.
- **Country / state** supports jurisdiction-specific borrowing rates.
- **Portfolio** scoping appears here as it does on code-table values and page layouts.

**Observed.** American Freight's screen is **identical and also empty** — same filter row, same
columns, *"No rows to display"*. Read from AF's admin capture and **independently confirmed by
`team-lead`, who opened the screenshot separately before recording it as §18 of
`tenants/bbw-vs-american-freight.md`**. *(The AF screenshot set is being re-captured as this is
written, so the file is not linked here; the observation has two witnesses.)*

**Derived, and it is the open problem.** **Neither tenant holds a single discount rate**, while both
run ASC 842, IFRS 16 and straight-line schedules. Two tenants agreeing makes the "one tenant happens
to be empty" explanation much weaker. The rate is therefore reaching the engine another way — the
per-record `DiscountRateOverride` on `Asset` and the `SLSummary` equivalent are the candidates — or
no schedule in either tenant has actually been calculated. **Do not conclude the feature is unused**;
what is safe to conclude is that **the seven-dimension lookup is the intended design** and a rebuild
should implement it, while the source of the rate in practice is an open question that blocks the
accounting work.

---

## Manage Exchange Rates — empty

**Observed**
(`bbw-admin/24-manage-exchange-rates.jpg`).
*"No rows to display."*

| | |
|---|---|
| Filter row | `Effective Date`, `From Currency` (All types), `To Currency` (All types), `Exchange Rate Type` (All types) |
| Columns | `Actions`, **`Effective Date *`**, **`From Currency *`**, **`To Currency *`**, **`Exchange Rate *`**, **`Exchange Rate Type *`** |
| Action | `Add Exchange Rate…` |

![`Manage Exchange Rates`, also empty. Every one of the five data columns is asterisked -- a rate row is meaningless without all of them, including `Exchange Rate Type`, which is how the product distinguishes spot from average from closing.](../../assets/screenshots/bbw-admin/24-manage-exchange-rates.jpg)


**Derived.** Every column is required — a rate is meaningless without all five. **`Exchange Rate
Type`** as a required dimension means the product distinguishes rate *kinds* (spot, average,
closing), which is what multi-currency lease accounting needs and what
`ExchangeRate` — 8 fields, *"a point-in-time currency rate captured per Contract"*
([`../../modules/platform-tenancy/data-model.md`](../../modules/platform-tenancy/data-model.md)) —
stores.

**Derived.** Empty, and both tenants are US retail. **Multi-currency is entitled but unused**, which
makes it a safe deferral for ASG Edge+ — with the caveat that `CodeCurrencyTypeID` appears on
`Contract`, `PaymentTransaction` and `ProjectEntity`, so the *columns* are everywhere even though
the rate table is bare.

---

## Manage Fiscal Calendar — retail calendars, and a computed fallback

**Observed**
(`bbw-admin/31-manage-fiscal-calendar.jpg`).
The richest of the five.

**Observed, on-screen text:** *"Computed calendar years will be used for date ranges not defined
below (based on last defined Fiscal Year)."*

![`Manage Fiscal Calendar`. The banner above the grid is the important part: years past the last defined one are computed rather than rejected, so a 20-year lease resolves to periods nobody entered. Note also that the dates render `DD/MM/YYYY` on a US retail tenant.](../../assets/screenshots/bbw-admin/31-manage-fiscal-calendar.jpg)


**Derived.** The calendar **extrapolates**. Years beyond the last defined one are computed from it
rather than erroring — so a contract dated 2035 still resolves to periods. A rebuild needs the same
fallback or it will fail on long leases; a 20-year lease signed today runs past any hand-maintained
calendar.

**Observed.** Scoped by **`<Year>`** and **`Portfolio`**. Nine defined years:

| Year | Begin | End | Periods | Type |
|---|---|---|---:|---|
| 2022 – 2030 | `01/01/YYYY` | `31/12/YYYY` | **12** | **Monthly** |

**Derived.** BBW's fiscal year **is** the calendar year, 12 monthly periods — the simple case. Note
the dates render **`DD/MM/YYYY`**, not US format, on a US retail tenant. Worth flagging for any
import or comparison work.

**Observed.** The `Year Details` grid (`Year`, `Quarter`, `Period`, `Begin Date`, `End Date`,
`Days`, `Weeks`) is **empty** for the selected year — period detail is generated on demand, not
stored up front.

**Observed.** Three **period-generation methods**, each with its own `Create Periods for Year`
button:

| Method | Inputs |
|---|---|
| **Multi-Period Add (equal period length)** | `Year *`, `Total Periods` (default **12**), `Fiscal Year Start *`, `Fiscal Year End *` |
| **Multi-Period Add (by weeks)** | `Year *`, **`Weeks In Quarter *`** — a dropdown defaulting to **`4-4-5`** — `Fiscal Year Start *` |
| **Per-period weeks** | `Year *`, `Fiscal Year Start *`, then **`Weeks each Period: 1 … 13`** — thirteen individual inputs |

**Derived, and this is the substantive finding.** The product supports the **retail fiscal
calendar** properly:

- **`4-4-5`** is the standard retail quarter — two four-week months and one five-week month, so each
  quarter is exactly 13 weeks and comparisons align year on year.
- **Thirteen period slots** means a **13-period (4-week) fiscal year** is supported, the other common
  retail convention.
- Per-period week counts allow a **53-week year**, which retail calendars need every five or six
  years.

**Derived.** `SLPeriod`, `ExpenseSchedule`, `FiscalPeriod` and every "Financial - Fiscal" field group
on `Contract` ([`008`](../../admin/008-manage-page-layouts.md)) hang off this. **ASG Edge+ cannot
treat a fiscal period as a calendar month.** Both tenants happen to use monthly, but the product —
and the retail domain it serves — does not assume it.

**Observed.** Each year row offers **`delete` only, no `edit`**. **Inferred:** a fiscal year is
regenerated rather than amended, which is consistent with periods being created in bulk by the three
buttons.

---

## Manage Holiday Calendar — scheduling, not accounting

**Observed**
(`bbw-admin/32-manage-holiday-calendar.jpg`).
*"No rows to display."* Columns: `Actions`, `Calendar Name`, `Portfolios / Programs`. Action:
`Add Holiday Calendar`.

**Observed, on-screen help:** *"Holiday days are used when determining task completion dates. If a
schedule is not 'crashed' then weekends and holidays will not be used when determining task dates
from lead/lag or duration values."*

> **This corrects an assumption.** `features/administration/` grouped the holiday calendar with
> financial reference data feeding the accounting engine. The product's own help text says it feeds
> **project scheduling** — the `Task` / `TaskPredecessor` critical-path network in
> [`../../modules/projects-capital/scheduling.md`](../../modules/projects-capital/scheduling.md), not
> the lease-accounting engine. Corrected here; the scheduling document did not mention the holiday
> calendar at all, so the fact has been **added** there rather than corrected.

**Derived.** "Crashed" is the project-management term for compressing a schedule by working through
non-working time. So a schedule has a flag controlling whether it respects the working calendar. That
is a real scheduling-engine behaviour and it belongs with capital projects — which are **out of
scope** for ASG Edge+.

**Derived.** Empty in BBW, and capital projects are out of scope. **Safe to skip entirely** — the
one tool of the five that is genuinely not needed.

---

## What these screens also prove about lists

**Observed across all five.** Every one of these screens is the standard list renderer, and together
they are the first direct evidence of its **runtime** behaviour — which
[`../search-filtering/`](../search-filtering/) could previously describe only from configuration:

| Element | Observed |
|---|---|
| **A typed filter row above the grid** | Date pickers, drop-downs defaulting to `All types` / `<Any>`, free-text boxes — per screen, matching that entity's columns |
| **A separate `Search:` box** | Top-right, *"Type to search"* — free text, distinct from the filter row |
| **Paging control** | First / previous / page number / next / last, plus a **refresh** icon |
| **A row count** | *"Displaying 1 - 15 of 3683"*, or *"No items to display"* |
| **A `Rows per page` control** | An editable box, observed showing `15`. Confirms `rowsPerPage` in `JSONConfigText` is a **default**, overridable at runtime |
| **An `Add <Thing>…` button** | Bottom-right of the grid |
| **Required markers on column headers** | **Red text with a trailing `*` on list column headers**, not only on form fields |

**Derived, and it matters for required-ness.** The red asterisk appears on **list column headers** —
`Effective End Date *`, `CPI Index *`, `From Currency *`. So whatever drives it is **not specific to
edit layouts**; it applies wherever a field is placed. That is consistent with the storage being on
the placement record (`PageLayoutField`), and it rules out any explanation that only covers detail
forms. See [`../required-and-validation/`](../required-and-validation/).

---

## What this means for ASG Edge+

| Finding | Consequence |
|---|---|
| Discount rates keyed by 7 dimensions incl. **length band** and **accounting method** | Implement the full lookup. A single tenant-wide rate will not serve ASC 842 |
| The discount-rate table is **empty** while the engine runs | Find where the rate actually comes from before building either path |
| One CPI index, 3,683 rows, 1932–2019 | Index must be a dimension; ASG needs exactly one series loaded |
| Fiscal calendar supports **4-4-5**, **13 periods** and 53-week years | A fiscal period is **not** a calendar month. Do not hard-code monthly |
| Fiscal years **extrapolate** beyond the last defined one | Long leases need the fallback, or they fail on dates past the calendar |
| Exchange rates empty; `Exchange Rate Type` required | Multi-currency is deferrable, but the currency columns exist everywhere |
| Holiday calendar is **scheduling**, not accounting | Out of scope with capital projects |
| Red required markers appear on **list** columns | Required-ness is a placement property, not a form property |

---

## Open questions

1. **Where does the ASC 842 discount rate actually come from**, given `DiscountRate` has no rows?
   `Asset.DiscountRateOverride` and the `SLSummary` equivalent are the candidates. **Highest
   priority** — it blocks the accounting rebuild.
2. **What is CPI month `0`?** Observed on the 2019 rows in both tenants. Probably an annual or
   average figure; unconfirmed.
3. **Why does the CPI series stop at 2019**, with a `Published Date` of `12/06/2019` on every row?
   Stale training data, or a real gap that would break any post-2019 index escalation?
4. **What are the `Accounting Method` and `Use Type` vocabularies** on the discount-rate screen? Both
   are drop-downs; neither appears by those names among the 207 firm code tables.
5. ~~**Does American Freight hold the same data?**~~ **Answered.** AF's discount-rate table is also
   empty, and its CPI data is identical to BBW's — same index, same 3,683 rows, same published date.
   AF's exchange-rate, fiscal-calendar and holiday-calendar screens have not been read. **Re-link the
   AF screenshots once the in-progress re-capture lands**; the observations stand on the BBW captures
   plus `team-lead`'s independent read.
6. **What does `Weeks In Quarter` offer besides `4-4-5`?** Only the default was visible. `4-5-4` and
   `5-4-4` are the other standard retail patterns.
7. **Has any fiscal `Year Details` ever been generated?** The detail grid was empty for the selected
   year, so period rows may not exist at all — in which case fiscal-period accounting is configured
   but unexercised.
