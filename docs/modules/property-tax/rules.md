# Property Tax — rules

`TAX-R-001` through `TAX-R-012`. Every rule below is derived from the FK graph
([`data-model.md`](data-model.md)) or the Data Fields `Required` column; none is derived from a live
screen capture of this module (no Property Tax screen has been opened — see Open Questions in
[`README.md`](README.md)), so confidence tops out at **Derived** except where noted. Evidence
discipline per [`../../CONVENTIONS.md`](../../CONVENTIONS.md).

---

### TAX-R-001 — A PropertyTaxAssessment must belong to exactly one PropertyTaxSummary
**Trigger:** Assessment create/save. **Input:** `PropertyTaxAssessment.PropertyTaxSummaryID`.
**Effect:** Required FK; save is blocked without a parent Summary. **Confidence:** Observed
(`Required = Yes`, [`../../data-fields/property-tax-assessment.md`](../../data-fields/property-tax-assessment.md)).

### TAX-R-002 — A PropertyTaxBill must belong to exactly one PropertyTaxAssessment
**Input:** `PropertyTaxBill.PropertyTaxAssessmentID`. **Effect:** A bill is always issued against a
specific assessed value, never against the summary directly. **Confidence:** Observed
([`../../data-fields/property-tax-bill.md`](../../data-fields/property-tax-bill.md)).

### TAX-R-003 — A PropertyTaxDetail must belong to exactly one PropertyTaxBill
**Input:** `PropertyTaxDetail.PropertyTaxBillID`. **Effect:** Each tax-type breakdown line is scoped
to one billing cycle. **Confidence:** Observed
([`../../data-fields/property-tax-bill.md`](../../data-fields/property-tax-bill.md) references;
`PropertyTaxDetail`'s own field list, `_lucernex_objects_summary.txt`).

### TAX-R-004 — A PropertyTaxAppeal must belong to exactly one PropertyTaxAssessment
**Input:** `PropertyTaxAppeal.PropertyTaxAssessmentID`. **Effect:** An appeal always contests one
specific dated assessed value, never the ongoing Summary as a whole. **Confidence:** Observed
([`../../data-fields/property-tax-appeal.md`](../../data-fields/property-tax-appeal.md)).

### TAX-R-005 — A PropertyTaxAppealAward must belong to exactly one PropertyTaxAppeal
**Input:** `PropertyTaxAppealAward.PropertyTaxAppealID`. **Confidence:** Observed
([`../../data-fields/property-tax-appeal-award.md`](../../data-fields/property-tax-appeal-award.md)).

### TAX-R-006 — Every object in the family also carries a direct Parcel pointer, independent of the chain
**Input:** `ParcelID` on all six objects, `Required = Yes` on each. **Effect:** Every level is
independently queryable by Parcel without walking the roll-up chain to `PropertyTaxSummary`; nothing
in the schema enforces that this direct value agrees with the `ParcelID` reachable by walking the
chain. **Confidence:** Observed (field presence, all six Data Fields catalogs); the consistency
guarantee is Inferred/unconfirmed — see [`data-model.md`](data-model.md#3-the-internal-fk-graph--5-edges).

### TAX-R-007 — Property tax attaches only to Parcel, never Facility or Contract
**Input:** No object in this family carries a `FacilityID` or `ContractID`. **Effect:** Corroborates
`FAC-R-014` in [`../facilities-locations/rules.md`](../facilities-locations/rules.md) from this
module's own side — the taxable unit is the land parcel, period. **Confidence:** Observed
(exhaustive field-list read).

### TAX-R-008 — Property tax expenses route through the same Expense Type/Group mechanism as any other recoverable expense
**Input:** `PropertyTaxSummary.CodeExpenseGroupID`/`.CodeExpenseTypeID`,
`PropertyTaxAppeal.CodeExpenseGroupID`/`.CodeExpenseTypeID`. **Effect:** Selecting an expense
type/group on a property-tax record is a GL-routing decision, identical in mechanism to
`CodeExpenseType`'s role documented in
[`../../data-model/code-table-registry.md`](../../data-model/code-table-registry.md). **Confidence:**
Observed (field presence).

### TAX-R-009 — Property tax is explicitly a recoverable (CAM) expense, not merely an expense
**Input:** `PropertyTaxSummary.CodeRecoveryGroupID`/`.CodeRecoveryTypeID`. **Effect:** Ties this
module directly into the CAM/expense-recovery engine
([`../accounting/README.md`](../accounting/README.md)'s "out of scope but adjacent" list) — a tax
summary is not just billed, it is (at least potentially) passed through to tenants under a recovery
group/type classification. **Confidence:** Observed (field presence); the recovery mechanism itself
is out of this module's scope to document further.

### TAX-R-010 — Only PropertyTaxBill, not Summary/Assessment/Appeal/Award, is reachable from the cash-payment engine
**Input:** `PaymentTransaction.PropertyTaxBillID` / `PaymentTransactionFullImport.PropertyTaxBillID`
— the family's only cross-module inbound edges. **Effect:** The bill is the sole payable, actionable
unit in this family. **Confidence:** Observed, exhaustive
([`../../mindmap/edges.json`](../../mindmap/edges.json)).

### TAX-R-011 — An appeal's outcome does not automatically adjust an already-issued bill
**Input:** No FK from `PropertyTaxAppeal` or `PropertyTaxAppealAward` to `PropertyTaxBill` or
`PropertyTaxDetail`. **Effect:** Reconciling a won appeal's computed reduction
(`AssessmentReduction`/`TaxReduction`/`NetTaxReduction`) against bills already issued or paid is not
represented anywhere in this object model. **Confidence:** Derived (absence of any such FK,
exhaustive read); see [`appeals.md`](appeals.md)§3.

### TAX-R-012 — `PropertyTaxDetail` is a structured, priced breakdown line, not a notes field
**Input:** `TaxAmount` (`sTYPE_MONEY`), `TaxRate` (`sTYPE_PERCENTAGE`), `CodeTaxTypeID`, `RateFlag`
— four substantive fields, plus one genuinely free-form `Notes` field among fifteen total.
**Effect:** A rebuild that models this object as a notes/comment record (per
[`../../data-fields/INDEX.md`](../../data-fields/INDEX.md)'s inferred one-liner) will lose the
actual per-tax-type amount/rate breakdown a bill is composed of. **Confidence:** Derived, direct
field-list read — see [`data-model.md`](data-model.md#2-propertytaxdetails-catalog-description-is-wrong-and-worth-correcting-explicitly)
for the correction in full.
