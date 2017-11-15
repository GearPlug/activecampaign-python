import os
from unittest import TestCase
from activecampaign.client import Client
import json

class ContactsTest(TestCase):
    def setUp(self):
        self.client = Client(os.environ.get('host'), os.environ.get('api_key'))

    def _get_datalist(self):
        return {'name': 'new_list',
                'sender_name': 'my company',
                'sender_addr1': 'calle123',
                'sender_zip': '0000',
                'sender_city': 'Bogota',
                'sender_country': 'Colombia',
                'sender_url': 'www.grplug.com',
                'sender_reminder': 'This is a unittest',
                }

    # def test_create_contact(self):
    #     data = {'email':'correonuevo@gmail.com'}
    #     result = self.client.contacts.create_contact(data)
    #     try:
    #         self.client.contacts.view_contact(result['subscriber_id'])
    #         _view = True
    #     except:
    #         _view = False
    #     self.client.contacts.delete_contact(result['subscriber_id'])

    def test_subscribe_contact(self):
        data_list = self._get_datalist()
        result_list = self.client.lists.create_list(data_list)
        data_contact = {'email': 'correonuevo@gmail.com', 'p[{0}]'.format(result_list['id']):result_list['id']}
        result_subscribe = self.client.contacts.subscribe_contact(data_contact)
        result_view = self.client.contacts.view_contact(result_subscribe['subscriber_id'])
        print(result_view)


