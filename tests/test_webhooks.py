import os
from unittest import TestCase
from activecampaign.client import Client
import json

class WebhooksTest(TestCase):
    def setUp(self):
        self.client = Client(os.environ.get('host'), os.environ.get('api_key'))

    def _get_data_webhook(self):
        return {'name': 'my_webhook',
            'url':'https://ad6045b6.ngrok.io',
            'action':'subscribe',
            'init':'admin'
        }

    def test_create_webhook(self):
        data =self._get_data_webhook()
        result_create = self.client.webhooks.create_webhook(data)
        try:
            self.client.webhooks.view_webhooks(result_create['id'])
            _view = True
        except:
            _view = False
        self.assertTrue(_view)
        self.client.webhooks.delete_webhook(result_create['id'])

    def test_delete_webhook(self):
        data =self._get_data_webhook()
        result_create = self.client.webhooks.create_webhook(data)
        self.client.webhooks.delete_webhook(result_create['id'])
        try:
            self.client.webhooks.view_webhooks(result_create['id'])
            _view = False
        except:
            _view = True
        self.assertTrue(_view)

