# Total Energy Map by Building - Building Type

<div style="position: relative; text-align: center;">
    <button onclick="toggleFullScreen()" style="margin-top: 10px;">🔍 Click for Fullscreen</button>
    <iframe id="energy-map" src="../mapenergychart.html" width="800" height="400" style="border: none;"></iframe>
</div>

<script>
function toggleFullScreen() {
    var iframe = document.getElementById("energy-map");
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


??? note "Show Code"
    Get energy data and sum/chart over map area
    ```python
        ### Use BDXpy here to call your buildings and load a gps file to match on building name #####
        ##  store variables in df in below code

        
        # Ensure your start and end dates are in datetime format
        start_date = pd.to_datetime('2024-09-01')
        end_date = pd.to_datetime('2024-09-30')

        # Filter the DataFrame
        filtered_df = df[(df['Timestamp'] >= start_date) & (df['Timestamp'] <= end_date)]
        filtered_df.to_csv("filtered_df.csv", index=False)

        # Define columns to keep without aggregation (taking the first occurrence)
        cols_to_keep = ["Building Name", "Building Type", "Latitude", "Longitude"]

        # Define columns to sum
        cols_to_sum = ["Total Energy", "Electric Energy", "Cooling Energy", "Heating Energy",
                    "Total Cost", "Metric Tons CO2"]

        # Group by 'Building Name', summing only the relevant columns
        df_summed = filtered_df.groupby("Building Name", as_index=False).agg(
            {**{col: 'first' for col in cols_to_keep},  # Keep first occurrence
            **{col: 'sum' for col in cols_to_sum},  # Sum numeric values
            "Timestamp": "count"}  # Count total rows
        )

        # Rename the counted column
        df_summed = df_summed.rename(columns={"Timestamp": "Total Rows Summed"})
        df_summed.to_csv("df_summed.csv", index=False)

        # Create a map with bubble size variation and opacity
        fig = px.scatter_mapbox(
            df_summed,
            lat='Latitude',
            lon='Longitude',
            hover_name='Building Name',
            size='Total Energy',  # Bubble size based on Total Energy
            color='Building Type',  # Color based on Building Type
            size_max=40,  # Max bubble size
            zoom=14,
            mapbox_style="carto-positron",
            text='Building Name', 
            opacity = 0.6,
            title= "Energy Consumption by Building Type"
        )

        # Set map layout
        fig.update_layout(
            mapbox_center={"lat": 51.7540, "lon": -1.2577},
            margin={"r": 10, "t": 100, "l": 10, "b": 10},
            height=800  # Adjust height for better layout
        )

        fig.update_traces(marker=dict(opacity=0.6))

        fig.show()
        print(fig.data[0])


        # Example usage
        fig.write_html("mapenergychart.html")
    ```