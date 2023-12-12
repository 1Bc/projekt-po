import datetime
from sqlalchemy import create_engine, Column, Integer, CHAR, DateTime, ForeignKey, String
from sqlalchemy.orm import sessionmaker, declarative_base
from base import Base

from user import User
from event import Event
from comment import Comment
from report import Report

# Base = declarative_base()

# Define your database connection
engine = create_engine('postgresql://postgres:toor@localhost:5432/projektpo', echo=True)

# Create tables in the database
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Perform database operations (if needed)

# Commit changes and close the session
session.commit()
session.close()
