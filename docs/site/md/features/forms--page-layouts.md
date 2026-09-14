# Forms & Page Layouts

Configuration of what users see. A page presents a record that already exists. A form is something else entirely: a tenant-authored request type with one layout per workflow step. A custom list is a form without the workflow. Lx never built a form builder; it built one ticket record and let the tenant define its subtypes.

## Who it is for

*Derived · fact · source: `docs/features/README.md`*

Configuration administrators. This is the surface on which the product is assembled, and the one a rebuild has to reproduce most faithfully.

## Where it is used

*Observed · fact · source: `docs/data-model/screen-routing.md`*

Manage Page Layouts and Manage Forms, plus the two JSP renderers that serve 56% of all end-user screens from what those editors produce.

## Form = Issue Type

*Observed · capability · source: `docs/modules/layouts-and-forms/forms-vs-pages-vs-layouts.md`*

A form is literally a value in the tenant's request-type list - which is why Manage Forms opens the same editor as every admin-controlled value list. Every request-shaped feature in the product is the same table with a different subtype value.

## Layouts bound to steps

*Observed · capability · source: `docs/data-model/screen-routing.md`*

Two renderer screens serve 56% of all end-user screens between them - the detail and list renderers. The layout is the runtime contract between the data model and the screen.

## One value-list editor

*Observed · capability · source: `docs/data-model/code-table-registry.md`*

Everything an admin controls is one editor: 207 platform-fixed value lists whose values you may edit but whose catalogue you may not extend, plus tenant-authored lists which support cascading values.

## Page Layouts

*Observed · fact · source: `docs/features/page-layouts/README.md`*

What the page layouts manual settles: Navigation layouts and firm layouts are disjoint id populations; SEP/SUB/LIST composition; the publish-and-fork model (80 shared names, 0 shared ids); layouts carry action buttons, not just fields. Biggest open question: How the runtime picks between 5 layouts on one navigation node.

## Manual contents

*Observed · fact · source: `docs/features/page-layouts/README.md`*

The page layouts manual is organised as: Two tiers of PageLayoutID, in one table; How the three modes compose; The publish-and-fork model; What a layout contains; The storage, recovered; Layout Changes — the vendor's own unexplained tool, explained; Conditional fields — used, and the stored shape is now known; What this means for ASG Edge+. Read it rather than this node when you need the detail — this is the index.

## Evidence

*Observed · fact · source: `features/page-layouts/README.md`*

Written up in features/page-layouts/README.md. 131 screen captures on disk, under docs/assets/screenshots/page-layouts, docs/assets/screenshots/forms, docs/assets/screenshots/bbw-admin, docs/assets/screenshots/af-admin — the screens themselves, not a description of them. 125 of them are cited by name in the documentation, which is what ties a capture to the screen it shows. 1 are held back from being shown here: they contain a named individual, and whether those images get redacted is an open decision. They still count as evidence — the file is on disk and named in the docs — they are simply not thumbnailed.

