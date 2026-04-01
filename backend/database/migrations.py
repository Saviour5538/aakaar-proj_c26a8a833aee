from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Define database connection URL
DATABASE_URL = os.environ.get('DATABASE_URL')

# Create a database engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()

# Define a class that inherits from Base and defines the columns
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

# Create all tables in the engine
Base.metadata.create_all(engine)

# Create a new session
session = Session()

# Add a new user
def add_user(name: str, email: str) -> None:
    try:
        new_user = User(name=name, email=email)
        session.add(new_user)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e

# Get all users
def get_users() -> List[User]:
    try:
        return session.query(User).all()
    except Exception as e:
        raise e