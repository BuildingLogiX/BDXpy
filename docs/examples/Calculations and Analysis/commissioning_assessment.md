# Commissioning Assessment Report

A worked example of a 7-day commissioning-style assessment produced from BDX trend data using BDXpy. The report rolls up AHU performance, hydronic pump health, VAV behavior, and electric-meter context for a single building into a navigable HTML deliverable — the same format we hand operators, engineers, and owners after a building review.

<div style="text-align: center; margin: 20px 0;">
    <a href="../commissioning_report_2026.html" target="_blank" rel="noopener">
        <button style="padding: 10px 20px; font-size: 14px; cursor: pointer;">Open Full Report in New Tab</button>
    </a>
</div>

## What's inside

- **Equipment inventory** — AHUs, VAVs, exhaust fans, pumps, heat exchangers, electric meters
- **AHU performance snapshot** — 7-day rollup of SAT vs. setpoint, cool/heat/preheat output, OA damper position, ERW behavior, airflow, duct static, and alarms across all four AHUs
- **Operational findings, ranked by impact** — each finding shows the temporal pattern, setpoint deviation, cross-variable root cause, peer comparison, and a direct TrendView deep link for further investigation
- **Energy snapshot** — supply-fan, return-fan, and total-fan-power meter context for the assessment window
- **Recommended next steps** — prioritized work-order list tied to the findings, plus what is working correctly
- **Methodology** — discovery, data window, property names, fan-on masking, simultaneous heat+cool definition, and the TrendView URL construction pattern

## Inline preview

The report is a single-file HTML with embedded chart images, so the full-report button above is usually the better way to read it. A lightweight preview is embedded below for convenience.

<iframe src="../commissioning_report_2026.html" width="100%" height="800" style="border: 1px solid #ddd;" loading="lazy"></iframe>

## How it was built

- **Data source:** BDX trend data (AHU, VAV, pump, exhaust-fan, heat-exchanger, and electric-meter properties) pulled via BDXpy at hourly aggregation over a rolling 7-day window.
- **Discovery:** cached site inventory CSV filtered to the target building, then per-template-type device lists driven into per-device fetches.
- **Pipeline:** pandas for shaping and per-AHU/VAV rollups, matplotlib for the embedded chart images, a Jinja-style HTML template for the report wrapper.
- **Analytical guardrails:** fan-on masking (every AHU metric except status booleans is masked by `supplyFanStatus > 0`); simultaneous heat+cool flagged when both `coolOutput > 5%` AND (`heatOutput > 5%` OR `preheatOutput > 5%`); reset-strategy validation by comparing peer AHUs.
- **Output:** one self-contained `.html` deliverable plus companion CSVs and Parquet caches for downstream work.

!!! note "Scrubbed demonstration data"
    Site identifiers, building names, and internal device IDs have been removed. The structure, chart types, finding categories, and analytical approach mirror the production deliverable.
