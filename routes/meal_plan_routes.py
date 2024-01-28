from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select, insert
from database import get_db
from entity.meal_plan import plans_meals_association, MealPlan, MealPlanCreate, PlanMealCreate

router = APIRouter()


def row2dict(row):
    return {"meal_id": row.meal_id, "plan_id": row.plan_id}


@router.get("/plans_meals")
def get_plans_meals(db: Session = Depends(get_db)):
    stmt = select(*plans_meals_association.c)
    result = db.execute(stmt).fetchall()
    return [row2dict(row) for row in result]


@router.post("/plans_meals")
def create_plan_meal(plan_meal: PlanMealCreate, db: Session = Depends(get_db)):
    stmt = insert(plans_meals_association).values(meal_id=plan_meal.meal_id, plan_id=plan_meal.plan_id)
    db.execute(stmt)
    db.commit()
    return {"meal_id": plan_meal.meal_id, "plan_id": plan_meal.plan_id}
