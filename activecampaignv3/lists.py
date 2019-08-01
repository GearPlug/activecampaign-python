class Lists(object):
    def __init__(self, client):
        self.client = client

    def create_a_list(self, data):
        """
        A list is a group of contacts that campaigns can be sent to.
        Every campaign is required to be sent to at least one list.
        Contacts can be added to and removed from lists manually in
        the ActiveCampaign UI, via automations, or via the API.

        NOTE: When creating a new list, it is important to then associate
        that list to a group permission as seen in "Create a list group permission" below.


        Args:
            data:

        Returns:

        """
        return self.client._post("/lists", json=data)

    def retrieve_a_list(self, list_id):
        """
        Retrieve an existing list


        Args:
            list_id:

        Returns:

        """
        return self.client._get("/lists/{}".format(list_id))

    def delete_a_list(self, list_id):
        """
        Delete an existing list


        Args:
            list_id:

        Returns:

        """
        return self.client._delete("/lists/{}".format(list_id))

    def retrieve_all_lists(self, **params):
        """
        Retrieve all existing deals


        Returns:

        """
        return self.client._get("/lists", params=params)

    def create_a_list_group_permission(self, data):
        """

        Args:
            data:

        Returns:

        """
        return self.client._post("/listGroups", json=data)
