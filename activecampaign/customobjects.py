class CustomObjects(object):
    def __init__(self, client):
        self.client = client

    def create_a_schema(self, data):
        """
        Create a schema resource


        Args:
            data:

        Returns:

        """
        return self.client._post("/customObjects/schemas", json=data)

    def retrieve_a_schema(self, schema_id, show_all_fields=False):
        """
        Retrieve an existing schema resource


        Args:
            schema_id:

        Returns:

        """
        url = "/customObjects/schemas/{}".format(schema_id)
        if show_all_fields:
            url += "?showFields=all"

        return self.client._get(url)

    def update_a_schema(self, schema_id, data, show_all_fields=False):
        """
        Update an existing schema resource


        Args:
            schema_id:
            data:

        Returns:

        """
        url = "/customObjects/schemas/{}".format(schema_id)
        if show_all_fields:
            url += "?showFields=all"

        return self.client._put(url, json=data)

    def delete_a_schema(self, schema_id):
        """
        Delete an existing schema resource

        Warning: Deleting schema will delete all associated records

        Args:
            schema_id:

        Returns:

        """
        return self.client._delete("/customObjects/schemas/{}".format(schema_id))

    def list_all_schemas(self, schema_relationship=None, limit=20, offset=0, ordering=None, show_all_fields=False):
        """
        List schemas


        Args:
            schema_relationship: Default: None. Options: contact, deal, account
            limit: pagination. Default: 20 Max: 100
            offset: pagination. Zero-based index
            ordering:
            show_all_fields:

        Returns:

        """
        url = "/customObjects/schemas?limit={}&offset={}".format(limit, offset)
        if schema_relationship and schema_relationship == "contact":
            url += "&filters[relationships.id][eq]=primary-contact&filters[relationships.namespace][eq]=contacts"
        elif schema_relationship and schema_relationship == "deal":
            url += "&filters[relationships.id][eq]=deal&filters[relationships.namespace][eq]=deals"
        elif schema_relationship and schema_relationship == "account":
            url += "&filters[relationships.id][eq]=account&filters[relationships.namespace][eq]=accounts"

        if show_all_fields:
            url += "&showFields=all"

        if not ordering:
            ordering = []

        for order in ordering:
            if order[1] not in ["ASC", "DESC"]:
                return "Error in Ordering definition"
            url += "&orders[{}]={}".format(order[0], order[1])

        return self.client._get(url)

    def delete_a_field(self, schema_id, field_id, show_all_fields=False):
        """
        Delete a field within a schema resource

        Args:
            schema_id:
            field_id:

        Returns:

        """
        url = "/customObjects/schemas/{}/fields/{}".format(schema_id, field_id)
        if show_all_fields:
            url += "?showFields=all"

        return self.client._delete(url)

    def create_a_public_schema(self, data):
        """
        Create public schema


        Args:
            data:

        Returns:

        """
        return self.client._post("/customObjects/schemas/public", json=data)

    def create_a_child_schema(self, parent_id):
        """
        Create schema by parent public schema


        Args:
            parent_id:

        Returns:

        """
        return self.client._post("/customObjects/schemas/{}/child".format(parent_id))

    def create_or_update_record(self, schema_id, data):
        """
        Upsert record by schema


        Args:
            schema_id:
            data:

        Returns:

        """
        return self.client._post("/customObjects/records/{}".format(schema_id), json=data)

    def retrieve_a_record(self, schema_id, record_id):
        """
        Get record by schema and id


        Args:
            schema_id:
            record_id:

        Returns:

        """
        return self.client._get("/customObjects/records/{}/{}".format(schema_id, record_id))

    def retrieve_a_record_by_external_id(self, schema_id, external_id):
        """
        Get record by schema and external id


        Args:
            schema_id:
            external_id:

        Returns:

        """
        return self.client._get("/customObjects/records/{}/external/{}".format(schema_id, external_id))

    def delete_a_record(self, schema_id, record_id):
        """
        Delete record by schema and id


        Args:
            schema_id:
            record_id:

        Returns:

        """
        return self.client._delete("/customObjects/records/{}/{}".format(schema_id, record_id))

    def delete_a_record_by_external_id(self, schema_id, external_id):
        """
        Delete record by schema and external id


        Args:
            schema_id:
            external_id:

        Returns:

        """
        return self.client._delete("/customObjects/records/{}/external/{}".format(schema_id, external_id))

    def list_all_records(self, schema_id, contact_id=None, deal_id=None, account_id=None,
                         limit=20, offset=0):
        """
        List records by schema


        Args:
            schema_id:
            contact_id:
            deal_id:
            account_id:
            limit: pagination. Default: 20 Max: 100
            offset: pagination. Zero-based index

        Returns:

        """
        if not contact_id and not deal_id and not account_id:
            return "A contact, deal or account ID is required"

        url = "/customObjects/records/{}".format(schema_id)
        if contact_id:
            url += "?filters[relationships.primary-contact][eq]={}".format(contact_id)
        elif deal_id:
            url += "?filters[relationships.deal][eq]={}".format(deal_id)
        elif account_id:
            url += "?filters[relationships.account][eq]={}".format(account_id)

        url += "&limit={}&offset={}".format(limit, offset)

        return self.client._get(url)
