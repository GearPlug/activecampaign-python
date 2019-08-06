class Webhooks(object):
    def __init__(self, client):
        self.client = client

    def create_a_webhook(self, data):
        """
        Create a new webhook


        Args:
            data:

        Returns:

        """
        return self.client._post("/webhooks", json=data)

    def retrieve_a_webhook(self, webhook_id):
        """
        Retrieve an existing webhook


        Args:
            webhook_id:

        Returns:

        """
        return self.client._get("/webhooks/{}".format(webhook_id))

    def update_a_webhook(self, webhook_id, data):
        """
        Update an existing webhook


        Args:
            webhook_id:
            data:

        Returns:

        """
        return self.client._put("/webhooks/{}".format(webhook_id), json=data)

    def delete_a_webhook(self, webhook_id):
        """
        Delete an existing webhook


        Args:
            webhook_id:

        Returns:

        """
        return self.client._delete("/webhooks/{}".format(webhook_id))

    def list_all_webhooks(self, **params):
        """
        List all existing webhooks


        Returns:

        """
        return self.client._get("/webhooks", params=params)

    def list_all_webhook_events(self):
        """
        List all available webhook events


        Returns:

        """
        return self.client._get("/webhooks/events")
