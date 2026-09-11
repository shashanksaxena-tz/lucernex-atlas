# People & Parties — data model

**Stated up front.** 10 objects, 301 fields, source `_lucernex_objects_summary.txt` parsed by
[`../../mindmap/build_graph.py`](../../mindmap/build_graph.py) (**Derived**, machine-readable in
[`../../mindmap/objects.json`](../../mindmap/objects.json)). Internal edges: 22. Edges leaving the
module: 14. Edges arriving from elsewhere: **309** — the highest inbound total of any module in the
product, driven almost entirely by one object.

## The 10 objects

| Object | Table | Fields | Spine role | In/Out FKs | What it is |
|---|---|---:|---|---:|---|
| `Member` | `member` | 81 | `firm_global` | 290 (columns) / 6 | Internal user/login account — see [`member-vs-person-vs-party.md`](member-vs-person-vs-party.md). |
| `Person` | `person` | 37 | `firm_global` | 0 / 4 | The base individual-contact identity — the supertype `Member`/`NonMember` share a key with. |
| `NonMember` | `non_member` | 37 | `firm_global` | 0 / 4 | Field-for-field identical to `Person` — see the [open question](member-vs-person-vs-party.md#open-questions) on what actually distinguishes it. |
| `Employer` | `employer` | 71 | `firm_global` | 30 / 3 | The vendor/landlord/tenant company record — one table, three business labels. |
| `EmployerSite` | `employer_site` | 20 | `firm_global` | 1 / 2 | A specific branch/site of a multi-location `Employer`. |
| `VendorInsurance` | `vendor_insurance` | 15 | `firm_global` | 0 / 3 | The vendor's actual insurance policy (distinct from `Insurance`, the lease's *required*-coverage terms, in `contracts-leases`). |
| `Party` | `party` | 12 | `entity_scoped` | 0 / 4 | A thin, classified role assignment (company and/or person) tied to a Contract/entity. |
| `LinkProjectEntityContact` | `link_project_entity_contact` | 12 | `entity_scoped` | 0 / 4 | The per-entity contact roster, with a `Landlord_*` variant pair. |
| `LinkProjectEntityVendor` | `link_project_entity_vendor` | 4 | `entity_scoped` | 0 / 2 | The per-entity approved-vendor list. |
| `MemberAudit` | `member_audit` | 12 | `entity_scoped` | 0 / 4 | Login/session audit trail for `Member` — action, date, impersonation tracking. |

## Why 290 foreign keys point at `Member`

**Derived**, exhaustive edge analysis against [`../../mindmap/edges.json`](../../mindmap/edges.json).
290 edges name `Member` as their target, arriving from **162 distinct objects** — i.e. most objects
that reference `Member` do so through more than one column.

| Source column | Edge count | What it is |
|---|---:|---|
| `ModifiedByID` | 161 | The universal "last touched by" audit stamp |
| `CreatedByID` | 79 | The universal "created by" audit stamp (present on fewer objects than `ModifiedByID` — see `../../data-model/object-catalog.md` open question 4) |
| **Audit-pair subtotal** | **240 (83%)** | — |
| `MemberID` | 5 | Direct ownership/assignment (e.g. `LinkMemberProjectEntity`) |
| `Assignee_MemberID`, `*MemberIDList` (Approver/Assignee/Notifiee) | 16 | Workflow routing — `../workflow/routing-and-approvals.md` |
| `CheckedOutByMemberID` | 2 | The workflow/document checkout lock |
| `InitiatedByMemberID`, `SubmitForApprovalByMemberID`, `PriorSubmitByMemberID` | 6 | Workflow instance actors |
| `CurrentStepMemberIDList` | 2 | Current workflow step's resolved actor list |
| `BidAwardByID`, `BidCancelledByID`, `WinningBidMemberIDList` | 3 | Bid-process actors (**out of scope** module, retained here only as FK-graph evidence) |
| `BrokerMemberID`, `Firm_LeaseAnalyst`, `AssignedToMemberIDs`, `MemberIDList` | 4 | Named business-role assignments elsewhere in the schema |
| **Business-identity subtotal** | **50 (17%)** | — |

