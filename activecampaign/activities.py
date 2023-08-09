class Activities(object):
    """
    https://developers.activecampaign.com/reference/contact-event-tracking-api-guide
    """
    def __init__(self, client):
        self.client = client

    def list_all_activities(self, contact_id):
        """

        """
        return self.client._get(f"/activities?contact={contact_id}")
