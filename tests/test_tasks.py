import os
from unittest import TestCase
from activecampaign.client import Client
import json

class TasksTest(TestCase):
    def setUp(self):
        self.client = Client(os.environ.get('host'), os.environ.get('api_key'))

    def _get_data_deal(self):
        return {'title': 'my_deal555',
                'value': 'my_value',
                'currency': 'usd',
                'pipeline': os.environ.get('pipeline'),
                'stage':'1',
                'contactid':'2',
                'owner':'1'}


    def test_get_tasks(self):
        result = self.client.tasks.get_tasks(1)
        self.assertIn('tasks', result)
