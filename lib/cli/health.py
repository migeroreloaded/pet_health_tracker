from lib.db.models import get_db_session, HealthRecord

def log_health_record(pet_id, visit_date, notes):
    """Log a new health record for a pet."""
    try:
        # Establish a new database session
        session = get_db_session()
        # Create a new HealthRecord instance
        health_record = HealthRecord(pet_id=pet_id, visit_date=visit_date, notes=notes)
        # Add the new health record to the session and commit the transaction
        session.add(health_record)
        session.commit()
        # Close the session
        session.close()
        
        print(f"Health record for pet {pet_id} logged successfully.")
    except Exception as e:
        # Handle any exceptions that occur and print an error message
        print(f"Error logging health record: {e}")

def view_health_records(pet_id):
    """View all health records for a pet."""
    try:
        # Establish a new database session
        session = get_db_session()
        # Query all health records for the given pet ID
        records = session.query(HealthRecord).filter_by(pet_id=pet_id).all()
        if not records:
            print(f"No health records found for pet ID {pet_id}")

        # Use list to hold health records
        health_records_list = []
        
        # Iterate over each record and add to the list
        for record in records:
            health_records_list.append((record.visit_date, record.notes))
        
        # Print each health record from the list
        for visit_date, notes in health_records_list:
            print(f"Visit Date: {visit_date}, Notes: {notes}")
        
        # Close the session
        session.close()
    except Exception as e:
        # Handle any exceptions that occur and print an error message
        print(f"Error viewing health records: {e}")
