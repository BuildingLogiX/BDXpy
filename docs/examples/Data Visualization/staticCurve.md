# AHU Static Pressure Distribution Curve

This example demonstrates how to chart AHU static pressure distribution for a time period by AHU.
Load your data from BDXpy, select a timeframe and revise any variables or chart formatting.
## Output

<img src="../staticCurve.png" alt="AHU Economizer Analysis" width="100%">


??? note "Show Code"
    ```python
        import pandas as pd
        import numpy as np
        import seaborn as sns
        import matplotlib.pyplot as plt

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

        # Plot the KDE curve using seaborn's displot
        sns.set(style="whitegrid")
        plt.figure(figsize=(10, 6))
        sns.displot(df, x='static_pressure', hue='AHU', kind="kde", fill=True, height=6, aspect=1.5)

        # Set title and adjust layout to avoid cutoff
        plt.suptitle("Curve of Static Pressure Ranges by AHU", y=1.05, fontsize=16)
        plt.xlabel("Static Pressure (in w.c.)")
        plt.ylabel("Density")
        plt.tight_layout(rect=[0, 0, 1, 0.95])  # Adding padding for the title

        # Save the plot as a PNG file
        plt.savefig("AHU_static_pressure_kde_curve.png", bbox_inches="tight")
        plt.show()

    ```

