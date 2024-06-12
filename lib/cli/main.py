import sys
from pathlib import Path

# Append parent directory to sys.path to import modules from lib
sys.path.append(str(Path(__file__).resolve().parents[2]))

from lib.cli import users, pets, health, appointments

# Valid choices for the initial menu and the main menu
choices_initial = ('1', '2', '0')
choices_main = ('1', '2', '3', '4', '5', '0')

# Function to display the initial menu
def display_initial_menu():
    """
    Displays the initial menu options for the Pet Health Tracker CLI.
    """
    print("\nWelcome to Pet Health Tracker CLI!\n")
    print("1. Register a new user")
    print("2. Login a user")
    print("0. Exit\n")

# Function to display the numbered menu
def display_menu():
    """
    Displays the numbered menu options for the Pet Health Tracker CLI.
    """
    print("\nPet Health Tracker CLI Menu:\n")
    print("1. Add a new pet")
    print("2. Log a health record")
    print("3. View health records")
    print("4. Set an appointment")
    print("5. View appointments")
    print("0. Exit\n")

# Function to display the main menu
def display_main_menu():
    """
    Displays the main menu options for the Pet Health Tracker CLI.
    """
    menu_options = {
        '1': pets.add_pet,
        '2': health.log_health_record,
        '3': health.view_health_records,
        '4': appointments.set_appointment,
        '5': appointments.view_appointments,
        '0': sys.exit
    }
    while True:
        display_menu()
        choice = input("Enter the number of your choice: ")
        if choice in choices_main:
            action = menu_options.get(choice)
            if action:
                if choice == '0':
                    print("Exiting...")
                    action()
                else:
                    action()
        else:
            print("Invalid choice. Please enter a number between 0 and 5.")

# Main function to parse command-line arguments and execute corresponding actions
def main():
    """
    Main function to run the Pet Health Tracker CLI.
    """
    display_initial_menu()
    
    initial_options = {
        '1': users.register_user,
        '2': users.login_user,
        '0': sys.exit
    }
    
    while True:
        choice = input("Enter the number of your choice: ")
        if choice in choices_initial:
            action = initial_options.get(choice)
            if action:
                if choice == '0':
                    print("Exiting...")
                    action()
                else:
                    action()
                    if choice in ['1', '2']:
                        display_main_menu()
                        break
        else:
            print("Invalid choice. Please enter a number between 0 and 2.")

if __name__ == "__main__":
    main()
