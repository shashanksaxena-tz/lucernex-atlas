# FAC-R-020 — `DemographicStudyArea` and `SiteSurvey`'s fixed mile-bands are two independent, non-integrated mechanisms for the same concept

*Facilities, Locations & Sites · Derived*

**Input: `SiteSurvey` carries `Population1Mile/3Miles/5Miles` (and six more metrics repeated the same way) as fixed columns; `DemographicStudyArea` carries `AreaRadius`/`AreaDriveTimeInMinutes` as a reusable, parameterised definition.**

Input: `SiteSurvey` carries `Population1Mile/3Miles/5Miles` (and six more metrics repeated the same way) as fixed columns; `DemographicStudyArea` carries `AreaRadius`/`AreaDriveTimeInMinutes` as a reusable, parameterised definition. Neither references the other. Confidence: Derived, exhaustive column-name comparison — see `demographics.md` §3 for the full argument and the rebuild consequence.

## What it constrains

[SiteSurvey](../entities/SiteSurvey.md), [DemographicStudyArea](../entities/DemographicStudyArea.md)

## Confidence

Derived, exhaustive column-name comparison — see `demographics.md` §3 for the full argument and the rebuild consequence

---

Source: `docs/modules/facilities-locations/rules.md`
