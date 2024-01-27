from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from entity.meals import Meals

router = APIRouter()


@router.get("/meals")
def get_meals(db: Session = Depends(get_db)):
    meals = db.query(Meals).all()
    return meals
