# People & Organisation

People, parties and the org chart. The user record is the most-referenced record in the schema - 290 foreign keys point at it, more than at the entity supertype - but 83% of those are just the universal created-by / modified-by audit pair. Person is a second, unnamed supertype.

## Who it is for

*Derived · fact · source: `docs/features/README.md`*

Administrators managing who exists in the system and what they may see. Security is per user class, not per person.

## Person supertype

*Derived · capability · source: `docs/modules/people-parties/member-vs-person-vs-party.md`*

There is a second supertype hiding in the schema: Person and NonMember are field-for-field identical (37 fields, zero differences); Member is Person's 37 plus 44 login and authentication fields. All three share PersonID, typed as a plain number rather than a declared foreign-key type. Same shared-key inheritance pattern the entity supertype uses, applied to people, and nothing names it.

## Geographic routing

*Observed · capability · source: `docs/modules/people-parties/README.md`*

The org chart used for routing is geographic: a supervisor chain exists on the user record, but the workflow's region-1 / region-2 / market routing does not use it - it resolves through the entity's region fields plus the region-manager link table. Two different hierarchies; routing uses the geographic one.

## Region people lists

*Observed · capability · source: `docs/data-model/reading-the-census.md`*

Regions resolve to people through lists: a region carries a self-reference (regions nest), plus manager and member lists pointing at users - this is how a region resolves to actual people for workflow routing.

## Stamps on every write

*Derived · capability · source: `docs/modules/people-parties/README.md`*

Identity sits on nearly every write path: 161 records carry modified-by and 79 carry created-by. Any write anywhere must resolve a user - arguing for one cross-cutting audit-stamp mechanism in the rebuild, not per-service copies.

## Security Access

*Observed · fact · source: `docs/features/security-access/README.md`*

What the security access manual settles: Four securable kinds — pages, 70 action verbs, 6,553 fields, budget columns — on a NoAccess/View/Edit/Delete/Default ladder per user class. Read-only is View on a field, which withdraws an anomaly the corpus had been treating as one. And it refutes the three-gate explanation of the Equipment Contract puzzle: all three gates are open at AF and the root still hides. Biggest open question: What actually suppresses a navigation root — it must explain Program too.

## Manual contents

*Observed · fact · source: `docs/features/security-access/README.md`*

The security access manual is organised as: The Equipment Contract gate — three gates open, root still hidden; Field Security — 6,553 fields, and the read-only answer; Actions — 70 securable verbs; The audit trail — field-level, before and after; What this means for ASG Edge+. Read it rather than this node when you need the detail — this is the index.

## Evidence

*Observed · fact · source: `features/security-access/README.md`*

Written up in features/security-access/README.md. 116 screen captures on disk, under docs/assets/screenshots/bbw-admin, docs/assets/screenshots/af-admin — the screens themselves, not a description of them. First few: 01-manage-company.jpg, 02-manage-schedule-templates.jpg, 03-manage-milestone-timeline.jpg, 04-manage-binder-templates.jpg, 05-manage-forms.jpg, 06-manage-custom-lists.jpg.

