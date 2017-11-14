import os
from unittest import TestCase
from activecampaign.client import Client

class AcountTest(TestCase):
    def setUp(self):
        self.host = os.environ.get('host')
        self.api_key = os.environ.get('api_key')
        self.client = Client(self.host, self.api_key)

    def test_schema(self):
        self.assertEqual(self.client._apikey, self.api_key)
        self.assertEqual(self.client._base_url, self.host)


