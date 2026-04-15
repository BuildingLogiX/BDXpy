# Energy Prediction Models

BuildingLogiX uses machine-learning models trained on historical building telemetry — weather, occupancy, schedules, metered loads, and equipment state — to forecast campus and building-level energy consumption. The models support short-horizon operational forecasts (hour / day ahead) as well as long-horizon budgeting and Measurement & Verification (M&V) baselines.

## Output

<iframe src="../energy_prediction.html" width="800" height="450" style="border: none;"></iframe>

*Illustrative chart — synthetic data shown for demonstration.*

## What we use it for

- **Day-ahead and week-ahead load forecasting** to support demand response, peak shaving, and thermal storage dispatch.
- **Weather-normalized baselines** for M&V on energy conservation measures (IPMVP Option C).
- **Budget and utility-bill forecasting** at the building and portfolio level.
- **Anomaly detection** — deviations from predicted load flag metering errors, off-schedule operation, or equipment drift.

## Approach (high level)

- Feature engineering from BDXpy time-series data: outdoor air temp, enthalpy, degree-day bins, time-of-week, occupancy proxies, rolling lags.
- Model families: gradient-boosted trees for robustness on mixed-feature sets, regularized regression for interpretable M&V baselines, and recurrent / temporal-fusion models where sub-hourly dynamics matter.
- Automated retraining and drift monitoring via BDXpy data services.

!!! note "Proprietary implementation"
    The specific feature pipelines, model architectures, and tuning procedures are part of BuildingLogiX's proprietary analytics stack. Reach out if you'd like to discuss applying these models to your portfolio.
