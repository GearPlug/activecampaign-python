"""
The tasks module provides functionality for working with tasks in your
ActiveCampaign account.
Documentation: https://www.activecampaign.com/api/overview.php
"""


class Tasks(object):
    def __init__(self, client):
        self.client = client

    def get_tasks(self, id):
        return self.client._get("tasks_get", aditional_data=[('id', id)])