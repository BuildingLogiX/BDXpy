## Example: Campus Utilities App
Example layout of a BDXpy app for reading/viewing campus utilities
**Note** this may take a minute to load as the example is being hosted on a free tier service

<div style="position: relative; text-align: center;">
    <button onclick="toggleFullScreen()" style="margin-top: 10px;">🔍 Click for Fullscreen</button>
    <iframe id="utl-dashboard" src="https://energy-dashboard-xpwn.onrender.com/" width="800" height="400" style="border: none;"></iframe>
</div>

<script>
function toggleFullScreen() {
    var iframe = document.getElementById("utl-dashboard");
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





