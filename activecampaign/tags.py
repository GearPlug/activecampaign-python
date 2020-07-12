class Tags(object):
    def __init__(self, client):
        self.client = client

    def create_a_tag(self, data):
        """
        Create a new contact


        Args:
            data:

        Returns:

        """
        return self.client._post("/tags", json=data)

    def retrieve_a_tag(self, tag_id):
        """
        Retrieve an existing tag


        Args:
            tag_id:

        Returns:

        """
        return self.client._get("/tags/{}".format(tag_id))

    def update_a_tag(self, tag_id, data):
        """
        Update an existing tag


        Args:
            tag_id:
            data:

        Returns:

        """
        return self.client._put("/tags/{}".format(tag_id), json=data)

    def delete_a_tag(self, tag_id):
        """
        Delete an existing contact


        Args:
            tag_id:

        Returns:

        """
        return self.client._delete("/tags/{}".format(tag_id))

    def list_all_tags(self, **params):
        """
        List all tags

        Returns:

        """
        return self.client._get("/tags", params=params)