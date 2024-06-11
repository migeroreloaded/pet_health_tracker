# Importing necessary module for command-line interface (CLI) management
import sys
from pathlib import Path

# Add the project's root directory to the Python path
sys.path.append(str(Path(__file__).resolve().parents[2]))

# Importing submodules containing commands for managing users, pets, health records, and appointments
from lib.cli import users, pets, health, appointments

# Function to display the numbered menu
def display_menu():
    print("\nPet Health Tracker CLI Menu:\n")
    print("1. Register a new user")
    print("2. Login a user")
    print("3. Add a new pet")
    print("4. Log a health record")
    print("5. View health records")
    print("6. Set an appointment")
    print("7. View appointments")
    print("0. Exit\n")

# Main function to parse command-line arguments and execute corresponding actions
def main():
    # Display the menu
    display_menu()
    
    # Loop to get user input until valid choice or exit
    while True:
        choice = input("Enter the number of your choice: ")
        
        if choice == '1':
            users.register_user()
        elif choice == '2':
            users.login_user()
        elif choice == '3':
            pets.add_pet()
        elif choice == '4':
            health.log_health()
        elif choice == '5':
            health.view_health()
        elif choice == '6':
            appointments.set_appointment()
        elif choice == '7':
            appointments.view_appointments()
        elif choice == '0':
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter a number between 0 and 7.")

# Entry point to execute the script
if __name__ == "__main__":
    main()
