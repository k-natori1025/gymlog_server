from pydantic import BaseModel

class ExerciseResponse(BaseModel):
    id: int
    name: str
    muscle_group_id: str

    class Config:
        orm_mode = True
