---
title: Administration
tags: [feature, administration]
evidence: Observed
---

**All 57 administration tools, classified with routes** — the complete inventory, which did not
previously exist. **55 of 57 have a screenshot**; the two without are `RESTful WebService Docs`
(renders live credentials) and `Delete Entities` (vendor-only, destructive).

| Group | Tools |
|---|---:|
| Configuration | **14** |
| Master data | 8 |
| People, organisations and access | 7 |
| Diagnostics, logs and developer tools | 7 |
| Import, export and jobs | 6 |
| Budget and bidding *(out of scope)* | 6 |
| Financial reference data | 5 |
| Vendor-only `/lxadmin/` | 4 |

**A quarter of the administration surface is the configuration engine** — and there is **no
tenant-facing tool for creating an entity type**.

Three route-level facts that settle long-standing confusions:

- `Import Data` and `Export Configuration` are one "Messenger" subsystem — `Messenger.jsp` and
  `MessengerExportData.jsp`.
- **Firm Drop Downs and Client Drop Downs are two registries, not two views** — `FirmCodeList.jsp`
  versus `CustomCodeTableEdit.jsp`.
- **`Job Log` and `Report Log` are the same screen** — both `JobLogEdit.jsp`.

The admin surface is a separate world from the [[navigation-tree]]: `Lx.ui.MenuTree` carries only the
end-user menu, which is why an `Administration` node kept appearing in layout metadata and never in
the 105-screen tree.

**AF exposes 6 more tools than BBW**, including `/lxadmin/` entries — so admin-tool visibility is
per-tenant or per-user-class, not fixed.

All of them: [[map-of-screens]] ·
[`features/administration/`](../../docs/features/administration/README.md)
