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

    def test_create_contact(self):
        data = {'email':'correonuevo@gmail.com'}
        result = self.client.contacts.create_contact(data)
        try:
            self.client.contacts.view_contact(result['subscriber_id'])
            _view = True
        except:
            _view = False
        self.client.contacts.delete_contact(result['subscriber_id'])

    def test_subscribe_contact(self):
        data_list = self._get_datalist()
        result_list = self.client.lists.create_list(data_list)
        data_contact = {'email': 'correonuevo@gmail.com', 'p[{0}]'.format(result_list['id']):result_list['id']}
        result_subscribe = self.client.contacts.subscribe_contact(data_contact)
        result_view = self.client.contacts.view_contact(result_subscribe['subscriber_id'])
        self.assertEqual(result_view['listid'], result_list['id'])
        self.client.lists.delete_list(result_list['id'])
        self.client.contacts.delete_contact(result_view['id'])

    def test_edit_contact(self):
        result_list = self.client.lists.create_list(data=self._get_datalist())
        result_create = self.client.contacts.create_contact(data={'email':'correonuevo@gmail.com'})
        data = self.client.contacts.view_contact(result_create['subscriber_id'])
        data ['p[{0}]'.format(result_list['id'])] = result_list['id']
        self.client.contacts.edit_contact(data)
        result_view = self.client.contacts.view_contact(result_create['subscriber_id'])
        self.assertEqual(result_view['listid'], result_list['id'])
        self.client.contacts.delete_contact(result_create['subscriber_id'])
        self.client.lists.delete_list(result_list['id'])

    def test_view_contact_email(self):
        result_create = self.client.contacts.create_contact(data={'email': 'correonuevo@gmail.com'})
        try:
            self.client.contacts.view_contact_email('correonuevo@gmail.com')
            _view = True
        except:
            _view = False
        self.assertTrue(_view)
        self.client.contacts.delete_contact(result_create['subscriber_id'])

    def test_view_contact(self):
        result_create = self.client.contacts.create_contact(data={'email': 'correonuevo@gmail.com'})
        try:
            self.client.contacts.view_contact(result_create['subscriber_id'])
            _view = True
        except:
            _view = False
        self.assertTrue(_view)
        self.client.contacts.delete_contact(result_create['subscriber_id'])

    def test_delete_contact(self):
        result_create = self.client.contacts.create_contact(data={'email': 'correonuevo@gmail.com'})
        self.client.contacts.delete_contact(result_create['subscriber_id'])
        try:
            self.client.contacts.view_contact(result_create['subscriber_id'])
            _view = False
        except:
            _view = True
        self.assertTrue(_view)


