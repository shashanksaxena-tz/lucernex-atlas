# Equipment Contracts — the fifth root, and the lease engine without the real estate

**Stated up front.** `Equipment Contract` is a fifth top-level navigation root, present in
`(ASG)BBW` and absent in `(ASG)American Freight`. It is **`Contract` with the retail-property layers
subtracted**: 26 screens against Contract's 39, and every one of those 26 except two is the same
screen, under the same group, with the same name. It keeps the entire ASC 842 / IFRS 16 /
straight-line engine untouched and drops co-tenancy, recoveries/CAM, percentage rent, sales,
invoices, alternate rent and the whole Accrual Info group. The vendor has, in effect, shipped its
own generic-lease / retail-lease split as two navigation roots over one engine.

**It has no table of its own.** Its entity type is `EquipmentContract`, yet neither the 223-object
census nor the 227-table platform inventory contains an `EquipmentContract` table. The discriminator
field `ProjectEntityTypeName` (`Entity Type`) exists on both `ProjectEntity` **and** `Contract`,
which makes storage-in-`Contract` the strong reading — **Inferred, not yet confirmed**; confirming
it needs one record opened, which has been requested.

**Nothing here has been rendered.** Every fact below comes from the navigation tree, the schema
inventory and the Firm record. Not one Equipment Contract screen has been opened in either tenant
([`../../tenants/bbw-vs-american-freight.md`](../../tenants/bbw-vs-american-freight.md) §14). Treat
the screen inventory as a map, not a description.

The screen-count diff and the AF-gating investigation are documented in
[`tenants/bbw-vs-american-freight.md`](../../tenants/bbw-vs-american-freight.md) §2 and §13 and are
**not** restated here. This document adds what that one does not carry: the per-screen
`PageLayoutID` table, the storage analysis, and the rebuild consequences.

---

## The 32 nodes, with ids

