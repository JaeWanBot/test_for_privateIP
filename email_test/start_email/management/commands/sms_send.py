from django.core.management import call_command
from django.core.management.base import BaseCommand


class GabiaSMS():
    def __init__(self, callback, refkey):
        self.callback = callback
        self.refkey = refkey

    def get_access_Token(self):
        import requests
        url = 'https://sms.gabia.com/oauth/token'
        payload = 'grant_type=client_credentials'
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic Y2xvYm90c3BvdDEyMzoxZTczZjVkODU3OTg5ZTlmN2VjZmMzODU3NjlmY2U0NA=='
        }
        response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False)
        response = response.json()

        print(response)
        return response['access_token']

    def send(self, phone, message):
        import requests
        import base64

        url = 'https://sms.gabia.com/api/send/sms'
        payload = \
        f'phone={phone}&callback={self.callback}&message={message}&refkey=[[{self.refkey}]]'

        access = f'clobotspot123:{self.get_access_Token()}'
        auth=base64.b64encode(access.encode('utf-8'))
        access_token=auth.decode('utf-8')

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': f'Basic {access_token}'
        }
        response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False)
        return response.json()

class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        Django Command for add Fixtures.
        """

        #IP need
        gabia_sms = GabiaSMS(callback='01087902898',refkey='clobotspot')

        import os
        phone = os.environ.get("PHONE")
        
        sms_response = gabia_sms.send(phone, "test")


        print('sms_response', sms_response)