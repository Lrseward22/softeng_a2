import os


class DiaryExistsException(Exception):
    pass


class EntryExistsException(Exception):
    pass


class NoEntryException(Exception):
    pass


class Diary:
    def __init__(self, **kwargs) -> None:
        DIARIES_PATH = os.getcwd() + "/diaries"
        if not os.path.exists(DIARIES_PATH):
            os.mkdir(DIARIES_PATH)

        if "owner" in kwargs:
            self._owner = kwargs["owner"].replace(" ", "_")
        else:
            self._owner = input("Enter the name of the owner of this diary: ")
            self._owner = self._owner.replace(" ", "_")
        self._diary_path = DIARIES_PATH + f"/{self._owner}/"

        if not os.path.exists(self._diary_path):
            os.mkdir(self._diary_path)
            self._entries = {}
        else:
            raise DiaryExistsException(f"diary: {self._owner} already exists")

    def write_entry(self):
        entry_name: str = input("Name this entry: ")
        entry_name.replace(" ", "_")
        if entry_name not in self._entries.keys():
            contents: str = input("Write the contents of this entry:\n")
            filename = self._diary_path + entry_name + ".txt"
            self._entries[entry_name] = filename

            with open(filename, "w") as file:
                file.write(contents)

        else:
            raise EntryExistsException(f"{entry_name} already exists.")

    def read_entry(self):
        entry_name: str = input("Enter name of entry to read: ")
        entry_name.replace(" ", "_")
        if entry_name in self._entries.keys():
            filename = self._entries[entry_name]
            with open(filename, "r") as file:
                print(f"{entry_name}:\n{file.read()}")

        else:
            raise NoEntryException(f"{entry_name} does not exist.")

    def delete_entry(self):
        entry_name: str = input("Name of entry to delete: ")
        entry_name.replace(" ", "_")
        if entry_name in self._entries.keys():
            filename = self._entries[entry_name]

            # get user confirmation on deletion
            while True:
                confirm = input(f"Confirm deletion: (y/n)").lower()
                if confirm == "y":
                    if os.path.exists(filename):
                        os.remove(filename)
                        del self._entries[entry_name]
                    else:
                        raise NoEntryException(f"{entry_name} does not exist.")
                    break
                elif confirm == "n":
                    print("Entry not going to be deleted.")
                    break
                else:
                    print("Invalid command.")

    def list_entries(self):
        entries = list(self._entries.keys())
        print(entries)
