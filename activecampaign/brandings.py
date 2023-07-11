class Brandings(object):
    def __init__(self, client):
        self.client = client
    
    def retrieve_a_branding(self, branding_id):
        return self.client._get("/brandings/{}".format(branding_id))
    
    def update_a_branding(self, data, branding_id):
        return self.client._put("/brandings/{}".format(branding_id), json=data)
    
    def list_all_brandings(self):
        return self.client._get("/brandings")
