from pydantic import BaseModel, ConfigDict
from datetime import date


class HabitCreate(BaseModel):
    title: str
    description: str | None = None


class HabitResponse(BaseModel):
    id: int
    title: str
    description: str | None
    user_id: int

    model_config = ConfigDict(from_attributes=True)


class UserResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )


class HabitCompletionCreate (BaseModel):
    habit_id: int
    date:date


   