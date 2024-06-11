# Importing necessary modules for database management and date handling
import sqlite3
from datetime import datetime

# Database file name
DATABASE = 'pet_health_tracker.db'

# Function to establish connection with the database
def get_db_connection():
    # Connecting to the SQLite database and setting row factory to retrieve rows as dictionaries
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Function to ensure database tables are created if they don't exist
def create_tables():
    # Establishing connection with the database
    conn = get_db_connection()
    
    # Creating tables if they don't exist based on schema
    conn.executescript('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        email TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS pets (
        pet_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        species TEXT NOT NULL,
        breed TEXT NOT NULL,
        age INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (user_id)
    );

    CREATE TABLE IF NOT EXISTS health_records (
        record_id INTEGER PRIMARY KEY AUTOINCREMENT,
        pet_id INTEGER NOT NULL,
        visit_date DATE NOT NULL,
        notes TEXT NOT NULL,
        FOREIGN KEY (pet_id) REFERENCES pets (pet_id)
    );

    CREATE TABLE IF NOT EXISTS appointments (
        appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        pet_id INTEGER NOT NULL,
        appointment_date DATE NOT NULL,
        details TEXT NOT NULL,
        FOREIGN KEY (pet_id) REFERENCES pets (pet_id)
    );
    ''')
    
    # Closing the database connection
    conn.close()

# Entry point to execute script
if __name__ == "__main__":
    create_tables()
