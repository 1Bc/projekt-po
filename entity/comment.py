from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

from base import Base


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    event_id = Column(Integer)
    description = Column(String)

    events = relationship('Event', back_populates='comment')


def __init__(self, event_id, description):
    self.event_id = event_id
    self.description = description


def __repr__(self):
    return f"({self.id}) {self.event_id} {self.description}"
