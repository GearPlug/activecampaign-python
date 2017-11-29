import os
from unittest import TestCase
from activecampaign.client import Client
import json

class DealsTest(TestCase):
    def setUp(self):
        self.client = Client(os.environ.get('host'), os.environ.get('api_key'))

    def _get_data_deal(self):
        return {'title': 'my_deal555',
                'value': 'my_value',
                'currency': 'usd',
                'pipeline': os.environ.get('pipeline'),
                'stage':'1',
                'contactid':os.environ.get('contact_id'),
                'owner':'1'}

    def test_create_deal(self):
        data_deal = self._get_data_deal()
        result_create = self.client.deals.create_deal(data_deal)
        try:
            self.client.deals.get_deal(result_create['id'])
            _view = True
        except:
            _view = False
        self.assertTrue(_view)
        self.client.deals.delete_deal(result_create['id'])

    def test_delete_deal(self):
        data_deal = self._get_data_deal()
        result_create = self.client.deals.create_deal(data_deal)
        self.client.deals.delete_deal(result_create['id'])
        try:
            self.client.deals.get_deal(result_create['id'])
            _view = False
        except:
            _view = True
        self.assertTrue(_view)

    def test_get_deals(self):
        data_deal = self._get_data_deal()
        result_create = self.client.deals.create_deal(data_deal)
        deals = self.client.deals.get_deals()['deals']
        _find = None
        for deal in deals:
            if deal['id'] == result_create['id']:
                _find = deal['id']
        self.assertEqual(result_create['id'], _find)
        self.client.deals.delete_deal(result_create['id'])

    def test_get_deal(self):
        data_deal = self._get_data_deal()
        result_create = self.client.deals.create_deal(data_deal)
        try:
            self.client.deals.get_deal(result_create['id'])
            _view = True
        except:
            _view = False
        self.assertTrue(_view)
        self.client.deals.delete_deal(result_create['id'])

    def test_get_deal_stage_list(self):
        result = self.client.deals.get_deal_stage_list()
        self.assertIsInstance(result, dict)


