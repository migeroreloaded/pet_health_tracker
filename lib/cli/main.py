# Importing necessary module for command-line interface (CLI) management
import sys
from pathlib import Path

# Add the project's root directory to the Python path
sys.path.append(str(Path(__file__).resolve().parents[2]))

# Importing submodules containing commands for managing users, pets, health records, and appointments
from lib.cli import users, pets, health, appointments

# Function to display the initial menu
def display_initial_menu():
    print("\nWelcome to Pet Health Tracker CLI!\n")
    print("1. Register a new user")
    print("2. Login a user")
    print("0. Exit\n")

# Function to display the numbered menu
def display_menu():
    print("\nPet Health Tracker CLI Menu:\n")
    print("1. Add a new pet")
    print("2. Log a health record")
    print("3. View health records")
    print("4. Set an appointment")
    print("5. View appointments")
    print("0. Exit\n")

# Main function to parse command-line arguments and execute corresponding actions
def main():
    # Display the initial menu
    display_initial_menu()
    
    # Get user input until valid choice or exit
    while True:
        choice = input("Enter the number of your choice: ")
        
        if choice == '1':
            users.register_user()
            # After registration, show login menu
            users.login_user()
            # Display main menu after login
            display_main_menu()
            break
        elif choice == '2':
            users.login_user()
            # Display main menu after login
            display_main_menu()
            break
        elif choice == '0':
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter a number between 0 and 2.")

# Function to display the main menu
def display_main_menu():
    while True:
        display_menu()
        choice = input("Enter the number of your choice: ")
        
        if choice == '1':
            pets.add_pet()
        elif choice == '2':
            health.log_health()
        elif choice == '3':
            health.view_health()
        elif choice == '4':
            appointments.set_appointment()
        elif choice == '5':
            appointments.view_appointments()
        elif choice == '0':
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter a number between 0 and 5.")

# Entry point to execute the script
if __name__ == "__main__":
    main()
