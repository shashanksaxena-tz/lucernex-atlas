# The property-tax appeal workflow

**Stated up front.** `PropertyTaxAppeal` (41 fields, the largest object in this module) and
`PropertyTaxAppealAward` (18 fields) together model a complete assessment-appeal lifecycle: an
appeal is filed against a specific `PropertyTaxAssessment`, carries a sequence of candidate assessed
values as it proceeds, resolves to a result classification, and — separately — produces a financial
award/refund record with its own payee and mechanism. Nothing in this corpus captures the workflow
running live (no screen for either object has been opened); the lifecycle below is **Derived**
entirely from the field roster, in the order the fields' names imply, per
[`../../CONVENTIONS.md`](../../CONVENTIONS.md)'s evidence discipline. Field-by-field detail:
[`../../data-fields/property-tax-appeal.md`](../../data-fields/property-tax-appeal.md) and
[`property-tax-appeal-award.md`](../../data-fields/property-tax-appeal-award.md).

## 1. The appeal record carries the whole negotiation, not just the outcome

**Observed**, `PropertyTaxAppeal`'s 41 fields. Grouped by what stage of the negotiation each field
plausibly represents:

| Stage | Fields |
|---|---|
| Filing | `AppealFiledDate`, `AppealYear`, `PropertyTaxAssessmentID` (required — the assessment being contested), `ParcelID` |
| Baseline | `PriorAssessment`, `PriorYearAssessment` — the assessed values the appeal starts from |
| The ask | `ProposedAssessment` — what the appellant is requesting |
| Successive candidate values as the case moves | `CertifiedAssessment`, `RenderedAssessment`, `ReducedAssessment`, `RevisedAssessmentAmount` (plus its four components: `RevisedAssessAmtAdjustments`, `RevisedAssessAmtImprovements`, `RevisedAssessmentAmountLand`, `RevisedAssessmentAmountOther`), `RevisedTaxAmount`, `RevisedAdjustmentAmount` |
| When a new value takes effect | `NewAssessmentDate`, `EffectiveDate`, `EndDate` |
| Status and outcome | `CodeTaxAppealStatusID` (the appeal's own workflow state), `CodeTaxAppealResultID` (the final result classification) |
| Computed savings | `AssessmentReduction`, `TaxReduction`, `NetTaxReduction` |
| Cost of pursuing the appeal | `AppraisalFee`, `AttorneyFee`, `TaxAttorneyID` + `TaxAttorneyFee`, `RefundFeeAmount` |
| Expense routing | `CodeExpenseGroupID`, `CodeExpenseTypeID` — the same GL-routing mechanism documented in [`data-model.md`](data-model.md#4-cross-module-edges) |

**Derived reading of the negotiation shape:** `PriorAssessment` is the starting point,
`ProposedAssessment` is what the appellant asked for, and `CertifiedAssessment`/`RenderedAssessment`/
`ReducedAssessment`/`RevisedAssessmentAmount` read as **successive candidate values a taxing
jurisdiction's appeal process typically produces** — a certified value from the assessor, a rendered
value from a hearing, a reduced value if the appeal succeeds, and a final revised figure with its
land/improvements/adjustments/other components broken out identically to `PropertyTaxAssessment`
itself. **No screen or live record confirms this is the actual sequence** rather than four
independently-populated alternative labels for the same concept; see Open Questions.

### 1.1 Two separate attorney-fee fields exist

`AttorneyFee` (no attorney FK attached) and `TaxAttorneyFee` (paired with `TaxAttorneyID`) both
exist on the same record. **Inferred:** the first may be a general/estimated legal-cost figure and
the second the actual fee tied to the specific attorney of record, but nothing distinguishes them
beyond the presence or absence of the paired FK — a genuine ambiguity worth resolving before
building a rule engine around either.

## 2. The award is a separate record, one level down

**Observed**, `PropertyTaxAppealAward`'s 18 fields, required `PropertyTaxAppealID` FK. Its own
fields are materially different in kind from the appeal's:

| Field | Reading |
|---|---|
| `EstimatedAwardDate`, `ActualAwardDate` | The award has its own estimate-then-actual date pair, mirroring the estimate/actual pattern the accounting and workflow modules use elsewhere. |
| `AwardAmount`, `AwardFeeAmount` | The money actually recovered, and a separate fee taken against it. |
| `CodeTaxPaidToID` | Who the award is paid to (Tax Paid To Code, 2188) — the record explicitly separates *who receives the money* from *who negotiated the appeal* (`TaxAttorneyID` lives on `PropertyTaxAppeal`, not here). |
| `CodeTaxRefundTypeID` | The mechanism of the refund (Tax Refund Type Code, 2189) — e.g. a direct refund vs. a credit against a future bill, by inference; not confirmed. |
| `VendorID` | A fourth, separate `Employer` role in this family (alongside `PropertyTaxSummary.TaxAuthorityID`/`.VendorID` and `PropertyTaxAssessment.AppraiserID`) — plausibly the tax-consulting firm that processed the award, distinct from the attorney who argued the case. |

**Derived:** splitting the award into its own object, rather than adding `AwardAmount`/
`ActualAwardDate` columns directly onto `PropertyTaxAppeal`, allows (in principle) more than one
award per appeal — though nothing in the schema states a cardinality, and no live record was
captured to confirm whether a tenant ever actually creates more than one `PropertyTaxAppealAward`
per `PropertyTaxAppeal`.

## 3. What the workflow does *not* touch

**Derived**, by absence: nothing in `PropertyTaxAppeal` or `PropertyTaxAppealAward` points at
`PropertyTaxBill` or `PropertyTaxDetail` directly. The appeal contests the *assessment*
(`PropertyTaxAppeal.PropertyTaxAssessmentID`), and per
[`data-model.md`](data-model.md#41-inbound--only-one-and-it-is-the-significant-one), only
`PropertyTaxBill` is reachable from the cash-payment engine. **This means an appeal in progress does
not, by any FK in this schema, automatically suspend or adjust the bills already issued against the
contested assessment** — reconciling a won appeal's `AssessmentReduction`/`TaxReduction` against
bills already paid appears to be a manual or out-of-schema process. This is the single most
consequential gap for a rebuild's rule engine: if ASG needs the appeal outcome to automatically
correct outstanding or paid bills, that logic has no home in Lucernex's own object model and must be
designed from scratch.

## 4. Confidence summary

| Claim | Label |
|---|---|
| An appeal contests a specific assessed value, not the summary or a bill directly | **Observed** — required FK |
| The appeal negotiation proceeds Prior → Proposed → Certified/Rendered/Reduced/Revised | **Inferred** — field-name ordering only, no screen confirms the actual sequence |
| The award is a separate record from the appeal, allowing (in principle) more than one award per appeal | **Derived** — object separation and FK cardinality; not confirmed against a live record |
| `AttorneyFee` and `TaxAttorneyFee` are genuinely distinct concepts | **Inferred** — no vendor definition or screen distinguishes them |
| Appeal outcomes do not automatically adjust already-issued bills | **Derived** — absence of any FK from `PropertyTaxAppeal`/`PropertyTaxAppealAward` to `PropertyTaxBill`/`PropertyTaxDetail` |

## Open questions

Ranked by how much each blocks a rebuild decision.

1. **What are the values in `Tax Appeal Status Code` (2187) and `Tax Appeal Result Code` (2186)?**
   Neither has been opened directly — this would settle the actual workflow states and outcome
   classifications rather than leaving them inferred from field names.
2. **Does a won appeal ever automatically adjust or credit an already-issued `PropertyTaxBill`?**
   (§3) No FK connects them; if ASG's business process requires this, it needs new modelling.
3. **What distinguishes `AttorneyFee` from `TaxAttorneyFee`** on the same `PropertyTaxAppeal` record?
4. **Can more than one `PropertyTaxAppealAward` exist for the same `PropertyTaxAppeal`** in a live
   tenant, or is the relationship 1:1 in practice despite the schema's N:1 shape?
5. **Is the candidate-value sequence** (`CertifiedAssessment` → `RenderedAssessment` →
   `ReducedAssessment` → `RevisedAssessmentAmount`) **the actual order a live appeal populates them
   in**, or four independent, situational labels? No screen capture exists to confirm either way.
