from sqlalchemy import Column, String, Integer, Date, ForeignKey, Table
from sqlalchemy.orm import relationship

from base import Base

allergens_ingredients_association = Table(
    'allergens_ingredients', Base.metadata,
    Column('allergen_id', Integer, ForeignKey('allergens.id')),
    Column('ingredient_id', Integer, ForeignKey('ingredients.id'))
)


class Allergens(Base):
    __tablename__ = 'allergens'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    allergens_ingredients_association = relationship("Ingredients", secondary=allergens_ingredients_association)


def __init__(self, name):
    self.name = name


def __repr__(self):
    return f"({self.id}) {self.name}"
