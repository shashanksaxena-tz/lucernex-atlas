# Member

*81 fields · module: People & Parties · Postgres: `member`*

The internal user/employee account record for Lx itself (not a lease party) — login and access-control fields (Accept EULA?, Always Spell Check?, Color Scheme) alongside org fields (Code Job Function, Code Analytics Role) and billing rates. 78 Global fields under Company Items; this is user-account metadata rather than lease data, included in the catalog because Member records are referenced everywhere else (Created By, Modified By, approvers, assignees) via sTYPE_MEMBER lookup fields.

Source: `data-fields/member.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 81 |
| Fields with a vendor definition | 79 of 81 inventoried |
| Physical tables | `member` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 78 (78 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 290 keys from 162 record types |
| Points at | 6 other records |
| Tenancy position | firm_global |
| Rules that name it | 17 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### A hub: 290 keys point here

**Observed.** 162 record types hold a foreign key into this one, so it sits at the centre of the relationship graph. Changing its key or its identity is a change to AccrualTransaction, Allowance, AllowanceTransaction, AlternateRentSchedule and 158 others.

### Lands in member

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 79 fields carry a vendor definition

**Observed.** 79 of this record's 81 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 19 of this record's fields required; the Data Fields catalogue marks 18; 18 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [ACC-R-062](../rules/ACC-R-062.md) | all three ASC 842 steps use `Member` — a named approver, resolved at configuration time rather than by org-chart position | Observed |
| [WF-R-026](../rules/WF-R-026.md) | The step's ApproverJobTitleIDList is intersected against the roster of the entity the workflow is running on, filtered to members holding a matching job title, and the resulting flat member list is frozen onto the running step as WorkFlowSt | Derived |
| [WF-R-027](../rules/WF-R-027.md) | User Class routing resolves against Member.CodeUserClassID intersected with the entity roster; Org Chart Level routing walks Member.SupervisorID the configured number of hops from an anchor that is itself unstated (OQ-22); | Derived |
| [WF-R-028](../rules/WF-R-028.md) | Step instantiation · `WFTS.ApproverType` = Org Chart Level; `WorkFlowTemplateStepMember.OrgChartLevel`; | Derived |
| [WF-R-035](../rules/WF-R-035.md) | Both this field and Member.IsUnassignedWorkFlowApprover are documented as unimplemented placeholders. | Observed |
| [LAY-R-009](../rules/LAY-R-009.md) | A step resolves its approver by `Approval Level`: `Member`, `Job Title`, or `Ad Hoc`. | Derived |
| [PPL-R-001](../rules/PPL-R-001.md) | `Person` and `NonMember` are field-for-field identical (37/37, zero type mismatches); `Member` is that same 37-field block plus 44 login/authorization fields | Derived |
| [PPL-R-002](../rules/PPL-R-002.md) | No `Person ID` FK type exists anywhere in the 60-odd declared FK types | Inferred |
| [PPL-R-003](../rules/PPL-R-003.md) | The existing identity is promoted to carry login/authorization data; it is not deleted and recreated. The exact mechanics (same row extended vs. new row sharing `PersonID`) are open — see `member-vs-person-vs-party.md` open question 1 | Inferred |
| [PPL-R-007](../rules/PPL-R-007.md) | The identity/user record must be cheaply reachable from nearly every write path in the product for stamping alone, independent of its true business-domain reference count (50 edges) | Derived |
| [PPL-R-009](../rules/PPL-R-009.md) | A person can be selected by class, by title (global or entity-specific), or by reporting-line position, and these three do not have to agree with each other | Observed |
| [PPL-R-010](../rules/PPL-R-010.md) | Differs from `Member.CodeJobTitleID` | Inferred |
| [PPL-R-011](../rules/PPL-R-011.md) | This is a two-hop resolution (entity → region/market → manager), not a direct `Member` attribute lookup | Derived |
| [PPL-R-012](../rules/PPL-R-012.md) | The rich role-based apparatus this module documents is largely latent in ASG's actual configuration. Treat as lower priority pending the answer to `../workflow/routing-and-approvals.md` OQ-42 (deliberate policy vs. workaround for the "all-f | Observed |
| [PPL-R-013](../rules/PPL-R-013.md) | No `WorkFlowTemplateStep`/`WorkFlowTemplateStepAction` field reads these columns (exhaustive check, `../workflow/step-actions.md`/`routing-and-approvals.md`) | Derived |
| [PRJ-R-010](../rules/PRJ-R-010.md) | A task needs an assignee, but not a named individual · `LinkTaskByCodeMember.CodeJobTitleID`, `OrgChartLevel` · Assigns by job title / org-chart level rather than by `Member`, matching the `AssigneeType` = `JOB_TITLE` routing option (`graph | Derived |
| [PRJ-R-011](../rules/PRJ-R-011.md) | A task needs a named assignee · `LinkTaskMember.MemberID` · Assigns a specific `Member`, alongside `TaskGroup.Assignee_MemberID`'s own direct field — two mechanisms for the same concept exist side by side. · Observed | Observed |

