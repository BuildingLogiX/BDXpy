# LLMs

Large Language Models (LLMs) can be used to summarize, interpret, and contextualize findings from BDX data. By processing HVAC and energy system data, LLMs can generate insights in a readable, action-oriented format, assisting building operators, facility managers, and analysts in making data-driven decisions.

**Example Use Case:** VAV Air System Analysis
There is an example using the OpenAI Python package to send BDX data for a VAV air system, prompting the model to generate a summary of airflow anomalies. The LLM can help highlight abnormal trends, suggest possible causes, and provide recommended actions based on the data.

## Using BDXpy with OpenAI API
This guide explains how to use `bdxpy` with an OpenAI API key to analyze HVAC airflow data. The script retrieves airflow data from a BDX instance, detects anomalies, and generates a summary using OpenAI's API.
Sending data to OpenAI is one piece that will be the focus of this example. But how you define data inputs, prompt engineering text, and select models is a crucial piece that each engineer or developer needs to review and account for.

## OpenAI API Rate Limits
OpenAI imposes rate limits on API calls, which vary based on the model and subscription plan. As of recent updates, rate limits typically include:
- **GPT-4o & GPT-4:** Limited to a set number of requests per minute (RPM) and tokens per minute (TPM).
- **GPT-3.5:** More relaxed limits but still subject to RPM and TPM constraints.
- Free-tier users have significantly lower limits compared to API subscription plans.

