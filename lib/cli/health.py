# Importing function to establish connection with the database
from lib.db.models import get_db_connection

# Function to log a health record for a pet
def log_health_record(args):
    # Establishing connection with the database
    conn = get_db_connection()
    
    # Inserting health record details into the 'health_records' table
    conn.execute('INSERT INTO health_records (pet_id, visit_date, notes) VALUES (?, ?, ?)', 
                 (args.pet_id, args.visit_date, args.notes))
    
    # Committing the transaction and closing the database connection
    conn.commit()
    conn.close()
    
    # Printing success message
    print(f"Health record for pet {args.pet_id} logged successfully.")

# Function to view health records of a pet
def view_health_records(args):
    # Establishing connection with the database
    conn = get_db_connection()
    
    # Retrieving health records of the specified pet
    records = conn.execute('SELECT * FROM health_records WHERE pet_id = ?', (args.pet_id,)).fetchall()
    
    # Closing the database connection
    conn.close()
    
    # Printing health records
    for record in records:
        print(f"Visit Date: {record['visit_date']}, Notes: {record['notes']}")

# Function to add command-line arguments for health-related commands
def add_health_commands(subparsers):
    # Adding command for logging a health record
    log_health_parser = subparsers.add_parser("log_health", help="Log a health record")
    log_health_parser.add_argument("--pet_id", required=True, type=int, help="Pet ID")
    log_health_parser.add_argument("--visit_date", required=True, help="Visit date")
    log_health_parser.add_argument("--notes", required=True, help="Notes")
    log_health_parser.set_defaults(func=log_health_record)

    # Adding command for viewing health records
    view_health_parser = subparsers.add_parser("view_health", help="View health records")
    view_health_parser.add_argument("--pet_id", required=True, type=int, help="Pet ID")
    view_health_parser.set_defaults(func=view_health_records)