## Fields

### Relationships (foreign keys) (5)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `EmployerID` | Employer | Select the person's employer from this field. Employers are third party companies that are involved in your lifecycle process. They can be companies you pay also known as vendors or companies that are part of projects such as architects or general contractors. | Employer ID | Global | yes | `member.EmployerID · TEXT` | [Employer](Employer.md) |
| `IStateProvinceCountryID` | State | Select the state or province from this field. | Country, State, County ID | — |  | `member.IStateProvinceCountryID · TEXT` | [StateProvinceCountry](StateProvinceCountry.md) |
| `JurisdictionID` | Jurisdiction | The county / province associated with the associated entity's address. | County ID | Global |  | `member.JurisdictionID · TEXT` | [Jurisdiction](Jurisdiction.md) |
| `StateProvinceCountryID` | State | The state / province of the address associated with this record. | Country, State, County ID | Global |  | `member.StateProvinceCountryID · TEXT` | [StateProvinceCountry](StateProvinceCountry.md) |
| `SupervisorID` | Supervisor | Select the member's supervisor from this field. | Member ID | Global |  | `member.SupervisorID · TEXT` | [Member](Member.md) |

### Coded values (drop-downs) (10)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeAnalyticsRoleID` | Code Analytics Role |  | Dropdown (Analytics Role Code) | Global |  | `member.CodeAnalyticsRoleID · TEXT` | Analytics Role Code |
| `CodeApprovalCurrencyTypeID` | Approval Currency Type | Select the member's approval currency type from this field. This field is used when determining whether a recurring amount or transaction exceeds the member's approval limits. | Dropdown (Currency Type Code) | Global |  | `member.CodeApprovalCurrencyTypeID · TEXT` | Currency Type Code |
| `CodeApprovalStatusID` | RE Contract Approval Level | Select the approval level that this user has for RE Contracts from this field. Approval levels restrict the types of items and amounts that approvers can approve. | Dropdown (Approval Status Code) | Global |  | `member.CodeApprovalStatusID · TEXT` | Approval Status Code |
| `CodeContactTypeIDList` | Contact Type List | Select the contact type this person should have using the multi-select field. | Dropdown (Contact Type Code) | — | yes | `member.CodeContactTypeIDList · TEXT` | Contact Type Code |
| `CodeEquipApprovalStatusID` | Equipment Contract Approval Level | Select the approval level that this user has for Equipment Contracts from this field. Approval levels restrict the types of items and amounts that approvers can approve. | Dropdown (Approval Status Code) | Global |  | `member.CodeEquipApprovalStatusID · TEXT` | Approval Status Code |
| `CodeJobFunctionID` | Code Job Function | Select this person's job function from this field. A job function is a broad category. Think of a job function as a person's department. This field is not functional unless you select System Administrator. | Dropdown (Job Function Code) | Global | yes | `member.CodeJobFunctionID · TEXT` | Job Function Code |
| `CodeJobTitleID` | Job Title | Select this person's job title from this field. A job title is more specific to the person than the job function. The Job Title is used when auto-assigning things like tasks, work flow steps, and notifications. | Dropdown (Job Title Code) | Global |  | `member.CodeJobTitleID · TEXT` | Job Title Code |
| `CodeJobTitleIDList` | Job Titles |  | Dropdown (Job Title Code) | Global | yes | `member.CodeJobTitleIDList · TEXT` | Job Title Code |
| `CodeLockOutReasonID` | Member Login Status | This field displays the reason the user is locked out of Lx. | Dropdown (Lock Out Reason Code) | Global | yes | `member.CodeLockOutReasonID · TEXT` | Lock Out Reason Code |
| `CodeUserClassID` | User Class | Select the member's user class from this field. | Dropdown (User Class) | Global | yes | `member.CodeUserClassID · TEXT` | User Class |

