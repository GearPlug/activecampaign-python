"""
The users module provides functionality for working with users in your
ActiveCampaign account.
Documentation: https://www.activecampaign.com/api/overview.php
"""

class Users(object):
    def __init__(self, client):
        self.client = client

    def view_contact(self, id):
        return self.client._get("user_view", aditional_data=[('id', id)])