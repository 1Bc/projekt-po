from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from entity.ingredients import Ingredients, IngredientsCreate

router = APIRouter()


@router.get("/ingredients")
def get_ingredients(db: Session = Depends(get_db)):
    ingredients = db.query(Ingredients).all()
    return ingredients


@router.post("/ingredients")
def add_ingredients(ingredients: List[IngredientsCreate], db: Session = Depends(get_db)):
    new_ingredients = []
    for ingredient in ingredients:
        new_ingredient = Ingredients(**ingredient.dict())
        db.add(new_ingredient)
        new_ingredients.append(new_ingredient)
    db.commit()
    for ingredient in new_ingredients:
        db.refresh(ingredient)
    return new_ingredients
