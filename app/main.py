from fastapi import FastAPI
from app.routers.users import router as users_router
from app.routers.habits import router as habits_router   # NEW

app = FastAPI()

app.include_router(users_router)
app.include_router(habits_router)   # NEW


@app.get("/")
def root():
    return {"message": "Habit Tracker API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000)

