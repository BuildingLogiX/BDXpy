# Historical Analysis

Years of BDX trend data is a dataset, not just a record. We apply ML techniques to long-horizon historical data to surface operational patterns, seasonality, and anomalies that point-in-time dashboards miss.

## Output

<iframe src="../historical_analysis.html" width="800" height="450" style="border: none;"></iframe>

*Illustrative chart — synthetic data shown for demonstration.*

## What we use it for

- **Load-profile clustering** — automatically grouping days into weekday / weekend / holiday / event-day / anomaly clusters without hand-labeling.
- **Seasonal decomposition** of utility and equipment performance to separate weather effects from operational change.
- **Anomaly detection** across multi-year windows — identifying days, weeks, or zones that deviate from learned norms.
- **Change-point detection** to pinpoint when a building's behavior shifted (commissioning, retrofit, schedule change, fault).
- **Portfolio benchmarking** — comparing similar buildings on normalized metrics to prioritize engineering attention.

## Approach (high level)

- Unsupervised clustering (k-means, DBSCAN, time-series-specific distance metrics) on daily load shapes and operating envelopes.
- Isolation forests and residual-based scoring for multivariate anomaly detection.
- Bayesian change-point detection on key KPIs.
- Results feed directly into the automated reporting and dashboard examples elsewhere in this gallery.

!!! note "Proprietary implementation"
    The full analytical pipeline — including the specific feature engineering and thresholds we use on client sites — is part of BuildingLogiX's internal tooling.
