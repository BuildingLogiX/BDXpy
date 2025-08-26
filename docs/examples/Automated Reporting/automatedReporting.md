# Automated Reporting Examples

This guide walks you through setting up BDXpy as a FastAPI data service on a Grafana server and configuring it as a JSON API data source.


## Example PDF generation of monthly energy report

<img src="../energysummarypdf.png" style="width: 100%; height: auto;">

Below is example code where you can insert BDXpy code to generate a PDF from a combination of images and tables. In the second example these principles can be applied to create a PDF that gets emailed.

??? note "Show Code"
    ```python  
        import numpy as np
        import pandas as pd
        import plotly.express as px
        import plotly.graph_objects as go
        import imgkit
        import time
        import plotly.io as pio
        import matplotlib.pyplot as plt
        import pandas as pd
        from pandas.plotting import table
        from selenium import webdriver
        from PIL import Image
        import matplotlib.pyplot as plt
        import pandas as pd
        from reportlab.lib.pagesizes import letter
        from reportlab.lib import colors
        from reportlab.lib.styles import getSampleStyleSheet
        from reportlab.lib.units import inch
        from reportlab.lib.utils import ImageReader
        from reportlab.pdfgen import canvas
        from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
        from datetime import datetime
        import os
        from reportlab.lib.pagesizes import letter
        from reportlab.platypus import SimpleDocTemplate, Image, Paragraph
        from reportlab.lib.styles import getSampleStyleSheet
        from reportlab.lib.units import inch
        from PIL import Image as PILImage

        print("Current Working Directory:", os.getcwd())

        # Function to save the DataFrame to a PNG
        def save_dataframe_to_png(df, file_name):
            # Set up the plot
            fig, ax = plt.subplots(figsize=(12, 6))  # Adjust size as necessary
            ax.axis('off')  # No axes
            ax.axis('tight')

            # Create the table from the DataFrame
            table_data = table(ax, df, loc='center', cellLoc='center', colWidths=[0.1] * len(df.columns))

            # Save the figure as a PNG
            plt.savefig(file_name, bbox_inches='tight', dpi=300)


        # Assuming 'fig' is your Plotly figure object
        def save_plotly_as_png(fig, output_filename):
            # Save the figure as a PNG file
            pio.write_image(fig, output_filename)

        def save_html_to_file(fig, file_name):
            # Save the Plotly figure as an HTML file
            fig.write_html(file_name)

        config = imgkit.config(wkhtmltoimage=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltoimage.exe')

        def html_to_png(html_file, output_image):
            time.sleep(2)  # Adjust the delay as necessary
            imgkit.from_file(html_file, output_image, config=config)

        #### BDXpy function would go here along with component selections #####

        df=data

        df['Timestamp'] = pd.to_datetime(df['Timestamp'])

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
        # Save the figure as a PNG file
        fig.write_image("mapenergychart.png", format="png", scale=2)

        df_expanded = df

        # Ensure 'Timestamp' column is in datetime format if not already
        df_expanded['Timestamp'] = pd.to_datetime(df_expanded['Timestamp'])

        # Extract the year from the 'Timestamp' column
        df_expanded['Year'] = df_expanded['Timestamp'].dt.year

        # Group by year and building type, calculating the sum of total cost
        cost_summary = df_expanded.groupby(['Building Type', 'Year'])['Total Cost'].sum().unstack().fillna(0)

        # Round cost values to the nearest whole number
        cost_summary = cost_summary.round(0)

        # Calculate percent change for the latest year compared to the previous year
        cost_summary['Percent Change'] = cost_summary.pct_change(axis=1).iloc[:, -1] * 100

        # Calculate actual cost change (difference between current year and previous year)
        last_year = cost_summary.columns[-2]  # Second to last year (previous year)
        current_year = cost_summary.columns[-3]  # Last year column (current year)

        cost_summary['Actual Cost Change'] = cost_summary[last_year] - cost_summary[current_year]

        # Add a totals row at the bottom of the DataFrame
        totals_row = cost_summary.sum(numeric_only=True)
        totals_row.name = 'Total'
        cost_summary = pd.concat([cost_summary, totals_row.to_frame().T], axis=0)

        # Styling the DataFrame for a report
        def color_percent(series):
            """Color green for negative (decrease), red for positive (increase)."""
            return ['color: green' if val < 0 else 'color: red' if val > 0 else 'color: black' for val in series]

        # Apply formatting to all year columns dynamically
        year_columns = [col for col in cost_summary.columns if isinstance(col, int)]  # Select only year columns

        # Apply formatting and coloring
        styled_summary = cost_summary.style.format({
            **{year: '${:,.0f}' for year in year_columns},  # Apply currency format to all year columns
            'Percent Change': '{:.2f}%',                    # Format percent change
            'Actual Cost Change': '${:,.0f}'                 # Format actual cost change as currency
        }).apply(color_percent, subset=['Percent Change', 'Actual Cost Change'])

        # Display or save to HTML for review
        styled_summary.to_html('cost_summary_report.html')

        # Show the styled DataFrame
        styled_summary

        # Use the function to save your cost_summary DataFrame
        # save_dataframe_to_png(cost_summary, 'cost_summary.png')

        # Replicating the logic for BTU for Total Energy instead of cost, rounding to the nearest whole number

        df_expanded = df_expanded.copy()  # Assuming df_expanded is your main DataFrame

        # Ensure 'Timestamp' column is in datetime format if not already
        df_expanded['Timestamp'] = pd.to_datetime(df_expanded['Timestamp'])

        # Extract the year from the 'Timestamp' column
        df_expanded['Year'] = df_expanded['Timestamp'].dt.year

        # Group by year and building type, calculating the sum of total energy (BTU)
        energy_summary = df_expanded.groupby(['Building Type', 'Year'])['Total Energy'].sum().unstack().fillna(0)

        # Round energy values to the nearest whole number
        energy_summary = energy_summary.round(0)

        # Calculate percent change for the latest year compared to the previous year
        energy_summary['Percent Change'] = energy_summary.pct_change(axis=1).iloc[:, -1] * 100

        # Calculate actual energy change (difference between current year and previous year)
        last_year = energy_summary.columns[-2]  # Second to last year (previous year)
        current_year = energy_summary.columns[-3]  # Last year column (current year)

        energy_summary['Actual Energy Change'] = energy_summary[last_year] - energy_summary[current_year]

        # Add a totals row at the bottom of the DataFrame
        totals_row = energy_summary.sum(numeric_only=True)
        totals_row.name = 'Total'
        energy_summary = pd.concat([energy_summary, totals_row.to_frame().T], axis=0)

        # Styling the DataFrame for a report
        def color_percent(series):
            """Color green for negative (decrease), red for positive (increase)."""
            return ['color: green' if val < 0 else 'color: red' if val > 0 else 'color: black' for val in series]

        # Apply formatting to all year columns dynamically
        year_columns = [col for col in energy_summary.columns if isinstance(col, int)]  # Select only year columns

        # Apply formatting and coloring
        styled_energy_summary = energy_summary.style.format({
            **{year: '{:,.0f}' for year in year_columns},  # Apply whole number format to all year columns
            'Percent Change': '{:.2f}%',                    # Format percent change
            'Actual Energy Change': '{:,.0f}'                 # Format actual energy change
        }).apply(color_percent, subset=['Percent Change', 'Actual Energy Change'])

        # Display or save to HTML for review
        styled_energy_summary.to_html('energy_summary_report.html')

        # Show the styled DataFrame
        styled_energy_summary

        # Use the function to save your cost_summary DataFrame
        # save_dataframe_to_png(energy_summary, 'energy_summary.png')



        # Assuming there is a 'Metric Tons CO2' column or we generate one based on energy (Total Energy * emission factor)
        # You can change the factor to match your data.
        emission_factor = 0.0001  # Example: 0.0001 Metric Tons of CO2 per BTU of energy

        # Create Metric Tons CO2 column if it doesn't exist
        if 'Metric Tons CO2' not in df_expanded.columns:
            df_expanded['Metric Tons CO2'] = df_expanded['Total Energy'] * emission_factor

        # Extract the year from the 'Timestamp' column
        df_expanded['Year'] = df_expanded['Timestamp'].dt.year

        # Group by year and building type, calculating the sum of Metric Tons CO2
        co2_summary = df_expanded.groupby(['Building Type', 'Year'])['Metric Tons CO2'].sum().unstack().fillna(0)

        # Round CO2 values to the nearest whole number
        co2_summary = co2_summary.round(0)

        # Calculate percent change for the latest year compared to the previous year
        co2_summary['Percent Change'] = co2_summary.pct_change(axis=1).iloc[:, -1] * 100

        # Calculate actual CO2 change (difference between current year and previous year)
        last_year = co2_summary.columns[-2]  # Second to last year
        current_year = co2_summary.columns[-3]  # Last year column

        co2_summary['Actual CO2 Change'] = co2_summary[last_year] - co2_summary[current_year]

        # Add a totals row at the bottom of the DataFrame
        totals_row = co2_summary.sum(numeric_only=True)
        totals_row.name = 'Total'
        co2_summary = pd.concat([co2_summary, totals_row.to_frame().T], axis=0)

        # Styling the DataFrame for a report
        def color_percent(series):
            """Color green for negative (decrease), red for positive (increase)."""
            return ['color: green' if val < 0 else 'color: red' if val > 0 else 'color: black' for val in series]

        # Apply formatting to all year columns dynamically
        year_columns = [col for col in co2_summary.columns if isinstance(col, int)]  # Select only year columns

        # Apply formatting and coloring
        styled_co2_summary = co2_summary.style.format({
            **{year: '{:,.0f}' for year in year_columns},  # Apply whole number format to all year columns
            'Percent Change': '{:.2f}%',                   # Format percent change
            'Actual CO2 Change': '{:,.0f}'                 # Format actual CO2 change
        }).apply(color_percent, subset=['Percent Change', 'Actual CO2 Change'])

        # Display or save to HTML for review
        styled_co2_summary.to_html('co2_summary_report.html')

        # Show the styled DataFrame
        styled_co2_summary

        # Use the function to save your cost_summary DataFrame
        # save_dataframe_to_png(co2_summary, 'co2_summary.png')


        # Group the data by year and month, summing the total energy for each month of each year
        df_expanded['Month'] = df_expanded['Timestamp'].dt.month
        monthly_energy_by_year = df_expanded.groupby(['Year', 'Month'])['Total Energy'].sum().unstack(level=0).fillna(0)

        # Convert the DataFrame to long format for Plotly
        monthly_energy_long = monthly_energy_by_year.reset_index().melt(id_vars='Month', var_name='Year', value_name='Total Energy')

        # Create a Plotly chart
        fig = px.bar(monthly_energy_long, x='Month', y='Total Energy', color='Year', barmode='group', 
                    labels={'Total Energy': 'Total Energy (BTU)', 'Month': 'Month'},
                    title='Monthly Total Energy Consumption by Year')

        # Show the chart
        fig.show()


        # Example usage
        fig.write_html("yearoveryearchart.html")
        fig.write_image("yearoveryearchart.png", format="png", scale=2)

        # Group the data by building and year to calculate the total energy for each building
        building_energy_2023 = df_expanded[df_expanded['Year'] == 2023].groupby('Building Name')[['Electric Energy', 'Heating Energy']].sum()
        building_energy_2024 = df_expanded[df_expanded['Year'] == 2024].groupby('Building Name')[['Electric Energy', 'Heating Energy']].sum()

        # Compute percent changes between 2023 and 2024
        building_percent_change = pd.DataFrame()
        building_percent_change['Percent Change Electric'] = ((building_energy_2024['Electric Energy'] - building_energy_2023['Electric Energy']) / building_energy_2023['Electric Energy']) * 100
        building_percent_change['Percent Change Heating'] = ((building_energy_2024['Heating Energy'] - building_energy_2023['Heating Energy']) / building_energy_2023['Heating Energy']) * 100
        building_percent_change['Total Energy'] = building_energy_2024.sum(axis=1)  # Total energy in 2024
        building_percent_change['Building Type'] = df_expanded.groupby('Building Name')['Building Type'].first()  # Get building type
        building_percent_change = building_percent_change.reset_index()

        # Create the updated bubble chart
        fig = px.scatter(
            building_percent_change, 
            x='Percent Change Heating', 
            y='Percent Change Electric',
            size='Total Energy',
            color='Building Type',
            text='Building Name',  # Show building names as visible text labels
            title='Energy Consumption Changes by University Buildings (2023 vs 2024)',
            labels={'Percent Change Heating': 'Heating Consumption Change (%)', 'Percent Change Electric': 'Electric Consumption Change (%)'},
            size_max=60,  # Maximum size for the bubbles
            template='plotly_white'  # Apply the Plotly white theme
        )

        # Add vertical and horizontal lines at x=0 and y=0
        fig.add_vline(x=0, line_dash="dash", line_color="black")
        fig.add_hline(y=0, line_dash="dash", line_color="black")

        # Customize text color based on conditions and add traces
        for i, row in building_percent_change.iterrows():
            text_color = None  # Reset the text_color for each row
            if row['Percent Change Heating'] < 0 and row['Percent Change Electric'] < 0:
                text_color = 'green'
            elif row['Percent Change Heating'] > 0 and row['Percent Change Electric'] > 0:
                text_color = 'red'
            else:
                text_color = 'black'  # Default color for other conditions

            # Add a new trace with the correct text color
            new_trace = px.scatter(
                pd.DataFrame([row]), 
                x='Percent Change Heating', 
                y='Percent Change Electric',
                size='Total Energy',
                text='Building Name',
                size_max=60
            ).data[0]

            # Update the text color for this trace and remove markers
            new_trace.textfont = dict(color=text_color, size=14)
            new_trace.marker = dict(size=0, opacity=0)  # Remove the marker but keep the text

            # Add the trace to the figure
            fig.add_trace(new_trace)

        # Update layout without explicitly specifying font family to use Plotly's default (Open Sans)
        fig.update_layout(
            font_size=14,
            xaxis_title="Heating Consumption Change (%)",
            yaxis_title="Electric Consumption Change (%)",
            title_font_size=20,
            height=800 
        )

        # Show the updated figure
        fig.show()

        # Example usage
        fig.write_html("pctchangechart.html")
        fig.write_image("pctchangechart.png", format="png", scale=2)



        # Function to add images with preserved aspect ratio
        def add_image_with_aspect_ratio(image_path, max_width=6*inch, max_height=4*inch):
            img = PILImage.open(image_path)
            width, height = img.size
            aspect_ratio = width / height

            if width > height:
                new_width = min(max_width, width * (max_height / height))
                new_height = new_width / aspect_ratio
            else:
                new_height = min(max_height, height * (max_width / width))
                new_width = new_height * aspect_ratio

            return Image(image_path, width=new_width, height=new_height)

        def create_pdf(output_filename, map_chart, cost_summary_img, energy_summary_img, co2_summary_img, yoy_chart, pct_change_chart):
            pdf = SimpleDocTemplate(output_filename, pagesize=letter)
            elements = []

            # Title and summary text
            styles = getSampleStyleSheet()
            title = Paragraph("Energy Consumption Summary", styles['Title'])
            summary_text = Paragraph(
                "This report provides an overview of the energy consumption for the month.", styles['Normal']
            )
            
            elements.append(title)
            elements.append(summary_text)

            # Add map chart image with aspect ratio preserved
            map_image = add_image_with_aspect_ratio(map_chart)
            elements.append(map_image)

            # Add year-over-year chart with aspect ratio preserved
            yoy_image = add_image_with_aspect_ratio(yoy_chart)
            elements.append(yoy_image)

            # Add percentage change chart with aspect ratio preserved
            pct_change_image = add_image_with_aspect_ratio(pct_change_chart)
            elements.append(pct_change_image)

            # Build PDF
            pdf.build(elements)

        # Call the create_pdf function with PNG paths
        create_pdf("energy_summary.pdf", "mapenergychart.png", "cost_summary.png", "energy_summary.png", "co2_summary.png", "yearoveryearchart.png", "pctchangechart.png")
    ```

