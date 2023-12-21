from sqlalchemy import Column, String, Integer, Date, ForeignKey, Table
from sqlalchemy.orm import relationship

from base import Base

meals_ingredients_association = Table(
    'meals_ingredients', Base.metadata,
    Column('meal_id', Integer, ForeignKey('meals.id')),
    Column('ingredient_id', Integer, ForeignKey('ingredients.id'))
)


class Meals(Base):
    __tablename__ = 'meals'

    id = Column(Integer, primary_key=True)
    calories = Column(Integer)
    meals_ingredients_association = relationship("Ingredients", secondary=meals_ingredients_association)


def __init__(self, calories):
    self.calories = calories


def __repr__(self):
    return f"({self.id}) {self.calories}"
