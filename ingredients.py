from sqlalchemy import Column, String, Integer, Date, ForeignKey
from base import Base


class Ingredients(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True)
    calories = Column(Integer)


def __init__(self, calories):
    self.calories = calories


def __repr__(self):
    return f"({self.id}) {self.calories}"
