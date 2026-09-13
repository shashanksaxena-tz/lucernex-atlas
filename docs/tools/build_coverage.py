#!/usr/bin/env python3
"""Regenerate docs/COVERAGE.md from the raw tenant captures.

Run from the repository root:  python3 docs/tools/build_coverage.py

Nothing here is hand-written: every row comes from a file under docs/tenants/ or
docs/mindmap/.  Two judgement columns are looked up rather than computed:

  Owner doc   - docs/tools/coverage-owners.json, curated by hand.
  Named in    - computed by scanning every .md under docs/ for the surface name.

"Named in" is deliberately weaker than "documented": it only proves a string
appears somewhere.  Add a surface to coverage-owners.json when a document
actually explains it.
"""
import json, os, re, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # docs/
REPO = os.path.dirname(ROOT)

def J(rel):
    with open(os.path.join(ROOT, rel)) as fh:
        return json.load(fh)

OWNERS = J('tools/coverage-owners.json')

# ---------------------------------------------------------------- corpus scan
CORPUS = {}
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if not d.startswith('.') and d not in ('assets', 'tools')]
    for fn in filenames:
        if fn.endswith('.md'):
            p = os.path.join(dirpath, fn)
            rel = os.path.relpath(p, ROOT)
            if rel in ('COVERAGE.md',):
                continue
            with open(p, errors='replace') as fh:
                CORPUS[rel] = fh.read()

# Single words too common to be evidence of anything.  "Summary" appears in 80
# documents and proves nothing about whether the Summary screen is documented.
GENERIC = {
    'summary', 'details', 'detail', 'equipment', 'documents', 'schedule', 'budget',
    'reports', 'forms', 'terms', 'sales', 'notes', 'contacts', 'general', 'options',
    'tasks', 'issues', 'binders', 'location', 'facility', 'contract', 'portfolio',
    'members', 'history', 'setup', 'status', 'type', 'code', 'table', 'list',
    'payments', 'invoices', 'receipts', 'expenses', 'allowances', 'parking', 'spaces',
    'work flow', 'work orders', 'key dates', 'amendments', 'covenants', 'insurance',
}

def measurable(name):
    """False when the name is too generic for a substring hit to mean anything."""
    n = (name or '').strip().lower()
    return bool(n) and len(n) >= 8 and n not in GENERIC and not (
        ' ' not in n and n in GENERIC)

def named_in(name, minlen=4):
    """Documents whose text contains this surface name verbatim."""
    if not name or len(name) < minlen:
        return []
    return sorted(rel for rel, txt in CORPUS.items() if name in txt)

def named_in_strict(name):
    """named_in, but refuses to answer for names too generic to be evidence."""
    return named_in(name) if measurable(name) else None

def cite(hits, limit=2):
    if hits is None:
        return '*name too generic to measure*'
    if not hits:
        return '—'
    shown = ', '.join(f'[{os.path.basename(h)}]({h})' for h in hits[:limit])
    if len(hits) > limit:
        shown += f' +{len(hits)-limit}'
    return shown

# ------------------------------------------------------------- screenshots
SHOTDIR = os.path.join(ROOT, 'assets', 'screenshots')
SHOTS = []
for dirpath, dirnames, filenames in os.walk(SHOTDIR):
    dirnames[:] = [d for d in dirnames if not d.startswith('.')]
    for fn in filenames:
        if fn.lower().endswith(('.png', '.jpg', '.jpeg')):
            SHOTS.append(os.path.relpath(os.path.join(dirpath, fn), ROOT))

def slug(s):
    return re.sub(r'[^a-z0-9]+', '-', (s or '').lower()).strip('-')

SHOT_BY_SLUG = {}
for s in SHOTS:
    base = os.path.splitext(os.path.basename(s))[0]
    base = re.sub(r'^\d+-', '', base)          # bbw-admin/01-manage-company.jpg
    SHOT_BY_SLUG.setdefault(slug(base), []).append(s)

