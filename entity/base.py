from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

# engine = create_engine('postgresql://postgres:toor@localhost:5432/projektpo', echo=True)
# Base.metadata.create_all(engine)
#
# Session = sessionmaker(bind=engine)
# session = Session()
