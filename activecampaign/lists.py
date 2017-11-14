"""
The lists module provides functionality for working with lists in your
ActiveCampaign account.
Documentation: https://www.activecampaign.com/api/overview.php
"""

class Lists(object):

    def __init__(self, client):
        self.client = client

    def get_list_field(self):
        """
        :return: A json
        """
        return self.client._get("list_field_view")

    def get_lists(self):
        """
        :return: A json
        """
        return self.client._get("list_list")