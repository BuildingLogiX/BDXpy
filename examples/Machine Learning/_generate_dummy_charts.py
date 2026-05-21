"""
Generates illustrative (dummy) Plotly charts for the Machine Learning examples
section of the BDXpy docs. Data is synthetic — intended for presentation only.

Run from this directory:
    python _generate_dummy_charts.py
"""
from pathlib import Path
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

OUT = Path(__file__).parent
rng = np.random.default_rng(7)

BLX_BLUE = "#1f4e79"
BLX_ACCENT = "#2e86ab"
BLX_WARN = "#d62828"
BLX_GOOD = "#2a9d8f"
BLX_GREY = "#6c757d"

LAYOUT = dict(
    template="plotly_white",
    font=dict(family="Inter, Segoe UI, Arial", size=13),
    margin=dict(l=60, r=30, t=70, b=50),
    legend=dict(bgcolor="rgba(255,255,255,0.7)"),
)


def write(fig, name):
    fig.update_layout(**LAYOUT)
    fig.write_html(OUT / name, include_plotlyjs="cdn", full_html=True)
    print(f"wrote {name}")


# 1. ENERGY PREDICTION — actual vs. predicted daily campus kWh with confidence band
def energy_prediction():
    dates = pd.date_range("2026-01-01", periods=120, freq="D")
    season = 400 * np.sin(np.linspace(0, 3.5, len(dates))) + 2200
    trend = np.linspace(0, 120, len(dates))
    actual = season + trend + rng.normal(0, 80, len(dates))
    predicted = season + trend + rng.normal(0, 25, len(dates))
    upper = predicted + 110
    lower = predicted - 110

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=list(dates) + list(dates[::-1]),
        y=list(upper) + list(lower[::-1]),
        fill="toself", fillcolor="rgba(31,78,121,0.15)",
        line=dict(color="rgba(0,0,0,0)"), hoverinfo="skip",
        name="95% Confidence Band",
    ))
    fig.add_trace(go.Scatter(x=dates, y=predicted, mode="lines",
                             line=dict(color=BLX_BLUE, width=2.5),
                             name="Predicted kWh"))
    fig.add_trace(go.Scatter(x=dates, y=actual, mode="markers",
                             marker=dict(color=BLX_WARN, size=6, opacity=0.75),
                             name="Actual kWh"))
    fig.update_layout(
        title="Daily Campus Energy — Predicted vs. Actual (Illustrative)",
        xaxis_title="Date", yaxis_title="Energy (kWh)",
        legend=dict(x=0.01, y=0.99),
    )
    write(fig, "energy_prediction.html")


# 2. EQUIPMENT PREDICTION — chiller fault-risk heatmap over time
def equipment_prediction():
    units = [f"CH-{i:02d}" for i in range(1, 13)]
    days = pd.date_range("2026-03-01", periods=45, freq="D")
    base = rng.uniform(0.02, 0.15, size=(len(units), len(days)))
    for i in [2, 6, 9]:
        base[i, -15:] += np.linspace(0.05, 0.7, 15)
    base = np.clip(base, 0, 1)

    fig = go.Figure(data=go.Heatmap(
        z=base, x=days, y=units,
        colorscale=[[0, "#e8f1f8"], [0.4, BLX_ACCENT],
                    [0.75, "#f4a261"], [1, BLX_WARN]],
        colorbar=dict(title="Fault Risk"),
        hovertemplate="%{y} — %{x|%b %d}<br>Risk: %{z:.2f}<extra></extra>",
    ))
    fig.update_layout(
        title="Chiller Fleet — Predicted Fault Risk (Illustrative)",
        xaxis_title="Date", yaxis_title="Chiller",
    )
    write(fig, "equipment_prediction.html")


# 3. HISTORICAL ANALYSIS — long-range load profile clustering / anomaly view
def historical_analysis():
    hours = np.arange(24)
    weekday = 60 + 40 * np.exp(-((hours - 14) ** 2) / 20)
    weekend = 55 + 15 * np.exp(-((hours - 14) ** 2) / 30)
    holiday = 45 + 8 * np.exp(-((hours - 13) ** 2) / 40)
    anomaly = weekday.copy()
    anomaly[18:] += np.linspace(10, 55, 6)

    fig = make_subplots(rows=1, cols=2, column_widths=[0.6, 0.4],
                        subplot_titles=("Typical Daily Load Profiles by Cluster",
                                        "Anomaly Score Distribution"))
    fig.add_trace(go.Scatter(x=hours, y=weekday, mode="lines+markers",
                             name="Weekday", line=dict(color=BLX_BLUE, width=3)), 1, 1)
    fig.add_trace(go.Scatter(x=hours, y=weekend, mode="lines+markers",
                             name="Weekend", line=dict(color=BLX_ACCENT, width=3)), 1, 1)
    fig.add_trace(go.Scatter(x=hours, y=holiday, mode="lines+markers",
                             name="Holiday", line=dict(color=BLX_GOOD, width=3)), 1, 1)
    fig.add_trace(go.Scatter(x=hours, y=anomaly, mode="lines",
                             name="Anomalous Day",
                             line=dict(color=BLX_WARN, width=2, dash="dash")), 1, 1)

    scores = np.concatenate([rng.normal(0.2, 0.08, 400),
                             rng.normal(0.85, 0.05, 25)])
    fig.add_trace(go.Histogram(x=scores, nbinsx=40, marker_color=BLX_BLUE,
                               name="Anomaly Score", showlegend=False), 1, 2)
    fig.add_vline(x=0.6, line_color=BLX_WARN, line_dash="dash",
                  annotation_text="Threshold", annotation_position="top",
                  row=1, col=2)

    fig.update_xaxes(title_text="Hour of Day", row=1, col=1)
    fig.update_yaxes(title_text="Load (kW)", row=1, col=1)
    fig.update_xaxes(title_text="Score", row=1, col=2)
    fig.update_yaxes(title_text="Days", row=1, col=2)
    fig.update_layout(title="Historical Load Clustering & Anomaly Detection (Illustrative)")
    write(fig, "historical_analysis.html")


# 4. CUSTOM ANALYTICS RULES — rule-hit counts and confidence scoring
def custom_analytics_rules():
    rules = [
        "Simultaneous Heat/Cool",
        "Economizer Not Engaging",
        "Static Pressure Reset Idle",
        "VAV Stuck Damper",
        "Chilled Water Reset Missing",
        "AHU Night Setback Fail",
        "Zone Temp Persistent Offset",
        "Fan Runtime Excess",
    ]
    hits = rng.integers(15, 220, size=len(rules))
    confidence = rng.uniform(0.72, 0.98, size=len(rules))
    order = np.argsort(hits)
    rules_s = [rules[i] for i in order]
    hits_s = hits[order]
    conf_s = confidence[order]

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Bar(
        y=rules_s, x=hits_s, orientation="h",
        marker=dict(color=conf_s, colorscale="Blues",
                    cmin=0.7, cmax=1.0,
                    colorbar=dict(title="Rule Confidence", x=1.02)),
        text=[f"{h} hits · {c:.0%}" for h, c in zip(hits_s, conf_s)],
        textposition="outside", name="Rule Hits",
    ))
    fig.update_layout(
        title="Custom Analytics Rules — 30-Day Hit Counts (Illustrative)",
        xaxis_title="Occurrences",
        yaxis_title="",
        height=520,
        showlegend=False,
    )
    write(fig, "custom_analytics_rules.html")


if __name__ == "__main__":
    energy_prediction()
    equipment_prediction()
    historical_analysis()
    custom_analytics_rules()
    print("done.")
