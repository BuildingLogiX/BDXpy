## Example: RTU Monitoring
Dash app containing standard colors and timeframes for various means of display on RTU data from BDX.
This example was deployed on https://render.com/
Beyond the code below there was additional server, css, and enviromental files required to deploy.

<div style="position: relative; text-align: center;">
    <button onclick="toggleFullScreen()" style="margin-top: 10px;">🔍 Click for Fullscreen</button>
    <iframe id="rtu-dashboard" src="https://rtu-dash-bdxpy.onrender.com/" width="800" height="400" style="border: none;"></iframe>
</div>

<script>
function toggleFullScreen() {
    var iframe = document.getElementById("rtu-dashboard");
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

This example demonstrates a dashboard for monitoring RTU (Rooftop Unit) performance using **BDXpy**. It features:

- **Real-time Data Visualization**: Tracks key RTU metrics over time.
- **Interactive Graphs & Charts**: Provides insights into energy consumption and efficiency.
- **Responsive Web Design**: Accessible on both desktop and mobile.

To explore the dashboard, visit the **live demo** above or check out the **source code**.


Code example here: https://github.com/dan-blx/rtu_dash_bdxpy
