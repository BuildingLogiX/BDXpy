## Example: AHU Cooling Performance App
Dash app that loads AHU data from BDX and visualizes Air Handling Unit cooling performance. 
Built with Dash, Plotly, and Dash AG Grid; includes fault filtering and fullscreen views. 


<div style="position: relative; text-align: center;">
    <button onclick="toggleFullScreen()" style="margin-top: 10px;">🔍 Click for Fullscreen</button>
    <iframe id="ahu-dashboard" src="https://ahu-cool-performance-buildinglogix.plotly.app/" width="800" height="400" style="border: none;"></iframe>
</div>

<script>
function toggleFullScreen() {
    var iframe = document.getElementById("ahu-dashboard");
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

Highlights

- **Bubble Chart of Cooling Valve % vs. Coil ΔT (°F)**: size ∝ fan VFD power, color = SAT (°F), optional red halo for AHUs with active faults.
- **Faults Dropdown**: Filter everything (chart + tables) by one or more active faults, or Any active fault.
- **Building Filter**: Multi-select buildings to focus the portfolio view.
- **Centered Link Ribbon**: When a point is clicked, SAT/CCT trend links appear above the chart.
- **Data Grids (AG Grid)**: Sort/filter, quick scan of main metrics and an “Active Faults” table.
- **One-click Downloads**: Export the currently displayed main or faults data to CSV.
- **Fullscreen Overlay**: Expand any chart/table; close with × or Esc.
- **Consistent UI**: Sticky header, compact padding, modern muted icon colors.