**The finding, stated plainly:** `Member` is the universal "who did this" anchor for the entire
223-object schema, not primarily a business-domain reference. Five of every six FKs into it are the
generic audit pair every other object carries; only the remaining sixth is a genuine
ownership/routing relationship (workflow actors, checkout locks, and a handful of named business
roles). **This has a direct implication for a rebuild's identity and audit design**: whatever
service owns "who is this user" in ASG Edge+ needs to be reachable from almost every other service's
write path purely for stamping, at a scale disproportionate to `Member`'s actual business role —
which argues strongly for putting the identity/user record in the Hub (as ASG Edge+'s workspace
index already intends) and for the audit-stamp columns being a cross-cutting concern the platform
handles once (a base entity class carrying `createdBy`/`modifiedBy`), not something every aggregate
re-implements. Cross-reference `../platform-tenancy/rules.md#plt-r-012` — the same two-mechanism
audit ambiguity (`AuditColumn` vs. inline stamps) applies to every one of these 240 columns.

By contrast, `ProjectEntity` — the second-most-referenced object at 163 edges from 161 distinct
source objects (**Observed**, `../../data-model/project-entity.md`) — carries almost no audit-stamp
traffic; its in-degree is a business relationship (every entity-scoped child says what it's about),
not a bookkeeping one. The two most-referenced objects in the product are referenced for two
structurally opposite reasons.

## Full field lists — the identity family

Reproduced in full because they are this module's core evidence; see
[`member-vs-person-vs-party.md`](member-vs-person-vs-party.md) for the diff and its conclusions.

### `Person` (37 fields) — identical to `NonMember`

`BOMapClientRecordID`(Text) · `BillRate1`(Currency) · `BillRate2`(Currency) · `City`(Text) ·
`CodeContactTypeIDList`(Dropdown) · `CodeJobFunctionID`(Dropdown) · `CodeJobTitleID`(Dropdown) ·
`CodeJobTitleIDList`(Dropdown) · `CountryID`(Text) · `Description`(Text) · `Designations`(Text) ·
`EMail1`(Text) · `EMail2`(Text) · `EmployerID`(Employer ID) · `Fax`(Text) · `FirstName`(Text) ·
`IStateProvinceCountryID`(Country, State, County ID) · `Inactive`(Boolean) · `JurisdictionID`(County
ID) · `LastName`(Text) · `MiddleName`(Text) · `MobileNumber`(Text) · `ModifiedByID`(Member ID) ·
`ModifiedDate`(Time) · `PersonID`(**Number** — shared key, not an FK) · `Phone`(Text) ·
`PhoneExtension`(Text) · `PostalCode`(Text) · `StreetAddress1..4`(Text) · `Suffix`(Text) ·
`Title`(Text) · `UseEmployerAddress`(Boolean) · `WebSite`(Text) · `WirelessEMail`(Text)

### `Member` (81 fields) — `Person`'s 37, plus these 44

`AcceptEULA`(Boolean) · `AlwaysSpellCheck`(Boolean) · `AnySiteLoginName`(Text) ·
`AnySitePassword`(Text) · `CodeAnalyticsRoleID`(Dropdown) · `CodeApprovalCurrencyTypeID`(Dropdown) ·
`CodeApprovalStatusID`(Dropdown) · `CodeEquipApprovalStatusID`(Dropdown) ·
`CodeLockOutReasonID`(Dropdown) · `CodeUserClassID`(Dropdown) · `ColorScheme`(Text) ·
`ConvertToMember`(Boolean) · `Country`(Text) · `CreatedDate`(Time) · `DatePattern`(Date Format) ·
`EmployerInactive`(Boolean) · `EquipPaymentApprovalMaxAmount`(Currency) ·
`EquipPaymentApprovalMinAmount`(Currency) · `EquipRecurringApprovalMaxAmount`(Currency) ·
`EquipRecurringApprovalMinAmount`(Currency) · `HtmlPersonAddress`(Text) · `IsAdministrator`(Boolean) ·
`IsExemptFromPWDExpiration`(Boolean) · `IsLucernexAdministrator`(Boolean) · `IsMasterMember`(Boolean)
· `IsMasterPerson`(Boolean) · `IsUnassignedWorkFlowApprover`(Boolean) ·
`IsViewPrivateIssueAllowed`(Boolean) · `Language`(Text) · `LastLoginDate`(Time) · `LoginName`(Text) ·
`MemberID`(**Number** — `Member`'s own key) · `MemberNameFirstLast`(Text) · `MemberPhoto`(Text) ·
`NumberPattern`(Number Format) · `Password`(Text) · `PaymentApprovalMaxAmount`(Currency) ·
`PaymentApprovalMinAmount`(Currency) · `PersonNameLastFirst`(Text) ·
`RecurringApprovalMaxAmount`(Currency) · `RecurringApprovalMinAmount`(Currency) ·
`StateProvinceCountryID`(Country, State, County ID) · `SupervisorID`(**Member ID** — self-referencing,
the org chart) · `TimeZone`(Text)

## The company and role objects

### `Employer` (71 fields) — grouped by purpose

| Purpose | Fields |
|---|---|
| Identity | `EmployerID`, `EmployerName`, `NameAKA`, `CompanyType` |
| Banking / AP | `BankAccountNumber`, `BankRoutingNumber`, `APVendorNumber`, `FederalTaxID`, `VendorEarlyPayDays`, `VendorEarlyPayDiscount`, `VendorNetPayDays` |
| Vendor classification flags | `IsVendor`, `IsPreferredVendor`, `IsEquipContractVendor`, `IsREContractVendor`, `CodeVendorGradeID`, `DateGraded` |
| Diversity/ownership flags | `IsFemaleOwned`, `IsGLBTOwned`, `IsMinorityOwned`, `IsSBAProgram`, `IsPrimaryOwner` |
| Capability | `SelfPerform`, `HasAfterHoursSupport`, `NumberOfServiceTrucks`, `NumberOfTechnicians`, `NumberOfStates` |
| Rates | `HourlyRate`, `AfterHoursRate`, `TravelRate` |
| Contact / address | `EMail1/2`, `Phone`, `Fax`, `MobileNumber`, `StreetAddress1..4`, `City`, `PostalCode`, `CountryID` |
| Firm customisation | `Firm_AlternatePayee`, `Firm_EmployerAttention`, `Firm_EmployerCareof`, `Firm_EmployerStoreNumber`, `Firm_PaymentMethod` |
| Document sharing | `IsSharedDocumentAccess` |

### `Party` (12 fields), `LinkProjectEntityContact` (12 fields), `LinkProjectEntityVendor` (4 fields)

Full field tables and the reasoning behind each are in
[`member-vs-person-vs-party.md`](member-vs-person-vs-party.md#party--a-thin-per-contract-role-assignment-not-an-identity-record).
In one line each: `Party` classifies a role on a **Contract**; `LinkProjectEntityContact` rosters
contacts on **any** `ProjectEntity`; `LinkProjectEntityVendor` is the simplest of the three — just
`ProjectEntityID` + `VendorID`, an approved-vendor list with no classification at all.

## Cross-module traffic

| Direction | Module | Edges | What crosses |
|---|---|---|---|
| depends on → | `platform-tenancy` | 13 | `Member.SupervisorID` (org chart), address/geography FKs |
| depends on → | `contracts-leases` | 1 | `Party.ContractID` |
| ← depended on by | `accounting` | 60 | `PaymentTransaction.VendorID`, audit stamps on every accounting object |
| ← depended on by | `projects-capital` | 35 | Task/issue assignment, audit stamps |
| ← depended on by | `workflow` | 34 | Approver/assignee/notifiee routing — `../workflow/routing-and-approvals.md` |
| ← depended on by | `facilities-locations` | 26 | Audit stamps, competitor/complex contacts |
| ← depended on by | `assets-equipment` | 24 | Vendor assignment on work orders |
| ← depended on by | 8 more modules | 4–17 each | Overwhelmingly audit-stamp traffic, per the breakdown above |

Full per-module edge counts: [`../../mindmap/modules.json`](../../mindmap/modules.json) →
`people-parties`. **Derived.**
