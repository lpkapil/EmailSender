# Django Email Sender

A simple email sending package for Django.

## Configurations

Make sure to configure your email settings in your settings.py.

```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.example.com'  # Your SMTP host
EMAIL_PORT = 587  # SMTP port
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@example.com'
EMAIL_HOST_PASSWORD = 'your_email_password'
```

## Installation

```bash
pip install git+https://github.com/yourusername/django_email_sender.git

```

## Example Uses

```
from email_sender import EmailSender

# Prepare email details
subject = "Welcome to Our Service"
template_name = "welcome_email.html"  # Your HTML template for the email
context = {"username": "John"}  # Context for rendering the template
to_email = "john.doe@example.com"

# Send the email
success = EmailSender.send_email(
    subject=subject,
    template_name=template_name,
    context=context,
    to_email=to_email
)

if success:
    print("Email sent successfully!")
else:
    print("Failed to send email.")
```
