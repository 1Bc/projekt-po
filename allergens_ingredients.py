from sqlalchemy import Column, String, Integer, Date, ForeignKey
from base import Base


class AllergensIngredients(Base):
    __tablename__ = 'allergens_ingredients'

    id = Column(Integer, primary_key=True)
    allergen_id = Column(Integer)
    ingredient_id = Column(Integer)


def __init__(self, allergen_id, ingredient_id):
    self.allergen_id = allergen_id
    self.ingredient_id = ingredient_id


def __repr__(self):
    return f"({self.id}) {self.allergen_id} {self.ingredient_id}"
