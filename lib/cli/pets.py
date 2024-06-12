from lib.db.models import get_db_session, Pet

# Function to add a new pet to the system
def add_pet():
    """
    This function allows adding a new pet to the system.
    """
    # Gather pet details from user input
    print("\nAdd a New Pet\n")
    user_id = input("Enter user ID: ")
    name = input("Enter pet's name: ")
    species = input("Enter pet's species: ")
    breed = input("Enter pet's breed: ")
    age = input("Enter pet's age: ")

    # Establish a database session
    session = get_db_session()
    
    try:
        # Create a new pet object and add it to the session
        new_pet = Pet(user_id=user_id, name=name, species=species, breed=breed, age=age)
        session.add(new_pet)
        # Commit the transaction
        session.commit()
        print(f"Pet {name} added successfully.")
    except Exception as e:
        # Rollback the session in case of an error
        session.rollback()
        print(f"Error adding pet: {e}")
    finally:
        # Close the session
        session.close()
