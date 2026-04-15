# LLM Integrations

<div align="center" style="display:flex; justify-content:center; align-items:center; gap:40px; margin: 20px 0 30px 0; flex-wrap:wrap;">
  <div style="text-align:center;">
    <img src="../../assets/openai.svg" alt="OpenAI" width="60" height="60">
    <div style="font-size:12px; margin-top:6px;"><strong>OpenAI</strong></div>
  </div>
  <div style="text-align:center;">
    <img src="https://cdn.simpleicons.org/claude/D97757" alt="Claude" width="60" height="60">
    <div style="font-size:12px; margin-top:6px;"><strong>Claude</strong></div>
  </div>
  <div style="text-align:center;">
    <img src="https://cdn.simpleicons.org/googlegemini/4285F4" alt="Gemini" width="60" height="60">
    <div style="font-size:12px; margin-top:6px;"><strong>Gemini</strong></div>
  </div>
</div>

> **BDXpy is LLM-agnostic.** Pipe live building data into the model of your choice — OpenAI, Claude, Gemini, or a self-hosted model — and turn raw HVAC and energy telemetry into decisions, narratives, and actions.

---

## Why Pair BDXpy With an LLM?

BDX gives you structured, high-fidelity building data. An LLM gives you reasoning, language, and summarization. Together they let a building "explain itself" — anomalies become recommendations, dashboards gain narrative, and operators get answers in plain English instead of spreadsheets.

**BDXpy acts as the bridge:** it authenticates, queries the building graph, pulls trend data at the right aggregation level, and hands the LLM a clean, token-efficient payload.

---

## What You Can Build

=== "Data Analyst"
    Feed BDXpy outputs — anomalies, utility spikes, equipment drift — to an LLM and get back a written summary, root-cause hypotheses, and prioritized actions. Replace the weekly report that nobody reads with a targeted brief that operators actually act on.

=== "Chatbot"
    Wrap BDXpy in a chat interface and let users ask:  
    *"Which VAVs are underperforming on AHU-3 this week?"*  
    *"Compare last month's chiller plant efficiency to the prior year."*  
    *"Why did the east wing setpoint drift overnight?"*  
    The LLM handles intent; BDXpy handles the query; the user gets an answer grounded in real data — not hallucination.

=== "Data Scientist"
    Use an LLM to scaffold analytics workflows: feature engineering on trend data, clustering similar equipment, drafting ML notebooks, and interpreting model outputs. BDXpy supplies the dataset; the LLM accelerates the exploratory loop.

=== "Agentic Workflows"
    Give an agent tools — `list_buildings`, `get_trend_data`, `find_anomalies` — and let it plan multi-step analyses on its own. Ideal for nightly runs, commissioning sweeps, and portfolio-wide audits.

=== "Narrative Reporting"
    Auto-generate monthly M&V reports, commissioning summaries, and stakeholder briefings. The LLM writes; BDXpy supplies the numbers; the human reviews.

=== "Copilot for Engineers"
    Paste a tag, a trend, or an error into chat and let the LLM + BDXpy lookup return context: what equipment it belongs to, recent behavior, related alarms, and likely next steps.

---

## BDXpy + `bdxpy-skills` for Agents

For agent-driven workflows, **`bdxpy-skills`** (available upon request) packages BDXpy's capabilities into pre-built tool definitions and prompts optimized for modern LLM function-calling and tool-use APIs. Drop it into a Claude agent, an OpenAI Assistant, a Gemini function-calling flow, or a Claude Agent SDK / LangChain / CrewAI project and skip the plumbing.

**What you get:**

- Tool schemas for the most common BDX operations (components, trends, alarms, buildings)
- Prompt scaffolding tuned for building-analytics reasoning
- Guardrails for token-efficient queries against large BDX datasets
- Examples for multi-provider deployment — the same skills, different back-ends

> *Interested in `bdxpy-skills`?* Reach out to BuildingLogiX to discuss access and a fit for your use case.

---

## Supercharge with CLIs & IDE Extensions

You don't have to build chat UIs from scratch. The fastest way to get BDXpy + LLM value today is to meet engineers **where they already work** — the terminal and the editor.

