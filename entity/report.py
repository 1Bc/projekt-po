from pydantic import BaseModel
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from entity.base import Base


class Report(Base):
    __tablename__ = 'reports'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    description = Column(String)
    result = Column(String)

    events = relationship('Event', back_populates='report')

    def __init__(self, first_name, last_name, description, result):
        self.first_name = first_name
        self.last_name = last_name
        self.description = description
        self.result = result

    def __repr__(self):
        return f"({self.id}) {self.first_name} {self.last_name} ({self.description}, {self.result})"


class ReportCreate(BaseModel):
    first_name: str = None
    last_name: str = None
    description: str
    result: str = None
