from lib.db.models import get_db_session, Appointment, Pet

def set_appointment(pet_id, appointment_date, details):
    """Set a new appointment for a pet."""
    try:
        # Establish a new database session
        session = get_db_session()
        # Create a new Appointment instance
        appointment = Appointment(pet_id=pet_id, appointment_date=appointment_date, details=details)
        # Add the new appointment to the session and commit the transaction
        session.add(appointment)
        session.commit()
        # Close the session
        session.close()
        
        print(f"Appointment for pet {pet_id} set successfully.")
    except Exception as e:
        # Handle any exceptions that occur and print an error message
        print(f"Error setting appointment: {e}")

def view_appointments(user_id):
    """View all appointments for pets owned by a user."""
    try:
        # Establish a new database session
        session = get_db_session()
        # Query all pets owned by the user
        pets = session.query(Pet).filter_by(user_id=user_id).all()
        if not pets:
            print(f"No pets found for user ID {user_id}")

        # Use list to hold appointments
        appointments_list = []
        
        # Iterate over each pet and get their appointments
        for pet in pets:
            appointments = session.query(Appointment).filter_by(pet_id=pet.pet_id).all()
            for appointment in appointments:
                appointments_list.append({
                    'pet_name': pet.name,
                    'appointment_date': appointment.appointment_date,
                    'details': appointment.details
                })
        
        # Print each appointment from the list
        for appointment in appointments_list:
            print(f"Pet: {appointment['pet_name']}, Appointment Date: {appointment['appointment_date']}, Details: {appointment['details']}")
        
        # Close the session
        session.close()
    except Exception as e:
        # Handle any exceptions that occur and print an error message
        print(f"Error viewing appointments: {e}")
