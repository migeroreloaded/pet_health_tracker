# Importing necessary module for password hashing
import bcrypt

# Importing function to establish connection with the database
from lib.db.models import get_db_connection

# Function to register a new user in the system
def register(args):
    # Establishing connection with the database
    conn = get_db_connection()
    
    # Hashing the password before storing it in the database
    hashed_password = bcrypt.hashpw(args.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    # Inserting user details into the 'users' table
    conn.execute('INSERT INTO users (username, password, email) VALUES (?, ?, ?)', (args.username, hashed_password, args.email))
    
    # Committing the transaction and closing the database connection
    conn.commit()
    conn.close()
    
    # Printing registration success message
    print(f"User {args.username} registered successfully.")

# Function to login a user
def login(args):
    # Establishing connection with the database
    conn = get_db_connection()
    
    # Retrieving user details based on provided username
    user = conn.execute('SELECT * FROM users WHERE username = ?', (args.username,)).fetchone()
    
    # Closing the database connection
    conn.close()
    
    # Verifying user credentials
    if user and bcrypt.checkpw(args.password.encode('utf-8'), user['password'].encode('utf-8')):
        # Printing login success message
        print(f"User {args.username} logged in successfully.")
        return True
    # Printing login failure message
    print("Invalid username or password.")
    return False

# Function to add command-line arguments for user-related commands
def add_user_commands(subparsers):
    # Adding command for registering a new user
    register_parser = subparsers.add_parser("register", help="Register a new user")
    register_parser.add_argument("--username", required=True, help="Username")
    register_parser.add_argument("--password", required=True, help="Password")
    register_parser.add_argument("--email", required=True, help="Email")
    register_parser.set_defaults(func=register)

    # Adding command for logging in a user
    login_parser = subparsers.add_parser("login", help="Login a user")
    login_parser.add_argument("--username", required=True, help="Username")
    login_parser.add_argument("--password", required=True, help="Password")
    login_parser.set_defaults(func=login)
