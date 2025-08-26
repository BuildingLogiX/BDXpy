# AHU Static Pressure Duration Comparison

This example demonstrates how to chart AHU static pressure duration for a time period by AHU.
Load your data from BDXpy, select a timeframe and revise any variables or chart formatting.
## Output


<iframe src="../staticDuration.html" width="800" height="400"></iframe>


??? note "Show Code"
    ```python
    import pandas as pd
    import numpy as np
    import plotly.graph_objects as go

    # Parameters for dummy data
    np.random.seed(0)  # For reproducibility
    num_ahus = 5
    ahus = [f'AHU_{i+1}' for i in range(num_ahus)]
    date_range = pd.date_range(start='2023-10-01', end='2023-10-31', freq='H')
    num_samples = len(date_range)

    # Generate random static pressure data with different transformations for each AHU
    data = {
        'datetime': np.tile(date_range, num_ahus),
        'AHU': np.repeat(ahus, num_samples),
        'static_pressure': []
    }

    # Apply different transformations to each AHU for variation
    for i, ahu in enumerate(ahus):
        if i == 0:  # AHU 1 - Flat line with slight random variation
            pressures = np.random.uniform(1.5, 2.0, num_samples)
        elif i == 1:  # AHU 2 - Logarithmic increase
            pressures = np.logspace(0.1, 1, num_samples) / 10 + np.random.uniform(-0.1, 0.1, num_samples)
        elif i == 2:  # AHU 3 - Polynomial curve (quadratic)
            pressures = (np.linspace(1, 3, num_samples) ** 2) / 5 + np.random.uniform(-0.1, 0.1, num_samples)
        elif i == 3:  # AHU 4 - Polynomial curve (cubic)
            pressures = (np.linspace(1, 3, num_samples) ** 3) / 10 + np.random.uniform(-0.1, 0.1, num_samples)
        else:  # AHU 5 - Linear with slight random variation and top values increased
            pressures = np.linspace(1.0, 3.0, num_samples) + np.random.uniform(-0.1, 0.1, num_samples)
            top_5_percent = int(0.05 * num_samples)
            pressures[:top_5_percent] += np.linspace(0.5, 1.0, top_5_percent)  # Slight increase in top 5%

        data['static_pressure'].extend(pressures)

    # Create the DataFrame
    df = pd.DataFrame(data)

    # Function to generate the duration curve with binned percent exceedance for AHU static pressure
    def generate_binned_duration_curve(df, ahus, bin_width=5):
        duration_data = []
        for ahu in ahus:
            ahu_data = df[df['AHU'] == ahu].copy()
            ahu_data = ahu_data.sort_values(by='static_pressure', ascending=False).reset_index(drop=True)
            
            # Calculate percent exceedance and bin it
            ahu_data['percent_exceedance'] = np.floor(np.arange(1, len(ahu_data) + 1) / len(ahu_data) * 100 / bin_width) * bin_width
            # Group by binned percent_exceedance and calculate mean only on numeric columns
            binned_ahu_data = ahu_data.groupby('percent_exceedance', as_index=False)['static_pressure'].mean()
            binned_ahu_data['AHU'] = ahu  # Retain AHU identifier
            duration_data.append(binned_ahu_data)
        return pd.concat(duration_data, ignore_index=True)

    # Generate binned duration curve data
    duration_df = generate_binned_duration_curve(df, ahus, bin_width=5)

    # Plot the duration curve as overlapping bar charts with wider bins
    def plot_binned_duration_curve(duration_df, ahus):
        fig = go.Figure()
        for ahu in ahus:
            ahu_duration = duration_df[duration_df['AHU'] == ahu]
            fig.add_trace(go.Bar(
                x=ahu_duration['percent_exceedance'],
                y=ahu_duration['static_pressure'],
                name=ahu,
                opacity=0.6
            ))
        fig.update_layout(
            title="Binned Duration Curve for AHU Static Pressure (Overlapping Bar Charts)",
            xaxis_title="Percent Exceedance (%)",
            yaxis_title="Static Pressure (inches of water)",
            barmode='overlay',
            legend_title="AHU",
            template="plotly_white"
        )
        fig.show()

    # Run the plot function to save the file as HTML
    plot_binned_duration_curve(duration_df, ahus)

    ```