### Money (10)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BillRate1` | Bill Rate #1 | Enter the person's primary billing rate in this field. | Currency | Global |  | `member.BillRate1 · TEXT` |  |
| `BillRate2` | Bill Rate #2 | Enter the person's secondary billing rate in this field. | Currency | Global |  | `member.BillRate2 · TEXT` |  |
| `EquipPaymentApprovalMaxAmount` | Equipment Contract Payment Approval Amount (Maximum) | Enter the maximum one-time payment amount this user is allowed to approve for equipment contracts in this field. | Currency | Global |  | `member.EquipPaymentApprovalMaxAmount · TEXT` |  |
| `EquipPaymentApprovalMinAmount` | Equipment Contract Payment Approval Amount (Minimum) | Enter the minimum one-time payment amount this user is allowed to approve for equipment contracts in this field. | Currency | Global |  | `member.EquipPaymentApprovalMinAmount · TEXT` |  |
| `EquipRecurringApprovalMaxAmount` | Equipment Contract Recurring Approval Amount (Maximum) | Enter the maximum recurring payment amount this user is allowed to approve for equipment contracts in this field. | Currency | Global |  | `member.EquipRecurringApprovalMaxAmount · TEXT` |  |
| `EquipRecurringApprovalMinAmount` | Equipment Contract Recurring Approval Amount (Minimum) | Enter the minimum recurring payment amount this user is allowed to approve for equipment contracts in this field. | Currency | Global |  | `member.EquipRecurringApprovalMinAmount · TEXT` |  |
| `PaymentApprovalMaxAmount` | RE Contract Payment Approval Amount (Maximum) | Enter the maximum one-time payment amount this user is allowed to approve for real estate contracts in this field. | Currency | Global |  | `member.PaymentApprovalMaxAmount · TEXT` |  |
| `PaymentApprovalMinAmount` | RE Contract Payment Approval Amount (Minimum) | Enter the minimum one-time payment amount this user is allowed to approve for real estate contracts in this field. | Currency | Global |  | `member.PaymentApprovalMinAmount · TEXT` |  |
| `RecurringApprovalMaxAmount` | RE Contract Recurring Approval Amount (Maximum) | Enter the maximum recurring payment amount this user is allowed to approve for real estate contracts in this field. | Currency | Global |  | `member.RecurringApprovalMaxAmount · TEXT` |  |
| `RecurringApprovalMinAmount` | RE Contract Recurring Approval Amount (Minimum) | Enter the minimum recurring payment amount this user is allowed to approve for real estate contracts in this field. | Currency | Global |  | `member.RecurringApprovalMinAmount · TEXT` |  |

### Quantities (3)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `MemberID` | Member RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `member.MemberID · VARCHAR(64) NOT NULL` |  |
| `NumberPattern` | Number Pattern | Select the member's number format from this field. Lx is configured to auto-detect the user's number format by default. | Number Format | Global |  | `member.NumberPattern · TEXT` |  |
| `PersonID` | Person RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global | yes | `member.PersonID · TEXT` |  |

### Dates & timestamps (1)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `LastLoginDate` | Last Login Date | The last login date for this member. | Time | Global |  | `member.LastLoginDate · TEXT` |  |

### Flags (13)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AcceptEULA` | Accept EULA? | This flag is set to TRUE when a member has accepted the terms and conditions for Lx. | Boolean | Global | yes | `member.AcceptEULA · TEXT` |  |
| `AlwaysSpellCheck` | Always Spell Check? | This field is currently disabled. | Boolean | Global | yes | `member.AlwaysSpellCheck · TEXT` |  |
| `ConvertToMember` | Convert To Member | When added to a custom layout for the Add Person window, this field allows the user to convert the person to a Member. | Boolean | Global |  | `member.ConvertToMember · TEXT` |  |
| `EmployerInactive` | Employer Inactive? | The active state of the member's employer. A member can't be active if their employer is inactive. | Boolean | Global |  | `member.EmployerInactive · TEXT` |  |
| `Inactive` | Is Inactive? | This flag indicates whether the member is active or inactive. | Boolean | Global | yes | `member.Inactive · TEXT` |  |
| `IsAdministrator` | Is Administrator? | If set to true, this user is a system administrator. If set to false, the user is not a system administrator. | Boolean | Global |  | `member.IsAdministrator · TEXT` |  |
| `IsExemptFromPWDExpiration` | Is Exempt from Password Expiration? | This setting controls whether a user is exempt from password expiration. | Boolean | Global | yes | `member.IsExemptFromPWDExpiration · TEXT` |  |
| `IsLucernexAdministrator` | Is Lx Administrator? | This setting controls whether or not a user has the Lx Administrator permission set. This security configuration is limited to Accruent employees only. | Boolean | Global |  | `member.IsLucernexAdministrator · TEXT` |  |
| `IsMasterMember` | Is Master Member? | This field determines if the person is in a firm that is a master firm of slave firms, and is in those slave firms. | Boolean | Global |  | `member.IsMasterMember · TEXT` |  |
| `IsMasterPerson` | Is Master Person? | This field determines if the person is in a firm that is a master firm of slave firms, and is in those slave firms. | Boolean | Global |  | `member.IsMasterPerson · TEXT` |  |
| `IsUnassignedWorkFlowApprover` | Unassigned WorkFlow Approver | This field is a placeholder for an upcoming feature. | Boolean | Global | yes | `member.IsUnassignedWorkFlowApprover · TEXT` |  |
| `IsViewPrivateIssueAllowed` | Is View Private Issue Allowed? | Select this check box if you want to allow the member to see private forms. | Boolean | Global | yes | `member.IsViewPrivateIssueAllowed · TEXT` |  |
| `UseEmployerAddress` | Use Employer Address? | If you want to use the address of the employer for this member record, select this check box. | Boolean | Global | yes | `member.UseEmployerAddress · TEXT` |  |

