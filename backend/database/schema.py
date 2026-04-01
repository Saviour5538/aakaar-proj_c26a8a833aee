from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for declarative class definitions
Base = declarative_base()

# Define a class that inherits from Base and defines the columns
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

# Define a class that inherits from Base and defines the columns for overlapping chunking strategy
class Chunk(Base):
    __tablename__ = 'chunks'
    id = Column(Integer, primary_key=True)
    data = Column(String)
    chunk_size = Column(Integer)