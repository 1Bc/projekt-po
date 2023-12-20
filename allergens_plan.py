from sqlalchemy import Column, String, Integer, Date, ForeignKey
from base import Base


class AllergensPlan(Base):
    __tablename__ = 'allergens_plan'

    id = Column(Integer, primary_key=True)
    allergen_id = Column(Integer)
    plan_id = Column(Integer)


def __init__(self, allergen_id, plan_id):
    self.allergen_id = allergen_id
    self.plan_id = plan_id


def __repr__(self):
    return f"({self.id}) {self.allergen_id} {self.plan_id}"
