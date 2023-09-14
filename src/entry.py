class Entry():
    def __init__(self, entry_name: str):
        self.entry_name = entry_name
        self.entry_path
        self.contents
        pass

    def create_file(self):
        open(self.entry_path, "x")
        pass

    # used by programmer
    def __repr__(self):
        pass 

    # used by user
    def __str__(self):
        pass 
