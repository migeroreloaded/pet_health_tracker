# Importing function to establish connection with the database
from lib.db.models import get_db_connection

# Function to add a new pet to the system
def add_pet():
    print("\nAdd a New Pet\n")
    # Get user input for pet details
    user_id = input("Enter user ID: ")
    name = input("Enter pet's name: ")
    species = input("Enter pet's species: ")
    breed = input("Enter pet's breed: ")
    age = input("Enter pet's age: ")

    # Establishing connection with the database
    conn = get_db_connection()
    
    # Inserting pet details into the 'pets' table
    conn.execute('INSERT INTO pets (user_id, name, species, breed, age) VALUES (?, ?, ?, ?, ?)', 
                 (user_id, name, species, breed, age))
    
    # Committing the transaction and closing the database connection
    conn.commit()
    conn.close()
    
    # Printing success message
    print(f"Pet {name} added successfully.")

# Function to add command-line arguments for pet-related commands
def add_pet_commands(subparsers):
    # Adding command for adding a new pet
    add_pet_parser = subparsers.add_parser("add_pet", help="Add a new pet")
    add_pet_parser.set_defaults(func=add_pet)
