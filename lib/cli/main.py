# Importing necessary module for command-line interface (CLI) management
import argparse

# Importing submodules containing commands for managing users, pets, health records, and appointments
from lib.cli import users, pets, health, appointments

# Main function to parse command-line arguments and execute corresponding actions
def main():
    # Creating a command-line argument parser
    parser = argparse.ArgumentParser(description="Pet Health Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Adding subparsers for different categories of commands
    users.add_user_commands(subparsers)
    pets.add_pet_commands(subparsers)
    health.add_health_commands(subparsers)
    appointments.add_appointment_commands(subparsers)

    # Parsing the command-line arguments
    args = parser.parse_args()
    
    # Executing the corresponding function based on the parsed command
    if args.command:
        args.func(args)
    else:
        parser.print_help()

# Entry point to execute the script
if __name__ == "__main__":
    main()
