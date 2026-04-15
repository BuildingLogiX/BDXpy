# Equipment Prediction Models

We train equipment-level ML models that flag performance degradation and emerging faults *before* they become operator-visible. Inputs are the same high-resolution trend data BDXpy already surfaces — valve positions, VFD commands, temperatures, flows, runtime, and staging — combined with engineered features that capture expected operating envelopes.

## Output

<iframe src="../equipment_prediction.html" width="800" height="450" style="border: none;"></iframe>

*Illustrative chart — synthetic data shown for demonstration.*

## What we use it for

- **Predictive fault risk** for chillers, AHUs, pumps, cooling towers, and VAVs — a rolling score per unit per day.
- **Efficiency drift detection** — e.g. chiller kW/ton trending above its expected curve for the current load and condenser conditions.
- **Runtime / wear forecasts** to inform preventive-maintenance scheduling.
- **Early warning for sensor and actuator failures** — stuck valves, drifting temperature sensors, miscalibrated airflow stations.

## Approach (high level)

- Expected-behavior models per equipment class (regression on load + boundary conditions) with residual-based anomaly scoring.
- Classification models trained on labeled fault history to assign fault-type probabilities.
- Fleet-level comparisons so a single unit's behavior is scored against its peers, not just against itself.
- Results are written back through BDXpy so they appear alongside live trend data in dashboards and reports.

!!! note "Proprietary implementation"
    Feature sets, labeling strategy, and model selection are specific to each equipment class and are not published. Contact BuildingLogiX to discuss a pilot on your systems.
