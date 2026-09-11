# ASG Edge+ mapping

**Stated up front.** ASG Edge+ has **nothing** in this space yet — no property-tax entity of any
kind exists in `ASG-Edgeplus-Configuration-Service` or the legacy monorepo, and the workspace index
(`ASG/Code/CLAUDE.md`) does not mention property tax at all. This module cannot be built before
[`../facilities-locations/`](../facilities-locations/)'s `Parcel` exists — every object here attaches
to `Parcel` alone (`TAX-R-007`) — so it is necessarily a second-wave build, sequenced strictly after
Facilities/Locations.

## 1. What exists today

| ASG Edge+ artefact | What it says | Gap |
|---|---|---|
| `ASG-Edgeplus-Configuration-Service` | No property-tax class or table found | Confirms greenfield |
| Workspace index target architecture | Silent on property tax entirely | No stated Hub/Spoke placement to check the roll-up chain against |
| `Parcel` (this module's prerequisite) | Not yet built either — see [`../facilities-locations/asg-edgeplus-mapping.md`](../facilities-locations/asg-edgeplus-mapping.md) | Build order is fixed: `Location` → `Parcel` → this module |

## 2. What must be built, and in what order

| Lucernex object | ASG Edge+ status | Priority reasoning |
|---|---|---|
| `PropertyTaxSummary` | Must build first | The top of the roll-up; nothing else in the family can exist without it. |
| `PropertyTaxAssessment` | Must build next | Required parent of both `PropertyTaxBill` and `PropertyTaxAppeal` — the fork point of the chain. |
| `PropertyTaxBill` | Must build | The only object in the family the payment engine can reach (`TAX-R-010`) — without it, property tax cannot generate a payable line at all. |
| `PropertyTaxDetail` | Should build alongside Bill | Needed the moment a bill must be broken out by tax type (county/city/school) rather than carried as one lump sum — cheap to add once `PropertyTaxBill` exists. |
| `PropertyTaxAppeal`, `PropertyTaxAppealAward` | Can defer | No dependency runs *from* the billing chain *to* the appeal branch (`TAX-R-011`) — a rebuild can ship billing without appeals and add the appeal branch later without touching what already works. |

## 3. What should deliberately differ

- **Decide, explicitly, whether an appeal outcome must adjust already-issued bills — and if so,
  build the connection Lucernex lacks.** `TAX-R-011` and [`appeals.md`](appeals.md)§3 document a
  real gap: nothing FKs a `PropertyTaxAppeal`/`PropertyTaxAppealAward` back to `PropertyTaxBill`. If
  ASG's process requires reconciling a won appeal against bills already paid, that has to be new
  design, not a port.
- **Do not let a rebuild's `PropertyTaxDetail` equivalent collapse into a notes field.** Lucernex's
  own catalog description undersells it (`TAX-R-012`); the object is a structured, priced tax-type
  breakdown line and should be modelled with real `amount`/`rate`/`tax-type` columns from the start.
- **Decide once whether every level needs its own direct `Parcel` pointer, or only the top of the
  chain does.** Lucernex keeps a redundant `ParcelID` on every object (`TAX-R-006`) with no enforced
  consistency guarantee. A rebuild gains nothing from copying the redundancy unless there is a
  genuine query-performance reason to avoid the join; if it is kept, add the consistency constraint
  Lucernex does not have.
- **Resolve the `AttorneyFee` vs. `TaxAttorneyFee` ambiguity before building the appeal object**,
  rather than carrying two similarly-named, undistinguished fee fields forward.
- **Give the four confusingly-named code-table pairs (`Property Tax Status`/`Tax Appeal Status`,
   `Property Tax Type`/`Tax Type`) unambiguous names in ASG Edge+'s own Masters catalog** — the
  incumbent's naming has already caused enough confusion in this documentation pass alone to be
  worth actively avoiding.

## 4. Decisions blocking a build

1. **Does ASG's property-tax process require appeal outcomes to adjust already-issued bills?** If
   yes, this is new design work, not something Lucernex's schema can be read for.
2. **Does ASG need property tax modelled as a recoverable/CAM-passthrough expense**, matching
   `PropertyTaxSummary.CodeRecoveryGroupID`/`.CodeRecoveryTypeID`, or does it operate this expense as
   a landlord-only cost? This decision should be made jointly with whoever designs the CAM/
   expense-recovery engine, since the mechanism itself belongs there.
3. **Build sequencing is fixed by the FK chain**: `Location` → `Parcel` (facilities-locations) →
   `PropertyTaxSummary` → `PropertyTaxAssessment` → (`PropertyTaxBill` → `PropertyTaxDetail`) and
   (`PropertyTaxAppeal` → `PropertyTaxAppealAward`). No object in this module can be built before its
   required parent exists.

## Open questions

Carried forward from the other documents in this folder, ranked by how much each blocks a build
decision.

1. What are the actual values in the seven property-tax code tables (2184–2190)? None has been
   opened directly.
2. Does a won appeal ever get reconciled against issued bills in ASG's actual (non-Lucernex)
   process, independent of whether Lucernex's schema supports it?
3. Does any approved BRD specify a property-tax appeal workflow requirement at all — a business
   question, not checked in this pass?
4. Can `PropertyTaxBill.ParcelID` and its assessment-chain-derived `ParcelID` ever disagree in a live
   Lucernex record, which would inform whether ASG Edge+ needs the same redundant column or can rely
   on the chain alone?
