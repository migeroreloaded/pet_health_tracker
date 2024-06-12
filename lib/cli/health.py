from lib.db.models import get_db_session, HealthRecord

# Function to log a health record for a pet
def log_health_record():
    """
    This function allows logging a health record for a pet.
    """
    # Gather health record details from user input
    print("\nLog a Health Record\n")
    pet_id = input("Enter pet ID: ")
    visit_date = input("Enter visit date (YYYY-MM-DD): ")
    notes = input("Enter notes: ")

    # Establish a database session
    session = get_db_session()
    
    try:
        # Create a new health record object and add it to the session
        new_record = HealthRecord(pet_id=pet_id, visit_date=visit_date, notes=notes)
        session.add(new_record)
        # Commit the transaction
        session.commit()
        print(f"Health record for pet {pet_id} logged successfully.")
    except Exception as e:
        # Rollback the session in case of an error
        session.rollback()
        print(f"Error logging health record: {e}")
    finally:
        # Close the session
        session.close()

# Function to view health records of a pet
def view_health_records():
    """
    This function allows viewing health records of a pet.
    """
    # Get pet ID input
    print("\nView Health Records\n")
    pet_id = input("Enter pet ID: ")

    session = get_db_session()
    
    try:
        # Query health records for the pet and print details
        records = session.query(HealthRecord).filter_by(pet_id=pet_id).all()
        for record in records:
            print(f"Visit Date: {record.visit_date}, Notes: {record.notes}")
    except Exception as e:
        print(f"Error retrieving health records: {e}")
    finally:
        # Close the session
        session.close()
