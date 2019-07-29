class Notes(object):
    def __init__(self, client):
        self.client = client

    def create_a_note(self, data):
        """
        Create a new note


        Args:
            data:

        Returns:

        """
        return self.client._post("/notes", json=data)

    def retrieve_a_note(self, note_id):
        """
        Retrieve an existing note


        Args:
            note_id:

        Returns:

        """
        return self.client._get("/notes/{}".format(note_id))

    def update_a_note(self, note_id, data):
        """
        Update an existing note


        Args:
            note_id:
            data:

        Returns:

        """
        return self.client._put("/notes/{}".format(note_id), json=data)

    def delete_a_note(self, note_id):
        """
        Delete an existing note


        Args:
            note_id:

        Returns:

        """
        return self.client._delete("/notes/{}".format(note_id))
