# Navigation & Screens

The front door. The navigation tree is platform-seeded and identical across tenants — 109 of 109 nodes at American Freight share their PageLayoutID with BBW's — and what a firm sees is decided by its data, not by its configuration.

## Who it is for

*Derived · fact · source: `docs/features/README.md`*

Every user. The navigation tree is the product's front door and it is platform-seeded, not tenant-authored.

## Where it is used

*Observed · fact · source: `docs/data-model/screen-routing.md`*

141 navigation nodes at BBW, 109 at American Freight, from one seeded tree.

## Data decides the roots

*Observed · capability · source: `docs/features/security-access/README.md`*

A navigation root renders if and only if the firm holds at least one record of that ProjectEntityTypeName. Four other candidate gates were tested and eliminated: user-class page security, the action-verb list, field-level security and the firm feature flags are all open at American Freight and the Equipment Contract root still does not render. This is the single most consequential navigation fact in the corpus, because it means an empty tenant looks like a differently-configured one.

## Layouts form a sequence

*Observed · capability · source: `docs/features/page-layouts/README.md`*

PreviousPageLayoutID is a sequence pointer, not a parent link. Layouts attached to one navigation node form an ordered chain, and the chains cross SEP and LIST modes. The parent link is a different column, ParentPageLayoutID.

## 135 layouts, not 93

*Observed · capability · source: `docs/features/page-layouts/README.md`*

Manage Page Layouts shows 93 rows. A further 42 form layouts are reachable only through Issue Types and never appear in that list. The real population is 135, and an inventory that stops at the admin screen is short by a third.

## Two tiers, one column

*Observed · fact · source: `docs/features/page-layouts/README.md`*

Navigation nodes and firm layouts share the PageLayoutID column and never collide: the navigation tier sits in a low, byte-identical band across tenants, the firm tier in a high tenant-specific block. A firm layout does not replace a navigation screen, it hangs off one — and several may hang off the same one.

## Evidence

*Observed · fact · source: `docs/assets/screenshots/`*

8 screen captures on disk, under docs/assets/screenshots/navigation, docs/assets/screenshots/dashboard, docs/assets/screenshots/end-user — the screens themselves, not a description of them. 7 of them are cited by name in the documentation, which is what ties a capture to the screen it shows.

![The main navigation, collapsed to its four roots](../../assets/screenshots/navigation/main-navigation-four-roots.jpg)
![System Administrator Dashboard](../../assets/screenshots/dashboard/admin-company-administration.png)
![Dashboard home with Help menu open](../../assets/screenshots/dashboard/dashboard-home-help-menu.png)
![The ASC 842 rent schedule screen](../../assets/screenshots/end-user/asc842-rent-schedule.jpg)
![A contract summary as an end user sees it](../../assets/screenshots/end-user/contract-summary-rendered.jpg)
![Expense Setup with its vendor allocations and an empty schedule](../../assets/screenshots/end-user/expense-setup-with-vendor-allocations.jpg)
![The Generate Payments dialog](../../assets/screenshots/end-user/generate-payments-dialog.jpg)
![payment-transactions-empty.jpg](../../assets/screenshots/end-user/payment-transactions-empty.jpg)

## Open questions (15)

*Inferred · group*

15 things nobody has confirmed for this feature. Each one is work somebody has to do before the feature can be rebuilt with confidence; they are carried here rather than resolved by guessing. Click one for the question and the document that raised it.

### Which dashboard layout

*Inferred · question · source: `docs/screens/001-dashboard-home.md`*

Which dashboard layout is intentionally assigned to Test2 User?. Nobody has confirmed this. Recorded in screens/001-dashboard-home.md, under the Screens & navigation area. Until it is settled, anything built on the assumption is a guess.

### Is the empty dashboard

*Inferred · question · source: `docs/screens/001-dashboard-home.md`*

Is the empty dashboard a permission outcome, an unconfigured personal tab, or a load issue?. Nobody has confirmed this. Recorded in screens/001-dashboard-home.md, under the Screens & navigation area. Until it is settled, anything built on the assumption is a guess.

### Which top right

*Inferred · question · source: `docs/screens/001-dashboard-home.md`*

Which top-right toolbar icons are enabled by role versus always visible?. Nobody has confirmed this. Recorded in screens/001-dashboard-home.md, under the Screens & navigation area. Until it is settled, anything built on the assumption is a guess.

### What does a Summary

*Inferred · question · source: `docs/screens/003-main-navigation.md`*

