# Property Tax

Out of scope - no approved BRD covers property tax, and ASG does not use this Lx module. Kept in the corpus so the relationship graph stays whole. The product models tax as a roll-up: a summary per parcel, assessments under it, then either a bill (with detail lines) or an appeal (with an award).

## Who it is for

*Derived · fact · source: `docs/features/README.md`*

The property-tax team and the outside consultants who file appeals.

## Assessment roll-up

*Observed · capability · source: `docs/modules/property-tax/README.md`*

Summary, then Assessment, then the branch: the normal path produces bills with detail lines; the contested path produces appeals and awards. All under the parcel the tax attaches to.

## Recoverable expense

*Observed · capability · source: `docs/modules/property-tax/appeals.md`*

Tax is also a recoverable expense: recovery-group and recovery-type references tie tax records into the CAM recovery world - property tax is modelled as something the landlord can pass through, not just a bill someone pays.

## Appeals miss bills

*Derived · capability · source: `docs/modules/property-tax/appeals.md`*

A won appeal never touches an issued bill: the appeal/award workflow documents a gap where an award reducing the tax does not flow back into an already-issued bill. The correction loop is manual, and a rebuild must decide deliberately whether to keep it that way.

## Open questions (16)

*Inferred · group*

16 things nobody has confirmed for this feature. Each one is work somebody has to do before the feature can be rebuilt with confidence; they are carried here rather than resolved by guessing. Click one for the question and the document that raised it.

### What are the values in

*Inferred · question · source: `docs/modules/property-tax/README.md`*

What are the values in the seven property-tax code tables (2184–2190)? None has been opened directly; this would resolve every "Inferred" reading of a code table's purpose in data-model.md §5 at once. Nobody has confirmed this. Recorded in modules/property-tax/README.md, under the Property Tax area. Until it is settled, anything built on the assumption is a guess.

### Does a won appeal ever

*Inferred · question · source: `docs/modules/property-tax/README.md`*

Does a won appeal ever automatically adjust or credit an already-issued bill in the live tenant's actual process, even though no FK represents it in the schema? appeals.md. Nobody has confirmed this. Recorded in modules/property-tax/README.md, under the Property Tax area. Until it is settled, anything built on the assumption is a guess.

### Can PropertyTaxBill

*Inferred · question · source: `docs/modules/property-tax/README.md`*

Can PropertyTaxBill.ParcelID and its parent chain's ParcelID ever disagree in a live record? Nothing in the schema forbids it. Nobody has confirmed this. Recorded in modules/property-tax/README.md, under the Property Tax area. Until it is settled, anything built on the assumption is a guess.

### How does the CAM

*Inferred · question · source: `docs/modules/property-tax/README.md`*

**How does the CAM/expense-recovery engine actually consume PropertyTaxSummary.CodeRecoveryGroupID/CodeRecoveryTypeID?** This module only establishes the connection exists; the mechanism itself is accounting/CAM's story, not written up there yet either. Nobody has confirmed this. Recorded in modules/property-tax/README.md, under the Property Tax area. Until it is settled, anything built on the assumption is a guess.

### What distinguishes

*Inferred · question · source: `docs/modules/property-tax/README.md`*

What distinguishes PropertyTaxAppeal.AttorneyFee from .TaxAttorneyFee? appeals.md. Nobody has confirmed this. Recorded in modules/property-tax/README.md, under the Property Tax area. Until it is settled, anything built on the assumption is a guess.

### What are the values in

*Inferred · question · source: `docs/modules/property-tax/appeals.md`*

What are the values in Tax Appeal Status Code (2187) and Tax Appeal Result Code (2186)? Neither has been opened directly — this would settle the actual workflow states and outcome classifications rather than leaving them inferred from field names. Nobody has confirmed this. Recorded in modules/property-tax/appeals.md, under the Property Tax area. Until it is settled, anything built on the assumption is a guess.

### Does a won appeal ever

*Inferred · question · source: `docs/modules/property-tax/appeals.md`*

Does a won appeal ever automatically adjust or credit an already-issued PropertyTaxBill? (§3) No FK connects them; if ASG's business process requires this, it needs new modelling. Nobody has confirmed this. Recorded in modules/property-tax/appeals.md, under the Property Tax area. Until it is settled, anything built on the assumption is a guess.

