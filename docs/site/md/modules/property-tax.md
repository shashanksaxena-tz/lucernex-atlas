# Property Tax

*In scope for the rebuild*

Assessment, bill, appeal and award tracking for real-property tax.

Stated up front. Six objects, 163 fields, all entity_scoped, forming one coherent five-level roll-up under a single Parcel — never a Facility, never a Contract (TAX-R-007, corroborating ../facilities-locations/location-vs-facility-vs-site.md's own finding that Parcel is the sole attachment point for this subsystem):

|  | Count |
|---|---|
| Record types | 6 |
| Fields | 163 |
| Keys in | 2 |
| Keys out | 28 |
| Rules | 12 |

## Record types

| Record type | Postgres table | Fields | Referenced by |
|---|---|---|---|
| [PropertyTaxAppeal](../entities/PropertyTaxAppeal.md) | `property_tax_appeal` | 41 | 1 |
| [PropertyTaxBill](../entities/PropertyTaxBill.md) | `property_tax_bill` | 32 | 3 |
| [PropertyTaxSummary](../entities/PropertyTaxSummary.md) | `property_tax_summary` | 32 | 1 |
| [PropertyTaxAssessment](../entities/PropertyTaxAssessment.md) | `property_tax_assessment` | 25 | 2 |
| [PropertyTaxAppealAward](../entities/PropertyTaxAppealAward.md) | `property_tax_appeal_award` | 18 | 0 |
| [PropertyTaxDetail](../entities/PropertyTaxDetail.md) | `property_tax_detail` | 15 | 0 |

## Rules

| Rule | Subject | What it requires | Confidence |
|---|---|---|---|
| [TAX-R-001](../rules/TAX-R-001.md) | A PropertyTaxAssessment must belong to exactly one PropertyTaxSummary | Trigger: Assessment create/save. Input: `PropertyTaxAssessment.PropertyTaxSummaryID`. | Observed |
| [TAX-R-002](../rules/TAX-R-002.md) | A PropertyTaxBill must belong to exactly one PropertyTaxAssessment | Input: `PropertyTaxBill.PropertyTaxAssessmentID`. Effect: A bill is always issued against a specific assessed value, never against the summary directly. | Observed |
| [TAX-R-003](../rules/TAX-R-003.md) | A PropertyTaxDetail must belong to exactly one PropertyTaxBill | Input: `PropertyTaxDetail.PropertyTaxBillID`. Effect: Each tax-type breakdown line is scoped to one billing cycle. | Observed |
| [TAX-R-004](../rules/TAX-R-004.md) | A PropertyTaxAppeal must belong to exactly one PropertyTaxAssessment | Input: `PropertyTaxAppeal.PropertyTaxAssessmentID`. Effect: An appeal always contests one specific dated assessed value, never the ongoing Summary as a whole. | Observed |
| [TAX-R-005](../rules/TAX-R-005.md) | A PropertyTaxAppealAward must belong to exactly one PropertyTaxAppeal | Input: `PropertyTaxAppealAward.PropertyTaxAppealID`. Confidence: Observed (`../../data-fields/property-tax-appeal-award.md`). | Observed |
| [TAX-R-006](../rules/TAX-R-006.md) | Every object in the family also carries a direct Parcel pointer, independent of the chain | Input: `ParcelID` on all six objects, `Required = Yes` on each. Effect: Every level is independently queryable by Parcel without walking the roll-up chain to `PropertyTaxSummary`; | Observed |
| [TAX-R-007](../rules/TAX-R-007.md) | Property tax attaches only to Parcel, never Facility or Contract | Input: No object in this family carries a `FacilityID` or `ContractID`. Effect: Corroborates `FAC-R-014` in `../facilities-locations/rules.md` from this module's own side — the taxable unit is the lan | Observed |
| [TAX-R-008](../rules/TAX-R-008.md) | Property tax expenses route through the same Expense Type/Group mechanism as any other recoverable expense | Input: `PropertyTaxSummary.CodeExpenseGroupID`/`.CodeExpenseTypeID`, `PropertyTaxAppeal.CodeExpenseGroupID`/`.CodeExpenseTypeID`. Effect: Selecting an expense type/group on a property-tax record is a  | Observed |
| [TAX-R-009](../rules/TAX-R-009.md) | Property tax is explicitly a recoverable (CAM) expense, not merely an expense | Input: `PropertyTaxSummary.CodeRecoveryGroupID`/`.CodeRecoveryTypeID`. Effect: Ties this module directly into the CAM/expense-recovery engine (`../accounting/README.md`'s "out of scope but adjacent" l | Observed |
| [TAX-R-010](../rules/TAX-R-010.md) | Only PropertyTaxBill, not Summary/Assessment/Appeal/Award, is reachable from the cash-payment engine | Input: `PaymentTransaction.PropertyTaxBillID` / `PaymentTransactionFullImport.PropertyTaxBillID` — the family's only cross-module inbound edges. Effect: The bill is the sole payable, actionable unit i | Observed |
| [TAX-R-011](../rules/TAX-R-011.md) | An appeal's outcome does not automatically adjust an already-issued bill | Input: No FK from `PropertyTaxAppeal` or `PropertyTaxAppealAward` to `PropertyTaxBill` or `PropertyTaxDetail`. Effect: Reconciling a won appeal's computed reduction (`AssessmentReduction`/`TaxReductio | Derived |
| [TAX-R-012](../rules/TAX-R-012.md) | `PropertyTaxDetail` is a structured, priced breakdown line, not a notes field | Input: `TaxAmount` (`sTYPE_MONEY`), `TaxRate` (`sTYPE_PERCENTAGE`), `CodeTaxTypeID`, `RateFlag` — four substantive fields, plus one genuinely free-form `Notes` field among fifteen total. Effect: A reb | Inferred |
