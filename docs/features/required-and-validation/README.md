# Required, mandatory, and validation — how Lucernex decides a field must be filled

**Stated up front.** Lucernex has **at least three, probably four, independent sources of
required-ness**, and they are not layered overrides of a single flag — they answer different
questions and a rebuild that collapses them loses obligations.

The two that are easiest to confuse are the physical column's `Required?` and Manage Data Fields'
`Required`. They agree on **5,650 of 5,694 jointly-observable fields (99.2%)** — **but they are not
the same flag**: the other 44 disagree, systematically and **in both directions**, and each direction
is a real obligation the other does not carry. *NOT NULL at storage* and *a user must supply this when
creating the record* are different promises that mostly coincide.

The third — the red `*` painted on fields like `Contract Status` and `Location`, which are required
in **neither** of the first two — is real but its storage is **unresolved**, and the last plausible
candidate is under test. The fourth, the conditional action `Show and Require`, exists in the
vocabulary and is **used zero times** in either tenant.

> **The denominator caveat is now lifted.** An earlier revision of this document withheld its
> agreement figure because the sweep behind it had been captured with `showGlobal=true` — the schema
> viewer's *Global Fields* radio — and so excluded every firm column. **It has been re-swept with
> `showGlobal=false`** and the finding survives intact:
>
> | | Global-only sweep | Re-swept (global **and** firm) |
> |---|---:|---:|
> | Fields | 6,487 | **6,785** |
> | `Contract` columns | 307 | **477** |
> | Agree | 5,452 | **5,650** |
> | Catalogue-Yes / schema-No | 42 | **42** |
> | Schema-Yes / catalogue-No | 2 | **2** |
> | Agreement | *(withheld)* | **99.2%** |
>
> **The 44 disagreements are identical** — the same 34 `ContractID`, 8 `ProjectEntityID` and 2
> `ProjectEntity` audit stamps. And the reason they could never have moved is now itself observed:
> **zero of the 298 firm-scope fields carry `Required`**, which was predicted in advance from
> `all-fields.csv` (none of its 205 firm leaves is `Required=Yes`) and confirmed independently by the
> re-sweep. The global subset also reproduced at exactly 6,487, so nothing drifted between runs.

> **One caveat does still stand. Layer 1 is barely a "required" layer at all.** Of its 603 flags,
> `BOMapClientRecordID` (the import key) accounts for **133**, and the rest are overwhelmingly
> ownership and audit columns. Not one of `Contract`'s seven is a field a user types. Treating it as
> a peer of the other layers overstates it — it is storage plumbing that happens to use the same word.

