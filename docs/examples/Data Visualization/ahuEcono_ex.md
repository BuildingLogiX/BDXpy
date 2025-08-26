# AHU Economizer Analysis

This example demonstrates a detailed review of AHU economizing conditions
## Output


<img src="../bdxpy econo chart.png" style="width: 100%; height: auto;">


??? note "Show Code"
    ```python
    import pandas as pd
    import plotly.graph_objects as go
    import numpy as np

    # # Load CSV data
    # df = pd


    # Dynamically identify the relevant column names
    occupancy_col = [col for col in df.columns if 'occupancystatus' in col.lower()][0]
    oat_col = [col for col in df.columns if 'outdoorairtemp' in col.lower()][0]
    mat_col = [col for col in df.columns if 'mixedairtemp' in col.lower()][0]
    rat_col = [col for col in df.columns if 'returnairtemp' in col.lower()][0]

    # Filter data for rows where occupancyStatus is 'occupied' and drop rows with NaN in key columns
    occupied_data = df[df[occupancy_col].str.lower() == 'occupied']
    occupied_data = occupied_data.dropna(subset=[oat_col, mat_col, rat_col])

    # Convert columns to numeric
    occupied_data[oat_col] = pd.to_numeric(occupied_data[oat_col], errors='coerce')
    occupied_data[mat_col] = pd.to_numeric(occupied_data[mat_col], errors='coerce')
    occupied_data[rat_col] = pd.to_numeric(occupied_data[rat_col], errors='coerce')

    # Drop rows with any remaining NaN after conversion
    occupied_data = occupied_data.dropna(subset=[oat_col, mat_col, rat_col])

    # Extract min and max values for axes
    oat_min = occupied_data[oat_col].min()
    oat_max = occupied_data[oat_col].max()

    # Calculate thresholds
    supply_air_setpoint = 55
    red_threshold = supply_air_setpoint - 1  # 1 degree below supply air setpoint
    average_rat = occupied_data[rat_col].mean()  # Average return air temperature
    green_threshold = average_rat + 3  # 3 degrees higher than average RAT

    # Define the piecewise function for the ideal line
    def ideal_line(oat):
        if oat <= 53:
            return 53
        elif oat <= 70:
            return 53 + (oat - 53) * 1
        else:
            return 70

    # Generate data points for the ideal line
    oat_range = np.linspace(oat_min, green_threshold, 500)  # Extend range to green threshold
    mat_ideal = [ideal_line(oat) for oat in oat_range]

    # Control bands around the ideal line
    upper_band = [mat + 2 for mat in mat_ideal]
    lower_band = [mat - 2 for mat in mat_ideal]

    # Define the percentage of outside air for minimum operation
    percent_outside_air = 0.2  # 20% outside air

    # Calculate the dynamic minimum outside air line
    min_outside_air = oat_range * percent_outside_air + average_rat * (1 - percent_outside_air)

    # Control bands around the dynamic minimum outside air line
    min_outside_air_upper_band = min_outside_air + 2
    min_outside_air_lower_band = min_outside_air - 2

    # Create the plot using Plotly
    fig = go.Figure()

    # Scatter plot of observed data
    fig.add_trace(go.Scatter(
        x=occupied_data[oat_col],
        y=occupied_data[mat_col],
        mode='markers',
        marker=dict(color='black', size=6, opacity=0.6),
        name='Observed Data'
    ))

    # Ideal line and control bands
    fig.add_trace(go.Scatter(
        x=oat_range,
        y=mat_ideal,
        mode='lines',
        line=dict(color='darkblue', width=3),
        name='Ideal Economizing Line'
    ))
    fig.add_trace(go.Scatter(
        x=oat_range,
        y=upper_band,
        mode='lines',
        line=dict(color='darkblue', dash='dot', width=2),
        name='Upper Control Band'
    ))
    fig.add_trace(go.Scatter(
        x=oat_range,
        y=lower_band,
        mode='lines',
        line=dict(color='darkblue', dash='dot', width=2),
        name='Lower Control Band'
    ))

    # Vertical lines with dynamic thresholds
    fig.add_vline(
        x=red_threshold,
        line_color='red',
        line_dash='dash',
        line_width=2,
        annotation_text=f'Red Threshold ({red_threshold}°F)',
        annotation_position='top left'
    )
    fig.add_vline(
        x=green_threshold,
        line_color='green',
        line_dash='dash',
        line_width=2,
        annotation_text=f'Green Threshold ({green_threshold:.2f}°F)',
        annotation_position='top left'
    )

    # Diagonal 100% outside air line (MAT = OAT)
    fig.add_trace(go.Scatter(
        x=[oat_min, green_threshold],
        y=[oat_min, green_threshold],
        mode='lines',
        line=dict(color='green', width=2),
        name='100% Outside Air Line (MAT = OAT)'
    ))

    # Dynamic minimum outside air line and its control bands
    fig.add_trace(go.Scatter(
        x=oat_range,
        y=min_outside_air,
        mode='lines',
        line=dict(color='red', width=2),
        name='Dynamic Minimum Outside Air Line'
    ))
    fig.add_trace(go.Scatter(
        x=oat_range,
        y=min_outside_air_upper_band,
        mode='lines',
        line=dict(color='red', dash='dot', width=2),
        name='Upper Control Band (+2°F)'
    ))
    fig.add_trace(go.Scatter(
        x=oat_range,
        y=min_outside_air_lower_band,
        mode='lines',
        line=dict(color='red', dash='dot', width=2),
        name='Lower Control Band (-2°F)'
    ))

    # Final plot adjustments
    fig.update_layout(
        title='AHU Economizer Analysis - Operation Chart',
        xaxis_title='Outside Air Temperature (°F)',
        yaxis_title='Mixed Air Temperature (°F)',
        legend=dict(x=0.01, y=0.99, bgcolor='rgba(255,255,255,0.7)'),
        template='plotly_white'
    )

    # Show the plot
    fig.show()

    ```

