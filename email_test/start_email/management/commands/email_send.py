from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from email.mime.image import MIMEImage
import smtplib


def send_email():
    import os
    recv_mail = os.environ.get("RECIPANTS")

    with open('/app/test.pdf', 'rb') as f:
        pdf_data = f.read()

    email = EmailMultiAlternatives(
        "Test_title",
        "Test_body",
        'ALGwangmyeong.Spot@kia.com',
        [recv_mail],
    )

    # 이미지 첨부
    
    from email.mime.application import MIMEApplication
    pdf = MIMEApplication(pdf_data, _subtype='pdf')
    pdf.add_header('Content-Disposition', 'attachment', filename='test1.pdf')
    email.attach(pdf)
    email.send(fail_silently=False)
    print(f'email has been sent to {email.recipients()}')


class Command(BaseCommand):

    def handle(self, *args, **options):
        """
        Django Command for add Fixtures.
        """

        self.stdout.write('add db fixtures1..')
        send_email()
        self.stdout.write('add db fixtures..')


if __name__ == "__main__":
    print(send_email())