![01-manage-company.jpg](../../assets/screenshots/bbw-admin/01-manage-company.jpg)
![02-manage-schedule-templates.jpg](../../assets/screenshots/bbw-admin/02-manage-schedule-templates.jpg)
![03-manage-milestone-timeline.jpg](../../assets/screenshots/bbw-admin/03-manage-milestone-timeline.jpg)
![04-manage-binder-templates.jpg](../../assets/screenshots/bbw-admin/04-manage-binder-templates.jpg)
![05-manage-forms.jpg](../../assets/screenshots/bbw-admin/05-manage-forms.jpg)
![06-manage-custom-lists.jpg](../../assets/screenshots/bbw-admin/06-manage-custom-lists.jpg)
![07-manage-parts-and-inventory.jpg](../../assets/screenshots/bbw-admin/07-manage-parts-and-inventory.jpg)
![08-manage-work-flows.jpg](../../assets/screenshots/bbw-admin/08-manage-work-flows.jpg)
![09-manage-page-layouts.jpg](../../assets/screenshots/bbw-admin/09-manage-page-layouts.jpg)
![10-manage-data-fields.jpg](../../assets/screenshots/bbw-admin/10-manage-data-fields.jpg)
![11-manage-dashboard-reports.jpg](../../assets/screenshots/bbw-admin/11-manage-dashboard-reports.jpg)
![12-import-data.jpg](../../assets/screenshots/bbw-admin/12-import-data.jpg)
![13-import-best-practice-templates.jpg](../../assets/screenshots/bbw-admin/13-import-best-practice-templates.jpg)
![14-export-configuration.jpg](../../assets/screenshots/bbw-admin/14-export-configuration.jpg)
![15-job-log.jpg](../../assets/screenshots/bbw-admin/15-job-log.jpg)
![16-manage-top-menu.jpg](../../assets/screenshots/bbw-admin/16-manage-top-menu.jpg)
![17-manage-firm-dictionary.jpg](../../assets/screenshots/bbw-admin/17-manage-firm-dictionary.jpg)
![18-manage-bid-package-templates.jpg](../../assets/screenshots/bbw-admin/18-manage-bid-package-templates.jpg)
![19-manage-budget-templates.jpg](../../assets/screenshots/bbw-admin/19-manage-budget-templates.jpg)
![20-manage-budget-views.jpg](../../assets/screenshots/bbw-admin/20-manage-budget-views.jpg)
![21-manage-budget-types.jpg](../../assets/screenshots/bbw-admin/21-manage-budget-types.jpg)
![22-manage-budget-summary-page.jpg](../../assets/screenshots/bbw-admin/22-manage-budget-summary-page.jpg)
![23-manage-budget-index-variables.jpg](../../assets/screenshots/bbw-admin/23-manage-budget-index-variables.jpg)
![24-manage-exchange-rates.jpg](../../assets/screenshots/bbw-admin/24-manage-exchange-rates.jpg)

## Open questions (23)

*Inferred · group*

23 things nobody has confirmed for this feature. Each one is work somebody has to do before the feature can be rebuilt with confidence; they are carried here rather than resolved by guessing. Click one for the question and the document that raised it.

### Does Manage Vendors

*Inferred · question · source: `docs/modules/people-parties/README.md`*

**Does "Manage Vendors" (VendorActivate.jsp) apply an IsVendor/IsPreferredVendor filter over Employer, or does it write to different columns than "Manage Employers"?** Neither screen has been opened. This is the single most direct way to confirm the Vendor-is-Employer reading with a live capture rather than schema inference alone. Nobody has confirmed this. Recorded in modules/people-parties/README.md, under the People & Parties area. Until it is settled, anything built on the assumption is a guess.

### What determines

*Inferred · question · source: `docs/modules/people-parties/README.md`*

**What determines whether a Person row also gets a Member row (login) versus a NonMember row (no login), if both are field-for-field identical to Person?** See member-vs-person-vs-party.md's open questions — this is the sharpest unresolved question in the whole module. Nobody has confirmed this. Recorded in modules/people-parties/README.md, under the People & Parties area. Until it is settled, anything built on the assumption is a guess.

### What is the actual

*Inferred · question · source: `docs/modules/people-parties/README.md`*

What is the actual value list for Party.CodePartyTypeID/CodePartyGroupID, and does it overlap with Employer.CodeContactTypeIDList/LinkProjectEntityContact.CodeContactTypeID? Three different "type of party" classifications exist across this module's objects and none has been observed populated. Nobody has confirmed this. Recorded in modules/people-parties/README.md, under the People & Parties area. Until it is settled, anything built on the assumption is a guess.

### Where does the org

*Inferred · question · source: `docs/modules/people-parties/README.md`*

