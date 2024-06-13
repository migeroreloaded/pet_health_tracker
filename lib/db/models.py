# Importing necessary modules for SQLAlchemy ORM
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Initialize the database engine
DATABASE_URL = 'sqlite:///pet_health_tracker.db'
engine = create_engine(DATABASE_URL)

# Create a base class for declarative models
Base = declarative_base()

# Define the User model
class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)
    pets = relationship('Pet', back_populates='owner')

# Define the Pet model
class Pet(Base):
    __tablename__ = 'pets'
    pet_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    name = Column(String, nullable=False)
    species = Column(String, nullable=False)
    breed = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    owner = relationship('User', back_populates='pets')
    health_records = relationship('HealthRecord', back_populates='pet')
    appointments = relationship('Appointment', back_populates='pet')

# Define the HealthRecord model
class HealthRecord(Base):
    __tablename__ = 'health_records'
    record_id = Column(Integer, primary_key=True, autoincrement=True)
    pet_id = Column(Integer, ForeignKey('pets.pet_id'), nullable=False)
    visit_date = Column(Date, nullable=False)
    notes = Column(String, nullable=False)
    pet = relationship('Pet', back_populates='health_records')

# Define the Appointment model
class Appointment(Base):
    __tablename__ = 'appointments'
    appointment_id = Column(Integer, primary_key=True, autoincrement=True)
    pet_id = Column(Integer, ForeignKey('pets.pet_id'), nullable=False)
    appointment_date = Column(Date, nullable=False)
    details = Column(String, nullable=False)
    pet = relationship('Pet', back_populates='appointments')

# Create the tables in the database
def create_tables():
    """Create all tables."""
    Base.metadata.create_all(engine)

# Create a sessionmaker to handle database sessions
Session = sessionmaker(bind=engine)

# Function to establish a new session with the database
def get_db_session():
    return Session()
