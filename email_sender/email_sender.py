import logging
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('email_sender')

class EmailSender:
    """A helper class for sending emails with HTML support, attachments, CC, BCC, and logging."""

    @staticmethod
    def send_email(subject, template_name, context, to_email, cc=None, bcc=None, attachments=None):
        """Sends an email with HTML template support and optional attachments."""
        # Render the email template
        html_content = render_to_string(template_name, context)
        text_content = strip_tags(html_content)

        # Create the email
        email = EmailMultiAlternatives(
            subject,
            text_content,
            settings.DEFAULT_FROM_EMAIL,
            [to_email],
            cc=cc,
            bcc=bcc,
        )
        email.attach_alternative(html_content, "text/html")

        # Attach files if provided
        if attachments:
            for attachment in attachments:
                if os.path.isfile(attachment):
                    email.attach_file(attachment)
                else:
                    logger.warning(f"Attachment {attachment} does not exist.")

        # Send the email and log the result
        try:
            email.send()
            logger.info(f"Email sent to {to_email} with subject: '{subject}'")
            if cc:
                logger.info(f"CC: {cc}")
            if bcc:
                logger.info(f"BCC: {bcc}")
            return True
        except Exception as e:
            logger.error(f"Failed to send email to {to_email}: {e}")
            return False