Where does the org chart actually live, beyond Member.SupervisorID? See security-model.md — the mechanism is schema-clear but the routing semantics (../workflow/routing-and-approvals.md OQ-22, OQ-23) remain open. Nobody has confirmed this. Recorded in modules/people-parties/README.md, under the People & Parties area. Until it is settled, anything built on the assumption is a guess.

### Does

*Inferred · question · source: `docs/modules/people-parties/README.md`*

**Does LinkProjectEntityContact's Landlord_EmployerID/Landlord_PersonID pair indicate a second, parallel contact record specifically for the landlord side of a lease**, or is it a convention for storing an alternate/secondary contact that happens to be named for the landlord case? No screen renders this pair. Nobody has confirmed this. Recorded in modules/people-parties/README.md, under the People & Parties area. Until it is settled, anything built on the assumption is a guess.

### Is NonMember a

*Inferred · question · source: `docs/modules/people-parties/member-vs-person-vs-party.md`*

**Is NonMember a physically separate row from its corresponding Person row, or a filtered/computed view of Person rows with no Member counterpart?** The field-for-field identity is consistent with either. Settling it requires a live capture of `ManageOneMemberMany Projects.jsp or ContactEdit.jsp showing whether converting a NonMember to a Member` preserves or replaces the underlying row. Nobody has confirmed this. Recorded in modules/people-parties/member-vs-person-vs-party.md, under the People & Parties area. Until it is settled, anything built on the assumption is a guess.

### What are

*Inferred · question · source: `docs/modules/people-parties/member-vs-person-vs-party.md`*

**What are AnySiteLoginName/AnySitePassword on Member, and how do they differ from LoginName/Password?** A second credential pair on the same object is unexplained — possibly an external/vendor-portal login distinct from the internal one, which would bear directly on how EnableVendorCollaboration (../workflow/routing-and-approvals.md §9) actually authenticates external members. Nobody has confirmed this. Recorded in modules/people-parties/member-vs-person-vs-party.md, under the People & Parties area. Until it is settled, anything built on the assumption is a guess.

### Does

*Inferred · question · source: `docs/modules/people-parties/member-vs-person-vs-party.md`*

**Does CodeContactTypeIDList on Person/Member/NonMember (the individual's own contact-type tags) share a value list with LinkProjectEntityContact.CodeContactTypeID (the per-entity roster's classification) and Party.CodePartyTypeID?** Three independent classification columns for "what kind of contact/party is this" exist across this module and none has been observed populated with real values. Nobody has confirmed this. Recorded in modules/people-parties/member-vs-person-vs-party.md, under the People & Parties area. Until it is settled, anything built on the assumption is a guess.

### Does Manage Vendors

*Inferred · question · source: `docs/modules/people-parties/member-vs-person-vs-party.md`*

Does "Manage Vendors" write to different Employer columns than "Manage Employers"? Would directly confirm or refine the Vendor-is-Employer reading with a live capture. See README.md's open questions. Nobody has confirmed this. Recorded in modules/people-parties/member-vs-person-vs-party.md, under the People & Parties area. Until it is settled, anything built on the assumption is a guess.

### Is Party

*Inferred · question · source: `docs/modules/people-parties/member-vs-person-vs-party.md`*

Is Party.ProjectEntityID ever populated for a non-Contract entity type, given Party also carries a direct ContractID? If Party is only ever used against Contracts in practice, the ProjectEntityID column may be vestigial generality rather than active polymorphism. Nobody has confirmed this. Recorded in modules/people-parties/member-vs-person-vs-party.md, under the People & Parties area. Until it is settled, anything built on the assumption is a guess.

### Open question

*Inferred · question · source: `docs/modules/people-parties/security-model.md`*

IsUnassignedWorkFlowApprover and UnassignedApproverID (the latter on WorkFlowTemplateStep, in ../workflow/) are stated dead in the vendor help text — *"a placeholder for an upcoming feature"* (Observed, routing-and-approvals.md §5). Confirm this is still true in the current build before assuming any approver-vacancy handling exists. Nobody has confirmed this. Recorded in modules/people-parties/security-model.md, under the People & Parties area. Until it is settled, anything built on the assumption is a guess.

