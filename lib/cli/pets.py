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

def update_pet(pet_id, name=None, species=None, breed=None, age=None):
    """Update pet details."""
    try:
        session = get_db_session()
        pet = session.query(Pet).filter_by(pet_id=pet_id).first()
        if not pet:
            print(f"No pet found with ID {pet_id}")
            return
        
        if name:
            pet.name = name
        if species:
            pet.species = species
        if breed:
            pet.breed = breed
        if age is not None:
            pet.age = age
        
        session.commit()
        session.close()
        print(f"Pet {pet_id} updated successfully.")
    except Exception as e:
        print(f"Error updating pet: {e}")

def delete_pet(pet_id):
    """Delete a pet."""
    try:
        session = get_db_session()
        pet = session.query(Pet).filter_by(pet_id=pet_id).first()
        if not pet:
            print(f"No pet found with ID {pet_id}")
            return
        
        session.delete(pet)
        session.commit()
        session.close()
        print(f"Pet {pet_id} deleted successfully.")
    except Exception as e:
        print(f"Error deleting pet: {e}")