def shot_for(name):
    hits = SHOT_BY_SLUG.get(slug(name), [])
    if not hits:
        return '—'
    # Cite by path, not as a link: the screenshot sets are periodically re-captured
    # and hard links break. COVERAGE regenerates, but prose citing it should not rot.
    return ', '.join(f'`{h.split("screenshots/")[-1]}`' for h in hits[:2])

def owner(kind, name):
    o = OWNERS.get(kind, {}).get(name)
    return f'[{os.path.basename(o)}]({o})' if o else '—'

# ----------------------------------------------------------------- captures
inv      = J('tenants/bbw-platform-inventory.json')
layouts  = J('tenants/bbw-page-layouts.json')
drops    = J('tenants/bbw-drop-downs.json')
wf       = J('tenants/bbw-workflow-steps.json')
tables   = J('tenants/bbw-platform-tables.json')
navbbw   = J('mindmap/navtree-bbw.json')
navaf    = J('mindmap/navtree.json')
afcounts = J('tenants/af-counts.json')
cmp_     = J('tenants/layout-set-comparison.json')

# AF nav carries routes; BBW nav does not.  109/109 PageLayoutIDs are identical
# across tenants, so the route joins on pageLayoutId.
AF_ROUTE = {s['pageLayoutId']: s.get('jsp', '') for s in navaf['screens']}
AF_ENTITY = {s['pageLayoutId']: s.get('entityType', '') for s in navaf['screens']}
AF_IDS = set(AF_ROUTE)

rows = []
out = []
W = out.append

# ------------------------------------------------------------------ counters
stat = collections.OrderedDict()

def pct(n, d):
    return f'{100*n//d}%' if d else '—'

# ================================================================== §1 nav
nav_rows = []
path = {}
for s in navbbw['screens']:
    d = s['depth']
    path[d] = s['name']
    trail = ' : '.join(path[i] for i in range(d + 1) if i in path)
    plid = s['pageLayoutId']
    route = AF_ROUTE.get(plid, '')
    nav_rows.append(dict(
        trail=trail, depth=d, name=s['name'], plid=plid,
        leaf=s.get('leaf', False),
        route=route or ('—' if plid in AF_IDS else '(BBW-only, not captured)'),
        entity=s.get('entityType') or AF_ENTITY.get(plid, ''),
        af=plid in AF_IDS,
        named=(named_in(trail) or named_in_strict(s['name'])) if s.get('leaf') else [],
        owner=owner('navScreens', trail),
    ))
nav_leaves = [r for r in nav_rows if r['leaf']]
nav_routed = [r for r in nav_leaves if r['route'].startswith('/')]
nav_bbwonly = [r for r in nav_rows if not r['af']]

# ============================================================== §2 admin
admin_rows = []
af_admin = {t['text'] for t in afcounts['adminToolList']}
for t in inv['adminTools']['tools']:
    name = t['text']
    admin_rows.append(dict(
        name=name, href=t['href'],
        shot=shot_for(name), owner=owner('adminTools', name),
        named=named_in(name), af=name in af_admin))
admin_shot = sum(1 for r in admin_rows if r['shot'] != '—')
admin_owned = sum(1 for r in admin_rows if r['owner'] != '—')

# ============================================================= §3 layouts
shared_names = {(s['mode'], s['name']) for s in cmp_['shared']}
lay_rows = []
for l in layouts['layouts']:
    key = (l['mode'], l['name'])
    lay_rows.append(dict(
        mode=l['mode'], name=l['name'], plid=l['pageLayoutId'],
        table=l.get('primaryTable') or '—',
        navto=(l.get('navigation') or '—').replace('&nbsp;', '').strip() or '—',
        shared=key in shared_names,
        owner=owner('layouts', l['name']),
        named=named_in_strict(l['name'])))
lay_named = sum(1 for r in lay_rows if r["named"])

# =========================================================== §4 workflows
wf_rows = [dict(name=t['template'], id=t['workFlowTemplateID'], steps=t['stepCount'],
                owner=owner('workflows', t['template']),
                named=named_in_strict(t['template'])) for t in wf['templates']]
