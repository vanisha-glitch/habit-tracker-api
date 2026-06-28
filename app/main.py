from fastapi import FastAPI

from app.database.base import Base
from app.database.database import engine

from app.routers.users import router as users_router
from app.routers.habits import router as habits_router   # NEW

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users_router)
app.include_router(habits_router)   # NEW


@app.get("/")
def root():
    return {"message": "Habit Tracker API is running"}

