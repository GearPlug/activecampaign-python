import os
from unittest import TestCase
from activecampaign.client import Client
import json

class ListsTest(TestCase):
    def setUp(self):
        self.client = Client(os.environ.get('host'), os.environ.get('api_key'))

    def _get_data_list(self):
        return {'name': 'new_list',
                'sender_name': 'my company',
                'sender_addr1': 'calle123',
                'sender_zip': '0000',
                'sender_city': 'Bogota',
                'sender_country': 'Colombia',
                'sender_url': 'www.grplug.com',
                'sender_reminder': 'This is a unittest',
                }

    def test_get_lists(self):
        result_create = self.client.lists.create_list(data=self._get_data_list())
        lists = self.client.lists.get_lists()
        _find = None
        for k,v in lists.items():
            if type(v) is dict:
                if result_create['id'] == v['id']:
                    _find = result_create['id']
        self.assertEqual(result_create['id'], _find)
        self.client.lists.delete_list(result_create['id'])

    def test_create_list(self):
        result_create = self.client.lists.create_list(data=self._get_data_list())
        lists = self.client.lists.get_lists()
        _find = False
        for k, v in lists.items():
            if type(v) is dict:
                if result_create['id'] == v['id']:
                    _find = True
        self.assertTrue(_find)
        self.client.lists.delete_list(result_create['id'])

    def test_create_list(self):
        result_create = self.client.lists.create_list(data=self._get_data_list())
        self.client.lists.delete_list(result_create['id'])
        lists = self.client.lists.get_lists()
        _find = True
        for k, v in lists.items():
            if type(v) is dict:
                if result_create['id'] == v['id']:
                    _find = False
        self.assertTrue(_find)