form_rows = [dict(name=f['name'], owner=owner('forms', f['name']),
                  named=named_in_strict(f['name'])) for f in inv['forms']['items']]

# ========================================================== §5 drop-downs
dd_rows = [dict(name=d['name'], tt=d['tableType'], named=named_in_strict(d['name']))
           for d in drops['dropDowns']]
dd_named = sum(1 for r in dd_rows if r['named'])

# ============================================================ §6 sql tables
refused = {r['uiName']: r for r in tables['refusedTables']}
by_name = {t['uiName']: t for t in tables['tables']}
tbl_rows = []
for opt in inv['sqlTables']['options']:
    n = opt['name']
    t = by_name.get(n)
    tbl_rows.append(dict(
        id=opt['id'], name=n,
        physical=(t or refused.get(n, {})).get('physical', '—'),
        fields=(t['fieldCount'] if t else None),
        req=(sum(1 for f in t['fields'] if f.get('required')) if t else None),
        census=(t.get('inObjectCatalog') if t else False),
        refused=n in refused,
        named=named_in_strict(n)))
tbl_detail = sum(1 for r in tbl_rows if r['fields'] is not None)
tbl_census = sum(1 for r in tbl_rows if r['census'])
tbl_named = sum(1 for r in tbl_rows if r['named'])

# ================================================================== render
W('# Coverage — every known surface of Lucernex, and whether it is documented')
W('')
W('**Stated up front.** Lucernex exposes **{:,} distinct surfaces** that this corpus has to account '
  'for: {} end-user navigation nodes ({} of them leaf screens), {} administration tools, {} page '
  'layouts, {} sql tables, {} firm drop-downs, {} workflow templates and {} form types. This file '
  'is the scoreboard. It is **generated** — do not hand-edit it; edit '
  '[`tools/coverage-owners.json`](tools/coverage-owners.json) and re-run '
  '`python3 docs/tools/build_coverage.py`.'
  .format(len(nav_rows) + len(admin_rows) + len(lay_rows) + len(tbl_rows) + len(dd_rows) + len(wf_rows) + len(form_rows),
          len(nav_rows), len(nav_leaves), len(admin_rows), len(lay_rows),
          len(tbl_rows), len(dd_rows), len(wf_rows), len(form_rows)))
W('')
W('Two columns carry different weight, and the difference matters:')
W('')
W('| Column | Means |')
W('|---|---|')
W('| **Owner doc** | A document that *explains* this surface. Curated by hand in `tools/coverage-owners.json`. This is the real coverage number. |')
W('| **Named in** | A document whose text contains the surface name verbatim. Computed. Proves only that the name has been written down somewhere — **not** that it is understood. |')
W('| **Shot** | A screenshot whose filename slug matches the surface name. |')
W('')
W('**Granularity, stated honestly.** Page layouts, workflow templates, form types and the Equipment '
  'Contract screens are owned at **registry level**: the owning document enumerates every one of them '
  'with its mode, primary table and attachment, but does not walk each one field by field. Sql tables '
  'and drop-downs are deliberately left **unowned** — they have registry coverage in '
  '[`data-model/`](data-model/) and no document explains any of them individually.')
W('')
W(f'Captured from `(ASG)BBW` (firmID 3159) and `(ASG)American Freight` (firmID 3158), both on '
  f'build `{inv["build"]}`, {inv["captured"]}. Confidence: **Derived** throughout — every row is a '
  'mechanical join over Observed captures.')
