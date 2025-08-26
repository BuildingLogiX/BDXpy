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


??? note "Show Code"
    ```python
        import pandas as pd
        from bdx.core import BDX
        from bdx.auth import UsernameAndPasswordAuthenticator
        from bdx.types import TimeFrame, AggregationLevel
        from bdx.components import ComponentFilter
        import plotly.express as px
        import dash
        from dash import dcc, html, Output, Input, ctx
        from dash.dependencies import Input, Output
        import re

        ##### APP Contains commented our BDXpy api sections and loads csv with dummy data instead.

        # BDX Credentials and Connection
        # BDX_URL = "http://your_BDX_URL.com"  # Replace with your actual BDX URL
        # USERNAME = "BDX_USERNAME"
        # PASSWORD = "BDX_PASSWORD"
        # BUILDING_NAME = "BuildingLogiX Campus" #name of the building in bdx for searching equipment ids

        # # Authenticate
        # auth = UsernameAndPasswordAuthenticator(USERNAME, PASSWORD)

        # with BDX(BDX_URL, auth) as bdx:
        #     buildings = bdx.buildings.list()
        #     matching_buildings = [b for b in buildings if b.name.lower() == BUILDING_NAME.lower()]
        #     if not matching_buildings:
        #         print(f"No building found with the name: {BUILDING_NAME}")
        #         exit()
            
        #     BUILDING_ID = matching_buildings[0].componentInstanceId
        #     BUILDING_NODE = f"Building: {BUILDING_NAME}"

        #     print(f"\nSelected Building ID: {BUILDING_ID} for '{BUILDING_NAME}'")
            
        #     components = bdx.components.by_building(BUILDING_ID)

        #     # Extract relevant component details into a DataFrame
        #     component_data = []

        #     # Iterate through retrieved components
        #     for component in components:
        #         component_data.append({
        #             "Component ID": component.componentInstanceId,
        #             "Display Name": component.path.displayName if component.path else "N/A",
        #             "Full Path": component.path.fullPath if component.path else "N/A",
        #             "Template Type": component.templateType,
        #             "Parent Name": component.parentName,
        #             "Root Parent Name": component.rootParentName
        #         })

        #     # Convert to DataFrame
        #     components_df = pd.DataFrame(component_data)


        #     filtered_components = [
        #         c for c in components
        #         if c.templateType == "LargeRtu" and c.path and "RTU_" in c.path.displayName
        #     ]

        #     # Convert filtered components to a DataFrame
        #     filtered_data = [
        #         {
        #             "Component Inst ID": c.componentInstanceId,
        #             "Display Name": c.path.displayName,
        #             "Full Path": c.path.fullPath,
        #             "Template Type": c.templateType,
        #         }
        #         for c in filtered_components
        #     ]

        #     filtered_df = pd.DataFrame(filtered_data)
            
        #     print(filtered_df)

        #     # Define properties to retrieve
        #     properties_to_fetch = [
        #         "ductStaticPressure",
        #         "ductStaticPressureSetpoint",
        #         "supplyAirTemp",
        #         "supplyFanVFDPercent",
        #         "supplyFanVFDPower",
        #         "coolOutput",
        #         "supplyFanStatus"
        #     ]

        #     data_requests = []

        #     # Create property descriptors
        #     for component in filtered_components:
        #         if component.path and component.path.componentPathId:  # Ensure the path exists
        #             for prop in properties_to_fetch:
        #                 data_requests.append({
        #                     "componentPathId": component.path.componentPathId,
        #                     "propertyName": prop
        #                 })

        #     # Debugging: Check if requests were created
        #     print(f"Total Data Requests: {len(data_requests)}")
        #     if len(data_requests) == 0:
        #         print("⚠ No data requests were generated! Check component paths.")

        #     # Fetch trending data for the last 7 days
        #     timeframe = TimeFrame.last_7_days()
        #     retrieval_result = bdx.trending.retrieve_data(data_requests, timeframe, AggregationLevel.POINT)

        #     # Convert the data to a Pandas DataFrame
        #     df = retrieval_result.dataframe

        #     # Create a mapping for renaming columns
        #     column_renaming = {}

        #     # Iterate through the filtered components to find correct display names
        #     for component in filtered_components:
        #         if component.path and component.path.componentPathId:  # Ensure valid path
        #             for prop in properties_to_fetch:
        #                 old_column_name = f"{component.path.componentPathId}_{prop}"
        #                 new_column_name = f"{component.path.displayName}_{prop}"
        #                 column_renaming[old_column_name] = new_column_name

        #     # Rename the columns
        #     df.rename(columns=column_renaming, inplace=True)

        #     # Print sample data with updated column names
        #     print(df.head())

        # -------------------------------------------------------------------------
        # 1) Load CSV data for dummy app data
        # -------------------------------------------------------------------------
        csv_file = "bdx_large_rtu_data_ex.csv"  # Update if needed
        df = pd.read_csv(csv_file)
        df['time'] = pd.to_datetime(df['time'])  # Ensure 'time' is a datetime

        # -------------------------------------------------------------------------
        # 2) Extract RTU names using regex
        # -------------------------------------------------------------------------
        rtu_names = sorted(
            set(re.findall(r'RTU_\d+', col)[0] for col in df.columns if re.findall(r'RTU_\d+', col))
        )

        # -------------------------------------------------------------------------
        # 3) Define a color map for RTUs
        # -------------------------------------------------------------------------
        color_seq = px.colors.qualitative.Dark24  # or choose another
        color_map = {}
        for i, rtu in enumerate(rtu_names):
            color_map[rtu] = color_seq[i % len(color_seq)]

        # For wide-format line plots, define a color sequence matching rtu_names order
        wide_format_colors = [color_map[rtu] for rtu in rtu_names]

        # -------------------------------------------------------------------------
        # 4) Define GPS coordinates for the 17 RTUs (example data)
        # -------------------------------------------------------------------------
        rtu_gps_data = {
            "RTU#": [f"RTU_{i}" for i in range(1, 18)],
            "Latitude": [
                52.00837569274067, 52.00830627568983, 52.00875609626744, 52.00854506989283,
                52.009003217993765, 52.00886993902999, 52.009108730225236, 52.009291987720204,
                52.0095002339626, 52.009336413666574, 52.009850085476714, 52.0101804982761,
                52.0103470920397, 52.00682072496339, 52.006956786798256, 52.006543046465836,
                52.0071900346995
            ],
            "Longitude": [
                -0.6927407350645639, -0.6933361764343267, -0.6924385034602146, -0.6916310488754607,
                -0.6915904506002495, -0.6919964333523606, -0.6904852753306141, -0.690088314417439,
                -0.6904762534916784, -0.6932865563201799, -0.6924610580520515, -0.6922445339175922,
                -0.6918746385212245, -0.6932053597447845, -0.6927768223953339, -0.6926550275697007,
                -0.6916265378920792
            ]
        }
        rtu_gps_df = pd.DataFrame(rtu_gps_data)

        # Calculate average lat/lon for map centering
        center_lat = rtu_gps_df["Latitude"].mean()
        center_lon = rtu_gps_df["Longitude"].mean()

        # -------------------------------------------------------------------------
        # 5) Dash App layout
        # -------------------------------------------------------------------------
        app = dash.Dash(__name__)

        # Define server (needed for deployment)
        server = app.server 

        app.layout = html.Div([
            html.Div([
                html.Img(src="/assets/blx white.svg", className="logo"),  # Logo (Make sure it's in the "assets" folder)
                html.H1("BuildingLogiX RTU Monitoring", className="header-text")
            ], className="header", style={"backgroundColor": "#00274D", "padding": "15px", "textAlign": "center"}),
            html.Div([
                # Left column
                html.Div([
                    # Top row: Map
                    dcc.Graph(id='map-runtime', style={'height': '700px'}, config={'scrollZoom': True}),

                    # Middle row: Violin (SupplyAirTemp, fan on)
                    dcc.Graph(id='violin-supply-air'),

                    # Bottom row: Time series (SupplyAirTemp)
                    dcc.Graph(id='time-series-supply-air')
                ], style={'width': '50%', 'display': 'inline-block'}),

                # Right column
                html.Div([
                    # Top row: Polar (VFD Power)
                    dcc.Graph(id='polar-vfd-power', style={'height': '700px'}),

                    # Middle row: Violin (Duct Static, fan on)
                    dcc.Graph(id='kde-duct-static'),

                    # Bottom row: Time series (SupplyFanSpeed)
                    dcc.Graph(id='time-series-duct-static')
                ], style={'width': '50%', 'display': 'inline-block'})
            ])
        ])

        # -------------------------------------------------------------------------
        # 6) Dash Callback for all figures
        # -------------------------------------------------------------------------
        @app.callback(
            Output('map-runtime', 'figure'),
            Output('violin-supply-air', 'figure'),
            Output('time-series-supply-air', 'figure'),
            Output('polar-vfd-power', 'figure'),
            Output('kde-duct-static', 'figure'),
            Output('time-series-duct-static', 'figure'),
            Input('map-runtime', 'clickData'),
        )

        def update_charts(_):
            """
            Returns six figures for the dashboard:
            1) Map showing RTU runtime hours (marker size), labeled with RTU name + hours
            2) Violin plot of Supply Air Temp (fan on)
            3) Time series of Supply Air Temp (wide format)
            4) Polar chart of VFD Power (most recent sample)
            5) Violin plot of Duct Static Pressure (fan on)
            6) Time series of Supply Fan Speed (wide format)
            """

            # ---------------------------------------------------------------------
            # A) Most recent data row (for polar chart)
            # ---------------------------------------------------------------------
            latest_data = df.iloc[-1]

            # ---------------------------------------------------------------------
            # B) Map: RTU Runtime Hours
            # ---------------------------------------------------------------------
            # Summation of supplyFanStatus over all rows => total "on" intervals
            # Each row is presumably 15 minutes => multiply by 0.25 to convert to hours
            runtime_values = [
                df[f"{rtu}_supplyFanStatus"].sum() * 0.25
                for rtu in rtu_names
            ]

            # Build a DF for the map
            runtime_df = rtu_gps_df.copy()
            runtime_df["RuntimeHours"] = runtime_values
            
            # Add a label with RTU name and hours on separate lines
            runtime_df["Label"] = runtime_df["RTU#"] + "<br>" + runtime_df["RuntimeHours"].round(1).astype(str) + " hrs"


            map_fig = px.scatter_mapbox(
                runtime_df,
                lat="Latitude",
                lon="Longitude",
                size="RuntimeHours",
                size_max=20,
                color="RuntimeHours",  # Assigns a color gradient based on runtime
                color_continuous_scale="Viridis",  # You can use "Plasma", "Cividis", "Turbo", etc.
                hover_name="RTU#",      # Shown in hover tooltip
                text="Label",           # Shown on the map
                title="RTU Runtime Map - Last 7 Days",
                zoom=15.5,
                center=dict(lat=center_lat, lon=center_lon),
                mapbox_style="carto-positron"
            )

            # Display the labels above each marker
            map_fig.update_traces(
                mode="markers+text",
                textposition="bottom center"
            )

            map_fig.update_layout(
                dragmode="pan",
                uirevision="constant",
                mapbox=dict(
                    pitch=60,  # Tilt for 3D effect
                    bearing=0,  # Rotate the view
                    style="carto-positron"
                )
            )



            # ---------------------------------------------------------------------
            # C) Violin: SupplyAirTemp (fan on)
            # ---------------------------------------------------------------------
            sat_dfs = []
            for rtu in rtu_names:
                sub_df = df[['time', f"{rtu}_supplyAirTemp", f"{rtu}_supplyFanStatus"]].copy()
                sub_df.rename(columns={
                    f"{rtu}_supplyAirTemp": "SupplyAirTemp",
                    f"{rtu}_supplyFanStatus": "SupplyFanStatus"
                }, inplace=True)
                sub_df["RTU"] = rtu
                sat_dfs.append(sub_df)

            melted_sat = pd.concat(sat_dfs, ignore_index=True)

            # Filter to fan on (True or ==1, depending on your data)
            melted_sat = melted_sat[melted_sat["SupplyFanStatus"] == True]
            melted_sat.dropna(subset=["SupplyAirTemp"], inplace=True)

            # Sort RTUs by descending average supply air temp
            avg_sat = melted_sat.groupby("RTU")["SupplyAirTemp"].mean().sort_values(ascending=False)
            rtu_order_sat = list(avg_sat.index)

            violin_sat_fig = px.violin(
                melted_sat,
                x="RTU",
                y="SupplyAirTemp",
                color="RTU",
                color_discrete_map=color_map,
                category_orders={"RTU": rtu_order_sat},
                box=True,
                points=False,
                hover_data=["time"],
                title="Operating Supply Air Temp"
            )

            # ---------------------------------------------------------------------
            # D) Time Series: SupplyAirTemp (wide format)
            # ---------------------------------------------------------------------
            supply_temp_fig = px.line(
                df,
                x="time",
                y=[f"{rtu}_supplyAirTemp" for rtu in rtu_names],
                title="Supply Air Temp Over Time",
                color_discrete_sequence=wide_format_colors
            )

            # ---------------------------------------------------------------------
            # E) Polar Chart: Supply Fan VFD Power (most recent)
            # ---------------------------------------------------------------------
            polar_df = pd.DataFrame({
                "RTU": rtu_names,
                "VFDPower": [latest_data[f"{rtu}_supplyFanVFDPower"] for rtu in rtu_names]
            })

            polar_fig = px.bar_polar(
                polar_df,
                r="VFDPower",
                theta="RTU",
                color="RTU",
                color_discrete_map=color_map,
                title="RTU kW (Most Recent)"
            )

            # ---------------------------------------------------------------------
            # F) Violin: Duct Static Pressure (fan on)
            # ---------------------------------------------------------------------
            rtu_dfs_2 = []
            for rtu in rtu_names:
                sub_df = df[['time', f"{rtu}_ductStaticPressure", f"{rtu}_supplyFanStatus"]].copy()
                sub_df.rename(columns={
                    f"{rtu}_ductStaticPressure": "DuctStaticPressure",
                    f"{rtu}_supplyFanStatus": "SupplyFanStatus"
                }, inplace=True)
                sub_df["RTU"] = rtu
                rtu_dfs_2.append(sub_df)

            melted_static = pd.concat(rtu_dfs_2, ignore_index=True)

            # Filter to fan on (True or 1)
            melted_static = melted_static[melted_static["SupplyFanStatus"] == True]
            melted_static.dropna(subset=["DuctStaticPressure"], inplace=True)

            avg_static = melted_static.groupby("RTU")["DuctStaticPressure"].mean().sort_values(ascending=False)
            rtu_order = list(avg_static.index)

            kde_fig = px.violin(
                melted_static,
                x="RTU",
                y="DuctStaticPressure",
                color="RTU",
                color_discrete_map=color_map,
                category_orders={"RTU": rtu_order},
                box=True,
                points=False,
                hover_data=["time"],
                title="Operating Duct Static Pressure"
            )

            # ---------------------------------------------------------------------
            # G) Time Series: Supply Fan Speed (wide format)
            # ---------------------------------------------------------------------
            speed_fig = px.line(
                df,
                x="time",
                y=[f"{rtu}_supplyFanVFDPercent" for rtu in rtu_names],
                title="Supply Fan Speed Over Time",
                color_discrete_sequence=wide_format_colors
            )

            return (
                map_fig,
                violin_sat_fig,
                supply_temp_fig,
                polar_fig,
                kde_fig,
                speed_fig
            )



        if __name__ == '__main__':
            app.run_server(debug=False)
    ```

