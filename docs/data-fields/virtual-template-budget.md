# VirtualTemplateBudget — Data Fields

Near-identical structure to VirtualTemplateBudgetOption; the two likely back two different UI pickers (a single-select field vs. an option list) over the same underlying budget template metadata. 16 Global fields under Company Items.

**Table Association:** `VirtualTemplateBudget` &nbsp;·&nbsp; **Total fields:** 16 (Global: 16, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Budget Template Description | `Description` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Budget Template |
| Budget Template Name | `TemplateName` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Budget Template |
| Budget Template Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Company Items / Budget Template |
| Budget Template RecID | `TemplateID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Budget Template |
| Budget Template Valid for Cap Program? | `IsValidForCapProgram` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Budget Template |
| Budget Template Valid for Cap Project? | `IsValidForCapProject` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Budget Template |
| Budget Template Valid for Equipment Contract? | `IsValidForEquipContract` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Budget Template |
| Budget Template Valid for Facility? | `IsValidForFacility` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Budget Template |
| Budget Template Valid for Location? | `IsValidForLocation` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Budget Template |
| Budget Template Valid for Open Project? | `IsValidForOpenProject` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Budget Template |
| Budget Template Valid for Parcel? | `IsValidForParcel` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Budget Template |
| Budget Template Valid for Portfolio? | `IsValidForPortfolio` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Budget Template |
| Budget Template Valid for Potential Project? | `IsValidForPotentialProject` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Budget Template |
| Budget Template Valid for Prototype? | `IsValidForPrototype` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Budget Template |
| Budget Template Valid for RE Contract? | `IsValidForContract` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Budget Template |
| Lock All Budget Groups | `LockAllBudgetGroups` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Budget Template |
