class DealActivities(object):
    def __init__(self, client):
        self.client = client
    
    def list_all_deal_activities(self, **params):
        """

        Returns:

        """
        return self.client._get("/dealActivities", params=params)
