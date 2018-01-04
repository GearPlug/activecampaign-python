"""
The webhooks module provides functionality for working with events in real-time in your
ActiveCampaign account.
Documentation: https://www.activecampaign.com/api/overview.php
"""

class Webhooks(object):

    def __init__(self, client):
        self.client = client

    def create_webhook(self, data):
        """
        Create a new webhook in ActiveCampaign
        :param data: A dictionary with the parameters
        data ={
                "name": String, Internal name for the webhook
                "url": String, URL of the webhook
                "lists[]": String, Assign to list. Can accept multiple lists here, example "lists[1,2,3]"
                "action": An String, Event that causes the webhook. Possible values: subscribe, unsubscribe, update, sent, click, forward, share, bounce,
                        deal_add, deal_task_add.
                "init": String. Source that triggered the event. Possible values: public, admin, api, system.
            }
        :return: A json
        """
        if "name" not in data:
            raise KeyError("The webhook must have a name")
        if "url" not in data:
            raise KeyError("The webhook must have a url")
        if "action" not in data:
            raise KeyError("The webhook must have an action")
        return self.client._post("webhook_add", data=data)

    def delete_webhook(self, id):
        return self.client._post("webhook_delete", aditional_data=[('id', id)])

    def view_webhooks(self, id):
        return self.client._post("webhook_view", aditional_data=[('id', id)])