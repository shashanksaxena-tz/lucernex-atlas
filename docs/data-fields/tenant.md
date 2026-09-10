# Tenant — Data Fields

The sub-tenant/occupant record under a Facility (for landlords or sub-lease scenarios) — headcount capacity fields (Capacity #1-4, calcTotalHeadcount) and a Contract linkage. 41 Global fields under Facility.

**Table Association:** `Tenant` &nbsp;·&nbsp; **Total fields:** 41 (Global: 41, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Capacity #1 | `Capacity1` | `sTYPE_NUMBER` | Global | No | No |  | Facility / Tenant |
| Capacity #2 | `Capacity2` | `sTYPE_NUMBER` | Global | No | No |  | Facility / Tenant |
| Capacity #3 | `Capacity3` | `sTYPE_NUMBER` | Global | No | No |  | Facility / Tenant |
| Capacity #4 | `Capacity4` | `sTYPE_NUMBER` | Global | No | No |  | Facility / Tenant |
| City | `City` | `sTYPE_TEXT` | Global | No | No |  | Facility / Tenant |
| Company | `CompanyID` | `sTYPE_EMPLOYER` | Global | No | No |  | Facility / Tenant |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | No | No |  | Facility / Tenant |
| Country | `CountryID` | `sTYPE_COUNTRY` | Global | No | No |  | Facility / Tenant |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Facility / Tenant |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Facility / Tenant |
| Description | `Description` | `sTYPE_TEXT` | Global | No | No |  | Facility / Tenant |
| Effective Date | `EffectiveDate` | `sTYPE_DATE` | Global | No | No |  | Facility / Tenant |
| Head Count #1 | `HeadCount1` | `sTYPE_NUMBER` | Global | No | No |  | Facility / Tenant |
| Head Count #2 | `HeadCount2` | `sTYPE_NUMBER` | Global | No | No |  | Facility / Tenant |
| Head Count #3 | `HeadCount3` | `sTYPE_NUMBER` | Global | No | No |  | Facility / Tenant |
| Head Count #4 | `HeadCount4` | `sTYPE_NUMBER` | Global | No | No |  | Facility / Tenant |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Facility / Tenant |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Facility / Tenant |
| Move In Date | `MoveInDate` | `sTYPE_DATE` | Global | No | No |  | Facility / Tenant |
| Move Out Date | `MoveOutDate` | `sTYPE_DATE` | Global | No | No |  | Facility / Tenant |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Facility / Tenant |
| Organization | `OrganizationID` | `sTYPE_ORGANIZATION` | Global | No | No |  | Facility / Tenant |
| Postal Code | `PostalCode` | `sTYPE_POSTALCODE` | Global | No | No |  | Facility / Tenant |
| Rev Number | `RevNumber` | `sTYPE_NUMBER` | Global | No | No |  | Facility / Tenant |
| Space | `SpaceID` | `sTYPE_SPACE` | Global | Yes | No |  | Facility / Tenant |
| State | `IStateProvinceCountryID` | `sTYPE_STATE_PROVINCE` | Global | No | No |  | Facility / Tenant |
| State Province | `StateProvince` | `sTYPE_TEXT` | Global | No | No |  | Facility / Tenant |
| Street Address #1 | `StreetAddress1` | `sTYPE_TEXT` | Global | No | No |  | Facility / Tenant |
| Street Address #2 | `StreetAddress2` | `sTYPE_TEXT` | Global | No | No |  | Facility / Tenant |
| Street Address #3 | `StreetAddress3` | `sTYPE_TEXT` | Global | No | No |  | Facility / Tenant |
| Street Address #4 | `StreetAddress4` | `sTYPE_TEXT` | Global | No | No |  | Facility / Tenant |
| Tenant Category | `CodeTenantCategoryID` | `sCODE_TENANT_CATEGORY` | Global | No | No |  | Facility / Tenant |
| Tenant ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Facility / Tenant |
| Tenant Group | `CodeTenantGroupID` | `sCODE_TENANT_GROUP` | Global | No | No |  | Facility / Tenant |
| Tenant Name | `TenantName` | `sTYPE_TEXT` | Global | Yes | No |  | Facility / Tenant |
| Tenant RecID | `TenantID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Facility / Tenant |
| Tenant Status | `CodeTenantStatusID` | `sCODE_TENANT_STATUS` | Global | No | No |  | Facility / Tenant |
| Tenant Type | `CodeTenantTypeID` | `sCODE_TENANT_TYPE` | Global | No | No |  | Facility / Tenant |
| Tenant Use | `CodeTenantUseID` | `sCODE_TENANT_USE` | Global | No | No |  | Facility / Tenant |
| Total Capacity | `TotalCapacity` | `sTYPE_NUMBER` | Global | No | No |  | Facility / Tenant |
| calcTotalHeadcount | `math_calcTotalCapacity_1` | `sTYPE_MATH_OPERATION` | Global | No | No |  | Facility / Tenant |
