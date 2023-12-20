from sqlalchemy import Column, String, Integer, Date, ForeignKey
from base import Base


class MealPlan(Base):
    __tablename__ = 'meal_plans'

    id = Column(Integer, primary_key=True)
    calories = Column(Integer)
    meals_amount = Column(Integer)
    description = Column(String)


def __init__(self, calories, meals_amount, description):
    self.calories = calories
    self.meals_amount = meals_amount
    self.description = description


def __repr__(self):
    return f"({self.id}) {self.calories} {self.meals_amount} {self.description}"
