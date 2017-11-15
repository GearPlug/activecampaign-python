"""
The contacts module provides functionality for working with contacts in your
ActiveCampaign account.
Documentation: https://www.activecampaign.com/api/overview.php
"""


class Contacts(object):
    def __init__(self, client):
        self.client = client

    def create_contact(self, data):
        """
        :param data: A dictionary with the parameters
        data ={
            "email": String, Unique email
            "first_name": String, First name of the contact.
            "last_name": String, Last name of the contact."
            "phone": An String, Phone number of the contact. Example: '+1 312 201 0300"
            "orgname": String. Organization name (if doesn't exist, this will create a new organization)
                        - MUST HAVE CRM FEATURE FOR THIS"
            "tags": String. Tags for this contact (comma-separated). Example: "tag1, tag2, etc"
            "ip4": IP address of the contact. Example: '127.0.0.1' If not supplied, it will default to '127.0.0.1"
            "field": String. Custom field values. Example: field[345,0] = 'value'. In this example,
                    "345" is the field ID. Leave 0 as is"
            "p[123]": String. Assign to lists. List ID goes in brackets, as well as the value"
            "status": String, The status for each list the contact is added to. Examples: 1 = active, 2 = unsubscribed"
            "form": String. Optional subscription Form ID, to inherit those redirection settings. Example: 1001.
                    This will allow you to mimic adding the contact through a subscription form, where you can take advantage
                    of the redirection settings."
            "noresponder": String. Whether or not to set "do not send any future responders." Examples: 1 = yes, 0 = no."
            "sdate": String. Subscribe date for particular list - leave out to use current date/time.
                    Example: '2009-12-07 06:00:00' Be sure to pass the date/time as CST (Central Standard Time)."
            "instantresponders": String. Use only if status = 1. Whether or not to set "send instant responders."
                                Examples: 1 = yes, 0 = no."
            "lastmessage": String. Whether or not to set "send the last broadcast campaign." Examples: 1 = yes, 0 = no."
            }
        :return: A json
        """
        if "email" not in data:
            raise KeyError("The contact must have an email")
        return self.client._post("contact_sync", data=data)

    def subscribe_contact(self, data):
        """
        :param data: A dictionary with the parameters
        data ={
                "email": String, Unique email
                "first_name": String, First name of the contact.
                "last_name": String, Last name of the contact."
                "phone": An String, Phone number of the contact. Example: '+1 312 201 0300"
                "orgname": String. Organization name (if doesn't exist, this will create a new organization)
                            - MUST HAVE CRM FEATURE FOR THIS"
                "tags": String. Tags for this contact (comma-separated). Example: "tag1, tag2, etc"
                "ip4": IP address of the contact. Example: '127.0.0.1' If not supplied, it will default to '127.0.0.1"
                "field": String. Custom field values. Example: field[345,0] = 'value'. In this example,
                        "345" is the field ID. Leave 0 as is"
                "p[123]": String. Assign to lists. List ID goes in brackets, as well as the value"
                "status[123]": String, The status for each list the contact is added to. Examples: 1 = active, 2 = unsubscribed"
                "form": String. Optional subscription Form ID, to inherit those redirection settings. Example: 1001.
                        This will allow you to mimic adding the contact through a subscription form, where you can take advantage
                        of the redirection settings."
                "noresponder": String. Whether or not to set "do not send any future responders." Examples: 1 = yes, 0 = no."
                "sdate": String. Subscribe date for particular list - leave out to use current date/time.
                        Example: '2009-12-07 06:00:00' Be sure to pass the date/time as CST (Central Standard Time)."
                "instantresponders": String. Use only if status = 1. Whether or not to set "send instant responders."
                                    Examples: 1 = yes, 0 = no."
                "lastmessage": String. Whether or not to set "send the last broadcast campaign." Examples: 1 = yes, 0 = no."
            }
        :return: A json
        """
        if "email" not in data:
            raise KeyError("The contact must have an email")

        return self.client._post("contact_add", data=data)

    def edit_contact(self, data):
        """
        :param data: A dictionary with the parameters
        data ={
            "email": String, Unique email
            "first_name": String, First name of the contact.
            "last_name": String, Last name of the contact."
            "phone": An String, Phone number of the contact. Example: '+1 312 201 0300"
            "orgname": String. Organization name (if doesn't exist, this will create a new organization)
                        - MUST HAVE CRM FEATURE FOR THIS"
            "tags": String. Tags for this contact (comma-separated). Example: "tag1, tag2, etc"
            "ip4": IP address of the contact. Example: '127.0.0.1' If not supplied, it will default to '127.0.0.1"
            "field": String. Custom field values. Example: field[345,0] = 'value'. In this example,
                    "345" is the field ID. Leave 0 as is"
            "p[123]": String. Assign to lists. List ID goes in brackets, as well as the value"
            "status": String, The status for each list the contact is added to. Examples: 1 = active, 2 = unsubscribed"
            "form": String. Optional subscription Form ID, to inherit those redirection settings. Example: 1001.
                    This will allow you to mimic adding the contact through a subscription form, where you can take advantage
                    of the redirection settings."
            "noresponder": String. Whether or not to set "do not send any future responders." Examples: 1 = yes, 0 = no."
            "sdate": String. Subscribe date for particular list - leave out to use current date/time.
                    Example: '2009-12-07 06:00:00' Be sure to pass the date/time as CST (Central Standard Time)."
            "instantresponders": String. Use only if status = 1. Whether or not to set "send instant responders."
                                Examples: 1 = yes, 0 = no."
            "lastmessage": String. Whether or not to set "send the last broadcast campaign." Examples: 1 = yes, 0 = no."
            }
        :return: A json
        """
        if "email" not in data:
            raise KeyError("The contact must have an email")
        return self.client._post("contact_edit", data=data)

    def view_contact_email(self, email):
        return self.client._get("contact_view_email", aditional_data=[('email',email)])

    def view_contact(self, id):
        return self.client._get("contact_view", aditional_data=[('id', id)])

    def delete_contact(self, id):
        return self.client._get("contact_delete", aditional_data=[('id', id)])