import os
from unittest import TestCase
from activecampaign.client import Client
import json

class WebhooksTest(TestCase):
    def setUp(self):
        self.client = Client(os.environ.get('host'), os.environ.get('api_key'))

    def _get_data_webhok(self):
        return {'name': 'my_webhook',
            'url':'https://ad6045b6.ngrok.io',
            'action':'subscribe',
            'init':'admin'
        }

    def test_create_webhook(self):
        data =_get_data_webhook()