### Does Member

*Inferred · question · source: `docs/modules/people-parties/security-model.md`*

Does Member.CodeAnalyticsRoleID gate anything security-relevant, or is it purely a reporting classification? No screen in this corpus renders it. Nobody has confirmed this. Recorded in modules/people-parties/security-model.md, under the People & Parties area. Until it is settled, anything built on the assumption is a guess.

### Is EmployerInactive on

*Inferred · question · source: `docs/modules/people-parties/security-model.md`*

Is EmployerInactive on Member a cached copy of Employer.Inactive, kept for fast filtering of external members whose employer has since been deactivated? Inferred from the name; not directly observed. Nobody has confirmed this. Recorded in modules/people-parties/security-model.md, under the People & Parties area. Until it is settled, anything built on the assumption is a guess.

### What suppresses a

*Inferred · question · source: `docs/features/security-access/README.md`*

What suppresses a navigation root, given all three known gates can be open? The central question in this area, and now sharper than before: it must explain both Equipment Contract and Program at AF. Candidate worth checking first — the action row Default access to Equipment Contracts for Portfolio Members, since an action-level default mentioning Portfolio membership is the right *shape*, though nothing yet connects it to root rendering. Other candidates: a Program/Portfolio record-level setting, a licence record outside FirmEdit.jsp, or a per-member rather than per-class grant. Nobody has confirmed this. Recorded in features/security-access/README.md, under the Security & Access area. Until it is settled, anything built on the assumption is a guess.

### Do the two hidden

*Inferred · question · source: `docs/features/security-access/README.md`*

Do the two hidden roots share a cause? Equipment Contract and Program both fail to render with page access open. If one mechanism explains both, it is general; if not, there may be two. Nobody has confirmed this. Recorded in features/security-access/README.md, under the Security & Access area. Until it is settled, anything built on the assumption is a guess.

### What do real user

*Inferred · question · source: `docs/features/security-access/README.md`*

~~What do real user classes hold?~~ Answered — all 10 AF classes read, matrix in af-security-page-access.json. BBW's have not been read, and BBW is the tenant where the root *does* render, so its matrix is the natural control. Nobody has confirmed this. Recorded in features/security-access/README.md, under the Security & Access area. Until it is settled, anything built on the assumption is a guess.

### What is on the Field

*Inferred · question · source: `docs/features/security-access/README.md`*

~~What is on the Field Security tab?~~ Answered — 6,553 field nodes, and read-only is View. What remains: whether its node tree is exactly the RGAF hierarchy, and what the 395-node difference from the 6,158 catalog leaves consists of. Nobody has confirmed this. Recorded in features/security-access/README.md, under the Security & Access area. Until it is settled, anything built on the assumption is a guess.

### What is on the Actions

*Inferred · question · source: `docs/features/security-access/README.md`*

~~What is on the Actions tab?~~ Answered — 70 verbs. What remains: whether this list is the same as the placeable action-button inventory on a page layout, or merely overlaps it. Nobody has confirmed this. Recorded in features/security-access/README.md, under the Security & Access area. Until it is settled, anything built on the assumption is a guess.

### Is Manage Top Menu

*Inferred · question · source: `docs/features/security-access/README.md`*

Is Manage Top Menu editable? If a firm can restructure navigation, "navigation is platform-seeded" needs qualifying — and it is another candidate for the missing mechanism. Nobody has confirmed this. Recorded in features/security-access/README.md, under the Security & Access area. Until it is settled, anything built on the assumption is a guess.

### How do the 70 Security

*Inferred · question · source: `docs/features/security-access/README.md`*

