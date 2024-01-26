from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from entity.event import Event, EventCreate
from datetime import datetime

router = APIRouter()


@router.get("/events")
def get_events(db: Session = Depends(get_db)):
    events = db.query(Event).all()
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
