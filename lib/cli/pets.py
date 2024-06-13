from lib.db.models import get_db_session, Pet

def add_pet(user_id, name, species, breed, age):
    """Add a new pet for a user."""
    try:
        # Establish a session with the database
        session = get_db_session()
        # Create a new Pet instance
        pet = Pet(user_id=user_id, name=name, species=species, breed=breed, age=age)
        # Add and commit the new pet to the database
        session.add(pet)
        session.commit()
        # Close the session
        session.close()
        print(f"Pet {name} added successfully.")
    except Exception as e:
        # Print any errors that occur
        print(f"Error adding pet: {e}")
