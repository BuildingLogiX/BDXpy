# Chiller Loading Analysis Report

A worked example of a full-year chiller-plant analysis produced from BDX trend data using BDXpy. The report combines operational metrics, staging behavior, load-duration curves, and outdoor-air-temperature relationships into a single navigable HTML deliverable — the same format we hand operators, engineers, and owners after a plant study.

<div style="text-align: center; margin: 20px 0;">
    <a href="../chiller_report_2025.html" target="_blank" rel="noopener">
        <button style="padding: 10px 20px; font-size: 14px; cursor: pointer;">Open Full Report in New Tab</button>
    </a>
</div>

## What's inside

- **Executive summary** — plant hours, total tonnage delivered, peak demand, and high-level findings
- **Runtime and cycles by machine** — uptime, short-cycle counts, and duty distribution per chiller
- **Startup loading and cycle analysis** — how each chiller ramps on, and whether it's cycling inefficiently
- **Chiller staging analysis** — when stages added or shed, and how often the plant ran in non-ideal configurations
- **Plant load duration curve** — hours-above-tonnage view, the single best chart for right-sizing decisions
- **Individual chiller loading** — per-unit tonnage distribution and part-load fingerprints
- **Plant tonnage timeline** — full-year hourly tonnage, annotated with operational events
- **Outdoor air temperature relationship** — tonnage vs. OAT scatter and binned regression
- **Chilled water temperatures** — supply/return behavior, delta-T analysis
- **Data accountability and strategic energy planning** — coverage, gaps, and recommended next steps
- **Methodology and data notes** — aggregation, filters, and assumptions

## Inline preview

The report is a 17 MB single-file HTML with embedded Plotly charts, so the full-report button above is usually the better way to read it. A lightweight preview is embedded below for convenience.

<iframe src="../chiller_report_2025.html" width="100%" height="800" style="border: 1px solid #ddd;" loading="lazy"></iframe>

## How it was built

- **Data source:** BDX trend data (chiller status, tonnage, CHW supply/return, OAT) pulled via BDXpy at hourly aggregation.
- **Pipeline:** pandas for shaping, Plotly for interactive charts, a Jinja-style HTML template for the report wrapper.
- **Output:** one self-contained `.html` deliverable plus companion CSVs and Parquet for downstream work.

!!! note "Scrubbed demonstration data"
    Site identifiers and proprietary specifics have been removed. The structure, chart types, and analytical approach mirror the production deliverable.
