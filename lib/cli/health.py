# Importing function to establish connection with the database
from lib.db.models import get_db_connection

# Function to log a health record for a pet
def log_health_record():
    print("\nLog a Health Record\n")
    # Get user input for health record details
    health_record = (
        input("Enter pet ID: "),
        input("Enter visit date (YYYY-MM-DD): "),
        input("Enter notes: ")
    )

    # Establishing connection with the database
    conn = get_db_connection()
    
    # Inserting health record details into the 'health_records' table
    conn.execute('INSERT INTO health_records (pet_id, visit_date, notes) VALUES (?, ?, ?)', health_record)
    
    # Committing the transaction and closing the database connection
    conn.commit()
    conn.close()
    
    # Printing success message
    print(f"Health record for pet {health_record[0]} logged successfully.")

# Function to view health records of a pet
def view_health_records():
    print("\nView Health Records\n")
    # Get user input for pet ID
    pet_id = input("Enter pet ID: ")

    # Establishing connection with the database
    conn = get_db_connection()
    
    # Retrieving health records of the specified pet
    records = conn.execute('SELECT * FROM health_records WHERE pet_id = ?', (pet_id,)).fetchall()
    
    # Closing the database connection
    conn.close()
    
    # Printing health records
    for record in records:
        print(f"Visit Date: {record['visit_date']}, Notes: {record['notes']}")
