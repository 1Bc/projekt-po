from sqlalchemy import Column, String, Integer, Date, Enum
from entity.base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    birth_date = Column(Date)
    gender = Column(String)
    pesel = Column(String)
    user_type = Column(Enum('sportowiec', 'lekarz', 'dietetyk sportowy', 'wydarzenie sportowe', name='user_enum'))


def __init__(self, first_name, last_name, email, birth_date, user_type):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.birth_date = birth_date
    self.user_type = user_type


def __repr__(self):
    return f"({self.id}) {self.first_name} {self.last_name} ({self.email}, {self.birth_date})"
