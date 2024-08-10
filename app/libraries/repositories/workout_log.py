from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.workout_log import WorkOutLogOrm
from app.schemas.workout_log import WorkoutLogRequest

class WorkoutLogRepository:
    async def create_workout_log(self, db: Session, body: WorkoutLogRequest, user_id: int):
        try:
            workout_log = WorkOutLogOrm(
                exercise_id=body.exercise_id,
                muscle_group_id=body.muscle_group_id,
                user_id=user_id,
                weight=body.weight, 
                reps=body.reps,
                sets=body.sets,
            )
            db.add(workout_log) 
            db.commit()
            db.refresh(workout_log)
            return workout_log
        except Exception as e:
            print(f"Error creating workout log: {e}")
            raise e