![Related Fields sidebar for the Facility layout, listing Company Items, Location, Milestones, Pro Forma Lease, Program Summary Information, Prototype, Purchase Management, Schedule, Site Survey, Summary Information — Contract is absent](../../assets/screenshots/page-layouts/facility-related-fields-no-contract.jpg)
![ASG Facility Summary layout showing a Contracts section containing "ASG Contract List (One to Many List)"](../../assets/screenshots/page-layouts/facility-summary-contracts-one-to-many-list.jpg)
![Add item for a new Summary Page, including "Initialize layout from existing layout"](../../assets/screenshots/page-layouts/page-layouts-add-item-modal.png)
![The layout editor's Available Fields tree with Contract -> Custom Lists expanded. Only the Contract-scoped lists appear -- Default Log, Funds, Operating Expenses, Reconciliation Log, Savings Log. Client Request Log is absent because its primary table is Portfolio.](../../assets/screenshots/page-layouts/page-layouts-available-fields-custom-lists-link.png)
![The layout editor for ASG Contract Summary. The asterisked, red-labelled fields are layer 3 in the act: Contract Status *, Contract Group *, Contract Type *, Contract Category *, Contract ID *, Contract Name *, Currency Type *, Location *, Lease Status *, and six of the Contract Critical Dates. Contract Name is required in layers 1 and 2 both; Contract Status and Location are required in neither, and Contract carries only 7 column-required fields and 3 catalog-required leaves in total -- so most of the asterisks on this screen are unaccounted for by the two layers whose storage is known.](../../assets/screenshots/page-layouts/page-layouts-conditional-field-associations.png)
![ASG Contract Payments — Edit Layout, sectioned detail form with action buttons](../../assets/screenshots/page-layouts/page-layouts-contract-payments-edit-layout.png)
![The List Layout tab on ASG Contract Payments, table PaymentTransaction. Thirteen column placements run left to right. Eight are red and asterisked -- Effective Date *, Effective End Date (Coverage End Date) *, Expense Group *, Expense Type *, Invoice Amount *, Primary Tax (Tax Amount #1) *, Due Date *, Vendor * -- and five are plain. The last chip is green and reads (Searchable, Hidden in grid): a placement that exists to be searched on and is not displayed.](../../assets/screenshots/page-layouts/page-layouts-contract-payments-list-layout.png)
![Edit item — Parent Tab tree, Primary Table, Allow Edit, Portfolio scope](../../assets/screenshots/page-layouts/page-layouts-edit-item-parent-tab-tree.png)
![List Layout not applicable for ASG Contract Summary](../../assets/screenshots/page-layouts/page-layouts-list-layout-not-applicable.png)
![page-layouts-setup-pages.png](../../assets/screenshots/page-layouts/page-layouts-setup-pages.png)
![ASG Contract Header sub-page — raw field grid, no title bar](../../assets/screenshots/page-layouts/page-layouts-subpage-contract-header.png)
![Related Fields drilled into Facility's Facility Info subgroup, listing dozens of native Facility fields](../../assets/screenshots/page-layouts/related-fields-facility-info-expanded.jpg)
![Related Fields sidebar expanded, showing Company Items, Contract, Facility, Location, Milestones, Program Summary Information, Schedule, Summary Information](../../assets/screenshots/page-layouts/related-fields-top-level-list.jpg)
![Manage Forms expanded — every form type's layouts](../../assets/screenshots/forms/manage-forms-expanded-all-layouts.jpg)
![Manage Forms — four form types, each with edit fields and add layout](../../assets/screenshots/forms/manage-forms-index.jpg)
![2. Administration tools (57)](../../assets/screenshots/bbw-admin/01-manage-company.jpg)
![2. Administration tools (57)](../../assets/screenshots/bbw-admin/02-manage-schedule-templates.jpg)
![2. Administration tools (57)](../../assets/screenshots/bbw-admin/03-manage-milestone-timeline.jpg)
![2. Administration tools (57)](../../assets/screenshots/bbw-admin/04-manage-binder-templates.jpg)
![Manage Forms. Every row offers edit | delete | edit fields | add layout -- the identical action set Manage Custom Lists offers, because they are two views over one code table discriminated by CodeIssueType.IsWorkFlow.](../../assets/screenshots/bbw-admin/05-manage-forms.jpg)
![2. Administration tools (57)](../../assets/screenshots/bbw-admin/06-manage-custom-lists.jpg)
![2. Administration tools (57)](../../assets/screenshots/bbw-admin/07-manage-parts-and-inventory.jpg)
![Manage Work Flows in BBW, all 13 rows -- the footer reads Displaying 1 - 13 of 13. Two things to read off it. The per-row actions are edit | delete | add task step | add form step, so a Task step is offered on every template and taken on none. And the Description column, empty on nine rows, carries a free-text archive note on exactly the versioned ones.](../../assets/screenshots/bbw-admin/08-manage-work-flows.jpg)
![2. Administration tools (57)](../../assets/screenshots/bbw-admin/09-manage-page-layouts.jpg)

*1 further capture(s) withheld: they contain a named individual and the redaction decision is open.*

## Open questions (34)

*Inferred · group*

34 things nobody has confirmed for this feature. Each one is work somebody has to do before the feature can be rebuilt with confidence; they are carried here rather than resolved by guessing. Click one for the question and the document that raised it.

### Which column actually

*Inferred · question · source: `docs/modules/layouts-and-forms/README.md`*

Which column actually persists json.conditionalFieldsConfig? The dialog posts it; the destination is not observed. PageLayoutField.DisplayOptionJSON is the strongest candidate — it is an optional per-placement JSON textarea, and a subPage_<id> target *is* a PageLayoutField row whose SubPageLayoutID holds that id. PageLayoutField.JSONConfigText and PageLayout.JSONConfigText are the alternatives. Settling this settles migration. Nobody has confirmed this. Recorded in modules/layouts-and-forms/README.md, under the Configuration, Layouts & Forms area. Until it is settled, anything built on the assumption is a guess.

### Is PageLayoutFilter

*Inferred · question · source: `docs/modules/layouts-and-forms/README.md`*

Is PageLayoutFilter the showInList=1 surface? Its IsListFilter flag and the layout builder's showInList=1 parameter for layoutMode list/budget describe the same distinction from two directions. If so, list-layout conditions are normalised rows while edit-layout conditions are a JSON blob — an odd asymmetry worth confirming before copying either. Nobody has confirmed this. Recorded in modules/layouts-and-forms/README.md, under the Configuration, Layouts & Forms area. Until it is settled, anything built on the assumption is a guess.

### Where is per placement

*Inferred · question · source: `docs/modules/layouts-and-forms/README.md`*

Where is per-placement required-ness stored? PageLayoutField has no IsRequired column, yet the vendor states the flag is set "from the Manage Page Layouts section … or the Manage Forms page" and is read-only on the field catalog (_xlsx_feature_list.txt line 938). The Show and Require action makes *conditional* required-ness clear; *unconditional* per-placement required-ness is not accounted for. Nobody has confirmed this. Recorded in modules/layouts-and-forms/README.md, under the Configuration, Layouts & Forms area. Until it is settled, anything built on the assumption is a guess.

### What is the complete

*Inferred · question · source: `docs/modules/layouts-and-forms/README.md`*

What is the complete PageLayoutType and OutputType vocabulary? Five mode values and three layoutMode values are observed; the schema implies at least nine more layout kinds. This sets the scope of PAGE-LAYOUTS-01. PageLayout.EquivalentPLTypes would enumerate them. Nobody has confirmed this. Recorded in modules/layouts-and-forms/README.md, under the Configuration, Layouts & Forms area. Until it is settled, anything built on the assumption is a guess.

### Does Program level

*Inferred · question · source: `docs/modules/layouts-and-forms/README.md`*

Does Program-level setup-page assignment override Firm-level? 18 sTYPE_PAGE_LAYOUT columns on Program against 11 on Firm; only the Firm screen has been seen. Doubles the scope of layout assignment if true. Nobody has confirmed this. Recorded in modules/layouts-and-forms/README.md, under the Configuration, Layouts & Forms area. Until it is settled, anything built on the assumption is a guess.

### How is a layout s

*Inferred · question · source: `docs/modules/layouts-and-forms/README.md`*

How is a layout's Portfolio/Capital-Program scope stored? The required chip control is observed on the layout edit dialog; no column in either offline artefact holds it. Presumed link table. Nobody has confirmed this. Recorded in modules/layouts-and-forms/README.md, under the Configuration, Layouts & Forms area. Until it is settled, anything built on the assumption is a guess.

### How are action buttons

*Inferred · question · source: `docs/modules/layouts-and-forms/README.md`*

How are action buttons stored on a layout? No column declares one, yet Approve Payments, Generate Rent, Extend Contracts and the "(Run Report Action)" buttons are placed, reordered and deleted exactly like fields. Nobody has confirmed this. Recorded in modules/layouts-and-forms/README.md, under the Configuration, Layouts & Forms area. Until it is settled, anything built on the assumption is a guess.

### What does Layout

*Inferred · question · source: `docs/modules/layouts-and-forms/README.md`*

What does Layout Changes (ShowLayoutChanges.jsp) record? ASG has explicitly asked for an explanation of this tool (_xlsx_feature_list.txt line 44). Nobody has confirmed this. Recorded in modules/layouts-and-forms/README.md, under the Configuration, Layouts & Forms area. Until it is settled, anything built on the assumption is a guess.

### Are layouts versioned

*Inferred · question · source: `docs/modules/layouts-and-forms/README.md`*

Are layouts versioned at all? VersionAdded/VersionModified exist on the *field* registry but not on PageLayout. Without layout versioning a historical form instance cannot be faithfully re-rendered, and Lx's only mitigation — Issue.LastPageLayoutID — is a single most-recent pointer, so it does not reconstruct what each approver saw at each step. Nobody has confirmed this. Recorded in modules/layouts-and-forms/README.md, under the Configuration, Layouts & Forms area. Until it is settled, anything built on the assumption is a guess.

### Is there a Global

*Inferred · question · source: `docs/modules/layouts-and-forms/README.md`*

Is there a Global/platform-wide Custom List concept? None observed; only Firm scope. Nobody has confirmed this. Recorded in modules/layouts-and-forms/README.md, under the Configuration, Layouts & Forms area. Until it is settled, anything built on the assumption is a guess.

### What is the populated

*Inferred · question · source: `docs/modules/layouts-and-forms/conditional-fields.md`*

What is the populated JSON shape of json.conditionalFieldsConfig? The captured target had no rules. Find a layout that already has conditional rules applied — use the **Conditions Applied** checkbox across layouts, or the Show Conditional Field Associations dialog, which lists Field / Rule / Criteria for any layout that has them — and read the hidden field. Until this is done, the storage format is inferred, not known. Nobody has confirmed this. Recorded in modules/layouts-and-forms/conditional-fields.md, under the Configuration, Layouts & Forms area. Until it is settled, anything built on the assumption is a guess.

### Is evaluation server

*Inferred · question · source: `docs/modules/layouts-and-forms/conditional-fields.md`*

Is evaluation server-side at render, or client-side on change? This determines whether a rule can depend on a value the user has just typed but not yet saved. Decisive for UX and for where the rule engine lives. Testable by opening an end-user Contract page with a rule applied and watching for a network round-trip when the driver field changes. Nobody has confirmed this. Recorded in modules/layouts-and-forms/conditional-fields.md, under the Configuration, Layouts & Forms area. Until it is settled, anything built on the assumption is a guess.

### What does Show and

*Inferred · question · source: `docs/modules/layouts-and-forms/conditional-fields.md`*

What does Show and Require do at runtime when the target is a sub-page rather than a single field — does it require every field in the section, or only those already marked required?. Nobody has confirmed this. Recorded in modules/layouts-and-forms/conditional-fields.md, under the Configuration, Layouts & Forms area. Until it is settled, anything built on the assumption is a guess.

### How does the list

*Inferred · question · source: `docs/modules/layouts-and-forms/conditional-fields.md`*

How does the list-layout conditional surface (showInList=1) differ, given the dialog's own heading says conditions do not affect list layouts?. Nobody has confirmed this. Recorded in modules/layouts-and-forms/conditional-fields.md, under the Configuration, Layouts & Forms area. Until it is settled, anything built on the assumption is a guess.

### Are Date drivers

*Inferred · question · source: `docs/modules/layouts-and-forms/conditional-fields.md`*

Are Date drivers genuinely unsupported, or absent only from this layout? The layout builder defines hideShowDateFieldsForCriteria and hideShowNumberCriteriaFields, which implies date-specific criteria inputs exist somewhere. Check a layout whose primary table is date-heavy. Nobody has confirmed this. Recorded in modules/layouts-and-forms/conditional-fields.md, under the Configuration, Layouts & Forms area. Until it is settled, anything built on the assumption is a guess.

### What is formFieldType

*Inferred · question · source: `docs/modules/layouts-and-forms/conditional-fields.md`*

What is formFieldType, observed as 0? Likely a discriminator distinguishing field targets from sub-page targets. Nobody has confirmed this. Recorded in modules/layouts-and-forms/conditional-fields.md, under the Configuration, Layouts & Forms area. Until it is settled, anything built on the assumption is a guess.

### What does a Task step

*Inferred · question · source: `docs/modules/layouts-and-forms/forms-vs-pages-vs-layouts.md`*

What does a Task step look like? All 22 steps observed across four workflows are Form steps. add task step exists but no task step is configured in this tenant. Its field set is unknown, and WorkFlowTemplateStep has 55 fields — far more than this grid shows. Nobody has confirmed this. Recorded in modules/layouts-and-forms/forms-vs-pages-vs-layouts.md, under the Configuration, Layouts & Forms area. Until it is settled, anything built on the assumption is a guess.

### Is branching possible

*Inferred · question · source: `docs/modules/layouts-and-forms/forms-vs-pages-vs-layouts.md`*

Is branching possible? The grid is strictly ordinal. Determine whether WorkFlowTemplateStepAction (37 fields) expresses conditional routing, and how KickOffMethod's four trigger types are configured. Nobody has confirmed this. Recorded in modules/layouts-and-forms/forms-vs-pages-vs-layouts.md, under the Configuration, Layouts & Forms area. Until it is settled, anything built on the assumption is a guess.

### What is Ad Hoc

*Inferred · question · source: `docs/modules/layouts-and-forms/forms-vs-pages-vs-layouts.md`*

What is Ad Hoc approval? Used on Rent Payment Review/Approval step 2 and User Request step 2, with no approver listed. Runtime-chosen approver, presumably. Nobody has confirmed this. Recorded in modules/layouts-and-forms/forms-vs-pages-vs-layouts.md, under the Configuration, Layouts & Forms area. Until it is settled, anything built on the assumption is a guess.

### What does edit fields

*Inferred · question · source: `docs/modules/layouts-and-forms/forms-vs-pages-vs-layouts.md`*

What does edit fields on a Form type show, and does it use the same field editor as Custom Lists (which was itself blocked by the Lx-namespace dependency now understood — see conditional-fields.md for the working method to reach it)?. Nobody has confirmed this. Recorded in modules/layouts-and-forms/forms-vs-pages-vs-layouts.md, under the Configuration, Layouts & Forms area. Until it is settled, anything built on the assumption is a guess.

### What is Collaborator

*Inferred · question · source: `docs/modules/layouts-and-forms/forms-vs-pages-vs-layouts.md`*

What is Collaborator Job Titles, a column on the workflow grid that is empty for all four?. Nobody has confirmed this. Recorded in modules/layouts-and-forms/forms-vs-pages-vs-layouts.md, under the Configuration, Layouts & Forms area. Until it is settled, anything built on the assumption is a guess.

### Enumerate every

*Inferred · question · source: `docs/modules/layouts-and-forms/forms-vs-pages-vs-layouts.md`*

Enumerate every layoutMode value, and confirm whether Form layouts use a distinct one. Nobody has confirmed this. Recorded in modules/layouts-and-forms/forms-vs-pages-vs-layouts.md, under the Configuration, Layouts & Forms area. Until it is settled, anything built on the assumption is a guess.

### How does a step

*Inferred · question · source: `docs/modules/layouts-and-forms/forms-vs-pages-vs-layouts.md`*

How does a step transition? What records the decision, what happens on rejection, and is there a rollback or re-open path?. Nobody has confirmed this. Recorded in modules/layouts-and-forms/forms-vs-pages-vs-layouts.md, under the Configuration, Layouts & Forms area. Until it is settled, anything built on the assumption is a guess.

### How does the runtime

*Inferred · question · source: `docs/features/page-layouts/README.md`*

~~How does the runtime pick between multiple layouts on one navigation node?~~ **Fully answered.** They form an ordered chain via PreviousPageLayoutID, and the chain renders as a layout-selector dropdown at the top right of the content area. The runtime renders the head and offers the rest as options. What remains is trivial by comparison: whether the dropdown lists the chain in PreviousPageLayoutID order, which needs one screenshot of the open list. Nobody has confirmed this. Recorded in features/page-layouts/README.md, under the Forms & Page Layouts area. Until it is settled, anything built on the assumption is a guess.

### What do DisplayOption1

*Inferred · question · source: `docs/features/page-layouts/README.md`*

What do DisplayOption1 / DisplayOption2 encode? They track placement kind on the one layout fully examined, and every ordinary data field there is all-zero. They remain the **last standing** candidate for per-placement required-ness after three others were eliminated, but the evidence is a partial negative from a layout that may have no required fields at all. Test and reasoning in ../required-and-validation/. Nobody has confirmed this. Recorded in features/page-layouts/README.md, under the Forms & Page Layouts area. Until it is settled, anything built on the assumption is a guess.

### Does Layout Changes

*Inferred · question · source: `docs/features/page-layouts/README.md`*

Does Layout Changes show history if the date is widened? It returned nothing with the date defaulted to today. A date set years back would show whether change history is actually retained. Nobody has confirmed this. Recorded in features/page-layouts/README.md, under the Forms & Page Layouts area. Until it is settled, anything built on the assumption is a guess.

### What is

*Inferred · question · source: `docs/features/page-layouts/README.md`*

What is PageLayoutField.JSONConfigText's full key vocabulary? 29 keys observed, but only across the layouts sampled. A key governing required-ness may exist and be unused here. Nobody has confirmed this. Recorded in features/page-layouts/README.md, under the Forms & Page Layouts area. Until it is settled, anything built on the assumption is a guess.

### What are PageLayout

*Inferred · question · source: `docs/features/page-layouts/README.md`*

What are PageLayout.PageLayoutType and OutputType? Single-character discriminators (V, L observed). Their relationship to the SEP / SUB / LIST modes is unestablished. Nobody has confirmed this. Recorded in features/page-layouts/README.md, under the Forms & Page Layouts area. Until it is settled, anything built on the assumption is a guess.

### What renders the

*Inferred · question · source: `docs/features/page-layouts/README.md`*

What renders the parentless top-level lists ASG Contract List, ASG Facility List, ASG Covenant List View?. Nobody has confirmed this. Recorded in features/page-layouts/README.md, under the Forms & Page Layouts area. Until it is settled, anything built on the assumption is a guess.

### What are

*Inferred · question · source: `docs/features/page-layouts/README.md`*

What are PageLayoutFilter's columns? BBW holds zero rows, so the serializer returns nothing. Needs a tenant that uses run-mode filters. Nobody has confirmed this. Recorded in features/page-layouts/README.md, under the Forms & Page Layouts area. Until it is settled, anything built on the assumption is a guess.

### Is the declared schema

*Inferred · question · source: `docs/features/page-layouts/README.md`*

Is the declared schema wider than REST returned? The serializer emits only populated columns, so PageLayout at 17 and PageLayoutField at 20 are lower bounds. Nobody has confirmed this. Recorded in features/page-layouts/README.md, under the Forms & Page Layouts area. Until it is settled, anything built on the assumption is a guess.

### What do the ASG Lease

*Inferred · question · source: `docs/features/page-layouts/README.md`*

What do the ASG Lease Abstract - * layouts render? Never opened. Nobody has confirmed this. Recorded in features/page-layouts/README.md, under the Forms & Page Layouts area. Until it is settled, anything built on the assumption is a guess.

### Can a SUB layout embed

*Inferred · question · source: `docs/features/page-layouts/README.md`*

Can a SUB layout embed another SUB layout? Structurally possible via SubPageLayoutID; the depth actually used is unknown. Nobody has confirmed this. Recorded in features/page-layouts/README.md, under the Forms & Page Layouts area. Until it is settled, anything built on the assumption is a guess.

### What is the full

*Inferred · question · source: `docs/features/page-layouts/README.md`*

What is the full inventory of placeable action buttons, and is it per entity or global? The Actions tab of Manage Security is the likeliest place to find it — see ../security-access/. Nobody has confirmed this. Recorded in features/page-layouts/README.md, under the Forms & Page Layouts area. Until it is settled, anything built on the assumption is a guess.

## Rules (84)

*Derived · group*

Every numbered rule the docs corpus records for this feature, named by a short summary. Click one: the panel opens with its ID, the full statement, and a link to the complete rule page.

### LAY R 018 from live — [LAY-R-001](../rules/LAY-R-001.md)

*Derived · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**Two of those bear repeating here because everything below assumes them: - `LAY-R-011` — a conditional rule set declares exactly one action: `SHOW`, `SHOW_AND_REQUIRE` or `HIDE`. Visibility and required-ness are one decision, not two.**

|  |  |
|---|---|
| Stated as | Range |
| Stated as | Subject |
| Stated as | Owning document |
| Stated as | `LAY-R-001` … `LAY-R-009` |
| Stated as | Forms, form types, layout-per-workflow-step, the Form ⇄ Work Flow 1:1 relationship, step and approval vocabulary |
| Stated as | forms-vs-pages-vs-layouts.md |

### The reconciliation — [LAY-R-002](../rules/LAY-R-002.md)

*Derived · rule · source: `docs/modules/layouts-and-forms/forms-vs-pages-vs-layouts.md`*

**A Page Layout presents a platform-defined entity. It does not define fields;.**

### The reconciliation — [LAY-R-003](../rules/LAY-R-003.md)

*Derived · rule · source: `docs/modules/layouts-and-forms/forms-vs-pages-vs-layouts.md`*

**A Form is a tenant-defined record type registered in the code-table registry (`TableType=2035`), extended with its own field schema and one layout per workflow step.**

### The reconciliation — [LAY-R-004](../rules/LAY-R-004.md)

*Derived · rule · source: `docs/modules/layouts-and-forms/forms-vs-pages-vs-layouts.md`*

**A Custom List is a tenant-defined record type with its own field schema and a layout, but no workflow.**

### The reconciliation — [LAY-R-005](../rules/LAY-R-005.md)

*Derived · rule · source: `docs/modules/layouts-and-forms/forms-vs-pages-vs-layouts.md`*

**A Form type declares attachability as a boolean per entity kind (Portfolio, RE Contract, Facility, …). A request may only be raised against an entity whose flag is set.**

### The reconciliation — [LAY-R-006](../rules/LAY-R-006.md)

*Derived · rule · source: `docs/modules/layouts-and-forms/forms-vs-pages-vs-layouts.md`*

**A Form type declares a sequence prefix and whether numbering is global.**

### The reconciliation — [LAY-R-007](../rules/LAY-R-007.md)

*Derived · rule · source: `docs/modules/layouts-and-forms/forms-vs-pages-vs-layouts.md`*

**Every Form type has exactly one Work Flow, identified by the same name.**

### The reconciliation — [LAY-R-008](../rules/LAY-R-008.md)

*Derived · rule · source: `docs/modules/layouts-and-forms/forms-vs-pages-vs-layouts.md`*

**A Work Flow is an ordered sequence of steps, each of type `Form` or `Task`. A `Form` step binds one of the form type's layouts.**

### The reconciliation — [LAY-R-009](../rules/LAY-R-009.md)

*Derived · rule · source: `docs/modules/layouts-and-forms/forms-vs-pages-vs-layouts.md`*

**A step resolves its approver by `Approval Level`: `Member`, `Job Title`, or `Ad Hoc`.**

### Rules for the ASG — [LAY-R-010](../rules/LAY-R-010.md)

*Derived · rule · source: `docs/modules/layouts-and-forms/conditional-fields.md`*

**A conditional rule set attaches to exactly one target, identified by a stable key. A target is either a single field or an entire sub-page section.**

### Rules for the ASG — [LAY-R-011](../rules/LAY-R-011.md)

*Derived · rule · source: `docs/modules/layouts-and-forms/conditional-fields.md`*

**A rule set declares exactly one action: `SHOW`, `SHOW_AND_REQUIRE`, or `HIDE`.**

### Rules for the ASG — [LAY-R-012](../rules/LAY-R-012.md)

*Derived · rule · source: `docs/modules/layouts-and-forms/conditional-fields.md`*

**A rule set declares exactly one quantifier over its predicates: `ALL` or `ANY`. Nesting is not supported.**

### Rules for the ASG — [LAY-R-013](../rules/LAY-R-013.md)

*Derived · rule · source: `docs/modules/layouts-and-forms/conditional-fields.md`*

**A predicate is a triple `(driverField, operator, value)`. Operators are constrained by the driver field's type: Dropdown → `IN`, `NOT_IN`, `IS_SPECIFIED`, `IS_NOT_SPECIFIED`;.**

### Rules for the ASG — [LAY-R-014](../rules/LAY-R-014.md)

*Derived · rule · source: `docs/modules/layouts-and-forms/conditional-fields.md`*

**`is any value` is the neutral state and contributes no predicate.**

### Rules for the ASG — [LAY-R-015](../rules/LAY-R-015.md)

*Derived · rule · source: `docs/modules/layouts-and-forms/conditional-fields.md`*

**Candidate driver fields are: the layout's primary table, plus every table reachable by a many-to-one FK from it, plus `ProjectEntity`.**

### Rules for the ASG — [LAY-R-016](../rules/LAY-R-016.md)

*Derived · rule · source: `docs/modules/layouts-and-forms/conditional-fields.md`*

**Only Dropdown, Number and Boolean fields may be drivers. Text and Date fields may not.**

### Rules for the ASG — [LAY-R-017](../rules/LAY-R-017.md)

*Derived · rule · source: `docs/modules/layouts-and-forms/conditional-fields.md`*

**Rule sets apply to the edit layout. List layouts carry a separate, independent rule surface.**

### Rules for the ASG — [LAY-R-018](../rules/LAY-R-018.md)

*Inferred · rule · source: `docs/modules/layouts-and-forms/conditional-fields.md`*

**`SHOW_AND_REQUIRE` makes the target mandatory for validation purposes only while its predicates match. (Inferred — the runtime behaviour was not observed, only the configuration option.).**

### from the schema — [LAY-R-100](../rules/LAY-R-100.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**Each carries an evidence label. Observed = seen in a capture or source artefact.**

|  |  |
|---|---|
| Stated as | # |
| Stated as | Rule |
| Stated as | Label |
| Stated as | Source |
| Stated as | LAY-R-101 |
| Stated as | Summary Pages, Sub-pages, List Layouts, Forms, Wizards, Map Popups, Reports and Dashboard tiles are all rows of one table, `PageLayout`. They are distinguished by discriminator columns, not by separate record types. |

### A Record identity — [LAY-R-101](../rules/LAY-R-101.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**Summary Pages, Sub-pages, List Layouts, Forms, Wizards, Map Popups, Reports and Dashboard tiles are all rows of one table, `PageLayout`. They are distinguished by discriminator columns, not by separate record types.**

|  |  |
|---|---|
| Stated as | Summary Pages, Sub-pages, List Layouts, Forms, Wizards, Map Popups, Reports and Dashboard tiles are all rows of one table, `PageLayout`. They are distinguished by discriminator columns, not by separate record types. |
| Stated as | Observed (schema) + Observed (008) |
| Stated as | `all-fields.csv`; 008 |

### A Record identity — [LAY-R-102](../rules/LAY-R-102.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**Every layout has exactly one required `PageLayoutType`, one required `OutputType`, and one required `PageLayoutName`. · Observed · `all-fields.csv`.**

|  |  |
|---|---|
| Stated as | Every layout has exactly one required `PageLayoutType`, one required `OutputType`, and one required `PageLayoutName`. |
| Stated as | Observed |
| Stated as | `all-fields.csv` |

### A Record identity — [LAY-R-103](../rules/LAY-R-103.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**A layout declares a single Primary Table (`PrimaryCodeSQLTableID`). Every field it may place is either a field of that table or a field reachable from it by a declared FK ("Related Fields").**

|  |  |
|---|---|
| Stated as | A layout declares a single Primary Table (`PrimaryCodeSQLTableID`). Every field it may place is either a field of that table or a field reachable from it by a declared FK ("Related Fields"). |
| Stated as | Observed (008, 009) |
| Stated as | 008, 009 |

### A Record identity — [LAY-R-104](../rules/LAY-R-104.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**A layout may be Global (platform-shipped, rendered with a `[Global Layout]` suffix) or Firm (tenant-authored). A tenant may keep the Global default per entity type or override it;.**

|  |  |
|---|---|
| Stated as | A layout may be Global (platform-shipped, rendered with a `[Global Layout]` suffix) or Firm (tenant-authored). A tenant may keep the Global default per entity type or override it; the two coexist in one selector list. |
| Stated as | Observed |
| Stated as | 008 § Setup Pages |

### A Record identity — [LAY-R-105](../rules/LAY-R-105.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**`AllowEdit = No` makes a layout read-only. `AllowUserCreate` separately controls whether end users may create records through it.**

|  |  |
|---|---|
| Stated as | `AllowEdit = No` makes a layout read-only. `AllowUserCreate` separately controls whether end users may create records through it. |
| Stated as | Observed (columns + 008 dialog) |
| Stated as | `all-fields.csv`; 008 |

### A Record identity — [LAY-R-106](../rules/LAY-R-106.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**A layout with a non-blank `URL` bypasses its own field configuration entirely and redirects to that system page. Vendor help text: "Leave blank for standard functionality.**

|  |  |
|---|---|
| Stated as | A layout with a non-blank `URL` bypasses its own field configuration entirely and redirects to that system page. Vendor help text: "Leave blank for standard functionality. To use a system page enter the url here, related layout fields will be ignored." |
| Stated as | Observed |
| Stated as | 008 |

### A Record identity — [LAY-R-107](../rules/LAY-R-107.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**A layout can be scoped to specific Portfolios/Capital Programs via a required multi-select, defaulting to All Portfolios/Capital Programs — the same control used for dropdown values. · Observed (UI);.**

|  |  |
|---|---|
| Stated as | A layout can be scoped to specific Portfolios/Capital Programs via a required multi-select, defaulting to All Portfolios/Capital Programs — the same control used for dropdown values. |
| Stated as | Observed (UI); storage not found in either artefact |
| Stated as | 008, 007 |

### B Composition — [LAY-R-110](../rules/LAY-R-110.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**A Summary Page is composed of Sub-pages, not authored monolithically. Each visible section corresponds to an independently-managed Sub-page layout.**

|  |  |
|---|---|
| Stated as | A Summary Page is composed of Sub-pages, not authored monolithically. Each visible section corresponds to an independently-managed Sub-page layout. Proven directly for `ASG Contract Header` ⇄ the "Contract Information" section of `ASG Contract Summary`. |
| Stated as | Observed |
| Stated as | 008 |

### B Composition — [LAY-R-111](../rules/LAY-R-111.md)

*Inferred · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**The inclusion mechanism is a `PageLayoutField` row whose `SubPageLayoutID` points at the child layout, positioned by the same coordinates as a field. · Inferred (high) · `all-fields.csv`.**

|  |  |
|---|---|
| Stated as | The inclusion mechanism is a `PageLayoutField` row whose `SubPageLayoutID` points at the child layout, positioned by the same coordinates as a field. |
| Stated as | Inferred (high) |
| Stated as | `all-fields.csv` |

### B Composition — [LAY-R-112](../rules/LAY-R-112.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**A section's title is supplied by the parent at the point of inclusion (`PageLayoutField.DisplayLabel`), not by the sub-page. A sub-page opened on its own renders with no title bar.**

|  |  |
|---|---|
| Stated as | A section's title is supplied by the parent at the point of inclusion (`PageLayoutField.DisplayLabel`), not by the sub-page. A sub-page opened on its own renders with no title bar. |
| Stated as | Observed (no title bar) + Inferred (mechanism) |
| Stated as | 008; `all-fields.csv` |

### B Composition — [LAY-R-113](../rules/LAY-R-113.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**A `PageLayoutField` row need not carry a field at all: it can be an embedded sub-layout (`SubPageLayoutID`) or literal copy (`StaticText`). · Observed (columns) · `all-fields.csv`.**

|  |  |
|---|---|
| Stated as | A `PageLayoutField` row need not carry a field at all: it can be an embedded sub-layout (`SubPageLayoutID`) or literal copy (`StaticText`). |
| Stated as | Observed (columns) |
| Stated as | `all-fields.csv` |

### B Composition — [LAY-R-114](../rules/LAY-R-114.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**A multi-step creation Wizard is a sequence of Sub-page layouts (`ASG Contract Wizard`, `Wizard Step 2`…`Step 5`), bound as an entity's creation flow via a Setup Page assignment. · Observed · 008.**

|  |  |
|---|---|
| Stated as | A multi-step creation Wizard is a sequence of Sub-page layouts (`ASG Contract Wizard`, `Wizard Step 2`…`Step 5`), bound as an entity's creation flow via a Setup Page assignment. |
| Stated as | Observed |
| Stated as | 008 |

### B Composition — [LAY-R-115](../rules/LAY-R-115.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**Layout ordering among siblings uses a previous-pointer chain (`PreviousPageLayoutID`, `PreviousID`) with a materialised `ComputedSequenceNumber`, not a plain integer sort key. · Observed (columns) · `all-fields.csv`.**

|  |  |
|---|---|
| Stated as | Layout ordering among siblings uses a previous-pointer chain (`PreviousPageLayoutID`, `PreviousID`) with a materialised `ComputedSequenceNumber`, not a plain integer sort key. |
| Stated as | Observed (columns) |
| Stated as | `all-fields.csv` |

### B Composition — [LAY-R-116](../rules/LAY-R-116.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**Layouts host placeable, reorderable business-action buttons (Approve Payments, Generate Rent, Extend Contracts, Alternate Rent Wizard, Copy Transaction, …) alongside fields, in the same grid with the same toolbars. A distinct button kind is labelled "(Run Report Action)".**

|  |  |
|---|---|
| Stated as | Layouts host placeable, reorderable business-action buttons (Approve Payments, Generate Rent, Extend Contracts, Alternate Rent Wizard, Copy Transaction, …) alongside fields, in the same grid with the same toolbars. A distinct button kind is labelled "(Run Report Action)". |
| Stated as | Observed |
| Stated as | 008 |

### B Composition — [LAY-R-117](../rules/LAY-R-117.md)

*Inferred · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**[BLOCKED] Action buttons are presumed to be `PageLayoutField` rows with no `ReportGroupAvailableFieldID`, identified by `DisplayOption`/`JSONConfigText`. No column declares a button.**

|  |  |
|---|---|
| Stated as | [BLOCKED] Action buttons are presumed to be `PageLayoutField` rows with no `ReportGroupAvailableFieldID`, identified by `DisplayOption`/`JSONConfigText`. No column declares a button. Check: read `PageLayoutField` rows for `ASG Contract Summary` (96289) via GraphQL Explorer. |
| Stated as | Inferred (low) |
| Stated as | — |

### C The Edit List — [LAY-R-120](../rules/LAY-R-120.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**A single `PageLayoutID` can carry both a detail Edit Layout and a grid List Layout, as two orthogonal facets of one record. Proven on `ASG Contract Payments` (96214, `PaymentTransaction`).**

|  |  |
|---|---|
| Stated as | A single `PageLayoutID` can carry both a detail Edit Layout and a grid List Layout, as two orthogonal facets of one record. Proven on `ASG Contract Payments` (96214, `PaymentTransaction`). |
| Stated as | Observed |
| Stated as | 008 |

### C The Edit List — [LAY-R-121](../rules/LAY-R-121.md)

*Inferred · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**The facet a placement belongs to is flagged by `PageLayoutField.IsInEditLayout`, and each facet has its own coordinate set — `EditRow/ColumnPosition`+`EditFieldWidth/Height` vs `ViewRow/ColumnPosition`+`ViewFieldWidth/Height`. · Inferred (high) · `all-fields.csv`.**

|  |  |
|---|---|
| Stated as | The facet a placement belongs to is flagged by `PageLayoutField.IsInEditLayout`, and each facet has its own coordinate set — `EditRow/ColumnPosition`+`EditFieldWidth/Height` vs `ViewRow/ColumnPosition`+`ViewFieldWidth/Height`. |
| Stated as | Inferred (high) |
| Stated as | `all-fields.csv` |

### C The Edit List — [LAY-R-122](../rules/LAY-R-122.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**A top-level parent entity with no natural "list of many inside one" view renders "List Layout not applicable for current layout type." This is a property of the target table, not a general one-facet-only rule. · Observed · 008.**

|  |  |
|---|---|
| Stated as | A top-level parent entity with no natural "list of many inside one" view renders "List Layout not applicable for current layout type." This is a property of the target table, not a general one-facet-only rule. |
| Stated as | Observed |
| Stated as | 008 |

### C The Edit List — [LAY-R-123](../rules/LAY-R-123.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**A field can be searchable but hidden from the grid — a distinct third visibility state, rendered in green as `(Searchable, Hidden in grid)`, present in both the Edit and List facets. · Observed · 008.**

|  |  |
|---|---|
| Stated as | A field can be searchable but hidden from the grid — a distinct third visibility state, rendered in green as `(Searchable, Hidden in grid)`, present in both the Edit and List facets. |
| Stated as | Observed |
| Stated as | 008 |

### C The Edit List — [LAY-R-124](../rules/LAY-R-124.md)

*Derived · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**A layout carries a separate mobile ordering (`MobileRowPosition`), i.e. responsive layout is configured, not derived.**

|  |  |
|---|---|
| Stated as | A layout carries a separate mobile ordering (`MobileRowPosition`), i.e. responsive layout is configured, not derived. |
| Stated as | Observed (column) |
| Stated as | `all-fields.csv` |

### C The Edit List — [LAY-R-125](../rules/LAY-R-125.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**Per-placement CSS is configurable independently for label and value (`LabelCSSStyle`, `ValueCSSStyle`). · Observed (columns) · `all-fields.csv`.**

|  |  |
|---|---|
| Stated as | Per-placement CSS is configurable independently for label and value (`LabelCSSStyle`, `ValueCSSStyle`). |
| Stated as | Observed (columns) |
| Stated as | `all-fields.csv` |

### D Conditional field — [LAY-R-130](../rules/LAY-R-130.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**A conditional rule set is posted as a single JSON document per target — hidden form field `json.conditionalFieldsConfig` on form `ConditionFilter` — not as normalised rows. · Observed · conditional-fields.md § Storage format.**

|  |  |
|---|---|
| Stated as | A conditional rule set is posted as a single JSON document per target — hidden form field `json.conditionalFieldsConfig` on form `ConditionFilter` — not as normalised rows. |
| Stated as | Observed |
| Stated as | conditional-fields.md § Storage format |

### D Conditional field — [LAY-R-131](../rules/LAY-R-131.md)

*Derived · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**Superseded. An earlier reading of this corpus put conditional rules in `PageLayoutFilter` with `IsListFilter = false`.**

|  |  |
|---|---|
| Stated as | Superseded. An earlier reading of this corpus put conditional rules in `PageLayoutFilter` with `IsListFilter = false`. The live capture shows JSON-blob storage instead, so `PageLayoutFilter` is re-read as the row-filter and pivot table for lists and reports. See LAY-R-140. |
| Stated as | Corrected |
| Stated as | this document |

### D Conditional field — [LAY-R-132](../rules/LAY-R-132.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**[BLOCKED] The destination column for that JSON is not observed. `PageLayoutField.DisplayOptionJSON` (optional per-placement textarea) is the strongest candidate: a `subPage_<id>` target is a `PageLayoutField` row whose `SubPageLayoutID` holds that id.**

|  |  |
|---|---|
| Stated as | [BLOCKED] The destination column for that JSON is not observed. `PageLayoutField.DisplayOptionJSON` (optional per-placement textarea) is the strongest candidate: a `subPage_<id>` target is a `PageLayoutField` row whose `SubPageLayoutID` holds that id. Alternatives: `PageLayoutField.JSONConfigText`, `PageLayout.JSONConfigText`. Check: read those three columns for a layout with rules. |
| Stated as | Inferred (moderate) |
| Stated as | `all-fields.csv` |

### D Conditional field — [LAY-R-133](../rules/LAY-R-133.md)

*Derived · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**Conditional rules are invisible to the data API. No type matching `condition`, `rule`, `criteria`, `visib`, `depend`, `trigger`, `expression` or `predicate` exists in the 490-type GraphQL schema, and `PageLayout*` tables are absent from the 223-object business model entirely.**

|  |  |
|---|---|
| Stated as | Conditional rules are invisible to the data API. No type matching `condition`, `rule`, `criteria`, `visib`, `depend`, `trigger`, `expression` or `predicate` exists in the 490-type GraphQL schema, and `PageLayout*` tables are absent from the 223-object business model entirely. Rules are platform configuration, not tenant data. |
| Stated as | Derived |
| Stated as | graphql-api.md; `_lucernex_objects_summary.txt` |

### D Conditional field — [LAY-R-134](../rules/LAY-R-134.md)

*Derived · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**Because storage is an opaque blob, Lx cannot answer "which layouts depend on this field or this dropdown value". Any Where-Used capability requires normalised predicate rows.**

|  |  |
|---|---|
| Stated as | Because storage is an opaque blob, Lx cannot answer "which layouts depend on this field or this dropdown value". Any Where-Used capability requires normalised predicate rows. |
| Stated as | Derived |
| Stated as | LAY-R-130 |

### D2 PageLayoutFilter — [LAY-R-140](../rules/LAY-R-140.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**`PageLayoutFilter` holds row filters, not field-visibility rules: `ReportGroupAvailableFieldID` (required) + `CriteriaType1`/`CriteriaValue1` + `CriteriaType2`/`CriteriaValue2`, discriminated by a required `IsListFilter` boolean. · Observed (columns) + Inferred (role) · `all-fields.csv`.**

|  |  |
|---|---|
| Stated as | `PageLayoutFilter` holds row filters, not field-visibility rules: `ReportGroupAvailableFieldID` (required) + `CriteriaType1`/`CriteriaValue1` + `CriteriaType2`/`CriteriaValue2`, discriminated by a required `IsListFilter` boolean. |
| Stated as | Observed (columns) + Inferred (role) |
| Stated as | `all-fields.csv` |

### D2 PageLayoutFilter — [LAY-R-141](../rules/LAY-R-141.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**The same row also carries grouping and totalling: `RowOrderBy`, `ColumnOrderBy`, `ShowLabel`, `ShowSubtotal`. Lx list/report output is pivot-shaped, not flat-list-shaped.**

|  |  |
|---|---|
| Stated as | The same row also carries grouping and totalling: `RowOrderBy`, `ColumnOrderBy`, `ShowLabel`, `ShowSubtotal`. Lx list/report output is pivot-shaped, not flat-list-shaped. |
| Stated as | Observed (columns) + Inferred (semantics) |
| Stated as | `all-fields.csv` |

### D2 PageLayoutFilter — [LAY-R-142](../rules/LAY-R-142.md)

*Inferred · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**Two `CriteriaType`/`CriteriaValue` pairs on one row express a two-clause predicate on one field — a `between`. Multiple rows chain through `ExtendedGroupFilterID` (self-FK);.**

|  |  |
|---|---|
| Stated as | Two `CriteriaType`/`CriteriaValue` pairs on one row express a two-clause predicate on one field — a `between`. Multiple rows chain through `ExtendedGroupFilterID` (self-FK); the combinator is undetermined. |
| Stated as | Inferred (moderate-high) |
| Stated as | `all-fields.csv` |

### D2 PageLayoutFilter — [LAY-R-143](../rules/LAY-R-143.md)

*Derived · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**[BLOCKED] `IsListFilter` and the layout builder's `showInList=1` parameter (passed when `layoutMode` is `list` or `budget`) describe the same edit-vs-list split from two directions. Whether they are the same mechanism is unconfirmed — if they are, list-layout conditions are normalised rows while….**

|  |  |
|---|---|
| Stated as | [BLOCKED] `IsListFilter` and the layout builder's `showInList=1` parameter (passed when `layoutMode` is `list` or `budget`) describe the same edit-vs-list split from two directions. Whether they are the same mechanism is unconfirmed — if they are, list-layout conditions are normalised rows while edit-layout conditions are a JSON blob. Check: open the `showInList=1` surface and inspect what it posts. |
| Stated as | Open |
| Stated as | conditional-fields.md § Scope of evaluation; `all-fields.csv` |

### D2 PageLayoutFilter — [LAY-R-144](../rules/LAY-R-144.md)

*Inferred · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**A filter may target a field reached through a relation, disambiguated by `FieldContext` — the same column `PageLayoutField` carries. · Inferred (moderate) · `all-fields.csv`;.**

|  |  |
|---|---|
| Stated as | A filter may target a field reached through a relation, disambiguated by `FieldContext` — the same column `PageLayoutField` carries. |
| Stated as | Inferred (moderate) |
| Stated as | `all-fields.csv`; 009 |

### E Fields required — [LAY-R-150](../rules/LAY-R-150.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**Placeable fields come from the shared field registry (`ReportGroupAvailableField`), scoped to the layout's Primary Table, presented as the Available Fields tree. · Observed · 008.**

|  |  |
|---|---|
| Stated as | Placeable fields come from the shared field registry (`ReportGroupAvailableField`), scoped to the layout's Primary Table, presented as the Available Fields tree. |
| Stated as | Observed |
| Stated as | 008 |

### E Fields required — [LAY-R-151](../rules/LAY-R-151.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**Related-table fields are placeable through Related Fields, which for a true many-to-one FK target exposes that table's complete native catalog, not a curated subset. · Observed · 009.**

|  |  |
|---|---|
| Stated as | Related-table fields are placeable through Related Fields, which for a true many-to-one FK target exposes that table's complete native catalog, not a curated subset. |
| Stated as | Observed |
| Stated as | 009 |

### E Fields required — [LAY-R-152](../rules/LAY-R-152.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**The relationship is asymmetric by cardinality: from the many side, the one side appears under Related Fields; from the one side, the many side appears as an embedded `(One to Many List)` List Layout, never under Related Fields.**

|  |  |
|---|---|
| Stated as | The relationship is asymmetric by cardinality: from the many side, the one side appears under Related Fields; from the one side, the many side appears as an embedded `(One to Many List)` List Layout, never under Related Fields. |
| Stated as | Observed |
| Stated as | 009 |

### E Fields required — [LAY-R-153](../rules/LAY-R-153.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**A layout's Available Fields tree exposes each table's Custom Lists as a nested branch, drilling into that list's own fields. A custom list appears only under the table it belongs to.**

|  |  |
|---|---|
| Stated as | A layout's Available Fields tree exposes each table's Custom Lists as a nested branch, drilling into that list's own fields. A custom list appears only under the table it belongs to. |
| Stated as | Observed |
| Stated as | 008 |

### E Fields required — [LAY-R-154](../rules/LAY-R-154.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**Required fields render in red with a trailing `*`. · Observed · 008.**

|  |  |
|---|---|
| Stated as | Required fields render in red with a trailing `*`. |
| Stated as | Observed |
| Stated as | 008 |

### E Fields required — [LAY-R-155](../rules/LAY-R-155.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**Required-ness is intended to be set from the layout editor (Manage Page Layouts) or from Manage Forms, not from the field catalog — where the flag "defaults to No and is read-only". · Observed (vendor text) · `_xlsx_feature_list.txt` line 938.**

|  |  |
|---|---|
| Stated as | Required-ness is intended to be set from the layout editor (Manage Page Layouts) or from Manage Forms, not from the field catalog — where the flag "defaults to No and is read-only". |
| Stated as | Observed (vendor text) |
| Stated as | `_xlsx_feature_list.txt` line 938 |

### E Fields required — [LAY-R-156](../rules/LAY-R-156.md)

*Derived · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**[BLOCKED] No `IsRequired`/`IsReadOnly` column exists on `PageLayoutField`, so LAY-R-155's storage is unknown — either packed into `DisplayOption1/2/JSON`, or written back to `RGAF.IsRequired`. Check: change a field's required flag from the layout editor and re-read the catalog row.**

|  |  |
|---|---|
| Stated as | [BLOCKED] No `IsRequired`/`IsReadOnly` column exists on `PageLayoutField`, so LAY-R-155's storage is unknown — either packed into `DisplayOption1/2/JSON`, or written back to `RGAF.IsRequired`. Check: change a field's required flag from the layout editor and re-read the catalog row. |
| Stated as | Open |
| Stated as | `all-fields.csv` |

### E Fields required — [LAY-R-157](../rules/LAY-R-157.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**Some fields render as system-computed read-only placeholders (`xxxxx` on `Check Amount`, `Check Date`, `Check Number`, `AP Export Base#`) — populated by downstream processes, not by the form. · Observed · 008.**

|  |  |
|---|---|
| Stated as | Some fields render as system-computed read-only placeholders (`xxxxx` on `Check Amount`, `Check Date`, `Check Number`, `AP Export Base#`) — populated by downstream processes, not by the form. |
| Stated as | Observed |
| Stated as | 008 |

### E Fields required — [LAY-R-158](../rules/LAY-R-158.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**Every registry field carries a Value Javascript hook, so a field can have scripted default/computed/visibility behaviour independent of the layout's declarative conditions. · Observed · 005.**

|  |  |
|---|---|
| Stated as | Every registry field carries a Value Javascript hook, so a field can have scripted default/computed/visibility behaviour independent of the layout's declarative conditions. |
| Stated as | Observed |
| Stated as | 005 |

### F Forms — [LAY-R-160](../rules/LAY-R-160.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**A Form Type is a `CodeIssueType` row. Lx's schema names the dropdown that selects one `Dropdown (Form Type)`.**

|  |  |
|---|---|
| Stated as | A Form Type is a `CodeIssueType` row. Lx's schema names the dropdown that selects one `Dropdown (Form Type)`. |
| Stated as | Observed |
| Stated as | `_lucernex_objects_summary.txt`, `Issue.CodeIssueTypeID` |

### F Forms — [LAY-R-161](../rules/LAY-R-161.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**Manage Forms administers a firm code table (`FirmCodeEdit.jsp?TableType=2035`), i.e. the catalog of Form Types — not a layout builder.**

|  |  |
|---|---|
| Stated as | Manage Forms administers a firm code table (`FirmCodeEdit.jsp?TableType=2035`), i.e. the catalog of Form Types — not a layout builder. `TableType=2035` is `Issue Type Code`, confirmed against the full 207-entry registry. A Form is an Issue Type; the record it produces is an `Issue`. |
| Stated as | Observed |
| Stated as | code-table-registry.md; 004 |

### F Forms — [LAY-R-162](../rules/LAY-R-162.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**A Form Type declares which entity types it may be raised against, via eleven `IsValidFor<Entity>` flags (Portfolio, CapProgram, CapProject, OpenProject, PotentialProject, Prototype, Parcel, Facility, Location, Contract, EquipContract). · Observed · `_lucernex_objects_summary.txt`, `CodeIssueType`.**

|  |  |
|---|---|
| Stated as | A Form Type declares which entity types it may be raised against, via eleven `IsValidFor<Entity>` flags (Portfolio, CapProgram, CapProject, OpenProject, PotentialProject, Prototype, Parcel, Facility, Location, Contract, EquipContract). |
| Stated as | Observed |
| Stated as | `_lucernex_objects_summary.txt`, `CodeIssueType` |

### F Forms — [LAY-R-163](../rules/LAY-R-163.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**A Form Type carries its own numbering (`SequencePrefix`, `IsSequencePerFirm`) and lifecycle behaviour (`AllowReply`, `AutoClose`, `IsWorkFlow`). · Observed · `_lucernex_objects_summary.txt`.**

|  |  |
|---|---|
| Stated as | A Form Type carries its own numbering (`SequencePrefix`, `IsSequencePerFirm`) and lifecycle behaviour (`AllowReply`, `AutoClose`, `IsWorkFlow`). |
| Stated as | Observed |
| Stated as | `_lucernex_objects_summary.txt` |

### F Forms — [LAY-R-164](../rules/LAY-R-164.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**A form instance is an `Issue` record. `Issue.LastPageLayoutID` records "the name of the last form layout used to update the issue" — singular, so it is depth-1 history, not a per-step audit trail.**

|  |  |
|---|---|
| Stated as | A form instance is an `Issue` record. `Issue.LastPageLayoutID` records "the name of the last form layout used to update the issue" — singular, so it is depth-1 history, not a per-step audit trail. It does not make a multi-step form reproducible as each participant saw it. |
| Stated as | Observed (vendor Definition text) |
| Stated as | `_xlsx_feature_list.txt`; `_lucernex_objects_summary.txt` |

### F Forms — [LAY-R-165](../rules/LAY-R-165.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**Forms are the workflow engine's rendering surface, bound at two levels: `WorkFlowTemplate.PageLayoutID` is the single kick-off/Submit form for the whole workflow, while `WorkFlowTemplateStep.PageLayoutApproversID` and `.PageLayoutAssigneesID` bind an approver-facing and an assignee-facing layout….**

|  |  |
|---|---|
| Stated as | Forms are the workflow engine's rendering surface, bound at two levels: `WorkFlowTemplate.PageLayoutID` is the single kick-off/Submit form for the whole workflow, while `WorkFlowTemplateStep.PageLayoutApproversID` and `.PageLayoutAssigneesID` bind an approver-facing and an assignee-facing layout per step. A workflow with N steps therefore carries N+1 layouts. Different participants see a different form for the same record at the same step. |
| Stated as | Observed (columns + vendor Definition text) |
| Stated as | `all-fields.csv`; `_xlsx_feature_list.txt` |

### F Forms — [LAY-R-166](../rules/LAY-R-166.md)

*Derived · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**The field registry's top-level group `Specialized Forms` is the only group applicable to Issue and not to Portfolio or Entity; its member entities are the Issue-derived transactional forms (Bid Package, Bidder Issue, Service Request, Work Order, Purchase Order, Change Order, Invoice Issue, Invoice….**

|  |  |
|---|---|
| Stated as | The field registry's top-level group `Specialized Forms` is the only group applicable to Issue and not to Portfolio or Entity; its member entities are the Issue-derived transactional forms (Bid Package, Bidder Issue, Service Request, Work Order, Purchase Order, Change Order, Invoice Issue, Invoice Item, Bid Package Template). |
| Stated as | Observed (applicability) + Derived (membership) |
| Stated as | 005; `docs/data-fields/INDEX.md` |

### G Custom Lists — [LAY-R-170](../rules/LAY-R-170.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**A Custom List is a tenant-authored mini record type: its own field schema plus its own layout. It is not a picklist.**

|  |  |
|---|---|
| Stated as | A Custom List is a tenant-authored mini record type: its own field schema plus its own layout. It is not a picklist. |
| Stated as | Observed |
| Stated as | 006 |

### G Custom Lists — [LAY-R-171](../rules/LAY-R-171.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**The list is a `ReportGroupData` node; its fields are `ReportGroupAvailableField` leaves;.**

|  |  |
|---|---|
| Stated as | The list is a `ReportGroupData` node; its fields are `ReportGroupAvailableField` leaves; its layout is a `PageLayout` whose `ClientListRGDID` points back at the node. The list itself is also an RGAF leaf of type `sTYPE_CLIENT_LISTS` on its owning entity. |
| Stated as | Observed (6/6 name match) |
| Stated as | `all-fields.csv`; 006 |

### G Custom Lists — [LAY-R-172](../rules/LAY-R-172.md)

*Derived · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**Each custom list gets its own field-name namespace derived from its initials (`CRL_*` for Client Request Log, `OpEx*` for Operating Expenses), plus shared system audit fields (`ModifiedByID`, `ModifiedDate`) with no prefix. · Observed · 006, 008.**

|  |  |
|---|---|
| Stated as | Each custom list gets its own field-name namespace derived from its initials (`CRL_*` for Client Request Log, `OpEx*` for Operating Expenses), plus shared system audit fields (`ModifiedByID`, `ModifiedDate`) with no prefix. |
| Stated as | Observed |
| Stated as | 006, 008 |

### G Custom Lists — [LAY-R-173](../rules/LAY-R-173.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**A custom-list field can be typed Drop Down >>, cascading into a Drop Down Type category and then a specific drop-down, binding it to Firm or Client Drop Downs. · Observed · 006, 007.**

|  |  |
|---|---|
| Stated as | A custom-list field can be typed Drop Down >>, cascading into a Drop Down Type category and then a specific drop-down, binding it to Firm or Client Drop Downs. |
| Stated as | Observed |
| Stated as | 006, 007 |

### G Custom Lists — [LAY-R-174](../rules/LAY-R-174.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**A custom list has a Type — `Standard` (2634) or `Part` (2635) — sharing machinery with the Parts and Inventory module. · Observed · 006.**

|  |  |
|---|---|
| Stated as | A custom list has a Type — `Standard` (2634) or `Part` (2635) — sharing machinery with the Parts and Inventory module. |
| Stated as | Observed |
| Stated as | 006 |

### G Custom Lists — [LAY-R-175](../rules/LAY-R-175.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**Custom Lists are Firm-scoped only; no Global/platform custom list concept was observed.**

|  |  |
|---|---|
| Stated as | Custom Lists are Firm-scoped only; no Global/platform custom list concept was observed. |
| Stated as | Observed (absence) |
| Stated as | 006 |

### H Role binding and — [LAY-R-180](../rules/LAY-R-180.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**A layout becomes an entity's creation wizard by assignment on Setup Pages, one slot per entity type. · Observed · 008.**

|  |  |
|---|---|
| Stated as | A layout becomes an entity's creation wizard by assignment on Setup Pages, one slot per entity type. |
| Stated as | Observed |
| Stated as | 008 |

### H Role binding and — [LAY-R-181](../rules/LAY-R-181.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**Setup-page assignment exists at two levels: `Firm` (11 slots, tenant default) and `Program` (18 slots — 11 setup pages + 7 map popups, per Portfolio/Capital Program). Only the Firm level was observed in the UI.**

|  |  |
|---|---|
| Stated as | Setup-page assignment exists at two levels: `Firm` (11 slots, tenant default) and `Program` (18 slots — 11 setup pages + 7 map popups, per Portfolio/Capital Program). Only the Firm level was observed in the UI. |
| Stated as | Observed (columns) + Inferred (override semantics) |
| Stated as | `all-fields.csv` |

### H Role binding and — [LAY-R-182](../rules/LAY-R-182.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**A setup-page selector lists any layout whose Primary Table matches the target — Summary Pages, Sub-pages and Wizards alike — not only Wizard-type records. · Observed (`ASG Client Request Log` offered as a Portfolio Layout) · 008.**

|  |  |
|---|---|
| Stated as | A setup-page selector lists any layout whose Primary Table matches the target — Summary Pages, Sub-pages and Wizards alike — not only Wizard-type records. |
| Stated as | Observed (`ASG Client Request Log` offered as a Portfolio Layout) |
| Stated as | 008 |

### H Role binding and — [LAY-R-183](../rules/LAY-R-183.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**Map Popup Layouts are a third, minimal rendering context, distinct from Summary Page and Wizard. The seven `*MapSetupLayoutID` columns sit on `Program`, not `Firm`, implying portfolio scope.**

|  |  |
|---|---|
| Stated as | Map Popup Layouts are a third, minimal rendering context, distinct from Summary Page and Wizard. The seven `*MapSetupLayoutID` columns sit on `Program`, not `Firm`, implying portfolio scope. |
| Stated as | Observed (UI + columns) + Inferred (scope) |
| Stated as | 008; `all-fields.csv` |

### H Role binding and — [LAY-R-184](../rules/LAY-R-184.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**A layout is placed in the navigation menu via a Parent Tab tree selection, materialised as `HierarchyName` (e.g. `Contract : Details : Summary`).**

|  |  |
|---|---|
| Stated as | A layout is placed in the navigation menu via a Parent Tab tree selection, materialised as `HierarchyName` (e.g. `Contract : Details : Summary`). Sub-pages have no such placement. |
| Stated as | Observed |
| Stated as | 008 |

### H Role binding and — [LAY-R-185](../rules/LAY-R-185.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**A new layout may be seeded from an existing one via "Initialize layout from existing layout", available only on create, not on edit. Whether it is a full clone or a partial template is unknown.**

|  |  |
|---|---|
| Stated as | A new layout may be seeded from an existing one via "Initialize layout from existing layout", available only on create, not on edit. Whether it is a full clone or a partial template is unknown. |
| Stated as | Observed (control) + Open (behaviour) |
| Stated as | 008 |

### I Security — [LAY-R-190](../rules/LAY-R-190.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**Access is granted per user class against a layout, a field, a field group, or a dashboard component — all from one `UserClassSecurity` table with a `CodeSecurityPrivilegeID` and a `SecurityLevelByteValue`. (A fifth subject in the out-of-scope budget domain also exists.) · Observed · `all-fields.csv`.**

|  |  |
|---|---|
| Stated as | Access is granted per user class against a layout, a field, a field group, or a dashboard component — all from one `UserClassSecurity` table with a `CodeSecurityPrivilegeID` and a `SecurityLevelByteValue`. (A fifth subject in the out-of-scope budget domain also exists.) |
| Stated as | Observed |
| Stated as | `all-fields.csv` |

### I Security — [LAY-R-191](../rules/LAY-R-191.md)

*Inferred · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**Granting on a `ReportGroupDataID` (group or subgroup) means field permissions inherit down the registry tree, not per-field only. · Inferred (high) · `all-fields.csv`.**

|  |  |
|---|---|
| Stated as | Granting on a `ReportGroupDataID` (group or subgroup) means field permissions inherit down the registry tree, not per-field only. |
| Stated as | Inferred (high) |
| Stated as | `all-fields.csv` |

### I Security — [LAY-R-192](../rules/LAY-R-192.md)

*Derived · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**Field visibility is therefore decided by three independent systems: security, layout placement, and conditional rules. A stated precedence is required;.**

|  |  |
|---|---|
| Stated as | Field visibility is therefore decided by three independent systems: security, layout placement, and conditional rules. A stated precedence is required; none is documented by Lx. Recommended for ASG Edge+: security → placement → condition. |
| Stated as | Derived + Inferred |
| Stated as | this document |

### J Change tracking — [LAY-R-200](../rules/LAY-R-200.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**Layout changes are audited — the admin dashboard exposes a Layout Changes tool (`ShowLayoutChanges.jsp`). Its contents were never opened;.**

|  |  |
|---|---|
| Stated as | Layout changes are audited — the admin dashboard exposes a Layout Changes tool (`ShowLayoutChanges.jsp`). Its contents were never opened; ASG's own review note records "Need further explanation as to what this is." |
| Stated as | Observed (link + note) |
| Stated as | 004, `_xlsx_feature_list.txt` line 44 |

### J Change tracking — [LAY-R-201](../rules/LAY-R-201.md)

*Derived · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**Field-level value changes are audited in `AuditColumn`, filed under the registry's group and subgroup — so an audit entry inherits the Data Fields taxonomy. · Derived (11-for-11 column match) · 007;.**

|  |  |
|---|---|
| Stated as | Field-level value changes are audited in `AuditColumn`, filed under the registry's group and subgroup — so an audit entry inherits the Data Fields taxonomy. |
| Stated as | Derived (11-for-11 column match) |
| Stated as | 007; `all-fields.csv` |

### J Change tracking — [LAY-R-202](../rules/LAY-R-202.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**Layout records carry `VersionAdded`/`VersionModified` at the field level (`RGAF`) but not at the layout level — layout versioning, if any, is not visible in the schema. · Observed (absence) · `all-fields.csv`.**

|  |  |
|---|---|
| Stated as | Layout records carry `VersionAdded`/`VersionModified` at the field level (`RGAF`) but not at the layout level — layout versioning, if any, is not visible in the schema. |
| Stated as | Observed (absence) |
| Stated as | `all-fields.csv` |
