from diary import Diary

if __name__ == "__main__":

    d1 = Diary()

    print("Before ENTRIES")
    d1.list_entries()

    d1.write_entry()

    print("After ENTRIES")
    d1.list_entries()

    print("Read ENTRIES")
    d1.read_entry()

    print("Add another ENTRY")
    d1.write_entry()

    d1.list_entries()

    print("Read one of the ENTRIES")
    d1.read_entry()
    
    print("After DELETE ENTRIES")
    d1.delete_entry()

    d1.list_entries()

    print("You are now writing to your own diary")
    d2 = Diary()

    stop = False
    while not stop:
        command = input("Input command")

        if command.lower() == "help":
            print("commands [w for write entries, r for read entries, l for list entries, d for delete entries, q for quit]")

        elif command.lower() == "r":
            d2.read_entry()

        elif command.lower() == "w":
            d2.write_entry()

        elif command.lower() == "d":
            d2.delete_entry()

        elif command.lower() == "l":
            d2.list_entries()

        elif command.lower() == "q":
            stop = True

        else:
            print("unkown command entered. Try using help")
