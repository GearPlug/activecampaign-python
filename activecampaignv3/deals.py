class Deals(object):
    def __init__(self, client):
        self.client = client

    def create_a_deal(self, data):
        """
        Create a new deal


        Args:
            data:

        Returns:

        """
        return self.client._post("/deals", json=data)

    def retrieve_a_deal(self, deal_id):
        """
        Retrieve an existing deal


        Args:
            deal_id:

        Returns:

        """
        return self.client._get("/deals/{}".format(deal_id))

    def update_a_deal(self, deal_id, data):
        """
        Update an existing deal


        Args:
            deal_id:
            data:

        Returns:

        """
        return self.client._put("/deals/{}".format(deal_id), json=data)

    def delete_a_deal(self, deal_id):
        """
        Delete an existing deal


        Args:
            deal_id:

        Returns:

        """
        return self.client._delete("/deals/{}".format(deal_id))

    def list_all_deals(self, **params):
        """
        Retrieve all existing deals


        Returns:

        """
        return self.client._get("/deals", params=params)

    def create_a_deal_note(self, deal_id, data):
        """
        Create a new note for a deal


        Args:
            deal_id:
            data:

        Returns:

        """
        return self.client._post("/deals/{}/notes".format(deal_id), json=data)

    def update_a_deal_note(self, deal_id, note_id, data):
        """
        Update an existing note for a deal


        Args:
            deal_id:
            note_id:
            data:

        Returns:

        """
        return self.client._put("/deals/{}/notes/{}".format(deal_id, note_id), json=data)

    def create_a_pipeline(self):
        raise NotImplementedError

    def retrieve_a_pipeline(self):
        raise NotImplementedError

    def update_a_pipeline(self):
        raise NotImplementedError

    def delete_a_pipeline(self):
        raise NotImplementedError

    def list_all_pipelines(self, **params):
        """
        Retrieve all existing pipelines


        Returns:

        """
        return self.client._get("/dealGroups", params=params)

    def create_a_stage(self):
        raise NotImplementedError

    def retrieve_a_stage(self):
        raise NotImplementedError

    def update_a_stage(self):
        raise NotImplementedError

    def delete_a_stage(self):
        raise NotImplementedError

    def list_all_stages(self, **params):
        """
        Retrieve all existing stages


        Returns:

        """
        return self.client._get("/dealStages", params=params)

    def move_deals_to_another_stage(self):
        raise NotImplementedError

    def create_a_custom_field(self):
        raise NotImplementedError

    def retrieve_a_custom_field(self):
        raise NotImplementedError

    def update_a_custom_field(self):
        raise NotImplementedError

    def delete_a_custom_field(self):
        raise NotImplementedError

    def list_all_custom_fields(self):
        raise NotImplementedError

    def create_a_custom_field_value(self):
        raise NotImplementedError

    def bulk_create_a_custom_field_value(self):
        raise NotImplementedError

    def retrieve_a_custom_field_value(self):
        raise NotImplementedError

    def update_a_custom_field_value(self):
        raise NotImplementedError

    def bulk_update_a_custom_field_value(self):
        raise NotImplementedError

    def delete_a_custom_field_value(self):
        raise NotImplementedError

    def list_all_custom_field_values(self):
        raise NotImplementedError

    def create_a_secondary_contact(self):
        raise NotImplementedError

    def retrieve_a_secondary_contact(self):
        raise NotImplementedError

    def update_a_secondary_contact(self):
        raise NotImplementedError

    def delete_a_secondary_contact(self):
        raise NotImplementedError

    def list_all_secondary_contacts(self):
        raise NotImplementedError
