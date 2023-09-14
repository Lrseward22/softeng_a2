import os
from entry import Entry


class Diary:

    def __init__(self, **kwargs):
        print(kwargs)
        DIARIES_PATH = os.getcwd() + "/../diaries"
        self.owner = kwargs["owner"]
        self.num_entries = 0
        self._entries = {}

        # check if DIARY_PATH exists
        if not os.path.exists(DIARIES_PATH):
            print("HERE")
            os.mkdir(DIARIES_PATH)

        self._diary_path = DIARIES_PATH + f"/{self.owner}/"

        if not os.path.exists(self._diary_path):
            os.mkdir(self._diary_path)
        else:
            # this diary already exists
            print(f"diary: {self.owner} already exists")

        pass

    def write_entry(self, **kwargs):
    #def write_entry(self):
        # entry_name (check if unique)
        # contents of entry (prompt for input)

        """
        create a new entry if name is unique
        """

        # make everything input
        entry_name = kwargs["entry_name"]
        contents = kwargs["contents"]

        filename = self._diary_path + entry_name + ".txt"

        if not os.path.exists(filename):
            with open(filename, "w") as file: 
                file.write(contents)

        else:
            print(f"Error: {entry_name} already exists.")

    def read_entry(self, **kwargs):
        # entry_name to read

        """
        prtint an entry if it exists
        """
        entry_name = kwargs["entry_name"]
        filename = self._diary_path + entry_name + ".txt"

        if os.path.exists(filename):
            with open(filename, "r") as file: 
                print(file.read())

        else:
            print(f"Error: {entry_name} does not exist.")


    def delete_entry(self, **kwargs):
        """
        delete an entry if it exists
        """
        
        entry_name = kwargs["entry_name"]

        filename = self._diary_path + entry_name + ".txt"
        if os.path.exists(filename):
            os.remove(filename)
        else:
            print(f"Error: {entry_name} does not exist.")


    def list_entries(self):
        entries = os.listdir(self._diary_path)
        entries = [entry.replace(".txt", "") for entry in entries]
        print(entries)
