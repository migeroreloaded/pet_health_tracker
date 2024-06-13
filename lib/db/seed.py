# Importing function to create database tables from models.py
from models import create_tables  

# Main function to execute database seeding
def main():
    # Create tables based on the defined schema
    create_tables()

# Entry point to execute the script
if __name__ == "__main__":
    main()
