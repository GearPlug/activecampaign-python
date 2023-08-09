class Events(object):
    """
    https://developers.activecampaign.com/reference/contact-event-tracking-api-guide
    """
    def __init__(self, client):
        self.client = client

    def create_an_event(self, name):
        """
        Create a new event


        Args:
            name:

        Returns:

        """
        data = {
            "eventTrackingEvent": {
                "name": name
            }
        }
        return self.client._post("/eventTrackingEvents", json=data)

    def list_all_events(self):
        """

        """
        return self.client._get(f"/eventTrackingEvents")
