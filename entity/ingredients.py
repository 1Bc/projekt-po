from sqlalchemy import Column, String, Integer, Date, ForeignKey
from entity.base import Base
from pydantic import BaseModel


class Ingredients(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    calories = Column(Integer)

    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def __repr__(self):
        return f"({self.id}) {self.name} {self.calories}"


class IngredientsCreate(BaseModel):
    name: str
    calories: int
