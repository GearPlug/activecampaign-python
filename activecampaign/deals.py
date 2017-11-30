"""
The deals module provides functionality for working with deals in your
ActiveCampaign account.
Documentation: https://www.activecampaign.com/api/overview.php
"""


class Deals(object):
    def __init__(self, client):
        self.client = client

    def create_deal(self, data):
        """
            :param data: A dictionary with the parameters
            data ={
                "title": String, Title of the new deal."
                "value": String. Value of the new deal in dollars. Example: '450.00' or 450."
                "currency": String. Currency of the new deal. Example: 'usd'."
                "pipeline": String. ID of the new deal's pipeline. Example: '3'
                                    (Get available pipeline IDs with "deal_pipeline_list" call)"
                "stage": String. ID of the new deal's stage. Example: '52' (Get available stage IDs with "deal_stage_list" call)"
                "contactid": String. D of an existing contact for the new deal.
                            Example: '8'. NOTE: IF THIS IS NOT PROVIDED, 'contact' MUST BE. (Get available contact IDs with "contact_list" call)"
                "contact_name": String. Name of the contact for the new deal. Example: 'John Doe'"
                "organization": String. Name of the organization of the contact for the new deal. Example: 'Acme Corp"
                }
            :return: A json
        """
        if "title" not in data:
            raise KeyError("The webhook must have a title")
        if "value" not in data:
            raise KeyError("The webhook must have a value")
        if "currency" not in data:
            raise KeyError("The webhook must have a currency")
        if "pipeline" not in data:
            raise KeyError("The webhook must have a pipeline")
        if "stage" not in data:
            raise KeyError("The webhook must have a stage")
        return self.client._post("deal_add", data)

    def delete_deal(self, id):
        return self.client._post("deal_delete", data={'id': id})

    def get_deals(self, page):
        return self.client._post("deal_list", aditional_data=[('page', page)])

    def get_deal(self, id):
        return self.client._post("deal_get", aditional_data=[('id', id)])

    def create_task_deal(self, data):
        """
        :param data: A dictionary with the parameters
        data ={
                "duedata": Due date of the new deal task. Example: '2014-03-17 09:30:00-06:00"
                "note": String. Text of the new deal task. Example: 'Discuss merger specifics'
                "dealid": String. ID of the deal for the new deal task. Example: '31' (Get available deal IDs with "deal_list" call)"
                "owner": String. ID of the owner of the new deal task. Example: '4' (Get available owner IDs with "user_list" call)
            }
        :return: A json
        """
        if "dealid" not in data:
            raise KeyError("The task must have a dealid")
        if "duedate" not in data:
            raise KeyError("The task must have a duedata")
        if "type" not in data:
            raise KeyError("The task must have a type")
        return self.client._post("deal_task_add", data)

    def get_deal_stage_list(self):
        return self.client._get("deal_stage_list")
