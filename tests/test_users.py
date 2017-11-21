import os
from unittest import TestCase
from activecampaign.client import Client
import json

class UsersTest(TestCase):
    def setUp(self):
        self.client = Client(os.environ.get('host'), os.environ.get('api_key'))

    def test_view_user(self):
        result = self.client.users.view_user(1)
        self.assertEqual(result['id'],'1')