**Observed.** [`../../mindmap/navtree-bbw.json`](../../mindmap/navtree-bbw.json). Root
`PageLayoutID 41087`, 5 groups, 26 leaf screens. These ids exist in the same platform-seeded band as
the four shared roots and appear in **neither** tenant's Manage Page Layouts list — so the Equipment
Contract screens are **platform layouts**, not firm layouts (see
[`../page-layouts/`](../page-layouts/#two-populations-of-pagelayoutid)).

**Routes are not captured.** `navtree-bbw.json` carries `jsp: ""` for all 32, and they cannot be
joined from American Freight the way the other 109 nodes were, because AF never renders this root.
Requested from `bbw-tracker`.

| Group | Screen | PageLayoutID | Also under `Contract`? |
|---|---|---:|:--:|
| *(root)* | **Equipment Contract** | `41087` | — |
| **Details** | *(group)* | `41094` | yes |
| Details | Summary | `41095` | yes |
| Details | Members/Contacts | `41128` | yes |
| Details | Forms | `41129` | yes |
| Details | Work Flow | `41130` | yes |
| Details | Documents | `41131` | yes |
| **Abstract Info** | *(group)* | `41090` | yes |
| Abstract Info | Abstract Details | `41091` | yes |
| Abstract Info | Terms | `41117` | yes |
| Abstract Info | Amendments | `41114` | yes |
| Abstract Info | Covenants | `41115` | yes |
| Abstract Info | Key Dates | `41120` | yes |
| Abstract Info | Responsibilities | `41121` | yes |
| Abstract Info | Insurance | `41122` | yes |
| **Payment Info** | *(group)* | `41092` | yes |
| Payment Info | Payment Details | `41093` | yes |
| Payment Info | **Recurring Payments** | `41116` | **renamed** from `Recurring Expenses` |
| Payment Info | Transactions | `41123` | yes |
| Payment Info | Receipts | `41124` | yes |
| Payment Info | Scheduled Offsets | `41125` | yes |
| Payment Info | Allowances | `41126` | yes |
| Payment Info | Security Deposit | `41127` | yes |
| **Accounting Info** | *(group)* | `41118` | yes |
| Accounting Info | Accounting Details | `45607` | yes |
| Accounting Info | Straight-Line Rent | `41153` | yes |
| Accounting Info | Accounting Assumptions | `43781` | yes |
| Accounting Info | ASC 842 Test | `41152` | yes |
| Accounting Info | ASC 842 Rent Schedule | `43782` | yes |
| Accounting Info | IFRS 16 Rent Schedule | `41151` | yes |
| **Reports** | *(group)* | `41119` | yes |
| Reports | **Equipment Contract Reports** | `41154` | **renamed** from `Contract Reports` |

**Derived.** 24 of 26 screens are name-identical to a `Contract` screen; the other 2 are renames.
**Equipment Contract introduces no screen that does not already exist under `Contract`.** It is a
pure subtraction plus two labels.

**Derived.** The id blocks are informative. `41090`–`41131` is one contiguous allocation, `41151`–
`41154` a second, and `43781`/`43782`/`45607` are three later insertions — all three of which are in
`Accounting Info` (`Accounting Assumptions`, `ASC 842 Rent Schedule`, `Accounting Details`).
**Inferred:** the accounting group was extended after the root was first laid out, which is what you
would expect if ASC 842 adoption post-dated the equipment module.

---

## The module, rendered — and it rests on a single record

**Observed.** Four Equipment Contract screens have now been rendered
(`screenshots/bbw-enduser/eq-01-details-summary.jpg` and three more). They are the first
Equipment Contract screens ever opened in this corpus.

> **Standing caveat on everything in this section.** BBW holds **exactly one** equipment contract —
> of 2,008 contracts sampled, **2,007 are `Contract` and 1 is `Equipment Contract`**. These screens
> show **one record's population, not the module's range.** An empty section may be empty for this
> record rather than unused in the module, and that record is barely populated: `Aggregate Payment`
> and `Remaining Payment Obligation` both read `$0.00`, and most date fields are blank.

**Observed**, from Details → Summary:

| Element | Detail |
|---|---|
| Breadcrumb | `EquipmentContract: ASG Equipment Contract` |
| Group tabs | `Details`, `Abstract Info`, `Payment Info`, `Accounting Info`, `Reports` — **five, no `Accrual Info`** |
| Screen tabs | `Summary`, `Members/Contacts`, `Forms`, `Work Flow`, `Documents` — **five, no `Binders` or `Schedule`** |
| Sections | `Equipment Contract Summary`, `General Information`, `Critical Dates`, `Payment Details`, **`Assets`**, `Notes` |
| **Layout selector** | **Absent** |

**Derived.** The tab strip matches the documented subtraction exactly, from the runtime rather than
from the navigation tree — independent confirmation of the diff.

**Derived, and it explains the missing dropdown.** All 32 Equipment Contract nav nodes carry **zero
`PageLayoutField` rows** — they are pure navigation structure, not content layouts. No firm layout
attaches to any of them, so there is no chain to pick from and no selector appears. Contract screens
show one because ASG's layouts attach there
([`../page-layouts/`](../page-layouts/#how-a-chain-renders--answered-a-layout-selector-dropdown)).
**Equipment Contract is rendered entirely by platform defaults.** For the rebuild that is a sharp
statement: ASG has configured nothing here.

### `Asset` is linked through an embedded Equipment grid

**Observed.** The `Assets` section carries an **`Equipment`** grid with columns `Asset Group`,
`Asset Type`, `Name`, `Maintenance Category`, `Contract`, `Asset Serial #`, `Location Details`,
`Operational Status`, **`Is Short Term`**, **`Is Low Asset Value`**. One row: a `Tractor`, asset group
`ASG`, pointing back at `ASG Equipment Contract`.

**Derived.** This answers how `Asset` attaches: **an embedded list on the Summary screen, with the
asset carrying the FK back to the contract.** And the two right-hand columns are the **ASC 842
classification flags** documented on `Asset` in
[`../../modules/assets-equipment/equipment-leases.md`](../../modules/assets-equipment/equipment-leases.md) —
so the classification surface really is per asset, visible here on the contract's own screen.

### Equipment-specific actions

**Observed.** The `Actions` rail carries `Edit`, `Printable View`, **`Add Equipment…`**, `Audit Log`,
**`Generate Paym…`**, `Approve Payme…`, **`Delete Asset Pa…`**, `Extend Contracts`,
**`Extend Asset P…`**, `Save to Docum…`, `Link`.

**Derived.** Three are equipment-specific — `Add Equipment`, `Delete Asset Payments`,
`Extend Asset Payments` — against the retail contract's `Add RE Contract`, `Delete Payments`,
`Alternate Rent Wizard` and `Lease Abstract`. So **the action set is specialised per entity type**,
not merely subtracted. Note `Generate Payments` and `Approve Payments` appear on both: the payment
engine is shared.

**Observed.** `Contract Status` reads `Active`. **No `Lease Status` field appears** — consistent with
`Lease Status` being a retail-lease concern
([`../drop-downs-code-tables/`](../drop-downs-code-tables/)).

## What is dropped, and why it is coherent

**Observed** ([`bbw-vs-american-freight.md`](../../tenants/bbw-vs-american-freight.md) §2), restated
here only as a checklist for the rebuild:

| Dropped | Group | Why *(Derived)* |
|---|---|---|
| `Co-Tenancy` | Abstract Info | A shopping-centre clause |
| `Binders`, `Schedule` | Details | Deal-packaging and capital-project furniture |
| `Recoveries` | Payment Info | Landlord CAM pass-through |
| `Percentage Rent`, `Sales` | Payment Info | Turnover rent |
| `Alternate Rent`, `Invoices` | Payment Info | Retail rent variants and landlord billing |
| **`Accrual Info` — entire group** | — | `Accrual Details`, `Expense Accruals`, `Percentage Rent Accruals`, `Transactions` — all recovery/turnover accounting |
| `Capital Lease Test` | Accounting Info | **Not real-estate-specific — unexplained.** Open question Q-BBW-02 |

**Kept in full:** `Terms`, `Amendments`, `Covenants`, `Key Dates`, `Responsibilities`, `Insurance`,
`Security Deposit`, `Allowances`, `Scheduled Offsets`, `Transactions`, `Receipts`, and all six
`Accounting Info` screens.

**Derived.** The dividing line is exactly *lessee-side generic lease* versus *retail real estate*.
For ASG Edge+ this is the clearest available statement of which contract features are core and which
are retail extensions — and it comes from the vendor's own product decisions rather than from
analysis.

---

## Storage: an entity type with no table

**Observed.** Q-BBW-05 in [`bbw-vs-american-freight.md`](../../tenants/bbw-vs-american-freight.md)
established that the root's `requestedProjectEntityType` is **`EquipmentContract`** — a distinct
`ProjectEntity` type, not `Contract` re-labelled at the navigation layer. The four shared roots
resolve to `Program` / `Location` / `Facility` / `Contract`.

**Observed, and new here.** There is no `EquipmentContract` table anywhere in the inventories:

**Observed.** `Contract` carries **zero fields matching "equip"**, so there is no `IsEquipment`-style
discriminator column either.

| Inventory | Size | Contains `EquipmentContract`? |
|---|---:|:--:|
| 223-object census (`_lucernex_objects_summary.txt`) | 223 objects | **no** |
| Platform sql-table picker ([`bbw-platform-inventory.json`](../../tenants/bbw-platform-inventory.json)) | 227 tables | **no** |
| Refused tables ([`bbw-platform-tables.json`](../../tenants/bbw-platform-tables.json)) | 25 tables | **no** |

The only equipment-named tables in the whole 227 are `Asset` and `Asset History`; the only
contract-named ones are `Contract`, `Contract Amendment`, `Contract Financial Test` and
`Contract Term`. The 227-table picker is the broader of the two inventories — it includes 31 tables
the census omits — so this is not the census's known incompleteness.

**Observed.** `Contract` carries a field `ProjectEntityTypeName` (`Entity Type`, `Text`), the same
field name that `ProjectEntity` carries. `Contract` also carries `ContractClass` (`Contract Class`,
`Text`).

**Observed — confirmed against real records.** Equipment contracts are rows in `Contract`,
discriminated by **`ProjectEntityTypeName`** (Text, UI label `Entity Type`). The stored value is
**`Equipment Contract` — with a space**, not the `EquipmentContract` spelling that the
`requestedProjectEntityType` URL parameter uses. That difference is not cosmetic: a FIQL filter on
`ProjectEntityTypeName==EquipmentContract` returns nothing.

**Observed.** `GET /rest/businessObject/EquipmentContract` **is** a valid REST type and returns 2,017
links — **but they are the same `Contract` records**. It is an **alias/view over `Contract`**, not a
separate store. (`EquipContract` 400s.)

**Derived.** So there are three spellings of one thing — the URL parameter, the stored discriminator
value, and the REST alias — and only the stored value has a space. Any rebuild that keys off a type
name needs one canonical spelling. The alternative — a table the picker hides — is weaker: the picker exposes
227 tables and *names* the 25 it refuses, and `EquipmentContract` is in neither list.
**Not confirmed.** Confirming it needs one record opened and its URL and identifiers read;
requested from `bbw-tracker`.

**Consequence if confirmed *(Derived)*.** The 307-column `Contract` table serves both roots, with
the retail columns simply unused on equipment rows. That is consistent with `Contract` requiring
only 7 of its 307 columns ([`../required-and-validation/`](../required-and-validation/)) — a table
that must accommodate two entity shapes cannot make either shape's fields mandatory.

**Cross-check.** [`modules/assets-equipment/equipment-leases.md`](../../modules/assets-equipment/equipment-leases.md)
established from the FK graph that `ContractFinancialTest`, `SLSummary` and `SLPeriod` each carry a
nullable FK to `Asset` alongside their FK to `Contract`, so the accounting engine can classify and
schedule per asset. An equipment contract stored as a `Contract` row with per-`Asset` schedule rows
fits that shape exactly, with no new machinery.

---

## Why American Freight does not show it

Summarised only; the investigation is [`bbw-vs-american-freight.md`](../../tenants/bbw-vs-american-freight.md) §13.

**Observed.** AF's Firm record carries `Allow Equipment Contracts? = Yes`
([`af-firm-record.json`](../../tenants/af-firm-record.json)) and AF *carries the full Equipment
Contract menu structure* — id `41087`, the same as BBW — and simply does not render it. The `Allow
X?` flags gate 13 of 14 menu structures correctly; this is the sole exception. That lead —
`/en/admin/SecurityPageAccess.jsp` and its `Equipment Contract` row — **has now been followed, across
all 10 user classes, and it does not explain the absence.** See below.

**The shape is platform-seeded, not a BBW customisation.** American Freight carries the complete
`Equipment Contract` menu structure — **id `41087`, 5 groups, 64 nodes** — and its shape matches every
published BBW detail: `Recurring Payments` rather than `Recurring Expenses`, no `Capital Lease Test`,
`Equipment Contract Reports`. **Derived:** the subtraction documented above is **the vendor's own
generic/retail split**, shipped to every tenant, not something ASG configured for BBW.

**The gate is NOT found — and three candidates are now eliminated, not one confirmed.** An earlier
revision of this document argued by elimination that per-user-class page access must be the
suppressor. **That is refuted.** All three hypothesised gates are **open** at American Freight:

| Gate | State at AF |
|---|---|
| 1. Firm entitlement — `Allow Equipment Contracts?` | **Yes** |
| 2. Menu structure — `Manage Top Menu` carries id `41087`, 5 groups, 64 nodes | **Present** |
| 3. Page access — read across **all 10** user classes | **Granted for 8 of 10** |

**Observed.** `Equipment Contract` page access is granted at `Delete` for five classes and `View` for
three, and **in every class that grants `Contract` at all, `Equipment Contract` is granted at the
same level** — the two are indistinguishable in that matrix
([`../../tenants/af-security-page-access.json`](../../tenants/af-security-page-access.json)).

**Derived.** A **fourth, unidentified mechanism** suppresses the root. And it is not specific to
Equipment Contract: `Program` is granted by all 10 classes and **also fails to render as a root**, so
an open page-access grant is demonstrably not sufficient for a root to appear. Full analysis and the
remaining candidates in [`../security-access/`](../security-access/).

**Supporting schema evidence.**

**Derived, and it matters more than the puzzle does.** Entitlement is at least two-layered: a Firm
flag *and* something else. A rebuild that models module entitlement as one boolean per firm will not
reproduce this, and the second layer looks like per-user-class page access — which would make
navigation visibility a **security** concern, not a licensing one. Settle which before designing
either.

---

## What this means for ASG Edge+

| Finding | Consequence |
|---|---|
| Equipment Contract adds no new screen kind | No new page types needed — a contract-shaped aggregate with a narrower screen set |
| The dividing line is generic-lease vs retail | Use it directly as the core/extension boundary for the contract module |
| One engine serves both roots | Do **not** build a second accounting engine for equipment. ASC 842/IFRS 16/SL are shared |
| `Recurring Expenses` → `Recurring Payments` | The same underlying feature under two labels. Label must be per entity type, not global |
| Probably one table with a type discriminator | Decide deliberately: one `contract` table with `entity_type`, or separate tables. Lucernex chose one, and pays for it with 307 columns of which 7 are required |
| Navigation visibility has a second gate beyond the Firm flag | Model entitlement and page-access security separately |
| `Capital Lease Test` dropped for equipment only | If it is the legacy FAS 13 test, ASG Edge+ can omit it for equipment too — confirm (Q-BBW-02) |

---

## Open questions

1. ~~**Does an Equipment Contract row live in `Contract`?**~~ **Answered: yes**, discriminated by
   `ProjectEntityTypeName = 'Equipment Contract'` (with a space). The REST `EquipmentContract` type is
   an alias over the same rows.
2. **What are the 32 JSP routes?** Not captured; not joinable from AF. **Requested.**
3. **What do the screens actually contain?** No Equipment Contract screen has ever been rendered.
   Screenshots of Summary (`41095`), Abstract Details (`41091`), Payment Details (`41093`),
   Accounting Details (`45607`) and ASC 842 Rent Schedule (`43782`) requested.
4. **Q-BBW-02 — why is `Capital Lease Test` dropped but `ASC 842 Test` kept?** The
   generic/specific reading does not explain it. Likely the legacy FAS 13 test; unconfirmed.
5. **Q-BBW-12 — what is the second gate on the root?** `UserClassSecurity.PageLayoutID` is now the
   predicted mechanism (see above). Confirming it needs `/en/admin/SecurityPageAccess.jsp` read with
   a real user class selected.
6. **Which layouts serve these screens?** No BBW firm layout attaches to any Equipment Contract
   navigation node, so the screens must be rendered by platform layouts — which are not listed in
   Manage Page Layouts and whose field content is therefore unreadable by the route used for the 93
   firm layouts. This is the same blind spot described in
   [`../page-layouts/`](../page-layouts/#the-storage-gap).
7. ~~**Is `Asset` linked to an Equipment Contract, and how?**~~ **Answered:** an embedded `Equipment`
   grid on the Summary screen, with the asset pointing back at the contract, and the ASC 842 flags
   `Is Short Term` / `Is Low Asset Value` shown as grid columns.
8. **What does the module look like with real data?** Everything observed rests on **one** record,
   itself barely populated. The range of the module is unknown.
