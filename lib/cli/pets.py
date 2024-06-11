# Importing function to establish connection with the database
from lib.db.models import get_db_connection

# Function to add a new pet to the system
def add_pet(args):
    # Establishing connection with the database
    conn = get_db_connection()
    
    # Inserting pet details into the 'pets' table
    conn.execute('INSERT INTO pets (user_id, name, species, breed, age) VALUES (?, ?, ?, ?, ?)', 
                 (args.user_id, args.name, args.species, args.breed, args.age))
    
    # Committing the transaction and closing the database connection
    conn.commit()
    conn.close()
    
    # Printing success message
    print(f"Pet {args.name} added successfully.")

# Function to add command-line arguments for pet-related commands
def add_pet_commands(subparsers):
    # Adding command for adding a new pet
    add_pet_parser = subparsers.add_parser("add_pet", help="Add a new pet")
    add_pet_parser.add_argument("--user_id", required=True, type=int, help="User ID")
    add_pet_parser.add_argument("--name", required=True, help="Pet name")
    add_pet_parser.add_argument("--species", required=True, help="Species")
    add_pet_parser.add_argument("--breed", required=True, help="Breed")
    add_pet_parser.add_argument("--age", required=True, type=int, help="Age")
    add_pet_parser.set_defaults(func=add_pet)
