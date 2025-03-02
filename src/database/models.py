from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from src.settings import WORKDIR
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv(WORKDIR / ".env")

# Retrieve MySQL username and password from environment variables
USERNAME = os.getenv("MYSQL_USERNAME")
PASSWORD = os.getenv("MYSQL_PASSWORD")

# Create the database URL for MySQL connection
db_url_for_mysql = f"mysql+mysqlconnector://{USERNAME}:{PASSWORD}@localhost:3306/calorie_tracker"

# Create a SQLAlchemy engine to connect to the database
engine = create_engine(db_url_for_mysql)

# Base class for declarative class definitions
Base = declarative_base()

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a Session instance
session = Session()

class BaseWithID(Base):
    """
    Abstract base class that provides an `id` column for all derived models.

    Attributes:
        id (int): Primary key column, auto-incremented.
    """
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)

class User(Base):
    """
    Represents a user in the calorie tracker application.

    Attributes:
        id (int): Primary key column, auto-incremented.
        firstname (str): The user's first name. Max length is 30 characters.
        lastname (str): The user's last name. Max length is 30 characters.
        age (int): The user's age.
        gender (str): The user's gender. Max length is 10 characters.
        bmr (int): The user's Basal Metabolic Rate (BMR).
        consumed_calories (int): Total calories consumed by the user.
        remaining_calories (int): Remaining calories for the user to consume.
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(30), nullable=False)
    lastname = Column(String(30), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(10), nullable=False)
    bmr = Column(Integer, nullable=False)
    consumed_calories = Column(Integer, nullable=False)
    remaining_calories = Column(Integer, nullable=False)

# Create all tables in the database
Base.metadata.create_all(engine)