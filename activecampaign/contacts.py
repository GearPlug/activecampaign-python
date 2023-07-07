class Contacts(object):
    def __init__(self, client):
        self.client = client

    def create_a_contact(self, data):
        """
        Create a new contact


        Args:
            data:

        Returns:

        """
        return self.client._post("/contacts", json=data)

    def create_or_update_contact(self, data):
        """
        Create a new contact or updates it


        Args:
            data:

        Returns:

        """
        return self.client._post("/contact/sync", json=data)

    def retrieve_a_contact(self, contact_id):
        """
        Retrieve an existing contact


        Args:
            contact_id:

        Returns:

        """
        return self.client._get("/contacts/{}".format(contact_id))

    def update_list_status_for_a_contact(self, data):
        """
        Subscribe a contact to a list or unsubscribe a contact from a list.


        Args:
            data:

        Returns:

        """
        return self.client._post("/contactLists", json=data)

    def update_a_contact(self, contact_id, data):
        """
        Update an existing contact


        Args:
            contact_id:
            data:

        Returns:

        """
        return self.client._put("/contacts/{}".format(contact_id), json=data)

    def delete_a_contact(self, contact_id):
        """
        Delete an existing contact


        Args:
            contact_id:

        Returns:

        """
        return self.client._delete("/contacts/{}".format(contact_id))

    def list_all_contacts(self, **params):
        """
        View many (or all) contacts by including their ID's or various filters.
        This is useful for searching for contacts that match certain criteria -
        such as being part of a certain list, or having a specific custom field value.


        Returns:

        """
        return self.client._get("/contacts", params=params)

    def list_all_automations_the_contacts_is_in(self, contact_id):
        """


        Returns:

        """
        return self.client._get("/contacts/{}/contactAutomations".format(contact_id))

    def retrieve_a_contacts_score_value(self, contact_id):
        """


        Returns:

        """
        return self.client._get("/contacts/{}/scoreValues".format(contact_id))

    def add_a_contact_to_an_automation(self, data):
        """


        Args:
            data:

        Returns:

        """
        return self.client._post("/contactAutomations", json=data)

    def retrieve_an_automation_a_contact_is_in(self, contact_automation_id):
        """


        Returns:

        """
        return self.client._get("/contactAutomations/{}".format(contact_automation_id))

    def remove_a_contact_from_an_automation(self, contact_automation_id):
        """


        Returns:

        """
        return self.client._delete("/contactAutomations/{}".format(contact_automation_id))

    def list_all_automations_a_contact_is_in(self):
        """


        Returns:

        """
        return self.client._get("/contactAutomations")

    def create_a_custom_field(self, data):
        """
        Create a new custom field


        Args:
            data:

        Returns:

        """
        return self.client._post("/fields", json=data)

    def retrieve_a_custom_field(self, field_id):
        """
        Retrieve an existing custom field


        Args:
            field_id:

        Returns:

        """
        return self.client._get("/fields/{}".format(field_id))

    def update_a_custom_field(self, field_id, data):
        """
        Update an existing custom field


        Args:
            field_id:
            data:

        Returns:

        """
        return self.client._put("/fields/{}".format(field_id), json=data)

    def delete_a_custom_field(self, field_id):
        """
        Delete an existing custom field


        Args:
            field_id:

        Returns:

        """
        return self.client._delete("/fields/{}".format(field_id))

    def list_all_custom_fields(self, **params):
        """

        Returns:

        """
        return self.client._get("/fields", params=params)

    def create_a_custom_field_relationship_to_list(self, data):
        """

        Args:
            data:

        Returns:

        """
        return self.client._post("/fieldRels", json=data)

    def create_custom_field_options(self, data):
        """

        Args:
            data:

        Returns:

        """
        return self.client._post("/fieldOption/bulk", json=data)

    def create_a_custom_field_value(self, data):
        return self.client._post("/fieldValues", json=data)
    
    def retrieve_a_custom_field_value(self, field_value_id):
        return self.client._get("/fieldValues/{}".format(field_value_id))

    def update_a_custom_field_value_for_contact(self, data, field_value_id):
         return self.client._put("/fieldValues/{}".format(field_value_id), json=data)

    def delete_a_custom_field_value(self, field_value_id):
        return self.client._delete("/fieldValues/{}".format(field_value_id))

    def list_all_custom_field_values(self):
        return self.client._get("/fieldValues")
    
    def retrieve_a_contacts_field_values(self, contact_id):
        return self.client._get("/contacts/{}/fieldValues".format(contact_id))
    
    def retrieve_a_contacts_tracking_logs(self, contact_id):
        return self.client._get("/contacts/{}/trackingLogs".format(contact_id))
    
    def retrieve_a_contacts_data(self, contact_id):
        return self.client._get("/contacts/{}/contactData".format(contact_id))
    
    def retrieve_a_contacts_bounce_logs(self, contact_id):
        return self.client._get("/contacts/{}/bounceLogs".format(contact_id))
    
    def retrieve_a_contacts_geo_ips(self, contact_id):
        return self.client._get("/contacts/{}/geoIps".format(contact_id))
    
    def retrieve_a_contacts_organization(self, contact_id):
        return self.client._get("/contacts/{}/organization".format(contact_id))
    
    def retrieve_a_contacts_account_contacts(self, contact_id):
        return self.client._get("/contacts/{}/accountContacts".format(contact_id))
    
    def retrieve_a_contacts_automation_entry_counts(self, contact_id):
        return self.client._get("/contacts/{}/automationEntryCounts".format(contact_id))

    def add_a_tag_to_contact(self, data):
        """
        Add a tag to a contact

        :param data:
        :return:
        """
        return self.client._post("/contactTags", json=data)

    def remove_a_tag_from_a_contact(self, contact_tag_id):
        """
        Remove a tag from a contact

        :param contact_tag_id: The contact tag id
        :return:
        """
        return self.client._delete("/contactTags/{}".format(contact_tag_id))

    def retrieve_contact_tags(self, contact_id):
        """
        Retrieve all tags from a contact

        :param contact_id:
        :return:
        """
        return self.client._get("/contacts/{}/contactTags".format(contact_id))

    def retrieve_field_options(self, field_id):
        """


        Args:
            field_id:

        Returns:

        """
        return self.client._get("/fields/{}/options".format(field_id))
