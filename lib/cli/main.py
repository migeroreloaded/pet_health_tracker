import sys
from pathlib import Path
import click

# Add the project's root directory to the Python path for module imports
sys.path.append(str(Path(__file__).resolve().parents[2]))

# Importing submodules containing commands for managing users, pets, health records, and appointments
from lib.cli import users, pets, health, appointments

@click.group()
def cli():
    """Pet Health Tracker CLI"""
    pass

@cli.command()
@click.argument('username')
@click.argument('password')
@click.argument('email')
def register_user(username, password, email):
    """Register a new user"""
    # Calls the register_user function from the users module
    users.register_user(username, password, email)

@cli.command()
@click.argument('username')
@click.argument('password')
def login_user(username, password):
    """Login a user"""
    # Calls the login_user function from the users module
    # If login is successful, display the main menu
    if users.login_user(username, password):
        main_menu()

def main_menu():
    """Display the main menu and handle user choices."""
    while True:
        # Display the main menu options
        print("\nPet Health Tracker CLI Menu:\n")
        print("1. Add a new pet")
        print("2. Log a health record")
        print("3. View health records")
        print("4. Set an appointment")
        print("5. View appointments")
        print("0. Exit\n")

        # Get user's choice
        choice = input("Enter the number of your choice: ")

        # Handle user's choice
        if choice == '1':
            user_id = input("Enter user ID: ")
            name = input("Enter pet name: ")
            species = input("Enter species: ")
            breed = input("Enter breed: ")
            age = input("Enter age: ")
            pets.add_pet(user_id, name, species, breed, age)
        elif choice == '2':
            pet_id = input("Enter pet ID: ")
            visit_date = input("Enter visit date (YYYY-MM-DD): ")
            notes = input("Enter visit notes: ")
            health.log_health_record(pet_id, visit_date, notes)
        elif choice == '3':
            pet_id = input("Enter pet ID: ")
            health.view_health_records(pet_id)
        elif choice == '4':
            pet_id = input("Enter pet ID: ")
            appointment_date = input("Enter appointment date (YYYY-MM-DD): ")
            details = input("Enter appointment details: ")
            appointments.set_appointment(pet_id, appointment_date, details)
        elif choice == '5':
            user_id = input("Enter user ID: ")
            appointments.view_appointments(user_id)
        elif choice == '0':
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter a number between 0 and 5.")

def initial_menu():
    """Display the initial menu and handle user choices."""
    print("\nWelcome to Pet Health Tracker CLI!\n")
    print("1. Register a new user")
    print("2. Login a user")
    print("0. Exit\n")

    choice = input("Enter the number of your choice: ")
    if choice == '1':
        username = input("Enter username: ")
        password = input("Enter password: ")
        email = input("Enter email: ")
        users.register_user(username, password, email)
    elif choice == '2':
        username = input("Enter username: ")
        password = input("Enter password: ")
        if users.login_user(username, password):
            main_menu()
    elif choice == '0':
        print("Exiting...")
        sys.exit(0)
    else:
        print("Invalid choice. Please enter a number between 0 and 2.")

if __name__ == "__main__":
    # Start with the initial menu
    initial_menu()