How do the 70 Security Privilege Code values relate to the four-level ladder? Note the coincidence that the Actions tab also has 70 rows; whether the code table *is* the action list is untested and would be worth one join. Nobody has confirmed this. Recorded in features/security-access/README.md, under the Security & Access area. Until it is settled, anything built on the assumption is a guess.

### Does Lx audit reads as

*Inferred · question · source: `docs/features/security-access/README.md`*

Does Lx audit reads as well as writes? The And Last Viewed <All Entities> filter on Audit Reports hints at view tracking. Unexercised, and it matters for SOC 2. Nobody has confirmed this. Recorded in features/security-access/README.md, under the Security & Access area. Until it is settled, anything built on the assumption is a guess.

### What is behind Special

*Inferred · question · source: `docs/features/security-access/README.md`*

What is behind Special Filters on Audit Reports? Never opened. Nobody has confirmed this. Recorded in features/security-access/README.md, under the Security & Access area. Until it is settled, anything built on the assumption is a guess.

### What is on the Budget

*Inferred · question · source: `docs/features/security-access/README.md`*

What is on the Budget Columns tab? Not read; budget is out of scope, so low priority. Nobody has confirmed this. Recorded in features/security-access/README.md, under the Security & Access area. Until it is settled, anything built on the assumption is a guess.

## Rules (13)

*Derived · group*

Every numbered rule the docs corpus records for this feature, named by a short summary. Click one: the panel opens with its ID, the full statement, and a link to the complete rule page.

### Person is a — [PPL-R-001](../rules/PPL-R-001.md)

*Derived · rule · source: `docs/modules/people-parties/rules.md`*

**`Person` and `NonMember` are field-for-field identical (37/37, zero type mismatches); `Member` is that same 37-field block plus 44 login/authorization fields.**

|  |  |
|---|---|
| When it fires | Any read or write that treats `Member`, `Person`, or `NonMember` as unrelated tables |
| What it reads | `PersonID`, typed `Number` (not a declared FK type) on all three objects |
| The test | `Person` and `NonMember` are field-for-field identical (37/37, zero type mismatches); `Member` is that same 37-field block plus 44 login/authorization fields |
| What it writes | All three share one identity key space. A rebuild should model one identity aggregate with an optional login/authorization extension, not three tables |

### No hard FK type — [PPL-R-002](../rules/PPL-R-002.md)

*Inferred · rule · source: `docs/modules/people-parties/rules.md`*

**No `Person ID` FK type exists anywhere in the 60-odd declared FK types.**

|  |  |
|---|---|
| When it fires | Any column that needs to reference "a person" from another object |
| What it reads | 12 columns across the schema declared type `Contact` (`Employer.AccountRepPersonID`, `Party.ContactID`, `LinkProjectEntityContact.PersonID`/`Landlord_PersonID`, `ProjectEntity. LinkProjectEntityContactListData` on all 9 spine roots, and others) |
| The test | No `Person ID` FK type exists anywhere in the 60-odd declared FK types |
| What it writes | A field typed `Contact` may resolve to a `Person`, `Member`, or `NonMember` row interchangeably. Model it as a polymorphic reference into the identity aggregate, not as an FK to a single physical table |

### ConvertToMember — [PPL-R-003](../rules/PPL-R-003.md)

*Inferred · rule · source: `docs/modules/people-parties/rules.md`*

**The existing identity is promoted to carry login/authorization data; it is not deleted and recreated. The exact mechanics (same row extended vs. new row sharing `PersonID`) are open — see `member-vs-person-vs-party.md` open question 1.**

|  |  |
|---|---|
| When it fires | A `Person`/`NonMember` is granted system login |
| What it reads | `Member.ConvertToMember` (Boolean) |
| What it writes | The existing identity is promoted to carry login/authorization data; it is not deleted and recreated. The exact mechanics (same row extended vs. new row sharing `PersonID`) are open — see `member-vs-person-vs-party.md` open question 1 |

### Employer is one — [PPL-R-004](../rules/PPL-R-004.md)

*Observed · rule · source: `docs/modules/people-parties/rules.md`*