W('')
W('## Scoreboard')
W('')
W('| Surface class | Count | Owner doc | Named in some doc | Screenshot | Section |')
W('|---|---:|---:|---:|---:|---|')
nav_owned = sum(1 for r in nav_rows if r['owner'] != '—')
W(f'| End-user navigation nodes (BBW) | {len(nav_rows)} | {nav_owned} | — | — | [§1](#1-end-user-navigation-141-nodes) |')
W(f'| — of which leaf screens | {len(nav_leaves)} | {sum(1 for r in nav_leaves if r["owner"] != "—")} | — | — | [§1](#1-end-user-navigation-141-nodes) |')
W(f'| — of which have a captured route | {len(nav_routed)} | — | — | — | [§1](#1-end-user-navigation-141-nodes) |')
W(f'| Administration tools | {len(admin_rows)} | {admin_owned} | {sum(1 for r in admin_rows if r["named"])} | {admin_shot} | [§2](#2-administration-tools-57) |')
lay_owned = sum(1 for r in lay_rows if r['owner'] != '—')
W(f'| Page layouts | {len(lay_rows)} | {lay_owned} | {lay_named} | — | [§3](#3-page-layouts-93) |')
W(f'| Workflow templates | {len(wf_rows)} | {sum(1 for r in wf_rows if r["owner"] != "—")} | {sum(1 for r in wf_rows if r["named"])} | — | [§4](#4-workflow-templates-13-and-form-types-6) |')
W(f'| Form types | {len(form_rows)} | {sum(1 for r in form_rows if r["owner"] != "—")} | {sum(1 for r in form_rows if r["named"])} | — | [§4](#4-workflow-templates-13-and-form-types-6) |')
W(f'| Firm drop-downs | {len(dd_rows)} | 0 | {dd_named} | — | [§5](#5-firm-drop-downs-207) |')
W(f'| Sql tables | {len(tbl_rows)} | 0 | {tbl_named} | — | [§6](#6-sql-tables-227) |')
W('')
W('> **Caveat on every field count below (severity HIGH, stated by the capture itself).** The sweep '
  'behind `bbw-platform-tables.json` passed `showGlobal=true`, which selects the schema viewer\'s '
  '**Global Fields** radio rather than *Global and Firm Fields*. Its 6,487 fields are the **global '
  'layer only** — firm (`Firm_`-prefixed) columns are absent by construction. `Contract` shows 307 '
  'fields there against **570** in the 223-object census. Treat every field and required count '
  'derived from it as a **lower bound**. Re-running with `showGlobal=false` would fix it.')
W('')
W(f'Field-level depth already held: **{tbl_detail} of {len(tbl_rows)}** sql tables have full field '
  f'detail ({tables["totals"]["fieldsHarvested"]:,} fields with name, type, required flag, UI label, '
  f'version added and max size); **{len(refused)}** are refused by the viewer. '
  f'**{tbl_census} of {len(tbl_rows)}** appear in the 223-object census — '
  f'**{len(tbl_rows)-tbl_census} do not**, and those are the real blind spot.')
W('')

# ---- §1
W(f'## 1. End-user navigation ({len(nav_rows)} nodes)')
W('')
W(f'`(ASG)BBW` carries **{len(nav_rows)}** navigation nodes under **{sum(1 for r in nav_rows if r["depth"]==0)}** roots; '
  f'`(ASG)American Freight` carries **{len(navaf["screens"])}** under 4. All {len(navaf["screens"])} AF '
  f'`PageLayoutID`s are present in BBW unchanged, so **routes below are joined from the AF capture by '
  f'`PageLayoutID`**; the **{len(nav_bbwonly)}** BBW-only nodes have no captured route yet.')
W('')
W('> **A route is not an addressable URL.** These are the JSP routes the menu declares. Driving all 46 '
  'Contract nodes in a real browser found only **14 render standalone**; **22 return a full HTML '
  'document and then redirect client-side** to the default Summary, 8 are AccessDenied and 2 bounce '
  'server-side. `Equipment Contract` is not deep-linkable at all. See '
  '[`data-model/screen-routing.md`](data-model/screen-routing.md).')
W('')
W('Source: [`mindmap/navtree-bbw.json`](mindmap/navtree-bbw.json), '
  '[`mindmap/navtree.json`](mindmap/navtree.json), '
  '[`data-model/screen-routing.md`](data-model/screen-routing.md).')
