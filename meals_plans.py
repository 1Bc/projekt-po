from sqlalchemy import Column, String, Integer, Date, ForeignKey
from base import Base


class MealsPlans(Base):
    __tablename__ = 'meals_plans'

    id = Column(Integer, primary_key=True)
    meal_id = Column(Integer)
    plan_id = Column(Integer)


def __init__(self, meal_id, plan_id):
    self.meal_id = meal_id
    self.plan_id = plan_id


def __repr__(self):
    return f"({self.id}) {self.meal_id} {self.plan_id}"
