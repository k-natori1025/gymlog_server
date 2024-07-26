from pydantic import BaseModel
from typing import List, Union

class AICoachRequest(BaseModel):
    gender: str
    age: int
    training_location: str
    goal: str
    training_days_per_week: int
    exercise_variety: int
    muscle_groups: Union[List[str], str]


class AICoachResponse(BaseModel):
    ai_response: str
