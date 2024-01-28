from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func, cast, Date
from database import get_db
from entity.event import Event, EventCreate
from gcsa.event import Event as GCEvent
from datetime import datetime
from google_calendar import calendar

router = APIRouter()


@router.get("/events")
def get_events(db: Session = Depends(get_db)):
    events = db.query(Event).all()
    return events


@router.get("/events/{start_time}")
def get_events_by_start_time(start_time: datetime, db: Session = Depends(get_db)):
    # Use the cast function to cast the database start_time to a date
    events = db.query(Event).filter(cast(Event.start_time, Date) == func.date(start_time)).all()
    return events


@router.post("/event")
def add_event(event_data: EventCreate, db: Session = Depends(get_db)):
    event_data.start_time = datetime.fromisoformat(str(event_data.start_time))
    event_data.end_time = datetime.fromisoformat(str(event_data.end_time))
    event = Event(**event_data.dict())

    gc_event = GCEvent(
        event_data.event_type,
        start=datetime.strptime(str(event_data.start_time), '%Y-%m-%d %H:%M:%S'),
        end=datetime.strptime(str(event_data.end_time), '%Y-%m-%d %H:%M:%S'),
        location=event_data.place,
        minutes_before_popup_reminder=event_data.minutes_before_event
    )
    calendar.add_event(gc_event)

    # Add the event to the database
    db.add(event)
    db.commit()
    db.refresh(event)

    return event
