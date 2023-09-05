import csv
from colorama import init, Fore, Style

# Init
init()

# Open files
item_list = open("../GetAllTheItemsinator/items_list.csv")
item_reader = csv.reader(item_list)

chest_list = open("chest_list.csv")
chest_reader = csv.reader(chest_list)
next(chest_list)
def main():
    print("Welcome to the GetAllTheItemsinator tool!")
    print("Type 'help' to open the user manual.")
    print()
    mainCmd()

# Main prompt which controls access to other functions.
def mainCmd():
    action = input("jk$ ")

    match action:
        case "help" | "man":
            help()
        case "chestvis":
            chestvis()
        case "exit":
            print("Bye")
            exit()
        case "searchid" | "sid":
            searchid()
        case "":
            mainCmd()
        case _:
            print("Invalid command.")
            mainCmd()

# Displays the help menu.
def help():
    print()
    print("Command List: ")
    print("help (or man): Opens the help window.")
    print("chestvis: Enables a double chest visualizer which shows a diagram of a double chest's slots, starting with the predefined ID.")
    print("searchfname: Search for an item's data by its friendly name. (e.g. 'Diamond Axe')")
    print("searchid (or sid): Search for an item's data by its ID.")
    print("search: Search for an item by it's in-game name. (e.g. DIAMOND_AXE)")
    print("exit: Exits the tool.")
    print()

    mainCmd()

# Tool that displays a diagram of a double chest based on defined starting index.
def chestvis():
    # Tool to display the ID of each needed item to associate it with a chest slot.
    starting_number = input("Enter the starting chest slot number: ")
    # Checks that the selected chest number is a digit. If it is,
    # the program automatically casts it to the int type.
    if starting_number.isdigit():
        starting_number = int(starting_number)

        while starting_number <= 0:
            starting_number = int(input("Starting ID must be 1 or larger. Enter a starting ID number: "))
        incremented_number = starting_number

        # Used to store all the values returned through the item count.
        index_viewer = []

        # Subtracts one number from the loop because the value doesn't start with 0.
        while incremented_number <= starting_number + 53:
            index_viewer.append(str(incremented_number))
            incremented_number = incremented_number + 1

        # Splits the 54-entry array into 6 even sub-arrays, similating 6 double chest rows.
        sorted_view = [index_viewer[i:i + 9] for i in range(0, len(index_viewer), 9)]

        # Reorganize data by columns
        cols = zip(*sorted_view)

        # Compute column widths by taking maximum length of values per column
        col_widths = [max(len(value) for value in col) for col in cols]

        # Create a format string
        format = ' '.join(['%%%ds ' % width for width in col_widths])

        # Print each row using the computed format
        print("LARGE CHEST -------------------------------")
        for row in sorted_view:
            print(format % tuple(row))

        print("")

        print("STATISTICS: ")
        print("Starts with:", index_viewer[0], "and ends with:", index_viewer[-1])
        print()
        mainCmd()
    else:
        print("Chest slot ID must be a number.")
        chestvis()
def chestvis(starting_slot, searched_value):
    # Tool to display the ID of each needed item to associate it with a chest slot.

    search_id = int(starting_slot)

    incremented_number = int(starting_slot)

    # Used to store all the values returned through the item count.
    index_viewer = []

    # Subtracts one number from the loop because the value doesn't start with 0.
    while incremented_number <= int(starting_slot) + 53:
        index_viewer.append(str(incremented_number))
        incremented_number = incremented_number + 1

    # Just before sorting, the program colors the item ID slot for easy viewing.
    searched_value = str(searched_value)
    for i in range(len(index_viewer)):
        if index_viewer[i] == searched_value:
            index_viewer[i] = f'{Fore.GREEN}' + searched_value + f'{Style.RESET_ALL}'
        else:
            index_viewer[i] = f'{Fore.RESET}' + index_viewer[i] + f'{Style.RESET_ALL}'

    # Splits the 54-entry array into 6 even sub-arrays, similating 6 double chest rows.
    sorted_view = [index_viewer[i:i + 9] for i in range(0, len(index_viewer), 9)]

    # Reorganize data by columns
    cols = zip(*sorted_view)

    # Compute column widths by taking maximum length of values per column
    col_widths = [max(len(value) for value in col) for col in cols]

    # Create a format string
    format = ' '.join(['%%%ds ' % width for width in col_widths])

    # Print each row using the computed format
    print("LARGE CHEST -------------------------------")
    for row in sorted_view:
        print(format % tuple(row))

    print("")

    print("STATISTICS: ")
    print("Starts with", starting_slot, "and ends with", index_viewer[-1])
    print()

def searchid():
    search_id = input("Enter the Item's number ID: ")
    if search_id.isdigit():
        for row in item_reader:
            if search_id == row[1]:
                print(row[1], row[0])
                print("The item should be placed in chest", findChest(search_id))
                mainCmd()
    else:
        print("You must use a number.")
        searchid()

def findChest(search_id):

    search_id = int(search_id)
    for row in chest_reader:
        starting_value = row[1]
        ending_value = row[2]

        if int(starting_value) <= search_id <= int(ending_value):
            chestvis(starting_value, search_id)
            return row[0]
        else:
            print("False")
    return "None"
main()
