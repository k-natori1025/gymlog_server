from fastapi import APIRouter, Depends, HTTPException, Response, Request
from sqlalchemy.orm import Session

from app.schemas.workout_log import WorkloutLogRequest
from app.libraries.repositories.muscle_group import MuscleGroupRepository
from app.settings.database import get_db

router = APIRouter()

@router.get("/muscle_groups", tags=["muscle_group"], summary="部位の全件取得")
async def get_muscle_groups(
    db: Session = Depends(get_db),
    muscle_group_repo: MuscleGroupRepository = Depends()
):
    try:
        response = await muscle_group_repo.get_muscle_groups(db)
        return response
    except HTTPException as e:
        print(f"HTTPエラー: {e.detail}")
        raise HTTPException(status_code=e.status_code, detail=e.detail)
