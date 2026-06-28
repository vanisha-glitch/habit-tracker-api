from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.habits import Habit
from app.models.habit_completion import HabitCompletion

from app.schemas.habits import HabitCreate, HabitCompletionCreate

from app.core.security import get_current_user

from app.services.streak_service import (
    calculate_current_streak,
    calculate_longest_streak
)

from app.services.calendar_service import get_calendar_data
from app.services.dashboard_service import (
    get_habit_dashboard,
    get_user_dashboard
)
from app.services.heatmap_service import get_heatmap

router = APIRouter(prefix="/habits", tags=["Habits"])

@router.post("/")
def create_habit(
    habit: HabitCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    new_habit = Habit(
        title=habit.title,
        description=habit.description,
        user_id=current_user.id
    )

    db.add(new_habit)
    db.commit()
    db.refresh(new_habit)

    return new_habit

@router.get("/")
def get_habits(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return db.query(Habit).filter(
        Habit.user_id == current_user.id
    ).all()

@router.post("/complete")
def complete_habit(
    data: HabitCompletionCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    existing = db.query(HabitCompletion).filter(
        HabitCompletion.habit_id == data.habit_id,
        HabitCompletion.user_id == current_user.id,
        HabitCompletion.date == data.date
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Already completed for this date"
        )

    completion = HabitCompletion(
        habit_id=data.habit_id,
        user_id=current_user.id,
        date=data.date,
        completed=True
    )

    db.add(completion)
    db.commit()
    db.refresh(completion)

    return {"message": "Habit marked as completed"}

@router.get("/dashboard")
def dashboard(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return get_user_dashboard(db, current_user.id)

@router.get("/{habit_id}/streak")
def get_streak(
    habit_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    completions = db.query(HabitCompletion).filter(
        HabitCompletion.habit_id == habit_id,
        HabitCompletion.user_id == current_user.id
    ).all()

    dates = sorted({c.date for c in completions})

    return {
        "habit_id": habit_id,
        "current_streak": calculate_current_streak(dates),
        "longest_streak": calculate_longest_streak(dates)
    }


@router.get("/{habit_id}/calendar")
def habit_calendar(
    habit_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return get_calendar_data(db, habit_id, current_user.id)

@router.get("/{habit_id}/dashboard")
def habit_dashboard(
    habit_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return get_habit_dashboard(db, habit_id, current_user.id)

@router.get("/{habit_id}/heatmap")
def habit_heatmap(
    habit_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return {
        "habit_id": habit_id,
        "heatmap": get_heatmap(db, habit_id, current_user.id)
    }