=== "Terminal CLIs"
    Purpose-built coding agents that run right in your shell, read your repo, and execute tools:

    - **[Claude Code](https://docs.claude.com/en/docs/claude-code/overview)** — Anthropic's official CLI; strong at multi-file edits, long-context reasoning, and skill/agent workflows
    - **[OpenAI Codex CLI](https://github.com/openai/codex)** — terminal agent for OpenAI models
    - **[Gemini CLI](https://github.com/google-gemini/gemini-cli)** — Google's open-source terminal agent

    Point any of these at a BDXpy project and ask: *"Write a script that pulls last week's chilled-water flow and flags sensors stuck at zero."* The agent reads your code, drafts it, and you review the diff.

=== "VS Code Extensions"
    Keep the LLM inside the editor where the code lives:

    - **[Claude Code for VS Code](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code)** — native extension with inline diffs and agent sessions
    - **[GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)** / **Copilot Chat** — in-editor completions and chat (OpenAI-powered, plus model picker)
    - **[Gemini Code Assist](https://marketplace.visualstudio.com/items?itemName=Google.geminicodeassist)** — Google's VS Code integration
    - **[Cline](https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev)** / **[Continue](https://marketplace.visualstudio.com/items?itemName=Continue.continue)** — provider-agnostic extensions; bring your own API key for OpenAI, Claude, Gemini, or local models

=== "Why this matters for BDXpy users"
    - **Zero boilerplate** — no need to stand up a chat app to start getting value
    - **Context-aware** — the agent sees your actual BDXpy code, `.env` structure, and prior scripts
    - **Skills & agents** — pair with `bdxpy-skills` to give the CLI a toolbox of BDX operations it can call directly
    - **Consistent across providers** — the same workflow whether your org standardizes on OpenAI, Claude, or Gemini

> **Tip:** pair a CLI with a project-level `CLAUDE.md` (or equivalent instructions file) that documents your BDX conventions, preferred libraries, and data hygiene rules. The agent will follow them on every run.

---

## Working Principles (Provider-Agnostic)

Regardless of which model you pick, a few rules keep LLM integrations fast, cheap, and useful:

### 1. Don't send raw time-series
LLMs are reasoning engines, not log parsers. Pre-process in BDXpy first — compute deltas, top-N anomalies, AHU roll-ups — then send the summary.

### 2. Prompt engineering is the product
Model choice matters less than prompt quality. Be specific, give formatting cues, define what "anomaly" means in your context, and iterate.

### 3. Respect rate limits and token budgets
Every provider throttles. Batch requests, cache where possible, and keep payloads lean.

### 4. Choose the model to fit the job
Use larger, reasoning-grade models for nuanced analysis and smaller, faster models for classification or routing. Most providers offer a tiered family — start cheap, escalate when the task demands it.

### 5. Keep a human in the loop
LLM outputs are recommendations, not commands. Route suggestions through an operator before anything writes back to the BAS.

---

## Example: VAV Air System Analysis

Below is a working example using the OpenAI Python package. The same pattern applies to Claude (via the `anthropic` SDK) and Gemini (via `google-genai`) — swap the client, keep the data pipeline.

**What it does:**

1. Connects to BDX and pulls 7-day and 14-day airflow data for VAVs under selected AHUs
2. Flags VAVs whose week-over-week airflow change exceeds ±20 %
3. Sends *only the anomalies* to the LLM for a written summary
4. Renders a PyVis network chart alongside the LLM's recommendations in a single HTML report

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

    load_dotenv()

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    LLM_MODEL = os.getenv("LLM_MODEL")  # pin the exact model in your env, not in code

    BDX_URL = os.getenv("BDX_URL")
    USERNAME = os.getenv("BDX_USERNAME")
    PASSWORD = os.getenv("BDX_PASSWORD")
    BUILDING_NAME = "Apex Building"
    AHU_NUMBERS = [1, 2, 3, 4, 6, 8]

    auth = UsernameAndPasswordAuthenticator(USERNAME, PASSWORD)
    with BDX(BDX_URL, auth) as bdx:
        buildings = bdx.buildings.list()
        matching_buildings = [b for b in buildings if b.name.lower() == BUILDING_NAME.lower()]
        if not matching_buildings:
            print(f"No building found with the name: {BUILDING_NAME}")
            exit()

        BUILDING_ID = matching_buildings[0].componentInstanceId
        all_components = bdx.components.by_building(building_id=BUILDING_ID)

        ahu_names = {f"AHU_{num}": f"AHU {num}" for num in AHU_NUMBERS}

        vav_components = [
            comp for comp in all_components
            if "VAV_" in comp.path.displayName and any(comp.path.displayName.startswith(f"VAV_{ahu}_") for ahu in AHU_NUMBERS)
        ]

        vav_to_ahu = {}
        for vav in vav_components:
            ahu_number = vav.path.displayName.split("_")[1]
            if f"AHU_{ahu_number}" in ahu_names:
                vav_to_ahu[vav.path.displayName] = f"AHU_{ahu_number}"

        timeframe_current = TimeFrame.last_7_days()
        timeframe_previous = TimeFrame.last_n_days(14)

        properties = [{"componentPathId": vav.path.componentPathId, "propertyName": "airFlow"} for vav in vav_components]

        trend_data_current = bdx.trending.retrieve_data(properties, timeframe_current, AggregationLevel.HOURLY)
        trend_data_previous = bdx.trending.retrieve_data(properties, timeframe_previous, AggregationLevel.HOURLY)

        df_current = trend_data_current.dataframe.fillna(0).set_index("time")
        df_previous = trend_data_previous.dataframe.fillna(0).set_index("time")
        df_previous = df_previous.iloc[:len(df_current)]

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
    # Generate Summary with an LLM
    # Swap providers by replacing the client — prompt and data pipeline stay identical.
    # -------------------
    def generate_summary(anomalies):
        if not anomalies:
            return "<p>No significant anomalies detected in VAV airflow this week.</p>"

        prompt_text = f"""
        Given the following data on airflow changes for VAVs in a building:
        {json.dumps(anomalies, indent=2)}

        ### **Summary Instructions**
        - **Only report the most significant anomalies** (up to **5 individual VAVs**) OR if there is a **system-wide AHU issue**.
        - **Exclude moderate changes** – focus on extreme cases that could indicate performance, comfort, or system inefficiencies.
        - **If there are no significant changes**, state: "No major anomalies detected this week."
        - **Airflow data is accumulated CFM, so units are CF.**
        - **Format the response as concise bullet points** using **Markdown**.

        ### **Response Format**
        - **Key Findings**
            - **VAV_3_3:** Airflow increased **+89.09%**
              🔹 Likely cause: [Occupancy shift / Calibration issue / Setpoint change]
              🔹 Recommended action: [Verify control settings / Check mechanical operation]

        - **If AHU-wide issues exist, summarize them separately.**

        Keep the response **short, direct, and action-oriented.**
        """

        client = openai.OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model=LLM_MODEL,  # set via env, e.g. your organization's approved model
            messages=[
                {"role": "system", "content": "You are an expert in HVAC systems analyzing airflow changes."},
                {"role": "user", "content": prompt_text}
            ]
        )

        markdown_summary = response.choices[0].message.content
        return markdown.markdown(markdown_summary)

    summary_text = generate_summary(anomalies)

    # -------------------
    # Generate PyVis Network Chart
    # -------------------
    html_path = "VAV_network_summary.html"
    net = Network(height="100vh", width="100%", notebook=True, directed=False)
    net.barnes_hut(gravity=-7000, central_gravity=0.2, spring_length=50, spring_strength=0.03)

    net.add_node("Building", size=100, color="#3e3e3e", label=f"Building: {BUILDING_NAME}", font={"size": 50})

    for ahu, ahu_label in ahu_names.items():
        net.add_node(ahu, size=50, color="#f5d76e", label=ahu_label, font={"size": 40})
        net.add_edge("Building", ahu)

    overall_max_airflow = max(all_current_airflows.values(), default=1)
    colormap = plt.get_cmap("RdBu_r")
    vmin = min(all_percent_diffs.values(), default=-1)
    vmax = max(all_percent_diffs.values(), default=1)
    norm = mcolors.TwoSlopeNorm(vmin=vmin, vcenter=0, vmax=vmax)

    for vav_name, ahu_name in vav_to_ahu.items():
        percent_diff = all_percent_diffs.get(vav_name, 0)
        current_airflow = all_current_airflows.get(vav_name, 0)
        rgba_color = colormap(norm(percent_diff))
        hex_color = mcolors.to_hex(rgba_color)
        node_size = 5 + (50 * (current_airflow / overall_max_airflow))

        net.add_node(
            vav_name,
            size=node_size,
            color=hex_color,
            title=f"{vav_name} - % Change: {percent_diff:.2f}%, Airflow: {current_airflow:.2f}",
            font={"size": 30}
        )
        net.add_edge(ahu_name, vav_name, width=1)

    net.save_graph(html_path)

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(f"""
        <html>
        <head>
            <style>
                body {{ font-size: 12px; }}
                .container {{ display: flex; height: 100vh; width: 100%; }}
                .left {{ width: 50%; height: 100%; overflow-y: hidden; }}
                .right {{ width: 50%; background: #f4f4f4; padding: 20px; overflow-y: auto;
                          font-size: 10px !important; line-height: 1.5; box-sizing: border-box; }}
                .right h1 {{ font-size: 16px !important; }}
                .right h2 {{ font-size: 14px !important; }}
                .right h3 {{ font-size: 12px !important; }}
                .right * {{ font-size: 10px !important; }}
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

---

## Swapping Providers

The same prompt, same BDXpy data pipeline, different back-end:

| Provider | Python SDK | Env Var |
|---|---|---|
| OpenAI | `openai` | `OPENAI_API_KEY` |
| Claude (Anthropic) | `anthropic` | `ANTHROPIC_API_KEY` |
| Gemini (Google) | `google-genai` | `GOOGLE_API_KEY` |

**Pin the specific model version in your environment config, not in source.** Models evolve fast — keeping the name out of code means you can upgrade without a PR.

---

## Final Recommendations

- Let BDXpy do the **data work**; let the LLM do the **reasoning**.
- Pre-process before prompting — small, targeted payloads beat firehoses every time.
- Treat prompts as **source code**: version them, test them, iterate on them.
- Stay provider-agnostic where you can; it keeps options open and costs competitive.
- Ask about **`bdxpy-skills`** if you're building agent workflows and want the tool definitions done for you.

> Questions, use-case ideas, or want early access to `bdxpy-skills`? Reach out to the BuildingLogiX team.
