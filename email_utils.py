import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def email(summaries):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = os.getenv("FROM_EMAIL")
    sender_password = os.getenv("APP_PASSWORD") 

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = os.getenv("TO_EMAIL")
    msg['Subject'] = "Reddit Daily Digest"

    header = "<html><head><title>My Email</title></head><body>"
    body = ""
    footer = "</body></html>"
    for summary in summaries:
        name, content = summary[0], summary[1]
        body += f"<h1>{name}</h1><h3>{content}</h3>"
    msg.attach(MIMEText(header + body + footer, 'html'))
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls() 
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")
