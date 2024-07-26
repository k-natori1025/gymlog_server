from pydantic import BaseModel
from typing import List, Union

class WorkloutLogRequest(BaseModel):
    exercise_id: int
    muscle_group_id: int
    user_id: int
    weight: int
    reps: int
    sets: int

class AICoachResponse(BaseModel):
    ai_response: str
