from sqlalchemy import Column, String, Integer, Date, ForeignKey
from base import Base


class Allergens(Base):
    __tablename__ = 'allergens'

    id = Column(Integer, primary_key=True)
    name = Column(String)


def __init__(self, name):
    self.name = name


def __repr__(self):
    return f"({self.id}) {self.name}"