What does a Summary screen actually render? It is the first screen of every entity and has never been opened. It will be driven by one of the ASG * Summary page layouts documented in 008 — opening it would connect the layout builder to its output for the first time. Nobody has confirmed this. Recorded in screens/003-main-navigation.md, under the Screens & navigation area. Until it is settled, anything built on the assumption is a guess.

### What is a Binder It

*Inferred · question · source: `docs/screens/003-main-navigation.md`*

What is a Binder? It appears on all four roots and matches the Manage Binder Templates admin link, also unexplored. Nobody has confirmed this. Recorded in screens/003-main-navigation.md, under the Screens & navigation area. Until it is settled, anything built on the assumption is a guess.

### Is ASC 842 Test the

*Inferred · question · source: `docs/screens/003-main-navigation.md`*

Is ASC 842 Test the same record as Capital Lease Test with a different layout, or a genuinely separate record? The schema says ContractFinancialTest holds both — so probably one record, two layouts, but that is Inferred. Nobody has confirmed this. Recorded in screens/003-main-navigation.md, under the Screens & navigation area. Until it is settled, anything built on the assumption is a guess.

### What does Pro Forma

*Inferred · question · source: `docs/screens/003-main-navigation.md`*

What does Pro Forma Lease model, and does it share the Contract schema or have its own?. Nobody has confirmed this. Recorded in screens/003-main-navigation.md, under the Screens & navigation area. Until it is settled, anything built on the assumption is a guess.

### Scheduled Offsets and

*Inferred · question · source: `docs/screens/003-main-navigation.md`*

Scheduled Offsets and Recoveries appear as peers under Payment Info; the schema has ScheduledOffsets, ExpenseRecovery and ExpenseOffset — which screen maps to which table?. Nobody has confirmed this. Recorded in screens/003-main-navigation.md, under the Screens & navigation area. Until it is settled, anything built on the assumption is a guess.

### Does the menu vary by

*Inferred · question · source: `docs/screens/003-main-navigation.md`*

Does the menu vary by user class? This capture is one user (Test 2 User). A different security level may see more or fewer of the 81 screens, which would make the menu itself permission-driven data rather than fixed structure. Nobody has confirmed this. Recorded in screens/003-main-navigation.md, under the Screens & navigation area. Until it is settled, anything built on the assumption is a guess.

### What does Generate

*Inferred · question · source: `docs/screens/014-contract-record-end-user.md`*

What does Generate Rent actually produce, and against which tables? It cannot be pressed on a live tenant without creating data — this needs a disposable record or an explicit go-ahead. Nobody has confirmed this. Recorded in screens/014-contract-record-end-user.md, under the Screens & navigation area. Until it is settled, anything built on the assumption is a guess.

### What is ASG Lease Logs

*Inferred · question · source: `docs/screens/014-contract-record-end-user.md`*

What is ASG Lease Logs, the second layout in the picker?. Nobody has confirmed this. Recorded in screens/014-contract-record-end-user.md, under the Screens & navigation area. Until it is settled, anything built on the assumption is a guess.

### What are the Status

*Inferred · question · source: `docs/screens/014-contract-record-end-user.md`*

What are the Status values on a schedule period row? The column is marked required but this contract has no schedule rows. Nobody has confirmed this. Recorded in screens/014-contract-record-end-user.md, under the Screens & navigation area. Until it is settled, anything built on the assumption is a guess.

### Why does this contract

*Inferred · question · source: `docs/screens/014-contract-record-end-user.md`*

Why does this contract have no ASC 842 schedule despite being Active with dates? Either none was generated, or generation is gated on something not visible here. Nobody has confirmed this. Recorded in screens/014-contract-record-end-user.md, under the Screens & navigation area. Until it is settled, anything built on the assumption is a guess.

### Import Data on the

*Inferred · question · source: `docs/screens/014-contract-record-end-user.md`*

Import Data on the schedule screen — is a schedule importable from outside, bypassing the engine? That would be a significant finding for migration. Nobody has confirmed this. Recorded in screens/014-contract-record-end-user.md, under the Screens & navigation area. Until it is settled, anything built on the assumption is a guess.

### What does Add RE

*Inferred · question · source: `docs/screens/014-contract-record-end-user.md`*

What does Add RE Contract create, and how does it relate to MasterContractID?. Nobody has confirmed this. Recorded in screens/014-contract-record-end-user.md, under the Screens & navigation area. Until it is settled, anything built on the assumption is a guess.
