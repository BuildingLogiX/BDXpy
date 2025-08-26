# Building Airflow by AHU and VAV

This example demonstrates the relationships, location, and changes related to airflow across different air systems within a building.


## Output

<div style="position: relative; text-align: center;">
    <button onclick="toggleFullScreen()" style="margin-top: 10px;">🔍 Click for Fullscreen</button>
    <iframe id="airflow-sankey" src="../airflow_sankey.html" width="800" height="400" style="border: none;"></iframe>
</div>

<script>
function toggleFullScreen() {
    var iframe = document.getElementById("airflow-sankey");
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
    ```python
    import networkx as nx
    from pyvis.network import Network
    import pandas as pd
    from bdx.core import BDX
    from bdx.auth import UsernameAndPasswordAuthenticator
    from bdx.types import TimeFrame, AggregationLevel
    from bdx.components import ComponentFilter
    import matplotlib.pyplot as plt
    import matplotlib.cm as cm
    import matplotlib.colors as mcolors

    # BDX Credentials and Connection
    BDX_URL = "http://yourURL.com"  # Replace with your actual BDX URL
    USERNAME = "YOUR_USERNAME"
    PASSWORD = "YOUR_PASSWORD"
    BUILDING_NAME = "YOUR_BUILDINGNAME"

    # Connect to BDX
    auth = UsernameAndPasswordAuthenticator(USERNAME, PASSWORD)
    with BDX(BDX_URL, auth) as bdx:
        buildings = bdx.buildings.list()
        matching_buildings = [b for b in buildings if b.name.lower() == BUILDING_NAME.lower()]
        if not matching_buildings:
            print(f"No building found with the name: {BUILDING_NAME}")
            exit()
        
        BUILDING_ID = matching_buildings[0].componentInstanceId
        BUILDING_NODE = f"Building: {BUILDING_NAME}"

        print(f"\nSelected Building ID: {BUILDING_ID} for '{BUILDING_NAME}'")

        # Retrieve all components
        all_components = bdx.components.by_building(building_id=BUILDING_ID)

        # Define AHUs of interest
        AHU_NUMBERS = [1, 2, 3, 4, 6, 8]
        ahu_names = {f"AHU_{num}": f"AHU {num}" for num in AHU_NUMBERS}

        # Prepare dict to hold AHU -> list of VAV components
        ahu_components = {ahu: [] for ahu in ahu_names}

        # Manually filter for VAVs that belong to these AHUs
        vav_components = [
            comp for comp in all_components 
            if "VAV_" in comp.path.displayName 
            and any(comp.path.displayName.startswith(f"VAV_{ahu}_") for ahu in AHU_NUMBERS)
        ]

        # Map each VAV displayName -> AHU_x
        vav_to_ahu = {}
        for vav in vav_components:
            ahu_number = vav.path.displayName.split("_")[1]  # Extract "1" from "VAV_1_xxx"
            if f"AHU_{ahu_number}" in ahu_names:
                vav_to_ahu[vav.path.displayName] = f"AHU_{ahu_number}"
                ahu_components[f"AHU_{ahu_number}"].append(vav)

        # Retrieve airFlow data for two timeframes
        timeframe_current = TimeFrame.last_7_days()
        timeframe_previous = TimeFrame.last_n_days(14)  # last 14 days, but we'll only compare the first 7 to the last 7

        properties = [{"componentPathId": vav.path.componentPathId, "propertyName": "airFlow"} for vav in vav_components]

        # Get current week data (7 days)
        trend_data_current = bdx.trending.retrieve_data(properties, timeframe_current, AggregationLevel.HOURLY)
        df_current = trend_data_current.dataframe.fillna(0).set_index("time")

        # Get previous week data (7 days before that)
        trend_data_previous = bdx.trending.retrieve_data(properties, timeframe_previous, AggregationLevel.HOURLY)
        df_previous = trend_data_previous.dataframe.fillna(0).set_index("time")
        # Trim previous to same length as current (assumes same # of hours)
        df_previous = df_previous.iloc[: len(df_current)]

        # Aggregate total airflow for both timeframes
        total_airflow_current = df_current.sum().to_dict()   # e.g. {'compId_airFlow': totalCFM, ...}
        total_airflow_previous = df_previous.sum().to_dict()

    # -----------------------------------------------------------------------------
    # 1) Compute all percent differences in one pass
    # -----------------------------------------------------------------------------
    all_percent_diffs = {}
    all_current_airflows = {}

    for vav_comp in vav_components:
        comp_id = vav_comp.path.componentPathId
        current_airflow = total_airflow_current.get(f"{comp_id}_airFlow", 0)
        previous_airflow = total_airflow_previous.get(f"{comp_id}_airFlow", 0)
        if previous_airflow != 0:
            percent_diff = ((current_airflow - previous_airflow) / previous_airflow) * 100
        else:
            percent_diff = 0

        # Store these results by VAV displayName
        all_percent_diffs[vav_comp.path.displayName] = percent_diff
        all_current_airflows[vav_comp.path.displayName] = current_airflow

    # If everything is empty, avoid errors
    if len(all_percent_diffs) == 0:
        vmin, vmax = -1, 1
    else:
        vmin = min(all_percent_diffs.values())
        vmax = max(all_percent_diffs.values())

    # -----------------------------------------------------------------------------
    # 2) Create the TwoSlopeNorm and colormap once
    # -----------------------------------------------------------------------------
    colormap = plt.get_cmap("RdBu_r")  # Blue for negative, red for positive
    norm = mcolors.TwoSlopeNorm(vmin=vmin, vcenter=0, vmax=vmax)

    # For consistent node sizing, get the max current airflow across all VAVs
    if len(all_current_airflows) == 0:
        overall_max_airflow = 1
    else:
        overall_max_airflow = max(all_current_airflows.values())

    # -----------------------------------------------------------------------------
    # 3) Build the PyVis network
    # -----------------------------------------------------------------------------
    net = Network(height="1000px", width="100%", notebook=True, directed=False)

    # Enable physics for dynamic spacing (avoids overlap)
    net.barnes_hut(gravity=-7000, central_gravity=0.2, spring_length=50, spring_strength=0.03)

    # Add building node
    net.add_node(
        BUILDING_NODE, 
        size=100, 
        color="#3e3e3e", 
        label=f"Building: Apex Pavilion", 
        physics=True,
        font={"size": 50}
    )

    # Add AHU nodes & connect them to the building
    for ahu, ahu_label in ahu_names.items():
        net.add_node(
            ahu, 
            size=50, 
            color="#f5d76e", 
            label=f"P1_{ahu_label}", 
            physics=True,
            font={"size": 40}
        )
        net.add_edge(BUILDING_NODE, ahu)

        # Get the VAV displayNames belonging to this AHU
        ahu_vavs = [vav for vav, linked_ahu in vav_to_ahu.items() if linked_ahu == ahu]

        # Sort them by absolute airflow change if you wish
        # (We can derive airflow change from the stored percent or from the actual flows if needed.)
        # For demonstration, let's just get the current minus previous from all_percent_diffs if needed.
        # But you already had a dictionary "airflow_differences" if you want to re-use it.
        # We'll do a quick inline approach:
        def get_airflow_change(vav_disp_name):
            # We can reconstruct from percent_diffs or better, do a direct sum again:
            # But let's use the dictionary "airflow_differences" from your original code.
            # If you still want that, we can compute it similarly:
            comp = next((c for c in vav_components if c.path.displayName == vav_disp_name), None)
            if comp is None:
                return 0
            comp_id = comp.path.componentPathId
            cur_val = total_airflow_current.get(f"{comp_id}_airFlow", 0)
            prev_val = total_airflow_previous.get(f"{comp_id}_airFlow", 0)
            return (cur_val - prev_val)

        sorted_vavs = sorted(
            ahu_vavs,
            key=lambda name: abs(get_airflow_change(name)),
            reverse=True
        )

        # Loop through each VAV
        for vav_disp_name in sorted_vavs:
            # Grab the current airflow & percent diff we stored
            current_airflow = all_current_airflows.get(vav_disp_name, 0)
            percent_diff = all_percent_diffs.get(vav_disp_name, 0)

            # Convert the percent_diff to a color
            rgba_color = colormap(norm(percent_diff))  # e.g. negative => bluish, positive => reddish
            hex_color = mcolors.to_hex(rgba_color)

            # Scale VAV size by current airflow
            node_size = 20 + (50 * (current_airflow / max(1, overall_max_airflow)))

            # Add VAV node
            net.add_node(
                vav_disp_name, 
                size=node_size, 
                color=hex_color,
                title=f"{vav_disp_name} - % Change: {percent_diff:.2f}%, Airflow: {current_airflow:.2f}",
                physics=True,
                font={"size": 30}
            )

            # Add edge from AHU -> VAV
            net.add_edge(
                ahu,
                vav_disp_name,
                width=1,
                title=f"% Change: {percent_diff:.2f}%"
            )

    # Generate and save the network visualization
    net.show("VAV_network.html")

    print("\n✅ Network visualization saved as 'VAV_network.html'. Open it in a browser to view.")


    ```

