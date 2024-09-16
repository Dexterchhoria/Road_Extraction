import os

SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.your-email-provider.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', 587))  # Adjust based on your needs
EMAIL_USER = os.getenv('EMAIL_USER', 'your-email@provider.com')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD', 'your-password')
