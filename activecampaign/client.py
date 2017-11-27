"""
The client module is responsible for abstracting away connecting to, making
requests to, and serializing responses from the ActiveCampaign API.
"""

import requests
from activecampaign import exception
from .contacts import Contacts
from .account import Account
from .lists import Lists
from .webhooks import Webhooks
from .tasks import Tasks
from .deals import Deals
from .users import Users
from requests.auth import HTTPBasicAuth

class Client(object):

    def __init__(self, url, apikey):

        if not url.startswith("http"):
            self._base_url = "https://" + url
        else:
            self._base_url = url
            self._apikey = apikey
            self.contacts = Contacts(self)
            self.account = Account(self)
            self.lists = Lists(self)
            self.webhooks = Webhooks(self)
            self.tasks = Tasks(self)
            self.deals = Deals(self)
            self.users = Users(self)

    def _get(self, action, aditional_data=None):
        return self._request('GET', action, aditional_data=aditional_data)

    def _post(self, action, data=None, aditional_data=None):
        return self._request('POST', action, data=data, aditional_data=aditional_data)

    def _delete(self, action):
        return self._request('DELETE', action)

    def _request(self, method, action, data=None, aditional_data=None):
        params =[
            ('api_action',action),
            ('api_key', self._apikey),
            ('api_output', 'json'),
        ]
        if aditional_data is not None:
            for aditional in aditional_data:
                params.append(aditional)
        response = requests.request(method, self._base_url+"/admin/api.php", params=params, data=data).json()
        return self._parse(response)

    def _parse(self, response):
        if response['result_code'] == 1:
            return response
        else:
            raise exception.ActiveCampaignError(response["result_message"])