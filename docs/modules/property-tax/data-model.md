# Property Tax — data model

**Stated up front.** Six objects, 163 fields, all `entity_scoped`, and every one of them carries its
own direct `ParcelID` — not only a pointer to its logical parent in the chain below. The six form a
genuine five-level roll-up under one `Parcel`:

```
Parcel
 └─ PropertyTaxSummary        (the ongoing obligation — rate, recovery routing, billing frequency)
     └─ PropertyTaxAssessment (a dated assessed-value version: land / improvements / other)
         ├─ PropertyTaxBill       (a billing period under this assessed value)
         │    └─ PropertyTaxDetail    (a per-Tax-Type line within one bill — county/city/school)
         └─ PropertyTaxAppeal        (a contest filed against this assessed value)
              └─ PropertyTaxAppealAward   (the financial resolution of one appeal)
```

Source: `_lucernex_objects_summary.txt` (**Observed**, field lists reproduced below), cross-checked
against [`../../mindmap/edges.json`](../../mindmap/edges.json) (**Derived** FK resolution) and, for
every object, a per-entity Data Fields catalog in [`../../data-fields/`](../../data-fields/).

## 1. The object roster

| Object | PG table | Fields | In/Out | Parent in the chain (FK, required) | Notes |
|---|---|---:|---:|---|---|
| `PropertyTaxSummary` | `property_tax_summary` | 32 | 1 / 6 | *(none — the top of the chain)* | Rate, mill rate, billing/payment frequency, and — critically — `CodeRecoveryGroupID`/`CodeRecoveryTypeID`, tying this record directly into the CAM/expense-recovery engine (out of this module, see §4). |
| `PropertyTaxAssessment` | `property_tax_assessment` | 25 | 2 / 6 | `PropertyTaxSummaryID`, required | The assessed value itself — land/improvements/other components, appraisal date/value, market value. |
| `PropertyTaxBill` | `property_tax_bill` | 32 | 3 / 5 | `PropertyTaxAssessmentID`, required | One billing cycle — invoice number/date, early-payment discount terms, equalization factor, `CodePropertyTaxStatusID`. |
| `PropertyTaxDetail` | `property_tax_detail` | 15 | 0 / 5 | `PropertyTaxBillID`, required | **Not** "free-form notes" despite [`../../data-fields/INDEX.md`](../../data-fields/INDEX.md)'s one-line summary — see §2. A structured per-Tax-Type breakdown line, `TaxAmount`/`TaxRate`/`CodeTaxTypeID`. |
| `PropertyTaxAppeal` | `property_tax_appeal` | 41 | 1 / 5 | `PropertyTaxAssessmentID`, required | The largest object in the family. Full workflow in [`appeals.md`](appeals.md). |
| `PropertyTaxAppealAward` | `property_tax_appeal_award` | 18 | 0 / 6 | `PropertyTaxAppealID`, required | The financial outcome of one appeal. |

Required/optional read directly from each entity's Data Fields `Required` column
([`../../data-fields/property-tax-summary.md`](../../data-fields/property-tax-summary.md),
[`property-tax-assessment.md`](../../data-fields/property-tax-assessment.md),
[`property-tax-bill.md`](../../data-fields/property-tax-bill.md),
[`property-tax-appeal.md`](../../data-fields/property-tax-appeal.md),
[`property-tax-appeal-award.md`](../../data-fields/property-tax-appeal-award.md)) — **Observed**.

## 2. `PropertyTaxDetail`'s catalog description is wrong, and worth correcting explicitly

[`../../data-fields/INDEX.md`](../../data-fields/INDEX.md) describes `PropertyTaxDetail` as
*"Free-form notes detail attached to a Parcel's property tax record"* — but its 15-field roster
([`_lucernex_objects_summary.txt`](../../../_lucernex_objects_summary.txt)) is `TaxAmount`
(`sTYPE_MONEY`), `TaxRate` (`sTYPE_PERCENTAGE`), `CodeTaxTypeID` (`sCODE_TAX_TYPE`), `RateFlag`
(boolean), a required `PropertyTaxBillID` and `ParcelID`, plus the usual audit columns and one
genuinely free-form `Notes` field. **This is a structured tax-type breakdown line with its own
amount and rate, not a notes record — `Notes` is one field of fifteen, not the object's purpose.**
Per [`../../CONVENTIONS.md`](../../CONVENTIONS.md)'s evidence discipline: `INDEX.md`'s one-line
summaries are themselves labelled **Inferred** there, generated from field labels without full
per-object review; this is a case where that inference undersells the object, and any document
citing `INDEX.md` for `PropertyTaxDetail` inherits the correction made here, not the original line.
**Derived**, direct field-list read.

