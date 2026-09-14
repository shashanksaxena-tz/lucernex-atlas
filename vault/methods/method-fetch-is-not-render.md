---
title: "Method: a 200 proves the server answered, not what renders"
tags: [method, meta, trap]
evidence: Observed
---

This application injects content client-side and redirects client-side. **A raw `fetch` sees neither.**

Two published results were wrong for exactly this reason:

**1. The conditional-fields false negative.** Fetching `LayoutEditorAJAX.jsp` over HTTP and regexing
the response returns **zero** conditional targets even for a layout directly observed to have 22 — the
`conditionOptions(...)` calls are **injected after load**. A second version of the same mistake read
the `value` attribute of the hidden `json.conditionalFieldsConfig` input in the *served* HTML, which is
**always empty** because the builder populates it from the field's record. **The probe was structurally
incapable of ever observing a rule, and "empty" was guaranteed regardless of the data.**

**2. The route audit.** 22 of 46 [[Contract]] routes return a full 37–40 KB HTML document — a clean
200 — and then **bounce client-side** to `EntityInfo.jsp`. `fetch` reported 36 addressable; a real
browser produced **14**. See [[finding-routes-are-not-addressable]].

### The validated methods, for reuse

- **Render, then read the live DOM.** An iframe works, same-origin. Poll until the injected calls
  appear.
- **Guard captures with a final-URL check.** This is what prevented ~20 correctly-named files all
  containing the same default page.
- **Better still, skip the DOM.** The definitive read of a conditional rule is one call:
  `GET /rest/businessObject/PageLayout/lxid/{id}?deep=true`.
- **Only one `LayoutEditorAJAX` builder can be open per session** — concurrent iframes collide. Any
  layout sweep must be serial.

See [[method-cheap-signals]] · [[conditional-field]]
