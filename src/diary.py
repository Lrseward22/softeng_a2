import os
from entry import Entry


class Diary:

    def __init__(self, **kwargs) -> None:
        DIARIES_PATH = os.getcwd() + "/../diaries"
        if not os.path.exists(DIARIES_PATH):
            os.mkdir(DIARIES_PATH)

        if "owner" in kwargs:
            self._owner = kwargs["owner"] 
        else:
            self._owner = input("Enter the name of the owner of this diary: ")
        self._dairy_path = DIARIES_PATH + f"/{self._owner/"

        if not os.path.exists(self._diary_path):
            os.mkdir(self._diary_path)
            self._entries = {}
        else:
            # raise an error (THIS DIARY ALREADY EXISTS)
            print(f"diary: {self.owner} already exists")


    def write_entry(self):
        # make everything input
        entry_name: str = input("Name is this entry: ")
        if entry_name not in self._entries.keys():
            # make new entry
            contents: str = input("Write the contents of this entry:\n")
            filename = self._diary_path + entry_name + ".txt"

            with open(filename, "w") as file: 
                file.write(contents)

        else: 
            # raise error: (THIS ENTRY NAME ALREADY EXISTS)
            print(f"Error: {entry_name} already exists.")


    def read_entry(self):
        # entry_name to read
        entry_name: str = input("Name of entry to read: ")
        if entry_name in self._entries.keys():
            filename = self._diary_path + entry_name + ".txt"

        with open(filename, "r") as file: 
            print(f"{entry_name}:\n{file.read()}")

        else:
            print(f"Error: {entry_name} does not exist.")


    def delete_entry(self):
        entry_name: str = input("Name of entry to delete: ")
        if entry_name in self._entries.keys():
            filename = self._diary_path + entry_name + ".txt"

            # prompt to delete

            if os.path.exists(filename):
                os.remove(filename)
            del self._entries[entry_name]

        else:
            print(f"Error: {entry_name} does not exist.")


    def list_entries(self):
        entries = os.listdir(self._diary_path)
        entries = [entry.replace(".txt", "") for entry in entries]
        print(entries)
