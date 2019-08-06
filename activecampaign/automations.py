class Automations(object):
    def __init__(self, client):
        self.client = client
    
    def list_all_automations(self, **params):
        """

        Returns:

        """
        return self.client._get("/automations", params=params)
