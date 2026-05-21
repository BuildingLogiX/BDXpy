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
