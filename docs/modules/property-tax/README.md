# Property Tax — module overview

**Stated up front.** Six objects, 163 fields, all `entity_scoped`, forming one coherent five-level
roll-up under a single `Parcel` — never a `Facility`, never a `Contract` (`TAX-R-007`, corroborating
[`../facilities-locations/location-vs-facility-vs-site.md`](../facilities-locations/location-vs-facility-vs-site.md)'s
own finding that `Parcel` is the sole attachment point for this subsystem):

```
Parcel
 └─ PropertyTaxSummary        the ongoing obligation — rate, recovery routing, billing frequency
     └─ PropertyTaxAssessment a dated assessed-value version: land / improvements / other
         ├─ PropertyTaxBill        a billing period under this assessed value
         │    └─ PropertyTaxDetail     a per-Tax-Type breakdown line within one bill
         └─ PropertyTaxAppeal          a contest filed against this assessed value
              └─ PropertyTaxAppealAward    the financial resolution of that appeal
```

**`PropertyTaxBill` is the only member of this family the cash-payment engine can reach** —
`PaymentTransaction.PropertyTaxBillID` is the sole cross-module inbound edge into the whole family.
Everything above the bill is valuation and configuration; everything beside it (the appeal branch)
is dispute tracking that produces no payment row of its own. And a genuine, non-obvious finding:
**`PropertyTaxSummary` carries `CodeRecoveryGroupID`/`CodeRecoveryTypeID`** — the same code-table
mechanism the CAM/expense-recovery engine uses elsewhere — meaning property tax in this schema is
explicitly modelled as a *recoverable* operating expense, passed through to tenants, not merely a
bill the landlord pays. An **appeal** workflow clearly exists (`PropertyTaxAppeal`, the largest
object in this module at 41 fields, plus `PropertyTaxAppealAward`), but nothing in the object model
connects a won appeal's computed reduction back to an already-issued bill — see
[`appeals.md`](appeals.md)§3, the module's most consequential gap for a rule engine.

*Evidence class for this paragraph: **Observed** FK types and required/optional flags from
`_lucernex_objects_summary.txt` and the per-entity Data Fields catalogs
([`../../data-fields/`](../../data-fields/)); the "recoverable expense" and "appeal doesn't touch
billing" readings are **Derived** from field presence/absence — full argument in
[`data-model.md`](data-model.md) and [`appeals.md`](appeals.md).*

## The module at a glance

