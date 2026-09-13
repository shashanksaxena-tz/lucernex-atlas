# Screen-capture exclusions — do not capture these routes

**Stated up front.** These routes render live credentials or other secrets. They must never be
screenshotted, and their HTML must never be stored. Any capture manifest built by enumerating the
admin tool list **will include them by default** — filter them explicitly when building the list,
not after.

| Route | Why |
|---|---|
| `/en/test/RESTful.jsp` | Renders a live **Basic Authentication token** and a live **JWT Bearer token** for the signed-in user |
| `/en/admin/graphql.jsp` | GraphQL Explorer — may carry an auth header in its console state |

## Incident, 2026-09-13

Both tenant sweeps built their manifest from the 57/63-entry admin tool enumeration, which contains
`RESTful.jsp`. Both attempted it.

- **American Freight** — attempted after the session had already expired, so the response was the
  login page. No token was exposed. Caught and reported by the capturing agent.
- **BBW** — attempted against a **live session**; `53-restful-webservice-docs.jpg` was written to
  disk. Deleted on discovery, removed from the git index, **never committed**, and never inspected.
  Verified absent from all git history.

**The lesson, and the rule:** filter forbidden routes when the manifest is *constructed*. Relying on
a tool enumeration to be safe is not a control — the enumeration is exactly where the unsafe route
comes from.

## Required guard for any capture sweep

`shot.mjs` prints the final URL on every line. A sweep must:

1. Drop excluded routes while building the manifest.
2. After each capture, check the final URL — if it is `login.jsp`, **discard the file and abort the
   sweep**. A session can expire mid-run, and the failure mode is a directory of login screens
   saved under meaningful names, which is worse than missing files.
