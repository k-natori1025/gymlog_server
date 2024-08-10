from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.exercise import ExercisesOrm
from app.schemas.exercise import ExerciseResponse

class ExerciseRepository:
    async def get_exercises_by_muscle_group_id(self, db: Session, muscle_group_id: int) -> List[ExerciseResponse]:
        exercises = db.scalars(select(ExercisesOrm).where(ExercisesOrm.muscle_group_id == muscle_group_id)).all()
        return [ExerciseResponse.from_orm(exercise) for exercise in exercises]
