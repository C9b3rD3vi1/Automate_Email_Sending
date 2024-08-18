
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time



def send_email_report():
    # Email configuration
    smtp_server = 'smtp.example.com'  # Replace with your SMTP server
    smtp_port = 587  # For TLS; use 465 for SSL
    smtp_user = 'your_email@example.com'
    smtp_password = 'your_password'
    
    sender_email = 'your_email@example.com'
    receiver_email = 'receiver_email@example.com'
    
    # Create the email content
    subject = 'Daily Report'
    body = 'This is your daily report.'
    
    # Create MIME object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        # Connect to the server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade the connection to secure
        server.login(smtp_user, smtp_password)
        
        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print('Email sent successfully!')
        
    except Exception as e:
        print(f'Error: {e}')
    
    finally:
        server.quit()

# Schedule the email to be sent daily
schedule.every().day.at("08:00").do(send_email_report)

print("Scheduler started. Waiting to send daily reports...")

while True:
    schedule.run_pending()
    time.sleep(60)  # Wait a minute before checking the schedule again
