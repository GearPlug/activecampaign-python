"""
The users module provides functionality for working with users in your
ActiveCampaign account.
Documentation: https://www.activecampaign.com/api/overview.php
"""

class Users(object):
    def __init__(self, client):
        self.client = client

    def view_user(self, id):
        return self.client._get("user_view", aditional_data=[('id', id)])

    def get_users(self):
        return  self.client._get("user_list", aditional_data=[('ids', 'all')])