from typing import List

from pydantic import BaseModel
from sqlalchemy import Column, String, Integer, Date, ForeignKey, Table
from sqlalchemy.orm import relationship
from entity.meals import Meals
from entity.allergens import Allergens
from entity.base import Base

plans_meals_association = Table(
    'plans_meals', Base.metadata,
    Column('meal_id', Integer, ForeignKey('meals.id')),
    Column('plan_id', Integer, ForeignKey('meal_plans.id'))
)

allergens_plan_association = Table(
    'allergens_plan', Base.metadata,
    Column('allergen_id', Integer, ForeignKey('allergens.id')),
    Column('plan_id', Integer, ForeignKey('meal_plans.id'))
)


class MealPlan(Base):
    __tablename__ = 'meal_plans'

    id = Column(Integer, primary_key=True)
    calories = Column(Integer)
    meals_amount = Column(Integer)
    description = Column(String)
    meals = relationship("Meals", secondary=plans_meals_association)
    allergens = relationship("Allergens", secondary=allergens_plan_association)

    events = relationship('Event', back_populates='meal_plans')


def __init__(self, calories, meals_amount, description):
    self.calories = calories
    self.meals_amount = meals_amount
    self.description = description


def __repr__(self):
    return f"({self.id}) {self.calories} {self.meals_amount} {self.description}"


class MealPlanCreate(BaseModel):
    calories: int
    meals_amount: int
    description: str
    meals: List[int]
    allergens: List[int]