## 3. The internal FK graph — 5 edges

**Observed**, resolution `high` ([`../../mindmap/edges.json`](../../mindmap/edges.json)):

| Source.Column | Target | Required? | Meaning |
|---|---|---|---|
| `PropertyTaxAssessment.PropertyTaxSummaryID` | `PropertyTaxSummary` | **Yes** | An assessed-value version belongs to one ongoing tax obligation. |
| `PropertyTaxBill.PropertyTaxAssessmentID` | `PropertyTaxAssessment` | **Yes** | A bill is issued under one specific assessed value. |
| `PropertyTaxDetail.PropertyTaxBillID` | `PropertyTaxBill` | **Yes** | A tax-type breakdown line belongs to one bill. |
| `PropertyTaxAppeal.PropertyTaxAssessmentID` | `PropertyTaxAssessment` | **Yes** | An appeal contests one specific assessed value, not the summary as a whole. |
| `PropertyTaxAppealAward.PropertyTaxAppealID` | `PropertyTaxAppeal` | **Yes** | The financial resolution of one appeal. |

**Every object in the chain also carries its own direct `ParcelID`**, not only the pointer above —
`PropertyTaxSummary`, `PropertyTaxAssessment`, `PropertyTaxBill`, `PropertyTaxDetail`,
`PropertyTaxAppeal`, and `PropertyTaxAppealAward` all repeat the same `ParcelID` FK independently of
their position in the roll-up. **Derived:** this is redundant by the chain (every level could reach
`Parcel` by walking up to `PropertyTaxSummary`), which means either the chain is not always intact in
practice (a `PropertyTaxBill` could theoretically exist with an inconsistent `ParcelID` relative to
its `PropertyTaxAssessmentID`'s own `ParcelID`, since nothing in the schema enforces the two agree),
or the direct column exists purely to make every level independently queryable by Parcel without a
join. Either reading matters for a rebuild: **do not assume the chain and the direct `ParcelID` are
guaranteed consistent; if both are kept, enforce their agreement explicitly.**

## 4. Cross-module edges

### 4.1 Inbound — only one, and it is the significant one

**Observed** ([`../../mindmap/edges.json`](../../mindmap/edges.json)):

| Source object | Source module | Column | Target |
|---|---|---|---|
| `PaymentTransaction` | accounting | `PropertyTaxBillID` | `PropertyTaxBill` |
| `PaymentTransactionFullImport` | accounting | `PropertyTaxBillID` | `PropertyTaxBill` |

**Only `PropertyTaxBill` is reachable from the cash-payment engine — not `PropertyTaxSummary`,
`PropertyTaxAssessment`, `PropertyTaxAppeal`, or `PropertyTaxAppealAward`.** The bill is the sole
actionable, payable unit in this whole family; everything above it (`Summary`, `Assessment`) is
configuration and valuation, and everything beside it (`Appeal`, `AppealAward`) is dispute tracking
that does not itself generate a payment row. `TAX-R-010`.

### 4.2 Outbound

**Observed.** Every object in the family carries the standard audit pair (`CreatedByID`/
`ModifiedByID` → `Member`) and its own `ProjectEntityID` → `ProjectEntity` (the soft, universal
attachment — all six are `entity_scoped`). Beyond that:

| Source.Column | Target | Module | Reading |
|---|---|---|---|
| `PropertyTaxSummary.TaxAuthorityID`, `.VendorID` | `Employer` | people-parties | The taxing authority and (separately) a vendor/tax-service-provider role, both reusing `Employer`. |
| `PropertyTaxSummary.CodeRecoveryGroupID`, `.CodeRecoveryTypeID` | Recovery Group / Recovery Type code tables | — | Ties property tax directly into the CAM/expense-recovery engine — see §5. |
| `PropertyTaxSummary.CodeExpenseGroupID`, `.CodeExpenseTypeID` (also on `PropertyTaxAppeal`) | Expense Group / Expense Type code tables | — | The same GL-routing mechanism [`../accounting/README.md`](../accounting/README.md) documents for `CodeExpenseType` applies to property tax expenses too. |
| `PropertyTaxAssessment.AppraiserID` | `Employer` | people-parties | The independent appraiser, a third `Employer` role alongside taxing authority and vendor. |
| `PropertyTaxAppeal.TaxAttorneyID` | `Person` | people-parties | The individual attorney handling the appeal — distinct from the company-level `Employer` roles elsewhere in the family. |
| `PropertyTaxAppealAward.VendorID` | `Employer` | people-parties | A fourth, separate `Employer` role, on the award record specifically. |
| every object | `Parcel` | facilities-locations | The direct `ParcelID` discussed in §3. |

## 5. Property tax is a recoverable expense — and the tax-code-table naming is easy to confuse

**Observed**, [`../../data-model/code-table-registry.md`](../../data-model/code-table-registry.md):
seven code tables exist for this family, and four of their names differ by only one or two words
from another table in the same family:

| ID | Code table | Used on | Purpose |
|---:|---|---|---|
| 2184 | Property Tax Status Code | `PropertyTaxBill.CodePropertyTaxStatusID` | The **bill's** processing status (e.g. paid/unpaid/hold). |
| 2185 | Property Tax Type Code | `PropertyTaxSummary.CodePropertyTaxTypeID` | The tax obligation's own type classification (real vs. personal property, by inference). |
| 2186 | Tax Appeal Result Code | `PropertyTaxAppeal.CodeTaxAppealResultID` | The **outcome** of a decided appeal. |
| 2187 | Tax Appeal Status Code | `PropertyTaxAppeal.CodeTaxAppealStatusID` | The appeal's own **workflow state** (filed, pending, decided...). |
| 2188 | Tax Paid To Code | `PropertyTaxAppealAward.CodeTaxPaidToID` | Who receives an awarded refund. |
| 2189 | Tax Refund Type Code | `PropertyTaxAppealAward.CodeTaxRefundTypeID` | The mechanism of the refund (check/credit/...). |
| 2190 | Tax Type Code | `PropertyTaxDetail.CodeTaxTypeID` | The specific tax-type breakdown line within a bill (county/city/school, by inference). |

**"Property Tax Status" (2184) vs. "Tax Appeal Status" (2187)** and **"Property Tax Type" (2185) vs.
"Tax Type" (2190)** are four *different* code tables, on four *different* objects, and none of them
values have been captured directly from a live screen in this pass — every reading of "purpose" in
the table above is **Inferred** from the field label and its parent object, not confirmed against an
opened `FirmCodeEdit.jsp?TableType=218x` screen. A rebuild's glossary must keep all four distinct;
collapsing "Property Tax Type" and "Tax Type" into one enum, in particular, would silently merge a
summary-level classification with a bill-line-level one.

That `PropertyTaxSummary` also carries `CodeRecoveryGroupID`/`CodeRecoveryTypeID` — the same code
tables `docs/modules/accounting/README.md` lists as belonging to the (out-of-scope-for-this-pass)
CAM/`ExpenseRecovery` engine — is the module's clearest single fact: **property tax is not a
standalone bill, it is a recoverable operating expense**, routed through the identical
Group/Type-code mechanism every other CAM-recoverable expense uses. Full detail on how that
recovery mechanism works is `docs/modules/accounting/README.md`'s "out of scope but adjacent" list,
not this module's.

## 6. Confidence summary

| Claim | Label |
|---|---|
| The five-level roll-up (`Summary → Assessment → {Bill → Detail, Appeal → Award}`) | **Observed** — required FK chain, `_lucernex_objects_summary.txt` + Data Fields `Required` columns |
| Every object also carries a direct, redundant `ParcelID` | **Observed** (field presence); whether the direct value and the chained value can ever disagree is **Inferred** — no constraint observed either way |
| `PropertyTaxDetail` is a structured tax-type line, not free-form notes | **Derived** — direct field-list read, correcting `INDEX.md`'s inferred summary |
| Only `PropertyTaxBill` is reachable from the payment engine | **Observed** — `edges.json`, exhaustive |
| Property tax routes through the same Expense Type/Recovery Type mechanism as CAM | **Observed** — field presence on `PropertyTaxSummary`/`PropertyTaxAppeal` |
| The seven code tables' individual purposes (status vs. status, type vs. type) | **Inferred** — field label and parent object only; none of the seven has been opened directly |

## Open questions

1. **What are the actual values in the seven property-tax code tables (2184–2190)?** None has been
   opened directly ([`../../data-model/code-table-registry.md`](../../data-model/code-table-registry.md)
   opened four *other* code tables in this pass but not these seven). This would resolve every
   "Inferred" purpose in §5 at once.
2. **Can `PropertyTaxBill.ParcelID` and `PropertyTaxBill.PropertyTaxAssessmentID`'s own `ParcelID`
   ever disagree in a live record?** Nothing in the schema forbids it (§3); no screen was captured
   to check whether the UI enforces agreement.
3. **How does the CAM/expense-recovery engine actually consume `PropertyTaxSummary.CodeRecoveryGroupID`/
   `CodeRecoveryTypeID`?** This module names the connection; `../../modules/accounting/` is where the
   mechanism itself would need to be documented, and it is explicitly out of that module's scope too.
4. Full open-questions list for the appeal workflow specifically: [`appeals.md`](appeals.md).