| Layer | Where it is set | Where it is stored | Scope | Confidence |
|---|---|---|---|---|
| **1. Column** | Not settable — vendor-fixed | The physical table definition, surfaced by `ShowObjectDetails.jsp` as `Required?` | Platform-wide, all tenants | **Observed** |
| **2. Catalog** | Not settable by a firm (read-only in both tenants) | **`ReportGroupAvailableField.IsRequired`** | Per field row, `Global` or `Firm` scope | **Observed** |
| **3. Placement** | Manage Page Layouts | **Unresolved** — `PageLayoutField` has no `IsRequired` column; see [below](#layer-3-the-red-asterisk--real-but-unlocated) | Per layout, per placed field | **Observed** (the effect); **unresolved** (the storage) |
| **4. Conditional** | Manage Page Layouts → Conditional Field Associations | `PageLayoutField.JSONConfigText` → `conditionalFieldsConfig` | Per placement, evaluated at runtime | **Observed** (the mechanism); **used 0 times** |

For the ASG Edge+ rebuild: **required-ness cannot be modelled as one boolean on a field.** It needs
a column constraint, a catalog-level obligation, a per-placement override, and a rule-engine effect —
and the second and third must be allowed to disagree with the first, because in Lucernex they do.

---

## Layers 1 and 2 are two obligations, not one flag

**Observed.** The schema viewer (`/en/admin/ShowObjectDetails.jsp`) reports a `Required?` column for
every field of every table it will expose. Manage Data Fields reports a `Required` column for every
catalog leaf. These were captured independently, from different screens, in different tenants, and
they were joined here field-by-field.

Source: [`../../tenants/bbw-platform-tables.json`](../../tenants/bbw-platform-tables.json) (202
tables, **6,785 fields — global and firm**, `(ASG)BBW`, build `26.09.0.113`) against
[`../../data-fields/all-fields.csv`](../../data-fields/all-fields.csv) (6,158 leaves).
Join key: data-field `Entity` → physical table name, data-field `InternalName` → field name.

| Result | Fields | |
|---|---:|---|
| Joined on both sides | 5,694 | 184 of 214 catalog entities matched a physical table by name |
| **Agree** | **5,650** | **99.2%** |
| Required in the catalog, not in the schema | 42 | see below — all owner foreign keys |
| Required in the schema, not in the catalog | 2 | `ProjectEntity.CreatedByID`, `ProjectEntity.ModifiedByID` |
| Catalog leaf with no matching physical field | 400 | mostly computed/virtual leaves and the 30 entities with no same-named table |

**Derived, and this replaces an earlier reading in this document.** A first pass concluded "the two
layers are one flag with a small override set, so a rebuild needs only one `is_required`". **That is
wrong, and collapsing them would lose 44 obligations.** The disagreements run in *both* directions
and neither set is a subset of the other:

- **42 catalogue-Yes / schema-No** — all owner foreign keys. The application demands a parent; the
  database permits an orphan.
- **2 schema-Yes / catalogue-No** — audit stamps the configuration layer does not expose.

So they are **two distinct obligations that mostly coincide**: `NOT NULL at storage` versus *the user
must supply this when creating the record*. A rebuild needs **both**, and must allow them to
disagree.

### The 42 overrides are all owner foreign keys

**Observed.** The 42 fields required in the catalog but nullable in the schema are exactly two field
names:

| Field | Tables | What it is |
|---|---:|---|
| `ContractID` | 34 | The owning contract on a child of `Contract` |
| `ProjectEntityID` | 8 | The owning entity on a link/child row |

The 34 `ContractID` tables are the contract aggregate itself: `AccrualTransaction`,
`AcctingAssumptionAdjust`, `Allowance`, `AlternateRentSchedule`, `CoTenancy`, `ContractAmendment`,
`ContractFinancialTest`, `ContractTerm`, `Covenant`, `ExpenseAccrualSetup`, `ExpenseAllocation`,
`ExpenseRecovery`, `ExpenseSetup`, `ExpenseVendorAllocation`, `Insurance`, `KeyDate`,
`LandlordInvoice`, `LandlordInvoiceItem`, `Party`, `PaymentReceipt`, `PaymentTransaction`,
`PercentageRent`, `PercentageRentBreakpoint`, `Responsibility`, `SLSummary`, `Sales`,
`SalesExclusion`, `SalesExclusionCap`, `ScheduledOffset`, `SecurityDeposit`, `Usage`,
`UseBasedRent`, `UseBasedRentBreakpoint`, `VariableRentOffset`.

**Derived.** *Parenthood is enforced by the application, not by the database.* Every child of a
contract must name its contract to be saved through the UI, yet the column itself is nullable — so
rows without a parent are physically representable. That is a deliberate choice, and it has a
direct rebuild consequence: an ASG Edge+ schema that makes these columns `NOT NULL` would be
**stricter than Lucernex**, and would reject data that Lucernex will import. Decide that explicitly
rather than inheriting it by accident.

The 2 reverse cases are the audit stamps `CreatedByID`/`ModifiedByID` on `ProjectEntity` — mandatory
in the table, simply not exposed as configurable catalog leaves. Not an override; an omission.

### What is actually required, across the whole schema

**Derived** from [`../../tenants/bbw-platform-tables.json`](../../tenants/bbw-platform-tables.json).

**603 of 6,487 fields (9.3%) carry the column-level required flag** — and the distribution is
extremely skewed:

| Required fields on a table | Tables |
|---:|---:|
| 0 | 32 |
| 1 | 35 |
| 2 | 41 |
| 3 | 40 |
| 4–9 | 46 |
| 10–20 | 8 |

**28 tables have exactly one required field, and it is always the same one.**

| Field | Required in | Note |
|---|---:|---|
| `BOMapClientRecordID` | **133 of 202 tables** | Present in 133 tables and **required in all 133** — never present-and-optional |
| `Inactive` | 18 | The soft-delete flag |
| `ProjectEntityID` | 11 | Entity supertype key |
| `ProjectEntityName` | 9 | |
| `FirmID` | 9 | Tenant key |
| `CreatedByID` | 8 | Audit stamp |
| `ModifiedByID` | 5 | Audit stamp |

**Derived.** Required-ness at the column layer is overwhelmingly *plumbing*, not business rule. The
single most required field in the product is `BOMapClientRecordID`, whose UI labels read
`Contract ClientID`, `Facility ClientID`, `Location ClientID` — an external client-side identifier,
mandatory wherever it exists.

**Inferred (unconfirmed).** `BOMapClientRecordID` is the external key the data importer upserts on.
The `BOMap` prefix, the per-entity `…ClientID` labels, the 256-character text type, and the perfect
present-⇒-required correlation all point that way, but the Import Data screen has not been opened.
This is an open request with `af-tracker`; see [Open questions](#open-questions). **Do not build
against this until it is confirmed** — if true, it is a mandatory column on 133 tables of the ASG
Edge+ schema, which is a large commitment to make on an inference.

**Derived.** Because business-meaningful required-ness is almost absent from layers 1 and 2, *almost
all* of the required-ness a user actually experiences must come from layers 3 and 4. That reframes
the layout system: it is not decoration over a validated schema, it **is** the validation layer.

---

### Layer 2 has a name: `ReportGroupAvailableField.IsRequired`

**Observed.** The catalog flag is not an abstraction — it is a column. `ReportGroupAvailableField`
(RGAF), the single shared field registry
([`../../modules/reporting/report-field-registry.md`](../../modules/reporting/report-field-registry.md)),
carries **`IsRequired (Boolean)`**, **`IsReadOnly (Boolean)`**, `MaxLength`, `DefaultValue`,
`IsGlobal`, `FirmID`, `IsFunctional`, `VersionAdded` and `VersionModified` — the whole Manage Data
Fields surface plus the three extra columns the schema viewer shows. Read from
`_lucernex_objects_summary.txt`; full column mapping in [`../data-fields/`](../data-fields/).

**Derived, and it closes one loop.** `IsFunctional` is the `Functional Field?` column of the schema
viewer, so that column is a **registry** property, not a table property. That narrows open question
4 without answering it: whatever "functional" means, it is decided once per field in the registry,
not per table.

**Derived, and it opens a candidate for layer 3.** RGAF rows carry a `FirmID`. A firm-scoped row
could in principle override a Global field's `IsRequired` without any per-placement storage at all —
which would explain the red asterisk *and* the absence of an `IsRequired` column on
`PageLayoutField`.

**But the data does not support it.** `Contract.CodeContractStatusID` and `Contract.LocationID` are
`Scope = Global`, `Required = No` in `all-fields.csv`, and there is no second, firm-scoped row for
either — all 205 firm-scoped leaves carry the `Firm_` prefix and none of them is a `Contract Status`
or `Location` override. The asterisk was observed on an American Freight layout, and that is
American Freight's catalog. **Recorded as a tested and rejected hypothesis** so it is not proposed
again.

### Read-only is a *grant*, not a field property — and the catalog was not wrong

**Observed.** `Manage Security` → **Field Security** (`/en/admin/SecurityFieldSecurity.jsp`) secures
**6,553 individual field nodes** per user class, on the vocabulary `NoAccess` / `View` / `Edit` /
`Default`. **There is no dedicated `ReadOnly` level** — but **read-only-ness is expressible as
`View`**: a class granted `View` on a field sees it and cannot edit it.

**Derived, and it withdraws an anomaly this document had been treating as one.** The field catalog
reports `ReadOnly = No` on **all 6,158** leaves, which this document previously read as "a catalog
slot the product never fills" and used as evidence that behaviour must live in the layout. **That
reading was wrong.** The two measure different things:

| | Measures | Scope |
|---|---|---|
| Catalog `ReadOnly` | Is this field **inherently** non-editable, for everyone? | The field *definition* |
| Field Security `View` | May **this user class** edit it? | A per-class *grant* |

A field can be universally editable by definition and still be read-only for eight of ten user
classes. **`No` across the board answers a question nobody was asking**, rather than failing to
answer the right one.

**Consequence for the required-ness argument.** The read-only half of the "the catalog carries no
behaviour" claim is withdrawn — read-only-ness has a real, separate home. The **required** half
stands: nothing in Field Security's four-value vocabulary can make a field *mandatory*, only
visible or editable. So required-ness still has no home outside layers 1, 2 and the unlocated 3.

> **Trap worth recording.** The strings `Is ReadOnly?` and `Read Only?` appear on that page, but they
> are the **names of data fields being secured** — alongside `Allow UI Edit?` and `Is Inactive?` —
> not access levels.

**Observed.** `UserClassSecurity` (21 columns) is the storage: `CodeUserClassID`,
`CodeSecurityPrivilegeID`, `SecurityLevelByteValue`, `SecurityLevelName`, `SecurityType`, plus
pointers to `PageLayoutID`, **`ReportGroupAvailableFieldID`**, `ReportGroupDataID` and
`DashboardComponentID`. The census object `Security` has a **byte-identical** column list — the same
duplication pattern already recorded for `Task`/`TaskGroup`/`TaskItem`.

**Derived.** 6,553 securable field nodes against 6,158 catalog leaves is close enough to confirm
Field Security is driven by the same registry `UserClassSecurity` references. Full detail in
[`../security-access/`](../security-access/).

## Layer 3: the red asterisk — real, but unlocated

**Observed.** [`admin/008`](../../admin/008-manage-page-layouts.md) records that in the **layout
editor** for `ASG Contract Summary`, required fields render red with a trailing `*` — e.g.
`Contract Status *`, `Location *`.

**Observed.** Neither field is required in layer 1 or layer 2:

| Field | Column `Required?` | Catalog `Required` |
|---|:--:|:--:|
| `Contract.CodeContractStatusID` (`Contract Status`) | No | No |
| `Contract.LocationID` (`Location`) | No | No |
| `Contract.ContractName` (`Contract Name`) | **Yes** | **Yes** |

`Contract` has only **7** column-required fields and only **3** catalog-required leaves. `Contract
Status` and `Location` are in neither list.

### Is it a fourth layer, or a builder artefact?

**A reframe worth taking seriously before hunting further**, raised by `bbw-tracker`. The asterisks
in `008` were seen in the **layout editor**, not on a rendered end-user form. A `*` in the builder
might mean *"this placement is structurally required for the layout to work"* rather than *"the user
must fill this in"* — in which case there is no fourth layer and the three above are the whole model.

**The end-user check has been run twice now, and it still does not settle it.**

**Observed.** Two rendered end-user screens show **no required marker at all**:

| Screen | Evidence |
|---|---|
| Contract → Details → Summary | `Contract Status` renders `Active` as plain text, no `*` |
| Equipment Contract → Details → Summary | **39 labels, 0 carrying the required class.** `Contract Status`, `Location` **and** `Master Contract` all appear, none asterisked |

That looks decisive, and `bbw-tracker` read it as supporting the reframe — a builder asterisk is not
an end-user required marker, therefore no fourth layer.

**It does not follow yet, and the reason is the same trap twice over.** **Both screens are in view
mode.** Each carries an `Edit` action in its right-hand rail, and **a view-mode page has no reason to
mark anything required** — there is nothing to fill in. An all-plain result is exactly what you would
see whether a fourth layer exists or not.

This is structurally identical to the `98925` `DisplayOption` result: a method validated only against
a case that cannot discriminate. It is the third instance in this project of a test that **fails in
the direction that looks like success** ([`../../CONVENTIONS.md`](../../CONVENTIONS.md)), and worth
naming as such rather than quietly accepting the conclusion.

**The outstanding test is one record opened for EDITING.** Until then the reframe is neither
confirmed nor refuted.

**Counter-evidence that does bear on it.** The asterisk renders **outside the builder**, on ordinary
rendered list screens. Five administration grids show it on **column headers**
([`../reference-data/`](../reference-data/)):

| Screen | Asterisked | Not asterisked |
|---|---|---|
| Manage Discount Rates | `Effective End Date *`, `Length Month (min) *`, `Length Month (max) *`, `Discount Rate *` | `Country`, `State / Province`, `Portfolio`, `Accounting Method`, `Use Type` |
| Manage Exchange Rates | all five data columns | — |
| Manage CPI Data | `CPI Index *`, `Year *`, `Month *`, `CPI Value *` | `Published Date` |

**Derived.** Whatever drives the marker **travels with the placement and renders on a LIST layout in
normal use**. So it is not a builder-only affordance, and no `PForm.jsp`-specific explanation can be
right either. The reframe does not dissolve the question — but `bbw-tracker` is right that the
cleanest confirmation is still to see `Contract Status` on a rendered end-user contract form, and
that check is cheaper than hunting for storage.

### Where it is not

**Observed.** `PageLayoutField` has been recovered in full through REST across 134 layouts
([`../../tenants/bbw-layout-engine-tables.json`](../../tenants/bbw-layout-engine-tables.json)) and
has exactly **20 columns, none named `IsRequired` or `IsReadOnly`**.

Four candidates have now been eliminated:

| # | Candidate | Status |
|---:|---|---|
| 1 | A `Show and Require` conditional rule with an always-true predicate | **Eliminated.** All 50 populated conditional records use `showHide: "show"`; `showAndRequire` is used **0** times |
| 2 | A firm-scoped RGAF row overriding the Global field's `IsRequired` | **Eliminated.** `Contract Status`, `Location` and `Master Contract` are all `Required=No` in `all-fields.csv`; no override row exists |
| 3 | `PageLayoutField.JSONConfigText` | **Eliminated for the test layout.** `98927`'s `JSONConfigText` is `{}` across **all 22** of its placements, and **no key** in the tenant's 29-key vocabulary matches require/mandatory/optional |
| 4 | `DisplayOption1` / `DisplayOption2` | **Last candidate standing — under test.** See below |

**Derived.** Because three of four are gone, **the outstanding test is decisive either way**: if
`DisplayOption` does not carry it, required-ness is not stored in `PageLayoutField` **at all**, and
that is itself a strong positive finding.

### `DisplayOption1` / `DisplayOption2` — a correction and a partial negative

> **Correction.** An earlier revision of this document, and a message I sent, stated these bitmasks
> take "only the values `0` and `288`", and reasoned from `288 = bits 5 and 8`. **That input was
> wrong** — `bbw-tracker` retracted it; it came from a key-union sample rather than from the values.
> The real distinct set on a single layout is `0, 288, 1024, 4112, 4864, 268435456, 268435744`. The
> bit-5-and-8 thread is withdrawn.

**Observed.** The complete deep serialisation of layout **`98925`** (`ASG Contract Abstract Details`,
primary table `Contract`, 28 placements) gives:

| Placement kind | Count | `DisplayOption1` | `DisplayOption2` |
|---|---:|---|---|
| `StaticText` | 9 | `0` | `288` (one variant `268435744`) |
| `SubEditForm` | 8 | `4112` or `4864` | `0` or `1024` |
| `OneToManyList` | 5 | `0` | `0` |
| **ordinary data fields** | **6** | **`0`** | **`0`** — every one |

**Derived.** On this layout `DisplayOption` tracks **placement kind**, not per-field required-ness —
it reads as rendering and structural flags: static-text styling, sub-form embedding behaviour. Every
ordinary data field is all-zero, including three `Firm_*` ones. One exception: an `EmployerID` picker
sets bit 28, which also appears on one `StaticText`, so bit 28 is an independent flag orthogonal to
placement kind.

**This is a partial negative, not an elimination — and the reason matters.** Nobody knows whether
`98925` has *any* asterisked field. A layout with no required fields produces exactly this all-zero
pattern whether the hypothesis is true or false. That is the same trap behind two earlier false
negatives in this project: a method validated only against a case with no data.

**The outstanding test**, and a better target for it:

```
GET /rest/businessObject/PageLayout/lxid/98927?deep=true
```
compare `DisplayOption1` / `DisplayOption2` on the `PageLayoutField` rows labelled `Contract Status`
and `Location` against `Master Contract`.

**Better still, the discount-rate LIST layout.** `98927` offers a 2-against-1 discriminator; Manage
Discount Rates shows a clean **four-asterisked against five-plain** split on one layout, which would
isolate the bit far more confidently for one extra REST call. Requested.

**If both come back all-zero**, the remaining candidates are required-ness attached to the RGAF
definition in a column `all-fields.csv` does not expose, or a layout-level rule stored outside
`PageLayoutField` entirely.

## Layer 4: `Show and Require` — required-ness as a rule outcome

**Observed.** The conditional filter editor offers exactly one action per rule set:
**`Show` | `Show and Require` | `Hide`**, applied when **`all`** or **`any`** of its predicates
match. Full mechanics in
[`modules/layouts-and-forms/conditional-fields.md`](../../modules/layouts-and-forms/conditional-fields.md).

**Derived.** Visibility and required-ness are a *single* administrator decision, not two flags. There
is no "conditional required" feature separate from conditional visibility.

> **Correction.** This document first recorded "854 conditional targets across all 93 layouts, zero
> populated". That holds for the **93 page layouts** and does not generalise: the feature is used on
> the **42 form layouts**, which that sweep never covered. A REST sweep of all **135** layouts finds
> **8 layouts, 50 conditional-field records, 54 criteria clauses**
> ([`../../tenants/bbw-form-layout-sweep.json`](../../tenants/bbw-form-layout-sweep.json)).

**Observed.** The engine is in production use — but **not for required-ness**:

| | |
|---|---:|
| Conditional-field records | **50** |
| Using `showHide: "show"` | **50** |
| Using `showHide: "showAndRequire"` | **0** |
| Using `showHide: "hide"` | **0** |

**Derived.** Conditional *visibility* is live; conditional *required-ness* is configured nowhere in
either tenant. Layer 4 exists in the vocabulary and is unexercised — so it explains none of the red
asterisks, and it is safe to build late. The stored shape is documented in
[`../page-layouts/`](../page-layouts/#conditional-fields--used-and-the-stored-shape-is-now-known).

**Observed, separate mechanism.** A `Conditional Workflow JS` field holds workflow-level rules as
**JavaScript**, distinct from `conditionalFieldsConfig`. Whether it can impose required-ness is
unknown. Recorded in [`tenants/bbw-vs-american-freight.md`](../../tenants/bbw-vs-american-freight.md).

---

## Layer 5: per-placement range validation, which nobody had recorded

**Observed.** `PageLayoutField.JSONConfigText` carries two keys that are validation, plainly:

| Key | Placements using it |
|---|---:|
| `FieldValidationMinValue` | **42** |
| `FieldValidationMaxValue` | **29** |
| `EditModeDefaultValue` | 133 |
| `IncludeInSearch` | 9 |
| `FieldScript` | 67 |

**Derived.** Lucernex supports **per-placement minimum and maximum values** — the same field can be
bounded differently on two layouts — and **per-placement defaults**. Neither is expressible anywhere
in the field catalog, which has no min/max columns at all; RGAF carries only `DefaultValue` and
`MaxLength`.

**Derived, and it settles the architecture question.** The reason required-ness could not be found as
a column is that **per-placement behaviour in Lucernex lives in a JSON blob, not in columns.**
Defaults, range validation, search participation and a JavaScript hook are all already there. A
rebuild should model the placement's behaviour as a typed configuration object from the start, rather
than adding `is_required_override` and `is_readonly_override` as isolated columns and then
discovering it needs min, max, default, search and script as well.

**Observed.** `FieldScript` on 67 placements is a **third** JavaScript escape hatch, alongside
`IsEnabledLxJSCode` on a workflow step action and `Conditional Workflow JS` on a workflow.

## Per-entity comparison

**Derived.** Column-required versus catalog-required for the entities that matter most. The
recurring `1 / 2` pattern on contract children is exactly the override described above:
`BOMapClientRecordID` in the schema, plus `ContractID` added by the catalog.

| Entity | Schema fields | Schema required | Catalog leaves | Catalog required |
|---|---:|---:|---:|---:|
| `Contract` | 307 | 7 | 402 | 3 |
| `Facility` | 125 | 14 | 89 | 12 |
| `Location` | 130 | 8 | 66 | 5 |
| `Program` (Portfolio) | 174 | 8 | 85 | 3 |
| `Member` | 81 | 19 | 78 | 18 |
| `Person` | 37 | 8 | 37 | 8 |
| `Parcel` | 148 | 10 | 74 | 6 |
| `Prototype` | 107 | 15 | 15 | 9 |
| `WorkFlowTemplate` | 25 | 9 | 25 | 9 |
| `WorkFlowTemplateStep` | 56 | 10 | 59 | 10 |
| `Document` | 23 | 7 | 22 | 7 |
| `Space` | 27 | 3 | 26 | 3 |
| `Asset` | 122 | 2 | 126 | 2 |
| `ContractTerm` | 23 | 1 | 29 | 2 |
| `KeyDate` | 32 | 1 | 41 | 2 |
| `Covenant` | 37 | 1 | 45 | 2 |
| `Insurance` | 27 | 1 | 26 | 2 |
| `SecurityDeposit` | 25 | 1 | 25 | 2 |
| `Allowance` | 18 | 1 | 21 | 2 |
| `PaymentTransaction` | 139 | 1 | 118 | 2 |
| `PercentageRent` | 42 | 1 | 44 | 2 |
| `Sales` | 28 | 1 | 27 | 2 |
| `ExpenseSetup` | 94 | 2 | 105 | 4 |
| `ExpenseRecovery` | 559 | 1 | 567 | 2 |
| `SLSummary` | 136 | 2 | 135 | 3 |
| `SLPeriod` | 79 | 4 | 78 | 4 |
| `ContractFinancialTest` | 93 | 1 | 92 | 2 |

**Derived, and worth stating plainly.** `Contract` carries 307 columns and requires 7 of them, none
of which is a business fact — not the status, not the location, not the facility, not a single date
or amount. **Lucernex's data model permits an almost entirely empty contract.** Every meaningful
constraint a user meets lives in the layout.

---

## Adjacent field properties captured alongside `Required?`

**Observed.** The schema viewer returns eight columns per field:
`Field Name | Required? | Type | UI Label | Version Added | Maximum Size | Definition | Functional Field?`.
Four are documented elsewhere; two are worth flagging here.

| Column | What is known |
|---|---|
| `Maximum Size` | Present per field. `BOMapClientRecordID` is 256; ordinary text is commonly 50. The only length-validation evidence in the corpus. |
| `Version Added` | The vendor release that introduced the field (e.g. `7.2`). Useful for dating features; not a validation input. |
| `Functional Field?` | **3,797 true / 2,690 false.** Meaning unknown — see Open questions. |
| `ReadOnly` (catalog only) | **`No` for all 6,158 catalog leaves.** The catalog never marks a field read-only, so read-only-ness — like required-ness — must come from the layout. |

**Derived.** `ReadOnly` being uniformly `No` across the entire catalog is the same finding as the
asterisk, from the other direction: the catalog describes *what a field is*, and the layout decides
*how it behaves*. Any rebuild that puts editability on the field definition will not be able to
express what Lucernex expresses.

---

## What this means for ASG Edge+

| Finding | Consequence for the rebuild |
|---|---|
| Layers 1 and 2 are **two obligations**, not one flag | Build both: a storage constraint *and* a creation-time obligation. Collapsing them loses 44 obligations |
| 42 owner-FK overrides where the catalog is stricter than the column | Model an explicit override, and **decide deliberately** whether owner FKs are `NOT NULL` — Lucernex's are not |
| A layout can require a field the schema does not | `is_required_override` must be a real, nullable column on the placement record — as [`layouts-and-forms/asg-edgeplus-mapping.md`](../../modules/layouts-and-forms/asg-edgeplus-mapping.md) already proposed. This document is the evidence that proposal was right |
| Catalog `ReadOnly` is uniformly `No` — **and that is correct** | Read-only is a per-user-class **grant** (`View` in Field Security), not a field property. Model both: an inherent flag on the definition *and* a grant level |
| `Show / Show and Require / Hide` is one enum | Model `effect enum(SHOW, SHOW_AND_REQUIRE, HIDE)`, not two booleans |
| Conditional fields are **in production** (8 layouts, 50 records) but `showAndRequire` is used **0** times | Conditional *visibility* is required for parity; conditional *required-ness* is not |
| Per-placement min/max/default/search/script all live in one JSON blob | Model placement behaviour as a typed config object, not as isolated override columns |
| `BOMapClientRecordID` required on 133 tables | If it is the import key, it is a mandatory external-identifier column on most of the schema. Confirm before committing |

---

## Open questions

1. **Where is per-placement required-ness stored?** The central question. Three of four candidates
   are eliminated; **`DisplayOption1`/`DisplayOption2` is the last standing**, and the test is
   written above. A null result is itself a strong finding: required-ness would not be stored in
   `PageLayoutField` at all.
2. **Does `Contract Status` render asterisked on a real end-user contract form — in EDIT mode?** The
   view-mode screen has now been captured and shows no asterisk, which proves nothing: view mode
   marks nothing required. Administration *lists* do show the marker outside the builder, which
   argues it is real. **The outstanding test is one record opened for editing.**
3. **Is layout-required enforced or cosmetic?** **This must be answered without mutating data.** The
   static route is to read the client-side validator and its message catalogue off the rendered edit
   page, and check whether the required flag appears in the submit-time validation path or only in
   the render path — the same class of evidence that settled `isReadOnlyRecord` from the grid
   renderer rather than by deleting a value. Capture requested on that basis.
4. ~~**Is `BOMapClientRecordID` the import upsert key?**~~ **Answered — Observed, not inferred.**
   `@clientID` in the REST serialisation **is** `BOMapClientRecordID`, and the route symmetry
   confirms the upsert: `/businessObject/{type}/clientid/{clientID}` is a first-class peer of
   `/lxid/{lxID}`, and `POST …?allowUpdate=true` updates. See
   [`../import-export/`](../import-export/).
5. **What does `Functional Field?` mean?** It is `ReportGroupAvailableField.IsFunctional`, a
   registry-level property — so it is decided once per field, not per table. 3,797 true / 2,690 false. `Notes` is false in 87 tables
   and `Description` in 49, which hints at "participates in business logic vs. free text" — but 18
   tables have *zero* functional fields, which that reading does not explain. Not guessed here.
6. **What does the contract wizard mean by "Required fields are the…"?** The step-one instruction in
   [`../../tenants/bbw-wizards.json`](../../tenants/bbw-wizards.json) is truncated mid-sentence, and
   every one of the 35 captured DOM fields came back `required:false` — so the HTML `required`
   attribute is not the mechanism there either. Capture requested.
7. **Does `Show and Require` on a sub-page target require every field in the section, or only those
   already marked required?** Carried forward unanswered from
   [`conditional-fields.md`](../../modules/layouts-and-forms/conditional-fields.md).
8. ~~**Does `UserClassSecurity` supply the missing read-only mechanism?**~~ **Answered: yes, as
   `View` in Field Security.** The catalog's uniform `ReadOnly = No` is not an error — it answers a
   different question. What remains open is narrower: whether anything in the security model can make
   a field **mandatory**, as opposed to visible or editable. On the observed four-value vocabulary,
   nothing can.
9. **Is required-ness settable per workflow step?** A Form has one layout per workflow step
   ([`forms-vs-pages-vs-layouts.md`](../../modules/layouts-and-forms/forms-vs-pages-vs-layouts.md)),
   so the same field could in principle be required at step 3 and not at step 1. Untested.
