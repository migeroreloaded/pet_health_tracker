import bcrypt
from lib.db.models import get_db_session, User

# Function to register a new user in the system
def register_user():
    # Input user details
    username = input("Enter username: ")
    password = input("Enter password: ")
    email = input("Enter email: ")

    # Establish a database session
    session = get_db_session()
    
    try:
        # Hash the password for storage
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        # Create a new user object
        new_user = User(username=username, password=hashed_password, email=email)
        # Add the new user to the session
        session.add(new_user)
        # Commit the transaction
        session.commit()
        print(f"User {username} registered successfully.")
    except Exception as e:
        # Rollback the session if an error occurs
        session.rollback()
        print(f"Error registering user: {e}")
    finally:
        # Close the session
        session.close()

# Function to login a user
def login_user():
    # Input login credentials
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Establish a database session
    session = get_db_session()
    
    try:
        # Query the database for the user
        user = session.query(User).filter_by(username=username).first()
        
        # Check if the user exists and if the password is correct
        if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            print(f"User {username} logged in successfully.")
            return True
        else:
            print("Invalid username or password.")
            return False
    except Exception as e:
        # Print error message if an exception occurs
        print(f"Error logging in user: {e}")
        return False
    finally:
        # Close the session
        session.close()