**No `Vendor`, `Landlord`, or `Tenant`-as-counterparty object exists in the 223-object schema.**

|  |  |
|---|---|
| When it fires | Any process that treats Vendor, Landlord, or Tenant-as-counterparty as separate entities |
| What it reads | `PaymentTransaction.VendorID` (type `Employer ID`), `LinkProjectEntityContact. Landlord_EmployerID`, `Employer.Is*Vendor` flags |
| The test | No `Vendor`, `Landlord`, or `Tenant`-as-counterparty object exists in the 223-object schema |
| What it writes | All three business roles resolve to one `Employer` row. A rebuild should not create separate entities that then require manual synchronisation |

### Party is a generic — [PPL-R-005](../rules/PPL-R-005.md)

*Derived · rule · source: `docs/modules/people-parties/rules.md`*

**Both `CompanyID` and `ContactID` are independently nullable.**

|  |  |
|---|---|
| When it fires | A role needs recording against a Contract that doesn't fit the standing roster (`LinkProjectEntityContact`) or a direct `Employer` relationship elsewhere on `Contract` |
| What it reads | `Party.CompanyID` (nullable `Employer ID`), `Party.ContactID` (nullable `Contact`, soft), `CodePartyGroupID`/`CodePartyTypeID`, `PrimaryFlag` |
| The test | Both `CompanyID` and `ContactID` are independently nullable |
| What it writes | A `Party` row can name a company, a person, or (in principle) both, classified by type — the escape hatch for a role that isn't one of the platform's named relationships |

### The per entity — [PPL-R-006](../rules/PPL-R-006.md)

*Observed · rule · source: `docs/modules/people-parties/rules.md`*

**Contacts get a typed, richer roster entry; approved vendors get a bare membership list with no role classification at all.**

|  |  |
|---|---|
| When it fires | Listing "who is associated with this entity." |
| What it reads | `LinkProjectEntityContact` (12 fields, classified by `CodeContactTypeID`, carries a parallel `Landlord_*` pair) vs. `LinkProjectEntityVendor` (4 fields, unclassified — just `ProjectEntityID` + `VendorID`) |
| What it writes | Contacts get a typed, richer roster entry; approved vendors get a bare membership list with no role classification at all |

### 83 of Member s in — [PPL-R-007](../rules/PPL-R-007.md)

*Derived · rule · source: `docs/modules/people-parties/rules.md`*

**The identity/user record must be cheaply reachable from nearly every write path in the product for stamping alone, independent of its true business-domain reference count (50 edges).**

|  |  |
|---|---|
| When it fires | Any capacity-planning or service-boundary decision involving the identity service |
| What it reads | 290 FK edges target `Member`; 240 of them are `CreatedByID`/`ModifiedByID` |
| What it writes | The identity/user record must be cheaply reachable from nearly every write path in the product for stamping alone, independent of its true business-domain reference count (50 edges) |

### MemberAudit is login — [PPL-R-008](../rules/PPL-R-008.md)

*Observed · rule · source: `docs/modules/people-parties/rules.md`*

**This is a distinct audit mechanism from `../platform-tenancy/`'s `AuditColumn` (which logs field-level changes) — `MemberAudit` logs session/security events specifically.**

|  |  |
|---|---|
| When it fires | A member logs in, is impersonated (support access), or performs an audited action |
| What it reads | `MemberAudit.CodeMemberActionID`, `AuditDate`, `ImpersonatingMemberID`, `SrcIP`, `UserAgent` |
| What it writes | This is a distinct audit mechanism from `../platform-tenancy/`'s `AuditColumn` (which logs field-level changes) — `MemberAudit` logs session/security events specifically |

### A member s routable — [PPL-R-009](../rules/PPL-R-009.md)

*Observed · rule · source: `docs/modules/people-parties/rules.md`*

**A person can be selected by class, by title (global or entity-specific), or by reporting-line position, and these three do not have to agree with each other.**

