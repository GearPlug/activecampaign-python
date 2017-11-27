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
        return self.client._get("list_field_view", aditional_data=[('ids', 'all')])

    def get_lists(self):
        """
        :return: A json
        """
        return self.client._get("list_list", aditional_data=[('ids', 'all')])

    def create_list(self, data):
        """
        :param data: A dictionary with the parameters
        data ={
            "name": String, Internal list name.
            "sunscription_notify": String, Comma-separated list of email addresses to notify on new subscriptions to this list.
            "unsubscription_notify": String, Comma-separated list of email addresses to notify on any unsubscriptions from this list.
            "to_name": String, If contact doesn't enter a name, use this. Example: 'Recipient'.
            "carboncopy": String, Comma-separated list of email addresses to send a copy of all mailings to upon send.
            "stringid": String, URL-safe list name. Example: 'api-test'.
            "p_use_twitter": String, Whether or not to send this campaign to Twitter. Examples: 1 = yes, 0 = no.
            "twitter_user": String, Twitter Account Username.
            "twitter_pass": String, Twitter Account Password.
            "send_last_broadcast": String, Whether or not to send the last broadcast campaign when subscribing. Examples: 1 = yes, 0 = no.
            "require_name": String, Whether or not to require name with email when subscribing. Examples: 1 = yes, 0 = no
            "private": String, Whether or not to hide it on public side (direct links to it will still work though). Examples: 1 = yes, 0 = no
            "sender_addr1": String, Physical mailing address
            "sender_zip": String, Physical mailing address: zip or postal code
            "sender_country": String, Physical mailing address country
            "sender_url": String, Website associated with this list
            "sender_reminder": String, Remind your contacts why they are on this list and why you are emailing them
        }
        :return: A json
        """
        if "name" not in data:
            raise KeyError("The list must have a name")
        if "sender_name" not in data:
            raise KeyError("The list must have sender information include sender_name")
        if "sender_addr1" not in data:
            raise KeyError("The list must have sender information include sender address")
        if "sender_zip" not in data:
            raise KeyError("The list must have sender information include sender zip")
        if "sender_city" not in data:
            raise KeyError("The list must have sender information include sender city")
        if "sender_country" not in data:
            raise KeyError("The list must have sender information include country")
        if "sender_url" not in data:
            raise KeyError("The list must have sender information include url")
        if "sender_reminder" not in data:
            raise KeyError("The list must have sender information include reminder")
        return self.client._post("list_add", data=data)

    def delete_list(self, list_id):
        """
        :return: A json
        """
        return self.client._post("list_delete", aditional_data=[('id', list_id)])
