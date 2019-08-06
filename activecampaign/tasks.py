class Tasks(object):
    def __init__(self, client):
        self.client = client

    def create_a_task(self, data):
        """
        Create a new task


        Args:
            data:

        Returns:

        """
        return self.client._post("/dealTasks", json=data)

    def retrieve_a_task(self, task_id):
        """
        Retrieve an existing task


        Args:
            task_id:

        Returns:

        """
        return self.client._get("/dealTasks/{}".format(task_id))

    def update_a_task(self, task_id, data):
        """
        Update an existing task


        Args:
            task_id:
            data:

        Returns:

        """
        return self.client._put("/dealTasks/{}".format(task_id), json=data)

    def delete_a_task(self, task_id):
        """
        Delete an existing task


        Args:
            task_id:

        Returns:

        """
        return self.client._delete("/dealTasks/{}".format(task_id))

    def list_all_tasks(self, **params):
        """
        Retrieve a list of existing tasks


        Returns:

        """
        return self.client._get("/dealTasks", params=params)