Refer to OpenAI’s [official rate limits documentation](https://platform.openai.com/docs/guides/rate-limits) for the most up-to-date details.

## Why Sending Large Volumes of raw BDX Data is Not Recommended
The example script retrieves extensive airflow data from a BDX instance, but sending large datasets to OpenAI is **inefficient** due to:  
1. **API Rate Limits:** Exceeding limits can result in throttling or failed requests.  
2. **High Token Costs:** Large payloads consume more tokens, increasing costs.  
3. **Performance Delays:** Processing large text blocks slows down response times and API calls.  

### Recommended Approach:
- **Use OpenAI as a Framework:** Instead of processing large volumes, focus on targeted statistics and smaller timeframes.  
- **Pre-process Data Locally:** Summarize key metrics (e.g., top anomalies, AHU-wide trends) before sending to OpenAI.  
- **Batch Requests:** Instead of one large request, break it into smaller, meaningful prompts.  

## Importance of Prompt Engineering
Prompt engineering plays a **critical** role in obtaining useful outputs from OpenAI models.

### Key Strategies:
- **Be Specific:** Provide context and constraints to guide responses.  
- **Use Formatting Cues:** Structure prompts using bullet points, tables, or numbered lists for better parsing.  
- **Avoid Ambiguity:** Clearly define what constitutes an anomaly or significant event in BDX data.  
- **Iterate and Refine:** Test different prompts to improve accuracy and relevance.  

## Model Selection Impact
Different OpenAI models produce varying results:

- **GPT-4o** (Best for complex, structured data insights)  

- **GPT-3.5** (Faster and cheaper but less accurate for nuanced analysis)  

- **Fine-tuned Models** (Can be trained on historical BDX data for better contextual responses)  

### Choosing the Right Model
| **Use Case**          | **Recommended Model** |
|----------------------|------------------|
| Detailed anomaly detection | GPT-4o |
| General HVAC summaries | GPT-3.5 |
| Custom BDX optimizations | Fine-tuned model |

## Final Recommendations
- Use OpenAI **strategically** to analyze key **data points**, not raw time-series data.  
- Fine-tune prompts to get **actionable insights** instead of general responses.  
- Optimize data selection **before API calls** to reduce costs and improve relevance.  
- Choose models based on complexity and budget.  

By following these best practices, you can maximize OpenAI's value while efficiently leveraging BDX data for meaningful insights.

## Example Code
Below is example code where you can insert BDXpy code to generate chart on the left and an html summary of two difference responses back from OpenAI's API.  
**Note:** these are purely for API example purposes and need heavy modification for custom implementation elsewhere.

??? note "Show Code"
    ```python  
        import openai
        import networkx as nx
        from pyvis.network import Network
        import pandas as pd
        from bdx.core import BDX
        from bdx.auth import UsernameAndPasswordAuthenticator
        from bdx.types import TimeFrame, AggregationLevel
        import matplotlib.pyplot as plt
        import matplotlib.colors as mcolors
        import json
        import os
        import markdown
        from dotenv import load_dotenv

        # Load environment variables
        load_dotenv()

        # OpenAI API Key
        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

        # BDX Credentials
        BDX_URL = os.getenv("BDX_URL")
        USERNAME = os.getenv("BDX_USERNAME")
        PASSWORD = os.getenv("BDX_PASSWORD")
        BUILDING_NAME = "Apex Building" #building name to match component lookups on

        # AHUs to lookup VAVs on per matching logic below
        AHU_NUMBERS = [1, 2, 3, 4, 6, 8]

        # Connect to BDX
        auth = UsernameAndPasswordAuthenticator(USERNAME, PASSWORD)
        with BDX(BDX_URL, auth) as bdx:
            buildings = bdx.buildings.list()
            matching_buildings = [b for b in buildings if b.name.lower() == BUILDING_NAME.lower()]
            if not matching_buildings:
                print(f"No building found with the name: {BUILDING_NAME}")
                exit()

            BUILDING_ID = matching_buildings[0].componentInstanceId
            all_components = bdx.components.by_building(building_id=BUILDING_ID)

            # Map AHUs
            ahu_names = {f"AHU_{num}": f"AHU {num}" for num in AHU_NUMBERS}

            # Filter for VAVs
            vav_components = [
                comp for comp in all_components
                if "VAV_" in comp.path.displayName and any(comp.path.displayName.startswith(f"VAV_{ahu}_") for ahu in AHU_NUMBERS)
            ]

            # Map VAVs to AHUs
            vav_to_ahu = {}
            for vav in vav_components:
                ahu_number = vav.path.displayName.split("_")[1]
                if f"AHU_{ahu_number}" in ahu_names:
                    vav_to_ahu[vav.path.displayName] = f"AHU_{ahu_number}"

            # Retrieve airflow data for two timeframes
            timeframe_current = TimeFrame.last_7_days()
            timeframe_previous = TimeFrame.last_n_days(14)

            properties = [{"componentPathId": vav.path.componentPathId, "propertyName": "airFlow"} for vav in vav_components]

            # Fetch Data
            trend_data_current = bdx.trending.retrieve_data(properties, timeframe_current, AggregationLevel.HOURLY)
            trend_data_previous = bdx.trending.retrieve_data(properties, timeframe_previous, AggregationLevel.HOURLY)

            df_current = trend_data_current.dataframe.fillna(0).set_index("time")
            df_previous = trend_data_previous.dataframe.fillna(0).set_index("time")
            df_previous = df_previous.iloc[:len(df_current)]

            # Compute Percent Differences
            anomalies = []
            all_percent_diffs = {}
            all_current_airflows = {}

            for vav in vav_components:
                comp_id = vav.path.componentPathId
                display_name = vav.path.displayName

                current_airflow = df_current.sum().get(f"{comp_id}_airFlow", 0)
                previous_airflow = df_previous.sum().get(f"{comp_id}_airFlow", 0)

                if previous_airflow != 0:
                    percent_diff = ((current_airflow - previous_airflow) / previous_airflow) * 100
                else:
                    percent_diff = 0

                all_percent_diffs[display_name] = percent_diff
                all_current_airflows[display_name] = current_airflow

                if abs(percent_diff) > 20:
                    anomalies.append({
                        "VAV": display_name,
                        "Current Airflow": round(current_airflow, 2),
                        "Previous Airflow": round(previous_airflow, 2),
                        "Change (%)": round(percent_diff, 2)
                    })

        # -------------------
        # Generate Summary with OpenAI (Using GPT-4o)

        # -------------------
        def generate_summary(anomalies):
            if not anomalies:
                return "<p>No significant anomalies detected in VAV airflow this week.</p>"

        # Customize this prompt depending on your model, needs, performance of the response, etc. **** this prompt engineering is a very important step 

            prompt_text = f"""
            Given the following data on airflow changes for VAVs in a building:
            {json.dumps(anomalies, indent=2)}

            ### **Summary Instructions**
            - **Only report the most significant anomalies** (up to **5 individual VAVs**) OR if there is a **system-wide AHU issue** (total airflow of all VAVs under an AHU changes drastically).
            - **Exclude moderate changes** – I only care about extreme cases that could indicate performance, comfort, or system inefficiencies.
            - **If there are no significant changes**, state: "No major anomalies detected this week."
            - **Airflow data provided in an accumulation of CFM so units are CF
            - **Format the response as concise bullet points**, using **Markdown formatting** for readability.

            ### **Response Format**
            - **Key Findings**  
                - **VAV_3_3:** Airflow increased **+89.09%** 
                🔹 Likely cause: [Occupancy shift / Calibration issue / Setpoint change]  
                🔹 Recommended action: [Verify control settings / Check mechanical operation]  

            - **If AHU-wide issues exist, summarize them separately**  
                - **AHU-1 System-Wide Change:** Total airflow increased by **+250,000 CF**, possibly due to [scheduling changes / pressure setpoint shift].  
                🔹 Recommended action: [Check AHU damper settings / Review scheduling].  

            Make sure the response is **short, direct, and action-oriented**.
            """

            client = openai.OpenAI(api_key=OPENAI_API_KEY)
            
        # if using a specific role/content/assistant in OpenAI make sure to correction specify in the client.chat.completions.create()

            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are an expert in HVAC systems analyzing airflow changes."},
                    {"role": "user", "content": prompt_text}
                ]
            )

            markdown_summary = response.choices[0].message.content
            return markdown.markdown(markdown_summary)  

        summary_text = generate_summary(anomalies)

        # -------------------
        # Generate PyVis Network Chart (With Hover Labels & Correct Sizing)
        # -------------------
        html_path = "VAV_network_summary_openai.html"
        net = Network(height="100vh", width="100%", notebook=True, directed=False)

        # Maintain PyVis physics settings
        net.barnes_hut(gravity=-7000, central_gravity=0.2, spring_length=50, spring_strength=0.03)

        # Add Building Node
        net.add_node("Building", size=100, color="#3e3e3e", label=f"Building: {BUILDING_NAME}", font={"size": 50})

        # Add AHU Nodes
        for ahu, ahu_label in ahu_names.items():
            net.add_node(ahu, size=50, color="#f5d76e", label=ahu_label, font={"size": 40})
            net.add_edge("Building", ahu)

        # Determine maximum airflow for scaling
        overall_max_airflow = max(all_current_airflows.values(), default=1)

        # Add VAV Nodes with Hover Labels and Correct Sizing
        colormap = plt.get_cmap("RdBu_r")
        vmin = min(all_percent_diffs.values(), default=-1)
        vmax = max(all_percent_diffs.values(), default=1)
        norm = mcolors.TwoSlopeNorm(vmin=vmin, vcenter=0, vmax=vmax)

        for vav_name, ahu_name in vav_to_ahu.items():
            percent_diff = all_percent_diffs.get(vav_name, 0)
            current_airflow = all_current_airflows.get(vav_name, 0)

            rgba_color = colormap(norm(percent_diff))
            hex_color = mcolors.to_hex(rgba_color)

            # Scale VAV size based on airflow
            node_size = 5 + (50 * (current_airflow / overall_max_airflow))

            net.add_node(
                vav_name, 
                size=node_size, 
                color=hex_color, 
                title=f"{vav_name} - % Change: {percent_diff:.2f}%, Airflow: {current_airflow:.2f}",
                font={"size": 30}
            )
            net.add_edge(ahu_name, vav_name, width=1)

        # Save chart
        net.save_graph(html_path)

        # -------------------
        # Write Final HTML
        # -------------------
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(f"""
            <html>
            <head>
                <style>
                    body {{
                        font-size: 12px; /* Base font size for body text */
                    }}
                    .container {{
                        display: flex;
                        height: 100vh;
                        width: 100%;
                    }}
                    .left {{
                        width: 50%;
                        height: 100%;
                        overflow-y: hidden; /* No scrollbar on left (chart) */
                    }}
                    .right {{
                        width: 50%;
                        background: #f4f4f4;
                        padding: 20px;
                        overflow-y: auto; /* Keep scrollbar on right (text) */
                        font-size: 10px !important; /* Force body text size with !important */
                        line-height: 1.5;
                        box-sizing: border-box;
                    }}
                    /* Force smaller header sizes in .right with higher specificity */
                    .right h1 {{
                        font-size: 16px !important; /* Smaller headline */
                    }}
                    .right h2 {{
                        font-size: 14px !important; /* Smaller subhead */
                    }}
                    .right h3 {{
                        font-size: 12px !important; /* Match body text size */
                    }}
                    /* Ensure all text in .right inherits the base size */
                    .right * {{
                        font-size: 10px !important; /* Apply to all elements in .right */
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="left">{net.generate_html()}</div>
                    <div class="right">{summary_text}</div>
                </div>
            </body>
            </html>
            """)


        print(f"Final version saved in '{html_path}'. Open in a browser.")
    ```
