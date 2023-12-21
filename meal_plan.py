from sqlalchemy import Column, String, Integer, Date, ForeignKey, Table
from sqlalchemy.orm import relationship

from base import Base

meals_plans_association = Table(
    'meals_plans', Base.metadata,
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
    meals = relationship("Meal", secondary=meals_plans_association)
    allergens = relationship("Allergens", secondary=allergens_plan_association)


def __init__(self, calories, meals_amount, description):
    self.calories = calories
    self.meals_amount = meals_amount
    self.description = description


def __repr__(self):
    return f"({self.id}) {self.calories} {self.meals_amount} {self.description}"
