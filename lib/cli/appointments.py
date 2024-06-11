# Importing function to establish connection with the database
from lib.db.models import get_db_connection

# Function to set an appointment for a pet
def set_appointment(args):
    # Establishing connection with the database
    conn = get_db_connection()
    
    # Inserting appointment details into the 'appointments' table
    conn.execute('INSERT INTO appointments (pet_id, appointment_date, details) VALUES (?, ?, ?)', 
                 (args.pet_id, args.appointment_date, args.details))
    
    # Committing the transaction and closing the database connection
    conn.commit()
    conn.close()
    
    # Printing success message
    print(f"Appointment for pet {args.pet_id} set successfully.")

# Function to view appointments of a user's pets
def view_appointments(args):
    # Establishing connection with the database
    conn = get_db_connection()
    
    # Retrieving user's pets
    pets = conn.execute('SELECT * FROM pets WHERE user_id = ?', (args.user_id,)).fetchall()
    
    # Iterating through pets to retrieve appointments
    for pet in pets:
        appointments = conn.execute('SELECT * FROM appointments WHERE pet_id = ?', (pet['pet_id'],)).fetchall()
        for appointment in appointments:
            print(f"Pet: {pet['name']}, Appointment Date: {appointment['appointment_date']}, Details: {appointment['details']}")
    
    # Closing the database connection
    conn.close()

# Function to add command-line arguments for appointment-related commands
def add_appointment_commands(subparsers):
    # Adding command for setting an appointment
    set_appointment_parser = subparsers.add_parser("set_appointment", help="Set an appointment")
    set_appointment_parser.add_argument("--pet_id", required=True, type=int, help="Pet ID")
    set_appointment_parser.add_argument("--appointment_date", required=True, help="Appointment date")
    set_appointment_parser.add_argument("--details", required=True, help="Details")
    set_appointment_parser.set_defaults(func=set_appointment)

    # Adding command for viewing appointments
    view_appointments_parser = subparsers.add_parser("view_appointments", help="View appointments")
    view_appointments_parser.add_argument("--user_id", required=True, type=int, help="User ID")
    view_appointments_parser.set_defaults(func=view_appointments)
