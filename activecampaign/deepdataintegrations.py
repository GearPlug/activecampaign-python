class DeepDataIntegrations(object):
    def __init__(self, client):
        self.client = client

    def create_a_connection(self, data):
        """
        Create a connection resource


        Args:
            data:

        Returns:

        """
        return self.client._post("/connections", json=data)

    def retrieve_a_connection(self, connection_id):
        """
        Retrieve an existing connection resource


        Args:
            connection_id:

        Returns:

        """
        return self.client._get("/connections/{}".format(connection_id))
    
    def update_a_connection(self, connection_id, data):
        """
        Update an existing connection resource


        Args:
            connection_id:
            data:

        Returns:

        """
        return self.client._put("/connections/{}".format(connection_id), json=data)
    
    def delete_a_connection(self, connection_id):
        """
        Delete an existing connection resource


        Args:
            connection_id:

        Returns:

        """
        return self.client._delete("/connections/{}".format(connection_id))
    
    def list_all_connections(self):
        raise NotImplementedError

    def create_an_ecommerce_customer(self, data):
        """
        Create a new e-commerce customer resource


        Args:
            data:

        Returns:

        """
        return self.client._post("/ecomCustomers", json=data)

    def retrieve_an_ecommerce_customer(self, customer_id):
        """
        Retrieve an existing e-commerce customer resource


        Args:
            customer_id:

        Returns:

        """
        return self.client._get("/ecomCustomers/{}".format(customer_id))

    def update_an_ecommerce_customer(self, customer_id, data):
        """
        Retrieve an existing e-commerce customer resource


        Args:
            customer_id:
            data:

        Returns:

        """
        return self.client._put("/ecomCustomers/{}".format(customer_id), json=data)
    
    def delete_an_ecommerce_customer(self, customer_id):
        """
        Delete an existing e-commerce customer resource


        Args:
            customer_id:

        Returns:

        """
        return self.client._delete("/ecomCustomers/{}".format(customer_id))

    def list_all_ecommerce_customer(self):
        raise NotImplementedError

    def create_an_ecommerce_order(self, data):
        """
        Create a new e-commerce order resource


        Args:
            data:

        Returns:

        """
        return self.client._post("/ecomOrders", json=data)

    def retrieve_an_ecommerce_order(self, order_id):
        """
        Retrieve an existing new e-commerce order resource


        Args:
            order_id:

        Returns:

        """
        return self.client._get("/ecomOrders/{}".format(order_id))

    def delete_an_ecommerce_order(self, order_id):
        """
        Delete an existing e-commerce order resource


        Args:
            order_id:

        Returns:

        """
        return self.client._delete("/ecomOrders/{}".format(order_id))

    def list_all_ecommerce_orders(self):
        raise NotImplementedError

    def update_an_ecommerce_order(self, order_id, data):
        """
        Update an existing ecommerce order/cart resource.


        Args:
            order_id:
            data:

        Returns:

        """
        return self.client._put("/ecomOrders/{}".format(order_id), json=data)

    def list_ecommerce_order_products(self):
        raise NotImplementedError

    def list_ecommerce_order_products_for_a_specific_ecommerce_order(self):
        raise NotImplementedError

    def retrieve_an_ecommerce_order_product(self):
        raise NotImplementedError