### What distinguishes

*Inferred · question · source: `docs/modules/property-tax/appeals.md`*

What distinguishes AttorneyFee from TaxAttorneyFee on the same PropertyTaxAppeal record?. Nobody has confirmed this. Recorded in modules/property-tax/appeals.md, under the Property Tax area. Until it is settled, anything built on the assumption is a guess.

### Can more than one

*Inferred · question · source: `docs/modules/property-tax/appeals.md`*

Can more than one PropertyTaxAppealAward exist for the same PropertyTaxAppeal in a live tenant, or is the relationship 1:1 in practice despite the schema's N:1 shape?. Nobody has confirmed this. Recorded in modules/property-tax/appeals.md, under the Property Tax area. Until it is settled, anything built on the assumption is a guess.

### Is the candidate value

*Inferred · question · source: `docs/modules/property-tax/appeals.md`*

Is the candidate-value sequence (CertifiedAssessment → RenderedAssessment → ReducedAssessment → RevisedAssessmentAmount) **the actual order a live appeal populates them in**, or four independent, situational labels? No screen capture exists to confirm either way. Nobody has confirmed this. Recorded in modules/property-tax/appeals.md, under the Property Tax area. Until it is settled, anything built on the assumption is a guess.

### What are the actual

*Inferred · question · source: `docs/modules/property-tax/asg-edgeplus-mapping.md`*

What are the actual values in the seven property-tax code tables (2184–2190)? None has been opened directly. Nobody has confirmed this. Recorded in modules/property-tax/asg-edgeplus-mapping.md, under the Property Tax area. Until it is settled, anything built on the assumption is a guess.

### Does a won appeal ever

*Inferred · question · source: `docs/modules/property-tax/asg-edgeplus-mapping.md`*

Does a won appeal ever get reconciled against issued bills in ASG's actual (non-Lx) process, independent of whether Lx's schema supports it?. Nobody has confirmed this. Recorded in modules/property-tax/asg-edgeplus-mapping.md, under the Property Tax area. Until it is settled, anything built on the assumption is a guess.

### Does any approved BRD

*Inferred · question · source: `docs/modules/property-tax/asg-edgeplus-mapping.md`*

Does any approved BRD specify a property-tax appeal workflow requirement at all — a business question, not checked in this pass?. Nobody has confirmed this. Recorded in modules/property-tax/asg-edgeplus-mapping.md, under the Property Tax area. Until it is settled, anything built on the assumption is a guess.

### Can PropertyTaxBill

*Inferred · question · source: `docs/modules/property-tax/asg-edgeplus-mapping.md`*

Can PropertyTaxBill.ParcelID and its assessment-chain-derived ParcelID ever disagree in a live Lx record, which would inform whether ASG Edge+ needs the same redundant column or can rely on the chain alone?. Nobody has confirmed this. Recorded in modules/property-tax/asg-edgeplus-mapping.md, under the Property Tax area. Until it is settled, anything built on the assumption is a guess.

### Can PropertyTaxBill

*Inferred · question · source: `docs/modules/property-tax/data-model.md`*

**Can PropertyTaxBill.ParcelID and PropertyTaxBill.PropertyTaxAssessmentID's own ParcelID ever disagree in a live record?** Nothing in the schema forbids it (§3); no screen was captured to check whether the UI enforces agreement. Nobody has confirmed this. Recorded in modules/property-tax/data-model.md, under the Property Tax area. Until it is settled, anything built on the assumption is a guess.

### Full open questions

*Inferred · question · source: `docs/modules/property-tax/data-model.md`*

Full open-questions list for the appeal workflow specifically: appeals.md. Nobody has confirmed this. Recorded in modules/property-tax/data-model.md, under the Property Tax area. Until it is settled, anything built on the assumption is a guess.

## Rules (12)

*Derived · group*

Every numbered rule the docs corpus records for this feature, named by a short summary. Click one: the panel opens with its ID, the full statement, and a link to the complete rule page.

### A — [TAX-R-001](../rules/TAX-R-001.md)

*Observed · rule · source: `docs/modules/property-tax/rules.md`*

**Trigger: Assessment create/save. Input: `PropertyTaxAssessment.PropertyTaxSummaryID`.**

### A PropertyTaxBill — [TAX-R-002](../rules/TAX-R-002.md)

