import os


# Displays to user what they want to do
def display_menu():
    option = 0

    while option != 3:
        print "Welcome to the To-Do App"
        print "1. Enter an entry"
        print "2. Show calendar"
        print "3. Exit"
        option = int(raw_input("Pick an item: "))
        pick_option(option)


# Picks option from what user picked
def pick_option(option):
    if option == 1:
        """Start game"""
        enter_entry()
    elif option == 2:
        """Show calendar"""
    elif option == 3:
        """Quit app"""
        print "Thanks for using our to-do app!\n"


# Gets user input and makes a calendar entry
def enter_entry():
    # Wipes screen from previous level
    os.system('clear')

    print "Enter an entry: "
    title = raw_input("Title of task: ")
    description = raw_input("Description of task: ")
    date = raw_input("Enter date (yyyy-mm-dd): ")
    time_of_day = raw_input("Time of day of task: ")


# Runs program
display_menu()