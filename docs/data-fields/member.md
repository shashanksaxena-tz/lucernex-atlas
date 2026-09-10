# Member — Data Fields

The internal user/employee account record for Lucernex itself (not a lease party) — login and access-control fields (Accept EULA?, Always Spell Check?, Color Scheme) alongside org fields (Code Job Function, Code Analytics Role) and billing rates. 78 Global fields under Company Items; this is user-account metadata rather than lease data, included in the catalog because Member records are referenced everywhere else (Created By, Modified By, approvers, assignees) via `sTYPE_MEMBER` lookup fields.

**Table Association:** `Member` &nbsp;·&nbsp; **Total fields:** 78 (Global: 78, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Accept EULA? | `AcceptEULA` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Company Items / Members |
| Address | `HtmlPersonAddress` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Members |
| Always Spell Check? | `AlwaysSpellCheck` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Company Items / Members |
| Approval Currency Type | `CodeApprovalCurrencyTypeID` | `sCODE_CURRENCY_TYPE` | Global | No | No |  | Company Items / Members |
| Bill Rate #1 | `BillRate1` | `sTYPE_MONEY` | Global | No | No |  | Company Items / Members |
| Bill Rate #2 | `BillRate2` | `sTYPE_MONEY` | Global | No | No |  | Company Items / Members |
| City | `City` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Members |
| Code Analytics Role | `CodeAnalyticsRoleID` | `sCODE_ANALYTICS_ROLE` | Global | No | No |  | Company Items / Members |
| Code Job Function | `CodeJobFunctionID` | `sCODE_JOB_FUNCTION` | Global | Yes | No |  | Company Items / Members |
| Color Scheme | `ColorScheme` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Members |
| Convert To Member | `ConvertToMember` | `sTYPE_CHECKBOX` | Global | No | No |  | Company Items / Members |
| Country | `Country` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Members |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Company Items / Members |
| Date Pattern | `DatePattern` | `sTYPE_DATEPATTERN` | Global | No | No |  | Company Items / Members |
| Demographics Login | `AnySiteLoginName` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Members |
| Demographics Password | `AnySitePassword` | `sTYPE_PASSWORD` | Global | No | No |  | Company Items / Members |
| Description | `Description` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Members |
| Designations | `Designations` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Members |
| Email #1 | `EMail1` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Members |
| Email #2 | `EMail2` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Members |
| Employer | `EmployerID` | `sTYPE_EMPLOYER` | Global | Yes | No |  | Company Items / Members |
| Employer Inactive? | `EmployerInactive` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Members |
| Equipment Contract Approval Level | `CodeEquipApprovalStatusID` | `sCODE_APPROVAL_STATUS_MEMBER_EQUIPMENT` | Global | No | No |  | Company Items / Members |
| Equipment Contract Payment Approval Amount (Maximum) | `EquipPaymentApprovalMaxAmount` | `sTYPE_MONEY` | Global | No | No |  | Company Items / Members |
| Equipment Contract Payment Approval Amount (Minimum) | `EquipPaymentApprovalMinAmount` | `sTYPE_MONEY` | Global | No | No |  | Company Items / Members |
| Equipment Contract Recurring Approval Amount (Maximum) | `EquipRecurringApprovalMaxAmount` | `sTYPE_MONEY` | Global | No | No |  | Company Items / Members |
| Equipment Contract Recurring Approval Amount (Minimum) | `EquipRecurringApprovalMinAmount` | `sTYPE_MONEY` | Global | No | No |  | Company Items / Members |
| Fax | `Fax` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Members |
| First Name | `FirstName` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / Members |
| Is Administrator? | `IsAdministrator` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Members |
| Is Exempt from Password Expiration? | `IsExemptFromPWDExpiration` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Company Items / Members |
| Is Inactive? | `Inactive` | `sTYPE_CHECKBOX` | Global | Yes | No |  | Company Items / Members |
| Is Lucernex Administrator? | `IsLucernexAdministrator` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Members |
| Is Master Member? | `IsMasterMember` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Members |
| Is Master Person? | `IsMasterPerson` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Members |
| Is View Private Issue Allowed? | `IsViewPrivateIssueAllowed` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Company Items / Members |
| Job Title | `CodeJobTitleID` | `sCODE_JOB_TITLE` | Global | No | No |  | Company Items / Members |
| Job Titles | `CodeJobTitleIDList` | `sCODE_JOB_TITLE` | Global | Yes | No |  | Company Items / Members |
| Jurisdiction | `JurisdictionID` | `sTYPE_JURISDICTION` | Global | No | No |  | Company Items / Members |
| Language | `Language` | `sTYPE_LANGUAGE` | Global | No | No |  | Company Items / Members |
| Last Login Date | `LastLoginDate` | `sTYPE_TIME` | Global | No | No |  | Company Items / Members |
| Last Name | `LastName` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / Members |
| Login Name | `LoginName` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / Members |
| Member ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / Members |
| Member Login Status | `CodeLockOutReasonID` | `sCODE_LOCK_OUT_REASON` | Global | Yes | No |  | Company Items / Members |
| Member Name | `MemberNameFirstLast` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Members |
| Member Name - Last, First | `PersonNameLastFirst` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Members |
| Member Photo | `MemberPhoto` | `sTYPE_PHOTO` | Global | No | No |  | Company Items / Members |
| Member RecID | `MemberID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Members |
| Middle Name | `MiddleName` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Members |
| Mobile Number | `MobileNumber` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Members |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Members |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Company Items / Members |
| Number Pattern | `NumberPattern` | `sTYPE_NUMBERPATTERN` | Global | No | No |  | Company Items / Members |
| Password | `Password` | `sTYPE_PASSWORD` | Global | Yes | No |  | Company Items / Members |
| Person RecID | `PersonID` | `sTYPE_UNFORMATTED_NUMBER` | Global | Yes | No |  | Company Items / Members |
| Phone | `Phone` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Members |
| Phone Extension | `PhoneExtension` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Members |
| Postal Code | `PostalCode` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Members |
| RE Contract Approval Level | `CodeApprovalStatusID` | `sCODE_APPROVAL_STATUS_MEMBER_RE` | Global | No | No |  | Company Items / Members |
| RE Contract Payment Approval Amount (Maximum) | `PaymentApprovalMaxAmount` | `sTYPE_MONEY` | Global | No | No |  | Company Items / Members |
| RE Contract Payment Approval Amount (Minimum) | `PaymentApprovalMinAmount` | `sTYPE_MONEY` | Global | No | No |  | Company Items / Members |
| RE Contract Recurring Approval Amount (Maximum) | `RecurringApprovalMaxAmount` | `sTYPE_MONEY` | Global | No | No |  | Company Items / Members |
| RE Contract Recurring Approval Amount (Minimum) | `RecurringApprovalMinAmount` | `sTYPE_MONEY` | Global | No | No |  | Company Items / Members |
| State | `StateProvinceCountryID` | `sTYPE_STATE_PROVINCE` | Global | No | No |  | Company Items / Members |
| Street Address #1 | `StreetAddress1` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Members |
| Street Address #2 | `StreetAddress2` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Members |
| Street Address #3 | `StreetAddress3` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Members |
| Street Address #4 | `StreetAddress4` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Members |
| Suffix | `Suffix` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Members |
| Supervisor | `SupervisorID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Members |
| Time Zone | `TimeZone` | `sTYPE_TIMEZONE` | Global | No | No |  | Company Items / Members |
| Title | `Title` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Members |
| Unassigned WorkFlow Approver | `IsUnassignedWorkFlowApprover` | `sTYPE_CHECKBOX` | Global | Yes | No |  | Company Items / Members |
| Use Employer Address? | `UseEmployerAddress` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Company Items / Members |
| User Class | `CodeUserClassID` | `sCODE_USER_CLASS` | Global | Yes | No |  | Company Items / Members |
| Web Site | `WebSite` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Members |
| Wireless E Mail | `WirelessEMail` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Members |
