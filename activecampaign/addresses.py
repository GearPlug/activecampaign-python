class Addresses(object):
    def __init__(self, client):
        self.client = client

    def create_an_address(self, data):
        return self.client._post("/addresses", json=data)    
    
    def retrieve_address(self, address_id):
        return self.client._get("/addresses/{}".format(address_id))
    
    def update_address(self, data, address_id):
        return self.client._put("/addresses/{}".format(address_id), json=data)
    
    def delete_address(self, address_id):
        return self.client._delete("/addresses/{}".format(address_id))
    
    def delete_address_associated_with_user_group(self, group_id):
        return self.client._delete("/addressGroups/{}".format(group_id))
    
    def delete_address_associated_with_list(self, list_id):
        return self.client._delete("/addressLists/{}".format(list_id))
    
    def retrieve_all_addresses(self):
        return self.client._get("/addresses")
