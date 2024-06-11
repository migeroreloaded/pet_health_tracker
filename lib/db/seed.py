# Importing necessary module for database management
import sqlite3

# Database file name
DATABASE = 'pet_health_tracker.db'

# Function to create database tables based on schema
def create_tables():
    # Connecting to the SQLite database
    conn = sqlite3.connect(DATABASE)
    
    # Reading schema file and executing SQL commands
    with open('lib/db/schema.sql') as f:
        conn.executescript(f.read())
    
    # Closing the database connection
    conn.close()

# Entry point to execute script
if __name__ == "__main__":
    create_tables()
