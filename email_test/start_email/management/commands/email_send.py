from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from django.core.mail import send_mail, EmailMessage


def send_email():
    import os
    recv_mail = os.environ.get("RECIPANTS")
    email = EmailMessage(
    "Test_title",
    "Test_body",
    "Test_from",
    [recv_mail],
    )
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