## Email PDF Report
A SMTP email service can be used to email this PDF. The python script can then be referenced in a BAT file and scheduled to run from the Windows Task Scheduler on a user specificed interval.

??? note "Show Code"
    ```python
        from bdx.auth import UsernameAndPasswordAuthenticator
        from bdx.core import BDX
        from bdx.types import TimeFrame
        from datetime import datetime, timedelta
        import os
        from dotenv import load_dotenv
        import pandas as pd
        import matplotlib.pyplot as plt
        from io import BytesIO
        from reportlab.lib.colors import HexColor
        from reportlab.lib import colors
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        import smtplib
        from email.message import EmailMessage

        # Load environment variables from .env file
        load_dotenv()

        SMTP_SERVER = os.getenv("SMTP_SERVER")
        SMTP_PORT = int(os.getenv("SMTP_PORT"))
        SMTP_USERNAME = os.getenv("SMTP_USERNAME")
        SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
        RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")
        ALERT_EMAIL = os.getenv("ALERT_EMAIL")

        BDX_USERNAME = os.getenv("BDX_USERNAME")
        BDX_PASSWORD = os.getenv("BDX_PASSWORD")

        def get_previous_month_dates():
            today = datetime.now()
            first_day_of_current_month = today.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            last_day_of_previous_month = first_day_of_current_month - timedelta(seconds=1)
            first_day_of_previous_month = last_day_of_previous_month.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            return first_day_of_previous_month, last_day_of_previous_month

        def create_pdf_report(data_summary, data_trend):
            try:
                pdf_path = "output/automated_report.pdf"
                pdf = SimpleDocTemplate(pdf_path, pagesize=A4)
                elements = []

                styles = getSampleStyleSheet()
                title = Paragraph("Automated Report Example", styles['Title'])
                elements.append(title)

                start_date, end_date = get_previous_month_dates()
                date_text = Paragraph(f"Reporting Period: {start_date.strftime('%B %d, %Y')} to {end_date.strftime('%B %d, %Y')}", styles['BodyText'])
                elements.append(date_text)
                elements.append(Spacer(1, 0.2 * A4[1]))

                # Example chart
                fig, ax = plt.subplots(figsize=(6, 4))
                ax.plot(data_trend['Date'], data_trend['Value'], marker='o')
                plt.title("Example Data Trend")
                plt.xlabel("Date")
                plt.ylabel("Value")
                plt.grid(True)

                chart_image = BytesIO()
                plt.savefig(chart_image, format="png")
                plt.close(fig)
                chart_image.seek(0)
                chart = Image(chart_image, width=5 * A4[0] / 8, height=3 * A4[1] / 8)
                elements.append(chart)

                # Example data table
                table_data = [data_summary.columns.to_list()] + data_summary.values.tolist()
                table = Table(table_data)
                table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black)
                ]))
                elements.append(table)
                pdf.build(elements)

                print(f"PDF report saved to {pdf_path}")
                return pdf_path
            except Exception as e:
                print(f"Error generating PDF: {e}")
                send_alert_email(f"Failed to generate PDF report: {e}")
                return None

        def send_email_with_pdf(pdf_path):
            subject = "Automated Report Example"
            body = "Please find the attached example automated report."
            
            msg = EmailMessage()
            msg["From"] = SMTP_USERNAME
            msg["To"] = RECEIVER_EMAIL
            msg["Subject"] = subject
            msg.set_content(body)
            
            with open(pdf_path, "rb") as f:
                msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename=os.path.basename(pdf_path))
            
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
                smtp.starttls()
                smtp.login(SMTP_USERNAME, SMTP_PASSWORD)
                smtp.send_message(msg)
            print(f"Email with PDF {pdf_path} sent.")

        def send_alert_email(error_message):
            subject = "PDF Generation Alert"
            msg = EmailMessage()
            msg["From"] = SMTP_USERNAME 
            msg["To"] = ALERT_EMAIL 
            msg["Subject"] = subject
            msg.set_content(f"An error occurred: {error_message}")
            
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
                smtp.starttls()
                smtp.login(SMTP_USERNAME, SMTP_PASSWORD)
                smtp.send_message(msg)
            print("Alert email sent due to PDF generation failure.")

        def main():
            with BDX("https://yourBDXURL.com", UsernameAndPasswordAuthenticator(BDX_USERNAME, BDX_PASSWORD)) as b:
                start_date, end_date = get_previous_month_dates()
                print(f"Start Date: {start_date}, End Date: {end_date}")
                
                # Example dummy data retrieval
                dummy_data = b.trending.retrieveData([
                    {"propertyName": "value", "componentPathId": 1234567890},
                    {"propertyName": "value", "componentPathId": 1234567891}
                ], timeframe=TimeFrame(start=start_date, end=end_date))
                
                df_dummy = pd.DataFrame({
                    "Date": pd.date_range(start=start_date, periods=10, freq='D'),
                    "Value": [x for x in range(10)]
                })

                df_summary = pd.DataFrame({
                    "Metric": ["Total Energy", "Peak Demand", "Average Usage"],
                    "Value": [10000, 500, 350]
                })

                pdf_path = create_pdf_report(df_summary, df_dummy)
                if pdf_path:
                    send_email_with_pdf(pdf_path)
                else:
                    print("PDF generation failed. Email not sent.")

        main()
    ```