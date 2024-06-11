# Importing necessary module for password hashing
import bcrypt

# Importing function to establish connection with the database
from lib.db.models import get_db_connection

# Function to register a new user in the system
def register_user():
    # Get user input for registration details
    username = input("Enter username: ")
    password = input("Enter password: ")
    email = input("Enter email: ")

    # Establishing connection with the database
    conn = get_db_connection()
    
    # Hashing the password before storing it in the database
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    # Inserting user details into the 'users' table
    conn.execute('INSERT INTO users (username, password, email) VALUES (?, ?, ?)', (username, hashed_password, email))
    
    # Committing the transaction and closing the database connection
    conn.commit()
    conn.close()
    
    # Printing registration success message
    print(f"User {username} registered successfully.")

# Function to login a user
def login_user():
    # Get user input for login details
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Establishing connection with the database
    conn = get_db_connection()
    
    # Retrieving user details based on provided username
    user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
    
    # Closing the database connection
    conn.close()
    
    # Verifying user credentials
    if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
        # Printing login success message
        print(f"User {username} logged in successfully.")
        return True
    # Printing login failure message
    print("Invalid username or password.")
    return False