W('')
W('| Path | Kind | PageLayoutID | Route | Entity | In AF? | Owner doc | Named in |')
W('|---|---|---:|---|---|:--:|---|---|')
for r in nav_rows:
    kind = 'screen' if r['leaf'] else 'group'
    W(f'| {r["trail"]} | {kind} | `{r["plid"]}` | `{r["route"]}` | {r["entity"] or "—"} | '
      f'{"yes" if r["af"] else "**BBW only**"} | {r["owner"]} | {cite(r["named"])} |')
W('')

# ---- §2
W(f'## 2. Administration tools ({len(admin_rows)})')
W('')
af_only = sorted(af_admin - {r['name'] for r in admin_rows})
W(f'The BBW admin dashboard lists **{len(admin_rows)}** tools; AF lists **{len(afcounts["adminToolList"])}**. '
  f'**{len(af_only)}** appear on AF and not on BBW: ' +
  (', '.join(f'`{n}`' for n in af_only) if af_only else 'none') + '.')
W('')
W('Source: [`tenants/bbw-platform-inventory.json`](tenants/bbw-platform-inventory.json) '
  '(`DashboardDispatchOld.jsp?dashboardName=admin`).')
W('')
W('| Tool | Route | Owner doc | Shot | Named in |')
W('|---|---|---|---|---|')
for r in sorted(admin_rows, key=lambda x: x['name']):
    href = r['href'].split('?')[0]
    W(f'| {r["name"]} | `{href}` | {r["owner"]} | {r["shot"]} | {cite(r["named"])} |')
W('')

# ---- §3
W(f'## 3. Page layouts ({len(lay_rows)})')
W('')
W(f'**{layouts["totals"]["SEP"]} SEP** (summary/detail pages), **{layouts["totals"]["SUB"]} SUB** '
  f'(sub-pages), **{layouts["totals"]["LIST"]} LIST** (list layouts). '
  f'**{cmp_["sharedByName"]}** are shared with AF by `(mode, name)` and **{cmp_["sharedIds"]}** by id — '
  'one ASG template set, copied per tenant and re-keyed, then forked.')
W('')
W(f'> {layouts["note"]}')
W('')
W('> **Scope of this count.** These 93 are the **firm-authored** layouts — the rows Manage Page '
  'Layouts lists. They are not all the layouts in the tenant. A further **42 form layouts** are '
  'reachable only through Issue Types (135 in total), and beyond both lies the platform-seeded '
  'population that renders the administration screens themselves — the `Manage Discount Rates` grid '
  'is rendered by a layout in **neither** set. "All 93 layouts" always means all *firm* layouts. See '
  '[`features/page-layouts/`](features/page-layouts/).')
W('')
W('Source: [`tenants/bbw-page-layouts.json`](tenants/bbw-page-layouts.json), '
  '[`tenants/layout-set-comparison.json`](tenants/layout-set-comparison.json).')
W('')
W('| Mode | Layout | PageLayoutID | Primary table | Attached to | In AF? | Owner doc | Named in |')
W('|---|---|---:|---|---|:--:|---|---|')
for r in sorted(lay_rows, key=lambda x: (x['mode'], x['name'])):
    W(f'| {r["mode"]} | {r["name"]} | `{r["plid"]}` | `{r["table"]}` | {r["navto"]} | '
      f'{"yes" if r["shared"] else "**BBW only**"} | {r["owner"]} | {cite(r["named"])} |')
W('')

# ---- §4
W(f'## 4. Workflow templates ({len(wf_rows)}) and form types ({len(form_rows)})')
W('')
W(f'**{wf["templateCount"]} templates, {wf["totalSteps"]} steps.** Every configured step is '
  f'`type={", ".join(wf["observedTypeValues"])}`; approval levels observed are '
  f'{", ".join("`"+a+"`" for a in wf["observedApprovalLevels"])}. '
  '**Not one step is a `Task` step**, so half the step model is unobserved.')
