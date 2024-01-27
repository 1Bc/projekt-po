from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func, cast, Date
from database import get_db
from entity.event import Event, EventCreate
from datetime import datetime

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

    # Add the event to the database
    db.add(event)
    db.commit()
    db.refresh(event)

    return event
