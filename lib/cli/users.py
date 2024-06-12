import bcrypt
from lib.db.models import get_db_session, User

# Function to register a new user in the system
def register_user():
    # Get user input for registration details
    username = input("Enter username: ")
    password = input("Enter password: ")
    email = input("Enter email: ")

    # Create a new session
    session = get_db_session()
    
    # Hash the password before storing it in the database
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    # Create a new User object
    new_user = User(username=username, password=hashed_password, email=email)
    
    # Add and commit the new user to the database
    session.add(new_user)
    session.commit()
    
    # Close the session
    session.close()
    
    # Print registration success message
    print(f"User {username} registered successfully.")

# Function to login a user
def login_user():
    # Get user input for login details
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Create a new session
    session = get_db_session()
    
    # Retrieve user details based on the provided username
    user = session.query(User).filter_by(username=username).first()
    
    # Close the session
    session.close()
    
    # Verify user credentials
    if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        # Print login success message
        print(f"User {username} logged in successfully.")
        session.close()
        return True
    
    # Print login failure message
    print("Invalid username or password.")
    session.close()
    return False
