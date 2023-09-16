from diary import Diary

if __name__ == "__main__":

    d1 = Diary(owner="Jed")

    print("Before ENTRIES")
    d1.list_entries()

    d1.write_entry()

    print("After ENTRIES")
    d1.list_entries()

    print("Read ENTRIES")
    d1.read_entry()

    d1.delete_entry()

    print("After Delete ENTRIES")
    d1.list_entries()
