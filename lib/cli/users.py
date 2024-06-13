import bcrypt
from lib.db.models import get_db_session, User

def register_user(username, password, email):
    """Register a new user."""
    try:
        # Establish a session with the database
        session = get_db_session()
        # Hash the user's password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        # Create a new User instance
        user = User(username=username, password=hashed_password, email=email)
        # Add and commit the new user to the database
        session.add(user)
        session.commit()
        # Close the session
        session.close()
        print(f"User {username} registered successfully.")
        return True
    except Exception as e:
        # Print any errors that occur
        print(f"Error registering user: {e}")
        return False

def login_user(username, password):
    """Login a user."""
    try:
        # Establish a session with the database
        session = get_db_session()
        # Query for the user by username
        user = session.query(User).filter_by(username=username).first()
        # Close the session
        session.close()
        # Check if user exists and the password is correct
        if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            print(f"User {username} logged in successfully.")
            return True
        # Print error message for invalid credentials
        print("Invalid username or password.")
        return False
    except Exception as e:
        # Print any errors that occur
        print(f"Error logging in user: {e}")
        return False
