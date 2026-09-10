# Prototype — Data Fields

A standardized store/facility design template used for rollout programs — approved flag, average project cost/duration, and default construction type/distribution center. 15 Global fields under its own Prototype group.

**Table Association:** `Prototype` &nbsp;·&nbsp; **Total fields:** 15 (Global: 15, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Approved? | `IsApproved` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Prototype / Prototype Info |
| Average Cost Of Project | `AverageCostOfProject` | `sTYPE_MONEY` | Global | Yes | No |  | Prototype / Prototype Info |
| Average Duration Of Project (months) | `AverageDurationOfProject` | `sTYPE_NUMBER` | Global | Yes | No |  | Prototype / Prototype Info |
| Building Area Unit | `CodeBuildingAreaUnitID` | `sCODE_BUILDING_AREA_UNIT` | Global | Yes | No |  | Prototype / Prototype Info |
| Default Construction Type | `CodeConstructionTypeID` | `sCODE_CONSTRUCTION_TYPE` | Global | No | No |  | Prototype / Prototype Info |
| Default Distribution Center | `CodeDistributionCenterID` | `sCODE_DISTRIBUTION_CENTER` | Global | No | No |  | Prototype / Prototype Info |
| Default Project Type | `CodeProjectTypeID` | `sCODE_PROJECT_TYPE` | Global | No | No |  | Prototype / Prototype Info |
| Default Rentable Area | `DefaultRentableArea` | `sTYPE_AREA` | Global | Yes | No |  | Prototype / Prototype Info |
| Default Usable Area | `DefaultUsableArea` | `sTYPE_AREA` | Global | Yes | No |  | Prototype / Prototype Info |
| Description | `ProjectDescription` | `sTYPE_TEXT` | Global | No | No |  | Prototype / Prototype Info |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Prototype / Prototype Info |
| Portfolio | `ProgramID` | `sTYPE_PROGRAM` | Global | Yes | No |  | Prototype / Prototype Info |
| Prototype ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Prototype / Prototype Info |
| Prototype Name | `PrototypeName` | `sTYPE_TEXT` | Global | Yes | No |  | Prototype / Prototype Info |
| Prototype RecID | `PrototypeID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Prototype / Prototype Info |
