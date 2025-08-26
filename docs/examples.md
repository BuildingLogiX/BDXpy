# 📊 Example Highlights Gallery
Click in the left navigation for more details on specific examples

## 🔥 Data Visualization

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
   
    <img src="Data Visualization/staticCurve.png" alt="AHU Economizer Analysis" width="100%">


## Dashboards

- :material-air-filter: **AHU Cooling Performance App**

<div style="position: relative; text-align: center;">
    <button onclick="toggleFullScreen('ahu-dashboard')" style="margin-top: 10px;">🔍 Click for Fullscreen</button>
    <iframe id="ahu-dashboard" src="https://ahu-cool-performance-buildinglogix.plotly.app/" width="800" height="400" style="border: none;"></iframe>
</div>

- :material-air-filter: **Campus Utilities App**

<div style="position: relative; text-align: center;">
    <button onclick="toggleFullScreen('utl-dashboard')" style="margin-top: 10px;">🔍 Click for Fullscreen</button>
    <iframe id="utl-dashboard" src="https://energy-dashboard-xpwn.onrender.com/" width="800" height="400" style="border: none;"></iframe>
</div>

- :material-air-filter: **RTU Dashboard**

<div style="position: relative; text-align: center;">
    <button onclick="toggleFullScreen('rtu-dashboard')" style="margin-top: 10px;">🔍 Click for Fullscreen</button>
    <iframe id="rtu-dashboard" src="https://rtu-dash-bdxpy.onrender.com/" width="800" height="400" style="border: none;"></iframe>
</div>

<script>
function toggleFullScreen(iframeId) {
    var iframe = document.getElementById(iframeId);
    if (iframe.requestFullscreen) {
        iframe.requestFullscreen();
    } else if (iframe.mozRequestFullScreen) { // Firefox
        iframe.mozRequestFullScreen();
    } else if (iframe.webkitRequestFullscreen) { // Chrome, Safari, Opera
        iframe.webkitRequestFullscreen();
    } else if (iframe.msRequestFullscreen) { // IE/Edge
        iframe.msRequestFullscreen();
    }
}
</script>


## Machine Learning
More examples coming soon!


## Public Kiosk App
More examples coming soon!



</div>
