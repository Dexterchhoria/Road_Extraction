import smtplib
from email.mime.text import MIMEText
from app.config.email_config import SMTP_SERVER, SMTP_PORT, EMAIL_USER, EMAIL_PASSWORD

def send_alert(email_address: str, message: str):
    """
    Sends an email alert.
    
    Args:
        email_address (str): Recipient's email address.
        message (str): Message content to send.
    """
    msg = MIMEText(message)
    msg['Subject'] = 'Road Network Change Alert'
    msg['From'] = EMAIL_USER
    msg['To'] = email_address

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_USER, email_address, msg.as_string())
            print(f"Alert sent to {email_address}")
    except smtplib.SMTPException as e:
        raise Exception(f"Failed to send email: {e}")
