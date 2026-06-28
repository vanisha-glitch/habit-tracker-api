from sqlalchemy import Column, Integer, ForeignKey, Date, Boolean
from app.database.base import Base


class HabitCompletion(Base):
    __tablename__ = "habit_completions"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    habit_id = Column(Integer, ForeignKey("habits.id"))

    date = Column(Date)
    completed = Column(Boolean, default=True)