W('')
W('Source: [`tenants/bbw-workflow-steps.json`](tenants/bbw-workflow-steps.json).')
W('')
W('| Workflow template | WorkFlowTemplateID | Steps | Owner doc | Named in |')
W('|---|---:|---:|---|---|')
for r in sorted(wf_rows, key=lambda x: x['name']):
    W(f'| {r["name"]} | `{r["id"]}` | {r["steps"]} | {r["owner"]} | {cite(r["named"])} |')
W('')
W(f'Form types — `TableType=2035` (`Issue Type Code`). A **Form is an Issue Type**; a Custom List is '
  'a Form without the workflow.')
W('')
W('| Form type | Owner doc | Named in |')
W('|---|---|---|')
for r in sorted(form_rows, key=lambda x: x['name']):
    W(f'| {r["name"]} | {r["owner"]} | {cite(r["named"])} |')
W('')

# ---- §5
W(f'## 5. Firm drop-downs ({len(dd_rows)})')
W('')
W(f'All **{drops["total"]}** code tables, `TableType` {drops["tableTypeRange"][0]}–{drops["tableTypeRange"][1]}. '
  f'Identical set in both tenants (207/207 matching `TableType`s). Values, row actions and the '
  '`isReadOnlyRecord` delete gate are in '
  '[`tenants/af-code-table-actions.json`](tenants/af-code-table-actions.json) and '
  '[`data-model/code-table-registry.md`](data-model/code-table-registry.md).')
W('')
W('| TableType | Drop-down | Named in |')
W('|---:|---|---|')
for r in sorted(dd_rows, key=lambda x: x['tt']):
    W(f'| `{r["tt"]}` | {r["name"]} | {cite(r["named"], 1)} |')
W('')

# ---- §6
W(f'## 6. Sql tables ({len(tbl_rows)})')
W('')
W(f'The `ShowObjectDetails.jsp` picker exposes **{len(tbl_rows)}** tables. '
  f'**{tbl_detail}** yielded field detail; **{len(refused)}** are refused '
  '("Data for that table not supported") — including the entire `Page Layout` trio, which is why the '
  'layout engine has to be read from its UI rather than its schema. '
  f'**Required?** counts below are the table\'s own NOT-NULL-equivalent flag, distinct from '
  'layout-level required.')
W('')
W('Source: [`tenants/bbw-platform-tables.json`](tenants/bbw-platform-tables.json), '
  '[`tenants/bbw-platform-inventory.json`](tenants/bbw-platform-inventory.json), '
  '[`data-model/object-catalog.md`](data-model/object-catalog.md).')
W('')
W('| sqlTableID | Table | Physical | Fields | Required | In 223-object census? | Named in |')
W('|---:|---|---|---:|---:|:--:|---|')
for r in sorted(tbl_rows, key=lambda x: x['name']):
    f = '**refused**' if r['refused'] else (str(r['fields']) if r['fields'] is not None else '—')
    q = '—' if r['req'] is None else str(r['req'])
    W(f'| `{r["id"]}` | {r["name"]} | `{r["physical"]}` | {f} | {q} | '
      f'{"yes" if r["census"] else "**no**"} | {cite(r["named"], 1)} |')
W('')

# ---- gaps
missing_census = [r for r in tbl_rows if not r['census']]
W('## 7. The gaps this file makes visible')
W('')
W('| Gap | Size | Consequence |')
W('|---|---:|---|')
W(f'| Sql tables absent from the 223-object census | {len(missing_census)} | **Composition matters more than the '
  'count.** The catalogue derives from `ShowObjectDetails.jsp`, so every table that viewer refuses is absent '
  '**by construction**: **25** are the refused set (all recoverable over REST), **4** are the out-of-scope '
  '`Punch List` family, and only **2** are genuine in-scope omissions — `ChangeManage` and '
  '`VirtualTemplateMember`, one field each. The business-object census is essentially complete for in-scope '
  'work. Joined on **physical name**; a label join invents 12 phantom gaps. |')
