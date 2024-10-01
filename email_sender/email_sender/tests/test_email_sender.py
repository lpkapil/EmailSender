import unittest
from unittest.mock import patch, MagicMock
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from email_sender import EmailSender  # Adjust the import based on your project structure


class EmailSenderTests(unittest.TestCase):

    @patch('your_app.email_sender.EmailMultiAlternatives')
    @patch('your_app.email_sender.render_to_string')
    @patch('your_app.email_sender.strip_tags')
    @patch('your_app.email_sender.logging')
    def test_send_email_success(self, mock_logging, mock_strip_tags, mock_render_to_string, mock_email):
        # Arrange
        mock_render_to_string.return_value = '<html>Content</html>'
        mock_strip_tags.return_value = 'Content'
        
        # Create a mock email instance
        mock_email_instance = MagicMock()
        mock_email.return_value = mock_email_instance

        # Act
        result = EmailSender.send_email(
            subject='Test Subject',
            template_name='email_template.html',
            context={'key': 'value'},
            to_email='recipient@example.com',
        )

        # Assert
        self.assertTrue(result)
        mock_email_instance.send.assert_called_once()
        mock_logging.info.assert_any_call("Email sent to recipient@example.com with subject: 'Test Subject'")

    @patch('your_app.email_sender.EmailMultiAlternatives')
    @patch('your_app.email_sender.render_to_string')
    @patch('your_app.email_sender.strip_tags')
    @patch('your_app.email_sender.logging')
    def test_send_email_failure(self, mock_logging, mock_strip_tags, mock_render_to_string, mock_email):
        # Arrange
        mock_render_to_string.return_value = '<html>Content</html>'
        mock_strip_tags.return_value = 'Content'
        
        # Create a mock email instance
        mock_email_instance = MagicMock()
        mock_email.return_value = mock_email_instance
        mock_email_instance.send.side_effect = Exception("Send failed")

        # Act
        result = EmailSender.send_email(
            subject='Test Subject',
            template_name='email_template.html',
            context={'key': 'value'},
            to_email='recipient@example.com',
        )

        # Assert
        self.assertFalse(result)
        mock_logging.error.assert_called_once_with("Failed to send email to recipient@example.com: Send failed")

    @patch('your_app.email_sender.EmailMultiAlternatives')
    @patch('your_app.email_sender.render_to_string')
    @patch('your_app.email_sender.strip_tags')
    @patch('your_app.email_sender.logging')
    def test_send_email_with_attachment(self, mock_logging, mock_strip_tags, mock_render_to_string, mock_email):
        # Arrange
        mock_render_to_string.return_value = '<html>Content</html>'
        mock_strip_tags.return_value = 'Content'
        
        # Create a mock email instance
        mock_email_instance = MagicMock()
        mock_email.return_value = mock_email_instance

        # Act
        result = EmailSender.send_email(
            subject='Test Subject',
            template_name='email_template.html',
            context={'key': 'value'},
            to_email='recipient@example.com',
            attachments=['/path/to/existing/file.txt']
        )

        # Assert
        self.assertTrue(result)
        mock_email_instance.attach_file.assert_called_once_with('/path/to/existing/file.txt')

    @patch('your_app.email_sender.EmailMultiAlternatives')
    @patch('your_app.email_sender.render_to_string')
    @patch('your_app.email_sender.strip_tags')
    @patch('your_app.email_sender.logging')
    def test_send_email_with_non_existent_attachment(self, mock_logging, mock_strip_tags, mock_render_to_string, mock_email):
        # Arrange
        mock_render_to_string.return_value = '<html>Content</html>'
        mock_strip_tags.return_value = 'Content'
        
        # Create a mock email instance
        mock_email_instance = MagicMock()
        mock_email.return_value = mock_email_instance

        # Act
        result = EmailSender.send_email(
            subject='Test Subject',
            template_name='email_template.html',
            context={'key': 'value'},
            to_email='recipient@example.com',
            attachments=['/path/to/nonexistent/file.txt']
        )

        # Assert
        self.assertTrue(result)
        mock_logging.warning.assert_called_once_with("Attachment /path/to/nonexistent/file.txt does not exist.")

# To run the tests, execute the following command:
# python manage.py test your_app.tests.test_email_sender
