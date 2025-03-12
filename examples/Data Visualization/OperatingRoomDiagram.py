import plotly.graph_objects as go
import pandas as pd
import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as mcolors

# Define seed for reproducibility
np.random.seed(42)

# Define the structure of data
buildings = ["General Hospital", "City Medical Center", "Westside Clinic", "Eastview Hospital"]
air_handlers = {
    "General Hospital": np.random.choice(["GH_AHU1", "GH_AHU2", "GH_AHU3"], size=np.random.randint(1, 4), replace=False).tolist(),
    "City Medical Center": np.random.choice(["CMC_AHU1", "CMC_AHU2", "CMC_AHU3"], size=np.random.randint(1, 4), replace=False).tolist(),
    "Westside Clinic": np.random.choice(["WC_AHU1", "WC_AHU2"], size=np.random.randint(1, 3), replace=False).tolist(),
    "Eastview Hospital": np.random.choice(["EVH_AHU1", "EVH_AHU2", "EVH_AHU3"], size=np.random.randint(1, 4), replace=False).tolist()
}

operating_rooms = {}
for ahu in sum(air_handlers.values(), []):
    num_ors = np.random.randint(2, 7)
    operating_rooms[ahu] = [f"{ahu}_OR{i+1}" for i in range(num_ors)]

# Generate dummy data with updated air changes and runtime-energy cost correlation
data = []
out_of_range_high = 0
out_of_range_low = 0

for building in buildings:
    for ahu in air_handlers[building]:
        for or_room in operating_rooms[ahu]:
            if out_of_range_high < 3 and building == "General Hospital":
                air_changes = np.round(np.random.uniform(23, 28), 2)  # Out of range high
                out_of_range_high += 1
            elif out_of_range_low < 1 and building == "City Medical Center":
                air_changes = np.round(np.random.uniform(17, 19), 2)  # Out of range low
                out_of_range_low += 1
            else:
                air_changes = np.round(np.random.uniform(20, 22), 2)  # Normal range
            
            runtime = np.round(np.random.uniform(50, 168), 2)  # Weekly runtime in hours
            energy_cost = np.round(runtime * air_changes * np.random.uniform(0.5, 1.5), 2)  # Scaled to runtime and air changes
            temperature = np.round(np.random.uniform(60, 80), 2)  # Temperature in F
            data.append([building, ahu, or_room, air_changes, runtime, energy_cost, temperature])

# Convert to DataFrame
columns = ["Building", "AirHandler", "OperatingRoom", "AirChanges", "Runtime", "Cost", "Temperature"]
df = pd.DataFrame(data, columns=columns)

# Aggregate data for Building -> AHU links
ahu_totals = df.groupby(["Building", "AirHandler"]).agg({
    "AirChanges": "sum",
    "Runtime": "sum",
    "Cost": "sum",
    "Temperature": "mean"  # Avg temperature for AHU
}).reset_index()

# Order nodes for better readability
ordered_nodes = []
for b in buildings:
    ordered_nodes.append(b)
    for ahu in air_handlers[b]:
        ordered_nodes.append(ahu)
        ordered_nodes.extend(operating_rooms[ahu])

nodes_map = {node: i for i, node in enumerate(ordered_nodes)}

# Create links with multiple metric values
links = []
link_values = {"AirChanges": [], "Runtime": [], "Cost": [], "Temperature": []}
colors_map = {"AirChanges": [], "Runtime": [], "Cost": [], "Temperature": []}
plasma = cm.get_cmap("plasma")

# Add Building -> AHU links
for _, row in ahu_totals.iterrows():
    links.append({"source": nodes_map[row['Building']], "target": nodes_map[row['AirHandler']]})
    link_values["AirChanges"].append(row['AirChanges'])
    link_values["Runtime"].append(row['Runtime'])
    link_values["Cost"].append(row['Cost'])
    link_values["Temperature"].append(row['Temperature'])
    colors_map["AirChanges"].append("gray")  # Default color
    colors_map["Runtime"].append("gray")
    colors_map["Cost"].append("gray")
    colors_map["Temperature"].append("gray")

# Add AHU -> OR links with color scaling
for _, row in df.iterrows():
    links.append({"source": nodes_map[row['AirHandler']], "target": nodes_map[row['OperatingRoom']]})
    link_values["AirChanges"].append(row['AirChanges'])
    link_values["Runtime"].append(row['Runtime'])
    link_values["Cost"].append(row['Cost'])
    link_values["Temperature"].append(row['Temperature'])
    
    # Air Changes color scheme
    if row['AirChanges'] < 20:
        colors_map["AirChanges"].append("lightcoral")  # Low side
    elif row['AirChanges'] > 22:
        colors_map["AirChanges"].append("firebrick")  # High side
    else:
        colors_map["AirChanges"].append("gray")  # Neutral range
    
    # Runtime and Cost color gradient using plasma colormap
    norm_runtime = (row['Runtime'] - 50) / (168 - 50)  # Normalize runtime
    norm_cost = (row['Cost'] - df['Cost'].min()) / (df['Cost'].max() - df['Cost'].min())
    colors_map["Runtime"].append(mcolors.to_hex(plasma(norm_runtime)))
    colors_map["Cost"].append(mcolors.to_hex(plasma(norm_cost)))
    colors_map["Temperature"].append("gray")  # Keep neutral gray for temperature

# Create Sankey diagram with dropdown selection
fig = go.Figure()
metrics = ["AirChanges", "Runtime", "Cost", "Temperature"]
for metric in metrics:
    fig.add_trace(go.Sankey(
        visible=(metric == "AirChanges"),  # Default visible metric
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color='black', width=0.5),
            label=ordered_nodes
        ),
        link=dict(
            source=[link['source'] for link in links],
            target=[link['target'] for link in links],
            value=link_values[metric],
            color=colors_map[metric]  # Apply colors dynamically
        )
    ))

# Add dropdown menu centered above the chart
fig.update_layout(
    title_text="Weekly KPIs - Operating Rooms",
    font_size=10,
    updatemenus=[
        {
            "buttons": [
                {"label": metric, "method": "update", "args": [{"visible": [m == metric for m in metrics]}]} 
                for metric in metrics
            ],
            "direction": "down",
            "showactive": True,
            "x": 0.5,
            "xanchor": "center",
            "y": 1.15,
            "yanchor": "top",
        }
    ]
)

# Save to HTML
fig.write_html("operating_room_sankey_diagram.html")
fig.show()
