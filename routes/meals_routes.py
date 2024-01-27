from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from entity.ingredients import Ingredients, IngredientsCreate
from entity.meals import Meals, MealsCreate, MealsResponse

router = APIRouter()


@router.get("/meals")
def get_meals(db: Session = Depends(get_db)):
    meals = db.query(Meals).all()
    return meals


@router.post("/meals", response_model=MealsResponse)
def create_meal(meal: MealsCreate, db: Session = Depends(get_db)):
    # Create a new meal instance
    db_meal = Meals(name=meal.name, calories=meal.calories)

    for ingredient_data in meal.ingredients:
        ingredient = Ingredients(**ingredient_data.dict())
        db_meal.ingredients.append(ingredient)

    db.add(db_meal)
    db.commit()
    db.refresh(db_meal)

    response_data = MealsResponse(
        id=db_meal.id,
        name=db_meal.name,
        calories=db_meal.calories,
        ingredients=[IngredientsCreate(name=ingredient.name, calories=ingredient.calories) for ingredient in
                     db_meal.ingredients]
    )

    return response_data
