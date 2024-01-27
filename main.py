from fastapi import FastAPI, Depends
from database import get_db
from routes.event_routes import router as event_router
from routes.ingredients_routes import router as ingredients_router
from routes.meals_routes import router as meals_router

db = Depends(get_db)

app = FastAPI()

app.include_router(event_router)
app.include_router(ingredients_router)
app.include_router(meals_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