W(f'| Tables refused by the schema viewer | {len(refused)} | **Recoverable after all** — all 25 appear in '
  '`GET /rest/firm/types` and deep-serialise via `/rest/businessObject/{type}/lxid/{id}?deep=true`. The '
  'layout trio was recovered this way. REST returns only *populated* columns, so it is a lower bound. |')
W(f'| Navigation nodes with no captured route | {len(nav_rows)-len([r for r in nav_rows if r["route"].startswith("/")])} | '
  'Groups mostly, plus every BBW-only Equipment Contract node. |')
W(f'| Admin tools with no screenshot | {len(admin_rows)-admin_shot} | Capture in progress. |')
W(f'| Admin tools with no owning document | {len(admin_rows)-admin_owned} | All 57 are classified with routes and '
  '55 are screenshotted in `features/administration/`. Of the unowned, **10 are deliberate** — 6 budget/bidding '
  '(out of scope by decision) and 4 vendor-only `/lxadmin/` — so the real debt is the remainder. The five '
  'financial reference-data tools (discount rates, CPI, exchange rates, fiscal and holiday calendars) are the '
  'highest value: they feed the accounting engine. |')
W(f'| Page layouts with no owning document | {len(lay_rows)-lay_owned} | Every layout is enumerated with its '
  'mode, primary table and attachment in `features/page-layouts/`; **none is documented field by field**. |')
W(f'| Sql tables with no owning document | {len(tbl_rows)} | Field detail exists for 202; no document explains '
  'an individual table. |')
W(f'| Firm drop-downs with no owning document | {len(dd_rows)} | Registry-level coverage only, in '
  '`data-model/code-table-registry.md`. |')
W('')
# The reverse gap: census objects the picker never lists.
CENSUS = set()
_census = os.path.join(REPO, '_lucernex_objects_summary.txt')
if os.path.exists(_census):
    with open(_census, errors='replace') as fh:
        for i, line in enumerate(fh):
            if i and line.strip():
                CENSUS.add(line.split('\t')[0].strip())
picker_phys = {r['physical'] for r in tbl_rows}
census_only = sorted(CENSUS - picker_phys)
if census_only:
    W(f'### Census objects the sql-table picker never lists ({len(census_only)})')
    W('')
    W('The gap runs both ways. These objects are in the 223-object census and absent from the 227-table '
      'picker, so neither inventory is complete — **the union is '
      f'{len(CENSUS | picker_phys)} distinct tables**. The `Code*` objects are expected (they are edited '
      'through `FirmCodeEdit.jsp`, not the sql viewer); the two `*FullImport` tables are not, and are a '
      'direct lead for import/export.')
    W('')
    W('| Object |')
    W('|---|')
    for n in census_only:
        W(f'| `{n}` |')
    W('')

W('### Sql tables absent from the 223-object census')
W('')
W('| sqlTableID | Table | Physical | Fields |')
W('|---:|---|---|---:|')
for r in sorted(missing_census, key=lambda x: x['name']):
    f = '**refused**' if r['refused'] else (str(r['fields']) if r['fields'] is not None else '—')
    W(f'| `{r["id"]}` | {r["name"]} | `{r["physical"]}` | {f} |')
W('')
W('---')
W('')
W('_Generated by [`tools/build_coverage.py`](tools/build_coverage.py). Re-run after any new capture '
  'lands in `docs/tenants/`._')

with open(os.path.join(ROOT, 'COVERAGE.md'), 'w') as fh:
    fh.write('\n'.join(out) + '\n')

print(f'COVERAGE.md written: {len(out)} lines')
print(f'  nav {len(nav_rows)} ({len(nav_leaves)} leaves, {len(nav_routed)} routed, {len(nav_bbwonly)} BBW-only)')
print(f'  admin {len(admin_rows)} (owner {admin_owned}, shot {admin_shot})')
print(f'  layouts {len(lay_rows)}  workflows {len(wf_rows)}  forms {len(form_rows)}')
print(f'  dropdowns {len(dd_rows)}  tables {len(tbl_rows)} (detail {tbl_detail}, census {tbl_census})')
