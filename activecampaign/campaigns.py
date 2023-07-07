class Campaigns(object):
    def __init__(self, client):
        self.client = client

    def list_all_campaigns(self, **params):
        return self.client._get("/campaigns", params=params)
    
    def retrieve_a_link_associated_campaign(self, campaign_id):
        return self.client._get("/campaigns/{}/links".format(campaign_id))
    
    def retrieve_a_campaign(self, campaign_id):
        return self.client._get("/campaigns/{}".format(campaign_id))