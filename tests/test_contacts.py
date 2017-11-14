import os
from unittest import TestCase
from activecampaign.client import Client
import json

class ContactsTest(TestCase):
    def setUp(self):
        self.client = Client(os.environ.get('host'), os.environ.get('api_key'))

    def test_get_acoount_info(self):
        result = self.client.account.get_account_info()
        self.assertIsInstance(result, dict)
        self.assertEqual(result['email'], os.environ.get('email'))