### Text & notes (34)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AnySiteLoginName` | Demographics Login | Enter the member's Intalytics username in this field. | Text | Global |  | `member.AnySiteLoginName · TEXT` |  |
| `AnySitePassword` | Demographics Password | Enter the member's Intalytics password in this field. | Text | Global |  | `member.AnySitePassword · TEXT` |  |
| `City` |  | The city associated with this record. | Text | Global |  | `member.City · TEXT` |  |
| `ColorScheme` | Color Scheme | This field is no longer used. | Text | Global |  | `member.ColorScheme · TEXT` |  |
| `Country` |  | The country of the address associated with this record. | Text | Global |  | `member.Country · TEXT` |  |
| `CountryID` | Country | Select the member's country from this field. | Text | — |  | `member.CountryID · TEXT` |  |
| `Description` |  | Write a description of the record. | Text | Global |  | `member.Description · TEXT` |  |
| `Designations` |  | The designation of the member from the Person table. | Text | Global |  | `member.Designations · TEXT` |  |
| `EMail1` | Email #1 | Enter the person's primary email address. | Text | Global |  | `member.EMail1 · TEXT` |  |
| `EMail2` | Email #2 | Enter the person's secondary email address. | Text | Global |  | `member.EMail2 · TEXT` |  |
| `Fax` |  | Enter the person's fax number in this field. | Text | Global |  | `member.Fax · TEXT` |  |
| `FirstName` | First Name | Enter the person's first name in this field. | Text | Global | yes | `member.FirstName · TEXT` |  |
| `HtmlPersonAddress` | Address | The address of the member. | Text | Global |  | `member.HtmlPersonAddress · TEXT` |  |
| `Language` |  | Select the member's language from this field. Lx is configured to auto-detect the user's language by default. | Text | Global |  | `member.Language · TEXT` |  |
| `LastName` | Last Name | Enter the person's last name in this field. | Text | Global | yes | `member.LastName · TEXT` |  |
| `LoginName` | Login Name | Enter the member's username in this field. | Text | Global | yes | `member.LoginName · TEXT` |  |
| `MemberNameFirstLast` | Member Name | The member's name in this format: "First Middle, Suffix, Last, Designations" | Text | Global |  | `member.MemberNameFirstLast · TEXT` |  |
| `MemberPhoto` | Member Photo | This field can be used to store a member's photo. | Text | Global |  | `member.MemberPhoto · TEXT` |  |
| `MiddleName` | Middle Name | Enter the person's middle name in this field. | Text | Global |  | `member.MiddleName · TEXT` |  |
| `MobileNumber` | Mobile Number | Enter the person's mobile phone number in this field. | Text | Global |  | `member.MobileNumber · TEXT` |  |
| `Password` |  | Enter the member's temporary password in this field. Make sure to send the member this temporary password. | Text | Global | yes | `member.Password · TEXT` |  |
| `PersonNameLastFirst` | Member Name - Last, First | The member's name in this format: "Last, Suffix, Designations, First Middle" | Text | Global |  | `member.PersonNameLastFirst · TEXT` |  |
| `Phone` |  | Enter the person's phone number in this field. | Text | Global |  | `member.Phone · TEXT` |  |
| `PhoneExtension` | Phone Extension | Enter the person's phone extenstion in this field. | Text | Global |  | `member.PhoneExtension · TEXT` |  |
| `PostalCode` | Postal Code | Enter the person's postal code in this field. | Text | Global |  | `member.PostalCode · TEXT` |  |
| `StreetAddress1` | Street Address #1 | The first line of the street address. | Text | Global |  | `member.StreetAddress1 · TEXT` |  |
| `StreetAddress2` | Street Address #2 | The second line of the street address. | Text | Global |  | `member.StreetAddress2 · TEXT` |  |
| `StreetAddress3` | Street Address #3 | The third line of the street address. | Text | Global |  | `member.StreetAddress3 · TEXT` |  |
| `StreetAddress4` | Street Address #4 | The fourth line of the street address. | Text | Global |  | `member.StreetAddress4 · TEXT` |  |
| `Suffix` |  | Enter the person's suffix if the person has one. | Text | Global |  | `member.Suffix · TEXT` |  |
| `TimeZone` | Time Zone | Select the member's default time zone from this field. | Text | Global |  | `member.TimeZone · TEXT` |  |
| `Title` |  | Enter the person's title in this field. | Text | Global |  | `member.Title · TEXT` |  |
| `WebSite` | Web Site | Enter the person's website in this field. | Text | Global |  | `member.WebSite · TEXT` |  |
| `WirelessEMail` | Wireless E Mail | Enter the person's wireless email in this field. | Text | Global |  | `member.WirelessEMail · TEXT` |  |

