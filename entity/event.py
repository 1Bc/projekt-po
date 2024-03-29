from sqlalchemy import Column, String, Integer, Date, ForeignKey, Enum as SqlEnum
from sqlalchemy.orm import relationship
from entity.report import Report
from entity.comment import Comment
from entity.meal_plan import MealPlan
from entity.base import Base
from pydantic import BaseModel
from datetime import datetime


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    start_time = Column(Date)
    end_time = Column(Date)
    place = Column(String)
    color = Column(SqlEnum('red', 'green', 'blue', name='color_enum'))
    minutes_before_event = Column(Integer)
    attendee_id = Column(Integer)
    creator_id = Column(Integer)
    event_type = Column(SqlEnum('trening', 'spotkanie', 'wizyta lekarska', 'wydarzenie sportowe', name='type_enum'))
    report_id = Column(Integer, ForeignKey('reports.id'))
    comment_id = Column(Integer, ForeignKey('comments.id'))
    meals_plan_id = Column(Integer, ForeignKey('meal_plans.id'))

    report = relationship('Report', back_populates='events')
    comment = relationship('Comment', back_populates='events')
    meal_plans = relationship('MealPlan', back_populates='events')


def __init__(self, start_time, end_time, place, color, minutes_before, attendee_id, creator_id, event_type):
    self.start_time = start_time
    self.end_time = end_time
    self.place = place
    self.color = color
    self.minutes_before = minutes_before
    self.attendee_id = attendee_id
    self.creator_id = creator_id
    self.event_type = event_type


def __repr__(self):
    return f"({self.id}) {self.start_time} {self.end_time} ({self.place}, {self.color}, {self.minutes_before}, {self.attendee_id}, {self.creator_id}, {self.event_type})"


class EventCreate(BaseModel):
    start_time: datetime
    end_time: datetime
    place: str
    color: str
    minutes_before_event: int
    attendee_id: int
    creator_id: int
    event_type: str
    report_id: int = None
    comment_id: int = None
    meals_plan_id: int = None