*Observed · rule · source: `docs/modules/property-tax/rules.md`*

**Input: `PropertyTaxBill.PropertyTaxAssessmentID`. Effect: A bill is always issued against a specific assessed value, never against the summary directly.**

### A PropertyTaxDetail — [TAX-R-003](../rules/TAX-R-003.md)

*Observed · rule · source: `docs/modules/property-tax/rules.md`*

**Input: `PropertyTaxDetail.PropertyTaxBillID`. Effect: Each tax-type breakdown line is scoped to one billing cycle.**

### A PropertyTaxAppeal — [TAX-R-004](../rules/TAX-R-004.md)

*Observed · rule · source: `docs/modules/property-tax/rules.md`*

**Input: `PropertyTaxAppeal.PropertyTaxAssessmentID`. Effect: An appeal always contests one specific dated assessed value, never the ongoing Summary as a whole.**

### A — [TAX-R-005](../rules/TAX-R-005.md)

*Observed · rule · source: `docs/modules/property-tax/rules.md`*

**Input: `PropertyTaxAppealAward.PropertyTaxAppealID`. Confidence: Observed (`../../data-fields/property-tax-appeal-award.md`).**

### Every object in the — [TAX-R-006](../rules/TAX-R-006.md)

*Observed · rule · source: `docs/modules/property-tax/rules.md`*

**Input: `ParcelID` on all six objects, `Required = Yes` on each. Effect: Every level is independently queryable by Parcel without walking the roll-up chain to `PropertyTaxSummary`;.**

### Property tax — [TAX-R-007](../rules/TAX-R-007.md)

*Observed · rule · source: `docs/modules/property-tax/rules.md`*

**Input: No object in this family carries a `FacilityID` or `ContractID`. Effect: Corroborates `FAC-R-014` in `../facilities-locations/rules.md` from this module's own side — the taxable unit is the land parcel, period.**

### Property tax — [TAX-R-008](../rules/TAX-R-008.md)

*Observed · rule · source: `docs/modules/property-tax/rules.md`*

**Input: `PropertyTaxSummary.CodeExpenseGroupID`/`.CodeExpenseTypeID`, `PropertyTaxAppeal.CodeExpenseGroupID`/`.CodeExpenseTypeID`. Effect: Selecting an expense type/group on a property-tax record is a GL-routing decision, identical in mechanism to `CodeExpenseType`'s role documented in….**

### Property tax is — [TAX-R-009](../rules/TAX-R-009.md)

*Observed · rule · source: `docs/modules/property-tax/rules.md`*

**Input: `PropertyTaxSummary.CodeRecoveryGroupID`/`.CodeRecoveryTypeID`. Effect: Ties this module directly into the CAM/expense-recovery engine (`../accounting/README.md`'s "out of scope but adjacent" list) — a tax summary is not just billed, it is (at least potentially) passed through to tenants….**

### Only PropertyTaxBill — [TAX-R-010](../rules/TAX-R-010.md)

*Observed · rule · source: `docs/modules/property-tax/rules.md`*

**Input: `PaymentTransaction.PropertyTaxBillID` / `PaymentTransactionFullImport.PropertyTaxBillID` — the family's only cross-module inbound edges. Effect: The bill is the sole payable, actionable unit in this family.**

### An appeal s outcome — [TAX-R-011](../rules/TAX-R-011.md)

*Derived · rule · source: `docs/modules/property-tax/rules.md`*

**Input: No FK from `PropertyTaxAppeal` or `PropertyTaxAppealAward` to `PropertyTaxBill` or `PropertyTaxDetail`. Effect: Reconciling a won appeal's computed reduction (`AssessmentReduction`/`TaxReduction`/`NetTaxReduction`) against bills already issued or paid is not represented anywhere in this….**

### PropertyTaxDetail is — [TAX-R-012](../rules/TAX-R-012.md)

*Inferred · rule · source: `docs/modules/property-tax/rules.md`*

**Input: `TaxAmount` (`sTYPE_MONEY`), `TaxRate` (`sTYPE_PERCENTAGE`), `CodeTaxTypeID`, `RateFlag` — four substantive fields, plus one genuinely free-form `Notes` field among fifteen total. Effect: A rebuild that models this object as a notes/comment record (per `../../data-fields/INDEX.md`'s inferred….**
