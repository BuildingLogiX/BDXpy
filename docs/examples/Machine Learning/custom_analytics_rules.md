# Custom Analytics Rules

Our analytics library combines **deterministic engineering rules** (encoding first-principles HVAC knowledge) with **ML-derived confidence scoring** that learns from each site's behavior. This hybrid approach gives operators explainable results while still adapting to the quirks of a specific building.

## Output

<iframe src="../custom_analytics_rules.html" width="800" height="550" style="border: none;"></iframe>

*Illustrative chart — synthetic data shown for demonstration.*

## What we use it for

- **Rule-based fault detection and diagnostics (FDD)** — simultaneous heat/cool, economizer not engaging, static-pressure reset idle, stuck dampers, night-setback failure, persistent zone offsets, and many more.
- **Per-site tuning** — ML models learn the thresholds, expected timing, and tolerances that make each rule meaningful at a given site instead of relying on generic defaults.
- **Confidence scoring** — every rule hit carries a confidence value so operators triage the highest-value issues first.
- **Feedback loop** — when engineers mark a hit as a false positive or a real finding, the confidence model updates.

## Approach (high level)

- A rule library expressed in BDXpy so rules can pull trend data, apply logic, and emit structured findings.
- Per-rule ML models that score confidence from historical context (time-of-day, outdoor conditions, recent equipment state, prior findings at the same point).
- Ranking and roll-up so a portfolio of thousands of point-level hits collapses to a short, prioritized work list.
- Findings are surfaced in the automated reports and dashboards shown elsewhere in this gallery.

!!! note "Proprietary implementation"
    The rule library, thresholds, and scoring models are BuildingLogiX IP. We license and deploy these as part of analytics engagements rather than publishing the source.
