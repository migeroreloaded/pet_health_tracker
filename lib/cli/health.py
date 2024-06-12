from lib.db.models import get_db_session, HealthRecord

# Function to log a health record for a pet
def log_health_record():
    print("\nLog a Health Record\n")
    # Get user input for health record details
    pet_id = input("Enter pet ID: ")
    visit_date = input("Enter visit date (YYYY-MM-DD): ")
    notes = input("Enter notes: ")

    # Create a new session
    session = get_db_session()
    
    # Create a new HealthRecord object
    new_record = HealthRecord(pet_id=pet_id, visit_date=visit_date, notes=notes)
    
    # Add and commit the new health record to the database
    session.add(new_record)
    session.commit()
    
    # Close the session
    session.close()
    
    # Print success message
    print(f"Health record for pet {pet_id} logged successfully.")

# Function to view health records of a pet
def view_health_records():
    print("\nView Health Records\n")
    # Get user input for pet ID
    pet_id = input("Enter pet ID: ")

    # Create a new session
    session = get_db_session()
    
    # Retrieve health records of the specified pet
    records = session.query(HealthRecord).filter_by(pet_id=pet_id).all()
    
    # Close the session
    session.close()
    
    # Print health records
    for record in records:
        print(f"Visit Date: {record.visit_date}, Notes: {record.notes}")
