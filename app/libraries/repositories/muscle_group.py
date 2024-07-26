from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.muscle_group import MuscleGroupOrm
from app.schemas.muscle_group import MuscleGroupResponse

class MuscleGroupRepository:
    async def get_muscle_groups(self, db: Session)->MuscleGroupResponse:
        return db.scalars(select(MuscleGroupOrm)).all()
