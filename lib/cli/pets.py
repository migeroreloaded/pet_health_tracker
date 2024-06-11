# Importing function to establish connection with the database
from lib.db.models import get_db_connection

# Function to add a new pet to the system
def add_pet():
    print("\nAdd a New Pet\n")
    # Get user input for pet details
    pet_details = (
        input("Enter user ID: "),
        input("Enter pet's name: "),
        input("Enter pet's species: "),
        input("Enter pet's breed: "),
        input("Enter pet's age: ")
    )

    # Establishing connection with the database
    conn = get_db_connection()
    
    # Inserting pet details into the 'pets' table
    conn.execute('INSERT INTO pets (user_id, name, species, breed, age) VALUES (?, ?, ?, ?, ?)', pet_details)
    
    # Committing the transaction and closing the database connection
    conn.commit()
    conn.close()
    
    # Printing success message
    print(f"Pet {pet_details[1]} added successfully.")
