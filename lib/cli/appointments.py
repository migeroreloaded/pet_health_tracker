from lib.db.models import get_db_session, Appointment, Pet

# Function to set an appointment for a pet
def set_appointment():
    """
    This function allows setting an appointment for a pet.
    """
    # Gather appointment details from user input
    print("\nSet an Appointment\n")
    pet_id = input("Enter pet ID: ")
    appointment_date = input("Enter appointment date (YYYY-MM-DD): ")
    details = input("Enter appointment details: ")

    # Establish a database session
    session = get_db_session()
    
    try:
        # Create a new appointment object and add it to the session
        new_appointment = Appointment(pet_id=pet_id, appointment_date=appointment_date, details=details)
        session.add(new_appointment)
        # Commit the transaction
        session.commit()
        print(f"Appointment for pet {pet_id} set successfully.")
    except Exception as e:
        # Rollback the session in case of an error
        session.rollback()
        print(f"Error setting appointment: {e}")
    finally:
        # Close the session
        session.close()

# Function to view appointments of a user's pets
def view_appointments():
    """
    This function allows viewing appointments for a user's pets.
    """
    # Get user ID input
    print("\nView Appointments\n")
    user_id = input("Enter user ID: ")

    session = get_db_session()
    
    try:
        # Query pets belonging to the user
        pets = session.query(Pet).filter_by(user_id=user_id).all()
        for pet in pets:
            # Query appointments for each pet and print details
            appointments = session.query(Appointment).filter_by(pet_id=pet.pet_id).all()
            for appointment in appointments:
                print(f"Pet: {pet.name}, Appointment Date: {appointment.appointment_date}, Details: {appointment.details}")
    except Exception as e:
        print(f"Error retrieving appointments: {e}")
    finally:
        # Close the session
        session.close()
