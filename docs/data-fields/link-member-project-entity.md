# LinkMemberProjectEntity — Data Fields

A join record linking an internal Member to a ProjectEntity in an org-chart role — manager name/title and job function, despite the Link-style name it carries enough project-team detail (24 fields) to warrant standalone treatment. 24 Global fields spanning Statics and Summary Information.

**Table Association:** `LinkMemberProjectEntity` &nbsp;·&nbsp; **Total fields:** 24 (Global: 24, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Added By Org Chart? | `AddedByOrgChart` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Statics / Hidden |
| Address | `PEMgr_HTMLAddress` | `sTYPE_TEXT` | Global | No | No |  | Summary Information / Management |
| Employer | `PEMgr_EmployerID` | `sTYPE_EMPLOYER` | Global | No | No |  | Summary Information / Management |
| Job Function | `PEMgr_CodeJobFunctionID` | `sCODE_JOB_FUNCTION` | Global | No | No |  | Summary Information / Management |
| Manager Name | `PEMgr_MemberID` | `sTYPE_MEMBER` | Global | No | No |  | Summary Information / Management |
| Manager Title | `PEMgr_CodeJobTitleID` | `sCODE_JOB_TITLE` | Global | No | No |  | Summary Information / Management |
| Modified By | `PEMgr_ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Summary Information / Management |
| Modified Date | `PEMgr_ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Summary Information / Management |
| User Class | `PEMgr_CodeUserClassID` | `sCODE_USER_CLASS` | Global | No | No |  | Summary Information / Management |
| Address | `HTMLAddress` | `sTYPE_TEXT` | Global | No | No |  | Summary Information / Membership |
| Billing Rate 1 | `BillRate1` | `sTYPE_MONEY` | Global | No | No |  | Summary Information / Membership |
| Billing Rate 2 | `BillRate2` | `sTYPE_MONEY` | Global | No | No |  | Summary Information / Membership |
| Employer | `EmployerID` | `sTYPE_EMPLOYER` | Global | No | No |  | Summary Information / Membership |
| Entity | `ProjectEntityID` | `sTYPE_PROJECT_ENTITY` | Global | Yes | No |  | Summary Information / Membership |
| Entity Assigned Job Title List | `AssignedCodeJobTitleIDList` | `sCODE_JOB_TITLE` | Global | No | No |  | Summary Information / Membership |
| Entity Job Title List | `CodeJobTitleIDList` | `sCODE_JOB_TITLE` | Global | No | No |  | Summary Information / Membership |
| Is Manager? | `IsManager` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Summary Information / Membership |
| Job Function | `CodeJobFunctionID` | `sCODE_JOB_FUNCTION` | Global | No | No |  | Summary Information / Membership |
| Job Title | `CodeJobTitleID` | `sCODE_JOB_TITLE` | Global | No | No |  | Summary Information / Membership |
| Link Member Project Entity RecID | `LinkMemberProjectEntityID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Summary Information / Membership |
| Member | `MemberID` | `sTYPE_MEMBER` | Global | Yes | No |  | Summary Information / Membership |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Summary Information / Membership |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Summary Information / Membership |
| User Class | `CodeUserClassID` | `sCODE_USER_CLASS` | Global | No | No |  | Summary Information / Membership |
