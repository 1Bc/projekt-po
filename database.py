from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from entity.base import Base


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


def get_db():
    return session
