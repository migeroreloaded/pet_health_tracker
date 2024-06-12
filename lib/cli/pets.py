from lib.db.models import get_db_session, Pet

# Function to add a new pet to the system
def add_pet():
    print("\nAdd a New Pet\n")
    # Get user input for pet details
    user_id = input("Enter user ID: ")
    name = input("Enter pet's name: ")
    species = input("Enter pet's species: ")
    breed = input("Enter pet's breed: ")
    age = input("Enter pet's age: ")

    # Create a new session
    session = get_db_session()
    
    # Create a new Pet object
    new_pet = Pet(user_id=user_id, name=name, species=species, breed=breed, age=age)
    
    # Add and commit the new pet to the database
    session.add(new_pet)
    session.commit()
    
    # Close the session
    session.close()
    
    # Print success message
    print(f"Pet {name} added successfully.")
