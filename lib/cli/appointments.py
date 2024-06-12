from lib.db.models import get_db_session, Appointment, Pet

# Function to set an appointment for a pet
def set_appointment():
    print("\nSet an Appointment\n")
    # Get user input for appointment details
    pet_id = input("Enter pet ID: ")
    appointment_date = input("Enter appointment date (YYYY-MM-DD): ")
    details = input("Enter appointment details: ")

    # Create a new session
    session = get_db_session()
    
    # Create a new Appointment object
    new_appointment = Appointment(pet_id=pet_id, appointment_date=appointment_date, details=details)
    
    # Add and commit the new appointment to the database
    session.add(new_appointment)
    session.commit()
    
    # Close the session
    session.close()
    
    # Print success message
    print(f"Appointment for pet {pet_id} set successfully.")

# Function to view appointments of a user's pets
def view_appointments():
    print("\nView Appointments\n")
    # Get user input for user ID
    user_id = input("Enter user ID: ")

    # Create a new session
    session = get_db_session()
    
    # Retrieve user's pets
    pets = session.query(Pet).filter_by(user_id=user_id).all()
    
    # Iterate through pets to retrieve appointments
    for pet in pets:
        appointments = session.query(Appointment).filter_by(pet_id=pet.pet_id).all()
        for appointment in appointments:
            print(f"Pet: {pet.name}, Appointment Date: {appointment.appointment_date}, Details: {appointment.details}")
    
    # Close the session
    session.close()
