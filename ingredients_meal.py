from sqlalchemy import Column, String, Integer, Date, ForeignKey
from base import Base


class IngredientsMeal(Base):
    __tablename__ = 'ingredients_meal'

    id = Column(Integer, primary_key=True)
    meal_id = Column(Integer)
    ingredient_id = Column(Integer)


def __init__(self, meal_id, ingredient_id):
    self.meal_id = meal_id
    self.ingredient_id = ingredient_id


def __repr__(self):
    return f"({self.id}) {self.meal_id} {self.ingredient_id}"
