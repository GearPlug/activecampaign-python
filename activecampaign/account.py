"""
The module provides information in your ActiveCampaign account.
Documentation: https://www.activecampaign.com/api/overview.php
"""

class Account(object):

    def __init__(self, client):
        self.client = client

    def get_account_info(self):
        """
        :return: A json
        """
        return self.client._get("account_view")