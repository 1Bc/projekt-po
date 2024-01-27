from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from entity.allergens import Allergens
from entity.meal_plan import MealPlan, MealPlanCreate
from entity.meals import Meals

router = APIRouter()



