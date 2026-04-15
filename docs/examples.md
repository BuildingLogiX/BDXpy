# 📊 Example Highlights Gallery
Click in the left navigation for more details on specific examples

## Data Visualization

<div class="vertical-list" markdown>


-   :material-lightbulb-outline: **Airflow Sankey**


    <iframe src="Data Visualization/airflow_sankey.html" width="800" height="400"></iframe>

-   :material-chart-scatter-plot: **Building CFM Network**
   
    <iframe src="Data Visualization/VAV_network.html" width="800" height="400"></iframe>

-   :material-chart-scatter-plot: **Campus Energy Map**
   
    <iframe src="Data Visualization/mapenergychart.html" width="800" height="400"></iframe>

-   :material-chart-scatter-plot: **AHU Economizer Analysis**
   
    <img src="Data Visualization/bdxpy econo chart.png" alt="AHU Economizer Analysis" width="100%">


-   :material-chart-scatter-plot: **Operating Room KPIs**
   
    <iframe src="Data Visualization/operating_room_sankey_diagram.html" width="800" height="400"></iframe>

-   :material-chart-scatter-plot: **Static Pressure Distribution**
   
    <img src="Data Visualization/staticCurve.png" alt="Static Pressure Distribution" width="100%">


## Dashboards

- :material-air-filter: **AHU Cooling Performance App**

<div style="position: relative; text-align: center;">
    <button onclick="openInNewTab('https://ahu-cool-performance-buildinglogix.plotly.app/')" style="margin-top: 10px;">🔍 Open in New Tab</button>
    <iframe id="ahu-dashboard" src="https://ahu-cool-performance-buildinglogix.plotly.app/" width="800" height="400" style="border: none;"></iframe>
</div>

- :material-air-filter: **Campus Utilities App**

<div style="position: relative; text-align: center;">
    <button onclick="openInNewTab('https://energy-dashboard-xpwn.onrender.com/')" style="margin-top: 10px;">🔍 Open in New Tab</button>
    <iframe id="utl-dashboard" src="https://energy-dashboard-xpwn.onrender.com/" width="800" height="400" style="border: none;"></iframe>
</div>

- :material-air-filter: **RTU Dashboard**

<div style="position: relative; text-align: center;">
    <button onclick="openInNewTab('https://rtu-dash-bdxpy.onrender.com/')" style="margin-top: 10px;">🔍 Open in New Tab</button>
    <iframe id="rtu-dashboard" src="https://rtu-dash-bdxpy.onrender.com/" width="800" height="400" style="border: none;"></iframe>
</div>

<script>
function openInNewTab(url) {
    window.open(url, '_blank');
}
</script>


## Machine Learning

BuildingLogiX applies machine learning across the BDX dataset to forecast energy use, flag equipment issues before operators see them, mine years of historical trend data, and tune site-specific analytics rules. The previews below are **illustrative** — the underlying feature pipelines and models are part of our proprietary analytics stack.

- :material-chart-line: **Energy Prediction Models** — day-ahead and M&V baselines ([details](examples/Machine Learning/energy_prediction.md))

    <iframe src="Machine Learning/energy_prediction.html" width="800" height="400"></iframe>

- :material-cog-outline: **Equipment Prediction Models** — fault risk and efficiency drift ([details](examples/Machine Learning/equipment_prediction.md))

    <iframe src="Machine Learning/equipment_prediction.html" width="800" height="400"></iframe>

- :material-history: **Historical Analysis** — clustering, seasonality, and anomaly detection ([details](examples/Machine Learning/historical_analysis.md))

    <iframe src="Machine Learning/historical_analysis.html" width="800" height="400"></iframe>

- :material-shield-check-outline: **Custom Analytics Rules** — hybrid engineering + ML rule library ([details](examples/Machine Learning/custom_analytics_rules.md))

    <iframe src="Machine Learning/custom_analytics_rules.html" width="800" height="450"></iframe>



## Public Kiosk App
More examples coming soon!



</div>