### Audit & record keeping (4)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Member ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `member.BOMapClientRecordID · TEXT` |  |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `member.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `member.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `member.ModifiedDate · TEXT` |  |

### Other (1)

Everything that did not fall into a named group.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DatePattern` | Date Pattern | Select the member's date format from this field. Lx is configured to auto-detect the user's date format by default. | Date Format | Global |  | `member.DatePattern · TEXT` |  |

## What points here (290 keys)

| Record type | Via column |
|---|---|
| [WorkFlowTemplateStep](WorkFlowTemplateStep.md) | `ApproverMemberIDList`, `AssigneeMemberIDList`, `CreatedByID`, `ModifiedByID`, `NotifieeMemberIDList`, `RunAtCompleteApprover1ID`, `RunAtCompleteApprover2ID`, `RunAtStartApprover1ID`, `RunAtStartApprover2ID`, `UnassignedApproverID` |
| [WFStepFullImport](WFStepFullImport.md) | `ApproverMemberIDList`, `AssigneeMemberIDList`, `CurrentStepMemberIDList`, `ModifiedByID`, `NotifieeMemberIDList`, `PriorSubmitByMemberID`, `SubmitForApprovalByMemberID` |
| [WorkFlowStep](WorkFlowStep.md) | `ApproverMemberIDList`, `AssigneeMemberIDList`, `CurrentStepMemberIDList`, `ModifiedByID`, `NotifieeMemberIDList`, `PriorSubmitByMemberID`, `SubmitForApprovalByMemberID` |
| [Issue](Issue.md) | `AssignedToMemberIDs`, `AttentionEmailTo`, `CheckedOutByMemberID`, `InitiatedByMemberID`, `ManagerMemberIDs`, `ModifiedByID` |
| [BidPackage](BidPackage.md) | `BidAwardByID`, `BidCancelledByID`, `CreatedByID`, `ModifiedByID`, `WinningBidMemberIDList` |
| [SLSummary](SLSummary.md) | `CreatedByID`, `ModifiedByID`, `NeedsRecalcModifiedByLastMember`, `NeedsRecalcModifiedByMemberIDList` |
| [BidderIssue](BidderIssue.md) | `CreatedByID`, `MemberIDList`, `ModifiedByID` |
| [Contract](Contract.md) | `CreatedByID`, `Firm_LeaseAnalyst`, `ModifiedByID` |
| [MemberAudit](MemberAudit.md) | `ImpersonatingMemberID`, `MemberID`, `ModifiedByID` |
| [RETransaction](RETransaction.md) | `AssigneeMemberID`, `CreatedByID`, `ModifiedByID` |
| [WorkOrder](WorkOrder.md) | `ApproverMemberID`, `CreatedByID`, `ModifiedByID` |
| [AccrualTransaction](AccrualTransaction.md) | `CreatedByID`, `ModifiedByID` |
| [AlternateRentSchedule](AlternateRentSchedule.md) | `CreatedByID`, `ModifiedByID` |
| [Asset](Asset.md) | `CreatedByID`, `ModifiedByID` |
| [AssetHistory](AssetHistory.md) | `CreatedByID`, `ModifiedByID` |
| [BidPackageTemplate](BidPackageTemplate.md) | `CreatedByID`, `ModifiedByID` |
| [BudgetColumn](BudgetColumn.md) | `CreatedByMemberID`, `ModifiedByID` |
| [BudgetColumnType](BudgetColumnType.md) | `CreatedByID`, `ModifiedByID` |
| [BudgetOption](BudgetOption.md) | `CreatedByMemberID`, `ModifiedByID` |
| [BudgetOptionTemplate](BudgetOptionTemplate.md) | `CreatedByID`, `ModifiedByID` |
| [BudgetTemplateAudit](BudgetTemplateAudit.md) | `CreatedByID`, `ModifiedByID` |
| [BudgetView](BudgetView.md) | `CreatedByID`, `ModifiedByID` |
| [ChangeOrder](ChangeOrder.md) | `CreatedByID`, `ModifiedByID` |
| [ContractFinancialTest](ContractFinancialTest.md) | `CreatedByID`, `ModifiedByID` |
| [CostTrackingTemplate](CostTrackingTemplate.md) | `CreatedByID`, `ModifiedByID` |
| [CustomCodeField](CustomCodeField.md) | `CreatedByID`, `ModifiedByID` |
| [DevelopmentSlot](DevelopmentSlot.md) | `BrokerMemberID`, `ModifiedByID` |
| [DiscountRate](DiscountRate.md) | `CreatedByID`, `ModifiedByID` |
| [Document](Document.md) | `CheckedOutByMemberID`, `ModifiedByID` |
| [EMailReceivedLog](EMailReceivedLog.md) | `CreatedByID`, `ModifiedByID` |
| [Employer](Employer.md) | `CreatedByID`, `ModifiedByID` |
| [ExpenseAccrualSchedule](ExpenseAccrualSchedule.md) | `CreatedByID`, `ModifiedByID` |
| [ExpenseAccrualSetup](ExpenseAccrualSetup.md) | `CreatedByID`, `ModifiedByID` |
| [ExpenseRecovery](ExpenseRecovery.md) | `CreatedByID`, `ModifiedByID` |
| [ExpenseRecoveryItem](ExpenseRecoveryItem.md) | `CreatedByID`, `ModifiedByID` |
| [ExpenseVendorAllocation](ExpenseVendorAllocation.md) | `CreatedByID`, `ModifiedByID` |
| [Facility](Facility.md) | `CreatedByID`, `ModifiedByID` |
| [FacilityExpense](FacilityExpense.md) | `CreatedByID`, `ModifiedByID` |
| [FinancialAdjustment](FinancialAdjustment.md) | `CreatedByID`, `ModifiedByID` |
| [FolderTemplateAudit](FolderTemplateAudit.md) | `CreatedByID`, `ModifiedByID` |
| [HolidayDate](HolidayDate.md) | `CreatedByID`, `ModifiedByID` |
| [HolidaySchedule](HolidaySchedule.md) | `CreatedByID`, `ModifiedByID` |
| [InvoiceIssue](InvoiceIssue.md) | `CreatedByID`, `ModifiedByID` |
| [InvoiceItem](InvoiceItem.md) | `CreatedByID`, `ModifiedByID` |
| [IssueResponse](IssueResponse.md) | `CreatedByID`, `ModifiedByID` |
| [LandlordInvoice](LandlordInvoice.md) | `CreatedByID`, `ModifiedByID` |
| [LandlordInvoiceItem](LandlordInvoiceItem.md) | `CreatedByID`, `ModifiedByID` |
| [LinkLandlordInvPaymentTxn](LinkLandlordInvPaymentTxn.md) | `CreatedByID`, `ModifiedByID` |
| [LinkMemberProjectEntity](LinkMemberProjectEntity.md) | `MemberID`, `ModifiedByID` |
| [LinkReTransScenContact](LinkReTransScenContact.md) | `CreatedByID`, `ModifiedByID` |
| [LinkReceiptTransaction](LinkReceiptTransaction.md) | `CreatedByID`, `ModifiedByID` |
| [LinkSchedOffsetExpGrpType](LinkSchedOffsetExpGrpType.md) | `CreatedByID`, `ModifiedByID` |
| [LinkTaskMember](LinkTaskMember.md) | `MemberID`, `ModifiedByID` |
| [Location](Location.md) | `CreatedByID`, `ModifiedByID` |
| [Member](Member.md) | `ModifiedByID`, `SupervisorID` |
| [Parcel](Parcel.md) | `CreatedByID`, `ModifiedByID` |
| [Parking](Parking.md) | `CreatedByID`, `ModifiedByID` |
| [PayApp](PayApp.md) | `CreatedByID`, `ModifiedByID` |
| [PercentageRentBreakpoint](PercentageRentBreakpoint.md) | `CreatedByID`, `ModifiedByID` |
| [PotentialProject](PotentialProject.md) | `CreatedByID`, `ModifiedByID` |
| [ProcessTimeline](ProcessTimeline.md) | `Assignee_MemberID`, `ModifiedByID` |
| [Program](Program.md) | `CreatedByID`, `ModifiedByID` |
| [Project](Project.md) | `CreatedByID`, `ModifiedByID` |
| [ProjectEntity](ProjectEntity.md) | `CreatedByID`, `ModifiedByID` |
| [PropertyTaxAppeal](PropertyTaxAppeal.md) | `CreatedByID`, `ModifiedByID` |
| [PropertyTaxAppealAward](PropertyTaxAppealAward.md) | `CreatedByID`, `ModifiedByID` |
| [PropertyTaxAssessment](PropertyTaxAssessment.md) | `CreatedByID`, `ModifiedByID` |
| [PropertyTaxBill](PropertyTaxBill.md) | `CreatedByID`, `ModifiedByID` |
| [PropertyTaxDetail](PropertyTaxDetail.md) | `CreatedByID`, `ModifiedByID` |
| [PropertyTaxSummary](PropertyTaxSummary.md) | `CreatedByID`, `ModifiedByID` |
| [Prototype](Prototype.md) | `CreatedByID`, `ModifiedByID` |
| [PurchaseOrder](PurchaseOrder.md) | `CreatedByID`, `ModifiedByID` |
| [Question](Question.md) | `CreatedByID`, `ModifiedByID` |
| [ReTransScenContact](ReTransScenContact.md) | `CreatedByID`, `ModifiedByID` |
| [RecalcOverrideNotes](RecalcOverrideNotes.md) | `CreatedByID`, `ModifiedByID` |
| [SLPeriod](SLPeriod.md) | `CreatedByID`, `ModifiedByID` |
| [SalesExclusion](SalesExclusion.md) | `CreatedByID`, `ModifiedByID` |
| [SalesExclusionCap](SalesExclusionCap.md) | `CreatedByID`, `ModifiedByID` |
| [Scenario](Scenario.md) | `CreatedByID`, `ModifiedByID` |
| [ScheduledOffset](ScheduledOffset.md) | `CreatedByID`, `ModifiedByID` |
| [ServiceRequest](ServiceRequest.md) | `CreatedByID`, `ModifiedByID` |
| [Space](Space.md) | `CreatedByID`, `ModifiedByID` |
| [Task](Task.md) | `Assignee_MemberID`, `ModifiedByID` |
| [TaskGroup](TaskGroup.md) | `Assignee_MemberID`, `ModifiedByID` |
| [TaskItem](TaskItem.md) | `Assignee_MemberID`, `ModifiedByID` |
| [TaskPredecessor](TaskPredecessor.md) | `CreatedByID`, `ModifiedByID` |
| [TaskTemplateAudit](TaskTemplateAudit.md) | `CreatedByID`, `ModifiedByID` |
| [TemplateAudit](TemplateAudit.md) | `CreatedByID`, `ModifiedByID` |
| [Tenant](Tenant.md) | `CreatedByID`, `ModifiedByID` |
| [UseBasedRentBreakpoint](UseBasedRentBreakpoint.md) | `CreatedByID`, `ModifiedByID` |
| [VendorInsurance](VendorInsurance.md) | `CreatedByID`, `ModifiedByID` |
| [WorkFlow](WorkFlow.md) | `InitiatedByMemberID`, `ModifiedByID` |
| [WorkFlowStepApprover](WorkFlowStepApprover.md) | `MemberID`, `ModifiedByID` |
| [WorkFlowStepAssignee](WorkFlowStepAssignee.md) | `MemberID`, `ModifiedByID` |
| [WorkFlowTemplate](WorkFlowTemplate.md) | `CreatedByID`, `ModifiedByID` |
| [WorkFlowTemplateStepAction](WorkFlowTemplateStepAction.md) | `CreatedByID`, `ModifiedByID` |
| [Allowance](Allowance.md) | `ModifiedByID` |
| [AllowanceTransaction](AllowanceTransaction.md) | `ModifiedByID` |
| [AuditColumn](AuditColumn.md) | `CreatedByID` |
| [BudgetColumnItemValue](BudgetColumnItemValue.md) | `ModifiedByID` |
| [BudgetIndex](BudgetIndex.md) | `ModifiedByID` |
| [BudgetIndexValue](BudgetIndexValue.md) | `ModifiedByID` |
| [BudgetLineGroup](BudgetLineGroup.md) | `ModifiedByID` |
| [BudgetLineItem](BudgetLineItem.md) | `ModifiedByID` |
| [BudgetLineLeaf](BudgetLineLeaf.md) | `ModifiedByID` |
| [CLRExtensionPart](CLRExtensionPart.md) | `ModifiedByID` |
| [CPI](CPI.md) | `ModifiedByID` |
| [ClientListRow](ClientListRow.md) | `ModifiedByID` |
| [CoTenancy](CoTenancy.md) | `ModifiedByID` |
| [CodeExpenseType](CodeExpenseType.md) | `ModifiedByID` |
| [Competitor](Competitor.md) | `ModifiedByID` |
| [Complex](Complex.md) | `ModifiedByID` |
| [ContractAmendment](ContractAmendment.md) | `ModifiedByID` |
| [ContractTerm](ContractTerm.md) | `ModifiedByID` |
| [Covenant](Covenant.md) | `ModifiedByID` |
| [DMA](DMA.md) | `ModifiedByID` |
| [DemographicReport](DemographicReport.md) | `ModifiedByID` |
| [DevelopmentPlan](DevelopmentPlan.md) | `ModifiedByID` |
| [EscalationIndex](EscalationIndex.md) | `ModifiedByID` |
| [ExpenseAllocation](ExpenseAllocation.md) | `ModifiedByID` |
| [ExpenseEscalation](ExpenseEscalation.md) | `ModifiedByID` |
| [ExpenseSchedule](ExpenseSchedule.md) | `ModifiedByID` |
| [ExpenseSetup](ExpenseSetup.md) | `ModifiedByID` |
| [Firm](Firm.md) | `ModifiedByID` |
| [FiscalPeriod](FiscalPeriod.md) | `ModifiedByID` |
| [Folder](Folder.md) | `ModifiedByID` |
| [Insurance](Insurance.md) | `ModifiedByID` |
| [Jurisdiction](Jurisdiction.md) | `ModifiedByID` |
| [KeyDate](KeyDate.md) | `ModifiedByID` |
| [LandPurchaseSummary](LandPurchaseSummary.md) | `ModifiedByID` |
| [LeaseInfo](LeaseInfo.md) | `ModifiedByID` |
| [LinkIssuePart](LinkIssuePart.md) | `ModifiedByID` |
| [LinkIssuePartOrder](LinkIssuePartOrder.md) | `ModifiedByID` |
| [LinkLandPurchaseInspection](LinkLandPurchaseInspection.md) | `ModifiedByID` |
| [LinkProjectEntityContact](LinkProjectEntityContact.md) | `ModifiedByID` |
| [LinkTaskByCodeMember](LinkTaskByCodeMember.md) | `ModifiedByID` |
| [NonMember](NonMember.md) | `ModifiedByID` |
| [Organization](Organization.md) | `ModifiedByID` |
| [Ownership](Ownership.md) | `ModifiedByID` |
| [ParcelAccess](ParcelAccess.md) | `ModifiedByID` |
| [Part](Part.md) | `ModifiedByID` |
| [PartPackage](PartPackage.md) | `ModifiedByID` |
| [PartPackageItem](PartPackageItem.md) | `ModifiedByID` |
| [Party](Party.md) | `ModifiedByID` |
| [PaymentReceipt](PaymentReceipt.md) | `ModifiedByID` |
| [PaymentTransaction](PaymentTransaction.md) | `ModifiedByID` |
| [PaymentTransactionFullImport](PaymentTransactionFullImport.md) | `ModifiedByID` |
| [PercentageRent](PercentageRent.md) | `ModifiedByID` |
| [Person](Person.md) | `ModifiedByID` |
| [ProFormaBudget](ProFormaBudget.md) | `ModifiedByID` |
| [ProcessTimelineTemplate](ProcessTimelineTemplate.md) | `ModifiedByID` |
| [ProgramRevenueWeeks](ProgramRevenueWeeks.md) | `ModifiedByID` |
| [Responsibility](Responsibility.md) | `ModifiedByID` |
| [Sales](Sales.md) | `ModifiedByID` |
| [Security](Security.md) | `ModifiedByID` |
| [SecurityDeposit](SecurityDeposit.md) | `ModifiedByID` |
| [SiteSurvey](SiteSurvey.md) | `ModifiedByID` |
| [StateProvinceCountry](StateProvinceCountry.md) | `ModifiedByID` |
| [Usage](Usage.md) | `ModifiedByID` |
| [UseBasedRent](UseBasedRent.md) | `ModifiedByID` |
| [UserClassSecurity](UserClassSecurity.md) | `ModifiedByID` |
| [VariableRentOffset](VariableRentOffset.md) | `ModifiedByID` |
