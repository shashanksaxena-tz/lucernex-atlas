# CON-R-144 — 12. Contract status and lifecycle

*Contracts & Leases · Observed*

**The tenant needs a lifecycle status: Contract.Firm_LeaseStatus (a Firm-scope custom code field, with a Firm_LeaseStatusNotes companion) is ASG's own answer, sitting in the same Contract Info sub-group as the platform's status field — not to be confused with the platform's own Lease Status Code….**

The tenant needs a lifecycle status: Contract.Firm_LeaseStatus (a Firm-scope custom code field, with a Firm_LeaseStatusNotes companion) is ASG's own answer, sitting in the same Contract Info sub-group as the platform's status field — not to be confused with the platform's own Lease Status Code (2043), which is used by exactly one unrelated object.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | The tenant needs a lifecycle status |
| Stated as | `Contract.Firm_LeaseStatus` (`sTYPE_CUSTOM_CODE_FIELD`, Firm) + `Firm_LeaseStatusNotes` |
| Stated as | ASG added its own contract-status field in the same `Contract / Contract Info` sub-group as the platform's. Do not confuse with `LeaseInfo.CodeLeaseStatusID` (`Lease Status Code` 2043), which is used by exactly one object and that object has no `ContractID` column |
| Stated as | Tenant-authored lifecycle |
| Stated as | Observed |

## What it constrains

[Contract](../entities/Contract.md), [LeaseInfo](../entities/LeaseInfo.md)

Columns named: `Contract.Firm_LeaseStatus`, `LeaseInfo.CodeLeaseStatusID`

---

Source: `docs/modules/contracts/rules.md`