|  |  |
|---|---|
| When it fires | Any workflow, task, or notification routing rule |
| What it reads | `Member.CodeUserClassID`, `Member.CodeJobTitleID` (default) / `LinkMemberProjectEntity.CodeJobTitleIDList`/`AssignedCodeJobTitleIDList` (per-entity override), `Member.SupervisorID` (org chart) |
| What it writes | A person can be selected by class, by title (global or entity-specific), or by reporting-line position, and these three do not have to agree with each other |

### Per entity job title — [PPL-R-010](../rules/PPL-R-010.md)

*Inferred · rule · source: `docs/modules/people-parties/rules.md`*

**Differs from `Member.CodeJobTitleID`.**

|  |  |
|---|---|
| When it fires | Job-Title-based routing evaluated in the context of a specific entity |
| What it reads | `LinkMemberProjectEntity.AssignedCodeJobTitleIDList` |
| The test | Differs from `Member.CodeJobTitleID` |
| What it writes | The entity-scoped assignment takes precedence for routing purposes on that entity — Inferred from the column's own definition text (*"the job titles that override the member's default job title"*), not confirmed by a live capture. See `../workflow/routing-and-approvals.md` OQ-24 |

### Region Market — [PPL-R-011](../rules/PPL-R-011.md)

*Derived · rule · source: `docs/modules/people-parties/rules.md`*

**This is a two-hop resolution (entity → region/market → manager), not a direct `Member` attribute lookup.**

|  |  |
|---|---|
| When it fires | `AssigneeType = REGION1 \| REGION2 \| MARKET` |
| What it reads | `ProjectEntity.RegionID`/`RootRegionID`/`SubRegionID`/`CodeMarketAreaID`/ `CodeMarketTypeID` (in `../platform-tenancy/`), then `LinkRegionManager` to find the responsible member |
| What it writes | This is a two-hop resolution (entity → region/market → manager), not a direct `Member` attribute lookup |

### Production routing — [PPL-R-012](../rules/PPL-R-012.md)

*Observed · rule · source: `docs/modules/people-parties/rules.md`*

**The rich role-based apparatus this module documents is largely latent in ASG's actual configuration. Treat as lower priority pending the answer to `../workflow/routing-and-approvals.md` OQ-42 (deliberate policy vs. workaround for the "all-for-one" overload).**

|  |  |
|---|---|
| When it fires | Prioritising which routing axes a rebuild must support on day one |
| What it reads | 17 of 19 live workflow steps route by named `Member`; 1 by Job Title; 1 by Ad Hoc; 0 by User Class, Org Chart level, or Region/Market |
| What it writes | The rich role-based apparatus this module documents is largely latent in ASG's actual configuration. Treat as lower priority pending the answer to `../workflow/routing-and-approvals.md` OQ-42 (deliberate policy vs. workaround for the "all-for-one" overload) |

### Approval amount — [PPL-R-013](../rules/PPL-R-013.md)

*Derived · rule · source: `docs/modules/people-parties/rules.md`*

**No `WorkFlowTemplateStep`/`WorkFlowTemplateStepAction` field reads these columns (exhaustive check, `../workflow/step-actions.md`/`routing-and-approvals.md`).**

|  |  |
|---|---|
| When it fires | Any attempt to implement amount-banded approval routing (route high-value payments to a different approver than low-value ones) |
| What it reads | `Member.PaymentApprovalMinAmount`/`MaxAmount`, `RecurringApprovalMinAmount`/`MaxAmount`, and the two `Equip*` pairs |
| The test | No `WorkFlowTemplateStep`/`WorkFlowTemplateStepAction` field reads these columns (exhaustive check, `../workflow/step-actions.md`/`routing-and-approvals.md`) |
| What it writes | These fields may be vestigial, may be read by application logic outside the schema dump, or may be populated but unused in the live tenant. Do not assume amount-banded routing works end-to-end without confirming a live step reads them |
