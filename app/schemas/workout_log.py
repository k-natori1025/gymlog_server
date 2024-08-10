from pydantic import BaseModel
from typing import List, Union

class WorkoutLogRequest(BaseModel):
    exercise_id: int
    muscle_group_id: int
    weight: int
    reps: int
    sets: int

class WorkoutLogResponse(WorkoutLogRequest):
    id: int

    class Config:
        or_mode = True