| Property | Value |
|---|---|
| Objects | 6 |
| Fields | 163 |
| `entity_scoped` objects | 6 of 6 |
| Internal FK edges | 5 — the roll-up chain in full |
| Inbound cross-module edges | 2, both into `PropertyTaxBill` alone (`PaymentTransaction`, `PaymentTransactionFullImport`) |
| Outbound cross-module edges | 28 — dominated by audit (`Member`), the direct `ParcelID` on every object, and four separate `Employer` roles (taxing authority, appraiser, vendor ×2) |
| Dashboard heading | Cost Management |
| Code tables | 7 — `Property Tax Status` (2184), `Property Tax Type` (2185), `Tax Appeal Result` (2186), `Tax Appeal Status` (2187), `Tax Paid To` (2188), `Tax Refund Type` (2189), `Tax Type` (2190) — see [`data-model.md`](data-model.md#5-property-tax-is-a-recoverable-expense--and-the-tax-code-table-naming-is-easy-to-confuse) for how easily the four similarly-named tables get confused |
| End-user screens | Not in the four-root navigation captured in [003](../../screens/003-main-navigation.md) directly — reached via `Parcel`'s Related Fields/child grids, as `Parcel` itself has no own nav root ([`../facilities-locations/location-vs-facility-vs-site.md`](../facilities-locations/location-vs-facility-vs-site.md) §1) |

## No screen of this module has ever been captured

**Stated plainly, because an absence recorded is worth more than an unrelated illustration.** There
is **no screenshot anywhere in `docs/assets/screenshots/` of any property-tax surface** — no
`Parcel` record, no `PropertyTaxBill`, no assessment, no appeal. A filename sweep for `tax`,
`propert`, `parcel` and `appeal` across all 179 captures returns nothing.

The reason is structural rather than an oversight: **`Parcel` has no navigation root of its own**
(the table above records this), and BBW holds **zero `Parcel` records**
([`../../tenants/bbw-navigation-gate.json`](../../tenants/bbw-navigation-gate.json)), so the root
would not render even if one were sought — it fails the record-existence gate
([`../../features/security-access/`](../../features/security-access/#the-equipment-contract-gate--three-gates-open-root-still-hidden)).
Property tax is reached only through a `Parcel`'s child grids, and there are no Parcels to open.

**Everything in this folder is therefore derived from field inventories and code-table registries,
not from a rendered screen.** That is a real confidence ceiling on the module and should be read
into every claim here. Per-surface status is tracked in
[`../../COVERAGE.md`](../../COVERAGE.md); this module's screens are the largest single block of
unobserved surface in the corpus.

## The roll-up, and the one redundancy worth flagging

Every object also carries its **own** direct `ParcelID`, in addition to its position in the chain
above — `PropertyTaxDetail` can be queried by Parcel without joining up through `Bill →
Assessment → Summary`. Nothing in the schema enforces that this direct value agrees with what the
chain would resolve to; a rebuild that keeps both should enforce their agreement explicitly rather
than assume it. `TAX-R-006`.

## The appeal workflow

Answered in full in [`appeals.md`](appeals.md). In short: an appeal is filed against a specific
`PropertyTaxAssessment` (not the summary as a whole), carries a sequence of candidate assessed
values as it proceeds (`ProposedAssessment` → `CertifiedAssessment`/`RenderedAssessment`/
`ReducedAssessment`/`RevisedAssessmentAmount`), resolves through its own status/result code pair, and
produces a separate `PropertyTaxAppealAward` record with its own payee (`CodeTaxPaidToID`), refund
mechanism (`CodeTaxRefundTypeID`), and processing vendor. **No FK connects either appeal object back
to `PropertyTaxBill`/`PropertyTaxDetail`** — reconciling a won appeal against bills already issued or
paid is not represented in this object model at all.

## What a rebuild must not get wrong

1. **`Parcel` is the sole attachment point — never `Facility`, never `Contract`.** `TAX-R-007`.
2. **`PropertyTaxDetail` is a structured, priced tax-type breakdown line, not a notes field**,
   despite `INDEX.md`'s own inferred one-line summary calling it exactly that. `TAX-R-012`,
   [`data-model.md`](data-model.md#2-propertytaxdetails-catalog-description-is-wrong-and-worth-correcting-explicitly).
3. **Property tax is modelled as a recoverable expense**, via the same `CodeRecoveryGroupID`/
   `CodeRecoveryTypeID` mechanism the CAM engine uses — do not build it as a simple landlord-pays
   bill without checking whether ASG needs the recovery/pass-through path too. `TAX-R-009`.
4. **Only `PropertyTaxBill` connects to the payment engine.** A "what has this parcel paid in
   property tax" report has to start from `PropertyTaxBill`, not `PropertyTaxSummary` or
   `PropertyTaxAssessment`. `TAX-R-010`.
5. **An appeal's outcome does not automatically touch billing.** If ASG's process requires a won
   appeal to credit or adjust an issued bill, that logic must be designed from scratch — Lucernex's
   own schema has no FK for it. `TAX-R-011`.
6. **Four of the seven code tables have easily-confused names** — "Property Tax Status" vs. "Tax
   Appeal Status", "Property Tax Type" vs. "Tax Type" — on four different objects. Keep all four
   distinct in any rebuilt Masters catalog. [`data-model.md`](data-model.md#5-property-tax-is-a-recoverable-expense--and-the-tax-code-table-naming-is-easy-to-confuse).

## Contents

| Document | Answers |
|---|---|
| [`data-model.md`](data-model.md) | Every object, the five-level roll-up chain, the cross-module edges, and the seven code tables' easily-confused names. |
| [`appeals.md`](appeals.md) | The appeal/award workflow, field by field, and why it does not touch billing. |
| [`rules.md`](rules.md) | `TAX-R-001`…`TAX-R-012` — every rule in trigger/input/effect/confidence form. |
| [`asg-edgeplus-mapping.md`](asg-edgeplus-mapping.md) | What exists (nothing), what must be built, what should deliberately differ, and the decisions blocking a build. |

## Open questions

Ranked by how much each blocks a rebuild decision.

1. **What are the values in the seven property-tax code tables (2184–2190)?** None has been opened
   directly; this would resolve every "Inferred" reading of a code table's purpose in
   [`data-model.md`](data-model.md) §5 at once.
2. **Does a won appeal ever automatically adjust or credit an already-issued bill** in the live
   tenant's actual process, even though no FK represents it in the schema? [`appeals.md`](appeals.md).
3. **Can `PropertyTaxBill.ParcelID` and its parent chain's `ParcelID` ever disagree** in a live
   record? Nothing in the schema forbids it.
4. **How does the CAM/expense-recovery engine actually consume
   `PropertyTaxSummary.CodeRecoveryGroupID`/`CodeRecoveryTypeID`?** This module only establishes the
   connection exists; the mechanism itself is `accounting`/CAM's story, not written up there yet
   either.
5. **What distinguishes `PropertyTaxAppeal.AttorneyFee` from `.TaxAttorneyFee`?** [`appeals.md`](appeals.md).
