from sqlalchemy import Column, String, Integer, Date
from base import Base


class Report(Base):
    __tablename__ = 'reports'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    description = Column(String)
    result = Column(String)


def __init__(self, first_name, last_name, description, result):
    self.first_name = first_name
    self.last_name = last_name
    self.description = description
    self.result = result


def __repr__(self):
    return f"({self.id}) {self.first_name} {self.last_name} ({self.description}, {self.result})"
