from datetime import date

from app.models.habit_completion import HabitCompletion
from app.models.habits import Habit

from app.services.streak_service import (
    calculate_current_streak,
    calculate_longest_streak,
)
from app.services.achievement_service import get_achievements
from app.services.calendar_service import get_calendar_data
from app.services.level_service import get_level
from app.services.insights_service import get_insights


def get_habit_dashboard(db, habit_id: int, user_id: int):

    completions = db.query(HabitCompletion).filter(
        HabitCompletion.habit_id == habit_id,
        HabitCompletion.user_id == user_id
    ).all()

    dates = sorted({c.date for c in completions})

    # No completions yet
    if not dates:
     return {
        "habit_id": habit_id,
        "current_streak": 0,
        "longest_streak": 0,
        "success_rate": 0,
        "calendar": {},
        "productivity_score": 0,
        "level": "Beginner",
        "achievements": [],
        "insights": ["Complete your habit today to begin your journey!"]
    }
        

    today = date.today()

    total_days = (today - dates[0]).days + 1
    completed_days = len(dates)

    current_streak = calculate_current_streak(dates)
    longest_streak = calculate_longest_streak(dates)

    calendar = get_calendar_data(db, habit_id, user_id)

    success_rate = round(
        (completed_days / total_days) * 100,
        2
    )

    productivity_score = round(
        (current_streak * 2)
        + (longest_streak * 1.5)
        + (success_rate / 10),
        2
    )
    level = get_level(productivity_score)
    insights = get_insights(
    current_streak,
    longest_streak,
    success_rate
    )
    # Achievement badges    
    achievements = get_achievements(
    current_streak,
    longest_streak,
    success_rate
)

    return {
    "habit_id": habit_id,
    "current_streak": current_streak,
    "longest_streak": longest_streak,
    "success_rate": success_rate,
    "calendar": calendar,
    "productivity_score": productivity_score,
    "level": level,
    "achievements": achievements,
    "insights": insights
}
    


def get_user_dashboard(db, user_id: int):

    habits = db.query(Habit).filter(
        Habit.user_id == user_id
    ).all()

    completions = db.query(HabitCompletion).filter(
        HabitCompletion.user_id == user_id
    ).all()

    completed_today = len([
        c for c in completions
        if c.date == date.today()
    ])

    active_days = len({c.date for c in completions})

    total_habits = len(habits)

    overall_success_rate = (
        round((completed_today / total_habits) * 100, 2)
        if total_habits
        else 0
    )

    best_streak = 0

    for habit in habits:

        habit_dates = sorted({
            c.date
            for c in completions
            if c.habit_id == habit.id
        })

        streak = calculate_longest_streak(habit_dates)

        if streak > best_streak:
            best_streak = streak

    productivity_score = round(
        (overall_success_rate * 0.5)
        + (best_streak * 2)
        + (active_days * 0.5),
        2
    )

    return {
        "total_habits": total_habits,
        "completed_today": completed_today,
        "active_days": active_days,
        "overall_success_rate": overall_success_rate,
        "best_streak": best_streak,
        "productivity_score": productivity_score
    }