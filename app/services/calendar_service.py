from datetime import date, timedelta
from app.models.habit_completion import HabitCompletion

def get_calendar_data(db, habit_id: int, user_id: int):

    completions = db.query(HabitCompletion).filter(
        HabitCompletion.habit_id == habit_id,
        HabitCompletion.user_id == user_id
    ).all()

    completed_dates = {c.date for c in completions}

    if not completed_dates:
        return {}

    start_date = min(completed_dates)
    end_date = date.today()

    calendar = {}

    current = start_date
    while current <= end_date:
        calendar[str(current)] = current in completed_dates
        current += timedelta(days=1)

    return calendar