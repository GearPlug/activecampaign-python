class Activities(object):
    def __init__(self, client):
        self.client = client
    
    def list_all_activities(self, **params):
        """

        Returns:

        """
        return self.client._get("/activities", params=params)
