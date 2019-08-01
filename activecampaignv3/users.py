class Users(object):
    def __init__(self, client):
        self.client = client

    def create_a_user(self, data):
        """
        Create a new user


        Args:
            data:

        Returns:

        """
        return self.client._post("/users", json=data)

    def retrieve_a_user(self, user_id):
        """
        Retrieve an existing user


        Args:
            user_id:

        Returns:

        """
        return self.client._get("/users/{}".format(user_id))

    def retrieve_a_user_by_email(self, email):
        """
        Retrieve an existing user by looking up their email address


        Args:
            email:

        Returns:

        """
        return self.client._get("/users/email/{}".format(email))

    def retrieve_a_user_by_username(self, username):
        """
        Retrieve an existing user by looking up their username


        Args:
            username:

        Returns:

        """
        return self.client._get("/users/username/{}".format(username))

    def retrieve_logged_in_user(self):
        """
        Retrieve the logged-in user


        Returns:

        """
        return self.client._get("/users/me")

    def update_a_user(self, user_id, data):
        """
        Update an existing user


        Args:
            user_id:
            data:

        Returns:

        """
        return self.client._put("/users/{}".format(user_id), json=data)

    def delete_a_user(self, user_id):
        """
        Delete an existing user


        Args:
            user_id:

        Returns:

        """
        return self.client._delete("/users/{}".format(user_id))

    def list_all_users(self, **params):
        """
        List all existing users


        Returns:

        """
        return self.client._get("/users", params=params)

    def create_a_group(self):
        raise NotImplementedError

    def retrieve_a_group(self):
        raise NotImplementedError

    def update_a_group(self):
        raise NotImplementedError

    def delete_a_group(self):
        raise NotImplementedError

    def list_all_groups(self):
        raise NotImplementedError
