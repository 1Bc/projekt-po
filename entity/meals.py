from typing import List

from pydantic import BaseModel
from sqlalchemy import Column, String, Integer, Date, ForeignKey, Table
from sqlalchemy.orm import relationship
from entity.ingredients import Ingredients, IngredientsCreate
from entity.base import Base

meals_ingredients_association = Table(
    'meals_ingredients', Base.metadata,
    Column('meal_id', Integer, ForeignKey('meals.id')),
    Column('ingredient_id', Integer, ForeignKey('ingredients.id'))
)


class Meals(Base):
    __tablename__ = 'meals'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    calories = Column(Integer)
    ingredients = relationship("Ingredients", secondary=meals_ingredients_association)

    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def __repr__(self):
        return f"({self.id}) Name: {self.name} Calories: {self.calories}"


class MealsCreate(BaseModel):
    name: str
    calories: int
    ingredients: List[IngredientsCreate]


class MealsResponse(BaseModel):
    id: int
    name: str
    calories: int
    ingredients: List[IngredientsCreate]
