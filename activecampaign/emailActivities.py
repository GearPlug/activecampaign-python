class EmailActivities(object):
    def __init__(self, client):
        self.client = client
    
    def list_all_email_activities(self, **params):
        """

        Returns:

        """
        return self.client._get("/emailActivities", params=params)
